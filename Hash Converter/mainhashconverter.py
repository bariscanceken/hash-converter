import hashlib
import os

password_input = input("Neyi Şifrelemek İstersin?: ")
with_which = input("Hangi Şifreleme Yöntemiyle Şifrelemek İstersin? |(1)md5,(2)sha1,(3)sha224,(4)sha256,(5)sha384,(6)sha512)| :  ")

number = ["1","2","3","4","5","6"]

def convert() :

     global password_input

     if with_which == "1" :
          encryptor = hashlib.md5()
          strfunc = "md5"
            
     elif with_which == "2" :
         encryptor = hashlib.sha1()
         strfunc = "sha1"
         
     elif with_which == "3" :
         encryptor = hashlib.sha224()
         strfunc = "sha224"
         
     elif with_which == "4" :
         encryptor = hashlib.sha256()
         strfunc = "sha256"
         
     elif with_which == "5" :
         encryptor = hashlib.sha384()
         strfunc = "sha384"
         
     elif with_which == "6" :
         encryptor = hashlib.sha512()
         strfunc = "sha512"
         
     while with_which not in number :
        print("Hatalı Veri Girdiniz. Tekrar Deneyin!")
        convert()

     encryptor.update(password_input.encode())
     typestr = encryptor.hexdigest()

     script_directory = os.path.dirname(os.path.abspath(__file__))
     file_path = os.path.join(script_directory, "hashconverterlist.txt")

     with open(file_path, "a") as file:
          file.write(f"{password_input} ----> {strfunc} ile sifrelenmis hali = {typestr}\n")

convert()