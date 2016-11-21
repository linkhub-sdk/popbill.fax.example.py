# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import FaxService, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest

'''
팩스 전송요청시 반환받은 접수번호(receiptNum)을 사용하여 팩스전송
결과를 확인합니다.
'''

try:
    print("=" * 15 + " 팩스전송 내역 및 전송상태 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팩스전송 요청시 반환받은 접수번호
    receiptNum = "016080910592000001"

    resultList = faxService.getFaxResult(CorpNum, receiptNum)

    i = 1
    for f in resultList:
        print("FaxResult[%d] : " % i)
        print("    sendState : %s" % f.sendState)
        print("    convState : %s" % f.convState)
        print("    sendNum : %s" % f.sendNum)
        print("    senderName : %s" % f.senderName)
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
