# pip3 install neo4j
# python3 example.py

from neo4j import GraphDatabase, basic_auth

cypher_query = '''
MATCH (s:State {code: $state})<-[:REPRESENTS]-(l:Legislator)
RETURN l.firstName+' '+l.lastName as name
'''

with GraphDatabase.driver(
    "neo4j://<HOST>:<BOLTPORT>",
    auth=("<USERNAME>", "<PASSWORD>")
) as driver:
    result = driver.execute_query(
        cypher_query,
        state="NY",
        database_="neo4j")
    for record in result.records:
        print(record['name'])
