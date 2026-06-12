# -*- coding: utf-8 -*-
import os

APP_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(APP_DIR, "buscas_dorks.db")

PALAVRAS_CHAVE = ["VIN", "CHASSI", "CODER", "LEITURA", "PECAS"]

MONTADORAS = [
    "", "volkswagen.com.br", "fiat.com.br", "chevrolet.com.br",
    "ford.com.br", "toyota.com.br", "honda.com.br", "hyundai.com.br",
    "renault.com.br", "jeep.com.br", "peugeot.com.br", "citroen.com.br",
    "nissan.com.br",
]

FILETYPES = ["", "pdf", "xls", "xlsx", "csv", "doc", "docx", "txt", "log"]
