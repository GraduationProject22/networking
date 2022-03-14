from send_files import send_files


class Observable:
    def __init__(self, state=None):
        self.subscribers = []
        self.state = state

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, new_state=None):
        self.state = new_state
        for subscriber in self.subscribers:
            send_files(subscriber, [self.state])
