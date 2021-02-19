from datetime import datetime

# test_dict = {'1': ['2', '6', '9', '4'], '2': [], '3': ['13', '5', '8', '2'], '4': ['3', '14', '9', '5']}
# cp_dict = {}
# quan_dict = {}
# cp_dict.update(test_dict)
# for k, v in test_dict.items():
#     if len(v)<2:
#         del cp_dict[k]
#     else:
#         quan_dict[k] = v[-1]
#         cp_dict[k] = cp_dict[k][:-1]

# print(cp_dict)
# print(quan_dict)
# input()

year = datetime.today().year
month = datetime.today().month

for m in range(1,11):
    print(year, month)
    month -= 1
    if month < 1:
        month = 12
        year -= 1
# print(datetime.today().month)