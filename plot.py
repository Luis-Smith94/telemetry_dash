"""
Implementation of the class responsible for plot updates
"""

from matplotlib import pyplot, animation


class Plot:
    """
    Class responsible, for plot updates
    """

    def __init__(self, conf: dict):
        self._figure = pyplot.figure()
        self._time = []
        self._data = {}
        self._subplots = {}
        self._conf = conf
        self._ani = animation.FuncAnimation(
            self._figure,
            animate,
            fargs=(self._time, self._data, self._subplots, self._conf),
            interval=0.0001,
            cache_frame_data=False,
        )

    def add_subplot(self, data_title: str):
        """
        Create a new subplot for given data
        """
        idx = self._conf["default"]["idx"]
        if data_title in self._conf:
            idx = self._conf[data_title]["idx"]
        self._subplots[data_title] = self._figure.add_subplot(len(self._conf) - 1, 1, idx)
        self._subplots[data_title].set_ylabel(data_title)
        self._subplots[data_title].set_xlabel("Time")
        self._data[data_title] = []

    def push_data(self, data_title: str, data):
        """
        Append data in the corresponding list
        """
        self._data[data_title].append(data)

    def push_time(self, timestamp):
        """
        Append data in the corresponding list
        """
        self._time.append(timestamp)


def animate(i, time: list, data: dict, subplots: dict, conf: dict):
    """
    Plot animation callback
    """
    for data_label, data_value in data.items():
        subplot = subplots[data_label]
        color = conf["default"]["color"]
        if data_label in conf:
            subplot.set_ylim(conf[data_label]["ylim"][0], conf[data_label]["ylim"][1])
            color = conf[data_label]["color"]
        subplot.clear()
        subplot.plot(time, data_value, label=data_label, color=color)
