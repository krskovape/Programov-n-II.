from os import stat
import json

class Zona():
    def __init__(self, data):
        self.object_id = data["properties"]["OBJECTID"]
        self.category = data["properties"]["CATEGORY"]
        self.tariftext = data["properties"]["TARIFTEXT"]
        self.code = data["properties"]["CODE"]
    
    @classmethod
    def from_geojson(cls, file_name):
        try:
            with open(file_name, encoding="utf-8") as f:
                if stat(file_name).st_size == 0:
                    print("File is empty.")
                    quit()

                data = json.load(f)
                seznam = []
                tariftab2zona = {}
                #print(data)
                for item in data["features"]:
                    a = cls(item)
                    seznam.append(a)
                    tariftab2zona[item["properties"]["CODE"]] = a

            return seznam, tariftab2zona
                
        except FileNotFoundError:
            print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
            quit()
        except PermissionError:
            print(f"Program doesn't have permisson to access file {file_name}.")
            quit()

class Usek():
    def __init__(self, data, tariftab2zona):
        self.object_id = data["properties"]["OBJECTID"]
        self.zps_id = data["properties"]["ZPS_ID"]
        self.typzony = data["properties"]["TYPZONY"]
        self.zona : Zona = tariftab2zona.get(data["properties"]["TARIFTAB"])
        self.ps_zps = data["properties"]["PS_ZPS"]
    
    @classmethod
    def from_geojson(cls, file_name, dict_zony):
        try:
            with open(file_name, encoding="utf-8") as f:
                if stat(file_name).st_size == 0:
                    print("File is empty.")
                    quit()

                data = json.load(f)
                seznam = []
                for item in data["features"]:
                    a = cls(item, dict_zony)
                    seznam.append(a)
            return seznam
                
        except FileNotFoundError:
            print(f"Cannot open file {file_name}. The file does not exist or the path to the file is incorrect")
            quit()
        except PermissionError:
            print(f"Program doesn't have permisson to access file {file_name}.")
            quit()

file_useky = "cviceni\\cv_12\\DOP_ZPS_USEKY_p.json"
file_zony= "cviceni\\cv_12\\DOP_ZPS_ZonyStani_p.json"

zony, tariftab2zona = Zona.from_geojson(file_zony)
useky = Usek.from_geojson(file_useky, tariftab2zona)

print(useky[4].object_id)
print(useky[4].zona.tariftext)