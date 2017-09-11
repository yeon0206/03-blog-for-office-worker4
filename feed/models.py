from django.db import models

# Create your models here.

class HashTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class AddTime(models.Model):
    posted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Article(AddTime):
    DEVELOPMENT = "dv"
    PERSONAL = "ps"
    CATEGORY_CHOICES=(
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal"),
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length = 2,
        choices = CATEGORY_CHOICES,
        default = DEVELOPMENT,
    )
    photo = models.ImageField(blank=True, null=True)
    public = models.BooleanField(default=False)

    hashtag = models.ManyToManyField(HashTag)

    def __str__(self):
        return self.title

class Comment(AddTime):
    article = models.ForeignKey(
        Article,
        related_name="article_comments", #아티클에서 커멘트로 접근할때
        on_delete=models.CASCADE
        )
    public = models.BooleanField(default=False)
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    def __str__(self):
        return "{}   Re:  {}".format(self.article.title, self.content)



# class ArticleHasHashTag(models.Model):
#     article = models.ForeignKey(Article)
#     hastag = models.ForeignKey(HashTag)
