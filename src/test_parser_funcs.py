import unittest
from markdown_parser import *

class TestParserFuncs(unittest.TestCase):
    def test_split_nodes_delimiter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("code block", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))

    def test_split_nodes_delimiter_italics(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("italic block", TextType.ITALIC))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))

    def test_split_nodes_delimiter_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("bold block", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))

    def test_split_nodes_delimiter_italics_many1(self):
        node1 = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        node2 = TextNode("This is text without an italic block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("italic block", TextType.ITALIC))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode("This is text without an italic block word", TextType.TEXT))

    def test_split_nodes_delimiter_italics_many2(self):
        node1 = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        node2 = TextNode("bold block", TextType.BOLD)
        node3 = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2, node3], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 7)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("italic block", TextType.ITALIC))
        self.assertEqual(new_nodes[2], TextNode(" word", TextType.TEXT))
        self.assertEqual(new_nodes[3], TextNode("bold block", TextType.BOLD))
        self.assertEqual(new_nodes[4], TextNode("This is text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[5], TextNode("italic block", TextType.ITALIC))
        self.assertEqual(new_nodes[6], TextNode(" word", TextType.TEXT))

    def test_split_nodes_delimiter_italics_many3(self):
        node1 = TextNode("_This_ is text with multiple _italic block_ words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 4)
        self.assertEqual(new_nodes[0], TextNode("This", TextType.ITALIC))
        self.assertEqual(new_nodes[1], TextNode(" is text with multiple ", TextType.TEXT))
        self.assertEqual(new_nodes[2], TextNode("italic block", TextType.ITALIC))
        self.assertEqual(new_nodes[3], TextNode(" words", TextType.TEXT))

    def test_split_nodes_delimiter_wo_leading(self):
        node = TextNode("**bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0], TextNode("bold block", TextType.BOLD))
        self.assertEqual(new_nodes[1], TextNode(" word", TextType.TEXT))

    def test_split_nodes_delimiter_wo_trailing(self):
        node = TextNode("This is text with a **bold block**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 2)
        self.assertEqual(new_nodes[0], TextNode("This is text with a ", TextType.TEXT))
        self.assertEqual(new_nodes[1], TextNode("bold block", TextType.BOLD))

    def test_split_nodes_delimiter_wo_leading_trailing(self):
        node = TextNode("**bold block**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], TextNode("bold block", TextType.BOLD))

    def test_split_nodes_delimiter_failure_1(self):
        node = TextNode("This is text with a **bold block", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)
    
    def test_split_nodes_delimiter_failure_2(self):
        node1 = TextNode("_This_ is text with multiple _italic block words", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node1], "_", TextType.ITALIC)

if __name__ == "__main__":
    unittest.main()