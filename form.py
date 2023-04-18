# importing Flask and other modules
from flask import Flask, request, render_template
import csv
import subprocess
from create_yml import ymlfile_1, ymlfile_2, ymlfile_3
# Flask constructor
app = Flask(__name__, static_folder='/Users/krnlet/Desktop/wizard')

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    file=open("results.csv", "a")
    writer=csv.writer(file)
    file1=open("results1.csv", "a")
    writer1=csv.writer(file1)
    file2=open("results2.csv", "a") 
    writer2=csv.writer(file2)
        

    if request.method == "POST":
            name = request.form.get("name")
            if(request.form.get("version")!='other'):
                version = request.form.get("version")
            else:
                version = request.form.get("version_other")

            if(request.form.get("purpose")!='other'):
                purpose = request.form.get("purpose")
            else:
                purpose = request.form.get("purpose_other")

            
            if(request.form.get("techniques")!='other'):
                techniques=request.form.get("techniques")
            else:
                techniques=request.form.get("techniques_other")

            if(request.form.get("task_tech")!='other'):
                task=request.form.get("task_tech")
            else:
                task=request.form.get("tt_other")

            if(request.form.get("features")!='other'):
                features=request.form.get("features")
            else:
                features=request.form.get("features_other")

            if(request.form.get("users")!='other'):
                users=request.form.get("users")
            else:
                users=request.form.get("users_other")
            
            tl=request.form.get("tl")
            al=request.form.get("al")
            appl=request.form.get("appl")
            fores=request.form.get("fores")
            issues=request.form.get("issue")
            benefits=request.form.get("benefits")
            negatives=request.form.get("negative")
            
            tf=request.form.get("tf")
            su=request.form.get("su")
            d=request.form.get("de")
            expectation=request.form.get("expectation")
            evidence=request.form.get("evidence")
            source=request.form.get("source")
            agent=request.form.get("agent")
            emailagent=request.form.get("emailagent")
            issues2=request.form.get("issue2")
            

            
            if(name):
                writer.writerow([name, version,purpose,techniques, task, features, users])
                
            elif(tl):
                writer1.writerow([tl,al,appl,fores,issues,benefits,negatives])
            elif(tf):    
                writer2.writerow([tf,su,d,expectation,evidence,source,agent,emailagent,issues2])
                #return "Your name is "+name + version
    return render_template("form.html")



    

# which URL is associated function
@app.route('/finish', methods =["GET", "POST"])
def instances():
    csvfile='/Users/krnlet/Desktop/wizard/results.csv~csv'    
    yml=ymlfile_1(csvfile)
    print('----------')
    generate=subprocess.Popen(['python3','-m', 'yatter', '-i','/Users/krnlet/Desktop/wizard/templates/results/file_yml_1.yml', '-o', 'templates/results/technology.ttl'])
    print('finish1')    
    generate2=subprocess.Popen(['java', '-jar', '/Users/krnlet/Desktop/wizard/templates/results/rmlmapper-6.1.3-r367-all.jar', '-m', '/Users/krnlet/Desktop/wizard/templates/results/technology.ttl', '-o', '/Users/krnlet/Desktop/wizard/templates/results/triplets1.nt'])
    exit_codes = [p.wait() for p in (generate, generate2)]
    print('finish2')    

    triplets_file=open('/Users/krnlet/Desktop/wizard/templates/results/triplets1.nt', 'r')
    triplets_file_read=triplets_file.readlines()
    triplets=str()
    for i in triplets_file_read:
        triplets+=i
    return render_template("triplets.html")   
            
# which URL is associated function
@app.route('/finish2', methods =["GET", "POST"])
def instances2():
    csvfile='/Users/krnlet/Desktop/wizard/results1.csv~csv'    
    
    yml=ymlfile_2(csvfile)
    print(yml)
    generate=subprocess.Popen(['python3','-m', 'yatter', '-i', '/Users/krnlet/Desktop/wizard/templates/results/file_yml_2.yml', '-o', 'templates/results/levels.ttl'])
    print('finish1')    
    generate2=subprocess.Popen(['java', '-jar', '/Users/krnlet/Desktop/wizard/templates/results/rmlmapper-6.1.3-r367-all.jar', '-m', '/Users/krnlet/Desktop/wizard/templates/results/levels.ttl', '-o', '/Users/krnlet/Desktop/wizard/templates/results/triplets2.nt'])
    exit_codes = [p.wait() for p in (generate, generate2)]
    print('finish2')    

    triplets_file=open('/Users/krnlet/Desktop/wizard/templates/results/triplets2.nt', 'r')
    triplets_file_read=triplets_file.readlines()
    triplets=str()
    for i in triplets_file_read:
        triplets+=i
        print(triplets)
    return render_template("triplets2.html")   

# which URL is associated function
@app.route('/finish3', methods =["GET", "POST"])
def instances3():
    csvfile='/Users/krnlet/Desktop/wizard/results2.csv~csv'    
    
    yml=ymlfile_3(csvfile)
    print(yml)
    generate=subprocess.Popen(['python3','-m', 'yatter', '-i', '/Users/krnlet/Desktop/wizard/templates/results/file_yml_3.yml', '-o', 'templates/results/expectations.ttl'])
    print('finish1')    
    generate2=subprocess.Popen(['java', '-jar', '/Users/krnlet/Desktop/wizard/templates/results/rmlmapper-6.1.3-r367-all.jar', '-m', '/Users/krnlet/Desktop/wizard/templates/results/expectations.ttl', '-o', '/Users/krnlet/Desktop/wizard/templates/results/triplets3.nt'])
    exit_codes = [p.wait() for p in (generate, generate2)]
    print('finish2')    

    triplets_file=open('/Users/krnlet/Desktop/wizard/templates/results/triplets3.nt', 'r')
    triplets_file_read=triplets_file.readlines()
    triplets=str()
    for i in triplets_file_read:
        triplets+=i
        print(triplets)
    return render_template("triplets3.html")   


if __name__=='__main__':
    app.run()

