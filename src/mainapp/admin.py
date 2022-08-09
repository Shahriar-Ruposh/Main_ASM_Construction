from django.contrib import admin
from .models import MainLogo, Services, Project, ProjectGallery, About,Category,Qualities,ServicesGallery,Profile,Brands
from django.db import models
from tinymce.widgets import TinyMCE

class textEditorAdmin(admin.ModelAdmin):
   formfield_overrides = {
   models.TextField: {'widget': TinyMCE()}
   }


admin.site.register(MainLogo)
admin.site.register(Qualities, textEditorAdmin)
admin.site.register(Services, textEditorAdmin)
admin.site.register(ServicesGallery)
admin.site.register(Category)
admin.site.register(Project, textEditorAdmin)
admin.site.register(ProjectGallery)
admin.site.register(Profile, textEditorAdmin)
admin.site.register(About, textEditorAdmin)
admin.site.register(Brands)

