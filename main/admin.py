from django.contrib import admin

from .models import Education, Publication


class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution')
    list_display_links = ('title', 'institution')
    list_per_page = 25


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Education, EducationAdmin)
admin.site.register(Publication, PublicationAdmin)