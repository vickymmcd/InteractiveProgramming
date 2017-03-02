''' 
Authors: Emily Lepert and Vicky McDermott

The Interpret class will take in the answer to a question and update
the probability that someone is from a region and their age based on that response
'''
from data import Data
from os.path import exists
import sys
from pickle import dump, load

class Interpret:
	def __init__(self, other): #, commas, question, answer):
		#self.earthquake = earthquake
		self.data = other
		#self.commas = commas
		#self.question = question
		#self.answer = answer
		self.question_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
		self.age_list = ['18 - 29', '30 - 44', '45 - 59', '60']
		self.location_list = ['East North Central', 'East South Central', 'Middle Atlantic', 
			'Mountain', 'New England', 'Pacific', 'South Atlantic', 'West North Central', 'West South Central']

	def total_responses_with_file(self, reset=False):
		"""
		Tallies up the total responses of the data
		"""
		total = 0
		if exists('total.txt') and reset == False:
			return(load(open('total.txt','rb+')))
		else:
			for i in self.question_list:
				for j in self.age_list:
					for l in self.location_list:
						result = self.data.get_data(l, j, i)
						for x in result:
							total += result[x]

			f = open('total.txt', 'wb')
			dump(total, f)
			f.close()
			return(load(open('total.txt', 'rb')))

	def denominator_factor(self, question, answer):
		"""
		Finds the total number of people for each hypothesis (location - age combo)
		for a question
		"""
		denominator = {}
		value = 0
		for i in self.location_list:
			for j in self.age_list:
				specific_data = self.data.get_data(i, j, question)
				key = i + '; ' + j
				result = self.data.get_data(i, j, question)
				for answer in result:
					value += result[answer]
				denominator[key] = value
				value = 0
		return(denominator)


	def numerator_factor(self, question, answer):
		"""
		Finds the number of people for each hypothesis (location - age combo) and each answer to a question
		"""
		factor = {}
		for i in self.location_list:
			for j in self.age_list:
				key = i + '; ' + j
				result = self.data.get_data(i, j, question)
				if answer in result:
					value = result[answer]
					factor[key] = value
				else:
					factor[key] = 0
		return(factor)

	def bayesian_factor(self, question, answer):
		"""
		Given a piece of data (question and answer), create dictionary with corresponding
		P(D|H)
		H: string of location + age 
		ie: 'East North Central; 18 - 29'
		"""
		denominator = self.denominator_factor(question, answer)
		numerator = self.numerator_factor(question, answer)
		factor = {}
		for i in denominator:
			if denominator[i] != 0:
				factor[i] = float(numerator[i]/denominator[i])
		return(factor)

	def bayesian_update(self):
		"""
		Updates a prior probabilities with posterior probabilities using Bayesian
		"""
		dic1 = self.bayesian_factor(6, 'Somewhat familiar')


data = Data('earthquake')
newdictionary = Interpret(data)
newdictionary.bayesian_update()






