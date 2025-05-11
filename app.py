"""
This file contains the main function
"""

from modules import (
    Log,  # Importing the Log class for logging
    currentTimeStamp,  # Importing the currentTimeStamp function for getting the current timestamp
    terminalASCII,  # Importing the terminalASCII function for displaying ASCII art in the terminal
    timedelta,  # Importing the timedelta class for working with time differences
)

# Get the start time of the app
startTime = currentTimeStamp()

# Print a line breaker and a ASCII art
print(terminalASCII())

# Print a line breaker and a message that the app is starting
Log.info("Starting...")

# Importing necessary modules and classes
from flask_wtf.csrf import (
    CSRFError,
    CSRFProtect,
)  # Importing CSRF protection for Flask forms

# Importing various configuration variables from the modules
# Importing reCAPTCHA configurations
# Import the contextProcessor module that contains custom functions for the app
from modules import (
    APP_HOST,  # Importing the application host configuration
    APP_NAME,  # Importing the application name configuration
    APP_PORT,  # Importing the application port configuration
    APP_ROOT_PATH,  # Importing the application root path configuration
    APP_SECRET_KEY,  # Importing the application secret key configuration
    APP_VERSION,  # Importing the application version configuration
    CUSTOM_LOGGER,  # Importing the custom logger configuration
    DEBUG_MODE,  # Importing the debug mode configuration
    DEFAULT_ADMIN,  # Importing the default admin configuration
    DEFAULT_ADMIN_EMAIL,  # Importing the default admin email configuration
    DEFAULT_ADMIN_PASSWORD,  # Importing the default admin password configuration
    DEFAULT_ADMIN_POINT,  # Importing the default admin point configuration
    DEFAULT_ADMIN_PROFILE_PICTURE,  # Importing the default admin profile picture configuration
    DEFAULT_ADMIN_USERNAME,  # Importing the default admin username configuration
    LOG_FILE_ROOT,  # Importing the log file root configuration
    LOG_FOLDER_ROOT,  # Importing the log folder root configuration
    LOG_IN,  # Importing the log-in configuration
    RECAPTCHA,  # Flag for enabling/disabling reCAPTCHA
    RECAPTCHA_BADGE,  # Flag for enabling/disabling reCAPTCHA for badge configuration
    RECAPTCHA_COMMENT,  # Flag for enabling/disabling reCAPTCHA for comment
    RECAPTCHA_COMMENT_DELETE,  # Flag for enabling/disabling reCAPTCHA for comment delete
    RECAPTCHA_DELETE_USER,  # Flag for enabling/disabling reCAPTCHA for delete user
    RECAPTCHA_LOGIN,  # Flag for enabling/disabling reCAPTCHA for login
    RECAPTCHA_PASSWORD_CHANGE,  # Flag for enabling/disabling reCAPTCHA for password change
    RECAPTCHA_PASSWORD_RESET,  # Flag for enabling/disabling reCAPTCHA for password reset
    RECAPTCHA_POST_CREATE,  # Flag for enabling/disabling reCAPTCHA for post create
    RECAPTCHA_POST_DELETE,  # Flag for enabling/disabling reCAPTCHA for post delete
    RECAPTCHA_POST_EDIT,  # Flag for enabling/disabling reCAPTCHA for post edit
    RECAPTCHA_PROFILE_PICTURE_CHANGE,  # Flag for enabling/disabling reCAPTCHA for profile picture change
    RECAPTCHA_SECRET_KEY,  # Flag for enabling/disabling reCAPTCHA for secret key
    RECAPTCHA_SIGN_UP,  # Flag for enabling/disabling reCAPTCHA for sign-up
    RECAPTCHA_SITE_KEY,  # Flag for enabling/disabling reCAPTCHA for site key
    RECAPTCHA_USERNAME_CHANGE,  # Flag for enabling/disabling reCAPTCHA for username change
    RECAPTCHA_VERIFY_URL,  # Flag for enabling/disabling reCAPTCHA for verify URL
    RECAPTCHA_VERIFY_USER,  # Flag for enabling/disabling reCAPTCHA for verify user
    REGISTRATION,  # Importing the registration configuration
    SESSION_PERMANENT,  # Importing the session permanence configuration
    SMTP_MAIL,  # Importing the SMTP mail configuration
    SMTP_PASSWORD,  # Importing the SMTP password configuration
    SMTP_PORT,  # Importing the SMTP port configuration
    SMTP_SERVER,  # Importing the SMTP server configuration
    STATIC_FOLDER,  # Importing the static folder configuration
    TEMPLATE_FOLDER,  # Importing the template folder configuration
    UI_NAME,  # Importing the UI name configuration
    WERKZEUG_LOGGER,  # Importing the werkzeug logger configuration
    Flask,
    browserLanguage,  # A function that sets the app language based on the browser's preferred language
    injectTranslations,  # A function that injects translations into the context of the application
    isLogin,  # A function that checks LOG_IN constant
    isRegistration,  # A function that checks REGISTRATION constant
    recaptchaBadge,  # A function that checks RECAPTCHA_BADGE constant
    returnPostUrlID,  # A function that returns the post's URL id
    returnUserProfilePicture,  # A function that returns the user's profile picture
    returnPostUrlSlug,  # A function that returns the post's URL slug
)  # Importing Flask class for creating the Flask application instance
from routes.about import (
    aboutBlueprint,
)  # Importing the blueprint for about route
from routes.accountSettings import (
    accountSettingsBlueprint,
)  # Importing the blueprint for account settings route
from routes.adminPanel import (
    adminPanelBlueprint,
)  # Importing the blueprint for admin panel route
from routes.adminPanelComments import (
    adminPanelCommentsBlueprint,
)  # Importing the blueprint for admin panel comments route
from routes.adminPanelPosts import (
    adminPanelPostsBlueprint,
)  # Importing the blueprint for admin panel posts route
from routes.adminPanelUsers import (
    adminPanelUsersBlueprint,
)  # Importing the blueprint for admin panel users route
from routes.category import (
    categoryBlueprint,
)  # Importing the blueprint for category route
from routes.changeLanguage import (
    changeLanguageBlueprint,
)  # Importing the blueprint for changing language route
from routes.changePassword import (
    changePasswordBlueprint,
)  # Importing the blueprint for changing password route
from routes.changeProfilePicture import (
    changeProfilePictureBlueprint,
)  # Importing the blueprint for changing profile picture route
from routes.changeUserName import (
    changeUserNameBlueprint,
)  # Importing the blueprint for changing username route
from routes.createPost import (
    createPostBlueprint,
)  # Importing the blueprint for creating post route
from routes.dashboard import (
    dashboardBlueprint,
)  # Importing the blueprint for dashboard route
from routes.editPost import (
    editPostBlueprint,
)  # Importing the blueprint for post editing route
from routes.index import (
    indexBlueprint,
)  # Importing the blueprint for index route
from routes.login import (
    loginBlueprint,
)  # Importing the blueprint for login route
from routes.logout import (
    logoutBlueprint,
)  # Importing the blueprint for logout route
from routes.passwordReset import (
    passwordResetBlueprint,
)  # Importing the blueprint for password reset route

# Importing blueprints for different routes
from routes.post import postBlueprint  # Importing the blueprint for post route
from routes.postsAnalytics import (
    analyticsBlueprint,
)  # Importing the blueprint for analytics page route
from routes.privacyPolicy import (
    privacyPolicyBlueprint,
)  # Importing the blueprint for privacy policy route
from routes.returnPostAnalyticsData import (
    returnPostAnalyticsDataBlueprint,
)  # Importing the blueprint for postAnalyticsData endpoint route
from routes.returnPostBanner import (
    returnPostBannerBlueprint,
)  # Importing the blueprint for returning post banners
from routes.search import (
    searchBlueprint,
)  # Importing the blueprint for search route
from routes.searchBar import (
    searchBarBlueprint,
)  # Importing the blueprint for search bar route
from routes.setLanguage import (
    setLanguageBlueprint,
)  # Importing the blueprint for setting language route
from routes.signup import (
    signUpBlueprint,
)  # Importing the blueprint for signup route
from routes.user import userBlueprint  # Importing the blueprint for user route
from routes.verifyUser import (
    verifyUserBlueprint,
)  # Importing the blueprint for user verification route
from utils.afterRequest import (
    afterRequestLogger,
)  # This function handles loggins of every request

# Importing database related utilities
from utils.dbChecker import (
    analyticsTable,
    commentsTable,
    dbFolder,
    postsTable,
    usersTable,
)
from utils.errorHandlers.csrfErrorHandler import (
    csrfErrorHandler,
)  # This function handles CSRF errors
from utils.errorHandlers.notFoundErrorHandler import (
    notFoundErrorHandler,
)  # This function handles 404 errors
from utils.errorHandlers.unauthorizedErrorHandler import (
    unauthorizedErrorHandler,
)  # This function handles unauthorized access errors
from utils.generateUrlIdFromPost import getSlugFromPostTitle

# Create a Flask app object with the app name, root path, static folder and template folder
app = Flask(
    import_name=APP_NAME,  # The name of the app
    root_path=APP_ROOT_PATH,  # The root path of the app
    static_folder=STATIC_FOLDER,  # The folder where the static files(*.js/*.css) are stored
    template_folder=TEMPLATE_FOLDER,  # The folder where the Jinja(*.html.jinja) templates are stored
)




# Enable autoescape for all rendered jinja pages irrespective of file extension.
app.jinja_options["autoescape"] = True

# Set the secret key and the session permanent flag for the app
app.secret_key = APP_SECRET_KEY  # The secret key for the app
app.config["SESSION_PERMANENT"] = (
    SESSION_PERMANENT  # A flag that determines if the session is permanent or not
)

# Create a CSRFProtect object for the app
csrf = CSRFProtect(app)  # A CSRF protection mechanism for the app

# Register the custom functions from the contextProcessor module as context processors for the app
# Context processors are functions that run before rendering a template and add variables to the template context
app.context_processor(
    isLogin
)  # A context processor that adds the isLogin variable to the template context
app.context_processor(
    recaptchaBadge
)  # A context processor that adds the recaptchaBadge variable to the template context
app.context_processor(
    isRegistration
)  # A context processor that adds the isRegistration variable to the template context
app.context_processor(
    returnUserProfilePicture
)  # A context processor that adds the getProfilePicture variable to the template context
app.context_processor(
    returnPostUrlID
)  # A context processor that adds the getPostUrlIdFromPost variable to template context
app.context_processor(
    returnPostUrlSlug
)  # A context processor that adds the A function that returns the post's urlSlug variable to template context
app.context_processor(
    injectTranslations
)  # A context processor that adds the translations variable to the template context
app.before_request(
    browserLanguage
)  # A function that sets the app language based on the browser's preferred language

# Match WERKZEUG_LOGGER status
match WERKZEUG_LOGGER:
    # If Werkzeug default logger is enabled
    case True:
        # Log that Werkzeug default logger is enabled
        Log.warning("Werkzeug default logger is enabled")
    # If Werkzeug default logger is disabled
    case False:
        # Import getLogger from logging module
        from logging import getLogger

        # Log that Werkzeug default logger is disabled
        Log.info("Werkzeug default logger is disabled")
        # Disable the Werkzeug default logger
        getLogger("werkzeug").disabled = True

# Match CUSTOM_LOGGER status
match CUSTOM_LOGGER:
    # If Custom logger is enabled
    case True:
        # Log that Custom logger is enabled
        Log.info("Custom logger is enabled")
    # If Custom logger is disabled
    case False:
        # Log that Custom logger is disabled
        Log.info("Custom logger is disabled")


# Log app settings
Log.info(f"Debug mode: {DEBUG_MODE}")
Log.info(f"Name: {APP_NAME}")
Log.info(f"Version: {APP_VERSION}")
Log.info(f"Host: {APP_HOST}")
Log.info(f"Port: {APP_PORT}")
Log.info(f"Secret key: {APP_SECRET_KEY}")
Log.info(f"Session permanent: {SESSION_PERMANENT}")
Log.info(f"Root path: {APP_ROOT_PATH}")
Log.info(f"Log folder root: {LOG_FOLDER_ROOT}")
Log.info(f"Log file root: {LOG_FILE_ROOT}")
Log.info(f"Log in: {LOG_IN}")
Log.info(f"Registration: {REGISTRATION}")
# Log the UI name, template folder and the static folder
Log.info(f"UI: {UI_NAME}")
Log.info(f"Template folder: {TEMPLATE_FOLDER}")
Log.info(f"Static folder: {STATIC_FOLDER}")
# Log the SMTP server settings
Log.info(f"SMTP server: {SMTP_SERVER}")
Log.info(f"SMTP port: {SMTP_PORT}")
Log.info(f"SMTP mail: {SMTP_MAIL}")
Log.info(f"SMTP password: {SMTP_PASSWORD}")

# Check if recaptcha is enabled
match RECAPTCHA:
    case True:
        # Check if the recaptcha site key and secret key are valid
        match RECAPTCHA_SITE_KEY == "" or RECAPTCHA_SECRET_KEY == "":
            case True:
                # Log a warning message that the recaptcha keys are invalid and may cause the app to crash
                Log.error(
                    "reCAPTCHA keys is unvalid this may cause the application to crash",
                )
                Log.error(
                    "Please check your recaptcha keys or set recaptcha to false from true in 'constants.py'",
                )
            case False:
                # Log a success message that recaptcha is on and print the recaptcha keys, url and badge status
                Log.info("reCAPTCHA is on")
                Log.info(f"reCAPTCHA recaptcha site key: {RECAPTCHA_SITE_KEY}")
                Log.info(f"reCAPTCHA secret key: {RECAPTCHA_SECRET_KEY}")
                Log.info(f"reCAPTCHA verify url: {RECAPTCHA_VERIFY_URL}")
                Log.info(f"reCAPTCHA badge: {RECAPTCHA_BADGE}")
                # Log the recaptcha settings for different actions
                Log.info(f"reCAPTCHA login: {RECAPTCHA_LOGIN}")
                Log.info(f"reCAPTCHA sign up: {RECAPTCHA_SIGN_UP}")
                Log.info(f"reCAPTCHA post create: {RECAPTCHA_POST_CREATE}")
                Log.info(f"reCAPTCHA post edit: {RECAPTCHA_POST_EDIT}")
                Log.info(f"reCAPTCHA post delete: {RECAPTCHA_POST_DELETE}")
                Log.info(f"reCAPTCHA comment: {RECAPTCHA_COMMENT}")
                Log.info(f"reCAPTCHA comment delete: {RECAPTCHA_COMMENT_DELETE}")
                Log.info(f"reCAPTCHA password reset: {RECAPTCHA_PASSWORD_RESET}")
                Log.info(f"reCAPTCHA password change: {RECAPTCHA_PASSWORD_CHANGE}")
                Log.info(f"reCAPTCHA username change: {RECAPTCHA_USERNAME_CHANGE}")
                Log.info(f"reCAPTCHA verify user: {RECAPTCHA_VERIFY_USER}")
                Log.info(f"reCAPTCHA delete user: {RECAPTCHA_DELETE_USER}")
                Log.info(
                    f"reCAPTCHA user profile picture change: {RECAPTCHA_PROFILE_PICTURE_CHANGE}",
                )
                Log.info(
                    f"reCAPTCHA profile picture change: {RECAPTCHA_PROFILE_PICTURE_CHANGE}",
                )
    case False:
        # Log a warning message that recaptcha is off
        Log.info("reCAPTCHA is off")

# Check if default admin is enabled
match DEFAULT_ADMIN:
    case True:
        # Log a success message that admin is on and print the default admin settings
        Log.info("Default admin is on")
        Log.info(f"Default admin username: {DEFAULT_ADMIN_USERNAME}")
        Log.info(f"Default admin email: {DEFAULT_ADMIN_EMAIL}")
        Log.info(f"Default admin password: {DEFAULT_ADMIN_PASSWORD}")
        Log.info(f"Default admin point: {DEFAULT_ADMIN_POINT}")
        Log.info(f"Default admin profile picture: {DEFAULT_ADMIN_PROFILE_PICTURE}")
    case False:
        # Log a danger message that admin is off
        Log.info("Default admin is off")

# Call the dbFolder, usersTable, postsTable , commentsTable and analyticsTable functions to check the database status
dbFolder()
usersTable()
postsTable()
commentsTable()
analyticsTable()


# Use the app.errorhandler decorator to register error handler functions for app
@app.errorhandler(404)
def notFound(e):
    # Call the notFoundErrorHandler function and return its result
    return notFoundErrorHandler(e)


# Use the app.errorhandler decorator to register error handler functions for app
@app.errorhandler(401)
def unauthorized(e):
    # Call the unauthorizedErrorHandler function and return its result
    return unauthorizedErrorHandler(e)


# Use the app.errorhandler decorator to register error handler functions for app
@app.errorhandler(CSRFError)
def csrfError(e):
    # Call the csrfErrorHandler function and return its result
    return csrfErrorHandler(e)


# Use the app.after_request decorator to handle every request
@app.after_request
def afterRequest(response):
    # Call the afterRequestLogger function and return its result
    return afterRequestLogger(response)

@app.context_processor
def inject_custom_functions():
    return dict(getSlugFromPostTitle=getSlugFromPostTitle)
# Registering blueprints for different routes with the Flask application instance
app.register_blueprint(
    postBlueprint
)  # Registering the blueprint for handling post routes
app.register_blueprint(
    userBlueprint
)  # Registering the blueprint for handling user routes
app.register_blueprint(indexBlueprint)  # Registering the blueprint for the index route
app.register_blueprint(aboutBlueprint)  # Registering the blueprint for the about route
app.register_blueprint(loginBlueprint)  # Registering the blueprint for the login route
app.register_blueprint(
    signUpBlueprint
)  # Registering the blueprint for the sign-up route
app.register_blueprint(
    logoutBlueprint
)  # Registering the blueprint for the logout route
app.register_blueprint(
    searchBlueprint
)  # Registering the blueprint for the search route
app.register_blueprint(
    categoryBlueprint
)  # Registering the blueprint for the category route
app.register_blueprint(
    editPostBlueprint
)  # Registering the blueprint for the edit post route
app.register_blueprint(
    dashboardBlueprint
)  # Registering the blueprint for the dashboard route
app.register_blueprint(
    searchBarBlueprint
)  # Registering the blueprint for the search bar route
app.register_blueprint(
    adminPanelBlueprint
)  # Registering the blueprint for the admin panel route
app.register_blueprint(
    createPostBlueprint
)  # Registering the blueprint for the create post route
app.register_blueprint(
    verifyUserBlueprint
)  # Registering the blueprint for the verify user route
app.register_blueprint(
    setLanguageBlueprint
)  # Registering the blueprint for the set language route
app.register_blueprint(
    privacyPolicyBlueprint
)  # Registering the blueprint for the privacy policy route
app.register_blueprint(
    passwordResetBlueprint
)  # Registering the blueprint for the password reset route
app.register_blueprint(
    changeUserNameBlueprint
)  # Registering the blueprint for the change username route
app.register_blueprint(
    changePasswordBlueprint
)  # Registering the blueprint for the change password route
app.register_blueprint(
    changeLanguageBlueprint
)  # Registering the blueprint for the change language route
app.register_blueprint(
    adminPanelUsersBlueprint
)  # Registering the blueprint for the admin panel users route
app.register_blueprint(
    adminPanelPostsBlueprint
)  # Registering the blueprint for the admin panel posts route
app.register_blueprint(
    accountSettingsBlueprint
)  # Registering the blueprint for the account settings route
app.register_blueprint(
    returnPostBannerBlueprint
)  # Registering the blueprint for the return post banner route
app.register_blueprint(
    adminPanelCommentsBlueprint
)  # Registering the blueprint for the admin panel comments route
app.register_blueprint(
    changeProfilePictureBlueprint
)  # Registering the blueprint for the change profile picture route
app.register_blueprint(
    analyticsBlueprint
)  # Registering the blueprint for the analytics page route
app.register_blueprint(
    returnPostAnalyticsDataBlueprint
)  # Registering the blueprint for the postAnalyticsData endpoint route

# Check if the name of the module is the main module
match __name__:
    case "__main__":
        # Log the host and port
        Log.info(f"Running on http://{APP_HOST}:{APP_PORT}")

        # Log a message that the app started successfully
        Log.success("App started")

        # Print a ASCII art
        print(terminalASCII())

        # Run the app with the debug mode, host and port settings
        app.run(debug=DEBUG_MODE, host=APP_HOST, port=APP_PORT)

        # Get the end time of the app
        endTime = currentTimeStamp()

        # Calculate the run time of the app
        runTime = endTime - startTime

        # Convert the run time to a string
        runTime = str(timedelta(seconds=runTime))

        # Log a message that shows the run time of the app
        Log.info(f"Run time: {runTime} ")

        # Log a message that the app shut down
        Log.info("Shut down")

        # Log a warning message that the app shut down
        Log.warning("App shut down")

        # Print a ASCII art
        print(terminalASCII())
