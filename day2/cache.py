import sys
from hash_table import HashTable

# Implement a data structure that stores the most recently accessed N pages.
# See the below test cases to see how it should work.
#
# Note: Please do not use a library like collections.OrderedDict). The goal is
#       to implement the data structure yourself!

class Node:
    def __init__(self, url):
        self.url = url
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #search the node which has the url you're trying to access to.
    def search_node(self, url):
        current_node = self.head
        while current_node:
            if current_node.url == url:
                return current_node
            current_node = current_node.next
        return None
    
    # add the node at the front of the doubly linked list
    def add_node_to_front(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node
            node.prev = None
            self.head = node
        else:
            node.next = node.prev = None
            self.head = self.tail = node
    
    # delete node from the doubly linked list
    def delete_node(self, node):
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.next:
            self.head = node.next
            self.head.prev = None
        elif node.prev:
            self.tail = node.prev
            self.tail.next = None
        else:
            self.head = self.tail = None
    
    # move the node to the front
    def move_to_front(self, node):
        tmp_node = node
        self.delete_node(node)
        self.add_node_to_front(tmp_node)
    
        
class Cache:
    # Initialize the cache.
    # |n|: The size of the cache.
    def __init__(self, n):
        self.url_list = DoublyLinkedList()
        self.hash_table = HashTable()
        self.cache_size = 0
        self.max_cache_size = n
        pass
    
    
    # Access a page and update the cache so that it stores the most recently
    # accessed N pages. This needs to be done with mostly O(1).
    # |url|: The accessed URL
    # |contents|: The contents of the URL
    def access_page(self, url, contents):
        url_list = self.url_list
        searched_node = url_list.search_node(url)
        if searched_node is None:
            url_list.add_node_to_front(Node(url))
            self.hash_table.put(url, contents)
            self.cache_size += 1
            self.check_cache_size()
        else:
            url_list.move_to_front(searched_node)
        pass
    
    def check_cache_size(self):
        url_list = self.url_list
        if self.cache_size > self.max_cache_size:
            self.hash_table.delete(url_list.tail.url)
            url_list.delete_node(url_list.tail)
            self.cache_size -= 1

    # Return the URLs stored in the cache. The URLs are ordered in the order
    # in which the URLs are mostly recently accessed.
    def get_pages(self):
        urls = []
        current_node = self.url_list.head
        while current_node:
            urls.append(current_node.url)
            current_node = current_node.next
        return urls
        pass


def cache_test():
    # Set the size of the cache to 4.
    cache = Cache(4)

    # Initially, no page is cached.
    assert cache.get_pages() == []

    # Access "a.com".
    cache.access_page("a.com", "AAA")
    # "a.com" is cached.
    assert cache.get_pages() == ["a.com"]

    # Access "b.com".
    cache.access_page("b.com", "BBB")
    # The cache is updated to:
    #   (most recently accessed)<-- "b.com", "a.com" -->(least recently accessed)
    assert cache.get_pages() == ["b.com", "a.com"]

    # Access "c.com".
    cache.access_page("c.com", "CCC")
    # The cache is updated to:
    #   (most recently accessed)<-- "c.com", "b.com", "a.com" -->(least recently accessed)
    assert cache.get_pages() == ["c.com", "b.com", "a.com"]

    # Access "d.com".
    cache.access_page("d.com", "DDD")
    # The cache is updated to:
    #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
    assert cache.get_pages() == ["d.com", "c.com", "b.com", "a.com"]

    # Access "d.com" again.
    cache.access_page("d.com", "DDD")
    # The cache is updated to:
    #   (most recently accessed)<-- "d.com", "c.com", "b.com", "a.com" -->(least recently accessed)
    assert cache.get_pages() == ["d.com", "c.com", "b.com", "a.com"]

    # Access "a.com" again.
    cache.access_page("a.com", "AAA")
    # The cache is updated to:
    #   (most recently accessed)<-- "a.com", "d.com", "c.com", "b.com" -->(least recently accessed)
    assert cache.get_pages() == ["a.com", "d.com", "c.com", "b.com"]

    cache.access_page("c.com", "CCC")
    assert cache.get_pages() == ["c.com", "a.com", "d.com", "b.com"]
    cache.access_page("a.com", "AAA")
    assert cache.get_pages() == ["a.com", "c.com", "d.com", "b.com"]
    cache.access_page("a.com", "AAA")
    assert cache.get_pages() == ["a.com", "c.com", "d.com", "b.com"]

    # Access "e.com".
    cache.access_page("e.com", "EEE")
    # The cache is full, so we need to remove the least recently accessed page "b.com".
    # The cache is updated to:
    #   (most recently accessed)<-- "e.com", "a.com", "c.com", "d.com" -->(least recently accessed)
    assert cache.get_pages() == ["e.com", "a.com", "c.com", "d.com"]

    # Access "f.com".
    cache.access_page("f.com", "FFF")
    # The cache is full, so we need to remove the least recently accessed page "c.com".
    # The cache is updated to:
    #   (most recently accessed)<-- "f.com", "e.com", "a.com", "c.com" -->(least recently accessed)
    assert cache.get_pages() == ["f.com", "e.com", "a.com", "c.com"]

    # Access "e.com".
    cache.access_page("e.com", "EEE")
    # The cache is updated to:
    #   (most recently accessed)<-- "e.com", "f.com", "a.com", "c.com" -->(least recently accessed)
    assert cache.get_pages() == ["e.com", "f.com", "a.com", "c.com"]

    # Access "a.com".
    cache.access_page("a.com", "AAA")
    # The cache is updated to:
    #   (most recently accessed)<-- "a.com", "e.com", "f.com", "c.com" -->(least recently accessed)
    assert cache.get_pages() == ["a.com", "e.com", "f.com", "c.com"]

    print("Tests passed!")


if __name__ == "__main__":
    cache_test()
