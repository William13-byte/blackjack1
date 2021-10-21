import random as ran
kortlek = []
test = "2"

def skapakortlek():
    
    global kortlek  
   
    
    kortnummer = ["Es","2","3","4","5","6","7","8","9","10",'Knäkt' , 'Dam' ,'Kung']
    minaSymbols = ["♣", "♦", "♥", "♠"]
    for nummer in range(len(kortnummer)):
        for symboler in range(len(minaSymbols)):
            kortlek.append(kortnummer[nummer]+minaSymbols[symboler] )
    return kortlek         
          
def visaKort(kortlek):
    print(kortlek) 
    return
def blandaKortLek(kortlek):
    
    nummer1 = 0     
    nummer2 = 0
    temp = 0
        
    for loop in range (1000):
       nummer1 = ran.random() * 52
       nummer1 = int(nummer1)
       nummer2 = ran.random() * 52
       nummer2 = int(nummer2)
       
       temp = kortlek[nummer1]
       kortlek[nummer1] = kortlek[nummer2]
       kortlek[nummer2] = temp 
    return kortlek      
    

    #return blandad
def TaEttKort(kortlek):
   
    taettkort = kortlek.pop(0)
    print(taettkort)
    
    return

#test 
test = str(input("1 , 2 , 3: ")) 
if test == '1':
    skapakortlek()
    visaKort(kortlek)
    
elif test == '2':
    skapakortlek()
    blandaKortLek(kortlek)     
    print(kortlek)
    
   
elif test == '3':
    skapakortlek()
    blandaKortLek(kortlek)
    TaEttKort(kortlek)                  
    


  


                
