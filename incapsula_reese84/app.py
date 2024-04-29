from flask import Flask, request,jsonify,render_template_string,g,render_template
import json
import re
import os

app = Flask(__name__)
log_path = os.path.join(os.getcwd(), "static\\json")
if not os.path.exists(log_path):
    os.mkdir(log_path)

@app.route("/index", methods=['GET'])
def index():
    path = os.path.join(os.getcwd(), "html\\reese.html")
    try:
        return render_template("./html/reese.html")
    except:
        return render_template_string(open(path, "r", encoding='utf-8').read())
@app.route("/sm_reese84",methods=['GET'])
def get_reese():
    while True:
        try:
                data=open(log_path + '/data.txt', 'r').read()
                data_=open(log_path + '/data.json', 'r').read()
                if re.search("p",str(data)):
                    if len(data_)<=0:
                        with open(log_path + '/data.json', 'w') as f:
                            f.write(data)
                        return jsonify({"code":0,"data":data})
                    else:
                        if str(data_) in str(data):
                            continue
                        else:
                            with open(log_path + '/data.json', 'w') as f:
                                f.write(data)
                            return jsonify({"code": 0, "data": data})
                else:
                    continue
        except Exception as e:
            continue
@app.route("/sm_update_seese84", methods=["POST"])
def get_update_seese84():
    data= request.values.get("data")
    with open(log_path + '/data.txt', 'w') as f:
        f.write(data)
    return jsonify({"code": 0})

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='12184',debug=False)