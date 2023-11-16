import requests
import simplekml


class NewData():
    def __init__(self,data,**kwargs):
        for key,valor in data.items():
            setattr(self,key,valor)
        for key,value in kwargs.items():
            setattr(self,key,value)

    def get_cantidad(self):
        try:
            return getattr(self,'Cantidad')
        except:
            return None
            
    def __str__(self):
        encabezados = list(self.__dict__.keys())
        aux = str()
        for encabezado in encabezados:
            aux += f"{encabezado}: {getattr(self,encabezado)},  "
        return aux

# url = "https://gaia.inegi.org.mx/wscatgeo/geo/agebr/16"



def get_all_agee():
    """Realiza una consulta al servicio web de inegi y obtine info general de los agee"""
    url = "https://gaia.inegi.org.mx/wscatgeo/mgee/"
    res = requests.get(url)
    aux = []
    if not res.ok:
        return []
    for ele in res.json()["datos"]:
        aux.append(NewData(ele))
    return aux

def get_all_agems_for_agee(cve_agee):
    """Realiza una consulta al servicio web de inegi y obtine info general de los agem a 
    partir de un agee"""

    url = f"https://gaia.inegi.org.mx/wscatgeo/mgem/{cve_agee}"
    res = requests.get(url)
    aux = []
    if not res.ok:
        return []
    for ele in res.json()["datos"]:
        aux.append(NewData(ele))
    return aux

def get_all_localidades_for_agem(cve_agee, cve_agem):
    """Realiza una consulta al servicio web de inegi y obtine info general de las loacalidades
    a partir de un agee y un agem"""

    url = f"https://gaia.inegi.org.mx/wscatgeo/localidades/{cve_agee}{cve_agem}"
    res = requests.get(url)
    aux = []
    if not res.ok:
        return []
    for ele in res.json()["datos"]:
        aux.append(NewData(ele))
    return aux

def get_manzanas(cve_agee, cve_agem, cve_loc, tipo="U"):
    """Realiza una consulta al servicio web de inegi y obtine info vectorial de las manzanas
    a partir de un agee, un agem y una localidad"""

    aux = []
    url = f"https://gaia.inegi.org.mx/wscatgeo/geo/mza/{cve_agee}/{cve_agem}/{cve_loc}/{tipo}"
    res = requests.get(url)
    if not res.ok:
        return []
    datos = res.json()
    try:
        for ele in datos["features"]:
            propiedades = ele["properties"]
            propiedades["coordenadas"] = ele["geometry"]["coordinates"]
            aux.append(NewData(propiedades))
    except:
        pass
    return aux

def create_kml(cve_agee, cve_agem, cve_loc):
    urbanas = get_manzanas(cve_agee, cve_agem, cve_loc, "U")
    rurales = get_manzanas(cve_agee, cve_agem, cve_loc, "R")
    kml = simplekml.Kml()
    for ele in urbanas + rurales:
        pol = kml.newpolygon(name=f'{ele.cve_agee}/{ele.cve_agem}/{ele.cve_loc}/{ele.cve_ageb}/{ele.cve_mza}')
        pol.outerboundaryis = ele.coordenadas[0]
        # pol.innerboundaryis = ele.coordenadas[0]
    kml.save(f"{ele.nom_loc}.kml")


if __name__ == "__main__":
    for ele in get_all_agee():
        print (str(ele))    
