#Importando Bibliotecas
from pyspectator.computer import Computer 
from pyspectator.processor import Cpu
from time import sleep
from  easygui  import  * 
import os

# Variaveis

computer = Computer()
cpu = Cpu(monitoring_latency = 1)
a = "º"
title = "Toma Cuidado"
msg = "O processador chegou aos 70º Graus, Deseja continuar ou suspender o computador?"
image = "cpuqueima.png"

#Imprimindo informações do processador
print("----------------------------------------")
print(computer.processor.name)
print("----------------------------------------")
    
with cpu:   
 
    for _ in range(1000000000):
       re = cpu.temperature
       print("----------------------------------------|")
       sleep(1.1)
       if(re <=50):
         print("Processador: "+ str(re)+ str(a), "Normal")
       else:
         if ccbox(msg, title, image=image):
            pass  
            print("Processador: "+ str(re)+ str(a), "Perigo")
         else:  
            os.system("systemctl suspend") #comando do linux, vai suspender o computador
            exit()

        
    