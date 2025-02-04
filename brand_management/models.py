class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)  # 品牌名稱
    logo_url = models.CharField(max_length=255, null=True, blank=True)  # LOGO 圖片 URL

    def __str__(self):
        return self.name
