from django.contrib import admin
from .models import Post, Comments, Booking, Register



# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author')
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','post')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("surname", "selected_tables")

@admin.register(Register)
class RegisterPerson(admin.ModelAdmin):
    list_display = ("nickname", "surname")