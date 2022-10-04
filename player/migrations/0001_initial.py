# Generated by Django 4.1.1 on 2022-09-19 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_year', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HighSchool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('high_school', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commited', models.CharField(max_length=100)),
                ('recruited_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', models.URLField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweets_count', models.IntegerField(null=True)),
                ('followers_count', models.IntegerField(null=True)),
                ('following_count', models.IntegerField(null=True)),
                ('last_tweet', models.CharField(max_length=500, null=True)),
                ('retweets_count', models.IntegerField(null=True)),
                ('profile_name', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.country')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField(max_length=100)),
                ('height', models.CharField(max_length=100, null=True)),
                ('weight', models.IntegerField(null=True)),
                ('city_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.city')),
                ('class_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.class')),
                ('commit_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.interest')),
                ('country_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.country')),
                ('offer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.offer')),
                ('position_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.position')),
                ('school_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.highschool')),
                ('twitter_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.twitter')),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='teams',
            field=models.ManyToManyField(blank=True, to='player.team'),
        ),
        migrations.AddField(
            model_name='interest',
            name='team_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.team'),
        ),
        migrations.AddField(
            model_name='city',
            name='state_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.state'),
        ),
    ]