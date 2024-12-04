class Meucantinho:
    def __init__(self): # o __init__ eh a sinalizacao pra o inicio do sistema
        self.catalogo = {
            'Linha grande':6.00,
            'Agulha pequena':0.50,
            'Agulha grande':0.50,
            'Linha pequena':2.00,
            'Linha de croche':15.00
        }
        self.carrinho={}
        self.total=0.00
    
    
    def comprar(self):
        while True:
            print('Catalogo do produtos:')
            for produto, preco in self.catalogo.items():
                print(f'{produto.capitalize()} - R${preco:.2f}')

            escolha=input('Digite o nome do produto que deseja comprar (ou "sair" para encerrar):')
            if escolha.lower() == 'sair':
                break
            
            if escolha in self.catalogo:
                quantidade=int(input ('Digite a quantidade desejada: '))
                if escolha in self.carrinho:
                    self.carrinho[escolha] += quantidade
                else:
                    self.carrinho[escolha] = quantidade
                print(f'{quantidade} unidade de {escolha.capitalize()} adicionadas ao carrinho. ')
            else:
                print('Produtos nao encontrado no catalogo, tente novamente.')

        print('\nResumo da compra ')
        for produto, quantidade in self.carrinho.items():
            preco_unitario=self.catalogo[produto]
            preco_total=preco_unitario * quantidade
            print(f'{quantidade} unidade de {produto.capitalize()} - R${preco_total: .2f}')
            self.total += preco_total

        print(f'Total de compras: R${self.total:.2f}')
        self.pagar
    
    def pagar(self):
        pagamento=input('Digite o valor recebido pelo cliente (ou "cancelar" para cancelar a compra)')
        if pagamento.lower() == 'Cancelar':
            print('Compra cancelada.')
            return
        
        valor_pago=float(pagamento)
        troco = valor_pago - self.total

        if troco<0:
            print(f'Valor insuficiente. Faltam R${-troco:.2f}') # o f'' permite criar strings com funcoes dentro das linhas para assim juntar informacoes
            self.pagar()
        else:
            if troco > 0:
                print(f'Troco? R${troco:.2f}') #.2f eh pra formatar o float em duas casa decimais
            cpf_nota=input('Deseja informas o CPF na nota fiscal? (s/n):  ')
            if cpf_nota.lower()=='sim':
                cpf=input('Digite o CPF:  ')
                print(f'Nota fiscal: Total da compra - R${self.total:.2f} | CPF - {cpf}')
            else:
                print(f'Nota fiscal: Total da compra - R${self.total}')
        
        self.catalogo = {'Linha Grande':6.00, 'Agulha Grande':1.00, 'Linha Pequena':2.00}
        self.carrinho={}
        self.total=0.00
    
Mercado= Meucantinho()
Mercado.comprar()
