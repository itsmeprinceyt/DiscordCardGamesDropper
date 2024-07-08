# Sofi Card Dropper Automatic

**Disclaimer:** This program is intended for educational purposes only. The use of this program is not encouraged, and the author does not endorse its use.

## Overview

The Sofi Card Dropper Automatic program is a Python-based tool designed to automate interactions with the Discord application. The tool uses the `pyautogui`, `time`, and `keyboard` modules to control mouse and keyboard inputs. By setting specific coordinates, the program can automatically send commands in Discord and interact with the Sofi bot to drop and tag cards.

## Working

The program functions by setting specific coordinates for where it should click on the Discord message bar. It pastes the 'SD' command to drop a card, then selects the first card by default and tags it with 'ST BD'. Users can modify the program as needed.

## Features

- **Automated Card Dropping:** Sends the 'SD' command in Discord to drop a card.
- **Automatic Tagging:** Tags the card with 'ST BD'.
- **Random Card Chooser:** Randomly selects any card from the available three options.

## Files

### auto_drop2.py [ v2 ]

This script adds a random card chooser, allowing the program to randomly select any card from the three available options.

### coordinates_grabber.py

This script helps you grab the necessary screen coordinates for your display. Since the main program is built on a display resolution of `1336x768`, you need to use this script to get coordinates for your display and modify the main program accordingly.

## Things to Consider

- The program is designed based on a display resolution of 1336x768.
- Ensure you use the coordinates_grabber.py to adjust the coordinates for your specific display resolution.
- Modify the program as needed to suit your requirements.

## Setup and Usage
- `Python 3.x`
- `Modules: pyautogui, time, keyboard, random`
