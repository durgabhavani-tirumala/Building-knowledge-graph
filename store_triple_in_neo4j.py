from py2neo import Graph, Node, Relationship
import pandas as pd

#give the ip address and port on which neo4j is running
# auth =(user_name,password), both neo4j in this case

graph = Graph("http://localhost:7474", auth=("neo4j", "neo4j"))

df = pd.read_csv("triple.csv")
##The header of the csv file must be subject ,relation,object
for index, row in triples_df.iterrows():
     tx = graph.begin()
     a = Node('Subject',name = row['subject'])
     tx.create(a)
     b = Node('Object',name = row['object'])
     ab = Relationship(a,row['relation'],b)
     tx.create(ab)
     tx.commit()
