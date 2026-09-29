#!/usr/bin/env python3
"""Assemble site/dist/index.html from the parts in site/src.

shell.html holds the page chrome, styles and router. sprites.svg holds every
character and prop drawing as <symbol>s. The numbered section files are the
home page, the seven lessons and the cheat sheet, in order.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
SRC, DIST = ROOT / "src", ROOT / "dist"
DIST.mkdir(exist_ok=True)

shell = (SRC / "shell.html").read_text()
sprites = (SRC / "sprites.svg").read_text()
sections = "\n".join(p.read_text() for p in sorted(SRC.glob("[0-9][0-9]-*.html")))

page = shell.replace("<!--@sprites-->", sprites).replace("<!--@sections-->", sections)
(DIST / "index.html").write_text(page)
print(f"wrote {DIST/'index.html'} ({len(page.encode())//1024} KB, {len(list(SRC.glob('[0-9][0-9]-*.html')))} sections)")
