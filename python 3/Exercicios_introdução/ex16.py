print("Informe o tamanho de um arquivo e a velocidade da internet para calcular o tempo de download!")

arquivo = float(input('Tamanho do arquivo em megabytes: '))
velocidade = int(input('Velocidade da internet em mbps: '))

tempo = (arquivo/(velocidade/8)) #formula: tamanho do arquivo em megabytes / (velocidade de download em megabits / 8) =  tempo em segundos

tempo_minuto = (tempo/60) #conversão segundos para minutos

print(f'\nO tempo total de download é de {tempo_minuto:.2f} minutos')