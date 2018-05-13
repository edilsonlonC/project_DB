# Generated by Django 2.0.4 on 2018-05-02 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instruments', '0002_instruments_id_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=25)),
                ('precio', models.FloatField()),
                ('Id_Material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='instruments.Material')),
            ],
        ),
    ]