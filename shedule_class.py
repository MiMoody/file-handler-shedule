from watchdog.events import FileSystemEventHandler
from utils import FileReader


class FileShedule(FileSystemEventHandler):
    
    def __init__(self, file_path) -> None:
        self._file_path = file_path
    
    def on_any_event(self, event):
        """ Любое событие """
        pass
        # print(event.event_type, event.src_path)

    def on_created(self, event):
        pass
    
    def on_deleted(self, event):
        pass

    def on_modified(self, event):
        if(event.src_path == self._file_path):
            last_line = FileReader.last_line(self._file_path)
            print("Last line in file: ", last_line)

    def on_moved(self, event):
        pass