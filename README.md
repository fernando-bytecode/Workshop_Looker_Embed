# README

## Create GCP Compute Instance

```bash
gcloud compute instances create 'embed-workshop' \
    --image-family=debian-11 \
    --image-project=debian-cloud \
    --machine-type=g1-small \
    --scopes userinfo-email,cloud-platform \
    --metadata-from-file startup-script=startup-script.sh \
    --tags http-server
```

## COPY OR CREATE .ENV FILE

We need to create the env file that contains our information. you can either ssh into your instance:

```bash
gcloud compute ssh embed-workshop
```

This will ssh you into your instance, you might want to switch to the `pythonapp` user with

```bash
su pythonapp
```

And create a file in the `opt/app/application`.

```bash
nano /opt/app/application/.env
```

Insert the values for the env file:
```yaml
# A URL like https://my.looker.com:19999. No default value.
LOOKERSDK_BASE_URL=	https://YOUR_LOOKER_INSTANCE:19999 
#true, t, yes, y, or 1 (case insensitive) to enable SSL verification. Any other value is treated as false. Defaults to true if not set.
LOOKERSDK_VERIFY_SSL=true	
#Request timeout in seconds. Defaults to 120 for most platforms.
LOOKERSDK_TIMEOUT=120	
#API3 credentials client_id. This and client_secret must be provided in some fashion to the Node SDK, or no calls to the API will be authorized. No default value.
LOOKERSDK_CLIENT_ID=YOUR_LOOKER_CLIENT_ID	
#API3 credentials client_secret. No default value
LOOKERSDK_CLIENT_SECRET=YOUR_LOOKER_CLIENT_ID	

# Fake Authentication
EMBED_DOMAIN_HOST_URL=http://YOUR_:8080
LOOKER_USER_FIRSTNAME=Fernando
LOOKER_USER_LASTNAME=Embed
LOOKER_USER_EXTERNAL_USER_ID=Fernando_Test
LOOKER_USER_PERMISSIONS= access_data,see_user_dashboards
LOOKER_USER_GROUPS=46
LOOKER_MODELS=ecommerce,retention_analysis
LOOKER_DASHBOARD=https://looker.bytecode.io/dashboards/yObpQDk1qZNdymPe30dtIi
```

Another option is to us `scp` to transfer the env file into the instance and the move the file into the correct folder (we are not sshing as sudo so we normally cannot copy direct to the `opt` folder)

```bash
gcloud compute scp ./application/.env embed-workshop:~

gcloud compute ssh embed-workshop

sudo mv ~/.env /opt/app/.env
```

