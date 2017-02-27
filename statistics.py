''' 
Authors: Emily Lepert and Vicky McDermott

The Interpret class will take in the answer to a question and update
the probability that someone is from a region and their age based on that response
'''

class Interpret:
	def __init__(self, earthquake, commas, question, answer):
		self.earthquake = earthquake
		self.commas = commas
		self.question = question
		self.answer = answer

	def reverse_dictionary(self):
		"""
		Makes a dictionary that, based on the answer to a question, gives the probability
		that someone is from a location and age range
		Basically it gives us P(D|H)
		"""
		factors = {}
		for i in self.earthquake: # in location of earthquake
			for j in i: # in age range of location
				for l in j: # in question of age 
					a = 0
					while a < len(l):
						#for a in l: # for each amount of each answer
						factors[l][a][i][j] += l[a]
						a +=1
		print(factors)

	def bayesian_update():
		"""
		Updates a prior probabilities with posterior probabilities using Bayesian
		"""
		pass





