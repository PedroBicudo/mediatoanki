import abc


class File(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def write_at(self, name, destination):
        pass
