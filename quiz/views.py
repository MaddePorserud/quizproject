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
def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[int(quiz_number)-1],
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)
def question(request, quiz_number, question_number):
	context = {
	"question_number":question_number,
	"question":"Hur många bultar har ölandsbron)",
	"answer1":"12",
	"answer2":"66 400",
	"answer3":"7 428 954",
	"quiz_number":quiz_number,
	}
	return render(request, "quiz/question.html",context)
def completed(request, quiz_number):
	context = {
	"correct":12,
	"total":20,
	"quiz_number":quiz_number,
	}
	return render(request, "quiz/results.html", context)
