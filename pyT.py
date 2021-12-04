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

    def __str__(self):
            return self.sym

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
    def JSON(file, obj):
        import json
        with open(file) as f:
            data = json.dump(f.read())
        return data[obj]

    @staticmethod
    def HTML(file, n=0):
        from bs4 import BeautifulSoup as soup
        proc = [], []
        with open(file) as f:
            data = f.read()
            bs = soup(data, "html.parser").find_all("table")[n].findAll("tr")
            for tr in bs:
                proc[0].append(tr.select("td") or tr.select("th"))
        for td in proc[0]:
            proc[1].append(tuple(map(lambda x: x.get_text().strip(),  td)))
        return proc[1]
        
 
