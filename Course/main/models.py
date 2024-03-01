from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    rate = models.FloatField(verbose_name='rate')
    count = models.IntegerField(verbose_name='Counts', default=0)

    def __str__(self):
        return self.title

    def update_rating(self, new_rating):
      if self.count  == 0:
        self.rate = new_rating
      else:  
        self.rate = (self.rate * self.count + new_rating) / (self.count + 1)
        self.count += 1
        self.save()
