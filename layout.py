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
from decimal import *


class Layout:
    def __init__(self, question_index, interpret, data, data_type):
        self.map = Map()
        self.ageline = AgeLine()
        self.scaleline = ScaleLine()
        self.question = Question(question_index, interpret, data, data_type)
        self.priors = [3] * 36
        self.region_probs = [0, 11, 11, 11, 11, 11, 11, 11, 11, 11]
        self.region_names = ['Unknown', 'East North Central',
                             'East South Central', 'Middle Atlantic',
                             'Mountain', 'New England', 'Pacific',
                             'South Atlantic', 'West North Central',
                             'West South Central']
        self.age_names = [' 18 - 29', ' 30 - 44', ' 45 - 59', ' 60']
        self.age_probs = [25, 25, 25, 25]
        # self.update()
        self.layout = row(column(self.map.get_fig(self.region_probs),
                                 self.ageline.get_fig(self.age_probs),
                                 self.scaleline.get_fig()),
                          column(self.question.get_fig(),
                                 self.question.get_button()))

    def show_layout(self):
        output_file('layout.html')
        show(self.layout)

    def get_layout(self):
        curdoc().add_root(self.layout)
        return self.layout

    def update(self):
        self.update_stuff(3, 'Some', 'comma')

    def update_stuff(self, ques_num, response, data_type):
        data = Data(data_type)
        interpret = Interpret(data, self.priors, ques_num, response, data_type)
        self.priors = interpret.bayesian_update()
        region1_probs = 0
        region2_probs = 0
        region3_probs = 0
        region4_probs = 0
        region5_probs = 0
        region6_probs = 0
        region7_probs = 0
        region8_probs = 0
        region9_probs = 0
        age1_probs = 0
        age2_probs = 0
        age3_probs = 0
        age4_probs = 0
        for i in range(len(self.priors)):
            if interpret.get_location(i) == self.region_names[1]:
                region1_probs += int(self.priors[i] * 100)
            elif interpret.get_location(i) == self.region_names[2]:
                region2_probs += int(self.priors[i] * 100)
            elif interpret.get_location(i) == self.region_names[3]:
                region3_probs += int(self.priors[i] * 100)
            elif interpret.get_location(i) == self.region_names[4]:
                region4_probs += int(self.priors[i] * 100)
            elif interpret.get_location(i) == self.region_names[5]:
                region5_probs += int(self.priors[i] * 100)
            elif interpret.get_location(i) == self.region_names[6]:
                region6_probs += int(self.priors[i] * 100)
            elif interpret.get_location(i) == self.region_names[7]:
                region7_probs += int(self.priors[i] * 100)
            elif interpret.get_location(i) == self.region_names[8]:
                region8_probs += int(self.priors[i] * 100)
            elif interpret.get_location(i) == self.region_names[9]:
                region9_probs += int(self.priors[i] * 100)
            if interpret.get_age(i) == self.priors[0]:
                age1_probs += int(self.priors[i] * 100)
            elif interpret.get_age(i) == self.age_names[1]:
                age2_probs += int(self.priors[i] * 100)
            elif interpret.get_age(i) == self.age_names[2]:
                age3_probs += int(self.priors[i] * 100)
            elif interpret.get_age(i) == self.age_names[3]:
                age4_probs += int(self.priors[i] * 100)
        self.region_probs = [0, region1_probs, region2_probs, region3_probs,
                             region4_probs, region5_probs, region6_probs,
                             region7_probs, region8_probs, region9_probs]
        self.age_probs = [age1_probs, age2_probs, age3_probs, age4_probs]
        self.layout = row(column(self.map.get_fig(self.region_probs),
                                 self.ageline.get_fig(self.age_probs),
                                 self.scaleline.get_fig()),
                          column(self.question.get_fig(),
                                 self.question.get_button()))


data = Data('comma')
prior = [3] * 36
newdictionary1 = Interpret(data, prior, 2, "No", "comma")
layout = Layout(1, newdictionary1, "comma", data)
layout.get_layout()
