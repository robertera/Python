
from multiprocessing import Process, Queue
import re

class Produtor(Process):
    
    def __init__(self,buffer,arquivoEntrada):
        Process.__init__(self)
        self.buffer = buffer
        self.arquivoEntrada = arquivoEntrada
        self.linhas = []
        self.palavras = []
        
    def _carregarArquivo(self):
        arquivo = open(self.arquivoEntrada,"rt")
        self.linhas=arquivo.readLines()
        
    def _processarLinhas(self):
        for linha in self.linhas:
            linha = re.sub(r"[^\w\s]","",linha)
            tokens = linha.split(" ")
            self.palavras.extend(tokens)
            
    def run(self):
        self._carregarArquivo()
        self._processarLinhas()
        for palavra in self.palavras:
            self.buffer.put(palavra)
        self.buffer.put("##FIM##")
        
        print("Produtor Finalizado")  