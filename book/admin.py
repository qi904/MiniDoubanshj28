from django.contrib import admin
from book.models import Book, Review
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description')
    search_fields = ['title', 'description']
    list_editable = ( 'description','title')
admin.site.register(Book,BookAdmin)

admin.site.register(Review)