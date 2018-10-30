# Generated by Django 2.0.4 on 2018-10-28 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockedUserId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blockee', to='study.User')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocker', to='study.User')),
            ],
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='StudyGroup_Filter',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('filterId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.Filter')),
            ],
        ),
        migrations.CreateModel(
            name='StudyGroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SystemLog',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('service', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=2000)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.User')),
            ],
        ),
        migrations.AddField(
            model_name='studygroup',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='studygroup',
            name='cNNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='studygroup',
            name='instructor',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='studygroup',
            name='semester',
            field=models.CharField(max_length=10),
        ),
        migrations.AddField(
            model_name='studygroupuser',
            name='studyGroupId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.StudyGroup'),
        ),
        migrations.AddField(
            model_name='studygroupuser',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.User'),
        ),
        migrations.AddField(
            model_name='studygroup_filter',
            name='studyGroupId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.StudyGroup'),
        ),
    ]