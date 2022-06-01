#verilen 2 sayının ebob ve ekok u
# inp = int(input("bir sayı giriniz:  "))
x = 20
# (1,2,3,4,.11.....19)
# for i in range(1,20):
#   if 20 % i == 0:
#     print(i)
inp1 = int(input("bir sayı giriniz:  "))
inp2 = int(input("bir sayı giriniz:  "))
mini = min(inp1, inp2)
# maxi = max(inp1, inp2)
for j in range(mini,1,-1):
  if inp1 % j == 0 and inp2 % j == 0 :
    print(j)
    break