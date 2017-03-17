"""Training script for the WaveNet network on the VCTK corpus.

This script trains a network with the WaveNet using data from the VCTK corpus,
which can be freely downloaded at the following site (~10 GB):
http://homepages.inf.ed.ac.uk/jyamagis/page3/page58/page58.html
"""

from __future__ import print_function

import time

import tensorflow as tf

from data import DataGenerator


def define_net(input_batch):
    return input_batch + 20


def main():
    batch_size = 1

    # Create coordinator.
    coord = tf.train.Coordinator()

    with tf.name_scope('create_inputs'):
        reader = DataGenerator(coord)
        input_batch = reader.dequeue(batch_size)

    sess = tf.Session(config=tf.ConfigProto(log_device_placement=False))
    init = tf.global_variables_initializer()
    sess.run(init)

    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    reader.start_threads(sess)

    net = define_net(input_batch)

    for step in range(int(1e9)):
        # The queue is filled faster than what the main thread can unstack.
        print('size queue =', sess.run(reader.size()))
        print(sess.run(net))
        time.sleep(3)

    coord.request_stop()
    coord.join(threads)


if __name__ == '__main__':
    main()
