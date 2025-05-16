class Jogo: 
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

class Jogador:
    def __init__(self, nickname, id_jogador, saldo_carteira=0.0):
        self.nickname=nickname
        self.id_jogador=id_jogador
        self.biblio_jogos= []
        self.saldo_carteira=saldo_carteira

    def exibir_perfil(self):
        print("nickname:", self.nickname)
        print("ID:", self.id_jogador)
        print("saldo da carteira:", self.saldo_carteira)
        print("biblioteca:", self.biblio_jogos)


    def adicionar_jogo_biblioteca(self,jogo_comprado):
        #self.jogo= jogo
        self.biblio_jogos.append(jogo_comprado)
        print(jogo_comprado.titulo, "adicionado à biblioteca")
        

    # def adicionar_saldo(self,valor_deposito, jogo_comprado):
    #     self.valor_deposito =  input ("Quanto de saldo deseja depositar?")

    #     if valor_deposito>0:
    #         self.saldo_carteira += valor_deposito
    #         print("debito realizado!! Saldo do jogador:", self.saldo_carteira)
    #     else:
    #         print("Saldo insulficiente")

    #     self.saldo_carteira += valor_deposito
    #     print("deposito adicionado!! Saldo do jogador:", self.saldo_carteira)

    # def debitar_saldo(self,valor_debito,saldo_carteira):
    #     self.valor_debito =  input ("Quanto de saldo deseja debitar?")

    #     if valor_debito <= self.saldo_carteira:
    #         self.saldo_carteira = saldo_carteira - valor_debito
    #         print("debito realizado!! Saldo do jogador:", self.saldo_carteira)
    #     else:
    #         print("Saldo insulficiente")

    def adicionar_saldo(self):
        valor_deposito =  float(input ("Quanto de saldo deseja adicionar?"))

        if valor_deposito>0:
            self.saldo_carteira+=valor_deposito
            # print("deposito de:", valor_deposito,"\ne valor da carteira agr:", self.saldo_carteira)
        else:
            print("valor invalido")

    def debitar_valor(self, valor):
            if valor <= self.saldo_carteira:
                self.saldo_carteira -= valor
                # print("débito realizado no valor de:", valor, "\nvalor da carteira agr: ", self.saldo_carteira)
                print("\nvalor da carteira agr: ", self.saldo_carteira)
                return True
            else:
                print("saldo insuficiente\n")
                return False

    def debitar_saldo(self):
        valor_debito =  float(input("Quanto de saldo deseja debitar?"))
        self.debitar_valor(valor_debito)
#meio q precisa desses dois, tipo facilita, o segundo nn é obrigatorio acho mas é legal colocar, o primeiro precsisa msm(precisamos dps no "realizar compra" os valores de true ou false), da pra tirar esse segundo mas ai teria que definir em algum lugar(no final acho) o valor

class PlataformaDeJogos:

    def __init__(self,nome_plataforma):
        self.nome_plataforma = nome_plataforma
        self.catalogo_jogos = []
        self.jogadores_cadastrados = []

    def adicionar_jogo_catalogo(self,jogo):
        self.catalogo_jogos.append(jogo)
        print(jogo.titulo, "adicionado ao catalogo")

    def adicionar_jogador(self, jogador):
        self.jogadores_cadastrados.append(jogador)
        print(jogador.nickname, "adicionado")

    def buscar_jogo_por_titulo(self, titulo_jogo):
        for jogo in self.catalogo_jogos:
            if jogo.titulo == titulo_jogo:
                return jogo
        return None
    #????

    def buscar_jogador_por_id(self, id_jogador_busca):
        for jogador in self.jogadores_cadastrados:
            if jogador.id_jogador == id_jogador_busca:
                return jogador
        return None

    #?
    #metodo de busca
    # def busca_sequencial(lista, item):
    #     for i in range(len(lista)):
    #         if lista[i] == item:
    #             return i  # Retorna o índice do item
    #     return -1  # Retorna -1 se o item não for encontrado

    def Listar_jogos_catalogo(self):
        if not self.catalogo_jogos:
            print("nenhum jogo no catalogo")
        for jogo in self.catalogo_jogos:
            jogo.exibir_detalhes()



    # Verifique se o jogador já possui o jogo em sua biblioteca_de_jogos.
    # (Dica: itere pela biblioteca do jogador e compare os títulos ou os
    # próprios objetos).
    # • Se não possuir, verifique se o jogador_obj.saldo_carteira é suficiente
    # para o jogo_obj.preco.
    # • Se tiver saldo, chame jogador_obj.debitar_saldo(jogo_obj.preco). Se
    # o débito for bem-sucedido:
    # • Chame jogador_obj.adicionar_jogo_biblioteca(jogo_obj).
    # • Imprima uma mensagem de "Compra realizada com sucesso!".
    # • Caso contrário (sem saldo, já possui, jogo/jogador não encontrado),
    # imprima mensagens de erro apropriadas.

    def realizar_compra(self, id_jogador_comprador, titulo_jogo_desejado):
        jogador_obj=self.buscar_jogador_por_id(id_jogador_comprador)
        jogo_obj=self.buscar_jogo_por_titulo(titulo_jogo_desejado)

        if not jogador_obj or not jogo_obj:
            print("jogador ou jogo não encontrado")
            return
        if jogo_obj in jogador_obj.biblio_jogos:
            print("o jogador ja tem esse jogo")
            return  #pelo visto seria uma  guard clause

        if jogador_obj.debitar_valor(jogo_obj.preço):
            jogador_obj.adicionar_jogo_biblioteca(jogo_obj)
            print("Compra realizada com sucesso!")
        # else:
        #     print("saldo insuficiente")



# print("\n")
# plataforma=PlataformaDeJogos("Steam")

# j1=Jogo("minecraft", "simulação", "livre", 120.0)
# j2=Jogo("The Sims", "simulaçaõ", "+12", 90.0)
# plataforma.adicionar_jogo_catalogo(j1)
# plataforma.adicionar_jogo_catalogo(j2)

# jogador1= Jogador("xxXxx", 123456)
# jogador2=Jogador("uuUuu", 987654)
# plataforma.adicionar_jogador(jogador1)
# plataforma.adicionar_jogador(jogador2)

# #teste
# jogador1.saldo_carteira = 150.0 
# print("saldo do jogador1:", jogador1.saldo_carteira)


# print("\njogos no catálogo:")
# plataforma.Listar_jogos_catalogo()

# plataforma.realizar_compra(jogador1.id_jogador, "Minecraft")

# print("\nPerfis dos jogadores:") #//
# jogador1.exibir_perfil()

# aqui o pra cima rascunho inicial parte 4



# Instância da plataforma
plataforma = PlataformaDeJogos("Steam")

jogo1 = Jogo("Minecraft", "Simulação", "Livre", 120.0)
jogo2 = Jogo("The Sims", "Simulação", "+12", 90.0)
plataforma.adicionar_jogo_catalogo(jogo1)
plataforma.adicionar_jogo_catalogo(jogo2)

jogador1 = Jogador("xxXxx", 123456)
jogador2 = Jogador("uuUuu", 987654)
plataforma.adicionar_jogador(jogador1)
plataforma.adicionar_jogador(jogador2)

# jogador1.saldo_carteira = 150.0  # saldo direto para teste rápido
jogador1.adicionar_saldo()
jogador1.debitar_saldo()
# print(f"Saldo do jogador1: {jogador1.saldo_carteira}")
print("saldo do jogador1:", jogador1.saldo_carteira)

print("\njogos:?")
plataforma.Listar_jogos_catalogo()

print("\nrealizar compra do jogador1 minecraft?")
plataforma.realizar_compra(jogador1.id_jogador, "Minecraft")

print("\nperfil atualizado")
jogador1.exibir_perfil()



print("\ntentativas")
print("jogador1 tenta realizar a compra novamente")
#tentativa do jogador1 comprar dnv(deve falhar)
plataforma.realizar_compra(jogador1.id_jogador, "Minecraft")


#agr o jogador2 nao tem saldo e tenta comprar The Sims(deve falhar)
print("\njogador2 tentando comprar The Sims sem saldo:")
plataforma.realizar_compra(jogador2.id_jogador, "The Sims")

jogador2.exibir_perfil()
#aqui ele adiciona saldo e dps tem que fiuncionar
# jogador2.saldo_carteira = 100.0
jogador2.adicionar_saldo()
print("saldo do jogador2:", jogador1.saldo_carteira)

plataforma.realizar_compra(jogador2.id_jogador, "The Sims")

print("\nperfil atualizado")
jogador2.exibir_perfil()


