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

'''
연동회원의 담당자 목록을 확인합니다.
'''

try:
    print("=" * 15 + " 담당자 목록 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    response = faxService.listContact(CorpNum, UserID)

    for info in response :
        for key, value in info.__dict__.items():
            print("%s : %s" % (key, value))
        print("")

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code , PE.message))
