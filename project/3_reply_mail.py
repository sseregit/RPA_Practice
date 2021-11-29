import smtplib
from email.message import EmailMessage
from imap_tools import MailBox
from account import *

max_val = 3 # 최대선정자
applicant_list = [] # 지원자 리스트

print("[1. 지원자 메일 조회]")
mailbox = MailBox("imap.kakao.com", 993)
with mailbox.login(KAKAO_EMAIL_ADDRESS,KAKAO_EMAIL_PASSWORD,initial_folder="INBOX") as mailbox:
    index = 0
    for mail in mailbox.fetch('(SENTSINCE 28-Nov-2021)'):
        index += 1
        if "파이썬 특강" in mail.subject:
            nickname, phone = mail.text.strip().split("/")
            print(f"순번 : {index} 닉네임 : {nickname} 전화번호 : {phone}")
            applicant_list.append((mail,index,nickname,phone))

print("[2. 선정 / 탈락 메일 발송]")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EAMIL_PASSWORD)

    for mail,index,nickname,phone in applicant_list:
        to_addr = mail.to
        
        title = None
        content = None

        if index <= max_val:
            title = "파이썬 특강 안내 [선정]"
            content = f"{nickname}님 축하드립니다. 특강 대상자로 선정되셨습니다. (선정순번 {index}번)"
        else:
            title = "파이썬 특강 안내 [탈락]"
            content = f"{nickname}님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락 드리겠습니다. (대기순번 {index - max_val}번)"    

        msg = EmailMessage()
        msg["Subject"] = title
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_addr
        msg.set_content(content)
        smtp.send_message(msg)
        print(f"{nickname}님에게 메일 발송 완료")