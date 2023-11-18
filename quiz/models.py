from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Question(models.Model):
    content = models.TextField()
    index = models.IntegerField(validators=[MinValueValidator(1)])

    def get_right_answers(self):
        return set(self.options.filter(iscorrect=True).values_list('id', flat=True))
    
    def check_answers(self, answers):
        return self.get_right_answers() == set(answers)
        
    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['index']
    


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    content = models.TextField()
    iscorrect = models.BooleanField(default=False)

    def __str__(self):
        return self.content

class QuizResult(models.Model):
    student_name = models.CharField(max_length=50)
    total_question = models.IntegerField(default=0)
    right_answers = models.IntegerField(default=0)
    wrong_answers = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def empty_answers(self):
        return self.total_question - (self.right_answers + self.wrong_answers)
    

    def __str__(self):
        return self.student_name