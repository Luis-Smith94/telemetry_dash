"""
Abstact class for Subjects
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from threading import Thread

from decoder import ForzaDecoder
from observer import IObserver
from udp.receiver import UdpReceiver

class ISubject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    def __init__(self):
        pass

    @abstractmethod
    def attach(self, observer: IObserver):
        """
        Attach an observer to the subject.
        """

    @abstractmethod
    def detach(self, observer: IObserver):
        """
        Detach an observer from the subject.
        """

    @abstractmethod
    def notify(self):
        """
        Notify all observers about an event.
        """

    @abstractmethod
    def get_metrics(self, topic: str) -> dict:
        """
        return the metrics associated to given topic
        """


class ForzaMetrics(ISubject):
    """
    The Subject that owns the metrics from Forza Motorsport
    """

    _metrics: dict
    """
    Data containing every metrics send by the game Forza Motorsport. Keys are
    """

    _observers: list
    """
    List of subscribers
    """

    _receiver: UdpReceiver
    """
    Object in charge of listening and receiving udp packets from the game Forza Motorsport.
    """

    _decoder: ForzaDecoder

    def __init__(self, conf: dict):
        super()
        self._metrics = {}
        self._observers = []
        self._conf = conf
        self._receiver = UdpReceiver(self._conf["receiver"])
        self._decoder = ForzaDecoder(self._conf["decoder"])

    def attach(self, observer: IObserver):
        """
        Add a new observer
        """
        print(f"ForzaMetrics Subject: Attached an observer for topic \
              {observer.get_topic()}")
        self._observers.append(observer)

    def detach(self, observer: IObserver):
        """
        Remove the observer
        """
        self._observers.remove(observer)

    def notify(self):
        """
        Notify all observers about an event.
        """
        for observer in self._observers:
            observer.update(self._metrics[observer.get_topic()])

    def get_metrics(self, topic: str) -> dict:
        """
        return the metrics associated to given topic
        """
        return self._metrics.get(topic)

    def run(self):
        """
        Run the thread for main loop
        """
        t = Thread(target=self.main_loop)
        t.start()

    def main_loop(self) -> None:
        """
        Implement business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """
        print("ForzaMetrics::main_loop")
        while True:
            self._metrics = self._decoder.decode(self._receiver.listen())
            self.notify()
