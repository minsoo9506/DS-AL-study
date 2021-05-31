import csv
import math
from decisiontreenode import Node
from voterecord import Record


class DecisionTree:
    def __init__(self, records):
        self.root = Node(0,records)

    def performID3(self, node = None):
        if node == None:
            node = self.root
        node.splitNode()
        for key in node.children.keys():
            if 0 in node.children[key].stat.values():
                pass
            else:
                self.performID3(node.children[key])
        return node

    def classify(self, test):
        types = Record.types
        currentNode = self.root
        while True:
            child = currentNode.children[test[currentNode.decisionAttribute]]
            if child.blnSplit == False:
                result = None
                for type in types:
                    if child.stat[type] > 0:
                        result = type
                        break
                break
            else:
                currentNode = child
        print('Test Data : ',test,', Classification : ', result)

    def __str__(self):
        ret = str(self.root)
        return ret

if __name__ == "__main__":
    csvfile = open('house-votes-84.csv', 'rt')
    reader = csv.reader(csvfile, delimiter=',')
    records = []

    for row in reader:
        record = Record(row)
        records.append(record)

    tree = DecisionTree(records)
    tree.performID3()
    print(tree)
    
    test = ['y', 'y', '?', 'y', 'n', '?', '?', '?', 'n', 'n', 'n', 'y', 'n', '?', 'y', 'n']
    
    # classify
    tree.classify(test)