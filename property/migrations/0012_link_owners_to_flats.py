# Generated by Django 2.2.24 on 2025-02-07 17:22

from django.db import migrations

def link_owners_to_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        owner, _ = Owner.objects.get_or_create(
            owner=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone
        )
        owner.flats.add(flat)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0011_auto_20250207_2015'),
    ]

    operations = [
        migrations.RunPython(link_owners_to_flats),
    ]
