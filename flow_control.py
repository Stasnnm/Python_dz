num_one = float(input('input number one : '))
num_two = float(input('input nomber two : '))
typ_one = print('num_one is int') if (num_one % 1) == 0 else print('num_one is float')
typ_two = print('num two is int') if (num_two % 1) ==0 else print('num_two is float')
ope_num = input('input operation "+" or "-" or "/" or "*" or "**" : ')
if ope_num == '+':
    res = num_one + num_two
elif ope_num == '-':
    res = num_one - num_two
elif ope_num == '/':
    res = num_one / num_two
elif ope_num == '*':
    res = num_one * num_two
elif ope_num == '**':
    res = num_one ** num_two
else:
    print('incorrect operation')

if (num_one % 1) == 0 and (num_two % 1) == 0:
    print(int(res))
else:
    print(float(res))
if num_one < num_two:
    print('num_one > num_two')
elif num_one > num_two:
    print('num_one > num_two')
else:
    print('num_one = num_two')

if (num_one % 1) == 0:
        print('order num_one :', len(str(int(num_one))))
else:
    len_fl = len(str(num_one))
    print('order num_one:', len_fl - 1)
if (num_two % 1) == 0:
    print('order num_two :', len(str(int(num_two))))
else:
    len_fl_two = len(str(num_two))
    print('order num_two:', len_fl_two - 1)


