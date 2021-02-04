from django import forms


# 입력 받을 값은 제목과 내용 두개
class BoardForm(forms.Form):
    title = forms.CharField(error_messages={
        'required': '제목을 입력해 주세요.'
    }, max_length=128, label="제목")
    contents = forms.CharField(error_messages={
        'required': '내용을 입력해 주세요.'
    }, widget=forms.Textarea, label="내용")
