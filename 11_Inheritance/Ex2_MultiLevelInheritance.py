print("----Ex2: Multi Level Inheritance-----")
#super class
class WhatsAppV1:
    def chat(self):
        print("Chat Feature")

#super/sub class
class WhatsAppV2(WhatsAppV1):
    def audioCalling(self):
        print("Audio Calling Feature")

    # def chat(self):
    #     print("Chat Feature")

#super/sub class
class WhatsAppV3(WhatsAppV2):
    def videoCalling(self):
        print("Video Calling Feature")

    # def audioCalling(self):
    #     print("Audio Calling Feature")

    # def chat(self):
    #     print("Chat Feature")

#sub class
class WhatsAppV4(WhatsAppV3):
    def status(self):
        print("status Feature")

    # def videoCalling(self):
    #     print("Video Calling Feature")

    # def audioCalling(self):
    #     print("Audio Calling Feature")

    # def chat(self):
    #     print("Chat Feature")



v4=WhatsAppV4()
v4.chat()
v4.audioCalling()
v4.videoCalling()
v4.status()
