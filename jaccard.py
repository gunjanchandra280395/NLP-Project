import tensorflow as tf;
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = tf.placeholder(tf.float32)
a={1,2,3,4,5,6,7,8,9};
b={1,4,7};
#a={1 2 3 4 5 6 7 8 9};
#b={1 5 7};
c=intersection(a,b);
sess=tf.Session()
result=sess.run(c)
print("Add:%s"%(result))
