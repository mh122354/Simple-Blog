from django.contrib import admin
from .models import Post






#Information on how to display model information
class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','publish',
                  'status')
    list_filter = ('status','created','publish','author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status','publish']


#Creates site based on Post class in models
admin.site.register(Post,PostAdmin)


