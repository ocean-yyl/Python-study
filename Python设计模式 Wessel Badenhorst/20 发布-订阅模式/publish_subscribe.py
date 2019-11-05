#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:24544
# datetime:2019-10-29 14:45
# software: PyCharm

class Message(object):
	def __init__(self):
		self.payload = None
		self.topic = "all"


class Subscriber(object):
	def __init__(self, dispatcher, topic,name):
		dispatcher.subscribe(self, topic)
		self.name = name

	def process(self, message):
		print(self.name,"get Message:{}".format(message.payload))


class Publisher(object):
	def __init__(self, dispatcher):
		self.dispatcher = dispatcher

	def publish(self, message):
		self.dispatcher.send(message)


class Dispatcher(object):
	def __init__(self):
		self.topic_subscribers = dict()

	def subscribe(self, subscriber, topic):
		self.topic_subscribers.setdefault(topic, set()).add(subscriber)
		"""
		以上代码相当于:
		new_set = set()
		new_set.add(subscriber)
		self.topic_subscribers.get(topic)= self.topic_subscribers.get(topic)|new_set # 集合"并"操作
		"""
	def unsubscribe(self, subscriber, topic):
		self.topic_subscribers.setdefault(topic, set()).discard(subscriber)

	def unsubscribe_all(self, topic):
		self.subscribers = self.topic_subscribers[topic] = set()

	def send(self, message):
		try:
			for subscriber in self.topic_subscribers[message.topic]:
				subscriber.process(message)
		except KeyError as e:
			print("error: nobody has subscribed the topic:",message.topic)

def main():
	dispatcher = Dispatcher()

	pub_1 = Publisher(dispatcher)
	sub_1 = Subscriber(dispatcher, "topic1","sub_1")
	sub_2 = Subscriber(dispatcher, "topic2","sub_2")


	message = Message()
	message.payload = "hello sub1"
	message.topic = "topic1"
	pub_1.publish(message)

	pub_2 = Publisher(dispatcher)
	message = Message()
	message.payload = "hello sub2"
	message.topic = "topic2"
	pub_2.publish(message)

	pub_3 = Publisher(dispatcher)
	message = Message()
	message.payload = "hello sub3"
	message.topic = "topic3"
	pub_3.publish(message)

if __name__ == '__main__':
	main()
