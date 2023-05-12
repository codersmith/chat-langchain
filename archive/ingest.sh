# Bash script to ingest data
# This involves scraping the data from the web and then cleaning up and putting in Weaviate.
!set -eu
wget -r -A.html https://langchain.readthedocs.io/en/latest/
python ingest.py
python ingest_examples.py
