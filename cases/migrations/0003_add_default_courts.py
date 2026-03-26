# Generated migration to add default courts in Nepal

from django.db import migrations


def add_default_courts(apps, schema_editor):
    Court = apps.get_model("cases", "Court")
    courts = [
        (1, "सर्वोच्च अदालत", "Supreme Court"),
        (2, "पाटन उच्च अदालत", "Patan High Court"),
        (3, "पोखरा उच्च अदालत", "Pokhara High Court"),
        (4, "वीरगञ्ज उच्च अदालत", "Birgunj High Court"),
        (5, "तुल्सीपुर उच्च अदालत", "Tulsipur High Court"),
        (6, "जनकपुर उच्च अदालत", "Janakpur High Court"),
        (7, "धनगढी उच्च अदालत", "Dhangadhi High Court"),
        (8, "भरतपुर उच्च अदालत", "Bharatpur High Court"),
        (9, "बुटवल उच्च अदालत", "Butwal High Court"),
        (10, "नेपालगञ्ज उच्च अदालत", "Nepalgunj High Court"),
        (11, "काठमाडौँ जिल्ला अदालत", "Kathmandu District Court"),
        (12, "ललितपुर जिल्ला अदालत", "Lalitpur District Court"),
        (13, "भक्तपुर जिल्ला अदालत", "Bhaktapur District Court"),
        (14, "अन्य अदालत", "Other Court"),
    ]
    for order, name, name_en in courts:
        Court.objects.get_or_create(
            name=name,
            defaults={"name_en": name_en, "order": order},
        )


def remove_default_courts(apps, schema_editor):
    Court = apps.get_model("cases", "Court")
    Court.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("cases", "0002_add_court_and_documents"),
    ]

    operations = [
        migrations.RunPython(add_default_courts, remove_default_courts),
    ]
