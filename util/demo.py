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
            os.chdir('../../')
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
            os.chdir('../../')
    else:
        for i in all_file:
            with open(i, 'w+') as f:
                pass
    return os.listdir()


if __name__ == '__main__':
    old_path_windows = 'F:/尚硅谷HTML+CSS基础教程/代码/代码/2_CSS2'
    old_path_linux = '/home/alex/桌面/尚硅谷HTML+CSS基础教程/代码/3_HTML5'
    os.chdir(old_path_windows)
    print('当前目录为：', os.getcwd())
    tmp_dict, tmp_list = get_all_file()
    new_path_widows = 'D:/code/WebstormProjects/learn-front-end/base/2_CSS2'
    new_path_linux = '/home/alex/VscodeProjects/learn-front-end/base/4_CSS3'
    os.chdir(new_path_widows)
    if len(tmp_list) != 0:
        create_file(tmp_list)
    elif len(tmp_dict) != 0:
        create_file(tmp_dict)
    else:
        pass
