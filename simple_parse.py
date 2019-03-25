import os
import re


class FolderParser:
    counted_tags = {}

    def simple_folder_parse(self, folder_path, check_words):
        all_files = os.listdir(folder_path)
        for f in all_files:
            file_path = folder_path + '/' + f
            if os.path.isdir(file_path):
                continue
            self.check_file(file_path, check_words)

    def check_file(self, file_name, check_words):
        if file_name.endswith('.txt') is False:
            return
        fp = open(file_name, 'r', encoding="utf-8")
        self.counted_tags[file_name] = {}
        for line in fp:
            for el in check_words:
                regex_form = r'\b{0}\b'.format(el)
                found = re.findall(regex_form, line.lower())
                # print(found, ' in line ', line)
                if el in self.counted_tags[file_name]:
                    self.counted_tags[file_name][el] += len(found)
                else:
                    self.counted_tags[file_name][el] = len(found)
            # found = [el for el in check_words if el in line]
            # print('LINE IS ', line)
            # if len(found) > 0:
            #     # found a matching word from the list
            #     print('FOUND IN FILE ', file_name, ' THE WORDS : ', found)
        # for el in counter:
        #     print(el, ' : ', counter[el])

    def recursive_folder_parse(self, folder_path, check_words):
        all_files = os.listdir(folder_path)
        for f in all_files:
            file_path = os.path.join(folder_path, f)
            if os.path.isdir(file_path):
                self.recursive_folder_parse(file_path, check_words)
            else:
                self.check_file(file_path, check_words)

    def parse(self, recursive, folder_path, check_words):
        self.counted_tags = {}
        if recursive:
            self.recursive_folder_parse(folder_path, check_words)
        else:
            self.simple_folder_parse(folder_path, check_words)
        # for el in self.counted_tags:
        #     print(el, self.counted_tags[el])
        return self.counted_tags


# check_file('test_folder/file1.txt', ['ana', 'are', 'banane'])
# check_list = ['ana', 'are', 'banane']
# simple_folder_parse('test_folder', check_list)
