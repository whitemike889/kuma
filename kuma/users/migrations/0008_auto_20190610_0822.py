# Generated by Django 1.11.21 on 2019-06-10 08:22


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190509_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='timezone',
            field=models.CharField(blank=True, default=b'US/Pacific', max_length=42, verbose_name='Timezone'),
        ),
    ]
