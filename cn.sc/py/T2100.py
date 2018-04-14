from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2100   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2100   ._SN',
            'ED6_DT21/T2100_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '奈尔',                                 # 9
        '朵洛希',                               # 10
        '诺曼候选人',                           # 11
        '德尔斯',                               # 12
        '海利欧',                               # 13
        '波尔多斯候选人',                       # 14
        '昆茨',                                 # 15
        '布诺安',                               # 16
        '围观者',                               # 17
        '围观者',                               # 18
        '围观者',                               # 19
        '围观者',                               # 20
        '围观者',                               # 21
        '围观者',                               # 22
        '围观者',                               # 23
        '围观者',                               # 24
        '围观者',                               # 25
        '围观者',                               # 26
        '围观者',                               # 27
        '围观者',                               # 28
        '围观者',                               # 29
        '围观者',                               # 30
        '围观者',                               # 31
        '围观者',                               # 32
        '围观者',                               # 33
        '围观者',                               # 34
        '围观者',                               # 35
        '中年男子',                             # 36
        '哈尔德',                               # 37
        '罗伊德',                               # 38
        '罗伊德',                               # 39
        '塞尔玛',                               # 40
        '玛奇尔达',                             # 41
        '菲利奥',                               # 42
        '拉科舒',                               # 43
        '昆茨',                                 # 44
        '利顿',                                 # 45
        '穆拉德老人',                           # 46
        '鲁蓓',                                 # 47
        '阿杰',                                 # 48
        '海利欧',                               # 49
        '修女芙丽达',                           # 50
        '森特',                                 # 51
        '船',                                   # 52
        '目标用照相机',                         # 53
        '连茨',                                 # 54
        '阿伦特',                               # 55
        '爱蕾塔',                               # 56
        '迪恩',                                 # 57
        '雷斯',                                 # 58
        '洛克',                                 # 59
        '布鲁托',                               # 60
        '梅威海道方向',                         # 61
        '卢安市·南街区',                       # 62
        '卢安飞船坪',                           # 63
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
        'ED6_DT07/CH02060 ._CH',             # 00
        'ED6_DT07/CH02070 ._CH',             # 01
        'ED6_DT07/CH01200 ._CH',             # 02
        'ED6_DT07/CH01040 ._CH',             # 03
        'ED6_DT07/CH01220 ._CH',             # 04
        'ED6_DT07/CH01680 ._CH',             # 05
        'ED6_DT07/CH01460 ._CH',             # 06
        'ED6_DT07/CH01500 ._CH',             # 07
        'ED6_DT07/CH01020 ._CH',             # 08
        'ED6_DT07/CH01030 ._CH',             # 09
        'ED6_DT07/CH01050 ._CH',             # 0A
        'ED6_DT07/CH01070 ._CH',             # 0B
        'ED6_DT07/CH01100 ._CH',             # 0C
        'ED6_DT07/CH01120 ._CH',             # 0D
        'ED6_DT07/CH01140 ._CH',             # 0E
        'ED6_DT07/CH01150 ._CH',             # 0F
        'ED6_DT07/CH01210 ._CH',             # 10
        'ED6_DT07/CH01130 ._CH',             # 11
        'ED6_DT07/CH01250 ._CH',             # 12
        'ED6_DT06/CH20092 ._CH',             # 13
        'ED6_DT07/CH01090 ._CH',             # 14
        'ED6_DT07/CH01153 ._CH',             # 15
        'ED6_DT07/CH01170 ._CH',             # 16
        'ED6_DT07/CH01000 ._CH',             # 17
        'ED6_DT07/CH01410 ._CH',             # 18
        'ED6_DT06/CH20063 ._CH',             # 19
        'ED6_DT06/CH20064 ._CH',             # 1A
        'ED6_DT06/CH20045 ._CH',             # 1B
        'ED6_DT06/CH20039 ._CH',             # 1C
        'ED6_DT07/CH01663 ._CH',             # 1D
        'ED6_DT07/CH01290 ._CH',             # 1E
        'ED6_DT07/CH02510 ._CH',             # 1F
        'ED6_DT07/CH02520 ._CH',             # 20
        'ED6_DT07/CH02530 ._CH',             # 21
        'ED6_DT07/CH01390 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT07/CH02060P._CP',             # 00
        'ED6_DT07/CH02070P._CP',             # 01
        'ED6_DT07/CH01200P._CP',             # 02
        'ED6_DT07/CH01040P._CP',             # 03
        'ED6_DT07/CH01220P._CP',             # 04
        'ED6_DT07/CH01680P._CP',             # 05
        'ED6_DT07/CH01460P._CP',             # 06
        'ED6_DT07/CH01500P._CP',             # 07
        'ED6_DT07/CH01020P._CP',             # 08
        'ED6_DT07/CH01030P._CP',             # 09
        'ED6_DT07/CH01050P._CP',             # 0A
        'ED6_DT07/CH01070P._CP',             # 0B
        'ED6_DT07/CH01100P._CP',             # 0C
        'ED6_DT07/CH01120P._CP',             # 0D
        'ED6_DT07/CH01140P._CP',             # 0E
        'ED6_DT07/CH01150P._CP',             # 0F
        'ED6_DT07/CH01210P._CP',             # 10
        'ED6_DT07/CH01130P._CP',             # 11
        'ED6_DT07/CH01250P._CP',             # 12
        'ED6_DT06/CH20092P._CP',             # 13
        'ED6_DT07/CH01090P._CP',             # 14
        'ED6_DT07/CH01153P._CP',             # 15
        'ED6_DT07/CH01170P._CP',             # 16
        'ED6_DT07/CH01000P._CP',             # 17
        'ED6_DT07/CH01410P._CP',             # 18
        'ED6_DT06/CH20063P._CP',             # 19
        'ED6_DT06/CH20064P._CP',             # 1A
        'ED6_DT06/CH20045P._CP',             # 1B
        'ED6_DT06/CH20039P._CP',             # 1C
        'ED6_DT07/CH01663P._CP',             # 1D
        'ED6_DT07/CH01290P._CP',             # 1E
        'ED6_DT07/CH02510P._CP',             # 1F
        'ED6_DT07/CH02520P._CP',             # 20
        'ED6_DT07/CH02530P._CP',             # 21
        'ED6_DT07/CH01390P._CP',             # 22
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 70990,
        Z                   = 1050,
        Y                   = 79010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 22310,
        Z                   = 0,
        Y                   = 76950,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 29307,
        Z                   = -1800,
        Y                   = 68254,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 21840,
        Z                   = 0,
        Y                   = 70280,
        Direction           = 60,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 23580,
        Z                   = 2160,
        Y                   = 102820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x154,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 46320,
        Z                   = 0,
        Y                   = 79740,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 47990,
        Z                   = 0,
        Y                   = 80530,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 46730,
        Z                   = 0,
        Y                   = 78510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 28500,
        Z                   = 0,
        Y                   = 82470,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 990,
        Z                   = -2250,
        Y                   = 94250,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 26280,
        Z                   = 0,
        Y                   = 88370,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 24400,
        Z                   = 0,
        Y                   = 93520,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 54940,
        Z                   = 0,
        Y                   = 78510,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 67840,
        Z                   = 500,
        Y                   = 93830,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39560,
        Z                   = -1770,
        Y                   = 69520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xA4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 52980,
        Z                   = 0,
        Y                   = 95770,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 43460,
        Z                   = 3500,
        Y                   = 72520,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 29170,
        Z                   = 0,
        Y                   = 89110,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 51800,
        Z                   = 0,
        Y                   = 71000,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 50200,
        Z                   = 0,
        Y                   = 71000,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 51000,
        Z                   = 0,
        Y                   = 72300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 93780,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 25260,
        Z                   = 0,
        Y                   = 128199,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 51060,
        Z                   = 400,
        Y                   = 27190,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 81750,
        Z                   = 0,
        Y                   = 80640,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 20100,
        Y                   = -2000,
        Z                   = 118500,
        Range               = 28900,
        Unknown_10          = 0x708,
        Unknown_14          = 0x1D524,
        Unknown_18          = 0x0,
        Unknown_1C          = 41,
    )

    DeclEvent(
        X                   = 48500,
        Y                   = -2000,
        Z                   = 68000,
        Range               = 53500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x11170,
        Unknown_18          = 0x0,
        Unknown_1C          = 32,
    )

    DeclEvent(
        X                   = 67740,
        Y                   = 0,
        Z                   = 84010,
        Range               = 66350,
        Unknown_10          = 0x708,
        Unknown_14          = 0x130B0,
        Unknown_18          = 0x0,
        Unknown_1C          = 42,
    )

    DeclEvent(
        X                   = 46730,
        Y                   = -1000,
        Z                   = 78510,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = 28500,
        Y                   = -1000,
        Z                   = 82470,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 54940,
        Y                   = -1000,
        Z                   = 78510,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 50950,
        Y                   = -1000,
        Z                   = 75000,
        Range               = 3000,
        Unknown_10          = 0x1388,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = 44990,
        Y                   = 0,
        Z                   = 89330,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 57,
    )

    DeclEvent(
        X                   = 38080,
        Y                   = 0,
        Z                   = 78540,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 58,
    )

    DeclEvent(
        X                   = 37930,
        Y                   = 0,
        Z                   = 89380,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 59,
    )

    DeclEvent(
        X                   = 30610,
        Y                   = 0,
        Z                   = 96060,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 59,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 108200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 60,
    )

    DeclEvent(
        X                   = 20930,
        Y                   = -1500,
        Z                   = 93960,
        Range               = 3500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 61,
    )

    DeclEvent(
        X                   = 61000,
        Y                   = 0,
        Z                   = 78900,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 62,
    )

    DeclEvent(
        X                   = 66890,
        Y                   = -500,
        Z                   = 93800,
        Range               = 2200,
        Unknown_10          = 0x898,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 63,
    )

    DeclEvent(
        X                   = 73630,
        Y                   = 0,
        Z                   = 80790,
        Range               = 3500,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 64,
    )


    DeclActor(
        TriggerX            = 23750,
        TriggerZ            = 1000,
        TriggerY            = 102860,
        TriggerRange        = 1000,
        ActorX              = 23580,
        ActorZ              = 4000,
        ActorY              = 102820,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 26630,
        TriggerZ            = 0,
        TriggerY            = 86030,
        TriggerRange        = 800,
        ActorX              = 26330,
        ActorZ              = 1000,
        ActorY              = 86030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 55,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 16250,
        TriggerZ            = -1800,
        TriggerY            = 112100,
        TriggerRange        = 1000,
        ActorX              = 13840,
        ActorZ              = -2500,
        ActorY              = 112130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 56,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_B0E",          # 00, 0
        "Function_1_E18",          # 01, 1
        "Function_2_E8B",          # 02, 2
        "Function_3_1008",         # 03, 3
        "Function_4_102C",         # 04, 4
        "Function_5_1050",         # 05, 5
        "Function_6_108C",         # 06, 6
        "Function_7_130C",         # 07, 7
        "Function_8_149B",         # 08, 8
        "Function_9_16F8",         # 09, 9
        "Function_10_19A9",        # 0A, 10
        "Function_11_1DEB",        # 0B, 11
        "Function_12_239C",        # 0C, 12
        "Function_13_2416",        # 0D, 13
        "Function_14_2496",        # 0E, 14
        "Function_15_254F",        # 0F, 15
        "Function_16_2871",        # 10, 16
        "Function_17_2921",        # 11, 17
        "Function_18_29B7",        # 12, 18
        "Function_19_29BC",        # 13, 19
        "Function_20_2ED9",        # 14, 20
        "Function_21_2F99",        # 15, 21
        "Function_22_300F",        # 16, 22
        "Function_23_334F",        # 17, 23
        "Function_24_343E",        # 18, 24
        "Function_25_3580",        # 19, 25
        "Function_26_3604",        # 1A, 26
        "Function_27_37C5",        # 1B, 27
        "Function_28_382D",        # 1C, 28
        "Function_29_3979",        # 1D, 29
        "Function_30_45A2",        # 1E, 30
        "Function_31_4EC9",        # 1F, 31
        "Function_32_529A",        # 20, 32
        "Function_33_7027",        # 21, 33
        "Function_34_713D",        # 22, 34
        "Function_35_7159",        # 23, 35
        "Function_36_717A",        # 24, 36
        "Function_37_7828",        # 25, 37
        "Function_38_7844",        # 26, 38
        "Function_39_7879",        # 27, 39
        "Function_40_78AE",        # 28, 40
        "Function_41_78CD",        # 29, 41
        "Function_42_7BEA",        # 2A, 42
        "Function_43_7C7C",        # 2B, 43
        "Function_44_8200",        # 2C, 44
        "Function_45_83C3",        # 2D, 45
        "Function_46_83D8",        # 2E, 46
        "Function_47_8401",        # 2F, 47
        "Function_48_842A",        # 30, 48
        "Function_49_8453",        # 31, 49
        "Function_50_857D",        # 32, 50
        "Function_51_9507",        # 33, 51
        "Function_52_9E52",        # 34, 52
        "Function_53_A4B0",        # 35, 53
        "Function_54_A549",        # 36, 54
        "Function_55_A5A2",        # 37, 55
        "Function_56_A61C",        # 38, 56
        "Function_57_A707",        # 39, 57
        "Function_58_A70B",        # 3A, 58
        "Function_59_A70F",        # 3B, 59
        "Function_60_A713",        # 3C, 60
        "Function_61_A717",        # 3D, 61
        "Function_62_A71B",        # 3E, 62
        "Function_63_A71F",        # 3F, 63
        "Function_64_A723",        # 40, 64
    )


    def Function_0_B0E(): pass

    label("Function_0_B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B96")
    SetChrFlags(0x2D, 0x80)
    SetChrFlags(0x30, 0x80)
    ClearChrFlags(0x3B, 0x80)
    ClearChrFlags(0x39, 0x80)
    SetChrPos(0x2C, 28500, 0, 82470, 45)
    SetChrPos(0x2E, 27820, 0, 98030, 225)
    SetChrPos(0x2F, 29470, 0, 97990, 45)
    OP_43(0x2F, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B7D")
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x2F, 0x10)
    Jump("loc_B93")

    label("loc_B7D")

    ClearChrFlags(0x36, 0x80)
    SetChrPos(0x39, 50750, 0, 78770, 0)

    label("loc_B93")

    Jump("loc_CE5")

    label("loc_B96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_BF3")
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 22804, 0, 71275, 220)
    TurnDirection(0x25, 0x27, 0)
    TurnDirection(0x27, 0x25, 0)
    SetChrFlags(0x25, 0x10)
    SetChrFlags(0x27, 0x10)
    SetChrFlags(0x30, 0x80)
    SetChrPos(0x2C, 46730, 0, 78510, 0)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x37, 0x80)
    Jump("loc_CE5")

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_C11")
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x2F, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x35, 0x80)
    Jump("loc_CE5")

    label("loc_C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_C88")
    Call(0, 31)
    SetChrFlags(0x2C, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrPos(0x2E, 47440, 0, 78530, 180)
    SetChrPos(0x2F, 46010, 0, 79440, 130)
    OP_43(0x2F, 0x0, 0x0, 0x2)
    ClearChrFlags(0x35, 0x80)
    SetChrPos(0x35, 66540, 0, 72560, 211)
    ClearChrFlags(0x25, 0x80)
    SetChrPos(0x25, 29920, -1800, 68470, 138)
    SetChrFlags(0x2D, 0x10)
    OP_71(0x12, 0x4)
    Jump("loc_CE5")

    label("loc_C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CAF")
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x2B, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CAC")
    ClearChrFlags(0x32, 0x80)

    label("loc_CAC")

    Jump("loc_CE5")

    label("loc_CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_CE5")
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x35, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_CD9")
    ClearChrFlags(0x32, 0x80)

    label("loc_CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 2)), scpexpr(EXPR_END)), "loc_CE5")
    ClearChrFlags(0x25, 0x80)

    label("loc_CE5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF6")
    SetChrFlags(0x2D, 0x80)

    label("loc_CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D05")
    OP_A2(0x1231)

    label("loc_D05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_D1B")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 36)
    Jump("loc_E17")

    label("loc_D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_D3A")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 44)
    Jump("loc_E17")

    label("loc_D3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_D50")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(1, 3)
    Jump("loc_E17")

    label("loc_D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_D66")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(1, 5)
    Jump("loc_E17")

    label("loc_D66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_D7C")
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(1, 4)
    Jump("loc_E17")

    label("loc_D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_D92")
    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 52)
    Jump("loc_E17")

    label("loc_D92")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DAC")
    OP_A3(0x10F6)
    Event(0, 43)
    Jump("loc_E17")

    label("loc_DAC")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_DC0"),
        (105, "loc_DD8"),
        (118, "loc_E04"),
        (SWITCH_DEFAULT, "loc_E17"),
    )


    label("loc_DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD5")
    SetMapFlags(0x10000000)
    Event(0, 30)

    label("loc_DD5")

    Jump("loc_E17")

    label("loc_DD8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF8")
    SetMapFlags(0x10000000)
    Event(0, 50)
    Jump("loc_E01")

    label("loc_DF8")

    SetMapFlags(0x10000000)
    Event(0, 51)

    label("loc_E01")

    Jump("loc_E17")

    label("loc_E04")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E14")
    Call(0, 49)

    label("loc_E14")

    Jump("loc_E17")

    label("loc_E17")

    Return()

    # Function_0_B0E end

    def Function_1_E18(): pass

    label("Function_1_E18")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFF5420, 0x230047)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3B")
    OP_64(0x2, 0x1)

    label("loc_E3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E50")
    OP_71(0x12, 0x4)

    label("loc_E50")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8A")
    OP_6F(0x11, 1500)
    OP_72(0x1A, 0x2)
    OP_71(0x12, 0x4)
    OP_71(0x1B, 0x4)
    OP_64(0x1, 0x1)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)

    label("loc_E8A")

    Return()

    # Function_1_E18 end

    def Function_2_E8B(): pass

    label("Function_2_E8B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB0")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_FF2")

    label("loc_EB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC9")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_FF2")

    label("loc_EC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE2")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_FF2")

    label("loc_EE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EFB")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_FF2")

    label("loc_EFB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F14")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_FF2")

    label("loc_F14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F2D")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_FF2")

    label("loc_F2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F46")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_FF2")

    label("loc_F46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5F")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_FF2")

    label("loc_F5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F78")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_FF2")

    label("loc_F78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F91")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_FF2")

    label("loc_F91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAA")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_FF2")

    label("loc_FAA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC3")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_FF2")

    label("loc_FC3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDC")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_FF2")

    label("loc_FDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF2")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_FF2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1007")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_FF2")

    label("loc_1007")

    Return()

    # Function_2_E8B end

    def Function_3_1008(): pass

    label("Function_3_1008")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_102B")
    OP_8D(0xFE, 24600, 90150, 28170, 94510, 4000)
    Jump("Function_3_1008")

    label("loc_102B")

    Return()

    # Function_3_1008 end

    def Function_4_102C(): pass

    label("Function_4_102C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_104F")
    OP_8D(0xFE, 28420, 86550, 31010, 89470, 4000)
    Jump("Function_4_102C")

    label("loc_104F")

    Return()

    # Function_4_102C end

    def Function_5_1050(): pass

    label("Function_5_1050")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        (
            "今天要和阿杰\x01",
            "外出游玩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "哎嘿，好高兴哦⊙\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_1050 end

    def Function_6_108C(): pass

    label("Function_6_108C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_116D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_10F2")

    ChrTalk(    #2
        0xFE,
        (
            "要去王立学院就读\x01",
            "果然需要很多钱啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "我也要在下次出海中\x01",
            "大赚一笔才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116A")

    label("loc_10F2")

    OP_A2(0xE)

    ChrTalk(    #4
        0xFE,
        (
            "我儿子好像有意\x01",
            "报考王立学院……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "要去那里上学，\x01",
            "需要很多钱啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "呼～首先要在下次出海中\x01",
            "大赚一笔才行啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116A")

    Jump("loc_1308")

    label("loc_116D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1219")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_11BB")

    ChrTalk(    #7
        0xFE,
        (
            "如果逃避争执\x01",
            "就不可能相互理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "我就是这么想的啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1216")

    label("loc_11BB")

    OP_A2(0xE)

    ChrTalk(    #9
        0xFE,
        (
            "打架什么的，也没什么啊。\x01",
            "争执多半伴随着争吵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "如果逃避争执\x01",
            "就不可能相互理解。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1216")

    Jump("loc_1308")

    label("loc_1219")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_124B")

    ChrTalk(    #11
        0xFE,
        "喂喂怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "在桥上干什么呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1308")

    label("loc_124B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_1286")

    ChrTalk(    #13
        0xFE,
        (
            "诺曼先生是很出色的人，\x01",
            "但就是对公约不重视。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1308")

    label("loc_1286")

    OP_A2(0xE)

    ChrTalk(    #14
        0xFE,
        (
            "诺曼先生是很出色的人，\x01",
            "但就是对公约不重视。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "卢安就不是旅游城市，\x01",
            "原本就是船员和渔夫的城市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "这点最好\x01",
            "别搞错了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1308")

    TalkEnd(0xFE)
    Return()

    # Function_6_108C end

    def Function_7_130C(): pass

    label("Function_7_130C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1324")
    SetChrSubChip(0xFE, 2)
    Jump("loc_1329")

    label("loc_1324")

    SetChrSubChip(0xFE, 1)

    label("loc_1329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_1388")

    ChrTalk(    #17
        0xFE,
        (
            "真想这样一直\x01",
            "待在卢安啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "啊～啊，前往王都的船\x01",
            "不能暂时停下吗～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1402")

    label("loc_1388")

    OP_A2(0xD)

    ChrTalk(    #19
        0xFE,
        (
            "工作结束之后\x01",
            "喝一杯真是格外美味呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "呼，真想这样一直\x01",
            "待在卢安啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "啊～啊，前往王都的船\x01",
            "不能暂时停下吗～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1402")

    Jump("loc_1492")

    label("loc_1405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1492")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_1449")

    ChrTalk(    #22
        0xFE,
        "呼～海风真舒服啊～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "呀～果然\x01",
            "卢安最棒了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1492")

    label("loc_1449")

    OP_A2(0xD)

    ChrTalk(    #24
        0xFE,
        (
            "呀，各位。\x01",
            "还在工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "我在等回去的船\x01",
            "现在是片刻的休息呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1492")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_7_130C end

    def Function_8_149B(): pass

    label("Function_8_149B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_15B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1503")

    ChrTalk(    #26
        0xFE,
        (
            "说来那些家伙，\x01",
            "连幽灵都要怪到我们头上啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "啊～回想起来\x01",
            "又开始焦躁不安了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15B1")

    label("loc_1503")

    OP_A2(0xC)

    ChrTalk(    #28
        0xFE,
        (
            "波尔多斯主任叫我来\x01",
            "向诺曼先生道歉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "明明是对方找的麻烦，\x01",
            "为什么要我去谢罪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "唉，虽说我说过那些贬低他儿子的话，\x01",
            "确实做的不对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "但还是～无法接受啊。\x02",
    )

    CloseMessageWindow()

    label("loc_15B1")

    Jump("loc_16F4")

    label("loc_15B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_164E")

    ChrTalk(    #32
        0xFE,
        (
            "市长候选人波尔多斯！\x01",
            "请多关照波尔多斯！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "海的男人波尔多斯！\x01",
            "懂道理的波尔多斯！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "波尔多斯将以火热的心\x01",
            "回应各位的期待！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F4")

    label("loc_164E")

    OP_A2(0xC)

    ChrTalk(    #35
        0xFE,
        (
            "诺曼阵营果然\x01",
            "出动不少宣传员啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "我虽然只有自己一个人，\x01",
            "但海的男人要以气势来决一胜负！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "呼～～吸～～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "市长候选人波尔多斯！\x01",
            "请多关照波尔多斯！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F4")

    TalkEnd(0xFE)
    Return()

    # Function_8_149B end

    def Function_9_16F8(): pass

    label("Function_9_16F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_17C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1779")

    ChrTalk(    #39
        0xFE,
        (
            "那个漂浮在远方天空\x01",
            "的大家伙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "那个到底是什么\x01",
            "谁都不告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "嗯～下次主日学校\x01",
            "问问看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_17C1")

    label("loc_1779")


    ChrTalk(    #42
        0xFE,
        (
            "浮在天上的那是什么\x01",
            "谁都不告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "嗯～下次主日学校\x01",
            "问问看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C1")

    Jump("loc_19A5")

    label("loc_17C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1864")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1828")

    ChrTalk(    #44
        0xFE,
        "哎呀，妈妈～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "那个浮在天上的\x01",
            "大家伙是什么～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "难道是新型飞船？\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_1861")

    label("loc_1828")


    ChrTalk(    #47
        0xFE,
        "哎呀，妈妈～～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "那个浮在天上的\x01",
            "大家伙是什么～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1861")

    Jump("loc_19A5")

    label("loc_1864")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_18BC")

    ChrTalk(    #49
        0xFE,
        (
            "刚才开始妈妈\x01",
            "就一直盯着海报看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "但是，海报里的那个人\x01",
            "并不怎么帅嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A5")

    label("loc_18BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_18DF")

    ChrTalk(    #51
        0xFE,
        (
            "妈妈～？\x01",
            "怎么了～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A5")

    label("loc_18DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1928")

    ChrTalk(    #52
        0xFE,
        "今天有主日学校吧⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "能见到朋友们，\x01",
            "真是好期待啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A5")

    label("loc_1928")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_19A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_195E")

    ChrTalk(    #54
        0xFE,
        (
            "声音最大的人\x01",
            "就会当上新市长吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A5")

    label("loc_195E")

    OP_A2(0xB)

    ChrTalk(    #55
        0xFE,
        (
            "总觉得叔叔们\x01",
            "叫得好大声哟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "问过妈妈了，\x01",
            "她说这个是选举。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A5")

    TalkEnd(0xFE)
    Return()

    # Function_9_16F8 end

    def Function_10_19A9(): pass

    label("Function_10_19A9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1A89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A30")

    ChrTalk(    #57
        0xFE,
        (
            "刚才游击士协会\x01",
            "有一些人冲了出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "说不定哪里\x01",
            "又发生事件了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "这种时候果然\x01",
            "还是游击士们可靠啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_1A86")

    label("loc_1A30")


    ChrTalk(    #60
        0xFE,
        (
            "这种时候还是\x01",
            "游击士们可靠啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "与王国军不同，\x01",
            "游击士在各地支部真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A86")

    Jump("loc_1DE7")

    label("loc_1A89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B1B")

    ChrTalk(    #62
        0xFE,
        (
            "由于大桥不能动了，\x01",
            "去南区现在很麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "真是的，市长诺曼先生\x01",
            "在干什么呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "不会是以为准备了渡船\x01",
            "就足够了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_1B71")

    label("loc_1B1B")


    ChrTalk(    #65
        0xFE,
        (
            "由于大桥不能动了，\x01",
            "去南区现在很麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "真是的，市长诺曼先生\x01",
            "在干什么呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B71")

    Jump("loc_1DE7")

    label("loc_1B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1C01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1BC6")

    ChrTalk(    #67
        0xFE,
        "重要的还是人品啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "嗯，只看海报\x01",
            "可不知道是好人坏人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BFE")

    label("loc_1BC6")

    OP_A2(0xA)

    ChrTalk(    #69
        0xFE,
        "重要的还是人品啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "就看这个\x01",
            "决定投谁票了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BFE")

    Jump("loc_1DE7")

    label("loc_1C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1C9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1C43")

    ChrTalk(    #71
        0xFE,
        (
            "真是难以置信，\x01",
            "居然做出打架这么危险的事……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C98")

    label("loc_1C43")

    OP_A2(0xA)

    ChrTalk(    #72
        0xFE,
        (
            "真是难以置信，\x01",
            "居然做出打架这么危险的事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "希望两边都\x01",
            "冷静一下头脑啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C98")

    Jump("loc_1DE7")

    label("loc_1C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_1CEF")

    ChrTalk(    #74
        0xFE,
        (
            "桥、桥上好像有人\x01",
            "在吵架啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "这样下去的话，\x01",
            "那气势都快打起来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DE7")

    label("loc_1CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1D52")

    ChrTalk(    #76
        0xFE,
        (
            "波尔多斯候选人\x01",
            "是个年轻的好男人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "但也不能因为这个理由\x01",
            "就投票啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D97")

    label("loc_1D52")

    OP_A2(0xA)

    ChrTalk(    #78
        0xFE,
        (
            "嗯～投给\x01",
            "谁好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "好像两个人都还缺点\x01",
            "决定性的东西似的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D97")

    Jump("loc_1DE7")

    label("loc_1D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1DE7")

    ChrTalk(    #80
        0xFE,
        (
            "选举的时候\x01",
            "这种宣传劲儿真讨厌啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "唉，只有\x01",
            "稍微忍耐一下了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE7")

    TalkEnd(0xFE)
    Return()

    # Function_10_19A9 end

    def Function_11_1DEB(): pass

    label("Function_11_1DEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1F04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9C")

    ChrTalk(    #82
        0xFE,
        (
            "那个浮在天上的东西\x01",
            "到底是什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "难道…\x01",
            "会是帝国军的新兵器……或者？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "不、不……那是不可能的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "就算是帝国\x01",
            "也不可能做出那种东西来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1F01")

    label("loc_1E9C")


    ChrTalk(    #86
        0xFE,
        (
            "那个浮在天上的东西\x01",
            "到底是什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "虽然觉得是帝国的新兵器，\x01",
            "但是这想法应该\x01",
            "也是有可能的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F01")

    Jump("loc_2398")

    label("loc_1F04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1FF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FA2")

    ChrTalk(    #88
        0xFE,
        "嗯、嗯…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "那个浮在天上的东西\x01",
            "到底是什么呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "至少发表一下市长声明\x01",
            "让大家安心啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "现在这时候\x01",
            "音信全无是怎么回事呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1FF4")

    label("loc_1FA2")


    ChrTalk(    #92
        0xFE,
        (
            "那个浮在天上的东西\x01",
            "到底是什么啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "至少发表一下市长声明\x01",
            "让大家安心啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF4")

    Jump("loc_2398")

    label("loc_1FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_214D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_20E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_205D")

    ChrTalk(    #94
        0xFE,
        (
            "市长候选人诺曼\x01",
            "请多多关照～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "诺曼将以旅游业为中心，\x01",
            "活化卢安市～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DD")

    label("loc_205D")

    OP_A2(0x7)

    ChrTalk(    #96
        0xFE,
        (
            "诺曼先生对港口问题\x01",
            "也不会轻视。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "希望各位市民\x01",
            "能更了解此事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "那么，已经到了最后阶段，\x01",
            "今天也要充满气势地高呼！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DD")

    Jump("loc_214A")

    label("loc_20E0")

    OP_A2(0x6)

    ChrTalk(    #99
        0xFE,
        (
            "诺曼先生对港口问题\x01",
            "也不会轻视。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "如果不是这样我也\x01",
            "不会支持他的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "因为我\x01",
            "本来也是渔师啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_214A")

    Jump("loc_2398")

    label("loc_214D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_222F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_21B4")

    ChrTalk(    #102
        0xFE,
        (
            "这种对立要是向全市\x01",
            "发展那可头痛了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "两个阵营都需要\x01",
            "相互理解从而更加努力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_222C")

    label("loc_21B4")

    OP_A2(0x6)

    ChrTalk(    #104
        0xFE,
        (
            "呀～刚才的\x01",
            "骚动真是危险啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "大家都杀气腾腾的，\x01",
            "真是差点打起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "这种对立要是向全市\x01",
            "发展那可头痛了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_222C")

    Jump("loc_2398")

    label("loc_222F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_231B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2294")

    ChrTalk(    #107
        0xFE,
        (
            "休息片刻\x01",
            "一会再播音和发放传单哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "无论如何都要让诺曼先生\x01",
            "当上市长啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2318")

    label("loc_2294")

    OP_A2(0x6)

    ChrTalk(    #109
        0xFE,
        (
            "我的本职是旅游向导，\x01",
            "不过暂时休假支持诺曼先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "反正选举期间\x01",
            "游客也显著减少了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "那么，休息片刻\x01",
            "再大声努力支援吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2318")

    Jump("loc_2398")

    label("loc_231B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2398")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_235B")

    ChrTalk(    #112
        0xFE,
        (
            "旅游城市卢安的啦啦队长！\x01",
            "请多支持诺曼～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2398")

    label("loc_235B")

    OP_A2(0x6)

    ChrTalk(    #113
        0xFE,
        (
            "市长候选人诺曼\x01",
            "将支援旅游业！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "请多\x01",
            "支持诺曼～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2398")

    TalkEnd(0xFE)
    Return()

    # Function_11_1DEB end

    def Function_12_239C(): pass

    label("Function_12_239C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_23A7")
    Return()

    label("loc_23A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_23B2")
    Return()

    label("loc_23B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_23BD")
    Return()

    label("loc_23BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_23C8")
    Return()

    label("loc_23C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23D6")
    Jump("loc_23DD")

    label("loc_23D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_23DD")

    label("loc_23DD")

    OP_4A(0x30, 0)

    ChrTalk(    #115 op#A
        0x30,
        (
            "#4A请多支持诺曼～！\x01",
            "请投诺曼宝贵１票！\x02",
        )
    )

    Sleep(2000)
    OP_4B(0x30, 0)
    Return()

    # Function_12_239C end

    def Function_13_2416(): pass

    label("Function_13_2416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2421")
    Return()

    label("loc_2421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_242C")
    Return()

    label("loc_242C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2437")
    Return()

    label("loc_2437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_2442")
    Return()

    label("loc_2442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2450")
    Jump("loc_2457")

    label("loc_2450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2457")

    label("loc_2457")

    OP_4A(0x2C, 0)

    ChrTalk(    #116 op#A
        0x2C,
        (
            "#4A旅游城市卢安的啦啦队长！\x01",
            "请多支持诺曼～！\x02",
        )
    )

    Sleep(2000)
    OP_4B(0x2C, 0)
    Return()

    # Function_13_2416 end

    def Function_14_2496(): pass

    label("Function_14_2496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_24A1")
    Return()

    label("loc_24A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_24AB")
    Jump("loc_24D7")

    label("loc_24AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_24B6")
    Return()

    label("loc_24B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_24C1")
    Return()

    label("loc_24C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_24CF")
    Jump("loc_24D7")

    label("loc_24CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_24D7")
    Return()

    label("loc_24D7")

    OP_4A(0x2B, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2516")

    ChrTalk(    #117 op#A
        0x2C,
        (
            "#4A旅游城市卢安的啦啦队长！\x01",
            "请多支持诺曼～！\x02",
        )
    )

    Jump("loc_2545")

    label("loc_2516")


    ChrTalk(    #118 op#A
        0x2B,
        (
            "#4A市长候选人波尔多斯！\x01",
            "请多关照波尔多斯！\x02",
        )
    )


    label("loc_2545")

    Sleep(2000)
    OP_4B(0x2B, 0)
    Return()

    # Function_14_2496 end

    def Function_15_254F(): pass

    label("Function_15_254F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_266E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_25BD")

    ChrTalk(    #119
        0xFE,
        (
            "说幽灵是波尔多斯阵营\x01",
            "搞的鬼是太轻率……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "就算如此贬低诺曼先生\x01",
            "的儿子也不应该吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_266B")

    label("loc_25BD")

    OP_A2(0x5)

    ChrTalk(    #121
        0xFE,
        (
            "酒店里出现了像幽灵一样的影子,\x01",
            "真是确有其事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "但说是波尔多斯阵营\x01",
            "搞的鬼是太轻率……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "就算如此贬低诺曼先生\x01",
            "的儿子也不应该吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "啊～想起来\x01",
            "还是火冒三丈啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_266B")

    Jump("loc_286D")

    label("loc_266E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2796")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_26F8")

    ChrTalk(    #125
        0xFE,
        (
            "市长候选人诺曼\x01",
            "请多多关照～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "让卢安市重生为\x01",
            "充满活力的旅游城市！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "这次的选举\x01",
            "请务必投诺曼宝贵１票！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2793")

    label("loc_26F8")

    OP_A2(0x5)

    ChrTalk(    #128
        0xFE,
        (
            "波尔多斯阵营的\x01",
            "宣传员好像也来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "好～这下\x01",
            "更要重新鼓足气势了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "市长候选人诺曼\x01",
            "请多多关照～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "下任市长是诺曼！\x01",
            "请投诺曼宝贵１票！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2793")

    Jump("loc_286D")

    label("loc_2796")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_286D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_281C")

    ChrTalk(    #132
        0xFE,
        (
            "市长候选人诺曼\x01",
            "请多多关照～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "让卢安市重生为\x01",
            "充满活力的旅游城市！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "这次的选举\x01",
            "请务必投诺曼宝贵１票！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_286D")

    label("loc_281C")

    OP_A2(0x5)

    ChrTalk(    #135
        0xFE,
        (
            "市长候选人诺曼\x01",
            "请多多关照～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "下任市长是诺曼！\x01",
            "请投诺曼宝贵１票！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_286D")

    TalkEnd(0xFE)
    Return()

    # Function_15_254F end

    def Function_16_2871(): pass

    label("Function_16_2871")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_28C6")

    ChrTalk(    #137
        0xFE,
        (
            "刚才开始\x01",
            "选举的声音就吵个不停。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "怪不得旅行费用\x01",
            "变得这么便宜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_291D")

    label("loc_28C6")

    OP_A2(0x4)

    ChrTalk(    #139
        0xFE,
        (
            "景色是很不错，\x01",
            "就是选举的声音有点吵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "休养的心情都破坏了，\x01",
            "唉，也没办法。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_291D")

    TalkEnd(0xFE)
    Return()

    # Function_16_2871 end

    def Function_17_2921(): pass

    label("Function_17_2921")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2973")

    ChrTalk(    #141
        0xFE,
        (
            "虽然是以娱乐场为目的\x01",
            "来旅行的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "但也不能不去市内看看啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29B3")

    label("loc_2973")

    OP_A2(0x3)

    ChrTalk(    #143
        0xFE,
        "喔喔，好厉害的桥啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "真想看一次\x01",
            "它运转时的样子啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B3")

    TalkEnd(0xFE)
    Return()

    # Function_17_2921 end

    def Function_18_29B7(): pass

    label("Function_18_29B7")

    Call(0, 19)
    Return()

    # Function_18_29B7 end

    def Function_19_29BC(): pass

    label("Function_19_29BC")

    TalkBegin(0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2A5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A36")

    ChrTalk(    #145
        0x28,
        (
            "浮在天上的岛\x01",
            "今天金光四射……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x28,
        "……那个光辉是通往未来的门吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x28,
        (
            "还是\x01",
            "是结束的征兆……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2A59")

    label("loc_2A36")


    ChrTalk(    #148
        0x28,
        (
            "浮在天上的岛\x01",
            "今天金光四射……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A59")

    Jump("loc_2ED5")

    label("loc_2A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2B4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B04")

    ChrTalk(    #149
        0x28,
        (
            "就算用沙筑起的宫殿，\x01",
            "沙子到底是沙子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x28,
        (
            "下一场雨\x01",
            "就烟消云散了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x28,
        (
            "难以得到的就难以失去，\x01",
            "容易得到的也容易失去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x28,
        "……同样的道理。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_2B4A")

    label("loc_2B04")


    ChrTalk(    #153
        0x28,
        (
            "就算用沙筑起的宫殿，\x01",
            "沙子到底是沙子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x28,
        (
            "下一场雨\x01",
            "就消失了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B4A")

    Jump("loc_2ED5")

    label("loc_2B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 3)), scpexpr(EXPR_END)), "loc_2C54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2BBB")

    ChrTalk(    #155
        0x28,
        (
            "发生过一次的事\x01",
            "就期待再次发生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x28,
        (
            "人心始终是复杂的啊。\x01",
            "但这也不是什么坏事。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C51")

    label("loc_2BBB")

    OP_A2(0x2)

    ChrTalk(    #157
        0x28,
        "………………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x28,
        (
            "发生过一次的事，\x01",
            "就期待再次发生……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x28,
        (
            "往这方向去想\x01",
            "是人心特有的结构哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x28,
        (
            "绝不是你的心\x01",
            "有什么不好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C51")

    Jump("loc_2CB7")

    label("loc_2C54")


    ChrTalk(    #161
        0x28,
        (
            "集聚，相恋，誓约，\x01",
            "吹走消散……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x28,
        (
            "空中的云也……\x01",
            "为了换取自身的自由，\x01",
            "承受着几多的离别啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CB7")

    Jump("loc_2ED5")

    label("loc_2CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2D93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2D18")

    ChrTalk(    #163
        0x28,
        (
            "人的心就像彼此\x01",
            "相照映的镜子一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x28,
        (
            "爱和憎，\x01",
            "都在被反射时\x01",
            "相互增辉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D90")

    label("loc_2D18")

    OP_A2(0x2)

    ChrTalk(    #165
        0x28,
        (
            "人的心就像彼此\x01",
            "相照映的镜子一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x28,
        (
            "如果我憎恨你\x01",
            "不知不觉你也会憎恨我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x28,
        (
            "而后我就会更加\x01",
            "强烈地憎恨你。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D90")

    Jump("loc_2ED5")

    label("loc_2D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DFD")

    ChrTalk(    #168
        0x28,
        (
            "哎呀，今天蓝天\x01",
            "也是这么广阔晴朗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x28,
        "看啊，看啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x28,
        (
            "从那么高的地方\x01",
            "俯视着我们。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ED5")

    label("loc_2DFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2ED5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2E6E")

    ChrTalk(    #171
        0x28,
        (
            "啊啊，如果没有名字\x01",
            "会有多么自由呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x28,
        (
            "像破茧而出的蝴蝶一样，\x01",
            "我也是因为自我而存在……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ED5")

    label("loc_2E6E")

    OP_A2(0x2)

    ChrTalk(    #173
        0x28,
        (
            "人的名字\x01",
            "到底有什么意义呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x28,
        "我就是我本身……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x28,
        (
            "为什么要使用语言\x01",
            "制造出另一个我呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ED5")

    TalkEnd(0x28)
    Return()

    # Function_19_29BC end

    def Function_20_2ED9(): pass

    label("Function_20_2ED9")


    ChrTalk(    #176
        0x27,
        "叔父大人怎么会这么晚呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x27,
        (
            "我已经\x01",
            "等了１个小时了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x25,
        "呀，抱歉抱歉。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x25,
        (
            "意想不到的大鱼\x01",
            "上钩了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x27,
        "啊，真受不了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x27,
        (
            "在这样的城市中\x01",
            "也能钓鱼吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x25,
        "哈哈，别那么生气嘛。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_20_2ED9 end

    def Function_21_2F99(): pass

    label("Function_21_2F99")

    TalkBegin(0xFE)
    OP_4A(0x25, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3000")

    ChrTalk(    #183
        0xFE,
        (
            "要吃饭的话，\x01",
            "推荐去南区的渔师酒馆哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "比起娱乐场\x01",
            "我想叔父大人更喜欢那家店。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_3000")

    OP_A2(0x1)
    Call(0, 20)

    label("loc_3007")

    OP_4B(0x25, 255)
    TalkEnd(0xFE)
    Return()

    # Function_21_2F99 end

    def Function_22_300F(): pass

    label("Function_22_300F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_3068")
    OP_4A(0x27, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_305A")

    ChrTalk(    #185
        0xFE,
        (
            "总之，\x01",
            "去填饱肚子吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "知道哪里比较好吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3061")

    label("loc_305A")

    OP_A2(0x1)
    Call(0, 20)

    label("loc_3061")

    OP_4B(0x27, 255)
    Jump("loc_334B")

    label("loc_3068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_30FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_30B6")

    ChrTalk(    #187
        0xFE,
        "唔～比试耐力吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "唔，这也挺有趣的。\x01",
            "就决一胜负吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30FC")

    label("loc_30B6")

    OP_A2(0x1)

    ChrTalk(    #189
        0xFE,
        "……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "………来，怎么了。\x01",
            "来，快咬钩啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30FC")

    Jump("loc_334B")

    label("loc_30FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_312E")

    ChrTalk(    #191
        0xFE,
        (
            "怎么怎么？\x01",
            "哎呀，怎么这么吵闹？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_334B")

    label("loc_312E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3253")
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3166")
    SetChrSubChip(0xFE, 1)
    Jump("loc_316B")

    label("loc_3166")

    SetChrSubChip(0xFE, 2)

    label("loc_316B")

    OP_8C(0xFE, 225, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_31D5")

    ChrTalk(    #192
        0xFE,
        (
            "朋友说得对，\x01",
            "的确是相当不错的钓鱼点呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "呼呼呼……\x01",
            "这下似乎能期待一下了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_324B")

    label("loc_31D5")

    OP_A2(0x1)

    ChrTalk(    #194
        0xFE,
        (
            "嗯，在这市区里有许多\x01",
            "相当不错的钓鱼点呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "虽然品种不怎么样，\x01",
            "但经常能上钩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "和拜舍尔\x01",
            "说的一样呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_324B")

    SetChrSubChip(0xFE, 0)
    Jump("loc_334B")

    label("loc_3253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_334B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_32D3")

    ChrTalk(    #197
        0xFE,
        (
            "卢安如传言一样，\x01",
            "真是满城选举的气氛啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "这么吵闹\x01",
            "真担心鱼会逃跑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "暂且喝杯茶，\x01",
            "然后再开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_334B")

    label("loc_32D3")

    OP_A2(0x1)

    ChrTalk(    #200
        0xFE,
        (
            "哎呀，是你们。\x01",
            "在工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "话说回来，如传言一样卢安\x01",
            "真是满城选举的气氛啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "这么吵闹\x01",
            "真担心鱼会逃跑呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334B")

    TalkEnd(0xFE)
    Return()

    # Function_22_300F end

    def Function_23_334F(): pass

    label("Function_23_334F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_343A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_33AB")

    ChrTalk(    #203
        0x24,
        (
            "再过一会儿\x01",
            "就去南区看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x24,
        (
            "好像是个危险的地方，\x01",
            "有点害怕呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_343A")

    label("loc_33AB")

    OP_A2(0x0)

    ChrTalk(    #205
        0x24,
        "嗯～好美的景色啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x24,
        (
            "我是柏斯来的商人，\x01",
            "正在寻找新的旅游资源。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x24,
        (
            "因为这个城市魅力的本质是港口呢。\x01",
            "我想南区的开发会是今后的关键。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_343A")

    TalkEnd(0xFE)
    Return()

    # Function_23_334F end

    def Function_24_343E(): pass

    label("Function_24_343E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3539")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34E0")

    ChrTalk(    #208
        0xFE,
        (
            "本、本来预定用打工\x01",
            "挣的钱作旅费……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "这、这么快就用光了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        "哈哈……怎么办……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "哈、哈哈……哈哈……\x01",
            "啊哈哈哈哈…………\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_3536")

    label("loc_34E0")


    ChrTalk(    #212
        0xFE,
        (
            "打、打工挣的钱\x01",
            "已经用光了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "这下又一分钱都没了吗。\x01",
            "哈、哈哈哈哈哈…………\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3536")

    Jump("loc_357C")

    label("loc_3539")


    ChrTalk(    #214
        0xFE,
        (
            "吃喝玩乐…把买回去的\x01",
            "船票钱都用掉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "啊啊……怎么办……\x02",
    )

    CloseMessageWindow()

    label("loc_357C")

    TalkEnd(0xFE)
    Return()

    # Function_24_343E end

    def Function_25_3580(): pass

    label("Function_25_3580")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35DB")

    ChrTalk(    #216
        0xFE,
        (
            "巡逻啦向导啦，\x01",
            "从早工作到晚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "呼，多少能理解\x01",
            "游击士的辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_3600")

    label("loc_35DB")


    ChrTalk(    #218
        0xFE,
        (
            "巡逻啦向导啦，\x01",
            "从早工作到晚啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3600")

    TalkEnd(0xFE)
    Return()

    # Function_25_3580 end

    def Function_26_3604(): pass

    label("Function_26_3604")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_371C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C5")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #219
        0xFE,
        "哟，艾丝蒂尔㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "你应该知道\x01",
            "去南区可以乘船了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        (
            "唉，不过想想\x01",
            "也真辛苦啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "因为，你看。\x01",
            "我是个好人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        (
            "被大家一拜托，\x01",
            "就怎么也拒绝不了啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_3719")

    label("loc_36C5")


    ChrTalk(    #224
        0xFE,
        (
            "看起来很轻松，\x01",
            "没想到这么辛苦啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "因为我是个好人，\x01",
            "有人拜托就拒绝不了啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3719")

    Jump("loc_37C1")

    label("loc_371C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_37C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3777")

    ChrTalk(    #226
        0xFE,
        (
            "桥不能动了，\x01",
            "去南区可以乘船了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "从酒店地下\x01",
            "可以到达渡口哦～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_37C1")

    label("loc_3777")


    ChrTalk(    #228
        0xFE,
        (
            "从酒店地下\x01",
            "可以到达渡口哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "那边有我们的成员\x01",
            "带路，可以问问看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37C1")

    TalkEnd(0xFE)
    Return()

    # Function_26_3604 end

    def Function_27_37C5(): pass

    label("Function_27_37C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3829")

    ChrTalk(    #230
        0xFE,
        (
            "城市暂时相当安定，\x01",
            "但不知道还会发生什么事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "我们也不能疏忽大意，\x01",
            "要持续警戒啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3829")

    TalkEnd(0xFE)
    Return()

    # Function_27_37C5 end

    def Function_28_382D(): pass

    label("Function_28_382D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_38BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3887")

    ChrTalk(    #232
        0xFE,
        (
            "要去南街区\x01",
            "请走这边的酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "酒店地下１层\x01",
            "可以通向渡口。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_38BC")

    label("loc_3887")


    ChrTalk(    #234
        0xFE,
        (
            "有事可做\x01",
            "真好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        (
            "至少\x01",
            "不会觉得无聊呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x12)

    label("loc_38BC")

    Jump("loc_3975")

    label("loc_38BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3975")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3933")

    ChrTalk(    #236
        0xFE,
        (
            "啊～现在大桥\x01",
            "不能通行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "要去南街区\x01",
            "请走这边的酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "酒店地下１层\x01",
            "可以通向渡口。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_3975")

    label("loc_3933")


    ChrTalk(    #239
        0xFE,
        (
            "要去南街区\x01",
            "请走这边的酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "酒店地下１层\x01",
            "可以通向渡口。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3975")

    TalkEnd(0xFE)
    Return()

    # Function_28_382D end

    def Function_29_3979(): pass

    label("Function_29_3979")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_398A")
    Return()

    label("loc_398A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_399F")
    Call(0, 53)
    Call(0, 54)

    label("loc_399F")

    EventBegin(0x0)
    OP_4A(0x3A, 255)
    OP_4A(0x38, 255)
    OP_4A(0x39, 255)
    TurnDirection(0x0, 0x3A, 0)
    TurnDirection(0x1, 0x3A, 0)
    TurnDirection(0x2, 0x3A, 0)
    TurnDirection(0x3, 0x3A, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #241
        0x101,
        "#1004F啊……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)

    def lambda_3A2F():
        OP_6D(51000, 0, 70500, 3000)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_3A2F)
    OP_0D()
    WaitChrThread(0x38, 0x1)
    Sleep(1000)
    SetChrPos(0x101, 51550, 0, 79700, 180)
    SetChrPos(0x102, 50300, 0, 80000, 180)
    SetChrPos(0xF8, 51550, 0, 80960, 180)
    SetChrPos(0xF9, 50300, 0, 81370, 180)

    ChrTalk(    #242
        0x3A,
        "哟，状况怎样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x38,
        (
            "啊啊，照指示\x01",
            "都在好好引导市民坐船呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x38,
        (
            "告诉他们桥不能通行，要去南区\x01",
            "就要使用酒店的小船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x39,
        (
            "#4P其他成员\x01",
            "也都各尽其职呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x39,
        (
            "#4P意外的是，我们的成员\x01",
            "中有不少认真的人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x3A,
        (
            "啊啊，现在\x01",
            "他们好像都很努力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x3A,
        (
            "如果有人偷懒\x01",
            "马上来通知我哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x3A,
        "我去搞定他。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x38,
        "噢、噢……\x02",
    )

    CloseMessageWindow()

    def lambda_3BCA():
        OP_6D(50910, 0, 72470, 2500)
        ExitThread()

    QueueWorkItem(0x38, 2, lambda_3BCA)

    def lambda_3BE2():
        OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3BE2)
    Sleep(100)

    def lambda_3BFD():
        OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3BFD)
    Sleep(100)

    def lambda_3C18():
        OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_3C18)
    Sleep(100)

    def lambda_3C33():
        OP_94(0x1, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_3C33)
    WaitChrThread(0xF9, 0x2)
    WaitChrThread(0x38, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CE7")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇听说了渡鸦帮的改正】\x01",      # 0
            "【◇没听说渡鸦帮的改正】\x01",      # 1
            "【◇不变更】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3CDB"),
        (1, "loc_3CE1"),
        (SWITCH_DEFAULT, "loc_3CE7"),
    )


    label("loc_3CDB")

    OP_A2(0x2080)
    Jump("loc_3CE7")

    label("loc_3CE1")

    OP_A3(0x2080)
    Jump("loc_3CE7")

    label("loc_3CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_END)), "loc_3D24")

    ChrTalk(    #251
        0x101,
        (
            "#1011F#1P？？？\x02\x03",

            "在这种地方商量什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DA8")

    label("loc_3D24")


    ChrTalk(    #252
        0x101,
        (
            "#1009F#1P什～么搞定他啊。\x02\x03",

            "在这种地方偷偷摸摸，\x01",
            "又在搞什么阴谋诡计？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3DA8")

    ChrTalk(    #253
        0x106,
        "#551F#3P……真是些毫无上进心的家伙啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3DA8")

    Jump("loc_3DE0")

    label("loc_3DAB")


    ChrTalk(    #254
        0x101,
        (
            "#1011F#1P哎啊～真令人吃惊。\x02\x03",

            "好像真的在努力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DE0")

    OP_62(0x3A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x38, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x39, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_3E3A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_3E3A)

    def lambda_3E48():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x38, 1, lambda_3E48)

    def lambda_3E56():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_3E56)
    Sleep(500)

    ChrTalk(    #255
        0x3A,
        "你，你们……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E9A")

    ChrTalk(    #256
        0x38,
        "阿、阿加特……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3EB0")

    label("loc_3E9A")


    ChrTalk(    #257
        0x38,
        "哦，好久不见啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_END)), "loc_3F03")

    ChrTalk(    #258
        0x101,
        (
            "#1015F#1P在南街区\x01",
            "也看到他们的身影……\x02\x03",

            "你们\x01",
            "在搞什么活动？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB6")

    label("loc_3F03")


    ChrTalk(    #259
        0x101,
        (
            "#1019F#1P那，这次\x01",
            "在商量什么坏事？\x02\x03",

            "顺手牵羊？\x01",
            "还是恐吓？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x39, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #260
        0x39,
        (
            "艾、艾丝蒂尔～\x01",
            "你又误解啦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x39,
        (
            "我们渡鸦帮\x01",
            "脱胎换骨了啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x101,
        "#1004F#1P咦？怎么回事？\x02",
    )

    CloseMessageWindow()

    label("loc_3FB6")


    ChrTalk(    #263
        0x38,
        (
            "喔……\x01",
            "是洛克那家伙提议的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x38,
        (
            "前阵子开始做城里的\x01",
            "警备和向导了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_405A")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4098")

    label("loc_405A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4081")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4098")

    label("loc_4081")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4098")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40BF")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_40FD")

    label("loc_40BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40E6")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_40FD")

    label("loc_40E6")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_40FD")

    Sleep(1000)

    ChrTalk(    #265
        0x101,
        "#1004F#1P骗、骗人……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4145")

    ChrTalk(    #266
        0x106,
        "#052F#3P真的假的……\x02",
    )

    CloseMessageWindow()

    label("loc_4145")


    ChrTalk(    #267
        0x102,
        (
            "#1044F#4P就是说……\x01",
            "像自卫队一样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x3A,
        "才没那么死板呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x3A,
        (
            "刚才还正在商量其他\x01",
            "相关活动呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x101,
        (
            "#1015F#1P嗯、嗯………\x02\x03",

            "感觉太突然了，\x01",
            "难以置信……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x102,
        "#1040F#4P不过看起来是真的呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x3A,
        (
            "嗯，反正也没\x01",
            "指望你们相信啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x3A,
        (
            "这不是为了任何人……\x01",
            "而是完全为了\x01",
            "我们自己。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x3A, 180, 400)
    Sleep(500)

    ChrTalk(    #274
        0x3A,
        "……继续商量了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x38,
        "噢……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x38, 315, 400)

    ChrTalk(    #276
        0x39,
        (
            "想去南区的话\x01",
            "请使用渡船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x39,
        (
            "从酒店地下\x01",
            "可以到达渡口哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_457F")

    label("loc_42D2")


    ChrTalk(    #278
        0x39,
        (
            "嘿嘿，怎样？\x01",
            "艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x39,
        (
            "我们的出色表现，\x01",
            "听说了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x101,
        (
            "#1000F#1P听嘉恩先生说了呢。\x02\x03",

            "似乎开始用自己的力量\x01",
            "保护起卢安了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x38,
        (
            "喔，这个活动\x01",
            "是洛克那家伙提议的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x38,
        (
            "现在正在城市中\x01",
            "负责警备和向导。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x102,
        (
            "#1044F#4P就是说……\x01",
            "像自卫队一样吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x3A,
        "才没那么死板呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x3A,
        (
            "刚才还正在商量其他\x01",
            "相关活动呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4478")

    ChrTalk(    #286
        0x106,
        (
            "#053F#3P嗯，算是给自己\x01",
            "做了个了断吗。\x02\x03",

            "#051F不知道你们能做到何种程度，\x01",
            "就都努力做做看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4478")


    ChrTalk(    #287
        0x3A,
        (
            "我们是自愿的，\x01",
            "不会给你们添麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x3A,
        (
            "当然实际的活动\x01",
            "还是要请协会配合吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        (
            "#1006F#1P啊，嗯。\x01",
            "请多帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x102,
        "#1040F#4P多多关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x3A,
        (
            "那么，我们\x01",
            "还要继续商量呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x3A, 180, 400)

    ChrTalk(    #292
        0x39,
        (
            "想去南区的话\x01",
            "请使用渡船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x39,
        (
            "从酒店地下\x01",
            "可以到达渡口哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x38,
        "那么，回头见。\x02",
    )

    CloseMessageWindow()

    label("loc_457F")

    OP_8C(0x38, 315, 400)
    OP_8C(0x39, 45, 400)
    OP_4B(0x3A, 255)
    OP_4B(0x38, 255)
    OP_4B(0x39, 255)
    OP_A2(0x20BA)
    OP_A2(0x2080)
    EventEnd(0x0)
    Return()

    # Function_29_3979 end

    def Function_30_45A2(): pass

    label("Function_30_45A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45B3")
    Call(0, 53)

    label("loc_45B3")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_6D(25350, 0, 114410, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 25710, 0, 114720, 179)
    SetChrPos(0xF7, 24700, 0, 115030, 168)
    SetChrPos(0x109, 25250, 0, 113150, 181)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #295
        0x109,
        "#1068F#5P哎呀哎呀，终于回来了吗～？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)

    ChrTalk(    #296
        0x109,
        (
            "#1062F太感谢了。\x01",
            "送到这里真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x101,
        "#1016F#5P啊哈哈，不用谢了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4715")

    ChrTalk(    #298
        0x106,
        (
            "#051F就算没有我们\x01",
            "你自己也没问题吧。\x02\x03",

            "虽说弩箭比较老式……\x01",
            "但本事可是相当了不得啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4766")

    label("loc_4715")


    ChrTalk(    #299
        0x103,
        (
            "#027F就算没有我们\x01",
            "你也没问题吧。\x02\x03",

            "弩箭虽然很少见……\x01",
            "但本领却是相当了得吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4766")


    ChrTalk(    #300
        0x109,
        (
            "#1066F呀～因为巡回神父\x01",
            "都是自己在外单独行事的嘛。\x02\x03",

            "最低限度的武装还是要准备的，\x01",
            "但哪里比得上专业人士嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        (
            "#1015F#5P嗯～是吗～？\x02\x03",

            "我倒觉得你的本事\x01",
            "当游击士都足够了哟。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #302
        0x109,
        (
            "#1061F哎呀，艾丝蒂尔真是的～\x01",
            "都把人捧上天啦。\x02\x03",

            "大哥哥会当真哦～？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #303
        0x101,
        "#1019F#5P说、说什么啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x109,
        (
            "#1061F哈哈，小事情不要介意。\x02\x03",

            "#1060F说到刚才的幽灵，\x01",
            "卢安教会\x01",
            "也有好几个人来询问的样子。\x02\x03",

            "只是，据迪奥德罗教区长说\x01",
            "好像不是普通的灵。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #305
        0x101,
        "#1004F#5P不是普通的灵……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_49C1")

    ChrTalk(    #306
        0x106,
        (
            "#050F根据教会的教条，人死之后，\x01",
            "多行善事的灵魂会上天堂对吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A03")

    label("loc_49C1")


    ChrTalk(    #307
        0x103,
        (
            "#020F根据教会的教条，人死之后，\x01",
            "多行善事的灵魂会上天堂对吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A03")


    ChrTalk(    #308
        0x109,
        (
            "#1065F嗯嗯，相反背负罪责的灵魂\x01",
            "会堕入昏暗的炼狱……\x02\x03",

            "但，偶尔也会有跳出这限制\x01",
            "两边都去不了的灵魂。\x02\x03",

            "#1060F那就是所谓的『幽灵』，\x01",
            "教会一般都是这么说的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #309
        0x101,
        (
            "#1007F#5P唔唔……\x01",
            "就是迷途的灵魂吧。\x02\x03",

            "#1015F但是，说它不普通\x01",
            "又是怎么回事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x109,
        (
            "#1063F普通的灵，大多数\x01",
            "都是被什么所束缚。\x02\x03",

            "或者是地方，或者是人。\x02\x03",

            "但是，这次的幽灵骚动\x01",
            "好像两者都不是。\x02\x03",

            "因此教区长\x01",
            "也束手无策啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x101,
        "#1002F#5P原来如此……这么回事啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x109,
        (
            "#1062F嗯，就作为\x01",
            "调查的参考吧。\x02\x03",

            "#1061F那么，我回教会了。\x02\x03",

            "再见～艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)

    def lambda_4C1D():
        OP_8E(0x109, 0x6356, 0x41A, 0x19262, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4C1D)

    def lambda_4C38():
        OP_6D(25620, 0, 112450, 1500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4C38)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)

    def lambda_4C5A():
        OP_6D(25470, 0, 115430, 1000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4C5A)
    WaitChrThread(0x109, 0x2)

    ChrTalk(    #313
        0x101,
        (
            "#1025F#5P嗯～刚才那番话倒\x01",
            "挺像个神职者的……\x02\x03",

            "但还是怎样看\x01",
            "也不像是个神父啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4D33")

    ChrTalk(    #314
        0x106,
        (
            "#051F#3P嗯，巡回神父\x01",
            "多数都是些怪家伙。\x02\x03",

            "从前来拉文努村的巡回神父\x01",
            "也是个很奇怪的大叔呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DA3")

    label("loc_4D33")


    ChrTalk(    #315
        0x103,
        (
            "#021F#3P呵呵，巡回神父\x01",
            "好像不少人都挺奇怪的。\x02\x03",

            "#020F我在剧团的时候就\x01",
            "有个不知为何随同旅行的\x01",
            "奇怪巡回修女。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DA3")

    TurnDirection(0x101, 0xF7, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 3)), scpexpr(EXPR_END)), "loc_4E1F")
    OP_28(0x82, 0x1, 0x400)

    ChrTalk(    #316
        0x101,
        (
            "#1016F#2P嗯～这样啊。\x02\x03",

            "#1006F好了……\x01",
            "嘉恩哥哥那需要我们收集\x01",
            "的目击情报都齐了吧。\x02\x03",

            "先回协会吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E7F")

    label("loc_4E1F")


    ChrTalk(    #317
        0x101,
        (
            "#1016F#2P嗯～这样啊。\x02\x03",

            "#1006F好了……\x01",
            "还有没收集到的目击情报吧。\x02\x03",

            "照这个势头去找下一个吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4EA3")

    ChrTalk(    #318
        0x106,
        "#051F#3P啊啊，是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EBD")

    label("loc_4EA3")


    ChrTalk(    #319
        0x103,
        "#020F#3P嗯嗯，是呢。\x02",
    )

    CloseMessageWindow()

    label("loc_4EBD")

    OP_59()
    OP_B7(0x8)
    RemoveParty(0x8, 0xFF)
    OP_A2(0x121B)
    EventEnd(0x0)
    Return()

    # Function_30_45A2 end

    def Function_31_4EC9(): pass

    label("Function_31_4EC9")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x1F, 0x40)
    SetChrFlags(0x20, 0x40)
    SetChrFlags(0x21, 0x40)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x10, 0x200)
    SetChrFlags(0x11, 0x200)
    SetChrFlags(0x12, 0x200)
    SetChrFlags(0x13, 0x200)
    SetChrFlags(0x14, 0x200)
    SetChrFlags(0x15, 0x200)
    SetChrFlags(0x16, 0x200)
    SetChrFlags(0x17, 0x200)
    SetChrFlags(0x18, 0x200)
    SetChrFlags(0x19, 0x200)
    SetChrFlags(0x1A, 0x200)
    SetChrFlags(0x1B, 0x200)
    SetChrFlags(0x1C, 0x200)
    SetChrFlags(0x1D, 0x200)
    SetChrFlags(0x1E, 0x200)
    SetChrFlags(0x1F, 0x200)
    SetChrFlags(0x20, 0x200)
    SetChrFlags(0x21, 0x200)
    SetChrFlags(0x22, 0x200)
    SetChrPos(0x8, 50530, 500, 56000, 180)
    SetChrPos(0x9, 49520, 500, 56510, 180)
    SetChrChipByIndex(0x9, 25)
    SetChrPos(0xA, 51000, 500, 53200, 180)
    SetChrPos(0xB, 52000, 500, 53900, 180)
    SetChrPos(0xC, 50000, 500, 53900, 180)
    SetChrPos(0xD, 51000, 500, 50900, 0)
    SetChrPos(0xE, 52000, 500, 50200, 0)
    SetChrPos(0xF, 50000, 500, 50200, 0)
    SetChrPos(0x10, 52430, 500, 57380, 180)
    SetChrPos(0x12, 51660, 500, 58000, 180)
    SetChrPos(0x13, 50430, 500, 58170, 180)
    SetChrPos(0x11, 51470, 500, 56000, 180)
    SetChrPos(0x15, 49980, 500, 58910, 180)
    SetChrPos(0x18, 51100, 500, 58910, 180)
    SetChrPos(0x16, 52320, 500, 58610, 180)
    SetChrPos(0x14, 49520, 500, 59500, 180)
    SetChrPos(0x19, 49520, 500, 57540, 180)
    SetChrPos(0x17, 52480, 500, 56280, 180)
    SetChrPos(0x1A, 52460, 500, 48150, 0)
    SetChrPos(0x1C, 51560, 500, 48150, 0)
    SetChrPos(0x1D, 50340, 500, 48330, 0)
    SetChrPos(0x21, 49530, 500, 48350, 0)
    SetChrPos(0x1B, 51920, 500, 47190, 0)
    SetChrPos(0x20, 50310, 500, 47010, 0)
    SetChrPos(0x1F, 49520, 500, 47190, 0)
    SetChrPos(0x22, 50900, 500, 46310, 0)
    SetChrPos(0x1E, 52460, 500, 46310, 0)
    OP_43(0x8, 0x1, 0x0, 0x2)
    OP_43(0x9, 0x1, 0x0, 0x2)
    OP_43(0x10, 0x1, 0x0, 0x2)
    OP_43(0x12, 0x1, 0x0, 0x2)
    OP_43(0x13, 0x1, 0x0, 0x2)
    OP_43(0x11, 0x1, 0x0, 0x2)
    OP_43(0x15, 0x1, 0x0, 0x2)
    OP_43(0x18, 0x1, 0x0, 0x2)
    OP_43(0x16, 0x1, 0x0, 0x2)
    OP_43(0x14, 0x1, 0x0, 0x2)
    OP_43(0x19, 0x1, 0x0, 0x2)
    OP_43(0x17, 0x1, 0x0, 0x2)
    OP_43(0x1A, 0x1, 0x0, 0x2)
    OP_43(0x1C, 0x1, 0x0, 0x2)
    OP_43(0x1D, 0x1, 0x0, 0x2)
    OP_43(0x21, 0x1, 0x0, 0x2)
    OP_43(0x1B, 0x1, 0x0, 0x2)
    OP_43(0x20, 0x1, 0x0, 0x2)
    OP_43(0x1F, 0x1, 0x0, 0x2)
    OP_43(0x22, 0x1, 0x0, 0x2)
    OP_43(0x1E, 0x1, 0x0, 0x2)
    Return()

    # Function_31_4EC9 end

    def Function_32_529A(): pass

    label("Function_32_529A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_52A7")
    Return()

    label("loc_52A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52B8")
    Call(0, 53)

    label("loc_52B8")

    EventBegin(0x0)
    Fade(500)
    OP_6D(51260, 0, 69660, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 51710, 0, 69900, 180)
    SetChrPos(0xF7, 50470, 0, 70110, 180)
    OP_0D()
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    SetChrPos(0xF, 49710, 500, 50290, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1500)
    Fade(1000)
    AddParty(0x3, 0xF8, 0xFF)
    OP_31(0x3, 0x0, 0x29)
    OP_31(0x3, 0xFE, 0x0)
    OP_41(0x3, 0x61, 0xFF)
    OP_41(0x3, 0xFF, 0xFF)
    OP_41(0x3, 0x120, 0xFF)
    OP_41(0x3, 0x25C, 0x0)
    OP_41(0x3, 0x276, 0x1)
    OP_41(0x3, 0x26A, 0x2)
    OP_41(0x3, 0x261, 0x3)
    OP_35(0x3, 0x0)
    OP_35(0x3, 0x8C)
    OP_BB(0x3, 0x6, 0xF5)
    ClearMapFlags(0x1)
    ClearMapFlags(0x10)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0xF7, 0x40)
    SetChrPos(0x101, 51880, 0, 66000, 180)
    SetChrPos(0xF7, 50550, 0, 66000, 180)
    OP_6D(51370, 500, 44910, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4620, 0)
    OP_6C(51000, 0)
    OP_6E(262, 0)

    def lambda_5412():
        OP_6D(51130, 500, 57140, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5412)
    Sleep(300)

    def lambda_542F():
        OP_67(0, 8000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_542F)

    def lambda_5447():
        OP_8E(0xFE, 0xC9C2, 0x1F4, 0xEF42, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5447)
    Sleep(300)

    def lambda_5467():
        OP_8E(0xFE, 0xC454, 0x1F4, 0xEFBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_5467)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0xF7, 0x0)
    Fade(1000)
    OP_6D(51380, 500, 52340, 0)
    OP_67(0, 4980, -10000, 0)
    OP_6B(3650, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #320
        0xC,
        "#5P别装傻了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xC,
        (
            "#5P酒店出现的幽灵\x01",
            "肯定是你们搞的鬼，\x01",
            "我们已经知道了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0xB,
        (
            "#5P诺曼先生的儿子\x01",
            "也因受惊而昏过去了哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xB,
        "#5P不觉得太过分了吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xF,
        (
            "#6P哼，那小子不是\x01",
            "渡鸦帮的不良少年吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xF,
        (
            "#6P那种不正经的人说的话\x01",
            "能信吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xA,
        "#5P……等一下。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xA,
        (
            "#5P要是批判我个人那还好说，\x01",
            "攻击家人太卑鄙了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xA,
        (
            "#5P那不正经这类的说法\x01",
            "能不能收回呢～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xD,
        (
            "#5P嗯～确实那句\x01",
            "可能说得过分了点。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 400)

    ChrTalk(    #330
        0xE,
        (
            "#2P我说主任！\x01",
            "别就这么认了吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xE,
        (
            "#2P就因为你这么软弱\x01",
            "才会让旅游推进派得势的！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xB, 400)

    ChrTalk(    #332
        0xC,
        "#5P你、你说什么～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xB,
        (
            "#5P得势的不是\x01",
            "你们港湾维持派吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xB,
        (
            "#5P还用幽灵骚动这种诡计，\x01",
            "让人感到恶心！\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x101, 0x7D0)

    ChrTalk(    #335
        0x101,
        (
            "#1007F#5P糟糕……\x01",
            "吵架升温了呢。\x02\x03",

            "#1002F是不是去阻止比较好？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_57EA")

    ChrTalk(    #336
        0x106,
        (
            "#050F#1P好像还没打起来，\x01",
            "可能还早了点……\x02\x03",

            "不过，一旦打起来的话\x01",
            "就马上移动到\x01",
            "能够阻止的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5851")

    label("loc_57EA")


    ChrTalk(    #337
        0x103,
        (
            "#022F#1P还没开始打架，\x01",
            "现在出面可能早了点。\x02\x03",

            "但是，一旦打起来的话\x01",
            "就马上移动到\x01",
            "能够阻止的地方吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5851")


    ChrTalk(    #338
        0x101,
        (
            "#1007F#5P话虽如此，围观的人太多\x01",
            "完全无法前进了啊……\x02\x03",

            "#1019F真是的，奈尔他们\x01",
            "竟然抢了前面的位置。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_58BE():
        OP_6D(51380, 500, 52340, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_58BE)
    OP_62(0xE, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(500)
    Sleep(100)
    OP_62(0xF, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(500)
    OP_62(0xC, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(500)
    OP_62(0xB, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(500)
    OP_62(0xF, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #339
        0xF,
        "#6P不能忍了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xE,
        (
            "#2P像你这么弱不禁风的家伙\x01",
            "比腕力别想赢！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #341
        0xC,
        (
            "#5P求、求之不得！\x01",
            "怕你不成！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xB,
        (
            "#5P诺曼先生的名誉\x01",
            "由我们诺曼商会员来守护！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 300, 500)
    Sleep(300)
    OP_8C(0xA, 49, 500)
    Sleep(300)

    ChrTalk(    #343
        0xA,
        (
            "#6P你们快住手！\x01",
            "暴力是不行的，不行！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 124, 500)
    Sleep(300)
    OP_8C(0xD, 213, 500)
    Sleep(300)

    ChrTalk(    #344
        0xD,
        (
            "#5P大家稳住！\x01",
            "现在应该冷静协商……\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x101, 0x5DC)

    ChrTalk(    #345
        0x101,
        "#1005F#5P（糟了……！）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5AE2")

    ChrTalk(    #346
        0x106,
        "#552F#1P（……阻止不了吗。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B08")

    label("loc_5AE2")


    ChrTalk(    #347
        0x103,
        "#025F#1P（这下阻止不了了啊……）\x02",
    )

    CloseMessageWindow()

    label("loc_5B08")

    OP_1F(0x0, 0x190)
    Sleep(400)
    OP_20(0x0)
    OP_22(0xBE, 0x0, 0x64)
    Sleep(1000)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_4A(0x17, 255)
    OP_4A(0x18, 255)
    OP_4A(0x19, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    OP_4A(0x1F, 255)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    OP_4A(0x22, 255)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x19, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x17, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x20, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x1F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x21, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x19, 0x2)
    OP_71(0x19, 0x20)
    OP_71(0x19, 0x40)
    OP_6F(0x19, 301)
    OP_70(0x19, 0x168)
    OP_A1(0x33, 0x19)
    SetChrFlags(0x33, 0x40)
    SetChrPos(0x33, 30000, -2800, 52100, 90)
    OP_8C(0x33, 270, 0)
    OP_89(0x104, 30500, -2500, 52100, 90)
    SetChrChipByIndex(0x104, 27)
    SetChrSubChip(0x104, 0)

    NpcTalk(    #348
        0x104,
        "青年的声音",
        (
            "呼……\x01",
            "真是可悲。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(1000)
    OP_6D(40290, 500, 51970, 0)
    OP_67(0, 7050, -10000, 0)
    OP_6B(3320, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    OP_43(0x33, 0x0, 0x0, 0x21)

    def lambda_5E99():
        OP_6D(47120, 500, 52000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5E99)

    def lambda_5EB1():
        OP_6C(270000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_5EB1)
    OP_0D()

    def lambda_5EC2():

        label("loc_5EC2")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5EC2")

    QueueWorkItem2(0x101, 1, lambda_5EC2)

    def lambda_5ED3():

        label("loc_5ED3")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5ED3")

    QueueWorkItem2(0xF7, 1, lambda_5ED3)

    def lambda_5EE4():

        label("loc_5EE4")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5EE4")

    QueueWorkItem2(0x8, 1, lambda_5EE4)
    Sleep(50)

    def lambda_5EFA():

        label("loc_5EFA")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5EFA")

    QueueWorkItem2(0x9, 1, lambda_5EFA)

    def lambda_5F0B():

        label("loc_5F0B")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5F0B")

    QueueWorkItem2(0xA, 1, lambda_5F0B)

    def lambda_5F1C():

        label("loc_5F1C")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5F1C")

    QueueWorkItem2(0xB, 1, lambda_5F1C)
    Sleep(50)

    def lambda_5F32():

        label("loc_5F32")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5F32")

    QueueWorkItem2(0xC, 1, lambda_5F32)

    def lambda_5F43():

        label("loc_5F43")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5F43")

    QueueWorkItem2(0xD, 1, lambda_5F43)

    def lambda_5F54():

        label("loc_5F54")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5F54")

    QueueWorkItem2(0xE, 1, lambda_5F54)

    def lambda_5F65():

        label("loc_5F65")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5F65")

    QueueWorkItem2(0xF, 1, lambda_5F65)
    Sleep(50)

    def lambda_5F7B():

        label("loc_5F7B")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5F7B")

    QueueWorkItem2(0x10, 1, lambda_5F7B)

    def lambda_5F8C():

        label("loc_5F8C")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5F8C")

    QueueWorkItem2(0x11, 1, lambda_5F8C)

    def lambda_5F9D():

        label("loc_5F9D")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5F9D")

    QueueWorkItem2(0x12, 1, lambda_5F9D)
    Sleep(50)

    def lambda_5FB3():

        label("loc_5FB3")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5FB3")

    QueueWorkItem2(0x13, 1, lambda_5FB3)

    def lambda_5FC4():

        label("loc_5FC4")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5FC4")

    QueueWorkItem2(0x14, 1, lambda_5FC4)

    def lambda_5FD5():

        label("loc_5FD5")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5FD5")

    QueueWorkItem2(0x15, 1, lambda_5FD5)
    Sleep(50)

    def lambda_5FEB():

        label("loc_5FEB")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5FEB")

    QueueWorkItem2(0x16, 1, lambda_5FEB)

    def lambda_5FFC():

        label("loc_5FFC")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_5FFC")

    QueueWorkItem2(0x17, 1, lambda_5FFC)

    def lambda_600D():

        label("loc_600D")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_600D")

    QueueWorkItem2(0x18, 1, lambda_600D)

    def lambda_601E():

        label("loc_601E")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_601E")

    QueueWorkItem2(0x19, 1, lambda_601E)
    Sleep(50)

    def lambda_6034():

        label("loc_6034")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_6034")

    QueueWorkItem2(0x1A, 1, lambda_6034)

    def lambda_6045():

        label("loc_6045")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_6045")

    QueueWorkItem2(0x1B, 1, lambda_6045)

    def lambda_6056():

        label("loc_6056")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_6056")

    QueueWorkItem2(0x1C, 1, lambda_6056)
    Sleep(50)

    def lambda_606C():

        label("loc_606C")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_606C")

    QueueWorkItem2(0x1D, 1, lambda_606C)

    def lambda_607D():

        label("loc_607D")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_607D")

    QueueWorkItem2(0x1E, 1, lambda_607D)

    def lambda_608E():

        label("loc_608E")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_608E")

    QueueWorkItem2(0x1F, 1, lambda_608E)
    Sleep(50)

    def lambda_60A4():

        label("loc_60A4")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_60A4")

    QueueWorkItem2(0x20, 1, lambda_60A4)

    def lambda_60B5():

        label("loc_60B5")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_60B5")

    QueueWorkItem2(0x21, 1, lambda_60B5)

    def lambda_60C6():

        label("loc_60C6")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_60C6")

    QueueWorkItem2(0x22, 1, lambda_60C6)
    WaitChrThread(0x33, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0xF7, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_44(0x1C, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    OP_44(0x1F, 0xFF)
    OP_44(0x20, 0xFF)
    OP_44(0x21, 0xFF)
    OP_44(0x22, 0xFF)
    Sleep(500)

    NpcTalk(    #349
        0x104,
        "金发的青年",
        (
            "#035F纷争无法蕴育任何东西……\x01",
            "只是产生空虚的裂缝。\x02\x03",

            "#030F让我为这样的你们，献上一曲。\x02\x03",

            "越过心中的鸿沟\x01",
            "让彼此携起手来\x01",
            "温柔而伤感的歌……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Sleep(1000)
    OP_1D(0x47)
    OP_43(0x104, 0x0, 0x0, 0x2)
    Sleep(1000)

    NpcTalk(    #350 op#A op#5
        0x104,
        "金发的青年",
        "#70A#035F阳光映照　虹彩之桥\x05\x02",
    )

    Sleep(7000)

    NpcTalk(    #351 op#A op#5
        0x104,
        "金发的青年",
        "#70A#035F跨越通往　你的去向……\x05\x02",
    )

    Sleep(7000)

    NpcTalk(    #352 op#A op#5
        0x104,
        "金发的青年",
        "#70A#035F有心追求 却消溶于空\x05\x02",
    )

    Sleep(7000)

    NpcTalk(    #353 op#A op#5
        0x104,
        "金发的青年",
        "#70A#035F寂寞来袭 听浅风低吟……\x05\x02",
    )

    Sleep(7000)

    NpcTalk(    #354 op#A op#5
        0x104,
        "金发的青年",
        "#70A#032F若无法传达 这份心愿\x05\x02",
    )

    Sleep(7500)

    NpcTalk(    #355 op#A op#5
        0x104,
        "金发的青年",
        "#70A#032F至少请留下 一道浅伤……\x05\x02",
    )

    Sleep(7500)

    NpcTalk(    #356 op#A op#5
        0x104,
        "金发的青年",
        "#70A#032F最初之约 未能守护\x05\x02",
    )

    Sleep(7500)

    NpcTalk(    #357 op#A op#5
        0x104,
        "金发的青年",
        "#70A#035F你的气息 化作琥珀\x05\x02",
    )

    Sleep(7500)

    NpcTalk(    #358 op#A op#5
        0x104,
        "金发的青年",
        "#70A#035F这份梦境 永远封存……\x05\x02",
    )

    OP_21()
    Sleep(300)
    OP_4A(0x104, 255)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 28)
    SetChrSubChip(0x104, 0)
    OP_0D()
    OP_99(0x104, 0x0, 0x3, 0x5DC)
    Sleep(300)
    OP_99(0x104, 0x3, 0xA, 0x3E8)
    Sleep(500)

    ChrTalk(    #359
        0x104,
        (
            "#035F呼……\x01",
            "大家都感觉得到吧。\x02\x03",

            "唯一的真实……\x01",
            "那就是爱的永恒。\x02\x03",

            "#030F用现代的话来说，\x01",
            "就是Ｌｏｖｅ·ｉｓ·ｅｔｅｒｎａｌ。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x89, 0x0, 0x64)
    OP_62(0x104, 0x12C, 1900, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x104)
    OP_1D(0xC)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x15, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x20, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1F, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x14, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x21, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_51(0x34, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x34, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x34, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x34, 0x5DC)

    ChrTalk(    #360
        0xA,
        "#5P唔、唔咳……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xD, 400)

    ChrTalk(    #361
        0xA,
        "#2P总而言之，波尔多斯先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xA,
        (
            "#2P现在还是双方都\x01",
            "冷静一下头脑比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xA, 400)

    ChrTalk(    #363
        0xD,
        (
            "#1P嗯嗯，是啊。\x01",
            "也妨碍大桥的通行了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 180, 400)

    ChrTalk(    #364
        0xD,
        "#2P各位，暂时回港口吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xD, 400)

    ChrTalk(    #365
        0xF,
        "#1P是、是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xC,
        (
            "#2P是啊……\x01",
            "还得发传单呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xA, 0x1, 0x0, 0x22)
    OP_43(0xB, 0x1, 0x0, 0x22)
    OP_43(0xC, 0x1, 0x0, 0x22)
    Sleep(50)
    OP_43(0x10, 0x1, 0x0, 0x22)
    OP_43(0x11, 0x1, 0x0, 0x22)
    OP_43(0x12, 0x1, 0x0, 0x22)
    Sleep(50)
    OP_43(0x13, 0x1, 0x0, 0x22)
    OP_43(0x14, 0x1, 0x0, 0x22)
    OP_43(0x15, 0x1, 0x0, 0x22)
    Sleep(50)
    OP_43(0x16, 0x1, 0x0, 0x22)
    OP_43(0x17, 0x1, 0x0, 0x22)
    OP_43(0x18, 0x1, 0x0, 0x22)
    OP_43(0x19, 0x1, 0x0, 0x22)
    OP_43(0xD, 0x1, 0x0, 0x23)
    OP_43(0xE, 0x1, 0x0, 0x23)
    OP_43(0xF, 0x1, 0x0, 0x23)
    Sleep(50)
    OP_43(0x1A, 0x1, 0x0, 0x23)
    OP_43(0x1B, 0x1, 0x0, 0x23)
    OP_43(0x1C, 0x1, 0x0, 0x23)
    Sleep(50)
    OP_43(0x1D, 0x1, 0x0, 0x23)
    OP_43(0x1E, 0x1, 0x0, 0x23)
    OP_43(0x1F, 0x1, 0x0, 0x23)
    Sleep(50)
    OP_43(0x20, 0x1, 0x0, 0x23)
    OP_43(0x21, 0x1, 0x0, 0x23)
    OP_43(0x22, 0x1, 0x0, 0x23)

    def lambda_696A():
        OP_8E(0xFE, 0xCA94, 0x1F4, 0xE254, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_696A)

    def lambda_6985():
        OP_8E(0xFE, 0xC468, 0x1F4, 0xE0F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_6985)

    def lambda_69A0():
        OP_8E(0xFE, 0xC15C, 0x1F4, 0xD39A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_69A0)

    def lambda_69BB():
        OP_6D(49500, 500, 55540, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_69BB)

    def lambda_69D3():
        OP_67(0, 7640, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_69D3)

    def lambda_69EB():
        OP_6B(3330, 3000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_69EB)
    WaitChrThread(0x9, 0x1)
    TurnDirection(0x9, 0x104, 400)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF7, 0x2)

    ChrTalk(    #367
        0x101,
        "#1019F（大、大家都走了……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6A60")

    ChrTalk(    #368
        0x106,
        "#551F#5P（……我算是明白了。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A8A")

    label("loc_6A60")


    ChrTalk(    #369
        0x103,
        (
            "#025F#5P（唉……\x01",
            "  又是这样收场啊。)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6A8A")


    ChrTalk(    #370
        0x104,
        (
            "#035F呼，对于任何国家来说，\x01",
            "都有一个相同之处，\x01",
            "就是民众们那容易发热又能快速冷静下来的头脑。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    TurnDirection(0xF7, 0x104, 400)
    Sleep(200)

    ChrTalk(    #371
        0x104,
        (
            "#033F不，真正恐怖的\x01",
            "是这让人们恢复平常心…\x01",
            "仿如奇迹般的旋律吗……\x02\x03",

            "#031F来吧诸位记者。\x01",
            "请尽情拍照\x01",
            "采访吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x9,
        (
            "#150F#6P哇～可以吗。\x01",
            "那么就不客气了。\x02\x03",

            "#151F来，茄～～子㈱\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 26)
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sleep(500)

    ChrTalk(    #373
        0x104,
        "#035F嗯～太棒了。\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0x104, 3)
    OP_0D()
    Sleep(250)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x104, 4)
    OP_0D()
    OP_8F(0x9, 0xC15C, 0x1F4, 0xC9EA, 0xBB8, 0x0)
    TurnDirection(0x9, 0x104, 400)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x104, 7)
    OP_0D()
    OP_8F(0x9, 0xC15C, 0x1F4, 0xCF80, 0xBB8, 0x0)
    TurnDirection(0x9, 0x104, 400)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Fade(250)
    SetChrSubChip(0x104, 10)
    OP_0D()
    OP_8F(0x9, 0xC15C, 0x1F4, 0xCB2A, 0xBB8, 0x0)
    TurnDirection(0x9, 0x104, 400)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    TurnDirection(0x8, 0x101, 400)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0xF7, 0x8, 400)

    ChrTalk(    #374
        0x8,
        (
            "#145F#5P唔～那个……\x02\x03",

            "#141F刚才的事\x01",
            "能说给我听吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x101,
        (
            "#1016F嗯、嗯，好。\x02\x03",

            "先回协会说吧，不赶快报告的话\x01",
            "感觉要忘了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6E65")

    ChrTalk(    #376
        0x106,
        (
            "#051F#5P赶快回协会\x01",
            "去向嘉恩报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6E92")

    label("loc_6E65")


    ChrTalk(    #377
        0x103,
        (
            "#021F#5P赶快回协会\x01",
            "去向嘉恩先生报告吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E92")

    OP_43(0x101, 0x1, 0x0, 0x22)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x22)
    Sleep(500)
    OP_43(0x8, 0x1, 0x0, 0x22)
    Sleep(500)
    OP_69(0x104, 0x7D0)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 65535)
    SetChrSubChip(0x104, 0)
    TurnDirection(0x104, 0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #378
        0x104,
        (
            "#033F哎呀……\x02\x03",

            "我说，艾丝蒂尔。\x01",
            "打算去哪里呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x104, 0xA2E4, 0xFFFFF4B6, 0xCB5C, 0x7D0, 0x0)
    TurnDirection(0x104, 0x101, 400)
    Sleep(500)

    ChrTalk(    #379
        0x104,
        (
            "#036F#5P等、等一下！\x01",
            "不，请等一下！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0x9,
        (
            "#151F#6P哇哇，表情真好～！\x02\x03",

            "好可爱哟～㈱\x02",
        )
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x9, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2120   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_32_529A end

    def Function_33_7027(): pass

    label("Function_33_7027")

    LoadEffect(0x1, "map\\\\mp013_00.eff")
    LoadEffect(0x2, "map\\\\mp013_02.eff")
    PlayEffect(0x1, 0x1, 0x33, 0, -100, 2000, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)

    def lambda_708A():
        OP_8F(0xFE, 0x9E34, 0xFFFFF510, 0xCB16, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_708A)
    Sleep(2000)

    def lambda_70AA():
        OP_8F(0xFE, 0x9E34, 0xFFFFF510, 0xCB16, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_70AA)
    Sleep(1200)

    def lambda_70CA():
        OP_8F(0xFE, 0x9E34, 0xFFFFF510, 0xCB16, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_70CA)
    Sleep(500)

    def lambda_70EA():
        OP_8F(0xFE, 0x9E34, 0xFFFFF510, 0xCB16, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_70EA)
    WaitChrThread(0x33, 0x1)
    OP_82(0x1, 0x2)
    PlayEffect(0x2, 0xFF, 0x33, 0, -200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_33_7027 end

    def Function_34_713D(): pass

    label("Function_34_713D")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xC738, 0x0, 0x102AC, 0x7D0, 0x0)
    Return()

    # Function_34_713D end

    def Function_35_7159(): pass

    label("Function_35_7159")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xC738, 0x0, 0x9858, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_35_7159 end

    def Function_36_717A(): pass

    label("Function_36_717A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_718B")
    Call(0, 53)

    label("loc_718B")

    EventBegin(0x0)
    AddParty(0x26, 0xFF, 0xFF)
    ClearChrFlags(0x127, 0x80)
    SetChrFlags(0x127, 0x40)
    SetChrFlags(0x104, 0x8)
    SetChrPos(0x101, 45070, 500, 91500, 180)
    SetChrPos(0xF7, 45070, 500, 91500, 180)
    SetChrPos(0x127, 45070, 500, 91500, 180)
    SetChrPos(0x104, 45070, 500, 91500, 180)
    OP_6D(45200, 0, 86800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x5, 0)
    OP_70(0x5, 0x1D)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x0, 0x25)
    OP_43(0xF7, 0x1, 0x0, 0x26)
    OP_43(0x127, 0x1, 0x0, 0x27)
    OP_43(0x104, 0x1, 0x0, 0x28)
    Sleep(3800)
    OP_6F(0x5, 29)
    OP_70(0x5, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x104, 0x1)

    ChrTalk(    #381
        0x101,
        (
            "#1007F#6P……怎么说呢～\x01",
            "事到如今再叹气也没什么意义了。\x02\x03",

            "#1011F奥利维尔你果然跟来了啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x104,
        (
            "#031F#2P哈哈哈。\x01",
            "真讨厌，艾丝蒂尔。\x02\x03",

            "这不是和鸟在天空飞，鱼在水中游\x01",
            "一样理所当然的事吗～？\x02\x03",

            "#030F你以为我是为了什么才肯舍弃那美妙的温泉，\x01",
            "从亚尔摩来到这里的啊？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_75A2")

    ChrTalk(    #383
        0x101,
        (
            "#1015F#6P嗯……\x02\x03",

            "对了，阿加特。\x01",
            "可以让他加入吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x106,
        (
            "#551F#1P随他便了……\x02\x03",

            "#552F不过，我可还没有\x01",
            "完全信任你。\x02\x03",

            "如果做出奇怪的举动，\x01",
            "别怪我不客气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x104,
        (
            "#034F#2P呼，那真遗憾。\x02\x03",

            "本来觉得像你这样\x01",
            "粗旷豪放的类型也不错的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0x106,
        "#055F#1P啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x104,
        (
            "#037F#2P呼，放心吧。\x02\x03",

            "在争取到你的信赖之前\x01",
            "我会控制追求的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x106,
        "#055F#1P……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #389
        0x106,
        (
            "#054F#1P#3S白痴！\x01",
            "说什么乱七八糟的！！？？\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x127, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #390
        0x127,
        (
            "#153F#6P啊哇哇～成熟的魅力\x01",
            "让人心跳不已呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x101,
        (
            "#1007F#6P（暂时把教训他的任务\x01",
            "交给阿加特好了……)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7809")

    label("loc_75A2")


    ChrTalk(    #392
        0x101,
        (
            "#1015F#6P嗯……\x02\x03",

            "对了，雪拉姐。\x01",
            "可以让他加入吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x103,
        (
            "#026F#1P唔，你来帮忙\x01",
            "说实话很感谢……\x02\x03",

            "#027F能不能问一件事？\x02\x03",

            "你现在还在利贝尔这事\x01",
            "卡西乌斯老师知道吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x101,
        "#1004F#6P啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x104,
        (
            "#033F#2P…………………………………\x02\x03",

            "#035F哎呀哎呀，不愧是雪拉。\x01",
            "问的问题一刀见血啊。\x02\x03",

            "#030F回答是Ｙｅｓ。\x01",
            "卡西乌斯先生知道哦。\x02\x03",

            "这样能接受了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x101,
        "#1015F#6P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x103,
        (
            "#021F#1P呵呵，好吧。\x02\x03",

            "#027F既然想帮忙\x01",
            "我们也不客气了。\x02\x03",

            "如果敢乱来\x01",
            "就要你陪我一晚上哦㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x104,
        "#034F#2P我一定诚心诚意，努力奋斗。\x02",
    )

    CloseMessageWindow()
    OP_62(0x127, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #399
        0x127,
        (
            "#151F#6P啊哇哇～成熟的魅力\x01",
            "让人心跳不已呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x101,
        (
            "#1016F#6P（不愧是雪拉姐……\x01",
            "很会使唤奥利维尔。)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7809")

    OP_28(0x82, 0x1, 0x1000)
    OP_28(0x82, 0x1, 0x2000)
    OP_28(0x83, 0x4, 0x2)
    OP_28(0x83, 0x4, 0x8)
    OP_28(0x83, 0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_36_717A end

    def Function_37_7828(): pass

    label("Function_37_7828")

    OP_8E(0xFE, 0xB180, 0x0, 0x14AF0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_37_7828 end

    def Function_38_7844(): pass

    label("Function_38_7844")

    Sleep(1000)
    OP_8E(0xFE, 0xB036, 0x0, 0x1561C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xADC0, 0x0, 0x14F50, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_38_7844 end

    def Function_39_7879(): pass

    label("Function_39_7879")

    Sleep(1800)
    OP_8E(0xFE, 0xB036, 0x0, 0x1561C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB3F6, 0x0, 0x14E4C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_39_7879 end

    def Function_40_78AE(): pass

    label("Function_40_78AE")

    Sleep(3000)
    ClearChrFlags(0x104, 0x8)
    OP_8E(0xFE, 0xB054, 0x0, 0x1564E, 0x7D0, 0x0)
    Return()

    # Function_40_78AE end

    def Function_41_78CD(): pass

    label("Function_41_78CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7974")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_791E")
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #401
        0x106,
        (
            "#050F……没空出去了。\x01",
            "赶紧去伦格兰德大桥吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7959")

    label("loc_791E")

    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #402
        0x103,
        (
            "#020F……没空出去了呢。\x01",
            "赶紧去伦格兰德大桥吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7959")

    OP_90(0x0, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BE9")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 6)), scpexpr(EXPR_END)), "loc_7AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7A1B")
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #403
        0x106,
        (
            "#050F还没找贝尔夫那家伙\x01",
            "问亡灵的事呢。\x02\x03",

            "要出城的话先去问问再说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #404
        0x101,
        (
            "#1007F啊，是喔。\x02\x03",

            "#1006F是市长官邸右边的房子吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AA9")

    label("loc_7A1B")

    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #405
        0x103,
        (
            "#020F还没找叫贝尔夫的孩子\x01",
            "问白影的事呢。\x02\x03",

            "要出城的话先去问问再说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #406
        0x101,
        (
            "#1007F啊，是喔。\x02\x03",

            "#1006F是市长官邸右边的房子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AA9")

    Jump("loc_7BCE")

    label("loc_7AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7B42")
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #407
        0x106,
        (
            "#050F还没找渡鸦帮那些小子\x01",
            "问亡灵的事呢。\x02\x03",

            "要出城的话先去问问再说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #408
        0x101,
        (
            "#1007F啊，是喔。\x02\x03",

            "#1006F要先去港口的仓库才是。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7BCE")

    label("loc_7B42")

    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #409
        0x103,
        (
            "#020F还没找渡鸦帮的小子们\x01",
            "问白影的事呢。\x02\x03",

            "要出城的话先去问问再说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #410
        0x101,
        (
            "#1007F啊，是喔。\x02\x03",

            "#1006F要先去港口的仓库才是。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BCE")

    OP_90(0x0, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7BE9")

    Return()

    # Function_41_78CD end

    def Function_42_7BEA(): pass

    label("Function_42_7BEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C7B")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7C31")
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #411
        0x106,
        (
            "#050F没空绕道了。\x01",
            "赶紧去桥那边吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C60")

    label("loc_7C31")

    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #412
        0x103,
        (
            "#020F没空绕道了。\x01",
            "赶紧去桥那边吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C60")

    OP_90(0x0, 0xFFFFF830, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_7C7B")

    Return()

    # Function_42_7BEA end

    def Function_43_7C7C(): pass

    label("Function_43_7C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C8D")
    Call(0, 53)

    label("loc_7C8D")

    EventBegin(0x0)
    OP_6D(44890, 0, 88850, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 44960, 0, 92120, 180)
    SetChrPos(0xF7, 44960, 0, 93120, 180)
    SetChrPos(0x105, 44960, 0, 94120, 180)
    SetChrPos(0x104, 44960, 0, 95120, 180)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(1500, 0)
    OP_0D()
    OP_6F(0x5, 0)
    OP_70(0x5, 0x1D)
    OP_73(0x5)
    Sleep(500)

    def lambda_7D71():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D71)
    Sleep(100)

    def lambda_7D91():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7D91)
    Sleep(100)

    def lambda_7DB1():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7DB1)

    def lambda_7DCC():
        OP_6D(44470, 0, 84530, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7DCC)
    Sleep(200)

    def lambda_7DE9():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7DE9)
    Sleep(2700)
    OP_6F(0x5, 29)
    OP_70(0x5, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)

    def lambda_7E24():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E24)

    def lambda_7E3F():
        OP_90(0xFE, 0xFFFFFC18, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7E3F)

    def lambda_7E5A():
        OP_90(0xFE, 0x3E8, 0x0, 0xFFFFF63C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E5A)

    def lambda_7E75():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7E75)
    WaitChrThread(0x101, 0x1)

    def lambda_7E95():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E95)
    WaitChrThread(0xF7, 0x1)
    OP_8C(0xF7, 90, 400)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 270, 400)

    ChrTalk(    #413
        0x101,
        (
            "#1006F#6P好了……\x01",
            "要出发去蔡斯地区了。\x02\x03",

            "准备结束后\x01",
            "就去飞船坪吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7F3D")

    ChrTalk(    #414
        0x106,
        (
            "#051F#5P是啊……\x02\x03",

            "如果没有其他事\x01",
            "最好马上出发吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F74")

    label("loc_7F3D")


    ChrTalk(    #415
        0x103,
        (
            "#020F#5P是啊……\x02\x03",

            "如果没有其他事\x01",
            "最好马上出发呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F74")


    ChrTalk(    #416
        0x104,
        (
            "#033F这么说来朵洛希小姐\x01",
            "在那之后，去了哪里？\x02\x03",

            "好像不知不觉\x01",
            "就不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x101,
        (
            "#1011F#6P啊，好像去酒店\x01",
            "找奈尔了。\x02\x03",

            "如果要离开卢安\x01",
            "最好还是去打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x105,
        (
            "#041F呵呵，是啊。\x02\x03",

            "#542F可以的话还想和院长他们\x01",
            "打个招呼……\x02\x03",

            "可惜之前联络过，似乎有要事\x01",
            "和孩子们一起出去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x101,
        (
            "#1015F#6P这样啊……\x02\x03",

            "#1007F嗯～其实我也想\x01",
            "临走前看看他们的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8118")

    ChrTalk(    #420
        0x106,
        (
            "#051F#5P嗯，到蔡斯\x01",
            "再写信吧。\x02\x03",

            "实在不行也没事的，\x01",
            "反正很快就会回来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_816C")

    label("loc_8118")


    ChrTalk(    #421
        0x103,
        (
            "#021F#5P嗯，到了蔡斯\x01",
            "再写信不就好了。\x02\x03",

            "实在不行也没事的，\x01",
            "反正很快就会回来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_816C")


    ChrTalk(    #422
        0x105,
        "#041F好，就这样吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x101,
        "#1001F#6P我也一起写吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x104,
        (
            "#035F呼……\x01",
            "那么出发吧。\x02\x03",

            "#030F去导力技术的殿堂，\x01",
            "全王国智慧集聚于一地的工房都市。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1400)
    EventEnd(0x0)
    Return()

    # Function_43_7C7C end

    def Function_44_8200(): pass

    label("Function_44_8200")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearMapFlags(0x10)
    OP_6F(0x11, 1500)
    SetChrPos(0x10, 51560, 0, 69340, 180)
    SetChrPos(0x14, 50310, 0, 70350, 180)
    SetChrPos(0x15, 51050, 0, 71430, 180)
    SetChrPos(0x2C, 51850, 0, 73410, 180)
    SetChrPos(0x12, 51850, 1050, 80560, 180)
    SetChrPos(0x16, 59910, 0, 81770, 270)
    SetChrPos(0x13, 39190, 0, 82810, 90)
    SetChrPos(0x18, 37700, 0, 82310, 90)
    OP_4A(0x2C, 255)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_6D(52150, 0, 68780, 0)
    OP_67(0, 8740, -10000, 0)
    OP_6B(4730, 0)
    OP_6C(139000, 0)
    OP_6E(343, 0)
    OP_43(0x12, 0x1, 0x0, 0x2D)
    OP_43(0x16, 0x1, 0x0, 0x2E)
    OP_43(0x13, 0x1, 0x0, 0x2F)
    OP_43(0x18, 0x1, 0x0, 0x30)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x1, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_8353():
        OP_6D(51840, 0, 52250, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8353)

    def lambda_836B():
        OP_67(0, 7140, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_836B)

    def lambda_8383():
        OP_6B(4970, 7000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_8383)

    def lambda_8393():
        OP_6C(113000, 7000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8393)
    OP_6E(431, 7000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T3101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_44_8200 end

    def Function_45_83C3(): pass

    label("Function_45_83C3")

    OP_8E(0xFE, 0xCA94, 0x0, 0x127E6, 0xFA0, 0x0)
    Return()

    # Function_45_83C3 end

    def Function_46_83D8(): pass

    label("Function_46_83D8")

    OP_8E(0xFE, 0xCD78, 0x0, 0x13F60, 0xFA0, 0x0)
    OP_8E(0xFE, 0xCD78, 0x0, 0x11A30, 0xFA0, 0x0)
    Return()

    # Function_46_83D8 end

    def Function_47_8401(): pass

    label("Function_47_8401")

    OP_8E(0xFE, 0xC1C0, 0x0, 0x13A24, 0xFA0, 0x0)
    OP_8E(0xFE, 0xC1C0, 0x0, 0x11CA6, 0xFA0, 0x0)
    Return()

    # Function_47_8401 end

    def Function_48_842A(): pass

    label("Function_48_842A")

    OP_8E(0xFE, 0xC1C0, 0x0, 0x13A24, 0xFA0, 0x0)
    OP_8E(0xFE, 0xC382, 0x0, 0x122BE, 0xFA0, 0x0)
    Return()

    # Function_48_842A end

    def Function_49_8453(): pass

    label("Function_49_8453")

    SetChrPos(0x10, 1310, -2250, 94760, 270)
    SetChrPos(0x11, 1960, -2250, 94550, 270)
    SetChrPos(0x12, 2700, -2250, 94650, 270)
    SetChrPos(0x13, 3410, -2250, 94720, 270)
    SetChrPos(0x14, 4130, -2250, 94610, 270)
    SetChrPos(0x16, 4450, -2250, 95100, 180)
    SetChrPos(0x17, 4460, -2250, 95780, 180)
    SetChrPos(0x18, 4470, -2250, 96560, 180)
    SetChrPos(0x19, 5090, -2250, 96860, 225)
    SetChrPos(0x23, 5880, -2250, 96840, 225)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x2)
    OP_43(0x23, 0x0, 0x0, 0x2)
    Return()

    # Function_49_8453 end

    def Function_50_857D(): pass

    label("Function_50_857D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8594")
    Call(0, 53)
    Call(0, 54)

    label("loc_8594")

    OP_A2(0x2035)
    SetChrPos(0x101, 6140, -2250, 93480, 270)
    SetChrPos(0x102, 6120, -2250, 92390, 270)
    SetChrPos(0xF8, 7260, -2250, 93700, 270)
    SetChrPos(0xF9, 7310, -2250, 92540, 270)
    SetChrPos(0x10, 1310, -2250, 94760, 270)
    SetChrPos(0x11, 1960, -2250, 94550, 270)
    SetChrPos(0x12, 2700, -2250, 94650, 270)
    SetChrPos(0x13, 3410, -2250, 94720, 270)
    SetChrPos(0x14, 4130, -2250, 94610, 270)
    SetChrPos(0x16, 4450, -2250, 95100, 180)
    SetChrPos(0x17, 4460, -2250, 95780, 180)
    SetChrPos(0x18, 4470, -2250, 96560, 180)
    SetChrPos(0x19, 5090, -2250, 96860, 225)
    SetChrPos(0x23, 5880, -2250, 96840, 225)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(2810, -2250, 93730, 0)
    OP_67(0, 6250, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(45000, 0)
    OP_6E(354, 0)
    FadeToBright(1000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_880A")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇绕道去嘉恩那里(修好了卢安支部的通讯器)】\x01",      # 0
            "【◇不绕道(没修好卢安支部的通讯器)】\x01",              # 1
            "【◇不变更】\x01",                                      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_87AB"),
        (1, "loc_87B1"),
        (SWITCH_DEFAULT, "loc_87B7"),
    )


    label("loc_87AB")

    OP_A2(0x2001)
    Jump("loc_87B7")

    label("loc_87B1")

    OP_A3(0x2001)
    Jump("loc_87B7")

    label("loc_87B7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_END)), "loc_87D2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_END)), "loc_87E3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_END)), "loc_87F4")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_87F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_8807")
    OP_A2(0x2091)
    Jump("loc_880A")

    label("loc_8807")

    OP_A3(0x2091)

    label("loc_880A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A4E")
    OP_6D(7470, -2250, 94090, 2000)

    ChrTalk(    #425
        0x101,
        "#1004F#5P这、这怎么了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x102,
        "#1042F#2P好混乱啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_887A():
        OP_6D(7160, -2250, 96060, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_887A)
    TurnDirection(0x23, 0x101, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #427
        0x23,
        (
            "#5P怎么，你们也要\x01",
            "前往对面吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_88C2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_88C2)
    Sleep(100)

    def lambda_88D5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_88D5)
    Sleep(100)

    def lambda_88E8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_88E8)
    Sleep(100)
    OP_8C(0xF9, 0, 400)

    ChrTalk(    #428
        0x101,
        "#1004F#6P啊……怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x23,
        (
            "#5P怎么回事……\x02\x03",

            "伦格兰德大桥吊起来\x01",
            "不动了知道吧？\x02\x03",

            "因为这个，要去对面\x01",
            "只能乘小船了。\x02\x03",

            "而这里就是渡口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x101,
        "#1007F#6P这、这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x102,
        (
            "#1043F#4P那……\x01",
            "还是很不方便啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x23,
        (
            "#5P不方便当然不方便。\x01",
            "说实话，真是受不了啊。\x02\x03",

            "虽然由于新市长的安排\x01",
            "坐船是免费的……\x02\x03",

            "尽管如此，光是排队\x01",
            "就要等上３０分钟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8BEA")

    label("loc_8A4E")

    OP_6D(7470, -2250, 94090, 2000)

    ChrTalk(    #433
        0x101,
        "#1004F#5P这个，难道就是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x102,
        (
            "#1042F#2P嘉恩先生说的\x01",
            "小船渡口呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_8AC5():
        OP_6D(7160, -2250, 96060, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8AC5)
    TurnDirection(0x23, 0x101, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #435
        0x23,
        (
            "#5P怎么，你们也要\x01",
            "前往对面吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8B0D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B0D)
    Sleep(100)

    def lambda_8B20():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_8B20)
    Sleep(100)

    def lambda_8B33():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8B33)
    Sleep(100)
    OP_8C(0xF9, 0, 400)

    ChrTalk(    #436
        0x101,
        (
            "#1025F#6P啊，嗯。\x01",
            "虽然有这打算……\x02\x03",

            "需要花钱吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x23,
        (
            "#5P不，由于新市长的安排\x01",
            "坐船是免费的……\x02\x03",

            "尽管如此，光是排队\x01",
            "就要等上３０分钟。\x02\x03",

            "说实话，真是受不了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C20")

    ChrTalk(    #438
        0x107,
        (
            "#065F#4P呜哎～……\x01",
            "要那么久吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C7B")

    label("loc_8C20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C4F")

    ChrTalk(    #439
        0x103,
        "#025F#4P那可够久的呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C7B")

    label("loc_8C4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C7B")

    ChrTalk(    #440
        0x106,
        "#052F#4P那可够久的啊……\x02",
    )

    CloseMessageWindow()

    label("loc_8C7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8CCB")

    ChrTalk(    #441
        0x108,
        (
            "#074F#4P不过，因为是往返航程，\x01",
            "需要这么长时间也没办法呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D68")

    label("loc_8CCB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D1B")

    ChrTalk(    #442
        0x106,
        (
            "#053F#4P不过，因为是往返航程，\x01",
            "需要这么长时间也没办法呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D68")

    label("loc_8D1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D68")

    ChrTalk(    #443
        0x103,
        (
            "#025F#4P不过，因为是往返航程，\x01",
            "需要这么长时间也没办法呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D68")

    OP_6D(7470, -2250, 94090, 1500)

    ChrTalk(    #444
        0x102,
        (
            "#1042F#4P怎么办，艾丝蒂尔。\x01",
            "我们也前往对面吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8DB3():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_8DB3)
    Sleep(100)

    def lambda_8DC6():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_8DC6)
    Sleep(100)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #445
        0x101,
        "#1015F#5P唔，嗯～……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【前往南街区】\x01",      # 0
            "【先不过去】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8ECD")

    ChrTalk(    #446
        0x101,
        (
            "#1025F#5P不，先不去了。\x02\x03",

            "做完手上的事之后\x01",
            "再去对面吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x102,
        (
            "#1040F#4P知道了。\x01",
            "那么回去吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT21/T2132   ._SN", 108, 0, 0)
    IdleLoop()

    label("loc_8ECD")

    OP_A2(0x2036)

    ChrTalk(    #448
        0x101,
        (
            "#1007F#5P……没法子。\x01",
            "似乎也没其他的办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0x102,
        (
            "#1040F#4P知道了。\x01",
            "那么排队吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(5640, -2250, 96310, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(116000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 1310, -2250, 94760, 270)
    SetChrPos(0x16, 1960, -2250, 94550, 270)
    SetChrPos(0x17, 2700, -2250, 94650, 270)
    SetChrPos(0x18, 3410, -2250, 94720, 270)
    SetChrPos(0x19, 4130, -2250, 94610, 270)
    SetChrPos(0x23, 4450, -2250, 95100, 180)
    SetChrPos(0x101, 4460, -2250, 95780, 180)
    SetChrPos(0x102, 4470, -2250, 96560, 180)
    SetChrPos(0xF8, 5090, -2250, 96860, 225)
    SetChrPos(0xF9, 5880, -2250, 96840, 225)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(4070, -2250, 95380, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(56000, 0)
    OP_6E(262, 0)
    SetChrPos(0x17, 1310, -2250, 94760, 270)
    SetChrPos(0x18, 1960, -2250, 94550, 270)
    SetChrPos(0x19, 2700, -2250, 94650, 270)
    SetChrPos(0x23, 3410, -2250, 94720, 270)
    SetChrPos(0x101, 4130, -2250, 94610, 270)
    SetChrPos(0x102, 4450, -2250, 95100, 180)
    SetChrPos(0xF8, 4460, -2250, 95780, 180)
    SetChrPos(0xF9, 4470, -2250, 96560, 180)
    SetChrPos(0x13, 5090, -2250, 96860, 225)
    SetChrPos(0x12, 5880, -2250, 96840, 225)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(2540, -2250, 94610, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 1310, -2250, 94760, 270)
    SetChrPos(0x102, 1960, -2250, 94550, 270)
    SetChrPos(0xF8, 2700, -2250, 94650, 270)
    SetChrPos(0xF9, 3410, -2250, 94720, 270)
    SetChrPos(0x13, 4130, -2250, 94610, 270)
    SetChrPos(0x12, 4450, -2250, 95100, 180)
    SetChrPos(0x16, 4460, -2250, 95780, 180)
    SetChrPos(0x10, 4470, -2250, 96560, 180)
    SetChrPos(0x15, 5090, -2250, 96860, 225)
    SetChrPos(0x19, 5880, -2250, 96840, 225)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x23, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x19, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(-600, -2250, 94270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    LoadEffect(0x1, "map\\\\mp013_02.eff")
    PlayEffect(0x1, 0x1, 0xFF, -1050, -3100, 92700, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x20, 0x4)
    OP_72(0x20, 0x4)
    OP_72(0x20, 0x2)
    OP_71(0x20, 0x400)
    OP_71(0x20, 0x40)
    OP_71(0x20, 0x20)
    OP_B0(0x20, 0x1E)
    OP_6F(0x20, 1)
    OP_70(0x20, 0xF0)
    OP_72(0x20, 0x4)
    OP_A1(0x33, 0x20)
    SetChrPos(0x33, -810, -2850, 92590, 0)
    OP_8C(0x33, 90, 0)
    OP_4A(0x2D, 255)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x40)
    SetChrBattleFlags(0x2D, 0x20)
    OP_89(0x2D, 400, -3000, 93100, 0)
    OP_48()
    SetChrPos(0x101, -650, -2250, 94360, 180)
    SetChrPos(0x102, 280, -2250, 94270, 180)
    SetChrPos(0xF8, -50, -2250, 95350, 180)
    SetChrPos(0xF9, 1040, -2250, 95340, 180)
    SetChrPos(0x13, 2700, -2250, 94650, 270)
    SetChrPos(0x12, 3410, -2250, 94720, 270)
    SetChrPos(0x16, 4130, -2250, 94610, 270)
    SetChrPos(0x10, 4450, -2250, 95100, 180)
    SetChrPos(0x15, 4460, -2250, 95780, 180)
    SetChrPos(0x19, 4470, -2250, 96560, 180)
    OP_6D(40, -2250, 94620, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(9000, 0)
    OP_6E(390, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #450
        0x2D,
        (
            "#6P久等了。\x01",
            "轮到你们了。\x02\x03",

            "赶快上小船吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0x101,
        "#1006F#5P啊，嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x102,
        "#1040F#5P麻烦您了。\x02",
    )

    CloseMessageWindow()
    OP_82(0x1, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x1CC, 0x0, 0x64)
    Sleep(2000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2101   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_50_857D end

    def Function_51_9507(): pass

    label("Function_51_9507")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_951E")
    Call(0, 53)
    Call(0, 54)

    label("loc_951E")

    SetChrPos(0x101, 6140, -2250, 93480, 270)
    SetChrPos(0x102, 6120, -2250, 92390, 270)
    SetChrPos(0xF8, 7260, -2250, 93700, 270)
    SetChrPos(0xF9, 7310, -2250, 92540, 270)
    SetChrPos(0x10, 1310, -2250, 94760, 270)
    SetChrPos(0x11, 1960, -2250, 94550, 270)
    SetChrPos(0x12, 2700, -2250, 94650, 270)
    SetChrPos(0x13, 3410, -2250, 94720, 270)
    SetChrPos(0x14, 4130, -2250, 94610, 270)
    SetChrPos(0x16, 4450, -2250, 95100, 180)
    SetChrPos(0x17, 4460, -2250, 95780, 180)
    SetChrPos(0x18, 4470, -2250, 96560, 180)
    SetChrPos(0x19, 5090, -2250, 96860, 225)
    SetChrPos(0x23, 5880, -2250, 96840, 225)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(7470, -2250, 94090, 0)
    OP_67(0, 6250, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(45000, 0)
    OP_6E(354, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96E3")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #453
        0x102,
        (
            "#1042F#4P怎么办，艾丝蒂尔。\x01",
            "我们也前往对面吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x101,
        "#1015F#5P唔，嗯～……\x02",
    )

    CloseMessageWindow()

    label("loc_96E3")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【前往南街区】\x01",      # 0
            "【先不过去】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_97CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97B1")
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #455
        0x101,
        (
            "#1025F#5P不，先不去了。\x02\x03",

            "做完手上的事之后\x01",
            "再去对面吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x102,
        (
            "#1040F#4P知道了。\x01",
            "那么回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97B1")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT21/T2132   ._SN", 108, 0, 0)
    IdleLoop()

    label("loc_97CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_982D")
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #457
        0x101,
        (
            "#1007F#5P……没法子。\x01",
            "似乎也没其他的办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x102,
        (
            "#1040F#4P知道了。\x01",
            "那么排队吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_982D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(5640, -2250, 96310, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(116000, 0)
    OP_6E(262, 0)
    SetChrPos(0x14, 1310, -2250, 94760, 270)
    SetChrPos(0x16, 1960, -2250, 94550, 270)
    SetChrPos(0x17, 2700, -2250, 94650, 270)
    SetChrPos(0x18, 3410, -2250, 94720, 270)
    SetChrPos(0x19, 4130, -2250, 94610, 270)
    SetChrPos(0x23, 4450, -2250, 95100, 180)
    SetChrPos(0x101, 4460, -2250, 95780, 180)
    SetChrPos(0x102, 4470, -2250, 96560, 180)
    SetChrPos(0xF8, 5090, -2250, 96860, 225)
    SetChrPos(0xF9, 5880, -2250, 96840, 225)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(4070, -2250, 95380, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(56000, 0)
    OP_6E(262, 0)
    SetChrPos(0x17, 1310, -2250, 94760, 270)
    SetChrPos(0x18, 1960, -2250, 94550, 270)
    SetChrPos(0x19, 2700, -2250, 94650, 270)
    SetChrPos(0x23, 3410, -2250, 94720, 270)
    SetChrPos(0x101, 4130, -2250, 94610, 270)
    SetChrPos(0x102, 4450, -2250, 95100, 180)
    SetChrPos(0xF8, 4460, -2250, 95780, 180)
    SetChrPos(0xF9, 4470, -2250, 96560, 180)
    SetChrPos(0x13, 5090, -2250, 96860, 225)
    SetChrPos(0x12, 5880, -2250, 96840, 225)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(2540, -2250, 94610, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 1310, -2250, 94760, 270)
    SetChrPos(0x102, 1960, -2250, 94550, 270)
    SetChrPos(0xF8, 2700, -2250, 94650, 270)
    SetChrPos(0xF9, 3410, -2250, 94720, 270)
    SetChrPos(0x13, 4130, -2250, 94610, 270)
    SetChrPos(0x12, 4450, -2250, 95100, 180)
    SetChrPos(0x16, 4460, -2250, 95780, 180)
    SetChrPos(0x10, 4470, -2250, 96560, 180)
    SetChrPos(0x15, 5090, -2250, 96860, 225)
    SetChrPos(0x19, 5880, -2250, 96840, 225)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x23, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x19, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(-600, -2250, 94270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    LoadEffect(0x1, "map\\\\mp013_02.eff")
    PlayEffect(0x1, 0x1, 0xFF, -1050, -3100, 92700, 90, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x20, 0x4)
    OP_72(0x20, 0x4)
    OP_72(0x20, 0x2)
    OP_71(0x20, 0x400)
    OP_71(0x20, 0x40)
    OP_71(0x20, 0x20)
    OP_B0(0x20, 0x1E)
    OP_6F(0x20, 1)
    OP_70(0x20, 0xF0)
    OP_72(0x20, 0x4)
    OP_A1(0x33, 0x20)
    SetChrPos(0x33, -810, -2850, 92590, 0)
    OP_8C(0x33, 90, 0)
    OP_4A(0x2D, 255)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x40)
    SetChrBattleFlags(0x2D, 0x20)
    OP_89(0x2D, 400, -3000, 93100, 0)
    OP_48()
    SetChrPos(0x101, -650, -2250, 94360, 180)
    SetChrPos(0x102, 280, -2250, 94270, 180)
    SetChrPos(0xF8, -50, -2250, 95350, 180)
    SetChrPos(0xF9, 1040, -2250, 95340, 180)
    SetChrPos(0x13, 2700, -2250, 94650, 270)
    SetChrPos(0x12, 3410, -2250, 94720, 270)
    SetChrPos(0x16, 4130, -2250, 94610, 270)
    SetChrPos(0x10, 4450, -2250, 95100, 180)
    SetChrPos(0x15, 4460, -2250, 95780, 180)
    SetChrPos(0x19, 4470, -2250, 96560, 180)
    OP_6D(40, -2250, 94620, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(9000, 0)
    OP_6E(390, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DF9")
    OP_A2(0x2036)

    ChrTalk(    #459
        0x2D,
        (
            "#6P久等了。\x01",
            "轮到你们了。\x02\x03",

            "赶快上小船吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x101,
        "#1006F#5P啊，嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0x102,
        "#1040F#5P麻烦您了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9E2D")

    label("loc_9DF9")


    ChrTalk(    #462
        0x2D,
        (
            "#6P好，轮到你们了哦。\x02\x03",

            "后面很挤\x01",
            "赶快上小船吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E2D")

    OP_82(0x1, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x1CC, 0x0, 0x64)
    Sleep(2000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2101   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_51_9507 end

    def Function_52_9E52(): pass

    label("Function_52_9E52")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E69")
    Call(0, 53)
    Call(0, 54)

    label("loc_9E69")

    OP_D2(0x270003, 0x270007, 0x23)
    OP_D2(0x270013, 0x270017, 0x24)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_9E96"),
        (5, "loc_9EA3"),
        (6, "loc_9EB0"),
        (7, "loc_9EBD"),
        (SWITCH_DEFAULT, "loc_9ECA"),
    )


    label("loc_9E96")

    OP_D2(0x70023, 0x7002B, 0x25)
    Jump("loc_9ECA")

    label("loc_9EA3")

    OP_D2(0x70053, 0x7005B, 0x25)
    Jump("loc_9ECA")

    label("loc_9EB0")

    OP_D2(0x70063, 0x7006B, 0x25)
    Jump("loc_9ECA")

    label("loc_9EBD")

    OP_D2(0x70073, 0x7007B, 0x25)
    Jump("loc_9ECA")

    label("loc_9ECA")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_9EE3"),
        (5, "loc_9EF0"),
        (6, "loc_9EFD"),
        (7, "loc_9F0A"),
        (SWITCH_DEFAULT, "loc_9F17"),
    )


    label("loc_9EE3")

    OP_D2(0x70023, 0x7002B, 0x26)
    Jump("loc_9F17")

    label("loc_9EF0")

    OP_D2(0x70053, 0x7005B, 0x26)
    Jump("loc_9F17")

    label("loc_9EFD")

    OP_D2(0x70063, 0x7006B, 0x26)
    Jump("loc_9F17")

    label("loc_9F0A")

    OP_D2(0x70073, 0x7007B, 0x26)
    Jump("loc_9F17")

    label("loc_9F17")

    SetChrChipByIndex(0x101, 35)
    SetChrChipByIndex(0x102, 36)
    SetChrChipByIndex(0xF8, 37)
    SetChrChipByIndex(0xF9, 38)
    SetChrPos(0x10, 1310, -2250, 94760, 270)
    SetChrPos(0x11, 1960, -2250, 94550, 270)
    SetChrPos(0x12, 2700, -2250, 94650, 270)
    SetChrPos(0x13, 3410, -2250, 94720, 270)
    SetChrPos(0x14, 4130, -2250, 94610, 270)
    SetChrPos(0x16, 4450, -2250, 95100, 180)
    SetChrPos(0x17, 4460, -2250, 95780, 180)
    SetChrPos(0x18, 4470, -2250, 96560, 180)
    SetChrPos(0x19, 5090, -2250, 96860, 225)
    SetChrPos(0x23, 5880, -2250, 96840, 225)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_4A(0x2D, 255)
    LoadEffect(0x0, "map\\\\mp013_00.eff")
    PlayEffect(0x0, 0x0, 0x33, 0, -150, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    OP_72(0x20, 0x4)
    OP_71(0x20, 0x2)
    OP_71(0x20, 0x40)
    OP_71(0x20, 0x20)
    OP_B0(0x20, 0x1E)
    OP_6F(0x20, 1)
    OP_70(0x20, 0xF0)
    OP_72(0x20, 0x4)
    OP_A1(0x33, 0x20)
    SetChrPos(0x33, -15000, -2850, 92590, 90)
    SetChrBattleFlags(0x2D, 0x20)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x102, 0x20)
    SetChrBattleFlags(0xF8, 0x20)
    SetChrBattleFlags(0xF9, 0x20)
    OP_48()
    OP_8C(0x33, 90, 0)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2D, 0x1)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    ClearChrFlags(0x2D, 0x1)
    SetChrFlags(0x2D, 0x20)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0xF8, 0x20)
    SetChrFlags(0xF9, 0x20)
    SetChrFlags(0x2D, 0x40)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0xF8, 0x40)
    SetChrFlags(0xF9, 0x40)
    OP_48()
    OP_8C(0x33, 270, 0)
    OP_89(0x101, -14050, -2800, 92360, 90)
    OP_89(0x102, -14050, -2800, 93000, 90)
    OP_89(0xF8, -15400, -2800, 93000, 90)
    OP_89(0xF9, -15400, -2800, 92360, 90)
    OP_89(0x2D, -16100, -3000, 92200, 180)
    OP_6D(-2540, -2820, 92800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_A1B5():

        label("loc_A1B5")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_A1B5")

    QueueWorkItem2(0x23, 1, lambda_A1B5)

    def lambda_A1C6():

        label("loc_A1C6")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_A1C6")

    QueueWorkItem2(0x10, 1, lambda_A1C6)

    def lambda_A1D7():

        label("loc_A1D7")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_A1D7")

    QueueWorkItem2(0x11, 1, lambda_A1D7)

    def lambda_A1E8():

        label("loc_A1E8")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_A1E8")

    QueueWorkItem2(0x12, 1, lambda_A1E8)

    def lambda_A1F9():

        label("loc_A1F9")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_A1F9")

    QueueWorkItem2(0x13, 1, lambda_A1F9)

    def lambda_A20A():

        label("loc_A20A")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_A20A")

    QueueWorkItem2(0x14, 1, lambda_A20A)

    def lambda_A21B():

        label("loc_A21B")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_A21B")

    QueueWorkItem2(0x16, 1, lambda_A21B)

    def lambda_A22C():

        label("loc_A22C")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_A22C")

    QueueWorkItem2(0x17, 1, lambda_A22C)

    def lambda_A23D():

        label("loc_A23D")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_A23D")

    QueueWorkItem2(0x18, 1, lambda_A23D)

    def lambda_A24E():

        label("loc_A24E")

        TurnDirection(0xFE, 0x33, 400)
        OP_48()
        Jump("loc_A24E")

    QueueWorkItem2(0x19, 1, lambda_A24E)

    def lambda_A25F():
        OP_8F(0xFE, 0xFFFFFCE0, 0xFFFFF4DE, 0x169AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_A25F)

    def lambda_A27A():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_A27A)

    def lambda_A295():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A295)

    def lambda_A2B0():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A2B0)

    def lambda_A2CB():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_A2CB)

    def lambda_A2E6():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_A2E6)
    Sleep(2000)

    def lambda_A306():
        OP_6D(200, -2250, 92990, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A306)
    Sleep(4000)

    def lambda_A323():
        OP_8F(0xFE, 0xFFFFFCD6, 0xFFFFF4DE, 0x169AE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_A323)

    def lambda_A33E():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_A33E)

    def lambda_A359():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A359)

    def lambda_A374():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A374)

    def lambda_A38F():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_A38F)

    def lambda_A3AA():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_A3AA)
    Sleep(2000)

    def lambda_A3CA():
        OP_8F(0xFE, 0xFFFFFCD6, 0xFFFFF4DE, 0x169AE, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x33, 1, lambda_A3CA)

    def lambda_A3E5():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_A3E5)

    def lambda_A400():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A400)

    def lambda_A41B():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A41B)

    def lambda_A436():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_A436)

    def lambda_A451():
        OP_91(0xFE, 0x3DB8, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_A451)
    WaitChrThread(0x33, 0x1)
    OP_44(0x2D, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_82(0x0, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0xF8, 0x1)
    SetChrFlags(0xF9, 0x1)
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT21/T2132   ._SN", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_52_9E52 end

    def Function_53_A4B0(): pass

    label("Function_53_A4B0")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A52A"),
        (1, "loc_A530"),
        (SWITCH_DEFAULT, "loc_A536"),
    )


    label("loc_A52A")

    OP_A2(0x1200)
    Jump("loc_A536")

    label("loc_A530")

    OP_A2(0x1201)
    Jump("loc_A536")

    label("loc_A536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_A544")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_A548")

    label("loc_A544")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_A548")

    Return()

    # Function_53_A4B0 end

    def Function_54_A549(): pass

    label("Function_54_A549")

    ClearMapFlags(0x1)
    OP_6D(-11050, -2250, 166960, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_54_A549 end

    def Function_55_A5A2(): pass

    label("Function_55_A5A2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #463
        (
            "\x07\x05　    卢安市长选举\x01",
            "※投票日请务必\x01",
            "　要去投票所\x01",
            "　　　　　选举管理委员会\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_55_A5A2 end

    def Function_56_A61C(): pass

    label("Function_56_A61C")

    EventBegin(0x1)

    ChrTalk(    #464
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_A648():
        OP_6D(15010, -1800, 111900, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A648)

    def lambda_A660():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_A660)

    def lambda_A670():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_A670)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #465
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6F7")
    OP_C0(0xE, 0x19, 0x3F7A, 0xFFFFF8F8, 0x1B5E4, 0x10E, 0x3610, 0xFFFFF510, 0x1B602)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_A706")

    label("loc_A6F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A706")
    EventEnd(0x1)

    label("loc_A706")

    Return()

    # Function_56_A61C end

    def Function_57_A707(): pass

    label("Function_57_A707")

    SetPlaceName(0x48)
    Return()

    # Function_57_A707 end

    def Function_58_A70B(): pass

    label("Function_58_A70B")

    SetPlaceName(0x4D)
    Return()

    # Function_58_A70B end

    def Function_59_A70F(): pass

    label("Function_59_A70F")

    SetPlaceName(0x4C)
    Return()

    # Function_59_A70F end

    def Function_60_A713(): pass

    label("Function_60_A713")

    SetPlaceName(0x4A)
    Return()

    # Function_60_A713 end

    def Function_61_A717(): pass

    label("Function_61_A717")

    SetPlaceName(0x4E)
    Return()

    # Function_61_A717 end

    def Function_62_A71B(): pass

    label("Function_62_A71B")

    SetPlaceName(0x4B)
    Return()

    # Function_62_A71B end

    def Function_63_A71F(): pass

    label("Function_63_A71F")

    SetPlaceName(0x49)
    Return()

    # Function_63_A71F end

    def Function_64_A723(): pass

    label("Function_64_A723")

    SetPlaceName(0x4F)
    Return()

    # Function_64_A723 end

    SaveToFile()

Try(main)
