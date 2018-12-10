# -*- coding: utf-8 -*-
# author:           inpurer(月小水长)
# pc_type           lenovo
# create_date:      2018/12/8
# file_name:        constant.py
# description:      月小水长，热血未凉

# 标志字段，标识一个帧的开始和结束
segmentFlag = "01111110"

# 地址字段，全“0”地址为无站地址，这种地址不分配给任何站，仅作作测试
segmentAddr = "00000000"

# SABM:建立,
segmentSABM = "11110100"

# DISC:拆除
segmentDISC = "11000110"

# 对建立和拆除和确认
segmentUA = "11001110"

dataDemo = {
    "Fs":segmentFlag,  # Flag_start
    "A":segmentAddr,
    "C":segmentSABM,
    "I":"0000000011111111",
    "FCS":"00000000",
    "Fe":segmentFlag  # Flag_end
}

# 内存换速度
i2s = {
    "0": "000",
    "1": "001",
    "2": "010",
    "3": "011",
    "4": "100",
    "5": "101",
    "6": "110",
    "7": "111"
}