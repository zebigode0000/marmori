import os

PASTA = "img"  # coloque o nome da pasta das imagens

extensoes_para_apagar = (".jpg", ".jpeg", ".png")

for arquivo in os.listdir(PASTA):
    if arquivo.lower().endswith(extensoes_para_apagar):
        caminho = os.path.join(PASTA, arquivo)
        os.remove(caminho)
        print(f"Apagado: {arquivo}")

print("✅ Imagens JPG e PNG removidas!")
