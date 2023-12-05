# Generated by Django 4.1.12 on 2023-12-05 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stanowisko',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=255, verbose_name='Nazwa')),
                ('opis', models.TextField(blank=True, null=True, verbose_name='Opis')),
            ],
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=255, verbose_name='Imię')),
                ('nazwisko', models.CharField(max_length=255, verbose_name='Nazwisko')),
                ('plec', models.CharField(choices=[('kobieta', 'Kobieta'), ('mezczyzna', 'Mężczyzna'), ('inne', 'Inne')], max_length=10, verbose_name='Płeć')),
                ('data_dodania', models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')),
                ('stanowisko', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.stanowisko', verbose_name='Stanowisko')),
            ],
        ),
    ]
