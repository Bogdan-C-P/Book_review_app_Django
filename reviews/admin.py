from django.contrib import admin
from .models import Book,Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('book', 'rating', 'user', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user']
    search_fields = ['comment']

admin.site.register(Book)
admin.site.register(Review, ReviewAdmin)
