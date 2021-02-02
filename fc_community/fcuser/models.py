from django.db import models

# Create your models here.


class Fcuser(models.Model):
    username = models.CharField(max_length=32, verbose_name='사용자명')
    useremail = models.EmailField(
        max_length=128, verbose_name='사용자 이메일')  # Email 형태 검증 까지 해줌
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트 캠퍼스 사용자'  # 기본적으로 복수형을 지원하기 때문에 s가 자동으로 붙게 되어 있음
        verbose_name_plural = '패스트 캠퍼스 사용자'  # 복수형이름을 따로 지정하여 자동으로 붙는 s를 제거 가능
