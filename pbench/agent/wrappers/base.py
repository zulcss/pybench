import abc


class BaseCommand:
    @abc.abstractmethod
    def run(self):
        raise NotImplementedError
