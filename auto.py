from selenium import webdriver
import time
import pyautogui
import pyscreenshot
import datetime
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header


def sendmail(path):
    mail_host = "smtp.qq.com"
    mail_sender = "xxxxxxxxxxx@qq.com"
    mail_license = "xxxxxxxxxxxx"
    mail_receiver = "xxxxxx@lzu.edu.cn"

    mm = MIMEMultipart('related')

    content = "自动打卡结果通知"
    mm["From"] = "sender_name<xxxxxxxx@qq.com>"
    mm["To"] = "receiver_name<xxxxxx@lzu.edu.cn>"
    mm["Subject"] = Header(content,'utf-8')

    body_content = "今日打卡结果已到，请查收！"
    message_text = MIMEText(body_content,"plain","utf-8")
    mm.attach(message_text)

    image_data = open(path,'rb')
    message_image = MIMEImage(image_data.read())
    image_data.close()
    mm.attach(message_image)

    stp = smtplib.SMTP_SSL(mail_host,465)
    stp.login(mail_sender,mail_license)
    stp.sendmail(mail_sender,mail_receiver,mm.as_string())
    print("邮件发送成功")
    stp.quit()

#设置页面不会自动关闭
option = webdriver.EdgeOptions()
option.add_experimental_option("detach",True)

# 打开兰州大学个人工作平台
drive = webdriver.Edge(options = option)
drive.get('http://my.lzu.edu.cn/main')
drive.maximize_window()

#登录
drive.find_element_by_id('username').send_keys('xxxxxxxxxxx')
drive.find_element_by_id('password').send_keys('xxxxxxxxx')
drive.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/form/div[4]/button').click()

#进入打卡页面，进行打卡
pyautogui.moveTo(300,640,duration=1)
pyautogui.click(300,640,button='left')
pyautogui.moveTo(1700,1050,duration=1)
time.sleep(10)
pyautogui.click(1700,1050,button='left')

#打卡结果截图
im = pyscreenshot.grab(bbox=(1420,150,1920,1080))

#打卡结果保存
year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day
save_path = 'xxxxxxxxxxx'
im.save(save_path+'\\'+str(year)+'-'+str(month)+'-'+str(day)+'.png')
im_path = save_path+'\\'+str(year)+'-'+str(month)+'-'+str(day)+'.png'
time.sleep(3)
drive.quit()

#发送邮件，展示打卡结果
sendmail(im_path)








