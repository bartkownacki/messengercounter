from fbchat import Client
from fbchat.models import *

class ReplyCount(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        if thread_id=="<id of person with which you want to count messages>":
            print(message_object)
            if message_object.text == "!count":
                thread = client.fetchThreadInfo(thread_id)[thread_id]
                self.send(Message(text="Actual amount of messages on chat: " + str(thread.message_count)), thread_id=thread_id, thread_type=thread_type)

client = ReplyCount("<email>", "<password>")
client.listen()