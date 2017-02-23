'''
Authors: Vicky McDermott and Emily Lepert
'''


class Data:
    def __init__(self, type):
        self.type = type

    def get_question(self, number):
        if self.type == 'earthquake':
            f = open('earthquake_data.csv')
            lines = f.readlines()
            lines[0].strip('"')
            ques = [line.strip('"') for line in lines[0].split('","')]
            print(ques[number])
