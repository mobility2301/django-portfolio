from django.contrib import admin
from .models import Project, ContactMessage, Profile
from django.utils.html import format_html
# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'image_tag', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'tech_stack')
    search_fields = ('title', 'description', 'tech_stack')
    ordering = ('-created_at',) 

    def image_tag(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html('<img src="{}" width="50" style="object-fit: cover;"/>', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)
