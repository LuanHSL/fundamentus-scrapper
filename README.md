# Fundamentus Scrapper

![GitHub repo size](https://img.shields.io/github/repo-size/LuanHSL/fundamentus-scrapper?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/LuanHSL/fundamentus-scrapper?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/LuanHSL/fundamentus-scrapper?style=for-the-badge)

> Este projeto utiliza Python para extrair dados financeiros de fundos imobiliários e ações listados no [FUNDAMENTUS](https://www.fundamentus.com.br/index.php). Através de técnicas de web scraping, o programa filtra e organiza as informações, gerando uma planilha personalizada dos melhores ativos de acordo com os critérios de um curso da [Finclass](https://app.finclass.com/).

## ⚠️ Aviso

As informações contidas na planilha destinam-se apenas a auxiliar na sua análise pessoal. **Não é recomendação de investimento**. Utilize-as como um ponto de partida para suas próprias pesquisas e decisões, sempre consultando um profissional financeiro antes de tomar qualquer decisão de investimento.

### Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas para as seguintes tarefas:

- [ ] Permitir que o usúario preencha o filtro, para que possa ter dados personalizados

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Para facilitar a instalação e execução do projeto, recomenda-se a utilização do Docker. Caso não esteja instalado, siga a [documentação oficial](https://docs.docker.com/desktop/) do Docker para seu sistema operacional.
> ou
- [Python ^3.9](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)

## 🚀 Instalando Fundamentus Scrapper

Para instalar, siga estas etapas:
```
git clone https://github.com/LuanHSL/fundamentus-scrapper.git
```
```
cd fundamentus-scrapper
```

Docker:

```
docker build -t python-fundamentus-scrapper .
```

> ou

Sem Docker:

```
pip install selenium pandas openpyxl
```

## Executando Fundamentus Scrapper

Para executar, siga estas etapas:

Docker:
- Filtrar por ações
- Substitua < caminho > pelo caminho que clonou o projeto
  - Exemplo: C:\\...\data
```
docker run -it -v <caminho>\data:/app/data python-fundamentus-scrapper 
```

- Filtrar por fundos imobiliários
- Substitua < caminho > pelo caminho que clonou o projeto
  - Exemplo: C:\\...\data
```
docker run -it -v <caminho>\data:/app/data python-fundamentus-scrapper fii.py
```

> ou

Sem Docker:
- Filtrar por ações
```
py acoes.py
```

- Filtrar por fundos imobiliários
```
py fii.py
```

## 📫 Contribuindo para Fundamentus Scrapper

Para contribuir com Fundamentus Scrapper, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b develop`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
