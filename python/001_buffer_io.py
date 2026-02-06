"""
Description: A buffer reader that flushes its content either when it reaches a certain size or after a specified time interval.
The buffer reader is designed to handle concurrent writes and ensure thread safety using locks.
It also uses a separate thread to monitor the time interval for flushing the buffer.
"""

from datetime import datetime
from threading import Event, Lock, Thread
from time import sleep


class BufferReader:
    def __init__(self, buffer_max_size: int = 10):
        self.buffer = ""
        self.buffer_max_size = buffer_max_size
        self.flush_interval_seconds = 5
        self.latest_flush_time: datetime | None = None

        self.lock = Lock()
        self.stop_event = Event()
        self.release_thread = Thread(target=self.release, daemon=True)

    def release(self):
        while not self.stop_event.is_set():
            with self.lock:
                if self.latest_flush_time is not None:
                    diff = datetime.now() - self.latest_flush_time
                    if diff.total_seconds() > self.flush_interval_seconds:
                        print("Flushing due to time interval")
                        self.flush()
            sleep(1)

    def flush(self):
        print(self.buffer)
        self.buffer = ""
        self.latest_flush_time = datetime.now()

    def write(self, data: str):
        with self.lock:
            buffer_size = len(self.buffer)
            ingest_size = min([self.buffer_max_size - buffer_size, len(data)])
            self.buffer += data[:ingest_size]
            if len(self.buffer) >= self.buffer_max_size:
                self.flush()

        if ingest_size < len(data):
            self.write(data[ingest_size:])

    def __enter__(self):
        self.release_thread.start()
        return self

    def __exit__(self, *_, **__):
        self.flush()
        self.stop_event.set()
        self.release_thread.join()


stream = [
    "HelloFromSarah",
    "World",
    "Saeed",
    "Saeed",
]
buffer_reader = BufferReader(buffer_max_size=7)
with buffer_reader:
    for data in stream:
        sleep(2)
        buffer_reader.write(data)
