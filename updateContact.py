# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it
import sys
import imp
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

import testValue

from popbill import ContactInfo, FaxService ,PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest

'''
연동회원의 담당자 정보를 수정합니다.
'''

try:
    print("=" * 15 + " 담당자 정보 수정 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 담당자 정보
    updateInfo = ContactInfo (

        # 담당자 아이디
        id = UserID,
        
        # 담당자 성명
        personName = "담당자 성명",

        # 연락처
        tel = "070-4304-2991",

        # 휴대폰번호
        hp = "010-4324-4324",

        # 팩스번호
        fax = "02-6442-9700",

        # 메일주소
        email = "dev@linkhub.co.kr",

        # 회사조회 여부, True-회사조회, False-개인조회
        searchAllAllowYN = True
    )

    result = faxService.updateContact(CorpNum, updateInfo, UserID)

    print("처리결과 : [%d] %s" % (result.code,result.message) )
except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
