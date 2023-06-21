import pyautogui
import time

while True:
    pos = pyautogui.position()  # Get the current mouse position.
    print(pos)  # Print it to the console.
    time.sleep(1)  # Wait for 1 second.