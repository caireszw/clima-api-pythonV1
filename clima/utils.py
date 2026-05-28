from rich import print
from rich.panel import Panel

def lin():
    print('-'*30)
    
def menu(*texto):
    
    ## EXIBIR OPÇÔES
    contador = 1
    msg = ''
    for i in texto:
        msg += f'{contador} - {i} \n'        
        contador += 1 
    print(Panel(msg,width=35,height=8, title= '[blue]PREVISÃO DO TEMPO[/]'))
    
def selecionar_opcao(msg):
    while True:
        try:
            return int(input(msg))
            break
        except ValueError:
            print('OPÇÃO INVALIDA TENTE NUMEROS')

