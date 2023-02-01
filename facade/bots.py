class PoliteChatbot:
    def greet(self, name: str) -> str:
        return f'Welcome good sir {name}!'

    def thank(self) -> str:
        return 'Thank you so much, sir!'

    def appologize(self) -> str:
        return 'I am truly sorry for that, sir.'

    def feature1(self) -> None:
        return None

    def feature2(self) -> None:
        return None

class RudeChatbot:
    def greet(self, name: str) -> str:
        return f'Oh, you again?'

    def thank(self) -> str:
        return 'About time!'

    def appologize(self) -> str:
        return 'Blame is all yours mate.'

    def feature1(self) -> None:
        return None

    def feature2(self) -> None:
        return None