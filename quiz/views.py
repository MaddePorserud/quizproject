from django.shortcuts import render

# Create your views here.


quizzes = [
{"quiz_number":1,
"name":"KLassiska böcker",
"description":"Hur bra kan du dina klassiker?"},
{"quiz_number":2,
"name":"Största lagen",
"description": "Kan du dina lang"},
{"quiz_number":3,
"name":"Värdelns mest kända hackare",
"description":"HAckerhistoria är viktig, kan du den?"},
]
def startpage (request):
	context = {
	"quizzes":quizzes,
	}
	return render(request, "quiz/start.html", context)
def quiz(request):
	return render(request, "quiz/quiz.html")
def question(request):
	return render(request, "quiz/question.html")
def completed(request):
	return render(request, "quiz/results.html")
