class Cat():
    def __init__(self, name, color = ' white'):
        self.name = name
        self.color = color
    def meow(self, name = "나"):
        print("My name is : {}, my color {}, MEOW~ 주인은 {}"\
        .format(self.name, self.color,name))
        
nabi = Cat('나비','검은색')
nero = Cat('네로','흰색')
raon = Cat('라온','노랑색')
nabi.meow()
nero.meow()
raon.meow()