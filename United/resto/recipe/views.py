from django.shortcuts import render

# Create your views here.
from recipe.models import Recipe, Suggestion
from recipe.services import get_recipes_all, get_recipes_one


def index(requests):
    recipes = Recipe.objects.all()

    ctx = {
        "recipes": recipes
    }

    return render(requests, 'site/index.html', ctx)


def about(requests):
    return render(requests, 'site/about.html', {})


def contact(requests):
    suggest = Suggestion()
    if requests.POST:
        suggest.name = requests.POST.get('name')
        suggest.email = requests.POST.get('email')
        suggest.subject = requests.POST.get('subject')
        suggest.message = requests.POST.get('message')
        suggest.save()

    return render(requests, 'site/contact.html')

def recipe(requests, pk=1):
    return render(requests, 'site/receipe_post.html', {})
