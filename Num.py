from person import Person
class Num(Person):
    def add(self):
        print(self.a)
        print(self._b)
        print(self._Person__c)

s1 = Num(1,2,3)
s1.add()