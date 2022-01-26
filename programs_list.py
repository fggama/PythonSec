import subprocess
  
# traverse the software list
print("check_output")
Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
a = str(Data)
  
# try block
try:
    cont = 0
    # arrange the string
    print('-'*10,"list",'-'*10)
    for i in range(len(a)):
        print(a.split("\\r\\r\\n")[6:][i])
        cont += 1
  
except IndexError as e:
    print("All Done")
print("Aplicaciones instaladas: " + str(cont))