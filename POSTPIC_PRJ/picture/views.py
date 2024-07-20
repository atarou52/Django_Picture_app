from django.shortcuts import render
# django.views.genericからTemplateViewをインポート
from django.views.generic import TemplateView
# django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
# django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
# formsモジュールからPicturePostFormをインポート
from .forms import PicturePostForm
# method_decoratorをインポート
from django.utils.decorators import method_decorator
# login_requiredをインポート
from django.contrib.auth.decorators import login_required
# django.views.genericからListViewをインポート
from django.views.generic import ListView
# modelsモジュールからモデルPicturePostをインポート
from .models import PicturePost
# django.views.genericからDetailViewをインポート
from django.views.generic import DetailView
# django.views.genericからDeleteViewをインポート
from django.views.generic import DeleteView

class IndexView(ListView):
    """トップページのビュー
    """    
    # index.htmlをレンダリングする
    template_name ='index.html'

    # モデルBlogPostのオブジェクトにorder_by()を適用して
    # 投稿日時の降順で並べ替える
    queryset = PicturePost.objects.order_by('-posted_at')

    # 1ページに表示するレコードの件数
    paginate_by = 9

# デコレーターにより、CreatePictureViewへのアクセスは
# ログインユーザーに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクト
@method_decorator(login_required, name='dispatch')
class CreatePictureView(CreateView):
    """写真投稿ページのビュー
        PicturePostFormで定義されているモデルとフィールドと連携して
        投稿データをデータベースに登録する
    
    Attributes:
        form_class: モデルとフィールドが登録されたフォームクラス
        template_name: レンダリングするテンプレート
        success_url: データベスへの登録完了後のリダイレクト先
    """
    # forms.pyのPicturePostFormをフォームクラスとして登録
    form_class = PicturePostForm
    # レンダリングするテンプレート
    template_name = 'post_ picture.html'
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('picture:post_done')

    def form_valid(self, form):
        """CreateViewクラスのform_valid()をオーバーライド

        Args:
            form (django.forms.Form): PicturePostFormオブジェクト

        Returns:
            HttpResponseRedirect:
                スーパークラスのform_valid()の戻り値を返すことで、
                success_urlで設定されているURLにリダイレクトさせる
        """        
        # commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値
        # (HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    """投稿完了ページのビュー
    
    Attributes:
        template_name: レンダリングするテンプレート
    """
    # index.htmlをレンダリングする
    template_name ='post_success.html'

class CategoryView(ListView):
    """カテゴリページのビュー
    
    Attributes:
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    """
    # index.htmlをレンダリングする
    template_name ='index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
        """クエリを実行する

        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset()のオーバーライドによりクエリを実行する

        Returns:
            クエリによって取得されたレコード
        """            
        # self.kwargsでキーワードの辞書を取得し、
        # categoryキーの値(Categorysテーブルのid)を取得
        category_id = self.kwargs['category']
        # filter(フィールド名=id)で絞り込む
        categories = PicturePost.objects.filter(
            category=category_id).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return categories

class UserView(ListView):
    """ユーザーの投稿一覧ページのビュー
    
    Attributes:
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    """
    # index.htmlをレンダリングする
    template_name ='index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
        """クエリを実行する
        
        self.kwargsの取得が必要なため、クラス変数querysetではなく
        get_queryset()のオーバーライドによりクエリを実行する
        
        Returns:
            クエリによって取得されたレコード
        """
        # self.kwargsでキーワードの辞書を取得し、
        # userキーの値(ユーザーテーブルのid)を取得
        user_id = self.kwargs['user']
        # filter(フィールド名=id)で絞り込む
        user_list = PicturePost.objects.filter(
            user=user_id).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return user_list

class DetailView(DetailView):
    """詳細ページのビュー
    
    投稿記事の詳細を表示するのでDetailViewを継承
    Attributes:
        template_name: レンダリングするテンプレート
        model: モデルのクラス
    """
    # detail.htmlをレンダリングする
    template_name ='detail.html'
    # クラス変数modelにモデルBlogPostを設定
    model = PicturePost

class MypageView(ListView):
    '''マイページのビュー
    
    Attributes:
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
    '''
    # mypage.htmlをレンダリングする
    template_name ='mypage.html'
    # 1ページに表示するレコードの件数
    paginate_by = 9

    def get_queryset(self):
        """クエリを実行する

        self.kwargsの取得が必要なため、クラス変数querysetではなく、
        get_queryset（）のオーバーライドによりクエリを実行する

        Returns:
            クエリによって取得されたレコード
        """        
        # 現在ログインしているユーザー名は
        # HttpRequest.userに格納されている
        # filter(userフィールド=userオブジェクト)で絞り込む
        queryset = PicturePost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        # クエリによって取得されたレコードを返す
        return queryset

class PictureDeleteView(DeleteView):
    """レコードの削除を行うビュー
    
    Attributes:
        model: モデル
        template_name: レンダリングするテンプレート
        paginate_by: 1ページに表示するレコードの件数
        success_url: 削除完了後のリダイレクト先のURL
    """
    # 操作の対象はPicturePostモデル
    model = PicturePost
    # picture_delete.htmlをレンダリングする
    template_name ='picture_delete.html'
    # 処理完了後にマイページにリダイレクト
    success_url = reverse_lazy('picture:mypage')

    def delete(self, request, *args, **kwargs):
        """レコードの削除を行う

        Args:
            request (WSGIRequest(HttpRequest)):
            args(dict)
            kwargs(dict):
                キーワード付きの辞書
                {'pk': 21}のようにレコードのidが渡される
        Returns:
            HttpResponseRedirect(success_url):
                戻り値を返してsuccess_urlにリダイレクト
        """
        # スーパークラスのdelete()を実行
        return super().delete(request, *args, **kwargs)