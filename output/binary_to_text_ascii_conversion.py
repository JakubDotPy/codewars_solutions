"""Kata - Binary to Text (ASCII) Conversion

completed at: 2023-06-17 20:13:01
by: Jakub Červinka

Write a function that takes in a binary string and returns the equivalent decoded text (the text is ASCII encoded).

Each 8 bits on the binary string represent 1 character on the ASCII table.

The input string will always be a valid binary string.

Characters can be in the range from "00000000" to "11111111" (inclusive)

Note: In the case of an empty binary string your function should return an empty string.


"""

def binary_to_string(binary):
    args = [iter(binary)] * 8
    return ''.join(chr(int(''.join(byte), 2)) for byte in zip(*args))
    
