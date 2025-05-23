from flask import Flask, request
from flask_wtf.csrf import CSRFProtect, CSRFError
import subprocess
from modules import Log, currentTimeStamp, terminalASCII, timedelta

# Get the start time of the app
startTime = currentTimeStamp()
print(terminalASCII())
Log.info("Starting...")

# Configuration from modules
from modules import (
    APP_HOST, APP_NAME, APP_PORT, APP_ROOT_PATH, APP_SECRET_KEY, APP_VERSION,
    CUSTOM_LOGGER, DEBUG_MODE, DEFAULT_ADMIN, DEFAULT_ADMIN_EMAIL,
    DEFAULT_ADMIN_PASSWORD, DEFAULT_ADMIN_POINT, DEFAULT_ADMIN_PROFILE_PICTURE,
    DEFAULT_ADMIN_USERNAME, LOG_FILE_ROOT, LOG_FOLDER_ROOT, LOG_IN, RECAPTCHA,
    RECAPTCHA_BADGE, RECAPTCHA_COMMENT, RECAPTCHA_COMMENT_DELETE,
    RECAPTCHA_DELETE_USER, RECAPTCHA_LOGIN, RECAPTCHA_PASSWORD_CHANGE,
    RECAPTCHA_PASSWORD_RESET, RECAPTCHA_POST_CREATE, RECAPTCHA_POST_DELETE,
    RECAPTCHA_POST_EDIT, RECAPTCHA_PROFILE_PICTURE_CHANGE, RECAPTCHA_SECRET_KEY,
    RECAPTCHA_SIGN_UP, RECAPTCHA_SITE_KEY, RECAPTCHA_USERNAME_CHANGE,
    RECAPTCHA_VERIFY_URL, RECAPTCHA_VERIFY_USER, REGISTRATION, SESSION_PERMANENT,
    SMTP_MAIL, SMTP_PASSWORD, SMTP_PORT, SMTP_SERVER, STATIC_FOLDER,
    TEMPLATE_FOLDER, UI_NAME, WERKZEUG_LOGGER, browserLanguage, injectTranslations,
    isLogin, isRegistration, recaptchaBadge, returnPostUrlID, returnUserProfilePicture,
    returnPostUrlSlug
)

from routes.about import aboutBlueprint
from routes.accountSettings import accountSettingsBlueprint
from routes.adminPanel import adminPanelBlueprint
from routes.adminPanelComments import adminPanelCommentsBlueprint
from routes.adminPanelPosts import adminPanelPostsBlueprint
from routes.adminPanelUsers import adminPanelUsersBlueprint
from routes.category import categoryBlueprint
from routes.changeLanguage import changeLanguageBlueprint
from routes.changePassword import changePasswordBlueprint
from routes.changeProfilePicture import changeProfilePictureBlueprint
from routes.changeUserName import changeUserNameBlueprint
from routes.createPost import createPostBlueprint
from routes.dashboard import dashboardBlueprint
from routes.editPost import editPostBlueprint
from routes.index import indexBlueprint
from routes.login import loginBlueprint
from routes.logout import logoutBlueprint
from routes.passwordReset import passwordResetBlueprint
from routes.post import postBlueprint
from routes.postsAnalytics import analyticsBlueprint
from routes.privacyPolicy import privacyPolicyBlueprint
from routes.returnPostAnalyticsData import returnPostAnalyticsDataBlueprint
from routes.returnPostBanner import returnPostBannerBlueprint
from routes.search import searchBlueprint
from routes.searchBar import searchBarBlueprint
from routes.setLanguage import setLanguageBlueprint
from routes.signup import signUpBlueprint
from routes.user import userBlueprint
from routes.verifyUser import verifyUserBlueprint
from utils.afterRequest import afterRequestLogger
from utils.dbChecker import analyticsTable, commentsTable, dbFolder, postsTable, usersTable
from utils.errorHandlers.csrfErrorHandler import csrfErrorHandler
from utils.errorHandlers.notFoundErrorHandler import notFoundErrorHandler
from utils.errorHandlers.unauthorizedErrorHandler import unauthorizedErrorHandler
from utils.generateUrlIdFromPost import getSlugFromPostTitle

# Create app and disable CSRF
app = Flask(import_name=APP_NAME, root_path=APP_ROOT_PATH, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER)
app.config["WTF_CSRF_ENABLED"] = False
csrf = CSRFProtect()
csrf.init_app(app)

app.secret_key = APP_SECRET_KEY
app.config["SESSION_PERMANENT"] = SESSION_PERMANENT
app.jinja_options["autoescape"] = True

# Context processors and middleware
app.context_processor(isLogin)
app.context_processor(recaptchaBadge)
app.context_processor(isRegistration)
app.context_processor(returnUserProfilePicture)
app.context_processor(returnPostUrlID)
app.context_processor(returnPostUrlSlug)
app.context_processor(injectTranslations)
app.before_request(browserLanguage)

# Routes
@app.route("/webhook/backup", methods=["POST"])
def backup_to_s3():
    try:
        subprocess.call(["/home/hans/cloudmailsvc/backup-server/backup-to-s3.sh"])
        return " 백업 스크립트 실행 완료", 200
    except Exception as e:
        return f" 백업 실패: {str(e)}", 500

@app.route("/webhook/restore", methods=["POST"])
@csrf.exempt
def restore_from_s3():
    print("==== restore_from_s3 진입 ====")
    try:
        subprocess.call(["/home/hans/cloudmailsvc/backup-server/restore-from-s3.sh"])
        return " 복원 시작됨", 200
    except Exception as e:
        return f" 복원 실패: {str(e)}", 500

# Error Handlers
@app.errorhandler(404)
def notFound(e):
    return notFoundErrorHandler(e)

@app.errorhandler(401)
def unauthorized(e):
    return unauthorizedErrorHandler(e)

@app.errorhandler(CSRFError)
def csrfError(e):
    return csrfErrorHandler(e)

@app.after_request
def afterRequest(response):
    return afterRequestLogger(response)

@app.context_processor
def inject_custom_functions():
    return dict(getSlugFromPostTitle=getSlugFromPostTitle)

# Register Blueprints
app.register_blueprint(postBlueprint)
app.register_blueprint(userBlueprint)
app.register_blueprint(indexBlueprint)
app.register_blueprint(aboutBlueprint)
app.register_blueprint(loginBlueprint)
app.register_blueprint(signUpBlueprint)
app.register_blueprint(logoutBlueprint)
app.register_blueprint(searchBlueprint)
app.register_blueprint(categoryBlueprint)
app.register_blueprint(editPostBlueprint)
app.register_blueprint(dashboardBlueprint)
app.register_blueprint(searchBarBlueprint)
app.register_blueprint(adminPanelBlueprint)
app.register_blueprint(createPostBlueprint)
app.register_blueprint(verifyUserBlueprint)
app.register_blueprint(setLanguageBlueprint)
app.register_blueprint(privacyPolicyBlueprint)
app.register_blueprint(passwordResetBlueprint)
app.register_blueprint(changeUserNameBlueprint)
app.register_blueprint(changePasswordBlueprint)
app.register_blueprint(changeLanguageBlueprint)
app.register_blueprint(adminPanelUsersBlueprint)
app.register_blueprint(adminPanelPostsBlueprint)
app.register_blueprint(accountSettingsBlueprint)
app.register_blueprint(returnPostBannerBlueprint)
app.register_blueprint(adminPanelCommentsBlueprint)
app.register_blueprint(changeProfilePictureBlueprint)
app.register_blueprint(analyticsBlueprint)
app.register_blueprint(returnPostAnalyticsDataBlueprint)

# Final App Runner
if __name__ == "__main__":
    Log.info(f"Running on http://{APP_HOST}:{APP_PORT}")
    Log.success("App started")
    print(terminalASCII())
    app.run(debug=DEBUG_MODE, host=APP_HOST, port=APP_PORT)
    endTime = currentTimeStamp()
    runTime = str(timedelta(seconds=endTime - startTime))
    Log.info(f"Run time: {runTime} ")
    Log.info("Shut down")
    Log.warning("App shut down")
    print(terminalASCII())
