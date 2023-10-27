# Generated by Django 4.2.5 on 2023-10-23 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastrar', '0002_curso_disciplina_turma'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalheCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoCurso', models.CharField(max_length=100)),
                ('CodigoTurma', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DetalheDisciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoCurso', models.CharField(max_length=100)),
                ('CodigoDisciplina', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DetalheTurma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoAluno', models.CharField(max_length=100)),
                ('CodigoProfessor', models.CharField(max_length=100)),
                ('CodigoTurma', models.CharField(max_length=100)),
            ],
        ),
    ]
