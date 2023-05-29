import wikipedia

def getWikiSummary(query, lang="en"):
    if(type(lang) == None.__class__):
        lang = "en"
    wikipedia.set_lang(lang)
    search_result = wikipedia.search(query, results=1)
    if len(search_result) >= 1:
        search_result = search_result[0]
        page = wikipedia.page(search_result, auto_suggest=False)
        title = page.title
        url = page.url
        summary = wikipedia.summary(title, sentences=2, auto_suggest=False)
        return [{"title": title, "url": url, "summary": summary}]
    else:
        return []

