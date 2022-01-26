import winreg

def foo(hive, flag):
    aReg = winreg.ConnectRegistry(None, hive)
    aKey = winreg.OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | flag)

    count_subkey = winreg.QueryInfoKey(aKey)[0]

    software_list = []

    for i in range(count_subkey):
        software = {}
        try:
            asubkey_name = winreg.EnumKey(aKey, i)
            asubkey = winreg.OpenKey(aKey, asubkey_name)
            software['name'] = str(winreg.QueryValueEx(asubkey, "DisplayName")[0]).strip()

            try:
                software['version'] = winreg.QueryValueEx(asubkey, "DisplayVersion")[0]
            except EnvironmentError:
                software['version'] = 'undefined'
            try:
                software['publisher'] = winreg.QueryValueEx(asubkey, "Publisher")[0]
            except EnvironmentError:
                software['publisher'] = 'undefined'
            software_list.append(software)
        except EnvironmentError:
            continue

    return software_list

software_list = foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY)\
        + foo(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY)\
        + foo(winreg.HKEY_CURRENT_USER, 0)

newlist = sorted(software_list, key=lambda d: d['name']) 

softFile = open('softLog.log', 'w')

for software in newlist:
    softFile.write('Name=%s, Version=%s, Publisher=%s\n' % (software['name'], software['version'], software['publisher']))

softFile.write('Aplicaciones instaladas: %s' % len(software_list))
softFile.close()

print('Aplicaciones instaladas: %s' % len(software_list))