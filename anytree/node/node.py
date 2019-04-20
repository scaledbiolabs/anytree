# -*- coding: utf-8 -*-

from .nodemixin import NodeMixin
from .util import _repr


class Node(NodeMixin, object):

    def __init__(self, gate, name, index, parent=None, children=None, **kwargs):
        u"""
        A simple tree node with a `name` and any `kwargs`.

        The `parent` attribute refers the parent node:

        >>> from anytree import Node, RenderTree
        >>> root = Node("root")
        >>> s0 = Node("sub0", parent=root)
        >>> s0b = Node("sub0B", parent=s0, foo=4, bar=109)
        >>> s0a = Node("sub0A", parent=s0)
        >>> s1 = Node("sub1", parent=root)
        >>> s1a = Node("sub1A", parent=s1)
        >>> s1b = Node("sub1B", parent=s1, bar=8)
        >>> s1c = Node("sub1C", parent=s1)
        >>> s1ca = Node("sub1Ca", parent=s1c)

        >>> print(RenderTree(root))
        Node('/root')
        ├── Node('/root/sub0')
        │   ├── Node('/root/sub0/sub0B', bar=109, foo=4)
        │   └── Node('/root/sub0/sub0A')
        └── Node('/root/sub1')
            ├── Node('/root/sub1/sub1A')
            ├── Node('/root/sub1/sub1B', bar=8)
            └── Node('/root/sub1/sub1C')
                └── Node('/root/sub1/sub1C/sub1Ca')

        The same tree can be constructed by using the `children` attribute:

        >>> root = Node("root", children=[
        ...     Node("sub0", children=[
        ...         Node("sub0B", bar=109, foo=4),
        ...         Node("sub0A", children=None),
        ...     ]),
        ...     Node("sub1", children=[
        ...         Node("sub1A"),
        ...         Node("sub1B", bar=8, children=[]),
        ...         Node("sub1C", children=[
        ...             Node("sub1Ca"),
        ...         ]),
        ...     ]),
        ... ])

        >>> print(RenderTree(root))
        Node('/root')
        ├── Node('/root/sub0')
        │   ├── Node('/root/sub0/sub0B', bar=109, foo=4)
        │   └── Node('/root/sub0/sub0A')
        └── Node('/root/sub1')
            ├── Node('/root/sub1/sub1A')
            ├── Node('/root/sub1/sub1B', bar=8)
            └── Node('/root/sub1/sub1C')
                └── Node('/root/sub1/sub1C/sub1Ca')
        """
        self.__dict__.update(kwargs)
        self.gate = gate
        self.name = name
        self.parent = parent
        self.index = set(index)
        if children:
            self.children = children

        
        # ADDED BY B. GRIFFEN (brendan.f.griffen@gmail.com) 20190320

        if self.parent == None:
            self.id = 0
        else:
            all_node_ids = [node.id for node in self.root.descendants if hasattr(node,'id')]
            if len(all_node_ids) == 0:
                self.id = 1
            else:
                self.id = max(all_node_ids) + 1
        

    def __repr__(self):
        args = ["%r" % self.separator.join([""] + [str(node.name) for node in self.path])]
        return _repr(self, args=args, nameblacklist=["name"])
