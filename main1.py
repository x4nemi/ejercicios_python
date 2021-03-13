from str import Str
# 1
# for i in range(2000, 3201):
#     if(i % 7 == 0 and i % 5 != 0):
#         print(i, end=", ")

# # 2
# f = 8
# for i in range(1, f):
#     f *= i
# print(f)

# # 3
# d = {}
# for i in range(1, 8):
#     d[i] = i ** 2
# print(d)

# 4
# valores = input("dame: ")
# lista = valores.split(",")
# t = tuple(lista)
# print(t)

#5
# p = Str()
# p.getStr()
# p.printStr()

#6
# valores_D = input("D: ")
# lista_D = valores_D.split(",")

# for i in lista_D:
#     q = (2 * 50 * int(i) / 30) ** 0.5
#     print(round(q), end=", ")

# 7
# x = int(input("x: "))
# y = int(input("y: "))

# m = [[0 for col in range(y)] for row in range(x)]

# for i in range(x):
#     for j in range(y):
#         m[i][j] = i * j

# print(m)

# # 8
# palabras = input("Dame: ")
# lista = palabras.split(",")
# lista.sort()
# print(lista)

# 9
cadena = input("Cadena: ")
print(cadena.upper())