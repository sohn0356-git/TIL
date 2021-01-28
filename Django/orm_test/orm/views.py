from django.shortcuts import render

from orm.models import Board

# Create your views here.
def getboard(request):
    boards = Board.objects.all()
    context = {'allboard' : boards}
    print(boards)
    return render(request, 'board.html', context)