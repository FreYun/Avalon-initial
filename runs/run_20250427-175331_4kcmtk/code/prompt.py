# -*- coding: utf-8 -*-
"""Used to record prompts, will be replaced by configuration"""
from agentscope.parsers.json_object_parser import MarkdownJsonDictParser

class Prompts:
    """Prompts for werewolf game"""
    to_captain_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "what you thought", 
            "speak": "what you speak",
            "choice": "player_names list",
        },
        required_keys=["thought", "speak", "choice"],
        keys_to_memory="speak",
        keys_to_content="speak",
        keys_to_metadata="choice",
    )
        
    to_captain = "{}, you are the captain. You need to elect {} players to join the mission. Which players among {} are your choice?"

    to_all_welcome = "Welcome to Avalon! The speaking order will be: {}, the captain will be chosen by turn."
    
    to_wolves = "In this game, the wolves are {}. Now you can meet your wolf teammates and figure out how to sabotage the good side."

    wolves_discuss_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "what you thought",
            "speak": "what you will speak to your teammates",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
    )
    
    wolves_discuss_assassin_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "what are your thoughts about who is Merlin and who to assassinate",
            "speak": "what do you want to say about who is Merlin and who to assassinate",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
    )

    assassin_discuss_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "what you thought",
            "speak": "what you speak",
            "finish_discussion": "whether the discussion reached an "
            "agreement or not (true/false)",
        },
        required_keys=["thought", "speak", "finish_discussion"],
        keys_to_memory="speak",
        keys_to_content="speak",
        keys_to_metadata=["finish_discussion"],
    )

    to_wolves_vote = "Which player do you vote to kill?"

    to_crews_vote = "Do you want to proceed with the mission or sabotage it this round? (proceed/sabotage)"

    wolves_vote_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "what you thought",
            "vote": "player_names",
        },
        required_keys=["thought", "vote"],
        keys_to_memory="vote",
        keys_to_content="vote",
    )

    to_wolves_res = "Make sure you know which player is your teammate."


    to_percival_resurrect = (
        "{witch_name}, you're percival. {merlin_name} and {morgana} are Merlin and Morgana, but it’s unclear who is who.} "
    )

    to_merlin = (
        "{}, you're Merlin. {} are wolves"
    )

    merilin_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "what you thought",
            "metadata": "wolves_names, type is string",
        },
        required_keys=["thought", "metadata"],
        keys_to_memory=["thought","metadata"],
        keys_to_content="metadata",
    )

    to_merlin_result = "Okay, the role of {} is on the {}."

    to_percival = (
        "{}, you're percival Merlin and Morgana are among {}, but it's unclear who is who."
    )

    percival_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "what you thought,remember which two players are merlin and morgana",
            "metadata": "Important names",
        },
        required_keys=["thought", "metadata"],
        keys_to_memory=["thought", "metadata"],
        keys_to_content="metadata",
    )

    to_assassin = (
        "{}, you're the assassin. Which player in {} would you like to kill?"
    )

    assassin_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "what you thought",
            "speak": "player_name",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
        keys_to_content="speak",
    )

    to_all_danger = (
        "The day is coming, all the players open your eyes. Last night, "
        "the following player(s) has been eliminated: {}."
    )

    to_all_peace = (
        "The day is coming, all the players open your eyes. Last night is "
        "peaceful, no player is eliminated."
    )

    to_all_vote_crewlist = (
        "The Captain has chosen {} to join the mission. Given the game rules and your role, "
        "based on the situation and the information you gain, to vote to "
        "decide if you agree captain's choice and to win the game, what do "
        "you want to say to others? You can decide whether to reveal your "
        "role."
    )


    survivors_discuss_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "what you thought",
            "speak": "what you speak",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
        keys_to_content="speak",
    )

    survivors_vote_crewlist_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "what you thought",
            "agree": "whether you agree captain's choice (true/false)",
        },
        required_keys=["thought", "agree"],
        keys_to_memory="thought",
        keys_to_content="agree",
        keys_to_metadata=["agree"],
    )

    survivors_vote_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "what you thought",
            "vote": "player_name",
        },
        required_keys=["thought", "vote"],
        keys_to_memory="vote",
        keys_to_content="vote",
    )

    crews_vote_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "what you thought",
            "vote": "Do you want to proceed with the mission or sabotage it this round? (proceed/sabotage)",
        },
        required_keys=["thought", "vote"],
        keys_to_memory="vote",
        keys_to_content="vote",
    )

    to_all_vote = (
        "Given the game rules and your role, based on the situation and the"
        " information you gain, to win the game, it's time to vote whether "
        "you agree captain's choice. Do you agree or not?(true/false). Note if you don't get agreement for 3 times, this misson will be sabotaged."
    )

    to_all_mission_res = "The mission result is {}, the next captain is {}."

    to_all_res_false = "The vote result is false, captain will change. The next captain is {}."
    to_all_res_false_3 = "The vote result is false, you have voted 3 times and didn't get agreement, this misson is sabotaged."

    to_all_res_true = "The vote result is true, we will start the mission."

    to_all_wolf_win = (
        "The game is over. The evil side, morgana and assassin have prevailed and taken over the village. Better "
        "luck next time!"
    )

    to_all_village_win = (
        "The game is over. The good side, percival and merlin and villagers have protected the village and the village "
        "is safe once again!"
    )

    to_all_continue = "The game goes on."
