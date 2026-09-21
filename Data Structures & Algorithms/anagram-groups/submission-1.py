class Solution:
    
    def is_angram(str1,str2):
        return sorted(str1)==sorted(str2)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angram_map={}

        for v in strs:
            map_key="".join(sorted(v))
            if map_key not in angram_map:
                angram_map[map_key] = []
            angram_map[map_key].append(v)
        return list(angram_map.values())
        




        