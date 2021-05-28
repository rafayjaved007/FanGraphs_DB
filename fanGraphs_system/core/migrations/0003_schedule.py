# Generated by Django 3.2.3 on 2021-05-25 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_team_league'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('opp', models.CharField(max_length=50)),
                ('tor_win_prob', models.CharField(max_length=50)),
                ('w_or_l', models.CharField(blank=True, choices=[('W', 'W'), ('L', 'L')], max_length=10)),
                ('tor_runs', models.IntegerField(max_length=50)),
                ('opp_runs', models.IntegerField(max_length=50)),
                ('tor_starter', models.CharField(max_length=100)),
                ('opp_starter', models.CharField(max_length=100)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.team')),
            ],
        ),
    ]