#Chapter 10 hangman

def hangman(word):
    wrong = 0
    stages = ["",
              "_________          ",
              "|                  ",
              "|        |         ",
              "|        0         ",
              "|       /|\        ",
              "|       / \        ",
              "|                  "]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ")
    count = 1
    while wrong < len(stages) - 1:
        print("\n")
        msg = "{}文字めを予想してね！".format(count)
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            count += 1
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち!!!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け!正解は{}.".format(word))

import random
wordlist = ["cat", "dog", "hedgehog", "cow"]
l = random.randint(0,3)
hangman(wordlist[l])
                        
