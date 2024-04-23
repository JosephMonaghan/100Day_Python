data = {"response_code":0, "results":[{"type":"boolean", "difficulty":"easy", "category":"General Knowledge", "question":"Pluto is a planet.", "correct_answer":"False", "incorrect_answers":["True"]}, {"type":"boolean", "difficulty":"easy", "category":"General Knowledge", "question":"Jingle Bells was originally meant for Thanksgiving", "correct_answer":"True", "incorrect_answers":["False"]}, {"type":"boolean", "difficulty":"easy", "category":"General Knowledge", "question":"In 2010, Twitter and the United States Library of Congress partnered together to archive every tweet by American citizens.", "correct_answer":"True", "incorrect_answers":["False"]}, {"type":"boolean", "difficulty":"easy", "category":"General Knowledge", "question":"It is automatically considered entrapment in the United States if the police sell you illegal substances without revealing themselves.", "correct_answer":"False", "incorrect_answers":["True"]}, {"type":"boolean", "difficulty":"easy", "category":"General Knowledge", "question":"The National Animal of Scotland is the Unicorn.", "correct_answer":"True", "incorrect_answers":["False"]}, {"type":"boolean", "difficulty":"easy", "category":"General Knowledge", "question":"One of Donald Trump&#039;s 2016 Presidential Campaign promises was to build a border wall between the United States and Mexico.", "correct_answer":"True", "incorrect_answers":["False"]}, {"type":"boolean", "difficulty":"easy", "category":"General Knowledge", "question":"Dihydrogen Monoxide was banned due to health risks after being discovered in 1983 inside swimming pools and drinking water.", "correct_answer":"False", "incorrect_answers":["True"]}, {"type":"boolean", "difficulty":"easy", "category":"General Knowledge", "question":"On average, at least 1 person is killed by a drunk driver in the United States every hour.", "correct_answer":"True", "incorrect_answers":["False"]}, {"type":"boolean", "difficulty":"easy", "category":"General Knowledge", "question":"Romanian belongs to the Romance language family, shared with French, Spanish, Portuguese and Italian. ", "correct_answer":"True", "incorrect_answers":["False"]}, {"type":"boolean", "difficulty":"easy", "category":"General Knowledge", "question":"A scientific study on peanuts in bars found traces of over 100 unique specimens of urine.", "correct_answer":"False", "incorrect_answers":["True"]}]}

#print(data["results"][1])

#print(len(data["results"]))

question_database = []
#print(len(data["results"]))

for question_num in range(len(data["results"])):
    #print(question_num)
    question_database.append(data["results"][question_num])
        
print(question_database)
