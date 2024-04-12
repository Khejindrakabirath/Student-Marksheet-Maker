from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class studentModel(models.Model):
    student_Name = models.CharField(max_length = 20)
    engMark = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    mathMark = models.IntegerField( 
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    sciMark = models.IntegerField( 
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    socMark = models.IntegerField( 
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    nepMark = models.IntegerField( 
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    heaMark = models.IntegerField( 
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    def total(self):
        return f"{self.engMark + self.mathMark + self.sciMark + self.socMark + self.nepMark + self.heaMark}"
    
    def percent(self):
        return f"{'%.2f' % (((self.engMark + self.mathMark + self.sciMark + self.socMark + self.nepMark + self.heaMark)/600)*100)}"
    
    def Remarks(self):
        if(self.engMark >= 40 and self.mathMark >= 40 and self.sciMark >= 40 and self.socMark >= 40 and self.nepMark >= 40 and self.heaMark >= 40):
            return "Pass"
        else:
            return "Fail"
    def alert(self):
        if(self.engMark > 100 and self.mathMark > 100 and self.sciMark > 100 and self.socMark > 100 and self.nepMark > 100 and self.heaMark > 100):
            return "Fail"
        else:
            return "pass"

    def engRemarks(self):
        if(self.engMark >= 40):
            return "Pass"
        else:
            return "Fail"
    
    def mathRemarks(self):
        if(self.mathMark >= 40):
            return "Pass"
        else:
            return "Fail"

    def sciRemarks(self):
        if(self.sciMark >= 40):
            return "Pass"
        else:
            return "Fail"
    
    def socRemarks(self):
        if(self.socMark >= 40):
            return "Pass"
        else:
            return "Fail"

    def nepRemarks(self):
        if(self.nepMark >= 40):
            return "Pass"
        else:
            return "Fail"

    def heaRemarks(self):
        if(self.heaMark >= 40):
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return self.student_Name
