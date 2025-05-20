import unittest

from htmlnode import *



class TestTextNode(unittest.TestCase):
    def test_props_to_html_1(self):
        node = HTMLNode(tag="h2", props={ "href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_props_to_html_2(self):
        node = HTMLNode(tag="h2", props={ "href": "https://www.google.com","target": "_blank", "extra": "another attribute"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\" extra=\"another attribute\"")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "I am a header", props={ "href": "https://www.google.com","target": "_blank", "extra": "another attribute"})
        self.assertEqual(node.to_html(), "<h1 href=\"https://www.google.com\" target=\"_blank\" extra=\"another attribute\">I am a header</h1>")
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        
    def test_complex_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], props={ "href": "https://www.google.com","target": "_blank",})
        self.assertEqual(parent_node.to_html(), "<div href=\"https://www.google.com\" target=\"_blank\"><span>child</span></div>")
        
    def test_to_html_with_complex_children(self):
        child_node = LeafNode("span", "child", props={ "href": "https://www.google.com","target": "_blank",})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span href=\"https://www.google.com\" target=\"_blank\">child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_many_children(self):
        child_node1 = LeafNode("b", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>child1</b><span>child2</span></div>")

if __name__ == "__main__":
    unittest.main()