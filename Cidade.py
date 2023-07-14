# Classe respónsavel pela cidade
# Ela recebe no seu constutor as cordenadas X e Y


class Cidade:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;
        
    def getX(self):
        return self.x;
    
    def getY(self):
        return self.y;
    