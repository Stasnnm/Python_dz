num_one = float(input('input number one :'))
num_two = float(input('input nomber two :'))
ope_num = input('input operation "+" or "-" or "/" or "*"')
if ope_num == '+' :
    res = num_one + num_two
    print('result', res)
elif ope_num == '-':
    res = num_one - num_two
    print('result', res)
elif ope_num == '/':
    res = num_one / num_two
    print('result', res)
elif ope_num == '*':
    res = num_one * num_two
    print('result', res)
else :
    print('incorrect operation')




