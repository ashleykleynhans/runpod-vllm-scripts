import time
from dotenv import dotenv_values


class Timer:
    def __init__(self):
        self.start = time.time()

    def restart(self):
        self.start = time.time()

    def get_elapsed_time(self):
        end = time.time()
        return round(end - self.start, 1)


env = dotenv_values('.env')
RUNPOD_API_KEY = env.get('RUNPOD_API_KEY', None)
RUNPOD_ENDPOINT_ID = env.get('RUNPOD_ENDPOINT_ID', None)
MODEL = env.get('MODEL', None)
