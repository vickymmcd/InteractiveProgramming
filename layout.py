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
from bokeh.io import curdoc


class Layout:
    def __init__(self, question_index, interpret, data, data_type, age_probs,
                 region_probs):
        self.map = Map()
        self.ageline = AgeLine()
        self.scaleline = ScaleLine()
        self.question_index = question_index
        self.data_type = data_type
        self.question = Question(question_index, interpret, data, data_type)
        self.possible_answers = self.question.get_list_answers(self.question.get_fig()[1])
        self.layout = row(column(self.map.get_fig(region_probs),
                                 self.ageline.get_fig(age_probs),
                                 self.scaleline.get_fig()),
                          column(self.question.get_fig()[0],
                                 self.question.get_button()))

    def show_layout(self):
        output_file('layout.html')
        show(self.layout)

    def show_list_answers(self):
        return([self.possible_answers, self.question_index])

    def get_layout(self):
        curdoc().add_root(self.layout)
        return self.layout

"""
data = Data('comma')
prior = [0.02777] * 36
newdictionary1 = Interpret(data, prior, 2, "No", "comma")
layout = Layout(1, newdictionary1, "comma", data, [.25, .25, .25, .25],
                [0, .11, .11, .11, .11, .11, .11, .11, .11, .11])
layout.get_layout()
"""

