from spacy import load as spacy_loader
from spacy.matcher import Matcher
import en_core_web_md
import time
nlp = en_core_web_md.load()



def Lemmatization(doc):
    lemmas = [token.lemma_ for token in doc if token.pos_!='-PRON-']
    return ' '.join(lemmas)
def RemoveStopWords(doc):
    filtered_questions=[]
    stopwords= ['a', 'about', 'an', 'and', 'are', 'as', 'at', 'be', 'been', 'but', 'by', 'can', \
                'even', 'ever', 'for', 'from', 'get', 'had', 'has', 'have', 'he', 'her', 'hers', 'his', \
                'how', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'me', 'my', 'of', 'on', 'or', \
                'see', 'seen', 'she', 'so', 'than', 'that', 'the', 'their', 'there', 'they', 'this', \
                'to', 'was', 'we', 'were', 'what', 'when', 'which', 'who', 'will', 'with', 'you','take', 'ten', 'than', 'that', 'the', 'their', 'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these', ]

    for question in doc:
        filtered_sent = []
        question = nlp(question.lower())
        #question = Lemmatization(question)
        for word in question:
            if word.text in list('\n\n!""-#$%&()--.*+,-/:;<=>?@[\\]^_`{|}~\t\n.') and word.is_alpha!=True:
                continue
            if word.text not in stopwords:    
                filtered_sent.append(word.text)
        filtered_questions.append(' '.join(filtered_sent))
    return filtered_questions



def get_catogarized_review(questions):
    filtered_questions = RemoveStopWords(questions)
    print(filtered_questions)
    patterns = {
            'Food/Shopping':[
                             [{'LOWER':'food'}],
                             [{'LOWER':'restaurants'}],
                             [{'LOWER':'shop'}],
     
                                
                            ],
            'Infrastructures':[
                             [{'LOWER':'signage'}],
                             [{'LOWER':'sign'}],
                             [{'LOWER':'wifi'}],
                             [{'LOWER':'facilities'}],
                            
                            ],
    
            'Maintenance/Clean':[
                             [{'LOWER':'maintenance'}],
                             [{'LOWER':'maintain'}],
                             [{'LOWER':'maintained'}],
                             [{'LOWER':'clean'}],
                             [{'LOWER':'unhygienic'}],

                             [{'LOWER':'sanitizer'}],
                             
        
                            ],                              
            'Security/Staff':[
                            [{'LOWER':'staff'}],
                            ]
            }


    final_res = {top:[] for top in patterns}
    length = len
    Tuple  = tuple
    List = list

    for topic in patterns:
        matcher = Matcher(nlp.vocab)
        pat = patterns[topic]
        res = set()
        matcher.add(topic,None,*pat)
        for i,question in enumerate(filtered_questions):
            doc = nlp(question)
            f = matcher(doc)
            if length(f)>0:

                res.add(question)

        final_res[topic]=List(res)

    return final_res


questions = ["food","Sanitizer","unhygienic bad local","signage was good"]
c1 = time.time()
final_res = get_catogarized_review(questions)
print(final_res)
c2 = time.time()
print(c2-c1,"seconds")
'''
for i,question in enumerate(questions):
    question = nlp(question.lower())
    print(RemoveStopWords(question))
'''