from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
	readonly_fields=['slug']

admin.site.register(Post,PostAdmin)