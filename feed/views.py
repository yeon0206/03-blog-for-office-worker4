from django.shortcuts import render
from .models import Article,Comment,HashTag
# Create your views here.

def index(request):
    
    ctx={
    }
    return render(request, "index.html", ctx )

def detail(request):
    pass

# def about(request):
#     pass
