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

print('bool None -', bool(None), ';',  'bool 7 -',  bool(7))
print('(bool None == bool 7) -', bool(None) == bool(7))
print('bool " " -', bool(' '), ';', 'bool (10 - 1) -', bool(10 - 1))
print('bool(" ") == bool(10 - 1))', bool(' ') == bool(10 - 1))
print('bool (True or False) -', bool(True or False))
print('bool print - ', bool(print('123')))