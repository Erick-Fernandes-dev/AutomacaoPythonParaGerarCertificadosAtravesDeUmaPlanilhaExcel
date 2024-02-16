"""
# Pegar os dados da planilha
Tipo nome do curso, nome participante, tipo de participação, data do inicio, data do final.
carga horária, data da emissão do certificado 

# Transferir os dados da planilha para a imagem do certificado
"""
import openpyxl as px
from PIL import Image, ImageDraw, ImageFont

workbook_alunos = px.load_workbook('./planilha_alunos.xlsx')
sheet_alunos = workbook_alunos['Sheet1'] 

def desenhar_texto(nome_curso, nome_participante, tipo_participacao, data_inicio, data_final, carga_horaria, data_emissao):
    desenhar.text((1050, 825), nome_participante,fill='black',font=fonte_nome)
    desenhar.text((1060, 950), nome_curso, fill='black', font=fonte_geral)
    desenhar.text((1435, 1065), tipo_participacao, fill='black', font=fonte_geral)
    desenhar.text((1480, 1182), str(carga_horaria), fill='black', font=fonte_geral)

    desenhar.text((750, 1770), data_inicio, fill='blue', font=fonte_data)
    desenhar.text((750, 1930), data_final, fill='blue', font=fonte_data)

    desenhar.text((2220, 1930), data_emissao, fill='blue', font=fonte_data)

# Comece a varrer os dados da planilha a partir da segunda linha
# use para quando for testar as posições dos dados (max_row=2)
# Pois irá gerar a penas a linha 2
for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):
    nome_curso = linha[0].value # nome do curso
    nome_participante = linha[1].value # nome do participante
    tipo_participacao = linha[2].value # tipo de participação
    data_inicio = linha[3].value # data do inicio
    data_final = linha[4].value # data do final
    carga_horaria = linha[5].value # carga horária
    data_emissao = linha[6].value # data da emissão do certificado
    #input('')

    # Transferir os dados da planilha para a imagem do certificado
    # Definindo fonte a ser usada
    fonte_nome = ImageFont.truetype('./tahomabd.ttf', 90)
    fonte_geral = ImageFont.truetype('./tahoma.ttf', 80)
    fonte_data = ImageFont.truetype('./tahoma.ttf', 55)

    image = Image.open('./certificado_padrao.jpg')
    desenhar = ImageDraw.Draw(image)

    desenhar_texto(nome_curso, nome_participante, tipo_participacao, data_inicio, data_final, carga_horaria, data_emissao)

    image.save(f'./{indice} {nome_participante} certificado.png')
