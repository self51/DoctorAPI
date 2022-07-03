from django.contrib import admin
from medic.models import Direction, Doctor


class DirectionAdmin(admin.ModelAdmin):
    list_display = ['name_direction', 'slug', 'sort_number']
    ordering = ['name_direction', 'sort_number']
    search_fields = ['name_direction', 'slug']


admin.site.register(Direction, DirectionAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'birth_date', 'sort_number', 'experience']
    ordering = ['name', 'sort_number']
    search_fields = ['name', 'slug', 'experience']


admin.site.register(Doctor, DoctorAdmin)
