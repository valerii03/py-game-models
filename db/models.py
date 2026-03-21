from django.db import models


class Race(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=30)
    motto = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=30)
    email = models.EmailField()
    bio = models.TextField()
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nickname
