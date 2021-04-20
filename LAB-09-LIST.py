# 71200640
# SHALOMMITA P.
# LAB-09-LIST

lstNIM=[]
lstUTS=[]
lstUAS=[]
lstTotal=[]

# INPUT
# Data, NIM, NIlai UTS, Nilai UAS
ulang=int(input("Menginputkan data sebanyak: ")) #0,1
for i in range(ulang):
    print("Data ke-"+ str(i+1))
    lstNIM.append(input("NIM: "))
    lstUTS.append(int(input("Nilai UTS: ")))
    lstUAS.append(int(input("Nilai UAS: ")))

# PROSES
# Perulangan ada 2 yaitu perulangan data dan perulangan total
for i in range(ulang):
    lstTotal.append((lstUAS[i]+lstUTS[i])/2)

# OUTPUT
# NIM   Nilai UTS   Nilai UAS   Nilai Total
print("-"*65)
print("NIM          Nilai UTS       Nilai UAS                Nilai Total")
print("-"*65)
print("%s\t%i\t\t%i\t\t\t%i"%(lstNIM[i],lstUTS[i],lstUAS[i],lstTotal[i]))
print("-"*65)
