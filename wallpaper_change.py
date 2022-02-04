import winreg as wreg
import os
import sys
import imghdr

def read_reg():
    """ Lectura de Windows Registry """
    with wreg.ConnectRegistry(None, wreg.HKEY_CURRENT_USER) as hive:
        with wreg.OpenKey(hive, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", 0, wreg.KEY_READ) as hosts_key:
            num_of_values = wreg.QueryInfoKey(hosts_key)[1]
            for i in range(num_of_values):
                values = wreg.EnumValue(hosts_key, i)
                print(values)

def write_reg(filename):
    """ Escritura de Windows Registry """
    key = wreg.OpenKey(wreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System", 0, wreg.KEY_SET_VALUE | wreg.KEY_WOW64_64KEY)
    wreg.SetValueEx(key, "Wallpaper", 0, wreg.REG_SZ, filename)
    wreg.SetValueEx(key, "Picture", 0, wreg.REG_SZ, filename)

def restart_service():
    """ Reinicia servicio Explorer.exe"""
    os.system("taskkill /im explorer.exe /F")
    os.system("start explorer.exe")

if __name__ == "__main__":
    """ Cambia el Wallpaper en el registry, ejecutar con 'exe_as_admin.py'
    ejemplo: 
    py exe_as_admin.py wallpaper_change.py "C:\Users\garciafr\Pictures\pexels-sebastiaan-stam-1482476.jpg"
    py exe_as_admin.py wallpaper_change.py "C:\Users\garciafr\Pictures\pexels-sebastiaan-stam-1097456.jpg"
    """
    archivo = ' '.join(sys.argv[1:])
    if  os.path.isfile(archivo) and imghdr.what(archivo) != None:
        write_reg(archivo)
        restart_service()
    else:
        print('Archivo "%s" no encontrado!' % archivo)