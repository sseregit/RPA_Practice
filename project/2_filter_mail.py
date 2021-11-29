from imap_tools import MailBox
from account import *

applicant_list = []

mailbox = MailBox("imap.kakao.com", 993)
with mailbox.login(KAKAO_EMAIL_ADDRESS,KAKAO_EMAIL_PASSWORD,initial_folder="INBOX") as mailbox:
    index = 0
    for mail in mailbox.fetch('(SENTSINCE 28-Nov-2021)'):
        index += 1
        if "파이썬 특강" in mail.subject:
            nickname, phone = mail.text.strip().split("/")
            print(f"순번 : {index} 닉네임 : {nickname} 전화번호 : {phone}")
            applicant_list.append((mail,index,nickname,phone))