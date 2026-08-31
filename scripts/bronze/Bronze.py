# Databricks notebook source
# MAGIC %md
# MAGIC # Reading from csv file

# COMMAND ----------

# MAGIC %md
# MAGIC # loading "cust_info.csv"

# COMMAND ----------


df = spark.read.option("header", "true").option("inferSchema", "true").csv('/Volumes/workspace/bronze/source_system/source_crm/cust_info.csv', header=True)
df.write.mode("overwrite").saveAsTable("workspace.bronze.crm_cust_info")

# COMMAND ----------

# MAGIC %md
# MAGIC # loading "prd_info.csv"

# COMMAND ----------

df = spark.read.option("header", "true").option("inferSchema", "true").csv('/Volumes/workspace/bronze/source_system/source_crm/prd_info.csv', header=True)
df.write.mode("overwrite").saveAsTable("workspace.bronze.crm_prd_info")

# COMMAND ----------

# MAGIC %md
# MAGIC # loading "sales_details.csv"

# COMMAND ----------

df = spark.read.option("header", "true").option("inferSchema", "true").csv('/Volumes/workspace/bronze/source_system/source_crm/sales_details.csv', header=True)
df.write.mode("overwrite").saveAsTable("workspace.bronze.crm_sales_details")

# COMMAND ----------

# MAGIC %md
# MAGIC # loading "CUST_AZ12.csv"

# COMMAND ----------

df = spark.read.option("header", "true").option("inferSchema", "true").csv('/Volumes/workspace/bronze/source_system/source_erp/CUST_AZ12.csv', header=True)
df.write.mode("overwrite").saveAsTable("workspace.bronze.erp_cust_az12")

# COMMAND ----------

# MAGIC %md
# MAGIC # loading "LOC_A101.csv"
# MAGIC

# COMMAND ----------

df = spark.read.option("header", "true").option("inferSchema", "true").csv('/Volumes/workspace/bronze/source_system/source_erp/LOC_A101.csv', header=True)
df.write.mode("overwrite").saveAsTable("workspace.bronze.erp_loc_a101")


# COMMAND ----------

# MAGIC %md
# MAGIC # loading "PX_CAT_G1V2.csv"

# COMMAND ----------

df = spark.read.option("header", "true").option("inferSchema", "true").csv('/Volumes/workspace/bronze/source_system/source_erp/PX_CAT_G1V2.csv', header=True)
df.write.mode("overwrite").saveAsTable("workspace.bronze.erp_px_cat_g1v2")
     