import os
from PIL import Image

# pasta onde estão suas imagens
PASTA_IMAGENS = "img"

# qualidade do webp (0–100)
QUALIDADE = 80

for arquivo in os.listdir(PASTA_IMAGENS):
    if arquivo.lower().endswith((".jpg", ".jpeg", ".png")):
        caminho = os.path.join(PASTA_IMAGENS, arquivo)

        imagem = Image.open(caminho).convert("RGB")

        nome_sem_ext = os.path.splitext(arquivo)[0]
        novo_caminho = os.path.join(PASTA_IMAGENS, f"{nome_sem_ext}.webp")

        imagem.save(novo_caminho, "webp", quality=QUALIDADE)

        print(f"Convertido: {arquivo} → {nome_sem_ext}.webp")
