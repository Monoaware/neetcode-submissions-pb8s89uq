class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        // STEP 1: Create a map to hold the sorted anagrams.
        unordered_map<string, vector<string>> anagramMap;

        // STEP 2: For each string being passed in, loop through the characters and calculate its order in the alphabet.
        for (const auto& str : strs)
        {
            vector<int> count(26, 0);

            for (char c : str)
            {
                count[c - 'a']++;
            }

            string key = to_string(count[0]);

            for (int i = 1; i < 26; i++)
            {
                key = key + ',' + to_string(count[i]);
            }

            anagramMap[key].push_back(str);
        }

        vector<vector<string>> result;

        for (const auto& pair : anagramMap)
        {
            result.push_back(pair.second);
        }

        return result;
    }
};
