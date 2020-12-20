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



def get_catogarized_questions(questions):
    filtered_questions = RemoveStopWords(questions)
    print(filtered_questions)
    patterns = {
            'Data Strutures and Algorithms':[
                             [{'LOWER':'array'}],
                             [{'LOWER':'list'}],
                             [{'LOWER':'data structure'}],
                             [{'LOWER':'algorithms'}],
                             [{'LOWER':'algorithm'}],
                             [{'LOWER':'dynamic'}],
                             [{'LOWER':'asymptotic'}],
                             [{'LOWER':'analysis'}],

                             [{'LOWER':'tree'}],                                
                             [{'LOWER':'Kruskal'}],                                

                            ],
            'Programming':[
                             [{'LOWER':'C'}],
                             [{'LOWER':'C++'}],
                             [{'LOWER':'java'}],
                             [{'LOWER':'int'}],

                             [{'LOWER':'program'}],
                             [{'LOWER':'linked list'}],
                             [{'LOWER':'list'}],
                             [{'LOWER':'variable'}],

                             [{'LOWER':'string'}],
                             [{'LOWER':'strings'}],
                             [{'LOWER':'lists'}],
                             [{'LOWER':'integer'}],

                             [{'LOWER':'array'}],
                             [{'LOWER':'arrays'}],
                             [{'LOWER':'number'}],
                             [{'LOWER':'pattern'}],



                            ],
    
            'Computer Networks':[
                             [{'LOWER':'IP'}],
                             [{'LOWER':'ARP'}],
                             [{'LOWER':'network'}],
                             [{'LOWER':'internet'}],
                             [{'LOWER':'port'}],
                             [{'LOWER':'switch'}],
                             [{'LOWER':'data'}],
                             [{'LOWER':'layer'}],
                             [{'LOWER':'address'}],
                             [{'LOWER':'DNS'}],
                             [{'LOWER':'server'}],
                             [{'LOWER':'client'}],
                             
                             
        
                            ],                              
            'Software Engineering':[
                            [{'LOWER':'water fall'}],
                            [{'LOWER':'model'}],
                            [{'LOWER':'coupling'}],
                            
                            [{'LOWER':'verification'}],
                            [{'LOWER':'validation'}],
                            [{'LOWER':'requirements'}],

                            [{'LOWER':'SDLC'}],
                            [{'LOWER':'function points'}],
                            [{'LOWER':'management'}],

                            [{'LOWER':'feasibility study'}],
                            [{'LOWER':'CASE'}],
                            [{'LOWER':'cohesion'}],

                            
                            ],
            'DBMS':[
                            [{'LOWER':'primary'}],
                            [{'LOWER':'key'}],
                            [{'LOWER':'database'}],
                            [{'LOWER':'DBMS'}],
                            [{'LOWER':'normalization'}],
                            [{'LOWER':'relation'}],
                            [{'LOWER':'tuple'}],
                            [{'LOWER':'row'}],
                            [{'LOWER':'relation'}],
                            [{'LOWER':'table'}],
                            [{'LOWER':'entity'}],
                            [{'LOWER':'relationship'}],
                            [{'LOWER':'indexing'}],
                            [{'LOWER':'trigger'}],
                            
                            ]
            }


    final_res = {top:[] for top in patterns}
    length = len
    Tuple  = tuple
    List = list
    others = set()
    dirty=[0 for i in range(len(questions))]
    for topic in patterns:
        matcher = Matcher(nlp.vocab)
        pat = patterns[topic]
        res = set()

        matcher.add(topic,None,*pat)
        for i,question in enumerate(filtered_questions):
            doc = nlp(question)
            f = matcher(doc)
            if length(f)>0:
                dirty[i] = 1
                res.add(questions[i])
        final_res[topic]=List(res)


    for i,question in enumerate(filtered_questions):
        if not dirty[i]:
            others.add(questions[i])

    final_res['Others'] = List(others)
    return final_res




