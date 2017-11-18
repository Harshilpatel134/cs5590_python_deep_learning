import numpy as np
import re
import itertools
from collections import Counter


def clean_str(string):
    """
    Tokenization/string cleaning for all datasets except for SST.
    Original taken from https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py
    """
    string = re.sub(r"[^A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    return string.strip().lower()


def load_data_and_labels(a_data_file, p_data_file,s_data_file,t_data_file,tr_data_file):
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    a_examples = list(open(a_data_file, "r",encoding='UTF8').readlines())
    a_examples = [s.strip() for s in a_examples]
    p_examples = list(open(p_data_file, "r",encoding='UTF8').readlines())
    p_examples = [s.strip() for s in p_examples]
    s_examples = list(open(s_data_file, "r", encoding='UTF8').readlines())
    s_examples = [s.strip() for s in s_examples]
    t_examples = list(open(t_data_file, "r", encoding='UTF8').readlines())
    t_examples = [s.strip() for s in t_examples]
    tr_examples = list(open(tr_data_file, "r", encoding='UTF8').readlines())
    tr_examples = [s.strip() for s in tr_examples]
    # Split by words
    x_text = a_examples + p_examples + s_examples + t_examples + tr_examples
    x_text = [clean_str(sent) for sent in x_text]
    # Generate labels
    a_labels = [[1,0,0,0,0] for _ in a_examples]
    p_labels = [[0,1,0,0,0] for _ in p_examples]
    s_labels = [[0, 1, 0, 0, 0] for _ in s_examples]
    t_labels = [[0, 1, 0, 0, 0] for _ in t_examples]
    tr_labels = [[0, 1, 0, 0, 0] for _ in tr_examples]
    y = np.concatenate([a_labels, p_labels,s_labels,t_labels,tr_labels], 0)
    return [x_text, y]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]
