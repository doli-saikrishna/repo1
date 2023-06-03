# Databricks notebook source
storage_account_name = "dookudu"
client_id            = "d6735a35-7500-4a15-9747-7fbd565e8da8"
tenant_id            = "4052f8a5-1721-4c62-a7c0-02d03bb8bb70"
client_secret        = "ky~8Q~CGnD15amuWskMUcalEnbbXCRGiP8SURabS"

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type" : "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id" : f"{client_id}",
           "fs.azure.account.oauth2.client.secret" : f"{client_secret}",
           "fs.azure.account.ouath2.client.endpoint" :f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"}

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "d6735a35-7500-4a15-9747-7fbd565e8da8",
          "fs.azure.account.oauth2.client.secret": dbutils.secrets.get(scope="<scope-name>",key="<service-credential-key-name>"),
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<directory-id>/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/",
  mount_point = "/mnt/<mount-name>",
  extra_configs = configs)

# COMMAND ----------

dbutils.fs.mount(
    source = f"abfss://raw@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/raw",
    extra_configs = configs)

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

dbutils.fs.mount(
    source = f"abfss://raw@{storage_account_name}.dfs.core.windows.net/",
    mount_point = f"/mnt/{storage_account_name}/raw",
    extra_configs = configs)

# COMMAND ----------



# COMMAND ----------


