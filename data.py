import threading

import numpy as np
import tensorflow as tf


def load_data():
    # custom it with your data loader here.
    for i in range(int(1e9)):
        yield np.random.uniform(size=(5, 5))


class DataGenerator(object):
    def __init__(self,
                 coord,
                 queue_size=32):
        # Change the shape of the input data here with the parameter shapes.
        self.queue = tf.PaddingFIFOQueue(queue_size, ['float32'], shapes=[(None, None)])
        self.threads = []
        self.coord = coord
        self.sample_placeholder = tf.placeholder(dtype=tf.float32, shape=None)
        self.enqueue = self.queue.enqueue([self.sample_placeholder])

    def size(self):
        return self.queue.size()

    def dequeue(self, num_elements):
        output = self.queue.dequeue_many(num_elements)
        return output

    def thread_main(self, sess):
        stop = False
        while not stop:
            iterator = load_data()
            for data in iterator:
                if self.coord.should_stop():
                    stop = True
                    break
                sess.run(self.enqueue, feed_dict={self.sample_placeholder: data})

    def start_threads(self, sess, n_threads=1):
        for _ in range(n_threads):
            thread = threading.Thread(target=self.thread_main, args=(sess,))
            thread.daemon = True  # Thread will close when parent quits.
            thread.start()
            self.threads.append(thread)
        return self.threads
