import winreg as wreg
import os
import sys
from PIL import Image

wallpaper_key=r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"

def read_reg():
    """ Lectura de Windows Registry """
    print("Valores actuales")
    with wreg.ConnectRegistry(None, wreg.HKEY_CURRENT_USER) as hive:
        with wreg.OpenKey(hive, wallpaper_key, 0, wreg.KEY_READ) as hosts_key:
            num_of_values = wreg.QueryInfoKey(hosts_key)[1]
            for i in range(num_of_values):
                values = wreg.EnumValue(hosts_key, i)
                print(values)
            print("""Center	0\nFill	4\nFit	3\nSpan	5\nStretch	2\nTile	1""")

def write_reg(filename):
    """ Escritura de Windows Registry """
    try:
        key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, wallpaper_key, 0, wreg.KEY_SET_VALUE | wreg.KEY_WOW64_64KEY)
        wreg.SetValueEx(key, "Wallpaper", 0, wreg.REG_SZ, filename)
        wreg.SetValueEx(key, "Picture", 0, wreg.REG_SZ, filename)
        return True
    except Exception as ex:
        print("Error:", ex)
        return False

def restart_service():
    """ Reinicia servicio Explorer.exe"""
    os.system("taskkill /im explorer.exe /F")
    os.system("start explorer.exe")

if __name__ == "__main__":
    """ Cambia el Wallpaper en el registry, ejecutar con 'exe_as_admin.py' o en una ventana como Administrador """
    
    dir = ' '.join(sys.argv[1:])
    if len(dir.strip()) == 0:
        dir = r'C:\Users\garciafr\Pictures'

    print("Directorio de imagenes: ", dir)
    print()
    cont = 0
    arch_dict = {}

    for arch in os.listdir(dir):
        if arch.endswith(".jpg"):
            archivo = os.path.join(dir,arch)
            im = Image.open(archivo)
            if im.size[0] > 1000:
                arch_dict[str(cont)] = arch
                print(cont,":",arch, im.size)
                cont += 1

    sel = input('Seleccione una imagen: ')
    try:
        archivo = os.path.join(dir,arch_dict[sel])
        if len(archivo.strip()) > 0 and os.path.isfile(archivo):
            if write_reg(archivo):
                restart_service()
                read_reg()
    except:
        print("\nOpcion invalida")