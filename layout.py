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
    def __init__(self, question_index, interpret, data, data_type, age_probs,
                 region_probs):
        self.map = Map()
        self.ageline = AgeLine()
        self.scaleline = ScaleLine()
        self.question = Question(question_index, interpret, data, data_type)
        self.layout = row(column(self.map.get_fig(region_probs),
                                 self.ageline.get_fig(age_probs),
                                 self.scaleline.get_fig()),
                          column(self.question.get_fig(),
                                 self.question.get_button()))

    def show_layout(self):
        output_file('layout.html')
        show(self.layout)


if __name__ == '__main__':
    data = Data('comma')
    prior = [0.02777] * 36
    '''newdictionary1 = Interpret(data, prior, 2, "No", "comma",
                               [.25, .25, .25, .25], [0, .11, .11, .11, .11,
                                                      .11, .11, .11, .11, .11])
    layout = Layout(1, newdictionary1, "comma", data)'''
    newdictionary1 = Interpret(data, prior, 2, "No", "comma")
    layout = Layout(1, newdictionary1, "comma", data, [.25, .25, .25, .25],
                    [0, .11, .11, .11, .11, .11, .11, .11, .11, .11])
    layout.show_layout()
