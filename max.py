#a lambda function to find the bigger number in two given numbers .

f=lambda x,y:x if x >y else y #write lambda function
a,b=[int(n) for n in input ("Enter two numbers :").split(',')]
print('Bigger number=',f(a,b)) #call lambda function 