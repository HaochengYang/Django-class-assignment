from django.shortcuts import render
from models import users, messages, comments

# Create your views here.
def index(request):
    users.objects.create(first_name="Haocheng", last_name="Yang")
    users_list = users.objects.all()
    print(users_list)

    messages.objects.create(user_id=users.objects.get(id=1),  messages="just dosplay this message on the commend prote")
    messages_list = messages.objects.all()
    print(messages_list)

    comments.objects.create(user_id=users.objects.get(id=1), messages_id=messages.objects.get(id=1), comment="This is Haocheng's comment")
    comments_list = comments.objects.all()
    print(comments_list)
    return render(request, 'wall/index.html')
