# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import CorpInfo, FaxService, PopbillException

faxService =  FaxService(testValue.LinkID,testValue.SecretKey)
faxService.IsTest = testValue.IsTest

corpInfo = CorpInfo (
                ceoname = "대표자성명_0728",
                corpName = "상호_0728",
                addr = "주소_0728",
                bizType = "업태_0728",
                bizClass = "종목_0728"
                )
try:
    print("=" * 15 + " 회사정보 수정 " + "=" * 15)

    result = faxService.updateCorpInfo(testValue.testCorpNum, corpInfo, testValue.testUserID)

    print("처리결과 : [%d] %s" % (result.code,result.message) )
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
