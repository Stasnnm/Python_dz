num_one = input('input number one : ')
num_two = input('input nomber two : ')
if '.' in num_one:
    num_one = float(num_one)
    print('number one is float')
else:
    num_one = int(num_one)
    print('number one is integer')
if '.' in num_two:
    num_two = float(num_two)
    print('number two is float')
else:
    num_two = int(num_two)
    print('number two is integer')
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
print('result :', res)
print('type of result is: ', type(res))
if num_one < num_two:
    print('num_one > num_two')
elif num_one > num_two:
    print('num_one > num_two')
else:
    print('num_one = num_two')
if type(num_one) is int:
   print('order num_one :', len(str(num_one)))
else:
    len_fl = len(str(num_one))
    print('order num_one:', len_fl - 1)
if type(num_two) is int:
    print('order num_two :', len(str(num_two)))
else:
    len_fl_two = len(str(num_two))
    print('order num_two:', len_fl_two - 1)


