# importando o módulo numpy
import numpy as np

# definindo a função
def calculate(list):
  # se o tamanho da lista for 9 (matriz 3x3)
  if len(list) == 9:
    # transformando a lista em um array do numpy
      list = np.array(list)
    # transformando numa matriz 3x3
      list.shape = (3, 3)
    # criando o dicionário pedido
      dictionary = {
        # o comando .tolist() transforma o array do numpy em lista, e para alguns fica necessário transformar para float ou int
        # média
          'mean': [(np.mean(list, axis = 0)).tolist(), (np.mean(list, axis = 1)).tolist(), float(np.mean(list))],
        # variância
          'variance': [(np.var(list, axis = 0)).tolist(), (np.var(list, axis = 1)).tolist(), float(np.var(list))],
        # desvio padrão
          'standard deviation': [(np.std(list, axis = 0)).tolist(), (np.std(list, axis = 1)).tolist(), float(np.std(list))],
        # máximo 
          'max': [(np.max(list, axis = 0)).tolist(), (np.max(list, axis = 1)).tolist(), int(np.max(list))],
        # mínimo
          'min': [(np.min(list, axis = 0)).tolist(), (np.min(list, axis = 1)).tolist(), int(np.min(list))],
        # soma
          'sum': [(np.sum(list, axis = 0)).tolist(), (np.sum(list, axis = 1)).tolist(), int(np.sum(list))]
          }
    # retorna o dicionário criado
      return dictionary
    # caso a lista tenha algo diferente de 9 entradas,
  else:  
    # retorna um ValueError do próprio python com essa mensagem
    raise ValueError ("List must contain nine numbers.")

