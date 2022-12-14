# Generated by Django 3.2 on 2022-08-08 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelInheritance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ISBN',
            fields=[
                ('books_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='modelInheritance.books')),
                ('ISBN', models.TextField()),
            ],
            bases=('modelInheritance.books',),
        ),
    ]
