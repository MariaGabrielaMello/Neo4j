from neo4j import GraphDatabase

uri = "neo4j+s://"
username = "neo4j"
password = "senha-aqui"

driver = GraphDatabase.driver(uri, auth=(username, password))

