app_name = "Steve's App Engine Boilerplate Test"

webapp2_config = {}
webapp2_config['webapp2_extras.sessions'] = {
    'secret_key': 'qaW23e4Rcd210MKn',
}
webapp2_config['webapp2_extras.auth'] = {
    'user_model': 'boilerplate.models.User',
    'cookie_name': 'session_name'
}
webapp2_config['webapp2_extras.jinja2'] = {
    'template_path': 'boilerplate/templates',
    'environment_args': {'extensions': ['jinja2.ext.i18n']},
}

# the default language code for the application.
# should match whatever language the site uses when i18n is disabled
app_lang = 'en'

# Locale code = <language>_<territory> (ie 'en_US')
# to pick locale codes see http://cldr.unicode.org/index/cldr-spec/picking-the-right-language-code
# also see http://www.sil.org/iso639-3/codes.asp
# Language codes defined under iso 639-1 http://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
# Territory codes defined under iso 3166-1 alpha-2 http://en.wikipedia.org/wiki/ISO_3166-1
# disable i18n if locales array is empty or None
locales = ['en_US', 'es_ES', 'it_IT', 'zh_CN', 'id_ID', 'fr_FR', 'de_DE']

contact_sender = "strefethen@gmail.com"
contact_recipient = "strefethen@gmail.com"

# Password AES Encryption Parameters
aes_key = "12_24_32_BYTES_KEY_FOR_PASSWORDS"
salt = "_PUT_SALT_HERE_TO_SHA512_PASSWORDS_"

# get your own consumer key and consumer secret by registering at https://dev.twitter.com/apps
# callback url must be: http://[YOUR DOMAIN]/login/twitter/complete
twitter_consumer_key = 'WuntC0JjwgkJvmaPkBBmzw'
twitter_consumer_secret = 'EAqaZeG5uLoThcUNxdLIPoQNShElHXIg2OENsg4eLE'

#Facebook Login
# get your own consumer key and consumer secret by registering at https://developers.facebook.com/apps
#Very Important: set the site_url= your domain in the application settings in the facebook app settings page
# callback url must be: http://[YOUR DOMAIN]/login/facebook/complete
_FbApiKey = '387405964661332'
_FbSecret = 'bc918e13d8d6d6967e243a6f70e06e0a'

# NOT DONE!!
#Linkedin Login
#Get you own api key and secret from https://www.linkedin.com/secure/developer
linkedin_api = 'ueNRJIsyU3Q_EXer9MTOT3fpH-rQCGZWBBhVCeV3gyDzgNSB9Ov04DM3j6WEpSHf'
linkedin_secret = 'NYgmelU0_7PKf0LXYNq8ujtrp0F9UWBKaxd1hQOoBwiwVecHyZB9uTihZ-y7g4Me'

# get your own recaptcha keys by registering at www.google.com/recaptcha
captcha_public_key = "6Ldx5tYSAAAAADapzMQjU3i4fvbanj2ViqQENE8j"
captcha_private_key = "6Ldx5tYSAAAAAGN3vGPxSxmdQ9Fuu6l1JLzZXQX1"

google_analytics_code = "UA-35060467-1"

error_templates = {
    403: 'errors/default_error.html',
    404: 'errors/default_error.html',
    500: 'errors/default_error.html',
}

# Enable Federated login (OpenID and OAuth)
# Google App Engine Settings must be set to Authentication Options: Federated Login
enable_federated_login = True

# jinja2 base layout templates
base_layout = 'base.html'
