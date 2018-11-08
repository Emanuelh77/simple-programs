class Dog:
    def __init__(self, breed, age, color):
        self.breed = breed
        self.age = age
        self.color = color
        self.status = "active"

    def bark(self):
        print("ruff")

    def play(self):
        self.status = "tired"

    def rest(self):
        self.status = "active"

#Examples:

Bruce = Dog("labrador",5,"black")

print(Bruce.breed)
#Bruce.play()
#print(Bruce.status)
Bruce.rest()
print(Bruce.status)
