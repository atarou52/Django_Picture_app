# UserCreationクラスをインポート
from django.contrib.auth.forms import UserCreationForm

# models.pyで定義したカスタムUserモデルをインポート
from .models import CustomUser

# インナークラスMetaのクラス変数をオーバーライドする
class CustomUserCreationForm(UserCreationForm): 
    # UserCreationFormのサブクラス
    class Meta:
        # UserCreationFormのインナークラス
        # Attributes:
        # model:連携するUserモデル
        # fields:フォームで使用するフィールド
        
        # 連携するUserモデルを設定
        model = CustomUser
        
        # フォームで使用するフィールドを設定
        # username, email, password, password2(確認用)
        fields = ('username', 'email', 'password1', 'password2')
    
        