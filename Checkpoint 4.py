#Exercise 1
my_list = ['Asia', 'Africa',' North America',' South America', 'Antarctica', 'Europe','Australia']
my_tuple = ('New York','Paris','Milan','Tokio')
my_float = 3.1456
my_integer = 2024
my_dictionary = {'name':'Nayra','nationality':'Spain' }

from decimal import Decimal
decimal_num = Decimal('3.14159')
print(decimal_num)  

#Exercise 2
print(round(my_float))

#Exercise 3

import math
print(math.sqrt(my_float))

#Exercise 4

print(my_dictionary['name'])

#Exercise 5

print(my_tuple[1])

#Exercise 6

my_list = ['Asia', 'Africa',' North America',' South America', 'Antarctica', 'Europe','Australia']
my_list.append('Oceania')

print(my_list)

#Exercise 7

my_list[0]='Arctic'
print(my_list)

#Exercise 8

my_list.sort()
print(my_list)

sorted_list = sorted(my_list)
print(sorted_list)

#Exercise 9

my_tuple = ('New York','Paris','Milan','Tokio')
more_cities =['Rio de Janeiro','Buenos Aires','Sidney']
my_tuple +=(more_cities,)

print(my_tuple)