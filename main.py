import time
from plyer import notification
while True:
    time.sleep(20*60)
    if __name__=="__main__":
        notification.notify(
            title="Take A Break!",
            message="Follow the 20-20-20 rule and protect your eyes.",
            app_icon="C:\Work\eye.ico",
            timeout=10,
        )
    