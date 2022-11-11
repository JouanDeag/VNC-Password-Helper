from pyautogui import typewrite
from time import sleep
import sys
import random


def main(password: str):
    sleep(1)
    typewrite(password)


def gen():

    all = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
    length = 20

    loop = 0
    pwd = ""
    while loop < length:
        number = random.SystemRandom().randint(0, len(all) - 1)
        pwd += all[number]
        loop += 1

    # wwrite to file
    with open("password.txt", "w") as f:
        f.write(pwd)

    return pwd


# Check if -p followed by a password argument is passed
if __name__ == '__main__':
    if (len(sys.argv) == 1):
        main(gen())
    else:
        if (sys.argv[1] == "-s"):
            # Read from file
            with open("password.txt", "r") as f:
                main(f.read())
        else:
            text_to_type = sys.argv[1]
            main(text_to_type)
