'''
Authors: Emily Lepert and Vicky McDermott

The Interpret class will take in the answer to a question and update
the probability that someone is from a region and their age based on that response
'''
from data import Data
from os.path import exists
from pickle import dump, load
import sys

class Interpret:
	def __init__(self, prior, question, answer, data_type):
		# differentiates between a comma or earthquake data set
		self.data_type = data_type
		if self.data_type == "comma":
			self.data = Data('comma')
		elif self.data_type == "earthquake":
			self.data = Data('earthquake')

		# prior probabilities
		self.prior = prior
		# question index
		self.question = question
		# answer to the question
		self.answer = answer

		#list of question indices
		if self.data_type == 'comma':
			self.question_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		elif self.data_type == 'earthquake':
			self.question_list = [0, 1, 2, 3, 4, 5, 6]
		#age lists
		self.age_list = ['18 - 29', '30 - 44', '45 - 59', '60']

		#location list
		self.location_list = ['East North Central', 'East South Central', 'Middle Atlantic',
			'Mountain', 'New England', 'Pacific', 'South Atlantic', 'West North Central', 'West South Central']

	def key_creator(self):
		"""
		Creates the location-age keys for the final output of new posterior probabilities
		"""
		key_list = []
		for i in self.location_list:
			for j in self.age_list:
				key = i+'; '+j
				key_list.append(key)
		return(key_list)

	def get_location(self, key):
		'''
		Gets the location associated with a given posterior output
		'''
		keys = self.key_creator()
		my_key = keys[key].split(';')
		return my_key[0]

	def get_age(self, key):
		'''
		Gets the location associated with a given posterior output
		'''
		keys = self.key_creator()
		my_key = keys[key].split(';')
		return my_key[1]

	def key_formatting(self, a):
		if self.data_type == 'earthquake':
			if a == '"Yes, one or more minor ones"':
				a1 = 'Yes, one or more minor ones'
			elif a == '"Yes, one or more major ones"':
				a1 = 'Yes, one or more major ones'
			else:
				a1 = a
		elif self.data_type == 'comma':
			if a == '"It\'s important for a person to be honest, kind and loyal."':
				a1 = "It's important for a person to be honest, kind and loyal."
			elif a == '"It\'s important for a person to be honest, kind, and loyal."':
				a1 = "It's important for a person to be honest, kind, and loyal."
			elif a == '"Some experts say it\'s important to drink milk, but the data are inconclusive."':
				a1 = "Some experts say it's important to drink milk, but the data are inconclusive."
			elif a == '"Some experts say it\'s important to drink milk, but the data is inconclusive."':
				a1 = "Some experts say it's important to drink milk, but the data is inconclusive."
			elif a == '"$50,000 - $99,999"':
				a1 = '$50,000 - $99,999'
			elif a == '"$25,000 - $49,999"':
				a1 = '$25,000 - $49,999'
			elif a == '"$0 - $24,999"':
				a1 = '$0 - $24,999'
			elif a == '"$150,000+"':
				a1 = '$150,000+'
			elif a == '"$100,000 - $149,999"':
				a1 = '$100,000 - $149,999'
			else:
				a1 = a

		return(a1)

	def denominator_factor(self, question, answer):
		"""
		Finds the total number of people for each hypothesis (location - age combo)
		who answered a question
		"""
		denominator = {}
		value = 0
		for i in self.location_list:
			for j in self.age_list:
				key = i + '; ' + j
				#calls on the get_data method of the Data class
				#returns dictionary of answers to a question with the number of people
				#who answered each answer
				result = self.data.get_data(i, j, question)
				for a1 in result:
					#a1 = self.key_formatting(a)
					# go through all the # of answers to a question and add them to one variable
					value += result[a1]
				#key is location-age, value is the total # of answers to a question
				denominator[key] = value
				value = 0
		return(denominator)

	def numerator_factor(self, question, a):
		"""
		Finds the number of people for each hypothesis (location - age combo) and each answer to a question
		"""
		factor = {}
		for i in self.location_list:
			for j in self.age_list:
				key = i + '; ' + j
				result = self.data.get_data(i, j, question)
				if a in result:
					a1 = self.key_formatting(a)
					#if the answer to the question is in result,
					#value is the number of people who's response was answer
					value = result[a]
					#key is location-age
					factor[key] = value
				else:
					#if nobody answered with that response, then make it 0
					factor[key] = 1
		return(factor)

	def bayesian_single_factor(self, question, answer):
		"""
		Given a piece of data (question and answer), create dictionary with corresponding
		P(D|H)
		H: string of location + age
		ie: 'East North Central; 18 - 29'
		Creates a dictionary for each specific question answer combo
		"""
		denominator = self.denominator_factor(question, answer)

		numerator = self.numerator_factor(question, answer)
		factor = {}
		for i in denominator:
			if denominator[i] != 0:
				#create a dictionary with the ratio of numerator/denominator
				factor[i] = float(numerator[i]/denominator[i])
		return(factor)

	def dictionary_of_qa(self):
		"""
		Creates a dictionary of questions with all the responses
		"""
		dic_of_qa = {}

		for l in self.location_list:
			for a in self.age_list:
				for q in self.question_list:
					#get all the answers to a question
					result = self.data.get_data(l, a, q)
					# if the question is not yet in the new dictionary
					if q not in dic_of_qa:
						dic_of_qa[q] = []
					#for every answer to the question
					for b in result:
						#a1 = self.key_formatting(b)
						if b not in dic_of_qa[q] and (b != ''):
							dic_of_qa[q].append(b)
		return(dic_of_qa)

	def bayesian_factors(self, file_name, reset=False):
		"""
		Creates file with all the factors for all combos of question answers
		"""
		prev_factors = self.dictionary_of_qa()
		new_factors = {}
		for q in prev_factors:
			for a in prev_factors[q]:
				if q not in new_factors:
					new_factors[q] = {}
				#clean the keys up
				a1 = self.key_formatting(a)
				new_factors[q][a1] = self.bayesian_single_factor(q, a)

		#pickles info to a txt file
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
		if self.data_type == 'comma':
			#self.bayesian_factors('comma_factors.txt')
			factors = load(open('comma_factors.txt', 'rb+'))
		elif self.data_type == 'earthquake':
			factors = load(open('earthquake_factors.txt', 'rb+'))
		list_of_factors = []
		#index into the right question answer combo

		for i in factors[self.question][self.answer]:
			list_of_factors.append(factors[self.question][self.answer][i])

		product = []
		j = 0
		#create the product
		while j<len(list_of_factors):
			prd = list_of_factors[j] * self.prior[j]
			product.append(prd)
			j += 1

		total = 0
		#find normalizing factor
		for l in product:
			total += l

		posterior = []
		for k in product:
			#normalize
			if total != 0:
				posterior.append(k/total)
			else:
				posterior.append(0)

		return(posterior)

	def biggest_probability(self):
		"""
		Finds the biggest probability someone has of being from somewhere
		"""
		posterior = self.bayesian_update()
		maximum = max(posterior)
		index = posterior.index(maximum)
		key_list = self.key_creator()
		return(key_list[index])


#data = Data('comma')
#prior = [0.02777] * 36
