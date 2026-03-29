class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for ch in path.split("/"):
            if ch == "..":
                if stack:
                    stack.pop()
            elif ch == "." or ch == "":
                continue

            else:
                stack.append(ch)

        return "/" + "/".join(stack)