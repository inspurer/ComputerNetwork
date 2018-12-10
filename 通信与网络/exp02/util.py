# -*- coding: utf-8 -*-
# author:           inpurer(月小水长)
# pc_type           lenovo
# create_date:      2018/12/8
# file_name:        util
# description:      月小水长，热血未凉

#发送端FCS检验
def setFCS(data):
    fcs = ['0','0','0','0','0','0','0','0']
    #信息字段的格式为"0000000011111111"或者"这是第i帧"
    hanzi = data.get("I")
    if len(hanzi)>5:
        pass
    else:
        for ch in hanzi:
            #  字符转编码值 19968~40870
            ch = ord(ch)
            # 如果是0~9,为了统一起来，不做处理
            if ch<57:
                continue
            else:
                #汉字的范围:0x4e00~0x9fa6 19968~40870
                ch = str(ch)
                ch = "000" + ch #00019968
                ch = list(ch)
                for i, item in enumerate(ch):
                    if item > '4':
                        fcs[i] = '1'
                    else:
                        fcs[i] = '0'
    for key in data.keys():
        if key == "FCS" or key == "I":
            continue
        value = data.get(key)
        valued = list(value)
        for i,item in enumerate(valued):
            if item is fcs[i]:
                fcs[i] = '0'
            else:
                fcs[i] = '1'
    for j,item in enumerate(fcs):
        if item is '0':
            fcs[j] = '1'
        else:
            fcs[j] = '0'
    fcs = "".join(fcs)
    data['FCS'] = fcs
    return data


# 接收端FCS检验,算法和生成FCS类似
def  fragmentChecker(receivedData):
    #return True
    fcsChecker = receivedData.get("FCS")
    #没有帧校验位，立即返回
    if not fcsChecker:
        return False

    fcs = ['0','0','0','0','0','0','0','0']
    #信息字段的格式为"0000000011111111"或者"这是第i帧"
    hanzi = receivedData.get("I")
    if len(hanzi)>5:
        pass
    else:
        for ch in hanzi:
            #  字符转编码值 19968~40870
            ch = ord(ch)
            # 如果是0~9,为了统一起来，不做处理
            if ch<57:
                continue
            else:
                #汉字的范围:0x4e00~0x9fa6 19968~40870
                ch = str(ch)
                ch = "000" + ch #00019968
                ch = list(ch)
                for i, item in enumerate(ch):
                    if item > '4':
                        fcs[i] = '1'
                    else:
                        fcs[i] = '0'
    for key in receivedData.keys():
        #python3 不能用 is 来判断两个字符串是否相等
        if key == "FCS" or key == "I":
            continue
        value = receivedData.get(key)
        valued = list(value)
        for i,item in enumerate(valued):
            if item is fcs[i]:
                fcs[i] = '0'
            else:
                fcs[i] = '1'
    for j,item in enumerate(fcs):
        if item is '0':
            fcs[j] = '1'
        else:
            fcs[j] = '0'
    fcs = "".join(fcs)
    print(receivedData,fcs)
    if fcsChecker == fcs:
        return True
    else:
        return False
    pass


