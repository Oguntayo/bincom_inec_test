from django.db import models

class Party(models.Model):

    partyid = models.CharField(primary_key=True, max_length=10)
    partyname = models.CharField(max_length=255)

    class Meta:
        db_table = "party"

    def __str__(self):
        return self.partyid
    
class LGA(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=255)
    state_id = models.IntegerField()

    class Meta:
        db_table = "lga"

    def __str__(self):
        return self.lga_name
    
class Ward(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    ward_id = models.IntegerField()

    lga = models.ForeignKey(
        LGA,
        db_column="lga_id",
        on_delete=models.CASCADE,
        related_name="wards"
    )

    ward_name = models.CharField(max_length=255)

    class Meta:
        db_table = "ward"

    def __str__(self):
        return self.ward_name

class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)

    ward = models.ForeignKey(
        Ward,
        db_column="ward_id",
        on_delete=models.CASCADE,
        related_name="polling_units"
    )

    lga = models.ForeignKey(
        LGA,
        db_column="lga_id",
        on_delete=models.CASCADE,
        related_name="polling_units"
    )

    polling_unit_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "polling_unit"

    def __str__(self):
        return self.polling_unit_name or str(self.uniqueid)

class AnnouncedPUResult(models.Model):

    result_id = models.AutoField(primary_key=True)

    polling_unit = models.ForeignKey(
        PollingUnit,
        db_column="polling_unit_uniqueid",
        on_delete=models.CASCADE,
        related_name="results"
    )

    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()

    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = "announced_pu_results"
        
class AnnouncedLGAResult(models.Model):

    result_id = models.IntegerField(primary_key=True)

    lga_name = models.CharField(max_length=255)

    party_abbreviation = models.CharField(max_length=10)

    party_score = models.IntegerField()

    class Meta:
        db_table = "announced_lga_results"