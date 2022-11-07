num_one = input('input number one : ')
num_two = input('input nomber two : ')
try:
    num_one = int(num_one)
    print('number one is integer')
except:
    num_one = float(num_one)
    print('number one is float')
try:
    num_two = int(num_two)
    print('number two is integer')
except:
    num_two = float(num_two)
    print('number two is float')
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
print('type of result is: ', type(res))

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


