import csv
from collections import OrderedDict, defaultdict

my_dict = defaultdict(int)
# my_dict = {}

my_dict['a'] += 10

print(my_dict)

#
# with open("dane/logs.txt") as f:
#     reader = csv.DictReader(f, delimiter=";")
#     for line in reader:
#         print(line)
#         print(line['LOGIN'])
#
