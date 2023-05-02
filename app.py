from distutils.log import error
from pyexpat import model
from flask import Flask, redirect, render_template,request
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open('car.pkl','rb'))

@app.route('/',methods=['post','get'])
def index():
    list1 = ['alfa-romero', 'audi', 'bmw', 'chevrolet', 'dodge', 'honda',
       'isuzu', 'jaguar', 'mazda', 'mercedes-benz', 'mercury',
       'mitsubishi', 'nissan', 'peugot', 'plymouth', 'porsche', 'renault',
       'saab', 'subaru', 'toyota', 'volkswagen', 'volvo']
    list2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    error1=''

    if request.method=='POST':
        try:
             horsePower =  float(request.form['one'])
             curb_weight = float(request.form['Two'])
             highway_mpg = float(request.form['Three'])
             Engine_size = float(request.form['four'])
             wheel_base= float(request.form['seven'])
             bore = float(request.form['eight'])
             city_mpg = int(request.form['ten'])
        

             if(request.form['five']=='rear'):
                 engine_location = 1
             else:
                 engine_location = 0
             j=0
             for i in list1:
                 j+=1
                 if(request.form['six']==i):
                     make = j-1
        
       
        
             if((request.form['nine'])=='yes'):
                  diesel = 1
             else:
                 diesel = 0
        
        
             input = np.array((horsePower,curb_weight,highway_mpg,Engine_size,engine_location,make,wheel_base,bore,diesel,city_mpg)).reshape(1,-1)
             print(input)
             output = model.predict(input)
             output1=output[0]
             output2 = 80*output1[0]
             print(output2)

            #  if((horsePower<48 or horsePower>205) or (curb_weight<1488 or curb_weight>4000) or (highway_mpg<16 or highway_mpg>54) or (Engine_size<75 or Engine_size>300) or (wheel_base<87 or wheel_base>121) or (bore<2.54 or bore>3.32) or (city_mpg<14 or city_mpg>49) or (make in list2 ) or (engine_location!=0 or engine_location!=1) or (diesel!=0 or diesel!=1)):
            #      error1='ERROR ! \n (Please follow the instructions)'
            #  else:
            #      error1=''
        except:
            print('some erro')
            error2='ERROR ! \n (Please follow the instructions)'
            return render_template('index.html',error=error2)
        print(error1)
        return render_template('index.html',output=int(output2),error=error1)
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)