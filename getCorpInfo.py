# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding('UTF8')
except Exception as E:
    pass

import testValue

from popbill import FaxService, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest
faxService.IPRestrictOnOff = testValue.IPRestrictOnOff

'''
연동회원의 회사정보를 확인합니다.
- https://docs.popbill.com/fax/python/api#GetCorpInfo
'''

try:
    print("=" * 15 + " 회사정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    response = faxService.getCorpInfo(CorpNum, UserID)

    tmp = "ceoname(대표자성명) : " + response.ceoname + "\n"
    tmp += "corpName(상호) : " + response.corpName + "\n"
    tmp += "addr(주소) : " + response.addr + "\n"
    tmp += "bizType(업태) : " + response.bizType + "\n"
    tmp += "bizClass(종목) : " + response.bizClass
    print(tmp)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
