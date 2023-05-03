for j in range(1,1000+1):
    contador=0
    for i in range(1,j+1):
        if j%i==0:
            contador+=1
    if contador==2:
        print(f"el numero {j} es primo ")
    else:
         print(f"no es primo el numreo {j}")