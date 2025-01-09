from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    # Your existing Post model fields (title, content, etc.)
    pass

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Link to Post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User (author)
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(default=timezone.now)  # Timestamp when comment is created
    updated_at = models.DateTimeField(default=timezone.now)  # Timestamp for the last update
    
    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
