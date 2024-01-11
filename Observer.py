class Observer:
    def update(self, message):
        raise NotImplementedError("You must implement the update method.")


class ConcreteObserver(Observer):
    def __init__(self, observer_name):
        self.observer_name = observer_name

    def update(self, message):
        print(f"{self.observer_name} received message: {message}")


class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)


if __name__ == "__main__":
    subject = Subject()

    # creating observers
    observer1 = ConcreteObserver("Observer1")
    observer2 = ConcreteObserver("Observer2")

    # registering observers
    subject.register_observer(observer1)
    subject.register_observer(observer2)

    # subject changes state and notifies observers
    subject.notify_observers("First notification")

    # remove an observer
    subject.remove_observer(observer1)

    # subject changes state and notifies remaining observers
    subject.notify_observers("Second notification")
