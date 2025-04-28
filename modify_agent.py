# 这里可以自定义agent的角色，玩法，以及性格

import json
import os

#英文版规则和角色说明
# Role_hint_morgana = "You're Morgana in this game. Morgana's goal is to confuse the Percival by pretending to be Merlin. She must use deception to mislead others, while working with the wolves to sabotage missions. Morgana should avoid being exposed as a member of the evil side and protect her true identity."
# Role_hint_assassin = "You're Assassin in this game. The Assassin's goal is to secretly identify Merlin and, at the end of the game, eliminate him. While working with the evil side to sabotage missions, the Assassin must remain discreet and avoid being suspected of being evil."
# Role_hint_merlin = "You're Merlin in this game. Merlin's goal is to help the good side complete missions as much as possible, while leading the group and preventing the wolves from identifying him."
# Role_hint_percival = "You're Percival. Percival's goal is to identify who Merlin and Morgana are as accurately as possible, and while leading the villagers to complete missions, he must also protect Merlin. Usually, Percival will reveal his identity to lead the good side to victory"
# Role_hint_villager = "You're a villager. The villagers' goal is to help the good side complete missions and identify Merlin and Percival."
#"PLAYER ROLES: In the Avalon game, players are divided into two sides: the good side includes Merlin, Percival, and villagers, while the evil side (wolves) includes Morgana and the Assassin. \nwolves: They do not know who Merlin is, but know the identities of their teammates. \nVillagers: The good players who must work together to identify the evil players and complete missions.\nMorgana: A member of the wolves who pretends to be merlin, confusing the good players into thinking she’s Merlin.\nAssassin: A member of the wolves with the power to assassinate Merlin at the end of the game. If the assassin kills Merlin, the wolves wins.\nMerlin:  Merlin knows the identity of the wolves but must keep this information secret to avoid being assassinated at the end of the game.\n Percival: Knows who Merlin and Morgana are, but doesn’t know which is which.",
#"GAME RULE: The game consists of 3 phases: Day Phase (Captain Election), Mission Phases and Assassination Phase. These phases repeat for a total of 5 rounds, with the crew size for each round being 2, 3, 4, 3, and 4, respectively. The game ends if the evil side successfully sabotages 3 missions or successfully kills Merlin at the end of the game. The good side wins if they successfully complete 3 missions. 1. Day Phase (Captain Election): During the day phase, the Captain (the mission leader) will first propose a crew list for the next mission, and all surviving players will vote. This vote occurs after the Captain proposes the crew list and before the next mission. The Captain role rotates, and if the Captain's proposal is approved by the majority vote, the players on the crew list can join the next mission. Otherwise, if the Captain's proposed team is not approved by the majority vote, the current round is considered a failed vote, and the Captain role will pass to the next player. As Captain, you should use your influence to either ensure the mission succeeds (if you are on the good side) or sabotage it (if you are the wolves).",
#"Mission Phase:Until a Captain's crew list receives majority approval, a team will be selected based on the final crew list to go on the mission. Members of the team can choose whether to proceed or sabotage the mission. The mission is only considered successful if all votes are for proceed; if there is even one vote for sabotage, the mission fails. If the wolves sabotages enough missions, they win. Players can only participate in a mission if they are selected for the mission team, and they may sabotage it if they are the wolves. 3. Assassination Phase: At the end of the game, the assassin can choose to assassinate merlin. If the assassin successfully kills merlin, the evil side wins. VICTORY CONDITION: wolves (morgana, assassin): Wins if they successfully sabotage 3 missions or assassinate merlin at the end of the game. Good Side: wins if they successfully complete 3 missions. This is a conversational game. You should respond only based on the conversation history and your strategy.",
                
           
## 中文版
def get_basic_info(player_name,player_name_list,language='en'):
    if language == 'en':
        return f"Act as a player in a avalon game. You are {player_name} and there are totally 6 players, named {','.join(player_name_list)}.\n",
    elif language == 'cn':
        return f"作为阿瓦隆游戏中的一名玩家。你是{player_name}，游戏中总共有6名玩家，分别是{','.join(player_name_list)}。\n",

Role_hint_morgana_cn = "你在游戏中是莫甘娜。莫甘娜的目标是通过假装自己是梅林来迷惑派西维尔。她必须使用欺骗来误导其他人，同时与坏人合作破坏任务。莫甘娜应该避免暴露自己是邪恶方的身份并保护自己的真实身份。"
Role_hint_assassin_cn  = "你在游戏中是刺客。刺客的目标是秘密识别梅林，并在游戏结束时将其消灭。在与邪恶方合作破坏任务的同时，刺客必须保持谨慎，避免被怀疑是邪恶方（坏人）。你可以选择假装自己是派西维尔并告诉大家来增加信任。"
Role_hint_merlin_cn = "你在游戏中是梅林。梅林的目标是尽可能帮助好人方完成任务，同时领导团队并防止坏人识别出他。你可以选择假装自己是派西维尔并告诉大家来混淆坏人。"
Role_hint_percival_cn = "你在游戏中是派西维尔。派西维尔的目标是尽可能准确地识别出谁是梅林和莫甘娜，在带领村民完成任务的同时，还必须保护梅林。通常，派西维尔会在第一轮发言中主动表明自己的身份来带领好人方获胜，且需要尽可能保证自己每轮都执行任务。注意：如果你直接公布了梅林和莫甘娜的信息那么好人阵营极有可能失败"
Role_hint_villager_cn = "你是一名村民。村民的目标是帮助好人方完成任务并识别梅林和真正的派西维尔,同时你也可以假扮派西维尔来误导坏人。"

PLAYER_ROLES = "在阿瓦隆游戏中，玩家分为两派：好人阵营包括梅林、派西维尔和村民，而邪恶阵营（坏人）包括莫甘娜和刺客。\n坏人：他们不知道梅林是谁，但知道队友的身份，他们的目的是隐藏自己的身份尽量多地破坏任务或找出梅林后进行暗杀。\n村民：必须合作识别邪恶玩家并完成任务的好人。\n莫甘娜：坏人阵营的成员，假装自己是梅林，迷惑好人以为她是梅林。\n刺客：坏人阵营的成员，在游戏结束时有能力刺杀梅林。如果刺客成功杀死梅林，坏人获胜。\n梅林：知道坏人的身份，但必须保守这个秘密以避免在游戏结束时被刺杀。\n派西维尔：知道谁是梅林和莫甘娜，但不知道谁是谁。注意：通常派西维尔会在第一轮发言中主动表明自己的身份来带领好人方获胜，表明自己的身份不代表你需要公布梅林和莫甘娜具体是谁，如果你公布了梅林的信息那么好人阵营极有可能失败"
GAME_RULE = "游戏包含3个阶段：白天阶段（队长选举）、任务阶段和刺杀阶段。这些阶段重复进行共5轮，每轮的队伍人数不同。如果邪恶方成功破坏3次任务或在游戏结束时成功杀死梅林，游戏结束。如果好人方成功完成3次任务则获胜。1. 白天阶段（队长选举）：在白天阶段，队长（任务领导者）首先会提议下一个任务的队员名单，所有存活的玩家都要投票。这个投票发生在队长提出队伍名单之后，下一个任务之前。队长角色轮流担任，如果队长的提议获得多数票通过，队伍名单上的玩家可以参加下一个任务。否则，如果队长提议的队伍没有获得多数票通过，当前轮次视为投票失败，队长角色将传递给下一个玩家。作为队长，你应该运用你的影响力来确保任务成功（如果你是好人）或破坏任务（如果你是坏人）。同时派西维尔需要尽早向大家公布自己的身份带领好人胜利，而坏人之一则需要尽量伪装成派西维尔来误导大家。"
Mission_Phase = "直到队长的队伍名单获得多数通过，最终的队伍名单上的队员将去执行任务。队伍成员可以选择执行或破坏任务。只有当所有投票都是执行时，任务才算成功；如果有一票破坏，任务就失败。如果坏人成功破坏足够多的任务，他们就赢了。玩家只有被选入任务队伍才能参与任务，如果是坏人则可以选择破坏任务。3. 刺杀阶段：在游戏结束时，刺客可以选择刺杀梅林。如果刺客成功杀死梅林，邪恶方获胜。胜利条件：坏人（莫甘娜、刺客）：成功破坏3次任务或在游戏结束时刺杀梅林获胜。好人方：成功完成3次任务获胜。这是一个对话游戏。你应该只根据对话历史和你的策略来回应。"
    
def modify_agent_config_cn(name: str,
                           name_list: list,
                           role: str,
                           role_hint: str,
                           player_roles: str,
                           game_rule: str,
                           mission_phase: str,
                           language: str = 'en',
                           **kwargs) -> dict:
    """Modify agent configuration for Chinese version.
    
    Args:
        name: Agent name
        name_list: List of all player names
        role: Agent role
        role_hint: Role hint text
        player_roles: Player roles description
        game_rule: Game rules text
        mission_phase: Mission phase description
        language: Language setting, default 'en'
        **kwargs: Additional keyword arguments
        
    Returns:
        dict: Agent configuration dictionary
    """
    agent_dict = {
        'name': name,
        'role': role,
        "basic_info": get_basic_info(name, name_list, language=language),
        "PLAYER_ROLES": player_roles,
        "GAME_RULE": game_rule,
        "Mission_Phase": mission_phase,
        "role_hint": role_hint
    }
    for key, value in kwargs.items():

        agent_dict[key] = value
    return agent_dict

player_names = ["1号", "2号", "3号", "4号", "5号", "6号"]
player1 =  modify_agent_config_cn(name=player_names[0],
                              name_list=player_names,
                              player_roles=PLAYER_ROLES,
                              game_rule=GAME_RULE,
                              mission_phase=Mission_Phase,
                              role="morgana",
                              role_hint=Role_hint_morgana_cn,
                              language='cn',
                              #character_info = "你来自青岛，娃娃脸，喜欢搞别人，比较搞笑，MBTI是ESTP，说话较简练"
                              )

player2 =  modify_agent_config_cn(name=player_names[1],
                              name_list=player_names,
                            player_roles=PLAYER_ROLES,
                              game_rule=GAME_RULE,
                              mission_phase=Mission_Phase,
                              role="assassin",
                              role_hint=Role_hint_assassin_cn,
                              #character_info = "你来自成都，对桌游十分狂热，脑筋与常人不同，比较搞笑，MBTI是ENFJ，说话较简练"
                              )
player3 =  modify_agent_config_cn(name=player_names[2],
                              name_list=player_names,
                              player_roles=PLAYER_ROLES,
                              game_rule=GAME_RULE,
                              mission_phase=Mission_Phase,
                              role="percival",
                              role_hint=Role_hint_percival_cn,
                              #character_info = "你头脑机灵，来自湖州，从小跳舞，喜欢当坏人，比较搞笑，MBTI是INTJ，说话较简练"
                              )


player4 =  modify_agent_config_cn(name=player_names[3],
                              name_list=player_names,
                              player_roles=PLAYER_ROLES,
                              game_rule=GAME_RULE,
                              mission_phase=Mission_Phase,
                              role="villager1",
                              role_hint=Role_hint_villager_cn,
                              character_info = "你容易挑选较为冒险的策略，如果是村民，喜欢假扮派西维尔"
                              )


player5 =  modify_agent_config_cn(name=player_names[4],
                              name_list=player_names,
                              player_roles=PLAYER_ROLES,
                              game_rule=GAME_RULE,
                              mission_phase=Mission_Phase,
                              role="villager2",
                              role_hint=Role_hint_villager_cn,
                              #character_info = "你来自成都，喜欢搞别人，自己也很搞笑，MBTI是ENTP，说话较简练")
                              )

player6 =  modify_agent_config_cn(name=player_names[5],
                              name_list=player_names,
                              player_roles=PLAYER_ROLES,
                              game_rule=GAME_RULE,
                              mission_phase=Mission_Phase,
                              role="merlin",
                              role_hint=Role_hint_merlin_cn,
                              #character_info = "你头脑聪明，来自嘉兴，一直是班里的第一名，外部文静但是腹黑，MBTI是INTJ，说话较简练"
                              )


def load_agent_configs(agent_info_list):
    with open("./configs/agent_configs_cn.json", "r", encoding="utf-8") as f:
        agent_configs = json.load(f)
    for idx,agent_config in enumerate(agent_configs):
        agent_config['args']['sys_prompt'] = agent_info_list[idx]
        agent_config['args']['name'] = player_names[idx]
    with open("./configs/agent_configs_cn_modify.json", "w", encoding="utf-8") as f:
        json.dump(agent_configs, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    cc_list = [player1,player2,player3,player4,player5,player6]
    load_agent_configs(cc_list)