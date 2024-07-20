from django.forms import ModelForm
from .models import PicturePost

class PicturePostForm(ModelForm):
    """ModelFormのサブクラス
    """
    class Meta:
        """ModelFormのインナークラス
        
        Attributes:
            model: モデルのクラス
            fields: フィールドを指定
        """
        model = PicturePost
        fields = [
            'category',
            'title',
            'comment',
            'image1',
            'image2']
