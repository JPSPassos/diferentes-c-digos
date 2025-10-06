#SISTEMA DE EMPRESTIMO DE LIVROS
import datetime as dt
from datetime import timedelta as td

hoje = dt.date.today()
devolucao = hoje + td(days=7)

data_str = input('Digite a data de hoje (dd/mm/aaaa): ')
data_devolvida = dt.datetime.strptime(data_str, '%d/%m/%Y').date()

if data_devolvida < devolucao:
    print('Falta(m) {} dia(s) para a devolução do livro'.format((devolucao - data_devolvida).days))
elif data_devolvida > devolucao:
    print('O livro está atrasado por {} dia(s)'.format((data_devolvida - devolucao).days))
else:
    print('O livro deve ser devolvido hoje!')

#CALCULADORA DE IDADE
nascimento_str = input('Digite sua data de nascimento (dd/mm/aaaa): ')
nascimento = dt.datetime.strptime(nascimento_str, '%d/%m/%Y').date()
idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
print('Você tem {} anos.'.format(idade))