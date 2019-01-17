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
팩스전송요청시 할당한 전송요청번호(requestNum)으로 전송결과를 확인합니다.
- 응답항목에 대한 자세한 사항은 "[팩스 API 연동매뉴얼] >  3.3.2 GetFaxDetailRN (전송내역 및 전송상태 확인 - 요청번호 할당)을 참조하시기 바랍니다.
'''

try:
    print("=" * 15 + " 팩스전송 내역 및 전송상태 확인 " + "=" * 15)

    # 팝빌회원 사업자번호
    CorpNum = testValue.testCorpNum

    # 팩스전송 요청시 할당한 전송요청번호 (requestNum)
    requestNum = "20180929-001"

    resultList = faxService.getFaxResultRN(CorpNum, requestNum)

    for index, f in enumerate(resultList):
        print("FaxResult[%d] : " % index)
        print("    state (전송상태 코드) : %s" % f.state)
        print("    result (전송결과 코드) : %s" % f.result)
        print("    sendNum (발신번호) : %s" % f.sendNum)
        print("    senderName (발신자명) : %s" % f.senderName)
        print("    receiveNum (수신번호) : %s" % f.receiveNum)
        print("    receiveName (수신자명) : %s" % f.receiveName)
        print("    title (팩스제목) : %s" % f.title)
        print("    sendPageCnt (전체 페이지수) : %s" % f.sendPageCnt)
        print("    successPageCnt (성공 페이지수) : %s" % f.successPageCnt)
        print("    failPageCnt (실패 페이지수) : %s" % f.failPageCnt)
        print("    refundPageCnt (환불 페이지수) : %s" % f.refundPageCnt)
        print("    cancelPageCnt (취소 페이지수) : %s" % f.cancelPageCnt)
        print("    receiptDT (접수일시) : %s" % f.receiptDT)
        print("    reserveDT (예약일시) : %s" % f.reserveDT)
        print("    sendDT (전송일시) : %s" % f.sendDT)
        print("    resultDT (전송결과 수신일시) : %s" % f.resultDT)
        print("    receiptNum (접수번호) : %s" % f.receiptNum)
        print("    requestNum (요청번호) : %s" % f.requestNum)
        print("    chargePageCnt (과금 페이지수) : %s" % f.chargePageCnt)
        print("    tiffFileSize (변환파일용랑(단위 : byte)) : %s" % f.tiffFileSize)


except PopbillException as PE:
    print("Exception Occur : [%d] %s" % (PE.code, PE.message))
