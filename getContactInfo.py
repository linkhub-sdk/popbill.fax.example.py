# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp

imp.reload(sys)
try:
    sys.setdefaultencoding("UTF8")
except Exception as E:
    pass

import testValue

from popbill import FaxService, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest
faxService.IPRestrictOnOff = testValue.IPRestrictOnOff
faxService.UseStaticIP = testValue.UseStaticIP
faxService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
연동회원 사업자번호에 등록된 담당자(팝빌 로그인 계정) 정보를 확인합니다.
- https://developers.popbill.com/reference/fax/python/api/member#GetContactInfo
"""

try:
    print("=" * 15 + " 담당자 정보 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 담당자 아이디
    contactID = "testkorea"

    contactInfo = faxService.getContactInfo(CorpNum, contactID)

    print("id (아이디) : %s " % contactInfo.id)
    print("personName (담당자 성명) : %s " % contactInfo.personName)
    print("tel (담당자 연락처(전화번호)) : %s " % contactInfo.tel)
    print("email (담당자 이메일) : %s " % contactInfo.email)
    print("regDT (등록일시) : %s " % contactInfo.regDT)
    print("searchRole (담당자 조회권한) : %s " % contactInfo.searchRole)
    print("mgrYN (관리자 여부) : %s " % contactInfo.mgrYN)
    print("state (계정상태) : %s " % contactInfo.state)
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
