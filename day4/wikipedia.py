import sys
from collections import deque
import copy


class ReversedLinkedList:
    def __init__(self, previous, id):
        self.previous = previous
        self.id = id

class Wikipedia:

    # Initialize the graph of pages.
    def __init__(self, pages_file, links_file):

        # A mapping from a page ID (integer) to the page title.
        # For example, self.titles[1234] returns the title of the page whose
        # ID is 1234.
        self.titles = {}

        # A set of page links.
        # For example, self.links[1234] returns an array of page IDs linked
        # from the page whose ID is 1234.
        self.links = {}

        # Read the pages file into self.titles.
        with open(pages_file) as file:
            for line in file:
                (id, title) = line.rstrip().split(" ")
                id = int(id)
                assert not id in self.titles, id
                self.titles[id] = title
                self.links[id] = []
        print("Finished reading %s" % pages_file)

        # Read the links file into self.links.
        with open(links_file) as file:
            for line in file:
                (src, dst) = line.rstrip().split(" ")
                (src, dst) = (int(src), int(dst))
                assert src in self.titles, src
                assert dst in self.titles, dst
                self.links[src].append(dst)
        print("Finished reading %s" % links_file)
        print()


    # Example: Find the longest titles.
    def find_longest_titles(self):
        titles = sorted(self.titles.values(), key=len, reverse=True)
        print("The longest titles are:")
        count = 0
        index = 0
        while count < 15 and index < len(titles):
            if titles[index].find("_") == -1:
                print(titles[index])
                count += 1
            index += 1
        print()


    # Example: Find the most linked pages.
    def find_most_linked_pages(self):
        link_count = {}
        for id in self.titles.keys():
            link_count[id] = 0

        for id in self.titles.keys():
            for dst in self.links[id]:
                link_count[dst] += 1

        print("The most linked pages are:")
        link_count_max = max(link_count.values())
        for dst in link_count.keys():
            if link_count[dst] == link_count_max:
                print(self.titles[dst], link_count_max)
        print()


    # Homework #1: Find the shortest path.
    # 'start': A title of the start page.
    # 'goal': A title of the goal page.
    def find_shortest_path(self, start, goal):
        start_id = self.find_page_id(start)
        if start_id == -1:
            return "NOT FOUND"
        queue = deque()
        seen = set(start) #見たページのタイトルを入れる
        trace_list = ReversedLinkedList(None, start_id) 
        queue.append(trace_list) #連結リストをキューに入れていく
        while queue:
            node = queue.popleft()
            if self.titles[node.id] == goal:
                path_id = self.print_path(node)
                return path_id #通ってきたページのidの配列を返す
            links = self.links[node.id] #つながっているページのidの配列
            for link in links:
                if self.titles[link] not in seen:
                    seen.add(self.titles[link])
                    queue.append(ReversedLinkedList(node, link)) 
        return []
    
    def find_page_id(self, target_title):
        target_id = [k for k, v in self.titles.items() if v == target_title]
        if target_id:
            return target_id[0]
        return -1
    
    def print_path(self, trace_list: ReversedLinkedList):
        path_id = []
        current = trace_list
        while current:
            path_id.append(current.id)
            current = current.previous
        print("Found path is: ")
        for id in path_id[::-1]:
            print(f" -> [{self.titles[id]}]", end="")
        return path_id[::-1]
            
    # Homework #2: Calculate the page ranks and print the most popular pages.
    def find_most_popular_pages(self):
        isConverged = False
        page_ranks = self.init_page_rank()
        iteration = 0
        while not isConverged:
            page_ranks, old_page_ranks = self.update_page_rank(page_ranks)
            print("Update page rank done")
            isConverged, diff_sum = self.check_converged(page_ranks, old_page_ranks)
            iteration += 1
            if iteration % 10 == 0:
                print("diff: ", diff_sum)
        self.find_top_10_pages(page_ranks)

    #全てのノードに初期値1を与える
    def init_page_rank(self):
        page_ranks = {}
        for key in (self.titles.keys()):
            page_ranks[key] = 1.0
        print("initial page ranks: ", page_ranks)
        return page_ranks
    
    # 各ノードのページランクを、random surfer modelを用いて更新する
    def update_page_rank(self, page_ranks):
        old_page_ranks = copy.deepcopy(page_ranks)
        distributions = {}
        for key in (page_ranks.keys()):
            distributions[key] = 0.0 
        page_ranks = self.random_surfer_model(page_ranks, old_page_ranks, distributions)
        self.print_page_rank_sum(page_ranks)
        return page_ranks, old_page_ranks
    
    #random surfer modelの実装(上手くいった方)
    def random_surfer_model(self, page_ranks, old_page_ranks, distributions):
        N = len(page_ranks)
        keys = list(page_ranks.keys())
        
        #隣接するページを持たないページのページランクの合計を出し、0.85倍し、Nで割る
        no_linked_page_node_sum = sum(old_page_ranks[key] for key in keys if len(self.links[key]) == 0) * 0.85 / N
        
        #隣接するページを持つページランクの合計を出し、0.15倍し、Nで割る
        linked_page_nodes_sum = sum(old_page_ranks[key] for key in keys) * 0.15 / N
        
        #全ノードにno_linked_page_node_sumからの分配と、15%分配を事前に加える
        for target_key in keys:
            distributions[target_key] += no_linked_page_node_sum + linked_page_nodes_sum

        #隣接ページを持つページランクの分配
        for key in keys:
            if len(self.links[key]) > 0:
                distribution = old_page_ranks[key] * 0.85 / len(self.links[key])
                for out_key in self.links[key]:
                    distributions[out_key] += distribution

        return distributions
        
    #random surfer modelの実装(遅い)
    def old_random_surfer_model(self, page_ranks, old_page_ranks, distributions):
        for key in page_ranks.keys():
            if len(self.links[key]) == 0: #隣接するページがないときは、全てのページにページランクを均等に分配する
                contribution = old_page_ranks[key] / len(page_ranks)
                for target_key in page_ranks.keys():
                    distributions[target_key] += contribution  ##ここでものすごく時間がかかる
            else: #そのページが持つページランクの85％を隣接するページに均等に分配し、残り15%を全体に均等に分配する 全体に分配するものをまとめたい....
                distribution = (old_page_ranks[key]*0.85) / len(self.links[key])
                contribution = (old_page_ranks[key]*0.15) / len(page_ranks)
                for key in self.links[key]:
                    distributions[key] +=  distribution
                for target_key in page_ranks.keys():
                    distributions[target_key] += contribution
        page_ranks = distributions
        return page_ranks

    #収束するかチェック
    def check_converged(self,page_ranks, old_page_ranks):
        isConverged = False
        diff_sum = 0
        for key in (page_ranks.keys()):
            diff_sum += (page_ranks[key] - old_page_ranks[key]) ** 2
        if diff_sum < 0.01:
            isConverged = True
        return isConverged, diff_sum
    
    #ページランクの高い上位10ページを見つける
    def find_top_10_pages(self, page_ranks):
        ranks = []
        print(page_ranks)
        for i, key in enumerate(page_ranks.keys()):
            ranks.append((key, page_ranks[key]))
        ranks = sorted(ranks, reverse=True, key=lambda rank_tuple: rank_tuple[1])
        for rank in ranks[:10]:
            print(self.titles[rank[0]])
        
    #ページランクの合計値を計算(デバッグ用)
    def print_page_rank_sum(self, page_ranks):
        rank_sum = 0
        for key in (page_ranks.keys()):
            rank_sum += page_ranks[key]
        print("ページランクの合計値: ", rank_sum)
        
    # Homework #3 (optional):
    # Search the longest path with heuristics.
    # 'start': A title of the start page.
    # 'goal': A title of the goal page.
    # まず最短経路を見つけて、そこからどんどん寄り道していくイメージで考えました
    def find_longest_path(self, start, goal):
        #まず一本パスを通す(最短経路)
        shortest_path_id = self.find_shortest_path(start, goal)
        
        #A->B->C->Dのようなパスが得られたら、
        #A->Cにいく別のパスをDFSで探し、一番経路の長いものを採用
        #A->E->R->C->Dになったとする
        #次は、E→Dにいく別のパスを探す
        # longer_path_id = [shortest_path_id[0]]
        # long_sub_path = []
        # index = 0
        # for id in shortest_path_id[2:]:
        #     long_sub_path = self.dfs(longer_path_id[index], self.titles[id]) #DFSで一番長かったものを選ぶ
        #     print("long sub path is: ", long_sub_path)
        #     longer_path_id.append(long_sub_path[1:3])
        #     index += 1
        # longer_path_id.append(long_sub_path[3:])
        longer_path_id = self.dfs(start, goal)
        print("経路長: ", len(longer_path_id))
        
        pass
    
    #深さ優先探索で、最も長い経路を返す
    def dfs(self, start, goal):
        start_id = self.find_page_id(start)
        stack = deque()
        seen = set(start) #見たページのタイトルを入れる
        trace_list = ReversedLinkedList(None, start_id) 
        stack.append(trace_list) #連結リストをキューに入れていく
        path_id = []
        while stack:
            # print(stack)
            node = stack.pop()
            if self.titles[node.id] == goal:
                current_path = self.print_path(node)
                path_id = current_path if len(current_path) > len(path_id) else path_id
                return path_id #通ってきたページのidの配列を返す
            links = self.links[node.id] #つながっているページのidの配列
            for link in links:
                if self.titles[link] not in seen:
                    seen.add(self.titles[link])
                    stack.append(ReversedLinkedList(node, link)) 
        return []
    
        pass


    # Helper function for Homework #3:
    # Please use this function to check if the found path is well formed.
    # 'path': An array of page IDs that stores the found path.
    #     path[0] is the start page. path[-1] is the goal page.
    #     path[0] -> path[1] -> ... -> path[-1] is the path from the start
    #     page to the goal page.
    # 'start': A title of the start page.
    # 'goal': A title of the goal page.
    def assert_path(self, path, start, goal):
        assert(start != goal)
        assert(len(path) >= 2)
        assert(self.titles[path[0]] == start)
        assert(self.titles[path[-1]] == goal)
        for i in range(len(path) - 1):
            assert(path[i + 1] in self.links[path[i]])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: %s pages_file links_file" % sys.argv[0])
        exit(1)

    wikipedia = Wikipedia(sys.argv[1], sys.argv[2])
    # Example
    # wikipedia.find_longest_titles()
    # Example
    # wikipedia.find_most_linked_pages()
    # Homework #1
    # wikipedia.find_shortest_path("渋谷", "パレートの法則")
    # wikipedia.find_shortest_path("A", "F")
    # Homework #2
    wikipedia.find_most_popular_pages()
    # Homework #3 (optional)
    # wikipedia.find_longest_path("渋谷", "池袋")
