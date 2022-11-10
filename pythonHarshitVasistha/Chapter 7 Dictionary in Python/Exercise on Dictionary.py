# ----------** Exercise **------------------
# 1.
'''
define a function that takes a number(n)
return a dictionary containing cube of numbers from 1 t0 o n
'''


def cube_dict(n):
    cube = {}
    for i in range(1, n + 1):
        cube[i] = i ** 3
    return cube


print(f"The cubes of number ranging from 1 to 10 is : \n {cube_dict(10)}")


# Question 2: charcter  counter
# count and store the freq of each unique char

def char_counter(s):
    ch_ct = dict.fromkeys(s,0) # dict created where every char is key and value is 0 for all
    # ch_ct = {} # empty dictionary this can also work
    for ch in s:
        ch_ct[ch] = s.count(ch)
    return ch_ct


print(char_counter("aabbac"))


# take input from user and make a dictionary if it
# prints dictionary of this kind by taking input from the user
'''
my_info = {
        'name': "Roshan",
        'age': 22,
        'DOB': '01/03/1999',
        'fav_movies': ["abc","xyz","pqr"],
        'fav_songs': ['song1' , 'song2']
}
'''
print("Creating Dictionary !!!")
my_info = {}
name = input("What is your name : ")
age = input("What is your age : ")
fav_movies = input("Enter your fav movies separed by commas").split(',')
print(fav_movies)
fav_songs = input("Enter your fav songs separed by commas").split(',')
print(fav_songs)

my_info['name'] = name
my_info['age'] = age
my_info['fav_movies'] = fav_movies
my_info['fav_songs'] = fav_songs
print(my_info)
print("dictionary Unpacking !!! ")
for key,value in my_info.items():
    print(f"{key}: {value},")

