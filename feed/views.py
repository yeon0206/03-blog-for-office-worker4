from django.shortcuts import render
from .models import Article,Comment,HashTag
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):
    #GET and #POST
    category = request.GET.get("category") #/?category=development or personal
                                            # <QueryDict: {'category':['검색']}>
    hashtag = request.GET.get("hashtag")

    hashtag_list = HashTag.objects.all() #조건 없이 항상 다보일수 있도록 if밖에 위치
    if not category and not hashtag:
        article_list= Article.objects.all()
    elif category:
        article_list= Article.objects.filter(category=category)
    else:
        article_list= Article.objects.filter(hashtag__name=hashtag)
        #hashtag=hashtag
        #hashtag__name=hashtag Article에있는 hashtag를 검색하는것이아니라
                              #Hashtag안에있는 name을 검색해줘야함
                              #따라서 Hastag name에 접근하기위해 hashtag__name을 씀


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

    # detail페지이에 댓글을 달아보자

    # 첫번째 방법:
    # comment_list = Comment.objects.filter(article__id=article_id)
         #Article(일) : Comment(다)
         #따라서 Comment에서 Article에있는 내용에 접근이 가능함
         #어떻게? 이렇게, #article__id 데이타베이스접근

    # 두번째 방법:
    comment_list = article.article_comments.filter(public=True)
        # comment_list = article.article_comments.all()
        # 문제가있음, article에서 comment로 접근을 할수가 없음
        # 그래서 comment 인스턴스에 접근코드를 작성해줘야함(related_name)

    # 세번째 방법:
     #두번째 방법처럼 comment 인스턴스에 접그코드를 작성하고
     #view에서 처리없이 바로 html에서 for comment in article.articel_comments.all 로 접근

    ctx={
        "article" : article,
        "comment_list" : comment_list, #두번째 방법
        "hashtag_list" : hashtag_list,

        }

    if request.method == "GET":
        pass

    elif request.method == "POST":
        username = request.POST.get("username")
        content = request.POST.get("content")

        Comment.objects.create(
            article=article,
            username=username,
            content=content,
        )

        return HttpResponseRedirect("/{}/".format(article_id))
        # print(username)
        # print(content)

    return render(request, "detail.html", ctx)

# def about(request):
#     pass
