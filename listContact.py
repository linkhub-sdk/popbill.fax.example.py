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
    print("=" * 15 + " 담당자 목록 확인 " + "=" * 15)

    ''' ContactInfo 구성
                id                  (담당자 아이디)
                personName          (담당자 성명)
                email               (이메일)
                hp                  (휴대폰번호)
                fax                 (팩스번호)
                tel                 (연락처)
                regDT               (등록일시)
                searchAllAllowYN    (조회권한, True-회사조회, False-개인조회)
                mgrYN               (관리자 여부, True-관리자, False-사용자)
                response[i].id, response[i].personName 등의 방식으로 항목 확인가능.
    '''
    response = faxService.listContact(testValue.testCorpNum, testValue.testUserID)

    for info in response :
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        print("")

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
