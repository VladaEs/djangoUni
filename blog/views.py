from django.shortcuts import render,redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm
from .models import Booking
from .models import Register
from django.core.mail import send_mail


class PostView(View):
    """Вывод записей"""
    def get(self,request):
        posts= Post.objects.all()
        count = Post.objects.filter().count()
        return render(request,'blog/blog.html',{'post_list':posts, 'count': count})


class PostDetail(View):
    """Страница записи"""
    def get(self,request, pk):
        post= Post.objects.get(id= pk)
        return  render(request, 'blog/blog_detail.html', {"post":post})

class AddComments(View):
    """Добавляем комментарий"""
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if(form.is_valid()):
            form = form.save(commit=False)
            form.post_id=pk
            form.save()
        return redirect(f'/{pk}')

class bookTable(View):
    """Переход на страницу bookTable"""
    def get(self, request):
        tables=Booking.selected_tables
        print(tables)
        return render(request,'blog/BookTable.html', {"tables":tables})

class BookingPost(View):
    def post(self ,request):
        selected_tables = request.POST.getlist('selected_tables')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        date= request.POST.get('dateGet')
        # Создаем объект Booking и сохраняем в базе данных
        booking = Booking.objects.create(
            selected_tables=', '.join(selected_tables),
            surname=surname,
            email=email,
            date=date,
        )
        return redirect('/book_table')
    def get(self,request):
        selected_date = request.GET.get('date')
        print(selected_date)

        bookings_for_date = Booking.objects.filter(date=selected_date)

        # Check if there are any records
        if bookings_for_date.exists():
            selected_tables_values = bookings_for_date.values_list('selected_tables', flat=True)

            # Combine arrays and get unique numbers
            result_list = list(set(str(x).strip() for values in selected_tables_values for x in values.split(',')))

            print(result_list)
        else:
            result_list = []
        return render(request, 'blog/BookTable.html', {'selected_date': selected_date, "tables": result_list})

class LoginPage(View):
    """Переход на страницу Login"""

    def get(self, request):
        return render(request, 'blog/Login.html')


class LoginPageCheck(View):
    def post(self,request):
        nickname= request.POST.get("NickName")
        password=request.POST.get('password')
        # Check if a user with the provided nickname and password exists
        user_exists = Register.objects.filter(nickname=nickname, password=password).exists()
        if user_exists:
            # User exists, you can redirect to a success page or do something else
            return render(request, 'blog/blog.html', {"login": True} )
        else:
            # User does not exist or password is incorrect, you can redirect to a failure page or do something else
            return render(request, 'blog/blog.html', {"login": False})

"""class RegisterUser(View):
    formClass=UserCreationForm
    template_name=  'blog/register.html'"""
