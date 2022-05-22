from utils.send_files import send_files


class Observable:
    def __init__(self, state=None):
        self.subscribers = []
        self.state = state

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, new_state=None, file_ip=""):
        self.state = new_state
        for subscriber in self.subscribers:
            if (file_ip != subscriber[1]):
                send_files(subscriber[0], [self.state])
