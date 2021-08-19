from django.contrib import admin
from demo.models import Note, User


# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(Note, NoteAdmin)
admin.site.register(User, UserAdmin)
