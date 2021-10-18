from django.shortcuts import render

from . import util


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

