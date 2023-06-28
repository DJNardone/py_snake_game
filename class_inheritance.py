class Animal():
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Breathe In, Breath Out.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("while underwater.")
    def swim(self):
        print("swim underwater.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)