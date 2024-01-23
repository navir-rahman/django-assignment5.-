# Generated by Django 4.2.7 on 2024-01-23 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Books', '0001_initial'),
        ('UserAccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('DEPOSIT', 'Deposit'), ('WITHDRAWAL', 'Withdrawal'), ('BORROW', 'Borrow Book'), ('RETURN', 'Return Book')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Books.book')),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserAccount.useraccount')),
            ],
        ),
    ]
