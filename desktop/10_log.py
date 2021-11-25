""" import logging
# DEBUG level 이상을 모두 저장
# format = 시간정보 레벨네임 메시지
# 기본적인 설정
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

# 적은 level = 기준 이상부터 찍힌다.
# critical > error > warning > info > debug
# 개발단계에서 쓰는것
logging.debug("아 이거 누가 짠거야~~")
# 실제로 프로그램을 쓰는 사람들도 볼수있음
logging.info("자동화 수행 준비")
# 경고를 준다
logging.warning("이 스크립트는 조금 오래 되었다. 실행상에 문제가 있을 수 있다.")
# 에러를 준다
logging.error("에러가 발생하였습니다. 에러 코드는 ...")
# 치명적인 문제
logging.critical("복구가 불가능한 심각한 문제가 발생했습니다.")
 """
# 터미널과 파일에 함께 로그 남기기
import logging
from datetime import datetime
# 시간 [로그레벨] 메시지 형태로 로그를 작성
logFormatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
# 로그레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림 (터미널)
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
# mylogfile_20211010141010.log 파일을 만듬.
filename = datetime.now().strftime("mylogfile_%Y%m%d%H%M%S.log")
fileHandler = logging.FileHandler(filename, encoding="utf-8")
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트")