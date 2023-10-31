# 代码 60行左右 不会每一行每一个细节  讲清楚！ 思路 在干啥 解释清楚！
import random
import sys
import tkinter  # 导入模块
from PIL import Image, ImageTk  # 从PIL里面导入Image ImageTk模块
import pygame                   # 导入python游戏模块 音乐播放
'''
    创建一个窗口
    设置窗口的宽度和搞高度 300x300
    隐藏窗口的标题栏和外框
    设置透明的颜色
    初始化一下游戏的环境
    加载一首音乐
'''
root = tkinter.Tk()
root.geometry('300x250')
root.overrideredirect(True)  # 画架边框去掉！
root.attributes('-transparentcolor', 'black')  # 黑色部分透明
pygame.mixer.init()
pygame.mixer.music.load('gif/music.mp3')

'''
    把gif的图像加载进来 随机的animationx.gif
    切割成一帧一帧的图像
    保存在frames里面备用
'''
index = random.randint(1, 8)  # 随机取一个gif
gif = Image.open(f'gif/animation{index}.gif')  # 加载animation1.gif
frames = []  # 用来存放每一帧图片的列表
try:
    while True:
        frame = gif.copy().convert('RGBA')        # 得到一帧图片
        frames.append(ImageTk.PhotoImage(frame))  # 转化成Tk可用的图片 放进列表去
        gif.seek(len(frames))                      # 把目标定在前一帧的后面
except EOFError:  # 如果发现后面没有图像了  结束！
    pass

'''
    创建一块画布
    先显示第-1帧 
    保证程序刚开始的时候不会出现白班
'''
canvas = tkinter.Canvas(root, borderwidth=0, highlightthickness=0)
canvas.pack()
image = frames[-1]  # 拿到第0帧的图像
canvas.create_image(0, 0, anchor='nw', image=image) # 图像->画布

'''
    touch_fish完成动画的播放-->画布上
    lbuttondown作为鼠标左键的回调函数 去触发动画播放
    root.bind鼠标左键 触发lbuttondown执行
'''
current_frame = 0  # 从第0帧开始！
def show_gif():  # 一个完整的动画！
    global current_frame
    image = frames[current_frame]  # 拿到第current_frame帧的图像
    canvas.create_image(0, 0, anchor='nw', image=image) # 图像->画布
    current_frame += 1  # 增加帧数
    if current_frame == len(frames):
        return
    canvas.after(100, show_gif)

def touch_fish(event):
    pygame.mixer.music.play()  # 播放音乐！
    global current_frame
    current_frame = 0
    show_gif()

    # 每一次摸鱼结束 重新加载一个gif进来
    global index, gif, frames
    index = random.randint(1, 8)  # 随机取一个gif
    gif = Image.open(f'gif/animation{index}.gif')  # 加载animation1.gif
    frames = []  # 用来存放每一帧图片的列表
    try:
        while True:
            frame = gif.copy().convert('RGBA')  # 得到一帧图片
            frames.append(ImageTk.PhotoImage(frame))  # 转化成Tk可用的图片 放进列表去
            gif.seek(len(frames))  # 把目标定在前一帧的后面
    except EOFError:  # 如果发现后面没有图像了  结束！
        pass

x = y = 0
def get_pos(event):
    global x, y
    x = event.x
    y = event.y

def move_window(event):
    root.geometry(f'+{event.x_root-x}+{event.y_root-y}')

def end_touch_fish(event):
    sys.exit()

root.bind('<Button-1>', get_pos)        # 左键点下去会计算鼠标的位置
root.bind('<B1-Motion>', move_window)   # 左键点下去移动 木鱼会跟着移动
root.bind('<ButtonRelease-1>', touch_fish)  # 释放左键 摸鱼！
root.bind('<Button-3>', end_touch_fish)  # 鼠标右键 结束摸鱼！

# 显示窗口
root.mainloop()

# 轴！

# 游戏！曾经玩过！现在在玩！
# 魔兽世界！
# 开荒！ BOSS  谁都不知道怎么打！Boss有几个阶段？不同的阶段会释放什么技能？如何应对
# 出教程 出装备 卖钱！ 一个高等级的装备！ 烂大街  开始一段时间值钱？

# 人生 是不是一场养成类的游戏！

# 已经有攻略的东西  不要花时间去怼！ 闭门造车！
# 前面！ 去创造新的东西！ 新的东西才值钱！

# 10几年 头破血流的知识！
# 6-8个月 8980的学费！ 贵！ 2005年！18年前  北大青x 2W多！ 3W5
# 4个月 3w5学费  脱产：5000*4 = 20000  4个月吃喝拉撒：2000*4 = 8000
# 线上 8980 -2000 = 6980
# 6-8个月  5年的时间！ 问题 学习 外包 工作 编程！
# C语言 C++ 带你搞！

# 君子性非异也 善假于物也！

# 世界就这么大！  资源就这么多！  优质的资源  走的更快 机会 抓住机会！

# VIP：6980  6-8个月！ 直播 录播 课后随时准备解答你的疑惑！
#        外包 兼职 首付款收多少 尾款！

# 1.预定200  总学费8980 - 2000 = 6980
# 2.分期 一个月是565块钱
# 3.6-8个月学习时间   5年学习权限
# 4.免费教你C  C++

# 原因：自学！ 知识体系不系统！ 简单的 难一点的东西 啥都不会！
# 下定决心！ 学不会！ 系统的训练！
# 生活中！ 开餐馆！  有人告诉怎么做！
# 外贸  外贸的资源！
# 接单做外包！ 程序！

# 扎心的话：
# 你们来  公司明天能上市？
# 你们都不来  公司明天会垮掉吗？

# 你！ 没有马云 趋势：人工智能 淘汰很多！
# 来！ 1 3 5 晚上8点上课！
#     python 基础  python学完
#     爬虫之后 外包怎么做？ 收多少钱！
#     转行  找谁去推荐  vip已经在上班的同学 武汉 上海 北京 广州 深圳
#     未知 = 恐惧

# 已知！愿意去做的！ 未知 = 恐惧 不敢去尝试！
# 吃了饭 = 不饿！
# 这个月上班 = 下个月15号发工资！
# 做地铁 20分钟！

# 成就的人！ 未知 = 恐惧
# 2017年  基金  广告 弹窗 推送！买的人很少！
# 2018年  基本上 所有基金 转到钱了！ 事情！
# 2019年 2020年！ 可靠的时候！ 亏了！

# 做别人不敢做的事情！ 翻盘！
# 读大学！ 没时间上课很忙！   上课 影响 学习！ 可也不上！
# 工作： 上班 影响 工作！    工作 自己的！ 上班是别人！
# 现在这份工作 一个月给你多少钱？ 23岁 上多少年  40  50岁  65岁退休！
# 技术学好   直播！ 解答！ 语音 远程  语音+远程
# 0基础 web 数据库 爬虫 数据分析 网站开发 一边 还差点火候！一遍！ 5年！
# 找你这么说: 不需要你努力  交点钱  2年以后 稳了！
# 小学  门口  小卖部！  100W   确定！有保障！






















