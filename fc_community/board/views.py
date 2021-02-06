from django.shortcuts import render, redirect
from fcuser.models import Fcuser
from .models import Board
from tag.models import Tag
from .forms import BoardForm
from django.http import Http404
from django.core.paginator import Paginator
# Create your views here.


def board_list(request):
    # all()은 모든 오브젝트를 가져오고 order_by는 정렬인데 '-'는 역순을 의미 즉, 최신것으로 가져오겠다.
    all_boards = Board.objects.all().order_by('-id')
    page = int(request.GET.get('p', 1))
    # Paginator 화면에 보여줄 게시글 수를 설정하여 page 객체로 만들어 버림
    paginator = Paginator(all_boards, 3)

    boards = paginator.get_page(page)

    return render(request, 'board_list.html', {'boards': boards})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login/')

    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            for tag in tags:
                if not tag:
                    continue

                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)

            return redirect('/board/list/')

    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다.')

    return render(request, 'board_detail.html', {'board': board})
