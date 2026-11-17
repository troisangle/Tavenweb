#!/usr/bin/env python3
"""Generates Taven guide/comparison pages as static HTML. Usage: python3 _tools/build.py .   (edit content.py, then re-run to regenerate /guides and /compare)"""
import json, sys, os, html
sys.path.insert(0, os.path.dirname(__file__))
from content import PAGES, HUB

ROOT = sys.argv[1]
SITE = "https://tavenproductivity.com"
APP = "https://apps.apple.com/app/id6761032737"
UPDATED_ISO = "2026-11-17"
UPDATED_TXT = "November 17, 2026"

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'

def esc(s): return html.escape(s, quote=True)

def nav(current):
    def li(href, text, key):
        cur = ' aria-current="page"' if key == current else ''
        return f'<li><a href="{href}"{cur}>{text}</a></li>'
    return f'''<header class="navbar">
  <div class="container">
    <a href="/" class="brand" aria-label="Taven home">
      <span class="brand-mark">{CHECK}</span>
      Taven
    </a>
    <nav aria-label="Main">
      <ul class="nav-links">
        {li("/", "Product", "home")}
        {li("/features.html", "Features", "features")}
        {li("/what-users-like.html", "What users like", "users")}
        {li("/guides/", "Guides", "guides")}
        {li("/faq.html", "FAQ", "faq")}
        {li("/privacy.html", "Privacy", "privacy")}
        {li("mailto:tavenproductivity@gmail.com", "Contact", "contact")}
      </ul>
    </nav>
    <a href="{APP}" class="btn btn-primary btn-sm">Download</a>
  </div>
</header>'''

FOOTER = f'''<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a href="/" class="brand">
          <span class="brand-mark">{CHECK}</span>
          Taven
        </a>
        <p>A privacy-first task manager for iPhone and iPad that tells you what to do next. Your tasks stay yours.</p>
      </div>
      <div>
        <h4>Product</h4>
        <ul>
          <li><a href="/features.html">Features</a></li>
          <li><a href="/what-users-like.html">What users like</a></li>
          <li><a href="/faq.html">FAQ</a></li>
          <li><a href="{APP}">Download</a></li>
        </ul>
      </div>
      <div>
        <h4>Guides</h4>
        <ul>
          <li><a href="/guides/">All guides</a></li>
          <li><a href="/compare/taven-vs-todoist.html">Taven vs. Todoist</a></li>
          <li><a href="/compare/taven-vs-ticktick.html">Taven vs. TickTick</a></li>
        </ul>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="/privacy.html">Privacy</a></li>
          <li><a href="mailto:tavenproductivity@gmail.com">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="copyright">© <span id="year">2026</span> Taven. All rights reserved.</div>
  </div>
</footer>
<script>document.getElementById('year').textContent = new Date().getFullYear();</script>'''

CTA = f'''<section class="cta frost">
    <div>
      <h2>Stop deciding. Start doing.</h2>
      <p>Taven is free on iPhone and iPad. No subscription. No account.</p>
    </div>
    <a class="btn btn-primary" href="{APP}">Download on the App Store</a>
  </section>'''

ORG = {"@type": "Organization", "name": "Taven", "url": SITE + "/"}

def head(title, desc, url, jsonld):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="color-scheme" content="light" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}" />
  <meta name="robots" content="index, follow, max-snippet:-1" />
  <link rel="canonical" href="{url}" />
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="Taven" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(desc)}" />
  <meta property="og:url" content="{url}" />
  <meta name="twitter:card" content="summary" />
  <meta name="apple-itunes-app" content="app-id=6761032737" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/assets/site.css" />
  <script type="application/ld+json">
{json.dumps(jsonld, indent=2, ensure_ascii=False)}
  </script>
</head>'''

def faq_html(faqs):
    if not faqs: return ""
    items = "\n".join(f'''    <details class="frost"><summary>{esc(q)}</summary><p>{a}</p></details>''' for q, a in faqs)
    return f'''
    <h2 id="faq">Frequently asked questions</h2>
    <div class="faq">
{items}
    </div>'''

def strip_tags(s):
    import re
    return html.unescape(re.sub(r"<[^>]+>", "", s))

def related_html(slugs):
    tiles = []
    for p in PAGES:
        if p["path"] in slugs:
            tiles.append(f'''      <a class="tile frost" href="/{p["path"]}"><div class="k">{p["label"]}</div><h3>{esc(p["short"])}</h3><p>{esc(p["blurb"])}</p></a>''')
    return f'''
    <h2>Keep reading</h2>
    <div class="grid">
{chr(10).join(tiles)}
    </div>'''

def render(p):
    url = f'{SITE}/{p["path"]}'
    section_name, section_url = ("Compare", "/guides/#compare") if p["path"].startswith("compare/") else ("Guides", "/guides/")
    graph = [
        {"@type": "Article", "headline": p["h1_plain"], "description": p["desc"],
         "datePublished": UPDATED_ISO, "dateModified": UPDATED_ISO,
         "author": ORG, "publisher": ORG, "mainEntityOfPage": url},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": section_name, "item": SITE + section_url},
            {"@type": "ListItem", "position": 3, "name": p["short"], "item": url}]},
    ]
    if p.get("faqs"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in p["faqs"]]})
    if p.get("itemlist"):
        graph.append({"@type": "ItemList", "name": p["h1_plain"], "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n} for i, n in enumerate(p["itemlist"])]})
    jsonld = {"@context": "https://schema.org", "@graph": graph}
    out = f'''{head(p["title"], p["desc"], url, jsonld)}
<body>

{nav("guides")}

<main class="container">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="{section_url}">{section_name}</a><span>/</span>{esc(p["short"])}</nav>

  <section class="page-head">
    <div class="label">{p["label"]}</div>
    <h1 class="h1">{p["h1"]}</h1>
    <p class="lede">{p["lede"]}</p>
    <div class="updated">Last updated: <time datetime="{UPDATED_ISO}">{UPDATED_TXT}</time></div>
  </section>

  <section class="answer frost" aria-label="Short answer">
    <h2>Short answer</h2>
    <p>{p["answer"]}</p>
  </section>

  <article class="article">
{p["body"]}
{faq_html(p.get("faqs"))}
{related_html(p.get("related", []))}
  </article>

  {CTA}
</main>

{FOOTER}
</body>
</html>
'''
    dest = os.path.join(ROOT, p["path"])
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    open(dest, "w").write(out)

def render_hub():
    url = SITE + "/guides/"
    def tiles(kind):
        return "\n".join(f'''      <a class="tile frost" href="/{p["path"]}"><div class="k">{p["label"]}</div><h3>{esc(p["short"])}</h3><p>{esc(p["blurb"])}</p></a>'''
                         for p in PAGES if p["kind"] == kind)
    jsonld = {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "name": HUB["title"], "description": HUB["desc"], "url": url, "publisher": ORG},
        {"@type": "ItemList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "url": f'{SITE}/{p["path"]}', "name": p["short"]} for i, p in enumerate(PAGES)]}]}
    out = f'''{head(HUB["title"], HUB["desc"], url, jsonld)}
<body>

{nav("guides")}

<main class="container">
  <section class="page-head">
    <div class="label">Guides</div>
    <h1 class="h1">Get more done by <span>deciding less.</span></h1>
    <p class="lede">{HUB["lede"]}</p>
  </section>

  <article class="article" style="max-width:none;padding-top:0">
    <h2>Productivity guides</h2>
    <div class="grid">
{tiles("guide")}
    </div>
    <h2>App roundups</h2>
    <div class="grid">
{tiles("list")}
    </div>
    <h2 id="compare">Comparisons</h2>
    <div class="grid">
{tiles("compare")}
    </div>
  </article>

  {CTA}
</main>

{FOOTER}
</body>
</html>
'''
    os.makedirs(os.path.join(ROOT, "guides"), exist_ok=True)
    open(os.path.join(ROOT, "guides/index.html"), "w").write(out)

def render_faq():
    from content import FAQ
    url = SITE + "/faq.html"
    title = "Taven FAQ — Pricing, Privacy, Devices & How It Works"
    desc = "Answers to common questions about Taven, the free AI to-do list and task manager for iPhone and iPad: how it picks your next task, pricing, accounts, privacy, devices and habits."
    jsonld = {"@context": "https://schema.org", "@type": "FAQPage", "url": url, "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
        for g, items in FAQ for q, a in items]}
    groups = []
    for g, items in FAQ:
        qs = "\n".join(f'      <details class="frost"><summary>{esc(q)}</summary><p>{a}</p></details>' for q, a in items)
        groups.append(f'    <h2>{g}</h2>\n    <div class="faq">\n{qs}\n    </div>')
    page_head = head(title, desc, url, jsonld).replace('content="article"', 'content="website"')
    out = f"""{page_head}
<body>

{nav("faq")}

<main class="container">
  <section class="page-head">
    <div class="label">FAQ</div>
    <h1 class="h1">Questions, <span>answered.</span></h1>
    <p class="lede">Everything people usually ask about Taven. Can't find your answer? <a class="inline" href="mailto:tavenproductivity@gmail.com">Email us</a>.</p>
  </section>

  <article class="article" style="padding-top:0">
{chr(10).join(groups)}
  </article>

  {CTA}
</main>

{FOOTER}
</body>
</html>
"""
    open(os.path.join(ROOT, "faq.html"), "w").write(out)

def render_users():
    from content import USERS
    url = SITE + "/what-users-like.html"
    title = "What Users Like About Taven — Design, AI Suggestions, Habits, Calendar & Stats"
    desc = "What Taven users tell us they love: the simple, aesthetic design, the AI Suggest feature, habits and one-time tasks together, the calendar and completion statistics."
    jsonld = {"@context": "https://schema.org", "@type": "WebPage", "name": "What users like about Taven",
              "url": url, "description": desc, "publisher": ORG,
              "about": {"@type": "MobileApplication", "name": "Taven", "operatingSystem": "iOS, iPadOS", "url": SITE + "/"}}
    jump = "".join(f'<a class="chip" href="#{t["id"]}">{t["title"]}</a>' for t in USERS)
    blocks = []
    for i, t in enumerate(USERS, 1):
        quotes = "".join(f'<blockquote class="quote"><p>“{esc(q)}”</p><cite>— {esc(who)}</cite></blockquote>' for q, who in t["quotes"])
        blocks.append(f"""    <section class="theme frost" id="{t["id"]}">
      <div class="theme-n">{i:02d}</div>
      <div>
        <h2>{t["title"]}</h2>
        <h3>What users tell us</h3>
        <p>{t["said"]}</p>{quotes}
        <h3>Why it matters</h3>
        <p>{t["why"]}</p>
        <p><a href="{t["link"][0]}">{t["link"][1]} →</a></p>
      </div>
    </section>""")
    page_head = head(title, desc, url, jsonld).replace('content="article"', 'content="website"')
    out = f"""{page_head}
<body>

{nav("users")}

<main class="container">
  <section class="page-head">
    <div class="label">What users like</div>
    <h1 class="h1">Why people <span>stick with</span> Taven.</h1>
    <p class="lede">We read every message we get. These are the five things Taven users bring up most.</p>
    <div class="chips">{jump}</div>
  </section>

  <div class="themes">
{chr(10).join(blocks)}
  </div>

  <section class="share frost">
    <div>
      <h2>Tell us what you like</h2>
      <p>Using Taven? A quick App Store review helps other people find it, and we read every email.</p>
    </div>
    <div class="share-actions">
      <a class="btn btn-primary" href="{APP}?action=write-review">Write a review</a>
      <a class="btn btn-ghost" href="mailto:tavenproductivity@gmail.com">Email us</a>
    </div>
  </section>

  {CTA}
</main>

{FOOTER}
</body>
</html>
"""
    open(os.path.join(ROOT, "what-users-like.html"), "w").write(out)

if __name__ == "__main__":
    for p in PAGES:
        render(p)
    render_hub()
    render_faq()
    render_users()
    print("built", len(PAGES) + 3, "pages")
