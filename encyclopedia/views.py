from django.shortcuts import render
from django import forms
from . import util
import re



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    if util.get_entry(title):
        return render(request, "encyclopedia/title.html", {
            'title_name': title,
            'title_context': util.get_entry(title)
        })
    else:
        return render(request, "encyclopedia/none_title.html", {
            'title_name': title
        })


# функція пошуку на сторінці
def search(request):
    found_matches = []
    if request.method == 'GET':
        form = request.GET
    list_of_articles = [item.lower() for item in util.list_entries()]
    if form['q'] in list_of_articles:
        return title(request, form['q'])
    elif list_of_articles:
        for article in list_of_articles:
            if re.findall(form['q'].lower(), article):
                found_matches.append(article)
        return render(request, "encyclopedia/search.html", {
            'contents': found_matches
        })
    else:
        return render(request, "encyclopedia/search.html", {
            'search_content': form['q']
        })
