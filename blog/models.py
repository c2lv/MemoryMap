from django.db import models
from django.conf import settings

# Create your models here.
def user_path(instance, filename): #파라미터 instance는 Photo 모델을 의미 filename은 업로드 된 파일의 파일 이름
    from random import choice
    import string # string.ascii_letters : ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr) # 8자리 임의의 문자를 만들어 파일명으로 지정
    extension = filename.split('.')[-1] # 배열로 만들어 마지막 요소를 추출하여 파일확장자로 지정
    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    return '%s/%s.%s' % (instance.owner.username, pid, extension) # 예 : wayhome/abcdefgs.png

class Mapmodel(models.Model):
    title = models.CharField(max_length=200)  #제목
    pub_date = models.DateTimeField('date published') #시간
    #장소정보
    body = models.TextField() #내용 입력 창
    image = models.ImageField(upload_to = user_path)
     # 어디로 업로드 할지 지정
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, 'on_delete') # 로그인 한 사용자, many to one relation
    # thumname_image = models.ImageField(blank = True) # 필수입력 해제
    # comment = models.CharField(max_length = 255)
    # pub_date = models.DateTimeField(auto_now_add = True) # 레코드 생성시 현재 시간으로 자동 생성

    # photo = models.ImageField(blank=True, upload_to="blog/%Y/%m/%d")