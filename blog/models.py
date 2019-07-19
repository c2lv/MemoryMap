from django.db import models
from django.conf import settings
from accounts.models import User
from django.urls import reverse

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Category(models.Model):
    DEFAULT = "카테고리"

    CATEGORY_CHOICE = [
        ("FOOD", "음식"),
        ("CAR", "자동차"),
        ("ETC", "기타"),
        # Add Category
        #("DB에 저장되는 이름", "읽기 좋은 뜻이 있는 이름"),
    ]

    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICE,
        default=DEFAULT,
    )


def user_path(instance, filename):  # 파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
    from random import choice
    from string import ascii_letters  # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    arr = [choice(ascii_letters) for _ in range(8)]

    pid = ''.join(arr)  # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1]  # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정

    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    return '%s/%s.%s' % (instance.owner.username, pid, extension)  # 예 : wayhome/abcdefgs.png


THUMBNAIL_WIDTH = 120
THUMBNAIL_HIGHT = 100


class Mapmodel(models.Model):

    # 로그인 한 사용자, many to one relation
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              null=True,
                              )

    title = models.CharField(max_length=200)  #제목
    content = models.TextField()
    
    # 주소 정보
    address = models.CharField(max_length=200, default="장소를 지정해주세요.")

    # 레코드 생성시 현재 시간으로 자동 생성
    pub_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # image는 선택사항
    image = models.ImageField(blank=True,null=True,upload_to=user_path)
    thumbnail = ImageSpecField(source='image',
                              processors=[ResizeToFill(THUMBNAIL_WIDTH, THUMBNAIL_HIGHT)],
                              format="JPEG",
                              options={'quality':60})

    # 색, 카테고리를 나타내는 태그
    # category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default="없음")
    # category = models.CharField(choices=CATEGORY_CHOICE)

    # like = models.ManyToManyField(User, related_name='likes')

    # photo = models.ImageField(blank=True, upload_to="blog/%Y/%m/%d")

    def get_absolute_url(self): # redirect시 활용
        return reverse('blog:home', args=[self.id]) # args=[self.id])

    class Meta:
        ordering = ('-pub_date',)


class Memo(models.Model):
    # map Data가 삭제되면 함께 삭제되야함
    target = models.ForeignKey(
                            Mapmodel, 
                            on_delete=models.CASCADE, 
                            related_name='memos')
    owner = models.ForeignKey(
                            settings.AUTH_USER_MODEL,
                            on_delete=models.SET_NULL,
                            null=True,
                              )
    
    pub_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    approved = models.BooleanField(default=False)
    memo = models.TextField()

    class Meta:
        ordering = ('-pub_date',)