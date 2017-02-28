'''
Authors: Vicky McDermott and Emily Lepert
'''


class Data:
    def __init__(self, type):
        self.type = type
        if self.type == 'earthquake':
            f = open('earthquake_data.csv')
            self.lines = f.readlines()

    def get_question(self, number):
        self.lines[0].strip('"')
        ques = [line.strip('"') for line in self.lines[0].split('","')]
        return ques[number]

    def sort_by_location(self):
        locations = {'East North Central': [], 'East South Central': [],
                     'Middle Atlantic': [], 'Mountain': [], 'New England': [],
                     'Pacific': [], 'South Atlantic': [],
                     'West North Central': [], 'West South Central': []}
        for line in self.lines:
            current_line = line.split(';')
            key = current_line[len(current_line)-1].strip()
            if key in locations:
                locations[str(key)].append(current_line[:len(current_line)-1])
        return locations

    def sort_by_age(self):
        ultimate_dict = {}
        locations = self.sort_by_location()
        for key in locations:
            ages = {}
            for line in locations[key]:
                if line[7] in ages:
                    ages[line[7]].append(line[:7] + line[8:])
                else:
                    ages[line[7]] = [line[:7] + line[8:]]
            ultimate_dict[key] = ages
        # print(ultimate_dict)
        return ultimate_dict

    def sort_answers(self):
        best_dict = {}
        # Get dictionary which is sorted by location and age
        ultimate_dict = self.sort_by_age()
        # Go through each location
        for location in ultimate_dict:
            # Go through each age for a specific location
            age_dict = ultimate_dict[location]
            nested_dict = {}
            for age in age_dict:
                # Access answers for specific location and age
                agedppl = age_dict[age]
                # Initialize list of answers for each question
                answers = []
                for i in range(9):
                    answers.append([])
                # Go through each person from that location and age group
                for person in agedppl:
                    # Go through that person's answers and add them to list
                    for i, answer in enumerate(person):
                        answers[i].append(answer)
                # After going through each person convert list to freqdict
                # Be sure to convert list for each question to freqdict
                    # print(answers)
                    new_ans_list = []
                    for i in range(9):
                        new_ans = self.wordListToFreqDict(answers[i])
                        # Recreate your dictionary
                        new_ans_list.append(new_ans)
                # print(new_ans_list)
                # print(age)
                nested_dict[age] = new_ans_list
                # print(nested_dict[age])
            # print(nested_dict)
            best_dict[location] = nested_dict
        print(best_dict)

    def wordListToFreqDict(self, wordlist):
        '''Given a list of words, return a dictionary of
         word-frequency pairs.
         >>> wordListToFreqDict(['hi', 'hi', 'hi'])
         {'hi': 3}
         '''
        wordfreq = [wordlist.count(p) for p in wordlist]
        return dict(zip(wordlist, wordfreq))

    def fix_comma_issue(self):
            f = open('earthquake_data.csv', 'wt')
            f.write(self.lines[0])
            for i in range(len(self.lines)):
                if i > 0:
                    print(i)
                    my_line = list(self.lines[i])
                    for i, letter in enumerate(my_line):
                        if letter == ',':
                            if my_line[i+1] == ' ':
                                pass
                            elif my_line[i+1] == '0' or my_line[i+1] == '9':
                                pass
                            else:
                                my_line[i] = ';'
                                print('fixing a comma')
                    self.lines[i] = ''.join(my_line)
                    print(self.lines[i])
                    f.write(self.lines[i])
