class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, next_node):
        self.next_node = next_node


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node:
            if current_node.get_value() is not None:
                string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()

        # The head node is to be removed
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        # Traverse nodes until find the next node has the target value
        else:
            while current_node:
                next_node = current_node.get_next_node()
                # check next nodes' value is the target value
                if ((next_node is not None) and
                        (next_node.get_value() == value_to_remove)):
                    # if yes, change current nodes' next node reference.
                    current_node.set_next_node(next_node.get_next_node())
                    # end loop
                    current_node = None
                else:
                    current_node = next_node

    def remove_all_occur(self, value_to_remove):
        """
        remove all the occurence of the value_to_remove
        """
        current_node = self.head_node
        # Traverse nodes until find the next node has the target value
        while current_node:
            if current_node.get_value() == value_to_remove:
                self.head_node = current_node.get_next_node()
                current_node = self.head_node
            else:
                next_node = current_node.get_next_node()
                # check next nodes' value is the target value
                if ((next_node is not None) and
                        (next_node.get_value() == value_to_remove)):
                    # if yes, change current nodes' next node reference.
                    current_node.set_next_node(next_node.get_next_node())
                    # continue until remove all the target values
                else:
                    current_node = next_node


def test_linked_list():
    a = LinkedList(4)
    for _ in range(3):
        a.insert_beginning(5)
    for _ in range(3):
        a.insert_beginning(4)
    print(a.stringify_list())
    a.remove_all_occur(4)
    print('after removed 4')
    print(a.stringify_list())

    b = LinkedList(2)
    for _ in range(3):
        b.insert_beginning(2)
    print(b.stringify_list())
    b.remove_node(4)
    print(b.stringify_list())


if __name__ == '__main__':
    test_linked_list()
