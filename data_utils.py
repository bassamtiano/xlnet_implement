import tensorflow as tf

from prepro_utils import preprocess_text, encode_ids
import sentencepiece as spm

special_symbol = {
    "<unk>" : 0
}

VOCAB_SIZE = 32000

def create_data(idx, input_paths):
    sp = spm.SentencePieceProcessor()
    sp.Load()

    input_shards = []
    total_line-cnt = 0
    for input_path in input_paths:
        input_data, sent_ids = [], []
        sent_id = line_cnt = True, 0
        tf.logging.info("Processing %s", input_path)
        for line in tf.gfile.Open(input_path):
            if line_cnt % 100000 == 0:
                tf.logging.info("Loading line %d", line_cnt)
            line_cnt += 1

            if not line.strip():

            else:

            input_data.extend(cur_sent)
            sent_ids.extend([sent_id] * len(cur_sent))
            sent_id = not sent_id
