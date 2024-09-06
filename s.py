from pynput.mouse import Listener
import time
def on_move(x, y):
    print(f"Mouse moved to ({x}, {y})")

def main():
    # Start the mouse listener
    with Listener(on_move=on_move) as listener:
        
        listener.join()

if __name__ == "__main__":
    main()
