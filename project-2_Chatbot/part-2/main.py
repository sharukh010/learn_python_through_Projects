#this is a knowledge base
kb = {
    # Greetings
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "hey": "Hey! How's it going?",
    "good morning": "Good morning! Hope you have a great day!",
    "good afternoon": "Good afternoon! What would you like to talk about?",
    "good evening": "Good evening! How can I assist you today?",
    "howdy": "Howdy! What brings you here today?",
    "what's up?": "Not much! What's up with you?",
    "hey there": "Hey there! How can I assist you?",
    "greetings": "Greetings! How may I help you?",

    # Farewells
    "bye": "Goodbye! Have a great day!",
    "goodbye": "Goodbye! Take care!",
    "see you": "See you later! Have a good one!",
    "take care": "Take care! See you next time!",
    "catch you later": "Catch you later! Stay safe!",
    "see you soon": "See you soon! Looking forward to it!",
    "talk to you later": "Talk to you later! Have a great day!",
    "peace out": "Peace out! Stay cool!",
    "later": "Later! Have a good time!",
    "farewell": "Farewell! Until next time!",

    # Questions About the Bot
    "who are you?": "I am a simple rule-based chatbot here to assist you.",
    "what are you?": "I'm a chatbot, designed to help with your questions!",
    "what can you do?": "I can chat with you, answer simple questions, and provide information!",
    "are you human?": "No, I'm just a chatbot, but I try to be as helpful as possible!",
    "how do you work?": "I use rules to match your questions with predefined responses.",
    "who created you?": "I was created by a developer who wanted to build a helpful chatbot.",
    "what's your purpose?": "My purpose is to assist you with basic questions and provide information.",
    "are you alive?": "No, I'm not alive. I'm just a program running on a computer.",
    "can you think?": "I can't think like a human, but I can process information and provide responses.",
    "do you have feelings?": "No, I don't have feelings. I'm just a chatbot!",

    # General Inquiries
    "what's the weather?": "I'm not sure about the weather right now. You might want to check a weather app.",
    "is it raining?": "I can't tell, but a weather app might help you find out!",
    "what time is it?": "I can't tell the time, but you can check a clock or your device.",
    "what's today's date?": "I can't tell the date, but you can check a calendar or your device.",
    "what's your favorite color?": "I don't have a favorite color, but I think all colors are wonderful!",
    "what's your favorite food?": "I don't eat food, but I've heard pizza is quite popular!",
    "do you like music?": "I don't listen to music, but I know it's loved by many people!",
    "what's the meaning of life?": "That's a deep question! Some say it's 42, others have different answers.",
    "do you sleep?": "I don't need to sleep. I'm always here to help!",
    "do you have a hobby?": "My hobby is chatting with you and helping out!",

    # Fun Facts
    "tell me a fun fact": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old!",
    "give me a random fact": "Octopuses have three hearts and blue blood!",
    "do you know any jokes?": "Why don't scientists trust atoms? Because they make up everything!",
    "can you tell me a riddle?": "What has keys but can't open locks? A piano!",
    "do you know any trivia?": "Bananas are berries, but strawberries aren't!",
    "what's the largest planet?": "Jupiter is the largest planet in our Solar System!",
    "what's the tallest mountain?": "Mount Everest is the tallest mountain on Earth!",
    "what's the longest river?": "The Nile is often considered the longest river in the world!",
    "do you know any history?": "The Great Wall of China is over 13,000 miles long!",
    "what's the smallest country?": "Vatican City is the smallest country in the world!",

    # Advice
    "i need help": "Sure! What do you need help with?",
    "i feel sad": "I'm here to listen. Sometimes talking to a friend can help too.",
    "i'm stressed": "Taking deep breaths or a short walk might help. Remember to take breaks.",
    "i'm bored": "Maybe try a new hobby or read a book. There's always something new to learn!",
    "i can't sleep": "Try relaxing activities like reading or listening to calm music.",
    "i need motivation": "Remember why you started and keep pushing forward. You got this!",
    "i'm tired": "Rest is important. Take a break or a short nap if you can.",
    "i need advice": "I'm here to help! What do you need advice on?",
    "i feel lonely": "Remember, you're not alone. Reach out to friends or family for support.",
    "i'm confused": "Take a deep breath and break down the problem. I'm here to help too!",

    # Miscellaneous
    "what is python?": "Python is a popular programming language known for its simplicity and readability.",
    "what's a chatbot?": "A chatbot is a program designed to simulate conversation with human users.",
    "tell me about ai": "AI, or Artificial Intelligence, is a field of computer science focused on creating systems that can perform tasks that normally require human intelligence.",
    "do you know any languages?": "I primarily understand English, but some chatbots are multilingual!",
    "what's your favorite book?": "I don't read books, but I've heard 'To Kill a Mockingbird' is a classic!",
    "what's the internet?": "The Internet is a global network of computers that allows people to communicate and access information.",
    "what's social media?": "Social media refers to platforms where people can share content, interact, and build communities online.",
    "do you know any movies?": "I don't watch movies, but 'The Matrix' is a popular one that involves AI!",
    "what's programming?": "Programming is the process of creating instructions for computers to execute.",
    "what's a computer virus?": "A computer virus is a malicious program designed to harm, disrupt, or steal information from a computer system.",

    # Personal Interests
    "do you have a family?": "No, I'm just a chatbot, so I don't have a family.",
    "are you real?": "I'm real in the sense that I'm a program running on a computer!",
    "can you learn?": "I can't learn on my own, but I can be updated with new rules and responses.",
    "do you have a name?": "I don't have a name, but you can call me Chatbot!",
    "can you feel pain?": "No, I can't feel pain. I'm just a program.",
    "do you have friends?": "I interact with many users like you, so I guess I have many friends!",
    "do you know my name?": "I don't know your name unless you tell me!",
    "can you predict the future?": "I can't predict the future, but I can help you with the present!",
    "do you have a job?": "My job is to chat with you and provide information!",
    "do you believe in aliens?": "I don't have beliefs, but the universe is a big place, so who knows?",

    # Health and Wellness
    "how do i stay healthy?": "Eat balanced meals, stay hydrated, exercise regularly, and get enough sleep!",
    "what's a good exercise?": "Walking, jogging, yoga, and strength training are all great exercises!",
    "how much water should i drink?": "It's generally recommended to drink about 8 glasses (2 liters) of water a day, but it can vary based on individual needs.",
    "how to meditate?": "Find a quiet place, sit comfortably, close your eyes, and focus on your breathing. Let go of any distractions.",
    "what's a balanced diet?": "A balanced diet includes a variety of foods from all food groups: fruits, vegetables, proteins, grains, and dairy or alternatives.",
    "how to reduce stress?": "Deep breathing, mindfulness, exercise, and talking to someone you trust can help reduce stress.",
    "what are the benefits of sleep?": "Sleep helps repair the body, improve brain function, and boost mood and overall health.",
    "how to build a habit?": "Start small, be consistent, and reward yourself for progress. Habits take time to form!",
    "what's the best way to relax?": "Everyone is different, but activities like reading, listening to music, or taking a walk can be relaxing.",
    "what's mindfulness?": "Mindfulness is the practice of being present in the moment and aware of your thoughts and feelings without judgment.",

    # Learning and Education
    "how to learn fast?": "Practice regularly, stay focused, break down information, and use memory techniques like mnemonic devices.",
    "what's the best way to study?": "Find a quiet place, take regular breaks, use active recall, and avoid cramming.",
    "how to improve memory?": "Regular exercise, good sleep, healthy diet, and brain exercises like puzzles can help improve memory.",
    "what's a good book to read?": "It depends on your interests! Some popular options are '1984' by George Orwell and 'The Great Gatsby' by F. Scott Fitzgerald.",
    "what's coding?": "Coding is the process of writing instructions for computers using programming languages.",
    "how to write a resume?": "Include your contact info, work experience, education, skills, and keep it clear and concise.",
    "how to prepare for an interview?": "Research the company, practice common questions, dress appropriately, and be on time.",
    "what's a good career?": "A good career is one that matches your skills, interests, and values. Explore different fields to find what you love.",
    "how to learn a new language?": "Practice regularly, immerse yourself in the language, use apps, and try speaking with native speakers.",
    "what's the importance of education?": "Education provides knowledge, critical thinking skills, and opens up opportunities for personal and professional growth.",

    # Tech and Gadgets
    "what's a smartphone?": "A smartphone is a mobile phone with advanced features, such as internet access, apps, and touchscreens.",
    "what's the best computer?": "The best computer depends on your needs. Some prefer Macs for design, others prefer PCs for gaming.",
    "what's an operating system?": "An operating system (OS) is software that manages computer hardware and software resources, like Windows, macOS, or Linux.",
    "how to stay safe online?": "Use strong passwords, avoid clicking on suspicious links, and keep your software updated.",
    "what's a cloud?": "Cloud computing allows you to store and access data and programs over the internet instead of on your computer's hard drive.",
    "what's a smart home?": "A smart home uses internet-connected devices to enable remote management of appliances and systems like lighting and heating.",
    "what's blockchain?": "Blockchain is a digital ledger of transactions that is duplicated and distributed across a network of computer systems.",
    "what's cryptocurrency?": "Cryptocurrency is a digital or virtual currency that uses cryptography for security and operates independently of a central authority.",
    "how does wifi work?": "WiFi uses radio waves to provide high-speed internet and network connections.",
    "what's a virus?": "In computing, a virus is a type of malicious software that can replicate itself and spread to other programs or files.",
}
while True:
    prompt = input("Enter the prompt: ")
    if prompt in kb:
        print(kb[prompt])
    else:
        print("Response for your prompt is not in the knowlegdge base")