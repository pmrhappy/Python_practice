import imp

if __name__ == '__main__':
    tree = imp.load_source('tree.Worm', 'wood/brookeside/tree.py')
    tree.Worm().crow()
