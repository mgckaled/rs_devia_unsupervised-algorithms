<!-- markdownlint-disable MD033 -->
<!-- markdownlint-disable MD014 -->

# Formação Desenvovimento de IA - Algoritmos Não Supervisionados

<div align="center">
   <img alt="logo trilha" src=".github/assets/images/banner.png" width="30%"/>
</div>

<br>

<div align="center">
  <img alt="Made by mgckaled" src="https://img.shields.io/badge/made%20by-mgckaled-darkblue">
  <img alt="GitHub Repo Size" src="https://img.shields.io/github/repo-size/mgckaled/rs_devia_unsupervised-algorithms">
  <img alt="pylint badge" src="https://img.shields.io/badge/linting-pylint-yellowgreen">
  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=49AA26&labelColor=000000">
</div>

## Sumário

- [Formação Desenvovimento de IA - Algoritmos Não Supervisionados](#formação-desenvovimento-de-ia---algoritmos-não-supervisionados)
  - [Sumário](#sumário)
  - [Sobre o Projeto](#sobre-o-projeto)
    - [Módulo 14 - K-Means](#módulo-14---k-means)
    - [Módulo 15 - Clusterização Hierárquica](#módulo-15---clusterização-hierárquica)
    - [Módulo 16 - PCA](#módulo-16---pca)
    - [Módulo 17 - t-SNE](#módulo-17---t-sne)
  - [Tecnologias](#tecnologias)
    - [Linguagem de Programação](#linguagem-de-programação)
    - [Gerenciadores de Ambiente Virtual](#gerenciadores-de-ambiente-virtual)
    - [Bibliotecas Instaladas (Packages)](#bibliotecas-instaladas-packages)
  - [Como clonar o projeto?](#como-clonar-o-projeto)
  - [Licença](#licença)

## Sobre o Projeto

Repositório que reuni os módulos 14 ao 16 da formação Desenvolvimento IA 2023-2024, desenvolvido pela Rocketseat Education.

### Módulo 14 - K-Means

O propósito deste módulo é introduzir os principais algoritmos de clusterização de forma conceitual, visando capacitar o desenvolvimento de projetos de aprendizado de máquina voltados para agrupamento de objetos. Para ilustrar esses conceitos, realizaremos um projeto centrado no primeiro desses algoritmos, o **K-Means**. Este projeto abrangerá todo o processo, desde a Análise Exploratória de Dados (EDA) até a implementação de um modelo por meio de uma aplicação para inferência em *batch*.

> Acesso ao [conteúdo das aulas](.github/docs/content/m14.md).
>
> [Apresentação em slides](.github/docs/pdf/ppts_m14.pdf) do conteúdo teórico.

### Módulo 15 - Clusterização Hierárquica

O módulo explora o algoritmo de clusterização hierárquica, crucial em aprendizado de máquina para agrupamento de dados. Inclui teoria, dendrogramas e aplicação em recomendação de laptops em um marketplace.

**Acesso ao app de consulta Streamlit:** `streamlit run .\apps\app_clustering_laptops.py` (Local URL: `http://localhost:8501`)

> Acesso ao [conteúdo das aulas](.github/docs/content/m15.md)
>
> [Apresentação em slides](.github/docs/pdf/ppts_m15.pdf) do conteúdo teórico.

### Módulo 16 - PCA

Abordagem com foco em algoritmos de redução de dimensionalidade, especialmente a Análise de Componentes Principais (PCA). Inclui EDA e um projeto prático para aplicar o PCA em análises de dados reais.

> Acesso ao [conteúdo das aulas](.github/docs/content/m16.md)
> 
> [Apresentação em slides](.github/docs/pdf/ppts_m16.pdf) do conteúdo teórico.

### Módulo 17 - t-SNE

Este módulo ensina o algoritmo t-SNE para redução de dimensionalidade, aplicado a um projeto de uma empresa de cosméticos. Inclui EDA e visualização dos resultados, capacitando você a usar t-SNE para interpretar grandes conjuntos de dados.

> Acesso ao [conteúdo das aulas](.github/docs/content/m17.md)
> 
> [Apresentação em slides](.github/docs/pdf/ppts_m17.pdf) do conteúdo teórico.

## Tecnologias

### Linguagem de Programação

- [`python`](https://www.python.org/) (v3.12.3)

### Gerenciadores de Ambiente Virtual

- [`pyenv`](https://github.com/pyenv/pyenv)
- [`pipenv`](https://pipenv.pypa.io/en/latest/)

### Bibliotecas Instaladas (Packages)

- [`pandas`](https://pandas.pydata.org/)
- [`numpy`](https://numpy.org/)
- [`matplotlib`](https://matplotlib.org/)
- [`seaborn`](https://seaborn.pydata.org/)
- [`scipy`](https://scipy.org/)
- [`scikit-learn`](https://scikit-learn.org/stable/)
- [`pingouin`](https://pingouin-stats.org/build/html/index.html)
- [`gradio`](https://www.gradio.app/)
- [`streamlit`](https://streamlit.io/)
- [`ipykernel`](https://pypi.org/project/ipykernel/)
- [`plotly`](https://plotly.com/python/)
- [`nbformat`](https://pypi.org/project/nbformat/)
- [`optuna`](https://optuna.org/)
- [`nbformat`](https://pypi.org/project/nbformat/)
- [`ipywidgets`](https://pypi.org/project/ipywidgets/)


## Como clonar o projeto?

1. Certifique-se de que está usando o `pyenv` e o `pipenv` para gerenciar as dependências do projeto. Veja como instalar e configurar clicando nos respectivos links do tópico [Gerenciadores de Ambiente Virtual](#gerenciadores-de-ambiente-virtual).

2. Faça o clone pelo Github:

    ```shell
    git clone https://github.com/mgckaled/rs_devia_unsupervised-algorithms.git
    ```

3. Acesse o diretório:

    ```shell
    cd rs_devia_unsupervised-algorithms
    ```

4. Ative o ambiente virtual pelo terminal

    ```shell
    pipenv shell
    ```

5. Instale as dependências. (Certifique-se de estar utilzando a versão exata do python - 3.12.3)

    ```shell
    pipenv install
    ```

    ou, como um recurso de degurança, instale dependências exatas do `requirements.txt`:

    ```shell
    pipenv install -r requirements.txt
    ```


## Licença

Distribuído sob a licença *MIT*. Veja [LICENSE](LICENSE) para mais informações.

---

<h5 align="center">
  2023-2024 - <a href="https://github.com/mgckaled/">Marcel Kaled</a>
</h5>