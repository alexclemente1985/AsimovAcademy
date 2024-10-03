class Dog:
    def __int__(self, raca):
        self.idade = 10
        self.raca = raca

    def envelhecer(self):
        print("Cachorro está ficando velho...")
        self.idade += 1
