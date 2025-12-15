"""
Main script
"""

# Standard imports
from sys import argv

# Third parts imports
from json import load
from matplotlib import pyplot

# Projects imports
from observer import AccelObserver, BrakeObserver, TimeObserver
from subject import ForzaMetrics
from plot import Plot

CONF_PATH = "res/conf/conf.json"

def get_conf_path(args: list):
    """
    Détermine le chemin vers la configuration à charger
    
    :param args: Arguments du programme
    :type args: list
    """
    if len(args) == 1:
        return CONF_PATH

    return args[1]


if __name__ == "__main__":
    conf = {}
    with open(get_conf_path(argv), mode="r", encoding="UTF-8") as json_file:
        conf = load(json_file)["forza_metrics"]
    print(conf)
    metrics = ForzaMetrics(conf)
    forza_plot = Plot(conf["plots"])
    time_observer = TimeObserver(forza_plot)
    accel_observer = AccelObserver(forza_plot)
    brake_observer = BrakeObserver(forza_plot)
    metrics.attach(time_observer)
    metrics.attach(accel_observer)
    metrics.attach(brake_observer)
    metrics.run()
    pyplot.show()
