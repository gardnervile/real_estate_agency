from django.contrib import admin
from .models import Flat, Complaint, Owner


class FlatsInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address',)
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'get_owners')
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    raw_id_fields = ('liked_by',)
    inlines = [FlatsInline]

    def get_owners(self, obj):
        return ", ".join([owner.owner for owner in obj.owners.all()])
    get_owners.short_description = "Владельцы"


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'phone', 'pure_phone')
    raw_id_fields = ('flats',)
    readonly_fields = ('pure_phone',)



class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('user','flat')


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)