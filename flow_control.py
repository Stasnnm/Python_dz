num_one = float(input('input number one : '))
num_two = float(input('input nomber two : '))
ope_num = input('input operation "+" or "-" or "/" or "*" : ')
if ope_num == '+' :
    res = num_one + num_two
elif ope_num == '-':
    res = num_one - num_two
elif ope_num == '/':
    res = num_one / num_two
elif ope_num == '*':
    res = num_one * num_two
else :
    print('incorrect operation')
if  num_one - int(num_one) > 0 and num_two - int(num_two) > 0:
    print(float(res))
else:
    print(int(res))


