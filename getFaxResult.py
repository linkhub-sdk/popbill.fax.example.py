# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import FaxService, PopbillException

faxService =  FaxService(testValue.LinkID,testValue.SecretKey)
faxService.IsTest = testValue.IsTest
  
try:
    print("팩스전송 내역 및 전송상태 확인")
    
    receiptNum = "015032710514400001" # 팩스전송 요청시 반환받은 접수번호
    resultList = faxService.getFaxResult(testValue.testCorpNum, receiptNum)
    
    #전송결과 항목에 대한 자세한 사항은 "팩스 API 연동매뉴얼 > [3.3.1. 전송내역 및 전송상태 상태확인] 참조
    
    i = 1
    for f in resultList:
        print("FaxResult[%d] : " % i)
        print("    sendState : %s" % f.sendState)
        print("    convState : %s" % f.convState)
        print("    sendNum : %s" % f.sendNum)
        print("    receiveNum : %s" % f.receiveNum)
        print("    receiveName : %s" % f.receiveName)
        print("    sendPageCnt : %s" % f.sendPageCnt)
        print("    successPageCnt : %s" % f.successPageCnt)
        print("    failPageCnt : %s" % f.failPageCnt)
        print("    refundPageCnt : %s" % f.refundPageCnt)
        print("    cancelPageCnt : %s" % f.cancelPageCnt)
        print("    reserveDT : %s" % f.reserveDT)
        print("    sendDT : %s" % f.sendDT)
        print("    resultDT : %s" % f.resultDT)
        print("    sendResult : %s" % f.sendResult)
        i += 1
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
