# -*- coding: utf-8 -*-

"""
 팝빌 팩스 API Python SDK Example

 - Python SDK 연동환경 설정방법 안내 : https://developers.popbill.com/guide/fax/python/getting-started/tutorial
 - 업데이트 일자 : 2023-05-10
 - 연동 기술지원 연락처 : 1600-9854
 - 연동 기술지원 이메일 : code@linkhubcorp.com

 <테스트 연동개발 준비사항>
 1) 17, 20번 라인에 선언된 링크아이디(LinkID)와 비밀키(SecretKey)를
    연동신청 후 메일로 발급받은 인증정보를 참조하여 변경합니다.
"""

# 링크아이디
LinkID = "TESTER"

# 비밀키
SecretKey = "SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I="

# 연동환경 설정값, 개발용(True), 상업용(False)
IsTest = True

# 테스트 회원 사업자번호
testCorpNum = "1234567890"

# 테스트 회원 팝빌 아아디
testUserID = "testkorea"

# 발급토큰 IP 제한기능 활성화 여부 (권장-True)
IPRestrictOnOff = True

# 팝빌 API 서비스 고정 IP 사용여부, true-사용, false-미사용, 기본값(false)
UseStaticIP = False

# 로컬시스템 시간 사용여부, 권장(True)
UseLocalTimeYN = True
