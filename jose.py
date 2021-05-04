dimension = int(input("Ingrese la dimension del vector: "))

n_array = []

for i in range (dimension):
  if((i+1) >= 2):
      n_array.append("x^"+str(i+1))  
  else:
      n_array.append("x")
     

print(n_array)