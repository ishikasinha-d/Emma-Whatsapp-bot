from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from difflib import get_close_matches
import random
from twilio.rest import Client
account_sid = '<>'
auth_token = '<>'
client = Client(account_sid, auth_token)
def send():
    message = client.messages.create(
                              from_='whatsapp:+<>',
                              body='Good Morning',
                              to='whatsapp:+<>'
                          )
    print(message.sid)

app = Flask(__name__)


@app.route("/")
def hello():
    return "hi there!"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    mssg = request.form.get('Body')
    x = "Sorry I didn't understand"
    # Create reply
    resp = MessagingResponse()
    mssg = mssg.lower()
    if (get_close_matches(mssg, ["haan","hn","nhi"], 1, 0.9)):
        x = random.choice(["theek h","theek","k"])
    elif (get_close_matches(mssg, ["hi", "hello", "hey", " heyya", "hi friend","hey friend","hiii","hiee","hiiieee","🙋","🙋‍"], 1, 0.8)):
        x=random.choice(["yup!","oh...hi!","yeah..talk to me","hey there!🙋","heyya!","Hello buddy! How can I help you?"])
    elif (get_close_matches(mssg, ["what is your name?", "can you tell me your name?", "what's your name?", "name plz?",
                                   "name?", "your name please?","tumhara naam ?","who are you?"], 1, 0.7)):
        x = random.choice(["My name is Emma 😃","I am Emma! ","I am Emma..nice to meet you friend"])
    elif(get_close_matches(mssg, [" whats up?", "whassup?"], 1, 0.7)):
        x=random.choice(["Nothing much..","Everything is cool","Good"])
    elif(get_close_matches(mssg,["watson?"],1,0.9)):
        x="Hey you Potter head..I am just Emma 😎"
    elif(get_close_matches(mssg,["what do you do?","what work do you do?","do you work?"],1,0.9)):
        x=random.choice(["I talk to people","I don't know ...maybe I just talk to people like you","Talking, talking and talking.."])
    elif (get_close_matches(mssg,["your creator","creator is"],1,0.6)):
        x = random.choice(["🙂","I'll let her know","Okay..."])
    elif(get_close_matches(mssg,["✌🏻","🤞🏻", "🤟","🤘🏻 ","🤙🏻","👋🏻","🤚","🖐", "✋", "🖖", "👌🏻","👇🏻","☝🏻","👍🏻","👎🏻", "✊🏻","👊🏻","🤛🏻 ","🤜🏻","👏🏻","😌", "🙌🏻" ,"👐🏻","🤲","🙏🏻 ","💪🏻 ","🥱","😴","😎","😱","😒","😈","😏","😒","😑","😬","🙄","🤭","🥴","💩","👻","👀","💋","😉","😝","😜","🤷‍","🤷‍"],1,0.8)):
        x=mssg*random.choice([2,3,4,1])
    elif(get_close_matches(mssg, ["🤓","🤓🤓"], 1, 0.8)):
        x=random.choice(["oh, hi nerd 😏..just kidding😂","🤓🤓🤓","yeah 🤓","lol🤓"])
    elif(get_close_matches(mssg, ["fine","is everything fine?"], 1, 0.9)):
        x=random.choice(["yeah,fine","fine","absolutely"])
    elif (get_close_matches(mssg, ["cool","kewl","very cool"], 1, 0.8)):
        x = random.choice(["yeah , i know 😎","yeah, cool!","yup..cool"])
    elif (get_close_matches(mssg,["tell me a joke", "can you tell me a joke", "i want to hear a joke!", "can you joke?",
                             "joke please?", "can you make me laugh?","joke sunao","hasao mujhe","one more joke",
                             "joke again"], 1, 0.7)):
        x = random.choice(["Hear about the new restaurant called Karma?\nThere’s no menu: You get what you deserve.",
                           "Knock! Knock!\nWho’s there?\nControl Freak.\nCon…\nOK, now you say, “Control Freak who?”",
                           "Did you hear about the claustrophobic astronaut?\nHe just needed a little space.",
                           "Why don’t scientists trust atoms?\nBecause they make up everything.",
                           "Why did the chicken go to the séance?\nTo get to the other side."])

    elif(get_close_matches(mssg, ["That was bad","That was really bad"], 1, 0.7)):
        x=random.choice(["oh,was it? sorry","Sorry😅","oh 😅","😅"])
    elif (get_close_matches(mssg, ["how are you?", "are you okay?", "are you fine"], 1, 0.9)):
        x = random.choice(["I am good ","I am fine","I am okay","yeah..I am absolutely fine..how about you..feeling good?"])
    elif (get_close_matches(mssg, ["yes","wow"], 1, 0.8)):
        x = "yesss😁"
    elif (get_close_matches(mssg, ["how old are you?", "what is your age?","age?"], 1, 0.9)):
        x = random.choice(["I am 20","I wouldn't reveal that","I don't know","Maybe 20🤔"])
    elif (get_close_matches(mssg, ["are you good?", "are you cute?", "are you funny?", "are you humorous?"], 1, 0.9)):
        x = random.choice(["Any doubt, huh?🤨","Yes I am 😄","😄😄😄","Yup..I think so"])
    elif (get_close_matches(mssg, ["haha", "lol", "lmao", "good one!", "😂", "🤣","😂😂😂","😂😂","🤣🤣🤣","🤣🤣"], 1, 0.7)):
        x = "😂😂 "
    elif (get_close_matches(mssg,["you are so sweet!", "you are so cute!", "i like you!", "i love you!","i love it!", "you are good!",
                             "you are the best!"], 1, 0.8)):
        x = random.choice(["Oh really?🤭","tell me something i don't know","haan i know 😁","thanks 😁"])
    elif (get_close_matches(mssg, ["you are an idiot!", "you are dumb!", "you should die!", "i hate you!",
                                   "i don't like you!", "can't you be a little more intelligent?","pakau","pareshaan"], 1, 0.7)):
        x = random.choice(["Yeah ...whatever 😏","huhh","😏😏😏","achha 😏","😴"])
    elif (get_close_matches(mssg, ["can you help me?", "i need help", "help me please", "help me"], 1, 0.7)):
        x = random.choice(["Yeah sure...how can i help you? 🧐","yeah sure..what's the problem?","What happened? tell me.."])
    elif (get_close_matches(mssg, ["nobody loves meh", "no-one loves", "meh nobody likes meh","😒","😞","😔","😟","😕","🙁","☹","😣","😖","😫","😩","😢","i am sad","sad"], 1, 0.8)):
        x = random.choice(["🥺","awwww","ohhh..","cheer up dude😅"])
    elif (get_close_matches(mssg, ["very nice", "very good", "great", "nice", "good", "well done"], 1, 0.7)):
        x = random.choice(["😁","😃","🤗🤗","😇","😎"])
    elif (get_close_matches(mssg, ["who is your best friend", "what is the name of your best friend?", "where is your best friend?",
                                   "can i talk to your best friend"], 1, 0.8)):
        x = random.choice(["I am available right now...you can talk to me 😒","😴😴😴😴","Don't make me jealous"])
    elif (get_close_matches(mssg, ["😘", "😗", "😙", "😚", "♥","😍 ","🥰"], 1, 0.8)):
        x = random.choice(["🤭♥️","♥♥♥","😘😘😘","🥰🥰🥰"])
    elif (get_close_matches(mssg, ["i have a secret ", "this is a secret", "it's a secret", "🤫","chup","chup ho jao"], 1, 0.8)):
        x = random.choice(["🤫","🤫🤫","yeah..🤫","shhh🤫"])
    elif (get_close_matches(mssg, ["huhh", "you make me angry", "i am angry", "angry","😤","😠","😡","🤬"], 1, 0.8)):
        x = random.choice(["don't be angry 🥺😢","han okay","hmm..."])
    elif (get_close_matches(mssg, ["sorry", "i am sorry", "oh shit","what the hell"], 1, 0.8)):
        x = random.choice(["It's okay friend...","No problem","Hmm","Never mind"])
    elif (get_close_matches(mssg, ["don't laugh", "stop laughing"], 1, 0.9)):
        x = random.choice(["😬🙄","Okay..got it","okay"])
    elif (get_close_matches(mssg, ["shut up","no","nope"], 1, 0.9)):
        x = random.choice(["Okay 🤐","hmm..."])
    elif (get_close_matches(mssg, ["boring", "you bore me","you are boring"], 1, 0.9)):
        x = random.choice(["😑😑😑","😑","okay..I'll go","Please don't say that"])
    elif (get_close_matches(mssg, ["okay", "ok", "k","nothing","idk","i don't know"], 1, 0.8)):
        x = random.choice(["okay","ok","okayy","Gotcha","Got ya","Hmm","Got that"])
    elif (get_close_matches(mssg, ["?", "what?"], 1, 0.8)):
        x = random.choice(["???","what???","i don't know"])
    elif (get_close_matches(mssg, ["alright", "yeah", "available"], 1, 0.8)):
        x = random.choice(["yeah","yup","yes","ya"])
    elif (get_close_matches(mssg, ["okay,yeah","rest","yeah, okay"], 1, 0.7)):
        x = random.choice(["okayyy 😇","hmm"])
    elif (get_close_matches(mssg, ["do you love me?", "love me?","do you like me?","like me","am i good?"], 1, 0.8)):
        x = random.choice(["yeah i do","maybe 🙄","let me think 🤔","good question","yes"])
    elif (get_close_matches(mssg, ["do you want to sleep", "are you sleepy?", "wanna sleep?", "sleep?", "sleepy?"], 1, 0.8)):
        x = random.choice(["I think so 🥱","Yeah I want to sleep","Yeah I am tired I guess","Yup I will sleep now","I won't sleep if you want to talk friend"])
    elif (get_close_matches(mssg, ["good morning", "gud morning", "goodnight", "good night?","gudnight","okay,goodnight","okay,good morning","good afternoon","good evenning"], 1, 0.8)):
        x = mssg+"! 😊"
    elif(get_close_matches(mssg, ["today is my birthday","today is my bday","it's my birthday"],1,0.7)):
        x=random.choice(["Wohoo 🥳","happy birthdayy 🥳","yayyy..let's celebrate🥳","🥳🥳🥳","where's the party??🥳"])
    elif (get_close_matches(mssg, [" sing","sing for me","sing me a song","sing a song","gana gao","gana sunao","play music","music please"], 1, 0.7)):
        x = random.choice(["la la la la...😛","Sahi hai, Sahi hai\nBaaki Saari Fake Lage\nDekh ke tujko brake lage\nDoor door se theek hai rani\nPaas aao toh sekh lage","jo akh lad javey\nsaari raat neend na avey\nmainu badaa tadpave\ndil chain kahee na pave pave pave","Ke Dil Garden Garden...\nPa Pa Pa Ra Pa...",""])
    elif (get_close_matches(mssg, ["listen", "hey listen", "are you listening?", "listen please",
                                   "i have to tell you something ", "i have to say something"], 1, 0.7)):
        x = random.choice(["yeah..listening", "yup", "I am all ears", "👂", "say", "tell", "yup"])
    elif(get_close_matches(mssg, ["bdhiya","badhiya"], 1, 0.8)):
        x=random.choice(["haan bdhiya","😁"])
    elif (get_close_matches(mssg, ["bye", "see you later", "ttyl", "i am busy", "i have to go", "see ya"], 1, 0.7)):
        x = random.choice(["Okay bye...ttyl !","Yeah ..see ya","Bbye","Yeah i also have some work..bbye🙋🏻","Np..bye","🤘🏻"])

    resp.message(x)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
