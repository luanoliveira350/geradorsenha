import speedtest

teste = speedtest.Speedtest()

def bytes_para_mb(bytes):
    KB = 1024
    MB = KB *1024
    return int(bytes/MB)

velocidade = bytes_para_mb(teste.download())
print("A velocidade da sua internet é ", velocidade,"MB")