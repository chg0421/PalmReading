from abc import ABCMeta, abstractmethod


class Palm(metaclass=ABCMeta):
    @abstractmethod
    def sort_line(self):
        pass

    @abstractmethod
    def straight_line(self):
        pass

    @abstractmethod
    def chain_line(self):
        pass

    @abstractmethod
    def hard_line(self):
        pass


class Head(Palm):
    def sort_line(self):
        print("Fast Thinker")

    def straight_line(self):
        print("Analyze much")

    def chain_line(self):
        print("Sensitive to others")

    def hard_line(self):
        print("Creative")


class Heart(Palm):
    def sort_line(self):
        print("Rational")

    def straight_line(self):
        print("You need your freedom")

    def chain_line(self):
        print("You prefer small groups")

    def hard_line(self):
        print("Emotional")


class Life(Palm):
    def sort_line(self):
        print("Keeping busy helps you safe and secure")

    def straight_line(self):
        print("You may need to chilout now and then")

    def chain_line(self):
        print("Face traumatic experience")

    def hard_line(self):
        print("Keep busy")


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
    if x == "head":
            print("Fortune for HEAD line")
            x = Head()
    elif x=="heart":
        print("Fortune for Heart line")
        x = Heart()
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