def print_faktor (x) :
 #fungsi menerima input bilangan dan mencetak faktor
    print("faktor dari", x , "adalah =")
    for i in range (1,x+1):
        if x % i == 0 : 
            print (i) 

# Input bilangan yang akan dicari faktornya
num = int(input("masukkan Bilangan : "))
print_faktor(num)