# トップページのビューへのリダイレクトを追加

from django.urls import path
from . import views

# URLパターンを逆引きできるように名前を付ける
app_name = 'picture'

# URLパターンを登録する変数
# pictureアプリへのアクセスに対して
# viewsモジュールのIndexViewを実行
urlpatterns = [
    path('', views.IndexView.as_view(),
         name = 'index'),
    
    # 写真投稿ページへのアクセスに対して
    # viewsモジュールのCreatePictureViewを実行
    path(
        'post/',
        views.CreatePictureView.as_view(),
        name='post'),
    
    # 投稿完了ページへのアクセスに対して
    # viewsモジュールのPostSuccessViewを実行
    path(
        'post_done/',
        views.PostSuccessView.as_view(),
        name='post_done'),
    
    # カテゴリページ
    # picture/<Categorysテーブルのid値>にマッチング
    # <int:category>は辞書{category: id値(int)}として
    # CategoryViewに渡される
    path(
        'picture/<int:category>',
        views.CategoryView.as_view(),
        name = 'picture_cat'),

    # ユーザーの投稿一覧ページ
    # picture/<ユーザーテーブルのid値>にマッチング
    # <int:user>は辞書{user: id値(int)}として
    # CategoryViewに渡される
    path(
        'user-list/<int:user>',
        views.UserView.as_view(),
        name = 'user_list'),
    
    # 詳細ページ
    # picture-detail/<Picture postsテーブルのid値>
    # にマッチング
    # <int:pk>は辞書{pk: id値(int)}として
    # DetailViewに渡される
    path(
        'picture-detail/<int:pk>',
        views.DetailView.as_view(),
        name = 'picture_detail'),
    
    # マイページ
    # mypage/へのアクセスはMypageViewを実行
    path(
        'mypage/',
        views.MypageView.as_view(),
        name = 'mypage'),

    # 投稿写真の削除
    # picture/<Picture postsテーブルのid値>/delete/
    # にマッチング
    # <int:pk>は辞書{pk: id値(int)}として
    # DetailViewに渡される
    path(
        'picture/<int:pk>/delete/',
        views.PictureDeleteView.as_view(),
        name = 'picture_delete'),
]
