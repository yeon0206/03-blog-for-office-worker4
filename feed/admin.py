from django.contrib import admin
from .models import Article,Comment,HashTag




class ArticleAdmin(admin.ModelAdmin):
    list_display=['id','title','posted_at','public']
    list_display_links=['title']
    list_editable=['public']

admin.site.register(Article,ArticleAdmin)

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display=['id','__str__','username','posted_at','public']
    list_display_links=['__str__']
    list_editale=['public']

admin.site.register(Comment,CommentAdmin)

class HashTagAdmin(admin.ModelAdmin):
    pass

admin.site.register(HashTag,HashTagAdmin)
