from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1131   ._SN',
        MapName             = 'Bose',
        Location            = 'T1131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 0,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T1131   ._SN',
            'ED6_DT21/T1131_1 ._SN',
            'ED6_DT21/T1131_2 ._SN',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '雷克多主管',                           # 9
        '罗宋厨师长',                           # 10
        '格露娜',                               # 11
        '斯托隆',                               # 12
        '莉诺',                                 # 13
        '赫雷思老人',                           # 14
        '阿尔妲婆婆',                           # 15
        '卡洛塔',                               # 16
        '沙库',                                 # 17
        '奥维德',                               # 18
        '芙拉瑟',                               # 19
        '蕾娜',                                 # 20
        '管家',                                 # 21
        '帝国贵族',                             # 22
        '青年管家',                             # 23
        '罗卡斯',                               # 24
        '爱蕾吉娅',                             # 25
        '雷塔',                                 # 26
        '法娜',                                 # 27
        '维尔纳',                               # 28
        '普拉达',                               # 29
        '龙谷',                                 # 30
        '卡特丽亚',                             # 31
        '芬尼尔',                               # 32
        '科尔娜',                               # 33
        '哈尔德',                               # 34
        '索斯摩夫',                             # 35
        '料理',                                 # 36
        '汤勺',                                 # 37
        '刚茨',                                 # 38
        '梅贝尔市长',                           # 39
        '莉拉',                                 # 40
        '汤碗',                                 # 41
        '汤勺',                                 # 42
        '餐具',                                 # 43
        '餐具',                                 # 44
        '小刀',                                 # 45
        '小刀',                                 # 46
        '汤碗',                                 # 47
        '葡萄酒',                               # 48
        '汤勺',                                 # 49
        '杯子',                                 # 50
        '茶壶',                                 # 51
        '茶壶',                                 # 52
        '茶壶',                                 # 53
        '瓶子',                                 # 54
        '酒杯',                                 # 55
        '茶壶',                                 # 56
        '杯子',                                 # 57
        '杯子',                                 # 58
        '汤碗',                                 # 59
        '汤勺',                                 # 60
        '瓶子',                                 # 61
        '酒杯',                                 # 62
        '甜点',                                 # 63
        '甜点',                                 # 64
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01560 ._CH',             # 00
        'ED6_DT07/CH01280 ._CH',             # 01
        'ED6_DT07/CH02480 ._CH',             # 02
        'ED6_DT07/CH01570 ._CH',             # 03
        'ED6_DT07/CH02540 ._CH',             # 04
        'ED6_DT07/CH01003 ._CH',             # 05
        'ED6_DT07/CH01183 ._CH',             # 06
        'ED6_DT07/CH01023 ._CH',             # 07
        'ED6_DT07/CH01123 ._CH',             # 08
        'ED6_DT07/CH01120 ._CH',             # 09
        'ED6_DT07/CH01370 ._CH',             # 0A
        'ED6_DT07/CH01220 ._CH',             # 0B
        'ED6_DT07/CH01223 ._CH',             # 0C
        'ED6_DT07/CH01570 ._CH',             # 0D
        'ED6_DT07/CH01093 ._CH',             # 0E
        'ED6_DT07/CH01140 ._CH',             # 0F
        'ED6_DT07/CH01150 ._CH',             # 10
        'ED6_DT07/CH01043 ._CH',             # 11
        'ED6_DT07/CH01053 ._CH',             # 12
        'ED6_DT07/CH01000 ._CH',             # 13
        'ED6_DT07/CH01180 ._CH',             # 14
        'ED6_DT07/CH01153 ._CH',             # 15
        'ED6_DT07/CH01143 ._CH',             # 16
        'ED6_DT07/CH01020 ._CH',             # 17
        'ED6_DT06/CH20021 ._CH',             # 18
        'ED6_DT06/CH20020 ._CH',             # 19
        'ED6_DT07/CH01270 ._CH',             # 1A
        'ED6_DT07/CH01050 ._CH',             # 1B
        'ED6_DT07/CH01660 ._CH',             # 1C
        'ED6_DT07/CH02490 ._CH',             # 1D
        'ED6_DT07/CH01040 ._CH',             # 1E
        'ED6_DT07/CH02360 ._CH',             # 1F
        'ED6_DT07/CH02370 ._CH',             # 20
        'ED6_DT07/CH01090 ._CH',             # 21
        'ED6_DT07/CH01453 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT07/CH01560P._CP',             # 00
        'ED6_DT07/CH01280P._CP',             # 01
        'ED6_DT07/CH02480P._CP',             # 02
        'ED6_DT07/CH01570P._CP',             # 03
        'ED6_DT07/CH02540P._CP',             # 04
        'ED6_DT07/CH01003P._CP',             # 05
        'ED6_DT07/CH01183P._CP',             # 06
        'ED6_DT07/CH01023P._CP',             # 07
        'ED6_DT07/CH01123P._CP',             # 08
        'ED6_DT07/CH01120P._CP',             # 09
        'ED6_DT07/CH01370P._CP',             # 0A
        'ED6_DT07/CH01220P._CP',             # 0B
        'ED6_DT07/CH01223P._CP',             # 0C
        'ED6_DT07/CH01570P._CP',             # 0D
        'ED6_DT07/CH01093P._CP',             # 0E
        'ED6_DT07/CH01140P._CP',             # 0F
        'ED6_DT07/CH01150P._CP',             # 10
        'ED6_DT07/CH01043P._CP',             # 11
        'ED6_DT07/CH01053P._CP',             # 12
        'ED6_DT07/CH01000P._CP',             # 13
        'ED6_DT07/CH01180P._CP',             # 14
        'ED6_DT07/CH01153P._CP',             # 15
        'ED6_DT07/CH01143P._CP',             # 16
        'ED6_DT07/CH01020P._CP',             # 17
        'ED6_DT06/CH20021P._CP',             # 18
        'ED6_DT06/CH20020P._CP',             # 19
        'ED6_DT07/CH01270P._CP',             # 1A
        'ED6_DT07/CH01050P._CP',             # 1B
        'ED6_DT07/CH01660P._CP',             # 1C
        'ED6_DT07/CH02490P._CP',             # 1D
        'ED6_DT07/CH01040P._CP',             # 1E
        'ED6_DT07/CH02360P._CP',             # 1F
        'ED6_DT07/CH02370P._CP',             # 20
        'ED6_DT07/CH01090P._CP',             # 21
        'ED6_DT07/CH01453P._CP',             # 22
    )

    DeclNpc(
        X                   = -42600,
        Z                   = 0,
        Y                   = 1700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -35500,
        Z                   = 0,
        Y                   = 46700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -47450,
        Z                   = 0,
        Y                   = 44160,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -42610,
        Z                   = 0,
        Y                   = 41570,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -53300,
        Z                   = 1500,
        Y                   = 200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -48300,
        Z                   = 1650,
        Y                   = 10950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -36300,
        Z                   = 1650,
        Y                   = -1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -54970,
        Z                   = 1600,
        Y                   = 5570,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -55100,
        Z                   = 1600,
        Y                   = 2970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -33640,
        Z                   = 0,
        Y                   = 42550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -32930,
        Z                   = 1600,
        Y                   = 2650,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -33800,
        Z                   = 1500,
        Y                   = 1300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -31760,
        Z                   = 1500,
        Y                   = 1300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = -33060,
        Z                   = 1750,
        Y                   = 5350,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -32560,
        Z                   = 1500,
        Y                   = 6200,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = -51940,
        Z                   = 1500,
        Y                   = 6490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = -46030,
        Z                   = 0,
        Y                   = -1790,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = -40300,
        Z                   = 1650,
        Y                   = 5950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = -39100,
        Z                   = 1650,
        Y                   = 7340,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 2970,
        Z                   = 0,
        Y                   = 3650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 1400,
        Z                   = 0,
        Y                   = 1500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 5480,
        Z                   = 0,
        Y                   = 1480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = -2790,
        Z                   = 0,
        Y                   = -5200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = -2790,
        Z                   = 0,
        Y                   = -3690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 4400,
        Z                   = 0,
        Y                   = 1480,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 4480,
        Z                   = 0,
        Y                   = 1520,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = -7160,
        Z                   = 1580,
        Y                   = -4250,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
    )

    DeclNpc(
        X                   = -6140,
        Z                   = 2250,
        Y                   = -4000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 262169,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6480,
        Z                   = 2250,
        Y                   = -4300,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1114137,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3200,
        Z                   = 0,
        Y                   = -3980,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = -980,
        Z                   = 0,
        Y                   = -2730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -230,
        Z                   = 0,
        Y                   = -1730,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35500,
        Z                   = 2150,
        Y                   = -1060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196633,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35750,
        Z                   = 2150,
        Y                   = -1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1114137,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35670,
        Z                   = 2150,
        Y                   = -950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1376281,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35670,
        Z                   = 2150,
        Y                   = -830,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1376281,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35550,
        Z                   = 2150,
        Y                   = -1350,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1441817,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -35550,
        Z                   = 2150,
        Y                   = -1490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1441817,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -47350,
        Z                   = 2150,
        Y                   = 11000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196633,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -47200,
        Z                   = 2150,
        Y                   = 11400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 327704,
        ChipIndex           = 0x18,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -47650,
        Z                   = 2150,
        Y                   = 11050,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1114137,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -46400,
        Z                   = 2200,
        Y                   = 11000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -55000,
        Z                   = 2200,
        Y                   = 4250,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703961,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -55000,
        Z                   = 2200,
        Y                   = 4750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -55000,
        Z                   = 2200,
        Y                   = 3550,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6490,
        Z                   = 2100,
        Y                   = -3560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835033,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -6360,
        Z                   = 2100,
        Y                   = -4420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 65560,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -33100,
        Z                   = 2200,
        Y                   = 4100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703961,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -33000,
        Z                   = 2200,
        Y                   = 4600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -33000,
        Z                   = 2200,
        Y                   = 3400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638425,
        ChipIndex           = 0x19,
        NpcIndex            = 0x146,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -53250,
        Z                   = 2250,
        Y                   = -950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 524313,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -53750,
        Z                   = 2150,
        Y                   = -1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1114137,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -52920,
        Z                   = 2250,
        Y                   = -630,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1835033,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -53500,
        Z                   = 2150,
        Y                   = -630,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 327704,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -39550,
        Z                   = 2250,
        Y                   = 6000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589849,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -38990,
        Z                   = 2250,
        Y                   = 6430,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 589849,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 3050,
        TriggerZ            = 0,
        TriggerY            = 1520,
        TriggerRange        = 400,
        ActorX              = 2970,
        ActorZ              = 1500,
        ActorY              = 3650,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_8E6",          # 00, 0
        "Function_1_E56",          # 01, 1
        "Function_2_E8F",          # 02, 2
        "Function_3_EB3",          # 03, 3
        "Function_4_114C",         # 04, 4
        "Function_5_12CB",         # 05, 5
        "Function_6_12EF",         # 06, 6
        "Function_7_19D6",         # 07, 7
        "Function_8_1F69",         # 08, 8
        "Function_9_1FAE",         # 09, 9
        "Function_10_28B4",        # 0A, 10
        "Function_11_2FCC",        # 0B, 11
        "Function_12_3574",        # 0C, 12
        "Function_13_3BB9",        # 0D, 13
        "Function_14_4276",        # 0E, 14
        "Function_15_465A",        # 0F, 15
        "Function_16_4A90",        # 10, 16
        "Function_17_69AB",        # 11, 17
        "Function_18_6AD7",        # 12, 18
        "Function_19_70AA",        # 13, 19
        "Function_20_74FF",        # 14, 20
        "Function_21_7895",        # 15, 21
        "Function_22_7AEC",        # 16, 22
        "Function_23_7EFB",        # 17, 23
        "Function_24_8476",        # 18, 24
        "Function_25_86FD",        # 19, 25
        "Function_26_8924",        # 1A, 26
        "Function_27_8CA6",        # 1B, 27
        "Function_28_8DD6",        # 1C, 28
        "Function_29_8EBA",        # 1D, 29
        "Function_30_8EBF",        # 1E, 30
        "Function_31_96D5",        # 1F, 31
        "Function_32_9D6E",        # 20, 32
        "Function_33_9E2D",        # 21, 33
        "Function_34_A07F",        # 22, 34
        "Function_35_A4BD",        # 23, 35
        "Function_36_A585",        # 24, 36
        "Function_37_A586",        # 25, 37
        "Function_38_A781",        # 26, 38
    )


    def Function_0_8E6(): pass

    label("Function_0_8E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_905")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x53), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(1, 6)
    Jump("loc_92E")

    label("loc_905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_91B")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(1, 10)
    Jump("loc_92E")

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_92E")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(2, 4)

    label("loc_92E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_99D")
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98B")
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x34, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_99A")

    label("loc_98B")

    ClearChrFlags(0x23, 0x80)
    SetChrSubChip(0x23, 8)
    ClearChrFlags(0x24, 0x80)

    label("loc_99A")

    Jump("loc_E1F")

    label("loc_99D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_A5A")
    SetChrPos(0x2E, -47250, 2250, 11000, 90)
    SetChrSubChip(0x2E, 8)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3F, 0x80)
    SetChrPos(0xB, -38500, 1500, 14200, 180)
    SetChrFlags(0x37, 0x80)
    SetChrFlags(0x38, 0x80)
    SetChrFlags(0x39, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrPos(0x1C, -1230, 0, 4400, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A57")
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, 2400, 0, 1370, 0)
    ClearChrFlags(0x38, 0x80)
    SetChrPos(0x38, 2250, 700, 2330, 0)

    label("loc_A57")

    Jump("loc_E1F")

    label("loc_A5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_B07")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -45760, 1550, 11100, 270)
    SetChrChipByIndex(0x17, 22)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x17, 0x4)
    ClearChrFlags(0x17, 0x1)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -54180, 1600, -1120, 90)
    SetChrChipByIndex(0x18, 21)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x4)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, -2790, 0, -4580, 90)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -2790, 0, -3690, 90)
    Jump("loc_E1F")

    label("loc_B07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_B9D")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -42360, 0, -1790, 0)
    OP_43(0x17, 0x0, 0x6, 0x2)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -54180, 1650, -1120, 90)
    SetChrChipByIndex(0x18, 21)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x4)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x3A, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x3C, 0x80)
    ClearChrFlags(0x3D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, -2790, 0, -4580, 90)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -2790, 0, -3690, 90)
    Jump("loc_E1F")

    label("loc_B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_D4B")
    ClearChrFlags(0x17, 0x80)
    OP_43(0x17, 0x0, 0x6, 0x2)
    ClearChrFlags(0x18, 0x80)
    OP_43(0x18, 0x0, 0x0, 0x5)
    SetChrPos(0xD, -52150, 1500, 8020, 180)
    SetChrChipByIndex(0xD, 19)
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x10)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x1)
    OP_43(0xD, 0x0, 0x6, 0x2)
    SetChrPos(0xE, -36410, 1500, 90, 225)
    SetChrChipByIndex(0xE, 20)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x1)
    OP_43(0xE, 0x0, 0x6, 0x2)
    SetChrPos(0xF, -53390, 1500, 3430, 132)
    SetChrChipByIndex(0xF, 23)
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x1)
    OP_43(0xF, 0x0, 0x6, 0x2)
    SetChrPos(0x10, -53720, 1500, 2050, 135)
    SetChrChipByIndex(0x10, 9)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x1)
    OP_43(0x10, 0x0, 0x6, 0x2)
    SetChrPos(0xC, -46440, 1500, 12150, 180)
    OP_43(0xC, 0x0, 0x6, 0x2)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1C, 140, 0, 1780, 180)
    OP_43(0x1C, 0x0, 0x6, 0x2)
    SetChrPos(0x12, -33720, 1500, 2810, 261)
    SetChrChipByIndex(0x12, 33)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x1)
    OP_43(0x12, 0x0, 0x6, 0x2)
    SetChrPos(0x15, -35370, 1500, 2950, 103)
    SetChrChipByIndex(0x15, 11)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x40)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x1)
    OP_43(0x15, 0x0, 0x6, 0x2)
    SetChrPos(0x14, -31820, 1500, 2029, 270)
    SetChrPos(0x13, -40690, 0, -510, 180)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x25, 0x80)
    Jump("loc_E1F")

    label("loc_D4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_E1F")
    ClearChrFlags(0x1D, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D9E")
    SetChrPos(0x13, -33800, 1500, 1300, 0)
    SetChrPos(0x14, -31760, 1500, 1300, 0)
    SetChrPos(0x12, -32930, 1600, 2650, 0)
    Jump("loc_E1F")

    label("loc_D9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE4")
    SetChrPos(0x13, -47400, 0, -1660, 90)
    SetChrPos(0x14, -33780, 1500, 2840, 0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x14, 0x10)
    Jump("loc_E1F")

    label("loc_DE4")

    SetChrPos(0x13, -47400, 0, -1660, 180)
    SetChrPos(0x14, -47400, 0, -2880, 0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x16, 0x10)
    SetChrFlags(0x39, 0x80)

    label("loc_E1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E2E")
    ClearChrFlags(0x11, 0x80)
    Jump("loc_E55")

    label("loc_E2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E45")
    SetChrFlags(0xA, 0x10)

    label("loc_E45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_E55")
    ClearChrFlags(0x11, 0x80)

    label("loc_E55")

    Return()

    # Function_0_8E6 end

    def Function_1_E56(): pass

    label("Function_1_E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E6E")
    OP_10(0x0, 0x0)
    OP_10(0x4, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x5, 0x1)

    label("loc_E6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8E")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)

    label("loc_E8E")

    Return()

    # Function_1_E56 end

    def Function_2_E8F(): pass

    label("Function_2_E8F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EB2")
    OP_8D(0xFE, -48200, 42570, -46450, 46500, 1000)
    Jump("Function_2_E8F")

    label("loc_EB2")

    Return()

    # Function_2_E8F end

    def Function_3_EB3(): pass

    label("Function_3_EB3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_114B")
    OP_8E(0xFE, 0xFFFF2CFC, 0x5DC, 0xBB8, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF3350, 0x5DC, 0xCE4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0xFA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x21FC, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5358, 0x5DC, 0x2580, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5358, 0x5DC, 0x2EE0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4D18, 0x5DC, 0x2EE0, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF4D7C, 0x5DC, 0x319C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF5FD8, 0x5DC, 0x319C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x2E7C, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF77AC, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF80A8, 0x5DC, 0x30D4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF80A8, 0x5DC, 0x1F40, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF6EB0, 0x5DC, 0xFA0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF6DE8, 0x5DC, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF72FC, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF748C, 0x5DC, 0xFFFFF7CC, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFF7428, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF81D5, 0x5DC, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF81D5, 0x5DC, 0x190, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7748, 0x5DC, 0x190, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0x960, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7040, 0x5DC, 0x2198, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF3990, 0x5DC, 0x2198, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x1CE8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF360C, 0x5DC, 0x9C4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF2FCC, 0x5DC, 0xC8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    Jump("Function_3_EB3")

    label("loc_114B")

    Return()

    # Function_3_EB3 end

    def Function_4_114C(): pass

    label("Function_4_114C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12CA")
    Sleep(2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1175")
    OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x3C, 0x7D0, 0x0)

    label("loc_1175")

    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE37C, 0x5DC, 0xFFFFFF9C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE37C, 0xCB2, 0x834, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFEC78, 0xCB2, 0x1004, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFE638, 0xCB2, 0x898, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFE638, 0x5DC, 0x0, 0x3E8, 0x0)
    OP_8E(0xFE, 0xFFFFE890, 0x5DC, 0xFFFFF574, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 200)
    Sleep(5000)
    OP_8E(0xFE, 0xFFFFEFFC, 0x5DC, 0xFFFFFBB4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF7CC, 0x0, 0xFFFFFB50, 0x3E8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_12A7")
    OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x3C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFB32, 0x0, 0x1130, 0x7D0, 0x0)
    Jump("loc_12BB")

    label("loc_12A7")

    OP_8E(0xFE, 0x578, 0x0, 0x5DC, 0x7D0, 0x0)

    label("loc_12BB")

    OP_8C(0xFE, 0, 200)
    Sleep(5000)
    Jump("Function_4_114C")

    label("loc_12CA")

    Return()

    # Function_4_114C end

    def Function_5_12CB(): pass

    label("Function_5_12CB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12EE")
    OP_8D(0xFE, -47100, -2490, -44490, -1060, 2000)
    Jump("Function_5_12CB")

    label("loc_12EE")

    Return()

    # Function_5_12CB end

    def Function_6_12EF(): pass

    label("Function_6_12EF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_13EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1382")

    ChrTalk(    #0
        0xFE,
        (
            "本店当前最大的问题是\x01",
            "定期船停航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "虽然筹集到了上等的葡萄酒，\x01",
            "但却缺乏运输手段……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "衷心希望\x01",
            "能够早日恢复。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_13E8")

    label("loc_1382")


    ChrTalk(    #3
        0xFE,
        (
            "本店当前最大的问题是\x01",
            "定期船停航了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "虽然筹集到了上等的葡萄酒，\x01",
            "但空中运输通道是必不可缺的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13E8")

    Jump("loc_19D2")

    label("loc_13EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_150E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C1")

    ChrTalk(    #5
        0xFE,
        (
            "为了应对这次状况，\x01",
            "老板梅贝尔市长\x01",
            "一直在忙碌着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "来到店里也只是稍做视察\x01",
            "就回市长官邸去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "虽然曾几次提醒\x01",
            "她注意身体，但……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "逼迫自己迎难而上的习惯\x01",
            "是从父亲那里遗传下来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_150B")

    label("loc_14C1")


    ChrTalk(    #9
        0xFE,
        (
            "老板好像也非常\x01",
            "繁忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "来到店里也只是稍做视察\x01",
            "就回市长官邸了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_150B")

    Jump("loc_19D2")

    label("loc_150E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_162C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1571")

    ChrTalk(    #11
        0xFE,
        (
            "享受葡萄酒的那种气氛\x01",
            "终于又回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "回过头来想想，\x01",
            "果然还是和平最重要。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1629")

    label("loc_1571")


    ChrTalk(    #13
        0xFE,
        (
            "欢迎光临。\x01",
            "欢迎来到安特洛丝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "享受葡萄酒的那种气氛\x01",
            "终于又回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "经常有人说\x01",
            "『空腹是最好的调味料』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "仿效这句话，\x01",
            "我们是不是可以说\x01",
            "『和平才是最棒的佐料』呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1629")

    Jump("loc_19D2")

    label("loc_162C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_171A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_168D")

    ChrTalk(    #17
        0xFE,
        (
            "超市的重建工程\x01",
            "加上拉文努村的复兴支援……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "老板梅贝尔市长也\x01",
            "终日忙碌。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1717")

    label("loc_168D")


    ChrTalk(    #19
        0xFE,
        (
            "超市的重建工程\x01",
            "加上拉文努村的复兴支援……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "老板梅贝尔市长\x01",
            "一直在忙碌着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "为了不劳烦到她，\x01",
            "我们尽力把店铺的经营做到最好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1717")

    Jump("loc_19D2")

    label("loc_171A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_183D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1768")

    ChrTalk(    #22
        0xFE,
        (
            "虽然混乱还在继续，\x01",
            "但本店依然照常营业。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "请多担待。\x02",
    )

    CloseMessageWindow()
    Jump("loc_183A")

    label("loc_1768")


    ChrTalk(    #24
        0xFE,
        (
            "欢迎光临。\x01",
            "昨天真是紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "但是，在非常时期\x01",
            "能无视利益团结起来…\x01",
            "这正是柏斯商人的传统。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "１０年前那场战争的时候，\x01",
            "本店也为难民们提供过伙食。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "今后若是有什么事的话，\x01",
            "也请让我们参与协助吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_183A")

    Jump("loc_19D2")

    label("loc_183D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1904")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1879")

    ChrTalk(    #28
        0xFE,
        (
            "老板联系过我们了，\x01",
            "看来情况非常严重。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1901")

    label("loc_1879")


    ChrTalk(    #29
        0xFE,
        (
            "老板联系过我们了，\x01",
            "看来情况非常严重。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "现在，正在为各位前来避难的\x01",
            "朋友准备热汤。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "喝一点热腾腾的东西\x01",
            "心情会比较平静吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1901")

    Jump("loc_19D2")

    label("loc_1904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_19D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1952")

    ChrTalk(    #32
        0xFE,
        (
            "必定会拿出\x01",
            "让各位满足的料理的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "请一定要好好品尝。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19D2")

    label("loc_1952")


    ChrTalk(    #34
        0xFE,
        (
            "欢迎光临。\x01",
            "欢迎来到安特洛丝。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "最棒的材料，最好的工作人员\x01",
            "将接待各位。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "请务必在我店\x01",
            "领略一下利贝尔料理的精髓。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_19D2")

    TalkEnd(0x8)
    Return()

    # Function_6_12EF end

    def Function_7_19D6(): pass

    label("Function_7_19D6")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1ABF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A79")

    ChrTalk(    #37
        0xFE,
        (
            "新出道的商人\x01",
            "干得不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "托他的福，特殊食材\x01",
            "的货源现在很充足。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A73")

    ChrTalk(    #39
        0xFE,
        (
            "……非常感激。\x01",
            "介绍了一位出色的商人给我们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A73")

    OP_A2(0x1)
    Jump("loc_1ABC")

    label("loc_1A79")


    ChrTalk(    #40
        0xFE,
        (
            "新出道的商人\x01",
            "干得不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "……虽然他的收集的种类非常极端。\x02",
    )

    CloseMessageWindow()

    label("loc_1ABC")

    Jump("loc_1F65")

    label("loc_1ABF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1B23")

    ChrTalk(    #42
        0xFE,
        (
            "就算没有了导力式的烹饪工具，\x01",
            "问题也不会很大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "真正的烹饪高手\x01",
            "是不会挑剔道具的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F65")

    label("loc_1B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1B8B")

    ChrTalk(    #44
        0xFE,
        (
            "食材总算进到货了，\x01",
            "恢复到平时的状态了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "这样就可以毫无顾虑地\x01",
            "放手做我的拿手好菜啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F65")

    label("loc_1B8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1CF5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C59")

    ChrTalk(    #46
        0xFE,
        (
            "由于定期船停航的缘故，\x01",
            "进货变得非常困难……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "不过好在多亏了那个新来的商人，\x01",
            "或许能够撑一段时间也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "虽然材料种类稍微有点极端，\x01",
            "但货源数量还是可以保证的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CF2")

    label("loc_1C59")


    ChrTalk(    #49
        0xFE,
        (
            "由于定期船停航的缘故，\x01",
            "食材的进货情况很紧张。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "花费时间过长，\x01",
            "有必要对菜单进行浓缩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "为了兴致勃勃赶来的客人，\x01",
            "这些事无论如何一定要避免……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF2")

    Jump("loc_1F65")

    label("loc_1CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_1DCA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D84")

    ChrTalk(    #52
        0xFE,
        "定期船好像停航了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "为了不使食材进货停滞，\x01",
            "必须先行动才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "唔……\x01",
            "现在就看新来的商人的表现了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DC7")

    label("loc_1D84")


    ChrTalk(    #55
        0xFE,
        "定期船好像停航了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "为了不使食材进货停滞，\x01",
            "必须尽早行动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DC7")

    Jump("loc_1F65")

    label("loc_1DCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1E0D")

    ChrTalk(    #57
        0xFE,
        (
            "经理满脸怒气的\x01",
            "来点东西吃……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "……出什么事了吗\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F65")

    label("loc_1E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1F65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E8E")

    ChrTalk(    #59
        0xFE,
        (
            "格露娜发明的料理\x01",
            "终于写进我们的菜单了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "她的料理完全发挥出她的特质，\x01",
            "我想应该能够形成一种崭新的风味。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F65")

    label("loc_1E8E")


    ChrTalk(    #61
        0xFE,
        (
            "格露娜发明的料理\x01",
            "终于写进我们的菜单了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "她的料理完全发挥出她的特质，\x01",
            "我想应该能够形成一种崭新的风味。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "菜单不能固定，\x01",
            "要不断给客人带来惊喜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "想成为一流的料理人\x01",
            "就是要不断追寻自我革新的力量。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1F65")

    TalkEnd(0x9)
    Return()

    # Function_7_19D6 end

    def Function_8_1F69(): pass

    label("Function_8_1F69")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F84")
    Call(0, 9)
    Jump("loc_1FAA")

    label("loc_1F84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_1F95")
    Call(2, 1)
    Jump("loc_1FAA")

    label("loc_1F95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1FA6")
    Call(2, 0)
    Jump("loc_1FAA")

    label("loc_1FA6")

    Call(0, 9)

    label("loc_1FAA")

    TalkEnd(0xA)
    Return()

    # Function_8_1F69 end

    def Function_9_1FAE(): pass

    label("Function_9_1FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_200A")

    ChrTalk(    #65
        0xA,
        (
            "今天太谢谢了。\x01",
            "真是帮了我们大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "那，若是有空的话，\x01",
            "请务必来店里吃饭。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B3")

    label("loc_200A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2138")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E1")

    ChrTalk(    #67
        0xA,
        "真不愧是罗宋厨师长……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xA,
        (
            "竟能用火炉把平常那些高级料理\x01",
            "简简单单的作出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        (
            "与之相比，\x01",
            "我真是差远了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xA,
        (
            "嗯～～热血沸腾了！\x01",
            "得好好锻炼本领了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "然后，总有一天一定\x01",
            "要赶上料理长！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2135")

    label("loc_20E1")


    ChrTalk(    #72
        0xA,
        (
            "和料理长比起来的话，\x01",
            "我还不成熟啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "嗯～～热血沸腾了！\x01",
            "得好好锻炼本领了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2135")

    Jump("loc_28B3")

    label("loc_2138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_220B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21C6")

    ChrTalk(    #74
        0xA,
        (
            "导，导力式炉子\x01",
            "用不了了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xA,
        (
            "看料理长优哉优哉的，\x01",
            "我就没有这么从容了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xA,
        (
            "不赶快掌握\x01",
            "炉灶的火候控制方法的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2208")

    label("loc_21C6")


    ChrTalk(    #77
        0xA,
        (
            "导力式火炉\x01",
            "不能使用了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xA,
        (
            "嗯～用火炉调理\x01",
            "能顺利完成吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2208")

    Jump("loc_28B3")

    label("loc_220B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_23AA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_232C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2284")

    ChrTalk(    #79
        0xA,
        (
            "定期船恢复了，\x01",
            "进货也恢复到原来的状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xA,
        (
            "感觉新菜单的研究\x01",
            "现在才算真正开始。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2329")

    label("loc_2284")


    ChrTalk(    #81
        0xA,
        (
            "定期船恢复了，\x01",
            "进货也恢复到原来的状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xA,
        (
            "稀有食材方面\x01",
            "有那个新出道的商人\x01",
            "在做调查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xA,
        (
            "感觉新菜单的研究\x01",
            "现在才算真正开始。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xA,
        "好，鼓足干劲加油吧！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2329")

    Jump("loc_23A7")

    label("loc_232C")


    ChrTalk(    #85
        0xA,
        (
            "虽然定期船恢复了，\x01",
            "进货也恢复了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xA,
        (
            "部分珍贵食材\x01",
            "还是很难弄到手呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xA,
        (
            "为了研究新菜单，\x01",
            "这个问题务必要解决啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23A7")

    Jump("loc_28B3")

    label("loc_23AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_25C5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2421")

    ChrTalk(    #88
        0xA,
        (
            "料理长好像也在为\x01",
            "进货的事烦恼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xA,
        (
            "和奥维德联手，\x01",
            "无论如何都要突破这次困境。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24E3")

    label("loc_2421")


    ChrTalk(    #90
        0xA,
        (
            "料理长好像也在为\x01",
            "进货的事烦恼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "和奥维德联手，\x01",
            "无论如何都要突破这次困境。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        (
            "虽然不知道为什么，\x01",
            "但那个人好像并不在乎\x01",
            "定期船停航。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xA,
        (
            "不知道是不是拥有和其它商人\x01",
            "不同的进货管道？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_24E3")

    Jump("loc_25C2")

    label("loc_24E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2540")

    ChrTalk(    #94
        0xA,
        (
            "料理长好像也在为\x01",
            "进货的事烦恼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xA,
        (
            "商人们因为超市的事\x01",
            "也没法顾及我们……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C2")

    label("loc_2540")


    ChrTalk(    #96
        0xA,
        (
            "料理长好像也在为\x01",
            "进货的事烦恼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        (
            "商人们因为超市的事\x01",
            "也没法顾及我们……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xA,
        (
            "啊，一感到不安，\x01",
            "舌头尝味的感觉会迟钝的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_25C2")

    Jump("loc_28B3")

    label("loc_25C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_26AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_262E")

    ChrTalk(    #99
        0xA,
        (
            "听莉诺说\x01",
            "好像有客人来相亲是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xA,
        (
            "如果能因为我们的料理\x01",
            "营造出不错的气氛就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A8")

    label("loc_262E")


    ChrTalk(    #101
        0xA,
        (
            "听莉诺说\x01",
            "好像有客人来相亲是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xA,
        (
            "这样的事\x01",
            "给人感觉压力很大呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xA,
        (
            "这种席位的气氛\x01",
            "会随料理的不同发生变化呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_26A8")

    Jump("loc_28B3")

    label("loc_26AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_279D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_271F")

    ChrTalk(    #104
        0xA,
        "好像店里的人在吵闹什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xA,
        (
            "但是……\x01",
            "我现在正忙着准备主菜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xA,
        "来，集中精神！集中精神！\x02",
    )

    CloseMessageWindow()
    Jump("loc_279A")

    label("loc_271F")


    ChrTalk(    #107
        0xA,
        "好像店里的人在吵闹什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xA,
        (
            "但是……\x01",
            "我现在正忙着准备主菜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        (
            "在这节骨眼上松懈的话，\x01",
            "成品可是会大大走样的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_279A")

    Jump("loc_28B3")

    label("loc_279D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_28B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_27FA")

    ChrTalk(    #110
        0xA,
        (
            "我制作的料理\x01",
            "终于写进菜单了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xA,
        (
            "当然我不会就此满足，\x01",
            "还要继续努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B3")

    label("loc_27FA")


    ChrTalk(    #112
        0xA,
        (
            "我制作的料理\x01",
            "终于写进菜单了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xA,
        (
            "不过这多亏了料理长用自己的时间\x01",
            "陪我做新菜的尝试啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xA,
        (
            "所以不能说是自己的实力，\x01",
            "现在绝对还不能满足呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xA,
        (
            "所以计划马上开始\x01",
            "新作品的研究。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_28B3")

    Return()

    # Function_9_1FAE end

    def Function_10_28B4(): pass

    label("Function_10_28B4")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_297F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_292C")

    ChrTalk(    #116
        0xFE,
        (
            "定期船好像\x01",
            "还没有恢复。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "正打算订购葡萄酒，\x01",
            "却发生这种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "啊，时机真的很糟糕啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_297C")

    label("loc_292C")


    ChrTalk(    #119
        0xFE,
        (
            "定期船好像\x01",
            "还没有恢复。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "正打算订购葡萄酒，\x01",
            "还在考虑的时候却出这种事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_297C")

    Jump("loc_2FC8")

    label("loc_297F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2A72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A13")

    ChrTalk(    #121
        0xFE,
        (
            "导力器停止的时候，\x01",
            "我在葡萄酒窖里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "结果在一片漆黑中\x01",
            "只能靠自己摸索走出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "结果身上满是灰尘。\x01",
            "怎么会那么巧呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2A6F")

    label("loc_2A13")


    ChrTalk(    #124
        0xFE,
        (
            "导力器停止时，\x01",
            "我在葡萄酒窖里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "在一片漆黑中靠摸索着…\x01",
            "想走出来真是太难了，可恶。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A6F")

    Jump("loc_2FC8")

    label("loc_2A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2B7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2ACD")

    ChrTalk(    #126
        0xFE,
        (
            "哎呀哎呀，今早的快递\x01",
            "终于把葡萄酒送来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "库存差一点\x01",
            "就没有了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7C")

    label("loc_2ACD")


    ChrTalk(    #128
        0xFE,
        (
            "哎呀哎呀，今早的快递\x01",
            "总算把葡萄酒送来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "每次定期船停班的时候\x01",
            "我都会很担心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "全靠这飞船\x01",
            "才能享受到世界上的各种美酒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "只要想到这个\x01",
            "就不会有太多怨言了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2B7C")

    Jump("loc_2FC8")

    label("loc_2B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2BE4")

    ChrTalk(    #132
        0xFE,
        (
            "柏斯地区的航空管制\x01",
            "似乎还没有解除。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "一部分品牌的葡萄酒\x01",
            "都已经快断货了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CB7")

    label("loc_2BE4")


    ChrTalk(    #134
        0xFE,
        "真差劲啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "柏斯地区的航空管制\x01",
            "似乎还没有解除。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "一部分品牌的葡萄酒\x01",
            "已经快把库存用光了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "库存最紧张的是\x01",
            "中等价格的葡萄酒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "因为来这里的客人大多是行家。\x01",
            "很清楚哪些酒质量高又价格合理。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2CB7")

    Jump("loc_2FC8")

    label("loc_2CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_2DB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2D23")

    ChrTalk(    #139
        0xFE,
        (
            "因为军队的作战\x01",
            "飞船又停开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "假如战斗持续太久的话，\x01",
            "销量大的葡萄酒会不够的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB5")

    label("loc_2D23")


    ChrTalk(    #141
        0xFE,
        "呼，真头疼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "因为军队的作战\x01",
            "飞船又停开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "诺桑普里亚产的葡萄酒\x01",
            "预定好了要送来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "真希望快点抓住龙，\x01",
            "好早日解除戒严。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2DB5")

    Jump("loc_2FC8")

    label("loc_2DB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_2E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2DF8")

    ChrTalk(    #145
        0xFE,
        (
            "虽然不是很清楚，\x01",
            "不过外面好像出什么事了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E5E")

    label("loc_2DF8")


    ChrTalk(    #146
        0xFE,
        (
            "虽然不是很清楚，\x01",
            "不过外面好像出什么事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "总之，\x01",
            "用箱子把矿泉水拿出去。\x01",
            "其他的以后再说。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2E5E")

    Jump("loc_2FC8")

    label("loc_2E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2FC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2ED2")

    ChrTalk(    #148
        0xFE,
        (
            "我正在和老板商量，\x01",
            "是不是也进一些东方的『清酒』\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "那个也有着不逊于葡萄酒\x01",
            "的丰富的味道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC8")

    label("loc_2ED2")


    ChrTalk(    #150
        0xFE,
        "我是这家店的品酒员。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "提起品酒员，\x01",
            "大多数人都是只热衷于葡萄酒，\x01",
            "而我的话则对所有酒类都在行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "我正在和老板商量，\x01",
            "是不是也进一些东方的『清酒』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "那个也有着不逊于葡萄酒\x01",
            "的丰富味道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "或许更适合配合清淡的食物\x01",
            "来吃也说不定。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2FC8")

    TalkEnd(0xB)
    Return()

    # Function_10_28B4 end

    def Function_11_2FCC(): pass

    label("Function_11_2FCC")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3078")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3040")

    ChrTalk(    #155
        0xFE,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "市里的情况已经\x01",
            "完全安定下来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "请各位客人\x01",
            "好好品尝我们的料理。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_3075")

    label("loc_3040")


    ChrTalk(    #158
        0xFE,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "请各位客人\x01",
            "好好品尝我们的料理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3075")

    Jump("loc_3570")

    label("loc_3078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3185")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_312E")

    ChrTalk(    #160
        0xFE,
        (
            "市里发生骚乱的时候，\x01",
            "我们正在店里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "协会前聚集了很多人，\x01",
            "一直争吵到深夜。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "因为从店里看去一片漆黑，\x01",
            "所以不知道发生了什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "啊，真的非常害怕。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_3182")

    label("loc_312E")


    ChrTalk(    #164
        0xFE,
        (
            "镇上发生骚乱的时候，\x01",
            "我们正在店里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "协会前聚集了很多人，\x01",
            "一直争吵到深夜。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3182")

    Jump("loc_3570")

    label("loc_3185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3280")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_31D8")

    ChrTalk(    #166
        0xFE,
        (
            "来相亲的帝国青年\x01",
            "已经回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "那位女学生\x01",
            "也回老家去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_327D")

    label("loc_31D8")


    ChrTalk(    #168
        0xFE,
        (
            "来相亲的帝国青年\x01",
            "已经回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xFE,
        (
            "那位女学生\x01",
            "也回老家去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "尽管如此，居然会来我们的餐厅相亲，\x01",
            "可真是万万没有想到啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "嗯。\x01",
            "一定都是出生自名门吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_327D")

    Jump("loc_3570")

    label("loc_3280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_32DC")

    ChrTalk(    #172
        0xFE,
        (
            "大家都在很卖力地为超市的\x01",
            "工程忙碌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "连这里也可以听到\x01",
            "机械轰鸣的声音呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3570")

    label("loc_32DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_3401")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3380")

    ChrTalk(    #174
        0xFE,
        (
            "坐在相亲席上的女性……\x01",
            "怎么看都好像是学生啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "那种年纪就来相亲，\x01",
            "是不是稍微着急了一点啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "还，还是说会这么想的我\x01",
            "还比较幼稚呢……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33FE")

    label("loc_3380")


    ChrTalk(    #177
        0xFE,
        (
            "看起来，\x01",
            "那桌人好像在相亲……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "那边那位女性……\x01",
            "怎么看都好像是学生啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "那种年纪就来相亲，\x01",
            "稍微着急了一点啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_33FE")

    Jump("loc_3570")

    label("loc_3401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_34A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3462")

    ChrTalk(    #180
        0xFE,
        (
            "超市被巨大的魔兽\x01",
            "袭击了是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "总之得把前来避难\x01",
            "的人们带到座位上。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A0")

    label("loc_3462")


    ChrTalk(    #182
        0xFE,
        (
            "超市被巨大的魔兽\x01",
            "袭击了是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "真不敢相信……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_34A0")

    Jump("loc_3570")

    label("loc_34A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3570")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_34FB")

    ChrTalk(    #184
        0xFE,
        (
            "相亲的对象\x01",
            "好像已经到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        (
            "是吗，太好了。\x01",
            "接下来就上菜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3570")

    label("loc_34FB")


    ChrTalk(    #186
        0xFE,
        (
            "今天预定要见\x01",
            "来自帝国的客人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "但是怎么说呢，\x01",
            "这好像是为了相亲而设的桌子哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "嗯，对象是\x01",
            "王国的人吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3570")

    TalkEnd(0xC)
    Return()

    # Function_11_2FCC end

    def Function_12_3574(): pass

    label("Function_12_3574")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3688")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_361B")

    ChrTalk(    #189
        0xFE,
        (
            "嗯…\x01",
            "这味道尝起来和平时一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "这里的餐厅\x01",
            "应该也不能使用导力炉才对……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "即使如此，味道还是维持原来的水平，\x01",
            "真不愧是安特洛丝啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_3685")

    label("loc_361B")


    ChrTalk(    #192
        0xFE,
        (
            "这里的餐厅\x01",
            "应该也不能使用导力炉才对……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "即使如此，味道还是维持原来的水平，\x01",
            "真不愧是安特洛丝啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3685")

    Jump("loc_3BB5")

    label("loc_3688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_376B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3714")

    ChrTalk(    #194
        0xFE,
        (
            "唔唔……\x01",
            "完全以为是导力器的故障……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "据我所见，\x01",
            "市里的情况有点异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "那么，这么说来，\x01",
            "究竟出什么事了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_3768")

    label("loc_3714")


    ChrTalk(    #197
        0xFE,
        (
            "因为导力器发生故障，\x01",
            "市里的情况有点异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "唔唔……\x01",
            "这个世界还真是奇妙……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3768")

    Jump("loc_3BB5")

    label("loc_376B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3884")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_37C3")

    ChrTalk(    #199
        0xFE,
        "和年轻人交谈果然有益啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "那个年轻人也为了取得\x01",
            "成功而努力着。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3881")

    label("loc_37C3")


    ChrTalk(    #201
        0xFE,
        (
            "哎呀，这几天，\x01",
            "和碰巧相识的一个新手商人\x01",
            "聊了聊关于买卖的话题……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "和年轻人交谈果然有益啊。\x01",
            "原本打算传授他人知识的我\x01",
            "反而受了鼓励啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "哈哈，真希望今后\x01",
            "还能在这里探讨问题啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3881")

    Jump("loc_3BB5")

    label("loc_3884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_38F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_38E9")

    ChrTalk(    #204
        0xFE,
        (
            "面对面做买卖，终究\x01",
            "是人与人的应对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "单纯的追求数字，\x01",
            "总有一天会吃苦头的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38ED")

    label("loc_38E9")

    Call(0, 25)

    label("loc_38ED")

    Jump("loc_3BB5")

    label("loc_38F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_39F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3953")

    ChrTalk(    #206
        0xFE,
        (
            "昨天遇到了一位\x01",
            "即将在超市里开店的年轻人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "并和他约定\x01",
            "今天也在这里见面。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39EF")

    label("loc_3953")


    ChrTalk(    #208
        0xFE,
        (
            "昨天遇到了一位\x01",
            "即将在超市里开店的年轻人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "因为想给他一些生意上的建议，\x01",
            "所以今天也约他在这里见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "哈哈，和晚辈交谈\x01",
            "真的是年长者的乐趣啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_39EF")

    Jump("loc_3BB5")

    label("loc_39F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_3B35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3A6D")

    ChrTalk(    #211
        0xFE,
        (
            "这个年轻人在商店即将开业前\x01",
            "被卷入了某起事件当中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "我也曾在超市开过店，\x01",
            "假如能帮上他的忙就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B32")

    label("loc_3A6D")


    ChrTalk(    #213
        0xFE,
        (
            "好像是\x01",
            "有某种巨大的怪物袭击了超市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "这位年轻人在即将开业的时候，\x01",
            "被卷入了某起事件当中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "一切都即将开始的时候，\x01",
            "遇到了这种事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "我也曾在超市开过店，\x01",
            "假如能帮上他的忙就好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3B32")

    Jump("loc_3BB5")

    label("loc_3B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_3BB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3B54")

    ChrTalk(    #217
        0xFE,
        "嗯嗯……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BB5")

    label("loc_3B54")


    ChrTalk(    #218
        0xFE,
        "嗯嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        (
            "嗯，这肉汁……\x01",
            "菜式新而且味道也非常棒啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "这里的料理\x01",
            "总是让人期待啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3BB5")

    TalkEnd(0xD)
    Return()

    # Function_12_3574 end

    def Function_13_3BB9(): pass

    label("Function_13_3BB9")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_3C9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C48")

    ChrTalk(    #221
        0xFE,
        (
            "城里的人们\x01",
            "虽然又有了精神……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "但这没有导力器的日子\x01",
            "究竟还要持续多久。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "一想到这个\x01",
            "实在没法尽情笑出来啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3C9C")

    label("loc_3C48")


    ChrTalk(    #224
        0xFE,
        (
            "但这没有导力器的日子\x01",
            "究竟还要持续多久。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "一想到这个\x01",
            "实在没法尽情笑出来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C9C")

    Jump("loc_4272")

    label("loc_3C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3DB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D5B")

    ChrTalk(    #226
        0xFE,
        "夜晚的骚乱可真严重啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "若没有梅贝尔市长出面说服的话，\x01",
            "险些就爆发暴动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "现在明明是\x01",
            "考验大家明辨是非能力的时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "那种丢人的举动\x01",
            "再也不想看到了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_3DAE")

    label("loc_3D5B")


    ChrTalk(    #230
        0xFE,
        "夜晚的骚乱可真严重啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "若没有梅贝尔市长出面说服的话，\x01",
            "险些就爆发暴动了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DAE")

    Jump("loc_4272")

    label("loc_3DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3E9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3DF9")

    ChrTalk(    #232
        0xFE,
        (
            "这肉汁\x01",
            "好像是道新菜式吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        "……嗯，味道很好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E98")

    label("loc_3DF9")


    ChrTalk(    #234
        0xFE,
        (
            "哎呀，之前丝毫\x01",
            "没有察觉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "这肉汁\x01",
            "好像是道新菜式吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "我可真是的……\x01",
            "明明吃过很多次了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "是啊，发生事件的期间\x01",
            "实在太多事情让人分心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3E98")

    Jump("loc_4272")

    label("loc_3E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3FBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3EFE")

    ChrTalk(    #238
        0xFE,
        (
            "我觉得梅贝尔市长\x01",
            "做的很出色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "父亲一定在女神爱德丝的身旁\x01",
            "对着她微笑吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FBB")

    label("loc_3EFE")


    ChrTalk(    #240
        0xFE,
        (
            "前市长的政治手段\x01",
            "真的很出色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "现任市长梅贝尔小姐\x01",
            "是前市长的亲生女儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "虽然市民经常拿她和她父亲比较。\x01",
            "但我认为她做得很出色。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "父亲一定在女神爱德丝的身旁\x01",
            "对着她微笑吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3FBB")

    Jump("loc_4272")

    label("loc_3FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_4084")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4010")

    ChrTalk(    #244
        0xFE,
        (
            "看着现在的城市\x01",
            "让我想起了战争……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_4081")

    label("loc_4010")


    ChrTalk(    #246
        0xFE,
        (
            "超市的修复工程，\x01",
            "在街上走的军人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "一切都和１０年前的战争\x01",
            "一摸一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_4081")

    Jump("loc_4272")

    label("loc_4084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_418D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_40F9")

    ChrTalk(    #249
        0xFE,
        (
            "在１０年前的那场战争里\x01",
            "也听到过刚才的声音。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "石造的建筑物坍塌时\x01",
            "肯定会发出那样的声音的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_418A")

    label("loc_40F9")


    ChrTalk(    #251
        0xFE,
        "刚才那声巨响……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "让我想起了\x01",
            "１０年前的那场战争……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "那个时候也是，\x01",
            "整个城市都被那种声音回绕着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        "建筑物……倒塌的声音啦……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_418A")

    Jump("loc_4272")

    label("loc_418D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_4272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_41E8")

    ChrTalk(    #255
        0xFE,
        (
            "虽然帝国的人\x01",
            "在这里并不罕见……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "但还是……\x01",
            "有种说不出的感觉……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4272")

    label("loc_41E8")


    ChrTalk(    #257
        0xFE,
        (
            "那边那张桌子的客人……\x01",
            "好像是帝国的人吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "互不侵犯条约也签订了，\x01",
            "隔阂虽然不像以前那么大……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "但还是\x01",
            "有种说不出的感觉……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_4272")

    TalkEnd(0xE)
    Return()

    # Function_13_3BB9 end

    def Function_14_4276(): pass

    label("Function_14_4276")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_42D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42B8")

    ChrTalk(    #260
        0xFE,
        "我也在赶时间。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        "快点开始商谈吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_42CE")

    label("loc_42B8")


    ChrTalk(    #262
        0xFE,
        "快点开始商谈吧。\x02",
    )

    CloseMessageWindow()

    label("loc_42CE")

    Jump("loc_4656")

    label("loc_42D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_4397")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4305")

    ChrTalk(    #263
        0xFE,
        (
            "哪里，这次\x01",
            "十分感谢您的协助。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4394")

    label("loc_4305")


    ChrTalk(    #264
        0xFE,
        (
            "哪里，这次\x01",
            "十分感谢您的协助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "超市被封锁的时候\x01",
            "有点不知所措……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        (
            "不过托各位的福，\x01",
            "本商会非但没有受到损失，\x01",
            "反而还获得了利益。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_4394")

    Jump("loc_4656")

    label("loc_4397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_44C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4414")

    ChrTalk(    #267
        0xFE,
        (
            "如果在果物进货方面遇到了困难，\x01",
            "本商会愿意提供储备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "哪里，毕竟是非常时期，\x01",
            "价格按照平常的就行了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44BE")

    label("loc_4414")


    ChrTalk(    #269
        0xFE,
        (
            "如果是拉文努村产的水果的话，\x01",
            "本商会的储备非常充足。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "看各位好像很为难，\x01",
            "若是不嫌弃的话我们来提供这些水果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "哪里，毕竟是非常时期，\x01",
            "价格按照平常的就行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_44BE")

    Jump("loc_4656")

    label("loc_44C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_451F")

    ChrTalk(    #272
        0xFE,
        (
            "继超市被封锁后\x01",
            "定期船也被停航了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "真为难啊。\x01",
            "这样的话进货就停止了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4656")

    label("loc_451F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_45FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_4582")

    ChrTalk(    #274
        0xFE,
        (
            "封锁超市的话，\x01",
            "会使物价发生很大的变化。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "这、这样的话商谈\x01",
            "就从头开始啰。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45FA")

    label("loc_4582")


    ChrTalk(    #276
        0xFE,
        (
            "在，在超市\x01",
            "发生这种事……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "这、这样的话商谈\x01",
            "就从头开始啰。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "通路被封锁的话\x01",
            "会使物价发生很大的变化。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_45FA")

    Jump("loc_4656")

    label("loc_45FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_4656")

    ChrTalk(    #279
        0xFE,
        (
            "关于下次的买卖，\x01",
            "这样的价格如何？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "即便和竞争公司相比\x01",
            "也是相当优惠的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4656")

    TalkEnd(0xF)
    Return()

    # Function_14_4276 end

    def Function_15_465A(): pass

    label("Function_15_465A")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_46F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46C0")

    ChrTalk(    #281
        0xFE,
        (
            "这么急把你叫来，\x01",
            "很抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "是有话要和你说，\x01",
            "希望能尽快把买卖定下来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_46F5")

    label("loc_46C0")


    ChrTalk(    #283
        0xFE,
        (
            "这么急把你叫来，\x01",
            "很抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "这次也请多关照。\x02",
    )

    CloseMessageWindow()

    label("loc_46F5")

    Jump("loc_4A8C")

    label("loc_46F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_480D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4773")

    ChrTalk(    #285
        0xFE,
        (
            "抛开这笔交易是否有利润不谈，\x01",
            "但总算还做得成买卖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "双方只要互相协助的话，\x01",
            "果然还是有好的结果的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_480A")

    label("loc_4773")


    ChrTalk(    #287
        0xFE,
        (
            "哪里哪里，\x01",
            "这都多亏了您。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "这次的交易虽然是\x01",
            "不考虑利益的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "总算是……\x01",
            "我们也得到很不错的商业伙伴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "定期船提前恢复\x01",
            "起作用了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_480A")

    Jump("loc_4A8C")

    label("loc_480D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_4906")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_4872")

    ChrTalk(    #291
        0xFE,
        (
            "海产品的进货\x01",
            "请交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        (
            "毕竟是非常时期，\x01",
            "就让我们互相协助经营下去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4903")

    label("loc_4872")


    ChrTalk(    #293
        0xFE,
        (
            "那么的话，\x01",
            "请交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "货物还有一部分\x01",
            "保管在柏斯的仓库。\x01",
            "应该就能够救急了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "毕竟是非常时期，\x01",
            "就让我们互相协助经营下去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_4903")

    Jump("loc_4A8C")

    label("loc_4906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_496F")

    ChrTalk(    #296
        0xFE,
        (
            "拉文努村\x01",
            "的果树园好像也被破坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "哎呀，真头痛。\x01",
            "我们的水果几乎都是\x01",
            "从那里进货的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A8C")

    label("loc_496F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_4A2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_49CF")

    ChrTalk(    #298
        0xFE,
        "没想到会发生这样的事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "本次的商业洽谈\x01",
            "进展的还算比较顺利，不过……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A2C")

    label("loc_49CF")


    ChrTalk(    #300
        0xFE,
        (
            "嗯……\x01",
            "好像是非常严重的事态呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "现在正在进行中的交易\x01",
            "必须要重新审查一遍才行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_4A2C")

    Jump("loc_4A8C")

    label("loc_4A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_4A8C")

    ChrTalk(    #302
        0xFE,
        (
            "不，很抱歉，\x01",
            "这样的价格我们无法答应。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        (
            "现在物流也通畅了，\x01",
            "库存应该很充裕吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A8C")

    TalkEnd(0x10)
    Return()

    # Function_15_465A end

    def Function_16_4A90(): pass

    label("Function_16_4A90")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BE5")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇123老爸帮忙通关＋关联任务完全称霸】\x01",      # 0
            "【◇123老爸帮忙通关】\x01",                        # 1
            "【◇101通关】\x01",                                # 2
            "【◇后编未接触】\x01",                             # 3
            "【◇５章看初次】\x01",                             # 4
            "【◇不变更】\x01",                                 # 5
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4B5A"),
        (1, "loc_4B77"),
        (2, "loc_4B94"),
        (3, "loc_4BB1"),
        (4, "loc_4BCE"),
        (5, "loc_4BE2"),
        (SWITCH_DEFAULT, "loc_4BE5"),
    )


    label("loc_4B5A")

    OP_28(0x7B, 0x4, 0x10)
    OP_28(0x7B, 0x1, 0x8)
    OP_28(0x65, 0x4, 0x10)
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x1F, 0x4, 0x10)
    Jump("loc_4BE5")

    label("loc_4B77")

    OP_28(0x7B, 0x4, 0x10)
    OP_28(0x7B, 0x1, 0x8)
    OP_28(0x65, 0x3, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_4BE5")

    label("loc_4B94")

    OP_28(0x7B, 0x3, 0x10)
    OP_28(0x7B, 0x2, 0x8)
    OP_28(0x65, 0x4, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_4BE5")

    label("loc_4BB1")

    OP_28(0x7B, 0x3, 0x10)
    OP_28(0x7B, 0x2, 0x8)
    OP_28(0x65, 0x3, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_4BE5")

    label("loc_4BCE")

    OP_28(0x7B, 0x4, 0x10)
    OP_28(0x7B, 0x1, 0x8)
    OP_28(0x7B, 0x1, 0x8000)
    Jump("loc_4BE5")

    label("loc_4BE2")

    Jump("loc_4BE5")

    label("loc_4BE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58EC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57AF")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -35260, 0, 42950, 90)
    SetChrPos(0xF7, -35690, 0, 41950, 90)
    SetChrPos(0xF8, -36550, 0, 43150, 90)
    SetChrPos(0xF9, -36640, 0, 41730, 90)
    OP_8C(0x11, 270, 0)
    OP_4A(0x11, 255)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C7A")
    SetChrPos(0x4, -35970, 0, 44280, 135)

    label("loc_4C7A")

    OP_6D(-35000, 0, 42570, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #304
        0x11,
        "噢噢，各位游击士！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x11,
        (
            "有好消息啊！\x01",
            "商业洽谈成功了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x11,
        (
            "我终于成为能够\x01",
            "出入一流餐厅的商人了！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #307
        0x101,
        (
            "#1004F真、真的！？\x02\x03",

            "#1001F说的是和安特洛丝的交易吧。\x01",
            "真厉害，叔叔！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x102,
        "#1040F祝贺你。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x11,
        (
            "各位游击士。\x01",
            "真的非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x11,
        (
            "能够和这家店做买卖\x01",
            "是我多年来的梦想。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x11,
        (
            "这梦想终于实现了……\x01",
            "这全都是各位的功劳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x101,
        (
            "#1017F嘿嘿，谢谢。\x02\x03",

            "不过，之所以会有今天\x01",
            "全都是叔叔自己努力的结果啊。\x02\x03",

            "我们只是稍微\x01",
            "帮了一点小忙而已啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5469")

    ChrTalk(    #313
        0x11,
        (
            "嗯……\x01",
            "和你们认识好像也已经很久了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x11,
        (
            "明明给你们添了很多麻烦，\x01",
            "你们却能一直帮助我到现在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x11,
        (
            "作为对过去的答谢，\x01",
            "请收下我这份谢礼。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #316
        0x101,
        (
            "#1020F难，难道……\x02\x03",

            "又想送很多奇怪的蘑菇\x01",
            "给我们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x11,
        "嗯？想要蘑菇吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x11,
        (
            "这样的话，\x01",
            "这里还有很多库存……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #319
        0x101,
        (
            "#1007F不，不，不用了。\x02\x03",

            "#1015F……抱歉。\x01",
            "打断你说话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x11,
        "嗯，刚才说到谢礼是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x11,
        (
            "所谓谢礼并不是别的。\x01",
            "那就是我奥维德商会的会员资格。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x11,
        (
            "这可不是一般的会员，\x01",
            "是最高级别的白金会员资格哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x101,
        "#1019F白、白金会员资格？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x11,
        (
            "啊，如你所知，\x01",
            "我是专门做食材生意的商人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x11,
        (
            "但我只和其他职业商人做买卖。\x01",
            "面向一般顾客的零售生意我是不做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x11,
        (
            "但是曾经受到你们太多的照顾。\x01",
            "所以我打算破格同意和你们交易。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x102,
        (
            "#1044F这也就是说……\x02\x03",

            "我可以从叔叔这里\x01",
            "买东西啰？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x11,
        "就是这么回事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x11,
        (
            "需要什么食材的话\x01",
            "就和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x11,
        (
            "只要支付适当的金额，\x01",
            "不管什么食材都可以为你们准备。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5258")

    ChrTalk(    #331
        0x104,
        (
            "#033F噢，这下厉害了。\x02\x03",

            "真的什么种类的\x01",
            "食材都有吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5330")

    label("loc_5258")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52A1")

    ChrTalk(    #332
        0x108,
        (
            "#070F噢，这可厉害了。\x02\x03",

            "真的什么种类的\x01",
            "食材都有吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5330")

    label("loc_52A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52E6")

    ChrTalk(    #333
        0x106,
        (
            "#052F这可真厉害。\x02\x03",

            "真的什么种类的\x01",
            "食材都有吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5330")

    label("loc_52E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5330")

    ChrTalk(    #334
        0x103,
        (
            "#023F哎呀，这可真厉害啊。\x02\x03",

            "真的什么种类的\x01",
            "食材都有吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5330")


    ChrTalk(    #335
        0x11,
        (
            "是啊，只要是利贝尔王国内\x01",
            "可见的食材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x11,
        (
            "各位游击士\x01",
            "很多时候都需要自己做饭吃吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x11,
        (
            "请不必客气，\x01",
            "尽管利用吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x101,
        (
            "#1006F嗯，有需要的话一定来。\x01",
            "那就先这样吧。\x02\x03",

            "那么，差不多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x11,
        (
            "噢，对不起。\x01",
            "耽误了各位这么长时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x11,
        "那么，我一直在这里经营。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x102,
        "#1040F是，告辞了。\x02",
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x4000)
    OP_A2(0xC)
    OP_28(0x7B, 0x1, 0x8000)
    EventEnd(0x0)
    OP_8C(0x11, 0, 0)
    OP_4B(0x11, 255)
    Return()

    label("loc_5469")


    ChrTalk(    #342
        0x11,
        (
            "啊啊，\x01",
            "或许的确是这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0x11,
        (
            "但是，最后再加把劲这样的事\x01",
            "我从来没有办到过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x11,
        (
            "为表感谢，\x01",
            "请收在下一份薄礼。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #345
        0x101,
        (
            "#1020F难，难道……\x02\x03",

            "又想送很多奇怪的蘑菇\x01",
            "给我们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x11,
        "嗯？想要蘑菇吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x11,
        (
            "这样的话，\x01",
            "这里还有很多库存……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #348
        0x101,
        (
            "#1007F不，不，不用了。\x02\x03",

            "#1015F……抱歉。\x01",
            "打断你说话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x11,
        "嗯，刚才说到谢礼是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x11,
        (
            "所谓谢礼并不是别的。\x01",
            "那就是我奥维德商会的利用权。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x101,
        "#1011F利用权？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x11,
        (
            "嗯，我的店是做批发生意的……\x01",
            "面向一般顾客的零售生意我是不做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x11,
        (
            "但是你们曾经照顾过我。\x01",
            "我打算破格给你们交易的权力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x11,
        (
            "不过交易的内容\x01",
            "仅限于一般的商品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x101,
        (
            "#1017F嘿，是这样啊。\x01",
            "谢谢，真是帮了大忙了。\x02\x03",

            "毕竟现在情况很乱，普通的食材也\x01",
            "不容易搞到嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x102,
        (
            "#1040F谢谢。\x01",
            "帮了大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x11,
        (
            "需要什么食材的话\x01",
            "就和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x11,
        (
            "店面出售的食材\x01",
            "都已经摆上货架了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_28(0x7B, 0x1, 0x8000)
    EventEnd(0x0)
    OP_8C(0x11, 0, 0)
    OP_4B(0x11, 255)
    Return()

    label("loc_57AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_57EE")

    ChrTalk(    #359
        0x11,
        "喔，你们几个！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x11,
        "之前真的是劳烦你们了啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_580E")

    label("loc_57EE")


    ChrTalk(    #361
        0x11,
        "哎呀？你们几个是游击士吗。\x02",
    )

    CloseMessageWindow()

    label("loc_580E")


    ChrTalk(    #362
        0x11,
        (
            "现在物流机能停滞，\x01",
            "想要保证食物充足是很困难的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x11,
        (
            "正是这种时期，\x01",
            "才是我们奥维德商会出场的时候！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x11,
        (
            "我商会会把从独有的渠道获得的山珍海味\x01",
            "以适当的价格提供给大家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x11,
        (
            "来，赶紧来\x01",
            "看一看我们的商品吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x8000)
    OP_A2(0xC)
    Jump("loc_6367")

    label("loc_58EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6367")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -35260, 0, 42950, 90)
    SetChrPos(0xF7, -35690, 0, 41950, 90)
    SetChrPos(0xF8, -36550, 0, 43150, 90)
    SetChrPos(0xF9, -36640, 0, 41730, 90)
    OP_8C(0x11, 270, 0)
    OP_4A(0x11, 255)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5972")
    SetChrPos(0x4, -35970, 0, 44280, 135)

    label("loc_5972")

    OP_6D(-35000, 0, 42570, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #366
        0x11,
        (
            "真没想到能这么简单\x01",
            "就可以谈下这个的商谈……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x11,
        (
            "各位游击士。\x01",
            "真的非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x11,
        (
            "和一流餐厅做买卖，\x01",
            "是我多年来的梦想。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x11,
        (
            "很快就会实现了……\x01",
            "这全都是各位的功劳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x101,
        (
            "#1017F嘿嘿，谢谢。\x02\x03",

            "不过，之所以会有今天\x01",
            "全都是叔叔自己努力的结果啊。\x02\x03",

            "我们只是稍微\x01",
            "帮了点小忙而已。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B3F")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇奥维德关联任务完全称霸】\x01",      # 0
            "【◇不变更】\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5B2A"),
        (1, "loc_5B3C"),
        (SWITCH_DEFAULT, "loc_5B3F"),
    )


    label("loc_5B2A")

    OP_28(0x65, 0x4, 0x10)
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x1F, 0x4, 0x10)
    Jump("loc_5B3F")

    label("loc_5B3C")

    Jump("loc_5B3F")

    label("loc_5B3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60AB")

    ChrTalk(    #371
        0x11,
        (
            "嗯……\x01",
            "和你们认识好像也已经很久了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x11,
        (
            "明明给你们添了很多麻烦，\x01",
            "你们却能一直帮助我到现在。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x11,
        (
            "作为对过去的答谢，\x01",
            "请收下我这份谢礼。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #374
        0x101,
        (
            "#1020F难，难道……\x02\x03",

            "又想送很多奇怪的蘑菇\x01",
            "给我们？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x11,
        "嗯？想要蘑菇吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x11,
        (
            "这样的话，\x01",
            "这里还有很多库存……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #377
        0x101,
        (
            "#1007F不，不，不用了。\x02\x03",

            "#1015F……抱歉。\x01",
            "打断你说话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x11,
        "嗯，刚才说到谢礼是吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x11,
        (
            "所谓谢礼并不是别的。\x01",
            "这是我奥维德商会的利用权。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x101,
        "#1011F啊？利用权？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x11,
        (
            "啊，如你所知，\x01",
            "我是专门做食材生意的商人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x11,
        (
            "但我只和其他职业商人做买卖。\x01",
            "面向一般顾客的零售生意我是不做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x11,
        (
            "但是曾经受到你们太多的照顾。\x01",
            "我打算破格给你们交易的权力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x101,
        (
            "#1000F也就是说……\x02\x03",

            "能够在叔叔的店里\x01",
            "买到东西？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x11,
        "就是这么回事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x11,
        (
            "需要什么食材的话\x01",
            "就和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x11,
        (
            "只要支付适当的金额，\x01",
            "不管什么食材都可以为你准备。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5ED0")

    ChrTalk(    #388
        0x104,
        (
            "#033F嗯，这下厉害了。\x02\x03",

            "真的什么种类的\x01",
            "食材都有吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FA6")

    label("loc_5ED0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F19")

    ChrTalk(    #389
        0x108,
        (
            "#070F噢，这可厉害了。\x02\x03",

            "真的什么种类的\x01",
            "食材都有吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FA6")

    label("loc_5F19")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F5E")

    ChrTalk(    #390
        0x106,
        (
            "#052F这可真厉害。\x02\x03",

            "真的什么种类的\x01",
            "食材都有吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FA6")

    label("loc_5F5E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FA6")

    ChrTalk(    #391
        0x103,
        (
            "#020F哎呀，这可真厉害。\x02\x03",

            "真的什么种类的\x01",
            "食材都有吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FA6")


    ChrTalk(    #392
        0x11,
        (
            "是啊，只要是利贝尔王国内\x01",
            "可见的食材。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x11,
        (
            "各位游击士\x01",
            "很多时候都需要自己做饭吃吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x11,
        (
            "请不必客气，\x01",
            "尽管利用吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x101,
        (
            "#1006F嗯，有需要的话。\x01",
            "那就这样吧。\x02\x03",

            "那么，差不多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x11,
        (
            "噢，对不起。\x01",
            "耽误了各位这么长时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x11,
        "那么，我一直在这里经营。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_28(0x7B, 0x1, 0x4000)
    Jump("loc_6357")

    label("loc_60AB")


    ChrTalk(    #398
        0x11,
        (
            "啊啊，\x01",
            "或许的确是这样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x11,
        (
            "就因为这一点\x01",
            "我也要感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x11,
        (
            "这就破例给你们\x01",
            "我商会的利用权资格。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x101,
        "#1011F啊？利用权？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x11,
        (
            "啊，如你所知，\x01",
            "我是个专门做食材生意的商人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x11,
        (
            "但我只和其他职业商人做买卖。\x01",
            "面向一般顾客的零售生意我是不做的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x11,
        (
            "但是你们曾经照顾过我。\x01",
            "我打算破格给你们交易的权力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x101,
        (
            "#1000F也就是说……\x02\x03",

            "能够在叔叔的店里\x01",
            "买到东西？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x11,
        "就是这么回事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x11,
        (
            "需要什么食材的话\x01",
            "就和我说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x11,
        (
            "本店的商品非常齐全，\x01",
            "这可是其它商店所不能媲美的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #409
        0x101,
        (
            "#1018F是吗，这可真方便。\x02\x03",

            "#1006F嗯，有机会的话。\x01",
            "我们一定光顾的。\x02\x03",

            "那么，差不多……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0x11,
        (
            "噢，对不起。\x01",
            "耽误了各位这么长时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x11,
        (
            "那么，各位游击士，\x01",
            "你们也要继续努力做好自己的工作哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x101,
        "#1001F再会，叔叔。\x02",
    )

    CloseMessageWindow()

    label("loc_6357")

    OP_A2(0xC)
    OP_28(0x7B, 0x1, 0x8000)
    EventEnd(0x0)
    OP_4B(0x11, 255)
    Return()

    label("loc_6367")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x4000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8000)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6436")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6425")
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63ED")

    ChrTalk(    #413
        0x11,
        "喔哟，要买点什么？\x02",
    )

    CloseMessageWindow()

    label("loc_63ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_63FD")
    OP_A9(0x38)
    Jump("loc_63FF")

    label("loc_63FD")

    OP_A9(0x37)

    label("loc_63FF")

    OP_A3(0xC)

    ChrTalk(    #414
        0x11,
        "那么，欢迎下次再来。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    TalkEnd(0x11)
    Return()

    label("loc_6425")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6436")
    TalkEnd(0x11)
    Return()

    label("loc_6436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6953")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_654B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64EE")

    ChrTalk(    #415
        0x11,
        (
            "我的食材在厨师长那里\x01",
            "也有很高的评价。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x11,
        (
            "对于职业食品商来说，\x01",
            "我们的产品优秀是理所当然的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x11,
        (
            "不过说真的，我还挺高兴的。\x01",
            "毕竟吃了这么多苦嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_6548")

    label("loc_64EE")


    ChrTalk(    #418
        0x11,
        (
            "我的食材在厨师长那里\x01",
            "也有很高的评价。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x11,
        (
            "对于职业食品商来说，\x01",
            "自然是理所当然的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6548")

    Jump("loc_6950")

    label("loc_654B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_665D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65F0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6580")

    ChrTalk(    #420
        0x11,
        "噢，是你们啊。\x02",
    )

    CloseMessageWindow()

    label("loc_6580")


    ChrTalk(    #421
        0x11,
        (
            "外面虽然很乱，\x01",
            "但我的生意却进行的非常顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x11,
        (
            "计划在大多数物流管道都停止之前，\x01",
            "扩大我的销售渠道。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_665A")

    label("loc_65F0")


    ChrTalk(    #423
        0x11,
        (
            "外面虽然很乱，\x01",
            "但我的生意却进行的非常顺利。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x11,
        (
            "计划在大多数物流管道都停止之前，\x01",
            "扩大我的销售渠道。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_665A")

    Jump("loc_6950")

    label("loc_665D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_670A")

    ChrTalk(    #425
        0x11,
        (
            "定期船虽然好像恢复了，\x01",
            "但对我的生意却一点影响也没有。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x11,
        (
            "因为我们商会\x01",
            "早准备好了各种极其珍贵的食材呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0x11,
        (
            "哼哼哼，\x01",
            "这可是其它同行所模仿不来的食材阵容啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6950")

    label("loc_670A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_681B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_6785")

    ChrTalk(    #428
        0x11,
        (
            "我们奥维德商会有自己的经营特色，\x01",
            "食材也都是自行收集的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x11,
        (
            "不管定期船是否停航\x01",
            "都丝毫不会受影响的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6818")

    label("loc_6785")


    ChrTalk(    #430
        0x11,
        (
            "我们奥维德商会有自己的经营特色，\x01",
            "食材也都是自行收集的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x11,
        (
            "不管定期船是否停航\x01",
            "都丝毫不会受影响的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x11,
        "嘿，这就是独立经营的最高境界啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_6818")

    Jump("loc_6950")

    label("loc_681B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_6873")

    ChrTalk(    #433
        0x11,
        (
            "因为定期船停航，\x01",
            "进货变得非常困难了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x11,
        (
            "哼哼，\x01",
            "这么快就轮到我出场了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6950")

    label("loc_6873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_68E7")

    ChrTalk(    #435
        0x11,
        (
            "嗯，由于那起事件，\x01",
            "店里也变得非常混乱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x11,
        (
            "呼，商业洽谈也推迟了，\x01",
            "毕竟是非常时期这也是无可奈何的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6950")

    label("loc_68E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_6950")

    ChrTalk(    #437
        0x11,
        (
            "虽然计划只要料理长有空，\x01",
            "就开始商业洽谈……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x11,
        (
            "但料理长似乎非常忙。\x01",
            "嗯嗯，不愧是一流的店。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6950")

    Jump("loc_69A7")

    label("loc_6953")


    ChrTalk(    #439
        0x11,
        (
            "不用客气。\x01",
            "请尽情享受本店的服务吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x11,
        (
            "虽然时间还早，\x01",
            "请问要不要买点什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69A7")

    TalkEnd(0x11)
    Return()

    # Function_16_4A90 end

    def Function_17_69AB(): pass

    label("Function_17_69AB")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_6A03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_69FC")

    ChrTalk(    #441
        0xFE,
        "这，这……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0xFE,
        (
            "请，请别这么说。\x01",
            "我只不过是个平常女孩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A00")

    label("loc_69FC")

    Call(0, 23)

    label("loc_6A00")

    Jump("loc_6AD3")

    label("loc_6A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_6A6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_6A68")

    ChrTalk(    #443
        0xFE,
        (
            "你说的对，都市生活\x01",
            "总觉得比较枯燥。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0xFE,
        (
            "在大自然中生活，\x01",
            "也许很不错也说不定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A6C")

    label("loc_6A68")

    Call(0, 23)

    label("loc_6A6C")

    Jump("loc_6AD3")

    label("loc_6A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_6AC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_6AC1")

    ChrTalk(    #445
        0x12,
        (
            "我好像……\x01",
            "听到了什么可怕的声音……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0x12,
        "到底出什么事了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_6AC5")

    label("loc_6AC1")

    Call(0, 23)

    label("loc_6AC5")

    Jump("loc_6AD3")

    label("loc_6AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_6AD3")
    Call(0, 23)

    label("loc_6AD3")

    TalkEnd(0x12)
    Return()

    # Function_17_69AB end

    def Function_18_6AD7(): pass

    label("Function_18_6AD7")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_6BCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 5)), scpexpr(EXPR_END)), "loc_6BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_6B40")

    ChrTalk(    #447
        0xFE,
        (
            "相亲之后\x01",
            "回帝国的老家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0xFE,
        (
            "芙拉瑟小姐真是的，\x01",
            "连休息的时间都没有呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6BC0")

    label("loc_6B40")


    ChrTalk(    #449
        0xFE,
        (
            "看来相亲\x01",
            "总算完满结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0xFE,
        (
            "但是，这结束之后\x01",
            "很快就要回帝国的老家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0xFE,
        (
            "芙拉瑟小姐真是的，\x01",
            "连休息的时间都没有呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_6BC0")

    Jump("loc_6BC7")

    label("loc_6BC3")

    Call(0, 19)

    label("loc_6BC7")

    Jump("loc_70A6")

    label("loc_6BCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_6CA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 5)), scpexpr(EXPR_END)), "loc_6C9F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_6C31")

    ChrTalk(    #452
        0xFE,
        (
            "由于时间开始空闲起来，\x01",
            "小姐似乎也变得冷静些了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0xFE,
        "嗯，算是因祸得福吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C9C")

    label("loc_6C31")


    ChrTalk(    #454
        0xFE,
        (
            "由于昨天的事，\x01",
            "相亲被迫中断了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0xFE,
        (
            "或者说……\x01",
            "今天是个好的开端。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0xFE,
        "呵呵，这可真值得期待啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_6C9C")

    Jump("loc_6CA3")

    label("loc_6C9F")

    Call(0, 19)

    label("loc_6CA3")

    Jump("loc_70A6")

    label("loc_6CA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_6D08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 5)), scpexpr(EXPR_END)), "loc_6D01")

    ChrTalk(    #457
        0xFE,
        (
            "嗯……\x01",
            "好像出什么大事了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0xFE,
        (
            "嗯，暂时\x01",
            "先留在屋子里看看情况吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D05")

    label("loc_6D01")

    Call(0, 19)

    label("loc_6D05")

    Jump("loc_70A6")

    label("loc_6D08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_70A6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6D47")

    ChrTalk(    #459
        0xFE,
        (
            "相亲\x01",
            "已经开始了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0xFE,
        "各位请静一下。\x02",
    )

    CloseMessageWindow()
    Jump("loc_70A6")

    label("loc_6D47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_6E8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_6DB9")

    ChrTalk(    #461
        0xFE,
        (
            "小姐的事，\x01",
            "就请你们多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0xFE,
        (
            "假如遇到困难的话，\x01",
            "请回忆一下传达给你的话。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E2A")

    label("loc_6DB9")


    ChrTalk(    #463
        0xFE,
        "哎呀，是你们啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0xFE,
        (
            "小姐的事，\x01",
            "就请你们多多关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xFE,
        (
            "假如遇到困难的话，\x01",
            "请回忆一下传达给你的话。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_6E2A")

    Jump("loc_6E8A")

    label("loc_6E2D")

    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #466
        0xFE,
        (
            "告辞了各位。\x01",
            "多谢关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0xFE,
        (
            "假如遇到困难的话，\x01",
            "请回忆一下传达给你的话。\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)

    label("loc_6E8A")

    Jump("loc_70A6")

    label("loc_6E8D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_6EB0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_6EA9")
    Call(1, 8)
    Jump("loc_6EAD")

    label("loc_6EA9")

    Call(1, 7)

    label("loc_6EAD")

    Jump("loc_70A6")

    label("loc_6EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 4)), scpexpr(EXPR_END)), "loc_6F40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_6EFC")

    ChrTalk(    #468
        0xFE,
        "能做的都已经做了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0xFE,
        (
            "剩下的，\x01",
            "就是和时间的战斗了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F3D")

    label("loc_6EFC")


    ChrTalk(    #470
        0xFE,
        (
            "请你想办法\x01",
            "再拖延点时间吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0xFE,
        (
            "我们已经\x01",
            "安排人去办了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_6F3D")

    Jump("loc_70A6")

    label("loc_6F40")


    ChrTalk(    #472
        0xFE,
        (
            "请您想办法\x01",
            "再拖延点时间吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0xFE,
        (
            "我们已经\x01",
            "安排人去办了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #474
        0x101,
        "#1004F（啊，这个人……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #475
        0x106,
        "#050F（……难道你认识吗？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7055")

    ChrTalk(    #476
        0x101,
        "#1002F（嗯、嗯……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0x105,
        (
            "#040F（王立学院的蕾娜。）\x02\x03",

            "（为什么……\x01",
            "  她会出现在这种地方呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70A3")

    label("loc_7055")


    ChrTalk(    #478
        0x101,
        (
            "#1015F（嗯……\x01",
            "王立学院的学生。）\x02\x03",

            "（究竟她……\x01",
            "  在这种地方做什么呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70A3")

    OP_A2(0x1A54)

    label("loc_70A6")

    TalkEnd(0x13)
    Return()

    # Function_18_6AD7 end

    def Function_19_70AA(): pass

    label("Function_19_70AA")

    TurnDirection(0xFE, 0x101, 0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #479
        0xFE,
        "啊，你是……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71A5")

    ChrTalk(    #480
        0x101,
        (
            "#1004F咦咦！？\x02\x03",

            "#1011F你好像叫蕾娜……是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0x105,
        (
            "#040F嗯，调查学院时\x01",
            "我们见过面。\x02\x03",

            "蕾娜，好久不见。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #482
        0xFE,
        "哎呀呀，连科洛丝都来了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0x101,
        (
            "#1015F那个，为什么\x01",
            "会在这种地方？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_724E")

    label("loc_71A5")


    ChrTalk(    #484
        0x101,
        (
            "#1004F咦咦！？\x02\x03",

            "#1011F你好像叫蕾娜……是吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #485
        0x107,
        "#064F姐姐的朋友？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #486
        0x101,
        (
            "#1015F嗯，学院调查的时候，\x01",
            "曾经向她打听过一些事……\x02\x03",

            "#1002F……那个，为什么\x01",
            "会在这种地方？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_724E")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #487
        0xFE,
        (
            "是。\x01",
            "我是来照顾芙拉瑟小姐的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #488
        0xFE,
        (
            "不管怎样，\x01",
            "今天是十分重要的相亲日子。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #489
        0x101,
        (
            "#1004F咦咦！？\x02\x03",

            "芙拉瑟……\x01",
            "要去相亲？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0xFE,
        (
            "是的。\x01",
            "虽然经过一番的周折……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0xFE,
        (
            "但得到了许多人的协助，\x01",
            "总算取得了成功。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_7432")

    ChrTalk(    #492
        0x101,
        (
            "#1016F可是，相亲什么的\x01",
            "是不是太、太早了点？\x02\x03",

            "她现在还只是个学生吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0xFE,
        (
            "虽说身为学生，\x01",
            "但小姐也已年满１６……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0xFE,
        (
            "作为帝国上层贵族千金，\x01",
            "连一门亲事也没有是种耻辱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0x101,
        (
            "#1008F原来是这么回事……\x02\x03",

            "#1015F嗯，这对我来说\x01",
            "非常难以理解。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74FB")

    label("loc_7432")


    ChrTalk(    #496
        0xFE,
        (
            "……对了，外面好像发生了骚乱，\x01",
            "究竟出什么事了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #497
        0x101,
        (
            "#1002F啊，嗯……\x02\x03",

            "我想虽然已经不危险了，\x01",
            "但还是不要出去比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0xFE,
        "原来如此，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0xFE,
        "大家多保重。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0x101,
        (
            "#1002F嗯……\x01",
            "蕾娜你们也多保重。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74FB")

    OP_A2(0x1A55)
    Return()

    # Function_19_70AA end

    def Function_20_74FF(): pass

    label("Function_20_74FF")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_75C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_7561")

    ChrTalk(    #501
        0xFE,
        (
            "看起来……\x01",
            "小姐也挺在意对方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0xFE,
        (
            "这之后请务必用\x01",
            "书信的形式加深交往。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75C0")

    label("loc_7561")


    ChrTalk(    #503
        0xFE,
        (
            "嗯，看来这场相亲\x01",
            "总算完满结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0xFE,
        (
            "对拉近两家的关系而言，\x01",
            "这次的相亲的确很有意义。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_75C0")

    Jump("loc_7891")

    label("loc_75C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_764C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_760F")

    ChrTalk(    #505
        0xFE,
        (
            "看来小姐对\x01",
            "对方有意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0xFE,
        "小姐，看起来就是这样的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7649")

    label("loc_760F")


    ChrTalk(    #507
        0xFE,
        (
            "看来小姐对\x01",
            "对方有意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0xFE,
        "嗯，这真是令人高兴。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_7649")

    Jump("loc_7891")

    label("loc_764C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_7697")

    ChrTalk(    #509
        0xFE,
        (
            "宛如打雷般\x01",
            "响亮的声音啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #510
        0xFE,
        "那么，外面到底发生什么了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7891")

    label("loc_7697")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_7891")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_77CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_771E")

    ChrTalk(    #511
        0xFE,
        (
            "明明非常讨厌相亲，\x01",
            "但现在又……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #512
        0xFE,
        (
            "一旦开始行动，\x01",
            "处事就变得如此伶俐……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0xFE,
        "……不，真不愧是小姐。\x02",
    )

    CloseMessageWindow()
    Jump("loc_77CA")

    label("loc_771E")


    ChrTalk(    #514
        0xFE,
        (
            "竟然将相亲进行得如此顺利，\x01",
            "但现在又……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #515
        0xFE,
        (
            "一旦开始行动，\x01",
            "处事就变得如此伶俐……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #516
        0xFE,
        (
            "这样的灵机应变，\x01",
            "正是在社交界生存必要的能力啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0xFE,
        "……呀，真不愧是小姐。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_77CA")

    Jump("loc_7891")

    label("loc_77CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_781E")

    ChrTalk(    #518
        0xFE,
        (
            "嗯……\x01",
            "小姐她现在正在补妆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0xFE,
        (
            "很快就会出来，\x01",
            "请各位稍等……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7891")

    label("loc_781E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_7841")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_783A")
    Call(1, 8)
    Jump("loc_783E")

    label("loc_783A")

    Call(1, 7)

    label("loc_783E")

    Jump("loc_7891")

    label("loc_7841")


    ChrTalk(    #520
        0xFE,
        (
            "告诉对方小姐正忙着补妆，\x01",
            "尽可能拖延时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #521
        0xFE,
        (
            "那么，那件事\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7891")

    TalkEnd(0x14)
    Return()

    # Function_20_74FF end

    def Function_21_7895(): pass

    label("Function_21_7895")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_78FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_78F5")

    ChrTalk(    #522
        0xFE,
        (
            "哪里，这样的评价\x01",
            "我觉得并不为过哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #523
        0xFE,
        (
            "和她相比，\x01",
            "我才更是不成熟呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78F9")

    label("loc_78F5")

    Call(0, 23)

    label("loc_78F9")

    Jump("loc_7AE8")

    label("loc_78FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_7976")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_796F")

    ChrTalk(    #524
        0xFE,
        (
            "繁忙的帝都生活\x01",
            "似乎不太适合我的性格。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #525
        0xFE,
        (
            "与其在人群中生活，\x01",
            "倒不如与自然为伴更为轻松自在。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7973")

    label("loc_796F")

    Call(0, 23)

    label("loc_7973")

    Jump("loc_7AE8")

    label("loc_7976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_79E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_79DB")

    ChrTalk(    #526
        0xFE,
        (
            "危机虽然已经过去了，\x01",
            "但此事绝非寻常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #527
        0x15,
        (
            "今天这场相亲\x01",
            "说不定必须早点结束呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79DF")

    label("loc_79DB")

    Call(0, 23)

    label("loc_79DF")

    Jump("loc_7AE8")

    label("loc_79E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_7AE8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_79FA")
    Call(0, 23)
    Jump("loc_7AE8")

    label("loc_79FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_7A5E")

    ChrTalk(    #528
        0xFE,
        (
            "该不会看到我穿着平时的衣服\x01",
            "对方觉得不高兴吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #529
        0xFE,
        (
            "嗯嗯嗯。\x01",
            "果然还是应该穿礼服出席。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AE8")

    label("loc_7A5E")


    ChrTalk(    #530
        0xFE,
        (
            "唔……\x01",
            "对象迟迟不出现啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #531
        0xFE,
        (
            "该不会看到我穿着平时的衣服\x01",
            "对方觉得不高兴吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #532
        0xFE,
        (
            "虽说是对方提出的，\x01",
            "但是在这种场合的确不适宜。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_7AE8")

    TalkEnd(0x15)
    Return()

    # Function_21_7895 end

    def Function_22_7AEC(): pass

    label("Function_22_7AEC")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_7C16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_7B5C")

    ChrTalk(    #533
        0xFE,
        (
            "这次的相亲，\x01",
            "看来是成功了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #534
        0xFE,
        (
            "为了加深两家的关系，\x01",
            "以后也希望你们能够持续保持友谊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C13")

    label("loc_7B5C")


    ChrTalk(    #535
        0xFE,
        (
            "起初，我还是非常担心\x01",
            "事情会发展成什么样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #536
        0xFE,
        (
            "这次的相亲，\x01",
            "看来是成功了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #537
        0xFE,
        (
            "为了加深两家的关系，\x01",
            "以后也希望你们能够持续保持友谊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #538
        0xFE,
        (
            "是否成婚\x01",
            "取决于他们个人的意愿……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_7C13")

    Jump("loc_7EF7")

    label("loc_7C16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_7C70")

    ChrTalk(    #539
        0xFE,
        (
            "少主人实在\x01",
            "太没有野心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #540
        0xFE,
        (
            "明明有着能在中央政治界大显身手\x01",
            "的家庭背景。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EF7")

    label("loc_7C70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_7D32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_7CC3")

    ChrTalk(    #541
        0xFE,
        (
            "这边的店铺\x01",
            "好像没有大碍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #542
        0xFE,
        (
            "少主人，\x01",
            "请在座位上稍等片刻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D2F")

    label("loc_7CC3")


    ChrTalk(    #543
        0xFE,
        (
            "少主人，这边的店铺\x01",
            "好像没有大碍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #544
        0xFE,
        (
            "请坐在座位上，\x01",
            "稍等片刻吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #545
        0xFE,
        (
            "等查明事情原因\x01",
            "再向您汇报。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_7D2F")

    Jump("loc_7EF7")

    label("loc_7D32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_7EF7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_7E2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_7D9B")

    ChrTalk(    #546
        0xFE,
        (
            "看来才女的称呼，\x01",
            "并非是浪得虚名啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #547
        0xFE,
        (
            "那种高雅的气质，\x01",
            "不愧出身名门。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E2B")

    label("loc_7D9B")


    ChrTalk(    #548
        0xFE,
        (
            "对面那位小姐正在王国留学，\x01",
            "据说不是一般人可以高攀的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #549
        0xFE,
        (
            "嗯，果然这称呼\x01",
            "并非是浪得虚名啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #550
        0xFE,
        (
            "那种高雅的气质，\x01",
            "不愧是出身名门啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_7E2B")

    Jump("loc_7EF7")

    label("loc_7E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_7E9C")

    ChrTalk(    #551
        0xFE,
        (
            "少主人好像过于温和了。\x01",
            "希望日后不要惧内就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #552
        0xFE,
        (
            "真的有点担心\x01",
            "他日后会不会太过依从妻子啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EF7")

    label("loc_7E9C")


    ChrTalk(    #553
        0xFE,
        (
            "少主人，这次的事\x01",
            "失败的并不是我们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #554
        0xFE,
        (
            "『请穿平时的服装』这要求\x01",
            "是对方提出来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_7EF7")

    TalkEnd(0x16)
    Return()

    # Function_22_7AEC end

    def Function_23_7EFB(): pass

    label("Function_23_7EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_8062")

    ChrTalk(    #555
        0x15,
        (
            "原来如此，那么这之后\x01",
            "是不是要回帝国的老家？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #556
        0x12,
        "是的，正是这样计划的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #557
        0x12,
        (
            "学校的假期\x01",
            "还剩下一点时间，\x01",
            "所以准备去看看父亲。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #558
        0x15,
        (
            "嗯，你果然\x01",
            "是我所期待的女性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #559
        0x15,
        (
            "一方面有着进步的思想，\x01",
            "一方面又保留着古典的道义。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #560
        0x15,
        (
            "太感谢您了，女神大人。\x01",
            "感谢你把这么优秀的女孩子介绍给我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #561
        0x12,
        "怎，怎么会……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #562
        0x12,
        (
            "请，请别这么说。\x01",
            "我只不过是个平常女孩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_846F")

    label("loc_8062")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_81E0")

    ChrTalk(    #563
        0x12,
        (
            "那个，抱歉\x01",
            "请问你从事什么样的工作？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #564
        0x15,
        (
            "平时管理从祖父那里继承下来的\x01",
            "农地和山林。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #565
        0x15,
        (
            "农闲的时候\x01",
            "看看书，打打猎，\x01",
            "可以说是自由自在的农村生活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #566
        0x15,
        (
            "繁忙的帝都生活\x01",
            "好像不太符合我的性格呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #567
        0x12,
        "乡村生活吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #568
        0x15,
        (
            "是的，听起来是很无聊，\x01",
            "习惯了的话还是很不错的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #569
        0x15,
        (
            "与其在人群中生活，\x01",
            "不如于自然为伴的话反而更轻松啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #570
        0x12,
        (
            "呵呵，原来如此。\x01",
            "或许真的是这样也说不定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_846F")

    label("loc_81E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_82B6")
    OP_4A(0x12, 255)
    OP_4A(0x15, 255)

    ChrTalk(    #571
        0x12,
        (
            "我好像……\x01",
            "听到了什么可怕的声音……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #572
        0x12,
        "到底出什么事了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #573
        0x15,
        (
            "看来不会很快有危险。\x01",
            "就在这里看看情况吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #574
        0x15,
        (
            "但是，总觉得\x01",
            "此事非同寻常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #575
        0x15,
        (
            "今天的相亲\x01",
            "可能必须提早结束也说不定。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x12, 255)
    OP_4B(0x15, 255)
    Jump("loc_846F")

    label("loc_82B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_846F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_834F")

    ChrTalk(    #576
        0x15,
        "总之先为我们两人的相遇\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #577
        0x15,
        (
            "以及彼此两家族的光荣未来，\x01",
            "以及两家的将来干杯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #578
        0x12,
        "嗯，荣幸之至。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #579
        0x12,
        (
            "不过，请允许我\x01",
            "用饮料代替酒。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_846F")

    label("loc_834F")


    ChrTalk(    #580
        0x12,
        (
            "初次见面，\x01",
            "我叫芙拉瑟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #581
        0x12,
        (
            "让您久等了，\x01",
            "真的非常抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #582
        0x12,
        (
            "因为学院布置了课题，\x01",
            "所以需要到社会上去实习。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #583
        0x15,
        (
            "啊……\x01",
            "我从心底希望和你见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #584
        0x15,
        (
            "但却一直等不到你来，\x01",
            "心里很着急……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #585
        0x15,
        (
            "不过，无论如何，\x01",
            "你不是正在我面前了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #586
        0x15,
        (
            "我也是帝国出身的男子，\x01",
            "不会太在意这些小细节。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)

    label("loc_846F")

    OP_A2(0x12)
    OP_A2(0x10)
    Return()

    # Function_23_7EFB end

    def Function_24_8476(): pass

    label("Function_24_8476")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_84E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_84DE")

    ChrTalk(    #587
        0xFE,
        (
            "果然重要的是\x01",
            "和客人间的信赖关系吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #588
        0xFE,
        (
            "仔细想想的话，\x01",
            "买卖也是人际关系啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_84E2")

    label("loc_84DE")

    Call(0, 25)

    label("loc_84E2")

    Jump("loc_86F9")

    label("loc_84E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_8614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_855A")

    ChrTalk(    #589
        0xFE,
        (
            "今天也是来向以前当商人的叔叔\x01",
            "请教一些事情的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #590
        0xFE,
        (
            "但这家店铺的门槛很高，\x01",
            "总也不好意思进去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8611")

    label("loc_855A")


    ChrTalk(    #591
        0xFE,
        (
            "昨天在这里避难时，\x01",
            "遇见过一位亲切的叔叔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #592
        0xFE,
        (
            "那个人原本也是商人，\x01",
            "向我提了很多意见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #593
        0xFE,
        (
            "他让我今天再来，\x01",
            "所以我就过来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #594
        0xFE,
        (
            "但这家店铺的门槛很高，\x01",
            "总也不好意思进去。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_8611")

    Jump("loc_86F9")

    label("loc_8614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_86F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_867E")

    ChrTalk(    #595
        0xFE,
        (
            "好不容易营业许可终于下来了，\x01",
            "但正在准备开门营业的时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #596
        0xFE,
        "唉，真是一大打击……\x02",
    )

    CloseMessageWindow()
    Jump("loc_86F9")

    label("loc_867E")


    ChrTalk(    #597
        0xFE,
        (
            "好不容易营业许可终于下来了，\x01",
            "但正在准备开门营业的时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #598
        0xFE,
        (
            "……超市居然\x01",
            "会出这种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #599
        0xFE,
        "唉，真是一大打击……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_86F9")

    TalkEnd(0x17)
    Return()

    # Function_24_8476 end

    def Function_25_86FD(): pass

    label("Function_25_86FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_8802")

    ChrTalk(    #600
        0x17,
        (
            "那个，想要吸引顾客，\x01",
            "最重要的是什么。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #601
        0x17,
        (
            "进行广告宣传的话\x01",
            "效果或许不错……\x01",
            "但是所花费的米拉也不少啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #602
        0xD,
        (
            "客人们留意的是\x01",
            "门前客人多的商店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #603
        0xD,
        (
            "满足每一位顾客的需要，\x01",
            "让他们不断回头消费……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #604
        0xD,
        "这是做买卖的基本。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #605
        0x17,
        "原，原来如此……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x15)
    OP_A2(0x6)
    Jump("loc_8923")

    label("loc_8802")


    ChrTalk(    #606
        0xD,
        (
            "那么，\x01",
            "你是想在超市里开店是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #607
        0x17,
        "是的，就在离南面出口不远处。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #608
        0x17,
        (
            "虽然现在摊位还空着，\x01",
            "但我觉得还是个不错的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #609
        0xD,
        "这倒是不错……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #610
        0xD,
        (
            "离入口近的商店\x01",
            "要在让客人驻足上下功夫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #611
        0xD,
        (
            "刚进超市的客人，脚步是很快的。\x01",
            "什么也不做的话客人们只会从店铺旁走过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #612
        0x17,
        "原，原来如此……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x16)

    label("loc_8923")

    Return()

    # Function_25_86FD end

    def Function_26_8924(): pass

    label("Function_26_8924")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_8A78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_89A6")

    ChrTalk(    #613
        0xFE,
        (
            "购物讲究的是气氛。\x01",
            "假的店铺是无法满足客人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #614
        0xFE,
        (
            "买东西不是客人们的目的，\x01",
            "购物中的乐趣才是顾客想要的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A75")

    label("loc_89A6")


    ChrTalk(    #615
        0xFE,
        (
            "超市的商人\x01",
            "虽然好像在酒店里营业……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #616
        0xFE,
        (
            "购物讲究的是气氛。\x01",
            "假的店铺是无法满足客人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #617
        0xFE,
        (
            "高高的天花板加上有感觉的展示，\x01",
            "以及平易近人的店员……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #618
        0xFE,
        (
            "这些结合在一起，\x01",
            "顾客就会从中体验到购物的乐趣。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_8A75")

    Jump("loc_8CA2")

    label("loc_8A78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_8B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_8AEB")

    ChrTalk(    #619
        0xFE,
        (
            "直到超市恢复以前\x01",
            "就在这里享受饭菜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #620
        0xFE,
        (
            "竟然那样好吃的东西啊。\x01",
            "吃好吃的东西可真放松心情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B71")

    label("loc_8AEB")


    ChrTalk(    #621
        0xFE,
        (
            "超市的恢复\x01",
            "看来还要些时日。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #622
        0xFE,
        (
            "在那之前别无选择\x01",
            "就在这里享受饭菜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #623
        0xFE,
        (
            "竟然那样好吃的东西啊。\x01",
            "吃好吃的东西可真放松心情。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_8B71")

    Jump("loc_8CA2")

    label("loc_8B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_8CA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_8C0E")

    ChrTalk(    #624
        0xFE,
        (
            "看到那个巨大的怪物，\x01",
            "一直逃到了这里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #625
        0xFE,
        (
            "但是仔细一看，\x01",
            "这里不是安特洛丝吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #626
        0xFE,
        (
            "嗯，不愧是我啊。\x01",
            "身体会自然向着一流的方面前进。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CA2")

    label("loc_8C0E")


    ChrTalk(    #627
        0xFE,
        (
            "正在想怎么突然刮起了大风，\x01",
            "突然周围就一下变得漆黑一片，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #628
        0xFE,
        (
            "紧接着超市上\x01",
            "就有个巨大的怪物站在那里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #629
        0xFE,
        (
            "我来不及思考，\x01",
            "就一直逃到了这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_8CA2")

    TalkEnd(0x18)
    Return()

    # Function_26_8924 end

    def Function_27_8CA6(): pass

    label("Function_27_8CA6")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_8DCB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_END)), "loc_8D18")

    ChrTalk(    #630
        0xFE,
        (
            "的确……\x01",
            "感觉和上次来时不太一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #631
        0xFE,
        (
            "今天觉得不可思议啊……\x01",
            "居然能挺起胸膛地坐在这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DC8")

    label("loc_8D18")


    ChrTalk(    #632
        0xFE,
        (
            "作为参加超市修复工程的答谢\x01",
            "市长亲自招待了我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #633
        0xFE,
        (
            "或许是由于这个原因，这次的感觉\x01",
            "和上次来的时候有些不一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #634
        0xFE,
        (
            "我自己也感到有些不可思议，\x01",
            "居然能挺起胸膛地坐在这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x18)

    label("loc_8DC8")

    Jump("loc_8DD2")

    label("loc_8DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_8DD2")

    label("loc_8DD2")

    TalkEnd(0x19)
    Return()

    # Function_27_8CA6 end

    def Function_28_8DD6(): pass

    label("Function_28_8DD6")

    TalkBegin(0x1A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_8EAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_8E38")

    ChrTalk(    #635
        0xFE,
        (
            "嗯，这里的料理\x01",
            "果然是最棒的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #636
        0xFE,
        (
            "一想到是市长款待的，\x01",
            "就更觉得美味了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EAC")

    label("loc_8E38")


    ChrTalk(    #637
        0xFE,
        (
            "这里的料理\x01",
            "果然最棒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #638
        0xFE,
        (
            "一想到是市长款待的，\x01",
            "就更觉得美味了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #639
        0xFE,
        (
            "嗯，呵呵……\x01",
            "为工程尽力果然是对的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x19)

    label("loc_8EAC")

    Jump("loc_8EB6")

    label("loc_8EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_8EB6")

    label("loc_8EB6")

    TalkEnd(0x1A)
    Return()

    # Function_28_8DD6 end

    def Function_29_8EBA(): pass

    label("Function_29_8EBA")

    Call(0, 30)
    Return()

    # Function_29_8EBA end

    def Function_30_8EBF(): pass

    label("Function_30_8EBF")

    TalkBegin(0x1B)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",                                # 0
            "买东西\x01",                              # 1
            "招牌菜『黄金调味饭』　1400米拉\x01",      # 2
            "离开\x01",                                # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F3F")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x34)
    OP_56(0x0)
    TalkEnd(0x1B)
    Return()

    label("loc_8F3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9079")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x578), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9041")
    SubMira(1400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #640
        "\x06\x07\x02黄金调味饭\x07\x00已经品尝过了。\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFC, 0x0)
    OP_31(0x1, 0xFC, 0x0)
    OP_31(0x2, 0xFC, 0x0)
    OP_31(0x3, 0xFC, 0x0)
    OP_31(0x4, 0xFC, 0x0)
    OP_31(0x5, 0xFC, 0x0)
    OP_31(0x6, 0xFC, 0x0)
    OP_31(0x7, 0xFC, 0x0)
    OP_31(0x8, 0xFC, 0x0)
    OP_31(0x0, 0xFD, 0xDAC)
    OP_31(0x1, 0xFD, 0xDAC)
    OP_31(0x2, 0xFD, 0xDAC)
    OP_31(0x3, 0xFD, 0xDAC)
    OP_31(0x4, 0xFD, 0xDAC)
    OP_31(0x5, 0xFD, 0xDAC)
    OP_31(0x6, 0xFD, 0xDAC)
    OP_31(0x7, 0xFD, 0xDAC)
    OP_31(0x8, 0xFD, 0xDAC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9033")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x5)"), scpexpr(EXPR_END)), "loc_9009")
    Jump("loc_9033")

    label("loc_9009")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #641
        "\x06\x07\x02黄金调味饭\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()

    label("loc_9033")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_9067")

    label("loc_9041")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #642
        "没有足够的米拉。\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_9067")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x1B)
    Return()

    label("loc_9079")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9093")
    FadeToBright(300, 0)
    TalkEnd(0x1B)
    Return()

    label("loc_9093")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_9191")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9132")

    ChrTalk(    #643
        0x1B,
        (
            "虽然工房的人也说修了，\x01",
            "可是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #644
        0x1B,
        (
            "总之，\x01",
            "只要炉子能用就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #645
        0x1B,
        (
            "假如没有导力器那强劲的火候\x01",
            "我们店的味道是出不来的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)
    Jump("loc_918E")

    label("loc_9132")


    ChrTalk(    #646
        0x1B,
        (
            "总之，\x01",
            "只要炉子能用就好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #647
        0x1B,
        (
            "假如没有导力器那强劲的火候\x01",
            "我们店的味道是出不来的啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_918E")

    Jump("loc_96D1")

    label("loc_9191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_9252")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9206")

    ChrTalk(    #648
        0x1B,
        (
            "虽然用不了导力器很为难，\x01",
            "但因此引发骚乱就不好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #649
        0x1B,
        (
            "同身为柏斯市民的我们\x01",
            "都感觉丢脸啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)
    Jump("loc_924F")

    label("loc_9206")


    ChrTalk(    #650
        0x1B,
        (
            "动摇的心情我能理解，\x01",
            "但爆发骚乱可就不好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #651
        0x1B,
        "都感觉太丢脸了啊。\x02",
    )

    CloseMessageWindow()

    label("loc_924F")

    Jump("loc_96D1")

    label("loc_9252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_929F")

    ChrTalk(    #652
        0x1B,
        (
            "呀——\x01",
            "超市能够顺利修复可真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #653
        0x1B,
        "是啊，真是太好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_96D1")

    label("loc_929F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_93DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_933A")

    ChrTalk(    #654
        0x1B,
        (
            "自从那家蛋糕店开门以来\x01",
            "我们的销量就一直下滑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #655
        0x1B,
        (
            "话虽如此，事到如今\x01",
            "想让他们走又是不可能的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #656
        0x1B,
        "……米拉和人情真是两难的取舍啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_93D7")

    label("loc_933A")


    ChrTalk(    #657
        0x1B,
        "嗯、嗯，糟糕了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #658
        0x1B,
        (
            "自从那家蛋糕店开门以来\x01",
            "销量越来越低。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #659
        0x1B,
        (
            "话虽如此，事到如今\x01",
            "想让他们走又是不可能的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #660
        0x1B,
        "生，生意真是到了最困窘的境地啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_93D7")

    Jump("loc_96D1")

    label("loc_93DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_94BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_9439")

    ChrTalk(    #661
        0x1B,
        (
            "那家蛋糕店\x01",
            "人气实在是太旺了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #662
        0x1B,
        (
            "因此我们这里的料理\x01",
            "几乎没有人来点了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94B7")

    label("loc_9439")


    ChrTalk(    #663
        0x1B,
        (
            "不～～～那家蛋糕店\x01",
            "人气实在是太旺了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #664
        0x1B,
        (
            "因此我们这里的料理\x01",
            "完全没有人来点了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #665
        0x1B,
        (
            "哈，哈哈……\x01",
            "这也算是帮助人吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_94B7")

    Jump("loc_96D1")

    label("loc_94BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_961E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_9564")

    ChrTalk(    #666
        0x1B,
        (
            "我们这里也有冰淇淋和蛋糕铺子\x01",
            "的人前来避难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #667
        0x1B,
        (
            "生意好像还要继续，\x01",
            "不嫌弃的话买一点回去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #668
        0x1B,
        (
            "买卖是很复杂的，\x01",
            "遇到困难的时候大家都是差不多的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_961B")

    label("loc_9564")


    ChrTalk(    #669
        0x1B,
        (
            "毕竟发生的是\x01",
            "超市倒塌这样的大事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #670
        0x1B,
        (
            "我们也想帮忙，\x01",
            "于是就报名承当起了避难所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #671
        0x1B,
        (
            "因此，开冰淇淋和蛋糕铺子\x01",
            "的人就来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #672
        0x1B,
        (
            "生意好像还要继续，\x01",
            "不嫌弃的话买一点回去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_961B")

    Jump("loc_96D1")

    label("loc_961E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_96D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_9662")

    ChrTalk(    #673
        0x1B,
        (
            "我店可是面向工薪阶层的平价店。\x01",
            "请慢慢享用吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96D1")

    label("loc_9662")


    ChrTalk(    #674
        0x1B,
        (
            "欢迎光临。\x01",
            "我店可是面向工薪阶层的平价店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #675
        0x1B,
        (
            "和安特洛丝不同，\x01",
            "为顾客提供像家一样的气氛是我们的卖点。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_96D1")

    TalkEnd(0x1B)
    Return()

    # Function_30_8EBF end

    def Function_31_96D5(): pass

    label("Function_31_96D5")

    TalkBegin(0x1C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_977E")

    ChrTalk(    #676
        0xFE,
        (
            "我们老板\x01",
            "只会使用导力炉做饭。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #677
        0xFE,
        (
            "但是，最近使用的是直接在火上烹调的方法，\x01",
            "因此不管什么料理闻起来都有股焦味儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #678
        0xFE,
        "这已经不是料理好不好吃的问题了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D6A")

    label("loc_977E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_988F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9826")

    ChrTalk(    #679
        0xFE,
        (
            "虽然听老板的口气，\x01",
            "好像对骚乱满不在乎……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #680
        0xFE,
        (
            "可是老板自己\x01",
            "还不是冲进市长官邸去抗议了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #681
        0xFE,
        (
            "把自己的事当作没发生过，\x01",
            "有什么好装模作样的……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1B)
    Jump("loc_988C")

    label("loc_9826")


    ChrTalk(    #682
        0xFE,
        (
            "老板嘴上虽这么说，\x01",
            "自己还不是冲进市长官邸去抗议了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #683
        0xFE,
        (
            "这样……\x01",
            "所说的跟所做的不是截然相反吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_988C")

    Jump("loc_9D6A")

    label("loc_988F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_99B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_9918")

    ChrTalk(    #684
        0xFE,
        (
            "本店正处在危机当中啊。\x01",
            "客人都被前来避难的那个蛋糕店老板抢走了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #685
        0xFE,
        (
            "要是超市再不开门话，\x01",
            "我想肯定会被吞并的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99B3")

    label("loc_9918")


    ChrTalk(    #686
        0xFE,
        (
            "呵呵，超市能够顺利恢复\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #687
        0xFE,
        (
            "要是超市再不开门话，\x01",
            "我们肯定被蛋糕店老板\x01",
            "完全吞并了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #688
        0xFE,
        (
            "不过，被并掉生意反而会更好些，\x01",
            "好像也不错。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1B)

    label("loc_99B3")

    Jump("loc_9D6A")

    label("loc_99B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_9AD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_9A21")

    ChrTalk(    #689
        0xFE,
        (
            "最近，我们这儿\x01",
            "几乎快成『蛋糕酒馆』了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #690
        0xFE,
        (
            "大家都是来吃蛋糕的，\x01",
            "再也没有人点菜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AD1")

    label("loc_9A21")


    ChrTalk(    #691
        0xFE,
        (
            "最近，我们这儿\x01",
            "几乎快成『蛋糕酒馆』了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #692
        0xFE,
        (
            "大家都是来吃蛋糕的，\x01",
            "再也没有人点菜了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #693
        0xFE,
        "不过，这样的结果是必然的吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #694
        0xFE,
        (
            "我们这儿的料理，\x01",
            "只有价格便宜是唯一的长处。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1B)

    label("loc_9AD1")

    Jump("loc_9D6A")

    label("loc_9AD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_9C40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_9B38")

    ChrTalk(    #695
        0xFE,
        (
            "来我们这里避难的蛋糕店老板。\x01",
            "跟我想的一样非常受欢迎啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #696
        0xFE,
        "客人都被抢走了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9C3D")

    label("loc_9B38")


    ChrTalk(    #697
        0xFE,
        (
            "来我们这里避难的蛋糕店老板。\x01",
            "跟我想的一样非常受欢迎啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #698
        0xFE,
        (
            "工地上班的工人，\x01",
            "休息的时候也会来买的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #699
        0xFE,
        (
            "店长最初的时候还洋洋得意，\x01",
            "但最近可没那么自在了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #700
        0xFE,
        (
            "本来就不是很有人气的店铺，又想装门面，\x01",
            "就是这样的结果啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #701
        0xFE,
        "……总之这就是叫自做自受吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1B)

    label("loc_9C3D")

    Jump("loc_9D6A")

    label("loc_9C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_9D44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_9CB1")

    ChrTalk(    #702
        0xFE,
        (
            "让人家在店铺里营业，\x01",
            "是不是太大方了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #703
        0xFE,
        (
            "老板的料理和人家一比，\x01",
            "我想会马上就败下阵来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D41")

    label("loc_9CB1")


    ChrTalk(    #704
        0xFE,
        (
            "虽然收留前来超市避难的人\x01",
            "是理所当然的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #705
        0xFE,
        (
            "但让人家在店铺里营业，\x01",
            "是不是太大方了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #706
        0xFE,
        (
            "难道打算让原本就低迷的销售额\x01",
            "下降到零吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1B)

    label("loc_9D41")

    Jump("loc_9D6A")

    label("loc_9D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_9D6A")

    ChrTalk(    #707
        0xFE,
        (
            "欢迎光临！\x01",
            "请空位上就坐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D6A")

    TalkEnd(0x1C)
    Return()

    # Function_31_96D5 end

    def Function_32_9D6E(): pass

    label("Function_32_9D6E")

    TalkBegin(0x1D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_9E29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_END)), "loc_9DC6")

    ChrTalk(    #708
        0xFE,
        (
            "我在找的东西\x01",
            "肯定在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #709
        0xFE,
        (
            "一定要将研究完成，\x01",
            "得到荣誉！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E29")

    label("loc_9DC6")


    ChrTalk(    #710
        0xFE,
        (
            "呼呼呼……\x01",
            "我是古代生物的研究者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #711
        0xFE,
        (
            "我在找的东西\x01",
            "肯定在这里……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #712
        0xFE,
        "哼哼，好好期待吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C)

    label("loc_9E29")

    TalkEnd(0x1D)
    Return()

    # Function_32_9D6E end

    def Function_33_9E2D(): pass

    label("Function_33_9E2D")

    TalkBegin(0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_9F4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_END)), "loc_9E97")

    ChrTalk(    #713
        0xFE,
        (
            "和喜欢的人一起工作，\x01",
            "果然是件快乐的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #714
        0xFE,
        (
            "现在，\x01",
            "真想稍微享受一下这种感觉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F48")

    label("loc_9E97")


    ChrTalk(    #715
        0xFE,
        (
            "在这之前，\x01",
            "和他在不同的店铺里工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #716
        0xFE,
        (
            "和喜欢的人一起工作，\x01",
            "果然是件开心的事⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #717
        0xFE,
        (
            "真想稍微体验一下\x01",
            "这种感觉啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #718
        0xFE,
        (
            "如果超市恢复的话，\x01",
            "我们就又是竞争对手了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)

    label("loc_9F48")

    Jump("loc_A07B")

    label("loc_9F4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_A022")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_END)), "loc_9FB2")

    ChrTalk(    #719
        0xFE,
        (
            "经过了一个晚上，\x01",
            "终于冷静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #720
        0xFE,
        (
            "现在只有和他同心协力，\x01",
            "一起努力往前走了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A01F")

    label("loc_9FB2")


    ChrTalk(    #721
        0xFE,
        "啊，欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #722
        0xFE,
        (
            "经过了一个晚上，\x01",
            "终于冷静下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #723
        0xFE,
        (
            "现在只有和他同心协力，\x01",
            "一起努力往前走了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)

    label("loc_A01F")

    Jump("loc_A07B")

    label("loc_A022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_A07B")

    ChrTalk(    #724
        0xFE,
        (
            "好像掉了一大堆瓦片什么的\x01",
            "在我的货车后面……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #725
        0xFE,
        (
            "嗯……\x01",
            "在那边的人没事吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A07B")

    TalkEnd(0x1E)
    Return()

    # Function_33_9E2D end

    def Function_34_A07F(): pass

    label("Function_34_A07F")

    TalkBegin(0x1F)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0E0")
    OP_0D()
    OP_A9(0x51)
    OP_56(0x0)
    TalkEnd(0x1F)
    Return()

    label("loc_A0E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A0F1")
    TalkEnd(0x1F)
    Return()

    label("loc_A0F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_A208")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 6)), scpexpr(EXPR_END)), "loc_A15C")

    ChrTalk(    #726
        0xFE,
        (
            "两人合作的话\x01",
            "似乎能开发出不错的商品啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #727
        0xFE,
        (
            "超市假如恢复的话\x01",
            "要试试开发新的商品吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A205")

    label("loc_A15C")


    ChrTalk(    #728
        0xFE,
        (
            "虽然真的好久没和卡特丽亚\x01",
            "一起工作了，\x01",
            "但因此会有很多新发现也挺有趣的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #729
        0xFE,
        (
            "两人合作的话\x01",
            "似乎能开发出不错的商品啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #730
        0xFE,
        (
            "超市假如恢复的话\x01",
            "要试试开发新的商品吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E)

    label("loc_A205")

    Jump("loc_A4B9")

    label("loc_A208")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_A369")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 6)), scpexpr(EXPR_END)), "loc_A285")

    ChrTalk(    #731
        0xFE,
        (
            "修复工程虽然开始了，\x01",
            "但恐怕要过很久才能恢复营业吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #732
        0xFE,
        (
            "总之现在要继续经营生意，\x01",
            "不能把客人置之不理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A366")

    label("loc_A285")


    ChrTalk(    #733
        0xFE,
        (
            "修复工程虽然开始了，\x01",
            "但恐怕要过很久才能恢复营业吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #734
        0xFE,
        (
            "总之现在要继续经营生意，\x01",
            "不能把客人置之不理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #735
        0xFE,
        (
            "不过，也许是因为换了地方吧，\x01",
            "客人果然不太多呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #736
        0xFE,
        (
            "刚才卡特丽亚还在担心呢，\x01",
            "每天都来的男性客人没有再来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E)

    label("loc_A366")

    Jump("loc_A4B9")

    label("loc_A369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_A4B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 6)), scpexpr(EXPR_END)), "loc_A3F7")

    ChrTalk(    #737
        0xFE,
        (
            "这可不是小事情……\x01",
            "就连卡特丽亚也深受打击啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #738
        0xFE,
        (
            "这样的话，正是轮到\x01",
            "身为未婚夫的我要支持她才行啊。\x01",
            "嗯，要支持她才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4B9")

    label("loc_A3F7")


    ChrTalk(    #739
        0xFE,
        (
            "虽然事态变得很严重，\x01",
            "但即使是为了未婚妻卡特丽亚，\x01",
            "我也会坚持下去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #740
        0xFE,
        (
            "以前，\x01",
            "我有很长一段时间不在店里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #741
        0xFE,
        (
            "那个时候她靠一个人的力量\x01",
            "保住了店铺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #742
        0xFE,
        (
            "所以这次……\x01",
            "轮到我支持她了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E)

    label("loc_A4B9")

    TalkEnd(0x1F)
    Return()

    # Function_34_A07F end

    def Function_35_A4BD(): pass

    label("Function_35_A4BD")

    TalkBegin(0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_A534")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_A51B")

    ChrTalk(    #743
        0x20,
        (
            "各位……\x01",
            "那就麻烦你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #744
        0x20,
        (
            "如果发现了什么，\x01",
            "请再来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A531")

    label("loc_A51B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_A52D")
    Call(1, 4)
    Jump("loc_A531")

    label("loc_A52D")

    Call(1, 3)

    label("loc_A531")

    Jump("loc_A581")

    label("loc_A534")


    ChrTalk(    #745
        0x20,
        "哈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #746
        0x20,
        "外国之地果然叫人不放心啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #747
        0x20,
        (
            "那个孩子\x01",
            "一定吃了不少苦……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A581")

    TalkEnd(0x20)
    Return()

    # Function_35_A4BD end

    def Function_36_A585(): pass

    label("Function_36_A585")

    Return()

    # Function_36_A585 end

    def Function_37_A586(): pass

    label("Function_37_A586")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_A666")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A638")

    ChrTalk(    #748
        0xFE,
        "哼哼哼，啦啦啦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #749
        0xFE,
        "………………咕咚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #750
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #751
        0xFE,
        (
            "可能是我的错觉……\x01",
            "总觉得有股焦味儿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #752
        0xFE,
        (
            "……也罢，\x01",
            "反正吃下去都一样。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20)
    Jump("loc_A663")

    label("loc_A638")


    ChrTalk(    #753
        0xFE,
        (
            "哼哼哼，啦啦啦……\x01",
            "………………咕咚。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A663")

    Jump("loc_A77D")

    label("loc_A666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A77D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A717")

    ChrTalk(    #754
        0xFE,
        (
            "啊，诸位是……\x01",
            "游击士吧～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #755
        0xFE,
        (
            "在我们的『赛希莉亚号』上\x01",
            "见过很多次呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #756
        0xFE,
        (
            "那个，\x01",
            "很不巧船停开了～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #757
        0xFE,
        (
            "看来一时半会儿还出不了港，\x01",
            "所以就先来吃个饭。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20)
    Jump("loc_A77D")

    label("loc_A717")


    ChrTalk(    #758
        0xFE,
        "那么，来吃点什么呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #759
        0xFE,
        (
            "店里推荐的价格都很贵，\x01",
            "我可不吃。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #760
        0xFE,
        (
            "毕竟……\x01",
            "那不是一个人能吃完的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A77D")

    TalkEnd(0x22)
    Return()

    # Function_37_A586 end

    def Function_38_A781(): pass

    label("Function_38_A781")

    TalkBegin(0x25)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_A78E")
    Jump("loc_A895")

    label("loc_A78E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_END)), "loc_A798")
    Jump("loc_A895")

    label("loc_A798")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_A895")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 1)), scpexpr(EXPR_END)), "loc_A801")

    ChrTalk(    #761
        0xFE,
        (
            "蛋糕店的姐姐\x01",
            "是和未婚夫一起经营店铺的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #762
        0xFE,
        (
            "虽说早知会有今天，\x01",
            "但还是挺受打击的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A895")

    label("loc_A801")


    ChrTalk(    #763
        0xFE,
        (
            "我是听说\x01",
            "蛋糕店姐姐在酒馆避难才来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #764
        0xFE,
        (
            "进去里面一看，姐姐她原来\x01",
            "是和未婚夫一起经营店铺的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #765
        0xFE,
        (
            "虽说早知会有今天，\x01",
            "但还是挺受打击的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x21)

    label("loc_A895")

    TalkEnd(0x25)
    Return()

    # Function_38_A781 end

    SaveToFile()

Try(main)
