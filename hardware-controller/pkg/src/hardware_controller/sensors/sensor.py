import abc

from ..device import HardwareDevice


class Sensor(HardwareDevice, metaclass=abc.ABCMeta):
    pass
