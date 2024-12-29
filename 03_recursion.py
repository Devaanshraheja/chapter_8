
def factorial(n): 
    if (n==1 or n==0):
         return 1
    else:
         
        return n * factorial(n-1)
   



n=int(input("enter the number:"))            
a=factorial(n) 
print(f"the factorial of {n} is ",a)     