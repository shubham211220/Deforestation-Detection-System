 
 
import numpy as np
from keras.models import load_model
#from keras.preprocessing import image
import keras.utils as image
import cv2
import collections
import datetime
import operator
from gtts import gTTS
import os
from utils import GreenEstimator
from utils import LocationFetcher
from utils import WASender
# import WhatsAPPSender

def initDetection(mobilenumber):
    
    
    mymodel=load_model('../../models/deforestation_trained_data.h5')

    
    
    cap=cv2.VideoCapture(1)
    
    x=200
    y=50
    h=380
    w=220
    resultlist=[]
    while cap.isOpened():
        _,img=cap.read()
     
        cr_img = img[y:y+h, x:x+w]
        dim = (150, 150)
        cr_img = cv2.resize(cr_img, dim, interpolation = cv2.INTER_AREA)
        
        
        cv2.imwrite('../../temp/temp.jpg',cr_img)
        defpercantage=GreenEstimator.getGreenPercentage('../../temp/temp.jpg')
        print('defpercantage ',defpercantage)
        if(defpercantage<97):
                           
            test_image=image.load_img('../../temp/temp.jpg',target_size=(150,150,3))
            
            test_image=image.img_to_array(test_image)
            test_image=np.expand_dims(test_image,axis=0)
            pred=mymodel.predict(test_image)[0][0]
            resultyype=""
            percentstr=str(defpercantage)
            
            print("Prediction number ",pred)
            if pred==1:
                
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                cv2.putText(img,'Forestation',((x+w)//2,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
                resultyype="Forestation"
            else:
                resultstr='De-Forestation with '+percentstr+" %"
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
               # cv2.putText(img,resultstr,((x+w)//2,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                cv2.putText(img,resultstr,((x+0)//2,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
                resultyype="De-Forestation"
                  
            cv2.imshow('DEFORESTATION DETECTION SYSTEM',img)
            
            resultlist.append(resultyype)
            frequency = collections.Counter(resultlist)
            cropfreq=dict(frequency)
            sorted_d = sorted(cropfreq.items(), key=operator.itemgetter(1))
           # print('Dictionary in ascending order by value : ',sorted_d)
            index=len(sorted_d)-1
            mxvaluecrop=sorted_d[index] 
            
            print("Matched ",mxvaluecrop)
            typename=mxvaluecrop[0]
            typecount=mxvaluecrop[1]
            print("typename ",typename)
            print("typecount ",typecount)
            count=int(typecount) 
            
            if(count>=150):
                if(typename=='De-Forestation'):
                    print("Deforestation Detected")
                    msg=LocationFetcher.getLocationMsg(defpercantage)
                    WASender.sendImage(mobilenumber, "../../temp/temp.jpg", msg)
                    resultlist.clear()
                    break
                    
                   # language = 'en'
                    # voicetext= "DE FORESTATION IS DETECTED"
                    # myobj = gTTS(text=voicetext, lang=language, slow=False)
                    # myobj.save("say.mp3")
                    # os.system("say.mp3")
                    
                
              
                
        else:
           # print("whhhhhh")
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
            cv2.putText(img,'NO FOREST AREA',((x+w)//2,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
            cv2.imshow('DEFORESTATION DETECTION SYSTEM',img)
            
            
        
        if cv2.waitKey(1)==ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    initDetection()        