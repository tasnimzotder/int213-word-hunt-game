"""
INT213 - Word Hunt Game
Let's hunt the lost words 🔍

Repository: https://github.com/tasnimzotder/int213-word-hunt-game/
Readme: https://github.com/tasnimzotder/int213-word-hunt-game/blob/master/README.md
"""

import string
import random
import tkinter as tk
from tkinter import ttk
import yaml
import gameUtils as gutils
import os

root = tk.Tk()
root.title("INT213 - Word Hunt Game")
root.iconbitmap(os.path.join(os.getcwd(), 'icons', 'x-48.ico'))

pressedWord = ''
prev = [0, 0]
route = [0, 0]

# ***************> Game Starts <******************


def gameHeader():
    game_header = tk.Frame(root)
    game_header.pack(fill=tk.X, side=tk.TOP)

    heading = tk.Label(game_header,
                       text='Word Hunt Game',
                       font=('Helvetica', 23, 'bold'),
                       fg='#313a57')
    heading.pack(expand=True, fill=tk.X, pady=12)


def gameFooter():
    game_footer = tk.Frame(root)
    game_footer.pack(fill=tk.X, side=tk.BOTTOM, pady=12)
    # gh_link_text = r'https://github.com/tasnimzotder/int213-word-hunt-game'

    footer = tk.Label(
        game_footer,
        text=
        '© Tasnim Zotder, Souvik Ghoshal, Fizan Naik | 2020\nhttps://github.com/tasnimzotder/int213-word-hunt-game',
    )
    footer.pack(expand=True, fill=tk.X, pady=0)


def startGame():
    frame1 = tk.Frame(master=root, bg="red")
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=20, pady=12)

    frame2 = tk.Frame(master=root)
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, padx=10, pady=12)

    configFile = gutils.readConfigFile()
    levelNum = configFile['player']['level']
    levelDetails = [
        configFile['levels'][levelNum]['name'],
        configFile['levels'][levelNum]['words']
    ]
    currScore = tk.StringVar()
    currScore.set(0)

    def updateScore():
        configFile = gutils.readConfigFile()
        score = configFile['player']['score']
        configFile['player']['score'] = score + 1
        currScore.set(score + 1)
        gutils.writeConfigFile(configFile)
        root.update_idletasks()

    # bg="#70889c"
    frame3 = tk.Frame(master=root)
    frame3.pack(fill=tk.BOTH, side=tk.RIGHT, padx=20, pady=30)

    labelWelcome = tk.Label(master=frame3,
                            text="Welcome",
                            fg='#2c334a',
                            font=('Helvetica', 12)).grid(row=0, column=0)

    labelWName = tk.Label(master=frame3,
                          text=configFile['player']['name'],
                          fg='#2c334a',
                          font=('Helvetica', 12, 'bold')).grid(row=0, column=1)

    labelLevelLbl = tk.Label(master=frame3,
                             text="Level",
                             fg='#2c334a',
                             font=('Helvetica', 12)).grid(row=1, column=0)

    labelLevel = tk.Label(master=frame3,
                          text=levelDetails[0],
                          fg='#2c334a',
                          font=('Helvetica', 12, 'bold')).grid(row=1, column=1)

    labelLevelLbl = tk.Label(master=frame3,
                             text="Words",
                             fg='#2c334a',
                             font=('Helvetica', 12)).grid(row=2, column=0)

    labelLevel = tk.Label(master=frame3,
                          text=levelDetails[1],
                          fg='#2c334a',
                          font=('Helvetica', 12, 'bold')).grid(row=2, column=1)

    labelLevelLbl = tk.Label(master=frame3,
                             text="Score",
                             fg='#2c334a',
                             font=('Helvetica', 12)).grid(row=3, column=0)

    labelLevel = tk.Label(master=frame3,
                          textvariable=currScore,
                          fg='#2c334a',
                          font=('Helvetica', 12, 'bold')).grid(row=3, column=1)
    wordList = []

    with open(r'data/words.yaml') as file:
        wordFile = yaml.load(file, Loader=yaml.FullLoader)
        wordList = [word for word in wordFile['words']]

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
            updateScore()
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
            # print(prev)
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
                       bg="#70889c",
                       font=('Helvetica', 10),
                       fg='white',
                       command=checkWord)
    checkW.grid()


def main():
    gameHeader()

    frame = tk.Frame(root)
    frame.pack(pady=56, padx=180)

    def updateUserInput():
        username = userNameField.get()
        gutils.gameLevel(str(levelInpCombo.get()), str(userNameField.get()))
        startGame()
        frame.destroy()

    tk.Label(frame, text="Name", font=('Helvetica', 15),
             fg='#456263').grid(row=0, padx=10, pady=6)
    userNameField = tk.Entry(frame)
    userNameField.grid(row=0, column=1, ipady=6, ipadx=10)

    tk.Label(frame, text="Game Level", font=('Helvetica', 15),
             fg='#456263').grid(row=1)
    levelInpCombo = ttk.Combobox(frame,
                                 values=['Mini', 'Normal', 'Pro', 'Pro Max'])
    levelInpCombo.grid(row=1, column=1, ipady=6, ipadx=10)
    levelInpCombo.current(0)

    tk.Button(frame,
              text="Start Game",
              font=('Helvetica', 12),
              bg='#70889c',
              fg='white',
              command=updateUserInput).grid(row=3,
                                            column=1,
                                            pady=8,
                                            ipady=6,
                                            ipadx=10)

    gameFooter()
    root.mainloop()


if __name__ == '__main__':
    main()
