import os


class DirDict():
    def __init__(self, path):
        self._path = path
        if not os.path.exists(path):
            raise IOError

    def __getitem__(self, key):
        if key in self._get_files():
            with open(self._join_path_file(key), 'r') as f:
                return f.read().strip()
        else:
            raise KeyError

    def __setitem__(self, key, value):
        with open(self._join_path_file(key), 'w') as f:
            f.write(str(value))

    def __delitem__(self, key):
        if os.path.exists(self._join_path_file(key)):
            os.remove(self._join_path_file(key))
        else:
           raise KeyError

    def __len__(self):
        return len(self._get_files())
    
    def __iter__(self):
        for key in self._get_files():
            yield key

    def __repr__(self):
        dict_of_file = {}
        for elem in self._get_files():
            with open(self._join_path_file(elem), 'r') as f:
                dict_of_file[elem] = f.read().strip()
        return str(dict_of_file)

    def _join_path_file(self, file):
        return os.path.join(self._path, file)

    def _get_files(self):
        return [file for file in os.listdir(self._path) if os.path.isfile(self._join_path_file(file))]
