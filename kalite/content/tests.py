"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import *


class SimpleTest(TestCase):
	def test_treecreate(self):
		t = TopicTree()
		self.assertTrue(t)

	def test_nodeconstruct(self):
		n = Node()
		self.assertTrue(n)

	def test_nodedataconstruct(self):
		d = NodeData()
		self.assertTrue(d)

	def test_nodepublished(self):
		n = Node(published=True)
		self.assertTrue(n)

	def test_nodedeleted(self):
		n = Node(deleted=True)
		self.assertTrue(n)

	def test_nodeordered(self):
		n = Node(sort_order=1)
		self.assertTrue(n)

	def test_nodecombo(self):
		n = Node(published=True, deleted=True, sort_order=1)
		self.assertTrue(n)

	def test_draft(self):
		n = Node()
		d = Draft(publish_in=n)
		self.assertTrue(d)

	def test_content(self):
		c = Content()
		self.assertTrue(c)

	def test_contentauthor(self):
		c = Content(author='calvin')
		self.assertTrue(c)

	def test_contentowner(self):
		c = Content(author='calvin', license_owner='calvin')
		self.assertTrue(c)