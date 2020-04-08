# Generated by Django 3.0.5 on 2020-04-03 04:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demon_Slayer',
            fields=[
                ('mymanga_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manga.myManga')),
            ],
            bases=('manga.mymanga',),
        ),
        migrations.CreateModel(
            name='Konosuba',
            fields=[
                ('mymanga_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manga.myManga')),
            ],
            bases=('manga.mymanga',),
        ),
        migrations.CreateModel(
            name='Nanatsu',
            fields=[
                ('mymanga_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manga.myManga')),
            ],
            bases=('manga.mymanga',),
        ),
        migrations.CreateModel(
            name='Onepunchman',
            fields=[
                ('mymanga_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manga.myManga')),
            ],
            bases=('manga.mymanga',),
        ),
        migrations.CreateModel(
            name='Overlord',
            fields=[
                ('mymanga_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='manga.myManga')),
            ],
            bases=('manga.mymanga',),
        ),
        migrations.AlterField(
            model_name='mymanga',
            name='Uploaded_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 3, 4, 18, 12, 557070, tzinfo=utc)),
        ),
    ]