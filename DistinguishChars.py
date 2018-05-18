# -*- coding: utf-8 -*-
# @Date    : 2018-05-18 21:59:40
# @Author  : Liu Huan (liuhuan@mail.las.ac.cn)


def is_chinese(char):
        # #判断一个字符是否为中文
        if char >= '\u4e00' and char <= '\u9fa5':
                return True
        else:
                return False


def is_alphabet(char):
        # 判断字符是否为英文字母
        if (char >= '\u0041' and char <= '\u005a') or (char >= '\u0061' and char <= '\u007a'):
                return True
        else:
                return False


def is_number(char):
        # 判断字符是否为数字
        if char >= '\u0030' and char <= '\u0039':
                return True
        else:
                return False


def is_other(uchar):
        # 判断字符是否非汉字，数字和英文字符
        if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
                return True
        else:
                return False


if __name__ == '__main__':
        string = '程序共43行，判断char属性'
        for s in string:
                if is_alphabet(s):
                        print('英文')
                if is_number(s):
                        print('数字')
                if is_chinese(s):
                        print('中文')
                if is_other(s):
                        print('其他')
