
import datetime
import urllib.parse


def montar_dork(palavra, termo, site, filetype, intitle, inurl):
    """
    Junta os campos preenchidos em uma string de busca do Google.

    Exemplo:
        montar_dork("VIN", "WVWZZZ", "fiat.com.br", "pdf", "", "")
        ->  '"VIN" WVWZZZ site:fiat.com.br filetype:pdf'
    """
    partes = []
    if palavra:
        partes.append(palavra.strip())        # aspas na palavra-chave
    if termo and termo.strip():
        partes.append(termo.strip())
    if intitle and intitle.strip():
        partes.append(f"intitle:{intitle.strip()}")
    if inurl and inurl.strip():
        partes.append(f"inurl:{inurl.strip()}")
    if site and site.strip():
        partes.append(f"site:{site.strip()}")
    if filetype and filetype.strip():
        partes.append(f"filetype:{filetype.strip()}")
    return " ".join(partes)                            # une tudo com espacos


def url_google(dork):
    """Transforma a dork em um link de busca do Google (com a URL codificada)."""
    return "https://www.google.com/search?q=" + urllib.parse.quote(dork or "")


def agora():
    """Devolve a data e hora atuais como texto, ex.: 11/06/2026 14:30:00."""
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")