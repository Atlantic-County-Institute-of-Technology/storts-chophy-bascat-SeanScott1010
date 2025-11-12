# scb_nocom.py
# description: A simple number-guessing game similar to Pico Fermi Bagels
# this time with zero comments
# author: pcostjr
# created: 11.03.2025
# last update: 11.03.2025

import random

MIN_VAL = 100
MAX_VAL = 999


def generate_number_list():
    value = random.randint(MIN_VAL, MAX_VAL)
    return str(value)


target = generate_number_list()
print(target)


def main():
    guess = input("Please enter a three-digit number: ")
    response = ["Bascat" for i in range(len(target))]
    if guess == target:
        print("yay")
    else:
        for gDigit in range(len(target)):
            for tDigit in range(len(target)):
                # print(f"Counter: {tDigit}")
                # print(f"Guess digit is {guess[gDigit]} | Target digit is {target[tDigit]}")
                if guess[gDigit] == target[tDigit]:
                    if gDigit == tDigit:
                        response[gDigit] = "Chophy"
                    else:
                        response[gDigit] = "Storts"


    print(response)










if __name__ == '__main__':
    main()
