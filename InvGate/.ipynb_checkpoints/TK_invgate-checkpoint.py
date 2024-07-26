
def renombrar():
    import os
    import re
    
    directorio ="G:/Unidades compartidas/SOC/Central Puerto/Controles SOX/2024/03 - Marzo/03 Mensuales/03 NET/solicitudes/CISCO"
    os.chdir(directorio)
    tks = os.listdir()
    regla_de_busqueda = "\#\d{5}"

    for i in tks:
        text = re.findall(regla_de_busqueda,i)
        try:
            os.rename(i, str(text[0]) + ".pdf")
        except:
            pass
    

if __name__ == '__main__':
    renombrar()
