#para processos
from concurrent.futures import process
from multiprocessing import Process, Queue

#para threads
#from queue import Queue

class Consumidor(Process):
    
    def _init_(self,buffer):
        Process.__init__(self)
        self.buffer=buffer
        self.agregador = {}
        
    def _agregar(self,palavra):
        if(not palavra in self.agregador.keys()):
            self.agregador[palavra]= 0
            
        self.agregador[palavra] += 1
    
    def run(self):
        contando = True
        while(contando):
            palavra = self.buffer.get()
            if(palavra == "##FIM##"):
                contador = False
            else:
                self._agregar(palavra)
            
            print(f"Consumidor Finalizado{self.agregador}")
        
        