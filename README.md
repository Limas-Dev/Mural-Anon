# 🟣 AnonFeedback — Plataforma de Feedback Anônimo

Este projeto é uma aplicação web desenvolvida com **Flask** que permite a **criação, envio e gerenciamento de murais de feedback anônimo**. Projetada para uso em **empresas**, **instituições educacionais**, **eventos**, ou qualquer ambiente que demande coleta de opiniões sigilosas.

A aplicação prioriza **privacidade, usabilidade e simplicidade**, garantindo que os feedbacks sejam completamente **desassociados de qualquer identificação do usuário**.

---

## 🚀 Funcionalidades Principais

| Funcionalidade            | Descrição                                                                 |
|--------------------------|---------------------------------------------------------------------------|
| 🎯 Criação de Murais      | Interface para criação rápida de murais com título personalizado          |
| 🗣️ Feedback Anônimo       | Usuários enviam mensagens sem login ou identificação                      |
| 📃 Exportação de Feedback | Geração de arquivo DOCX com todos os feedbacks recebidos                  |
| ❌ Encerramento Seguro    | Botão para encerramento e exclusão segura dos dados                       |
| 🧾 Apoio ao Dev           | Botão de apoio ao desenvolvedor com opção de doação via Pix               |

---

## 🧩 Arquitetura e Organização

A estrutura do projeto segue o padrão MVC simplificado:

## 📂 Estrutura de Diretórios

```bash
Anon/
├── app/
│   ├── __init__.py          # Inicialização da aplicação Flask
│   ├── routes.py            # Definição das rotas e lógica de negócio
│   ├── models.py            # Modelos de dados (ORM / SQLite)
│   ├── static/              # Arquivos estáticos (CSS customizado)
│   │   ├── style1.css
│   │   └── style2.css
│   └── templates/           # Templates HTML (Jinja2)
│       ├── index.html
│       └── mural.html
│
├── instance/
│   └── feedback.db          # Banco de dados SQLite local
│
├── requirements.txt         # Lista de dependências do projeto
├── run.py                   # Script principal para execução do app
└── README.md                # Documentação do projeto
