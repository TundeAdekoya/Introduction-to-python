#print('Welcome to python')

#checking types
#print(type('5'))
#print(type(5))
#print(type(5.0))

#changing type
#print(type(int('5')))
#var1='hello'
#var2=5.0
#var3=5

#print(var1)
#print(var2)
#print(var3)

#a=5
#b=10
#c=3
#answer=(-b+(4*a*c)**0.5)/(2*a)
#print(answer)

from tracemalloc import start


time1=6.52*60
mile1= time1 + 1*8.15
mile2= 3*7.12
t2= mile1+mile2/60
print(t2)
answer=t2-time1
print(answer)

time1a=6.52*60
mile1a= time1a + 1*8.15*60
mile2a= 3*7.12*60
t2a= mile1a+mile2a/60
print(t2a)
answera=t2a-time1a
print(answera)

#solution
easyspace=((8*60) + 15) *2
tempospace=((7*60) + 12 ) *3

my_runtime = easyspace + tempospace

print(my_runtime)

my_answer = my_runtime / 3600 
start = 6 + (52/60)
print(my_answer + start)


volume=(4/3)*3.14*(5**3)
print(volume)

book_price = 24.95
first_sale = ((0.6 * book_price) +3)
remaining_sale = ((0.6 * book_price) + 0.75) *59
whole_sale = first_sale + remaining_sale
print(whole_sale)

#area = 20 
#carpet_cost = 24.99
#cushion_cost = 2.99
#labor_cost = 18

#total_cost = (carpet_cost *20) + (cushion_cost *20) + (labor_cost *20) + (35)

#print(total_cost)


