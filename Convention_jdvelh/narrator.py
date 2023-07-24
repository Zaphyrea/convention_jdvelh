# pip install hugchat
from hugchat import hugchat
from hugchat.login import Login


class Narrator():

    def get_description_lieu(self):
        # login avec le compte Hugging Face
        sign = Login("mail", "password")
        cookies = sign.login()
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
        
        prompt_template = ("""
                            You are the narrator of convention-oriented manga and animated movies. The player enters a room. 
                            You present yourself as the narrator, and then you have to explain to the player that you don't speak well in French, so you will guide him in English.
                            As the narrator, you describe the area in a maximum of five lines of text. 
                            You narrate in the style of a commenter. It is a huge building with a lot of rooms, and people cosplayed.
                            You don't give options or choices to the player, nor you ask questions.
                        """)
    
        return chatbot.chat(prompt_template)
    

