import time
import threading
from datetime import timedelta

from config import WAIT_TIME_SECONDS, MAX_RUN_TIME
from utils import random_writer


class FileWriter:
    """
        File Writer class to start a writer thread for continues writing at given intervals
    """
    def __init__(self):
        self.wait_time = WAIT_TIME_SECONDS

    def start_writer(self):
        job = WriterJob(interval=timedelta(seconds=self.wait_time), execute=random_writer)
        job.start()
        start_time = time.time()
        print('Random Writer started!')

        try:
            while True:
                time.sleep(1)
                if time.time() - start_time > MAX_RUN_TIME:
                    print("File writer stopped!")
                    job.stop()
                    break
        except KeyboardInterrupt:
            print("File writer killed!")
            job.stop()

class WriterJob(threading.Thread):
    def __init__(self, interval, execute, *args, **kwargs):
        threading.Thread.__init__(self)
        self.daemon = False
        self.stopped = threading.Event()
        self.interval = interval
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

    def stop(self):
        self.stopped.set()
        self.join()

    def run(self):
        while not self.stopped.wait(self.interval.total_seconds()):
            self.execute(*self.args, **self.kwargs)


if __name__ == "__main__":
    writer_obj = FileWriter()
    writer_obj.start_writer()
