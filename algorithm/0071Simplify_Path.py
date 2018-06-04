class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        paths = path.split('/')
        new_path = []
        for path in paths[:]:
            if path == '..':
                if new_path:
                    new_path.pop()
            elif path != '.' and path != '':
                new_path.append(path)
        new_path = '/'.join(new_path)
        new_path = '/' + new_path
        return new_path
