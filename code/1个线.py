import re
import matplotlib.pyplot as plt
import chardet
import os

# 读取log文件并提取倒数第四行
with open('log/LightGCN-test1-Aug-05-2024-20-21-50.log', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    target_line = lines[-3]


# 使用正则表达式提取所需的数据
pattern = r'recall@5: ([0-9.]+)\s+recall@10: ([0-9.]+)\s+recall@20: ([0-9.]+)\s+recall@50: ([0-9.]+)'
match = re.search(pattern, target_line)

if match:
    recall_5 = float(match.group(1))
    recall_10 = float(match.group(2))
    recall_20 = float(match.group(3))
    recall_50 = float(match.group(4))

    # 数据
    x = ['recall@5', 'recall@10', 'recall@20', 'recall@50']
    y = [recall_5, recall_10, recall_20, recall_50]

    # 绘制折线图
    plt.figure(dpi=300)  # 设置分辨率为300 DPI
    plt.plot(x, y, marker='o')
    plt.xlabel('Recall Metrics')
    plt.ylabel('Values')
    plt.title('Recall Metrics Values (Validation)')
    plt.grid(True)

    # 保存为矢量图 (SVG) 和位图 (PNG)
    # plt.savefig('picture/recall_metrics_validation.svg')
    plt.savefig('picture/recall_metrics_validation.png')

    # 显示图像
    plt.show()
else:
    print("没有找到匹配的数据")