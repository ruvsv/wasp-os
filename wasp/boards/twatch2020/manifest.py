# SPDX-License-Identifier: LGPL-3.0-or-later
# Copyright (C) 2020 Daniel Thompson

freeze('.', 'watch.py', opt=3)
freeze('../..',
    (
        'apps/clock.py',
        'apps/flashlight.py',
        'apps/heart.py',
        'apps/launcher.py',
        'apps/pager.py',
        'apps/settings.py',
        'apps/steps.py',
        'apps/stopwatch.py',
        'apps/testapp.py',
        'boot.py',
        'draw565.py',
        'drivers/bma421.py',
        'drivers/st7789.py',
        'drivers/axp202c.py',
        'drivers/focaltouch.py',
        'drivers/pcf8563.py',
        'adapters/touch.py',
        'adapters/wifi.py',
        'adapters/backlight.py',
        'adapters/app.py',
        'adapters/battery.py',
        'adapters/power_management_service.py',
        'adapters/rtc.py',
        'adapters/vibrator.py',
        'fonts/__init__.py',
        'fonts/clock.py',
        'fonts/sans24.py',
        'fonts/sans28.py',
        'fonts/sans36.py',
        'gadgetbridge.py',
        'icons.py',
        'ppg.py',
        'shell.py',
        'wasp.py',
        'widgets.py',
    ),
    opt=3
)
