# Generated by Django 3.2.2 on 2021-05-25 08:51

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('office_zone', models.CharField(max_length=100)),
                ('office_location', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Residence_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('residence_zone', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('lead_gen', models.DateTimeField(auto_now_add=True)),
                ('lead_status', models.CharField(choices=[('N', 'New'), ('C', 'Cold'), ('W', 'Warm'), ('H', 'Hot'), ('I', 'Hot Ice')], max_length=1)),
                ('campaign', models.CharField(blank=True, max_length=30, null=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('mail', models.EmailField(max_length=254)),
                ('property_type', models.CharField(choices=[('AP', 'Apartment'), ('BF', 'Builder Floor'), ('BT', 'Both')], max_length=2)),
                ('bedrooms', models.CharField(choices=[('2', '2 BHK'), ('2+st', '2 BHK + Study'), ('2+sr', '2 BHK + Servant'), ('3', '3 BHK'), ('3+st', '3 BHK + Study'), ('3+sr', '3 BHK + Servant'), ('4', '4 BHK'), ('4+sr', '4 BHK + Servant')], max_length=4)),
                ('budget_category', models.CharField(choices=[('50-70', '50 L to 70 L '), ('70-90', '70 L to 90 L '), ('90-120', '90 L to 1.20 Cr '), ('120-140', '1.20 Cr to 1.40 Cr'), ('140-160', '1.40 Cr to 1.60 Cr'), ('160-180', '1.60 Cr to 1.80 Cr'), ('180-200', '1.80 Cr to 2.00 Cr'), ('200-250', '2.00 Cr to 2.50 Cr'), ('250-300', '2.50 Cr to 3.00 Cr'), ('300-350', '3.00 Cr to 3.50 Cr'), ('350+', '3,50 Cr +')], max_length=7)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=5)),
                ('project_status', models.CharField(choices=[('R', 'Ready To Move'), ('U', 'Under Construction'), ('A', 'Any')], max_length=1)),
                ('purpose', models.CharField(choices=[('INV', 'Investment'), ('END', 'End Use')], default='END', max_length=3)),
                ('preferred_location', models.CharField(blank=True, max_length=30, null=True)),
                ('remarks', models.TextField(blank=True, max_length=254, null=True)),
                ('notes', models.TextField(blank=True, max_length=254, null=True)),
                ('inventory_shared', models.BooleanField(blank=True, default=False, null=True)),
                ('next_call_date', models.DateTimeField()),
                ('occupation', models.CharField(blank=True, max_length=30, null=True)),
                ('office_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dash.office_address')),
                ('residence_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dash.residence_address')),
            ],
        ),
    ]
