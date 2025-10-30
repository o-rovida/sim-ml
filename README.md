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
<h2>Dicionário de Dados</h2>
<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th>Nome Original</th>
      <th>Nome Normalizado</th>
      <th>Categoria</th>
      <th>Observações</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>CONTADOR</td><td>contador</td><td>Metadado</td><td></td></tr>
    <tr><td>ORIGEM</td><td>origem</td><td>Metadado</td><td>1 – Oracle; 2 – Banco estadual via FTP; 3 – Banco SEADE; 9 – Ignorado</td></tr>
    <tr><td>DTNASC</td><td>data_nascimento</td><td>Falecido</td><td>ddmmaaaa</td></tr>
    <tr><td>IDADE</td><td>idade</td><td>Falecido</td><td>O primeiro dígito indica a unidade da idade (1=minuto, 2=hora, 3=mês, 4=ano, 5&gt;100 anos); o segundo dígito indica a quantidade de unidades</td></tr>
    <tr><td>NATURAL</td><td>naturalidade</td><td>Falecido</td><td></td></tr>
    <tr><td>CODMUNRES</td><td>municipio_residencia</td><td>Falecido</td><td>Código IBGE</td></tr>
    <tr><td>SEXO</td><td>sexo</td><td>Falecido</td><td>1 – masculino; 2 – feminino</td></tr>
    <tr><td>RACACOR</td><td>raca_cor</td><td>Falecido</td><td>1 – Branca; 2 – Preta; 3 – Amarela; 4 – Parda; 5 – Indígena</td></tr>
    <tr><td>ESTCIV</td><td>situacao_conjugal</td><td>Falecido</td><td>1 – Solteiro; 2 – Casado; 3 – Viúvo; 4 – Separado/divorciado; 5 – União estável; 9 – Ignorado</td></tr>
    <tr><td>ESC</td><td>escolaridade_em_anos</td><td>Falecido</td><td>1 – Nenhuma; 2 – 1 a 3 anos; 3 – 4 a 7 anos; 4 – 8 a 11 anos; 5 – 12 anos ou mais; 9 – Ignorado</td></tr>
    <tr><td>OCUP</td><td>ocupacao</td><td>Falecido</td><td>CBO 2002</td></tr>
    <tr><td>DTOBITO</td><td>data_obito</td><td>Óbito</td><td>ddmmaaaa</td></tr>
    <tr><td>HORAOBITO</td><td>hora_obito</td><td>Óbito</td><td>hhmm</td></tr>
    <tr><td>LOCOCOR</td><td>local_obito</td><td>Óbito</td><td>1 – hospital; 2 – outros estabelecimentos; 3 – domicílio; 4 – via pública; 5 – outros; 6 – aldeia indígena; 9 – ignorado</td></tr>
    <tr><td>CODMUNOCOR</td><td>municipio_obito</td><td>Óbito</td><td>Código IBGE</td></tr>
    <tr><td>CODEESTAB</td><td>estabelecimento</td><td>Óbito</td><td>CNES</td></tr>
    <tr><td>CAUSABAS</td><td>causa_obito</td><td>Óbito</td><td>CID-10</td></tr>
    <tr><td>CAUSABAS_O</td><td>causa_obito_origem</td><td>Óbito</td><td>CID-10</td></tr>
    <tr><td>LINHAA</td><td>causas_obito_1a</td><td>Óbito</td><td>CID-10</td></tr>
    <tr><td>LINHAB</td><td>causas_obito_1b</td><td>Óbito</td><td>CID-10</td></tr>
    <tr><td>LINHAC</td><td>causas_obito_1c</td><td>Óbito</td><td>CID-10</td></tr>
    <tr><td>LINHAD</td><td>causas_obito_1d</td><td>Óbito</td><td>CID-10</td></tr>
    <tr><td>LINHAII</td><td>causas_obito_2</td><td>Óbito</td><td>CID-10</td></tr>
    <tr><td>ASSISTMED</td><td>recebeu_assistencia_medica</td><td>Óbito</td><td>1 – sim; 2 – não; 9 – ignorado</td></tr>
    <tr><td>EXAME</td><td>realizacao_de_exame</td><td>Óbito</td><td>1 – sim; 2 – não; 9 – ignorado</td></tr>
    <tr><td>CIRURGIA</td><td>realizacao_de_cirurgia</td><td>Óbito</td><td>1 – sim; 2 – não; 9 – ignorado</td></tr>
    <tr><td>TIPOBITO</td><td>obito_fetal</td><td>Óbito</td><td>1 – Fetal; 2 – Não fetal</td></tr>
    <tr><td>NECROPSIA</td><td>necropsia</td><td>Post-mortem</td><td>1 – sim; 2 – não; 9 – ignorado</td></tr>
    <tr><td>TPPOS</td><td>investigado</td><td>Post-mortem</td><td>S – sim; N – não</td></tr>
    <tr><td>DTATESTADO</td><td>data_atestado</td><td>Post-mortem</td><td>ddmmaaaa</td></tr>
    <tr><td>DTCADASTRO</td><td>data_cadastro</td><td>Post-mortem</td><td>ddmmaaaa</td></tr>
    <tr><td>DTRECEBIM</td><td>data_recebimento</td><td>Post-mortem</td><td>ddmmaaaa</td></tr>
    <tr><td>ATESTANTE</td><td>atestante</td><td>Post-mortem</td><td>1 – Assistente; 2 – Substituto; 3 – IML; 4 – SVO; 5 – Outro</td></tr>
  </tbody>
</table>
