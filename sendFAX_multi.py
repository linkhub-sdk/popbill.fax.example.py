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

from popbill import FaxService, FaxReceiver, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest
faxService.IPRestrictOnOff = testValue.IPRestrictOnOff
faxService.UseStaticIP = testValue.UseStaticIP
faxService.UseLocalTimeYN = testValue.UseLocalTimeYN

'''
동일한 팩스파일을 다수의 수신자에게 전송하기 위해 팝빌에 접수합니다. (최대 전송파일 개수 : 20개) (최대 1,000건)
- https://docs.popbill.com/fax/python/api#SendFAX_Multi
'''

try:
    print("=" * 15 + " 팩스전송. 1파일 동보전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 발신번호
    Sender = ''

    # 발신자명
    SenderName = '발신자명'

    # 파일경로 (해당파일에 읽기 권한이 설정되어 있어야 함. 최대 20개)
    FilePath = ['test.jpeg', 'test2.jpeg']

    # 광고팩스 전송여부 , true / false 중 택 1
    # └ true = 광고 , false = 일반
    # └ 미입력 시 기본값 false 처리 , true / false 중 택 1
    AdsYN = False

    # 예약전송시간, None처리시 즉시전송, 작성형태 'yyyyMMddHHmmss'
    ReserveDT = None

    # 팩스제목
    Title = '팩스 동보전송 제목'

    Receivers = []  # 수신정보 배열, 최대 1000개
    for x in range(0, 5):
        Receivers.append(
            FaxReceiver(
                receiveNum = '',  # 수신번호
                receiveName = '수신자명' + str(x),  # 수신자명
                interOPRefKey = '20220803-' + str(x) # 파트너 지정키
            )
        )

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    RequestNum = ""

    receiptNum = faxService.sendFax_multi(CorpNum, Sender, Receivers,
                                          FilePath, ReserveDT, UserID, SenderName, AdsYN, Title, RequestNum)

    print("receiptNum (접수번호) : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
