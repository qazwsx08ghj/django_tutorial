from django.shortcuts import render

# Create your views here.


def main(request):
    posts = {'title': 'Title', 'content': 'Content'}, {'title': 'Title2', 'content': 'Content2'}

    return render(request, 'home.html', {"posts": posts})
