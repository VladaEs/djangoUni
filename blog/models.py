from django.db import models
from datetime import datetime
class Post(models.Model):
    '''данные о посте'''
    title= models.CharField("Заголовок записи",max_length=100)
    description= models.TextField("текст записи - контент")
    author= models.CharField("Имя автора",max_length=100 )
    date= models.DateField("Дата создания записи")
    img = models.ImageField("картинка", upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'
    class Meta:
        verbose_name="Запись"
        verbose_name_plural="Записи"

class Comments(models.Model):
    """Комментарии"""
    email= models.EmailField()
    name= models.CharField("Имя", max_length=50)
    text_comments= models.TextField("Текст комментария", max_length=2000)
    post= models.ForeignKey(Post , verbose_name="Публикация", on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}, {self.post}'
    class Meta:
        verbose_name="Комментарий"
        verbose_name_plural="Комментарии"

class Register(models.Model):
    """РЕгистрация польззователя"""
    surname = models.CharField("Фамилия", max_length=50)
    email = models.EmailField("Email")
    nickname= models.CharField("Имя пользователя", max_length=25)
    password= models.CharField("Password", max_length=50)
    def __str__(self):
        return f'{self.nickname}, {self.surname}'
    class Meta:
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"




class Booking(models.Model):
    """Данные о бронировании"""
    surname= models.CharField("Фамилия", max_length=50)
    email=models.EmailField("Email")
    selected_tables = models.CharField('tables',max_length= 50)
    date = models.DateField("date", default=datetime.today().strftime('%Y-%m-%d'))
    class Meta:
        verbose_name="Бронирование"
        verbose_name_plural="Бронирования"
    def __str__(self):
        return f'{self.surname}, {self.selected_tables}'
