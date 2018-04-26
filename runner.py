from Head import Head
from Heart import Heart
from Life import Life


def do_one(palm):
    palm.sort_line()


def do_two(palm):
    palm.straight_line()


def do_three(palm):
    palm.chain_line()


def do_four(palm):
    palm.hard_line()


if __name__ == "__main__":

    x = (input("Enter the type of line >>>"+'\n'))
    if x == "Head":
        print("Fortune for HEAD line")
        x = Head()
        y = (input("Enter Short/Straight/Hard  >>> " + '\n'))
        if y == "Short":
            do_one(x)
        elif y == "Straight":
            do_two(x)
        elif y == "Chain":
            do_three(x)
        elif y == "Hard":
            do_four(x)
    elif x == "Life":
        print("Fortune for Life line")
        x = Life()
        y = (input("Enter Short/Straight/Hard  >>> " +'\n'))
        if y == "Short":
            do_one(x)
        elif y == "Straight":
            do_two(x)
        elif y == "Chain":
            do_three(x)
        elif y == "Hard":
            do_four(x)
    elif x == "Heart":
        print("Fortune for Heart line")
        x = Heart()
        y = (input("Enter Short/Straight/Hard  >>> " + '\n'))
        if y == "Short":
            do_one(x)
        elif y == "Straight":
            do_two(x)
        elif y == "Chain":
            do_three(x)
        elif y == "Hard":
            do_four(x)