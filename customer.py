from atm_card import ATMCard
class Customer(ATMCard):
    def __init__(self, id, custPin = 1234, custBalance = 10000):
        self.id = id
        self.Pin = custPin
        self.Balance = custBalance
    def id_customer (self):
        return self.id
    def Pin_customer (self):
        return self.Pin
    def Saldo_awal (self):
        return self.Balance
    def debit (self, nominal):
        self.Balance -= nominal
    def simpan (self, nominal_simpan):
        self.Balance += nominal_simpan