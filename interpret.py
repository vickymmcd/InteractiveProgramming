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
	def __init__(self, other, prior, question, answer):
		#self.earthquake = earthquake
		self.data = other
		self.prior = prior
		#self.commas = commas
		self.question = question
		self.answer = answer
		self.question_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
		self.age_list = ['18 - 29', '30 - 44', '45 - 59', '60']
		self.location_list = ['East North Central', 'East South Central', 'Middle Atlantic', 
			'Mountain', 'New England', 'Pacific', 'South Atlantic', 'West North Central', 'West South Central']

	def total_responses_with_file(self, reset=False):
		"""
		Tallies up the total responses of the data
		"""
		total = 0
		for i in self.question_list:
			for j in self.age_list:
				for l in self.location_list:
					result = self.data.get_data(l, j, i)
					for x in result:
						total += result[x]


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


	def bayesian_single_factor(self, question, answer):
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
			

	def dictionary_of_qa(self):
		dic_of_qa = {}
		for l in self.location_list:
			for a in self.age_list:
				for q in self.question_list:
					result = self.data.get_data(l, a, q)
					if q not in dic_of_qa:
						dic_of_qa[q] = []
					for answer in result:
						if answer not in dic_of_qa[q]:
							dic_of_qa[q].append(answer)
		return(dic_of_qa)

						
	def bayesian_factors(self, file_name):

		prev_factors = self.dictionary_of_qa()
		new_factors = {}
		for q in prev_factors:
			for a in prev_factors[q]:
				if q not in new_factors:
					new_factors[q] = {}
				new_factors[q][a] = self.bayesian_single_factor(q, a)
		
		if exists(file_name) and reset == False:
			return(load(open(file_name,'rb+')))
		else:
			f = open(file_name, 'wb')
			dump(new_factors, f)
			f.close()
			return(load(open(file_name, 'rb')))



	def bayesian_update(self):
		"""
		Updates a prior probabilities with posterior probabilities using Bayesian
		"""
		factors = load(open('bayesian_factors.txt', 'rb+'))
		list_of_factors = []
		for i in factors[self.question][self.answer]:
			list_of_factors.append(factors[self.question][self.answer][i])

		product = []
		j = 0
		while j<len(list_of_factors):
			prd = list_of_factors[j] * self.prior[j]
			product.append(prd)
			j += 1

		total = 0
		for l in product:
			total += l

		posterior = []
		for k in product:
			posterior.append(k/total)

		sum_of_posterior = sum(posterior)
		return(sum_of_posterior)
		


data = Data('earthquake')
prior = [0.02777] * 36
question = 0
answer = "Somewhat worried"
newdictionary = Interpret(data, prior, question, answer)

print(newdictionary.bayesian_update())






