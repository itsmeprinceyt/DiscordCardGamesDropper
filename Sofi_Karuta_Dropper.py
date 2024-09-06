import pyautogui
import time
import keyboard
import random

def convert_seconds_to_min_sec(seconds):
    minutes, remaining_seconds = divmod(seconds, 60)
    if minutes > 0:
        result = f"{minutes} minute{'s' if minutes > 1 else ''} and {remaining_seconds} second{'s' if remaining_seconds > 1 else ''}"
    else:
        result = f"{remaining_seconds} second{'s' if remaining_seconds > 1 else ''}"
    return result

class AU:
    SOFI_DROP = "sd"
    SOFI_TAG = "st bd"
    KARUTA_DROP = "kd"
    KARUTA_TAG = "kt bd"
    GLOBAL_TIME_SLEEP = 5
    SOFI_CARD_SELECTOR = [419, 486, 560]
    KARUTA_CARD_SELECTOR = [408,455,506]

    @staticmethod
    def move_click(x, y):
        time.sleep(AU.GLOBAL_TIME_SLEEP)
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(AU.GLOBAL_TIME_SLEEP)
        pyautogui.click()
    
    @staticmethod
    def press_enter():
        time.sleep(AU.GLOBAL_TIME_SLEEP)
        keyboard.press('enter')
    
    @staticmethod
    def paste_string(string):
        time.sleep(AU.GLOBAL_TIME_SLEEP)
        keyboard.write(string)

    @staticmethod
    def auto_drop(drop_command, tag_command, bot_name):
        print("Dropping... ")
        time.sleep(AU.GLOBAL_TIME_SLEEP)
        AU.move_click(422, 691)
        AU.paste_string(drop_command)
        AU.press_enter()
        time.sleep(AU.GLOBAL_TIME_SLEEP)
        random_number = random.randint(0, 2)
        print(f"Choosen Card Number: {random_number+1} ")
        print("Selecting Card... ")
        if bot_name == "Sofi":
            AU.move_click(AU.SOFI_CARD_SELECTOR[random_number], 626)
        elif bot_name == "Karuta":
            AU.move_click(AU.KARUTA_CARD_SELECTOR[random_number], 626)
        AU.move_click(422, 691)
        print("Tagging Card... ")
        AU.paste_string(tag_command)
        AU.press_enter()
        AU.move_click(422, 691)

def main():
    print("SOFI & KARUTA DROPPER IS NOT ACTIVATED: ")
    print("AUTOMATION WILL START IN 10 SECONDS: ")
    for i in range(11):
        print(f"{11-i} seconds remaining.")
        time.sleep(1)
    
    SOFI_COUNTER = 3
    KARUTA_COUNTER = 1
    SOFI = "Sofi"
    KARUTA = "Karuta"

    while True:
        # Phase 1: Dropping 3 times in Sofi
        for _ in range(SOFI_COUNTER):

            #Sofi Drop
            print("SOFI (Phase 1):")
            AU.auto_drop(AU.SOFI_DROP, AU.SOFI_TAG, SOFI)
            random_time = random.randint(480, 495)
            formatted_time = convert_seconds_to_min_sec(random_time)
            print(f"[Phase 1] Sofi's Next Drop will occur in {formatted_time}.")
            time.sleep(random_time)


        # Phase 2: Dropping Sofi card once and then karuta card and then going into 8 minute delay.
        for _ in range(KARUTA_COUNTER):

            # Sofi Drop
            print("SOFI (Phase 2):")
            AU.auto_drop(AU.SOFI_DROP, AU.SOFI_TAG, SOFI)
            
            time.sleep(5)  # Short delay between Sofi and Karuta drops

            # Karuta Drop
            print("\nKARUTA (Phase 3): ")
            AU.auto_drop(AU.KARUTA_DROP, AU.KARUTA_TAG, KARUTA)
            karuta_cooldown = random.randint(1800, 1860)
            formatted_time = convert_seconds_to_min_sec(karuta_cooldown)
            print(f"Karuta's Next Drop will occur in approximately {formatted_time}.")

            random_time = random.randint(480, 495)
            formatted_time = convert_seconds_to_min_sec(random_time)
            print(f"[Phase 1] Sofi's Next Drop will occur in {formatted_time}.")
            time.sleep(random_time)


if __name__ == "__main__":
    main()