# -*- coding: utf-8 -*-
"""utils."""
import re
from typing import Union, Any, Sequence

import numpy as np
from loguru import logger
from agentscope.agents import AgentBase
from agentscope.message import Msg


def check_winning(mission_record: list, host: str, assassin_mission: bool,Prompts) -> bool:
    """check which group wins"""
    proceed_count = sum(1 for result in mission_record if result == "proceed")
    fail_count = sum(1 for result in mission_record if result == "sabotage")
    if fail_count >= 3 and assassin_mission==False:
        msg = Msg(host, Prompts.to_all_wolf_win, role="assistant")
        logger.chat(msg)
        return True
    elif proceed_count >= 3 and assassin_mission==False:
        msg = Msg(host, Prompts.to_all_village_win, role="assistant")
        logger.chat(msg)
        return True
    elif assassin_mission==True:
        msg = Msg(host, Prompts.to_all_wolf_win, role="assistant")
        logger.chat(msg)
        return True
    return False


def update_alive_players(
    survivors: Sequence[AgentBase],
    wolves: Sequence[AgentBase],
    dead_names: Union[str, list[str]],
) -> tuple[list, list]:
    """update the list of alive agents"""
    if not isinstance(dead_names, list):
        dead_names = [dead_names]
    return [_ for _ in survivors if _.name not in dead_names], [
        _ for _ in wolves if _.name not in dead_names
    ]


def majority_vote(votes: list) -> Any:
    """majority_vote function"""
    votes_valid = [item for item in votes if item != "Abstain"]
    # Count the votes excluding abstentions.
    unit, counts = np.unique(votes_valid, return_counts=True)
    return unit[np.argmax(counts)]


def extract_name_and_id(name: str) -> tuple[str, int]:
    """extract player name and id from a string"""
    try:
        name = re.search(r"\b[Pp]layer\d+\b", name).group(0)
        idx = int(re.search(r"[Pp]layer(\d+)", name).group(1)) - 1
    except AttributeError:
        # In case Player remains silent or speaks to abstain.
        logger.warning(f"vote: invalid name {name}, set to Abstain")
        name = "Abstain"
        idx = -1
    return name, idx

def extract_name_and_id_list(name: str) -> list[tuple[str, int]]:
    """extract player name and id from a string as a list"""
    try:
        name_list = []
        names = re.findall(r"\b[Pp]layer\d+\b", name)
        for _ in names:
            name1 = re.search(r"\b[Pp]layer\d+\b", _).group(0)
            idx = int(re.search(r"[Pp]layer(\d+)", _).group(1)) - 1
            name_list.append((name1, idx))
    except AttributeError:
        # In case Player remains silent or speaks to abstain.
        #logger.warning(f"vote: invalid name {name}, set to Abstain")
        name = "Abstain"
        idx = -1
    return name_list


def n2s(agents: Sequence[Union[AgentBase, str]]) -> str:
    """combine agent names into a string, and use "and" to connect the last
    two names."""

    def _get_name(agent_: Union[AgentBase, str]) -> str:
        return agent_.name if isinstance(agent_, AgentBase) else agent_

    if len(agents) == 1:
        return _get_name(agents[0])

    return (
        ", ".join([_get_name(_) for _ in agents[:-1]])
        + " and "
        + _get_name(agents[-1])
    )


def set_parsers(
    agents: Union[AgentBase, list[AgentBase]],
    parser_name: str,
) -> None:
    """Add parser to agents"""
    if not isinstance(agents, list):
        agents = [agents]
    for agent in agents:
        agent.set_parser(parser_name)
