import sentry_sdk
import json
from flask import Flask, request, render_template,redirect,abort
from flask_cors import CORS
import getaudio as ga
import time
"""
pip install sentry_sdk flask flask_cors
"""


your_url="http://127.0.0.1"#改为你的域名或者ip

sentry_sdk.init(
    dsn="https://3914502367488b8603d657216f5dadb2@o4507525750521856.ingest.us.sentry.io/4507525753208832",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)#sentry sdk

app = Flask(__name__)

@app.route("/getaudio", methods=['GET'])
def getaudio():
    """
    text:文本
    name:模型代号
    
    """
    m=[
      ['models/paimon6k.json', 'models/paimon6k_390k.pth', 'character_paimon', 1],
      ['models/yunfeimix2.json', 'models/yunfeimix2_53k.pth', 'character_yunfei', 1.1],
      ['models/catmix.json', 'models/catmix_107k.pth', 'character_catmaid', 1.2]
    ]
    
    text = request.args.get('text')
    name = request.args.get('name')
    s = request.args.get('s')
    if name==None:name=0
            
    if int(name)>9 or int(name)<0:return {"ok":False,"code":201,"msg":"模型编号错误，name参数应该填0到3的数字"}
    if text==None:return {"ok":False,"code":202,"msg":"请填写text(文本)参数，该值不能为空"}
    
    t=time.time()
    p=f"C:\\inetpub\\wwwroot\\{t}.wav"#改为你的域名/ip对应的物理地址(网站目录)
    ga.generateAudio(text,p,m=m[int(name)])
    
    return {"ok":True,"url":your_url+'/'+str(t)+'.wav',"msg":""}
    
CORS(app)#跨域

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)