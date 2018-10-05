import os


class FileManager:

    def __init__(self):
        self.file_list = list()

    def create_dir(self, name, address):
        if not os._exists(name + os.sep + address):
            os.makedirs(name + os.sep + address)

    def create_file(self, name, address):
        os.path.join(address, name)


if __name__ == '__main__':
    file_manager = FileManager()

    file_manager.create_dir('/media/mehran/240BCADA758C30EE/cuda', 'tmp_folder')
