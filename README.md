# ETL-Pipeline
This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine

Astro project contains the following files and folders:


***Dags***: This folder contains the Python files for your Airflow DAGs. By default, this directory includes one example DAG:
  example_astronauts: This DAG shows a simple ETL pipeline example that queries the list of astronauts currently in space from the Open Notify API and prints a statement for each astronaut. The DAG uses the TaskFlow API to define tasks in 
  Python, and dynamic task mapping to dynamically print a statement for each astronaut. For more on how this DAG works, see our Getting started tutorial.
***Dockerfile***: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
**include**: This folder contains any additional files that you want to include as part of your project. It is empty by default.
**packages.txt**: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
**requirements.txt**: Install Python packages needed for your project by adding them to this file. It is empty by default.
**plugins**: Add custom or community plugins for your project to this file. It is empty by default.
**airflow_settings.yaml**: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.
