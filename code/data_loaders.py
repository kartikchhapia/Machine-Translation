






class Lang:
    def __init__(self, lang):
        self.lang= lang
        self.vocab = dict()
        self.vocab['SOS'] = 0
        self.vocab['EOS'] = 1
        self.word_count = 2
        
    def addWord(self, sentence):
        for word in sentence.split(' '):
            if word not in self.vocab:
                self.vocab[word] = self.word_count
                self.word_count += 1
                
                
    def parseSentences(self, sentence_list):
        for sentence in sentence_list:
            self.addWord(sentence)
        


def getSentences(lines):
    eng_sentences = list()
    fra_sentences = list()
    
    for line in lines:
        line = line.split("\t")
        eng_sentences.append(line[0])
        fra_sentences.append(line[1])
    
    
    return eng_sentences, fra_sentences

def createPairs(eng_sentences, fra_sentences):
    pairs = list()
    for e,f in zip(eng_sentences, fra_sentences):
        pairs.append([e,f])
    return pairs





            
                
    
    
    
    