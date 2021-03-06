from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from . import util
import re
import random


class NewPageForm(forms.Form):
    title_name = forms.CharField(label="Article name")
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 5}))




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


def edit(request, title):
    text = util.get_entry(title)
    return render(request, "encyclopedia/edit.html", {
        'form': NewPageForm({'title_name':title, 'text':text}),
        'title_name': title
    })

def saveedit(request):
    if request.method == 'POST':
        form = NewPageForm(request.POST)
        if form.is_valid():
            article_name = form.cleaned_data['title_name']
            content = form.cleaned_data['text']
            util.save_entry(article_name, content)
            return HttpResponseRedirect(reverse('wiki:title', args=[article_name]))  # робимо перенаправлення на збережену статю

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

# функція створення нової сторінки
def create_page(request):
    if request.method == 'POST':
        form = NewPageForm(request.POST)
        if form.is_valid():
            title_name = form.cleaned_data['title_name']
            text = form.cleaned_data['text']
            util.save_entry(title_name, f"#{title_name}  {text}")
            return title(request, title_name)
    return render(request, "encyclopedia/create_page.html", {
                'form': NewPageForm()
            })


# функція вибору випадкової сторінки
def random_choice(request):
    random_title = random.choice(util.list_entries())

    return render(request, "encyclopedia/randompage.html", {
        'random_title_name': random_title,
        'random_title_context': util.get_entry(random_title)
        
    })

