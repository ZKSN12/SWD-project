# Generated by Django 4.1.3 on 2022-11-21 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("petsitterapp", "0012_comment"),
    ]

    operations = [
        migrations.RemoveField(model_name="comment", name="sitter",),
        migrations.AddField(
            model_name="comment",
            name="sitterProfile",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="petsitterapp.sitterprofile",
            ),
        ),
    ]
