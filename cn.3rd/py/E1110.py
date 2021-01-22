from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E1110   ._SN',
        MapName             = 'event',
        Location            = 'E1110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60170",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
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
        '谜一样的人物',                         # 9
        '武器商康莱特',                         # 10
        '黑衣人',                               # 11
        '黑衣人',                               # 12
        '黑衣人',                               # 13
        '黑衣人',                               # 14
        '黑衣人',                               # 15
        '黑衣人',                               # 16
        '黑衣人',                               # 17
        '黑衣人',                               # 18
        '戴面具的妇人',                         # 19
        '戴面具的男人',                         # 20
        '戴面具的老人',                         # 21
        '戴面具的贵妇人',                       # 22
        '戴面具的男人',                         # 23
        '戴面具的青年',                         # 24
        '戴面具的青年',                         # 25
        '戴面具的绅士',                         # 26
        '戴面具的青年',                         # 27
        '戴面具的男人',                         # 28
        '戴面具的妇人',                         # 29
        '戴面具的老绅士',                       # 30
        '戴面具的男人',                         # 31
        '戴面具的女人',                         # 32
        '戴面具的男人',                         # 33
        '戴面具的女人',                         # 34
        '戴面具的妇人',                         # 35
        '戴面具的绅士',                         # 36
        '戴面具的老绅士',                       # 37
        '女仆',                                 # 38
        '女仆',                                 # 39
        '侍者',                                 # 40
        '侍者',                                 # 41
        '乘客',                                 # 42
        '乘客',                                 # 43
        '乘客',                                 # 44
        '乘客',                                 # 45
        '职员',                                 # 46
        '黑衣人',                               # 47
        '黑衣人',                               # 48
        '贵族模样的男性',                       # 49
        '乘客',                                 # 50
        '乘客',                                 # 51
        '戴面具的青年',                         # 52
        '戴面具的男人',                         # 53
        '庄家',                                 # 54
        '庄家',                                 # 55
        '庄家',                                 # 56
        '庄家',                                 # 57
        '接待',                                 # 58
        '黑衣人',                               # 59
        '黑衣人',                               # 60
        '老绅士',                               # 61
        '老妇人',                               # 62
        '红茶',                                 # 63
        '红茶',                                 # 64
        '女仆',                                 # 65
        '乘客',                                 # 66
        '乘客',                                 # 67
        '黑衣人',                               # 68
        '黑衣人',                               # 69
        '黑衣人',                               # 70
        '黑衣人',                               # 71
        '乘客',                                 # 72
        '乘客',                                 # 73
        '女仆',                                 # 74
        '尼尔森',                               # 75
        '黑衣人',                               # 76
        '黑衣人',                               # 77
        '障碍用临时角色',                       # 78
        '障碍用临时角色',                       # 79
        '障碍用临时角色',                       # 80
        '障碍用临时角色',                       # 81
        '障碍用临时角色',                       # 82
        '障碍用临时角色',                       # 83
        '障碍用临时角色',                       # 84
        '障碍用临时角色',                       # 85
        '障碍用临时角色',                       # 86
        '障碍用临时角色',                       # 87
        '障碍用临时角色',                       # 88
        '障碍用临时角色',                       # 89
        '障碍用临时角色',                       # 90
        '障碍用临时角色',                       # 91
        '装甲猎豹',                             # 92
        '装甲猎豹',                             # 93
        '猎兵',                                 # 94
        '猎兵',                                 # 95
        '猎兵',                                 # 96
        '猎兵',                                 # 97
        '猎兵',                                 # 98
        '猎兵',                                 # 99
        '猎兵',                                 # 100
        '猎兵',                                 # 101
        '',                                     # 102
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02650 ._CH',             # 00
        'ED6_DT07/CH02770 ._CH',             # 01
        'ED6_DT07/CH02880 ._CH',             # 02
        'ED6_DT27/CH03420 ._CH',             # 03
        'ED6_DT27/CH03460 ._CH',             # 04
        'ED6_DT27/CH04420 ._CH',             # 05
        'ED6_DT27/CH04421 ._CH',             # 06
        'ED6_DT27/CH04422 ._CH',             # 07
        'ED6_DT27/CH04423 ._CH',             # 08
        'ED6_DT26/CH20613 ._CH',             # 09
        'ED6_DT27/CH04460 ._CH',             # 0A
        'ED6_DT27/CH04461 ._CH',             # 0B
        'ED6_DT27/CH04462 ._CH',             # 0C
        'ED6_DT27/CH04463 ._CH',             # 0D
        'ED6_DT26/CH20618 ._CH',             # 0E
        'ED6_DT26/CH20603 ._CH',             # 0F
        'ED6_DT26/CH20373 ._CH',             # 10
        'ED6_DT27/CH04080 ._CH',             # 11
        'ED6_DT27/CH04081 ._CH',             # 12
        'ED6_DT27/CH04082 ._CH',             # 13
        'ED6_DT26/CH20604 ._CH',             # 14
        'ED6_DT26/CH20605 ._CH',             # 15
        'ED6_DT27/CH04440 ._CH',             # 16
        'ED6_DT27/CH04441 ._CH',             # 17
        'ED6_DT27/CH04442 ._CH',             # 18
        'ED6_DT07/CH02660 ._CH',             # 19
        'ED6_DT07/CH02840 ._CH',             # 1A
        'ED6_DT07/CH02850 ._CH',             # 1B
        'ED6_DT07/CH02860 ._CH',             # 1C
        'ED6_DT07/CH02870 ._CH',             # 1D
        'ED6_DT07/CH01350 ._CH',             # 1E
        'ED6_DT07/CH01570 ._CH',             # 1F
        'ED6_DT27/CH03930 ._CH',             # 20
        'ED6_DT07/CH01560 ._CH',             # 21
        'ED6_DT29/CH12330 ._CH',             # 22
        'ED6_DT29/CH12331 ._CH',             # 23
        'ED6_DT07/CH01210 ._CH',             # 24
        'ED6_DT07/CH01143 ._CH',             # 25
        'ED6_DT07/CH01493 ._CH',             # 26
        'ED6_DT07/CH01223 ._CH',             # 27
        'ED6_DT07/CH01120 ._CH',             # 28
        'ED6_DT07/CH01140 ._CH',             # 29
        'ED6_DT07/CH01023 ._CH',             # 2A
        'ED6_DT07/CH01040 ._CH',             # 2B
        'ED6_DT07/CH02540 ._CH',             # 2C
        'ED6_DT07/CH01183 ._CH',             # 2D
        'ED6_DT07/CH01060 ._CH',             # 2E
        'ED6_DT07/CH01150 ._CH',             # 2F
        'ED6_DT07/CH01660 ._CH',             # 30
        'ED6_DT07/CH01220 ._CH',             # 31
        'ED6_DT06/CH20020 ._CH',             # 32
    )

    AddCharChipPat(
        'ED6_DT07/CH02650P._CP',             # 00
        'ED6_DT07/CH02770P._CP',             # 01
        'ED6_DT07/CH02880P._CP',             # 02
        'ED6_DT27/CH03420P._CP',             # 03
        'ED6_DT27/CH03460P._CP',             # 04
        'ED6_DT27/CH04420P._CP',             # 05
        'ED6_DT27/CH04421P._CP',             # 06
        'ED6_DT27/CH04422P._CP',             # 07
        'ED6_DT27/CH04423P._CP',             # 08
        'ED6_DT26/CH20613P._CP',             # 09
        'ED6_DT27/CH04460P._CP',             # 0A
        'ED6_DT27/CH04461P._CP',             # 0B
        'ED6_DT27/CH04462P._CP',             # 0C
        'ED6_DT27/CH04463P._CP',             # 0D
        'ED6_DT26/CH20618P._CP',             # 0E
        'ED6_DT26/CH20603P._CP',             # 0F
        'ED6_DT26/CH20373P._CP',             # 10
        'ED6_DT27/CH04080P._CP',             # 11
        'ED6_DT27/CH04081P._CP',             # 12
        'ED6_DT27/CH04082P._CP',             # 13
        'ED6_DT26/CH20604P._CP',             # 14
        'ED6_DT26/CH20605P._CP',             # 15
        'ED6_DT27/CH04440P._CP',             # 16
        'ED6_DT27/CH04441P._CP',             # 17
        'ED6_DT27/CH04442P._CP',             # 18
        'ED6_DT07/CH02660P._CP',             # 19
        'ED6_DT07/CH02840P._CP',             # 1A
        'ED6_DT07/CH02850P._CP',             # 1B
        'ED6_DT07/CH02860P._CP',             # 1C
        'ED6_DT07/CH02870P._CP',             # 1D
        'ED6_DT07/CH01350P._CP',             # 1E
        'ED6_DT07/CH01570P._CP',             # 1F
        'ED6_DT27/CH03930P._CP',             # 20
        'ED6_DT07/CH01560P._CP',             # 21
        'ED6_DT29/CH12330P._CP',             # 22
        'ED6_DT29/CH12331P._CP',             # 23
        'ED6_DT07/CH01210P._CP',             # 24
        'ED6_DT07/CH01143P._CP',             # 25
        'ED6_DT07/CH01493P._CP',             # 26
        'ED6_DT07/CH01223P._CP',             # 27
        'ED6_DT07/CH01120P._CP',             # 28
        'ED6_DT07/CH01140P._CP',             # 29
        'ED6_DT07/CH01023P._CP',             # 2A
        'ED6_DT07/CH01040P._CP',             # 2B
        'ED6_DT07/CH02540P._CP',             # 2C
        'ED6_DT07/CH01183P._CP',             # 2D
        'ED6_DT07/CH01060P._CP',             # 2E
        'ED6_DT07/CH01150P._CP',             # 2F
        'ED6_DT07/CH01660P._CP',             # 30
        'ED6_DT07/CH01220P._CP',             # 31
        'ED6_DT06/CH20020P._CP',             # 32
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = -370,
        Z                   = 0,
        Y                   = 21560,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 54,
    )

    DeclNpc(
        X                   = -2810,
        Z                   = 0,
        Y                   = -390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 48,
    )

    DeclNpc(
        X                   = -2810,
        Z                   = 0,
        Y                   = -390,
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
        X                   = 2750,
        Z                   = 0,
        Y                   = -420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 49,
    )

    DeclNpc(
        X                   = 2750,
        Z                   = 0,
        Y                   = -420,
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
        X                   = 7000,
        Z                   = 1000,
        Y                   = 21890,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 50,
    )

    DeclNpc(
        X                   = 7000,
        Z                   = 1000,
        Y                   = 21890,
        Direction           = 180,
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
        X                   = -7950,
        Z                   = 1000,
        Y                   = 22550,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 51,
    )

    DeclNpc(
        X                   = -7950,
        Z                   = 1000,
        Y                   = 22550,
        Direction           = 180,
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
        X                   = 6300,
        Z                   = 0,
        Y                   = 13440,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 55,
    )

    DeclNpc(
        X                   = -2620,
        Z                   = 0,
        Y                   = 15940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 56,
    )

    DeclNpc(
        X                   = -110,
        Z                   = 0,
        Y                   = 18900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 57,
    )

    DeclNpc(
        X                   = 5160,
        Z                   = 0,
        Y                   = 7060,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 58,
    )

    DeclNpc(
        X                   = -3730,
        Z                   = 0,
        Y                   = 5490,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 59,
    )

    DeclNpc(
        X                   = -4460,
        Z                   = 0,
        Y                   = 3830,
        Direction           = 360,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 60,
    )

    DeclNpc(
        X                   = 3420,
        Z                   = 0,
        Y                   = 12930,
        Direction           = 80,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 61,
    )

    DeclNpc(
        X                   = 9240,
        Z                   = 0,
        Y                   = 8690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 62,
    )

    DeclNpc(
        X                   = 10750,
        Z                   = 0,
        Y                   = 8690,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 63,
    )

    DeclNpc(
        X                   = 5340,
        Z                   = 0,
        Y                   = 7140,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 64,
    )

    DeclNpc(
        X                   = 3640,
        Z                   = 0,
        Y                   = 6190,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 65,
    )

    DeclNpc(
        X                   = -10530,
        Z                   = 0,
        Y                   = 8540,
        Direction           = 266,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 66,
    )

    DeclNpc(
        X                   = -11800,
        Z                   = 0,
        Y                   = 9200,
        Direction           = 125,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 67,
    )

    DeclNpc(
        X                   = -6590,
        Z                   = 0,
        Y                   = 14350,
        Direction           = 115,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 68,
    )

    DeclNpc(
        X                   = -5090,
        Z                   = 0,
        Y                   = 13560,
        Direction           = 266,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 69,
    )

    DeclNpc(
        X                   = -8260,
        Z                   = 0,
        Y                   = 6010,
        Direction           = 167,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 70,
    )

    DeclNpc(
        X                   = -8390,
        Z                   = 0,
        Y                   = 4210,
        Direction           = 6,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 71,
    )

    DeclNpc(
        X                   = -14250,
        Z                   = 0,
        Y                   = 2670,
        Direction           = 181,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 73,
    )

    DeclNpc(
        X                   = 8310,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 272,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 74,
    )

    DeclNpc(
        X                   = -5030,
        Z                   = 0,
        Y                   = 8760,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 75,
    )

    DeclNpc(
        X                   = -9430,
        Z                   = 0,
        Y                   = 13630,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 76,
    )

    DeclNpc(
        X                   = 14280,
        Z                   = 0,
        Y                   = 2410,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 77,
    )

    DeclNpc(
        X                   = -14030,
        Z                   = 0,
        Y                   = -70,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 78,
    )

    DeclNpc(
        X                   = -58040,
        Z                   = 0,
        Y                   = -26840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 79,
    )

    DeclNpc(
        X                   = -60670,
        Z                   = 350,
        Y                   = -36890,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 80,
    )

    DeclNpc(
        X                   = -60620,
        Z                   = 250,
        Y                   = -39170,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 81,
    )

    DeclNpc(
        X                   = -53910,
        Z                   = 300,
        Y                   = -45800,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 82,
    )

    DeclNpc(
        X                   = -51030,
        Z                   = 20,
        Y                   = -40450,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 83,
    )

    DeclNpc(
        X                   = -50920,
        Z                   = 0,
        Y                   = -27420,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 84,
    )

    DeclNpc(
        X                   = -50920,
        Z                   = 0,
        Y                   = -27420,
        Direction           = 225,
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
        X                   = -59640,
        Z                   = 0,
        Y                   = -118280,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 49,
        ChipIndex           = 0x31,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 85,
    )

    DeclNpc(
        X                   = -54670,
        Z                   = 0,
        Y                   = -110110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 86,
    )

    DeclNpc(
        X                   = -51170,
        Z                   = 300,
        Y                   = -126580,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 87,
    )

    DeclNpc(
        X                   = -58300,
        Z                   = 0,
        Y                   = -123940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 88,
    )

    DeclNpc(
        X                   = -56940,
        Z                   = 0,
        Y                   = -112010,
        Direction           = 284,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 89,
    )

    DeclNpc(
        X                   = -60310,
        Z                   = 0,
        Y                   = -111770,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 90,
    )

    DeclNpc(
        X                   = -58240,
        Z                   = 0,
        Y                   = -121360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 91,
    )

    DeclNpc(
        X                   = -58520,
        Z                   = 0,
        Y                   = -128880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 92,
    )

    DeclNpc(
        X                   = -51630,
        Z                   = 0,
        Y                   = -110280,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 93,
    )

    DeclNpc(
        X                   = -51660,
        Z                   = 0,
        Y                   = -120900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 94,
    )

    DeclNpc(
        X                   = -61170,
        Z                   = 0,
        Y                   = -115150,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 95,
    )

    DeclNpc(
        X                   = -61170,
        Z                   = 0,
        Y                   = -115150,
        Direction           = 90,
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
        X                   = 80880,
        Z                   = 300,
        Y                   = -35450,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 96,
    )

    DeclNpc(
        X                   = 82600,
        Z                   = 300,
        Y                   = -37010,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 97,
    )

    DeclNpc(
        X                   = 81900,
        Z                   = 650,
        Y                   = -37000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638450,
        ChipIndex           = 0x32,
        NpcIndex            = 0x167,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 81000,
        Z                   = 650,
        Y                   = -36100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638450,
        ChipIndex           = 0x32,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 85160,
        Z                   = 20,
        Y                   = -72010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 98,
    )

    DeclNpc(
        X                   = 79610,
        Z                   = 0,
        Y                   = -110650,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 99,
    )

    DeclNpc(
        X                   = 79590,
        Z                   = 0,
        Y                   = -112460,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 100,
    )

    DeclNpc(
        X                   = 1940,
        Z                   = 0,
        Y                   = -85780,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 104,
    )

    DeclNpc(
        X                   = 1940,
        Z                   = 0,
        Y                   = -85780,
        Direction           = 180,
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
        X                   = 84380,
        Z                   = 0,
        Y                   = -168870,
        Direction           = 222,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 105,
    )

    DeclNpc(
        X                   = 84380,
        Z                   = 0,
        Y                   = -168870,
        Direction           = 222,
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
        X                   = 3460,
        Z                   = 0,
        Y                   = -198800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 47,
        ChipIndex           = 0x2F,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 102,
    )

    DeclNpc(
        X                   = 5030,
        Z                   = 0,
        Y                   = -198760,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 103,
    )

    DeclNpc(
        X                   = 3060,
        Z                   = 0,
        Y                   = -132830,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 101,
    )

    DeclNpc(
        X                   = 92200,
        Z                   = 0,
        Y                   = -175500,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 106,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 1800,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 1800,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2500,
        Z                   = 0,
        Y                   = -139810,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2580,
        Z                   = 0,
        Y                   = -138900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2000,
        Z                   = 0,
        Y                   = -140260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2520,
        Z                   = 0,
        Y                   = -139340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2530,
        Z                   = 0,
        Y                   = -137270,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3450,
        Z                   = 0,
        Y                   = -137000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2020,
        Z                   = 0,
        Y                   = -137880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2920,
        Z                   = 0,
        Y                   = -137420,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -5500,
        Y                   = -1000,
        Z                   = -143000,
        Range               = 6000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFDDD20,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = -5500,
        Y                   = -1000,
        Z                   = -103000,
        Range               = 6000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFE7960,
        Unknown_18          = 0x0,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = -380,
        Y                   = 0,
        Z                   = 20340,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 52,
    )

    DeclEvent(
        X                   = -380,
        Y                   = 0,
        Z                   = 20340,
        Range               = 2000,
        Unknown_10          = 0x640,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 53,
    )

    DeclEvent(
        X                   = -2500,
        Y                   = -1000,
        Z                   = -209500,
        Range               = 2500,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFCC7C8,
        Unknown_18          = 0x0,
        Unknown_1C          = 110,
    )

    DeclEvent(
        X                   = 77000,
        Y                   = -1000,
        Z                   = -161500,
        Range               = 83000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0xFFFD92E8,
        Unknown_18          = 0x0,
        Unknown_1C          = 111,
    )


    DeclActor(
        TriggerX            = 5020,
        TriggerZ            = 0,
        TriggerY            = -96990,
        TriggerRange        = 500,
        ActorX              = 5020,
        ActorZ              = 1000,
        ActorY              = -96990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 107,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5060,
        TriggerZ            = 0,
        TriggerY            = -120950,
        TriggerRange        = 500,
        ActorX              = 5060,
        ActorZ              = 1000,
        ActorY              = -120950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 107,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5050,
        TriggerZ            = 0,
        TriggerY            = -144940,
        TriggerRange        = 500,
        ActorX              = 5050,
        ActorZ              = 1000,
        ActorY              = -144940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 107,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85860,
        TriggerZ            = 0,
        TriggerY            = -27250,
        TriggerRange        = 1000,
        ActorX              = 85860,
        ActorZ              = 1000,
        ActorY              = -27250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 86100,
        TriggerZ            = 0,
        TriggerY            = -78920,
        TriggerRange        = 1000,
        ActorX              = 86100,
        ActorZ              = 1000,
        ActorY              = -78920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 83290,
        TriggerZ            = 0,
        TriggerY            = -106000,
        TriggerRange        = 1000,
        ActorX              = 83290,
        ActorZ              = 1000,
        ActorY              = -106000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 84750,
        TriggerZ            = 0,
        TriggerY            = -106000,
        TriggerRange        = 1000,
        ActorX              = 84750,
        ActorZ              = 1000,
        ActorY              = -106000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -52700,
        TriggerZ            = 0,
        TriggerY            = -121000,
        TriggerRange        = 800,
        ActorX              = -51660,
        ActorZ              = 1500,
        ActorY              = -120900,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 94,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 12500,
        TriggerZ            = 0,
        TriggerY            = 2410,
        TriggerRange        = 500,
        ActorX              = 14280,
        ActorZ              = 1500,
        ActorY              = 2410,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 77,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 92500,
        TriggerZ            = 0,
        TriggerY            = -175750,
        TriggerRange        = 500,
        ActorX              = 92500,
        ActorZ              = 1000,
        ActorY              = -175750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 107,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -53840,
        TriggerZ            = 0,
        TriggerY            = -25950,
        TriggerRange        = 500,
        ActorX              = -53840,
        ActorZ              = 1000,
        ActorY              = -25950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 112,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_102E",         # 00, 0
        "Function_1_120C",         # 01, 1
        "Function_2_12BD",         # 02, 2
        "Function_3_13E3",         # 03, 3
        "Function_4_1509",         # 04, 4
        "Function_5_162F",         # 05, 5
        "Function_6_1755",         # 06, 6
        "Function_7_18D2",         # 07, 7
        "Function_8_18F6",         # 08, 8
        "Function_9_2C91",         # 09, 9
        "Function_10_2D6A",        # 0A, 10
        "Function_11_2D97",        # 0B, 11
        "Function_12_2DBE",        # 0C, 12
        "Function_13_2F3C",        # 0D, 13
        "Function_14_31C3",        # 0E, 14
        "Function_15_31FE",        # 0F, 15
        "Function_16_320A",        # 10, 16
        "Function_17_36EE",        # 11, 17
        "Function_18_3BD2",        # 12, 18
        "Function_19_3FFE",        # 13, 19
        "Function_20_4061",        # 14, 20
        "Function_21_40C9",        # 15, 21
        "Function_22_4108",        # 16, 22
        "Function_23_4147",        # 17, 23
        "Function_24_4682",        # 18, 24
        "Function_25_46A3",        # 19, 25
        "Function_26_4B31",        # 1A, 26
        "Function_27_62CC",        # 1B, 27
        "Function_28_631C",        # 1C, 28
        "Function_29_6340",        # 1D, 29
        "Function_30_6364",        # 1E, 30
        "Function_31_6388",        # 1F, 31
        "Function_32_63AC",        # 20, 32
        "Function_33_63D0",        # 21, 33
        "Function_34_63F4",        # 22, 34
        "Function_35_6418",        # 23, 35
        "Function_36_643C",        # 24, 36
        "Function_37_6461",        # 25, 37
        "Function_38_6486",        # 26, 38
        "Function_39_64AB",        # 27, 39
        "Function_40_64D0",        # 28, 40
        "Function_41_64F5",        # 29, 41
        "Function_42_650A",        # 2A, 42
        "Function_43_651F",        # 2B, 43
        "Function_44_6534",        # 2C, 44
        "Function_45_65EF",        # 2D, 45
        "Function_46_66E3",        # 2E, 46
        "Function_47_67D7",        # 2F, 47
        "Function_48_6C4E",        # 30, 48
        "Function_49_6CBE",        # 31, 49
        "Function_50_6CFA",        # 32, 50
        "Function_51_6D40",        # 33, 51
        "Function_52_6E2C",        # 34, 52
        "Function_53_6E39",        # 35, 53
        "Function_54_70F7",        # 36, 54
        "Function_55_71C0",        # 37, 55
        "Function_56_7319",        # 38, 56
        "Function_57_73F8",        # 39, 57
        "Function_58_74CC",        # 3A, 58
        "Function_59_751E",        # 3B, 59
        "Function_60_7607",        # 3C, 60
        "Function_61_76CF",        # 3D, 61
        "Function_62_774C",        # 3E, 62
        "Function_63_7839",        # 3F, 63
        "Function_64_78ED",        # 40, 64
        "Function_65_79DA",        # 41, 65
        "Function_66_7AB5",        # 42, 66
        "Function_67_7B93",        # 43, 67
        "Function_68_7CAE",        # 44, 68
        "Function_69_7DCB",        # 45, 69
        "Function_70_7EE6",        # 46, 70
        "Function_71_808A",        # 47, 71
        "Function_72_80FD",        # 48, 72
        "Function_73_8104",        # 49, 73
        "Function_74_822D",        # 4A, 74
        "Function_75_8316",        # 4B, 75
        "Function_76_83B7",        # 4C, 76
        "Function_77_846D",        # 4D, 77
        "Function_78_8516",        # 4E, 78
        "Function_79_85DB",        # 4F, 79
        "Function_80_86E5",        # 50, 80
        "Function_81_87EF",        # 51, 81
        "Function_82_890B",        # 52, 82
        "Function_83_89E3",        # 53, 83
        "Function_84_8A83",        # 54, 84
        "Function_85_8AA8",        # 55, 85
        "Function_86_8B93",        # 56, 86
        "Function_87_8C53",        # 57, 87
        "Function_88_8D2E",        # 58, 88
        "Function_89_8DE0",        # 59, 89
        "Function_90_8EB7",        # 5A, 90
        "Function_91_8F5B",        # 5B, 91
        "Function_92_900D",        # 5C, 92
        "Function_93_90C6",        # 5D, 93
        "Function_94_9151",        # 5E, 94
        "Function_95_924F",        # 5F, 95
        "Function_96_929A",        # 60, 96
        "Function_97_937C",        # 61, 97
        "Function_98_941C",        # 62, 98
        "Function_99_9514",        # 63, 99
        "Function_100_9653",       # 64, 100
        "Function_101_96BE",       # 65, 101
        "Function_102_97A5",       # 66, 102
        "Function_103_98FA",       # 67, 103
        "Function_104_99C8",       # 68, 104
        "Function_105_9B59",       # 69, 105
        "Function_106_9BE5",       # 6A, 106
        "Function_107_9D30",       # 6B, 107
        "Function_108_9D85",       # 6C, 108
        "Function_109_9DFC",       # 6D, 109
        "Function_110_9E73",       # 6E, 110
        "Function_111_9F24",       # 6F, 111
        "Function_112_A0AB",       # 70, 112
    )


    def Function_0_102E(): pass

    label("Function_0_102E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1052")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_104F")
    Event(0, 16)

    label("loc_104F")

    Jump("loc_1073")

    label("loc_1052")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1073")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1073")
    Event(0, 17)

    label("loc_1073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_1084")
    OP_A3(0x2506)
    Event(0, 47)
    Jump("loc_10AB")

    label("loc_1084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_1095")
    OP_A3(0x2505)
    Event(0, 26)
    Jump("loc_10AB")

    label("loc_1095")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_10AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AB")
    OP_A3(0x2504)
    Event(0, 8)

    label("loc_10AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 0)), scpexpr(EXPR_END)), "loc_1196")
    OP_8C(0x1B, 0, 0)
    OP_8C(0x1C, 270, 0)
    OP_8C(0x1D, 225, 0)
    OP_8C(0x1E, 270, 0)
    OP_8C(0x1F, 360, 0)
    OP_8C(0x20, 0, 0)
    OP_8C(0x21, 90, 0)
    OP_8C(0x22, 270, 0)
    OP_8C(0x23, 180, 0)
    OP_8C(0x24, 0, 0)
    OP_8C(0x25, 270, 0)
    OP_8C(0x26, 135, 0)
    OP_8C(0x27, 115, 0)
    OP_8C(0x28, 270, 0)
    OP_8C(0x29, 180, 0)
    OP_8C(0x2A, 360, 0)
    OP_8C(0x2B, 180, 0)
    OP_8C(0x2C, 270, 0)
    SetChrPos(0x11, -370, 0, 21560, 180)
    SetChrPos(0x1B, -110, 0, 18900, 0)
    SetChrPos(0x1C, -1300, 0, 19540, 0)
    SetChrPos(0x1D, 870, 0, 20420, 270)
    SetChrPos(0x20, 3700, 0, 13120, 91)
    SetChrPos(0x23, 3670, 0, 7920, 180)

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_11CF")
    SetChrFlags(0x4D, 0x80)
    SetChrFlags(0x4B, 0x80)
    SetChrFlags(0x51, 0x80)
    SetChrFlags(0x44, 0x80)
    SetChrFlags(0x45, 0x80)
    SetChrFlags(0x49, 0x80)
    SetChrFlags(0x4A, 0x80)
    SetChrFlags(0x4F, 0x80)
    SetChrFlags(0x50, 0x80)
    SetChrFlags(0x52, 0x80)

    label("loc_11CF")

    OP_43(0x12, 0x0, 0x0, 0x6)
    OP_43(0x14, 0x0, 0x0, 0x6)
    OP_43(0x16, 0x0, 0x0, 0x6)
    OP_43(0x18, 0x0, 0x0, 0x6)
    OP_43(0x42, 0x0, 0x0, 0x6)
    OP_43(0x4D, 0x0, 0x0, 0x6)
    OP_43(0x36, 0x0, 0x0, 0x6)
    OP_43(0x4B, 0x0, 0x0, 0x6)
    Call(0, 25)
    Return()

    # Function_0_102E end

    def Function_1_120C(): pass

    label("Function_1_120C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_1221")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_1221")

    OP_1B(0x0, 0x0, 0xD)
    OP_1B(0x4, 0x0, 0x6C)
    OP_1B(0x5, 0x0, 0x6D)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_124C")
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    Jump("loc_1258")

    label("loc_124C")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)

    label("loc_1258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126A")
    OP_6F(0xB, 0)
    Jump("loc_1271")

    label("loc_126A")

    OP_6F(0xB, 60)

    label("loc_1271")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1283")
    OP_6F(0xC, 0)
    Jump("loc_128A")

    label("loc_1283")

    OP_6F(0xC, 60)

    label("loc_128A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129C")
    OP_6F(0xD, 0)
    Jump("loc_12A3")

    label("loc_129C")

    OP_6F(0xD, 60)

    label("loc_12A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B5")
    OP_6F(0xE, 0)
    Jump("loc_12BC")

    label("loc_12B5")

    OP_6F(0xE, 60)

    label("loc_12BC")

    Return()

    # Function_1_120C end

    def Function_2_12BD(): pass

    label("Function_2_12BD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13A2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_1331")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    Jump("loc_1316")

    label("loc_1316")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x25F8)
    Jump("loc_139F")

    label("loc_1331")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF6\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1380")

    label("loc_1380")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_139F")

    Jump("loc_13D5")

    label("loc_13A2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_13D5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_12BD end

    def Function_3_13E3(): pass

    label("Function_3_13E3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_1457")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    Jump("loc_143C")

    label("loc_143C")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x25F9)
    Jump("loc_14C5")

    label("loc_1457")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFE\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_14A6")

    label("loc_14A6")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_14C5")

    Jump("loc_14FB")

    label("loc_14C8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_14FB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_13E3 end

    def Function_4_1509(): pass

    label("Function_4_1509")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_157D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    Jump("loc_1562")

    label("loc_1562")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x25FA)
    Jump("loc_15EB")

    label("loc_157D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF6\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_15CC")

    label("loc_15CC")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_15EB")

    Jump("loc_1621")

    label("loc_15EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1621")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1509 end

    def Function_5_162F(): pass

    label("Function_5_162F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1714")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_16A3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xFE\x01\x07\x00。\x02",
    )

    Jump("loc_1688")

    label("loc_1688")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x25FB)
    Jump("loc_1711")

    label("loc_16A3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xFE\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFE\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_16F2")

    label("loc_16F2")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_1711")

    Jump("loc_1747")

    label("loc_1714")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1747")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_162F end

    def Function_6_1755(): pass

    label("Function_6_1755")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177A")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_18BC")

    label("loc_177A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1793")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_18BC")

    label("loc_1793")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17AC")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_18BC")

    label("loc_17AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C5")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_18BC")

    label("loc_17C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17DE")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_18BC")

    label("loc_17DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F7")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_18BC")

    label("loc_17F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1810")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_18BC")

    label("loc_1810")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1829")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_18BC")

    label("loc_1829")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1842")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_18BC")

    label("loc_1842")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_185B")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_18BC")

    label("loc_185B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1874")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_18BC")

    label("loc_1874")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_188D")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_18BC")

    label("loc_188D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A6")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_18BC")

    label("loc_18A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18BC")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_18BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18D1")
    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_18BC")

    label("loc_18D1")

    Return()

    # Function_6_1755 end

    def Function_7_18D2(): pass

    label("Function_7_18D2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_18F5")
    OP_8D(0xFE, 1950, -130840, 3370, -135280, 2000)
    Jump("Function_7_18D2")

    label("loc_18F5")

    Return()

    # Function_7_18D2 end

    def Function_8_18F6(): pass

    label("Function_8_18F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x109, 0x80)
    SetChrPos(0x109, 14170, 0, 16810, 270)
    SetChrPos(0x1A, 13860, 0, 12730, 270)
    SetChrPos(0x1B, 11840, 0, 2410, 90)
    SetChrPos(0x1C, 3340, 0, 12270, 90)
    SetChrPos(0x20, -3460, 0, 14470, 315)
    SetChrPos(0x23, 3450, 0, 14610, 45)
    OP_8C(0x24, 45, 0)
    OP_4A(0x12, 0)
    OP_4A(0x14, 0)
    OP_4A(0x16, 0)
    OP_4A(0x18, 0)
    OP_4A(0x1A, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1D, 0)
    OP_4A(0x1E, 0)
    OP_4A(0x1F, 0)
    OP_4A(0x20, 0)
    OP_4A(0x21, 0)
    OP_4A(0x22, 0)
    OP_4A(0x23, 0)
    OP_4A(0x24, 0)
    OP_4A(0x25, 0)
    OP_4A(0x26, 0)
    OP_4A(0x27, 0)
    OP_4A(0x28, 0)
    OP_4A(0x29, 0)
    OP_4A(0x2A, 0)
    OP_4A(0x2B, 0)
    OP_4A(0x2C, 0)
    OP_4A(0x2D, 0)
    OP_4A(0x2E, 0)
    OP_4A(0x2F, 0)
    OP_4A(0x30, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -250, 0, -2840, 0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-3910, 3570, 1000, 0)
    OP_6C(45000, 0)
    OP_67(0, 5510, -10000, 0)
    OP_6B(1400, 0)
    OP_6E(628, 0)

    def lambda_1A44():
        OP_6D(-2710, 3570, 23290, 20000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1A44)

    def lambda_1A5C():
        OP_6C(33000, 20000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A5C)
    OP_43(0x11, 0x0, 0x0, 0xB)
    OP_22(0xEA, 0x1, 0x64)
    OP_43(0x11, 0x3, 0x0, 0xC)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    def lambda_1AD3():

        label("loc_1AD3")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1AD3")

    QueueWorkItem2(0x1E, 1, lambda_1AD3)
    Sleep(200)

    def lambda_1AE9():

        label("loc_1AE9")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1AE9")

    QueueWorkItem2(0x1F, 1, lambda_1AE9)
    Sleep(600)

    def lambda_1AFF():

        label("loc_1AFF")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1AFF")

    QueueWorkItem2(0x1D, 1, lambda_1AFF)
    Sleep(100)

    def lambda_1B15():

        label("loc_1B15")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B15")

    QueueWorkItem2(0x24, 1, lambda_1B15)
    Sleep(600)

    def lambda_1B2B():

        label("loc_1B2B")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B2B")

    QueueWorkItem2(0x23, 1, lambda_1B2B)
    Sleep(100)

    def lambda_1B41():

        label("loc_1B41")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B41")

    QueueWorkItem2(0x29, 1, lambda_1B41)
    Sleep(100)

    def lambda_1B57():

        label("loc_1B57")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B57")

    QueueWorkItem2(0x2A, 1, lambda_1B57)
    Sleep(100)

    def lambda_1B6D():

        label("loc_1B6D")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B6D")

    QueueWorkItem2(0x20, 1, lambda_1B6D)
    Sleep(100)

    def lambda_1B83():

        label("loc_1B83")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B83")

    QueueWorkItem2(0x1C, 1, lambda_1B83)
    Sleep(100)

    def lambda_1B99():

        label("loc_1B99")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1B99")

    QueueWorkItem2(0x21, 1, lambda_1B99)
    Sleep(100)

    def lambda_1BAF():

        label("loc_1BAF")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1BAF")

    QueueWorkItem2(0x22, 1, lambda_1BAF)
    Sleep(100)

    def lambda_1BC5():

        label("loc_1BC5")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1BC5")

    QueueWorkItem2(0x1B, 1, lambda_1BC5)
    Sleep(200)

    def lambda_1BDB():

        label("loc_1BDB")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1BDB")

    QueueWorkItem2(0x25, 1, lambda_1BDB)
    Sleep(100)

    def lambda_1BF1():

        label("loc_1BF1")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1BF1")

    QueueWorkItem2(0x26, 1, lambda_1BF1)
    Sleep(100)

    def lambda_1C07():

        label("loc_1C07")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1C07")

    QueueWorkItem2(0x27, 1, lambda_1C07)
    Sleep(100)

    def lambda_1C1D():

        label("loc_1C1D")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1C1D")

    QueueWorkItem2(0x28, 1, lambda_1C1D)
    Sleep(100)

    def lambda_1C33():

        label("loc_1C33")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1C33")

    QueueWorkItem2(0x2B, 1, lambda_1C33)
    Sleep(100)

    def lambda_1C49():

        label("loc_1C49")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1C49")

    QueueWorkItem2(0x2C, 1, lambda_1C49)
    Sleep(1000)

    def lambda_1C5F():
        OP_8E(0xFE, 0x7B2, 0x0, 0x3458, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_1C5F)
    Sleep(200)

    def lambda_1C7F():
        OP_8E(0xFE, 0x8AC, 0x0, 0x2FA8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1C7F)
    WaitChrThread(0x1C, 0x1)
    WaitChrThread(0x23, 0x1)
    WaitChrThread(0x11, 0x0)
    OP_8C(0x11, 90, 400)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(300)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    OP_43(0x11, 0x0, 0x0, 0xA)

    def lambda_1CFC():

        label("loc_1CFC")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1CFC")

    QueueWorkItem2(0x23, 2, lambda_1CFC)

    def lambda_1D0D():

        label("loc_1D0D")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_1D0D")

    QueueWorkItem2(0x1C, 2, lambda_1D0D)
    Sleep(3500)
    Fade(1000)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x109, 0x2)
    OP_44(0x109, 0x3)
    OP_6D(1000, 1070, 29960, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(2490, 0)
    OP_6C(45000, 0)
    OP_6E(326, 0)
    OP_23(0xEA)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x11, 0x0)

    NpcTalk(    #12
        0x11,
        "主办人",
        "#5P各位，请安静。\x02",
    )

    Jump("loc_1DAA")

    label("loc_1DAA")

    CloseMessageWindow()

    NpcTalk(    #13
        0x11,
        "主办人",
        (
            "#5P今日承蒙各位光临\x01",
            "我们康莱特公司举办的宴会，\x01",
            "在此表示衷心感谢。\x02",
        )
    )

    Jump("loc_1E08")

    label("loc_1E08")

    CloseMessageWindow()

    NpcTalk(    #14
        0x11,
        "主办人",
        (
            "#5P各位可能都知道，\x01",
            "今日是值得纪念的……\x02",
        )
    )

    Jump("loc_1E4D")

    label("loc_1E4D")

    CloseMessageWindow()

    def lambda_1E54():
        OP_6D(14860, 0, 17520, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1E54)

    def lambda_1E6C():
        OP_67(0, 5000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1E6C)

    def lambda_1E84():
        OP_6C(33000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1E84)
    Sleep(4000)
    SetMessageWindowPos(0, 100, -1, -1)
    SetChrName("主办人")

    AnonymousTalk(    #15
        (
            "\x07\x00…………没错！\x02\x03",

            "#4P１０年前的今日，\x01",
            "我们康莱特公司……\x02",
        )
    )

    Jump("loc_1EF6")

    label("loc_1EF6")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    OP_62(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x1A, 0, 400)
    Sleep(500)

    def lambda_1F45():
        OP_6D(14860, 0, 18520, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1F45)
    OP_8F(0x1A, 0x36BA, 0x0, 0x3D2C, 0x3E8, 0x0)
    WaitChrThread(0x109, 0x0)
    Fade(500)
    OP_6D(14920, 0, 15780, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(1570, 0)
    OP_6C(135000, 0)
    OP_6E(480, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #16
        0x1A,
        (
            "#11P嘻嘻……\x01",
            "你好像觉得很无聊啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x1A,
        (
            "#11P不过，就算是假装，\x01",
            "也还是做出认真听的样子比较好哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x1A,
        (
            "#11P既然身在这里，\x01",
            "那位先生是怎样的人物，\x01",
            "你应该知道吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(1000, 1070, 29960, 0)
    OP_67(0, 5650, -10000, 0)
    OP_6B(2490, 0)
    OP_6C(45000, 0)
    OP_6E(326, 0)
    OP_0D()
    Sleep(500)
    OP_43(0x11, 0x0, 0x0, 0x9)
    Sleep(500)
    SetMessageWindowPos(250, 300, -1, -1)
    SetChrName("戴面具的绅士")

    AnonymousTalk(    #19
        (
            "\x07\x00#1600F──赫尔曼·康莱特。\x02\x03",

            "在那场『百日战役』中发家，\x01",
            "虽是暴发户却已成为帝国中屈指可数的资产家，\x01",
            "赫赫有名的军火商人。\x02\x03",

            "而且还是在几年前\x01",
            "与莱恩福尔特集团合作，\x01",
            "现在兼任其董事的人物──\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)
    Fade(500)
    OP_6D(14920, 0, 15780, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(1570, 0)
    OP_6C(135000, 0)
    OP_6E(480, 0)
    OP_0D()
    Sleep(500)
    OP_44(0x11, 0x0)

    NpcTalk(    #20
        0x109,
        "戴面具的绅士",
        (
            "#1600F#6P哎呀，从履历来看，\x01",
            "确实是个了不起的大人物啊。\x02\x03",

            "……不过说实话，\x01",
            "看到真人还真是有点失望啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x1A,
        (
            "#11P嘻嘻。\x01",
            "这种话你也敢说……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x1A,
        (
            "#11P就算戴着面具，\x01",
            "说不定也会被那边那些黑衣人\x01",
            "包围起来哦。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #23
        0x109,
        "戴面具的绅士",
        (
            "#1600F#6P呵呵，真吓人啊。\x02\x03",

            "一般来说，\x01",
            "像我这种粗人会被乱棒打出去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    Sleep(300)

    NpcTalk(    #24
        0x109,
        "戴面具的绅士",
        "#1603F#6P……打破玻璃从窗户扔出去。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x1A,
        "#11P嘻嘻，你真是有趣的人啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x1A,
        (
            "#11P是媒体的人……\x01",
            "不，也许更出人意料……\x01",
            "是政府官员吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 190, 400)

    NpcTalk(    #27
        0x109,
        "戴面具的绅士",
        (
            "#1600F#6P呵呵，随您想像。\x02\x03",

            "话虽如此……\x01",
            "真想不到这是在船上呢。\x02\x03",

            "更别说是在\x01",
            "距地面几千亚矩的高度……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x1A,
        (
            "#11P莱恩福尔特社\x01",
            "新出品的飞行客船……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x1A,
        (
            "#11P是当今世界最大的飞艇，\x01",
            "宣传词上是这么说的吧？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #30
        0x109,
        "戴面具的绅士",
        (
            "#1600F#6P从全长１２０亚矩的规模来看，\x01",
            "应该是这样没错。\x02\x03",

            "#1601F……至少在『表面世界』的范围内。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x1A,
        "#11P嘻嘻，话中有话啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x1A,
        (
            "#11P竟然用这种猜谜似的话\x01",
            "来吸引女人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x1A,
        (
            "#11P看你这么年轻，\x01",
            "没想到还挺老练的嘛。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #34
        0x109,
        "戴面具的绅士",
        (
            "#1603F#6P哦，被看穿了吗。\x02\x03",

            "#1600F哎呀哎呀……\x01",
            "趁着我还没露出更多马脚之前\x01",
            "似乎还是赶快撤退比较好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x1A,
        (
            "#11P嘻嘻……有心情的话\x01",
            "能再陪我聊天吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x1A,
        (
            "#11P像这样\x01",
            "和不知名的对象\x01",
            "愉快交谈的机会可不多呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2726():
        OP_6B(1400, 2200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2726)
    SetChrFlags(0x1A, 0x40)
    OP_8F(0x1A, 0x36BA, 0x0, 0x401A, 0x1F4, 0x0)
    WaitChrThread(0x109, 0x2)
    Sleep(500)

    ChrTalk(    #37
        0x1A,
        (
            "#11P……既然如此，\x01",
            "不如等宴会结束后\x01",
            "到你的房间去慢慢聊吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #38
        0x109,
        "戴面具的绅士",
        (
            "#1600F#6P呵呵……\x01",
            "光荣之至，女士。\x02\x03",

            "……若能瞒过女神的眼睛，\x01",
            "自然乐意效劳。\x02\x03",

            "#1601F不能去你房间的理由，\x01",
            "嗯，我就不问了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x1A,
        "#11P你真讨厌。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8F(0x109, 0x33CC, 0x0, 0x4164, 0x3E8, 0x0)
    Fade(500)
    OP_6D(13500, 0, 16790, 0)
    OP_67(0, 5680, -10000, 0)
    OP_6B(1570, 0)
    OP_6C(45000, 0)
    OP_6E(480, 0)
    OP_0D()
    OP_44(0x1B, 0x1)
    OP_44(0x1C, 0x1)
    OP_44(0x1D, 0x1)
    OP_44(0x1E, 0x1)
    OP_44(0x1F, 0x1)
    OP_44(0x20, 0x1)
    OP_44(0x21, 0x1)
    OP_44(0x22, 0x1)
    OP_44(0x23, 0x1)
    OP_44(0x24, 0x1)
    OP_44(0x1B, 0x2)
    OP_44(0x23, 0x2)
    OP_44(0x25, 0x1)
    OP_44(0x26, 0x1)
    OP_44(0x27, 0x1)
    OP_44(0x28, 0x1)
    OP_44(0x29, 0x1)
    OP_44(0x2A, 0x1)
    OP_44(0x2B, 0x1)
    OP_44(0x2C, 0x1)
    OP_8C(0x1B, 0, 0)
    OP_8C(0x1C, 270, 0)
    OP_8C(0x1D, 225, 0)
    OP_8C(0x1E, 270, 0)
    OP_8C(0x1F, 360, 0)
    OP_8C(0x20, 0, 0)
    OP_8C(0x21, 90, 0)
    OP_8C(0x22, 270, 0)
    OP_8C(0x23, 180, 0)
    OP_8C(0x24, 0, 0)
    OP_8C(0x25, 270, 0)
    OP_8C(0x26, 135, 0)
    OP_8C(0x27, 115, 0)
    OP_8C(0x28, 270, 0)
    OP_8C(0x29, 180, 0)
    OP_8C(0x2A, 360, 0)
    OP_8C(0x2B, 180, 0)
    OP_8C(0x2C, 270, 0)
    SetChrPos(0x11, -370, 0, 21560, 180)
    SetChrPos(0x1B, -110, 0, 18900, 0)
    SetChrPos(0x1C, -1300, 0, 19540, 0)
    SetChrPos(0x1D, 870, 0, 20420, 270)
    SetChrPos(0x20, 3700, 0, 13120, 91)
    SetChrPos(0x23, 3670, 0, 7920, 180)
    OP_43(0x11, 0x0, 0x0, 0x9)
    OP_43(0x1B, 0x0, 0x0, 0x9)
    OP_43(0x1C, 0x0, 0x0, 0x9)
    OP_43(0x1D, 0x0, 0x0, 0x9)

    def lambda_2A09():

        label("loc_2A09")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_2A09")

    QueueWorkItem2(0x1A, 0, lambda_2A09)

    def lambda_2A1A():
        OP_8F(0xFE, 0x3430, 0x0, 0x38E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2A1A)
    Sleep(500)

    def lambda_2A3A():
        OP_6D(11220, 0, 4480, 8000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A3A)
    WaitChrThread(0x109, 0x1)
    OP_8E(0x109, 0x283C, 0x0, 0xDFC, 0x7D0, 0x0)
    Sleep(300)
    OP_8C(0x109, 0, 400)
    Fade(500)
    OP_6D(760, 0, 21620, 0)
    OP_67(0, 5970, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(45000, 0)
    OP_6E(325, 0)
    OP_0D()
    SetChrPos(0x109, 900, 0, 9460, 0)
    Sleep(1000)

    NpcTalk(    #40
        0x109,
        "戴面具的绅士",
        (
            "#1602F#5P（宴会气氛正佳……\x01",
            "  差不多快到时候了吧。）\x02\x03",

            "（要穿过甲板才能到达\x01",
            "  最上层他的私人房间……）\x02\x03",

            "#1601F（好……开始行动吧。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(10300, 0, 3580, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x109, 10300, 0, 3580, 0)
    OP_0D()
    OP_44(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x40)
    SetChrPos(0x1A, 6300, 0, 13440, 270)
    OP_44(0x11, 0x0)
    OP_44(0x1B, 0x0)
    OP_44(0x1C, 0x0)
    OP_44(0x1D, 0x0)
    OP_43(0x11, 0x0, 0x0, 0x6)
    OP_43(0x1A, 0x0, 0x0, 0x6)
    OP_43(0x1B, 0x0, 0x0, 0x6)
    OP_43(0x1C, 0x0, 0x0, 0x6)
    OP_43(0x1D, 0x0, 0x0, 0x6)
    OP_4B(0x11, 0)
    OP_4B(0x12, 0)
    OP_4B(0x14, 0)
    OP_4B(0x16, 0)
    OP_4B(0x18, 0)
    OP_4B(0x1A, 0)
    OP_4B(0x1B, 0)
    OP_4B(0x1C, 0)
    OP_4B(0x1D, 0)
    OP_4B(0x1E, 0)
    OP_4B(0x1F, 0)
    OP_4B(0x20, 0)
    OP_4B(0x21, 0)
    OP_4B(0x22, 0)
    OP_4B(0x23, 0)
    OP_4B(0x24, 0)
    OP_4B(0x25, 0)
    OP_4B(0x26, 0)
    OP_4B(0x27, 0)
    OP_4B(0x28, 0)
    OP_4B(0x29, 0)
    OP_4B(0x2A, 0)
    OP_4B(0x2B, 0)
    OP_4B(0x2C, 0)
    OP_4B(0x2D, 0)
    OP_4B(0x2E, 0)
    OP_4B(0x2F, 0)
    OP_4B(0x30, 0)
    OP_A2(0x25E0)
    EventEnd(0x0)
    Return()

    # Function_8_18F6 end

    def Function_9_2C91(): pass

    label("Function_9_2C91")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D69")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CCD")
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_2D66")

    label("loc_2CCD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CF4")
    Sleep(1500)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_2D66")

    label("loc_2CF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1B")
    Sleep(2000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_2D66")

    label("loc_2D1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D42")
    Sleep(2500)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_2D66")

    label("loc_2D42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D66")
    Sleep(3000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    label("loc_2D66")

    Jump("Function_9_2C91")

    label("loc_2D69")

    Return()

    # Function_9_2C91 end

    def Function_10_2D6A(): pass

    label("Function_10_2D6A")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x0, 0x42E, 0x7148, 0x7D0, 0x0)
    Sleep(100)
    OP_8C(0xFE, 180, 400)
    Sleep(300)
    Return()

    # Function_10_2D6A end

    def Function_11_2D97(): pass

    label("Function_11_2D97")


    def lambda_2D9D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D9D)
    OP_8E(0xFE, 0x28, 0x0, 0x3084, 0x7D0, 0x0)
    Return()

    # Function_11_2D97 end

    def Function_12_2DBE(): pass

    label("Function_12_2DBE")

    Sleep(3000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS533._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS533._CH")
    OP_C6(0x0, 0x3, -1996488705, 1500, 0)
    OP_C6(0x1, 0x3, -1996488705, 1500, 0)
    Sleep(3000)
    OP_C6(0x0, 0x0, 100000, 0, 2500)
    OP_C6(0x1, 0x0, -100000, 0, 2500)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(4000)
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS534._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS534._CH")
    OP_C6(0x2, 0x3, -1996488705, 1500, 0)
    OP_C6(0x3, 0x3, -1996488705, 1500, 0)
    Sleep(3000)
    OP_C6(0x2, 0x0, 100000, 0, 2500)
    OP_C6(0x3, 0x0, -100000, 0, 2500)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    Return()

    # Function_12_2DBE end

    def Function_13_2F3C(): pass

    label("Function_13_2F3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 1)), scpexpr(EXPR_END)), "loc_2F4D")
    NewScene("ED6_DT21/E1110   ._SN", 101, 1, 0)
    IdleLoop()
    Return()

    label("loc_2F4D")

    EventBegin(0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 12000, 180)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 0, 400)
    Fade(500)
    OP_6D(-80, 0, 5270, 0)
    OP_67(0, 5120, -10000, 0)
    OP_6B(1260, 0)
    OP_6C(0, 0)
    OP_6E(590, 0)
    SetChrPos(0x109, 0, 0, 1270, 0)

    def lambda_2FE1():
        OP_6D(0, 0, 13110, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2FE1)

    def lambda_2FF9():
        OP_67(0, 4480, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2FF9)
    OP_43(0x10, 0x0, 0x0, 0xF)
    Sleep(4000)

    NpcTalk(    #41
        0x109,
        "戴面具的绅士",
        (
            "#1602F#5P（……………………………………）\x02\x03",

            "（真奇怪……\x01",
            "  好像有种被谁注视着的感觉……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #42
        0x109,
        "戴面具的绅士",
        (
            "#1600F#5P（……算了。\x01",
            "  赶快开始吧。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(630, 0, 2000, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(44000, 0)
    OP_6E(285, 0)
    OP_0D()
    OP_8C(0x109, 180, 400)
    Sleep(500)

    NpcTalk(    #43
        0x109,
        "戴面具的绅士",
        (
            "#1601F#5P（目标是甲板上面……\x01",
            "  最上层的私人房间。）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_43(0x109, 0x0, 0x0, 0xE)

    def lambda_3189():
        OP_6D(630, 0, 0, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3189)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x2)
    OP_A2(0x25E1)
    Sleep(1000)
    NewScene("ED6_DT21/E1110   ._SN", 101, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_13_2F3C end

    def Function_14_31C3(): pass

    label("Function_14_31C3")

    OP_8E(0xFE, 0xFFFFFF56, 0x0, 0xFFFFFC90, 0x7D0, 0x0)

    def lambda_31DD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31DD)
    OP_8E(0xFE, 0xFFFFFEE8, 0x0, 0xFFFFF150, 0x7D0, 0x0)
    Return()

    # Function_14_31C3 end

    def Function_15_31FE(): pass

    label("Function_15_31FE")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    Return()

    # Function_15_31FE end

    def Function_16_320A(): pass

    label("Function_16_320A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 6350, 0, -203180, 270)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_44(0x12, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x16, 0xFF)
    SetChrPos(0x12, 680, 0, -202850, 270)
    SetChrPos(0x14, -650, 0, -202040, 180)
    SetChrPos(0x16, -1100, 0, -204230, 0)
    SetChrChipByIndex(0x12, 3)
    SetChrChipByIndex(0x14, 4)
    SetChrChipByIndex(0x16, 4)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x16, 0)
    OP_6D(7830, 500, -202430, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(45000, 0)
    OP_6E(284, 0)

    def lambda_32D6():
        OP_6D(3050, 0, -202330, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_32D6)

    def lambda_32EE():
        OP_67(0, 7020, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_32EE)

    def lambda_3306():
        OP_6B(2670, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3306)

    def lambda_3316():
        OP_6E(284, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3316)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x109, 0x0)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_33A0():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_33A0)
    Sleep(100)

    def lambda_33B3():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_33B3)
    Sleep(100)
    OP_8C(0x16, 90, 600)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x16, 10)
    SetChrSubChip(0x16, 0)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 17)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    def lambda_3424():
        OP_6D(5520, 0, -202080, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3424)

    def lambda_343C():
        OP_67(0, 7020, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_343C)

    def lambda_3454():
        OP_6B(2150, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3454)

    def lambda_3464():
        OP_6E(275, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3464)
    SetChrChipByIndex(0x12, 6)

    def lambda_3479():
        OP_8F(0xFE, 0x1482, 0x0, 0xFFFCE5DC, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_3479)
    Sleep(30)
    SetChrChipByIndex(0x14, 11)

    def lambda_349E():
        OP_8F(0xFE, 0xFDB, 0x0, 0xFFFCE7B2, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_349E)
    Sleep(30)
    SetChrChipByIndex(0x16, 11)

    def lambda_34C3():
        OP_8F(0xFE, 0x107C, 0x0, 0xFFFCE276, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_34C3)
    WaitChrThread(0x109, 0x0)
    Battle(0x78, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_44(0x12, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x16, 0x0)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x800)
    SetChrPos(0x13, 1810, 0, -201990, 45)
    ClearChrFlags(0x55, 0x80)
    OP_9F(0x55, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x55, 2430, 0, -201300, 0)
    ClearChrFlags(0x56, 0x80)
    OP_9F(0x56, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x56, 2290, 0, -202020, 0)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 14)
    SetChrSubChip(0x15, 0)
    ClearChrFlags(0x15, 0x1)
    SetChrFlags(0x15, 0x800)
    SetChrPos(0x15, 930, 0, -204040, 90)
    ClearChrFlags(0x57, 0x80)
    OP_9F(0x57, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x57, 1330, 0, -204100, 0)
    ClearChrFlags(0x58, 0x80)
    OP_9F(0x58, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x58, 400, 0, -204320, 0)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x17, 14)
    SetChrSubChip(0x17, 0)
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x800)
    SetChrPos(0x17, -270, 0, -201860, 135)
    ClearChrFlags(0x59, 0x80)
    OP_9F(0x59, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x59, 130, 0, -202300, 0)
    ClearChrFlags(0x5A, 0x80)
    OP_9F(0x5A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x5A, -700, 0, -201900, 0)
    SetChrPos(0x109, 4490, 0, -203260, 270)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_6D(4490, 0, -203260, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    OP_A2(0x25EA)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_16_320A end

    def Function_17_36EE(): pass

    label("Function_17_36EE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -6370, 0, -202880, 90)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_44(0x12, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x16, 0xFF)
    SetChrPos(0x12, -1460, 0, -203170, 90)
    SetChrPos(0x14, 410, 0, -202170, 225)
    SetChrPos(0x16, -160, 0, -204510, 0)
    SetChrChipByIndex(0x12, 3)
    SetChrChipByIndex(0x14, 4)
    SetChrChipByIndex(0x16, 4)
    SetChrSubChip(0x12, 0)
    SetChrSubChip(0x14, 0)
    SetChrSubChip(0x16, 0)
    OP_6D(-5970, 0, -202340, 0)
    OP_67(0, 7090, -10000, 0)
    OP_6B(2430, 0)
    OP_6C(45000, 0)
    OP_6E(283, 0)

    def lambda_37BA():
        OP_6D(-2000, 0, -202240, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_37BA)

    def lambda_37D2():
        OP_67(0, 7020, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_37D2)

    def lambda_37EA():
        OP_6B(2670, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_37EA)

    def lambda_37FA():
        OP_6E(284, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_37FA)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x109, 0x0)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3884():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3884)
    Sleep(100)

    def lambda_3897():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3897)
    Sleep(100)
    OP_8C(0x16, 270, 600)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x12, 5)
    SetChrSubChip(0x12, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x14, 10)
    SetChrSubChip(0x14, 0)
    Sleep(50)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x16, 10)
    SetChrSubChip(0x16, 0)
    OP_0D()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 17)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    def lambda_3908():
        OP_6D(-4170, 0, -202320, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3908)

    def lambda_3920():
        OP_67(0, 7020, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3920)

    def lambda_3938():
        OP_6B(2150, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3938)

    def lambda_3948():
        OP_6E(275, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3948)
    SetChrChipByIndex(0x12, 6)

    def lambda_395D():
        OP_8F(0xFE, 0xFFFFEBC4, 0x0, 0xFFFCE79E, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_395D)
    Sleep(30)
    SetChrChipByIndex(0x14, 11)

    def lambda_3982():
        OP_8F(0xFE, 0xFFFFF09C, 0x0, 0xFFFCE9BA, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_3982)
    Sleep(30)
    SetChrChipByIndex(0x16, 11)

    def lambda_39A7():
        OP_8F(0xFE, 0xFFFFEFC0, 0x0, 0xFFFCE5BE, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_39A7)
    WaitChrThread(0x109, 0x0)
    Battle(0x78, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_44(0x12, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x16, 0x0)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x800)
    SetChrPos(0x13, -1540, 0, -203070, 270)
    ClearChrFlags(0x55, 0x80)
    OP_9F(0x55, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x55, -1850, 0, -202700, 0)
    ClearChrFlags(0x56, 0x80)
    OP_9F(0x56, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x56, -880, 0, -203000, 0)
    SetChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 14)
    SetChrSubChip(0x15, 0)
    ClearChrFlags(0x15, 0x1)
    SetChrFlags(0x15, 0x800)
    SetChrPos(0x15, 690, 0, -201320, 315)
    ClearChrFlags(0x57, 0x80)
    OP_9F(0x57, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x57, 170, 0, -201120, 0)
    ClearChrFlags(0x58, 0x80)
    OP_9F(0x58, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x58, 750, 0, -201740, 0)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x17, 14)
    SetChrSubChip(0x17, 0)
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x800)
    SetChrPos(0x17, 690, 0, -203800, 225)
    ClearChrFlags(0x59, 0x80)
    OP_9F(0x59, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x59, 370, 0, -204200, 0)
    ClearChrFlags(0x5A, 0x80)
    OP_9F(0x5A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x5A, 880, 0, -203500, 0)
    SetChrPos(0x109, -4900, 0, -202900, 90)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_6D(-4900, 0, -202900, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    OP_A2(0x25EB)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_17_36EE end

    def Function_18_3BD2(): pass

    label("Function_18_3BD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 4)), scpexpr(EXPR_END)), "loc_3BDD")
    Return()

    label("loc_3BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE6")
    Return()

    label("loc_3BE6")

    EventBegin(0x0)
    Fade(500)
    OP_6D(930, 0, -141490, 0)
    OP_67(0, 6440, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(45000, 0)
    OP_6E(259, 0)
    SetChrPos(0x109, -70, 0, -142470, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3C68():
        OP_6D(790, 0, -138040, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3C68)

    def lambda_3C80():
        OP_67(0, 5920, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3C80)

    def lambda_3C98():
        OP_6B(2850, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3C98)

    def lambda_3CA8():
        OP_6E(270, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3CA8)
    OP_44(0x18, 0xFF)
    OP_44(0x42, 0xFF)
    OP_44(0x4D, 0xFF)
    OP_44(0x36, 0xFF)
    OP_43(0x18, 0x0, 0x0, 0x13)
    OP_43(0x42, 0x0, 0x0, 0x14)
    OP_43(0x4D, 0x0, 0x0, 0x15)
    OP_43(0x36, 0x0, 0x0, 0x16)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x42, 0x0)
    WaitChrThread(0x4D, 0x0)
    WaitChrThread(0x36, 0x0)
    WaitChrThread(0x109, 0x0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 17)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    def lambda_3D17():
        OP_6D(720, 0, -139720, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D17)

    def lambda_3D2F():
        OP_67(0, 6200, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3D2F)

    def lambda_3D47():
        OP_6B(2450, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3D47)

    def lambda_3D57():
        OP_6E(255, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3D57)
    SetChrChipByIndex(0x18, 6)

    def lambda_3D6C():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3D6C)
    Sleep(30)
    SetChrChipByIndex(0x42, 6)

    def lambda_3D91():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x42, 0, lambda_3D91)
    Sleep(30)
    SetChrChipByIndex(0x4D, 11)

    def lambda_3DB6():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x4D, 0, lambda_3DB6)
    Sleep(30)
    SetChrChipByIndex(0x36, 11)

    def lambda_3DDB():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x36, 0, lambda_3DDB)
    WaitChrThread(0x109, 0x0)
    Battle(0x79, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_44(0x18, 0x0)
    OP_44(0x42, 0x0)
    OP_44(0x4D, 0x0)
    OP_44(0x36, 0x0)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x19, 9)
    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x19, 0x1)
    SetChrFlags(0x19, 0x800)
    SetChrPos(0x19, 2500, 0, -139480, 180)
    ClearChrFlags(0x5B, 0x80)
    OP_9F(0x5B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x5C, 0x80)
    OP_9F(0x5C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x42, 0x80)
    ClearChrFlags(0x43, 0x80)
    OP_51(0x43, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x43, 9)
    SetChrSubChip(0x43, 0)
    ClearChrFlags(0x43, 0x1)
    SetChrFlags(0x43, 0x800)
    SetChrPos(0x43, -2500, 0, -140020, 135)
    ClearChrFlags(0x5D, 0x80)
    OP_9F(0x5D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x5E, 0x80)
    OP_9F(0x5E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x4D, 0x80)
    ClearChrFlags(0x4E, 0x80)
    OP_51(0x4E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x4E, 14)
    SetChrSubChip(0x4E, 0)
    ClearChrFlags(0x4E, 0x1)
    SetChrFlags(0x4E, 0x800)
    SetChrPos(0x4E, 3200, 0, -136900, 270)
    ClearChrFlags(0x5F, 0x80)
    OP_9F(0x5F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x60, 0x80)
    OP_9F(0x60, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    OP_51(0x37, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x37, 14)
    SetChrSubChip(0x37, 0)
    ClearChrFlags(0x37, 0x1)
    SetChrFlags(0x37, 0x800)
    SetChrPos(0x37, -2440, 0, -137500, 135)
    ClearChrFlags(0x61, 0x80)
    OP_9F(0x61, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x62, 0x80)
    OP_9F(0x62, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x109, -340, 0, -140900, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_6D(-340, 0, -140900, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    OP_A2(0x25EC)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_18_3BD2 end

    def Function_19_3FFE(): pass

    label("Function_19_3FFE")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -6420, 0, -137240, 90)
    SetChrChipByIndex(0xFE, 3)

    def lambda_402A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_402A)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0x172, 0x0, 0xFFFDE69E, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 180, 400)
    OP_22(0xD5, 0x0, 0x64)
    Return()

    # Function_19_3FFE end

    def Function_20_4061(): pass

    label("Function_20_4061")

    Sleep(600)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, -6420, 0, -137240, 90)
    SetChrChipByIndex(0xFE, 3)

    def lambda_4092():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4092)
    SetChrChipByIndex(0xFE, 6)
    OP_8E(0xFE, 0xFFFFFAF6, 0x0, 0xFFFDE680, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 5)
    OP_8C(0xFE, 180, 400)
    OP_22(0xD5, 0x0, 0x64)
    Return()

    # Function_20_4061 end

    def Function_21_40C9(): pass

    label("Function_21_40C9")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 390, 0, -125960, 180)
    SetChrChipByIndex(0xFE, 4)
    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x294, 0x0, 0xFFFDEE82, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 10)
    OP_22(0xD8, 0x0, 0x64)
    Return()

    # Function_21_40C9 end

    def Function_22_4108(): pass

    label("Function_22_4108")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -2170, 0, -126000, 180)
    SetChrChipByIndex(0xFE, 4)
    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0xFFFFF970, 0x0, 0xFFFDEBA8, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 10)
    OP_22(0xD8, 0x0, 0x64)
    Return()

    # Function_22_4108 end

    def Function_23_4147(): pass

    label("Function_23_4147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 5)), scpexpr(EXPR_END)), "loc_4152")
    Return()

    label("loc_4152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_415B")
    Return()

    label("loc_415B")

    EventBegin(0x0)
    Fade(500)
    OP_6D(660, 0, -101930, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(2890, 0)
    OP_6C(45000, 0)
    OP_6E(252, 0)
    SetChrPos(0x109, -300, 0, -103010, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    ClearChrFlags(0x54, 0x80)
    SetChrChipByIndex(0x54, 5)
    SetChrSubChip(0x54, 0)
    SetChrPos(0x54, 1100, 0, -85000, 180)
    ClearChrFlags(0x53, 0x80)
    SetChrChipByIndex(0x53, 10)
    SetChrSubChip(0x53, 0)
    SetChrPos(0x53, -1000, 0, -85150, 180)
    ClearChrFlags(0x63, 0x80)
    ClearChrFlags(0x64, 0x80)
    SetChrPos(0x63, 1290, 0, -88670, 180)
    SetChrPos(0x64, -1420, 0, -88700, 180)
    SetChrFlags(0x63, 0x800)
    SetChrFlags(0x64, 0x800)
    OP_51(0x63, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x64, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4269():

        label("loc_4269")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_4269")

    QueueWorkItem2(0x63, 3, lambda_4269)

    def lambda_427C():

        label("loc_427C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_427C")

    QueueWorkItem2(0x64, 3, lambda_427C)

    def lambda_428F():
        OP_6D(1060, 350, -89440, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_428F)

    def lambda_42A7():
        OP_67(0, 4710, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_42A7)

    def lambda_42BF():
        OP_6B(3240, 2500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_42BF)

    def lambda_42CF():
        OP_6E(267, 2500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_42CF)
    OP_8F(0x109, 0xBE, 0x0, 0xFFFE8D92, 0x1388, 0x0)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #44
        0x53,
        "#5P来了吗……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x54,
        (
            "#2P赌上『北之猎兵』的名号，\x01",
            "你别想再前进一步！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #46
        0x109,
        "凯文·格拉汉姆",
        (
            "#1068F#4P呼～\x01",
            "果然是现役中生龙活虎的猎兵团……\x01",
            "而且还挺有名的嘛。\x02\x03",

            "#1066F贵国的情况我也有所了解，\x01",
            "不过这次你们能不能让开呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #47
        0x53,
        (
            "#5P闭嘴！\x01",
            "你到底了解我们什么！\x02",
        )
    )

    Jump("loc_441D")

    label("loc_441D")

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #48
        0x54,
        (
            "#2P为了我们因饥饿贫困而痛苦\x01",
            "的故乡诺桑比亚，\x01",
            "绝不可在此丢脸！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #49
        0x109,
        "凯文·格拉汉姆",
        (
            "#1065F……真是的。\x01",
            "这世道还真是艰苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 17)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #50
        0x109,
        "凯文·格拉汉姆",
        (
            "#1069F#4P好吧，\x01",
            "那我也要出全力了！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    def lambda_4531():
        OP_6D(450, 0, -92000, 300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4531)

    def lambda_4549():
        OP_67(0, 6230, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4549)

    def lambda_4561():
        OP_6B(2720, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4561)

    def lambda_4571():
        OP_6E(235, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_4571)
    SetChrChipByIndex(0x63, 35)

    def lambda_4586():

        label("loc_4586")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_4586")

    QueueWorkItem2(0x63, 3, lambda_4586)

    def lambda_4599():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x63, 0, lambda_4599)
    Sleep(30)
    SetChrChipByIndex(0x64, 35)

    def lambda_45BE():

        label("loc_45BE")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_45BE")

    QueueWorkItem2(0x64, 3, lambda_45BE)

    def lambda_45D1():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x64, 0, lambda_45D1)
    OP_43(0x64, 0x3, 0x0, 0x18)
    Sleep(10)
    SetChrChipByIndex(0x54, 6)

    def lambda_45FD():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x54, 0, lambda_45FD)
    Sleep(10)
    SetChrChipByIndex(0x53, 11)

    def lambda_4622():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x53, 0, lambda_4622)
    WaitChrThread(0x109, 0x0)
    Battle(0x7A, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_44(0x54, 0x0)
    OP_44(0x53, 0x0)
    OP_44(0x63, 0x0)
    OP_44(0x64, 0x0)
    OP_44(0x63, 0x3)
    OP_44(0x64, 0x3)
    OP_A2(0x25ED)
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/E1110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_4147 end

    def Function_24_4682(): pass

    label("Function_24_4682")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46A2")
    OP_22(0x13F, 0x0, 0x50)
    Sleep(150)
    OP_22(0x13F, 0x0, 0x50)
    Sleep(300)
    Jump("Function_24_4682")

    label("loc_46A2")

    Return()

    # Function_24_4682 end

    def Function_25_46A3(): pass

    label("Function_25_46A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 2)), scpexpr(EXPR_END)), "loc_482A")
    SetChrFlags(0x12, 0x80)
    OP_44(0x12, 0xFF)
    ClearChrFlags(0x13, 0x80)
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x800)
    SetChrPos(0x13, 1810, 0, -201990, 45)
    ClearChrFlags(0x55, 0x80)
    OP_9F(0x55, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x55, 2430, 0, -201300, 0)
    ClearChrFlags(0x56, 0x80)
    OP_9F(0x56, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x56, 2290, 0, -202020, 0)
    SetChrFlags(0x14, 0x80)
    OP_44(0x14, 0xFF)
    ClearChrFlags(0x15, 0x80)
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 14)
    SetChrSubChip(0x15, 0)
    ClearChrFlags(0x15, 0x1)
    SetChrFlags(0x15, 0x800)
    SetChrPos(0x15, 930, 0, -204040, 90)
    ClearChrFlags(0x57, 0x80)
    OP_9F(0x57, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x57, 1330, 0, -204100, 0)
    ClearChrFlags(0x58, 0x80)
    OP_9F(0x58, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x58, 400, 0, -204320, 0)
    SetChrFlags(0x16, 0x80)
    OP_44(0x16, 0xFF)
    ClearChrFlags(0x17, 0x80)
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x17, 14)
    SetChrSubChip(0x17, 0)
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x800)
    SetChrPos(0x17, -270, 0, -201860, 135)
    ClearChrFlags(0x59, 0x80)
    OP_9F(0x59, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x59, 130, 0, -202300, 0)
    ClearChrFlags(0x5A, 0x80)
    OP_9F(0x5A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x5A, -700, 0, -201900, 0)

    label("loc_482A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 3)), scpexpr(EXPR_END)), "loc_49B1")
    SetChrFlags(0x12, 0x80)
    OP_44(0x12, 0xFF)
    ClearChrFlags(0x13, 0x80)
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 9)
    SetChrSubChip(0x13, 0)
    ClearChrFlags(0x13, 0x1)
    SetChrFlags(0x13, 0x800)
    SetChrPos(0x13, -1540, 0, -203070, 270)
    ClearChrFlags(0x55, 0x80)
    OP_9F(0x55, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x55, -1850, 0, -202700, 0)
    ClearChrFlags(0x56, 0x80)
    OP_9F(0x56, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x56, -880, 0, -203000, 0)
    SetChrFlags(0x14, 0x80)
    OP_44(0x14, 0xFF)
    ClearChrFlags(0x15, 0x80)
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x15, 14)
    SetChrSubChip(0x15, 0)
    ClearChrFlags(0x15, 0x1)
    SetChrFlags(0x15, 0x800)
    SetChrPos(0x15, 690, 0, -201320, 315)
    ClearChrFlags(0x57, 0x80)
    OP_9F(0x57, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x57, 170, 0, -201120, 0)
    ClearChrFlags(0x58, 0x80)
    OP_9F(0x58, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x58, 750, 0, -201740, 0)
    SetChrFlags(0x16, 0x80)
    OP_44(0x16, 0xFF)
    ClearChrFlags(0x17, 0x80)
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x17, 14)
    SetChrSubChip(0x17, 0)
    ClearChrFlags(0x17, 0x1)
    SetChrFlags(0x17, 0x800)
    SetChrPos(0x17, 690, 0, -203800, 225)
    ClearChrFlags(0x59, 0x80)
    OP_9F(0x59, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x59, 370, 0, -204200, 0)
    ClearChrFlags(0x5A, 0x80)
    OP_9F(0x5A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x5A, 880, 0, -203500, 0)

    label("loc_49B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BD, 4)), scpexpr(EXPR_END)), "loc_4B30")
    SetChrFlags(0x18, 0x80)
    OP_44(0x18, 0xFF)
    ClearChrFlags(0x19, 0x80)
    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x19, 9)
    SetChrSubChip(0x19, 0)
    ClearChrFlags(0x19, 0x1)
    SetChrFlags(0x19, 0x800)
    SetChrPos(0x19, 2500, 0, -139480, 180)
    ClearChrFlags(0x5B, 0x80)
    OP_9F(0x5B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x5C, 0x80)
    OP_9F(0x5C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x42, 0x80)
    OP_44(0x42, 0xFF)
    ClearChrFlags(0x43, 0x80)
    OP_51(0x43, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x43, 9)
    SetChrSubChip(0x43, 0)
    ClearChrFlags(0x43, 0x1)
    SetChrFlags(0x43, 0x800)
    SetChrPos(0x43, -2500, 0, -140020, 135)
    ClearChrFlags(0x5D, 0x80)
    OP_9F(0x5D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x5E, 0x80)
    OP_9F(0x5E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x4D, 0x80)
    OP_44(0x4D, 0xFF)
    ClearChrFlags(0x4E, 0x80)
    OP_51(0x4E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x4E, 14)
    SetChrSubChip(0x4E, 0)
    ClearChrFlags(0x4E, 0x1)
    SetChrFlags(0x4E, 0x800)
    SetChrPos(0x4E, 3200, 0, -136900, 270)
    ClearChrFlags(0x5F, 0x80)
    OP_9F(0x5F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x60, 0x80)
    OP_9F(0x60, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x36, 0x80)
    OP_44(0x36, 0xFF)
    ClearChrFlags(0x37, 0x80)
    OP_51(0x37, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x37, 14)
    SetChrSubChip(0x37, 0)
    ClearChrFlags(0x37, 0x1)
    SetChrFlags(0x37, 0x800)
    SetChrPos(0x37, -2440, 0, -137500, 135)
    ClearChrFlags(0x61, 0x80)
    OP_9F(0x61, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x62, 0x80)
    OP_9F(0x62, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_4B30")

    Return()

    # Function_25_46A3 end

    def Function_26_4B31(): pass

    label("Function_26_4B31")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -170, 1070, 28810, 180)
    SetChrFlags(0x1B, 0x40)
    ClearChrFlags(0x54, 0x80)
    ClearChrFlags(0x53, 0x80)
    SetChrPos(0x54, 160, 1070, 27030, 0)
    SetChrPos(0x53, -1290, 1020, 26650, 45)
    SetChrFlags(0x54, 0x40)
    SetChrFlags(0x53, 0x40)
    SetChrPos(0x109, 10, 0, 11000, 0)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrPos(0x1B, 660, 0, 20500, 225)
    SetChrPos(0x20, 650, 0, 18760, 0)
    SetChrPos(0x23, -1060, 0, 19200, 45)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x20, 0x40)
    SetChrFlags(0x23, 0x40)
    SetChrPos(0x1C, -2290, 0, 16710, 0)
    SetChrPos(0x1D, 2490, 0, 17300, 45)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    OP_4A(0x11, 255)
    OP_4A(0x1B, 255)
    OP_4A(0x20, 255)
    OP_4A(0x23, 255)
    OP_4A(0x1C, 255)
    OP_4A(0x1D, 255)
    SetChrChipByIndex(0x23, 2)
    SetChrSubChip(0x23, 0)
    OP_6D(930, 1070, 28880, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(255, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #51
        0x11,
        (
            "#5P什、什么……\x01",
            "到底发生了什么事！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x54,
        "#4P恐、恐怕是入侵者……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x53,
        (
            "#6P而且看来……\x01",
            "似乎相当老练。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        (
            "#5P哼，我到底是为了什么\x01",
            "而雇你们来的啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x11,
        (
            "#5P下杀手也无所谓！\x01",
            "赶快给我消灭掉！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #56
        0x109,
        "凯文的声音",
        "#1P哎呀～这可不太现实啊。\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x54, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x53, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4E10():
        OP_6D(1470, 0, 21330, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4E10)

    def lambda_4E28():
        OP_67(0, 5580, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4E28)

    def lambda_4E40():
        OP_6B(3080, 2000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4E40)

    def lambda_4E50():
        OP_6E(278, 2000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_4E50)

    def lambda_4E60():
        OP_8C(0xFE, 180, 600)
        ExitThread()

    QueueWorkItem(0x54, 0, lambda_4E60)
    Sleep(100)
    OP_8C(0x53, 180, 600)

    def lambda_4E7A():

        label("loc_4E7A")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_4E7A")

    QueueWorkItem2(0x1B, 3, lambda_4E7A)

    def lambda_4E8B():

        label("loc_4E8B")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_4E8B")

    QueueWorkItem2(0x20, 3, lambda_4E8B)

    def lambda_4E9C():

        label("loc_4E9C")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_4E9C")

    QueueWorkItem2(0x23, 3, lambda_4E9C)

    def lambda_4EAD():

        label("loc_4EAD")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_4EAD")

    QueueWorkItem2(0x1C, 3, lambda_4EAD)

    def lambda_4EBE():

        label("loc_4EBE")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_4EBE")

    QueueWorkItem2(0x1D, 3, lambda_4EBE)
    OP_22(0xB0, 0x0, 0x64)
    WaitChrThread(0x11, 0x0)

    def lambda_4ED9():
        OP_8E(0xFE, 0xFFFFFE34, 0x0, 0x54B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4ED9)
    Sleep(500)

    def lambda_4EF9():
        OP_6B(3200, 1850)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4EF9)
    Sleep(1500)
    OP_43(0x20, 0x0, 0x0, 0x2A)
    Sleep(200)
    OP_43(0x23, 0x0, 0x0, 0x2B)
    Sleep(150)
    OP_43(0x1B, 0x0, 0x0, 0x29)

    def lambda_4F2D():
        OP_6D(1770, 0, 26480, 2500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_4F2D)

    def lambda_4F45():
        OP_67(0, 5170, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4F45)

    def lambda_4F5D():
        OP_6B(3080, 2500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4F5D)

    def lambda_4F6D():
        OP_6E(289, 2500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_4F6D)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #57
        0x11,
        "#5P你、你是什么人……\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #58
        0x11,
        "#5P教会的神父──难道！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #59
        0x109,
        "凯文·格拉汉姆",
        (
            "#1071F#4P哈哈，\x01",
            "不愧是持有这种东西的人，\x01",
            "对我们的存在很了解嘛。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x109, 15)
    SetChrSubChip(0x109, 0)
    SetChrFlags(0x109, 0x2)
    OP_22(0x8F, 0x0, 0x64)
    Sleep(500)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x109, 1)
    OP_0D()
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x11,
        "#5P你、你这小子……！\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #61
        0x11,
        (
            "#3S#5P还给我！！\x01",
            "这是我的私人财产！！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    CloseMessageWindow()

    NpcTalk(    #62
        0x109,
        "凯文·格拉汉姆",
        (
            "#1075F#4P十分遗憾，\x01",
            "这是要还给女神的东西。\x02\x03",

            "不是某一个人\x01",
            "可以随随便便拥有的。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #63
        0x11,
        "#5P#80W杀、杀了他………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #64
        0x11,
        (
            "#3S#5P赶快把这家伙杀掉，\x01",
            "把挂坠夺回来！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    CloseMessageWindow()

    def lambda_51ED():
        OP_6D(1190, 270, 24840, 1500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_51ED)

    def lambda_5205():
        OP_67(0, 4290, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5205)

    def lambda_521D():
        OP_6B(3050, 1500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_521D)

    def lambda_522D():
        OP_6E(289, 1500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_522D)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x54, 12)
    SetChrSubChip(0x54, 0)
    Sleep(100)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x53, 12)
    SetChrSubChip(0x53, 0)
    Sleep(100)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x2)
    OP_0D()
    Sleep(300)
    OP_22(0x15E, 0x0, 0x64)
    OP_62(0x20, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x20, 0x0, 0x0, 0x24)
    Sleep(30)
    OP_62(0x23, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x23, 0x0, 0x0, 0x25)
    OP_62(0x1C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x1C, 0x0, 0x0, 0x27)
    Sleep(50)
    OP_62(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x1B, 0x0, 0x0, 0x26)
    Sleep(100)
    Sleep(50)
    OP_62(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0x1D, 0x0, 0x0, 0x28)
    WaitChrThread(0x11, 0x0)
    LoadEffect(0x0, "monster\\msc0311.eff")
    LoadEffect(0x1, "monster\\ms10997.eff")
    LoadEffect(0x2, "scraft\\sc008_02.eff")
    LoadEffect(0x3, "monster\\ms31004a.eff")
    LoadEffect(0x4, "map\\mp009_00.eff")
    LoadEffect(0x5, "scraft\\sc000_11.eff")
    LoadEffect(0x6, "battle\\btgun10.eff")
    Fade(250)
    SetChrChipByIndex(0x109, 16)
    SetChrSubChip(0x109, 0)
    Sleep(500)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x109, 1)
    PlayEffect(0x2, 0xFF, 0xFF, -430, 1100, 22410, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD7, 0x0, 0x64)
    Sleep(300)
    PlayEffect(0x3, 0x0, 0x109, 0, 500, 0, 0, 0, 0, 3000, 3500, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)

    def lambda_5448():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5448)
    PlayEffect(0x0, 0x1, 0x53, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_548D():

        label("loc_548D")

        OP_99(0xFE, 0x0, 0x1, 0x9C4)
        OP_48()
        Jump("loc_548D")

    QueueWorkItem2(0x53, 3, lambda_548D)
    PlayEffect(0x0, 0x2, 0x54, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_54D5():

        label("loc_54D5")

        OP_99(0xFE, 0x0, 0x1, 0x9C4)
        OP_48()
        Jump("loc_54D5")

    QueueWorkItem2(0x54, 3, lambda_54D5)
    PlayEffect(0x1, 0xFF, 0xFF, -460, 500, 22500, 0, 45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x109, 0x0, 0x0, 0x2C)
    Sleep(2000)
    OP_82(0x1, 0x0)
    OP_44(0x53, 0x3)
    SetChrSubChip(0x53, 0)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x53, 10)
    SetChrSubChip(0x53, 0)
    Sleep(100)
    OP_44(0x54, 0x3)
    OP_82(0x2, 0x0)
    SetChrSubChip(0x54, 0)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x54, 10)
    SetChrSubChip(0x54, 0)
    OP_44(0x109, 0x0)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x53, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x54, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x0, 0x2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 17)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0x109, 19)
    OP_99(0x109, 0x0, 0x7, 0xBB8)
    OP_22(0xD8, 0x0, 0x64)

    def lambda_55FA():
        OP_6D(440, 1070, 26800, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_55FA)

    def lambda_5612():
        OP_67(0, 4290, -10000, 500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5612)

    def lambda_562A():
        OP_6B(2920, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_562A)

    def lambda_563A():
        OP_6E(289, 500)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_563A)

    def lambda_564A():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_564A)
    Sleep(300)
    OP_43(0x54, 0x0, 0x0, 0x2D)

    def lambda_5666():
        OP_99(0xFE, 0x7, 0xD, 0xFA0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5666)
    Sleep(200)
    OP_43(0x53, 0x0, 0x0, 0x2E)
    WaitChrThread(0x109, 0x1)
    SetChrSubChip(0x109, 7)
    Sleep(1500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #65
        0x11,
        "#5P#80W呜，哇……\x02",
    )

    CloseMessageWindow()

    def lambda_56B8():
        OP_6D(1500, 1070, 29500, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_56B8)

    def lambda_56D0():
        OP_67(0, 4290, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_56D0)

    def lambda_56E8():
        OP_6B(2900, 1500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_56E8)
    SetChrChipByIndex(0x109, 20)

    def lambda_56FD():
        OP_8E(0xFE, 0xFFFFFEE8, 0x42E, 0x6842, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_56FD)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_572F():
        OP_8F(0xFE, 0xFFFFFF56, 0x42E, 0x733C, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_572F)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x11, 0x3)
    WaitChrThread(0x11, 0x0)
    Sleep(500)

    NpcTalk(    #66
        0x109,
        "凯文·格拉汉姆",
        (
            "#1065F#4P赫尔曼·康莱特。\x02\x03",

            "#1063F根据教会法，\x01",
            "以空之女神爱德丝之名\x01",
            "将你逮捕。\x02\x03",

            "罪名是涉嫌非法持有及使用\x01",
            "『古代遗物』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        (
            "#5P你、你以为做这种事\x01",
            "还能全身而退吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x11,
        (
            "#5P就算是七耀教会，\x01",
            "竟敢对身为莱恩福尔特\x01",
            "董事长的我下手……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #69
        0x109,
        "凯文·格拉汉姆",
        (
            "#1068F#4P啊～关于这个\x01",
            "我也和他们说好了。\x02\x03",

            "#1066F反正你不过是用这东西\x01",
            "大肆乱来而已吧？\x02\x03",

            "而且好像在各方面\x01",
            "都引起了不少问题吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        "#5P#3S！！！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #71
        0x109,
        "凯文·格拉汉姆",
        (
            "#1075F#4P像你这样的外来人员\x01",
            "似乎树敌相当多嘛。\x02\x03",

            "#1060F唔，你就当是运气不好，\x01",
            "乖乖束手就擒吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x11,
        "#5P#80W呜呜……\x02",
    )

    CloseMessageWindow()

    def lambda_59D6():
        OP_6D(1500, 1070, 30000, 1500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_59D6)
    SetChrFlags(0x11, 0x40)
    OP_8F(0x11, 0xFFFFFF56, 0x42E, 0x7530, 0x1F4, 0x0)
    Fade(250)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 1)
    SetChrFlags(0x11, 0x2)
    OP_0D()

    def lambda_5A1C():
        OP_6B(2750, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5A1C)
    OP_22(0xD8, 0x0, 0x64)
    SetChrSubChip(0x11, 2)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    ChrTalk(    #73 op#A op#5
        0x11,
        "#5P#4S#8A呜哇啊啊啊啊啊！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_5A7C():
        OP_6D(1000, 1070, 31000, 200)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_5A7C)

    def lambda_5A94():
        OP_67(0, 4290, -10000, 200)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5A94)

    def lambda_5AAC():
        OP_6B(2750, 200)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5AAC)

    def lambda_5ABC():
        OP_6E(260, 200)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_5ABC)
    OP_7D(0x0, 0x109, 0x32, 0x1F4)
    OP_22(0xCB, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)

    def lambda_5AE3():
        OP_8F(0xFE, 0xFFFFFD62, 0x42E, 0x6F54, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5AE3)
    WaitChrThread(0x109, 0x0)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 3)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x11, 0x800)
    SetChrFlags(0x109, 0x8)
    SetChrPos(0x109, -670, 1070, 29000, 0)
    Sleep(50)
    SetChrSubChip(0x11, 4)
    OP_22(0x1FB, 0x0, 0x64)
    OP_22(0x209, 0x0, 0x64)

    def lambda_5B41():
        OP_7C(0x28, 0x28, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_5B41)
    OP_7D(0x1, 0x109, 0x0, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    ChrTalk(    #74 op#A op#5
        0x11,
        "#5P#15A呜……\x05\x02",
    )

    CloseMessageWindow()
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0x11, 0x5, 0x8, 0x3E8)
    Sleep(1000)

    NpcTalk(    #75
        0x109,
        "凯文·格拉汉姆",
        (
            "#1067F#4P……真是的。\x01",
            "又给我添多余的麻烦。\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x11, 0x9, 0xC, 0x3E8)
    Sleep(500)

    NpcTalk(    #76
        0x109,
        "凯文·格拉汉姆",
        (
            "#1068F#5P本来还觉得\x01",
            "这次任务相当简单呢……\x02\x03",

            "要把这家伙活捉回去\x01",
            "也的确是很费事啊……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x65, 0x80)
    SetChrPos(0x65, -430, 0, 13590, 0)
    ClearChrFlags(0x66, 0x80)
    ClearChrFlags(0x67, 0x80)
    ClearChrFlags(0x68, 0x80)
    ClearChrFlags(0x69, 0x80)
    ClearChrFlags(0x6A, 0x80)
    ClearChrFlags(0x6B, 0x80)
    ClearChrFlags(0x6C, 0x80)
    SetChrPos(0x66, 800, 0, 12480, 0)
    SetChrPos(0x67, -1980, 0, 11780, 0)
    SetChrPos(0x68, -630, 0, 10730, 0)
    SetChrPos(0x69, 580, 0, 10220, 0)
    SetChrPos(0x6A, -2310, 0, 9980, 0)
    SetChrPos(0x6B, -1290, 0, 8820, 0)
    SetChrPos(0x6C, -330, 0, 7600, 0)
    Sleep(500)

    NpcTalk(    #77
        0x65,
        "男人的声音",
        "#3S到此为止了！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x109, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_43(0x65, 0x1, 0x0, 0x1C)
    OP_43(0x66, 0x1, 0x0, 0x1D)
    OP_43(0x67, 0x1, 0x0, 0x1E)
    OP_43(0x68, 0x1, 0x0, 0x1F)
    OP_43(0x69, 0x1, 0x0, 0x20)
    OP_43(0x6A, 0x1, 0x0, 0x21)
    OP_43(0x6B, 0x1, 0x0, 0x22)
    OP_43(0x6C, 0x1, 0x0, 0x23)
    Fade(500)
    OP_6D(580, 1000, 25220, 0)
    OP_67(0, 4270, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    OP_0D()
    OP_99(0x11, 0xD, 0x13, 0x5DC)
    WaitChrThread(0x65, 0x1)
    WaitChrThread(0x66, 0x1)
    WaitChrThread(0x67, 0x1)
    WaitChrThread(0x68, 0x1)
    WaitChrThread(0x69, 0x1)
    WaitChrThread(0x6A, 0x1)
    WaitChrThread(0x6B, 0x1)
    WaitChrThread(0x6C, 0x1)
    Sleep(300)

    NpcTalk(    #78
        0x109,
        "凯文·格拉汉姆",
        (
            "#1060F#5P哦……\x01",
            "全副武装的家伙们来了啊。\x02\x03",

            "不愧是有名的『北之猎兵』。\x01",
            "应对很迅速呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x65,
        (
            "#6P住口……！\x02\x03",

            "现在面对全副武装的我们，\x01",
            "别以为还能像之前那样！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x66,
        (
            "#4P我可告诉你，这艘飞艇上\x01",
            "有一个中队的战斗力！\x02\x03",

            "就算你有人质\x01",
            "也是无处可逃！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #81
        0x109,
        "凯文·格拉汉姆",
        (
            "#1075F#5P呼……\x02\x03",

            "这次我们双方都很幸运呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x66,
        "#4P啊……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x65,
        "#6P你、你说什么呢？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #84
        0x109,
        "凯文·格拉汉姆",
        (
            "#1075F#5P如果这个小恶党\x01",
            "被认定是『异端』的话……\x02\x03",

            "#1073F搞不好你们所有人\x01",
            "都要被『制裁』了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x67, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x66, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x6C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x6B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x69, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x68, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x6A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x65, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #85
        0x65,
        "#6P什……\x02",
    )

    Jump("loc_6128")

    label("loc_6128")

    CloseMessageWindow()

    ChrTalk(    #86
        0x66,
        "#4P这、这家伙……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #87
        0x109,
        "凯文·格拉汉姆",
        (
            "#1072F#5P不过，你们不要为这个而气馁，\x01",
            "为了故乡复兴而好好努力吧。\x02\x03",

            "只要小心不成为\x01",
            "我们『骑士团』的猎物就行了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(0, 1000, 32000, 0)
    OP_67(0, 4160, -10000, 0)
    OP_6B(2040, 0)
    OP_6C(0, 0)
    OP_6E(376, 0)
    SetChrChipByIndex(0x11, 21)
    SetChrSubChip(0x11, 22)
    OP_0D()
    OP_43(0x11, 0x0, 0x0, 0x1B)

    def lambda_623E():
        OP_6D(3420, 1550, 35070, 600)
        ExitThread()

    QueueWorkItem(0x65, 0, lambda_623E)

    def lambda_6256():
        OP_67(0, 5290, -10000, 600)
        ExitThread()

    QueueWorkItem(0x65, 1, lambda_6256)

    def lambda_626E():
        OP_6B(1690, 2000)
        ExitThread()

    QueueWorkItem(0x65, 2, lambda_626E)

    def lambda_627E():
        OP_6C(12000, 600)
        ExitThread()

    QueueWorkItem(0x65, 3, lambda_627E)

    def lambda_628E():
        OP_6E(427, 2000)
        ExitThread()

    QueueWorkItem(0x66, 1, lambda_628E)
    Sleep(300)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E1100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_26_4B31 end

    def Function_27_62CC(): pass

    label("Function_27_62CC")

    SetChrFlags(0x11, 0x4)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_62DC():
        OP_99(0xFE, 0x14, 0x15, 0x5DC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_62DC)
    WaitChrThread(0x11, 0x2)
    SetChrFlags(0x11, 0x800)
    OP_22(0xA3, 0x0, 0x64)
    OP_7D(0x0, 0x11, 0x32, 0x1F4)

    def lambda_6303():
        OP_96(0xFE, 0x12AC, 0xFFFFEC78, 0x8F16, 0x5DC, 0x1388)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6303)
    Return()

    # Function_27_62CC end

    def Function_28_631C(): pass

    label("Function_28_631C")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0xFFFFFE2A, 0x0, 0x5546, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_28_631C end

    def Function_29_6340(): pass

    label("Function_29_6340")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0x53C, 0x0, 0x5294, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_29_6340 end

    def Function_30_6364(): pass

    label("Function_30_6364")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0xFFFFF7C2, 0x0, 0x53B6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_30_6364 end

    def Function_31_6388(): pass

    label("Function_31_6388")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0xFFFFFBE6, 0x0, 0x4F06, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_31_6388 end

    def Function_32_63AC(): pass

    label("Function_32_63AC")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0x352, 0x0, 0x4CFE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_32_63AC end

    def Function_33_63D0(): pass

    label("Function_33_63D0")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0xFFFFF254, 0x0, 0x4C40, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_33_63D0 end

    def Function_34_63F4(): pass

    label("Function_34_63F4")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0xFFFFF66E, 0x0, 0x4948, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_34_63F4 end

    def Function_35_6418(): pass

    label("Function_35_6418")

    SetChrChipByIndex(0xFE, 23)
    OP_8F(0xFE, 0xFFFFFCC2, 0x0, 0x46E6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 22)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_35_6418 end

    def Function_36_643C(): pass

    label("Function_36_643C")

    OP_44(0xFE, 0x3)
    OP_8C(0xFE, 180, 600)
    OP_8E(0xFE, 0x29E, 0x0, 0x276A, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_36_643C end

    def Function_37_6461(): pass

    label("Function_37_6461")

    OP_44(0xFE, 0x3)
    OP_8C(0xFE, 270, 600)
    OP_8E(0xFE, 0xFFFFD5E4, 0x0, 0x4704, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_37_6461 end

    def Function_38_6486(): pass

    label("Function_38_6486")

    OP_44(0xFE, 0x3)
    OP_8C(0xFE, 180, 600)
    OP_8E(0xFE, 0x238C, 0x0, 0x3F20, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_38_6486 end

    def Function_39_64AB(): pass

    label("Function_39_64AB")

    OP_44(0xFE, 0x3)
    OP_8C(0xFE, 180, 600)
    OP_8E(0xFE, 0xFFFFF3F8, 0x0, 0x2576, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_39_64AB end

    def Function_40_64D0(): pass

    label("Function_40_64D0")

    OP_44(0xFE, 0x3)
    OP_8C(0xFE, 180, 600)
    OP_8E(0xFE, 0x6F4, 0x0, 0x25A8, 0x1770, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_40_64D0 end

    def Function_41_64F5(): pass

    label("Function_41_64F5")

    OP_8F(0xFE, 0xAA0, 0x0, 0x50E6, 0x7D0, 0x0)
    Return()

    # Function_41_64F5 end

    def Function_42_650A(): pass

    label("Function_42_650A")

    OP_8F(0xFE, 0x74E, 0x0, 0x49B6, 0x7D0, 0x0)
    Return()

    # Function_42_650A end

    def Function_43_651F(): pass

    label("Function_43_651F")

    OP_8F(0xFE, 0xFFFFF56A, 0x0, 0x4B6E, 0x7D0, 0x0)
    Return()

    # Function_43_651F end

    def Function_44_6534(): pass

    label("Function_44_6534")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65EE")
    PlayEffect(0x4, 0xFF, 0xFF, -260, 600, 23000, 0, 45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x4, 0xFF, 0xFF, 460, 500, 22500, 0, 45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x4, 0xFF, 0xFF, 0, 700, 22000, 0, 45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    Jump("Function_44_6534")

    label("loc_65EE")

    Return()

    # Function_44_6534 end

    def Function_45_65EF(): pass

    label("Function_45_65EF")

    PlayEffect(0x6, 0x3, 0x109, 0, 1250, 750, 0, 0, 0, 500, 500, 500, 0x54, 0, 500, 0, 0)
    OP_22(0x1F6, 0x0, 0x64)
    Sleep(200)
    OP_8C(0xFE, 225, 0)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_667A():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_667A)

    def lambda_6694():
        OP_7C(0x1E, 0x1E, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6694)

    def lambda_66AC():
        OP_96(0xFE, 0xA8C, 0x3E8, 0x7724, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_66AC)
    WaitChrThread(0xFE, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x800)
    Return()

    # Function_45_65EF end

    def Function_46_66E3(): pass

    label("Function_46_66E3")

    PlayEffect(0x6, 0x3, 0x109, 0, 1250, 750, 0, 0, 0, 500, 500, 500, 0x53, 0, 500, 0, 0)
    OP_22(0x1F6, 0x0, 0x64)
    Sleep(200)
    OP_8C(0xFE, 135, 0)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_676E():
        OP_9E(0xFE, 0x14, 0x0, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_676E)

    def lambda_6788():
        OP_7C(0x1E, 0x1E, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6788)

    def lambda_67A0():
        OP_96(0xFE, 0xFFFFF556, 0x3E8, 0x7724, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_67A0)
    WaitChrThread(0xFE, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    ClearChrFlags(0xFE, 0x1)
    SetChrFlags(0xFE, 0x800)
    Return()

    # Function_46_66E3 end

    def Function_47_67D7(): pass

    label("Function_47_67D7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_71(0x409, 0x0)
    ExitThread()
    OP_72(0x40A, 0x0)
    ExitThread()
    SetChrFlags(0x109, 0x80)
    ClearChrFlags(0x65, 0x80)
    ClearChrFlags(0x66, 0x80)
    ClearChrFlags(0x67, 0x80)
    ClearChrFlags(0x68, 0x80)
    ClearChrFlags(0x69, 0x80)
    ClearChrFlags(0x6A, 0x80)
    ClearChrFlags(0x6B, 0x80)
    ClearChrFlags(0x6C, 0x80)
    SetChrPos(0x65, 2180, 1000, 31360, 45)
    SetChrPos(0x66, 4150, 1000, 29590, 0)
    SetChrPos(0x67, 890, 1000, 30840, 45)
    SetChrPos(0x68, -1480, 1000, 30440, 45)
    SetChrPos(0x69, 3100, 1000, 27910, 0)
    SetChrPos(0x6A, 380, 1000, 28930, 45)
    SetChrPos(0x6B, -680, 1000, 27990, 45)
    SetChrPos(0x6C, 1100, 1000, 27030, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -140, 0, 9680, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrPos(0x1A, 1530, 0, 16510, 0)
    SetChrPos(0x1B, 20, 0, 17600, 0)
    SetChrPos(0x1C, -1080, 0, 16600, 0)
    SetChrPos(0x1D, 710, 0, 15170, 0)
    SetChrPos(0x1E, -290, 0, 15120, 0)
    SetChrPos(0x1F, 2400, 0, 14670, 0)
    SetChrPos(0x20, -3340, 0, 13820, 45)
    SetChrPos(0x21, -2480, 0, 17130, 0)
    SetChrPos(0x22, 4970, 0, 18670, 0)
    SetChrPos(0x23, -4860, 0, 18200, 45)
    SetChrPos(0x24, -2520, 0, 13550, 0)
    OP_8C(0x27, 45, 0)
    OP_8C(0x28, 0, 0)
    SetChrPos(0x2D, 2800, 0, 12100, 0)
    SetChrPos(0x2E, 3630, 0, 12040, 315)
    SetChrPos(0x2F, -1940, 0, 12660, 0)
    SetChrPos(0x30, 6290, 0, 13380, 315)
    ClearChrFlags(0x54, 0x80)
    SetChrPos(0x54, 3000, 1000, 30000, 225)
    SetChrChipByIndex(0x54, 14)
    SetChrSubChip(0x54, 0)
    ClearChrFlags(0x54, 0x1)
    SetChrFlags(0x54, 0x800)
    ClearChrFlags(0x53, 0x80)
    SetChrPos(0x53, -2730, 1000, 30500, 135)
    SetChrChipByIndex(0x53, 14)
    SetChrSubChip(0x53, 0)
    ClearChrFlags(0x53, 0x1)
    SetChrFlags(0x53, 0x800)
    OP_4A(0x12, 0)
    OP_4A(0x14, 0)
    OP_4A(0x16, 0)
    OP_4A(0x18, 0)
    OP_4A(0x1A, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1D, 0)
    OP_4A(0x1E, 0)
    OP_4A(0x1F, 0)
    OP_4A(0x20, 0)
    OP_4A(0x21, 0)
    OP_4A(0x22, 0)
    OP_4A(0x23, 0)
    OP_4A(0x24, 0)
    OP_4A(0x25, 0)
    OP_4A(0x26, 0)
    OP_4A(0x27, 0)
    OP_4A(0x28, 0)
    OP_4A(0x29, 0)
    OP_4A(0x2A, 0)
    OP_4A(0x2B, 0)
    OP_4A(0x2C, 0)
    OP_4A(0x2D, 0)
    OP_4A(0x2E, 0)
    OP_4A(0x2F, 0)
    OP_4A(0x30, 0)
    OP_6D(2570, 1000, 33180, 0)
    OP_67(0, 4580, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(0, 0)
    OP_6E(282, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #88
        0x65,
        "#5P怎、怎么可能……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x66,
        (
            "『星杯骑士团』……\x01",
            "到底是一群怎样的家伙啊……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_20(0x2710)
    Fade(1000)
    OP_6D(1280, 0, 18500, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(44000, 0)
    OP_6E(289, 0)

    def lambda_6B91():
        OP_6D(1230, 0, 11100, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6B91)
    OP_22(0xB0, 0x0, 0x64)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    def lambda_6BBE():
        OP_6B(2500, 8000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6BBE)

    ChrTalk(    #90
        0x10,
        (
            "\x07\x02#5P呵呵……\x01",
            "还挺能给人找乐子的。\x02\x03",

            "不过，事情现在才刚开始呢，\x01",
            "凯文·格拉汉姆──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 225, 300)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_47_67D7 end

    def Function_48_6C4E(): pass

    label("Function_48_6C4E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6C7E")
    OP_A2(0x0)

    ChrTalk(    #91
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_6CBA")

    label("loc_6C7E")


    ChrTalk(    #92
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "……请问您有何贵干？\x02",
    )

    CloseMessageWindow()

    label("loc_6CBA")

    TalkEnd(0xFE)
    Return()

    # Function_48_6C4E end

    def Function_49_6CBE(): pass

    label("Function_49_6CBE")

    TalkBegin(0xFE)

    ChrTalk(    #94
        0xFE,
        (
            "会场内的安全\x01",
            "由我们来保障。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "请您放心。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_49_6CBE end

    def Function_50_6CFA(): pass

    label("Function_50_6CFA")

    TalkBegin(0xFE)

    ChrTalk(    #96
        0xFE,
        (
            "……请不用在意\x01",
            "我们的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "在这里好好放松一下吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_50_6CFA end

    def Function_51_6D40(): pass

    label("Function_51_6D40")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6DB8")
    OP_A2(0x1)

    ChrTalk(    #98
        0xFE,
        (
            "实在抱歉，\x01",
            "我们的打扮可能不合风趣。\x01",
            "但这都是为了保障大家的安全……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "还请您多多理解和宽容。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6E28")

    label("loc_6DB8")


    ChrTalk(    #100
        0xFE,
        (
            "实在抱歉，\x01",
            "我们的打扮可能不合风趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "但这也是为了\x01",
            "大家的安全着想……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "还请您多多理解和宽容。\x02",
    )

    CloseMessageWindow()

    label("loc_6E28")

    TalkEnd(0xFE)
    Return()

    # Function_51_6D40 end

    def Function_52_6E2C(): pass

    label("Function_52_6E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E38")
    Call(0, 53)

    label("loc_6E38")

    Return()

    # Function_52_6E2C end

    def Function_53_6E39(): pass

    label("Function_53_6E39")

    EventBegin(0x1)
    TurnDirection(0x0, 0x11, 400)
    OP_6D(80, 0, 20820, 1500)
    Fade(500)
    OP_4A(0x11, 0)
    OP_4A(0x1B, 0)
    OP_4A(0x1C, 0)
    OP_4A(0x1D, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_6F26")

    ChrTalk(    #103
        0x11,
        (
            "……啊，嗯嗯………\x01",
            "………这当然。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x11,
        "而我们公司今后的展望也……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #105
        0x109,
        "戴面具的绅士",
        (
            "#1600F（呵呵……\x01",
            "  看来气氛很热闹啊。）\x02\x03",

            "#1601F（你们就趁现在\x01",
            "  好好玩个痛快吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70BE")

    label("loc_6F26")


    ChrTalk(    #106
        0x1C,
        (
            "哇哈哈……！\x01",
            "真有一手啊，康莱特君。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x1C,
        (
            "竟然在天上开宴会……\x01",
            "其他的资本家真是可望不可及啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x1D,
        "嘻嘻，一点不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x11,
        "哈哈哈，看来你们很满意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x11,
        (
            "不过这还只是余兴而已哦。\x01",
            "今后还会为大家……\x02",
        )
    )

    CloseMessageWindow()
    OP_69(0x0, 0x5DC)

    NpcTalk(    #111
        0x109,
        "戴面具的绅士",
        (
            "#1602F（哦…………\x01",
            "  这是以挥霍出名的巴拉德侯爵\x01",
            "  以及珠宝店『柯利兹商会』的女社长啊。）\x02\x03",

            "#1602F（谄媚的也都是富豪啊。）\x02\x03",

            "#1601F（呵呵……\x01",
            "  就请暂时享受一下宴会吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70BE")

    Sleep(500)
    Fade(500)
    OP_4B(0x11, 0)
    OP_4B(0x1B, 0)
    OP_4B(0x1C, 0)
    OP_4B(0x1D, 0)
    SetChrPos(0x109, 100, 0, 16140, 174)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x2)
    EventEnd(0x1)
    Return()

    # Function_53_6E39 end

    def Function_54_70F7(): pass

    label("Function_54_70F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_71B8")

    ChrTalk(    #112
        0x11,
        (
            "……啊，嗯嗯………\x01",
            "………这当然。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x11,
        "而我们公司今后的展望也……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #114
        0x109,
        "戴面具的绅士",
        (
            "#1600F（呵呵……\x01",
            "  看来气氛很热闹啊。）\x02\x03",

            "#1601F（你们就趁现在\x01",
            "  好好玩个痛快吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71BC")

    label("loc_71B8")

    Call(0, 52)

    label("loc_71BC")

    TalkEnd(0xFE)
    Return()

    # Function_54_70F7 end

    def Function_55_71C0(): pass

    label("Function_55_71C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_7261")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x0, 450)

    ChrTalk(    #115
        0x1A,
        "哎呀，你是之前的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x1A,
        (
            "嘻嘻，\x01",
            "请别忘了我刚才的话哦。\x02",
        )
    )

    Jump("loc_7231")

    label("loc_7231")

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "我在这边也会\x01",
            "做好适当应对的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 0)
    Jump("loc_7315")

    label("loc_7261")

    OP_4A(0x1A, 0)
    OP_4A(0x20, 0)

    ChrTalk(    #118
        0x1A,
        "哎呀，你刚才说什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x20,
        (
            "我都说了，\x01",
            "那水灵通透的雪白肌肤……\x01",
            "以及水润娇艳的红唇……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x20,
        (
            "即使戴着面具\x01",
            "也无法隐藏你的美丽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x1A,
        "呵呵，你真会说话。\x02",
    )

    CloseMessageWindow()
    OP_4B(0x1A, 0)
    OP_4B(0x20, 0)
    OP_A2(0x3)

    label("loc_7315")

    TalkEnd(0xFE)
    Return()

    # Function_55_71C0 end

    def Function_56_7319(): pass

    label("Function_56_7319")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_73F0")

    ChrTalk(    #122
        0xFE,
        (
            "#2P哎呀呀，贵公司成长之快\x01",
            "真是令人生畏啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "#2P……对了对了，之前那件好事\x01",
            "让我们也受益匪浅哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x11, 255)

    ChrTalk(    #124
        0x11,
        "……您喜欢吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "#2P#1K哈哈哈哈哈……！！\x02",
    )


    ChrTalk(    #126
        0x11,
        "#1K哈哈哈哈哈哈……！！\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_4B(0x11, 255)
    Jump("loc_73F4")

    label("loc_73F0")

    Call(0, 52)

    label("loc_73F4")

    TalkEnd(0xFE)
    Return()

    # Function_56_7319 end

    def Function_57_73F8(): pass

    label("Function_57_73F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_74C4")

    ChrTalk(    #127
        0xFE,
        (
            "啊哈哈，能获得公司顾问之名\x01",
            "我也感到骄傲呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "……不过康莱特君，\x01",
            "还远远不止如此而已吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "莱恩福尔特的董事\x01",
            "这头衔还太小太小。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "哈哈，\x01",
            "你还要继续往上爬才行啊。\x02",
        )
    )

    Jump("loc_74C0")

    label("loc_74C0")

    CloseMessageWindow()
    Jump("loc_74C8")

    label("loc_74C4")

    Call(0, 52)

    label("loc_74C8")

    TalkEnd(0xFE)
    Return()

    # Function_57_73F8 end

    def Function_58_74CC(): pass

    label("Function_58_74CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7516")

    ChrTalk(    #131
        0xFE,
        (
            "还有很多惊喜\x01",
            "等在后头呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "呵呵，真令人期待呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_751A")

    label("loc_7516")

    Call(0, 52)

    label("loc_751A")

    TalkEnd(0xFE)
    Return()

    # Function_58_74CC end

    def Function_59_751E(): pass

    label("Function_59_751E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_757E")

    ChrTalk(    #133
        0xFE,
        "……这拼盘的质量不行啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "真是不像话……\x01",
            "一会儿要去提醒一下厨师长……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7603")

    label("loc_757E")


    ChrTalk(    #135
        0xFE,
        (
            "这里的主厨\x01",
            "是从我的酒店派来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "如果因为厨具不顺手之类的理由\x01",
            "就随便乱来，那可不行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "……我还是得去监督一下。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_7603")

    TalkEnd(0xFE)
    Return()

    # Function_59_751E end

    def Function_60_7607(): pass

    label("Function_60_7607")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_765F")

    ChrTalk(    #138
        0xFE,
        "今天我们是客人吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "爸爸，赶快去跟那个\x01",
            "主办者大叔打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_76CB")

    label("loc_765F")


    ChrTalk(    #140
        0xFE,
        "别这样爸爸，多丢人啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "今天我们只是客人而已吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "赶快去跟那个\x01",
            "主办者大叔打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_76CB")

    TalkEnd(0xFE)
    Return()

    # Function_60_7607 end

    def Function_61_76CF(): pass

    label("Function_61_76CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_7744")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #143
        0xFE,
        (
            "呼，不过主动来搭话的\x01",
            "是那位夫人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "哎呀哎呀，没办法……\x01",
            "随便附和一下好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    Jump("loc_7748")

    label("loc_7744")

    Call(0, 55)

    label("loc_7748")

    TalkEnd(0xFE)
    Return()

    # Function_61_76CF end

    def Function_62_774C(): pass

    label("Function_62_774C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_77C0")

    ChrTalk(    #145
        0xFE,
        (
            "这么难得的宴会，\x01",
            "本来想说不定\x01",
            "能给她找到好对象的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "琳德尔那家伙，\x01",
            "竟然会找借口反抗我……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7835")

    label("loc_77C0")


    ChrTalk(    #147
        0xFE,
        (
            "哎呀哎呀，\x01",
            "这么难得的宴会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "琳德尔那家伙，\x01",
            "不是在装病吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "竟然会\x01",
            "找借口反抗我……\x02",
        )
    )

    Jump("loc_7831")

    label("loc_7831")

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_7835")

    TalkEnd(0xFE)
    Return()

    # Function_62_774C end

    def Function_63_7839(): pass

    label("Function_63_7839")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_789F")

    ChrTalk(    #150
        0xFE,
        (
            "主、主人，\x01",
            "就让她稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "再说，\x01",
            "宴会也不止是今晚而已……\x02",
        )
    )

    Jump("loc_789B")

    label("loc_789B")

    CloseMessageWindow()
    Jump("loc_78E9")

    label("loc_789F")


    ChrTalk(    #152
        0xFE,
        (
            "……是，\x01",
            "小姐在房间里休息。\x02",
        )
    )

    Jump("loc_78CD")

    label("loc_78CD")

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "说是身体不适……\x02",
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_78E9")

    TalkEnd(0xFE)
    Return()

    # Function_63_7839 end

    def Function_64_78ED(): pass

    label("Function_64_78ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_7960")

    ChrTalk(    #154
        0xFE,
        (
            "……话说回来，\x01",
            "奥利维特皇子的回归真是令人惊讶。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "应该算是这半年来，\x01",
            "帝都最大的事件了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_79D6")

    label("loc_7960")


    ChrTalk(    #156
        0xFE,
        "哈哈哈，我也是这么觉得。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "帝都果然令人压抑得透不过气来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "我的休假也是在\x01",
            "南国的别墅度过的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_79D6")

    TalkEnd(0xFE)
    Return()

    # Function_64_78ED end

    def Function_65_79DA(): pass

    label("Function_65_79DA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_7A35")

    ChrTalk(    #159
        0xFE,
        (
            "帝都阴沉沉的天空\x01",
            "真是令人厌烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "没有人能让那里\x01",
            "变得热闹起来吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AB1")

    label("loc_7A35")


    ChrTalk(    #161
        0xFE,
        (
            "豪华客船露西塔尼亚号……\x01",
            "真是漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "帝都阴沉沉的天空\x01",
            "真是让人厌烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "好久没像今天\x01",
            "这么开心了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_7AB1")

    TalkEnd(0xFE)
    Return()

    # Function_65_79DA end

    def Function_66_7AB5(): pass

    label("Function_66_7AB5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_7B16")

    ChrTalk(    #164
        0xFE,
        (
            "呵呵……中央政府\x01",
            "不过是官员集中的地方。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "只要用对了方法，\x01",
            "总能搞定的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B8F")

    label("loc_7B16")


    ChrTalk(    #166
        0xFE,
        "呵呵，你还年轻呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "中央政府\x01",
            "不过是官员集中的地方……\x02",
        )
    )

    Jump("loc_7B66")

    label("loc_7B66")

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "只要用对了方法，\x01",
            "总能搞定的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_7B8F")

    TalkEnd(0xFE)
    Return()

    # Function_66_7AB5 end

    def Function_67_7B93(): pass

    label("Function_67_7B93")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_7C33")

    ChrTalk(    #169
        0xFE,
        (
            "那个该死的法案，\x01",
            "竟然冻结了我的私人帐户……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "还好我立刻提出抗议，\x01",
            "才得以挽回……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "这都是那个暴发户宰相所为。\x01",
            "真是气死人了……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7CAA")

    label("loc_7C33")


    ChrTalk(    #172
        0xFE,
        "哼，那个军人出身的暴发户宰相……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "接二连三地\x01",
            "通过麻烦的法案……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "把愚民们捧上天\x01",
            "有什么好开心的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_7CAA")

    TalkEnd(0xFE)
    Return()

    # Function_67_7B93 end

    def Function_68_7CAE(): pass

    label("Function_68_7CAE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_7D1A")

    ChrTalk(    #175
        0xFE,
        (
            "莱恩福尔特集团……\x01",
            "今后也很有发展前途呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "呵呵，\x01",
            "再稍微增加点投资额吧。\x02",
        )
    )

    Jump("loc_7D16")

    label("loc_7D16")

    CloseMessageWindow()
    Jump("loc_7DC7")

    label("loc_7D1A")


    ChrTalk(    #177
        0xFE,
        (
            "康莱特公司\x01",
            "也被纳入那个\x01",
            "莱恩福尔特集团旗下了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "囊括帝国军需产业、\x01",
            "工业的第一大财阀，\x01",
            "『莱恩福尔特集团』……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        (
            "呵呵，\x01",
            "再稍微增加点投资额吧。\x02",
        )
    )

    Jump("loc_7DC3")

    label("loc_7DC3")

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_7DC7")

    TalkEnd(0xFE)
    Return()

    # Function_68_7CAE end

    def Function_69_7DCB(): pass

    label("Function_69_7DCB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_7E3C")

    ChrTalk(    #180
        0xFE,
        (
            "不愧是康莱特先生……\x01",
            "担任警卫的保安们也都是超水准的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        (
            "一会儿请他\x01",
            "也为我介绍一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EE2")

    label("loc_7E3C")


    ChrTalk(    #182
        0xFE,
        (
            "嗯，\x01",
            "今天担任警卫的黑衣人\x01",
            "看上去都很可靠的样子啊。\x02",
        )
    )

    Jump("loc_7E7B")

    label("loc_7E7B")

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "我的私人部队\x01",
            "差不多也该\x01",
            "补充一些新鲜血液了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "一会儿请康莱特先生\x01",
            "也为我介绍一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)

    label("loc_7EE2")

    TalkEnd(0xFE)
    Return()

    # Function_69_7DCB end

    def Function_70_7EE6(): pass

    label("Function_70_7EE6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_7F8F")

    ChrTalk(    #185
        0x29,
        (
            "……嗯嗯，说到皮毛的质量，\x01",
            "还是巴利亚哈特略胜一筹啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "特别是北部高原养育的梅尔格羊，\x01",
            "毛质实在是十分优良……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x2A,
        "（突然精神起来了呢……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8086")

    label("loc_7F8F")

    OP_4A(0x29, 0)
    OP_4A(0x2A, 0)

    ChrTalk(    #188
        0x29,
        "那个，公爵夫人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x2A,
        (
            "呵呵，真是巧啊。\x01",
            "您竟然也受到了招待……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x2A,
        (
            "莫非是到巴利亚哈特\x01",
            "购买皮毛去的吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x29,
        "嗯，是啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x29,
        (
            "那个，\x01",
            "能不能帮忙向我丈夫保密？\x02",
        )
    )

    Jump("loc_804E")

    label("loc_804E")

    CloseMessageWindow()

    ChrTalk(    #193
        0x2A,
        (
            "呵呵，\x01",
            "这点小事有什么问题。\x02",
        )
    )

    Jump("loc_807A")

    label("loc_807A")

    CloseMessageWindow()
    OP_4B(0x29, 0)
    OP_4B(0x2A, 0)
    OP_A2(0x12)

    label("loc_8086")

    TalkEnd(0xFE)
    Return()

    # Function_70_7EE6 end

    def Function_71_808A(): pass

    label("Function_71_808A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_80F5")

    ChrTalk(    #194
        0xFE,
        (
            "不过作为掩口费\x01",
            "希望您能给我介绍点东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "帝都的服装店里，\x01",
            "都找不到什么好的皮毛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80F9")

    label("loc_80F5")

    Call(0, 70)

    label("loc_80F9")

    TalkEnd(0xFE)
    Return()

    # Function_71_808A end

    def Function_72_80FD(): pass

    label("Function_72_80FD")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_72_80FD end

    def Function_73_8104(): pass

    label("Function_73_8104")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_8166")
    OP_8C(0xFE, 180, 0)

    ChrTalk(    #196
        0xFE,
        (
            "啊啊，\x01",
            "赶快趁热吃吧。\x02",
        )
    )

    Jump("loc_813A")

    label("loc_813A")

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "对了，\x01",
            "再尝一下这种派。\x02",
        )
    )

    Jump("loc_8162")

    label("loc_8162")

    CloseMessageWindow()
    Jump("loc_8229")

    label("loc_8166")


    ChrTalk(    #198
        0xFE,
        (
            "……对了，\x01",
            "你看到我妻子没有啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "真是的，\x01",
            "亏我总跟她说别到处乱转……\x02",
        )
    )

    Jump("loc_81C3")

    label("loc_81C3")

    CloseMessageWindow()

    NpcTalk(    #200
        0x109,
        "戴面具的绅士",
        (
            "#1602F#6P（嗯…………？）\x02\x03",

            "#1601F#6P（啊啊，\x01",
            "  是刚才那位夫人的丈夫吧……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)

    label("loc_8229")

    TalkEnd(0xFE)
    Return()

    # Function_73_8104 end

    def Function_74_822D(): pass

    label("Function_74_822D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_828B")

    ChrTalk(    #201
        0xFE,
        (
            "居然敢到\x01",
            "我的领地来撒野……\x02",
        )
    )

    Jump("loc_8265")

    label("loc_8265")

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        "小毛头………可别太嚣张了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8312")

    label("loc_828B")


    ChrTalk(    #203
        0xFE,
        (
            "仅仅十年就跃居前列的\x01",
            "康莱特公司……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "哼，不过是依靠莱恩福尔特集团，\x01",
            "狐假虎威罢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "小毛头………可别太嚣张了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x15)

    label("loc_8312")

    TalkEnd(0xFE)
    Return()

    # Function_74_822D end

    def Function_75_8316(): pass

    label("Function_75_8316")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_836F")

    ChrTalk(    #206
        0xFE,
        (
            "本船露西塔尼亚号\x01",
            "提供了最优质的服务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "有需要的话\x01",
            "请随时吩咐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83B3")

    label("loc_836F")


    ChrTalk(    #208
        0xFE,
        (
            "本船露西塔尼亚号\x01",
            "提供了最优质的服务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "请慢慢享受。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x16)

    label("loc_83B3")

    TalkEnd(0xFE)
    Return()

    # Function_75_8316 end

    def Function_76_83B7(): pass

    label("Function_76_83B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_83FC")

    ChrTalk(    #210
        0xFE,
        "接下来还准备了各种活动。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "祝大家玩得开心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8469")

    label("loc_83FC")


    ChrTalk(    #212
        0xFE,
        (
            "之后是法兰·德·席埃尔\x01",
            "的音乐会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "从11点开始\x01",
            "还将进行歌剧等演出活动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "请不要错过。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x17)

    label("loc_8469")

    TalkEnd(0xFE)
    Return()

    # Function_76_83B7 end

    def Function_77_846D(): pass

    label("Function_77_846D")

    TalkBegin(0x2F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_84C2")

    ChrTalk(    #215
        0x2F,
        (
            "今日是康莱特大人\x01",
            "举办的宴会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x2F,
        (
            "有需要的话，\x01",
            "请随时吩咐。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8512")

    label("loc_84C2")


    ChrTalk(    #217
        0x2F,
        "这位客人，需要来点饮料吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x2F,
        (
            "我们还准备了\x01",
            "『圣蔷薇』的陈年美酒。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_8512")

    TalkEnd(0x2F)
    Return()

    # Function_77_846D end

    def Function_78_8516(): pass

    label("Function_78_8516")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 3)), scpexpr(EXPR_END)), "loc_8574")

    ChrTalk(    #219
        0xFE,
        (
            "这边的料理都是用\x01",
            "严格挑选的上等材料制作的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        "这位客人，要尝尝吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_85D7")

    label("loc_8574")


    ChrTalk(    #221
        0xFE,
        (
            "今天的推荐菜是主厨的拿手绝品……\x01",
            "清蒸奶油鲍鱼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "我想您一定会\x01",
            "喜欢这种绝妙滋味的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1B)

    label("loc_85D7")

    TalkEnd(0xFE)
    Return()

    # Function_78_8516 end

    def Function_79_85DB(): pass

    label("Function_79_85DB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 4)), scpexpr(EXPR_END)), "loc_867F")

    ChrTalk(    #223
        0xFE,
        "哎呀，这里还有《红耀石》呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "呵呵，\x01",
            "这部小说还挺有人气的呢。\x02",
        )
    )

    Jump("loc_8638")

    label("loc_8638")

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "自从发售以来，很多人猜测\x01",
            "里面的故事可能是真实发生的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_86E1")

    label("loc_867F")


    ChrTalk(    #226
        0xFE,
        (
            "呵呵，\x01",
            "不愧是豪华客船，\x01",
            "藏书真是丰富啊。\x02",
        )
    )

    Jump("loc_86B7")

    label("loc_86B7")

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "好吧，\x01",
            "要读哪一本呢。\x02",
        )
    )

    Jump("loc_86DD")

    label("loc_86DD")

    CloseMessageWindow()
    OP_A2(0x1C)

    label("loc_86E1")

    TalkEnd(0xFE)
    Return()

    # Function_79_85DB end

    def Function_80_86E5(): pass

    label("Function_80_86E5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 5)), scpexpr(EXPR_END)), "loc_874D")

    ChrTalk(    #228
        0xFE,
        "哈哈，反正和我们无关。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "如果有什么事发生，军方也会行动的，\x01",
            "没什么好担心的啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_87EB")

    label("loc_874D")


    ChrTalk(    #230
        0xFE,
        (
            "啊啊，是说南部城市有一段时间\x01",
            "暂时无法使用导力制品的事吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "听说导力铁道和国际航班\x01",
            "也暂时停止运行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "这个，我觉得\x01",
            "并不是什么大事呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1D)

    label("loc_87EB")

    TalkEnd(0xFE)
    Return()

    # Function_80_86E5 end

    def Function_81_87EF(): pass

    label("Function_81_87EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 6)), scpexpr(EXPR_END)), "loc_886F")

    ChrTalk(    #233
        0xFE,
        (
            "虽然我的一个朋友说\x01",
            "曾经目击到那个浮游物体\x01",
            "崩塌的现场……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "但其他人都不知道这件事，\x01",
            "是不是他看错了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8907")

    label("loc_886F")


    ChrTalk(    #235
        0xFE,
        (
            "……还有传言说\x01",
            "那是王国军的新型武器呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "中央政府\x01",
            "已经下达了缄口令。\x02",
        )
    )

    Jump("loc_88CC")

    label("loc_88CC")

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "之后没有任何官方消息发布，\x01",
            "我们完全不清楚状况。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E)

    label("loc_8907")

    TalkEnd(0xFE)
    Return()

    # Function_81_87EF end

    def Function_82_890B(): pass

    label("Function_82_890B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 7)), scpexpr(EXPR_END)), "loc_8967")

    ChrTalk(    #238
        0xFE,
        (
            "虽然有些对不起\x01",
            "送给我票的儿子和儿媳……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        "但我还是不喜欢这种场合。\x02",
    )

    CloseMessageWindow()
    Jump("loc_89DF")

    label("loc_8967")


    ChrTalk(    #240
        0xFE,
        "哎呀呀，真是没法静下心来呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        "所有东西都太过豪华了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "对我这把老骨头来说，\x01",
            "刺激实在有点强烈。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1F)

    label("loc_89DF")

    TalkEnd(0xFE)
    Return()

    # Function_82_890B end

    def Function_83_89E3(): pass

    label("Function_83_89E3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 4)), scpexpr(EXPR_END)), "loc_8A42")

    ChrTalk(    #243
        0xFE,
        (
            "只要不离开本船，\x01",
            "这里的书都可以自由借阅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "带回到房间里\x01",
            "也没问题哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A7F")

    label("loc_8A42")


    ChrTalk(    #245
        0xFE,
        (
            "这里是\x01",
            "本船的图书角。\x02",
        )
    )

    Jump("loc_8A67")

    label("loc_8A67")

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        "请慢慢阅览。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C)

    label("loc_8A7F")

    TalkEnd(0xFE)
    Return()

    # Function_83_89E3 end

    def Function_84_8A83(): pass

    label("Function_84_8A83")

    TalkBegin(0xFE)

    ChrTalk(    #247
        0xFE,
        "……在室内请保持安静。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_84_8A83 end

    def Function_85_8AA8(): pass

    label("Function_85_8AA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 0)), scpexpr(EXPR_END)), "loc_8B0B")

    ChrTalk(    #248
        0xFE,
        (
            "呵呵，这里的庄家\x01",
            "都知道如何让人玩得开心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "和下贱的赌场\x01",
            "真是截然不同啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B8F")

    label("loc_8B0B")


    ChrTalk(    #250
        0xFE,
        (
            "原来这里是总店开设在帝都的\x01",
            "高级俱乐部『亚利夏』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "难怪，\x01",
            "职员的素质都很不错啊。\x02",
        )
    )

    Jump("loc_8B71")

    label("loc_8B71")

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        "来，喝点葡萄酒吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20)

    label("loc_8B8F")

    TalkEnd(0xFE)
    Return()

    # Function_85_8AA8 end

    def Function_86_8B93(): pass

    label("Function_86_8B93")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 1)), scpexpr(EXPR_END)), "loc_8BE3")

    ChrTalk(    #253
        0xFE,
        "下、下次一定要赢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "来、来吧……！\x01",
            "……黑色１１！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C4F")

    label("loc_8BE3")


    ChrTalk(    #255
        0xFE,
        "来、来吧……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        "这次、这次一定是黑色……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "已经有５次是红色了。\x01",
            "这次绝对是黑色了！！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x21)

    label("loc_8C4F")

    TalkEnd(0xFE)
    Return()

    # Function_86_8B93 end

    def Function_87_8C53(): pass

    label("Function_87_8C53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 2)), scpexpr(EXPR_END)), "loc_8CC7")

    ChrTalk(    #258
        0xFE,
        (
            "不过，像我这种平民\x01",
            "能够有这样的美梦，\x01",
            "都多亏宰相阁下啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "『实力主义』……\x01",
            "多棒的名称啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D2A")

    label("loc_8CC7")


    ChrTalk(    #260
        0xFE,
        (
            "……里面的会场\x01",
            "正在举办豪华宴会吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "等着瞧吧……\x01",
            "总有一天我也会去参加那种宴会……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22)

    label("loc_8D2A")

    TalkEnd(0xFE)
    Return()

    # Function_87_8C53 end

    def Function_88_8D2E(): pass

    label("Function_88_8D2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 3)), scpexpr(EXPR_END)), "loc_8D81")

    ChrTalk(    #262
        0xFE,
        "呵呵，那真是令人期待。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "光是赢\x01",
            "也很没意思呢……\x02",
        )
    )

    Jump("loc_8D7D")

    label("loc_8D7D")

    CloseMessageWindow()
    Jump("loc_8DDC")

    label("loc_8D81")


    ChrTalk(    #264
        0xFE,
        (
            "是啊……\x01",
            "刚才真是精彩的对决。\x02",
        )
    )

    Jump("loc_8DB1")

    label("loc_8DB1")

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "怎么办呢，先生。\x01",
            "要再比一场吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x23)

    label("loc_8DDC")

    TalkEnd(0xFE)
    Return()

    # Function_88_8D2E end

    def Function_89_8DE0(): pass

    label("Function_89_8DE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 4)), scpexpr(EXPR_END)), "loc_8E30")

    ChrTalk(    #266
        0xFE,
        "挥霍不过是单纯的娱乐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "不明白的人\x01",
            "就没资格来这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EB3")

    label("loc_8E30")


    ChrTalk(    #268
        0xFE,
        "呼，挥霍不过是单纯的娱乐而已。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "所谓赌博，\x01",
            "就是要大赢大输才有乐趣啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "若总拘泥于赢钱，\x01",
            "就只说明还远未成熟。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x24)

    label("loc_8EB3")

    TalkEnd(0xFE)
    Return()

    # Function_89_8DE0 end

    def Function_90_8EB7(): pass

    label("Function_90_8EB7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 6)), scpexpr(EXPR_END)), "loc_8EEC")
    TurnDirection(0xFE, 0x0, 0)

    ChrTalk(    #271
        0xFE,
        "怎么样，这位客人。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    Jump("loc_8F57")

    label("loc_8EEC")

    OP_4A(0xFE, 0)
    OP_4A(0x3C, 0)

    ChrTalk(    #272
        0x3C,
        "来，和我赌一把吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x3C,
        "押３０万在红色２１上……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        "不愧是客人，眼光真高。\x02",
    )

    CloseMessageWindow()
    OP_4B(0xFE, 0)
    OP_4B(0x3C, 0)
    OP_A2(0x2E)

    label("loc_8F57")

    TalkEnd(0xFE)
    Return()

    # Function_90_8EB7 end

    def Function_91_8F5B(): pass

    label("Function_91_8F5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 7)), scpexpr(EXPR_END)), "loc_8FA1")

    ChrTalk(    #275
        0xFE,
        "啊，当然可以。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        (
            "不过下一次\x01",
            "就轮到我赢了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9009")

    label("loc_8FA1")


    ChrTalk(    #277
        0xFE,
        "哈哈哈，真是败给你了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        (
            "这位客人，\x01",
            "您似乎精通玩牌的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "那么，您意下如何呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F)

    label("loc_9009")

    TalkEnd(0xFE)
    Return()

    # Function_91_8F5B end

    def Function_92_900D(): pass

    label("Function_92_900D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 0)), scpexpr(EXPR_END)), "loc_905E")

    ChrTalk(    #280
        0xFE,
        "这位客人，您也来玩一把吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        "我想一定能让您玩得开心的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_90C2")

    label("loc_905E")

    OP_8C(0xFE, 0, 0)

    ChrTalk(    #282
        0xFE,
        "唰唰唰……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        "啪啦啦啦啦啦…………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(    #284
        0xFE,
        (
            "哎呀客人……\x01",
            "来玩一局如何呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x30)

    label("loc_90C2")

    TalkEnd(0xFE)
    Return()

    # Function_92_900D end

    def Function_93_90C6(): pass

    label("Function_93_90C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 1)), scpexpr(EXPR_END)), "loc_90F9")

    ChrTalk(    #285
        0xFE,
        (
            "呵呵，\x01",
            "祝您玩得开心。\x02",
        )
    )

    Jump("loc_90F5")

    label("loc_90F5")

    CloseMessageWindow()
    Jump("loc_914D")

    label("loc_90F9")


    ChrTalk(    #286
        0xFE,
        (
            "呵呵，\x01",
            "祝您玩得开心。\x02",
        )
    )

    Jump("loc_911E")

    label("loc_911E")

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "不过还是要提醒您注意\x01",
            "不要热衷过头。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x31)

    label("loc_914D")

    TalkEnd(0xFE)
    Return()

    # Function_93_90C6 end

    def Function_94_9151(): pass

    label("Function_94_9151")

    TalkBegin(0x41)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 5)), scpexpr(EXPR_END)), "loc_91C4")

    ChrTalk(    #288
        0x41,
        (
            "持有招待券的客人\x01",
            "就是本俱乐部的正式会员，\x01",
            "可以享受一切服务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x41,
        (
            "请自由\x01",
            "选择台面。\x02",
        )
    )

    Jump("loc_91C0")

    label("loc_91C0")

    CloseMessageWindow()
    Jump("loc_924B")

    label("loc_91C4")


    ChrTalk(    #290
        0x41,
        "啊啊，是受招待的客人吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x41,
        (
            "只要有康莱特大人的招待券，\x01",
            "就可以作为本俱乐部的正式会员\x01",
            "享受一切服务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x41,
        "祝您玩得开心。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2D)

    label("loc_924B")

    TalkEnd(0x41)
    Return()

    # Function_94_9151 end

    def Function_95_924F(): pass

    label("Function_95_924F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 2)), scpexpr(EXPR_END)), "loc_9272")

    ChrTalk(    #293
        0xFE,
        "……请慢慢玩。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9296")

    label("loc_9272")


    ChrTalk(    #294
        0xFE,
        (
            "……怎么样，\x01",
            "玩得开心吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2A)

    label("loc_9296")

    TalkEnd(0xFE)
    Return()

    # Function_95_924F end

    def Function_96_929A(): pass

    label("Function_96_929A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 5)), scpexpr(EXPR_END)), "loc_92FF")

    ChrTalk(    #295
        0xFE,
        (
            "这就是飞艇啊……\x01",
            "坐起来相当舒适嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        (
            "今后旅行的时候\x01",
            "也可以经常来搭乘一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9378")

    label("loc_92FF")


    ChrTalk(    #297
        0xFE,
        (
            "露西塔尼亚号……\x01",
            "据说是最新型的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        "呵呵，真舒服、真舒服。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "今后旅行的时候\x01",
            "也可以经常来搭乘一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x25)

    label("loc_9378")

    TalkEnd(0xFE)
    Return()

    # Function_96_929A end

    def Function_97_937C(): pass

    label("Function_97_937C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 5)), scpexpr(EXPR_END)), "loc_93C4")

    ChrTalk(    #300
        0xFE,
        (
            "房间里的日用品\x01",
            "也都是一流的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        "嗯，不错啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9418")

    label("loc_93C4")


    ChrTalk(    #302
        0xFE,
        "嗯，不错呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        "这红茶也挺香的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "这里的服务\x01",
            "真是值回票价了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x25)

    label("loc_9418")

    TalkEnd(0xFE)
    Return()

    # Function_97_937C end

    def Function_98_941C(): pass

    label("Function_98_941C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_947B")

    ChrTalk(    #305
        0xFE,
        (
            "这边的二等客房\x01",
            "今天没有人住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "只要是受招待的客人，\x01",
            "都可以随时使用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9510")

    label("loc_947B")


    ChrTalk(    #307
        0xFE,
        "……哎呀，失礼了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        "请问您是受到招待的客人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "宴会会场\x01",
            "就在走廊的尽头。\x02",
        )
    )

    Jump("loc_94E3")

    label("loc_94E3")

    CloseMessageWindow()

    NpcTalk(    #310
        0x109,
        "戴面具的绅士",
        "#1600F呵呵……谢谢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x19)

    label("loc_9510")

    TalkEnd(0xFE)
    Return()

    # Function_98_941C end

    def Function_99_9514(): pass

    label("Function_99_9514")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 7)), scpexpr(EXPR_END)), "loc_9594")

    ChrTalk(    #311
        0xFE,
        (
            "这就是上流社会的生存方式……\x01",
            "今天你可要\x01",
            "亲眼见识一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        (
            "然后，将来一定要\x01",
            "让我这个当父亲的也享受享受。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_964F")

    label("loc_9594")


    ChrTalk(    #313
        0xFE,
        "听好了，儿子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        (
            "为了你，我花了大笔的米拉\x01",
            "才坐上这艘船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        (
            "这就是上流社会的生存方式……\x01",
            "今天你可要\x01",
            "亲眼见识一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        (
            "然后，将来一定要\x01",
            "让我这个当父亲的也享受享受。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x27)

    label("loc_964F")

    TalkEnd(0xFE)
    Return()

    # Function_99_9514 end

    def Function_100_9653(): pass

    label("Function_100_9653")

    TalkBegin(0xFE)

    ChrTalk(    #317
        0xFE,
        (
            "嗯，关键就是要当上军人，\x01",
            "然后取得地位就行了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xFE,
        (
            "嘿嘿，话说回来，\x01",
            "飞艇还真是厉害啊～⊙\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_100_9653 end

    def Function_101_96BE(): pass

    label("Function_101_96BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9745")
    OP_A2(0x18)

    ChrTalk(    #319
        0xFE,
        "客人，您在散步吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        (
            "从这前面的楼梯上去\x01",
            "就能到甲板上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        (
            "看着星星吹吹晚风\x01",
            "是不错的转换心情的方法哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97A1")

    label("loc_9745")


    ChrTalk(    #322
        0xFE,
        (
            "从这前面的楼梯上去\x01",
            "就能到甲板上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        (
            "看着星星吹吹晚风\x01",
            "是不错的转换心情的方法哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97A1")

    TalkEnd(0xFE)
    Return()

    # Function_101_96BE end

    def Function_102_97A5(): pass

    label("Function_102_97A5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 0)), scpexpr(EXPR_END)), "loc_982D")

    ChrTalk(    #324
        0xFE,
        "咦…………？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x0, 500)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #325
        0xFE,
        "啊，那个……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        "哦，您辛苦了……\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 0)
    Jump("loc_98F6")

    label("loc_982D")

    OP_4A(0x4F, 0)
    OP_4A(0x50, 0)

    ChrTalk(    #327
        0x4F,
        "喂，怎么办啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x4F,
        (
            "我捡到了那个化装宴会\x01",
            "的招待券……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x50,
        (
            "笨、笨蛋……！\x01",
            "那是只发给\x01",
            "一等客房的有钱人的吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0x50,
        (
            "我、我们拿着\x01",
            "能有什么好事啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x4F,
        "但、但是…………\x02",
    )

    CloseMessageWindow()
    OP_4B(0x4F, 0)
    OP_4B(0x50, 0)
    OP_A2(0x28)

    label("loc_98F6")

    TalkEnd(0xFE)
    Return()

    # Function_102_97A5 end

    def Function_103_98FA(): pass

    label("Function_103_98FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 0)), scpexpr(EXPR_END)), "loc_99C0")

    NpcTalk(    #332
        0x109,
        "戴面具的绅士",
        (
            "#1600F……请问，\x01",
            "展望甲板是从\x01",
            "这个楼梯上去吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x0, 500)

    ChrTalk(    #333
        0xFE,
        "啊……是、是的！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        "没、没错！\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #335
        0x109,
        "戴面具的绅士",
        "#1603F呵呵，谢谢。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 0)
    Jump("loc_99C4")

    label("loc_99C0")

    Call(0, 102)

    label("loc_99C4")

    TalkEnd(0xFE)
    Return()

    # Function_103_98FA end

    def Function_104_99C8(): pass

    label("Function_104_99C8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 3)), scpexpr(EXPR_END)), "loc_9A37")

    ChrTalk(    #336
        0xFE,
        (
            "对进入会场的客人\x01",
            "都要检查是否持有招待券。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        (
            "这是保安上的必要事项，\x01",
            "敬请理解。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B55")

    label("loc_9A37")


    ChrTalk(    #338
        0xFE,
        (
            "……客人，\x01",
            "请问您有招待券吗？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #339
        0x109,
        "戴面具的绅士",
        "#1600F啊啊，是这个吗？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #340
        "\x07\x05将招待券出示给黑衣保安。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #341
        0xFE,
        "真是失礼了…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        (
            "这是保安上的必要事项，\x01",
            "敬请理解。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #343
        0x109,
        "戴面具的绅士",
        "#1601F呵呵，没关系。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2B)

    label("loc_9B55")

    TalkEnd(0xFE)
    Return()

    # Function_104_99C8 end

    def Function_105_9B59(): pass

    label("Function_105_9B59")

    TalkBegin(0xFE)

    ChrTalk(    #344
        0xFE,
        (
            "哦……？\x01",
            "您来这里有什么事吗？\x02",
        )
    )

    Jump("loc_9B8C")

    label("loc_9B8C")

    CloseMessageWindow()

    ChrTalk(    #345
        0xFE,
        (
            "这前面是通往\x01",
            "展望甲板的通道。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        (
            "宴会会场\x01",
            "在下层走廊的尽头。\x02",
        )
    )

    Jump("loc_9BE0")

    label("loc_9BE0")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_105_9B59 end

    def Function_106_9BE5(): pass

    label("Function_106_9BE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 2)), scpexpr(EXPR_END)), "loc_9C45")

    ChrTalk(    #347
        0xFE,
        (
            "唔，这引擎的声音\x01",
            "也是以前没听过的啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        "看来是新型的呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D2C")

    label("loc_9C45")


    ChrTalk(    #349
        0xFE,
        (
            "呼，\x01",
            "这就是很早就开始宣传的\x01",
            "最新型的飞行客船吗。\x02",
        )
    )

    Jump("loc_9C87")

    label("loc_9C87")

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        (
            "原来如此……\x01",
            "连引擎的声音\x01",
            "也是以前没听过的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        "看来是新型的呢……\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #352
        0x109,
        "戴面具的绅士",
        (
            "#1602F（咦……？\x01",
            "  难道这个男的看不见东西吗？）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x32)

    label("loc_9D2C")

    TalkEnd(0xFE)
    Return()

    # Function_106_9BE5 end

    def Function_107_9D30(): pass

    label("Function_107_9D30")

    EventBegin(0x1)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #353
        "\x07\x05门牢牢地锁着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(50)
    EventEnd(0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_9D84")
    SetMapFlags(0x2000000)

    label("loc_9D84")

    Return()

    # Function_107_9D30 end

    def Function_108_9D85(): pass

    label("Function_108_9D85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_9DF2")
    EventBegin(0x1)
    OP_8C(0x0, 270, 0)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #354
        "\x07\x05门牢牢地锁着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_90(0x0, 0x3E8, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_9DFB")

    label("loc_9DF2")

    NewScene("ED6_DT21/E1110   ._SN", 113, 1, 0)
    IdleLoop()

    label("loc_9DFB")

    Return()

    # Function_108_9D85 end

    def Function_109_9DFC(): pass

    label("Function_109_9DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_9E69")
    EventBegin(0x1)
    OP_8C(0x0, 270, 0)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #355
        "\x07\x05门牢牢地锁着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_90(0x0, 0x3E8, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_9E72")

    label("loc_9E69")

    NewScene("ED6_DT21/E1110   ._SN", 114, 1, 0)
    IdleLoop()

    label("loc_9E72")

    Return()

    # Function_109_9DFC end

    def Function_110_9E73(): pass

    label("Function_110_9E73")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_9EAF")

    NpcTalk(    #356
        0x109,
        "凯文·格拉汉姆",
        "#1060F会场不在这边。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9F08")

    label("loc_9EAF")


    NpcTalk(    #357
        0x109,
        "戴面具的绅士",
        (
            "#1602F（目标是最上层……）\x02\x03",

            "#1602F（没有去这边的必要。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F08")

    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_110_9E73 end

    def Function_111_9F24(): pass

    label("Function_111_9F24")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4BC, 5)), scpexpr(EXPR_END)), "loc_9F80")

    NpcTalk(    #358
        0x109,
        "凯文·格拉汉姆",
        "#1060F会场不在这边。\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_A0AA")

    label("loc_9F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 3)), scpexpr(EXPR_END)), "loc_9FE4")

    NpcTalk(    #359
        0x109,
        "戴面具的绅士",
        (
            "#1602F（……还是不要\x01",
            "  往这边走了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_A0AA")

    label("loc_9FE4")

    OP_4A(0x4D, 255)
    SetChrPos(0x4D, 82560, 0, -169000, 0)
    OP_8E(0x4D, 0x13BC8, 0x0, 0xFFFD759C, 0xBB8, 0x0)

    ChrTalk(    #360
        0x4D,
        (
            "……这位客人，\x01",
            "您有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x4D, 400)

    NpcTalk(    #361
        0x109,
        "戴面具的绅士",
        "#1602F……不，没什么。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x33)
    Sleep(300)
    Fade(300)
    SetChrPos(0x109, 80000, 0, -162800, 180)
    OP_4B(0x4D, 255)
    SetChrPos(0x4D, 84380, 0, -168870, 222)
    OP_69(0x0, 0x0)
    OP_0D()
    EventEnd(0x1)

    label("loc_A0AA")

    Return()

    # Function_111_9F24 end

    def Function_112_A0AB(): pass

    label("Function_112_A0AB")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #362
        "\x07\x05书架上有《红耀石》。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    Menu(
        0,
        10,
        10,
        1,
        (
            "【１～６卷】\x01",        # 0
            "【７～最终卷】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A121"),
        (1, "loc_A23F"),
        (SWITCH_DEFAULT, "loc_A33E"),
    )


    label("loc_A121")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【读第１卷】\x01",      # 0
            "【读第２卷】\x01",      # 1
            "【读第３卷】\x01",      # 2
            "【读第４卷】\x01",      # 3
            "【读第５卷】\x01",      # 4
            "【读第６卷】\x01",      # 5
            "【放弃】\x01",          # 6
        )
    )

    Jump("loc_A1AA")

    label("loc_A1AA")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1E2")
    OP_B8(0xE6, 0x0)

    label("loc_A1E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1F4")
    OP_B8(0xE7, 0x0)

    label("loc_A1F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A206")
    OP_B8(0xE8, 0x0)

    label("loc_A206")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A218")
    OP_B8(0xE9, 0x0)

    label("loc_A218")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A22A")
    OP_B8(0xEA, 0x0)

    label("loc_A22A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A23C")
    OP_B8(0xEB, 0x0)

    label("loc_A23C")

    Jump("loc_A33E")

    label("loc_A23F")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        10,
        1,
        (
            "【读第７卷】\x01",      # 0
            "【读第８卷】\x01",      # 1
            "【读第９卷】\x01",      # 2
            "【读第10卷】\x01",      # 3
            "【读最终卷】\x01",      # 4
            "【放弃】\x01",          # 5
        )
    )

    Jump("loc_A2BB")

    label("loc_A2BB")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2F3")
    OP_B8(0xEC, 0x0)

    label("loc_A2F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A305")
    OP_B8(0xED, 0x0)

    label("loc_A305")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A317")
    OP_B8(0xEE, 0x0)

    label("loc_A317")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A329")
    OP_B8(0xEF, 0x0)

    label("loc_A329")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A33B")
    OP_B8(0xF0, 0x0)

    label("loc_A33B")

    Jump("loc_A33E")

    label("loc_A33E")

    OP_5F(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_112_A0AB end

    SaveToFile()

Try(main)
