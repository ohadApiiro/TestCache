
class MainClass:
    def __init__(self):
        self.name = "yo"

    def hello(self):
        print(self.name)


def main():
    m = MainClass()
    m.hello()


if __name__ == '__main__':
    main()
