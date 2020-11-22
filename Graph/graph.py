
class graph:

    def __init__(self):
        self.graph = dict()

    def add_edge(self, s, d):
        
        if self.graph.get(s):
            self.graph.get(s).append(d)
        else:
            self.graph[s] = [d]

    def __str__(self):
        return str(self.graph)

    def DFS(self, u, visited):

        if u not in visited:
            print(u, end=" ")

        visited.append(u)

        # print(self.graph.get(u), end=" ")

        if self.graph.get(u):
            for i in self.graph.get(u):
                # print(i, end=' ')
                if i not in visited:
                    # check.remove(i)
                    # print(u, end='')
                    self.DFS(i, visited)


def main():
    
    print('--------------START-------------')

    g0 = graph()

    user = 'A B,B A,C A,D S,B F,F G'.split(',')

    for i in user:

        g0.add_edge(i.split()[0], i.split()[1])

    print(g0)

    check = [i for i in g0.graph]
    
    visited = []

    for i in check:
        g0.DFS(i, visited)



if __name__ == "__main__":
    main()