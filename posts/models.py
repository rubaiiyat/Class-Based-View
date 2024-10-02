from django.db import models
from categories.models import Category
from django.contrib.auth.models import User


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="posts/media/uploads/",
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        cat = ",".join([str(c) for c in self.category.all()])
        return f"{self.title} -- {cat}"


class CommnetPost(models.Model):
    post = models.ForeignKey(Posts, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} on {self.post}"
