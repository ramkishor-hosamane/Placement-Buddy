from django.db import models
from django_mysql.models import ListCharField
from Home.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)  
    date =  models.CharField(max_length=20)
    job_title = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=10)
    experience = models.CharField(max_length=200)
    questions = ListCharField(
        base_field=models.CharField(max_length=20),
        max_length=(20 * 20)
    )

    def __str__(self):
        return self.date
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)

    def __str__(self):
        return self.comment[:10]

class FavouritePost(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    def __str__(self):
        return self.post.date
