from __future__ import print_function

import time

import tensorflow as tf

from data import DataGenerator


def define_net(input_batch):
    return input_batch + 20  # simplest network I could think of.


def main():
    batch_size = 1

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
        # That's the reason why size of the queue is almost always equal to 32.
        print('size queue =', sess.run(reader.size()))
        print(sess.run(net))
        time.sleep(3) # Make this thread slow.

    coord.request_stop()
    coord.join(threads)


if __name__ == '__main__':
    main()
