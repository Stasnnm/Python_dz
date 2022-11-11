dat_inp = input('input data :')
var_one = ""
var_two = ""
counter = 0
num_one = 100
for index, elem in enumerate(dat_inp):
    if str(num_one) in dat_inp and num_one < 1000 :
        print('stop')
        break
    elif int(num_one) < 1000:
        num_one = int(num_one) + 1

    elif elem.isupper():
        var_one = var_one + elem
    elif elem == " ":
         if counter == 0:
             var_two = var_two + str(index)
         else :
             var_two = var_two + ',' +str(index)
         counter += 1

print(var_one)
print(var_two)
