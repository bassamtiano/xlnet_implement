import math
import re
import random

import tensorflow as tf
import numpy as np

# Parameters

device_id = "/gpu:0"

model_dir = "./data/models"

# Load Datasets

with open("") as f:


class BERT():
    def __init__(self):

    def forward():


def train(device_id):

    train_input_fn


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
