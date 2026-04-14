import abc

from ..device import HardwareDevice


class Actor(HardwareDevice, metaclass=abc.ABCMeta):
    pass
