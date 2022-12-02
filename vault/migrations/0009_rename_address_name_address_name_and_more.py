# Generated by Django 4.0.6 on 2022-07-26 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vault', '0008_alter_address_address2_alter_paymentcard_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='bankaccount',
            old_name='bank_account_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='note',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='note_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='password',
            old_name='password_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='paymentcard',
            old_name='payment_card_name',
            new_name='name',
        ),
    ]