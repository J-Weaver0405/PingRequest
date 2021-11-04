
class Money():
    def __init__(self, dollars, cents):
        self._dollars = dollars
        self._cents = cents
        
    def __str__(self ):
        return f"{self._dollars}dollars and {self._cents} cents"
    
    def __repr__(self):
        return 'Money(%s, %s)' % (self._dollars, self._cents)
    
    @property(self)
    def get_dollars(self):
        return self._dollars
    
    @dollars.setter
    def set_dollars(self, dollar_amt):
        if dollar_amt < 0:
            raise ValueError("Dollars cant be negative")
        self._dollars = dollar_amt
        
    @property(self)
    def get_cents(self):
        return self._cents
    
    @cents.setter
    def set_cents(self, cents_amt):
        if cents_amt < 0:
            raise ValueError("Dollars cant be negative")
        self._cents = cents_amt
        
    def __eq__(self):
        print("other", other)
        if self.dollars == other.dollars and self.cents == other.cents:
            return True
        return False
    
    def __add__(self,other):
        return Money(self.dollars + other.dollars, self.cents + other.cents)
    
    def __gt__(self, other):
        self_left = self.dollars + self._cents
        sum_right = other.dollars + other.cents
        if sum_left > sum_right:
            return True
        return False
    
    def __lt__(self, other):
        self_left = self.dollars + self._cents
        sum_right = other.dollars + other.cents
        if sum_left < sum_right:
            return True
        return False
    
    def __ge__(self, elem):
        self_left = self.dollars + self._cents
        sum_right = other.dollars + other.cents
        if sum_left >= sum_right:
            return True
        return False
    
    def __le__(self, other):
        self_left = self.dollars + self._cents
        sum_right = other.dollars + other.cents
        if sum_left <= sum_right:
            return True
        return False
        
    
if __name__ == '__main__':
    money1 = Money(10, 50)
    money1 = Money(20, 75)
    print(money1)
    print(money2)
    print(money1 > money2)