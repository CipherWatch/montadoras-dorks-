# -*- coding: utf-8 -*-
import io, csv, html
from flask import Flask, request, redirect, url_for, render_template_string, Response
import config, dorks, banco
from paginas import PAGINA

app = Flask(__name__)

def dados_do_form(form):
    palavra = form.get("palavra", "")
    termo = form.get("termo_extra", "")
    site = form.get("site_alvo", "")
    ft = form.get("filetype", "")
    intitle = form.get("intitle", "")
    inurl = form.get("inurl", "")
    dork = dorks.montar_dork(palavra, termo, site, ft, intitle, inurl)
    return {"titulo": (form.get("titulo","").strip() or palavra), "palavra": palavra,
            "termo_extra": termo.strip(), "site_alvo": site.strip(), "filetype": ft.strip(),
            "intitle": intitle.strip(), "inurl": inurl.strip(), "dork": dork,
            "resultado": form.get("resultado","").strip(), "criado_em": dorks.agora()}

@app.route("/")
def home():
    return render_template_string(PAGINA, buscas=banco.listar(), editar=None,
        palavras=config.PALAVRAS_CHAVE, montadoras=config.MONTADORAS,
        filetypes=config.FILETYPES, google=dorks.url_google)

@app.route("/salvar", methods=["POST"])
def salvar():
    d = dados_do_form(request.form)
    if d["dork"]: banco.inserir(d)
    return redirect(url_for("home"))

@app.route("/editar/<int:id>")
def editar_busca(id):
    return render_template_string(PAGINA, buscas=banco.listar(), editar=banco.buscar_por_id(id),
        palavras=config.PALAVRAS_CHAVE, montadoras=config.MONTADORAS,
        filetypes=config.FILETYPES, google=dorks.url_google)

@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):
    banco.atualizar(id, dados_do_form(request.form))
    return redirect(url_for("home"))

@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    banco.excluir(id)
    return redirect(url_for("home"))

@app.route("/relatorio")
def relatorio():
    registros = banco.listar()
    contagem = {}
    for r in registros: contagem[r["palavra"]] = contagem.get(r["palavra"], 0) + 1
    resumo = "".join(f"<li><b>{html.escape(k)}</b>: {v}</li>" for k, v in contagem.items())
    linhas = ""
    for r in registros:
        linhas += f"<tr><td>{r['id']}</td><td>{html.escape(r['titulo'] or '')}</td>" \
                  f"<td><span class='tag'>{html.escape(r['palavra'] or '')}</span></td>" \
                  f"<td>{html.escape(r['termo_extra'] or '')}</td><td>{html.escape(r['site_alvo'] or '-')}</td>" \
                  f"<td><code>{html.escape(r['dork'] or '')}</code></td><td>{html.escape(r['resultado'] or '')}</td>" \
                  f"<td>{html.escape(r['criado_em'] or '')}</td>" \
                  f"<td><a href='{html.escape(dorks.url_google(r['dork']))}' target='_blank'>abrir</a></td></tr>"
    doc = f"""<!DOCTYPE html><html lang="pt-br"><head><meta charset="utf-8">
<title>Relatorio Montadoras Dorks</title><style>
 body{{font-family:Arial,sans-serif;margin:30px;color:#1a1a1a}} h1{{color:#1f6aa5}}
 .box{{background:#f5f5f5;border:1px solid #ddd;border-radius:8px;padding:12px 18px;margin:18px 0}}
 table{{border-collapse:collapse;width:100%;font-size:13px}}
 th,td{{border:1px solid #ccc;padding:7px 9px;text-align:left}}
 th{{background:#1f6aa5;color:#fff}} tr:nth-child(even){{background:#fafafa}}
 code{{background:#eee;padding:1px 4px;border-radius:4px}}
 .tag{{background:#144870;color:#fff;padding:2px 8px;border-radius:10px;font-size:11px}}
</style></head><body>
<h1>RELATORIO DE BUSCAS - MONTADORAS DORKS SITES</h1><p>Gerado em {dorks.agora()}</p>
<div class="box"><b>Total de buscas:</b> {len(registros)}<ul>{resumo}</ul></div>
<table><thead><tr><th>ID</th><th>Titulo</th><th>Palavra</th><th>Termo</th><th>Site</th>
<th>Dork</th><th>Resultado</th><th>Criado em</th><th>Google</th></tr></thead>
<tbody>{linhas}</tbody></table></body></html>"""
    return doc

@app.route("/exportar.csv")
def exportar_csv():
    registros = banco.listar()
    buffer = io.StringIO()
    w = csv.writer(buffer, delimiter=";")
    w.writerow(["id","titulo","palavra","termo_extra","site_alvo","filetype",
                "intitle","inurl","dork","resultado","criado_em","url_google"])
    for r in registros:
        w.writerow([r["id"], r["titulo"], r["palavra"], r["termo_extra"], r["site_alvo"],
                    r["filetype"], r["intitle"], r["inurl"], r["dork"], r["resultado"],
                    r["criado_em"], dorks.url_google(r["dork"])])
    dados = "\ufeff" + buffer.getvalue()
    return Response(dados, mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=buscas_dorks.csv"})

if __name__ == "__main__":
    banco.criar_tabela()
    app.run(host="0.0.0.0", port=8080, debug=True)
