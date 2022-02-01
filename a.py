class ball:

    def __init__(self,no,name):
        self.no=no
        self.name=name

    def __sub__(self,another):
        return self.no-another.no

    def __str__(self):
        return  "{}".format(self.name)

b1=ball(20,"football")
b2=ball(14,"cricketball")
print(b1)
print(b2)