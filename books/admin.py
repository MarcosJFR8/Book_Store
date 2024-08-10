from django.contrib import admin
from .models import Book, Review

# Register your models here.

class ReviewInLine(admin.TabularInline):
    model = Review

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    list_filter = ('author',)
    search_fields = ('title', 'author', 'description')
    ordering = ('title', 'price',)
    inlines = [ReviewInLine, ]

admin.site.register(Book, BookAdmin)
    



