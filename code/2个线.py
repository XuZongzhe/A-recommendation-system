import re
import matplotlib.pyplot as plt
import chardet
import os

# 读取log文件并提取倒数第四行
with open('log/LightGCN-test1-Aug-05-2024-20-21-50.log', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    target_line_test = lines[-3]
    target_line_valid = lines[-4]

# 使用正则表达式提取所需的数据
pattern = r'recall@5: ([0-9.]+)\s+recall@10: ([0-9.]+)\s+recall@20: ([0-9.]+)\s+recall@50: ([0-9.]+)'

match_test = re.search(pattern, target_line_test)
match_valid = re.search(pattern, target_line_valid)

if match_test and match_valid:
    recall_test = [float(match_test.group(i)) for i in range(1, 5)]
    recall_valid = [float(match_valid.group(i)) for i in range(1, 5)]

    # 数据
    x = ['recall@5', 'recall@10', 'recall@20', 'recall@50']

    # 设置图表大小和分辨率
    plt.figure(figsize=(8, 6), dpi=100)

    # 绘制折线图
    plt.plot(x, recall_test, marker='o', label='Test', linestyle='-', color='b')
    plt.plot(x, recall_valid, marker='o', label='Valid', linestyle='--', color='r')

    # 图表美化
    plt.xlabel('Recall Metrics', fontsize=12)
    plt.ylabel('Values', fontsize=12)
    plt.title('Recall Metrics Values for Test and Valid', fontsize=14)
    plt.legend(loc='best', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # 创建picture文件夹（如果不存在）
    if not os.path.exists('picture'):
        os.makedirs('picture')

    # 保存图表到picture文件夹
    plt.savefig('picture/recall_metrics.svg', format='svg', bbox_inches='tight')
    plt.show()
else:
    print("没有找到匹配的数据")