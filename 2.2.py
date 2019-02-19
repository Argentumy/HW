import time
import pprint


class FileOpener:
    start = 0
    end = 0

    def __init__(self, file_path):
        self.start = time.perf_counter_ns()
        print(f'Время начала выполнения кода: {self.start}ns')
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.end = time.perf_counter_ns()
        print(f'Время окончания выполнения кода: {self.end}ns')
        print(f'Время выполнения кода: {self.end - self.start}ns')


if __name__ == '__main__':
    with FileOpener('test1') as file:
        x = set(file.file.read().split(sep='\n'))
        print(x)
