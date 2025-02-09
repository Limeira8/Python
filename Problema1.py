class User(object):
    # Construtor da classe, inicializa uma instância de User com nome, saldo e uma flag que indica se a conta é verificável.
    def __init__(self, nome, balance, checkacc):
        self.nome = nome
        self.balance = balance
        self.checkacc = checkacc
    
    # Método para transferir dinheiro de um usuário para outro
    def check(self, nome, sum):
        # Verifica se a conta do destinatário é verificável e se tem saldo suficiente para a transferência
        if not nome.checkacc or nome.balance < sum:
            raise ValueError()  # Lança uma exceção se a conta não é verificável ou saldo insuficiente
        # Processo de transferência
        self.balance += sum  # Adiciona o valor à conta do remetente
        nome.balance -= sum  # Subtrai o valor da conta do destinatário
        # Retorna uma string informando o novo saldo de ambos os usuários
        return self.nome + " has " + str(self.balance) + " and " + nome.nome + " has " + str(nome.balance) + "."
    
    # Método para sacar dinheiro
    def withdraw(self, draw):
        # Verifica se o saldo após o saque seria negativo
        if self.balance - draw < 0:
            raise ValueError()  # Lança uma exceção se o saldo não for suficiente
        else:
            self.balance -= draw  # Reduz o saldo pelo valor sacado
            return self.nome + " has " + str(self.balance) + "."  # Retorna o saldo após o saque
    
    # Método para adicionar dinheiro à conta
    def add_cash(self, sum):
        self.balance += sum  # Adiciona o valor ao saldo
        return self.nome + " has " + str(self.balance) + "."  # Retorna o saldo após a adição
