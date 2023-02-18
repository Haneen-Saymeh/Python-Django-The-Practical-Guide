from django.contrib import admin
from .models import *




# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # readonly_fields=("slug",)
    prepopulated_fields={"slug": ("title", )}
    list_filter=("author","rating",)
    list_display=("title","author",)

admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(Author, AuthorAdmin)


class AddressAdmin(admin.ModelAdmin):
    pass

admin.site.register(Address, AddressAdmin)

admin.site.register(Country)
