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

pip install stanford-openiepip install stanford-openie

The openie is supporting only 100000 characters,so the length of the text must be below 100000 characters ,you can know the length of the text by using below python 


Run triple_generator.py program to generate triples from txt files


