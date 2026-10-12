#10 
#12.10. 
#kmitani kulicky
import time 
import math 
pocet = 8 
print("Kulička jede") 
for i in range(pocet): 
    print(" " * i + "O") 
    time.sleep(0.1) 
for i in range(pocet): 
    print(" " * (pocet - i) + "O") 
    time.sleep(0.1) 
print("tabulka") 
for i in range(1, pocet + 1): 
    print(i, i*i, math.sqrt(i))