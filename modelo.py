class Jogo:

    def __init__(self, titulo, genero, classificacao_etaria, preco):
        self.titulo = titulo
        self.genero = genero
        self.classificacao_etaria = classificacao_etaria
        self.preco = preco

    def exibir_detalhes(self):
        print ("Título do jogo: ", self.titulo)
        print ("Gênero do jogo: ", self.genero)
        print ("Classificação etária do jogo: ", self.classificacao_etaria)
        print ("Preço do jogo: ", self.preco)


class jogador():
    def __init__(self, nickname, id, saldo_carteira):
        
        self.nickname = nickname
        self.id = id
        self.biblioteca = []
        self.saldo_carteira = saldo_carteira
    
    def exibir_perfil(self):
        print ("Nickname do jogador: ", self.nickname)
        print ("Id do jogador: ", self.id)
        print ("Saldo do jogador: ", self.saldo_carteira)
        print ("Jogos do jogador: ", self.biblioteca)
    
    def adicionar_jogo(self, Jogo):
        self.Jogo = Jogo
        self.biblioteca.append(Jogo)
    
    def adicionar_saldo(self):
        self.valor_deposito = float (input ("Quanto de saldo deseja adicionar a carteira? "))
        self.saldo_carteira += self.valor_deposito
        print ("Depósito concluído com sucesso! Saldo do jogador após saldo adicionado: ", self.saldo_carteira)

    def debitar_saldo(self):
        self.valor_saque = float (input ("Quanto de saldo deseja sacar da carteira? "))
        if (self.saldo_carteira < self.valor_saque):
            print ("Você não possui saldo suficiente para o saque.")
        else:
            self.saldo_carteira = (self.saldo_carteira - self.valor_saque)
            print ("Retirada concluída com sucesso! Saldo do jogador após saldo debitado: ", self.saldo_carteira)


jogador1 = jogador ("MGG", 123, 0)
Jogo1 = Jogo ("Valorant", "FPS", "14+", 0)
Jogo2 = Jogo ("Fortnite", "Battle Royale", "12+", 0)
jogador1.adicionar_jogo(Jogo1.titulo)
jogador1.adicionar_jogo(Jogo2.titulo)
jogador1.adicionar_saldo()
jogador1.debitar_saldo()
jogador1.exibir_perfil()
    


    
        
        
