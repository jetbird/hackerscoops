from django.contrib import admin
from article.models import Article, Category,Photo, Comment,ImageThumbnail

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    pass
class CategoryAdmin(admin.ModelAdmin):
    pass
class PhotoAdmin(admin.ModelAdmin):
    pass
class CommentAdmin(admin.ModelAdmin):
    pass
class ImageThumbnailAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(ImageThumbnail,ImageThumbnailAdmin)
