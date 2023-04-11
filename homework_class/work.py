#sınıflar => classlar 
#modules
#paket yönetimi

class Human:
    name = "Melike"
    #built-in #constructor #initialize
    def __init__(self,name):
        self.name = name 
        print("Bir human instance'i üretildi")
    def __str__(self):
        return f"STR Fonksiyonundan dönen değer: {self.name}"
    def talk(self, sentence):
        print(f"{self.name}: {sentence}")
    def walk(self):
        print(f"{self.name} is walking..")

#instance 
human1 = Human("Burcu")
human1.talk("Merhaba")
human1.walk()
print(human1)



human2 = Human("Melike")
human2.talk("Selam")
human2.walk()
print(human2)