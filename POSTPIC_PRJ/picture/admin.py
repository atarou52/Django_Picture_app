from django.contrib import admin

# CustomUserをインポート
from .models import Category, PicturePost

class CategoryAdmin(admin.ModelAdmin):
    """管理ページのレコード一覧に表示するカラムを設定する
    """
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

class PicturePostAdmin(admin.ModelAdmin):
    """管理ページのレコード一覧に表示するカラムを設定する
    """
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')

# Django管理サイトにCategory、CategoryAdminを登録
admin.site.register(Category, CategoryAdmin)

# Django管理サイトにPicturePost、PicturePostAdminを登録
admin.site.register(PicturePost, PicturePostAdmin)
