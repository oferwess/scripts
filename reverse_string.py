#Code to return reverse string

#Method 1
input1_string = input("method 1 - please type your string\n")
length = (len(input1_string))-1

while length > 0:
    for each in input1_string:
        print (input1_string[length])
        length = length -1

#Method 2
input2_string = input("method 2 - please type your string\n")
reverse = input2_string[::-1]
print (reverse)

#Method3

def reverse_string(string):
    temp = ""
    for char in string:
        temp =  char + temp
    return temp

string = input("method 3 - please type your string\n")
print (reverse_string(string))