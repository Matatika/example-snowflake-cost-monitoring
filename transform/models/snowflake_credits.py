def model(dbt, session):

    dbt.config(materialized="incremental", unique_key="run_timestamp", schema="SNOWFLAKE_COST")

    session.sql("SHOW RESOURCE MONITORS").collect()  # populate RESULT_SCAN

    df = session.sql("""
        SELECT
            "name"
            , "credit_quota"
            , "used_credits"
            , "remaining_credits"
            , "level"
            , "frequency"
            , "notify_users"
            , CURRENT_TIMESTAMP() AS run_timestamp
        FROM TABLE(RESULT_SCAN(LAST_QUERY_ID()))
    """)

    # This logic means ALWAYS ONLY append new rows, even on --full-refresh, maintaining history
    if not dbt.is_incremental:
        full_table_name = f'{dbt.this.database}.{dbt.this.schema}.{dbt.this.identifier}'
        existing = session.table(full_table_name)
        df = existing.union_by_name(df)

    return df
