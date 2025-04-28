# -*- coding: utf-8 -*-
"""Used to record prompts, will be replaced by configuration"""
from agentscope.parsers.json_object_parser import MarkdownJsonDictParser

class Prompts:
    """Prompts for werewolf game"""
    to_captain_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "你的想法是什么", 
            "speak": "你要说什么",
            "choice": "玩家名单列表",
        },
        required_keys=["thought", "speak", "choice"],
        keys_to_memory="speak",
        keys_to_content="speak",
        keys_to_metadata="choice",
    )
        
    to_captain = "{}, 你是队长。你需要选择{}名玩家参加任务。在{}中你选择哪些玩家？"

    to_all_welcome = "欢迎来到阿瓦隆！发言顺序将是：{}，队长将轮流担任。"
    
    to_wolves = "在这局游戏中，坏人是{}。现在你可以见到你的坏人队友并商议如何破坏好人阵营。"

    wolves_discuss_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "你的想法是什么",
            "speak": "你要对你的队友说什么，谁来假扮派西维尔。",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
    )
    to_wolves_early_assassin = "这轮任务成功了是否要立刻开启刺杀？(true/false)"
    wolves_early_assassin_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "关于Merlin是谁",
            "speak": "关于Merlin是谁",
            "metadata": "是否要立刻刺杀(true/false)",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
        keys_to_content ="metadata",
    )
    wolves_discuss_assassin_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "关于Merlin是谁，以及刺杀的目标，你的想法是什么",
            "speak": "关于Merlin是谁，以及刺杀的目标，你要说什么",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
    )

    assassin_discuss_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "你的想法是什么",
            "speak": "你要说什么",
            "finish_discussion": "讨论是否达成一致 (true/false)",
        },
        required_keys=["thought", "speak", "finish_discussion"],
        keys_to_memory="speak",
        keys_to_content="speak",
        keys_to_metadata=["finish_discussion"],
    )

    to_wolves_vote = ""

    to_crews_vote = "这轮任务你想要执行还是破坏？(proceed/sabotage)"



    to_wolves_res = "请确保你知道谁是你的队友。"

    to_percival_resurrect = (
        "{witch_name}，你是派西维尔。{merlin_name}和{morgana}是梅林和莫甘娜，但不清楚谁是谁。"
    )

    to_merlin = (
        "{}，你是梅林。{}是坏人"
    )

    merilin_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "你的想法是什么",
            "metadata": "坏人名字，字符串类型",
        },
        required_keys=["thought", "metadata"],
        keys_to_memory=["thought","metadata"],
        keys_to_content="metadata",
    )

    to_merlin_result = "好的，{}的角色在{}阵营。"

    to_villagers = "你是村民。请想一想自己在这轮游戏中的策略"

    villagers_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "你本局的策略是什么,要不要假扮派西维尔以混淆坏人",
        },
        required_keys=["thought"],
        keys_to_memory="thought",
    )

    to_percival = (
        "{}，你是派西维尔。梅林和莫甘娜在{}中，但不清楚谁是谁。"
    )

    percival_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "字符串：你的想法是什么，是否要直接向大家公布自己的身份",
            "note":"1.请不要直接暴露梅林和莫甘娜的玩家名，这样会导致任务失败\n2.如果有玩家和你对跳派西维尔，他可能是坏人，也可能是村民保护梅林",
            "metadata": "字符串：重要的名字",
        },
        required_keys=["thought", "metadata","note"],
        keys_to_memory=["thought", "metadata","note"],
        keys_to_content="metadata",
    )

    to_assassin = (
        "{}，你是刺客。你想要在{}中刺杀哪个玩家？"
    )

    assassin_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "你的想法是什么",
            "speak": "玩家名字",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
        keys_to_content="speak",
    )

    to_all_danger = (
        "天亮了，所有玩家睁开眼睛。昨晚，"
        "以下玩家被淘汰：{}。"
    )

    to_all_peace = (
        "天亮了，所有玩家睁开眼睛。昨晚很平静，"
        "没有玩家被淘汰。"
    )

    to_all_vote_crewlist = (
        "队长已选择{}参加任务。根据游戏规则和你的角色，"
        "基于当前情况和你获得的信息，为了投票决定是否同意队长的选择并赢得游戏，"
        "你想对其他人说什么？你可以决定是否透露你的角色。"
    )

    survivors_discuss_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "你的想法是什么",
            "speak": "你要说什么",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
        keys_to_content="speak",
    )

    survivors_vote_crewlist_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "你的想法是什么",
            "agree": "你是否同意队长的选择 (true/false)",
        },
        required_keys=["thought", "agree"],
        keys_to_memory="thought",
        keys_to_content="agree",
        keys_to_metadata=["agree"],
    )

    survivors_vote_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "你的想法是什么",
            "vote": "玩家名字",
        },
        required_keys=["thought", "vote"],
        keys_to_memory="vote",
        keys_to_content="vote",
    )

    crews_vote_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "你的想法是什么",
            "vote": "这轮任务你想要执行还是破坏？(proceed/sabotage)",
        },
        required_keys=["thought", "vote"],
        keys_to_memory="vote",
        keys_to_content="vote",
    )

    wolves_vote_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "这轮要不要sabotage，有没有其他队友在任务中，暴露的可能性",
            "vote": "这轮任务你想要执行还是破坏？(proceed/sabotage)",
        },
        required_keys=["thought", "vote"],
        keys_to_memory=["thought", "vote"],
        keys_to_content="vote",
    )

    to_all_vote = (
        "根据游戏规则和你的角色，基于当前情况和你获得的信息，"
        "为了赢得游戏，现在是投票时间，你是否同意队长的选择。"
        "你同意吗？(true/false)。注意如果连续3次没有达成一致，这个任务将被破坏。"
    )

    to_all_mission_res = "任务票型是{},结果是{}，下一任队长是{}。"

    to_all_res_false = "投票票型为{},结果是否决，队长将更换。下一任队长是{}。"
    to_all_res_false_3 = "投票票型为{},结果是否决，你们已经投票3次都没有达成一致，这个任务被破坏。"

    to_all_res_true = "投票票型为{}, 结果是通过，我们将开始任务。"

    to_all_wolf_win = (
        "游戏结束。邪恶阵营，莫甘娜和刺客已经占领了村庄。"
        "祝下次好运！"
    )

    to_all_village_win = (
        "游戏结束。好人阵营，派西维尔、梅林和村民保护了村庄，"
        "村庄再次安全了！"
    )

    to_all_continue = "当前任务完成情况为：{},游戏继续。"
