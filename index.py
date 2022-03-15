import os
import re

script_dir = os.path.dirname(__file__)
# files_dir = 'files\example.txt'
files_dir = 'files\example2.txt'
absolute_files_dir = os.path.join(script_dir, files_dir)

with open(absolute_files_dir, 'r') as fp:
    lines = fp.readlines()
    result = ''

    for index, line in enumerate(lines):
        next_index = index + 1

        while next_index < len(lines):
            first_line = lines[index].split('=')
            next_line = lines[next_index].split('=')
            same_range = 0

            for i in first_line[1].split(','):
                for j in next_line[1].split(','):
                    if i[:2] == j[:2]:
                        first_hour = re.split('-|\n', i[2:])
                        next_hour = re.split('-|\n', j[2:])

                        if first_hour[0] >= next_hour[0] and first_hour[1] <= next_hour[1]:
                            same_range += 1
                    else:
                        pass

            # common_days = set(first_line[1].split(',')).intersection(next_line[1].split(','))
            result = result + first_line[0] + '-' + next_line[0] + ': ' + str(same_range) + '\n'
            next_index += 1
    
    print(result)
