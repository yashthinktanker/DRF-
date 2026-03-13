from django.db import models



class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Model_name(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,related_name='model_name')
    modelname = models.CharField(max_length=100)
    color = models.CharField(max_length=10,default="black")
    m_img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.modelname


class InstaUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


    profile_picture = models.ImageField(upload_to='instagram/profile_pics/', blank=True, null=True)

    followers_count = models.PositiveIntegerField(default=0)
    following_count = models.PositiveIntegerField(default=0)
    posts_count = models.PositiveIntegerField(default=0)

    is_verified = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    password = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.username
    


class InstaPost(models.Model):
    user = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    caption = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to='instagram/posts/',
        blank=True,
        null=True
    )

    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)

    posted_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.id}"
    
class InstaLike(models.Model):
    user = models.ForeignKey(
        InstaUser,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    post = models.ForeignKey(
        InstaPost,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    liked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"
    
