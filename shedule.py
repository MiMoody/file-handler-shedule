import time
from shedule_class import FileShedule
from watchdog.observers import Observer

path_to_file = r"./file.txt"
event_handler = FileShedule(path_to_file)
observer = Observer()
observer.schedule(event_handler, path=path_to_file, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()