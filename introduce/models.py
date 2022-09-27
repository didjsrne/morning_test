from django.db import models


# Create your models here.
class AccessLog(models.Model):
    class Meta:
        db_table = "accesslog"

    """
    1. default : 기본적으로 사용될 날짜를 지정
    2. auto_now : 데이터가 수정될 때마다 갱신됨
    3. auto_now_add : 데이터가 생성될 때 시간을 기록
    """
    created_at = models.DateTimeField("접속 시간", auto_now_add=True)  # read only
    location = models.CharField("접속 경로", max_length=256)

    # 보기 좋게 만들기
    def __str__(self):
        return f"{self.created_at} / {self.location}"
