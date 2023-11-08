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