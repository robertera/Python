from concurrent.futures import process
from multiprocessing import Process, Queue

class Produtor(Process):
    
    def _init(self,buffer,arquivoEntrada):
        Process.__init__(self)
        self.buffer = buffer
        self.arquivoEntrada = arquivoEntrada
        self.linhas = []
        self.palavras = []
        
    def carregarArquivo(self):
        arquivo = open(self.arquivoEntrada,"rt")
        self.linhas=arquivo.redLines()
        
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
            print(f"Produtor Finalizado")  