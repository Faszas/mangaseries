# Generated by Django 3.0.5 on 2020-04-03 05:17

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0002_auto_20200403_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prison_school',
            fields=[
                ('mymanga_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manga.myManga')),
            ],
            bases=('manga.mymanga',),
        ),
        migrations.AlterField(
            model_name='mymanga',
            name='Uploaded_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 3, 5, 17, 51, 531973, tzinfo=utc)),
        ),
    ]