from django.db import models


# Пользователи
class user(models.Model):
    user_id = models.CharField("Telegram ID пользователя",max_length = 130)
    username = models.CharField("Telegram username пользователя",max_length = 130)


class Categorys(models.Model):
    name = models.CharField("Имя категории",max_length = 130)
    answere = models.TextField("Ответ при выборе категории",blank = True)


    def __str__(self):
        return self.name


# База знаний
class questions(models.Model):
    SERIVICE_CHOICES=(
    ('Тарифы','Тарифы'),
    ('Интернет','Интернет'),
    ('Мобильная связь','Мобильная связь'),
    ('Телевидение','Телевидение'),
    ('Телефон','Телефон'),
    )
    service = models.CharField("Услуга", max_length = 130,choices=SERIVICE_CHOICES)
    category = models.ForeignKey(Categorys,
                                 related_name='Категория',
                                 on_delete=models.CASCADE) # Категория
    subcategory = models.CharField("Подкатегория",max_length = 130 , blank = True)
    answere = models.TextField("Ответ")
    tags = models.TextField("Тэги\n    (Указываются через ':')")

# Вспомогательная таблица
class auxiliary_table(models.Model):
    user_id = models.CharField(max_length = 130)
    service = models.CharField(max_length = 130, blank = True)
    category = models.CharField(max_length = 130, blank = True)
    subcategory = models.CharField(max_length = 130, blank = True)
