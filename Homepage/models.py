from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

GENDER = (
    (0, 'Female'),
    (1, 'Male')
)


class Data(models.Model):

    name = models.CharField(max_length=100, null=True)
    age = models.PositiveSmallIntegerField(null=True)
    height = models.PositiveSmallIntegerField(null=True)
    sex = models.PositiveSmallIntegerField(choices=GENDER, null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        classifier_model = joblib.load('classifier_model/ML_prdictor_model.joblib')
        self.predictions = classifier_model.predict(
            [[self.age, self.height, self.sex]])
        return super().save(*args, *kwargs)


    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.name


