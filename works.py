import  random
#SÜPER LOTO TEST
liste = [1, 8, 12, 40, 52, 56] #BU HAFTANIN SANŞLI NUMARALARI
sayici = 1
while(sayici<9):
    sayisal_loto = random.sample(range(1, 61), 6) # SENİN NUMARALARIN
    name = sorted(sayisal_loto)
    sayici +=1
    if(name == liste):
        print("You Winn!!", name)

    else:
        print("You Lost..", name)




