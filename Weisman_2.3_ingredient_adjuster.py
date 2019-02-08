# Jim Weisman

"""
A cookie recipe calls for the following ingredients:

1.5 cups of sugar
1 cup of butter
2.75 cups of flour

The recipe produces 48 cookies with this amount of ingredients. 
Write a program that asks the user how many cookies they want to make, 
and then displays the number of cups (to two decimal places) 
of each ingredient needed for the specified number of cookies. 

"""


c=input('Enter number of cookies:')
a=(int(c))
sugar=(a/48)*1.5
butter=(a/48)*1
flour=(a/48)*2.75


print("To make ", a, " cookies, you will need:\n", \
format(sugar, '.2f'), " cups of sugar\n", \
format(butter, '.2f'), " cups of butter\n", \
format(flour, '.2f'), " cups of flour", sep='')



