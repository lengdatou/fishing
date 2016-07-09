#coding:utf-8
'''
Created on 2016年3月2日

@author: lengwei
'''

import json
import os





#===============================================================================
# if __name__ == "__main__":
#     fishs=json.load(file('fish.json'), 'utf-8')
#     fishid={}
#     for f in fishs:
#         fishid[str(f['id'])]=0
#         
#     fishrefresh=json.load(file('refresh5.json'), 'utf-8')
#     for ref in fishrefresh:
#         reftimes=3600/ref["interval"]
#         randall=0
#         for item in ref['items']:
#             randall=randall+item['rand']
#         for item in ref['items']:
#             if item['type']=='single':
#                 fishid[str(item['fishid'])]=fishid[str(item['fishid'])]+item['rand']*reftimes/randall
# 
#     
#     for i in fishid.keys():
#         print i,fishid[i]
#===============================================================================
    
#===============================================================================
# if __name__ == "__main__":
#     goods=json.load(file('otherjson\\trade.json'), 'utf-8')
#     evegood = goods['common2']
#     for f in evegood:
#         #print 'goodsId is',f['goodsId']
#         a=(f['cv']/5)/f['money']
#         b=(f['cvpool']/5)/f['money']
#         if a==300 and b==30:
#             print f['vis'],'||||',f['name'],f['money'],a,b,'OK'
#         else:
#             print 'error!!!!',f['vis'],'||||',f['name'],f['money'],a,b
#         print '------------------------------------'
#     raw_input()
#===============================================================================
 
partner  =  0
jsonname = 'goods'


def getfiles(vname):
    allfiles=os.listdir('otherjson')
    tempfiles=[]
    for i in range(len(allfiles)):
        if allfiles[i].endswith(vname+'.json')==True:
                tempfiles.append(allfiles[i])
    return tempfiles
 
def checkgoods(vjsonname):
    goods=json.load(file('otherjson\\'+vjsonname), 'utf-8')
    paytypelist=json.load(file('paytypelist.json'), 'utf-8')
    vpartner=vjsonname.split('-')[0]
    if vpartner==vjsonname or vpartner=='11':
        cvrate=300
        cvpoolrate=30
        vpartner=11 
    else:
        cvrate=150
        cvpoolrate=15
    if vjsonname.endswith('goods.json')==True:
        evegood = goods['goods']  
    else:
        evegood = goods['common2']
    countright=0
    countwrong=0
    for f in evegood:
        #print 'goodsId is',f['goodsId']
        for pp in f['']
        a=(f['cv']/5)/f['money']
        b=(f['cvpool']/5)/f['money']          
        if a==cvrate and b==cvpoolrate and (f['id']/1000-int(vpartner))==1000:
            print f['id'],'||||',f['vis'],'||||',f['name'],f['money'],a,b,'OK'
            countright+=1
        else:
            print f['id'],'||||',f['vis'],'||||',f['name'],f['money'],a,b,'error!!!!'
            countwrong+=1
        print '------------------------------------'
    print "right : ",countright,", wrong : ",countwrong
    if countwrong>0:
        return vpartner,False
    else:
        return vpartner,True

            
def updateactions():
    filename='actions'
    allfiles=os.listdir('otherjson')
    tempfiles=[]
    for i in range(len(allfiles)):
        if allfiles[i].endswith(filename+'.json')==True:
                tempfiles.append(allfiles[i])
    for j in tempfiles:
        actionfile=json.load(file('otherjson\\'+j), 'utf-8')


if __name__ == "__main__":
    wrongfiles=[]
    handlefilenames=getfiles('goods')
    for vf in handlefilenames:
        checkresult=eval('checkgoods')(vf)
        if checkresult[1]==False:
            wrongfiles.append(checkresult[0])
    print wrongfiles


    
                
   
