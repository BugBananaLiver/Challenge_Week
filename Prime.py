# def is_prime(integer):
#     if integer == 0:
#         print("False")
#         return
#     if integer == 1:
#         print("False")
#         return
#     if integer == 2:
#         print("True")
#         return
#     if integer == 3:
#         print("True")
#         return
#     if integer % 2 == 0:
#         print("False")
#         return
#     if integer % 3 == 0:
#         print("False")
#         return
#     if integer % 5 == 0:
#         print("False")
#         return
#     print("True")
#     return

# is_prime(9)
#is_prime(2)     #Output: True 
#is_prime(11)  #Output: True  
#is_prime(15)  #Output: False  
#is_prime(1)  #Output:  False  
#is_prime(0) #Output:  False  
#Does not work for larger numbers, divisible by prime numbers....

def is_prime(integer):
    for number in range(2,integer):
        if integer % number == 0:
            print("False")
            return
    print("True")
    return


#is_prime(9)
#is_prime(2)     #Output: True 
#is_prime(11)  #Output: True  
#is_prime(15)  #Output: False  
#is_prime(1)  #Output:  False  
#is_prime(0) #Output:  False  