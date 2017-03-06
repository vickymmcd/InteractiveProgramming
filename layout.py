'''
Authors: Vicky McDermott and Emily Lepert

This function represents the visual Layout object.
'''
from bokeh.layouts import column, row
from ageline import AgeLine
from map import Map
from question import Question
from interpret import Interpret
from data import Data
from scaleline import ScaleLine
from bokeh.plotting import output_file, show


class Layout:
    def __init__(self, question_index, data, data_type):
        self.map = Map()
        self.ageline = AgeLine()
        self.scaleline = ScaleLine()
        self.question = Question(question_index, data, data_type)
        self.layout = row(column(self.map.get_fig([0, .11, .11, .11, .11,
                                               .11, .11, .11, .11, .11]),
                             self.ageline.get_fig([.25, .25, .25, .25]),
                             self.scaleline.get_fig()), self.question.get_fig())

    def show_layout(self):
        output_file('layout.html')
        show(self.layout)



if __name__ == '__main__':
    data = Data('comma')
    prior = [0.02777] * 36
    newdictionary1 = Interpret(data, prior, 2, "No", "comma")
    layout = Layout(1, newdictionary1, "comma")
    layout.show_layout()
