print("Pul Vahidini Daxil Edin :")
print("1) Azn ")
print("2) Lira ")
print("3) Dollar ")
proses=int(input())
print("Pul Miqdarınızı Daxil Edin : ")
if proses == 1:
    azn=int(input())
    Lira=azn*11
    Dollar=azn/1.7
    print("Azn:", azn)
    print("Lira :", Lira)
    print("Dollar :" ,Dollar)
if proses == 2:
    Lira=int(input())
    Azn=Lira*0.090
    Dollar=Lira*0.053
    print("Lira : ", Lira)
    print("Azn: ", Azn)
    print("Dollar :" ,Dollar)
if proses == 3:
    Dollar=int(input())
    Azn=Dollar*1.7
    Lira=Dollar*18.82
    print("Dollar : " , Dollar)
    print("Azn:  ", Azn)
    print("Lira: " , Lira)
