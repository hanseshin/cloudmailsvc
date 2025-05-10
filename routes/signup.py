# Import necessary modules and functions
from modules import (
    APP_NAME,  # Constant for application name
    DB_USERS_ROOT,  # Path to the users database
    RECAPTCHA,  # Recaptcha module
    RECAPTCHA_SECRET_KEY,  # Recaptcha secret key
    RECAPTCHA_SIGN_UP,  # Flag for enabling/disabling Recaptcha for sign-up
    RECAPTCHA_SITE_KEY,  # Recaptcha site key
    RECAPTCHA_VERIFY_URL,  # Recaptcha verification URL
    REGISTRATION,  # Flag for enabling/disabling user registration
    SMTP_MAIL,  # SMTP email address
    SMTP_USER,
    SMTP_PASSWORD,  # SMTP password
    SMTP_PORT,  # SMTP port number
    SMTP_SERVER,  # SMTP server address
    Blueprint,  # Blueprint class for creating modular applications
    EmailMessage,  # Class for creating email messages
    Log,  # Logging module
    SignUpForm,  # Form for user sign-up
    abort,  # Function for aborting requests
    addPoints,  # Function for adding points to user
    currentTimeStamp,  # Function for getting current timestamp
    encryption,  # Encryption module
    flashMessage,  # Flash messaging module
    redirect,  # Function for redirecting requests
    render_template,  # Function for rendering templates
    request,  # Module for handling HTTP requests
    requestsPost,  # Module for making HTTP POST requests
    requests,
    session,  # Session management module
    smtplib,  # SMTP client module
    sqlite3,  # SQLite database module
    ssl,  # SSL/TLS module
)

# Create a blueprint for the signup route
signUpBlueprint = Blueprint("signup", __name__)



# Define the route handler for the signup page
@signUpBlueprint.route("/signup", methods=["GET", "POST"])
def signup():
    """
    This function handles the sign up route.

    If the user is already signed in, they will be redirected to the homepage.
    If the user submits the sign up form, their information is checked to ensure it is valid.
    If the information is valid, their account is created and they are signed in.

    Returns:
    The sign up page with any errors or a confirmation message.
    """
    # Check if registration is enabled
    match REGISTRATION:
        # If registration is enabled
        case True:
            # Check if the user is already logged in
            match "userName" in session:
                # If user is already logged in, redirect to homepage
                case True:
                    Log.error(f'USER: "{session["userName"]}" ALREADY LOGGED IN')
                    return redirect("/")
                # If user is not logged in
                case False:
                    # Create sign up form object
                    form = SignUpForm(request.form)
                    # Check if request method is POST (form submitted)
                    match request.method == "POST":
                        # If form is submitted
                        case True:
                            # Extract form data
                            userName = request.form["userName"]
                            email = request.form["email"]
                            password = request.form["password"]
                            passwordConfirm = request.form["passwordConfirm"]
                            # Remove spaces from username
                            userName = userName.replace(" ", "")
                            Log.database(
                                f"Connecting to '{DB_USERS_ROOT}' database"
                            )  # Log the database connection is started
                            # Connect to the database
                            connection = sqlite3.connect(DB_USERS_ROOT)
                            connection.set_trace_callback(
                                Log.database
                            )  # Set the trace callback for the connection
                            cursor = connection.cursor()
                            # Fetch existing usernames and emails from the database
                            cursor.execute("select userName from users")
                            users = str(cursor.fetchall())
                            cursor.execute("select email from users")
                            mails = str(cursor.fetchall())
                            # Check if username and email are available
                            match userName not in users and email not in mails:
                                # If username and email are available
                                case True:
                                    # Check if passwords match
                                    match passwordConfirm == password:
                                        # If passwords match
                                        case True:
                                            # Check if username contains only ASCII characters
                                            match userName.isascii():
                                                # If username contains only ASCII characters
                                                case True:
                                                    # Hash the password
                                                    password = encryption.hash(password)
                                                    # Connect to the database
                                                    connection = sqlite3.connect(
                                                        DB_USERS_ROOT
                                                    )
                                                    connection.set_trace_callback(
                                                        Log.database
                                                    )  # Set the trace callback for the connection
                                                    # Check if reCAPTCHA is enabled for sign up
                                                    match (
                                                        RECAPTCHA and RECAPTCHA_SIGN_UP
                                                    ):
                                                        # If reCAPTCHA is enabled
                                                        case True:
                                                            # Verify reCAPTCHA response
                                                            secretResponse = request.form[
                                                                "g-recaptcha-response"
                                                            ]
                                                            verifyResponse = requestsPost(
                                                                url=f"{RECAPTCHA_VERIFY_URL}?secret={RECAPTCHA_SECRET_KEY}&response={secretResponse}"
                                                            ).json()
                                                            # If reCAPTCHA verification is successful
                                                            match (
                                                                verifyResponse[
                                                                    "success"
                                                                ]
                                                                is True
                                                                or verifyResponse[
                                                                    "score"
                                                                ]
                                                                > 0.5
                                                            ):
                                                                # If reCAPTCHA verification is successful
                                                                case True:
                                                                    Log.success(
                                                                        f"Sign up reCAPTCHA | verification: {verifyResponse['success']} | verification score: {verifyResponse['score']}",
                                                                    )
                                                                    # Insert user data into the database
                                                                    cursor = connection.cursor()
                                                                    cursor.execute(
                                                                        """
                                                                        insert into users(userName,email,password,profilePicture,role,points,timeStamp,isVerified) \
                                                                        values(?, ?, ?, ?, ?, ?, ?, ?)
                                                                        """,
                                                                        (
                                                                            userName,
                                                                            email,
                                                                            password,
                                                                            f"https://api.dicebear.com/7.x/identicon/svg?seed={userName}&radius=10",
                                                                            "user",
                                                                            0,
                                                                            currentTimeStamp(),
                                                                            "False",
                                                                        ),
                                                                    )
                                                                    connection.commit()
                                                                    # Log user addition
                                                                    Log.success(
                                                                        f'User: "{userName}" added to database',
                                                                    )
                                                                    # Store username in session (log user in)
                                                                    session[
                                                                        "userName"
                                                                    ] = userName
                                                                    # Add points to the user
                                                                    addPoints(
                                                                        1,
                                                                        session[
                                                                            "userName"
                                                                        ],
                                                                    )
                                                                    # Log user login
                                                                    Log.success(
                                                                        f'User: "{userName}" logged in',
                                                                    )
                                                                    # Flash success message
                                                                    flashMessage(
                                                                        page="signup",
                                                                        message="success",
                                                                        category="success",
                                                                        language=session[
                                                                            "language"
                                                                        ],
                                                                    )  # Display a flash message
                                                                    # Set up email server connection
                                                                    context = ssl.create_default_context()
                                                                    server = (
                                                                        smtplib.SMTP(
                                                                            SMTP_SERVER,
                                                                            SMTP_PORT,
                                                                        )
                                                                    )
                                                                    server.ehlo()
                                                                    server.starttls(
                                                                        context=context
                                                                    )
                                                                    server.ehlo()
                                                                    server.login(
                                                                        SMTP_USER,
                                                                        SMTP_PASSWORD,
                                                                    )
                                                                    # Compose email message
                                                                    mail = (
                                                                        EmailMessage()
                                                                    )
                                                                    mail.set_content(
                                                                        f"Hi {userName}👋,\n Welcome to {APP_NAME}"
                                                                    )
                                                                    mail.add_alternative(
                                                                        f"""\
                                                                    <html>
                                                                    <body>
                                                                        <div
                                                                        style="font-family: Arial, sans-serif;  max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius:0.5rem;"
                                                                        >
                                                                        <div style="text-align: center;">
                                                                            <h1 style="color: #F43F5E;">
                                                                            Hi {userName}, <br />
                                                                            Welcome to {APP_NAME}!
                                                                            </h1>
                                                                            <p style="font-size: 16px;">
                                                                            We are glad you joined us.
                                                                            </p>
                                                                        </div>
                                                                        </div>
                                                                    </body>
                                                                    </html>
                                                                    """,
                                                                        subtype="html",
                                                                    )
                                                                    mail["Subject"] = (
                                                                        f"Welcome to {APP_NAME}"
                                                                    )
                                                                    mail["From"] = (
                                                                        SMTP_MAIL
                                                                    )
                                                                    mail["To"] = email
                                                                    # Send email
                                                                    server.send_message(
                                                                        mail
                                                                    )
                                                                    SLACK_WEBHOOK_URL ="https://hooks.slack.com/services/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"

                                                                    admin_mail = EmailMessage()
                                                                    admin_mail.set_content(f"New user signed up: {userName} ({email})")
                                                                    admin_mail["Subject"] = f"[Admin Alert] New signup: {userName}"
                                                                    admin_mail["From"] = SMTP_MAIL
                                                                    admin_mail["To"] = "hansesin143@gmail.com"
                                                                    
                                                                    
                                                                    try:
                                                                        server.send_message(admin_mail)
                                                                        Log.success(f"Admin notified of new signup: {userName}")
                                                                    except Exception as e:
                                                                        Log.error(f"Failed to notify admin: {str(e)}")                                                                        
                                                                   

                                                                    
                                                                    slack_message = {
                                                                            "text": f"📬 New user signup: *{userName}* ({email}) just joined {APP_NAME}!"
                                                                        }

                                                                    try:
                                                                         requests.post(SLACK_WEBHOOK_URL, json=slack_message)
                                                                         Log.success(f"Slack notified for new signup: {userName}")
                                                                    except Exception as e:
                                                                         Log.error(f"Slack notification failed: {str(e)}")
                                                                         
                                                                    server.quit()
                                                                    # Redirect user for further verification
                                                                    return redirect(
                                                                        "/verifyUser/codesent=false"
                                                                    )
                                                                # If reCAPTCHA verification fails
                                                                case False:
                                                                    Log.error(
                                                                        f"Sign up reCAPTCHA | verification: {verifyResponse['success']} | verification score: {verifyResponse['score']}",
                                                                    )
                                                                    abort(401)
                                                        # If reCAPTCHA is not enabled
                                                        case False:
                                                            # Insert user data into the database
                                                            cursor = connection.cursor()
                                                            cursor.execute(
                                                                """
                                                                        insert into users(userName,email,password,profilePicture,role,points,timeStamp,isVerified) \
                                                                        values(?, ?, ?, ?, ?, ?, ?, ?)
                                                                        """,
                                                                (
                                                                    userName,
                                                                    email,
                                                                    password,
                                                                    f"https://api.dicebear.com/7.x/identicon/svg?seed={userName}&radius=10",
                                                                    "user",
                                                                    0,
                                                                    currentTimeStamp(),
                                                                    "False",
                                                                ),
                                                            )
                                                            connection.commit()
                                                            # Log user addition
                                                            Log.success(
                                                                f'User: "{userName}" added to databse',
                                                            )
                                                            # Store username in session (log user in)
                                                            session["userName"] = (
                                                                userName
                                                            )
                                                            # Add points to the user
                                                            addPoints(
                                                                1, session["userName"]
                                                            )
                                                            # Log user login
                                                            Log.success(
                                                                f'User: "{userName}" logged in',
                                                            )
                                                            flashMessage(
                                                                page="signup",
                                                                message="success",
                                                                category="success",
                                                                language=session[
                                                                    "language"
                                                                ],
                                                            )  # Display a flash message
                                                            # Set up email server connection
                                                            context = ssl.create_default_context()
                                                            server = smtplib.SMTP(
                                                                SMTP_SERVER, SMTP_PORT
                                                            )
                                                            server.ehlo()
                                                            server.starttls(
                                                                context=context
                                                            )
                                                            server.ehlo()
                                                            server.login(
                                                                SMTP_USER, SMTP_PASSWORD
                                                            )
                                                            # Compose email message
                                                            mail = EmailMessage()
                                                            mail.set_content(
                                                                f"Hi {userName}👋,\n Welcome to {APP_NAME}"
                                                            )
                                                            mail.add_alternative(
                                                                f"""\
                                                                <html>
                                                                <body>
                                                                    <div
                                                                    style="font-family: Arial, sans-serif;  max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius:0.5rem;"
                                                                    >
                                                                    <div style="text-align: center;">
                                                                        <h1 style="color: #F43F5E;">
                                                                        Hi {userName}, <br />
                                                                        Welcome to {APP_NAME}!
                                                                        </h1>
                                                                        <p style="font-size: 16px;">
                                                                        We are glad you joined us.
                                                                        </p>
                                                                    </div>
                                                                    </div>
                                                                </body>
                                                                </html>
                                                            """,
                                                                subtype="html",
                                                            )
                                                            mail["Subject"] = (
                                                                f"Welcome to {APP_NAME}!👋🏻"
                                                            )
                                                            mail["From"] = SMTP_MAIL
                                                            mail["To"] = email
                                                            # Send email
                                                            server.send_message(mail)
                                                            server.quit()
                                                            # Redirect user for further verification
                                                            return redirect(
                                                                "/verifyUser/codesent=false"
                                                            )
                                                # If username contains non-ASCII characters
                                                case False:
                                                    Log.error(
                                                        f'Username: "{userName}" do not fits to ascii characters',
                                                    )
                                                    flashMessage(
                                                        page="signup",
                                                        message="ascii",
                                                        category="error",
                                                        language=session["language"],
                                                    )  # Display a flash message
                                        # If passwords do not match
                                        case False:
                                            Log.error("Passwords do not match")
                                            # Flash error message
                                            flashMessage(
                                                page="signup",
                                                message="password",
                                                category="error",
                                                language=session["language"],
                                            )  # Display a flash message
                            # If username or email is not available
                            match userName in users and email in mails:
                                case True:
                                    Log.error(
                                        f'"{userName}" & "{email}" is unavailable '
                                    )
                                    flashMessage(
                                        page="signup",
                                        message="taken",
                                        category="error",
                                        language=session["language"],
                                    )  # Display a flash message
                            match userName not in users and email in mails:
                                case True:
                                    Log.error(f'This email "{email}" is unavailable')
                                    # Flash error message
                                    flashMessage(
                                        page="signup",
                                        message="email",
                                        category="error",
                                        language=session["language"],
                                    )  # Display a flash message
                            match userName in users and email not in mails:
                                case True:
                                    Log.error(
                                        f'This username "{userName}" is unavailable',
                                    )
                                    # Flash error message
                                    flashMessage(
                                        page="signup",
                                        message="username",
                                        category="error",
                                        language=session["language"],
                                    )  # Display a flash message
                    # Render sign up template with form data
                    return render_template(
                        "signup.html.jinja",
                        form=form,
                        hideSignUp=True,
                        siteKey=RECAPTCHA_SITE_KEY,
                        recaptcha=RECAPTCHA,
                    )
        # If registration is disabled
        case False:
            # Redirect to homepage
            return redirect("/")
