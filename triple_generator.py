from openie import StanfordOpenIE
import pathlib
import sys
import glob
import errno
from textwrap import wrap
import csv

def triple_generation(text,file_name):
    subject_s=[]
    relation_s=[]
    object_s=[]

    with StanfordOpenIE() as client:
        for triple in client.annotate(text):
            subject_s.append(triple['subject'])
            relation_s.append(triple['relation'])
            object_s.append(triple['object'])

    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(subject_s, relation_s,object_s))
    return "success"

def text_to_triples(path):
    #path = 'text_files2/*.txt'   
    files = glob.glob(path)   
    for name in files:
        print(name)
        with open(name) as f:
            text=f.read()
            print(len(text))
            if len(text)<100000:
                file_name= name +".csv"
                triple_generation(text,file_name)
            else:
                sub_text= wrap(text,100000)
                for i in sub_text :
                    print(len(i))
                    index=sub_text.index(i)
                    file_name= name +str(index) +".csv"
                    triple_generation(i,file_name)
                    
    return "files generated"

print(text_to_triples('text_files1/*.txt'))
