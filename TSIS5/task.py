import re

task1 = 'ab*'
task2 = 'ab{2,3}'
task3 = '[a-z]+_[a-z]+'
task4 = '[A-Z][a-z]+'
task5 = 'a.*?b$'
task6 = '[ ,.]'


task8 = '(?=[A-Z])'



with open('row.txt', 'r') as file:
        for line in file:
            if re.search(task1, line):
                  print(line.strip())

            if re.search(task2, line):
                  print(line.strip())

            if re.search(task3, line):
                  print(line.strip())

            if re.search(task4, line):
                  print(line.strip())

            if re.search(task5, line):
                  print(line.strip())
            
            #task6
            replaced_line = re.sub(task6, ':', line)
            print(replaced_line.strip())

            #task7 snake to camel
            print(''.join(word.title() for word in line.strip().split('_')))

            #task8 split at upper
            split_line = re.split(task8, line.strip())
            print(' '.join(split_line))

            #task9
            converted_line = re.sub('(?<!^)(?=[A-Z])', ' ', line.strip())
            print(converted_line)

            #task10
            print(re.sub('(?<!^)(?=[A-Z])', '_', line.strip()).lower())

