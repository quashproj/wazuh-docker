FROM 'wazuh/wazuh-manager:4.7.4'

# Install thehive4py module
RUN  /var/ossec/framework/python/bin/pip3 install thehive4py==1.8.1

# Wazuh TMP folder, things are installed from here

# Custom extensions
COPY ./integrations /var/ossec/data_tmp/exclusion/var/ossec/integrations
RUN chown -R root:wazuh  /var/ossec/data_tmp/exclusion/var/ossec/integrations/

# Config for files that shuld be updated
COPY ./etc/ /var/ossec/data_tmp/etc/
COPY ./permanent_data.env /
