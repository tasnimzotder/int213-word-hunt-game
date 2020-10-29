"""
INT213 - Word Hunt Game
Let's hunt the lost words 🔍

Repository: https://github.com/tasnimzotder/int213-word-hunt-game/
Readme: https://github.com/tasnimzotder/int213-word-hunt-game/blob/master/README.md
"""

import string
import random
import tkinter as tk
import yaml

pressedWord = ''
prev = [0, 0]
route = [0, 0]


def readConfigFile():
    with open(r'config.yaml') as file:
        configFile = yaml.load(file, Loader=yaml.FullLoader)

    return configFile


def writeConfigFile(data):
    with open('config.yaml', 'w') as file:
        yaml.dump(data, file)


def startGame():
    root = tk.Tk()
    root.title("INT213 - Word Hunt Game")

    frame1 = tk.Frame(master=root, bg="red")
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=False, padx=20, pady=12)

    frame2 = tk.Frame(master=root)
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=12)

    configFile = readConfigFile()

    # bg="#70889c"
    frame3 = tk.Frame(master=root)
    frame3.pack(fill=tk.BOTH, side=tk.RIGHT, padx=20, pady=30)

    labelWelcome = tk.Label(master=frame3, text="Welcome").grid(row=0)

    labelWName = tk.Label(master=frame3,
                          text=configFile['player'][1]['name']).grid(row=1)

    wordList = [word for word in configFile['words']]
    size = numWords = configFile['words_count']

    arr = [[0 for x in range(size)] for y in range(size)]
    button = [[0 for x in range(size)] for y in range(size)]
    check = [0 for numWords in range(size)]
    dictionary = [0 for createWordSet in range(numWords)]

    directionArr = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1],
                    [0, -1], [1, -1]]

    class square:
        status = False
        char = ''
        filled = False

    def fill(x, y, word, direction):
        for i in range(len(word)):
            arr[x + direction[0] * i][y + direction[1] * i].char = word[i]
            arr[x + direction[0] * i][y + direction[1] * i].filled = True

    def wordPlace(j, dictionary):
        word = random.choice(wordList)
        direction = directionArr[random.randrange(0, 7)]

        x = random.randrange(0, size - 1)
        y = random.randrange(0, size - 1)

        if (x + len(word) * direction[0] > size - 1
                or x + len(word) * direction[0] < 0
                or y + len(word) * direction[1] > size - 1
            ) or y + len(word) * direction[1] < 0:
            wordPlace(j, dictionary)
            return

        for i in range(len(word)):
            if (arr[x + direction[0] * i][y +
                                          direction[1] * i].filled == True):
                if (arr[x + direction[0] * i][y + direction[1] * i].char !=
                        word[i]):
                    wordPlace(j, dictionary)
                    return
        dictionary[j] = word

        check[j] = tk.Label(frame2,
                            text=word,
                            height=1,
                            width=15,
                            font=('None %d ' % (10)),
                            anchor='c')
        check[j].grid()

        fill(x, y, word, direction)
        return dictionary

    def colourWord(pressedWord, valid):
        route[0] *= -1
        route[1] *= -1
        for i in range(len(pressedWord)):
            if valid == True or arr[prev[0] +
                                    i * route[0]][prev[1] +
                                                  i * route[1]].status == True:
                button[prev[0] + i * route[0]][prev[1] + i * route[1]].config(
                    bg='#535edb')
                arr[prev[0] + i * route[0]][prev[1] +
                                            i * route[1]].status = True
            elif (arr[prev[0] + i * route[0]][prev[1] +
                                              i * route[1]].status == False):
                button[prev[0] + i * route[0]][prev[1] + i * route[1]].config(
                    bg='#53dbb5')

    def checkWord():
        global pressedWord

        if pressedWord in dictionary:
            check[int(dictionary.index(pressedWord))].configure(
                font=('None %d overstrike' % (10)))
            check[int(dictionary.index(pressedWord))].grid()
            dictionary[dictionary.index(pressedWord)] = ''

            colourWord(pressedWord, True)
        else:
            colourWord(pressedWord, False)
        pressedWord = ''
        prev = [0, 0]

    def buttonPress(x, y):
        global pressedWord, prev, route
        newPressed = [x, y]

        if (len(pressedWord) == 0):
            prev = newPressed
            print(prev)
            pressedWord = arr[x][y].char
            button[x][y].configure(bg='yellow')

        elif (len(pressedWord) == 1 and (x - prev[0])**2 <= 1
              and (y - prev[1])**2 <= 1 and newPressed != prev):
            pressedWord += arr[x][y].char
            button[x][y].configure(bg='yellow')

            route = [x - prev[0], y - prev[1]]
            prev = [x, y]

        elif (len(pressedWord) > 1 and x - prev[0] == route[0]
              and y - prev[1] == route[1]):
            pressedWord += arr[x][y].char
            button[x][y].configure(bg='yellow')
            prev = [x, y]

    for x in range(size):
        for y in range(size):
            arr[x][y] = square()

    for i in range(numWords):
        wordPlace(i, dictionary)

    for y in range(size):
        for x in range(size):

            if (arr[x][y].filled == False):
                arr[x][y].char = random.choice(string.ascii_uppercase)

            button[x][y] = tk.Button(
                frame1,
                text=arr[x][y].char,
                bg='#53dbb5',
                width=2,
                height=1,
                command=lambda x=x, y=y: buttonPress(x, y))
            button[x][y].grid(row=x, column=y)

    checkW = tk.Button(frame2,
                       text="check Word",
                       height=1,
                       width=15,
                       anchor='c',
                       bg="#d7f7f1",
                       command=checkWord)
    checkW.grid()

    root.mainloop()


def main():
    preRoot = tk.Tk()
    preRoot.geometry("300x250")
    frame = tk.Frame(preRoot)
    frame.pack(pady=20, padx=26)
    preRoot.title("[Setup] INT213 - Word Hunt Game")

    def updateUserInput():
        username = userNameField.get()
        nosWords = nosWordsField.get()

        data = readConfigFile()
        data['player'][1]['name'] = str(username)
        data['words_count'] = int(nosWords)
        writeConfigFile(data)
        startGame()
        preRoot.destroy()

    tk.Label(frame, text="Name").grid(row=0)
    userNameField = tk.Entry(frame)
    userNameField.grid(row=0, column=1)

    tk.Label(frame, text="No. of Words").grid(row=1)
    nosWordsField = tk.Entry(frame)
    nosWordsField.grid(row=1, column=1)

    tk.Button(frame, text="Enter", command=updateUserInput).grid(row=3,
                                                                 column=1,
                                                                 pady=8)

    preRoot.mainloop()


if __name__ == '__main__':
    main()
