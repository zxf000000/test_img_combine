import os
import random
import xlwt
from threading import Thread, Lock

# 百鬼夜行拼接图片

# 文件夹
bg_dir = '/Users/mr.zhou/Desktop/百鬼夜行/背景'
frame_dir = '/Users/mr.zhou/Desktop/百鬼夜行/边框'
role_dir = '/Users/mr.zhou/Desktop/百鬼夜行/人物'
soul_dir = '/Users/mr.zhou/Desktop/百鬼夜行/御魂'

bg_list = {}
frame_list = {}
role_list = {}
soul_list = {}

# 数量
role_count = {
    '依加博': 500,
    '五千郎大屋': 450,
    '阿伊努死骸': 400,
    '板鬼': 350,
    '池袋之女': 300,
    '垢尝': 450,
    '海坊主': 400,
    '海怪': 350,
    '后追小僧': 150,
    '矶抚': 150,
    '矶天狗': 150,
    '忙': 150,
    '蟒蛇': 150,
    '牛打坊': 150,
    '牛鬼': 150,
    '围棋精': 100,
    '伊草袈裟坊': 100,
    '异兽': 100,
    '缢鬼': 100,
    '油取': 100,
    '婴儿笼': 61,
    '油须磨': 61,
    '雨女': 61,
    '足长手长': 61,
    '一目连': 6,
}

bg_count = {
    '鬼': 1250,
    '人': 1000,
    '动物': 750,
    '器物': 500,
    '执念': 400,
    '植物': 350,
    '神': 300,
    '超自然现象': 250,
    '特殊': 200,
}

soul_count = {
    '网剪': 1250,
    '山姥': 1000,
    '提灯火': 750,
    '三味': 500,
    '针女': 400,
    '火消婆': 350,
    '阴摩罗鬼': 300,
    '骨女': 250,
    '业原火': 175,
    '古战场火': 25,
}

frame_count = {
    '木': 1500,
    '树': 1250,
    '水': 1000,
    '花': 750,
    '石': 375,
    '鬼': 100,
    '金': 25,
}

# 组合逻辑
# 组成数组
# 角色
# all_role = []
# for key in role_count:
#     value = role_count[key]
#     for i in range(0, value):
#         all_role.append(key)

# all_bg = []
# for key in bg_count:
#     value = bg_count[key]
#     for i in range(0, value):
#         all_bg.append(key)
#
# all_soul = []
# for key in soul_count:
#     value = soul_count[key]
#     for i in range(0, value):
#         all_soul.append(key)
#
# all_frame = []
# for key in frame_count:
#     value = frame_count[key]
#     for i in range(0, value):
#         all_frame.append(key)
#
# print(len(all_role))
# print(len(all_soul))
# print(len(all_frame))
# print(len(all_bg))

# 提取文件列表
bg_files = os.listdir(bg_dir)
for file in bg_files:
    if file != '.DS_Store':
        bg_list[file.replace('.png', '')] = bg_dir + '/' + file

frame_files = os.listdir(frame_dir)
for file in frame_files:
    if file != '.DS_Store':
        frame_list[file.replace('.png', '')] = frame_dir + '/' + file

role_files = os.listdir(role_dir)
for file in role_files:
    if file != '.DS_Store':
        role_list[file.replace('.png', '')] = role_dir + '/' + file

soul_files = os.listdir(soul_dir)
for file in soul_files:
    if file != '.DS_Store':
        soul_list[file.replace('.png', '')] = soul_dir + '/' + file

# 尺寸-位置
frame_size = '1560:2160'

frame_pos = '0:0'


# 合成图片
def combine_img(img1, img2, img3, img4, output_name):
    os.system('ffmpeg -i {} -i {} -i {} -i {}'
              ' -filter_complex '
              '"[1]scale={}[v11];'
              '[2]scale={}[v22];'
              '[3]scale={}[v33];'
              '[0][v11]overlay={}[v1];'
              '[v1][v22]overlay={}[v2];'
              '[v2][v33]overlay={}[v3]"'
              ' -map "[v3]" -qscale 0 {}.png'.format(img1, img2, img3, img4,
                                                     frame_size, frame_size, frame_size,
                                                     frame_pos, frame_pos, frame_pos, './output/' + output_name))


role_keys = list(role_count.keys())
frame_keys = list(frame_count.keys())
soul_keys = list(soul_count.keys())
bg_keys = list(bg_count.keys())

names = []

for role in role_keys:
    for soul in soul_keys:
        for frame in frame_keys:
            for bg in bg_keys:
                names.append((role, soul, frame, bg))


def gen_res_count_arr(origin):
    res = {}
    for aKey in origin:
        res[aKey] = 0
    return res


# 生成数量为0的结果数组
role_res_count = gen_res_count_arr(role_count)
soul_res_count = gen_res_count_arr(soul_count)
frame_res_count = gen_res_count_arr(frame_count)
bg_res_count = gen_res_count_arr(bg_count)

res_arr = []

names.reverse()

for name in names:
    role = name[0]
    soul = name[1]
    frame = name[2]
    bg = name[3]
    role_res_count[role] += 1
    soul_res_count[soul] += 1
    frame_res_count[frame] += 1
    bg_res_count[bg] += 1
    # if role_res_count[role] < role_count[role] and soul_res_count[soul] < soul_count[soul] and frame_res_count[frame] < frame_count[frame] and bg_res_count[bg] < bg_count[bg]:
    #     role_res_count[role] += 1
    #     soul_res_count[soul] += 1
    #     frame_res_count[frame] += 1
    #     bg_res_count[bg] += 1
    #     res_arr.append('{}-{}-{}-{}'.format(role, soul, frame, bg))

print(role_res_count)
print(soul_res_count)
print(frame_res_count)
print(bg_res_count)


# def filter_keys(keys, count_dic):
#     for aKey in count_dic:
#         if count_dic[aKey] <= 0 and aKey in keys:
#             keys.remove(aKey)


# count = 0
# name_arr = []
# while count < 5000:
#
#     filter_keys(role_keys, role_count)
#     filter_keys(frame_keys, frame_count)
#     filter_keys(soul_keys, soul_count)
#     filter_keys(bg_keys, bg_count)
#
#     role_num = random.randint(0, len(role_keys) - 1)
#     soul_num = random.randint(0, len(soul_keys) - 1)
#     frame_num = random.randint(0, len(frame_keys) - 1)
#     bg_num = random.randint(0, len(bg_keys) - 1)
#
#     role_name = role_keys[role_num]
#     soul_name = soul_keys[soul_num]
#     frame_name = frame_keys[frame_num]
#     bg_name = bg_keys[bg_num]
#
#     role_pic = role_list[role_name]
#     soul_pic = soul_list[soul_name]
#     frame_pic = frame_list[frame_name]
#     bg_pic = bg_list[bg_name]
#
#     name = '{}-{}-{}-{}'.format(role_name, bg_name, frame_name, soul_name)
#     if name not in name_arr:
#         name_arr.append(name)
#         count += 1
#         # combine_img(bg_img, frame_img, role_img, soul_img, name)
#         # 数量减一
#         role_count[role_name] -= 1
#         frame_count[frame_name] -= 1
#         soul_count[soul_name] -= 1
#         bg_count[bg_name] -= 1
#
#         print(name)
#         print(count)

# print(role_count)
#
# wb = xlwt.Workbook()
# ws = wb.add_sheet('name sheet')
#
# for index in range(0, len(name_arr)):
#     ws.write(index, 0, name_arr[index])
#
# wb.save('names.xls')

# # 遍历文件列表合成
# for bg_img in bg_list:
#     for frame_img in frame_list:
#         for role_img in role_list:
#             for soul_img in soul_list:
#                 name = '{}{}{}{}'.format(bg_list.index(bg_img), role_list.index(role_img), frame_list.index(frame_img), soul_list.index(soul_img))
#                 combine_img(bg_img, frame_img, role_img, soul_img, name)
