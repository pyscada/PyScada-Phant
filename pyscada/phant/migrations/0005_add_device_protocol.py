# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyscada.phant import PROTOCOL_ID
from django.db import migrations


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    DeviceProtocol = apps.get_model("pyscada", "DeviceProtocol")
    db_alias = schema_editor.connection.alias
    DeviceProtocol.objects.using(db_alias).update_or_create(
        protocol="phant",
        defaults={
            "pk": PROTOCOL_ID,
            "description": "Phant Device",
            "app_name": "pyscada.phant",
            "device_class": "pyscada.phant.device",
            "daq_daemon": True,
            "single_thread": True,
        },
    )


def reverse_func(apps, schema_editor):
    # forwards_func() creates two Country instances,
    # so reverse_func() should delete them.
    DeviceProtocol = apps.get_model("pyscada", "DeviceProtocol")
    db_alias = schema_editor.connection.alias
    DeviceProtocol.objects.using(db_alias).filter(protocol="phant").delete()


class Migration(migrations.Migration):
    dependencies = [
        ("phant", "0004_extendedphantdevice_extendedphantvariable"),
        ("pyscada", "0041_update_protocol_id"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
