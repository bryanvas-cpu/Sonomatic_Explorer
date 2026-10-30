#!/usr/bin/env python3
"""Regenerate the standalone page, gallery, data.js and photo credits. Python 3 only."""
import base64,csv,html,json
from pathlib import Path
out=Path(__file__).resolve().parents[1]
docs=out/'docs'
r=json.loads((docs/'data.json').read_text())
nodes=[]
def walk(n):
    nodes.append(n)
    for c in n.get('kids',[]): walk(c)
walk(r)
used={n['image'] for n in nodes if n.get('image')}
(docs/'data.js').write_text('window.SONOMATIC_DATA='+json.dumps(r,ensure_ascii=False)+';\n')
credits=[{'item':n['name'],'asset':'assets/'+n['image'],'source':n.get('imageSource',n['url']),'page':n.get('imagePage',''),'caption':n.get('imageCaption','')} for n in nodes if n.get('image')]
with (docs/'photo-sources.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['item','asset','source','page','caption']);w.writeheader();w.writerows(credits)
(docs/'photo-sources.json').write_text(json.dumps(credits,ensure_ascii=False,indent=2))
# Static photo gallery with local images and complete source attribution.
items=[]
for n in nodes:
 if not n.get('image'):continue
 e=html.escape;items.append(f'<article data-search="{e((n["name"]+" "+n["where"]).lower())}"><a href="{e(n["imageSource"])}" target="_blank" rel="noopener noreferrer"><img loading="lazy" src="assets/{n["image"]}" alt="{e(n["name"])}"></a><h2>{e(n["name"])}</h2><p>{e(n["work"])}</p><p><b>Installation:</b> {e(n["where"])}</p><small>{e(n["imageCaption"])}</small><p><a href="{e(n["url"])}" target="_blank" rel="noopener noreferrer">Official product / service source ↗</a> · <a href="{e(n["imageSource"])}" target="_blank" rel="noopener noreferrer">Image document ↗</a></p></article>')
(docs/'gallery.html').write_text('''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sonomatic | Photo catalogue</title><style>body{margin:0;background:#0b141e;color:#e2edf4;font:15px system-ui,sans-serif}header{padding:24px 5%;background:#132d43;color:white}a{color:#8bd6e1}header a{color:#a9e8ed}h1{margin:12px 0}input{background:#172735;color:#e2edf4;box-sizing:border-box;width:100%;padding:14px;border:1px solid #c2d0da;border-radius:9px;font:inherit}.search{padding:20px 5%}main{padding:0 5% 40px;display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px}article{padding:20px;border-radius:14px;background:#172735;border:1px solid #2b4254}article img{width:100%;height:230px;object-fit:contain;background:#fff}h2{font-size:20px}p{line-height:1.6}small{display:block;color:#a5bac9;line-height:1.5}[hidden]{display:none}</style><header><a href="index.html">← Branch explorer</a><h1>Equipment in view</h1><p>Photos and manufacturer illustrations from Sonomatic documents and official pages. Shared family images and historical excerpts are labelled.</p></header><div class="search"><input id="q" type="search" placeholder="Filter photos by item or installation…" aria-label="Filter photos"></div><main>'''+''.join(items)+'''</main><script>document.querySelector('#q').addEventListener('input',e=>{const q=e.target.value.toLowerCase().trim();document.querySelectorAll('article').forEach(a=>a.hidden=!a.dataset.search.includes(q))})</script></html>''')
# Root launch page works from both file:// and project-based GitHub Pages.
(out/'index.html').write_text('<!doctype html><html lang="en"><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=docs/index.html"><title>Sonomatic explorer</title><a href="docs/index.html">Open Sonomatic explorer</a></html>')
(docs/'.nojekyll').touch();(out/'.nojekyll').touch()
# Make a genuinely self-contained HTML alternative: CSS, data, app and all photos embedded.
standalone=(docs/'index.html').read_text();standalone=standalone.replace('<link rel="stylesheet" href="style.css">','<style>'+(docs/'style.css').read_text()+'</style>')
standalone=standalone.replace('<script src="data.js"></script>','<script>'+(docs/'data.js').read_text().replace('</script','<\\/script')+'</script>');standalone=standalone.replace('<script src="app.js"></script>','<script>'+(docs/'app.js').read_text().replace('</script','<\\/script')+'</script>')
# Runtime templates use assets/ + filename; change data image fields to base64 and app src to the whole value.
for file in used:
 data='data:image/'+('png' if file.endswith('.png') else 'jpeg')+';base64,'+base64.b64encode((docs/'assets'/file).read_bytes()).decode()
 standalone=standalone.replace('"image": "'+file+'"','"image": "'+data+'"')
standalone=standalone.replace('src="assets/${esc(n.image)}"','src="${esc(n.image)}"').replace('href="gallery.html"','href="docs/gallery.html"')
(out/'sonomatic_bloom.html').write_text(standalone)

print("Updated data.js, gallery, credits and sonomatic_bloom.html")
