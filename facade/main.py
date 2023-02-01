from typing import Protocol
from bots import RudeChatbot, PoliteChatbot


'''
A good explanation for facade:
Identification: Facade can be recognized in a class that has a simple interface,
but delegates most of the work to other classes.
Usually, facades manage the full life cycle of objects they use.
'''

class Chatbot(Protocol):
    def greet(self, name: str) -> str:
        raise NotImplementedError

    def thank(self) -> str:
        raise NotImplementedError

    def appologize(self) -> str:
        raise NotImplementedError

    def feature1(self) -> None:
        raise NotImplementedError

    def feature2(self) -> None:
        raise NotImplementedError

class Facade:
    def __init__(self, chatbot: Chatbot) -> None:
        self.chatbot = chatbot

    def say_hi(self, name: str) -> None:
        print(self.chatbot.greet(name))

    def error_occured(self) -> None:
        print('Error occured during runtime...')
        print(self.chatbot.appologize())

def main():
    active_bot = RudeChatbot()
    facade = Facade(active_bot)
    facade.say_hi(str(input('Your name: ')))
    facade.error_occured()


if __name__ == '__main__':
    main()