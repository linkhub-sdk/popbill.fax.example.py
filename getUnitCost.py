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
    print("팩스 전송 단가 확인")

    unitCost = faxService.getUnitCost(testValue.testCorpNum)

    print("단가: %f" % unitCost)
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))