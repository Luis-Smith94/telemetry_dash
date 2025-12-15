"""
Abstact class for Observers
"""
from abc import ABC, abstractmethod

from plot import Plot


class IObserver(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, raw_value) -> None:
        """
        Receive update from subject.
        """

    @abstractmethod
    def get_topic(self) -> str:
        """
        Get the topic associated to the Observer
        """

class AccelObserver(IObserver):
    """
    Observer for the throtlle percentage data, named Accel
    """

    _topic:str
    """
    Key associated to the relevent data in the subject _buffer
    """

    def __init__(self, plot: Plot):
        self._topic = "Accel"
        self._plot = plot
        self._plot.add_subplot(self._topic)

    def update(self, raw_value) -> None:
        """
        Method called for treating the new value of the subject
        """
        new_value = raw_value * 100 / 255
        self._plot.push_data(self._topic, new_value)

    def get_topic(self) -> str:
        """
        Get the topic associated to the Observer
        """
        return self._topic

class BrakeObserver(IObserver):
    """
    Observer for the throtlle percentage data, named Accel
    """

    _topic:str
    """
    Key associated to the relevent data in the subject _buffer
    """

    def __init__(self, plot: Plot):
        self._topic = "Brake"
        self._plot = plot
        self._plot.add_subplot(self._topic)

    def update(self, raw_value) -> None:
        """
        Method called for treating the new value of the subject
        """
        new_value = raw_value * 100 / 255
        self._plot.push_data(self._topic, new_value)

    def get_topic(self) -> str:
        """
        Get the topic associated to the Observer
        """
        return self._topic

class TimeObserver(IObserver):
    """
    Observer for the throtlle percentage data, named Accel
    """

    _topic:str
    """
    Key associated to the relevent data in the subject _buffer
    """

    def __init__(self, plot: Plot):
        self._topic = "CurrentRaceTime"
        self._plot = plot

    def update(self, raw_value) -> None:
        """
        Method called for treating the new value of the subject
        """
        self._plot.push_time(raw_value)

    def get_topic(self) -> str:
        """
        Get the topic associated to the Observer
        """
        return self._topic
