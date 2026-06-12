import sqlite3
from config import DB_PATH


# ---- Pedaco 1: conectar -------------------------------------------
def conectar():
    """Abre a conexao com o arquivo do banco e devolve ela."""
    conexao = sqlite3.connect(DB_PATH)
    conexao.row_factory = sqlite3.Row   # permite acessar colunas por nome
    return conexao


# ---- Pedaco 2: criar a tabela -------------------------------------
def criar_tabela():
    """Cria a tabela de buscas, se ainda nao existir."""
    conexao = conectar()
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS buscas (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo      TEXT,
            palavra     TEXT,
            termo_extra TEXT,
            site_alvo   TEXT,
            filetype    TEXT,
            intitle     TEXT,
            inurl       TEXT,
            dork        TEXT,
            resultado   TEXT,
            criado_em   TEXT
        )
    """)
    conexao.commit()
    conexao.close()


# ---- Pedaco 3: salvar e listar ------------------------------------
def inserir(dados):
    """Salva uma nova busca (recebe um dicionario) e devolve o id criado."""
    conexao = conectar()
    cursor = conexao.execute(
        """INSERT INTO buscas
           (titulo, palavra, termo_extra, site_alvo, filetype,
            intitle, inurl, dork, resultado, criado_em)
           VALUES (?,?,?,?,?,?,?,?,?,?)""",
        (dados["titulo"], dados["palavra"], dados["termo_extra"],
         dados["site_alvo"], dados["filetype"], dados["intitle"],
         dados["inurl"], dados["dork"], dados["resultado"], dados["criado_em"]),
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    return novo_id


def listar():
    """Devolve TODAS as buscas, da mais nova para a mais antiga."""
    conexao = conectar()
    linhas = conexao.execute("SELECT * FROM buscas ORDER BY id DESC").fetchall()
    conexao.close()
    return linhas


# ---- Pedaco 4: buscar uma, editar e excluir -----------------------
def buscar_por_id(id):
    """Devolve UMA busca especifica (usada na hora de editar)."""
    conexao = conectar()
    linha = conexao.execute("SELECT * FROM buscas WHERE id=?", (id,)).fetchone()
    conexao.close()
    return linha


def atualizar(id, dados):
    """Atualiza uma busca existente, identificada pelo id."""
    conexao = conectar()
    conexao.execute(
        """UPDATE buscas SET
           titulo=?, palavra=?, termo_extra=?, site_alvo=?, filetype=?,
           intitle=?, inurl=?, dork=?, resultado=? WHERE id=?""",
        (dados["titulo"], dados["palavra"], dados["termo_extra"],
         dados["site_alvo"], dados["filetype"], dados["intitle"],
         dados["inurl"], dados["dork"], dados["resultado"], id),
    )
    conexao.commit()
    conexao.close()


def excluir(id):
    """Apaga uma busca pelo id."""
    conexao = conectar()
    conexao.execute("DELETE FROM buscas WHERE id=?", (id,))
    conexao.commit()
    conexao.close()