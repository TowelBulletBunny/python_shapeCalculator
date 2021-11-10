def CuboidVolume():
    length = int(input("Masukkan panjang : "))
    width = int(input("Masukkan lebar : "))
    height = int(input("Masukkan ketinggian : "))
    cuboidVolumeCalc = length*width*height
    return cuboidVolumeCalc

def SilinderVolume(pi):
    radius = int(input("Masukkan jejari : "))
    height = int(input("Masukkan ketinggian : "))
    circleBase = pi*radius**2
    silinderVolumeCalc = circleBase*height
    return silinderVolumeCalc

def ConeVolume(pi):
    radius = int(input("Masukkan jejari : "))
    height = int(input("Masukkan ketinggian : "))
    circleBase = pi*radius**2
    coneVolumeCalc = 1/3*circleBase*height
    return coneVolumeCalc

def SphereVolume(pi):
    radius = int(input("Masukkan jejari : "))
    sphereVolumeCalc = 4/3*pi*radius**3
    return sphereVolumeCalc

def Menu():
    print("*"*40)
    print(" "*7,"Menu Mengira Isi Padu"," "*7) 
    print("*"*40)
    print("1. Kuboid")
    print("2.Silinder")
    print("3. Kon")
    print("4. Sfera")
    print("*"*40)
    choose = int(input("Masukkan pilihan anda: [1 - 4] : "))
    return choose

def Calc(choose):
    if choose == 1:
        cuboidVolume = CuboidVolume()
        print("Isi padu ialah",cuboidVolume)
    elif choose == 2:
        silinderVolume = SilinderVolume(22/7)
        print("Isi padu ialah",silinderVolume)
    elif choose == 3:
        coneVolume = ConeVolume(22/7)
        print("Isi padu ialah",coneVolume)
    elif choose == 4:   
        sphereVolume = SphereVolume(22/7)
        print("Isi padu ialah",sphereVolume)
    else:
        print("This choice is unavailable")

resume = "y"

while resume == "y":
    chooseValue = Menu()
    Calc(chooseValue)
    resume = str(input("Type y to continue or n to stop: "))
    if resume == "n":
        break
    else:
        resume = str(input("This is not an option. Continue? [y/n] "))

while resume != "y" or "n":
    resume = str(input("This is not an option. Continue? [y/n] "))
        


print("Thanks for using the calculator.")

