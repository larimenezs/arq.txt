"""Queremos analisar quantos alunos de uma plataforma de ensino vieram de 'anúncios' 
e quantos vieram 'orgânico'.

site_org -> pessoas que vieram pelo site
ytb_org -> pessoas que vieram pelo youtube
ig_org -> pessoas que vieram pelo instagram
igfb_org -> pessoas que vieram pelo instagram ou facebook

Se for diferente destas opções significa que vieram de Anúncios.
"""
arquivo = open('Alunos.txt', 'r')
linhas = arquivo.readlines()

del linhas[:4]

qtde_anuncio = 0
qtde_org = 0
qtde_igfb_org = 0
qtde_yt_org = 0
qtde_site_org = 0

for linha in linhas:
    email, origem = linha.split(',') #split pega a informação e separa em duas (informações entre ',')
    if '_org' in origem:
        qtde_org += 1
        if 'yt_org' in origem:
            qtde_yt_org += 1
        if 'site_org' in origem: #não usar o 'elif' pois uma mesma pessoa pode ter acessado por dois lugares
            qtde_site_org += 1 
        if 'ig_org' in origem or 'igfb_org' in origem:
            qtde_igfb_org += 1
    else:
        qtde_anuncio += 1

with open('Indicadores.txt', 'w') as arquivos_indicadores:
    arquivos_indicadores.write(f'Quantidade por anuncio: {qtde_anuncio}\n')
    arquivos_indicadores.write(f'Quantidade por orgânico: {qtde_org}\n')
    arquivos_indicadores.write(f'Quantidade por instagram ou facebook: {qtde_igfb_org}\n')
    arquivos_indicadores.write(f'Quantidade por youtube: {qtde_yt_org}\n')
    arquivos_indicadores.write(f'Quantidade por site: {qtde_site_org}')