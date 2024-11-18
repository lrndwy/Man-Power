from django.contrib import admin
from unfold.admin import ModelAdmin
from import_export.admin import ImportExportModelAdmin
from unfold.contrib.import_export.forms import ExportForm, ImportForm, SelectableFieldsExportForm
from .models import ManPower
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(ManPower)
class ManPowerAdmin(ModelAdmin, ImportExportModelAdmin):
    import_form_class = ImportForm
    export_form_class = ExportForm
    
    # Menampilkan kolom di list view
    list_display = ('tanggal', 'nama_projek', 'keterangan', 'total_pekerja', 'total_alat_berat')
    
    # Menambahkan filter
    list_filter = ('tanggal', 'nama_projek')
    
    # Menambahkan pencarian
    search_fields = ('nama_projek', 'keterangan')
    
    # Mengelompokkan field dalam fieldsets
    fieldsets = (
        ('Informasi Umum', {
            'fields': ('tanggal', 'nama_projek', 'keterangan')
        }),
        ('Pekerja Harian', {
            'fields': (
                'besi', 'baja', 'batu_galli_cor', 'kayu', 'bekisting', 'paving',
                'sipil', 'atap', 'plafon', 'kaca', 'scaffolding', 'opr_excavator',
                'opr_crane', 'mekanik', 'me', 'finishing', 'cat', 'aluminium',
                'cleaning', 'operator', 'rigger', 'flagman', 'security', 'safety',
                'subcon', 'canwood', 'bobok_pancang', 'helper', 'waterproofing', 'drv_dt',
                'kja', 'welder'
            )
        }),
        ('Total Pekerja', {
            'fields': (
                'jumlah_pekerja_harian', 'staff_pekerja'
            )
        }),
        ('Alat Berat', {
            'fields': (
                'excavator', 'virbo', 'engkel', 'dump_truck', 'pc'
            )
        }),
    )
    
    # Mengaktifkan fitur Unfold
    list_fullwidth = True  # Tampilan full width
    warn_unsaved_form = True  # Peringatan saat ada perubahan belum disimpan

