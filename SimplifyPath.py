class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_name = ""
        path += "/"

        for c in path:
            if (c == "/" and len(path_name )> 0):
                if stack and path_name == "..":
                    print(stack)
                    stack.pop()

                is_a_path = not (path_name == ".." or path_name == ".")
                if is_a_path:
                    stack.append(path_name)
                
                path_name = ""
            else:
                if (c != '/'):
                    path_name += c


        compressed_path = "/".join(stack)
        return "/" + compressed_path    
