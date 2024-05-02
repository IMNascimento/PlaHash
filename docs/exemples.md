# Exemplos de Uso do Detector de Plágio

Este documento oferece uma visão detalhada de como usar o Detector de Plágio em vários cenários e formatos de arquivo. Os exemplos abaixo demonstram o uso prático do sistema para detectar plágio entre documentos.

## Configuração Inicial

Antes de executar os exemplos, certifique-se de que o sistema está configurado corretamente. Isso inclui a instalação de todas as dependências necessárias e a configuração dos leitores de documentos conforme descrito no arquivo README.

## Exemplo 1: Comparando Dois Documentos DOCX

### Código
```python
from setup import setup_plagiarism_detector

# Configurar o detector para arquivos DOCX
detector = setup_plagiarism_detector('docx')

# Caminho para os documentos a serem comparados
file1 = 'caminho_para_documento1.docx'
file2 = 'caminho_para_documento2.docx'

# Executar detecção de plágio
result = detector.detect(file1, file2)

# Imprimir os resultados
print(f"Porcentagem de Semelhança: {result['similarity_percentage']}%")
for block1, block2 in result['common_blocks']:
    print(f"Bloco comum: {block1} | {block2}")

```

Este exemplo demonstra como configurar e usar o detector para comparar dois documentos DOCX. Os resultados incluirão a porcentagem de semelhança e os blocos de texto comuns encontrados.

## Exemplo 2: Comparando Dois Documentos PDF

```python
from setup import setup_plagiarism_detector

# Configurar o detector para arquivos PDF
detector = setup_plagiarism_detector('pdf')

# Caminho para os documentos a serem comparados
file1 = 'caminho_para_documento1.pdf'
file2 = 'caminho_para_documento2.pdf'

# Executar detecção de plágio
result = detector.detect(file1, file2)

# Imprimir os resultados
print(f"Porcentagem de Semelhança: {result['similarity_percentage']}%")
for block1, block2 in result['common_blocks']:
    print(f"Bloco comum: {block1} | {block2}")


```

Este exemplo mostra como usar o sistema para comparar documentos em formato PDF. O processo é similar ao exemplo anterior, ajustando-se para o formato de arquivo específico.


## Exemplo 3: Entrada de Texto Direta

```python
from plahash import PlagiarismDetector
from utils.text_normalizer import TextNormalizer
from utils.block_creator import BlockCreator
from hashing.simple_hash import SimpleHash

# Criar instâncias das classes de utilidade
normalizer = TextNormalizer()
block_creator = BlockCreator()
hash_function = SimpleHash()

# Instanciar o detector manualmente
detector = PlagiarismDetector(None, normalizer, block_creator, hash_function)

# Textos simulados para comparação
text1 = "Este é um exemplo de texto que poderia ser parte de um documento maior."
text2 = "Este texto é um exemplo que poderia ser considerado similar ao primeiro."

# Normalizar e criar blocos para ambos os textos
text1 = normalizer.normalize(text1)
text2 = normalizer.normalize(text2)
blocks1 = block_creator.create_blocks(text1)
blocks2 = block_creator.create_blocks(text2)

# Calcular hash e detectar
hashes1 = {hash_function.hash(block): block for block in blocks1}
hashes2 = {hash_function.hash(block): block for block in blocks2}
common_hashes = set(hashes1.keys()) & set(hashes2.keys())
similarity = len(common_hashes) / len(hashes1) * 100

# Imprimir os resultados
print(f"Porcentagem de Semelhança: {similarity}%")
for hash_code in common_hashes:
    print(f"Bloco comum: {hashes1[hash_code]} | {hashes2[hash_code]}")

```
Este exemplo ilustra como usar o sistema para comparar texto direto, útil para testes rápidos ou integração com outras aplicações onde os textos não estão em arquivos.