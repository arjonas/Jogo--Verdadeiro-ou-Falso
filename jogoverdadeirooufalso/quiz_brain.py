class QuizBrain:

    def __init__(self, listadequestoes ):
                self.numerodaquestao =0
                self.listadequestoes = listadequestoes
                self.escolha = ''
                #self.scorre=0




    def nextquestion(self):
        contador =0
        scorre  =0
        while contador < len(self.listadequestoes) :
            perguntaatual = self.listadequestoes[self.numerodaquestao]

            self.escolha =input(f'Q{self.numerodaquestao+1} {perguntaatual.texto} Verdadeiro/Falso')

            if self.escolha == perguntaatual.resposta:
                scorre =scorre+1
                contador =contador+1
                print(f'Pontos {scorre}')
                self.numerodaquestao = self.numerodaquestao +1

                
                
            else :
                print('Resposta Errada')
                
                contador = len(self.listadequestoes)
              


        print(f'Total de pontos  = {scorre}')
        if scorre == 12:
            print('Parabéns você zerou o quiz !!! ^^')


     