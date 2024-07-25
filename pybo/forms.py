from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content', 'public_method', 'issued_date', 'expiry_date', 'push']  # 사용할 필드 지정
        labels = {
            'subject': 'タイトル',
            'content': '内容',
            # 'issued_date': '発信日',
            # 'expiry_date': '満了日',
        }
        widgets = {
            'public_method': forms.RadioSelect,
            'push': forms.RadioSelect,
            'issued_date': forms.DateTimeInput(format='%Y-%m-%d %H:%M'),
            'expiry_date': forms.DateTimeInput(format='%Y-%m-%d %H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['issued_date'].required = False

    # 다른 필드에 대한 추가적인 설정이 필요하다면 여기에 추가할 수 있습니다.