import math
import re
import random

import tensorflow as tf
import numpy as np

# Parameters

device_id = "/gpu:0"

model_dir = "./data/models"


train_batch_size = 100
num_core_per_host = 100

mem_len = 10

# Load Datasets

with open("") as f:


class BERT():
    def __init__(self):

    def forward():


def train(device_id):

    train_input_fn, record_info_dict = data_utils.get_input_fn(

    )

    tf.logging.info("num of batches {}".format(record_info_dict["num_batch"]))
    bsz_per_core = train_batch_size // num_core_per_host

    params = {
        "batch_size": train_batch_size
    }
    train_set = train_input_fn(params)
    example = train_set.make_one_shot_iterator().get_next()

    if num_core_per_host > 1:
        examples = [{} for _ in range(num_core_per_host)]
        for key in example.keys():
            vals = tf.split(example[key], num_core_per_host, 0)
            for device_id in range(num_core_per_host):
                examples[device_id][key] = vals[device_id]
    else:
        examples = [example]

    tower_means, tower_losses, tower_new_mems, tower_grads_and_vars = [], [], [], []

    for i in range(num_core_per_host):
        reuse = True if i > 0 else None
        with tf.device(assign_to_gpu(i, ps_device)), tf.variable_scope(tf.get_variable_scope(), reuse=reuse):
            mems_i = {}
            if FLAGS.mem_len:
                mems_i["mems"] = create_mems_tf(bsz_per_core)


def main(unused_argv):
    del unused_argv

    tf.logging.set_verbosity(tf.logging.INFO)

    n_token = data_utils.VOCAB_SIZE
    tf.logging.info("n_token {}".format(FLAGS.n_token))

    if not tf.gfile.Exists(model_dir):
        tf.gfile.MakeDirs(model_dir)

    train(device_id)

if __name__ == "__main__":
    tf.app.run()
