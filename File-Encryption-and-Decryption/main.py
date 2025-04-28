#
# Syrus Freeman
# 4/27/2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 
# Open the file
input_file = open ('File-Encryption-and-Decryption//text.txt', 'r')
output_file = open ('File-Encryption-and-Decryption/encrypted.txt', 'r')
def encrypt_file (input_file, output_file, codes):
    try:
        file = open(input_file, 'r')
        original_text = file.read()
        encrypted_text = ""
        for char in original_text:
            encrypted_text += codes.get(char, char)
        encrypted_file = open(output_file, 'w')
        encrypted_file.write(encrypted_text)
        print("File Encrypted Succesfully.")
    except FileNotFoundError:
        print("Input file not found.")
encryption_codes = {'Q':'!', 'W':'@', 'E':'$', 'R':'#', 'T':'^', 'Y':'*',
            'U':'&', 'I':'1', 'O':'2', 'P':'3', 'A':'4', 'S':'5',
            'D':'6', 'F':'7', 'G':'8', 'H':'9', 'J':'0', 'K':'_',
            'L':'+', 'Z':'~', 'X':'`', 'C':'|', 'V':'<', 'B':'>',
            'N':'?', 'M' : '-', 'q':'w', 'w':'e', 'r':'e', 'e':'r',
            't':'y', 'y':'u',
            'u':'i', 'i':'o', 'o':'p', 'p':'a', 'a':'s', 's':'d',
            'd':'f', 'f':'g', 'g':'h', 'h':'j', 'j':'k', 'k':'l',
            'l':'z', 'z':'x', 'x':'c', 'c':'v', 'v':'b', 'b':'n',
            'n':'m', 'm' : 'n' }
encrypt_file('File-Encryption-and-Decryption//text.txt', 'File-Encryption-and-Decryption/encrypted.txt', encryption_codes)
