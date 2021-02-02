from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password  # 저장된 password 암호화
from .models import Fcuser
# Create your views here.


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        res_data = {}
        if not (username and password):
            res_data['error'] = '모든 값을 입력해 주세요.'
        else:
            fcuser = Fcuser.objects.get(username=username)
            if check_password(password, fcuser.password):
                # 로그인 처리
                pass
            else:
                res_data['error'] = '잘못된 아이디 또는 비밀번호 입니다.'
        return render(request, 'login.html', res_data)


def register(request):  # request 형태로 전달해줘야 되고
    if request.method == 'GET':
        # 반환하고 싶은 html파일, 폴더를 포함하면 경로 모양으로
        return render(request, 'register.html')
    elif request.method == 'POST':
        # username = request.POST['username'] # 값을 못받고 제출시 오류가 나기 때문에 예외 처리 필요
        # password = request.POST['password']
        # re_password = request.POST['re-password']
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}

        if not (username and useremail and password and re_password):  # 값을 못받는 경우 에러시 에러출력 메세지
            res_data['error'] = '모든 값을 입력해야 합니다.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 일치하지 않습니다!'
            # return HttpResponse('비밀번호가 일치하지 않습니다!')
        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)  # 암호화 함수를 사용해서 암호화 하여 생성
            )

            fcuser.save()

        return render(request, 'register.html', res_data)
# 들어오는 방법이 2가지임, 직접 주소를 작성하는 경우 및 등록버튼을 눌러서 보내는 경우
