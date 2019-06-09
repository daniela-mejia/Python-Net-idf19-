#Daniela Mejia 04/25/2019
# design a class thta hold personal info 
#class
class perInfo:

    def __init__(self, name, address, age, phoneNum):
        self.name = name
        self.address = address
        self.age = age
        self.phoneNum = phoneNum

#method
    def fulldata(self):
        return 'Name:{},Address: {}, Age{}, PhoneNum=: {}'.format(self.name, self.address, self.age, self.phoneNum)

#data instance variables    
uno = perInfo('Dany Targaryen','Dragon Steet','29','63155555')
dos = perInfo('John Snow','Dead Road','32','96233332')
tres = perInfo('Sansa Stark','100 Winterfell Road','25','560000')


print(uno.fulldata())
print(dos.fulldata())
print(tres.fulldata())
