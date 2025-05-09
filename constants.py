"""
This module contains all the general application settings.
"""

# Import necessary modules from the modules module
from modules import secrets, socket

# Name of the Flask application
APP_NAME = "flaskBlog"  # (str)

# Version of the Flask application
APP_VERSION = "3.0.0-dev"  # (str)

# Path to the root of the application files
APP_ROOT_PATH = "."  # (str)

# Hostname or IP address for the Flask application
APP_HOST = "0.0.0.0"  

# Port number for the Flask application
APP_PORT = 5000  # (int)

# Toggle debug mode for the Flask application
DEBUG_MODE = False  # (bool)

# Name of the UI framework being used
UI_NAME = "tailwindUI"  # (str)

# Path to the templates folder
TEMPLATE_FOLDER = f"templates/{UI_NAME}"  # (str)

# Path to the static folder
STATIC_FOLDER = f"static/{UI_NAME}"  # (str)

# Toggle user login feature
LOG_IN = True  # (bool)

# Toggle user registration feature
REGISTRATION = True  # (bool)

# Supported languages for the application
LANGUAGES = ["en", "tr", "es", "de", "zh", "fr", "uk", "ru", "pt", "ja", "pl"]  # (list)

# Enable or Disable analytics feature for posts
ANALYTICS = True  # (bool)

### LOGGER SETTINGS ###
# Toggle custom logging feature
CUSTOM_LOGGER = True  # (bool)

# Toggle werkzeug logging feature
WERKZEUG_LOGGER = False  # (bool)

# Toggle logging to file feature
LOG_TO_FILE = True  # (bool)

# Root path of the log folder
LOG_FOLDER_ROOT = "log/"  # (str)

# Root path of the log file
LOG_FILE_ROOT = LOG_FOLDER_ROOT + "log.log"  # (str)


# Secret key for Flask sessions
APP_SECRET_KEY = secrets.token_urlsafe(32)  # (str)

# Toggle permanent sessions for the Flask application
SESSION_PERMANENT = True  # (bool)

# Separator text used in log files
BREAKER_TEXT = "\n"  # (str)


### DATABASE SETTINGS ###

# Root path of the database folder
DB_FOLDER_ROOT = "db/"  # (str)

# Root path of the users database
DB_USERS_ROOT = DB_FOLDER_ROOT + "users.db"  # (str)

# Root path of the posts database
DB_POSTS_ROOT = DB_FOLDER_ROOT + "posts.db"  # (str)

# Root path of the comments database
DB_COMMENTS_ROOT = DB_FOLDER_ROOT + "comments.db"  # (str)

# Root path of the analytics database
DB_ANALYTICS_ROOT = DB_FOLDER_ROOT + "analytics.db"  # (str)


### SMTP MAIL SETTINGS ###

# SMTP server address
SMTP_SERVER = "email-smtp.ap-northeast-2.amazonaws.com"  # (str)

# SMTP server port
SMTP_PORT = 587  # (int)

SMTP_MAIL = "noreply@cloudmailsvc.com"          # 발신자 이메일 (도메인 인증된 주소)
SMTP_USER = "AKIA3B5SO64XN3XCUAAW"   
SMTP_PASSWORD = "BK03Tir2pEa4Qa1uHhOmCmjYAxhM9xGdTdJJbrQCiYPP" # SES SMTP 비밀번호


### slack webhook ###
SLACK_WEBHOOK_URL ="https://hooks.slack.com/services/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"

# Toggle creation of default admin account
DEFAULT_ADMIN = False  # (bool)

# Default admin username
DEFAULT_ADMIN_USERNAME = "admin"  # (str)

# Default admin email address
DEFAULT_ADMIN_EMAIL = "admin@flaskblog.com"  # (str)

# Default admin password
DEFAULT_ADMIN_PASSWORD = "admin"  # (str)

# Default starting point score for admin
DEFAULT_ADMIN_POINT = 0  # (int)

# Default admin profile picture URL
DEFAULT_ADMIN_PROFILE_PICTURE = f"https://api.dicebear.com/7.x/identicon/svg?seed={DEFAULT_ADMIN_USERNAME}&radius=10"  # (str)


### RECAPTCHA SETTINGS ###

# Toggle reCAPTCHA verification
RECAPTCHA = False  # (bool)

# Toggle display of reCAPTCHA badge
RECAPTCHA_BADGE = False  # (bool)

# reCAPTCHA site key
RECAPTCHA_SITE_KEY = ""  # (str)

# reCAPTCHA secret key
RECAPTCHA_SECRET_KEY = ""  # (str)

# reCAPTCHA verify URL
RECAPTCHA_VERIFY_URL = "https://www.google.com/recaptcha/api/siteverify"  # (str)

# Toggle reCAPTCHA verification for different actions
RECAPTCHA_LOGIN = True  # (bool)
RECAPTCHA_SIGN_UP = True  # (bool)
RECAPTCHA_POST_CREATE = True  # (bool)
RECAPTCHA_POST_EDIT = True  # (bool)
RECAPTCHA_POST_DELETE = True  # (bool)
RECAPTCHA_COMMENT = True  # (bool)
RECAPTCHA_COMMENT_DELETE = True  # (bool)
RECAPTCHA_PASSWORD_RESET = True  # (bool)
RECAPTCHA_PASSWORD_CHANGE = True  # (bool)
RECAPTCHA_USERNAME_CHANGE = True  # (bool)
RECAPTCHA_VERIFY_USER = True  # (bool)
RECAPTCHA_DELETE_USER = True  # (bool)
RECAPTCHA_PROFILE_PICTURE_CHANGE = True  # (bool)
