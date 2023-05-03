import json
import sys
import uuid
import requests
from PySide6 import QtWidgets
from PySide6.QtCore import Slot, Qt, QObject, Signal, QThread, QSize
from PySide6.QtWidgets import QMessageBox, QDialog, QPushButton, QHBoxLayout, QLabel, QLineEdit, QFormLayout, QSpinBox, \
    QComboBox, QListWidget, QCheckBox, QListWidgetItem

from UIDesign import main, mywidget
from createSignature import RequestMsgByUrl

Beijing1 = "console-beijing-1"
Suzhou = "console-wuxi-1"
Chengdu = "console-yaan-1"
Zhengzhou = "console-zhengzhou-1"
Beijing3 = "console-beijing-2"
Changsha2 = "console-zhuzhou-1"
Jinan = "console-jinan-1"
Xian = "console-xian-1"
Shanghai1 = "console-shanghai-1"
Chongqing = "console-chongqing-1"
Hangzhou = "console-ningbo-1"
Huhehaote = "console-huhehaote-1"
Guiyang = "console-guiyang-1"
reversedict = {
    "华北-呼和浩特": "console-huhehaote-1",
    "华北-北京3  ": "console-beijing-2",
    "华中-郑州": "console-zhengzhou-1",
    "华中-长沙": "console-zhuzhou-1",
    "华东-苏州": "console-wuxi-1",
    "华东-济南": "console-jinan-1",
    "华东-上海": "console-shanghai-1",
    "华东-杭州": "console-ningbo-1",
    "西南-贵阳": "console-guiyang-1",
    "西南-成都": "console-yaan-1",
    "西南-重庆": "console-chongqing-1",
    "华北-北京1": "console-beijing-1",
    "西北-西安": "console-xian-1",
}


# 创建监听器和后端服务器组工作线程
class createListenerAndServerWorker(QObject):
    createListenerAndServer = Signal(bool)

    def __init__(self, ak, sk, vlbId, listenerName, listenerProtocolPort, healthDelay, healthMaxRetries, healthTimeout,
                 currentEndPoint):
        super().__init__()
        self.ak = ak
        self.sk = sk
        self.vlbId = vlbId
        self.listenerName = listenerName
        self.listenerProtocolPort = listenerProtocolPort
        self.healthDelay = healthDelay
        self.healthMaxRetries = healthMaxRetries
        self.healthTimeout = healthTimeout
        self.currentEndPoint = currentEndPoint




    def asynCreateListenerAndServer(self):
        client = RequestMsgByUrl(access_key=self.ak, secret_key=self.sk, method=None, endpoint=None, path=None,
                                 body=None)
        querystring = {"AccessKey": self.ak, "Timestamp": "", "Signature": "",
                       "SignatureMethod": "HmacSHA1", "SignatureNonce": "", "SignatureVersion": "V2.0"}
        querystring['SignatureNonce'] = uuid.uuid4()
        querystring['Signature'] = client.sign('POST', querystring, '/api/slb/v2/listener')
        payload = {
                   "healthDelay": self.healthDelay,
                   "healthMaxRetries": self.healthMaxRetries,
                   "healthTimeout": self.healthTimeout,
                   "healthType": "TCP",
                   "lbAlgorithm": "ROUND_ROBIN",
                   "loadBalanceId":self.vlbId,
                   "name": self.listenerName,
                   "protocol": "TCP",
                   "protocolPort": self.listenerProtocolPort
        }
        requestQuery = requests.post('https://' + self.currentEndPoint + '.cmecloud.cn:8443/api/slb/v2/listener',
                                     params=querystring,json=payload)
        result = json.loads(requestQuery.text)
        if result.get('state') == 'OK':
            self.createListenerAndServer.emit(True)
        else:
            self.createListenerAndServer.emit(False)

class MainPage_windows(main.Ui_Form, QtWidgets.QMainWindow):
    def __init__(self, currentAK, currentSK, checkboxlist, rgnCheckboxdict, realnamedict, vlbs,backEndPools):
        super(MainPage_windows, self).__init__()
        self.setupUi(self)
        self.currentAK = currentAK
        self.currentSK = currentSK
        self.checkboxlist = checkboxlist
        self.rgnCheckboxdict = rgnCheckboxdict
        self.realnamedict = realnamedict
        self.vlbs = vlbs
        self.backEndPools = backEndPools
        self.queryVlBtn.clicked.connect(self.queryExistVlb)
        self.vlbListWidget.itemClicked.connect(self.querySelectedVlb)
        self.listenerListWidget.itemClicked.connect(self.querySelectedListener)
        self.addListenerBtn.clicked.connect(self.showDialog)
        self.addListenerBtn.setEnabled(False)
        self.addVMButton.setEnabled(False)
        self.addVMButton.clicked.connect(self.showVMBindDialog)

    def getCurrentRegion(self):
        # 获取当前所选的负载均衡
        vlbSelected = self.vlbListWidget.currentIndex()
        vlbItemIndex = vlbSelected.row()
        arrs = self.vlbListWidget.item(vlbItemIndex).text().split("---")
        # 获取当前所选的后端服务器
        backEndPoolSelected = self.listenerListWidget.currentIndex()
        backEndItemIndex = backEndPoolSelected.row()
        arrs2 = self.listenerListWidget.item(backEndItemIndex).text()

        # 找出PoolId
        for eachBackEndPool in self.backEndPools:
            if arrs2 == eachBackEndPool.poolName:
                poolId = eachBackEndPool.poolId
                break
        return (arrs[0],poolId)


    @Slot()
    def querySelectedListener(self):
        self.addVMButton.setEnabled(True)
        self.vmlistWidget.clear()
        poolId=self.getCurrentRegion()[1]
        region = self.getCurrentRegion()[0]
        client = RequestMsgByUrl(access_key=self.currentAK, secret_key=self.currentSK, method=None, endpoint=None, path=None, body=None)
        querystring = {"AccessKey": self.currentAK, "Timestamp": "", "Signature": "",
                           "SignatureMethod": "HmacSHA1", "SignatureNonce": "", "SignatureVersion": "V2.0"}
        querystring['SignatureNonce'] = uuid.uuid4()
        querystring['Signature'] = client.sign('GET', querystring, '/api/slb/v2/member/'+poolId+'/members')
        requestQuery = requests.get('https://' + reversedict[region] + '.cmecloud.cn:8443/api/slb/v2/member/'+poolId+'/members',
                                        params=querystring)
        result = json.loads(requestQuery.text)
        if result.get('body') != None and result.get('body').get('total') > 0:
            vmDict ={}
            for eachVM in result.get('body').get('content'):
                if vmDict.get(eachVM.get('vmName')) == None:
                    vmDict[eachVM.get('vmName')]=[eachVM.get('port')]
                else:
                    list = vmDict[eachVM.get('vmName')]
                    list.append(eachVM.get('port'))
            for key,value in vmDict.items():
                self.vmlistWidget.addItem(key+"---"+str(len(value))+'个端口')

    @Slot()
    def querySelectedVlb(self, item):
        self.addListenerBtn.setEnabled(True)
        self.listenerListWidget.clear()
        arrs = item.text().split('---')
        loadBalanceId = ""
        region = ""
        for vlb in self.vlbs:
            if vlb.name == arrs[1] and vlb.region == arrs[0]:
                loadBalanceId = vlb.vlbId
                region = vlb.region
                break
        client = RequestMsgByUrl(access_key=self.currentAK, secret_key=self.currentSK, method=None, endpoint=None,
                                 path=None, body=None)
        querystring = {"AccessKey": self.currentAK, "Timestamp": "", "Signature": "",
                       "SignatureMethod": "HmacSHA1", "SignatureNonce": "", "SignatureVersion": "V2.0",
                       "bindListener": True}
        querystring['SignatureNonce'] = uuid.uuid4()
        querystring['Signature'] = client.sign('GET', querystring, '/api/slb/v2/pool/' + loadBalanceId + '/pools')
        requestQuery = requests.get(
            'https://' + reversedict[region] + '.cmecloud.cn:8443/api/slb/v2/pool/' + loadBalanceId + '/pools',
            params=querystring)
        result = json.loads(requestQuery.text)

        if result.get('body') != None and result.get('body').get('total') > 0:
            for eachBackServer in result.get('body').get('content'):
                self.listenerListWidget.addItem(eachBackServer.get('poolName'))
                backEndPool = BackEndPool(poolId=eachBackServer.get('poolId'),poolName=eachBackServer.get('poolName'),loadBalanceId=eachBackServer.get('loadBalanceId'),
                                          listenerName=eachBackServer.get('listenerName'),listenerId=eachBackServer.get('listenerId'))
                self.backEndPools.append(backEndPool)
        else:
            reply = QMessageBox.warning(self, '警告', '当前负载均衡并无绑定的后端服务器组，是否新建', QMessageBox.Yes | QMessageBox.No,
                                        QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.showDialog()

    @Slot()
    def showVMBindDialog(self):
        dialog = QDialog()
        dialog.resize(600,400)
        layout = QFormLayout()
        #可添加的主机列表
        memberlist = QListWidget()
        layout.addRow(memberlist)
        startPort = QSpinBox()
        startPort.setMinimum(1)
        startPort.setMaximum(65536)
        layout.addRow("业务主机需要绑定的起始的端口", startPort)
        endPort=QSpinBox()
        endPort.setMinimum(1)
        endPort.setMaximum(65536)
        layout.addRow("业务主机需要绑定的最后的端口", endPort)
        percent = QSpinBox()
        percent.setMinimum(1)
        percent.setMaximum(100)
        percent.setSuffix("%")
        layout.addRow("比重", percent)
        confirmBtn = QPushButton('确认')
        cancelBtn = QPushButton('取消')
        layout.addRow(confirmBtn, cancelBtn)
        dialog.setLayout(layout)
        dialog.setWindowTitle('批量添加业务主机')
        dialog.setWindowModality(Qt.ApplicationModal)
        poolId=self.getCurrentRegion()[1]
        region = self.getCurrentRegion()[0]
        #查询可添加的主机列表
        client = RequestMsgByUrl(access_key=self.currentAK, secret_key=self.currentSK, method=None, endpoint=None, path=None, body=None)
        querystring = {"AccessKey": self.currentAK, "Timestamp": "", "Signature": "",
                       "SignatureMethod": "HmacSHA1", "SignatureNonce": "", "SignatureVersion": "V2.0","poolId":poolId,"pageSize":20,"page":1}
        querystring['SignatureNonce'] = uuid.uuid4()
        querystring['Signature'] = client.sign('GET', querystring, '/api/slb/v2/member/serverPorts')
        requestQuery = requests.get('https://' + reversedict[region] + '.cmecloud.cn:8443/api/slb/v2/member/serverPorts',
                                    params=querystring)
        result = json.loads(requestQuery.text)
        print(result)
        memberVMs=[]
        vmCheckBoxes=[]
        if result.get('body') != None and result.get('body').get('total') > 0:
            for eachVm in result.get('body').get('content'):
                item = QListWidgetItem(memberlist)
                vmCheckBox = QCheckBox()
                item.setSizeHint(QSize(0,20))
                vmCheckBox.setText(eachVm.get('resourceName'))
                memberlist.setItemWidget(item,vmCheckBox)
                membervm = memberVM(resourceName=eachVm.get('resourceName'),ip=eachVm.get('privateIp'),subnetId=eachVm.get('subnetId'),vmHostId=eachVm.get('resourceId'),type=None)
                memberVMs.append(membervm)
                vmCheckBoxes.append(vmCheckBox)

            confirmBtn.clicked.connect(lambda :self.batchAddMembers(vmCheckBoxes,memberVMs,startPort.value(),endPort.value(),percent.value()))
            dialog.close()
        else:
            confirmBtn.setEnabled(False)

        cancelBtn.clicked.connect(dialog.close)
        dialog.exec()

    @Slot()
    def batchAddMembers(self,vmCheckBoxes,memberVMs,startPort,endPort,percent):
        #找到他们的Id，放到一个集合里
        vMembers = []
        region = self.getCurrentRegion()[0]
        poolId= self.getCurrentRegion()[1]
        for vmCheckBox in vmCheckBoxes:
            if vmCheckBox.isChecked():
                #去memberVMs里找memberId
                for membervm in memberVMs:
                    if membervm.resourceName == vmCheckBox.text():
                            vMembers.append(membervm)

        if startPort>endPort:
            QMessageBox.critical(self,"错误","起始端口比终止端口大")

        else:
            client = RequestMsgByUrl(access_key=self.currentAK, secret_key=self.currentSK, method=None,
                                         endpoint=None, path=None, body=None)
            querystring = {"AccessKey": self.currentAK, "Timestamp": "", "Signature": "",
                               "SignatureMethod": "HmacSHA1", "SignatureNonce": "", "SignatureVersion": "V2.0","poolId":poolId
                               }
            querystring['SignatureNonce'] = uuid.uuid4()
            querystring['Signature'] = client.sign('POST', querystring, '/api/slb/v2/member/'+poolId+'/members')
            params = []
            for index in range(startPort, endPort + 1):
                for eachvm in vMembers:
                    param ={
                            "description": "",
                            "ip": eachvm.ip,
                            "port": index,
                            "subnetId": eachvm.subnetId,
                            "type": 1,
                            "vmHostId": eachvm.vmHostId,
                            "weight": percent
                    }
                    params.append(param)
            requestQuery = requests.post(
                'https://' + reversedict[region] + '.cmecloud.cn:8443/api/slb/v2/member/'+poolId+'/members',
                params=querystring,json=params)
            result = json.loads(requestQuery.text)
            if result.get('state') == 'OK':
                QMessageBox.information(self,"成功","创建成功，请稍后刷新")

            else:
                QMessageBox.critical(self,"失败","创建失败,请检查参数。或者联系wx（18359103384）进行排查故障")
    @Slot()
    def showDialog(self):
        dialog = QDialog()
        dialog.resize(600, 200)
        layout = QFormLayout()
        vlbIdLineEdit = QLineEdit()
        layout.addRow("负载均衡ID", vlbIdLineEdit)
        listenerNameLineEdit = QLineEdit()
        layout.addRow("监听器名(5~22位的中文、英文、数字、下划线等的组合)", listenerNameLineEdit)
        listenerProtocolPortLineEdit = QLineEdit()
        layout.addRow("监听器前端协议的端口号(不能使用（9090 | 9080 | 9070 | 9004 | 2222）", listenerProtocolPortLineEdit)
        healthDelaySpinBox = QSpinBox()
        layout.addRow("监听器绑定的健康检查的时间间隔，单位为秒", healthDelaySpinBox)
        healthMaxRetriesSpinBox = QSpinBox()
        layout.addRow("监听器绑定的健康检查检查失败后的最大尝试检查次数，取值为1~10", healthMaxRetriesSpinBox)
        healthTimeoutSpinbox = QSpinBox()
        layout.addRow("监听器的超时时间，取值为1~100", healthTimeoutSpinbox)
        confirmBtn = QPushButton('确认')
        cancelBtn = QPushButton('取消')
        layout.addRow(confirmBtn, cancelBtn)
        dialog.setLayout(layout)
        dialog.setWindowTitle('创建监听器及后端服务器组')
        dialog.setWindowModality(Qt.ApplicationModal)
        selected = self.vlbListWidget.currentIndex()
        itemindex = selected.row()
        arrs = self.vlbListWidget.item(itemindex).text().split("---")
        for vlb in self.vlbs:
            if vlb.region == arrs[0] and vlb.name == arrs[1]:
                vlbIdLineEdit.setText(vlb.vlbId)
                break
        confirmBtn.clicked.connect(lambda: self.asynCreate(vlbId=vlbIdLineEdit.text(), listenerName=listenerNameLineEdit.text(),
                                                   listenerProtocolPort=listenerProtocolPortLineEdit.text(),
                                                   healthDelay=healthDelaySpinBox.value(),
                                                   healthMaxRetries=healthMaxRetriesSpinBox.value()
                                                   , healthTimeout=healthTimeoutSpinbox.value(),
                                                   currentEndPoint=reversedict[arrs[0]]))
        confirmBtn.clicked.connect(dialog.close)
        cancelBtn.clicked.connect(dialog.close)

        dialog.exec()

    #不用做异步，因为人家已经是异步的了，fuck~
    @Slot()
    def asynCreate(self, vlbId, listenerName, listenerProtocolPort, healthDelay, healthMaxRetries, healthTimeout,
                    currentEndPoint):
        self.addListenerBtn.setEnabled(False)
        self.createListenerAndServerWorker = createListenerAndServerWorker(self.currentAK, self.currentSK, vlbId,
                                                                           listenerName, listenerProtocolPort,
                                                                           healthDelay, healthMaxRetries, healthTimeout,
                                                                           currentEndPoint)
        self.createListenerAndServerThread = QThread()
        self.createListenerAndServerWorker.moveToThread(self.createListenerAndServerThread)
        self.createListenerAndServerThread.started.connect(
            self.createListenerAndServerWorker.asynCreateListenerAndServer)
        self.createListenerAndServerWorker.createListenerAndServer.connect(self.displayCreate)
        self.createListenerAndServerThread.finished.connect(self.createListenerAndServerWorker.deleteLater)
        self.createListenerAndServerThread.finished.connect(self.createListenerAndServerThread.deleteLater)
        self.createListenerAndServerThread.start()

    def displayCreate(self, res):
        self.addListenerBtn.setEnabled(True)
        self.createListenerAndServerThread.quit()
        if res == False:
            QMessageBox.critical(self, "错误", "创建失败,请检查参数。或者联系wx（18359103384）进行排查故障")
        else:
            QMessageBox.information(self, "成功", "创建成功,请耐心等待大约（30s）后重新点击即可刷新")
            # selected = self.vlbListWidget.currentIndex()
            # itemindex = selected.row()
            # self.querySelectedVlb(self.vlbListWidget.item(itemindex))

    @Slot()
    def queryExistVlb(self):
        self.vlbListWidget.clear()
        self.vmlistWidget.clear()
        self.listenerListWidget.clear()
        ak = self.currentAK
        sk = self.currentSK
        checkedbox = []
        for i in self.checkboxlist:
            if i.isChecked():
                checkedbox.append(i)
        if len(checkedbox) == 0:
            QMessageBox.warning(self, "警告", "请选择节点")
        else:
            for eachEndpoint in checkedbox:
                client = RequestMsgByUrl(access_key=ak, secret_key=sk, method=None, endpoint=None, path=None, body=None)
                querystring = {"AccessKey": ak, "Timestamp": "", "Signature": "",
                               "SignatureMethod": "HmacSHA1", "SignatureNonce": "", "SignatureVersion": "V2.0"}
                querystring['SignatureNonce'] = uuid.uuid4()
                querystring['Signature'] = client.sign('GET', querystring, '/api/slb/v2/loadBalancer/loadBalancers')
                requestQuery = requests.get('https://' + self.rgnCheckboxdict[
                    eachEndpoint] + '.cmecloud.cn:8443/api/slb/v2/loadBalancer/loadBalancers',
                                            params=querystring)
                result = json.loads(requestQuery.text)
                if result.get('body') != None and result.get('body').get('total') > 0:
                    for eachVLB in result.get('body').get('content'):
                        listeners = []
                        if eachVLB.get('bindListeners') != None:
                            for eachListener in eachVLB.get('bindListeners'):
                                listener = Listener(eachListener.get('id'), eachListener.get('name'),
                                                    eachListener.get('protocol'), eachListener.get('protocolPort'))
                                listeners.append(listener)
                        vlb = Vlb(eachVLB.get('id'), eachVLB.get('name'), listeners, self.realnamedict[eachEndpoint])
                        self.vlbs.append(vlb)
                        self.vlbListWidget.addItem(self.realnamedict[eachEndpoint] + "---" + eachVLB.get('name'))


class LogPage_windows(mywidget.Ui_myWidget, QtWidgets.QMainWindow):
    def __init__(self, mainWindow):
        super(LogPage_windows, self).__init__()
        self.mainWindow = mainWindow
        self.setupUi(self)
        self.logpushButton.clicked.connect(self.checkAkSK)
        self.rgnCheckboxdict = {self.mainWindow.HuhehaotecheckBox_2: Huhehaote,
                                self.mainWindow.Beijing3checkBox: Beijing3,
                                self.mainWindow.ZhengzhoucheckBox_3: Zhengzhou,
                                self.mainWindow.Changsha2checkBox_4: Changsha2,
                                self.mainWindow.SuzhoucheckBox_6: Suzhou,
                                self.mainWindow.JinancheckBox_5: Jinan,
                                self.mainWindow.ShanghaicheckBox_7: Shanghai1,
                                self.mainWindow.HangzhoucheckBox_8: Hangzhou,
                                self.mainWindow.GuiyangcheckBox_10: Guiyang,
                                self.mainWindow.ChengducheckBox_9: Chengdu,
                                self.mainWindow.ChongqingcheckBox_11: Chongqing,
                                self.mainWindow.XiancheckBox_13: Xian,
                                self.mainWindow.Beijing1checkBox: Beijing1}
        self.checkboxlist = [self.mainWindow.HuhehaotecheckBox_2, self.mainWindow.Beijing3checkBox,
                             self.mainWindow.ZhengzhoucheckBox_3, self.mainWindow.Changsha2checkBox_4,
                             self.mainWindow.SuzhoucheckBox_6, self.mainWindow.JinancheckBox_5,
                             self.mainWindow.ShanghaicheckBox_7,
                             self.mainWindow.HangzhoucheckBox_8,
                             self.mainWindow.GuiyangcheckBox_10, self.mainWindow.ChengducheckBox_9,
                             self.mainWindow.ChongqingcheckBox_11,
                             self.mainWindow.XiancheckBox_13, self.mainWindow.Beijing1checkBox]
        self.realnamedict = {
            self.mainWindow.HuhehaotecheckBox_2: "华北-呼和浩特", self.mainWindow.Beijing3checkBox: "华北-北京3",
            self.mainWindow.ZhengzhoucheckBox_3: "华中-郑州",
            self.mainWindow.Changsha2checkBox_4: "华中-长沙", self.mainWindow.SuzhoucheckBox_6: "华东-苏州",
            self.mainWindow.JinancheckBox_5: "华东-济南", self.mainWindow.ShanghaicheckBox_7: "华东-上海",
            self.mainWindow.HangzhoucheckBox_8: "华东-杭州",
            self.mainWindow.GuiyangcheckBox_10: "西南-贵阳", self.mainWindow.ChengducheckBox_9: "西南-成都",
            self.mainWindow.ChongqingcheckBox_11: "西南-重庆", self.mainWindow.Beijing1checkBox: "华北-北京1",
            self.mainWindow.XiancheckBox_13: "西北-西安"}

    @Slot()
    def checkAkSK(self):
        ak = self.accessKeylineEdit.text().strip()
        sk = self.secretKeylineEdit.text().strip()
        self.logpushButton.setEnabled(False)
        signClient = RequestMsgByUrl(access_key=ak, secret_key=sk, method=None, endpoint=None, path=None, body=None)
        # 签名公参，如果有其他参数，同样在此添加
        querystring = {"AccessKey": ak, "Timestamp": "", "Signature": "",
                       "SignatureMethod": "HmacSHA1", "SignatureNonce": "", "SignatureVersion": "V2.0"}
        querystring['SignatureNonce'] = uuid.uuid4()
        querystring['Signature'] = signClient.sign('GET', querystring, '/api/slb/v2/loadBalancer/quota')
        test = requests.get('https://api-wuxi-1.cmecloud.cn:8443/api/slb/v2/loadBalancer/quota',
                            params=querystring)
        result = json.loads(test.text)
        if result['state'] == 'ERROR':
            if result['errorMessage'] == 'Invalid parameter AccessKey ' or result[
                'errorMessage'] == 'Invalid parameter Signature ':
                QMessageBox.warning(self, "警告", "AccessKey或SecretKey错误")
            self.logpushButton.setEnabled(True)
        elif result['state'] == 'OK':
            self.hide()
            self.mainWindow.currentAK = self.accessKeylineEdit.text().strip()
            self.mainWindow.currentSK = self.secretKeylineEdit.text().strip()
            self.mainWindow.checkboxlist = self.checkboxlist
            self.mainWindow.rgnCheckboxdict = self.rgnCheckboxdict
            self.mainWindow.realnamedict = self.realnamedict
            self.mainWindow.show()
        else:
            QMessageBox.critical(self, "错误", "内部系统异常")
            self.logpushButton.setEnabled(True)


class Vlb:
    def __init__(self, vlbId, name, bindListeners, region):
        self.vlbId = vlbId
        self.name = name
        self.bindListeners = bindListeners
        self.region = region

class memberVM:
    def __init__(self,ip,subnetId,vmHostId,type,resourceName):
        self.ip=ip
        self.subnetId = subnetId
        self.vmHostId = vmHostId
        self.type = type
        self.resourceName = resourceName

class Listener:
    def __init__(self, id, name, protocol, protocolPort):
        self.id = id
        self.name = name
        self.protocol = protocol
        self.protocolPort = protocolPort

class BackEndPool:
    def __init__(self,poolId,poolName,loadBalanceId,listenerId,listenerName):
        self.poolId = poolId
        self.poolName = poolName
        self.loadBalanceId = loadBalanceId
        self.listenerId = listenerId
        self.listenerName = listenerName

def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWidget = MainPage_windows("", "", None, None, None, [],[])
    logWidget = LogPage_windows(mainWidget)
    logWidget.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
