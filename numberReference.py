import os
import random
import math
wordList = []
wordLen = 5
maxTries = 5
counter = 0
def extractWords():
    global wordList
    try:
        with open("assets/words_alpha.txt", "r") as file:
            for word in file:
                if len(word.strip()) == wordLen:
                    wordList.append(word.strip())
    except FileNotFoundError:
        print("[!] Error! File not found.")
    wordRandomizer = random.randint(0, len(wordList))
    target = wordList[wordRandomizer]
    return(target)


def main():
    global counter
    global maxTries
    target = extractWords()
    guess = input("Please enter a five letter word: ")
    response = ["Bascat" for i in range(len(target))]
    while counter <= maxTries:
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
            counter += 1

    print(response)
    print(target)


if __name__ == "__main__":
    main()

