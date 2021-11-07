from pprint import pprint
import operator
with open('1.txt', 'r') as file1:
     count_line = 0
     list1 = []
     for lines in file1:
          list1.append(lines)
          count = (lines.count('\n'))
          if count == 1 :
               count_line += 1

     count_line_file1 = count_line + 1
     dict_1 = {count_line_file1: list1}

with open('2.txt', 'r') as file2:
     count_line = 0
     list2 = []
     for lines in file2:
          list2.append(lines)
          count = (lines.count('\n'))
          if count == 1 :
               count_line += 1

     count_line_file2 = count_line + 1
     dict_2 = {count_line_file2: list2}

with open('3.txt', 'r') as file3:
     count_line = 0
     list3 = []
     for lines in file3:
          list3.append(lines)
          count = int((lines.count('\n')))
          if count == 1 :
               count_line += 1

     count_line_file3 = count_line + 1
     dict_3 = {count_line_file3: list3}

result_list = [dict_1, dict_2, dict_3]


for dicts in result_list:
     if dicts.keys() == max(dicts.keys()):
          print(dicts.items())
          # with open('123.txt', 'w+') as file4:
          #      file4.write(dicts.items())
          #
          # print(count_lines)
