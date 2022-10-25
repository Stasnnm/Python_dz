# correct = 3 != 5
# print(correct)
# sim_equ = (5 == 5)
# print(sim_equ)
# sim_large = 5 >= 5
# print(sim_large)
# sim_less = 5 <= 5
# print(sim_less)

result_tr_or = True or True or False
print(result_tr_or)
result_tr_and = True and True or False
print(result_tr_and)
result_tr_not = True and True and not False
print(result_tr_not)
result_not_tr = not True or not True or not False
print(result_not_tr)
result_last = not True or True and not False
print(result_last)