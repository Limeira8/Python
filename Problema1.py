class User(object):

    def __init__(self, nome, balance, checkacc):
        self.nome = nome
        self.balance = balance
        self.checkacc = checkacc
    
    def check(self, nome, sum):
        if not nome.checkacc or nome.balance < sum:
            raise ValueError()
        self.balance += sum
        nome.balance -= sum
        return self.nome + " has " + str(self.balance) + " and " + nome.nome + " has " + str(nome.balance) + "."
    
    def withdraw(self, draw):
        if self.balance - draw < 0:
            raise ValueError()
        else:
            self.balance -= draw
            return self.nome + " has " + str(self.balance) + "."
    
    def add_cash(self, sum):
        self.balance += sum
        return self.nome + " has " + str(self.balance) + "."