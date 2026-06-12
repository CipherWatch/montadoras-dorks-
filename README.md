# 🚗 Montadoras Dorks Sites

Aplicação web em **Python + Flask** para montar, salvar e gerenciar buscas no
Google usando *Google Dorks* voltadas ao mundo automotivo (VIN, chassi, peças,
diagramas, manuais e codificação).

Roda em qualquer ambiente Linux — incluindo o **Google Cloud Shell** — sem
precisar de tela gráfica.

---

## ✨ Funcionalidades

- **CRUD completo** de buscas (criar, listar, editar, excluir), salvas em SQLite.
- **Montagem automática da dork** com pré-visualização ao vivo enquanto você digita.
- **Operadores do Google** suportados:
  - `site:` (site ou montadora) e `filetype:` (tipo de arquivo)
  - `intitle:` / `inurl:`
  - `"frase exata"` (aspas)
  - `-palavra` (excluir termos)
  - `after:` / `before:` (filtro por data)
  - idioma (`lr=`) e última atualização (`tbs=qdr:`) no link do Google
- **Palavras-chave fixas:** VIN, CHASSI, CODER, LEITURA, PECAS.
- **75 montadoras** nas sugestões (populares, premium, elétricas, caminhões e motos).
- **Filtros na tabela:** por categoria (botões), por montadora (dropdown) e busca livre.
- **Relatório em HTML** e **exportação para CSV** (compatível com Excel).

---

## 🛠️ Tecnologias

- Python 3
- Flask (servidor web)
- SQLite (banco de dados local)
- HTML + CSS + JavaScript (interface)

---

## 📦 Estrutura do projeto

```
M-D-S/
├── config.py     # listas e configurações (palavras-chave, montadoras, filetypes)
├── dorks.py      # lógica que monta as buscas (dorks)
├── banco.py      # camada de banco de dados (SQLite) com CRUD e migração
├── paginas.py    # o HTML da interface
└── app.py        # rotas do Flask que juntam tudo
```

---

## 🚀 Como rodar

Pré-requisito: Python 3 instalado.

```bash
# 1. Instale o Flask
pip install flask

# 2. Rode o app
python app.py
```

O servidor sobe em `http://0.0.0.0:8080`.

**No Google Cloud Shell:** após `python app.py`, clique em **Web Preview** →
**Preview on port 8080**.

---

## 🔍 Como usar

1. Escolha a **palavra-chave** (VIN, PECAS, etc.).
2. Preencha os campos (termo, frase exata, site/montadora, filtros...).
3. Veja a **dork** se montar na pré-visualização.
4. Clique em **Salvar** para guardar, ou **Buscar no Google** para pesquisar.
5. Use os **filtros** da tabela para encontrar buscas salvas.
6. Gere um **relatório** ou exporte em **CSV** quando quiser.

---

## ⚠️ Uso responsável

Esta ferramenta serve para localizar conteúdo **público** (catálogos, manuais,
documentação técnica) e para consultas técnicas de veículos. Use sempre dentro
da lei e dos termos de uso dos sites. Evite buscar ou tratar dados pessoais de
terceiros (LGPD).

---

## 📄 Licença

Projeto de uso pessoal/educacional.