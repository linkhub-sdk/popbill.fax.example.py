# -*- coding: utf-8 -*-

'''
 팝빌 팩스 API Python SDK Example

 - Python SDK 연동환경 설정방법 안내 : https://docs.popbill.com/fax/tutorial/python
 - 업데이트 일자 : 2019-10-25
 - 연동 기술지원 연락처 : 1600-9854 / 070-4304-2991~2
 - 연동 기술지원 이메일 : code@linkhub.co.kr

 <테스트 연동개발 준비사항>
 1) 18, 21번 라인에 선언된 링크아이디(LinkID)와 비밀키(SecretKey)를
    링크허브 가입시 메일로 발급받은 인증정보를 참조하여 변경합니다.
 2) 팝빌 개발용 사이트(test.popbill.com)에 연동회원으로 가입합니다.
'''

# 링크아이디
LinkID = 'TESTER'

# 비밀키
SecretKey = 'SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I='

# 연동환경 설정값, 개발용(True), 상업용(False)
IsTest = True

# 테스트 회원 사업자번호
testCorpNum = "1234567890"

# 테스트 회원 팝빌 아아디
testUserID = "testkorea"

# 발급토큰 IP 제한기능 활성화 여부 (권장-True)
IPRestrictOnOff = True
