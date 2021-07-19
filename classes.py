#
# Example file for working with classes
#

class myClass():
    def func1(self):
        print("myClass func1")

    def func2(self, someString):
        print("myClass func2 " + someString)


class secondClass():
    def func2(self):
        print("secondClass func2")

    def func1(self):
        myClass.func1(self)
        print("secondClass func1")


def main():
    c = myClass()
    c.func1()
    c.func2("This is a string")
    c2 = secondClass()
    c2.func1()


if __name__ == "__main__":
    main()
