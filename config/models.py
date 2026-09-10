from django.db import models

class Calculation(models.Model):
    number1=models.PositiveIntegerField()
    number2=models.PositiveIntegerField()
    operator=models.CharField(max_length=10, choices=[('ADDITITON', 'Addition'), ('SUBTRACTION', 'Subtraction'), ('MULTIPLICATION', 'Multiplication'), ('DIVISION', 'Division')])
    result=models.PositiveIntegerField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.number1} {self.operator} {self.number2} = {self.result}"