from flask import Flask, render_template
import looker_sdk
from looker_sdk import models as mdls
import dotenv
from flask_cors import CORS
import os

# Load your .env file
dotenv.load_dotenv()

# Initialize your Flask application
app = Flask(__name__)
CORS(app)

# Initialize the Looker SDK (since we will use it to handle the sso creation)
sdk=looker_sdk.init40()


# Normally we would do something to grab the right credentials from a cookie or something similar
EMBED_DOMAIN_HOST_URL=os.getenv('EMBED_DOMAIN_HOST_URL')
LOOKER_USER_FIRSTNAME= os.getenv('LOOKER_USER_FIRSTNAME')
LOOKER_USER_LASTNAME=os.getenv('LOOKER_USER_LASTNAME')
LOOKER_USER_EXTERNAL_USER_ID=os.getenv('LOOKER_USER_EXTERNAL_USER_ID')
LOOKER_USER_PERMISSIONS=os.getenv('LOOKER_USER_PERMISSIONS').split(",")
LOOKER_USER_GROUPS = os.getenv('LOOKER_USER_GROUPS').split(",")
LOOKER_MODELS=os.getenv('LOOKER_MODELS').split(",")
LOOKER_DASHBOARD=os.getenv('LOOKER_DASHBOARD')

host_url=EMBED_DOMAIN_HOST_URL

@app.route("/")
def embed_dashboard():
    target=LOOKER_DASHBOARD
    first_name=LOOKER_USER_FIRSTNAME
    last_name=LOOKER_USER_LASTNAME
    external_user_id=LOOKER_USER_EXTERNAL_USER_ID
    session_length=600
    force_logout_login=True
    permissions=LOOKER_USER_PERMISSIONS
    group_ids=LOOKER_USER_GROUPS
    models=LOOKER_MODELS
    external_group_id=""

    embed_url=create_embeded_url(
        target=target, 
        first_name=first_name, 
        last_name=last_name,
        external_user_id=external_user_id,
        session_length=session_length,
        force_logout_login=force_logout_login,
        permissions=permissions,
        group_ids=group_ids,
        models=models,
        external_group_id=external_group_id
        )
    return render_template('embed_dashboard.html',embed_url=embed_url.url, first_name=first_name)

@app.route("/themed")
def embed_dashboard_themed():
    target=LOOKER_DASHBOARD
    first_name=LOOKER_USER_FIRSTNAME
    last_name=LOOKER_USER_LASTNAME
    external_user_id=LOOKER_USER_EXTERNAL_USER_ID
    session_length=600
    force_logout_login=True
    permissions=LOOKER_USER_PERMISSIONS
    group_ids=LOOKER_USER_GROUPS
    models=LOOKER_MODELS
    external_group_id=""

    embed_url=create_embeded_url(
        target=target, 
        first_name=first_name, 
        last_name=last_name,
        external_user_id=external_user_id,
        session_length=session_length,
        force_logout_login=force_logout_login,
        permissions=permissions,
        group_ids=group_ids,
        models=models,
        external_group_id=external_group_id
        )
    return render_template('embed_dashboard.html',embed_url=embed_url.url)

@app.route("/js")
def embed_dashboard_js():
    target=LOOKER_DASHBOARD+f'?embed_domain={host_url}'
    first_name=LOOKER_USER_FIRSTNAME
    last_name=LOOKER_USER_LASTNAME
    external_user_id=LOOKER_USER_EXTERNAL_USER_ID
    session_length=600
    force_logout_login=True
    permissions=LOOKER_USER_PERMISSIONS
    group_ids=LOOKER_USER_GROUPS
    models=LOOKER_MODELS
    external_group_id=""

    embed_url=create_embeded_url(
        target=target, 
        first_name=first_name, 
        last_name=last_name,
        external_user_id=external_user_id,
        session_length=session_length,
        force_logout_login=force_logout_login,
        permissions=permissions,
        group_ids=group_ids,
        models=models,
        external_group_id=external_group_id
        )
    return render_template('embed_dashboard_js.html',embed_url=embed_url.url)

@app.route("/js_interact")
def embed_dashboard_js_interact():
    target=target=LOOKER_DASHBOARD+f'?embed_domain={host_url}'
    target=LOOKER_DASHBOARD
    first_name=LOOKER_USER_FIRSTNAME
    last_name=LOOKER_USER_LASTNAME
    external_user_id=LOOKER_USER_EXTERNAL_USER_ID
    session_length=600
    force_logout_login=True
    permissions=LOOKER_USER_PERMISSIONS
    group_ids=LOOKER_USER_GROUPS
    models=LOOKER_MODELS
    external_group_id=""

    embed_url=create_embeded_url(
        target=target, 
        first_name=first_name, 
        last_name=last_name,
        external_user_id=external_user_id,
        session_length=session_length,
        force_logout_login=force_logout_login,
        permissions=permissions,
        group_ids=group_ids,
        models=models,
        external_group_id=external_group_id
        )
    return render_template('embed_dashboard_js_button.html',embed_url=embed_url.url)


def create_embeded_url(target, first_name, last_name, external_user_id, session_length=600, force_logout_login=True,
                       permissions=[], group_ids=[], external_group_id="", models=[], user_timezone="UTC" ):
    body=mdls.EmbedSsoParams(
        target_url=target,
        session_length=session_length,
        force_logout_login=force_logout_login,
        external_user_id=external_user_id,
        first_name=first_name,
        last_name=last_name,
        permissions=permissions,
        models=models,
        group_ids=group_ids,
        external_group_id=external_group_id,
        user_timezone=user_timezone
    )

    response = sdk.create_sso_embed_url(body=body)

    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)