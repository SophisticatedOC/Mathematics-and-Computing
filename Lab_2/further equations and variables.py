
# variable a is set to 15, the +=5 adds 5 to 15 making the variable a 20, the calling of variable type_a is set to the result of a so that the a variable may change
# further throught the code but the current output wil be saved in the variable type_a and printed

a = 15
a +=5
type_a = type(a)
print(f"a = {a} and its data type is {type_a}")


b = 3952
c = 4029
result = a < b
type_result = type(result)
print(f"result = {result} and its data type is {type_a}")

x = True
y = False


unit_name = "level 4 programming"
print("this unit is: ", unit_name)
print("the first character of this unit name is:", unit_name[0]) #in binary 0 is the first and 1 is second and so on so this will print the first character of the variable unit_name
print("the fourth character is: ", unit_name[3])
print("the eighth character is: ", unit_name[7])


supposed_to_be_greeting_string_but_BOB_is_what_i_chose_instead = ".B.O.B."
print("the first character is: ", supposed_to_be_greeting_string_but_BOB_is_what_i_chose_instead[0])
print("the fith character is: ", supposed_to_be_greeting_string_but_BOB_is_what_i_chose_instead[4])

print("the last character is: ", supposed_to_be_greeting_string_but_BOB_is_what_i_chose_instead[-1])
print("the first 5 characters are: ", supposed_to_be_greeting_string_but_BOB_is_what_i_chose_instead[0:5])

supposed_to_be_greeting_string_but_BOB_is_what_i_chose_instead[0] = "X"
supposed_to_be_greeting_string_but_BOB_is_what_i_chose_instead[6] = "X"


d = 11
print(type(d)) 

# worked example
e = 11.0
print(type(e)) 
# print the type of a
f = “11”
print(type(f)) 
# print the type of a
g = “11” + “11”
print(type(g)) 
# print the type of a
h = “a”
print(type(h)) 
# print the type of a
i = True
print(type(i)) 
# print the type of a
j = “False”
print(type(j)) 
# print the type of a


k = 10.5
print(type(k))

k = int(k) #the only point of making a decimal number an interger is to round down to a "whole number"


l = "i dunno"
m = 10
n = 7.7

print(type(l))

print(type(m))

print(type(n))

mn = m + n
mnr = type(mn)
print(f"result: {mn} type: {mnr} ")

mnint = m + int(n)
mnintr = type(mnint)
print(f"result: {mnint} type: {mnintr} ")

nfloatm = n + float(m)
nfloatmr = type(nfloatm)
print(f"result: {nfloatm} type: {nfloatmr} ")

strn = str(n)
strnr = type(strn)
print(f"type: {strnr} ")

lstrm = l + str(m)
lstrmstrn = lstrm + str(n)
lstrmstrnr = type(lstrmstrn)
print(f"result: {lstrmstrn} type: {lstrmstrnr} ")

lm = l + m
print(f"{l} + {m} = {lm} ")


make_upper = "why do i need to know this"
make_upper = make_upper.upper()
print(make_upper)


such_a_random_exampe = "replace word with word and other word"
