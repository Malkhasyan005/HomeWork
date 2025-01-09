# Create a simple encryption program using the XOR operator. You'll take two integers, apply XOR to create an "encrypted" value, and then decrypt it by applying XOR again. This task will show you how XOR can toggle bits to hide and reveal data.

#num1 = int(input("Enter the first number: "))
#num2 = int(input("Enter the secind number: "))
#
#enc_num = num1 ^ num2
#dec_num = enc_num ^ num2
#
#print(f"original num = {num1}")
#print(f"Encrypted num = {enc_num}")
#print(f"Decrypt num = {dec_num}")

# Write a program that uses the bitwise AND operator to determine if a number is even or odd. You’ll only need to check if the last bit is 0 (even) or 1 (odd). This will help you see how individual bits can reveal specific properties of a number.

#num = int(input("Enter a number: "))
#
#if num & 1:
#    print(f"{num} is Odd")
#else:
#    print(f"{num} is Even")

# Write a program that sets or clears a specific bit in a binary number. For example, turn the 3rd bit on or off using the bitwise OR (for setting) and AND with NOT (for clearing). This will demonstrate how to control individual bits.

#num = int(input("Enter a number: "))
#print(f"Decimal {num} = Binary {str(bin(num))[2:]}")
#
#bit_num = 4
#set_num = num | bit_num
#cleaned_num = num & ~bit_num
#
#print(f"Set number = {set_num} (Binary {str(bin(set_num))[2:]})")
#print(f"Cleaned number = {cleaned_num} (Binary {str(bin(cleaned_num))[2:]})")


# Take a number and use bitwise AND with 1 to check if each bit is 1 or 0. Repeat for each bit position by moving from right to left in the binary representation. Count how many 1s you find. This helps you see how binary numbers are made up of individual bits.

#num = int(input("Enter a number: "))
#one_bit_cnt = 0
#
#while num != 0:
#    if num & 1:
#        one_bit_cnt += 1
#    num = num >> 1
#
#print(f"1 bit count is {one_bit_cnt}")

# Choose any number and select one bit to toggle (turn on if it’s off or off if it’s on). Use the XOR operator with 1 in that bit’s position to change its state. Write down the result to see how XOR can flip bits individually.

num = int(input("Enter a number: "))
print(f"Decimal {num} = Binary {str(bin(num))[2:]}")
bit_ind = int(input("Enter bit index which do you want to change: ")) - 1
xor_num = 1 << bit_ind

changed_num = num ^ xor_num
print(f"Changed number = {changed_num} \nDecimal {changed_num} = Binary {str(bin(changed_num))[2:]}")
