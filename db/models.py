from django.db import models

class Race(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    bonus = models.TextField(blank=True, null=True)
    race = models.ForeignKey(
        Race, related_name="skills", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Guild(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    nickname = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    bio = models.TextField(blank=True, null=True)
    race = models.ForeignKey(
        Race, related_name="players", on_delete=models.CASCADE
    )
    guild = models.ForeignKey(
        Guild, related_name="players", null=True, blank=True, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname
