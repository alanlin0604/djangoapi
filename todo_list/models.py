from django.db import models

class ToDoItem(models.Model):
    title = models.CharField(max_length=255)  # 標題
    content = models.TextField()  # 內容
    status = models.BooleanField(default=False)  # 狀態 (已完成/未完成)
    created_at = models.DateTimeField(auto_now_add=True)  # 建立時間
    updated_at = models.DateTimeField(auto_now=True)  # 最後更新時間

    def __str__(self):
        return self.title
