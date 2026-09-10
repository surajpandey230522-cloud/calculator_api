from django.db import models

class Calculation(models.Model):
    number1=models.FloatField()
    number2=models.FloatField()
    operator=models.CharField(max_length=15, choices=[('ADDITION', 'Addition'), ('SUBTRACTION', 'Subtraction'), ('MULTIPLICATION', 'Multiplication'), ('DIVISION', 'Division')])
    result=models.FloatField()
    created_on=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.operator=='ADDITION':
            self.result=self.number1 + self.number2
        elif self.operator=='SUBTRACTION':
            self.result= self.number1 - self.number2
        elif self.operator=='MULTIPLICATION':
            self.result=self.number1 * self.number2
        elif self.operator=='DIVISION':
            self.result=self.number1 / self.number2
        else:
            raise ValueError("Enter the valid operator from the options")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.number1} {self.operator} {self.number2} = {self.result}"