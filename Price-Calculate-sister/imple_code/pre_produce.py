# import pandas as pd

# 读取 Excel 文件
# df = pd.read_excel('C:\\file.xls')
# 将数据保存为 CSV 文件
# df.to_csv('D:\\file.txt', index=False)
# print("输出结果已保存到 D:\\file.txt 文件")


# file_path = 'D:\\file.txt'
# file_path_final = "D:\\file_final.txt"
# # 打开文件
# with open(file_path, 'r', encoding='utf-8') as file:

#     # {
#     #   "上海市":[[上海市,25,0.8,0.6,0.5],[崇明岛,30,1.0,0.7,0.65]]
#     # }
#     provinceMap = {}
#     currProvinceName = ""


#     # 逐行读取并遍历内容
#     for line in file:
#         # 移除行尾的换行符
#         line = line.rstrip('\n')
        
#         items = line.split(',')
#         if line.startswith(','):
#             print(f"该行以逗号开头：{line}")
#             # print(f"市/区：{items[1]}")
#             # print(f"起步价：{items[2]}")
#             # print(f"30kg以下：{items[3]}")
#             # print(f"50kg-600kg：{items[4]}")
#             # print(f"601kg及以上：{items[5]}")  
                     
#             provinceMap[currProvinceName].append([str(items[1]),str(items[2]),str(items[3]),str(items[4]),str(items[5])])
#             print()
#         else:
#             print(f"该行不以逗号开头：{line}")
#             # 打印分割后的内容

#             print(f"省份：{items[0]}")
#             currProvinceName = items[0]
#             provinceMap.update({str(items[0]):[[str(items[1]),str(items[2]),str(items[3]),str(items[4]),str(items[5])]]})

#             # print(f"市/区：{items[1]}")
#             # print(f"起步价：{items[2]}")
#             # print(f"30kg以下：{items[3]}")
#             # print(f"50kg-600kg：{items[4]}")
#             # print(f"601kg及以上：{items[5]}")
#             print()

#     print(provinceMap)
#     f = open(file_path_final,"w",encoding="utf-8")
#     f.write(str(provinceMap))

# 是一个map，格式为：{
	# '上海市': [
	# 	['上海市', '25', '0.8', '0.6', '0.5'],
	# 	['崇明岛', '30', '1.0', '0.7', '0.65']
	# ],
	# '江苏省': [
	# 	['常州、苏州、无锡、南京、南通、泰州', '30', '1.0', '0.6', '0.55'],
	# 	['扬州、镇江、淮安', '30', '1.0', '0.65', '0.6'],
	# 	['连云港、盐城、宿迁、徐州、大丰', '30', '1.3', '0.7', '0.65']
	# ]
# }
# file_path_final = "D:\\file_final.txt"

# # 将file_final中的内容转为map
# f = open(file_path_final,"r",encoding="utf-8")
# fileContent = f.read()
# fileMap = dict(eval(fileContent))
# print(fileMap["上海市"])
