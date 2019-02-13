# Generated by Django 2.1.5 on 2019-02-06 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0003_auto_20190206_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='bits',
            field=models.IntegerField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='block_index',
            field=models.IntegerField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='fee',
            field=models.IntegerField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='hash',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='height',
            field=models.IntegerField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='merkle_root',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='n_tx',
            field=models.IntegerField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='nonce',
            field=models.IntegerField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='previous_block',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='received_time',
            field=models.IntegerField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='size',
            field=models.IntegerField(auto_created=True, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='time',
            field=models.IntegerField(auto_created=True, blank=True, null=True),
        ),
    ]