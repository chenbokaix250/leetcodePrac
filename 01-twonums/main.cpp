#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums,int target){
        int i,j;
        for(int i=0;nums.size()-1;i++){
            for(int j=i+1;j<nums.size();j++){
                if(nums[i]+nums[j]==target){
                    return {i,j};
                }
            }
        }
        return {};
    };
};

int main(){
    Solution solution;
    vector<int> nums = {2,7,11,15};
    int target = 9;
    vector<int> result = solution.twoSum(nums,target);
    for(int i=0;i<result.size();i++){
        cout<<result[i]<<endl;
    }
    return 0;
}