"""
 Copyright (c) 2018 Intel Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

import networkx as nx
import numpy as np

from mo.graph.graph import Node
from mo.ops.op import Op


class Tile(Op):
    op = 'Tile'
    enabled = True

    def __init__(self, graph: nx.MultiDiGraph, attrs: dict):
        super().__init__(graph, {
            'kind': 'op',
            'type': __class__.op,
            'op': __class__.op,
            'infer': Tile.infer
        }, attrs)

    def supported_attrs(self):
        return ['axis', 'tiles']

    @staticmethod
    def infer(node: Node):
        shape = node.in_node().shape
        if shape is None:
            return
        shape = np.copy(shape)
        shape[node.axis] = shape[node.axis] * node.tiles
        node.out_node().shape = shape
