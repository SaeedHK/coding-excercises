"""
71. Simplified Path (Leetcode)

"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        derived_path = []
        for directory in path.split("/"):
            print(derived_path)
            if not directory or directory == ".":
                continue

            if directory == "..":
                if derived_path:
                    derived_path.pop()
                continue

            derived_path.append(directory)

        if not derived_path:
            return "/"

        return "/".join([""] + derived_path)


path = "/.../a/../b/c/../d/./"
output = "/.../b/d"

assert Solution().simplifyPath(path) == output
print("Tests passed")
