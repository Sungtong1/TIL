# table = {
#     'black' : {
#         'value' : 0,
#         'multi' : 1
#     },
#     'brown': {
#         'value': 1,
#         'multi': 10
#     },
#     'red': {
#         'value': 2,
#         'multi': 100
#     },
#     'orange': {
#         'value': 3,
#         'multi': 1000
#     },
#     'yellow': {
#         'value': 4,
#         'multi': 10000
#     },
#     'green': {
#         'value': 5,
#         'multi': 100000
#     },
#     'blue': {
#         'value': 6,
#         'multi': 1000000
#     },
#     'violet': {
#         'value': 7,
#         'multi': 10000000
#     },
#     'grey': {
#         'value': 8,
#         'multi': 100000000
#     },
#     'white': {
#         'value': 9,
#         'multi': 1000000000
#     },
# }
# result = ''
# for i in range(3):
#     word = input()
#     if i < 2:
#         result += str(table[word]['value'])
#     else :
#         result = result + str(table[word]['multi'])[1:]
#
# print(result)


table = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']

result = 0
first = input()
result += table.index(first)*10
second = input()
result += table.index(second)
third = input()
result *= 10 ** table.index(third)

print(result)

