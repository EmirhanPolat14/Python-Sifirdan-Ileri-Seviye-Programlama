class Kareler():
    def __init__(self,maksimum):
        self.maksimum = maksimum
        self.sayi = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.sayi <= self.maksimum:
            sonuc = self.sayi ** 2
            self.sayi += 1
            return sonuc
        else:
            self.sayi = 1
            raise StopIteration

kareler = Kareler(5)

iteration = iter(kareler)

for i in kareler:
    print(i)
