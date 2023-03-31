# Copyright (c) 2022 Itz-fork

import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 2448614))
    API_HASH = os.environ.get("API_HASH", "c1c1a85c23643876d4ae5c76b20e821f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5911585169:AAEoVnmJ3W1_rpZgalbbAj_Qu8rDHoJgwaU")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5010755990").split())
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT") in ["False", "false"]
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-1001936951452")) if os.environ.get("LOGS_CHANNEL", "-1001936951452") else None
    # DON'T CHANGE THESE 2 VARS
    DOWNLOAD_LOCATION = "./NexaBots"
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "denebi6238@djpich.com")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "stark2023")
