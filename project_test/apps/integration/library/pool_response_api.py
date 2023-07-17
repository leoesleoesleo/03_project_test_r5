import threading
import time


class PoolResponse:
    def __init__(self):
        self.data = {}
        self.lock = threading.Lock()

        self.start_cleanup_timer()

    def start_cleanup_timer(self):
        cleanup_thread = threading.Thread(target=self.cleanup_timer)
        cleanup_thread.daemon = True
        cleanup_thread.start()

    def cleanup_timer(self):
        while True:
            time.sleep(1000)
            self.cleanup()

    def cleanup(self):
        with self.lock:
            current_time = time.time()
            keys_to_remove = []

            for key, value in self.data.items():
                if value['timestamp'] + 600 < current_time:
                    keys_to_remove.append(key)

            for key in keys_to_remove:
                del self.data[key]

    def add_data(self, key, value):
        with self.lock:
            self.data[key] = {'value': value, 'timestamp': time.time()}

    def get_data(self, key):
        with self.lock:
            return self.data.get(key, {}).get('value')
