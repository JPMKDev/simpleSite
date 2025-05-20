class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"<{self.tag} {self.props}>{self.value}\n{self.children}</{self.tag}>"

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        attributes = ""
        if self.props is None:
            return attributes
        for key in self.props:
            attributes += f" {key}=\"{self.props[key]}\""
        return attributes
    
class LeafNode(HTMLNode):
    def __init__(self, leaf_tag, leaf_value, props=None):
        super().__init__(tag=leaf_tag, value=leaf_value, props=props)

    def to_html(self):
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, parent_tag, parent_children, props=None):
        super().__init__(tag=parent_tag, children=parent_children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("parent without tag")
        if self.children is None:
            raise ValueError("parent has no children object")
        if len(self.children) == 0:
            raise ValueError("parent has no child")
        html_string = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html_string += child.to_html()
        html_string += f"</{self.tag}>"
        return html_string
