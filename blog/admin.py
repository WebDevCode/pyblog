from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
  list_display = ["title", "slug", "author", "publish", "status"] #display on the Posts page
  list_filter = ["status", "created", "publish", "author"]
  search_fields = ["title", "body"]
  prepopulated_fields = {"slug": ["title"]} # a dict with fields mapped to a list of fields
  raw_id_fields = ["author"]
  date_hierarchy = "publish"
  ordering = ["status", "publish"]

admin.site.register(Post, PostAdmin)
