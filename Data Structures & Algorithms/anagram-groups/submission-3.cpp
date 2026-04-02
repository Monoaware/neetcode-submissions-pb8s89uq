class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        // STEP 1: Create a map to hold the sorted values of the anagram list.
        unordered_map<string, vector<string>> anagramMap;

        // STEP 2: Iterate over the anagram list and sort the strings, adding them to the map as you go.
        for (const auto& str : strs)
        {
            string sorted_string = str;

            sort(sorted_string.begin(), sorted_string.end());

            anagramMap[sorted_string].push_back(str);
        }

        // STEP 3: Create a vector of vectors of string to contain the output.
        vector<vector<string>> result;

        // STEP 4: For each completed entry pair of the map, 
        for (auto& pair : anagramMap)
        {
            result.push_back(pair.second);
        }

        return result;
    }
};
