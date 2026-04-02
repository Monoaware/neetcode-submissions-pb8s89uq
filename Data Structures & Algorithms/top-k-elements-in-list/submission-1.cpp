class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        // STEP 1: Record the frequency of each element.
        unordered_map<int, int> count;

        for (int num : nums) 
        {
            count[num]++;
        }

        // STEP 2: Create a priority_queue to generate a minimum heap.
        priority_queue<pair<int, int>, vector<pair<int, int>>, 
        greater<pair<int, int>>> heap;

        // STEP 3: Loop through each element-frequency record and store it to the heap (with frequncy coming first).
        for (auto& entry : count)
        {
            heap.push({entry.second, entry.first});

            if (heap.size() > k)
            {
                heap.pop();
            }
        }

        // 
        vector<int> res;
        
        for (int i = 0; i < k; i++)
        {
            res.push_back(heap.top().second);
            heap.pop();
        }

        return res;
    }
};
