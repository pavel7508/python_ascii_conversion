from time import time,sleep

a='='*30
print(a)
print('Převody ascii kodu na znaky a opačně')
print(a)
print('''Zadej svoji volbu:
1.Rozmezí ascii kodů
2.Zadávání znaků
3.Název v unicode sadě
4.Rozmezí znaků v unicode sadě
5.Konec''')
print(a)




def volba1():   
    b=int(input("Zadej počáteční číslo, od kterého se ascii kody zobrazí: "))
    c=int(input("Zadej konečné číslo ,do kterého se ascii kody zobrazí: "))
    asciikod={}
    for i in range(b,c+1):
        a=chr(i)
        asciikod.setdefault(i,a)
    print(asciikod)

def volba2():
    d=input('Zadej písmeno,jehož ascii kod se má zobrazit: ')
    e=ord(d)
    print('Ascii kod písmene ', d ,' je ', e )

def volba3():
    print( '''Tato volba má význam až pro čísla vyšší než 159''')
    f=int(input('Zadej číslo znaku , jehož název se má v Unicode sadě zobrazit: '))
    print('Znak s číslem ',f,' se jmenuje v sadě Unicode: ')
    g=chr(f)
    print(g.encode(encoding='ASCII',errors ='namereplace',))
    print('Zadané číslo znaku se zobrazí jak :',g)

def volba4():
    print('''Tato volba rozšiřuje možnosti  volby 3 ,kde je rozmezí kodů.''')
    h=int(input("Zadej kod vyšší než 159: "))
    j=int(input("Zadej kod, do kterého se seznam kodů vypsat: "))
    for k in range(h,j+1):
        g=chr(k)
        l=g.encode(encoding='ASCII',errors ='namereplace',)
        print('Znak s číslem {} se jmenuje v sadě Unicode: {} a vypada:{}'.format(k,l,chr(k)))
        
        sleep(1)
t=1
while t>0:
    
    try:    
        volba=int(input('Zadej svojí volbu : '))
        if volba == 1 :
            volba1()
        elif volba == 2 :
            volba2()
        elif volba == 3 :
            volba3()
        elif volba == 4 :
            volba4()
        elif volba ==5 :
            t=0
        
        else :
            print('Neplatná volba')
            t=1
        
            
    except:
            print('Neplatná volba')
            t=1

print('Konec programu')

