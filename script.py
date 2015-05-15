#author : ashish belwase & sagar duwal| web : www.geeknepal.com

import requests
import re

class website(object):

    def __init__(self,username,password,title,desc,cat,tag,vfile):
        self.username = username
        self.password = password

        self.upload_submit = ''
        self.upload_id = ''
        self.title = title
        self.desc = desc
        self.cat = cat
        self.tag = tag
        self.vfile = vfile
        
        self.lurl = 'http://websitez69.com/ajax.php?s=user_login'
        self.upurl = 'http://websitez69.com/ajax.php?s=video_upload'
        self.purl = 'http://websitez69.com/upload/'
        
        self.ldata = {'username':self.username,
                      'password':self.password,
                      'loginRedirect':'http://websitez69.com/upload/'
                      }

        self.udata = {'upload-submitted':self.upload_submit,
                      'unique_id':self.upload_id,
                      'title':self.title,
                      'description':self.desc,
                      'category':self.cat,
                      'tags':self.tag
                      }
                      
        self.files = {'file': open(self.vfile, 'rb')}
        self.uploadEnabled = False
        self.s = requests.Session()

    
    
    def login(self):
        self.reply = self.s.post(self.lurl, data=self.ldata)
        
        if 'Login successful!' in self.reply.text:
            print 'You are now Logged in...'
            self.uploadEnabled  = True
        else:
            print "Authentication failed."
            self.uploadEnabled = False
    
    def getUploadId(self, pageText):
         for line in pageText.splitlines():
            
            if 'upload-submitted' in line:  
                number = line.split(" ")[3]
                self.upload_submit = re.split('\"', number)[1]
                
            if 'unique_id' in line:  
                number = line.split(" ")[3]
                self.upload_id = re.split('\"', number)[1]
                   
                
    def upload(self):
        if(self.uploadEnabled):
            self.page = self.s.get(self.purl) 
            self.getUploadId(self.page.text)
                    
            #Now uploading
            print("Uploading.......")
            v = self.s.post('http://websitez69.com/ajax.php?s=video_upload&id='+self.upload_id,data=self.udata,files=self.files)
            
            #print(v.text)
            print("-----------------------------")
            print ("Upload success")
        else:
            print ("Upload Failed")

if __name__ == '__main__':
    website = website('username','password','Dangerous video','desc','danger','Danger','test.mp4')
    website.login()
    
    website.upload()
    
