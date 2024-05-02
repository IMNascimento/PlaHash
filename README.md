<h1 align="center">
  <br>
  <a href="#"><img src="https://github.com/IMNascimento/DVR/assets/28989407/84028706-5a9e-4d00-af2c-2935e5604035" alt="Nascimento" width="200"></a>
  <br>
  Nascimento
  <br>
</h1>

# PLAHASH - Detector de Plágio

## Descrição
O Detector de Plágio é uma ferramenta desenvolvida para ajudar educadores e profissionais a identificar possíveis casos de plágio em documentos textuais. O sistema suporta múltiplos formatos de arquivo, incluindo DOCX, PDF, ODT, HTML e TXT.

## Características
- Suporte a múltiplos formatos de arquivo.
- Detecção de blocos de texto semelhantes entre dois documentos.
- Cálculo de porcentagem de semelhança entre os documentos.
- Arquitetura modular com implementação do padrão Factory para fácil expansão.

## Tecnologias Utilizadas
- Python 3.x
- Bibliotecas: python-docx, PyPDF2, odfpy, BeautifulSoup4, Pytest

## Configuração do Ambiente

### Pré-requisitos
Certifique-se de que o Python 3.x esteja instalado em seu sistema. Além disso, você precisará das seguintes bibliotecas:

```bash
pip install python-docx PyPDF2 odfpy beautifulsoup4 pytest
```

```markdown

plahash/
│
├── readers/                  
│   ├── __init__.py
│   ├── document_reader.py
│   ├── docx_reader.py
│   ├── pdf_reader.py
│   ├── odt_reader.py
│   ├── html_reader.py
│   └── txt_reader.py
│
├── utils/                    
│   ├── __init__.py
│   ├── text_normalizer.py
│   └── block_creator.py
│
├── hashing/                  
│   ├── __init__.py
│   └── simple_hash.py
│
├── tests/                    
│   ├── __init__.py
│   ├── test_readers.py
│   ├── test_utils.py
│   └── test_hashing.py
│
├── docs/                      
│   ├── index.md
│   └── usage_examples.md
│
├── plahash.py   
└── setup.py 
```


## Execução

Para executar o detector de plágio, navegue até o diretório do projeto e execute o seguinte comando:

```bash
python setup.py
```

Certifique-se de ajustar os parâmetros dentro do setup.py para apontar para os arquivos corretos que você deseja analisar.

## Testes
So ir na pasta do repositorio e executar o comando no terminal, caso sinta vontade pode criar mais testes na suite.

```bash
pytest tests/
```

## Documentação
Documentação e exemplos de usos estão na pasta /docs.

## Contribuições

Contribuições são bem-vindas! Se você deseja melhorar o detector de plágio, considere forkear o projeto e submeter um pull request.

## Licença
Este projeto é distribuído sob a licença GNU. Veja o arquivo LICENSE para mais detalhes.









