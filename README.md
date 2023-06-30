# Snowflake Cost Monitoring

This stand alone Meltano project with the Matatika lab is a quick and easy way to monitor your Snowflake costs.

---

## Prerequisites

**NB - Currently this project is only supported to work on Linux and MacOS**

1. Get Docker - [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
2. Your Snowflake database credentials

---

## From 0 to ELT in seconds


Using Matatika you can run this example with only docker and we create all the following for you:
- Postgres data warehouse
- Meltano jobs for running dbt models
- Lab (UI for Meltano) to run and schedule jobs
- Simple charts that can be embedded anywhere [https://github.com/Matatika/dataset-component-example](https://github.com/Matatika/dataset-component-example)

### Steps

You can run this as a stand alone Meltano project, you will need to provide all your Snowflake credentials through `meltano config` or a `.env` for the `dbt` plugin. You will then need to run `meltano run dbt:deps dbt:run`. Finally you can check your processed Snowflake cost data in new tables in your Snowflake database.

Or you can follow the steps below, use a UI to configure your project and see datasets in the Matatika Lab UI.

1. Clone and start up the project:
   ```terminal
   git clone git@github.com:Matatika/snowflake-cost-monitoring.git
   cd snowflake-cost-monitoring
   meltano install
   meltano invoke matatika lab
   ```

1. Your web browser automatically opens [https://localhost:3443](https://localhost:3443)

1. You will see a task to complete `Complete your 'Snowflake' store configuration`, click `LET'S GO`, fill in your Snowflake credentials and click `SAVE`

1. On the left hand menu go to the `Stores` screen, click the three dots at the end of the `Snowflake` data store, and click `Make default`

1. Go to the `Pipelines screen`, and click the Run (play) button on the `Cost analysis` pipeline. This should take less than 2 minutes, you can check to job logs by expanding the pipeline with the button to the right of the Run (play) button.

1. When this pipeline has completed go to the `Datasets` screen to see insights into your Snowflake costs!

---

### Support

Join our community on the [Matatika Slack](https://join.slack.com/t/matatika/shared_invite/zt-19n1bfokx-F31DNitTpSxWCFO2aFlgxg) to get help and updates.

You can read more about Matatika and our Lab in our [Documentation](https://www.matatika.com/docs/).
