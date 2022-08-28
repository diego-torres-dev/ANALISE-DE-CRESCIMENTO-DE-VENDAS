# Lista de produtos
produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell',
            'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']

# Lista com os dados de vendas de 2019
vendas2019 = [558147, 712350, 573823, 405252, 718654, 531580, 973139,
              892292, 422760, 154753, 887061, 438508, 237467, 489705, 328311, 591120]

# Lista com os dados de vendas de 2020
vendas2020 = [951642, 244295, 26964, 787604, 867660, 78830, 710331,
              646016, 694913, 539704, 324831, 667179, 295633, 725316, 644622, 994303]

print("-" * 84)
print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(
    "PRODUTO", "VENDAS 2019", "VENDAS 2020", "CRESCIMENTO (%)"))
print("-" * 84)

for i, produto in enumerate(produtos):
    if vendas2020[i] > vendas2019[i]:
        crescimento = (vendas2020[i] / vendas2019[i]) - 1
        linha = "|{:<20}|{:>20}|{:>20}|{:^20.2%}|".format(
            produto, vendas2019[i], vendas2020[i], crescimento)
        print(linha)

print("-" * 84)
