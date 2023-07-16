from abc import ABC, abstractmethod
import json


class FileReader(ABC):
    @abstractmethod
    def read_data(self, filename):
        pass


class FileWriter(ABC):
    @abstractmethod
    def write_data(self, filename, data):
        pass


class JsonFileReader(FileReader):
    def read_data(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data


class JsonFileWriter(FileWriter):
    def write_data(self, filename, data):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file)
