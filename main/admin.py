from django.contrib import admin

from .models import Education, Publication, Research, Teaching, Resource


class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution')
    list_display_links = ('title', 'institution')
    list_per_page = 25


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)


class ResearchAdmin(admin.ModelAdmin):
    list_display = ('research',)


class TeachingAdmin(admin.ModelAdmin):
    list_display = ('topic',)


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic')


admin.site.register(Education, EducationAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Teaching, TeachingAdmin)
