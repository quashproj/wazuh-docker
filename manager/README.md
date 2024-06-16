# Wazuh Manager/Worker - QUASH Image

It adds integrations to the default **Wazuh** image.

## Versions

Make sure to build an image for a specific version, do no t use **latest**. The base image version is in the **Dockerfile**

For examples:

```bash
docker build -t ghcr.io/quashproj/wazuh-manager:4.7.3-2 .
docker image push ghcr.io/quashproj/wazuh-manager:4.7.3-2
```

## Integrations

1. Copy integration files to integrations
2. Modify permanent_data.env file with new integrations
3. Build and deploy image.  Use new TAG!

