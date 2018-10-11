from data_loaders import Lang
import data_loaders
import train
import torch
from models import EncoderRNN
from models import DecoderRNN
 




device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def main():
    lang1 = "eng"
    lang2 = "fra"
    f = open("../data/data/"+lang1+"-"+lang2+".txt", encoding='utf-8')
    print (f)
    lines = f.readlines()
    eng_sentences, fra_sentences = data_loaders.getSentences(lines)
    print (len(eng_sentences), len(fra_sentences))
    eng_lang = Lang(lang1)
    eng_lang.parseSentences(eng_sentences)
    fra_lang = Lang(lang2)
    fra_lang.parseSentences(fra_sentences)
    print ("No of eng words: ", len(eng_lang.vocab))
    print ("No of fra words: ", len(fra_lang.vocab))
    pairs = data_loaders.createPairs(eng_sentences, fra_sentences)
    print ("Length of pairs: ", len(pairs))
    
    hidden_size = 256
    encoder1 = EncoderRNN(len(eng_lang.vocab), hidden_size).to(device)
    attn_decoder1 = DecoderRNN(len(fra_lang.vocab), hidden_size, len(fra_lang.vocab)).to(device)

    train.trainIters(encoder1, attn_decoder1,  75000, pairs, eng_lang, fra_lang, print_every=5000)    



if __name__ == "__main__": 
    main()