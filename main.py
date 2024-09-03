from typing import List

def stringMatching(words: List[str]) -> List[str]:
    result_list: List[str] = []
    for i in words:
        for j in words:
            if i.find(j) >= 0 and i != j:
                if not j in result_list:
                    result_list.append(j)
    return result_list            

def main() -> None:
    print(stringMatching(["mass","as","hero","superhero"]))
    print(stringMatching(["leetcode","et","code"]))
    print(stringMatching(["blue","green","bu"]))
    print(stringMatching(["leetcoder","leetcode","od","hamlet","am"]))
    
if __name__ == "__main__":
    main()