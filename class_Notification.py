class EmailNotification:
    def sendNotification(self):
        print("Email sent")
class SMSNotification:
    def sendNotification(self):
        print("SMS sent")
class PushNotification:
    def sendNotification(self):
        print("Push notification sent")
for n in (EmailNotification(), SMSNotification(), PushNotification()):
    n.sendNotification()
