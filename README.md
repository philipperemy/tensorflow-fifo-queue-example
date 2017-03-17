# Tensorflow FIFO Queue example
### Example on how to use a Tensorflow Queue to feed data to your models. 
Compatible with Tensorflow 1.x. Please upgrade if you have Tensorflow 0.x.

<div align="center">
  <img src="https://www.tensorflow.org/images/tf_logo_transp.png" width="200"><br><br>
</div>
## How to use it?
```
git clone git@github.com:philipperemy/tensorflow-fifo-queue-example.git tf-queue
cd tf-queue
# make sure at least Tensorflow 1.0.1 is installed.
python main.py # to start the example which uses the Tensorflow queue.
```

## Output

```
size queue = 2
[[[ 20.68614197  20.15329361  20.39105034  20.90393257  20.8211174 ]
  [ 20.21601105  20.20680237  20.63046837  20.11518097  20.2508316 ]
  [ 20.362957    20.39513588  20.35568619  20.95798302  20.71342659]
  [ 20.58656502  20.94277954  20.59599304  20.31328011  20.04895973]
  [ 20.71495628  20.77456474  20.75753403  20.87974739  20.58901596]]]
size queue = 32
[[[ 20.00242424  20.91688347  20.93519402  20.9217968   20.38695526]
  [ 20.87318802  20.75139427  20.08540344  20.78540802  20.7677784 ]
  [ 20.1153717   20.56425858  20.81686783  20.97789001  20.55836296]
  [ 20.5869751   20.9584446   20.81368828  20.98579597  20.55318069]
  [ 20.02428436  20.96101379  20.37574196  20.5288887   20.97519875]]]
size queue = 32
[[[ 20.72234535  20.75441933  20.00969887  20.94854736  20.19271469]
  [ 20.01235771  20.57665443  20.37540245  20.1708107   20.77712822]
  [ 20.82086945  20.53391647  20.28100777  20.27137947  20.87246895]
  [ 20.63288879  20.74639893  20.88269043  20.81982231  20.77005577]
  [ 20.57556725  20.25545311  20.99351501  20.12363815  20.93238068]]]
  ```
  
  In this example, we define:
  - one pusher thread (data) - The data thread (could be more than 1 thread) is used to generate the data and push it to the queue.
  - one poller thread (model) - The model thread (should be 1) is used to pop the queue and process the data.
