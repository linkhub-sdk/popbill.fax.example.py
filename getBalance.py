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
    print("회원 잔여포인트 확인")

    balance = faxService.getBalance(testValue.testCorpNum)

    print("회원잔액 : %f" % balance)
    
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))