# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import FaxService, PopbillException

faxService = FaxService(testValue.LinkID,testValue.SecretKey)
faxService.IsTest = testValue.IsTest

try:
    print("팩스 전송내역 조회 URL 확인")
    TOGO = "BOX" # 팩스 전송내역 URL 지정문자
    url = faxService.getURL(testValue.testCorpNum, testValue.testUserID, TOGO)
    print("BOX URL : " +url)
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))