# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import FaxService,PopbillException

faxService =  FaxService(testValue.LinkID,testValue.SecretKey)
faxService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 과금정보 확인 " + "=" * 15)

    ''' ChargeInfo 구성
                unitCost        (단가)
                chargeMethod    (과금유형)
                rateSystem      (과금제도)
    '''

    response = faxService.getChargeInfo(testValue.testCorpNum, testValue.testUserID)

    tmp = "unitCost (단가) : " + response.unitCost + "\n"
    tmp += "chargeMethod (과금유형) : " + response.chargeMethod + "\n"
    tmp += "rateSystem (과금제도) : " + response.rateSystem
    print(tmp);

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
