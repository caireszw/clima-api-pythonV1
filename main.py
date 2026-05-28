from clima import consulta
from clima import utils
from time import sleep

while True:
    utils.menu('VISUALIZAR CLIMA ATUAL','CONSULTAR HISTORICO','PREVISÃO PROXIMOS DIAS','COMPARAR TEMPERATURAS','LIMPAR HISTORICO','SAIR DO PROGRAMA')
    opc1 = utils.selecionar_opcao('Digite a opção desejada: ')
    if opc1 == 1:
        consulta.visualizar_clima()
    elif opc1 == 2:
        consulta.consultar_historico()
    elif opc1 == 3:
        consulta.proximos_dias()
    elif opc1 == 4:
        consulta.comparar_temperatura()
    elif opc1 == 5:
        consulta.limpar_historico()
    elif opc1 == 6:
        print('FIM DO SISTEMA OBRIGADO!')
        break
    elif opc1 > 6:
        print('Opção Invalida!')   
    sleep(2)