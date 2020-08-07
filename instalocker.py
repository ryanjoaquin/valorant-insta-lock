import time
import pyautogui
import keyboard
import configparser

character = {}


def lock_character():
    pyautogui.click(900, 846)
    pyautogui.click(960, 846)


def wait_for_keyboard_press():
    print("Press F6 to lock the character. Tipp: You can do this "
          "at the end of the load screen")
    while True:
        if keyboard.is_pressed('f6'):
            print("F6 pressed.")
            break


def read_config():
    config = configparser.ConfigParser()
    configfilepath = 'C:\\config.ini'
    config.read(configfilepath)
    for i in range(12):
        character[str(i)] = config.get('main', str(i + 1))
        #print(character)

    for i in character:
        if character[str(i)] == "1":
            character[str(i)] = "Brimstone"
        if character[str(i)] == "2":
            character[str(i)] = "Cypher"
        if character[str(i)] == "3":
            character[str(i)] = "Jett"
        if character[str(i)] == "4":
            character[str(i)] = "Omen"
        if character[str(i)] == "5":
            character[str(i)] = "Pheonix"
        if character[str(i)] == "6":
            character[str(i)] = "Sage"
        if character[str(i)] == "7":
            character[str(i)] = "Sova"
        if character[str(i)] == "8":
            character[str(i)] = "Breach"
        if character[str(i)] == "9":
            character[str(i)] = "Killjoy"
        if character[str(i)] == "10":
            character[str(i)] = "Raze"
        if character[str(i)] == "11":
            character[str(i)] = "Reyna"
        if character[str(i)] == "12":
            character[str(i)] = "Viper"
    print("Converting done!")

    return character


def choose_0():
    wait_for_keyboard_press()
    pyautogui.click(454, 960)
    lock_character()
    print("Character chosen!")


def choose_1():
    wait_for_keyboard_press()
    pyautogui.click(540, 960)
    lock_character()
    print("Character chosen!")


def choose_2():
    wait_for_keyboard_press()
    pyautogui.click(628, 960)
    lock_character()
    print("Character chosen!")


def choose_3():
    wait_for_keyboard_press()
    pyautogui.click(720, 960)
    lock_character()
    print("Character chosen!")


def choose_4():
    wait_for_keyboard_press()
    pyautogui.click(813, 960)
    lock_character()
    print("Character chosen!")


def choose_5():
    wait_for_keyboard_press()
    pyautogui.click(921, 960)
    lock_character()
    print("Character chosen!")


def choose_6():
    wait_for_keyboard_press()
    pyautogui.click(998, 960)
    lock_character()
    print("Character chosen!")


def choose_7():
    wait_for_keyboard_press()
    pyautogui.click(1099, 960)
    lock_character()
    print("Character chosen!")


def choose_8():
    wait_for_keyboard_press()
    pyautogui.click(1200, 960)
    lock_character()
    print("Character chosen!")


def choose_9():
    wait_for_keyboard_press()
    pyautogui.click(1281, 960)
    lock_character()
    print("Character chosen!")


def choose_10():
    wait_for_keyboard_press()
    pyautogui.click(1373, 960)
    lock_character()
    print("Character chosen!")


def choose_11():
    wait_for_keyboard_press()
    pyautogui.click(1460, 960)
    lock_character()
    print("Character chosen!")


def insta_lock_character(character):
    for i in character:
        print(i + "=" + character[i])

    characterstr = input("Which character do you want to insta-lock?[number]")

    if characterstr == "0":
        choose_0()
    if characterstr == "1":
        choose_1()
    if characterstr == "2":
        choose_2()
    if characterstr == "3":
        choose_3()
    if characterstr == "4":
        choose_4()
    if characterstr == "5":
        choose_5()
    if characterstr == "6":
        choose_6()
    if characterstr == "7":
        choose_7()
    if characterstr == "8":
        choose_8()
    if characterstr == "9":
        choose_9()
    if characterstr == "10":
        choose_10()
    if characterstr == "11":
        choose_11()


def main():
    while True:
        read_config()
        insta_lock_character(character)


if __name__ == '__main__':
    main()

#Positions:
# Y: 960
# Brimstone:    454
# Cypher:       540
# Jett:         628
# Omen:         728
# Pheonix:      813
# Sage:         921
# Sova:         998
# Breach:       1099
# Killjoy:      1200
# Raze:         1281
# Reyna:        1373
# Viper:        1460

# Lock: 960    846