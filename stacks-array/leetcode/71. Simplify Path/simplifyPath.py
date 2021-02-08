class Solution(object):

    def simplifyPath(path):
        """
        :type path: str
        :rtype: str
        """
        # "/a/b/c/../.././//d" = "a","b", "c", "..", "..", ".", "", "", "d"


        if not path or path == "/" or path == "//":
            return "/"

        stack = []
        paths = path.split("/")

        for portion in paths:
            
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                continue
            else:
                stack.append(portion)
        
            print("stack :", stack)

        return "/" + "/".join(stack)

        # return final_str
        # result = ""
        # for s in stack:
        #     result += "/" + s

        # if len(result) == 0:
        #     return "/"
        # else:
        #     return result



# path =  "/a/b/c/../.././//d"
path =  "/"
path =  "//"

print (Solution.simplifyPath(path))
