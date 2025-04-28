# -*- coding: utf-8 -*-
"""A werewolf game implemented by agentscope."""
# 切换到游戏目录
import os
from functools import partial
file_path = os.getcwd()
os.chdir(file_path)

from prompt_cn import Prompts
from avalon_units import (
    check_winning,
    n2s,
    majority_vote,
    set_parsers,
)
from agentscope.message import Msg
from agentscope.msghub import msghub
from agentscope.pipelines import sequential_pipeline
from collections import Counter
import agentscope
import random
import re
from typing import Sequence, Union
import agentscope
from agentscope.agents import AgentBase,DictDialogAgent

def n2s_dist(agents: Sequence[Union[AgentBase, str]]) -> str:
    """combine agent names into a string, and use "and" to connect the last
    two names."""

    def _get_name(agent_: Union[AgentBase, str]) -> str:
        try:
            return agent_.name
        except:
            return agent_

    if len(agents) == 1:
        return _get_name(agents[0])

    return (
        ", ".join([_get_name(_) for _ in agents[:-1]])
        + " and "
        + _get_name(agents[-1])
    )

# pylint: disable=too-many-statements
def main() -> None:
    """werewolf game"""
    # default settings
    HostMsg = partial(Msg, name="Moderator", role="assistant", echo=True)
    MAX_GAME_ROUND = 10
    # read model and agent configs, and initialize agents automatically

    players = agentscope.init(
        model_configs="./configs/model_configs_lcoal.json",
        agent_configs="./configs/agent_configs_cn_modify.json",
        project="Avalon",
    )
    # initialize roles
    name_role_dict = {agent.name: agent.sys_prompt['role'] for agent in players}
    role_agent_dict = {agent.sys_prompt['role']: agent for agent in players}
   
    # initialize players
    morgana,assassin,villager,villager2,percival,merlin = role_agent_dict['morgana'],role_agent_dict['assassin'],role_agent_dict['villager1'],role_agent_dict['villager2'],role_agent_dict['percival'],role_agent_dict['merlin']
    survivors = [morgana,assassin,villager,villager2,percival,merlin]
    random.shuffle(survivors)
    wolves = [morgana, assassin]
    leaders = [morgana, merlin]
    villagers = [villager,villager2]
    crews_each_round = [2,3,4,3,4]
    
    # welcome message
    hint = HostMsg(content=Prompts.to_all_welcome.format(n2s(survivors)))
    with msghub(survivors) as hub:
        hub.broadcast(hint)

    # start the game
    it_captain = iter(survivors*5)
    survivors_name_dict = {agent.name: agent for agent in survivors}
    mission_record = []

    # merlin
    def ask_merlin():
        hint = HostMsg(
            content=Prompts.to_merlin.format(merlin.name, n2s(wolves)),
        )
        set_parsers(merlin, Prompts.merilin_parser)
        merlin(hint)
        merlin.observe(hint)
    ask_merlin()

    # Let wolves know their teammates
    hint = HostMsg(content=Prompts.to_wolves.format(n2s(wolves)))
    with msghub(wolves, announcement=hint) as hub:
        set_parsers(wolves, Prompts.wolves_discuss_parser)
        x = sequential_pipeline(wolves)

    # percival
    hint = HostMsg(content=Prompts.to_percival.format(percival.name, n2s(leaders)))
    set_parsers(percival, Prompts.percival_parser)
    x = percival(hint)
    captain = next(it_captain)
    round = 0
    vote_fail = 0

    # villagers
    hint = HostMsg(content=Prompts.to_villagers.format(n2s(villagers)))
    set_parsers(villagers, Prompts.villagers_parser)
    for _ in villagers:
        _(hint)

    for _ in range(0, MAX_GAME_ROUND + 1):
        # Captain phase: Captain selects crew members for the mission
        number_of_crews = crews_each_round[round]
        with msghub(survivors) as hub:
            hint = HostMsg(content=Prompts.to_captain.format(captain.name, number_of_crews, n2s(survivors)))
            set_parsers(captain, Prompts.to_captain_parser)
            captain_choice = captain(hint)
            crews_by_captain = n2s(captain_choice.metadata)
        hints = [
            HostMsg(content=Prompts.to_all_vote_crewlist.format(crews_by_captain)),
        ]
        with msghub(survivors, announcement=hints) as hub:
             # discuss
            set_parsers(survivors, Prompts.survivors_discuss_parser)
            survivors_after_captain = survivors[survivors.index(captain)+1:] + survivors[:survivors.index(captain)+1]
            x = sequential_pipeline(survivors_after_captain)

        # vote
        set_parsers(survivors, Prompts.survivors_vote_crewlist_parser)
        hint = HostMsg(content=Prompts.to_all_vote.format(n2s(survivors)))
        votes = [
            _(hint).metadata['agree'] for _ in survivors
        ]
        votes = [str(vote).lower() for vote in votes]
        agree_count = votes.count('true')
        false_count = votes.count('false')
        vote_res = majority_vote(votes)
        votes_res_str = f'agree:{agree_count},false:{false_count}'

        #平票则流局
        if agree_count == false_count:
            vote_res = 'false'

        with msghub(survivors, announcement=hints) as hub:
            if vote_fail >=3:
                round += 1
                captain = next(it_captain)
                mission_result = 'sabotage'
                result = HostMsg(content=Prompts.to_all_res_false_3.format(votes_res_str,vote_fail))
                hub.broadcast(result)
                mission_record.append(mission_result)
                vote_fail = 0
                continue
            # broadcast the result to all players
            if vote_res == "false":
                vote_fail+=1
                captain = next(it_captain)
                result = HostMsg(content=Prompts.to_all_res_false.format(votes_res_str,captain.name))
                hub.broadcast(result)
                continue
            else:
                vote_fail = 0
                round += 1
                result = HostMsg(content=Prompts.to_all_res_true.format(votes_res_str,crews_by_captain))
                hub.broadcast(result)

        crews_names  = captain_choice.metadata
        crews = [survivors_name_dict[name] for name in crews_names]

        # vote the mission
        set_parsers(crews, Prompts.crews_vote_parser)
        hint = HostMsg(content=Prompts.to_crews_vote)

        votes = []
        for _ in crews:
            if _ in [morgana,assassin]:
                set_parsers(crews, Prompts.wolves_vote_parser)
                x = _(hint)
                votes.append(x.content)
            else:
                set_parsers(crews, Prompts.crews_vote_parser)
                x = _(hint)
                votes.append(x.content)

        votes = [str(vote).lower() for vote in votes]
        agree_count = votes.count('proceed')
        false_count = votes.count('sabotage')
        votes_res_str = f'proceed:{agree_count},sabotage:{false_count}'

        # record the result
        mission_result = "sabotage" if 'sabotage' in votes else "proceed"
        mission_record.append(mission_result)

        #early assassin
        if mission_result =='proceed':
            set_parsers(wolves, Prompts.wolves_early_assassin_parser)
            with msghub(wolves) as hub:
                hint = HostMsg(content=Prompts.to_wolves_early_assassin)
                votes = [str(_(hint).content).lower() for _ in wolves]
                if not 'false' in votes:
                    set_parsers(wolves, Prompts.wolves_discuss_assassin_parser)
                    x = sequential_pipeline(wolves)
                    #Assassin
                    hint = HostMsg(content=Prompts.to_assassin.format(assassin.name, n2s(survivors)))
                    set_parsers(assassin, Prompts.assassin_parser)
                    x = assassin(hint)
                    assassin_choice = x.content
                    assassin_mission_res = name_role_dict[assassin_choice].lower()=='merlin'
                    check_winning(mission_record = mission_record, host = "Moderator", assassin_mission = assassin_mission_res,Prompts=Prompts)
                    break
        
        # check if the game is close to end
        mission_record_count = Counter(mission_record).most_common(1)[0][1]
        if mission_record_count>=3:
            break
        
        # next round, change captain
        captain = next(it_captain)
        # broadcast the result to all players
        content = Prompts.to_all_mission_res.format(votes_res_str,mission_result,captain.name)
        hints = [HostMsg(content=content)]
        with msghub(survivors, announcement=hints) as hub:
            hub.broadcast(HostMsg(content=Prompts.to_all_continue.format(','.join(mission_record))))


    proceed_count = sum(1 for result in mission_record if result == "proceed")
    if proceed_count>=3:
        set_parsers(wolves, Prompts.wolves_discuss_assassin_parser)
        x = sequential_pipeline(wolves)
        #Assassin
        hint = HostMsg(content=Prompts.to_assassin.format(assassin.name, n2s(survivors)))
        set_parsers(assassin, Prompts.assassin_parser)
        x = assassin(hint)
        assassin_choice = x.content
        assassin_mission_res = name_role_dict[assassin_choice].lower()=='merlin'
        check_winning(mission_record = mission_record, host = "Moderator", assassin_mission = assassin_mission_res,Prompts=Prompts)
    else:
        check_winning(mission_record, "Moderator", False,Prompts=Prompts)
            


if __name__ == "__main__":
    main()