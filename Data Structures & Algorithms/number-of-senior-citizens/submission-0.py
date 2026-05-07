class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for det in details:
            age = det[11:13]
            if age[0] == "0":
                continue
            elif int(age) > 60:
                count += 1
        return count