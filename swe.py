def is_prime(n):
   if n <= 1:
      return"NO"
   if n <= 3:
      return"YES"
   if n%2 == 0 or n%3 == 0:
        return"NO"
   i=5
   while i*i<=n:
    if n%i == 0 or n%(i+2) == 0:
        return"NO"
    i+=6
   reurn"YES"
n=int(input("enter a number:"))
print(is_prime(n))
        
