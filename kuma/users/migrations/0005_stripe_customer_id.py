# Generated by Django 1.11.16 on 2018-10-24 07:31


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_add_choices_to_timezone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
