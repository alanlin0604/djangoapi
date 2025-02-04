class ShoeDetail(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE, related_name="details")
    image_url = models.CharField(max_length=255, null=True, blank=True)  # 鞋子圖片 URL

    def __str__(self):
        return f"{self.shoe.brand} - {self.shoe.model}"
