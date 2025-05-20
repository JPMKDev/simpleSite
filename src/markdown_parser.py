from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if len(split_text) % 2 != 1:
            raise Exception(f"Missing closing {delimiter} from {node.text}")
        for i in range(len(split_text)):
            block_len = len(split_text[i])
            if i%2 == 0 and block_len>0:
                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
            elif block_len > 0:
                new_nodes.append(TextNode(split_text[i], text_type))
    return new_nodes