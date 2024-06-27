from neo4j import GraphDatabase

uri = "neo4j+s://a9bfa888.databases.neo4j.io"
username = "neo4j"
password = "uygzFjyQ_DbUsgSPf_P4ywowk4eVbv4r5uOf1GiIafo"

driver = GraphDatabase.driver(uri, auth=(username, password))

