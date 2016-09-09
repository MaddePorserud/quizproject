from django.db import models

# Create your models here.
#models.Model anropar klasser i Django.
class Quiz(models.Model):
		quiz_number = models.PositiveIntegerField()
		name = models.CharField(max_length=100)
		description = models.TextField()
		def __str__(self):
			return self.name
		# Anger här information om vad de olika objekten i klassen kommer
		# innehålla. GEnom att speca Integer (Siffra) lagras ett anpassat område för detta

class Question(models.Model):
	question = models.TextField()
	answer1 = models.CharField(max_length=100)
	answer2 = models.CharField(max_length=100)
	answer3 = models.CharField(max_length=100)
	correct = models.PositiveIntegerField()
	quiz = models.ForeignKey(Quiz, related_name="questions")