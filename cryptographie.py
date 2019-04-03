import hashlib
import sys

command = sys.argv[1]
file = sys.argv[2]
key = sys.argv[3]
key = key.encode()
hash_object = hashlib.sha256(key)
key_hash = hash_object.hexdigest()

key_calcul = [int(x, 16) for x in key_hash]


if command  == "crypt" :
    title = file

    novoTitle = title.split(".")



    if novoTitle[1] == "txt":

        with open(file,'r')  as f:



            fout = open(novoTitle[0]+".crypt",'w')
            index = 0

            for line in f:
                for char in line:



                    numero = ord(char)
                    novoChar = chr((numero + key_calcul[index])%126)
                    print(char + " : " + str(key_calcul[index]) + " : " + novoChar)
                    index += 1
                    index = index % len(key_calcul)

                    fout.write(novoChar)


        print("key: " + key.decode())
        print("key hash: " + key_hash)
        print("The file has been successfully crypted! ")
    else:
        print("The file must be a .txt file.")


elif command == "decrypt" :

    title = file

    novoTitle = title.split(".")

    if novoTitle[1] == "crypt":


        with open(file,'r')  as f:



            fout = open(novoTitle[0]+"_decrypt.txt",'w')
            index = 0

            for line in f:
                for char in line:



                    numero = ord(char)
                    novoChar = chr((numero - key_calcul[index])%126)
                    print(char + " : " + str(key_calcul[index]) + " : " + novoChar)
                    index += 1
                    index = index % len(key_calcul)

                    fout.write(novoChar)
        print("The file has been successfully decrypted! ")
    else:
        print("The file must be a .crypt file.")

else:
    print("Wrong command. You must put 'crypt' or 'decrypt' as first parameter.")









