import sys
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from fuzzysearch import find_near_matches

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 626)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.province_label = QtWidgets.QLabel(self.centralwidget)
        self.province_label.setGeometry(QtCore.QRect(120, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.province_label.setFont(font)
        self.province_label.setObjectName("province_label")
        self.area_label = QtWidgets.QLabel(self.centralwidget)
        self.area_label.setGeometry(QtCore.QRect(120, 240, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.area_label.setFont(font)
        self.area_label.setObjectName("area_label")
        self.weight_label = QtWidgets.QLabel(self.centralwidget)
        self.weight_label.setGeometry(QtCore.QRect(120, 400, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.weight_label.setFont(font)
        self.weight_label.setObjectName("weight_label")

        self.calculate_Button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_Button.setGeometry(QtCore.QRect(310, 470, 99, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.calculate_Button.setFont(font)
        self.calculate_Button.setMouseTracking(False)
        self.calculate_Button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.calculate_Button.setObjectName("calculate_Button")
        self.calculate_Button.clicked.connect(self.computePrice)

        self.province_text = QtWidgets.QLineEdit(self.centralwidget)
        self.province_text.setGeometry(QtCore.QRect(330, 100, 113, 25))
        self.province_text.setObjectName("province_text")
        self.province_text.textChanged.connect(self.list_probably_provinces)
        
        self.area_text = QtWidgets.QLineEdit(self.centralwidget)
        self.area_text.setGeometry(QtCore.QRect(330, 240, 113, 25))
        self.area_text.setObjectName("area_text")
        self.area_text.textChanged.connect(self.list_probably_areas)

        self.weight_text = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_text.setGeometry(QtCore.QRect(330, 400, 113, 25))
        self.weight_text.setObjectName("weight_text")

        self.finalPrice_label = QtWidgets.QLabel(self.centralwidget)
        self.finalPrice_label.setGeometry(QtCore.QRect(200, 560, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.finalPrice_label.setFont(font)
        self.finalPrice_label.setObjectName("finalPrice_label")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(500, 100, 120, 102))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 118, 100))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.provinceList = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.provinceList.setGeometry(QtCore.QRect(0, 0, 121, 102))
        self.provinceList.setObjectName("provinceList")
        self.provinceList.addItems(provinceList)
        self.provinceList.itemDoubleClicked.connect(self.select_confirm_province)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(500, 240, 120, 102))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 118, 100))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")

        self.areaList = QtWidgets.QListWidget(self.scrollAreaWidgetContents_3)
        self.areaList.setGeometry(QtCore.QRect(0, 0, 120, 102))
        self.areaList.setObjectName("areaList")
        self.areaList.itemDoubleClicked.connect(self.select_confirm_area)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.finalPrice_text = QtWidgets.QLineEdit(self.centralwidget)
        self.finalPrice_text.setGeometry(QtCore.QRect(390, 560, 221, 25))
        self.finalPrice_text.setObjectName("finalPrice_text")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.finalPrice_text.setFont(font)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    # 点击计算按钮时触发的事件
    def computePrice(self):
        money = 0.0
        weight = float(self.weight_text.text())
        provinceName = self.province_text.text()
        areaName = self.area_text.text()
        self.lists = fileMap[provinceName]

        for list in self.lists:
            areas = list[0]
            if areaName in areas:
                basePrice = float(list[1])
                low_30_price = float(list[2])
                high_50_low_600 = float(list[3])
                high_601 = float(list[4])

                if 0.0 <= weight <= 30.0:
                    money = weight * low_30_price
                elif 31.0 <= weight <= 49.0:
                    money = 30.0 * low_30_price + (weight - 30.0) * high_50_low_600
                elif 50.0 <= weight <= 600.0:
                    money = weight * high_50_low_600
                elif weight >= 601.0:
                    money = weight * high_601
                
                if money < basePrice:
                    money = basePrice

                money = "{:.2f}".format(money)
                self.finalPrice_text.clear()
                self.finalPrice_text.setText(str(money))

    def select_confirm_area(self):
        areaName = self.areaList.selectedItems()[0].text()
        self.area_text.setText(areaName)
        print(areaName)

        found_keys = [key for key, value in provin_area_map.items() if areaName in value]

        print(found_keys)  # 输出包含 my_list_element 的键列表
        # 回显到provinceText中
        self.province_text.setText(found_keys[0])


    # 根据选中的省份，获取到所有区域，然后再进行模糊查询
    def list_probably_areas(self):

        input_area = self.area_text.text()
        self.areaList.clear()
        for area in all_areas:
            if input_area in area:
                self.areaList.addItem(area)


    # 从provinceList中选中需要的省份
    def select_confirm_province(self):
        # 获取到选中的省份的名字
        provinceName = self.provinceList.selectedItems()[0].text()
        # 回显到provinceText中
        self.province_text.setText(provinceName)
        # 将province对应的所有区域的名字回显到areaList中
        # 当选中省份名称时，在areaList中回显这个
        self.lists = fileMap[provinceName]
        self.areas = []
        for list in self.lists:
            # lists的格式：[
                        # 	['上海市', '25', '0.8', '0.6', '0.5'],
                        # 	['崇明岛', '30', '1.0', '0.7', '0.65']
                        # ]
            # areaName格式：株洲、湘潭、娄底、益阳、岳阳、衡阳、常德
            areaName = list[0]
            # areaNameList格式：['株洲', '湘潭', '娄底', '益阳', '岳阳', '衡阳', '常德']
            areaNameList = areaName.split("、")
            for one_area in areaNameList:
                self.areas.append(one_area)
        self.areaList.clear()
        self.areaList.addItems(self.areas)

    def list_probably_provinces(self):
        self.provinceList.clear()
        # 接受的模糊查询关键词
        keyword = self.province_text.text()

        # # 对list列表进行模糊查询，设置最大编辑距离为1
        # matches = find_near_matches(keyword, provinceList, max_l_dist=1)

        # # 打印匹配结果
        # print(matches)
        for province in provinceList:
            if keyword in province:
                # 匹配的省份的名字
                self.provinceList.addItem(province)
                

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "价格计算器"))
        self.province_label.setText(_translate("MainWindow", "请输入省份"))
        self.area_label.setText(_translate("MainWindow", "请输入市/区"))
        self.weight_label.setText(_translate("MainWindow", "请输入重量"))
        self.calculate_Button.setText(_translate("MainWindow", "计算"))
        self.finalPrice_label.setText(_translate("MainWindow", "最终价格为："))




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)



# file_path_final = "C:\\file_final.txt"

# 将file_final中的内容转为map。filemap的格式为：{
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
#f = open(file_path_final,"r",encoding="utf-8")
#fileContent = f.read()
fileContent="{'上海市': [['上海市', '25', '0.8', '0.6', '0.5'], ['崇明岛', '30', '1.0', '0.7', '0.65']], '江苏省': [['常州、苏州、无锡、南京、南通、泰州', '30', '1.0', '0.6', '0.55'], ['扬州、镇江、淮安', '30', '1.0', '0.65', '0.6'], ['连云港、盐城、宿迁、徐州、大丰', '30', '1.3', '0.7', '0.65']], '浙江省': [['杭州、嘉兴、宁波、绍兴、金华、湖州、温州', '30', '1.0', '0.65', '0.6'], ['台州、衢州、丽水', '30', '1.3', '0.7', '0.65'], ['舟山', '30', '1.5', '0.75', '0.7']], '安徽省': [['合肥、六安、滁州、淮南、蚌埠、马鞍山、芜湖', '30', '1.5', '0.8', '0.75'], ['安庆、铜陵、池州、宣城、阜阳、淮北、黄山、宿州、亳州', '30', '1.8', '0.85', '0.8']], '山东省': [['临沂、枣庄、日照、淄博、青岛济宁、济南、泰安市', '30', '2.3', '1.1', '1.0'], ['聊城、菏泽、德州、莱芜、潍坊、烟台、威海、滨州、东营', '30', '2.5', '1.25', '1.2']], '河南省': [['郑州、开封、新乡、许昌、平顶山、洛阳、漯河、鹤壁、济源、焦作', '30', '2.8', '1.3', '1.2'], ['商丘、安阳、驻马店、周口、濮阳、三门峡、南阳、信阳', '30', '3.0', '1.4', '1.3']], '天津市': [['天津市', '30', '2.5', '1.25', '1.2']], '北京市': [['北京市', '35', '2.9', '1.3', '1.2']], '河北省': [['保定、廊坊、石家庄', '30', '2.8', '1.3', '1.2'], ['沧州、定州、邯郸、辛集、邢台、张家口', '35', '2.9', '1.4', '1.3'], ['承德、衡水、唐山、秦皇岛', '35', '2.9', '1.45', '1.4']], '福建省': [['福州、厦门、漳州、泉州', '30', '2.5', '1.25', '1.2'], ['龙岩、南平、宁德、莆田、三明', '30', '3.0', '1.35', '1.3']], '广东省': [['东莞、广州、深圳、汕头、中山、珠海、佛山、潮州', '30', '2.8', '1.3', '1.2'], ['江门、惠州、揭阳、清远、河源、肇庆、韶关梅州、汕尾、茂名、云浮、阳江、湛江', '30', '3.0', '1.4', '1.3']], '江西省': [['南昌', '30', '2.5', '1.2', '1.1'], ['九江、宜春、鹰潭、萍乡、上饶、抚州、景德镇、新余', '30', '2.8', '1.3', '1.2'], ['赣州、吉安', '30', '3.0', '1.4', '1.3']], '湖北省': [['武汉', '30', '2.5', '1.25', '1.2'], ['黄冈、鄂州、黄石、仙桃、孝感、咸宁、天门、荆州、荆门潜江', '30', '2.8', '1.3', '1.2'], ['襄阳、宜昌、随州、十堰、神农架林、恩施土家族', '30', '3.0', '1.4', '1.3']], '湖南省': [['长沙', '30', '2.5', '1.2', '1.1'], ['株洲、湘潭、娄底、益阳、岳阳、衡阳、常德', '30', '2.8', '1.3', '1.2'], ['郴州、永州、怀化、邵阳、张家界、湘西', '30', '3.0', '\"1', '4\"']], '山西省': [['太原', '35', '2.9', '1.4', '1.35'], ['长治、晋城、运城、晋中、朔州、吕梁、大同', '35', '3.2', '1.5', '1.4'], ['忻州、阳泉、临汾', '35', '3.4', '1.6', '1.4']], '陕西省': [['西安、咸阳、渭南、铜川、商洛、宝鸡、安康、汉中', '40', '3.5', '1.7', '1.5'], ['榆林市', '40', '4.0', '1.8', '1.6']], '重庆市': [['重庆市', '40', '3.5', '1.7', '1.6']], '四川省': [['成都', '40', '3.5', '1.7', '1.6'], ['德阳、乐山、眉山、绵阳、内江、资阳', '40', '3.8', '1.8', '1.7'], ['自贡、雅安、遂宁、宜宾、南充、泸州、广元、广安、达州、巴中、阿坝藏族', '50', '3.8', '1.9', '1.8'], ['甘孜藏族、凉山彝族、攀枝花', '50', '4.5', '2', '1.9']], '广西省': [['南宁', '40', '3.5', '1.7', '1.6'], ['钦州、来宾、河池、北海、崇左、百色、防城港、贵港、', '40', '3.8', '1.8', '1.7'], ['柳州、玉林、梧州、桂林、贺州', '40', '4.0', '1.9', '1.8']], '贵州省': [['贵阳、仁怀、安顺、毕节', '45', '4.4', '1.9', '1.7'], ['六盘水、黔东南苗、黔南布依、黔西南布、铜仁、遵义', '45', '5.4', '2.2', '2.0']], '云南省': [['昆明、玉溪、曲靖', '45', '4.2', '2.3', '2.0'], ['文山壮族、红河、昭通、楚雄、大理', '50', '5.3', '2.4', '2.2'], ['普洱、丽江、临沧、西双版纳、迪庆、德宏、保山、怒江', '50', '5.8', '2.5', '2.3']], '甘肃省': [['兰州、白银、定西', '50', '5.0', '2.2', '2.0'], ['甘南藏族、嘉谷关、金昌、酒泉、临夏、陇南、平凉、庆阳、天水、武威、张掖', '50', '5.3', '2.5', '2.4']], '海南省': [['海口、澄迈、定安、白沙黎族、文昌、屯昌、万宁、琼海、琼中黎族、临高、儋州', '50', '4.8', '2.2', '1.9'], ['陵水黎族、乐东黎族、东方、昌江、保亭三亚、三沙、五指山', '55', '5.2', '2.3', '2.0']], '黑龙江省': [['哈尔滨', '50', '4.8', '2.1', '2.0'], ['绥化、大庆、齐齐哈尔、伊春、牡丹江、佳木斯、', '50', '5.0', '2.2', '2.0'], ['鹤岗、七台河、双鸭山、黑河、鸡西大兴安岭', '60', '5.0', '2.3', '2.1']], '吉林省': [['长春、松原、吉林、辽源', '45', '4.2', '1.9', '1.7'], ['四平、通化、延边朝鲜族、白山、白城', '50', '4.5', '2.1', '2.0']], '辽宁省': [['大连、本溪、鞍山、抚顺、朝阳、阜新、锦州、沈阳、辽阳、葫芦岛、铁岭', '40', '4.0', '1.8', '1.7'], ['营口、丹东', '40', '4.3', '1.9', '1.85']], '内蒙古': [['赤峰、锡林郭勒盟、通辽、呼和浩特、乌兰察布、鄂尔多斯、包头', '50', '4.5', '2', '1.8'], ['兴安盟、呼伦贝尔、巴彦淖尔、阿拉善、乌海', '60', '4.8', '2.2', '2.0']], '宁夏': [['银川、石嘴山、吴忠', '50', '4.8', '2.2', '2.0'], ['中卫、固原', '50', '5.3', '2.3', '2.1']], '青海省': [['西宁、海北藏族、东海、海南藏族自治州', '60', '5.5', '2.6', '2.4'], ['黄南藏族、果洛藏族、海西藏族玉树藏族自治州', '60', '6.0', '2.7', '2.5']], '西藏': [['拉萨市', '80', '7.3', '3.6', '3.4'], ['林芝、那曲、日喀则、山南地区、昌都、阿里地区、', '90', '7.8', '3.9', '3.7']], '新疆': [['乌鲁木齐', '65', '5.9', '2.9', '2.8'], ['五家渠、吐鲁番、石河子、克拉玛依、昌吉', '70', '6.3', '3', '2.9'], ['阿勒泰、巴音郭楞、博尔塔拉、哈密、塔城地区', '75', '7.2', '3.4', '3.2'], ['伊犁哈萨克自治州', '75', '7.4', '3.5', '3.2'], ['阿克苏、阿拉尔、喀什地区、和田地区、图木舒克、克孜勒苏柯尔克', '80', '8.0', '3.8', '3.6']]}"
fileMap = dict(eval(fileContent))

# 获取所有的province
provinceList = []
keys = fileMap.keys()
# 用for循环遍历keys
for key in keys:
    provinceList.append(key)

# 一个省份的所有地区名称 string:list
provin_area_map = {}

all_areas = []
for province in provinceList:
    one_pro_area = []
    province_areas = fileMap[province]
    for list in province_areas:
        # province_areas的格式：[
                    # 	['上海市', '25', '0.8', '0.6', '0.5'],
                    # 	['崇明岛', '30', '1.0', '0.7', '0.65']
                    # ]
        # areaName格式：株洲、湘潭、娄底、益阳、岳阳、衡阳、常德
        areaName = list[0]
        # areaNameList格式：['株洲', '湘潭', '娄底', '益阳', '岳阳', '衡阳', '常德']
        areaNameList = areaName.split("、")
        for one_area in areaNameList:
            all_areas.append(one_area)
            one_pro_area.append(one_area)
    provin_area_map[province] = one_pro_area

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
