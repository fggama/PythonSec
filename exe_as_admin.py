import sys
import ctypes

def ejecutar(programa):
    """ Ejecuta un programa Python como administrador """
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, programa, None, 1)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, 'open', sys.executable, programa, None, 1)


if __name__ == "__main__":
    print('Ejecutando %s' % ' '.join(sys.argv[1:]))
    ejecutar(' '.join(sys.argv[1:]))