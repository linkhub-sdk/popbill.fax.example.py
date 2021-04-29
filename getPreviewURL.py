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
접수한 팩스 전송건에 대한 미리보기 팝업 URL을 반환합니다.
- 팩스 미리보기는 팩스 변환 완료후 가능합니다
- 보안정책으로 인해 반환된 URL은 30초의 유효시간을 갖습니다.
- https://docs.popbill.com/fax/python/api#GetPreviewURL
'''

try:
    print("=" * 15 + " 팩스 미리보기 팝업 URL 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팩스 접수번호
    ReceiptNum = "019011813341400001"

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    url = faxService.getPreviewURL(CorpNum, ReceiptNum, UserID)

    print("URL: %s" % url)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
