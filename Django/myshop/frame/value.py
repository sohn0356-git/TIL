class User:
    def __init__(self, id, pwd, name):
        self.id = id
        self.pwd = pwd
        self.name = name
    
    def __str__(self):
        return self.id+' '+self.pwd+' '+self.name
