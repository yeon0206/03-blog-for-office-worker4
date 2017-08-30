from django.db import models

# Create your models here.
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
    content = models.TextField()
    category = models.CharField(
        max_length = 2,
        choices = CATEGORY_CHOICES,
        default = DEVELOPMENT,
    )
    photo = models.ImageField(blank=True, null=True)
    public = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(AddTime):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    public = models.BooleanField(default=False)

    def __str__(self):
        return "{}   Re:  {}".format(self.article.title, self.content)

class HashTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
