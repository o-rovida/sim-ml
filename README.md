# Fontes de Dados

- **[Sistema de Informação sobre Mortalidade (SIM)](https://dados.gov.br/dados/conjuntos-dados/sim-1979-2019)**  
  Desenvolvido pelo Ministério da Saúde em 1975, o SIM unifica mais de quarenta modelos de Declaração de Óbito para coletar dados sobre mortalidade no país. O arquivo `.duckdb` é resultado da extração do seed disponível neste [repositório](https://github.com/o-rovida/sim-seed).

- **[Tabelas da CID-10](http://www2.datasus.gov.br/cid10/V2008/cid10.htm)**  
  Classificação Estatística Internacional de Doenças e Problemas Relacionados à Saúde, conhecida como CID-10.

- **[Códigos dos Municípios Base dos Dados](https://basedosdados.org/dataset/33b49786-fb5f-496f-bb7c-9811c985af8e?table=dffb65ac-9df9-4151-94bf-88c45bfcb056)**  
  Lista dos municípios brasileiros com códigos de 6 e 7 dígitos do IBGE, sendo os dois primeiros referentes à Unidade da Federação.

- **[CBO 2002](http://www.mtecbo.gov.br/cbosite/pages/downloads.jsf)**: A Classificação Brasileira de Ocupações - CBO, instituída por portaria em 2002, tem por finalidade a identificação das ocupações no mercado de trabalho, para fins classificatórios junto aos registros administrativos e domiciliares. Complementado pelos dados nesse [documento](https://central3.to.gov.br/arquivo/312288/).

A fonte de dados está no arquivo `data.7z` e e pode ser baixado [aqui](https://drive.google.com/file/d/1pTQxlx-hPJHjtLDtZFXtj5eg5DW-CMal/view?usp=drive_link).  
Para executar o `generate_dataset.ipynb`, é necessário descompactá-lo antes.
