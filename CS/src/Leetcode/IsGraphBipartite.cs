// 785. Is Graph Bipartite?


using System.Collections.Generic;
using System.Linq;

namespace Leetcode
{
    public partial class Algorithm
    {
        public static bool IsBipartite(int[][] graph)
        {
            var colors = Enumerable.Repeat(-1, graph.Length).ToArray();
            var q = new Queue<int>();

            for (var i = 0; i < graph.Length; i++)
            {
                if (colors[i] == -1)
                {
                    q.Enqueue(i);
                    colors[i] = 1;
                    while (q.Count > 0)
                    {
                        var u = q.Dequeue();

                        foreach (var v in graph[u])
                        {
                            if (colors[v] == colors[u])
                                return false;
                            if (colors[v] == -1)
                            {
                                colors[v] = 1 - colors[u];
                                q.Enqueue(v);
                            }
                        }
                    }
                }
            }

            return true;
        }

    }
}