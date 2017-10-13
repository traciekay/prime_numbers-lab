def prime_numbers(num):
 list_of_prime_numbers = []

 for i in range(2, num+1): # loops through 2 3 4 5 6 7
   prime = True

   for t in range(2, i): # 2,3
     if i % t == 0:
       prime = False

   if prime == True:
     list_of_prime_numbers.append(i)

 return list_of_prime_numbers

print prime_numbers(8)
