import string

def caesar_cipher(text, shift, decode = False):
   if decode: shift = 26 - shift
   return text.translate(
       str.maketrans(
           string.ascii_uppercase + string.ascii_lowercase,
           string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift] +
           string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
           )
       )
