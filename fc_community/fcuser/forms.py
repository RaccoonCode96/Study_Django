from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(error_messages={
        'required': '아이디를 입력해 주세요.'
    }, max_length=32, label="사용자 이름")
    password = forms.CharField(error_messages={
        'required': '비밀번호를 입력해 주세요.'
    }, widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        # 값의 빈 값인지 유효성 검증(is_valid)에서 clean을 불러서 검증하고 검증된 값을 cleande_data에 사전 형태로 저장함
        # (여기서 맞지 않으면 바로 진행안하고 나가게 됨), super를 통해 원래 있던 clean()를 먼저 호출
        # clean을 사용하여 오버라이딩 한것임 즉, is_valid가 clean을 사용하는 습성을 이용해서 clean을 새로 정의하고
        # cleaned_data를 먼저 원래 clean()함수 기능을 실행하게 끔 하기 위해서 정의하는 것
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            fcuser = Fcuser.objects.get(username=username)
            if not check_password(password, fcuser.password):
                # form 안에 기본적으로 있는 add_error()함수로 특정 필드에 error를 넣는 함수임
                self.add_error('password', '비밀번호가 일치하지 않습니다.')
            else:
                self.user_id = fcuser.id
