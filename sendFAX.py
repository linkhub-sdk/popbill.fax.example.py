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

'''
팩스를 전송합니다. (전송할 파일 개수는 최대 20개까지 가능)
 - 팩스전송 문서 파일포맷 안내 : http://blog.linkhub.co.kr/2561
'''

try:
    print("=" * 15 + " 팩스전송. 1파일 1건 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 발신번호
    Sender = '07043042992'

    # 발신자명
    SenderName = '발신자명'

    # 수신번호
    Receiver = '010111222'

    # 수신자명
    ReceiverName = '수신자명'

    # 파일경로 (해당파일에 읽기 권한이 설정되어 있어야 함. 최대 20개)
    FilePath = ['test.jpeg']

    # 예약전송일시, None처리시 즉시전송, 작성형태 'yyyyMMddHHmmss'
    ReserveDT = ''

    # 광고팩스 전송여부
    AdsYN = False

    # 팩스제목
    Title = "팩스제목"

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    RequestNum = ""

    receiptNum = faxService.sendFax(CorpNum, Sender, Receiver, ReceiverName,
                                    FilePath, ReserveDT, UserID, SenderName, AdsYN, Title, RequestNum)

    print("receiptNum (접수번호) : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
