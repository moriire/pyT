class Table:
    def __init__(self, *data,**kdata):
        self.data = data
        self.kdata = kdata
        if self.data:
            self.width = max([len(j) for j in self.data[0]])+2
            self.l = len(self.data[0])
            if isinstance(self.data[0], dict):
                header = self.data[0].keys()
                self.info = list(map(lambda x: tuple(x.values()), self.data))
                self.info.insert(0, tuple(header))
                
            elif isinstance(self.data[0], (tuple, list)):
                header = self.data[0]
                self.info = self.data[0:]
                
        elif self.kdata:
            header = self.kdata.keys()
            self.data =list(zip(*self.kdata.values()))
            self.data.insert(0, tuple(header))
            self.width = max((len(j) for j in header))+2
            self.l = len(header)
                
        self.sym = f"{self.width * '-'}+"

    def __mul__(self):
            return self.sym*(self.l-1)

    def __str__(self):
            return self.__mul__()

    def row(self, *row):
        out = "+"
        for s in row:
            out += f"{str(self)}"
        return out
    
    def _pos(self, u,v):
        bef, aft = (u-v)//2, (u-v)-((u-v)//2)
        return bef, aft
    
    def col(self, *row):
        out = "|"
        for s in row:
            out += f"{' '*self._pos(self.width, len(s))[0]}{s}{' '*self._pos(self.width, len(s))[1]}|"
        return out

    def comp(self, *row):
        return f"{self.row(*row)}\n{self.col(*row)}\n"

    def draw(self):
        st = ""
        for t in self.info:
            st+=self.comp(*t)
        st+=self.row(*t)
        return st
    @staticmethod
    def CSV(file):
        with open(file) as f:
            read = f.read().replace(',,', ',None,None')
            lines = read.split('\n')
            return lines
    
    @staticmethod
    def JSON(file):
        z = []
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                z.append(line.strip())
        return z
        
    
#a=Table(adewale=['adewale', '0'], cet=['adewale', 'adewale'], jit=['adewale', 'adewale'])
#a=Table({'name':'adewale', 'surname':'0'}, {'name':'adewale', 'surname':'0'},{'name':'adewale', 'surname':'0'})
a=Table(('adewale', 'adewa1hfhfhle'),('adewale', 'adewale'))
#print(a.draw())
v=Table.CSV('C:/Users/Mobolaji/Downloads/contacts.csv')
print(Table(*v))
