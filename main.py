import os

# 百鬼夜行拼接图片

# 文件夹
bg_dir = '/Users/mr.zhou/Desktop/百鬼夜行/背景'
frame_dir = '/Users/mr.zhou/Desktop/百鬼夜行/边框'
role_dir = '/Users/mr.zhou/Desktop/百鬼夜行/人物'
soul_dir = '/Users/mr.zhou/Desktop/百鬼夜行/御魂'

bg_list = []
frame_list = []
role_list = []
soul_list = []


# 提取文件列表
bg_files = os.listdir(bg_dir)
for file in bg_files:
    if file != '.DS_Store':
        bg_list.append(bg_dir + '/' + file)

frame_files = os.listdir(frame_dir)
for file in frame_files:
    if file != '.DS_Store':
        frame_list.append(frame_dir + '/' + file)

role_files = os.listdir(role_dir)
for file in role_files:
    if file != '.DS_Store':
        role_list.append(role_dir + '/' + file)

soul_files = os.listdir(soul_dir)
for file in soul_files:
    if file != '.DS_Store':
        soul_list.append(soul_dir + '/' + file)

print(bg_list)
print(frame_list)
print(role_list)
print(soul_list)


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


# 遍历文件列表合成
for bg_img in bg_list:
    for frame_img in frame_list:
        for role_img in role_list:
            for soul_img in soul_list:
                name = '{}{}{}{}'.format(bg_list.index(bg_img), role_list.index(role_img), frame_list.index(frame_img), soul_list.index(soul_img))
                combine_img(bg_img, frame_img, role_img, soul_img, name)
