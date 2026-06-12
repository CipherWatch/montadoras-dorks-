# -*- coding: utf-8 -*-
PAGINA = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Montadoras Dorks Sites</title>
<style>
  :root {
    --azul:#1f6aa5; --azul2:#144870; --bg:#181a1b; --card:#23272a;
    --txt:#e8eaed; --muted:#9aa0a6; --borda:#3c4043; --campo:#1c1f21;
  }
  * { box-sizing: border-box; }
  body { font-family: 'Segoe UI', Arial, sans-serif; margin:0; background:var(--bg); color:var(--txt); }
  header { background:var(--azul2); padding:18px 28px; box-shadow:0 2px 8px rgba(0,0,0,.3); }
  header h1 { margin:0; font-size:20px; font-weight:600; letter-spacing:.3px; }
  .wrap { padding:24px 28px; max-width:1100px; margin:0 auto; }
  .card { background:var(--card); border-radius:12px; padding:22px 24px; margin-bottom:20px; box-shadow:0 1px 4px rgba(0,0,0,.25); }

  .secao { font-size:13px; text-transform:uppercase; letter-spacing:.6px; color:var(--azul);
           font-weight:700; margin:22px 0 6px; padding-bottom:6px; border-bottom:1px solid var(--borda); }
  .secao:first-child { margin-top:4px; }

  .linha { display:grid; grid-template-columns:170px 1fr; align-items:center; gap:14px; margin:12px 0; }
  .linha label { color:var(--muted); font-size:13px; }
  .linha-dupla { display:grid; grid-template-columns:170px 1fr 150px 1fr; align-items:center; gap:14px; margin:12px 0; }
  .linha-dupla label { color:var(--muted); font-size:13px; }
  .linha-tripla { display:grid; grid-template-columns:1fr 1fr; gap:14px; margin:12px 0; }
  .linha-tripla .rot-cima { display:block; color:var(--muted); font-size:13px; margin-bottom:5px; }

  input, select, textarea { width:100%; padding:10px 12px; border-radius:8px; border:1px solid var(--borda);
    background:var(--campo); color:#fff; font-size:14px; outline:none; transition:border .15s; }
  input:focus, select:focus, textarea:focus { border-color:var(--azul); }
  textarea { min-height:60px; resize:vertical; }

  .preview-box { margin:16px 0 4px; }
  .preview-box .secao { border:none; margin-bottom:8px; }
  .preview { font-family:Consolas,monospace; background:#0f1419; color:#7fd1ff; padding:12px 14px;
    border-radius:8px; word-break:break-all; min-height:22px; border:1px solid var(--borda); }

  .btns { margin-top:18px; display:flex; gap:10px; flex-wrap:wrap; }
  button, .btn { border:none; border-radius:8px; padding:11px 18px; font-size:14px; cursor:pointer;
    color:#fff; background:var(--azul); text-decoration:none; display:inline-block; transition:filter .15s; font-weight:500; }
  button:hover, .btn:hover { filter:brightness(1.12); }
  .btn-red { background:#c5372c; } .btn-gray { background:#5f6368; } .btn-green { background:#2e8b4f; }

  table { width:100%; border-collapse:collapse; font-size:13px; }
  th, td { padding:9px 11px; border-bottom:1px solid #34383b; text-align:left; vertical-align:top; }
  th { background:var(--azul); position:sticky; top:0; }
  code { background:#0f1419; color:#7fd1ff; padding:2px 6px; border-radius:5px; }
  .tag { background:var(--azul2); padding:3px 9px; border-radius:12px; font-size:11px; font-weight:600; }
  a { color:#7fd1ff; }
  .acoes a, .acoes button { font-size:12px; padding:6px 10px; }
  .topbtns { display:flex; gap:8px; }
  .filtro-btn { background:#34383b; }
  .filtro-btn.ativo { background:var(--azul); }
  .barra-filtros { display:flex; gap:6px; flex-wrap:wrap; align-items:center; }
  .filtros-montadora { margin:10px 0 4px; display:flex; align-items:center; gap:8px; }
  .filtros-montadora select { width:auto; min-width:200px; }

  @media (max-width:680px){
    .linha, .linha-dupla { grid-template-columns:1fr; gap:4px; }
  }
</style>
</head>
<body>
<header><h1>Montadoras Dorks Sites</h1></header>
<div class="wrap">

  <div class="card">
    <form method="post" action="{{ url_for('atualizar', id=editar.id) if editar else url_for('salvar') }}">

      <div class="secao">{{ 'Editar busca #' ~ editar.id if editar else 'Localizar paginas com' }}</div>

      <div class="linha-dupla">
        <label>Palavra-chave</label>
        <select name="palavra" id="palavra">
          {% for p in palavras %}<option value="{{ p }}" {{ 'selected' if editar and editar.palavra==p else '' }}>{{ p }}</option>{% endfor %}
        </select>
        <label>Titulo da busca</label>
        <input name="titulo" value="{{ editar.titulo if editar else '' }}" placeholder="ex.: Catalogo de pecas VW">
      </div>

      <div class="linha">
        <label>Todas estas palavras</label>
        <input name="termo_extra" id="termo_extra" value="{{ editar.termo_extra if editar else '' }}" placeholder="ex.: Toyota Corolla catalogo">
      </div>

      <div class="linha">
        <label>Site ou montadora</label>
        <input name="site_alvo" id="site_alvo" list="montadoras" value="{{ editar.site_alvo if editar else '' }}" placeholder="ex.: Toyota  (ou toyota.com.br)">
        <datalist id="montadoras">{% for m in montadoras %}<option value="{{ m }}">{% endfor %}</datalist>
      </div>

      <div class="secao">Em seguida, limite os resultados por</div>

      <div class="linha-dupla">
        <label>Tipo de arquivo</label>
        <select name="filetype" id="filetype">
          {% for f in filetypes %}<option value="{{ f }}" {{ 'selected' if editar and editar.filetype==f else '' }}>{{ f or 'Qualquer formato' }}</option>{% endfor %}
        </select>
        <label>Palavra no titulo</label>
        <input name="intitle" id="intitle" value="{{ editar.intitle if editar else '' }}" placeholder="intitle: ex.: manual">
      </div>

      <div class="linha-dupla">
        <label>Palavra na URL</label>
        <input name="inurl" id="inurl" value="{{ editar.inurl if editar else '' }}" placeholder="inurl: ex.: catalogo">
        <label>Resultado / anotacoes</label>
        <textarea name="resultado">{{ editar.resultado if editar else '' }}</textarea>
      </div>

      <div class="linha-tripla">
        <div>
          <label class="rot-cima">Idioma</label>
          <select id="f_idioma">
            <option value="">Qualquer idioma</option>
            <option value="lang_pt">Portugues</option>
            <option value="lang_en">Ingles</option>
            <option value="lang_es">Espanhol</option>
            <option value="lang_de">Alemao</option>
            <option value="lang_fr">Frances</option>
            <option value="lang_it">Italiano</option>
            <option value="lang_ar">Arabe</option>
            <option value="lang_bg">Bulgaro</option>
            <option value="lang_ca">Catalao</option>
            <option value="lang_zh-CN">Chines (simplificado)</option>
            <option value="lang_zh-TW">Chines (tradicional)</option>
            <option value="lang_hr">Croata</option>
            <option value="lang_cs">Tcheco</option>
            <option value="lang_da">Dinamarques</option>
            <option value="lang_nl">Holandes</option>
            <option value="lang_et">Estoniano</option>
            <option value="lang_fi">Finlandes</option>
            <option value="lang_el">Grego</option>
            <option value="lang_iw">Hebraico</option>
            <option value="lang_hi">Hindi</option>
            <option value="lang_hu">Hungaro</option>
            <option value="lang_is">Islandes</option>
            <option value="lang_id">Indonesio</option>
            <option value="lang_ja">Japones</option>
            <option value="lang_ko">Coreano</option>
            <option value="lang_lv">Letao</option>
            <option value="lang_lt">Lituano</option>
            <option value="lang_no">Norueguic</option>
            <option value="lang_pl">Polones</option>
            <option value="lang_ro">Romeno</option>
            <option value="lang_ru">Russo</option>
            <option value="lang_sr">Servio</option>
            <option value="lang_sk">Eslovaco</option>
            <option value="lang_sl">Esloveno</option>
            <option value="lang_sv">Sueco</option>
            <option value="lang_th">Tailandes</option>
            <option value="lang_tr">Turco</option>
            <option value="lang_uk">Ucraniano</option>
            <option value="lang_vi">Vietnamita</option>
          </select>
        </div>
        <div>
          <label class="rot-cima">Ultima atualizacao</label>
          <select id="f_data">
            <option value="">Qualquer data</option>
            <option value="h">Ultima hora</option>
            <option value="d">Ultimas 24 horas</option>
            <option value="w">Ultima semana</option>
            <option value="m">Ultimo mes</option>
            <option value="y">Ultimo ano</option>
          </select>
        </div>
      </div>

      <div class="preview-box">
        <div class="secao">Dork gerada (preview)</div>
        <div class="preview" id="preview"></div>
      </div>

      <div class="btns">
        <button type="submit">{{ 'Atualizar' if editar else 'Salvar busca' }}</button>
        <a class="btn btn-green" id="btn_google" href="#" target="_blank">Buscar no Google</a>
        {% if editar %}<a class="btn btn-gray" href="{{ url_for('home') }}">Cancelar</a>{% endif %}
      </div>
    </form>
  </div>

  <div class="card">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
      <div class="secao" style="margin:0; border:none;">Buscas salvas ({{ buscas|length }})</div>
      <div class="topbtns">
        <a class="btn" href="{{ url_for('relatorio') }}" target="_blank">Relatorio HTML</a>
        <a class="btn btn-green" href="{{ url_for('exportar_csv') }}">Exportar CSV</a>
      </div>
    </div>

    <input type="text" id="busca" onkeyup="aplicarFiltros()" placeholder="Buscar por termo, pdf, palavra..." style="margin-bottom:12px;">

    <div class="barra-filtros">
      <button type="button" class="btn filtro-btn ativo" data-filtro="TODOS" onclick="filtrar('TODOS', this)">Todos</button>
      {% for p in palavras %}
        <button type="button" class="btn filtro-btn" data-filtro="{{ p }}" onclick="filtrar('{{ p }}', this)">{{ p }}</button>
      {% endfor %}
    </div>

    <div class="filtros-montadora">
      <label style="color:var(--muted); font-size:13px;">Montadora:</label>
      <select id="filtro_montadora" onchange="aplicarFiltros()">
        <option value="">Todas as montadoras</option>
        {% for m in montadoras %}{% if m %}<option value="{{ m }}">{{ m }}</option>{% endif %}{% endfor %}
      </select>
    </div>

    <div style="overflow-x:auto; margin-top:12px;">
    <table>
      <thead><tr><th>ID</th><th>Titulo</th><th>Palavra</th><th>Termo</th><th>Site</th><th>Dork</th><th>Resultado</th><th>Criado em</th><th>Acoes</th></tr></thead>
      <tbody>
      {% for b in buscas %}
        <tr data-palavra="{{ b.palavra }}">
          <td>{{ b.id }}</td><td>{{ b.titulo }}</td><td><span class="tag">{{ b.palavra }}</span></td>
          <td>{{ b.termo_extra }}</td><td>{{ b.site_alvo or '-' }}</td><td><code>{{ b.dork }}</code></td>
          <td>{{ (b.resultado or '')[:40] }}{{ '...' if b.resultado and b.resultado|length>40 else '' }}</td>
          <td>{{ b.criado_em }}</td>
          <td class="acoes" style="white-space:nowrap">
            <a class="btn btn-green" href="{{ google(b.dork) }}" target="_blank">Buscar</a>
            <a class="btn" href="{{ url_for('editar_busca', id=b.id) }}">Editar</a>
            <form method="post" action="{{ url_for('excluir', id=b.id) }}" style="display:inline" onsubmit="return confirm('Excluir a busca #{{ b.id }}?')">
              <button class="btn-red" type="submit">Excluir</button>
            </form>
          </td>
        </tr>
      {% else %}
        <tr><td colspan="9" style="text-align:center; color:#888">Nenhuma busca salva ainda.</td></tr>
      {% endfor %}
      </tbody>
    </table>
    </div>
  </div>

</div>
<script>
  function montarDork() {
    const palavra=document.getElementById('palavra').value.trim();
    const termo=document.getElementById('termo_extra').value.trim();
    const site=document.getElementById('site_alvo').value.trim();
    const filetype=document.getElementById('filetype').value.trim();
    const intitle=document.getElementById('intitle').value.trim();
    const inurl=document.getElementById('inurl').value.trim();
    const partes=[];
    if(palavra) partes.push(palavra);
    if(termo) partes.push(termo);
    if(intitle) partes.push('intitle:'+intitle);
    if(inurl) partes.push('inurl:'+inurl);
    if(site) partes.push('site:'+site);
    if(filetype) partes.push('filetype:'+filetype);
    const dork=partes.join(' ');
    document.getElementById('preview').textContent=dork||'(preencha os campos acima)';
    // Monta a URL do Google. Idioma/regiao/data NAO entram na dork:
    // entram como parametros na URL (lr=, cr=, tbs=qdr:)
    let url='https://www.google.com/search?q='+encodeURIComponent(dork);
    const lr=document.getElementById('f_idioma').value;
    const qdr=document.getElementById('f_data').value;
    if(lr)  url+='&lr='+lr;
    if(qdr) url+='&tbs=qdr:'+qdr;
    document.getElementById('btn_google').href=url;
    return dork;
  }
  document.querySelectorAll('#palavra,#termo_extra,#site_alvo,#filetype,#intitle,#inurl,#f_idioma,#f_data').forEach(function(el){
    el.addEventListener('input', montarDork); el.addEventListener('change', montarDork);
  });
  montarDork();

  let filtroCategoria = 'TODOS';
  function filtrar(alvo, botao) {
    filtroCategoria = alvo;
    document.querySelectorAll('.filtro-btn').forEach(function(b){ b.classList.remove('ativo'); });
    botao.classList.add('ativo');
    aplicarFiltros();
  }
  function aplicarFiltros() {
    const texto = document.getElementById('busca').value.toLowerCase();
    const montadora = document.getElementById('filtro_montadora').value.toLowerCase();
    document.querySelectorAll('tbody tr[data-palavra]').forEach(function(linha){
      const palavra = linha.getAttribute('data-palavra');
      const conteudo = linha.textContent.toLowerCase();
      const passaCategoria = (filtroCategoria === 'TODOS' || palavra === filtroCategoria);
      const passaTexto = (texto === '' || conteudo.indexOf(texto) !== -1);
      const passaMontadora = (montadora === '' || conteudo.indexOf(montadora) !== -1);
      linha.style.display = (passaCategoria && passaTexto && passaMontadora) ? '' : 'none';
    });
  }
</script>
</body>
</html>
"""