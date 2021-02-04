from django.shortcuts import render, redirect
from fcuser.models import Fcuser
from .models import Board
from .forms import BoardForm
# Create your views here.


def board_list(request):
    # all()은 모든 오브젝트를 가져오고 order_by는 정렬인데 '-'는 역순을 의미 즉, 최신것으로 가져오겠다.
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards': boards})


def board_write(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})


def board_detail(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'board_detail.html', {'board': board})
