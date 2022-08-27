from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User


class Book(models.Model):
    name = models.CharField(max_length=200)
    image= models.ImageField(default='default.jpg', upload_to='profile_pics',null=True,blank=True)
    author = models.CharField(max_length=200)
    resume = models.TextField(null=True,blank=True)
    publication_year = models.DateTimeField()
    def average_rating(self):
        return self.review_set.aggregate(Avg('rating'))['rating__avg']
    def get_all_reviews(self):
        return self.review_set.count()     
    def __unicode__(self):
        return self.name
    def get_year(self):
        return self.publication_year.year
    def __str__(self):
        return self.name

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    #user_name = models.CharField(max_length=100)
    comment = models.TextField(null=True,blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return ("Review made by " + str(self.user) +" on " + str(self.book))