class Observer:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f'{self.name} received this message: {message}')
