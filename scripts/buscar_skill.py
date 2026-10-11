#!/usr/bin/env python3
"""Busca termos em uma lista de skills do LinkedIn (um termo por linha).

Uso:
  python buscar_skill.py <arquivo.txt> "termo1" "termo2" ...
  python buscar_skill.py --baixar <destino.txt>   # baixa a lista comunitária

A lista comunitária vem de github.com/maciejszewczyk/linkedin-skills
(arquivo linkedin_skills.txt). Pode estar desatualizada: confirme o nome
final no autocompletar do LinkedIn.
Criado por Daniel Rodrigues.
"""
import sys, urllib.request

URL = ("https://raw.githubusercontent.com/maciejszewczyk/linkedin-skills/"
       "master/linkedin_skills.txt")

def baixar(destino):
    with urllib.request.urlopen(URL, timeout=30) as r:
        open(destino, "wb").write(r.read())
    print(f"Lista salva em {destino}")

def buscar(arquivo, termos):
    with open(arquivo, encoding="utf-8", errors="ignore") as f:
        skills = [l.strip() for l in f if l.strip()]
    for t in termos:
        achados = [s for s in skills if t.lower() in s.lower()]
        print(f"\n== {t} ({len(achados)} resultados) ==")
        for s in sorted(achados, key=len)[:15]:
            print(" -", s)

if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "--baixar":
        baixar(sys.argv[2])
    elif len(sys.argv) >= 3:
        buscar(sys.argv[1], sys.argv[2:])
    else:
        print(__doc__)
