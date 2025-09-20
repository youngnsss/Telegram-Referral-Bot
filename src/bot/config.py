import os

class Config(object):
    LOGGER = True

    # Use Railway’s provided DATABASE_URL environment variable
    DATABASE_URI = os.environ.get('DATABASE_URL')

    # Telegram channel ID for error logs
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1001410504549'))

    # List of Telegram user IDs (admins)
    SUDO_USERS = []
    sudo_env = os.environ.get('SUDO_USERS')
    if sudo_env:
        # Expecting a comma-separated list like "12345,67890"
        SUDO_USERS = [int(uid) for uid in sudo_env.split(',') if uid]

    # Your Bot token from @BotFather
    BOT_TOKEN = os.environ.get('BOT_TOKEN')

    # Number of worker processes
    WORKERS = int(os.environ.get('WORKERS', '8'))

    # Support channel username (without @)
    SUPPORT_CHANNEL = os.environ.get('SUPPORT_CHANNEL', '')
