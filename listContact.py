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
faxService.UseStaticIP = testValue.UseStaticIP
faxService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
연동회원의 담당자 목록을 확인합니다.
- https://docs.popbill.com/fax/python/api#ListContact
'''

try:
    print("=" * 15 + " 담당자 목록 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    response = faxService.listContact(CorpNum, UserID)

    for info in response:
        print("id (아이디) : %s" % info.id)
        print("personName (담당자 성명) : %s" % info.personName)
        print("email (담당자 이메일) : %s" % info.email)
        print("hp (담당자 휴대폰번호) : %s" % info.hp)
        print("fax (담당자 팩스번호) : %s" % info.fax)
        print("tel (담당자 연락처) : %s" % info.tel)
        print("regDT (등록일시) : %s" % info.regDT)
        print("searchAllAllowYN (회사 조회권한) : %s" % info.searchAllAllowYN)
        print("mgrYN (관리자 여부): %s" % info.mgrYN)
        print("state (상태): %s" % info.state + '\n')
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
