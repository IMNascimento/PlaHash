# Documentação do Detector de Plágio

## Visão Geral
Este documento fornece uma visão detalhada da arquitetura, classes, métodos e exemplos de uso do Detector de Plágio. O sistema é projetado para identificar semelhanças entre documentos de diferentes formatos, ajudando a detectar casos de plágio.

## Arquitetura
O projeto segue uma arquitetura modular com o uso do padrão Factory para a criação de leitores de documentos, facilitando a expansão e manutenção do código.

### Estrutura de Diretórios
A estrutura organizacional dos diretórios é projetada para separar responsabilidades claramente:

- `readers/`: Contém classes que lidam com a leitura de diferentes formatos de arquivos.
- `utils/`: Inclui utilitários como normalizadores de texto e criadores de blocos de texto.
- `hashing/`: Armazena implementações de funções hash.
- `plahash.py`: Classe principal que orquestra o processo de detecção de plágio.
- `setup.py`: Script de configuração e execução do sistema.

## Classes e Métodos

### Readers
Cada classe de leitor suporta um formato específico de documento e implementa o método `read`.

#### `DocxReader`, `PDFReader`, `ODTReader`, `HTMLReader`, `TXTReader`
- `read(file_path)`: Lê o documento do caminho especificado e retorna o texto como uma string.

### Utils
Ferramentas auxiliares para normalização de texto e criação de blocos.

#### `TextNormalizer`
- `normalize(text)`: Normaliza o texto removendo caracteres especiais e convertendo para minúsculas.

#### `BlockCreator`
- `create_blocks(text, block_size)`: Divide o texto em blocos de palavras de tamanho especificado.

### Hashing
Implementações de funções de hash para criar hashes de blocos de texto.

#### `SimpleHash`
- `hash(data)`: Calcula e retorna o hash do dado fornecido.

### `PlagiarismDetector`
Classe principal que usa os componentes acima para detectar plágio.

- `__init__(reader, normalizer, block_creator, hash_function)`: Inicializa o detector.
- `detect(file1, file2)`: Analisa dois arquivos e retorna a porcentagem de semelhança e blocos de texto comuns.

## Exemplo de Uso
Abaixo está um exemplo de como configurar e usar o detector de plágio para comparar dois documentos:

```python
detector = setup_plagiarism_detector('docx')
result = detector.detect('documento1.docx', 'documento2.docx')
print(f"Porcentagem de Semelhança: {result['similarity_percentage']}")
for block in result['common_blocks']:
    print(f"Bloco comum: {block[0]} | {block[1]}")
```