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
		"""
		Makes a dictionary that, based on the answer to a question, gives the probability
		that someone is from a location and age range
		Basically it gives us P(D|H)
		"""
		factors = {}
		for i in self.earthquake: # in location of earthquake
			location = self.earthquake[i]
			for j in location: # in age range of location
				age = location[j]
				for l in age: # in question of age 
					question = age[l]
					a = 0
					while a < len(question):
						
						if a > 0:
							#current_value = factors.get(l, {}).get(a, {}).get(i, {}).get(j, {})
							current_value = 0
							updated_value = current_value + self.earthquake[i][j][l][a]
						elif a == 0:
							current_value = 0
						factors[l] = {a : {i: {j: current_value}}} # factors.get([l][a][i][j])
						a +=1

		print(factors)

	def bayesian_update():
		"""
		Updates a prior probabilities with posterior probabilities using Bayesian
		"""
		pass

earthquake = {'loc1' : 
				{'age1' : 
					{'q1' : [3,4,7,2], 
					'q2': [4,9,3,2], 
					'q3' : [9,2,1,0]}, 
				'age2' : 
					{'q1' : [3,4,7,2], 
					'q2': [4,9,3,2], 
					'q3' : [9,2,1,0]} 
				},
			'loc2' : 
				{'age1' : 
					{'q1' : [3,4,7,2], 
					'q2': [4,9,3,2], 
					'q3' : [9,2,1,0]}, 
				'age2' : 
					{'q1' : [3,4,7,2], 
					'q2': [4,9,3,2], 
					'q3' : [9,2,1,0]} 
				}
			}
newdictionary = Interpret(earthquake)
print(newdictionary.reverse_dictionary())





