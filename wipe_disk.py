import os
import numpy
import psutil
import datetime
import ClassProgressBar

p = ClassProgressBar.ProgressBar('Borrando...')

def secure_delete(path, random_fill=True, null_fill=True, passes=3):
    """
    securely delete a file by passing it through both random and null filling
    """
    files = os.listdir(path)
    for i, f in enumerate(files):
        files[i] = "{}/{}".format(path, f)
    for item in files:
        with open(item, "wb") as data:
            length = data.tell()
            if random_fill:
                for _ in range(passes):
                    data.seek(0)
                    data.write(os.urandom(length))
            if null_fill:
                arr = [None] 
                a = numpy.repeat(arr, length)
                for _ in range(passes):
                    data.seek(0)
                    data.write(a)
        os.remove(item)


def wipe_disk(path):
    hdds = psutil.disk_partitions()
    maxfilesize = 0
    for part in hdds:
        if path == part.device:
            print(part.fstype)
            if part.fstype == "FAT32":
                maxfilesize = 100 * 1024 * 1024 # 4_278_188_032 #4_177_918 #4,294,967,296
            elif part.fstype == "NTFS":
                maxfilesize = (2**44)- (64*1024) #16_000_000_000 - 16_000

    print("[info]")
    print("\tTam. max.= %s bytes" % "{:,}".format(maxfilesize))
    hdd = psutil.disk_usage(path)
    print("\tLibre = %s bytes" % "{:,}".format(hdd.free))

    numfiles = hdd.free // maxfilesize
    print("\t# archivos = %s" % "{:,}".format(numfiles))
    passes = 1
    print("\t# repasos = %s" % "{:,}".format(passes))
    print("[+] inicio %s" % datetime.datetime.now())
    length = maxfilesize

    used = 0
    for idx in range(numfiles + 1):
        archivo = os.path.join(path, "tmp_%s" % '{:0>9}'.format(idx))
        p.message = "\tprocesando = %s" % archivo
        p.calculateAndUpdate(idx, numfiles+1)
        if hdd.free < used + length:
            length = hdd.free - used - 1
        used += length

        with open(archivo, "w+b") as data:
            for _ in range(passes):
                data.seek(0)
                data.write(os.urandom(length*8))

            # arr = [None] 
            # a = numpy.repeat(arr, length)
            # for _ in range(passes):
            #     # data.seek(length)
            #     # data.write(struct.pack("B",0))
                
            #     data.seek(0)
            #     data.write(s)

            data.flush()

    for idx in range(numfiles + 1):
        archivo = os.path.join(path, "tmp_%s" % '{:0>9}'.format(idx))
        os.remove(archivo)

    print
    print("[+] fin %s" % datetime.datetime.now())


wipe_disk("F:\\")