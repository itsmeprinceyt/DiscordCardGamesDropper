# Discord Card Games Dropper

**Disclaimer:** This program is intended for educational purposes only. The use of this program is not encouraged, and the author does not endorse its use.

## Overview

This repository contains various Python scripts designed to automate interactions with popular Discord card game bots such as **Sofi** and **Karuta**. These scripts use modules like `pyautogui`, `time`, and `keyboard` to simulate user interactions, allowing you to drop and tag cards automatically. Each variation of the program offers unique features for automating different aspects of the game.

## Features

- **Automated Card Dropping:** Automatically sends the appropriate commands (`SD`, `KD`, etc.) to drop cards for Sofi and Karuta bots.
- **Automatic Tagging:** Tags the cards after dropping them with custom commands like `ST BD`.
- **Random Card Chooser:** Randomly selects a card from the available options.
- **Customizable:** Easily customizable for different screen resolutions and specific automation needs.
- **Supports Multiple Bots:** The scripts automate card dropping and tagging for both Sofi and Karuta bots. (Check Variations Carefully)

## Files and Variations

### `Coordinates_Grabber.py`

This helper script allows you to capture the screen coordinates required by the main automation program. Since the `auto_drop2.py` script is built on a display resolution of `1336x768`, use this script to adjust the coordinates for your specific display resolution and update the main script accordingly. Use this to make changes to the auto dropper according to your screen resolution.

### `Sofi_Karuta_Dropper.py`

This script automates the process of card dropping and tagging for both **Sofi** and **Karuta** bots on Discord. It uses randomization to select one of the available cards after a drop and tags it appropriately. You can configure it to run drops in cycles, alternating between Sofi and Karuta as per their cooldown periods. It contains:

- Automated card dropping and tagging.
- Random card selection.
- Looping mechanisms for continuous gameplay.

### Custom Variations
Several variations of the main automation script exist, designed to support different patterns of gameplay. For example:

- **Sofi_Dropper.py:** Automatically drops cards for Sofi every 8 minutes and always selects the first card.
- **Sofi_Dropper_Sofu.py:** Automatically drops cards for Sofi every 8 minutes and always selects the first card. This variation works with SOFU enabled.
- **Sofi_Dropper2.py:** Automatically drops cards for Sofi every 8 minutes and randomly selects any one of the three cards.

> Note: The programs are designed to run indefinitely, continuously automating the card drops. To stop the execution, you'll need to manually terminate the program by closing the script or using a keyboard interrupt (e.g., `Ctrl + C` in the terminal).

## Things to Consider

- The program is designed based on a display resolution of **1336x768**. You will need to use `coordinates_grabber.py` to adjust the screen coordinates for your display and modify the main automation script accordingly.
- This tool automates mouse clicks and keyboard inputs, so ensure that no important work is running in the background when you execute the script.
- Modify the automation logic to suit your specific gameplay requirements for Sofi and Karuta bots.

## Setup and Usage

### Requirements

- `Python 3.x`
- Install the following Python modules:
  ```bash
  pip install pyautogui keyboard
