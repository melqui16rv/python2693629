import random
tam=random.randint(15,20)
list=[random.randrange(0,9) for i in range(tam)]
print(list)

num=int(input('digite un numero de 0 a 9: '))

repe = 0
for n in list:
    if n == num:
        repe += 1

print(f'El numero {num} se repite {repe} en la lista')



#if num not in list:
#    print(f'El numero {num}no serepite')
#else:
#    print(f"El numero {num} si se repite")
    
    
    
    
    
    
    
    
"""if num==i or num==j:
    num==1+=repe
    print('si',j)
else:
    num!=i
    num!=j
    print('no' ,j)
print(f"se repite {repe} el numero {num} ")"""
    



#for i in range(len(list)):
#    if num==list:
#        repe+=1
    

   # for j in range (i+1,tam):


#    if num==j:
#        repe+=1
#print("se repite: ", repe)





