import math

def p0003fast(n):
    largest_prime_factor = 1

    # lets deal with 2
    while n % 2 == 0:
        n = n/2

    remaining_n = n 

    if remaining_n == 1:
        return 2

    starting_factor = 3

    while remaining_n > 1 and starting_factor < math.sqrt(remaining_n):
        if remaining_n % starting_factor == 0:
            largest_prime_factor = starting_factor

            while remaining_n % starting_factor == 0:
                remaining_n = remaining_n / starting_factor     

        starting_factor += 2

    if remaining_n == 1:
        return largest_prime_factor

    else:
        return remaining_n

print p0003fast(600851475143)

     
    
     

#This approch could work but it takes too much time

# def is_prime(n):
#     for i in xrange(2,int(round(math.sqrt(n) + 1))):
#         if n % i == 0:
#             return False

#     return True


# def largest_prime(n):
#     div = int(round(n/2))

#     while True:
#         if n % div == 0:
#             if is_prime(div):
#                 return div
                
#         if div == 2:
#             break

#         div -= 1

#     return 1

#print largest_prime(600851475143)






        
        