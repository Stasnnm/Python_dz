dat_inp = input('input data :')
var_one = ""
var_two = ""
for index, elem in enumerate(dat_inp):
    if elem.isupper():
        var_one = var_one + elem
    elif elem == " ":
         var_two = str(index) + var_two






print(var_one)
print(var_two)

