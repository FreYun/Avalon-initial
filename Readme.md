# Avalon Game Project

This is an implementation of the Avalon board game using AI agents as players. The game features multiple AI agents taking on different roles and interacting through natural language to play the classic social deduction game.

## Features

- Multi-agent gameplay with AI players
- Natural language interactions between agents
- Support for all classic Avalon roles:
  - Merlin
  - Percival 
  - Morgana
  - Assassin
  - Villagers
- Configurable game settings
- Detailed game logs and conversation history

## Requirements

- Python 3.8+


## Installation

1. Clone this repository
2. Install dependencies:

## modify agent
You can modify agent configurations in modify_agent.py, including roles, prompts, personalities, etc. After making changes, run modify_agent.py to generate the corresponding JSON file that will be used to configure the agent model.
Then in avalon.py, change model_configs to point to the corresponding JSON file for the changes to take effect.