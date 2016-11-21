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

try:
    print("=" * 15 + " 연동회원 가입여부 확인 " + "=" * 15)

    # 가입여부 조회할 사업자번호
    CorpNum = "1234567890"

    result = faxService.checkIsMember(CorpNum)

    print("가입여부 : [%d] %s" % (result.code,result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
