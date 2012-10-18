# -*- coding: gb2312 -*-

import time
from cPAMIE import PAMIE
from sgmllib import SGMLParser

NUM_DICT = {}
HOSPITAL = {'bjkq':[]}
GUAHAO_HAO = 'http://www.bjguahao.gov.cn/comm/%s/ksyy.php'
GUAHAO_URL = 'http://www.bjguahao.gov.cn/comm/index.php'
GUAHAO_KOUQIANG = GUAHAO_HAO % 'kouqiang'
TO_MAILS = ['v-chuans@microsoft.com','act.of.war.sunzi@hotmail.com','bessie.yan@thomsonreuters.com']

class test:
    def test2(self):
        import win32com.client
        self._ie = win32com.client.DispatchEx('InternetExplorer.Application')
        self._ie.Visible = 1
        self._ie.Navigate('www.baidu.com')
        time.sleep(5)
        print self._ie.Document.forms[0].getElementsByTagName("wd").length
        

    def test1(self):
        self.ie = PAMIE()
        #self.ie = getIE ()
        #self.ie.navigate('http://www.bjguahao.gov.cn/comm/kouqiang/ksyy.php?ksid=1040000&hpid=109')
        #self.ie.textBoxGet('yy')
        #self.ie.linkExists('dd')        
        self.ie.navigate('www.baidu.com')
        self.ie.textBoxSet('wd','Computer')
        #self._ie.Document.getElementById("kw").value ="Computer"
        #self.ie.Document.getElementById("su").click()


def LoginPage():
    '''
    login in the web page with username pwd and code
    '''
    ie = PAMIE()
    ie.navigate("http://www.bjguahao.gov.cn/comm/yyks.php?hpid=109") 
    #time.sleep(10)
    #return ie
    ie.textBoxSet('truename','王三')
    ie.textBoxSet('sfzhm', '身份证号')
    Downloadcode(ie.cookieGet())
    ie.textBoxSet('yzm',GetCode(CodeFilter()))
    #time.sleep(15)
    ie.formSubmit('form1') 
    if ie.textBoxExists('truename'):
        print 'fail to login in, please true again'
        return None    
    #ie.navigate('http://www.bjguahao.gov.cn/comm/kouqiang/ksyy.php?ksid=1040000&hpid=109')
    #print ie.pageGetText()
    #ie.javaScriptExecute(SetDocumentMode())
    #ie.javaScriptExecute('document.documentMode="7";')
    #ie.javaScriptExecute('document.write(document.getElementsByTagName("head"))')
    #ie.javaScriptExecute('document.getElementsByTagName(\'head\')[0].appendChild(\'<meta http-equiv="X-UA-Compatible" content="IE=7">\');')
    return ie


def GetRegisterInfo(ie,Ikeshi,Ihospital,registerCount=1,startDate=None, endDate=None, isExpert=True):
    '''
    get the register info.
    Ikeshi means keshi id,
    Ihospital means hospital id,
    registerCount means to want to register count which must fit to hospital policy
    startDate type is string, means the date want to preregister, include that day.
    endDate type is string, means the date is last date, include the day.
    the date form is '2012-07-06'
    the litter default is that you must change the IE9 document mode
    '''
    hos = '?ksid=%d&hpid=%d'
    dclick = '&wday=%d&sx=%d'
    url = GUAHAO_KOUQIANG + hos %(Ikeshi,Ihospital) +dclick
    #print 'url is:', url    
    # the times we have re-register
    iCount = 0
    for i in range(1,14):
        for j in range(0,7):
            #i=2
            #j=5
            # the count of that day we can re-register
            item = 0
            # index which can register 
            RIndex = []                        
            #print 'url is:', url %(i,j)
            ie.navigate(url %(i,j))
            time.sleep(5)            
            # find the info table
            tables = ie.tablesGet('bgColor=#b8d9f5')
            table = tables[0]
            myDataList = []
            myData = ''
            lastIndex = -1
            for cell in table.cells:
                if cell.cellIndex <= lastIndex:
                    myDataList.append(myData)
                    myData = ''
                myData += (cell.innerText + "\t")
                lastIndex = cell.cellIndex
            myDataList.append(myData)            
            #print '\n'.join( myDataList)
            # date range judgement TODO
            
            for m in range(len(myDataList)):
                #print myDataList[m].encode('gb2312')
                #print myDataList[m].encode('gb2312').find(u'预约挂号'.encode('gb2312'))
                if myDataList[m].encode('gb2312').find(u'预约挂号'.encode('gb2312'))>0:
                    if isExpert :
                        if myDataList[m].encode('gb2312').find(u'普通门诊'.encode('gb2312'))<0:                        
                            RIndex.append(item)
                            print '-------',myDataList[m]
                    else:
                        RIndex.append(item)
                        print '------',myDataList[m]
                    item += 1            
            #print 'start to find the link control'
            ## if ie.linkExists(u'预约挂号'):
            ##     links = ie.linksGet(u'预约挂号')
            ##     for li in RIndex:
            ##         if iCount <registerCount:
            ##             print 'the %dth sucessful' %li
            ##             #if ie.elementClick(links[li]):
            ##             #    print 'the %dth sucessful' %li
            ##             # TODO deal with pop widowns
            ##             iCount += 1
            ##         else:
            ##             break
                


def GetRegisterInfo2(ie, Ikeshi, Ihospital,startDate=None, endDate=None, isExpert=True):
    '''
    startDate, endDate form is yyyy-MM-dd
    '''
    import urllib2, codecs, datetime, time
    data = []    
    hos = '?ksid=%d&hpid=%d'
    dclick = '&wday=%d&sx=%d'    
    url = GUAHAO_KOUQIANG + hos %(Ikeshi,Ihospital) +dclick
    sDate = None
    if startDate!=None:
        sDate_temp = time.strptime(startDate, '%Y-%m-%d')
        sDate = datetime.date(sDate_temp.tm_year, sDate_temp.tm_mon, sDate_temp.tm_mday)
    eDate = None
    if endDate!=None:
        eDate_temp = time.strptime(endDate, '%Y-%m-%d')
        eDate = datetime.date(eDate_temp.tm_year, eDate_temp.tm_mon, eDate_temp.tm_mday)
    today = datetime.date.today()
    
    for i in range(1,14):
        for j in range(0,7):
            #d=datetime.timedelta(weeks=i-1, days=j)
            d = (i-1) * 7 + j
            #print today,'\t',d, '\t', sDate, '\t', eDate            
            if sDate!=None and (sDate-today).days>d+1:
                continue

            if eDate!=None and (eDate-today).days<d+1:
                continue
                
            print url %(i,j)            
            req = urllib2.Request(url %(i,j))
            req.add_header("Cookie", ie.cookieGet())
            req.add_header("Referer", GUAHAO_URL)
            req.add_header("User-agent",'Mozilla/5.0')
            res_info = urllib2.urlopen(req)
            Reader = codecs.getreader("gb2312")
            fh = Reader(res_info)            
            result = GetInfo()
            result.feed(fh.read())
            result.close()
            info = result.output()
            ##print info.encode('gb2312')
            #dd = ''.join(info)
            print len(info)
            for li in info:
                #print li[3],'\t', li[8]
                if (isExpert and  \
                   li[3].encode('gb2312').find(u'普通门诊'.encode('gb2312'))<0 and \
                   li[8].encode('gb2312').find(u'预约挂号'.encode('gb2312')) >= 0) or \
                   (not isExpert and \
                   li[8].encode('gb2312').find(u'预约挂号'.encode('gb2312')) >= 0): 
                        data.append('\t'.join(li))
                        #print 'in'
    #print '\n'.join(data)
    if len(data)==0:
        ie.quit()
        return
    body = '\n'.join(data)
    print body
    SendMail(body.encode('gb2312'), 'hospital register info[%s--%s]' %(startDate, endDate))
    ie.quit()
    



def Downloadcode(cookie,savefile='code.gif',url=r'http://www.bjguahao.gov.cn/comm/code.php'):
    '''
    download code image from url
    '''
    import urllib2
    req = urllib2.Request(url)
    req.add_header("Cookie", cookie)
    req.add_header("Referer", GUAHAO_URL)
    res_img = urllib2.urlopen(req)
    f = open(savefile, 'wb')
    f.write(res_img.read())
    f.close()


def CodeFilter(fromfile='code.gif', tofile='code_temp.png'):
    '''
    pre-process the image.
    '''
    import Image,ImageEnhance,ImageFilter, ImageDraw
    import sys
    #image_name = "D:\\SUN\\HOME\\python\\guahao\\code.gif"
    image_name = 'code.gif'
    #image_name = "D:\\SUN\\HOME\\python\\guahao\\code.png"
    im = Image.open(image_name)
    #print im.format, im.size, im.mode
    #im.show()
    #print im.info
    #print im.palette
    im_new = im.convert('L')
    #im_new.show()
    #im_new.save('dd.png')
    # 删除边框
    draw = ImageDraw.Draw(im_new)
    draw.line((0, 0, im.size[0], 0), fill=255)
    draw.line((0, 0, 0, im.size[1]), fill=255)
    draw.line((0, im.size[1]-1, im.size[0], im.size[1]-1), fill=255)
    draw.line((im.size[0]-1, 0, im.size[0]-1, im.size[1]-1), fill=255)
    enhancer = ImageEnhance.Brightness(im_new)
    im_new = enhancer.enhance(2.0) #加亮，效果见图1
    enhancer = ImageEnhance.Contrast(im_new)
    im_new = enhancer.enhance(4) #提高对比度，效果见图2
    im_new.convert('1')
    im_new.filter(ImageFilter.MedianFilter)
    im_new.save(tofile)
    return im_new


def TrainCode(im, sname='code.txt'):
    '''
    train the data
    '''
    fh = open(sname,'a')
    for img in GetFourNumImage(im):
        fh.write(ImageToString(img)+'\n')
    fh.close()


def GetCode(im):
    '''
    get the four code numbers.
    '''
    retVal = ''
    LoadCodeFromTrain()
    for img in GetFourNumImage(im):
        retVal += NUM_DICT[ImageToString(img)]
    return retVal

    
def GetFourNumImage(im):
    fstNum = im.crop((5,4,11,12))
    fstNum.save('fstnum.png')
    sedNum = im.crop((12,4,18,12))
    sedNum.save('sednum.png')
    thrNum = im.crop((19,4,25,12))
    thrNum.save('thrnum.png')
    forNum = im.crop((26,4,32,12))
    forNum.save('fornum.png')
    return [fstNum,sedNum,thrNum,forNum]


def ImageToString(img):
    '''
    convert image to string with "0" and "1"
    '''
    im = img.load()
    nstr = ''
    for x in xrange(6): #生成目标图像的特征字符串
        for y in xrange(6):
            if im[x, y] == 255:
                nstr += '0'
            else:
                nstr += '1'
    return nstr


def LoadCodeFromTrain(fName='code.txt'):
    with open(fName) as f:
        for line in f:
            (key, val) = line.split()
            NUM_DICT[key] = val


def SendMail(data,subject):
    import smtplib
    from email.MIMEText import MIMEText
    fromaddr = 'sc369963@gmail.com'  
    toaddrs  = TO_MAILS

    msg = MIMEText(data, 'plain','gb2312')
    msg['Subject'] = subject
    msg['From'] = fromaddr
    msg['To'] = ";".join(toaddrs)
    #msg = 'There was a terrible error that occured and I wanted you to know!'  
  
  
    # Credentials (if needed)  
    username = 'sc369963@gmail.com'  
    password = 'sc369963'  
    
    # The actual mail send  
    server = smtplib.SMTP('smtp.gmail.com:587')  
    server.starttls()  
    server.login(username,password)  
    server.sendmail(fromaddr, toaddrs, msg.as_string())  
    server.quit()


def SetDocumentMode():
    code = '''
    engine = null;
    if (window.navigator.appName == "Microsoft Internet Explorer")
    {
        // This is an IE browser. What mode is the engine in?
        if (document.documentMode) // IE8 or later
        {
          engine = document.documentMode;
          document.documentMode = 7;
        }
        else // IE 5-7
        {  
           engine = 5; // Assume quirks mode unless proven otherwise
           if (document.compatMode)
           {
             if (document.compatMode == "CSS1Compat")
             engine = 7; // standards mode
           }
           // There is no test for IE6 standards mode because that mode  
           // was replaced by IE7 standards mode; there is no emulation.
           document.documentMode = 7;
        }
        // the engine variable now contains the document compatibility mode.        
    }
    '''
    code2 = '''
    document.getElementsByTagName(\'head\')[0].appendChild(\'<meta http-equiv="X-UA-Compatible" content="IE=7">\');
    '''
    return code2;


class GetInfo(SGMLParser):
            
    def reset(self):
        self._totalResult = []        
        self._pieces = []
        self._url = ''
        self._inTag_table = False
        self._inLabel = False
        SGMLParser.reset(self)

    def start_table(self, attrs):        
        for k, v in attrs:
            #print k, v
            if k=='bgcolor' and v=='#B8D9F5':
                self._inTag_table = True
                break

    def end_table(self):
        if self._inTag_table:
            self._inTag_table = False

    def start_tr(self, attrs):
        if self._inTag_table:
            self._inLabel = True
            

    def end_tr(self):
        if self._inLabel:
            self._inLabel = False
            self._totalResult.append(self._pieces)
            self._pieces = []
            

    def handle_data(self, text):           
        if self._inLabel and self._inTag_table:            
            #self._pieces.append(text.encode('gb2312'))
            self._pieces.append(text)
            #print text


    def output(self):              
        """Return processed HTML as a single string"""
        #return self._totalResult
        return self._totalResult



if __name__=='__main__':
    #t = test()
    #t.test1() 
    #Downloadcode()    
    #print GetCode(CodeFilter())
    #TrainCode(CodeFilter())

    ie = LoginPage()
    if ie==None:
        ie = LoginPage()
    if ie==None:
        print 'fail to login'    
    #yazhou beijingkouqiang
    #GetRegisterInfo(ie, Ikeshi=1030200,Ihospital=109)
    #GetRegisterInfo(ie, Ikeshi=1040000,Ihospital=109, isExpert=False)
    #GetRegisterInfo2(ie, Ikeshi=1040000,Ihospital=109,startDate='2012-9-24', endDate='2012-10-24', isExpert=False)
    GetRegisterInfo2(ie, Ikeshi=1040000,Ihospital=109,isExpert=True)
    #SendMail('shifei')
    #t = test()
    #t.test1()
   
    #ie.navigate('http://www.bjguahao.gov.cn/comm/kouqiang/ksyy.php?ksid=1040000&hpid=109')
    #t = test()
    #t.test2()       


