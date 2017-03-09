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
from bokeh.client import push_session


class Layout:
    def __init__(self, question_index, interpret, data, data_type):
        '''
        Gathers the Map, AgeLine, ScaleLine, Question class layouts
        and combines them onto one document

        Attributes: map, ageline, scaleline, question, priors,
            region_probs, region_names, age_names, age_probs, layout
        '''
        self.map = Map()
        self.ageline = AgeLine()
        self.scaleline = ScaleLine()
        self.question = Question(question_index, interpret, data,
                                 data_type)
        self.priors = [.0278] * 36
        self.region_probs = [0, 11, 11, 11, 11, 11, 11, 11, 11, 11]
        self.region_names = ['Unknown', 'East North Central',
                             'East South Central', 'Middle Atlantic',
                             'Mountain', 'New England', 'Pacific',
                             'South Atlantic', 'West North Central',
                             'West South Central']
        self.age_names = [' 18 - 29', ' 30 - 44', ' 45 - 59', ' 60']
        self.age_probs = [25, 25, 25, 25]

        self.layout = row(column(self.map.get_fig(self.region_probs),
                                 self.ageline.get_fig(self.age_probs),
                                 self.scaleline.get_fig()),
                          column(self.question.get_fig()[0]))


    def get_layout(self):
        '''
        Creates the document and adds the layout to it
        '''
        curdoc().add_root(self.layout)

    def change_layout(self, new_question_index, interpret, new_data, new_data_type):
        '''
        Changes the question child based on the new question by accessing the question object
        '''
        self.question = Question(new_question_index, interpret,
                                 new_data_type, new_data)
        self.layout.children[1] = self.question.get_fig()[0]

    def final_layout(self, new_fig):
        '''
        This makes the final layout
        '''
        self.layout.children[1] = new_fig

    def update_visuals(self, ques_num, response, data_type):
        '''
        This function uses the interpret class to update
        the probabilities of the person who answered the question
        with a given response being from a certain location and age
        group. It updates self.region_probs and self.age_probs
        and updates the map and ageline appropriately.

        ques_num: number of question being answered
        response: the response from the user
        data_type: specifies whether it is a comma or earthquake question
        '''
        interpret = Interpret(self.priors, ques_num, response, data_type)
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
            # add all the probabilities that you are from a given location
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
            # add all the probabilities that you are from a given age group
            if interpret.get_age(i) == self.age_names[0]:
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
        self.map.update_map(self.region_probs)
        self.ageline.update_ageline(self.age_probs)

    def biggest_prob(self):
        '''
        For the final message, find the str version of the highest probability information
        '''
        biggest_age_prob = max(self.age_probs)
        age_index = self.age_probs.index(biggest_age_prob)
        biggest_age = self.age_names[age_index]
        biggest_loc_prob = max(self.region_probs)
        loc_index = self.region_probs.index(biggest_loc_prob)
        biggest_loc = self.region_names[loc_index]
        biggest_prob = str(biggest_age) + ' years old and from the ' + str(biggest_loc)
        return(biggest_prob)
