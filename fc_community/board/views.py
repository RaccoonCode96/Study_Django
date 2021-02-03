from django.shortcuts import render
from .models import Board
# Create your views here.


def board_list(request):
    # all()은 모든 오브젝트를 가져오고 order_by는 정렬인데 '-'는 역순을 의미 즉, 최신것으로 가져오겠다.
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards': boards})
