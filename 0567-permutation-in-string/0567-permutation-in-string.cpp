class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int n = s1.size();
        int m = s2.size();
        if(m<n) return false;
        vector<int>map1(26,0);
        vector<int>map2(26,0);
        for(int i = 0;i <n;i++){
            map1[s1[i] - 'a']++;
        }
        for(int i = 0;i <= m-n;i++){
            fill(map2.begin(),map2.end(),0);
            for(int j = 0;j<n;j++){
                map2[s2[i+j] -'a']++;
            }
            if(map1 == map2)
            return true;
        }
        return false;
    }
};