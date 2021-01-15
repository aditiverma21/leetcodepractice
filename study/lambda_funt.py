#lambda functions are the function having no name and having one time use 

add=(lambda a, b: a+b)
sub=(lambda a,b :a-b)
prod=(lambda a,b :a*b)
div=(lambda a,b: a//b)
A=add(2,3)
S=sub(10,3)
P=prod(4,4)
D=div(10,2)
print(A,S,P,D)

#but above we can see we are calling lambda function by giving a names like add sub etc. Actually Lambda function ussed in conjuction with Map filter and reduce function.

#map(funct,iterable)

out=list(map(lambda x: x**2,[x for x in range(10)]))
print(out)