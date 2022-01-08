import requests
from bs4 import BeautifulSoup
import re
from time import sleep
from random import randint


class Request:
    def __init__(self):
        self.url = None

    def send_request(self):
        return requests.get(self.url)


class ResponseHandler(Request):
    def __init__(self):
        super().__init__()
        self.response = None
        self.soup = None
        self.text = None
        self.temp_list = []

    def get_text(self):
        self.soup = BeautifulSoup(self.response.text, 'lxml')
        self.text = self.soup.get_text()[579:]

    def take_names(self):
        self.get_text()
        self.text = re.findall(r'\w+', self.text)
        for i in range(len(self.text)):
            if i % 2 == 0:
                self.temp_list.append(self.text[i])
        return self.temp_list


class DataFormatting:
    def __init__(self, requested_length, data):
        self.length = requested_length
        self.data = data

    def length_reduction(self):
        if len(self.data) < self.length:
            print('Error: Not enough data!')
            exit(1)
        self.data = self.data[:self.length]

    def list_sorting(self):
        self.data.sort()


class NamesParser(ResponseHandler):
    def __init__(self, output_names_number):
        super().__init__()

        self.output_names_number = output_names_number
        self.temp_output_names_number = self.output_names_number
        self.requested_names_numbers = []

        self.array = []
        self.data_formatting = None

    def base_condition_for_requested_names_numbers_generator(self):
        if self.temp_output_names_number < 10:
            self.requested_names_numbers.append(10)
        elif self.temp_output_names_number < 25:
            self.requested_names_numbers.append(25)
        elif self.temp_output_names_number < 50:
            self.requested_names_numbers.append(50)
        elif self.temp_output_names_number < 100:
            self.requested_names_numbers.append(100)

    def requested_names_numbers_generator(self):
        if self.temp_output_names_number <= 0:
            print('Error: "output_names_number" value must be greater than 0!')
            exit(1)
        elif self.temp_output_names_number <= 100:
            self.base_condition_for_requested_names_numbers_generator()
        else:
            self.temp_output_names_number = self.output_names_number // 100
            _ = [self.requested_names_numbers.append(100) for i in range(self.temp_output_names_number)]
            self.temp_output_names_number = self.output_names_number - self.temp_output_names_number * 100
            self.base_condition_for_requested_names_numbers_generator()

    def take_unformatted_data(self):
        self.requested_names_numbers_generator()
        for i in range(len(self.requested_names_numbers)):
            sleep(randint(0, 2))
            self.url = f'http://random-name-generator.info/index.php?n={self.requested_names_numbers[i]}&g=1&st=1'
            self.response = self.send_request()
            self.array = self.array + self.take_names()

    def format_data(self):
        self.data_formatting = DataFormatting(self.output_names_number, self.array)
        self.data_formatting.length_reduction()
        self.data_formatting.list_sorting()
        self.array = self.data_formatting.data

    def parse(self):
        self.take_unformatted_data()
        self.format_data()
        return self.array
