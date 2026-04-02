class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        
        // STEP 1: Create a hashmap that counts the frequency of each element.
        unordered_map<int, int> frequencyCounter; // (key: element, value: frequency) 

        // STEP 2: Iterate over the vector "nums" and start recording frequency.
        for (const auto& element : nums)
        {
            frequencyCounter[element]++;
        }

        // STEP 3: Take the hashmap and convert it into an array, sorting by frequency in DESCENDING order.
        vector<pair<int, int>> arr;

        for (const auto& p : frequencyCounter)
        {
            arr.push_back({p.second, p.first});
        }

        sort(arr.rbegin(), arr.rend());

        // STEP 4: Iterate "k" times starting from the beginning to add the most frequent elements to the result vector.
        vector<int> result;

        for (int i = 0; i < k; i++)
        {
            result.push_back(arr[i].second);
        }

        return result;
    }
};
