correct = 3 != 5
print(correct)
sim_equ = (5 == 5)
print(sim_equ)
sim_large = 5 >= 5
print(sim_large)
sim_less = 5 <= 5
print(sim_less)

print(True or True or False)
print(True and True or False)
print(True and True and not False)
print(not True or not True or not False)
print(not True or True and not False)

bool_none = bool(None)
bool_numb = bool (7)
print('bool_none -', bool_none, 'bool_numb -', bool_numb)
comp = bool(bool_numb) == bool(bool_none)
print('bool_none == bool_numb -', comp)

empt_str = bool("")
subtr = bool(10 - 1)
print('empt_str', empt_str, 'subtr', subtr)
comp_two = bool(empt_str) == bool(subtr)
print('bool("") == bool(10 - 1) -', comp_two)

tru_or_fal = bool(True or False)
f_prin = bool(print('123'))
print('bool True or False -', tru_or_fal)
print('bool(print("123"))- ', f_prin)
comp_three = bool(tru_or_fal) == bool(f_prin)
print('bool(True or false) == bool(print("123"))-', comp_three)

f_typ = bool(type(None))
f_id = bool(id(None))
print('bool(type(None)) -', f_typ, 'bool(id(None))', f_id)
comp_four = print('bool(type(None)) == bool(id(None))', bool(f_typ) == bool(f_id))




