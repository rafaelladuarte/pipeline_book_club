# Pipeline Book Club
<p align="center">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/rafaelladuarte/pipeline_book_club?style=plastic">
</p>

<p align="center">
<img src="https://raw.githubusercontent.com/rafaelladuarte/pipeline_book_club/main/images/BookClub.jpg"/>
</p>

<p align="center">
<img src="https://img.shields.io/static/v1?label=Status&message=DESENVOLVIMENTO&color=yellow&style=for-the-badge"/>
</p>

#

<p align="center">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
    <img src="https://img.shields.io/badge/bash-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white"/>
    <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white"/>
    <img src="https://img.shields.io/badge/Apache%20Airflow-%23CC342D?style=for-the-badge&logo=Apache%20Airflow&logoColor=white"/>
	<img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white"/>
</p>

#

## Tema

Utilizaçãao do Apache Airflow para orquestração da pipeline de transferência de dados entre a internet e um banco de dados SQL

## Descrição

A Book Club é uma Startup de troca de livros. O modelo de negócio funciona com base na troca de livros pelos usuários, cada livro cadastrado pelo usuário, dá o direito à uma troca, porém o usuário também pode comprar o livro, caso ele não queira oferecer outro livro em troca.

Umas das ferramentas mais importantes para que esse modelo de negócio rentabilize, é a recomendação. Uma excelente recomendação aumenta o volume de trocas e vendas no site.

Você é um Data Scientist contrato pela empresa para construir um Sistema de Recomendação que impulsione o volume de trocas e vendas entre os usuários. Porém, a Book Club não coleta e nem armazena os livros enviados pelos usuários.

Os livros para troca, são enviados pelos próprios usuários através de um botão “Fazer Upload”, eles ficam visíveis no site, junto com suas estrelas, que representam o quanto os usuários gostaram ou não do livro, porém a Startup não coleta e nem armazena esses dados em um banco de dados.

Logo, antes de construir um sistema de recomendação, você precisa coletar e armazenar os dados do site. Portanto seu primeiro trabalho como um Data Scientist será coletar e armazenar os seguintes dados:

* O nome do livro.
* A categoria do livro.
* O número de estrelas que o livro recebeu.
* O preço do livro.
* Se o livro está em Estoque ou não.

## Roteiro da Resolução:
Esse é o roteiro de resolução do desafio que eu sugiro:

* Faça o web scraper para coletar os dados das páginas HTML, necessariamente, utilizando a linguagem Python.
* Armazene os dados brutos em um arquivo csv.
* Normalize os dados brutos de acordo com Modelo Entidade-Relacionamento e Star Schema.
* Armazene os dados tratados em um banco de dados Postgres, utilizando um script em bash.
* Agende seu script para rodar todos os dias em um horário específico, utilizando o Apache Airflow.
* Crie uma vizualização dos dados em um dashboard.


### Tornar sua solução Profissionalmente Respeitada: 

* Garanta que seu script saiba lidar com possíveis erros e não pare de funcionar por qualquer problema. 
* Crie sua solução modularizada
* Sincronize os script de coleta e inserção.
* Faça o gerenciamento desses jobs utilizando o Airflow
* Crie workers que trabalham em paralelo, cada um coleta e armazena os dados dos livros de uma página.

## Observações 

Os dados para serem coletados e armazenados, estão disponíveis neste site. http://books.toscrape.com/

Esse site foi desenvolvido e disponibilizado especialmente para praticar web scraping. Não existe nenhum tipo de problema legal ao fazer a coleta de dados.

Referência: https://medium.com/@meigarom/o-projeto-de-data-engineering-para-o-seu-portf%C3%B3lio-c186c7191823

