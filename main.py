import pyautogui
from PIL import Image
import pytesseract
import keyboard
import time

def get_stats():
    screenshot = pyautogui.screenshot(region=(35, 620, 380, 130))
    screenshot.save('data/screenshot.png')
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    base_image = Image.open("data\\screenshot.png")
    name_image = base_image.crop((80, 15, 300, 40))
    name_image.save('data/name.png')
    name_image_saved = Image.open("data\\name.png")
    name_text = pytesseract.image_to_string(name_image_saved).strip()


    stats_image = base_image.crop((78, 38, 169, 120))
    stats_image.save("data/stats.png")
    stats_image_saved = Image.open("data\\stats.png")
    stats_text = pytesseract.image_to_string(stats_image_saved)
    stats = stats_text.strip().split("\n")


    hp_data = stats[0].split(" ")[1]
    spd_data = stats[1].split(" ")[1]
    atk_data = stats[2].split(" ")[1]
    def_data = stats[3].split(" ")[1]
    print(f"hp = {hp_data}, speed = {spd_data}, atk = {atk_data}, def = {def_data}, name = {name_text}")

def drop_item():
    pyautogui.click(146,794)

if __name__ == "__main__":
    while True:
        if keyboard.is_pressed("f12"):
            get_stats()
        if keyboard.is_pressed("right ctrl"):
            drop_item()
            time.sleep(0.5)
            pyautogui.click(-219,21)
