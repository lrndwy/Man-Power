from django.db import models

class ManPower(models.Model):
    tanggal = models.DateField()
    nama_projek = models.CharField(max_length=100)
    keterangan = models.TextField(blank=True, null=True)

    # Pekerja Harian
    besi = models.IntegerField(default=0)
    baja = models.IntegerField(default=0)
    batu_galli_cor = models.IntegerField(default=0)
    kayu = models.IntegerField(default=0)
    bekisting = models.IntegerField(default=0)
    paving = models.IntegerField(default=0)
    sipil = models.IntegerField(default=0)
    atap = models.IntegerField(default=0)
    plafon = models.IntegerField(default=0)
    kaca = models.IntegerField(default=0)
    scaffolding = models.IntegerField(default=0)
    opr_excavator = models.IntegerField(default=0)
    opr_crane = models.IntegerField(default=0)
    mekanik = models.IntegerField(default=0)
    me = models.IntegerField(default=0)
    finishing = models.IntegerField(default=0)
    cat = models.IntegerField(default=0)
    aluminium = models.IntegerField(default=0)
    cleaning = models.IntegerField(default=0)
    operator = models.IntegerField(default=0)
    rigger = models.IntegerField(default=0)
    flagman = models.IntegerField(default=0)
    security = models.IntegerField(default=0)
    safety = models.IntegerField(default=0)
    subcon = models.IntegerField(default=0)
    canwood = models.IntegerField(default=0)
    bobok_pancang = models.IntegerField(default=0)
    helper = models.IntegerField(default=0)
    waterproofing = models.IntegerField(default=0)
    drv_dt = models.IntegerField(default=0)
    kja = models.IntegerField(default=0)
    welder = models.IntegerField(default=0)
    
    # Pekerja
    jumlah_pekerja_harian = models.IntegerField(default=0)
    staff_pekerja = models.IntegerField(default=0)
    
    
    # Alat Berat
    excavator = models.IntegerField(default=0)
    virbo = models.IntegerField(default=0)
    engkel = models.IntegerField(default=0)
    dump_truck = models.IntegerField(default=0)
    pc = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nama_projek} ({self.tanggal})"

    def total_pekerja(self):
        return sum([
            self.jumlah_pekerja_harian, self.staff_pekerja,
        ])
    
    def total_alat_berat(self):
        return sum([
            self.excavator, self.virbo, self.engkel, self.dump_truck, self.pc
        ])
        
    class Meta:
        verbose_name = "Man Power"
        verbose_name_plural = "Man Power"
        ordering = ['-tanggal']