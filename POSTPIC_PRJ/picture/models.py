from django.db import models
# accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser

class Category(models.Model):
    """投稿する写真のカテゴリを管理するモデル
    """
    # カテゴリ名のフィールド
    title = models.CharField(
        # フィールドのタイトル
        verbose_name='カテゴリ',
        # 最大文字数20
        max_length=20)
    
    def __str__(self):
        """オブジェクトを文字列に変換して返す

        Returns:
            str: カテゴリ名
        """
        return self.title

class PicturePost(models.Model):
    """投稿されたデータを管理するモデル
    """
    # CustomUserモデル(のuser_id)とPicturePostモデルを
    # 1対多の関係で結び付ける
    # CustomUserが親でPicturePostが子の関係となる
    user = models.ForeignKey(
        CustomUser,
        # フィールドのタイトル
        verbose_name='ユーザー',
        # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
        on_delete=models.CASCADE
        )
    # Categoryモデル(のtitle)とPicturePostモデルを
    # 1対多の関係で結び付ける
    # Categoryが親でPicturePostが子の関係となる
    category = models.ForeignKey(
        Category,
        # フィールドのタイトル
        verbose_name='カテゴリ',
        # カテゴリに関連付けられた投稿データが存在する場合は
        # そのカテゴリを削除できないようにする
        on_delete=models.PROTECT
        )
    # タイトル用のフィールド
    title = models.CharField(
        # フィールドのタイトル
        verbose_name='タイトル',
        # 最大文字数200
        max_length=200
        )
    # コメント用のフィールド
    comment = models.TextField(
        # フィールドのタイトル
        verbose_name='コメント',
        )
    # イメージのフィールド1
    image1 = models.ImageField(
        # フィールドのタイトル
        verbose_name='イメージ1',
        # MEDIA_ROOT以下のpicturesにファイルを保存  
        upload_to = 'pictures'
        )
    # イメージのフィールド2
    image2 = models.ImageField(
        # フィールドのタイトル
        verbose_name='イメージ2',
        # MEDIA_ROOT以下のpicturesに画像ファイルを保存
        upload_to = 'pictures',
        # フィールド値の設定は必須でない
        blank=True,
        # データベースにnullが保存されることを許容
        null=True              
        )
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(
        # フィールドのタイトル
        verbose_name='投稿日時',
        # 日時を自動追加
        auto_now_add=True
        )
    
    def __str__(self):
        """オブジェクトを文字列に変換して返す

        Returns:
            str: 投稿記事のタイトル
        """
        return self.title
