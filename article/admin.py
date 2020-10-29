from django.contrib import admin

# Register your models here.
# 导入ArticlerPost和ArticleColumn
from .models import ArticlePost, ArticleColumn

# 注册文章栏目
admin.site.register(ArticleColumn)

# 注册ArticlePost到admin中
admin.site.register(ArticlePost)

