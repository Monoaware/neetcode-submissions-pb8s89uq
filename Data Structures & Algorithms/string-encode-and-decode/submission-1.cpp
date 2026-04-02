class Solution {
public:

    string encode(vector<string>& strs) {

        if (strs.empty())
        {
            return "";
        }

        // STEP 1: Create a vector to keep track of string sizes.
        vector<int> sizes;
        string res = "";

        for (string& s : strs)
        {
            sizes.push_back(s.size());
        }

        // STEP 2: Store the sizes within the result string.
        for (int sz : sizes) 
        {
            res = res + to_string(sz) + ',';
        }

        // Use a delimiter to separate the sizes from the actual strings.
        res = res + '#';

        for (string& s : strs)
        {
            res = res + s;
        }

        return res;
    }

    vector<string> decode(string s) {

        if (s.empty())
        {
            return {};
        }

        vector<int> sizes;
        vector<string> res;
        int i = 0;

        // STEP 1: Store all the sizes back into a vector.
        while (s[i] != '#')
        {
            string cur = "";

            while (s[i] != ',')
            {
                cur = cur + s[i];
                i++;
            }

            sizes.push_back(stoi(cur));
            i++;
        }

        i++;

        // STEP 2: Proceed onto the string portion and capture each string.
        for (int sz : sizes)
        {
            res.push_back(s.substr(i, sz));
            i = i + sz;
        }

        return res;
    }
};
