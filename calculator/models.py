from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    groups = models.ManyToManyField(Group, blank=True, related_name='calculator_users')
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='calculator_users',
        verbose_name=('user permissions'),
        help_text=('Specific permissions for this user.'),
        related_query_name='calculator_user',
    )

class Calculation(models.Model):
    master = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calculations')
    left_operand = models.ForeignKey('Number', on_delete=models.CASCADE, related_name='left_calculations')
    right_operand = models.ForeignKey('Number', on_delete=models.CASCADE, related_name='right_calculations')
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE)
    result = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.left_operand} {self.operation} {self.right_operand} = {self.result}"

class Number(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)

class Operation(models.Model):
    symbol = models.CharField(max_length=10)
    function_name = models.CharField(max_length=50)

    def __str__(self):
        return self.symbol
