import os
from PIL import Image

def otimizar_imagens(diretorio_entrada, diretorio_saida, qualidade=80):
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    for arquivo in os.listdir(diretorio_entrada):
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            caminho_completo = os.path.join(diretorio_entrada, arquivo)
            
            with Image.open(caminho_completo) as img:
                
                if img.width > 1920:
                    proporcao = 1920 / float(img.width)
                    altura = int((float(img.height) * float(proporcao)))
                    img = img.resize((1920, altura), Image.LANCZOS)

              
                nome_sem_extensao = os.path.splitext(arquivo)[0]
                caminho_saida = os.path.join(diretorio_saida, f"{nome_sem_extensao}.webp")
                
                
                img.save(caminho_saida, "WEBP", quality=qualidade, method=6)
                
                tamanho_kb = os.path.getsize(caminho_saida) / 1024
                print(f"Otimizado: {arquivo} -> {tamanho_kb:.2f} KB")


otimizar_imagens('otimizadas', 'otimizadas')