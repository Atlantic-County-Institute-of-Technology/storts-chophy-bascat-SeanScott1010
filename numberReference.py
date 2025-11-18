import os
import random
import math
wordList = []
maxTries = [1, 2, 3, 4, 5]
wordLen = 0


def fetchDifficulty():
    while True:
        global wordLen
        print("[-] 0. Exit \n"
                "[-] 1. Change word Length\n"
                "[-] 2. Start a round\n")
        selection = int(input("[-] Please select an option: "))
        if selection == 0:
            exit()
        elif selection == 1:
                wordNumber = input("How many letters should your word be: ")
                try:
                    int(wordNumber)
                    wordLen = int(wordNumber)
                except:
                    print("choose an →→→→→→→→NUMBER←←←←←←←←")
        elif selection == 2 and wordLen != 0:
            main()
            return wordLen
        elif selection == 2 and wordLen == 0:
            print("[!] Choose a number before starting")
        else:
            print("hey dummy that's not an option")


def extractWords():
    global wordList
    global wordLen
    try:
        with open("assets/words_alpha.txt", "r") as file:
            for word in file:
                if len(word.strip()) == wordLen:
                    wordList.append(word.strip())
    except FileNotFoundError:
        print("[!] Error! File not found.")
    wordRandomizer = random.randint(0, len(wordList))
    target = wordList[wordRandomizer]
    return target


def main():
    global maxTries
    target = extractWords()
    response = ["Red" for i in range(len(target))]
    for yes in maxTries:
        guess = input(f"Please enter a {wordLen} letter word: ")
        if guess == target:
            print("yay")
            exit()
        else:
            for gDigit in range(len(target)):
                for tDigit in range(len(target)):
                    if guess[gDigit] == target[tDigit]:
                        if gDigit == tDigit:
                            response[gDigit] = "Green"
                        else:
                            response[gDigit] = "Yellow"
            print(response)
    print(target)


if __name__ == "__main__":
    fetchDifficulty()


