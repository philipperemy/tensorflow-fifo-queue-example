import multiprocessing
import threading
import time
import numpy as np
import tensorflow as tf


def load_data():
    # custom it with your data loader here.
    for i in xrange(10000):
        yield np.random.uniform(size=(29))


class DataGenerator(object):
    def __init__(self,
                 coord,
                 max_queue_size=32):
        # Change the shape of the input data here with the parameter shapes.
        self.max_queue_size = max_queue_size
        self.queue = tf.FIFOQueue(max_queue_size, ['float32'], shapes=[29])
        self.queue_size = self.queue.size()
        self.threads = []
        self.coord = coord
        self.sample_placeholder = tf.placeholder(dtype=tf.float32, shape=[29])
        self.enqueue = self.queue.enqueue([self.sample_placeholder])

    def dequeue(self, num_elements):
        output = self.queue.dequeue_many(num_elements)
        return output

    def thread_main(self, sess):
        stop = False
        while not stop:
            iterator = load_data()
            for data in iterator:
                while self.queue_size.eval(session=sess) == self.max_queue_size:
                    if self.coord.should_stop():
                        break
                    time.sleep(0.02)
                if self.coord.should_stop():
                    stop = True
                    print("Process -1 receive stop request.")
                    break
                sess.run(self.enqueue, feed_dict={self.sample_placeholder: data})

    def start_threads(self, sess, n_threads=1):
        for _ in range(n_threads):
            thread = threading.Thread(target=self.thread_main, args=(sess, ))
            thread.daemon = True  # Thread will close when parent quits.
            thread.start()
            self.threads.append(thread)
        return self.threads
