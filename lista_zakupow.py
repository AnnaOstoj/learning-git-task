lista_zakupow = {"piekarnia":["chleb","bulki","paczek"],\
                "warzywniak":["marchew","seler","rukola"]}
sum_of_products = 0

for item in lista_zakupow:
    produkty = ", ".join(lista_zakupow.get(item)).title()
    print(f"Idę do {str.capitalize(item)}, żeby kupić{produkty}")
    sum_of_products +=len(lista_zakupow.get(item))

print(f"W sklepie kupuję {sum_of_products} produktów")     
print("la la la")
for i in (100):
    if i % 3 == 0:
        print(i)
