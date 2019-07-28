import json

class Plate:
    def __init__(self, serial):
        self.serial = serial

    def toDict(self):
        return {"serial": self.serial}

class PlateList:
    def append(self, plate):
        plates_list = []
        
        with open('plates.json') as f:
            plates_list = json.load(f)
            
        plates_list.append(plate.toDict())
        
        with open('plates.json', 'w') as f:
            json.dump(plates_list, f)

        return

    def get_list(self):
        plates_list = None

        with open('plates.json') as f:
            plates_list = json.load(f)

            plates_list = [Plate(p['serial']) for p in plates_list]
        
        return plates_list
            
