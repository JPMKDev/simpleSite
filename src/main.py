from textnode import *
from htmlnode import *

def main():
    t1 = TextNode("t1 message", TextType.TEXT)
    t2 = TextNode("t2 message", TextType.BOLD)
    t3 = TextNode("img desc", TextType.IMAGE, "src.of.url.for.img")
    print(t1, t2, t3)

    hn1 = HTMLNode(tag="h1", value="header")
    hn2 = HTMLNode(tag="h2", props={ "href": "https://www.google.com","target": "_blank",}, children=[hn1])
    print(hn1)
    print(hn2)
    print(hn2.props_to_html())
    

main()