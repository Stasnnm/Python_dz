correct = 3 != 5
print(correct)
sim_equ = (5 == 5)
print(sim_equ)
sim_large = 5 >= 5
print(sim_large)
sim_less = 5 <= 5
print(sim_less)

result_tr_or = True or True or False
print(result_tr_or)
result_tr_and = (True and True) or False
print(result_tr_and)
result_tr_not = True and True and not False
print(result_tr_not)
result_not_tr = (not True or not True) or not False
print(result_not_tr)
result_last = not True or (True and not False)
print(result_last)

bool_none = bool(None)
print('bool_none -', bool_none)
bool_numb = bool (7)
print('bool_numb -', bool_numb)
comp = bool(bool_numb == bool_none)
print('comp', comp)
empt_str = bool('')
subtr = bool(10 - 1)
print('empt_str', empt_str, 'subtr', subtr)
comp_two = bool(empt_str == subtr)
print(comp_two)


