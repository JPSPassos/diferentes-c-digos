import datetime

agora = datetime.datetime.now()
print(agora)
hoje = datetime.date.today()
print(hoje)

data_especifica = datetime.date(2025, 9, 24)
print(data_especifica)

hora_especifica = datetime.time(14, 30, 0)
print(hora_especifica)

agora = datetime.datetime.now()
print(agora.year)
print(agora.month)
print(agora.day)
print(agora.hour)
print(agora.minute)
print(agora.second)
print(agora.microsecond)

hoje_str = hoje.strftime('%d/%m/%Y')
print(hoje_str)

passado = hoje - datetime.timedelta(weeks=2)
print(passado)

futuro = hoje + datetime.timedelta(weeks=2)
diferenca = futuro - hoje
print(diferenca.days)