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

from popbill import ContactInfo, FaxService, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest

try:
    print("=" * 15 + " 담당자 등록 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 담당자 정보
    newContact = ContactInfo(

        # 아이디 (6자 이상 50자 미만)
        id="popbill_test_id",

        # 비밀번호 (6자 이상 20자 미만)
        pwd="popbill_test_pwd",

        # 담당자명 (최대 100자)
        personName="담당자명",

        # 담당자 연락처 (최대 20자)
        tel="010-111-222",

        # 담당자 휴대폰번호 (최대 20자)
        hp="010-111-222",

        # 담당자 팩스번호 (최대 20자)
        fax="070-111-222",

        # 담당자 이메일 (최대 100자)
        email="test@test.com",

        # 회사조회 권한여부, True(회사조회) False(개인조회)
        searchAllAllowYN=True,

        # 관리자 권한여부, True(관리자), False(사용자)
        mgrYN=True
    )

    result = faxService.registContact(CorpNum, newContact, UserID)

    print("처리결과 : [%d] %s" % (result.code, result.message))

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
