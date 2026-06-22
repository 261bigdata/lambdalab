from zipfile import ZipFile
import xml.etree.ElementTree as ET
from pathlib import Path

DOCX = Path('/app/PROYECTO EVALUACIÓN DE FIN DE CARRERA _LIM_JUL_TPP 2026 (A y B).docx')
OUT = Path('/app/infraestructura_gti.md')
NS = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

def texts(node):
    return ''.join(t.text or '' for t in node.findall('.//w:t', NS)).strip()

def p_style(p):
    st = p.find('./w:pPr/w:pStyle', NS)
    if st is None:
        return ''
    return st.attrib.get('{%s}val' % NS['w'], '')

def para_to_md(p):
    txt = texts(p)
    if not txt:
        return None
    style = p_style(p).lower()
    if 'heading1' in style or style == 'title':
        return '# ' + txt
    if 'heading2' in style:
        return '## ' + txt
    if 'heading3' in style:
        return '### ' + txt
    return txt

def table_to_md(tbl):
    rows = []
    for tr in tbl.findall('./w:tr', NS):
        cells = []
        for tc in tr.findall('./w:tc', NS):
            val = ' '.join(filter(None, [texts(p) for p in tc.findall('./w:p', NS)]))
            cells.append(val.replace('|', '\\|'))
        if cells:
            rows.append(cells)
    if not rows:
        return []
    width = max(len(r) for r in rows)
    rows = [r + [''] * (width - len(r)) for r in rows]
    out = []
    out.append('| ' + ' | '.join(rows[0]) + ' |')
    out.append('| ' + ' | '.join(['---'] * width) + ' |')
    for r in rows[1:]:
        out.append('| ' + ' | '.join(r) + ' |')
    return out

with ZipFile(DOCX) as z:
    xml = z.read('word/document.xml')
root = ET.fromstring(xml)
body = root.find('w:body', NS)
lines = []
for child in body:
    tag = child.tag.rsplit('}', 1)[-1]
    if tag == 'p':
        line = para_to_md(child)
        if line:
            lines.append(line)
            lines.append('')
    elif tag == 'tbl':
        lines.extend(table_to_md(child))
        lines.append('')
OUT.write_text('\n'.join(lines).strip() + '\n', encoding='utf-8')
print(OUT)
