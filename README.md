Steps to build knowledge Graph for search:

1.Generating triples from given text

2.Storing Triples in Graph Database

3.Querying the graph 



Step1:Generating triples from given text using pip install stanford-openie  package

Open information extraction (openie) was released by the stanford natural processing group.This software is a Java implementation of an open IE system.

Installation Steps:

1.Since it is written in Java, make sure java 1.8 is installed in your system .To check whether java is installed or not run below command in terminal

          java -version

2.If OS is windows system ,download and install the java from https://www.oracle.com/in/java/technologies/javase-downloads.html and set the path

3.If OS is linux system,install the java using below commands

          sudo add-apt-repository ppa:webupd8team/java

          sudo apt-get update

          sudo apt-get install oracle-java8-installer

4.Install stanford openie python package using below command:

              pip install stanford-openie


The openie is supporting only 100000 characters,so the length of the text must be below 100000 characters ,you can know the length of the text by using below python 


Run triple_generator.py program to generate triples from txt files

Step2:Storing triples in Graph Database:

Neo4j is available in two editions:

    • Community edition:It is fully functional and designed for single instance deployments .
    
    • Enterprise edition:It has all the features of community edition and has extra features like clustering and online backup facility .
    
Installation steps for community edition:

    • In windows, download neo4j from https://neo4j.com/download/neo4j-desktop/?edition=desktop&flavour=unix&release=1.2.9&offline=true and install it
    
    • In ubuntu, java has to be installed to install neo4j.Follow the steps in below link to install neo4j in ubuntu  https://dzone.com/articles/installing-neo4j-on-ubuntu-1604
 
Once the installation is completed neo4j can be accessible in the browser also,the default username and password for the browser version is neo4j.


Install py2neo package using below command:

         pip install py2neo
         
Now give the triple.csv (which is generated from the previous step) as input to store_triple_in_neo4j.py to store triples in neo4j Database.

Now you can visualise knowledge graph in neo4j database


Step3: Querying neo4j or knowledge Graph:

Go to the neo4j web browser,there you can start searching nodes

Sample query to start with:

            MATCH (n:Subject) RETURN n LIMIT 25 
            
- Matches the nodes with label Subject and returns 25 results as a limitation is mentioned in the query.

- You can select the label from Subject and Object and query the graph using the query.

or you can access the neo4j graph with credentials using python script.

