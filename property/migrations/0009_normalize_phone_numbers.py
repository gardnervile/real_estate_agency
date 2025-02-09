from django.db import migrations
import phonenumbers


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.iterator():
        if flat.owners_phonenumber:
            try:
                parsed_number = phonenumbers.parse(flat.owners_phonenumber, "RU")
                if phonenumbers.is_valid_number(parsed_number):
                    flat.owner_pure_phone = phonenumbers.format_number(
                        parsed_number, phonenumbers.PhoneNumberFormat.E164
                    )
                    flat.save(update_fields=['owner_pure_phone'])
            except phonenumbers.NumberParseException:
                pass 


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20250206_2212'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers),
    ]
