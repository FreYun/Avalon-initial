# -*- coding: utf-8 -*-
"""Used to record prompts, will be replaced by configuration"""
from agentscope.parsers.json_object_parser import MarkdownJsonDictParser

class Prompts:
    """Prompts for werewolf game"""
    to_captain_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "What are your thoughts",
            "speak": "What do you want to say",
            "choice": "List of player names",
        },
        required_keys=["thought", "speak", "choice"],
        keys_to_memory="speak",
        keys_to_content="speak",
        keys_to_metadata="choice",
    )
        
    to_captain = "{}, you are the captain. You need to select {} players for the mission. Who do you choose from {}?"

    to_all_welcome = "Welcome to Avalon! The speaking order will be: {}, and the captain role will rotate."
    
    to_wolves = "In this game, the wolves are {}. Now you can meet your wolf teammates and discuss how to sabotage the good team."

    wolves_discuss_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "What are your thoughts",
            "speak": "What do you want to say to your teammates, who will pretend to be Percival",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
    )
    to_wolves_early_assassin = "The mission succeeded, do you want to start assassination now? (true/false)"
    wolves_early_assassin_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "About who Merlin is",
            "speak": "About who Merlin is",
            "metadata": "Whether to assassinate now (true/false)",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
        keys_to_content ="metadata",
    )
    wolves_discuss_assassin_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "Your thoughts about who Merlin is and who to assassinate",
            "speak": "What you want to say about who Merlin is and who to assassinate",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
    )

    assassin_discuss_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "What are your thoughts",
            "speak": "What do you want to say",
            "finish_discussion": "Has discussion reached consensus (true/false)",
        },
        required_keys=["thought", "speak", "finish_discussion"],
        keys_to_memory="speak",
        keys_to_content="speak",
        keys_to_metadata=["finish_discussion"],
    )

    to_wolves_vote = ""

    to_crews_vote = "Do you want to proceed or sabotage this mission? (proceed/sabotage)"

    to_wolves_res = "Please make sure you know who your teammates are."

    to_percival_resurrect = (
        "{witch_name}, you are Percival. {merlin_name} and {morgana} are Merlin and Morgana, but you don't know who is who."
    )

    to_merlin = (
        "{}, you are Merlin. {} are the wolves"
    )

    merilin_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "What are your thoughts",
            "metadata": "Names of wolves, string type",
        },
        required_keys=["thought", "metadata"],
        keys_to_memory=["thought","metadata"],
        keys_to_content="metadata",
    )

    to_merlin_result = "Okay, {}'s role is on the {} team."

    to_villagers = "You are a villager. Please think about your strategy for this game"

    villagers_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "What is your strategy for this game, do you want to pretend to be Percival to confuse the wolves",
        },
        required_keys=["thought"],
        keys_to_memory="thought",
    )

    to_percival = (
        "{}, you are Percival. Merlin and Morgana are among {}, but you don't know who is who."
    )

    percival_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "string: What are your thoughts, whether to reveal your identity directly to everyone",
            "note":"1. Please don't directly expose the player names of Merlin and Morgana, this will lead to mission failure\n2. If a player claims to be Percival like you, they could be a wolf or a villager protecting Merlin",
            "metadata": "string: Important names",
        },
        required_keys=["thought", "metadata","note"],
        keys_to_memory=["thought", "metadata","note"],
        keys_to_content="metadata",
    )

    to_assassin = (
        "{}, you are the Assassin. Which player do you want to assassinate from {}?"
    )

    assassin_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "What are your thoughts",
            "speak": "Player name",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
        keys_to_content="speak",
    )

    to_all_danger = (
        "Dawn breaks, all players open their eyes. Last night, "
        "the following players were eliminated: {}."
    )

    to_all_peace = (
        "Dawn breaks, all players open their eyes. Last night was peaceful, "
        "no players were eliminated."
    )

    to_all_vote_crewlist = (
        "The captain has chosen {} to participate in the mission. Based on game rules and your role, "
        "and the current situation and information you have, to vote on whether to approve the captain's choice and win the game, "
        "what do you want to say to others? You can decide whether to reveal your role. Note: Team composition cannot be changed manually unless it's the next round."
    )

    survivors_discuss_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "What are your thoughts",
            "speak": "What do you want to say",
        },
        required_keys=["thought", "speak"],
        keys_to_memory="speak",
        keys_to_content="speak",
    )

    survivors_vote_crewlist_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "What are your thoughts",
            "agree": "Do you agree with the captain's choice (true/false)",
        },
        required_keys=["thought", "agree"],
        keys_to_memory="thought",
        keys_to_content="agree",
        keys_to_metadata=["agree"],
    )

    survivors_vote_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "What are your thoughts",
            "vote": "Player name",
        },
        required_keys=["thought", "vote"],
        keys_to_memory="vote",
        keys_to_content="vote",
    )

    crews_vote_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "What are your thoughts",
            "vote": "Do you want to proceed or sabotage this mission? (proceed/sabotage)",
        },
        required_keys=["thought", "vote"],
        keys_to_memory="vote",
        keys_to_content="vote",
    )

    wolves_vote_parser = MarkdownJsonDictParser(
        content_hint={
            "thought": "Should you sabotage this round, are there other teammates on the mission, what's the chance of exposure",
            "vote": "Do you want to proceed or sabotage this mission? (proceed/sabotage)",
        },
        required_keys=["thought", "vote"],
        keys_to_memory=["thought", "vote"],
        keys_to_content="vote",
    )

    to_all_vote = (
        "Based on game rules and your role, and the current situation and information you have, "
        "to win the game, it's now voting time, do you agree with the captain's choice. "
        "Do you agree? (true/false). Note that if consensus is not reached after 3 consecutive votes, this mission will be sabotaged."
    )

    to_all_mission_res = "The mission vote pattern is {}, the result is {}, the next captain is {}."

    to_all_res_false = "The vote pattern is {}, the result is rejected, the captain will change. The next captain is {}."
    to_all_res_false_3 = "The vote pattern is {}, the result is rejected, you have failed to reach consensus after 3 votes, this mission is sabotaged."

    to_all_res_true = "The vote pattern is {}, the result is approved, we will begin the mission, team composition is {}."

    to_all_wolf_win = (
        "Game Over. The evil team, Morgana and the Assassin have taken over the village. "
        "Better luck next time!"
    )

    to_all_village_win = (
        "Game Over. The good team, Percival, Merlin and the villagers have protected the village, "
        "the village is safe again!"
    )

    to_all_continue = "Current mission completion status: {}, game continues."
