import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq1(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
    def test_eq3(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
        
    def test_eq4(self):
        node = TextNode("This is an image node", TextType.IMAGE, "url/to/image")
        node2 = TextNode("This is an image node", TextType.IMAGE, "url/to/image")
        self.assertEqual(node, node2)
        
    def test_eq5(self):
        node = TextNode("This is an image node", TextType.IMAGE, "url/to/different/image")
        node2 = TextNode("This is an image node", TextType.IMAGE, "url/to/image")
        self.assertNotEqual(node, node2)
        
    def test_eq6(self):
        node = TextNode("This is an image node", TextType.IMAGE,)
        node2 = TextNode("This is an image node", TextType.IMAGE, "url/to/image")
        self.assertNotEqual(node, node2)

    def test_text_to_html(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_to_html(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")

    def test_italic_to_html(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")

    def test_code_to_html(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")

    def test_link_to_html(self):
        node = TextNode("This is a link node", TextType.LINK, "url.to.follow")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href":"url.to.follow",})

    def test_image_to_html(self):
        node = TextNode("This is an image node", TextType.IMAGE, "url.to.follow")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"url.to.follow","alt":"This is an image node",})
    
    def test_to_html_failure(self):
        node = TextNode("filler", TextType.TEXT)
        node.text_type = "invalid"
        with self.assertRaises(TypeError):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()