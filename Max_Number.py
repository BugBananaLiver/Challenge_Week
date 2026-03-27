def find_max(list):
    max_num = list[0]
    for number in list:
        if number > max_num:
            max_num = number
    print(max_num)
    return

#find_max([2, 6, 7, 9, 3])
#find_max([4, 9, 1, 17, 2])   #Output : 17  
#find_max([-5, -9, -2, -12]) #Output :  -2  
#find_max([42])  #Output : 42


# def find_max(list):
#     list.sort()
#     highest_number = list[-1]
#     print(highest_number)
#     return

#find_max([2, 6, 7, 9, 3])
#find_max([4, 9, 1, 17, 2])   #Output : 17  
#find_max([-5, -9, -2, -12]) #Output :  -2  
#find_max([42])  #Output : 42