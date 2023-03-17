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

from popbill import FaxService, FaxReceiver, FileData, PopbillException

faxService = FaxService(testValue.LinkID, testValue.SecretKey)
faxService.IsTest = testValue.IsTest
faxService.IPRestrictOnOff = testValue.IPRestrictOnOff
faxService.UseStaticIP = testValue.UseStaticIP
faxService.UseLocalTimeYN = testValue.UseLocalTimeYN

"""
전송할 파일의 바이너리 데이터로 다수의 수신자에게 팩스를 전송하기 위해 팝빌에 접수합니다. (최대 전송파일 개수 : 20개) (최대 1,000건)
- https://developers.popbill.com/reference/fax/python/api/send#SendFAXBinary_multi
"""

try:
    print("=" * 15 + " 팩스전송. 1파일 1건 전송 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팝빌회원 아이디
    UserID = testValue.testUserID

    # 발신번호
    Sender = ""

    # 발신자명
    SenderName = "발신자명"

    # 광고팩스 전송여부 , true / false 중 택 1
    # └ true = 광고 , false = 일반
    # └ 미입력 시 기본값 false 처리 , true / false 중 택 1
    AdsYN = False

    # 예약전송시간, 작성형식:yyyyMMddHHmmss, 공백 기재시 즉시전송
    ReserveDT = ""

    # 팩스제목
    Title = "Python 팩스동보전송 제목"

    Receivers = []  # 수신정보 리스트, 최대 1000개
    for x in range(0, 5):
        Receivers.append(
            FaxReceiver(
                receiveNum="",  # 수신번호
                receiveName="수신자명" + str(x),  # 수신자명
                interOPRefKey="20220803-" + str(x),  # 파트너 지정키
            )
        )

    # 전송 파일 객체정보 리스트, 최대 20개
    FileDatas = []
    with open("./test.jpeg", "rb") as f:
        FileDatas.append(
            FileData(
                fileName="test.jpeg", fileData=f.read()  # 전송 파일명  # 전송 파일 바이너리 데이터
            )
        )

    # 전송요청번호
    # 파트너가 전송 건에 대해 관리번호를 구성하여 관리하는 경우 사용.
    # 1~36자리로 구성. 영문, 숫자, 하이픈(-), 언더바(_)를 조합하여 팝빌 회원별로 중복되지 않도록 할당.
    RequestNum = ""

    receiptNum = faxService.sendFaxBinary_multi(
        CorpNum,
        Sender,
        Receivers,
        FileDatas,
        ReserveDT,
        UserID,
        SenderName,
        AdsYN,
        Title,
        RequestNum,
    )

    print("receiptNum (접수번호) : %s" % receiptNum)

except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
