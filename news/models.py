from django.db import models
from django.contrib.auth.models import User

class NewsModel(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title = models.CharField(max_length=100)
    info = models.CharField(max_length=500)
    regions = models.CharField(max_length=30)
    
    
    def __str__(self) -> str:
        return f"{self.title} - {self.info} - {self.regions}"
    
    
class CommentsModle(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(NewsModel, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.comment} - {self.user} - {self.news}"
    

