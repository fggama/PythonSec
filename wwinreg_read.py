import winreg
import base64
from struct import *
from codecs import decode

if __name__ == "__main__":
    with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as hive:
        with winreg.OpenKey(hive, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs", 0, winreg.KEY_READ) as hosts_key:
            num_of_values = winreg.QueryInfoKey(hosts_key)[1]
            for i in range(num_of_values):
                values = winreg.EnumValue(hosts_key, i)
                print("-" * 20)
                ba = bytearray(values[1])
                # print(decode(values[1], "windows-1252", "ignore"))

                # decodedBytes = base64.b64decode(values[1].hex())
                #  print(decodedBytes)
                decodedStr = str(values[1], "windows-1252")
                print(decodedStr)

                # valor = values[1].decode(encoding="windows-1252")
                # print(type(values[1]))
