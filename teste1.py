class jogo: 
    def __init__(self, titulo, genero,classificaçao,preço):
        self.titulo = titulo
        self.genero = genero
        self.classificaçao = classificaçao
        self.preço = preço


    def exibir_detalhes(self):
        print("Titulo de jogos:", self.titulo)
        print("Genero:", self.genero)
        print("Classificação etária:", self.classificaçao)
        print("Preço:", self.preço)

class jogador:
    def __init__(self, nickname, id_jogador, saldo_carteira,biblio_jogos):
        self.nickname=nickname
        self.id_jogador=id_jogador
        self.bilio_jogos= []
        self.saldo_carteira=saldo_carteira

    def exibir_perfil(self):
        print("nickname:", self.nickname)
        print("ID:", self.id_jogador)
        print("saldo da carteira:", self.saldo_carteira)
        print("biblioteca:", self.bilio_jogos)

    def adicionar_jogo(self,jogo):
        #self.jogo= jogo
        self.biblio_jogos.append(jogo)
        

    def adicionar_saldo(self,valor_deposito):
        self.valor_deposito =  input ("Quanto de saldo deseja depositar?")
        self.saldo_carteira += valor_deposito
        print("deposito adicionado!! Saldo do jogador:", self.saldo_carteira)

    def debitar_saldo(self,valor_debito,saldo_carteira):
        self.valor_debito =  input ("Quanto de saldo deseja debitar?")

        if valor_debito <= saldo_carteira:
            self.saldo_carteira = saldo_carteira - valor_debito
            print("debito realizado!! Saldo do jogador:", self.saldo_carteira)
        else:
            print("Saldo insulficiente")


class plataforma_de_jogos:

    def __init__(self,nome_platarforma,catalogo_jogos,jogadores_cadastrados):
        self.nome_plataforma = nome_platarforma
        self.catalogo_jogos = []
        self.jogadores_cadastrados = []

    def adicionar_jogo_catalogo(jogo):
        

        









# meu_jogo1 = jogo("minecraft", "simulacao", "livre", 100)

# jogador1 = jogador("red",1,1000)

# jogador1.bilio_jogos.append(meu_jogo1)

# meu_jogo2 = jogo("minecraft2", "simulacao", "livre", 100)
    
# jogador1.bilio_jogos.append(meu_jogo2)

#for i in jogador1.bilio_jogos:
#    print(i.titulo)

        
    

