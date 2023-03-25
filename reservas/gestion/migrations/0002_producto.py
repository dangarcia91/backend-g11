# Generated by Django 4.1.7 on 2023-03-25 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('precio', models.FloatField()),
                ('disponible', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, db_column='created_at')),
                ('updateAt', models.DateTimeField(auto_now=True, db_column='updated_at')),
                ('categoria', models.ForeignKey(db_column='categoria_id', on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='gestion.categoria')),
            ],
            options={
                'db_table': 'productos',
                'ordering': ['-nombre', 'precio'],
                'unique_together': {('nombre', 'precio')},
            },
        ),
    ]
