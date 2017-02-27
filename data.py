'''
Authors: Vicky McDermott and Emily Lepert
'''


class Data:
    def __init__(self, type):
        self.type = type
        if self.type == 'earthquake':
            f = open('earthquake_data.csv')
            self.lines = f.readlines()
            print(self.lines)

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
            current_line = line.split(',')
            key = current_line[len(current_line)-1].strip()
            if key in locations:
                locations[str(key)].append(current_line[:len(current_line)-1])
        return locations

    def sort_by_age(self):
        ultimate_dict = {}
        locations = self.sort_by_location()
        for key in locations:
            ages = {}
            print(locations[key])
            for line in locations[key]:
                print(line[8])
                print(line[:7] + line[9:])
                if line[8] in ages:
                    ages[line[8]].append(line[:7] + line[9:])
                else:
                    ages[line[8]] = [line[:7] + line[9:]]
            ultimate_dict[key] = ages
        # print(ultimate_dict)

    def fix_comma_issue(self):
            f = open('earthquake_data.csv', 'wt')
            print(len(self.lines))
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
            '\n'.join(self.lines)
            # f.writelines(self.lines)
