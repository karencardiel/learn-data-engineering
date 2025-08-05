import psycopg2
import os

# --- Configuración de la conexión ---
DB_NAME = "catalogo_recursos"
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')
DB_HOST = "localhost"
DB_PORT = "5432"

if not DB_USER or not DB_PASS:
    print("Error: Por favor, define las variables de entorno DB_USER y DB_PASS")
    exit()

# --- Conexión, borrado y creación de la tabla ---
conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS resources;")

create_script = """
    CREATE TABLE resources (
        id SERIAL PRIMARY KEY,
        resource_name VARCHAR(255) NOT NULL,
        description TEXT,
        resource_type VARCHAR(100),
        link VARCHAR(255) NOT NULL,
        technologies VARCHAR(100)[],
        level VARCHAR(50)
    );
"""
cur.execute(create_script)

# --- Datos de ejemplo ---
resources_to_insert = [
    ('Data Engineering with Python', 'A very complete course on Datacamp that teaches you how to build data pipelines from scratch using Python.', 'Online Course', 'https://www.datacamp.com/tracks/data-engineer-with-python', '{"Python", "SQL", "Airflow"}', 'Beginner'),
    ('dbt (Data Build Tool)', 'The most popular tool for transforming data directly in your data warehouse. It''s the heart of the "T" in ELT.', 'Tool', 'https://www.getdbt.com/', '{"SQL", "dbt"}', 'Intermediate'),
    ('Seattle Data Guy', 'A YouTube channel with clear and direct explanations of data engineering concepts and tools.', 'Video/Channel', 'https://www.youtube.com/c/SeattleDataGuy', '{"Python", "SQL", "Spark", "Airflow"}', 'Intermediate'),
    ('The Data Engineering Show', 'A blog with in-depth articles on the latest trends, architectures, and best practices in the data world.', 'Article/Blog', 'https://www.dataengineeringshow.com/', ['BigQuery', 'Snowflake', 'Kafka'], 'Advanced'),
    ('Apache Airflow', 'Open-source tool to programmatically author, schedule, and monitor complex data workflows (pipelines).', 'Tool', 'https://airflow.apache.org/', '{"Python", "Airflow"}', 'Intermediate'),
    ('Designing Data-Intensive Applications', 'Considered the "bible" of data engineering. It explains the fundamentals of how large-scale data systems work.', 'Book', 'https://www.oreilly.com/library/view/designing-data-intensive-applications/9781491903063/', '{"Theoretical"}', 'Advanced'),
    ('Taming Big Data with Apache Spark and Python', 'A hands-on course to learn Spark, the most important framework for processing large volumes of data.', 'Online Course', 'https://www.udemy.com/course/taming-big-data-with-apache-spark-hands-on/?referralCode=297D37262CF83C2A61AE&couponCode=2021PM25', ['Spark', 'Python', 'SQL'], 'Intermediate'),
    ('Fundamentals of Data Engineering', 'A modern and comprehensive guide covering the entire data engineering lifecycle, from data generation to analytics.', 'Book', 'https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/', ['Theoretical', 'Best Practices'], 'Beginner'),
    ('Apache Kafka', 'A distributed event streaming platform used for building real-time data pipelines and streaming applications.', 'Tool', 'https://kafka.apache.org/', ['Kafka', 'Java', 'Scala', 'Streaming'], 'Advanced'),
    ('Data Engineering Weekly', 'A popular weekly newsletter that curates the best articles, news, and tools in the world of data engineering.', 'Article/Blog', 'https://www.dataengineeringweekly.com/', ['General', 'Cloud', 'ETL'], 'Intermediate'),
    ('Snowflake', 'A cloud data platform that provides a data warehouse-as-a-service designed for performance, concurrency, and simplicity.', 'Tool', 'https://www.snowflake.com/', ['SQL', 'Cloud', 'Snowflake'], 'Intermediate'),
    ('Fivetran', 'An automated data movement platform that simplifies the process of extracting and loading data from various sources into a data warehouse.', 'Tool', 'https://www.fivetran.com/', ['ETL', 'ELT', 'Cloud'], 'Beginner'),
    ('a16z: Modern Data Infrastructure', 'An influential article by Andreessen Horowitz that defines and analyzes the components of the modern data stack, from ingestion to business intelligence.', 'Article/Blog', 'https://a16z.com/emerging-architectures-for-modern-data-infrastructure-2020/', ['Architecture', 'AI', 'Modern Data Stack'], 'Advanced'),
    ('Andreas Kretz', 'A YouTube channel focused on practical tutorials for data engineering, especially with Spark, Kafka, and cloud technologies.', 'Video/Channel', 'https://www.youtube.com/channel/UCY8mzqqGwl5_bTpBY9qLMAA', ['Spark', 'Kafka', 'Python', 'Cloud'], 'Intermediate')
]

insert_query = "INSERT INTO resources (resource_name, description, resource_type, link, technologies, level) VALUES (%s, %s, %s, %s, %s, %s)"

for resource in resources_to_insert:
    cur.execute(insert_query, resource)

conn.commit()
cur.close()
conn.close()

print("✅ Base de datos 'catalogo_recursos' y tabla 'resources' creadas y pobladas con éxito.")