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

'''
전송요청번호(requestNum)을 할당한 팩스를 재전송합니다.
- 접수일로부터 60일이 경과된 경우 재전송할 수 없습니다.
- 팩스 재전송 요청시 포인트가 차감됩니다. (전송실패시 환불처리)
- https://docs.popbill.com/fax/python/api#ResendFAXRN
'''

try:
    print("=" * 15 + " 팩스 재전송. 1건 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 원본 팩스 전송시 할당한 전송요청번호
    OrgRequestNum = '20190129100253'

    # 발신번호, 공백처리시 기존전송정보로 재전송
    Sender = '010111222'

    # 발신자명, 공백처리시 기존전송정보로 재전송
    SenderName = '발신자명'

    # 수신번호/수신자명 모두 공백처리시 기존전송정보로 재전송
    # 수신번호
    Receiver = ''

    # 수신자명
    ReceiverName = ''

    # 예약전송시간, 공백시 즉시전송, 작성형태 yyyyMMddHHmmss
    ReserveDT = ''

    # 팩스제목
    Title = '팩스 재전송 제목 (요청번호할당)'

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    RequestNum = ""

    receiptNum = faxService.resendFaxRN(CorpNum, OrgRequestNum, Sender, SenderName,
                                        Receiver, ReceiverName, ReserveDT, UserID, Title, RequestNum)

    print("receiptNum : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
