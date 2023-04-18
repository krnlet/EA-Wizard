import subprocess
import random

namefile='results.csv'

def ymlfile_1(csvfile1):  
    yfile=open('templates/results/file_yml_1.yml', 'w')
    ymlfile=str()

    ymlfile='prefixes:\n'
    ymlfile+='  eao: http://eaontology.linkeddata.es/def/\n'
    ymlfile+='  ebocaev: https://w3id.org/eboca/evidences#\n'
    ymlfile+='  owl: http://www.w3.org/2002/07/owl#\n'
    ymlfile+='  dc: http://purl.org/dc/terms/\n'
    ymlfile+='  foaf: http://xmlns.com/foaf/0.1/\n'
    ymlfile+='  prov: http://www.w3.org/ns/prov#\n'
    ymlfile+='  modsci: https://w3id.org/skgo/modsci#\n'
    ymlfile+='  pmlp: http://inference-web.org/2.0/pml-provenance.owl#\n'
    ymlfile+='  rdfs: http://www.w3.org/2000/01/rdf-schema#\n'
    ymlfile+='  pav: http://purl.org/pav/\n'
    
    ymlfile+='mappings:\n'
    if(csvfile1):
        ymlfile+='  technology:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile1+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(technology_name)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, modsci:Technology]\n'
        ymlfile+='          - [pav:version, $(technology_version)]\n'
        ymlfile+='          - [eao:purpose, $(technology_purpose)]\n'
        ymlfile+='  technique:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile1+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(technique)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, eao:Technique]\n'
        ymlfile+='          - [eao:especificActivity, $(task_of_technique)]\n'
        ymlfile+='  feature:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile1+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(feature)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, eao:feature]\n'
        ymlfile+='          - [eao:formalFeature, $(feature)]\n'
        ymlfile+='  users:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile1+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(users)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, foaf:Group]\n'
        ymlfile+='          - [dc:identifier, $(users)]\n'



    #print(ymlfile)
    for line in ymlfile:
        yfile.write(line)

    return(ymlfile)

def ymlfile_2(csvfile2):  
    yfile=open('templates/results/file_yml_2.yml', 'w')
    ymlfile=str()

    ymlfile='prefixes:\n'
    ymlfile+='  eao: http://eaontology.linkeddata.es/def/\n'
    ymlfile+='  ebocaev: https://w3id.org/eboca/evidences#\n'
    ymlfile+='  owl: http://www.w3.org/2002/07/owl#\n'
    ymlfile+='  dc: http://purl.org/dc/terms/\n'
    ymlfile+='  foaf: http://xmlns.com/foaf/0.1/\n'
    ymlfile+='  prov: http://www.w3.org/ns/prov#\n'
    ymlfile+='  modsci: https://w3id.org/skgo/modsci#\n'
    ymlfile+='  pmlp: http://inference-web.org/2.0/pml-provenance.owl#\n'
    ymlfile+='  rdfs: http://www.w3.org/2000/01/rdf-schema#\n'
    ymlfile+='  pav: http://purl.org/pav/\n'
    
    ymlfile+='mappings:\n'
    if(csvfile2):
        ymlfile+='  technology:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile2+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(technology_level)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, modsci:TechnologyLevel]\n'
        ymlfile+='          - [eao:description, $(technology_level)]\n'
        ymlfile+='  artefact:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile2+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(artefact_level)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, eao:ArtefactLevel]\n'
        ymlfile+='          - [eao:description, $(artefact_level)]\n'
        ymlfile+='  app:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile2+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(app_level)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, eao:app_level]\n'
        ymlfile+='          - [eao:description, $(app_level)]\n'
        ymlfile+='  eval:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile2+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(evaluation)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, eao:EthicalEvaluation]\n'
        ymlfile+='          - [eao:description, $(evaluation)]\n'
        ymlfile+='  issue:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile2+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(ethical_issue)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, eao:EthicalIssue]\n'
        ymlfile+='          - [eao:description, $(ethical_issue)]\n'
        ymlfile+='  benefit:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile2+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(benefit)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, eao:Benefit]\n'
        ymlfile+='          - [eao:description, $(benefit)]\n'
        ymlfile+='  negative:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile2+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(negative)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, eao:NegativeImplication]\n'
        ymlfile+='          - [eao:description, $(negative)]\n'

    #print(ymlfile)
    for line in ymlfile:
        yfile.write(line)

    return(ymlfile)

def ymlfile_3(csvfile3):  
    yfile=open('templates/results/file_yml_3.yml', 'w')
    ymlfile=str()

    ymlfile='prefixes:\n'
    ymlfile+='  eao: http://eaontology.linkeddata.es/def/\n'
    ymlfile+='  ebocaev: https://w3id.org/eboca/evidences#\n'
    ymlfile+='  owl: http://www.w3.org/2002/07/owl#\n'
    ymlfile+='  dc: http://purl.org/dc/terms/\n'
    ymlfile+='  foaf: http://xmlns.com/foaf/0.1/\n'
    ymlfile+='  prov: http://www.w3.org/ns/prov#\n'
    ymlfile+='  modsci: https://w3id.org/skgo/modsci#\n'
    ymlfile+='  pmlp: http://inference-web.org/2.0/pml-provenance.owl#\n'
    ymlfile+='  rdfs: http://www.w3.org/2000/01/rdf-schema#\n'
    ymlfile+='  pav: http://purl.org/pav/\n'
    
    ymlfile+='mappings:\n'
    if(csvfile3):
        ymlfile+='  feasability:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile3+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(feasability)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, eao:TechnologyFeasability]\n'
        ymlfile+='          - [eao:description, $(feasability)]\n'
        ymlfile+='  usability:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile3+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$usability)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, eao:SocialUsability]\n'
        ymlfile+='          - [eao:description, $(usability)]\n'
        ymlfile+='  desirability:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile3+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(desirability)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, eao:ArtefactLevel]\n'
        ymlfile+='          - [eao:description, $(desirability)]\n'
        ymlfile+='  expectation:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile3+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(expectation)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, eao:expectation]\n'
        ymlfile+='          - [eao:description, $(expectation)]\n'
        ymlfile+='  evidence:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile3+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(evidence)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, ebocaev:evidence]\n'
        ymlfile+='          - [pav:createdOn, $(evidence)]\n'
        ymlfile+='  source:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile3+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(source)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, pmlp:source]\n'
        ymlfile+='          - [rdfs:seeAlso, $(source)]\n'
        ymlfile+='  agent:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile3+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(agent)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, prov:Agent]\n'
        ymlfile+='          - [foaf:givenName, $(agent)]\n'
        ymlfile+='          - [foaf:mbox, $(emailagent)]\n'
        ymlfile+='  exp_ev:\n'
        ymlfile+='      sources:\n'
        ymlfile+='          - ["'+csvfile3+'"]\n'
        ymlfile+='      s: https://eaontology.linkeddata.es/def/eao#$(ethical_issue)\n'
        ymlfile+='      po:\n'
        ymlfile+='          - [a, eao:ExpectationEvaluation]\n'
        ymlfile+='          - [eao:description, $(ethical_issue)]\n'
        



    #print(ymlfile)
    for line in ymlfile:
        yfile.write(line)

    return(ymlfile)

'''
csvfile='/Users/krnlet/Desktop/wizard/templates/results/results1.csv~csv'
ymlfile_1(csvfile)
csvfile2='/Users/krnlet/Desktop/wizard/templates/results/results1.csv~csv'
ymlfile_2(csvfile2)
csvfile3='/Users/krnlet/Desktop/wizard/templates/results/results2.csv~csv'
ymlfile_3(csvfile3)
'''