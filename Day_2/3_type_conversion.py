# type conversion
print(int("123") + int("345"))

# we can use type converter to convert these string into integer and so on but there is some ristiction in this like:-

# print(int("abc")+int("345")) 

#this will give us a error "ValueError" 'cause alphabets can't be converted into a int and int into a alphabets, we can convert  a int into a float like:-
print(float("234")+float("457")) 

name = input("Enter your name?")
length = len(name)
print(f"Number of letter in your name: {length}")