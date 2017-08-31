from django.shortcuts import render
from .models import Article,Comment,HashTag
# Create your views here.

def index(request):
    #GET and posted_at
    category = request.GET.get("category")

    if not category: #카테고리가 존재하지 않으면
        article_list = Article.objects.all()
    else:
        article_list = Article.objects.filter(category=category)

    hashtag_list = HashTag.objects.all()
    # category_list = set([article.get_category_display() for article in article_list])

    category_list = set([
        (article.category, article.get_category_display())
        for article in article_list
        ])

    # for article in article_list:
    #     category_list.add(article.get_category_display())


    ctx={
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }

    # print(ctx.keys())
    # print(ctx.values())
    # print(ctx.items())

    return render(request, "index.html", ctx )

def detail(request, article_id):
    article = Article.objects.get(id=article_id)
    hashtag_list = HashTag.objects.all()
    ctx={
        "article" : article,
        "hashtag_list" : hashtag_list,
    }
    return render(request, "detail.html", ctx)

# def about(request):
#     pass
