# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardInDeck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.SmallIntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('hero', models.CharField(choices=[('druid', 'druid'), ('hunter', 'hunter'), ('mage', 'mage'), ('paladin', 'paladin'), ('priest', 'priest'), ('rogue', 'rogue'), ('shaman', 'shaman'), ('warlock', 'warlock'), ('warrior', 'warrior')], max_length=16)),
                ('cards', models.ManyToManyField(related_name='decks_in', through='deck.CardInDeck', to='card.Card')),
            ],
        ),
        migrations.AddField(
            model_name='cardindeck',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deck.Deck'),
        ),
    ]
