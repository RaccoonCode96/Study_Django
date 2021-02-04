from django.db import models

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey(
        'fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='작성자')
    # on_delete=models.CASCADE 는 models의 key가 삭제 되면 해당 모델도 지우겠다.
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트 캠퍼스 게시글'  # 기본적으로 복수형을 지원하기 때문에 s가 자동으로 붙게 되어 있음
        verbose_name_plural = '패스트 캠퍼스 게시글'  # 복수형이름을 따로 지정하여 자동으로 붙는 s를 제거 가능
