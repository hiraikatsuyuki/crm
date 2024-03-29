from django.db import models


class Nayose(models.Model):
    class Meta:
        verbose_name = verbose_name_plural = "名寄せデータ"

    nayose_id = models.AutoField("名寄せID", primary_key=True)
    eradcode = models.CharField(
        "研究者番号", max_length=8, blank=True, null=True, unique=True)
    shokuincode = models.CharField(
        "職員番号（常勤）", max_length=8, blank=True, null=True, unique=True)
    hijoukincode = models.CharField(
        "職員番号（非常勤）", max_length=8, blank=True, null=True, unique=True)
    kanjishimei_sei = models.CharField("漢字氏名（姓）", max_length=30)
    kanjishimei_mei = models.CharField("漢字氏名（名）", max_length=30)
    kanashimei_sei = models.CharField("カナ氏名（姓）", max_length=30)
    kanashimei_mei = models.CharField("カナ氏名（名）", max_length=30)
    eijishimei_sei = models.CharField(
        "英字氏名（姓）", max_length=30, blank=True, null=True)
    eijishimei_mei = models.CharField(
        "英字氏名（名）", max_length=30, blank=True, null=True)
    betsumei = models.CharField("別名", max_length=30, blank=True, null=True)
    seinengappi = models.DateField("生年月日")
    SEX_CHOICES = (("0", ""), ("1", "男性"), ("2", "女性"), ("9", "その他"))
    seibetsu = models.CharField("性別", choices=SEX_CHOICES, max_length=1)
    orcid = models.CharField("ORCID", max_length=19,
                             blank=True, null=True, unique=True)

    def __str__(self):
        return self.pk
