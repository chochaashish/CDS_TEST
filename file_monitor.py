import time
from watchdog.observers import Observer
from watchdog.events import RegexMatchingEventHandler

from config import KEYWORD_TO_COUNT, CURRENT_DIR, MAX_RUN_TIME
from utils import file_reader, count_word
from logger import Logger


class FileMonitor:
    """
        File Monitor class to monitor files system events in specified directory
    """
    def __init__(self):
        self.src_path = CURRENT_DIR

    def start_monitor(self):
        event_handler = Handler()
        observer = Observer()
        observer.schedule(event_handler, path=self.src_path, recursive=True)
        start_time = time.time()
        observer.start()
        print('File Monitor started!')
        try:
            while True:
                time.sleep(1)
                if time.time() - start_time > MAX_RUN_TIME:
                    print('File monitor stopped!')
                    observer.stop()
                    break
        except KeyboardInterrupt:
            print('File monitor Killed!')
            observer.stop()
        observer.join()


class Handler(RegexMatchingEventHandler):

    def __init__(self):
        # Set the patterns for RegexMatchingEventHandler
        RegexMatchingEventHandler.__init__(self, regexes=['^\.(/|\\\\)test.*\.log$'], ignore_directories=True)

    def on_modified(self, event):
        modified_content = file_reader(event.src_path)
        count = count_word(modified_content, KEYWORD_TO_COUNT)
        log_writer = Logger()
        log_writer.write_logs(f'In file: {event.src_path} Keyword count of {KEYWORD_TO_COUNT} is {count}')
        print('%s File modified  CDS count: %s' % (event.src_path, count))


if __name__ == "__main__":
    file_monitor = FileMonitor()
    file_monitor.start_monitor()
