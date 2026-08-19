class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> heap;
        vector<bool> visited(n, false);
        heap.push({0, 0});
        int total = 0;
        int count = 0;

        while (!heap.empty() && count < n) {
            auto [dist, u] = heap.top();
            heap.pop();
            if (visited[u]) continue;

            visited[u] = true;
            total += dist;
            count++;

            for (int v = 0; v < n; v++) {
                if (!visited[v]) {
                    int d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1]);
                    heap.push({d, v});
                }
            }
        }
        return total;
    }
};