class User:
    def __init__(self, id, pwd, name):
        self.id = id
        self.pwd = pwd
        self.name = name
    
    def __str__(self):
        return self.id+' '+self.pwd+' '+self.name


class Item:
    def __init__(self, id, name, price, regdate, imgname):
        self.id = id
        self.name = name
        self.price = price
        self.imgname = imgname
        self.regdate = regdate
   
    
    def __str__(self):
        return str(self.id)+' '+self.name+' '+str(self.price)+' '+self.imgname+' '+str(self.regdate)
