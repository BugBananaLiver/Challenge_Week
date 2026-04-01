# def Caesar_Cipher(string, integer):
#     text = string
#     for char in text:
#         ord_value = ord(char)
#         shift_ord_value = ord_value + integer
#         chr_shift_ord_value = chr(shift_ord_value)
#         print(chr_shift_ord_value, end="")
#     return  

# Caesar_Cipher("zebra", 2)



def Caesar_Cipher(string, shift):
    result = ""

    for char in string:
        if char.isalpha(): #only shift letters
            shifted = ((ord(char) - ord('a') + shift) % 26) + ord('a')
            result += chr (shifted)
        else:
            result += char #keep spaces punctuation
    print(result)

Caesar_Cipher("The zebra is pink.", 3)