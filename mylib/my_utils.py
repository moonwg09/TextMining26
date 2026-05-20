import pandas as pd

def integer_indexing(test_tokenizer, texts):
    test_tokenizer.fit_on_texts(texts)
    return test_tokenizer


def rare_word_status(threshold, word_count_list):
    total_cnt = total_freq = 0
    rare_cnt = rare_freq = 0 
    
    for _, freq in word_count_list:
        total_freq += freq
        total_cnt += 1
        if freq < threshold:
            rare_cnt += 1
            rare_freq += freq

    print(f'전체 단어 : {total_cnt:,}개 {total_freq:,}번')
    print(f'희귀 단어 : (등장빈도 {threshold}번 이하 :  {rare_cnt:,}개 {rare_freq:,}번')
    print(f'희귀 단어 비율 : 단어수 {rare_cnt/total_cnt * 100:.2f}%, 빈도수 {rare_freq/total_freq*100:.2f}%')
    print(f'희귀 단어를 뺀 단어수 : {total_cnt - rare_cnt:,}개 {(total_freq-rare_freq)/total_freq*100:.2f}%') # max_words

def len_words_list(texts):
    len_list = [len(text.split()) for text in texts]
    len_df = pd.DataFrame(len_list, columns=['length'])
    print(len_df.describe())
    return len_df

def below_threshold_len(max_len, texts):
    count = 0
    for text in texts:
        if (len(text.split()) <= max_len):
            count += 1
    print(f'길이가 {max_len} 이하인 텍스트의 비율 : {count / len(texts)*100:.2f}%')

def below_threshold_len_from_list(max_len, texts):
    count = 0
    for text in texts:
        if (len(text) <= max_len):
            count += 1
    print(f'길이가 {max_len} 이하인 텍스트의 비율 : {count / len(texts)*100:.2f}%')