import os


# 获取文件和替换文件
# 获取所有文件
def get_all_file():
    tmp_dict = dict()
    tmp_list = list()
    for i in os.listdir():
        if os.path.isdir(i):
            os.chdir(i)
            tmp_dict.update({i: os.listdir(os.getcwd())})
            os.chdir('../')
        else:
            tmp_list.append(i)
    return tmp_dict, tmp_list


# 创建文件
def create_file(all_file):
    if isinstance(all_file, dict):
        for i in dict(all_file).keys():
            os.mkdir(i)
            os.chdir(i)
            for j in all_file[i]:
                with open(j, 'w+') as f:
                    pass
            os.chdir('../')
    else:
        for i in all_file:
            with open(i, 'w+') as f:
                pass
    return os.listdir()


if __name__ == '__main__':
    os.chdir('/home/alex/桌面/尚硅谷HTML+CSS基础教程/代码/3_HTML5')
    print('1', os.getcwd())
    tmp_dict, tmp_list = get_all_file()
    os.chdir('/home/alex/VscodeProjects/learn-front-end/base/3_HTML5')
    if len(tmp_dict) == 0:
        create_file(tmp_list)
    else:
        create_file(tmp_dict)
