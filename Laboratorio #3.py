print ("SIMULACION DE COLA MM1")
lambada = 2
mu= 3

print("Clientes atendidos:" , lambada , "por hora")
print("Llegada de Clientes estimado : ",  mu ,"por hora")
print("--------------------------------------------------------\n")


#numero promedio de pacientes en el sistema
def Ls():
    ls= (lambada) / (mu- lambada)
    print("Numero Promedio de de pacientes en el sistema:",ls, "Pacintes\n")
    
#tiempo total que consume un paciente en el consultorio
def Ws():
    ws= (1) / (mu- lambada)
    print("tiempo total que consume un paciente en el consultorio:",ws, "horas\n ")
   
#Factor de uso del Sistema
def P():
    global p 
    p= (lambada)/(mu)
    p1=p *100
    print("Factor de uso del Sistema: ",p1,"%\n")
    
#Numero Promedio de pacientes haciendo fila
def Lq():
    poten= pow(lambada, 2)
    lq=  poten /(mu* (mu-lambada))
    print("Numero Promedio de pacientes haciendo fila: ",lq,"pacientes\n")
    
#Probabiliad de que el consultorio este vacío
def P0():
    p0= (1-p)*100
    print("Probabiliad de que el consultorio este vacío ",p0,"%\n")

def P2():
#Probabiliad de halla 2 paceintes
    p2= (1-p)* pow(p, 2)
    p3= p2*100
    print("Probabiliad que de halla 2 paceintes en el consultorio",p3,"%\n")
    
    
Ls()
Ws()
P()
Lq()
P0()
P2()

