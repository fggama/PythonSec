import sys
 
class ProgressBar(object):

    def __init__(self, message, width=20, progressSymbol=u'▣ ', emptySymbol=u'□ '):
        self.width = width
    
        if self.width < 0:
            self.width = 0
        
        self.message = message
        self.progressSymbol = progressSymbol
        self.emptySymbol = emptySymbol

    def update(self, progreso):
        """ Actualiza e imprime valores """
        totalBlocks = self.width
        filledBlocks = int(round(progreso / (100 / float(totalBlocks)) ))
        emptyBlocks = totalBlocks - filledBlocks
        
        progressBar = self.progressSymbol * filledBlocks + \
        self.emptySymbol * emptyBlocks
        
        if not self.message:
            self.message = u''
        
        mensaje = u'\r{0} {1} {2}%'.format(self.message,progressBar,progreso)
        
        sys.stdout.write(mensaje)
        sys.stdout.flush()
        
    def calculateAndUpdate(self, hecho, total):
        """ Calcula los nuevos valores y los actualiza """
        progreso = int(round( (hecho / float(total)) * 100) )
        self.update(progreso)