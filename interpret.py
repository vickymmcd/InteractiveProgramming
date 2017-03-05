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
	def __init__(self, data, prior, question, answer, data_type):
		#self.earthquake = earthquake
		self.data_type = data_type
		self.data = data
		self.prior = prior
		#self.commas = commas
		self.question = question
		self.answer = answer
		self.question_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
		self.age_list = ['18 - 29', '30 - 44', '45 - 59', '60']
		self.location_list = ['East North Central', 'East South Central', 'Middle Atlantic', 
			'Mountain', 'New England', 'Pacific', 'South Atlantic', 'West North Central', 'West South Central']

	def key_creator(self):
		key_list = []
		for i in self.location_list:
			for j in self.age_list:
				key = i+'; '+j
				key_list.append(key)
		return(key_list)

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
		if self.data_type != 'earthquake':
			self.data_type = self.data_type[1:]

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

						
	def bayesian_factors(self, file_name, reset=False):

		prev_factors = self.dictionary_of_qa()
		new_factors = {}
		for q in prev_factors:
			for a in prev_factors[q]:
				if self.data_type == 'earthquake':
					if a == '"Yes, one or more minor ones"':
						a1 = 'Yes, one or more minor ones'
					elif a == '"Yes, one or more major ones"':
						a1 = 'Yes, one or more major ones'
					elif a == '"$50,000 to $74,999"':
						a1 = '$50,000 to $74,999'
					elif a == '"$0 to $9,999"':
						a1 = '$0 to $9,999'
					elif a == '"$25,000 to $49,999"':
						a1 = '$25,000 to $49,999'
					elif a == '"$10,000 to $24,999"':
						a1 = '$10,000 to $24,999'
					elif a == '"$100,000 to $124,999"':
						a1 = '$100,000 to $124,999'
					elif a == '"$75,000 to $99,999"':
						a1 = '$75,000 to $99,999'
					elif a == '"$125,000 to $149,999"':
						a1 =  '$125,000 to $149,999'
					elif a == '"$200,000 and up"':
						a1 = '$200,000 and up'
					elif a == '"$150,000 to $174,999"':
						a1 = '$150,000 to $174,999'
					elif a == '"$175,000 to $199,999"':
						a1 = '$175,000 to $199,999'
					else:
						a1 = a
				if q not in new_factors:
					new_factors[q] = {}
				new_factors[q][a1] = self.bayesian_single_factor(q, a)
		
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
		#self.bayesian_factors('earthquake_factors.txt')
		if self.data_type != 'earthquake':
			self.question_list = self.question_list[1:]
			factors = load(open('comma_factors.txt'))
		else:
			factors = load(open('earthquake_factors.txt', 'rb+'))
		print(factors)
		list_of_factors = []
		for i in factors[self.question][self.answer]:
			list_of_factors.append(factors[self.question][self.answer][i])
		

		product = []
		j = 0
		while j<len(list_of_factors):
			prd = list_of_factors[j] * self.prior[j]
			product.append(prd)
			j += 1
		print('\n')
		total = 0
		for l in product:
			total += l

		posterior = []
		for k in product:
			if total != 0:
				posterior.append(k/total)
			else:
				posterior.append(0)

		return(posterior)

	def biggest_probability(self):
		posterior = self.bayesian_update()
		maximum = max(posterior)
		index = posterior.index(maximum)
		key_list = self.key_creator()
		return(key_list[index])


data = Data('earthquake')
prior = [0.02777] * 36

newdictionary = Interpret(data, prior, 0, "Not at all worried", "earthquake")
posterior1 = newdictionary.bayesian_update()

newdictionary1 = Interpret(data, posterior1, 1, "Not so worried", "earthquake")
posterior2 = newdictionary1.bayesian_update()

newdictionary2 = Interpret(data, posterior2, 2, "No", "earthquake")
posterior3 = newdictionary2.bayesian_update()

newdictionary3 = Interpret(data, posterior3, 3, "Yes, one or more minor ones", "earthquake")
posterior4 = newdictionary3.bayesian_update()

newdictionary4 = Interpret(data, posterior4, 4, 'No', "earthquake")
posterior5 = newdictionary4.bayesian_update()

newdictionary5 = Interpret(data, posterior5, 5, 'Not so familiar', "earthquake")
posterior6 = newdictionary5.bayesian_update()

newdictionary6 = Interpret(data, posterior6, 6, 'Somewhat familiar', "earthquake")
posterior7 = newdictionary6.bayesian_update()

print(newdictionary6.biggest_probability())









