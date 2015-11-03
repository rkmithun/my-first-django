
# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
   
''' how to work on model objects? ''' 
'''

from django.contrib.auth.models import User
User.objects.all()

#returns a user model object
admin=User.objects.get(username='admin')

#select all query; return the django .db.models.query.QuerySet
Post.objects.all()

#create objects
Post.objects.create(author=admin,title="my 4th post",text="will this work from CLI",created_date=timezone.now())
#Filter objects
Post.objects.filter(author=me)
#title like %blog%
Post.objects.filter(title__contains='blog')
#created_date <= timezone.now()
Post.objects.filter(created_date__lte=timezone.now())

#get a model object and apply its method
p=Post.objects.get(title='Python Myenv')
p.publish()
Post.objects.filter(published_date__lte=timezone.now())
#order by
Post.objects.order_by('created_date')
# reverse order
Post.objects.order_by('-created_date')


for p in Post.objects.order_by('created_date'): 
    print "{} {} {}".format(p.author,p.title,p.text)

#chain QuerySets
Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

'''