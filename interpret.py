''' 
Authors: Emily Lepert and Vicky McDermott

The Interpret class will take in the answer to a question and update
the probability that someone is from a region and their age based on that response
'''

class Interpret:
	def __init__(self, earthquake): #, commas, question, answer):
		self.earthquake = earthquake
		#self.commas = commas
		#self.question = question
		#self.answer = answer

	def reverse_dictionary(self):
		'''
		Makes a dictionary that, based on the answer to a question, gives the probability
		that someone is from a location and age range
		Basically it gives us P(D|H)
		'''
		factors = {}
		# first level of earthquake: locations
		for i in self.earthquake: 
			location = self.earthquake[i]
			
			# second level: age
			for j in location: # in age range of location
				age = location[j]
				new_question = {}
				# third level: question
				for l in age: # in question of age 
					question = age[l]
					
					a = 0
					factors[l] = new_question # value associated with q
					# 4th level: answer
					while a < len(question):
						new_age = {}
						new_answer = {}
						new_question[a] = new_answer # value associated with each answer index
						print(a)
						new_answer[i] = new_age # value associated with each location
						new_age[j] = self.earthquake[i][j][l][a] # value associated with each age
						a +=1
					print(l)
					print(factors)
					print("\n")

		

	def bayesian_update():
		"""
		Updates a prior probabilities with posterior probabilities using Bayesian
		"""
		pass

earthquake = {'loc1' : 
				{'age1' : 
					{'q1' : [1,2,3,4], 
					'q2': [5,6,7,8], 
					'q3' : [9,10,11,12]}, 
				'age2' : 
					{'q1' : [13,14,15,16], 
					'q2': [17,18,19,20], 
					'q3' : [21,22,23,24]} 
				},
			'loc2' : 
				{'age1' : 
					{'q1' : [25,26,27,28], 
					'q2': [29,30,31,32], 
					'q3' : [33,34,35,36]}, 
				'age2' : 
					{'q1' : [37,38,39,40], 
					'q2': [41,42,43,44], 
					'q3' : [45,46,47,48]} 
				}
			}
newdictionary = Interpret(earthquake)
print(newdictionary.reverse_dictionary())





