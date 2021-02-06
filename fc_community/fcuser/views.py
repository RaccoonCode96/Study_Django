from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password  # 저장된 password 암호화
from .models import Fcuser
from .forms import LoginForm
# Create your views here.


def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)  # pk primary key
        k = fcuser
    else:
        k = "로그인이 필요합니다."
    return render(request, 'home.html', {'k': k})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)  # POST 데이터를 넣어서 할당
        if form.is_valid():  # is_valid() 함수를 통해 정상적인지 검증(값이 단지 들어가 있는지 확인만 함)
            # 세션 코드
            request.session['user'] = form.user_id
            return redirect('/')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

    return redirect('/')


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
