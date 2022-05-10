from django.db import models


#  Team player
class Player(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(null=True, max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    img_player = models.ImageField(upload_to='images/', default='images/default_img.png', verbose_name='Фото')
    player_number = models.CharField(max_length=2, default='00', verbose_name='Номер')
    role = models.ForeignKey('Role', null=True, on_delete=models.PROTECT, verbose_name='Амплуа')
    grip = models.ForeignKey('Grip', null=True, on_delete=models.PROTECT, verbose_name='Хват')

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name_plural = 'Игроки'
        verbose_name = 'Игрок'


#  Position on the field
class Role(models.Model):
    role = models.CharField(max_length=15, verbose_name='Амплуа')

    def __str__(self):
        return self.role

    class Meta:
        verbose_name_plural = 'Амплуа'
        verbose_name = 'Амплуа'


#  Stick grip
class Grip(models.Model):
    grip = models.CharField(max_length=10, verbose_name='Хват')

    def __str__(self):
        return self.grip

    class Meta:
        verbose_name_plural = 'Хват'
        verbose_name = 'Хват'


# #  Tournaments
# class Tournament(models.Model):
#     pass
#
#
# #  Team participation in the tournament
# class In_Tournament(models.Model):
#     pass
