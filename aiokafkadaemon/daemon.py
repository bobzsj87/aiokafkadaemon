"""
aiokafkadaemon Daemon class
"""
import asyncio

from .worker import Worker


class Daemon:
    def __init__(self, test=False, worker=None):
        """

        :param test:
        :param worker:
        """
        args = {
            'testing': test,
        }
        self._worker = worker
        if not self._worker:
            self._worker = Worker(**args)

    def run(self):
        pass


def main():
    loop = asyncio.get_event_loop()
    daemon = Daemon()
    daemon.run()


if __name__ == '__main__':
    main()
