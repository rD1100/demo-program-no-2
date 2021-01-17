
def back():
  print("1. persegi")
  print("2. Segitiga ")
  print("3. Keluar")
  print("\n")
  pilih=int(input("Silahkan masukkan pilihan anda: "))
  if pilih==1:
    print("pilihan: 1")
    print("menghitung luas persegi ")
    a=int(input("masukkan Sisi: "))

    c=a*a
    print("luas persegi :",c)
    ask()
  elif pilih==2 :
    print("pilihan: 2")
    print("Menghitung luas Segitiga")
    a=int(input("masukkan Alas: "))
    b=int(input("masukkan Tinggi: "))
    c=1/2*a*b
    print("Luas Segitiga: ",c)
    ask()

  else :
    exit()
 
def ask():
    tanya=(input("ingin memasukkan lagi y/t: "))
    if tanya=="ya" or tanya=="y":
        back()
    else :
      exit()
back()


   
