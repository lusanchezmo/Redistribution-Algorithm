
a = [["107-1",11],
    ["404",5],
    ["210",2],
    ["508",0],
    ["502",1],
    ["306",0],
    ["406",7],
    ["502_2", 8],
    ["305",3],
    ["506_2", 4],]


total=0
for sentinela in range(0,10):
  total+=a[sentinela][1]
adecuado=total//10

###Ordena la matriz de forma descendente.
for i in range(1,len(a)):
  for j in range(len(a) - i):
    if(a[j+1][1] > a[j][1]):
      mayor = a[j+1]
      a[j+1] = a[j]
      a[j] = mayor

###El casi incompresible algoritmo de redistribucion.

j=0
i=9
s=0
while(i>-1 and s<100000 and j<10):

  y=0
  while(a[i][1]<adecuado and a[j][1]>adecuado):
    a[i][1]+=1
    a[j][1]-=1
    y+=1
  
  if(y!=0):
    print("El ", a[i][0], " va por",y, "al ", a[j][0] )
  
  if(a[j][1]==adecuado):
    j+=1
  if(a[i][1]==adecuado):
    i-=1
