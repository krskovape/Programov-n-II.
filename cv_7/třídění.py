# v knihovně pythonu
# sorted(list) - vrátí setříděnou kopii seznamu
# list.sort() - setřídí seznam
    # parametr key - podle čeho chceme třídit

data = [{"name": "Pavel", "age": 20}, {"name": "Anna", "age": 15}, {"name": "Betty", "age": 22}]

def name(item):
    return item["name"]

def age(item):
    return item["age"]

print(data)
#data.sort(key= name)
data.sort(key = lambda it : it["name"]) #zkratka pro psaní funkcí - teď funguje jako fce name
#data.sort(key = lambda it : it["properties"]["id"]) #u geojsonu
#data.sort(key = lambda it : it["coordinates"][0]) #podle první souřadnice
print(data)