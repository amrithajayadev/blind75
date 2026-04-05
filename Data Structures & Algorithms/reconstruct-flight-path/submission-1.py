class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        1. Create adjacency list from src->dest(s) and a map to keep the frequency of each city occurence
        2. Sort each list 
        3. Do DFS to create a path
        """
        # 1. Build the graph with sorted destinations (lexicographical order)
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
            
        res = []

        def dfs(city):
            # 2. While there are available flights from this city
            while graph[city]:
                # Pop the lexicographically smallest destination
                next_city = graph[city].pop()
                dfs(next_city)
            
            # 3. Add to result after all neighbors are visited (Post-order)
            res.append(city)

        dfs("JFK")
        
        # 4. The path is built backwards, so reverse it
        return res[::-1]
            

