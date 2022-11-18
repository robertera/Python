from produtor import Produtor
from consumidor import Consumidor
from multiprocessing import Queue

if __name__ == '__main__':
    
    buffer = Queue(maxsize=2)
    arquivoEntrada = "entrada.txt"
    
    produtor = Produtor(buffer, arquivoEntrada)
    consumidor = Consumidor(buffer)
    
    produtor.start()
    consumidor.start()
    
    produtor.join()
    consumidor.join()
    
    print('Fim')
    