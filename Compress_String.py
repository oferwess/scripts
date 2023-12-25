#function gets input string and compress identical chars
def compress (input_to_compress):
    letters_array = []
    index = 0
    for x in range(len(input_to_compress)):
        letters_array.append (input_to_compress[x])
        index = index+1
    my_dict = {i:letters_array.count(i) for i in letters_array}
    return(my_dict)

#function gets input string and decompress identical chars
def decompress (input_to_decompress):
    letters_array = []
    index = 0
    for x in range(len(input_to_compress)):
        letters_array.append (input_to_compress[x])
        index = index +1    
    return (letters_array)


input_to_compress = input("please type your string to compress\n")
print (compress(input_to_compress))

input_to_decompress = input("please type your string to decompress\n")
print (decompress (input_to_decompress))