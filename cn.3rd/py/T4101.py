from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4101   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '索露贝',                               # 9
        '黑衣人',                               # 10
        '黑衣人',                               # 11
        '黑衣人',                               # 12
        '黑衣人',                               # 13
        '黑衣人',                               # 14
        '黑衣人',                               # 15
        '奈尔',                                 # 16
        '朵洛希',                               # 17
        '士兵达克特',                           # 18
        '士兵贝尔坎',                           # 19
        '娜碧',                                 # 20
        '米亚尔',                               # 21
        '戈万',                                 # 22
        '帕菲',                                 # 23
        '娜娜',                                 # 24
        '安敦',                                 # 25
        '利库斯',                               # 26
        '卡拉莉丝',                             # 27
        '尼莫',                                 # 28
        '吉米',                                 # 29
        '拉奥尼',                               # 30
        '梅夏',                                 # 31
        '维尔娜婆婆',                           # 32
        '王国军士兵',                           # 33
        '王国军士兵',                           # 34
        '王国军士兵',                           # 35
        '游客',                                 # 36
        '游客',                                 # 37
        '伊尔',                                 # 38
        '士兵布朗斯',                           # 39
        '潘娜',                                 # 40
        '阿尔丹',                               # 41
        '鸽子',                                 # 42
        '鸽子',                                 # 43
        '鸽子',                                 # 44
        '王都格兰赛尔·北街区',                 # 45
        '王都格兰赛尔·南街区',                 # 46
        '王都格兰赛尔·空港',                   # 47
        '穆拉少校',                             # 48
        '发烟筒用目标角色',                     # 49
        '目标用照相机',                         # 50
        '',                                     # 51
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
        'ED6_DT07/CH01050 ._CH',             # 00
        'ED6_DT27/CH03460 ._CH',             # 01
        'ED6_DT07/CH02060 ._CH',             # 02
        'ED6_DT07/CH02720 ._CH',             # 03
        'ED6_DT27/CH04230 ._CH',             # 04
        'ED6_DT27/CH04232 ._CH',             # 05
        'ED6_DT27/CH04234 ._CH',             # 06
        'ED6_DT27/CH04464 ._CH',             # 07
        'ED6_DT07/CH01640 ._CH',             # 08
        'ED6_DT07/CH01540 ._CH',             # 09
        'ED6_DT07/CH01470 ._CH',             # 0A
        'ED6_DT07/CH01150 ._CH',             # 0B
        'ED6_DT07/CH01040 ._CH',             # 0C
        'ED6_DT07/CH01120 ._CH',             # 0D
        'ED6_DT07/CH02480 ._CH',             # 0E
        'ED6_DT07/CH02490 ._CH',             # 0F
        'ED6_DT07/CH01143 ._CH',             # 10
        'ED6_DT07/CH01100 ._CH',             # 11
        'ED6_DT07/CH01210 ._CH',             # 12
        'ED6_DT07/CH01110 ._CH',             # 13
        'ED6_DT07/CH01680 ._CH',             # 14
        'ED6_DT07/CH01030 ._CH',             # 15
        'ED6_DT06/CH20086 ._CH',             # 16
        'ED6_DT07/CH01140 ._CH',             # 17
        'ED6_DT07/CH01350 ._CH',             # 18
        'ED6_DT07/CH01070 ._CH',             # 19
        'ED6_DT07/CH02900 ._CH',             # 1A
        'ED6_DT26/CH20783 ._CH',             # 1B
        'ED6_DT07/CH01730 ._CH',             # 1C
        'ED6_DT07/CH01731 ._CH',             # 1D
        'ED6_DT07/CH01410 ._CH',             # 1E
        'ED6_DT06/CH20112 ._CH',             # 1F
        'ED6_DT26/CH20770 ._CH',             # 20
        'ED6_DT27/CH03570 ._CH',             # 21
        'ED6_DT27/CH03573 ._CH',             # 22
        'ED6_DT07/CH01480 ._CH',             # 23
        'ED6_DT26/CH20680 ._CH',             # 24
        'ED6_DT26/CH20681 ._CH',             # 25
        'ED6_DT26/CH20688 ._CH',             # 26
        'ED6_DT27/CH03233 ._CH',             # 27
        'ED6_DT26/CH20692 ._CH',             # 28
        'ED6_DT26/CH20686 ._CH',             # 29
        'ED6_DT26/CH20689 ._CH',             # 2A
        'ED6_DT26/CH20690 ._CH',             # 2B
        'ED6_DT26/CH20618 ._CH',             # 2C
        'ED6_DT27/CH04460 ._CH',             # 2D
        'ED6_DT27/CH04463 ._CH',             # 2E
        'ED6_DT27/CH03231 ._CH',             # 2F
        'ED6_DT26/CH20684 ._CH',             # 30
        'ED6_DT27/CH03234 ._CH',             # 31
    )

    AddCharChipPat(
        'ED6_DT07/CH01050P._CP',             # 00
        'ED6_DT27/CH03460P._CP',             # 01
        'ED6_DT07/CH02060P._CP',             # 02
        'ED6_DT07/CH02720P._CP',             # 03
        'ED6_DT27/CH04230P._CP',             # 04
        'ED6_DT27/CH04232P._CP',             # 05
        'ED6_DT27/CH04234P._CP',             # 06
        'ED6_DT27/CH04464P._CP',             # 07
        'ED6_DT07/CH01640P._CP',             # 08
        'ED6_DT07/CH01540P._CP',             # 09
        'ED6_DT07/CH01470P._CP',             # 0A
        'ED6_DT07/CH01150P._CP',             # 0B
        'ED6_DT07/CH01040P._CP',             # 0C
        'ED6_DT07/CH01120P._CP',             # 0D
        'ED6_DT07/CH02480P._CP',             # 0E
        'ED6_DT07/CH02490P._CP',             # 0F
        'ED6_DT07/CH01143P._CP',             # 10
        'ED6_DT07/CH01100P._CP',             # 11
        'ED6_DT07/CH01210P._CP',             # 12
        'ED6_DT07/CH01110P._CP',             # 13
        'ED6_DT07/CH01680P._CP',             # 14
        'ED6_DT07/CH01030P._CP',             # 15
        'ED6_DT06/CH20086P._CP',             # 16
        'ED6_DT07/CH01140P._CP',             # 17
        'ED6_DT07/CH01350P._CP',             # 18
        'ED6_DT07/CH01070P._CP',             # 19
        'ED6_DT07/CH02900P._CP',             # 1A
        'ED6_DT26/CH20783P._CP',             # 1B
        'ED6_DT07/CH01730P._CP',             # 1C
        'ED6_DT07/CH01731P._CP',             # 1D
        'ED6_DT07/CH01410P._CP',             # 1E
        'ED6_DT06/CH20112P._CP',             # 1F
        'ED6_DT26/CH20770P._CP',             # 20
        'ED6_DT27/CH03570P._CP',             # 21
        'ED6_DT27/CH03573P._CP',             # 22
        'ED6_DT07/CH01480P._CP',             # 23
        'ED6_DT26/CH20680P._CP',             # 24
        'ED6_DT26/CH20681P._CP',             # 25
        'ED6_DT26/CH20688P._CP',             # 26
        'ED6_DT27/CH03233P._CP',             # 27
        'ED6_DT26/CH20692P._CP',             # 28
        'ED6_DT26/CH20686P._CP',             # 29
        'ED6_DT26/CH20689P._CP',             # 2A
        'ED6_DT26/CH20690P._CP',             # 2B
        'ED6_DT26/CH20618P._CP',             # 2C
        'ED6_DT27/CH04460P._CP',             # 2D
        'ED6_DT27/CH04463P._CP',             # 2E
        'ED6_DT27/CH03231P._CP',             # 2F
        'ED6_DT26/CH20684P._CP',             # 30
        'ED6_DT27/CH03234P._CP',             # 31
    )

    DeclNpc(
        X                   = 37580,
        Z                   = 1250,
        Y                   = 49800,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
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
        X                   = 40490,
        Z                   = 1250,
        Y                   = 50080,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 71040,
        Z                   = 0,
        Y                   = -9000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 74970,
        Z                   = 0,
        Y                   = 71250,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 100180,
        Z                   = 250,
        Y                   = 33080,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 52990,
        Z                   = 250,
        Y                   = 46290,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 52990,
        Z                   = 250,
        Y                   = 44530,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 39700,
        Z                   = 1250,
        Y                   = 46260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39700,
        Z                   = 1250,
        Y                   = 47860,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 70490,
        Z                   = 250,
        Y                   = 6990,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 71500,
        Z                   = 750,
        Y                   = 7870,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 48810,
        Z                   = 250,
        Y                   = 49340,
        Direction           = 227,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 49630,
        Z                   = 0,
        Y                   = 61870,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 50410,
        Z                   = 0,
        Y                   = 81110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 81160,
        Z                   = 0,
        Y                   = -2940,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 69020,
        Z                   = 250,
        Y                   = 4960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 63010,
        Z                   = 0,
        Y                   = 62930,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 93700,
        Z                   = 0,
        Y                   = 32900,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 53830,
        Z                   = 250,
        Y                   = 24100,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54040,
        Z                   = 250,
        Y                   = 8750,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 9,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 250,
        Y                   = 76500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 45300,
        Z                   = 250,
        Y                   = 77950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 44290,
        Z                   = 250,
        Y                   = 75360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 71040,
        Z                   = 0,
        Y                   = -9000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 100960,
        Z                   = 250,
        Y                   = 34810,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 10,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 59400,
        Z                   = 1250,
        Y                   = 24170,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 70180,
        Z                   = 250,
        Y                   = 4580,
        Direction           = 47,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 70180,
        Z                   = 250,
        Y                   = 4580,
        Direction           = 47,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 70180,
        Z                   = 250,
        Y                   = 4580,
        Direction           = 47,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 17760,
        Z                   = 0,
        Y                   = 63880,
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
        X                   = 29270,
        Z                   = 0,
        Y                   = -950,
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
        X                   = 51010,
        Z                   = 0,
        Y                   = 102170,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1EE,
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


    DeclEvent(
        X                   = 109720,
        Y                   = 1000,
        Z                   = 32980,
        Range               = 2000,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 68,
    )

    DeclEvent(
        X                   = 76740,
        Y                   = 1000,
        Z                   = 23010,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 69,
    )

    DeclEvent(
        X                   = 69950,
        Y                   = 1000,
        Z                   = 14290,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 69,
    )

    DeclEvent(
        X                   = 63260,
        Y                   = 1000,
        Z                   = 22960,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 69,
    )

    DeclEvent(
        X                   = 69910,
        Y                   = 1000,
        Z                   = 31710,
        Range               = 2000,
        Unknown_10          = 0x9C4,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 69,
    )

    DeclEvent(
        X                   = 42920,
        Y                   = 0,
        Z                   = 81110,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 70,
    )

    DeclEvent(
        X                   = 70940,
        Y                   = 0,
        Z                   = -9490,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 71,
    )

    DeclEvent(
        X                   = 75010,
        Y                   = 0,
        Z                   = 71300,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 72,
    )

    DeclEvent(
        X                   = 41440,
        Y                   = 0,
        Z                   = -5500,
        Range               = 39540,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0xDAC,
        Unknown_18          = 0x0,
        Unknown_1C          = 57,
    )

    DeclEvent(
        X                   = 37140,
        Y                   = 0,
        Z                   = 56520,
        Range               = 35140,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x1188C,
        Unknown_18          = 0x0,
        Unknown_1C          = 56,
    )

    DeclEvent(
        X                   = 72300,
        Y                   = 3500,
        Z                   = 50780,
        Range               = 67700,
        Unknown_10          = 0x0,
        Unknown_14          = 0xBF18,
        Unknown_18          = 0x0,
        Unknown_1C          = 51,
    )

    DeclEvent(
        X                   = 72300,
        Y                   = 3500,
        Z                   = 39180,
        Range               = 67700,
        Unknown_10          = 0x0,
        Unknown_14          = 0x9F4C,
        Unknown_18          = 0x0,
        Unknown_1C          = 52,
    )


    DeclActor(
        TriggerX            = 38820,
        TriggerZ            = 1250,
        TriggerY            = 36920,
        TriggerRange        = 800,
        ActorX              = 38820,
        ActorZ              = 2250,
        ActorY              = 36920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 64,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 124880,
        TriggerZ            = -3500,
        TriggerY            = 70940,
        TriggerRange        = 800,
        ActorX              = 124880,
        ActorZ              = -2500,
        ActorY              = 70940,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 67,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_942",          # 00, 0
        "Function_1_BBE",          # 01, 1
        "Function_2_CED",          # 02, 2
        "Function_3_E6A",          # 03, 3
        "Function_4_E8E",          # 04, 4
        "Function_5_F7B",          # 05, 5
        "Function_6_1028",         # 06, 6
        "Function_7_1161",         # 07, 7
        "Function_8_1206",         # 08, 8
        "Function_9_130B",         # 09, 9
        "Function_10_1410",        # 0A, 10
        "Function_11_1434",        # 0B, 11
        "Function_12_1637",        # 0C, 12
        "Function_13_1672",        # 0D, 13
        "Function_14_1796",        # 0E, 14
        "Function_15_19D4",        # 0F, 15
        "Function_16_1C6D",        # 10, 16
        "Function_17_1DF9",        # 11, 17
        "Function_18_1F9F",        # 12, 18
        "Function_19_20FB",        # 13, 19
        "Function_20_2335",        # 14, 20
        "Function_21_249C",        # 15, 21
        "Function_22_2572",        # 16, 22
        "Function_23_2747",        # 17, 23
        "Function_24_290C",        # 18, 24
        "Function_25_2A8A",        # 19, 25
        "Function_26_2D34",        # 1A, 26
        "Function_27_2DE9",        # 1B, 27
        "Function_28_2E4D",        # 1C, 28
        "Function_29_2F74",        # 1D, 29
        "Function_30_30D3",        # 1E, 30
        "Function_31_3AC8",        # 1F, 31
        "Function_32_3B5D",        # 20, 32
        "Function_33_3ED4",        # 21, 33
        "Function_34_4014",        # 22, 34
        "Function_35_40E4",        # 23, 35
        "Function_36_416F",        # 24, 36
        "Function_37_41F5",        # 25, 37
        "Function_38_4240",        # 26, 38
        "Function_39_4281",        # 27, 39
        "Function_40_5496",        # 28, 40
        "Function_41_553A",        # 29, 41
        "Function_42_55CB",        # 2A, 42
        "Function_43_55F8",        # 2B, 43
        "Function_44_6AB0",        # 2C, 44
        "Function_45_6AF7",        # 2D, 45
        "Function_46_6B38",        # 2E, 46
        "Function_47_6B79",        # 2F, 47
        "Function_48_6BC6",        # 30, 48
        "Function_49_6C08",        # 31, 49
        "Function_50_6C70",        # 32, 50
        "Function_51_6CD8",        # 33, 51
        "Function_52_6E95",        # 34, 52
        "Function_53_7052",        # 35, 53
        "Function_54_7AFE",        # 36, 54
        "Function_55_7C2F",        # 37, 55
        "Function_56_7E91",        # 38, 56
        "Function_57_81E3",        # 39, 57
        "Function_58_8348",        # 3A, 58
        "Function_59_839C",        # 3B, 59
        "Function_60_83F0",        # 3C, 60
        "Function_61_8444",        # 3D, 61
        "Function_62_8498",        # 3E, 62
        "Function_63_85C2",        # 3F, 63
        "Function_64_977F",        # 40, 64
        "Function_65_97E7",        # 41, 65
        "Function_66_9831",        # 42, 66
        "Function_67_9887",        # 43, 67
        "Function_68_98D8",        # 44, 68
        "Function_69_98DC",        # 45, 69
        "Function_70_98E0",        # 46, 70
        "Function_71_98E4",        # 47, 71
        "Function_72_98E8",        # 48, 72
        "Function_73_98EC",        # 49, 73
    )


    def Function_0_942(): pass

    label("Function_0_942")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B44")
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x27, 0x80)
    SetChrChipByIndex(0x20, 26)
    SetChrSubChip(0x20, 0)
    SetChrChipByIndex(0x21, 27)
    SetChrSubChip(0x21, 0)
    SetChrFlags(0x20, 0x10)
    SetChrPos(0x20, 70490, 250, 6990, 180)
    SetChrPos(0x1D, 48230, 250, 52350, 270)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    OP_43(0x31, 0x0, 0x0, 0xB)
    OP_43(0x32, 0x0, 0x0, 0xB)
    OP_43(0x33, 0x0, 0x0, 0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_9EE")
    Jump("loc_B44")

    label("loc_9EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_A39")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 32100, 0, 64760, 180)
    OP_43(0x11, 0x0, 0x0, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 32100, 0, 62820, 0)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x3, 0x0, 0xC)
    Jump("loc_B44")

    label("loc_A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_AFD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_END)), "loc_AA2")
    SetChrPos(0x17, 73240, 250, 43820, 270)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x40)
    SetChrPos(0x18, 72140, 250, 43820, 270)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x40)

    def lambda_A83():

        label("loc_A83")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_A83")

    QueueWorkItem2(0x17, 2, lambda_A83)
    OP_43(0x17, 0x3, 0x0, 0x36)
    SetChrChipByIndex(0x18, 36)
    SetChrSubChip(0x18, 0)
    Jump("loc_ACC")

    label("loc_AA2")

    SetChrPos(0x17, 73960, 260, 45140, 0)
    SetChrChipByIndex(0x17, 38)
    SetChrSubChip(0x17, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x40)

    label("loc_ACC")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 32320, 0, 63960, 270)
    OP_43(0x11, 0x0, 0x0, 0x2)
    SetChrPos(0x30, 59400, 1250, 24170, 270)
    Jump("loc_B44")

    label("loc_AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_B44")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 32320, 0, 63960, 270)
    OP_43(0x11, 0x0, 0x0, 0x2)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x10)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_62(0x20, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    label("loc_B44")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_B6F")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 32)
    Jump("loc_B8B")

    label("loc_B6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_B8B")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 39)

    label("loc_B8B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_BAA")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 63)

    label("loc_BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_BBD")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 25)

    label("loc_BBD")

    Return()

    # Function_0_942 end

    def Function_1_BBE(): pass

    label("Function_1_BBE")

    OP_16(0x2, 0xFA0, 0xFFFF4C50, 0xFFFEA070, 0x23005C)
    OP_B1("t4101_n")
    OP_82(0x80, 0x0)
    OP_71(0x411, 0x0)
    ExitThread()
    OP_10(0xB, 0x0)
    OP_10(0xC, 0x1)
    OP_72(0x1009, 0x0)
    ExitThread()
    OP_72(0x100A, 0x0)
    ExitThread()
    OP_72(0x1005, 0x0)
    ExitThread()
    OP_72(0x1006, 0x0)
    ExitThread()
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_72(0x1008, 0x0)
    ExitThread()
    OP_64(0x1, 0x1)
    OP_72(0x100B, 0x0)
    ExitThread()
    OP_B2(0x0, 0x8, 0x80)
    OP_B2(0x0, 0x9, 0x80)
    OP_B2(0x0, 0xA, 0x80)
    OP_B2(0x0, 0xB, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CEC")
    OP_65(0x1, 0x1)
    OP_1B(0xC, 0x0, 0x37)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_C49")
    Jump("loc_CEC")

    label("loc_C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_C84")
    OP_B2(0x1, 0x9, 0x80)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_1C(0x0, 0x0, 0x3C)
    OP_1C(0x1, 0x0, 0x3D)
    OP_1C(0x2, 0x0, 0x3A)
    OP_1C(0x3, 0x0, 0x3B)
    Jump("loc_CEC")

    label("loc_C84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_CCE")
    OP_B2(0x1, 0x8, 0x80)
    OP_B2(0x1, 0x9, 0x80)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_72(0x1003, 0x0)
    ExitThread()
    OP_1C(0x0, 0x0, 0x3C)
    OP_1C(0x1, 0x0, 0x3D)
    OP_1C(0x2, 0x0, 0x3A)
    OP_1C(0x3, 0x0, 0x3B)
    OP_B2(0x1, 0xA, 0x80)
    OP_B2(0x1, 0xB, 0x80)
    Jump("loc_CEC")

    label("loc_CCE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_CEC")
    OP_B2(0x1, 0x9, 0x80)
    OP_62(0x20, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)

    label("loc_CEC")

    Return()

    # Function_1_BBE end

    def Function_2_CED(): pass

    label("Function_2_CED")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D12")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_E54")

    label("loc_D12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_E54")

    label("loc_D2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D44")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_E54")

    label("loc_D44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D5D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_E54")

    label("loc_D5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D76")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_E54")

    label("loc_D76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D8F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_E54")

    label("loc_D8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA8")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_E54")

    label("loc_DA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC1")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_E54")

    label("loc_DC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DDA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_E54")

    label("loc_DDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF3")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_E54")

    label("loc_DF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E0C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_E54")

    label("loc_E0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E25")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_E54")

    label("loc_E25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E3E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_E54")

    label("loc_E3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E54")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_E54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E69")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_E54")

    label("loc_E69")

    Return()

    # Function_2_CED end

    def Function_3_E6A(): pass

    label("Function_3_E6A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E8D")
    OP_8D(0xFE, 102900, 37500, 97550, 28500, 2000)
    Jump("Function_3_E6A")

    label("loc_E8D")

    Return()

    # Function_3_E6A end

    def Function_4_E8E(): pass

    label("Function_4_E8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F7A")
    OP_8E(0xFE, 0xCCF6, 0x0, 0xFFFFF484, 0x9C4, 0x0)
    OP_8E(0xFE, 0xC472, 0x0, 0x8C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xC472, 0x0, 0xF32A, 0x9C4, 0x0)
    OP_8E(0xFE, 0xCFE4, 0x0, 0x100A4, 0x9C4, 0x0)
    OP_8E(0xFE, 0x15AC2, 0x0, 0xFCBC, 0x9C4, 0x0)
    OP_8E(0xFE, 0x16314, 0x0, 0xFB86, 0x9C4, 0x0)
    OP_8E(0xFE, 0x164E0, 0x0, 0x826E, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(4000)
    OP_8E(0xFE, 0x164E0, 0x0, 0x7E86, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x16152, 0x0, 0x4CE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x15B12, 0x0, 0xFFFFF8BC, 0x9C4, 0x0)
    Jump("Function_4_E8E")

    label("loc_F7A")

    Return()

    # Function_4_E8E end

    def Function_5_F7B(): pass

    label("Function_5_F7B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1027")
    OP_8E(0xFE, 0xCE9A, 0x0, 0xF5D2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCB0C, 0x0, 0xF258, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCB0C, 0x0, 0x816, 0x7D0, 0x0)
    OP_8E(0xFE, 0xCEEA, 0x0, 0x33E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15590, 0x0, 0x33E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x158D8, 0x0, 0x6B8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x158D8, 0x0, 0xEF56, 0x7D0, 0x0)
    OP_8E(0xFE, 0x15572, 0x28, 0xF5D2, 0x7D0, 0x0)
    Jump("Function_5_F7B")

    label("loc_1027")

    Return()

    # Function_5_F7B end

    def Function_6_1028(): pass

    label("Function_6_1028")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1160")
    OP_8E(0xFE, 0xD6EC, 0xFA, 0x1360, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6EC, 0xFA, 0x59EC, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEA2E, 0x4E2, 0x59EC, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEA2E, 0x4E2, 0x84B2, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFA5A, 0x4E2, 0x8CC8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10928, 0x4E2, 0x8CC8, 0x9C4, 0x0)
    OP_8E(0xFE, 0x11148, 0x4E2, 0x9470, 0x9C4, 0x0)
    OP_8E(0xFE, 0x111CA, 0x4E2, 0xCAB2, 0x9C4, 0x0)
    OP_8E(0xFE, 0x130BA, 0x4E2, 0xCAB2, 0x9C4, 0x0)
    OP_8E(0xFE, 0x130BA, 0x4E2, 0xBA36, 0x9C4, 0x0)
    OP_8E(0xFE, 0x138D0, 0x4E2, 0xABF4, 0x9C4, 0x0)
    OP_8E(0xFE, 0x138D0, 0x4E2, 0x2DBE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x11968, 0x4E2, 0x2DBE, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10CE8, 0x4E2, 0x272E, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10CE8, 0xFA, 0x16C6, 0x9C4, 0x0)
    Jump("Function_6_1028")

    label("loc_1160")

    Return()

    # Function_6_1028 end

    def Function_7_1161(): pass

    label("Function_7_1161")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1205")
    OP_8E(0xFE, 0x16E04, 0x0, 0x9DBC, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x16E04, 0x0, 0x8084, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x16E04, 0x0, 0x61EE, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1500)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x16E04, 0x0, 0x8084, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1500)
    Jump("Function_7_1161")

    label("loc_1205")

    Return()

    # Function_7_1161 end

    def Function_8_1206(): pass

    label("Function_8_1206")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_130A")
    OP_8E(0xFE, 0xD2F0, 0xFA, 0x1086, 0x9C4, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x14F64, 0xFA, 0x1086, 0x9C4, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x14C44, 0xFA, 0xE6AA, 0x9C4, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x10F86, 0xFA, 0xE6AA, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10F86, 0x4E2, 0xD2AA, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEE7A, 0x4E2, 0xD2AA, 0x9C4, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xEE7A, 0x4E2, 0xB84C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6F6, 0xFA, 0xB84C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6F6, 0xFA, 0x6586, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD246, 0xFA, 0x5E24, 0x9C4, 0x0)
    Jump("Function_8_1206")

    label("loc_130A")

    Return()

    # Function_8_1206 end

    def Function_9_130B(): pass

    label("Function_9_130B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_140F")
    OP_8E(0xFE, 0xD2F0, 0xFA, 0x1086, 0x9C4, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x14F64, 0xFA, 0x1086, 0x9C4, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x14C44, 0xFA, 0xE6AA, 0x9C4, 0x0)
    OP_8C(0xFE, 45, 400)
    Sleep(1500)
    OP_8E(0xFE, 0x10F86, 0xFA, 0xE6AA, 0x9C4, 0x0)
    OP_8E(0xFE, 0x10F86, 0x4E2, 0xD2AA, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEE7A, 0x4E2, 0xD2AA, 0x9C4, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(1500)
    OP_8E(0xFE, 0xEE7A, 0x4E2, 0xB84C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6F6, 0xFA, 0xB84C, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD6F6, 0xFA, 0x6586, 0x9C4, 0x0)
    OP_8E(0xFE, 0xD246, 0xFA, 0x5E24, 0x9C4, 0x0)
    Jump("Function_9_130B")

    label("loc_140F")

    Return()

    # Function_9_130B end

    def Function_10_1410(): pass

    label("Function_10_1410")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1433")
    OP_8D(0xFE, 102900, 37500, 97550, 28500, 2000)
    Jump("Function_10_1410")

    label("loc_1433")

    Return()

    # Function_10_1410 end

    def Function_11_1434(): pass

    label("Function_11_1434")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    OP_8D(0xFE, 67800, 6820, 72340, 2850, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1468")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1636")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15FF")
    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14EF")

    def lambda_14D3():

        label("loc_14D3")

        OP_97(0xFE, 0x11224, 0x11E4, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_14D3")

    QueueWorkItem2(0xFE, 1, lambda_14D3)
    Jump("loc_150E")

    label("loc_14EF")


    def lambda_14F5():

        label("loc_14F5")

        OP_97(0xFE, 0x11224, 0x11E4, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_14F5")

    QueueWorkItem2(0xFE, 1, lambda_14F5)

    label("loc_150E")

    SetChrChipByIndex(0xFE, 28)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)

    label("loc_151D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1555")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_154D")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_1555")

    label("loc_154D")

    Sleep(15)
    Jump("loc_151D")

    label("loc_1555")

    SetChrFlags(0xFE, 0x80)
    OP_44(0xFE, 0x1)
    ClearChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 70140, 250, 4470, 143)

    label("loc_1574")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15FC")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x61A8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15F4")
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 29)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8D(0xFE, 67800, 6820, 72340, 2850, 0)
    Jump("loc_15FC")

    label("loc_15F4")

    Sleep(500)
    Jump("loc_1574")

    label("loc_15FC")

    Jump("loc_1633")

    label("loc_15FF")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1633")

    def lambda_161B():
        OP_8D(0xFE, 67800, 6820, 72340, 2850, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_161B)

    label("loc_1633")

    Jump("loc_1468")

    label("loc_1636")

    Return()

    # Function_11_1434 end

    def Function_12_1637(): pass

    label("Function_12_1637")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1671")
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jump("Function_12_1637")

    label("loc_1671")

    Return()

    # Function_12_1637 end

    def Function_13_1672(): pass

    label("Function_13_1672")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_167F")
    Jump("loc_1792")

    label("loc_167F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_16EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_16BA")

    ChrTalk(    #0
        0xFE,
        "好慢啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "发生什么事了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_16EB")

    label("loc_16BA")


    ChrTalk(    #2
        0xFE,
        "好慢啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "那家伙，在干什么呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_16EB")

    Jump("loc_1792")

    label("loc_16EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1792")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_173B")

    ChrTalk(    #4
        0xFE,
        "我们经常约在这儿等呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "因为这里很容易辨认嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1792")

    label("loc_173B")


    ChrTalk(    #6
        0xFE,
        (
            "我正在这里\x01",
            "等人呢。\x02",
        )
    )

    Jump("loc_1761")

    label("loc_1761")

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "这里很容易辨认吧？\x01",
            "『历史资料馆前』。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1792")

    TalkEnd(0xFE)
    Return()

    # Function_13_1672 end

    def Function_14_1796(): pass

    label("Function_14_1796")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_17A3")
    Jump("loc_19D0")

    label("loc_17A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_18A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1809")

    ChrTalk(    #8
        0xFE,
        (
            "这里面是埃雷波尼亚帝国大使馆。\x01",
            "无关人员禁止进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "请回吧。\x02",
    )

    Jump("loc_1805")

    label("loc_1805")

    CloseMessageWindow()
    Jump("loc_18A3")

    label("loc_1809")


    ChrTalk(    #10
        0xFE,
        (
            "……从刚才开始，\x01",
            "就到处能看到穿黑衣服的男人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "…………啊，不。\x01",
            "咳咳，失礼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "这里面是埃雷波尼亚帝国大使馆。\x01",
            "无关人员禁止进入。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_18A3")

    Jump("loc_19D0")

    label("loc_18A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1974")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1919")

    ChrTalk(    #13
        0xFE,
        (
            "这里面是埃雷波尼亚帝国大使馆。\x01",
            "无关人员禁止进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "如果发生什么事\x01",
            "就会引起国际问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1971")

    label("loc_1919")


    ChrTalk(    #15
        0xFE,
        (
            "这里面是埃雷波尼亚帝国大使馆。\x01",
            "无关人员禁止进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "请回吧。\x02",
    )

    Jump("loc_196D")

    label("loc_196D")

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1971")

    Jump("loc_19D0")

    label("loc_1974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_19D0")

    ChrTalk(    #17
        0xFE,
        (
            "这里面是埃雷波尼亚帝国大使馆。\x01",
            "无关人员禁止进入。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "请回吧。\x02",
    )

    Jump("loc_19CF")

    label("loc_19CF")

    CloseMessageWindow()

    label("loc_19D0")

    TalkEnd(0xFE)
    Return()

    # Function_14_1796 end

    def Function_15_19D4(): pass

    label("Function_15_19D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_19E1")
    Jump("loc_1C69")

    label("loc_19E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_1B22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 7)), scpexpr(EXPR_END)), "loc_1A83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1A2F")

    ChrTalk(    #19
        0xFE,
        "嗯，大哥正义感很强。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "所以不会后悔的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A80")

    label("loc_1A2F")


    ChrTalk(    #21
        0xFE,
        "我大哥也是游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "在百日战役期间\x01",
            "引导市民避难的时候\x01",
            "牺牲了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1A80")

    Jump("loc_1B1F")

    label("loc_1A83")

    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0xFE,
        "…………你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "难不成是游击士？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x103,
        (
            "#1643F咦……？\x01",
            "是没错，怎么了？？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "是、是吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "不，没什么。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F57)

    label("loc_1B1F")

    Jump("loc_1C69")

    label("loc_1B22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1BC8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1B78")

    ChrTalk(    #28
        0xFE,
        "最近有很多奇怪的家伙。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "没有许可的人\x01",
            "是不能通过这里的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC5")

    label("loc_1B78")


    ChrTalk(    #30
        0xFE,
        "这里是共和国大使馆哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "抱歉，\x01",
            "一般人是禁止进入的。\x02",
        )
    )

    Jump("loc_1BC1")

    label("loc_1BC1")

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1BC5")

    Jump("loc_1C69")

    label("loc_1BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1C69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1C1C")

    ChrTalk(    #32
        0xFE,
        "这里是共和国大使馆。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "没有许可的人\x01",
            "是不能通过这里的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C69")

    label("loc_1C1C")


    ChrTalk(    #34
        0xFE,
        "这里是共和国大使馆哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "抱歉，\x01",
            "一般人是禁止进入的。\x02",
        )
    )

    Jump("loc_1C65")

    label("loc_1C65")

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1C69")

    TalkEnd(0xFE)
    Return()

    # Function_15_19D4 end

    def Function_16_1C6D(): pass

    label("Function_16_1C6D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1C7A")
    Jump("loc_1DF5")

    label("loc_1C7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1D53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1CD2")

    ChrTalk(    #36
        0xFE,
        "妈妈是个忘性很大的人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "是不是把潘娜忘了，\x01",
            "已经回去了呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D50")

    label("loc_1CD2")


    ChrTalk(    #38
        0xFE,
        "妈妈，好慢啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "难不成，\x01",
            "把潘娜给忘了吗？\x02",
        )
    )

    Jump("loc_1D14")

    label("loc_1D14")

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "不行啊。\x02",
    )

    Jump("loc_1D4C")

    label("loc_1D4C")

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1D50")

    Jump("loc_1DF5")

    label("loc_1D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1DF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1DAD")

    ChrTalk(    #42
        0xFE,
        "妈妈还在百货店买东西吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "真没办法啊，唉。\x01",
            "还是在这里等吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DF5")

    label("loc_1DAD")


    ChrTalk(    #44
        0xFE,
        "我和妈妈走散了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "不过没关系。\x01",
            "潘娜自己一个人也能回去。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1DF5")

    TalkEnd(0xFE)
    Return()

    # Function_16_1C6D end

    def Function_17_1DF9(): pass

    label("Function_17_1DF9")

    TalkBegin(0xFE)
    SetMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1E0B")
    Jump("loc_1F96")

    label("loc_1E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_1EC4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1E56")

    ChrTalk(    #46
        0xFE,
        (
            "#3S大家，快看！\x01",
            "我在这里哦～！#2S\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    Jump("loc_1EC1")

    label("loc_1E56")


    ChrTalk(    #47
        0xFE,
        (
            "咦，怎么回事。\x01",
            "为何心里好难受……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(    #48
        0xFE,
        (
            "#3S大家，快看！\x01",
            "我在这里哦～！#2S\x02",
        )
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1EC1")

    Jump("loc_1F96")

    label("loc_1EC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_1F96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1EF3")

    ChrTalk(    #49
        0xFE,
        "看啊，世界多么美丽……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F96")

    label("loc_1EF3")


    ChrTalk(    #50
        0xFE,
        (
            "啊啊，温暖的阳光……\x01",
            "流动的云彩……温柔的微风……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "看，看啊，利库斯……\x01",
            "世界正在祝福着我们！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    ChrTalk(    #52
        0xFE,
        "#4S王立学院万岁——！#2S\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1F96")

    ClearMapFlags(0x20)
    TalkEnd(0xFE)
    Return()

    # Function_17_1DF9 end

    def Function_18_1F9F(): pass

    label("Function_18_1F9F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_1FAC")
    Jump("loc_20F7")

    label("loc_1FAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_200A")

    ChrTalk(    #53
        0xFE,
        (
            "不过，没关系吧。\x01",
            "安敦就是安敦嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "放着不管的话，\x01",
            "一定又会陷入烦恼了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20F7")

    label("loc_200A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_20F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2071")

    ChrTalk(    #55
        0xFE,
        (
            "怎么了，安敦。\x01",
            "从没见过你这么闪耀啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "小心别发光太多，\x01",
            "导致燃烧殆尽哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20F7")

    label("loc_2071")


    ChrTalk(    #57
        0xFE,
        (
            "不知道是出了什么差错，\x01",
            "安敦那家伙竟然考上了王立学院。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "还有抱着随便的态度去参加考试的我。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "这是女神的恶作剧吗。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_20F7")

    TalkEnd(0xFE)
    Return()

    # Function_18_1F9F end

    def Function_19_20FB(): pass

    label("Function_19_20FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_2108")
    Jump("loc_2331")

    label("loc_2108")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_2246")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2196")

    ChrTalk(    #60
        0xFE,
        (
            "现在去买利贝尔通讯，\x01",
            "就能在头版头条上看到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "难得我还买了\x01",
            "香槟和蛋糕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "这下一点也没有\x01",
            "庆祝的气氛了啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2243")

    label("loc_2196")


    ChrTalk(    #63
        0xFE,
        (
            "哎呀，我说你！\x01",
            "知道吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "据说致力于\x01",
            "飞艇公社筹建的那个\x01",
            "霍尔登先生去世了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "怎、怎么会这样。\x01",
            "我还是他的支持者呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x151,
        "#1654F…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2243")

    Jump("loc_2331")

    label("loc_2246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_2331")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_22A7")

    ChrTalk(    #67
        0xFE,
        (
            "首先去百货店\x01",
            "买些必要的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "至少要有\x01",
            "香槟和蛋糕吧。\x02",
        )
    )

    Jump("loc_22A3")

    label("loc_22A3")

    CloseMessageWindow()
    Jump("loc_2331")

    label("loc_22A7")


    ChrTalk(    #69
        0xFE,
        (
            "定期船赛希莉亚号\x01",
            "今年已经２０岁了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "因此我打算开办一个\x01",
            "个人的纪念庆祝会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "首先要去百货店\x01",
            "买些必要的东西才行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_2331")

    TalkEnd(0xFE)
    Return()

    # Function_19_20FB end

    def Function_20_2335(): pass

    label("Function_20_2335")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_2342")
    Jump("loc_2498")

    label("loc_2342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_23E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_238A")

    ChrTalk(    #72
        0xFE,
        (
            "开店的那个人\x01",
            "好像还是学生呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "是打工吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_23DD")

    label("loc_238A")


    ChrTalk(    #74
        0xFE,
        (
            "那个冰淇淋店，\x01",
            "好像是最近才开的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "开店的那个人\x01",
            "好像还是学生呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_23DD")

    Jump("loc_2498")

    label("loc_23E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_2498")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2449")

    ChrTalk(    #76
        0xFE,
        (
            "那里原来就有\x01",
            "冰淇淋店吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "我记得之前\x01",
            "好像没有吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "是新开的店吧？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2498")

    label("loc_2449")

    OP_8C(0xFE, 270, 0)

    ChrTalk(    #79
        0xFE,
        (
            "咦，\x01",
            "那里原来就有冰淇淋店吗？\x02",
        )
    )

    Jump("loc_247A")

    label("loc_247A")

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "唔，没注意过啊……\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_2498")

    TalkEnd(0xFE)
    Return()

    # Function_20_2335 end

    def Function_21_249C(): pass

    label("Function_21_249C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_256E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_2500")

    NpcTalk(    #81
        0xFE,
        "长雀斑的少女",
        (
            "#1660F唉，好闲啊～……\x02\x03",

            "要不要吃点\x01",
            "冰淇淋呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_256E")

    label("loc_2500")


    NpcTalk(    #82
        0xFE,
        "长雀斑的少女",
        (
            "#1660F唉，好闲啊～……\x02\x03",

            "《不为人知的格兰赛尔\x01",
            "  景观探访系列》\x01",
            "也看腻了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_256E")

    TalkEnd(0xFE)
    Return()

    # Function_21_249C end

    def Function_22_2572(): pass

    label("Function_22_2572")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_257F")
    Jump("loc_2743")

    label("loc_257F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_264F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_25D5")

    ChrTalk(    #83
        0xFE,
        (
            "卢安也是靠\x01",
            "发展旅游业热闹起来的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "真想去一次看看啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_264C")

    label("loc_25D5")


    ChrTalk(    #85
        0xFE,
        (
            "话说回来，\x01",
            "听说最近卢安也很热闹啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "戴尔蒙市长\x01",
            "似乎在旅游业上下了不少气力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "真想去一次看看啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_264C")

    Jump("loc_2743")

    label("loc_264F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_2743")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_26C5")

    ChrTalk(    #88
        0xFE,
        (
            "对了，听说温德曼市长的女儿\x01",
            "在王立学院里的成绩也很优秀呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "哈哈，柏斯的未来值得期待啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2743")

    label("loc_26C5")


    ChrTalk(    #90
        0xFE,
        (
            "你知道柏斯的\x01",
            "温德曼市长吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "不管是在柏斯地区锻炼出来的经营手段，\x01",
            "还是战灾复兴时的领导能力，\x01",
            "都是相当优秀啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_2743")

    TalkEnd(0xFE)
    Return()

    # Function_22_2572 end

    def Function_23_2747(): pass

    label("Function_23_2747")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_2754")
    Jump("loc_2908")

    label("loc_2754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_282C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_27CA")

    ChrTalk(    #92
        0xFE,
        (
            "王太子夫妇\x01",
            "有一位子嗣哦。\x01",
            "名叫科洛蒂娅殿下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "虽然年纪还小，\x01",
            "不过真是个可爱的小公主啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2829")

    label("loc_27CA")


    ChrTalk(    #94
        0xFE,
        (
            "这么说来，\x01",
            "王太子夫妇应该是有子嗣的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "名字……对了，\x01",
            "记得是叫科洛蒂娅殿下。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_2829")

    Jump("loc_2908")

    label("loc_282C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_2908")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_28A4")

    ChrTalk(    #96
        0xFE,
        (
            "尤迪斯王太子夫妇\x01",
            "去世的时候\x01",
            "我真是深受打击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "即使现在\x01",
            "我还记得他们的笑容……\x02",
        )
    )

    Jump("loc_28A0")

    label("loc_28A0")

    CloseMessageWindow()
    Jump("loc_2908")

    label("loc_28A4")


    ChrTalk(    #98
        0xFE,
        (
            "尤迪斯王太子夫妇\x01",
            "去世的时候\x01",
            "我真是深受打击。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "他们两人\x01",
            "明明那么善良……\x02",
        )
    )

    Jump("loc_2904")

    label("loc_2904")

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_2908")

    TalkEnd(0xFE)
    Return()

    # Function_23_2747 end

    def Function_24_290C(): pass

    label("Function_24_290C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_2919")
    Jump("loc_2A86")

    label("loc_2919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_29B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2970")

    ChrTalk(    #100
        0xFE,
        (
            "欢迎光临。\x01",
            "要来点冰淇淋吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "很美味很美味的\x01",
            "冰淇淋哦～⊙\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29AE")

    label("loc_2970")


    ChrTalk(    #102
        0xFE,
        "啊，是刚才的客人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "十分感谢。\x01",
            "欢迎再次光临。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_29AE")

    Jump("loc_2A86")

    label("loc_29B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_29BF")
    Call(0, 30)
    Jump("loc_2A86")

    label("loc_29BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_2A86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2A3D")

    ChrTalk(    #104
        0xFE,
        (
            "其实我\x01",
            "还是个学生……\x02",
        )
    )

    Jump("loc_29F2")

    label("loc_29F2")

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "这份兼职，\x01",
            "好像很合我的个性呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "呵呵，要不要当成本职呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A86")

    label("loc_2A3D")


    ChrTalk(    #107
        0xFE,
        (
            "欢迎光临。\x01",
            "要来点冰淇淋吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "很美味很美味的\x01",
            "冰淇淋哦～。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_2A86")

    TalkEnd(0xFE)
    Return()

    # Function_24_290C end

    def Function_25_2A8A(): pass

    label("Function_25_2A8A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 68770, 250, -9000, 0)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 77220, 250, 71250, 180)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 38350, 1250, 48810, 315)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 72940, 250, 45680, 180)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, 72920, 250, 44130, 0)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 48280, 250, 49330, 180)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, 48150, 250, 48100, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 39220, 1250, 48760, 270)
    SetChrChipByIndex(0x24, 35)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 24)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x2B, 0x80)
    SetChrPos(0x2B, 41350, 1250, 47920, 315)
    ClearChrFlags(0x2C, 0x80)
    SetChrPos(0x2C, 40300, 1250, 48720, 270)
    OP_43(0x1C, 0x0, 0x0, 0x1A)
    OP_43(0x1D, 0x0, 0x0, 0x1B)
    OP_43(0x1F, 0x0, 0x0, 0x1C)
    OP_43(0x1E, 0x0, 0x0, 0x1C)
    OP_43(0x23, 0x0, 0x0, 0x1D)
    OP_43(0x10, 0x0, 0x0, 0x1C)
    OP_62(0x21, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_6D(70530, 0, 180, 0)
    OP_67(0, 9250, -10000, 0)
    OP_6B(3900, 0)
    OP_6C(33000, 0)
    OP_6E(406, 0)

    def lambda_2C32():
        OP_6D(71110, 0, 47280, 10000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2C32)

    def lambda_2C4A():
        OP_67(0, 9250, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C4A)

    def lambda_2C62():
        OP_6B(3900, 10000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2C62)

    def lambda_2C72():
        OP_6C(33000, 10000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2C72)

    def lambda_2C82():
        OP_6E(406, 3000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2C82)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)

    def lambda_2CA1():
        OP_6D(41760, 1250, 46430, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2CA1)

    def lambda_2CB9():
        OP_67(0, 9250, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2CB9)

    def lambda_2CD1():
        OP_6B(3900, 6000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2CD1)

    def lambda_2CE1():
        OP_6C(333000, 6000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2CE1)

    def lambda_2CF1():
        OP_6E(406, 6000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2CF1)
    Sleep(4000)
    OP_62(0x1B, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_23(0xF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4200   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_25_2A8A end

    def Function_26_2D34(): pass

    label("Function_26_2D34")

    Sleep(4000)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 64550, 1810, 22920, 270)
    OP_72(0x1001, 0x0)
    ExitThread()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    OP_8E(0xFE, 0xEC9A, 0x4E2, 0x5AA0, 0x1388, 0x0)
    OP_6F(0x1, 59)
    OP_70(0x1, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xEB0A, 0x4E2, 0xB900, 0x1388, 0x0)
    OP_8E(0xFE, 0xD6E2, 0xFA, 0xB946, 0x1388, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xA5FA, 0x4E2, 0xB914, 0x1388, 0x0)
    Return()

    # Function_26_2D34 end

    def Function_27_2DE9(): pass

    label("Function_27_2DE9")

    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 68820, 250, 6150, 0)
    OP_8E(0xFE, 0x1112A, 0x5D2, 0x3412, 0x7D0, 0x0)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    OP_8E(0xFE, 0x10FC2, 0x6D6, 0x401A, 0x7D0, 0x0)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    Return()

    # Function_27_2DE9 end

    def Function_28_2E4D(): pass

    label("Function_28_2E4D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2F73")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E89")
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_2F70")

    label("loc_2E89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EB0")
    Sleep(1300)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_2F70")

    label("loc_2EB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ED7")
    Sleep(1600)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_2F70")

    label("loc_2ED7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EFE")
    Sleep(1900)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_2F70")

    label("loc_2EFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F25")
    Sleep(2200)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_2F70")

    label("loc_2F25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F4C")
    Sleep(2500)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("loc_2F70")

    label("loc_2F4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F70")
    Sleep(2800)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    label("loc_2F70")

    Jump("Function_28_2E4D")

    label("loc_2F73")

    Return()

    # Function_28_2E4D end

    def Function_29_2F74(): pass

    label("Function_29_2F74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30D2")
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FB8")
    Sleep(1000)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Jump("loc_30CF")

    label("loc_2FB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE7")
    Sleep(1300)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Jump("loc_30CF")

    label("loc_2FE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3016")
    Sleep(160)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Jump("loc_30CF")

    label("loc_3016")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3045")
    Sleep(1900)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Jump("loc_30CF")

    label("loc_3045")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3074")
    Sleep(2200)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Jump("loc_30CF")

    label("loc_3074")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A3")
    Sleep(2500)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Jump("loc_30CF")

    label("loc_30A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30CF")
    Sleep(2800)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)

    label("loc_30CF")

    Jump("Function_29_2F74")

    label("loc_30D2")

    Return()

    # Function_29_2F74 end

    def Function_30_30D3(): pass

    label("Function_30_30D3")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(37620, 1250, 49780, 0)
    OP_67(0, 7540, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x151, 38880, 1250, 48440, 315)
    SetChrPos(0x103, 38660, 1250, 46800, 0)
    TurnDirection(0x10, 0x151, 0)
    Sleep(1500)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    OP_62(0x151, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #109
        "\x07\x05爱娜购买了两个冰淇淋。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    TurnDirection(0x151, 0x103, 400)
    Sleep(500)

    def lambda_31D6():
        OP_8F(0xFE, 0x9704, 0x4E2, 0xBB30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_31D6)
    WaitChrThread(0x151, 0x1)
    Sleep(500)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_3217():
        OP_6D(34940, 1450, 43480, 5000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_3217)

    def lambda_322F():
        OP_67(0, 5940, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_322F)

    def lambda_3247():
        OP_6C(300000, 5000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_3247)

    def lambda_3257():

        label("loc_3257")

        TurnDirection(0xFE, 0x151, 400)
        OP_48()
        Jump("loc_3257")

    QueueWorkItem2(0x103, 3, lambda_3257)

    def lambda_3268():
        OP_8E(0xFE, 0x9114, 0x4E2, 0xB644, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3268)
    WaitChrThread(0x151, 0x1)

    def lambda_3288():
        OP_8E(0xFE, 0x9114, 0x4E2, 0xA53C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3288)
    Sleep(1000)
    OP_44(0x103, 0x3)
    OP_43(0x103, 0x3, 0x0, 0x1F)
    WaitChrThread(0x151, 0x1)

    def lambda_32B8():
        OP_8E(0xFE, 0x8D90, 0x4E2, 0xA53C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_32B8)
    WaitChrThread(0x151, 0x1)
    SetChrFlags(0x151, 0x40)
    OP_22(0x8F, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x151, 40)
    SetChrSubChip(0x151, 0)
    SetChrFlags(0x151, 0x4)
    SetChrPos(0x151, 35580, 1450, 42300, 90)
    Sleep(250)
    WaitChrThread(0x103, 0x3)
    Sleep(500)
    WaitChrThread(0x39, 0x0)
    Sleep(500)
    OP_62(0x103, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #110
        0x103,
        (
            "#1645F#2P我都说\x01",
            "我不要了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x151,
        (
            "#1651F没关系。\x01",
            "很美味的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        "#1647F#2P（……什么没关系啊！）\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_33BE():
        OP_6D(37860, 4500, 36920, 3000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_33BE)

    def lambda_33D6():
        OP_67(0, 6040, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_33D6)

    def lambda_33EE():
        OP_6C(270000, 3000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_33EE)
    WaitChrThread(0x39, 0x0)
    Sleep(200)
    SetChrSubChip(0x151, 2)
    Sleep(500)

    ChrTalk(    #113
        0x151,
        (
            "#1654F#3P（差不多快正午了……）\x02\x03",

            "（还有２４个小时……\x01",
            "  没有多少时间了……）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    SetChrPos(0x11, 68800, 1250, 38200, 0)
    SetChrPos(0x12, 68800, 250, 46000, 180)

    def lambda_34A6():
        OP_6D(65286, 250, 44280, 3500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_34A6)

    def lambda_34BE():
        OP_67(0, 8300, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_34BE)

    def lambda_34D6():
        OP_6B(2920, 3500)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_34D6)

    def lambda_34E6():
        OP_6C(225000, 3500)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_34E6)

    def lambda_34F6():
        OP_8E(0xFE, 0x10CC0, 0xFA, 0xACA8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_34F6)
    SetChrSubChip(0x151, 0)
    WaitChrThread(0x39, 0x0)
    WaitChrThread(0x11, 0x1)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)
    Sleep(500)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)
    OP_8C(0x11, 180, 400)

    def lambda_356A():
        OP_8E(0xFE, 0x10CC0, 0x4E2, 0x8408, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_356A)
    Sleep(500)
    OP_8C(0x12, 0, 400)

    def lambda_3591():
        OP_8E(0xFE, 0x10CC0, 0x4E2, 0xD098, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3591)
    Sleep(1000)
    SetMessageWindowPos(350, 50, -1, -1)
    SetChrName("爱娜")

    AnonymousTalk(    #114
        "\x07\x00#1656F（虽然有点危险……）\x02",
    )

    Jump("loc_35E6")

    label("loc_35E6")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(400, 50, -1, -1)
    SetChrName("雪拉扎德")

    AnonymousTalk(    #115
        "\x07\x00#1644F#3S……喂！#2S\x02",
    )

    Jump("loc_3632")

    label("loc_3632")

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrSubChip(0x103, 2)
    Fade(500)
    OP_6D(34940, 1450, 43480, 0)
    OP_67(0, 5940, -10000, 0)
    OP_6B(2880, 0)
    OP_6C(300000, 0)
    OP_6E(262, 0)
    Sleep(1000)
    OP_44(0x11, 0x1)
    OP_44(0x12, 0x1)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)

    ChrTalk(    #116
        0x151,
        "#1653F咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x103,
        (
            "#1642F#2P从刚才开始就一直心不在焉。\x02\x03",

            "发什么呆啊！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x151, 1)
    Sleep(300)

    ChrTalk(    #118
        0x151,
        (
            "#1653F……哎…………\x02\x03",

            "#1651F怎么了，雪拉扎德小姐。\x01",
            "表情好可怕……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x103,
        (
            "#1646F#2P……你啊，\x01",
            "是不是瞒了我什么事情。\x02\x03",

            "从刚才开始\x01",
            "就一副可疑的样子。\x02\x03",

            "#1648F……快招了吧。\x02\x03",

            "还是说\x01",
            "有什么不安的事？\x02",
        )
    )

    Jump("loc_37FA")

    label("loc_37FA")

    CloseMessageWindow()

    ChrTalk(    #120
        0x151,
        (
            "#1652F…………………………\x02\x03",

            "………………其实我……\x02\x03",

            "#1651F好像有些东西\x01",
            "忘在酒店里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x103,
        "#1647F#2P唔…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #122
        0x103,
        (
            "#1646F#2P（又想蒙混过关了……！）\x02\x03",

            "#1648F（看来打算\x01",
            "  装傻装到底了。\x01",
            "  哼，正好。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x151,
        (
            "#1650F可以回酒店\x01",
            "取一下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        (
            "#1646F#2P……好啊。\x01",
            "我陪你去。\x02\x03",

            "#1642F（直到你露出马脚来！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x151,
        (
            "#1651F谢谢你，雪拉扎德小姐。\x01",
            "那我们走吧。\x02\x03",

            "……走南边的大道吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x103,
        "#1642F#2P…………明白了。\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrPos(0x151, 36240, 1250, 42300, 90)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    ClearChrFlags(0x151, 0x4)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    Fade(250)
    SetChrPos(0x103, 36240, 1250, 43680, 90)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    ClearChrFlags(0x103, 0x4)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    ClearChrFlags(0x103, 0x40)
    ClearChrFlags(0x151, 0x40)
    SetChrSubChip(0x11, 0)
    SetChrSubChip(0x12, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 32100, 0, 64760, 180)
    OP_43(0x11, 0x0, 0x0, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 32100, 0, 62820, 0)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x3, 0x0, 0xC)
    OP_B2(0x0, 0xA, 0x80)
    OP_B2(0x0, 0xB, 0x80)
    OP_B2(0x0, 0x8, 0x80)
    OP_A2(0x2F4C)
    EventEnd(0x0)
    Return()

    # Function_30_30D3 end

    def Function_31_3AC8(): pass

    label("Function_31_3AC8")


    def lambda_3ACE():
        OP_8E(0xFE, 0x9114, 0x4E2, 0xB02C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3ACE)
    WaitChrThread(0x103, 0x1)

    def lambda_3AEE():
        OP_8E(0xFE, 0x9114, 0x4E2, 0xAAA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3AEE)
    WaitChrThread(0x103, 0x1)

    def lambda_3B0E():
        OP_8E(0xFE, 0x8D90, 0x4E2, 0xAAA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3B0E)
    WaitChrThread(0x103, 0x1)
    SetChrFlags(0x103, 0x40)
    OP_22(0x8F, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x103, 39)
    SetChrSubChip(0x103, 0)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x103, 35580, 1450, 43680, 90)
    Sleep(250)
    Return()

    # Function_31_3AC8 end

    def Function_32_3B5D(): pass

    label("Function_32_3B5D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(50600, 0, 45600, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(354, 0)
    SetChrPos(0x103, 51540, 0, 65160, 180)
    SetChrPos(0x151, 50540, 0, 63540, 180)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    SetChrPos(0x11, 51740, 0, 70120, 180)
    SetChrPos(0x12, 50320, 0, 68900, 180)
    SetChrChipByIndex(0x11, 41)
    SetChrChipByIndex(0x12, 41)
    SetChrChipByIndex(0x13, 41)
    SetChrChipByIndex(0x14, 41)
    SetChrChipByIndex(0x15, 41)
    SetChrChipByIndex(0x16, 41)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x27, 0x80)
    FadeToBright(1000, 0)

    def lambda_3C4F():
        OP_6D(50600, 0, 25600, 8000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_3C4F)

    def lambda_3C67():
        OP_6B(2700, 8000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_3C67)

    def lambda_3C77():
        OP_6E(302, 8000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_3C77)

    def lambda_3C87():
        OP_67(0, 7000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_3C87)

    def lambda_3C9F():
        OP_8E(0xFE, 0xC56C, 0x0, 0xB7C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3C9F)
    Sleep(10)

    def lambda_3CBF():
        OP_8E(0xFE, 0xC954, 0x0, 0x14F0, 0x1F72, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3CBF)
    Sleep(900)

    def lambda_3CDF():
        OP_8E(0xFE, 0xC490, 0x0, 0x22C4, 0x1E78, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3CDF)
    Sleep(100)

    def lambda_3CFF():
        OP_8E(0xFE, 0xCA1C, 0x0, 0x2788, 0x1EDC, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3CFF)
    Sleep(7000)
    Fade(250)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x151, 0xFF)
    OP_44(0x103, 0xFF)
    OP_6D(50720, 0, 2400, 0)
    OP_67(0, 6360, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(304000, 0)
    OP_6E(322, 0)
    SetChrPos(0x151, 51060, 0, 13620, 180)
    SetChrPos(0x103, 51060, 0, 16620, 180)
    SetChrPos(0x11, 51060, 0, 32900, 180)
    SetChrPos(0x12, 51060, 0, 35200, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x13, 18600, 0, -1640, 90)
    SetChrPos(0x14, 17300, 0, -2880, 90)

    def lambda_3DE1():
        OP_6D(50720, 0, -400, 2500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_3DE1)

    def lambda_3DF9():
        OP_6B(2800, 2500)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_3DF9)
    Sleep(250)
    OP_43(0x151, 0x3, 0x0, 0x21)
    Sleep(100)
    OP_43(0x103, 0x3, 0x0, 0x22)
    Sleep(2000)
    OP_43(0x13, 0x3, 0x0, 0x25)
    Sleep(100)
    OP_43(0x14, 0x3, 0x0, 0x26)
    OP_43(0x11, 0x3, 0x0, 0x23)
    OP_43(0x12, 0x3, 0x0, 0x24)
    Sleep(500)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x15, 17300, 0, -2080, 90)

    def lambda_3E67():
        OP_8E(0xFE, 0x15A7C, 0x0, 0xFFFFF7E0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3E67)
    Sleep(500)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x40)
    SetChrPos(0x16, 18600, 0, 640, 90)

    def lambda_3EA2():
        OP_8E(0xFE, 0x1633C, 0x0, 0x280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3EA2)
    Sleep(3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_32_3B5D end

    def Function_33_3ED4(): pass

    label("Function_33_3ED4")


    def lambda_3EDA():
        OP_8E(0xFE, 0xC774, 0x0, 0x190, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3EDA)
    WaitChrThread(0x151, 0x1)

    def lambda_3EFA():
        OP_8E(0xFE, 0xC2EC, 0x0, 0xFFFFFD58, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3EFA)
    WaitChrThread(0x151, 0x1)

    def lambda_3F1A():
        OP_8E(0xFE, 0xBF04, 0x0, 0xFFFFF970, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3F1A)
    WaitChrThread(0x151, 0x1)

    def lambda_3F3A():
        OP_8E(0xFE, 0xBB80, 0x0, 0xFFFFF970, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3F3A)
    WaitChrThread(0x151, 0x1)

    def lambda_3F5A():
        OP_8E(0xFE, 0xBB1C, 0x0, 0xFFFFF970, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3F5A)
    WaitChrThread(0x151, 0x1)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x151, 0x0, 0x0, 0x0, 0x320, 0x1388)
    Sleep(500)
    OP_8C(0x151, 90, 500)
    Sleep(200)

    def lambda_3FB9():
        OP_8E(0xFE, 0x15E50, 0x0, 0xFFFFF970, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3FB9)
    WaitChrThread(0x151, 0x1)

    def lambda_3FD9():
        OP_8E(0xFE, 0x16300, 0x0, 0xFFFFFE20, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3FD9)
    WaitChrThread(0x151, 0x1)

    def lambda_3FF9():
        OP_8E(0xFE, 0x16300, 0x0, 0xC0A8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_3FF9)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_33_3ED4 end

    def Function_34_4014(): pass

    label("Function_34_4014")


    def lambda_401A():
        OP_8E(0xFE, 0xC774, 0x0, 0x50, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_401A)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 270, 500)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    def lambda_405D():
        OP_8F(0xFE, 0xCB5C, 0x0, 0x50, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_405D)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 90, 500)
    Sleep(200)

    def lambda_4089():
        OP_8E(0xFE, 0x15680, 0x0, 0x50, 0x1EDC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4089)
    WaitChrThread(0x103, 0x1)

    def lambda_40A9():
        OP_8E(0xFE, 0x15A68, 0x0, 0x438, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_40A9)
    WaitChrThread(0x103, 0x1)

    def lambda_40C9():
        OP_8E(0xFE, 0x15A68, 0x0, 0xC3A0, 0x1E14, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_40C9)
    WaitChrThread(0x103, 0x1)
    Return()

    # Function_34_4014 end

    def Function_35_40E4(): pass

    label("Function_35_40E4")


    def lambda_40EA():
        OP_8E(0xFE, 0xC774, 0x0, 0x44C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_40EA)
    WaitChrThread(0x11, 0x1)

    def lambda_410A():
        OP_8E(0xFE, 0xC968, 0x0, 0x258, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_410A)
    WaitChrThread(0x11, 0x1)

    def lambda_412A():
        OP_8E(0xFE, 0x15860, 0x0, 0x258, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_412A)
    WaitChrThread(0x11, 0x1)
    Sleep(750)

    def lambda_414F():
        OP_8E(0xFE, 0x15860, 0x0, 0xC5A8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_414F)
    Sleep(50)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_35_40E4 end

    def Function_36_416F(): pass

    label("Function_36_416F")


    def lambda_4175():
        OP_8E(0xFE, 0xC774, 0x0, 0xFFFFFF9C, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4175)
    WaitChrThread(0x12, 0x1)

    def lambda_4195():
        OP_8E(0xFE, 0xC968, 0x0, 0xFFFFFDA8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4195)
    WaitChrThread(0x12, 0x1)

    def lambda_41B5():
        OP_8E(0xFE, 0x15F40, 0x0, 0xFFFFFDA8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_41B5)
    WaitChrThread(0x12, 0x1)
    Sleep(50)

    def lambda_41DA():
        OP_8E(0xFE, 0x15F40, 0x0, 0xC094, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_41DA)
    WaitChrThread(0x12, 0x1)
    Return()

    # Function_36_416F end

    def Function_37_41F5(): pass

    label("Function_37_41F5")


    def lambda_41FB():
        OP_8E(0xFE, 0x1633C, 0x0, 0xFFFFF998, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_41FB)
    WaitChrThread(0x13, 0x1)
    Sleep(250)

    def lambda_4220():
        OP_8E(0xFE, 0x1633C, 0x0, 0xC1E8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4220)
    Sleep(300)
    WaitChrThread(0x13, 0x1)
    Return()

    # Function_37_41F5 end

    def Function_38_4240(): pass

    label("Function_38_4240")


    def lambda_4246():
        OP_8E(0xFE, 0x15A7C, 0x0, 0xFFFFF4C0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4246)
    WaitChrThread(0x14, 0x1)

    def lambda_4266():
        OP_8E(0xFE, 0x15A7C, 0x0, 0xBC98, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4266)
    WaitChrThread(0x14, 0x1)
    Return()

    # Function_38_4240 end

    def Function_39_4281(): pass

    label("Function_39_4281")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(102420, 1250, 14240, 0)
    OP_67(0, 9840, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(135000, 0)
    OP_6E(328, 0)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x151, 0x4)
    SetChrPos(0x103, 103800, 1250, 16600, 270)
    SetChrPos(0x151, 102560, 1250, 15500, 270)
    SetChrChipByIndex(0x103, 49)
    SetChrSubChip(0x103, 0)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x2F, 0x80)

    def lambda_431A():
        OP_6D(103660, 1250, 15100, 6000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_431A)

    def lambda_4332():
        OP_67(0, 4280, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_4332)

    def lambda_434A():
        OP_6C(145000, 6000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_434A)

    def lambda_435A():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_435A)
    OP_20(0x1770)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x39, 0x0)

    def lambda_437E():
        OP_8F(0xFE, 0x18FC4, 0x4E2, 0x4178, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_437E)
    WaitChrThread(0x151, 0x1)
    Sleep(300)

    ChrTalk(    #127
        0x151,
        "#1652F……伤脑筋啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x103,
        (
            "#1645F#5P呼，呼…………\x01",
            "总、总算是……\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x8F, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #129
        0x103,
        (
            "#1642F#5P你、你差不多\x01",
            "该说出来了吧。\x02\x03",

            "#1644F那些黑衣的家伙是什么人？\x02\x03",

            "为什么要追杀我们？\x02\x03",

            "……你的目的是什么！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 400)
    Sleep(300)

    ChrTalk(    #130
        0x151,
        "#1656F#4P唔…………\x02",
    )

    CloseMessageWindow()
    OP_59()

    ChrTalk(    #131
        0x103,
        "#1646F#5P再装傻就打你哦。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 4)
    SetChrSubChip(0x103, 0)
    Sleep(500)

    ChrTalk(    #132
        0x103,
        "#1648F#5P………………用这根鞭子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x151,
        (
            "#1655F#4P看、看起来好像很痛。\x02\x03",

            "#1654F………………………………\x02\x03",

            "#1656F……其实，那些人……\x02\x03",

            "好像是\x01",
            "想来抓我的。\x02",
        )
    )

    Jump("loc_45D5")

    label("loc_45D5")

    CloseMessageWindow()
    OP_59()
    Fade(400)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    Sleep(800)

    ChrTalk(    #134
        0x103,
        (
            "#1645F#5P……这我也能看出来。\x02\x03",

            "#1642F我想知道的 \x01",
            "是你的事情。\x02\x03",

            "为什么\x01",
            "会被那些人追杀，\x01",
            "给我好好说明白。\x02",
        )
    )

    Jump("loc_4675")

    label("loc_4675")

    CloseMessageWindow()

    ChrTalk(    #135
        0x151,
        "#1654F#4P这、这个啊……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x103, 104040, 1250, 17520, 250)
    SetChrPos(0x151, 102460, 1250, 16600, 60)
    OP_6D(102880, 750, 14840, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(186000, 0)
    OP_6E(262, 0)

    def lambda_4705():
        OP_6D(102880, 1250, 14840, 18000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_4705)

    def lambda_471D():
        OP_67(0, 4200, -10000, 18000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_471D)
    Sleep(1000)
    OP_1D(0x73)
    Sleep(500)

    ChrTalk(    #136
        0x151,
        (
            "#1656F#2P嗯，那个……\x01",
            "这是一个月之前的事了……\x02\x03",

            "和我相依为命的\x01",
            "祖父去世了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x103,
        "#1642F你祖父？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x151,
        (
            "#1654F#2P……嗯。\x02\x03",

            "祖父是一位资产家，\x01",
            "所以也给我\x01",
            "留下了遗产……\x02\x03",

            "遗嘱上写着\x01",
            "『一切都交给我孙女爱娜』\x01",
            "这样的话。\x02\x03",

            "#1656F所以，那个…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x103,
        (
            "#1646F资产家的遗产……\x02\x03",

            "啊……\x01",
            "嗯，大概能想像到。\x02\x03",

            "#1648F近亲远戚什么的\x01",
            "都蜂拥而至\x01",
            "前来分遗产了吧？\x02",
        )
    )

    Jump("loc_48E6")

    label("loc_48E6")

    CloseMessageWindow()

    ChrTalk(    #140
        0x151,
        (
            "#1654F#2P嗯……\x01",
            "我伯父虽说是个和蔼的人……\x02\x03",

            "#1656F……但他说有一直\x01",
            "照顾我到二十岁的义务……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x103,
        (
            "#1648F『所以遗产的管理\x01",
            "　都交给我吧』？\x02\x03",

            "#1648F…………太差劲了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x151,
        (
            "#1656F#2P嗯……\x02\x03",

            "#1651F因为他眼神有点可怕，\x01",
            "我就拒绝了……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #143
        0x103,
        "#1647F……啊，快躲起来！\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_44(0x39, 0xFF)
    Fade(500)
    OP_6D(97630, 250, 16560, 0)
    OP_67(0, 5860, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(140000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x11, 0x80)
    OP_44(0x11, 0xFF)
    SetChrPos(0x11, 97100, 250, 5380, 0)

    def lambda_4A9C():
        OP_8E(0xFE, 0x17B4C, 0xFA, 0x6FB8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4A9C)
    SetChrPos(0x103, 103230, 1250, 16079, 270)
    SetChrPos(0x151, 102560, 1250, 15500, 270)
    WaitChrThread(0x11, 0x1)
    SetChrFlags(0x11, 0x80)
    Sleep(500)

    ChrTalk(    #144
        0x151,
        (
            "#1656F#4P那些黑衣人\x01",
            "好像是他最近雇佣的。\x02\x03",

            "要是我没有正式继承，\x01",
            "遗嘱就会无效。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()

    def lambda_4B4A():
        OP_6D(103660, 1250, 15100, 2500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_4B4A)

    def lambda_4B62():
        OP_67(0, 4100, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_4B62)

    def lambda_4B7A():
        OP_6C(145000, 2500)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_4B7A)

    def lambda_4B8A():
        OP_6B(3000, 2500)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_4B8A)

    def lambda_4B9A():
        OP_6E(262, 2500)
        ExitThread()

    QueueWorkItem(0x151, 3, lambda_4B9A)
    Sleep(500)

    def lambda_4BAF():
        OP_8F(0xFE, 0x18FC4, 0x4E2, 0x4178, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4BAF)
    Sleep(500)

    def lambda_4BCF():
        OP_8F(0xFE, 0x19578, 0x4E2, 0x40D8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4BCF)
    WaitChrThread(0x39, 0x0)

    ChrTalk(    #145
        0x151,
        (
            "#1656F#4P……所以大概就是为这个\x01",
            "才来抓我的吧。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #146
        0x103,
        (
            "#1646F#5P从他们的战斗能力来看……\x01",
            "不是普通的小混混。\x02\x03",

            "那么危险的人，\x01",
            "大白天的就在王都晃悠……\x02\x03",

            "#1642F军队到底在干什么啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x151, 0x103, 400)
    Sleep(300)

    ChrTalk(    #147
        0x151,
        (
            "#1652F#4P我亲戚当中\x01",
            "似乎有人和军部有关系。\x02\x03",

            "#1651F……因为我们家是名门嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x103,
        (
            "#1645F#5P啊啊……开始头痛了……\x02\x03",

            "居然会为了争夺遗产\x01",
            "雇佣那种人……\x02\x03",

            "真是有钱人特有的烦恼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x151,
        (
            "#1656F#4P哎……\x02\x03",

            "#1655F对、对不起……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x103,
        (
            "#1646F#5P…………没什么。\x01",
            "你不用道歉的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x103)

    ChrTalk(    #151
        0x103,
        (
            "#1642F（事情变得麻烦了呢……）\x02\x03",

            "（说实话，要是再打的话\x01",
            "  我也没有赢的自信。）\x02\x03",

            "（要想办法不被他们发现\x01",
            "  跑到协会避难……）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_4EE0():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4EE0)
    Sleep(50)
    OP_62(0x151, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_4F0A():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_4F0A)
    Sleep(450)

    def lambda_4F1D():
        OP_8F(0xFE, 0x190A0, 0x4E2, 0x3C8C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_4F1D)

    def lambda_4F38():
        OP_6D(97630, 250, 16560, 2000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_4F38)

    def lambda_4F50():
        OP_67(0, 5860, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_4F50)

    def lambda_4F68():
        OP_6C(140000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_4F68)

    def lambda_4F78():
        OP_6B(2780, 2000)
        ExitThread()

    QueueWorkItem(0x39, 3, lambda_4F78)

    def lambda_4F88():
        OP_6E(262, 2000)
        ExitThread()

    QueueWorkItem(0x151, 3, lambda_4F88)
    Sleep(200)

    def lambda_4F9D():
        OP_8F(0xFE, 0x1933E, 0x4E2, 0x3ECF, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4F9D)
    WaitChrThread(0x39, 0x0)
    OP_44(0x103, 0x1)
    ClearChrFlags(0x12, 0x80)
    OP_44(0x12, 0xFF)
    SetChrPos(0x12, 97100, 250, 28600, 0)

    def lambda_4FDB():
        OP_8E(0xFE, 0x17B4C, 0xFA, 0x43A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4FDB)
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #152
        0x151,
        "#4P（………………………………）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x103,
        "#4P（咕噜…………）\x02",
    )

    CloseMessageWindow()

    def lambda_506B():
        OP_8E(0xFE, 0x17B4C, 0xFA, 0x2C10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_506B)
    Sleep(600)

    ChrTalk(    #154
        0x103,
        "#1645F#4P哦……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)
    Sleep(300)
    OP_20(0x3E8)

    ChrTalk(    #155
        0x12,
        (
            "#3P…………………………\x02\x03",

            "#3P这么说来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x12,
        (
            "#3P好像忘记给鸠\x01",
            "喂食了啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #157
        0x151,
        "#1653F#4P（给鸠喂食……？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x103,
        (
            "#1642F#4P（……可能是他们的密语，\x01",
            "  或者是接头暗号……）\x02\x03",

            "（…………如果是这样……）\x02\x03",

            "#1647F…………糟了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x151,
        "#1653F#4P？？\x02",
    )

    CloseMessageWindow()
    OP_59()
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    SetChrPos(0x13, 100900, 250, 40500, 180)
    SetChrPos(0x14, 97960, 250, 40900, 180)

    def lambda_521C():
        OP_8E(0xFE, 0x18A24, 0xFA, 0x8980, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_521C)
    OP_43(0x14, 0x3, 0x0, 0x2A)
    Fade(500)
    SetChrPos(0x103, 101700, 1250, 14500, 0)
    SetChrPos(0x151, 100740, 1250, 14300, 0)
    OP_6D(101400, 0, 26460, 0)
    OP_67(0, 3840, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_43(0x103, 0x3, 0x0, 0x28)
    OP_43(0x151, 0x3, 0x0, 0x29)
    WaitChrThread(0x103, 0x3)
    WaitChrThread(0x13, 0x1)

    ChrTalk(    #160
        0x13,
        (
            "#6P哎呀。\x01",
            "此路不通哦。\x02",
        )
    )

    Jump("loc_52DE")

    label("loc_52DE")

    CloseMessageWindow()

    ChrTalk(    #161
        0x14,
        "#6P净给人添麻烦。\x02",
    )

    CloseMessageWindow()

    def lambda_5302():
        OP_8F(0xFE, 0x18C18, 0xFA, 0x7738, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5302)

    ChrTalk(    #162
        0x103,
        "#1647F#5P呜…………！！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 4)
    SetChrSubChip(0x103, 0)
    OP_8C(0x103, 315, 600)
    Sleep(250)
    SetChrPos(0x12, 98100, 250, 21760, 0)

    def lambda_5377():
        OP_8E(0xFE, 0x17F34, 0xFA, 0x6824, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5377)
    WaitChrThread(0x12, 0x1)
    Sleep(300)

    ChrTalk(    #163
        0x12,
        (
            "#1P哼，\x01",
            "逃跑技术倒是值得表扬。\x02",
        )
    )

    Jump("loc_53C5")

    label("loc_53C5")

    CloseMessageWindow()

    ChrTalk(    #164
        0x12,
        "#1P……#3S抓起来！#2S\x02",
    )

    Sleep(30)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_5411():
        OP_6B(2100, 1000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_5411)
    SetChrChipByIndex(0x13, 41)
    SetChrSubChip(0x13, 0)

    def lambda_542B():
        OP_8F(0xFE, 0x18A24, 0xFA, 0x7ABC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_542B)
    SetChrChipByIndex(0x14, 41)
    SetChrSubChip(0x14, 0)

    def lambda_5450():
        OP_8F(0xFE, 0x1863C, 0xFA, 0x7ABC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5450)
    Sleep(400)
    OP_44(0x39, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    Battle(0x3AD, 0x0, 0x0, 0x0, 0xFF)
    SetMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 43)
    Return()

    # Function_39_4281 end

    def Function_40_5496(): pass

    label("Function_40_5496")


    def lambda_549C():
        OP_8E(0xFE, 0x18C18, 0x4E2, 0x4CF4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_549C)
    WaitChrThread(0x103, 0x1)
    SetChrChipByIndex(0x103, 47)
    SetChrSubChip(0x103, 2)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_54CB():
        OP_96(0xFE, 0x18C18, 0xFA, 0x66BC, 0x546, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_54CB)
    WaitChrThread(0x103, 0x1)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    ClearChrFlags(0x103, 0x4)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_5502():
        OP_8E(0xFE, 0x18C18, 0xFA, 0x78C8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5502)

    def lambda_551D():
        OP_6D(101400, 250, 29720, 1500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_551D)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0x39, 0x0)
    Return()

    # Function_40_5496 end

    def Function_41_553A(): pass

    label("Function_41_553A")

    Sleep(100)

    def lambda_5545():
        OP_8E(0xFE, 0x18984, 0x4E2, 0x4B00, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5545)
    WaitChrThread(0x151, 0x1)
    SetChrChipByIndex(0x151, 48)
    SetChrSubChip(0x151, 5)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_5574():
        OP_96(0xFE, 0x18984, 0xFA, 0x6270, 0x514, 0xA8C)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5574)
    WaitChrThread(0x151, 0x1)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    ClearChrFlags(0x151, 0x4)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)

    def lambda_55B0():
        OP_8E(0xFE, 0x18984, 0xFA, 0x74A4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_55B0)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_41_553A end

    def Function_42_55CB(): pass

    label("Function_42_55CB")

    Sleep(150)

    def lambda_55D6():
        OP_8E(0xFE, 0x17EA8, 0xFA, 0x8750, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_55D6)
    WaitChrThread(0x14, 0x1)
    OP_8C(0x14, 135, 500)
    Return()

    # Function_42_55CB end

    def Function_43_55F8(): pass

    label("Function_43_55F8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_31(0x2, 0xFC, 0x0)
    OP_31(0x50, 0xFC, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x50, 0xFE, 0x0)
    OP_1D(0x29)
    OP_6D(101400, 0, 29720, 0)
    OP_67(0, 3840, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 101400, 250, 30520, 0)
    SetChrPos(0x151, 100740, 250, 29860, 0)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrPos(0x13, 100900, 250, 35200, 180)
    SetChrPos(0x14, 97960, 250, 34640, 135)
    SetChrPos(0x12, 98100, 250, 26660, 0)
    SetChrPos(0x15, 91000, 0, 35280, 90)
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x14, 45)
    SetChrSubChip(0x14, 0)
    SetChrChipByIndex(0x13, 45)
    SetChrSubChip(0x13, 0)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x2F, 0x80)
    LoadEffect(0x1, "map\\\\mp286_00.eff")
    SoundLoad(393)
    SoundLoad(127)
    SoundLoad(132)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_5750"),
        (0, "loc_575D"),
        (SWITCH_DEFAULT, "loc_576A"),
    )


    label("loc_5750")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_576A")

    label("loc_575D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_576A")

    label("loc_576A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57B5")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "◆赢了\x01",      # 0
            "◆输了\x01",      # 1
        )
    )

    Jump("loc_57A4")

    label("loc_57A4")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)

    label("loc_57B5")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_57C6"),
        (0, "loc_57D3"),
        (SWITCH_DEFAULT, "loc_57E7"),
    )


    label("loc_57C6")

    SetChrChipByIndex(0x103, 6)
    SetChrSubChip(0x103, 3)
    Jump("loc_57E7")

    label("loc_57D3")

    SetChrChipByIndex(0x103, 4)
    SetChrSubChip(0x103, 0)
    OP_8C(0x103, 315, 0)
    Jump("loc_57E7")

    label("loc_57E7")

    FadeToBright(1000, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_5802"),
        (0, "loc_5931"),
        (SWITCH_DEFAULT, "loc_59ED"),
    )


    label("loc_5802")


    ChrTalk(    #165
        0x103,
        "#1647F呼、呼、呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x103,
        "#1645F呜…………咳咳！\x02",
    )

    OP_9E(0x103, 0xA, 0x0, 0x1F4, 0xBB8)
    CloseMessageWindow()

    ChrTalk(    #167
        0x151,
        (
            "#1652F雪拉扎德小姐！？\x02\x03",

            "不、不要紧吗……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_589D():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_589D)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x103, 4)
    SetChrSubChip(0x103, 0)
    OP_8C(0x103, 315, 0)
    Sleep(500)

    ChrTalk(    #168
        0x103,
        (
            "#1647F没、没事……\x02\x03",

            "你别管，快退下！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x12,
        "#1P哎呀哎呀，真努力啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_59ED")

    label("loc_5931")

    OP_8C(0x103, 315, 0)

    ChrTalk(    #170
        0x12,
        (
            "#1P哦，\x01",
            "还挺有一手的嘛。\x02",
        )
    )

    Jump("loc_5961")

    label("loc_5961")

    CloseMessageWindow()

    ChrTalk(    #171
        0x103,
        (
            "#1642F#1P呼，呼，呼……\x02\x03",

            "#1647F（呜…………\x01",
            "　到底还是棘手啊……）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x151,
        (
            "#1653F不、不要紧吗？\x01",
            "雪拉扎德小姐……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59ED")

    label("loc_59ED")


    ChrTalk(    #173
        0x15,
        "#1P喂，要玩到什么时候啊。\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_9F(0x15, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x15, 90800, 0, 31660, 90)

    def lambda_5A35():
        OP_8E(0xFE, 0x17C78, 0xFA, 0x7BAC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5A35)
    Sleep(400)

    def lambda_5A55():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5A55)
    Sleep(200)

    def lambda_5A68():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_5A68)
    Sleep(200)

    def lambda_5A7B():
        OP_8F(0xFE, 0x18D80, 0xFA, 0x72B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5A7B)
    Sleep(1000)

    def lambda_5A9B():
        OP_6D(99000, 0, 29760, 1000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_5A9B)

    def lambda_5AB3():
        OP_6B(2860, 1000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_5AB3)
    OP_43(0x103, 0x3, 0x0, 0x2C)
    WaitChrThread(0x15, 0x1)

    ChrTalk(    #174 op#A
        0x15,
        "#10A哎呀。\x02",
    )

    Jump("loc_5AE7")

    label("loc_5AE7")

    Sleep(50)

    def lambda_5AF2():
        OP_96(0xFE, 0x17340, 0x0, 0x7C74, 0x258, 0x1770)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5AF2)
    WaitChrThread(0x15, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    Sleep(300)
    OP_22(0xD8, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x15, 45)
    SetChrSubChip(0x15, 0)
    Sleep(250)
    OP_22(0xD8, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x12, 45)
    SetChrSubChip(0x12, 0)
    Sleep(250)

    ChrTalk(    #175
        0x15,
        "危险危险……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #176
        0x103,
        (
            "#1647F#3P呼、呼、呼……\x02\x03",

            "（可恶……\x01",
            "  怎么能输给这些人……！）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x151,
        (
            "#1652F#4P（……雪拉扎德小姐，\x01",
            "  有什么办法吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x103,
        "#1643F#3P……咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x151,
        "#1652F#4P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x103,
        (
            "#1643F#3P啊……………………\x02\x03",

            "#1642F（…………在这附近\x01",
            "  有地下水路的入口。）\x02\x03",

            "（通过那个\x01",
            "  应该能穿行到西街区。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x151,
        (
            "#1654F#4P……知道了，\x01",
            "那就走吧。\x02\x03",

            "#1656F闭上眼睛哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(250)

    def lambda_5D29():
        OP_6D(100660, 0, 30060, 1400)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_5D29)

    def lambda_5D41():
        OP_6C(135000, 1400)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_5D41)

    def lambda_5D51():
        OP_6B(3260, 1400)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_5D51)

    def lambda_5D61():
        OP_8E(0xFE, 0x18BF0, 0xFA, 0x72B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5D61)
    WaitChrThread(0x151, 0x1)

    def lambda_5D81():
        OP_8E(0xFE, 0x18740, 0xFA, 0x7760, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_5D81)
    WaitChrThread(0x151, 0x1)
    WaitChrThread(0x39, 0x0)
    Fade(250)
    SetChrChipByIndex(0x103, 4)
    SetChrSubChip(0x103, 0)
    OP_8C(0x103, 315, 0)
    OP_0D()

    ChrTalk(    #182 op#A
        0x103,
        "#1642F#3P#17A等、等一下………？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x151, 42)
    SetChrSubChip(0x151, 0)
    OP_8C(0x151, 45, 0)
    Sleep(800)

    ChrTalk(    #183
        0x151,
        "#1652F一、二…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #184
        0x15,
        (
            "喂，我说你。\x01",
            "干什么…………\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_6B(3060, 0)
    OP_0D()

    def lambda_5E86():
        OP_6D(100660, 1000, 30060, 500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_5E86)
    PlayEffect(0x1, 0x1, 0x151, -1500, 1500, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #185 op#A
        0x151,
        "#4S#10A#6P三！！#2S\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x3E8)
    SetChrSubChip(0x151, 1)
    Sleep(500)

    def lambda_5F0D():
        OP_6D(100660, 0, 30060, 1000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_5F0D)

    def lambda_5F25():
        OP_6B(3260, 1000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_5F25)
    Sleep(900)
    OP_22(0x189, 0x0, 0x64)
    Sleep(2600)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x7F, 0x0, 0x64)
    Sleep(500)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    OP_8C(0x103, 315, 400)
    Sleep(300)

    ChrTalk(    #186
        0x103,
        (
            "#1643F#3S慢、慢着！？\x01",
            "这是什么！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x12,
        "#3S发、发烟筒！？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x13, 7)
    SetChrSubChip(0x13, 0)

    def lambda_6061():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_6061)
    OP_22(0x20C, 0x0, 0x64)

    ChrTalk(    #188
        0x13,
        "咳咳……\x02",
    )

    Jump("loc_608F")

    label("loc_608F")

    CloseMessageWindow()
    SetChrChipByIndex(0x14, 7)
    SetChrSubChip(0x14, 0)

    def lambda_60A0():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_60A0)
    OP_22(0x20C, 0x0, 0x64)

    ChrTalk(    #189
        0x14,
        "眼、眼睛好痛……！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x12, 7)
    SetChrSubChip(0x12, 0)

    def lambda_60DD():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_60DD)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(500)
    SetChrChipByIndex(0x15, 7)
    SetChrSubChip(0x15, 0)

    def lambda_6101():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_6101)
    OP_22(0x20C, 0x0, 0x64)
    WaitChrThread(0x15, 0x3)
    OP_82(0x1, 0x2)
    OP_11(0xFF, 0xFF, 0x0, 0x9C40, 0x249F0, 0x0)
    StopSound(0x64, 0x249F0, 0x3E8)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    OP_8C(0x151, 315, 0)
    Sleep(500)

    def lambda_615B():
        OP_6D(101760, 250, 32900, 1000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_615B)

    def lambda_6173():
        OP_6B(3100, 1000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_6173)

    def lambda_6183():
        OP_8E(0xFE, 0x188F8, 0xFA, 0x8318, 0xAF0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_6183)
    Sleep(800)

    def lambda_61A3():
        TurnDirection(0xFE, 0x151, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_61A3)
    WaitChrThread(0x151, 0x1)
    Fade(250)
    SetChrChipByIndex(0x151, 43)
    SetChrSubChip(0x151, 0)
    Sleep(250)

    def lambda_61CA():
        OP_99(0xFE, 0x0, 0x2, 0x5DC)
        ExitThread()

    QueueWorkItem(0x151, 3, lambda_61CA)
    WaitChrThread(0x151, 0x3)
    Sleep(100)

    def lambda_61E4():
        OP_6B(3000, 500)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_61E4)
    SetChrFlags(0x151, 0x20)
    SetChrFlags(0x151, 0x1000)

    def lambda_61FE():
        OP_99(0xFE, 0x2, 0x6, 0x5DC)
        ExitThread()

    QueueWorkItem(0x151, 3, lambda_61FE)

    def lambda_620E():
        OP_96(0xFE, 0x188F8, 0xFA, 0x850C, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_620E)

    ChrTalk(    #190 op#A
        0x151,
        "#3S#5A#2P嘿！#2S\x02",
    )

    Sleep(150)

    def lambda_624D():
        OP_6B(3200, 1000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_624D)
    OP_22(0x8E, 0x0, 0x64)

    def lambda_6262():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_6262)
    SetChrFlags(0x13, 0x4)
    SetChrChipByIndex(0x13, 46)
    SetChrSubChip(0x13, 0)

    def lambda_628B():
        OP_95(0xFE, 0x0, 0xFFFFFF9C, 0x5DC, 0x2BC, 0x9C4)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_628B)

    ChrTalk(    #191 op#A
        0x13,
        "#3S#8A呜啊……！？#2S\x02",
    )

    OP_7C(0xC8, 0xC8, 0xBB8, 0x12C)
    WaitChrThread(0x13, 0x1)
    OP_22(0x20C, 0x0, 0x64)
    SetChrPos(0x13, 100550, 250, 37400, 180)
    ClearChrFlags(0x13, 0x1)
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 44)
    SetChrSubChip(0x13, 0)
    Sleep(500)

    def lambda_6314():
        OP_9E(0xFE, 0xA, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_6314)
    Sleep(1000)
    SetChrSubChip(0x151, 7)
    Sleep(100)
    Fade(250)
    SetChrChipByIndex(0x151, 65535)
    SetChrSubChip(0x151, 0)
    ClearChrFlags(0x151, 0x20)
    ClearChrFlags(0x151, 0x1000)
    OP_0D()
    Sleep(100)
    TurnDirection(0x151, 0x103, 500)
    WaitChrThread(0x39, 0x2)
    Sleep(100)

    ChrTalk(    #192
        0x151,
        "#1651F好，趁现在！\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_43(0x151, 0x3, 0x0, 0x2D)
    Sleep(500)
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #193
        0x103,
        (
            "#1643F#2P咦、\x01",
            "#3S……咦——！？#2S\x02",
        )
    )

    CloseMessageWindow()
    StopSound(0x64, 0x13880, 0x3E8)

    ChrTalk(    #194 op#A
        0x103,
        (
            "#1642F#2P（呜……这是什么，\x01",
            "  好刺激的味道……）\x02\x03",

            "（…………芥末粉？）\x02\x03",

            "#1644F#3S等、等一下啊！！#2S\x02\x03",

            "#1643F#3S#22A为什么你会有\x01",
            "这种东西啊！？#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x103, 0x3, 0x0, 0x2E)
    Sleep(1000)

    def lambda_64A6():
        OP_6D(100660, 0, 30060, 1000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_64A6)
    WaitChrThread(0x39, 0x0)

    def lambda_64C3():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_64C3)

    ChrTalk(    #195
        0x14,
        "咳……咳……\x02",
    )

    CloseMessageWindow()
    OP_99(0x15, 0x3, 0x1, 0x3E8)
    Fade(100)
    SetChrChipByIndex(0x15, 1)
    SetChrSubChip(0x15, 0)
    Sleep(100)
    OP_8C(0x15, 0, 500)
    Sleep(300)

    ChrTalk(    #196
        0x15,
        "#3S别、别跑！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    SetChrChipByIndex(0x15, 41)
    SetChrSubChip(0x15, 0)

    def lambda_6555():
        OP_8E(0xFE, 0x17480, 0x0, 0xAFA0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6555)
    Sleep(100)
    OP_99(0x12, 0x3, 0x1, 0x3E8)
    Fade(100)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    Sleep(100)
    SetChrChipByIndex(0x12, 41)
    SetChrSubChip(0x12, 0)

    def lambda_659C():
        OP_8E(0xFE, 0x184AC, 0xFA, 0x7EF4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_659C)
    WaitChrThread(0x12, 0x1)

    def lambda_65BC():
        OP_8E(0xFE, 0x184AC, 0xFA, 0xADD4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_65BC)
    Sleep(1500)
    Fade(1000)
    OP_44(0x15, 0x1)
    OP_44(0x12, 0x1)
    SetChrPos(0x15, 97400, 250, 39800, 0)
    SetChrPos(0x12, 95300, 0, 38340, 0)
    OP_44(0x103, 0x3)
    OP_44(0x151, 0x3)
    SetChrPos(0x151, 124140, -3500, 70900, 110)
    SetChrPos(0x103, 97140, 250, 39000, 0)
    OP_6D(97000, 250, 49280, 0)
    OP_67(0, 4760, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_6672():
        OP_8E(0xFE, 0x17B74, 0xFA, 0x10DD8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6672)
    StopSound(0x9C40, 0x249F0, 0x5DC)
    PlayEffect(0x1, 0x1, 0xFF, 96160, 250, 39220, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 4000)
    Sleep(1000)
    OP_11(0xA4, 0xB7, 0xFF, 0x9C40, 0x249F0, 0x0)
    Sleep(700)

    ChrTalk(    #197 op#A
        0x103,
        (
            "#1644F#40A#3S不对，\x01",
            "在这之前轻易就打飞那个壮汉，\x01",
            "你是普通人吗！？#2S\x02",
        )
    )

    Sleep(100)

    def lambda_673E():
        OP_6D(97140, 250, 54600, 2000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_673E)
    Sleep(2000)

    def lambda_675B():
        OP_8E(0xFE, 0x17C78, 0xFA, 0x110A8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_675B)

    def lambda_6776():
        OP_8E(0xFE, 0x17444, 0x0, 0x10AF4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6776)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x15, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x103, 0x1)
    OP_6D(125460, -3500, 72120, 0)
    OP_67(0, 4760, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(70000, 0)
    OP_6E(262, 0)
    OP_82(0x1, 0x0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)

    ChrTalk(    #198
        0x151,
        "#1655F#6P上锁了……\x02",
    )

    CloseMessageWindow()
    OP_44(0x103, 0xFF)
    ClearChrFlags(0x103, 0x4)
    SetChrPos(0x103, 105160, 250, 69000, 90)

    ChrTalk(    #199
        0x103,
        "#1644F#3S让开！#2S\x02",
    )

    CloseMessageWindow()
    OP_43(0x103, 0x3, 0x0, 0x2F)
    Sleep(1000)
    Sleep(500)
    TurnDirection(0x151, 0x103, 500)
    Sleep(500)

    def lambda_6899():
        OP_8F(0xFE, 0x1E26C, 0xFFFFF254, 0x11954, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_6899)
    WaitChrThread(0x151, 0x1)

    def lambda_68B9():

        label("loc_68B9")

        TurnDirection(0xFE, 0x103, 500)
        OP_48()
        Jump("loc_68B9")

    QueueWorkItem2(0x151, 3, lambda_68B9)
    WaitChrThread(0x103, 0x3)
    Sleep(100)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #200
        (
            "\x07\x05雪拉扎德拿出一根针，\x01",
            "插进锁孔。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_22(0x73, 0x0, 0x64)
    Sleep(200)
    OP_22(0x73, 0x0, 0x64)
    Sleep(350)
    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_70(0xB, 0x78)
    OP_73(0xB)

    def lambda_6943():
        OP_8F(0xFE, 0x1ECA8, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6943)
    WaitChrThread(0x103, 0x1)
    OP_44(0x151, 0x3)
    OP_8C(0x103, 290, 500)
    Sleep(100)

    ChrTalk(    #201
        0x103,
        "#1644F好了，赶快！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 110, 500)
    Sleep(100)
    OP_43(0x14, 0x3, 0x0, 0x30)

    def lambda_69A5():
        OP_8F(0xFE, 0x1FA40, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_69A5)

    def lambda_69C0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_69C0)
    Sleep(100)

    def lambda_69D7():
        OP_8E(0xFE, 0x1E424, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_69D7)
    WaitChrThread(0x151, 0x1)

    def lambda_69F7():
        OP_8E(0xFE, 0x1ECA8, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_69F7)
    WaitChrThread(0x151, 0x1)

    def lambda_6A17():
        OP_8E(0xFE, 0x1FA40, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_6A17)

    def lambda_6A32():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_6A32)
    Sleep(500)
    OP_6F(0xB, 120)
    OP_72(0x200B, 0x0)
    ExitThread()
    OP_72(0xB, 0x8)
    ExitThread()
    OP_70(0xB, 0x0)
    Sleep(100)
    OP_22(0xA8, 0x0, 0x64)
    OP_73(0xB)
    OP_43(0x12, 0x3, 0x0, 0x31)
    Sleep(800)
    OP_43(0x15, 0x3, 0x0, 0x32)
    OP_22(0x73, 0x0, 0x64)
    WaitChrThread(0x12, 0x3)
    OP_22(0x18A, 0x0, 0x64)
    Sleep(1300)
    FadeToDark(2000, 0, -1)
    OP_22(0x18A, 0x0, 0x64)
    Sleep(1300)
    OP_0D()
    NewScene("ED6_DT21/C4202   ._SN", 121, 0, 0)
    IdleLoop()
    Return()

    # Function_43_55F8 end

    def Function_44_6AB0(): pass

    label("Function_44_6AB0")


    ChrTalk(    #202 op#A
        0x103,
        "#3S#6A#1P唰……！\x02",
    )

    Sleep(200)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 5)

    def lambda_6AE2():
        OP_99(0x103, 0x0, 0x9, 0x5DC)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_6AE2)
    Sleep(100)
    OP_22(0x84, 0x0, 0x64)
    Return()

    # Function_44_6AB0 end

    def Function_45_6AF7(): pass

    label("Function_45_6AF7")


    def lambda_6AFD():
        OP_8E(0xFE, 0x1854C, 0xFA, 0x8890, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_6AFD)
    WaitChrThread(0x151, 0x1)

    def lambda_6B1D():
        OP_8E(0xFE, 0x1854C, 0xFA, 0xB388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_6B1D)
    WaitChrThread(0x151, 0x1)
    Return()

    # Function_45_6AF7 end

    def Function_46_6B38(): pass

    label("Function_46_6B38")


    def lambda_6B3E():
        OP_8E(0xFE, 0x1854C, 0xFA, 0x80C0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B3E)
    WaitChrThread(0x103, 0x1)

    def lambda_6B5E():
        OP_8E(0xFE, 0x1854C, 0xFA, 0xB388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B5E)
    WaitChrThread(0x103, 0x1)
    Return()

    # Function_46_6B38 end

    def Function_47_6B79(): pass

    label("Function_47_6B79")


    def lambda_6B7F():
        OP_8F(0xFE, 0x1D164, 0xFFFFF254, 0x10D88, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B7F)
    WaitChrThread(0x103, 0x1)

    def lambda_6B9F():
        OP_8F(0xFE, 0x1E4EC, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B9F)
    WaitChrThread(0x103, 0x1)
    OP_8C(0x103, 110, 500)
    Sleep(100)
    Return()

    # Function_47_6B79 end

    def Function_48_6BC6(): pass

    label("Function_48_6BC6")

    SetChrPos(0x14, 105760, 250, 68820, 90)

    ChrTalk(    #203 op#A
        0x14,
        "#10A#3S给我站住！！\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x3E8)
    CloseMessageWindow()
    Return()

    # Function_48_6BC6 end

    def Function_49_6C08(): pass

    label("Function_49_6C08")

    SetChrPos(0x12, 105160, 250, 69000, 90)

    def lambda_6C1F():
        OP_8E(0xFE, 0x1D164, 0xFFFFF254, 0x10D88, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6C1F)
    WaitChrThread(0x12, 0x1)

    def lambda_6C3F():
        OP_8E(0xFE, 0x1E4EC, 0xFFFFF254, 0x114F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6C3F)
    WaitChrThread(0x12, 0x1)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    OP_8C(0x12, 110, 500)
    Sleep(100)
    Return()

    # Function_49_6C08 end

    def Function_50_6C70(): pass

    label("Function_50_6C70")

    SetChrPos(0x15, 105160, 250, 69600, 90)

    def lambda_6C87():
        OP_8E(0xFE, 0x1D164, 0xFFFFF254, 0x10FE0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6C87)
    WaitChrThread(0x15, 0x1)

    def lambda_6CA7():
        OP_8E(0xFE, 0x1DF24, 0xFFFFF254, 0x11940, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6CA7)
    WaitChrThread(0x15, 0x1)
    SetChrChipByIndex(0x15, 1)
    SetChrSubChip(0x15, 0)
    OP_8C(0x15, 110, 500)
    Sleep(100)
    Return()

    # Function_50_6C70 end

    def Function_51_6CD8(): pass

    label("Function_51_6CD8")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DA8")
    Fade(1000)
    OP_6D(72000, 1250, 52940, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(55000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 71700, 1250, 52340, 180)
    SetChrPos(0x151, 70340, 1250, 52400, 180)
    OP_0D()
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(150)
    OP_62(0x151, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    def lambda_6D85():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6D85)
    Sleep(150)

    def lambda_6D98():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_6D98)
    Sleep(300)
    Jump("loc_6DC4")

    label("loc_6DA8")


    def lambda_6DAE():
        TurnDirection(0xFE, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6DAE)

    def lambda_6DBC():
        TurnDirection(0xFE, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_6DBC)

    label("loc_6DC4")

    Call(0, 53)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E2D")

    def lambda_6DD6():
        OP_6D(72000, 1250, 52940, 1500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_6DD6)
    WaitChrThread(0x39, 0x0)
    Sleep(300)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x151, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_A2(0x2F53)
    EventEnd(0x0)
    Jump("loc_6E94")

    label("loc_6E2D")

    Fade(1000)
    SetChrPos(0x103, 70000, 1250, 51780, 180)
    SetChrPos(0x151, 70000, 1250, 51780, 180)
    OP_6D(70000, 1250, 51780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    EventEnd(0x0)

    label("loc_6E94")

    Return()

    # Function_51_6CD8 end

    def Function_52_6E95(): pass

    label("Function_52_6E95")

    EventBegin(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F65")
    Fade(1000)
    OP_6D(71440, 1250, 39340, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(55000, 0)
    OP_6E(262, 0)
    SetChrPos(0x103, 70700, 1250, 38560, 315)
    SetChrPos(0x151, 69340, 1250, 38040, 315)
    OP_0D()
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(150)
    OP_62(0x151, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(300)

    def lambda_6F42():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6F42)
    Sleep(150)

    def lambda_6F55():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_6F55)
    Sleep(300)
    Jump("loc_6F81")

    label("loc_6F65")


    def lambda_6F6B():
        TurnDirection(0xFE, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6F6B)

    def lambda_6F79():
        TurnDirection(0xFE, 0x18, 400)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_6F79)

    label("loc_6F81")

    Call(0, 53)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FEA")

    def lambda_6F93():
        OP_6D(71440, 1250, 39340, 1500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_6F93)
    WaitChrThread(0x39, 0x0)
    Sleep(300)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x151, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)
    OP_A2(0x2F53)
    EventEnd(0x0)
    Jump("loc_7051")

    label("loc_6FEA")

    Fade(1000)
    SetChrPos(0x103, 70000, 1250, 38200, 0)
    SetChrPos(0x151, 70000, 1250, 38200, 0)
    OP_6D(70000, 1250, 38200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    EventEnd(0x0)

    label("loc_7051")

    Return()

    # Function_52_6E95 end

    def Function_53_7052(): pass

    label("Function_53_7052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 3)), scpexpr(EXPR_END)), "loc_7273")

    def lambda_705F():
        OP_6D(74200, 500, 45620, 2000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_705F)

    def lambda_7077():
        OP_67(0, 7500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_7077)

    def lambda_708F():
        OP_6C(55000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_708F)
    WaitChrThread(0x39, 0x0)
    Sleep(500)

    NpcTalk(    #204
        0x17,
        "眼神凶恶的男子",
        (
            "#143F还、还给我！！\x02\x03",

            "要是弄坏了，\x01",
            "我的工资可赔不起啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrChipByIndex(0x18, 37)
    SetChrSubChip(0x18, 0)
    Sleep(250)

    NpcTalk(    #205
        0x18,
        "长雀斑的少女",
        (
            "#1661F不会弄坏的啦～。\x02\x03",

            "#1662F哦哦，\x01",
            "远处的东西也看得很清楚～⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x17, 3)
    LoadEffect(0x3, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x18, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x18, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    NpcTalk(    #206
        0x17,
        "眼神凶恶的男子",
        "#144F#3S住、住手～～～！！！\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x3E8)
    CloseMessageWindow()
    Sleep(1000)
    OP_59()
    Fade(250)
    SetChrChipByIndex(0x18, 36)
    SetChrSubChip(0x18, 0)
    Sleep(250)
    OP_4B(0x17, 3)
    Jump("loc_7AFD")

    label("loc_7273")


    def lambda_7279():
        OP_6D(74200, 500, 45620, 2000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_7279)

    def lambda_7291():
        OP_67(0, 7500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_7291)

    def lambda_72A9():
        OP_6C(55000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 2, lambda_72A9)
    WaitChrThread(0x39, 0x0)
    Sleep(500)

    NpcTalk(    #207
        0x17,
        "眼神凶恶的男子",
        (
            "#142F#2P啧……这种时候\x01",
            "感光结晶回路偏偏用完了……\x02\x03",

            "……先把这些显像出来吧。\x02\x03",

            "#145F要是在两点之前写不完，\x01",
            "就赶不上截稿时间了……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x40)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_7381"),
        (0, "loc_73B0"),
        (SWITCH_DEFAULT, "loc_73DF"),
    )


    label("loc_7381")

    SetChrPos(0x18, 70400, 1250, 51500, 180)

    def lambda_7398():
        OP_8E(0xFE, 0x1142C, 0xFA, 0xB054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7398)
    Jump("loc_73DF")

    label("loc_73B0")

    SetChrPos(0x18, 70400, 1250, 37500, 0)

    def lambda_73C7():
        OP_8E(0xFE, 0x1142C, 0xFA, 0xB054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_73C7)
    Jump("loc_73DF")

    label("loc_73DF")

    WaitChrThread(0x18, 0x1)
    TurnDirection(0x18, 0x17, 500)
    Sleep(300)
    OP_62(0x18, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #208
        0x18,
        "长雀斑的少女",
        "#1662F咦～，那个人……\x02",
    )

    CloseMessageWindow()

    def lambda_7442():
        OP_8E(0xFE, 0x11D14, 0xFA, 0xB054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7442)
    WaitChrThread(0x18, 0x1)

    def lambda_7462():
        OP_9E(0xFE, 0x14, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_7462)

    NpcTalk(    #209
        0x17,
        "眼神凶恶的男子",
        (
            "#143F#2P#3S哇，笨蛋！？#2S\x02\x03",

            "……干什么呢！！\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_22(0x124, 0x0, 0x64)
    Fade(250)
    SetChrChipByIndex(0x18, 36)
    SetChrSubChip(0x18, 0)
    SetChrChipByIndex(0x17, 22)
    SetChrSubChip(0x17, 0)
    SetChrPos(0x17, 73960, 500, 45140, 270)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #210
        (
            "\x07\x05少女强行把相机夺走，\x01",
            "感光结晶回路都露出来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_7565():
        OP_8F(0xFE, 0x119CC, 0xFA, 0xB054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7565)
    WaitChrThread(0x18, 0x1)

    def lambda_7585():
        OP_96(0xFE, 0x11E7C, 0xFA, 0xB054, 0x12C, 0x1770)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7585)
    WaitChrThread(0x17, 0x1)
    SetChrChipByIndex(0x17, 2)
    SetChrSubChip(0x17, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_8C(0x17, 270, 0)
    ClearChrFlags(0x17, 0x4)
    OP_62(0x17, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(    #211
        0x17,
        "眼神凶恶的男子",
        (
            "#143F#3S#2P啊啊～！！#2S\x02\x03",

            "#144F笨、笨蛋……！\x01",
            "你都做了什么啊！！\x02\x03",

            "这东西见到光\x01",
            "就不能用了啊！？\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x1F4)
    CloseMessageWindow()
    CloseMessageWindow()

    NpcTalk(    #212
        0x18,
        "长雀斑的少女",
        "#1662F哦～，是这样吗～？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #213
        0x17,
        "眼神凶恶的男子",
        (
            "#144F#2P『是这样吗～？』个头啊！\x01",
            "快、快点盖上盖子！\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x82, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #214
        0x17,
        "眼神凶恶的男子",
        (
            "#145F#2P真、真是的…………\x02\x03",

            "一套感光结晶回路，\x01",
            "你以为要多少钱啊！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #215
        0x18,
        "长雀斑的少女",
        "#1660F这孩子不就是……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x18, 270, 500)
    Sleep(300)

    NpcTalk(    #216
        0x18,
        "长雀斑的少女",
        (
            "#1661F……小不点！？\x01",
            "很像附近的小不点！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #217
        0x17,
        "眼神凶恶的男子",
        "#143F#2P什么！？　你白痴啊！\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_7825():

        label("loc_7825")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_7825")

    QueueWorkItem2(0x17, 2, lambda_7825)

    def lambda_7836():
        OP_8F(0xFE, 0x11A58, 0xFA, 0xAD5C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7836)
    WaitChrThread(0x17, 0x1)

    def lambda_7856():
        OP_8F(0xFE, 0x115E4, 0xFA, 0xB054, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7856)
    WaitChrThread(0x17, 0x1)
    OP_8C(0x18, 90, 500)
    Sleep(300)

    NpcTalk(    #218
        0x17,
        "眼神凶恶的男子",
        "#144F#3P这是借来的！\x02",
    )

    CloseMessageWindow()

    def lambda_78B2():
        OP_8F(0xFE, 0x11AD0, 0xFA, 0xB48C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_78B2)
    WaitChrThread(0x17, 0x1)

    def lambda_78D2():
        OP_8F(0xFE, 0x11E7C, 0xFA, 0xB054, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_78D2)
    WaitChrThread(0x17, 0x1)

    def lambda_78F2():
        OP_8E(0xFE, 0x119CC, 0xFA, 0xAB2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_78F2)
    WaitChrThread(0x18, 0x1)

    def lambda_7912():
        OP_8F(0xFE, 0x11E18, 0xFA, 0xAB2C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7912)
    WaitChrThread(0x17, 0x1)
    OP_8C(0x18, 270, 500)
    Sleep(300)

    NpcTalk(    #219
        0x17,
        "眼神凶恶的男子",
        (
            "#144F#2P…………是主编最喜欢的\x01",
            "高级导力照相机啊！！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #220
        0x18,
        "长雀斑的少女",
        (
            "#1661F要怎样用呢～？\x02\x03",

            "#1662F喀嚓喀嚓……\x01",
            "哦哦！？　动起来了！！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrChipByIndex(0x18, 37)
    SetChrSubChip(0x18, 0)
    Sleep(250)
    LoadEffect(0x3, "map\\\\mp032_00.eff")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x18, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x3, 0xFF, 0x18, 0, 1500, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    NpcTalk(    #221
        0x17,
        "眼神凶恶的男子",
        "#144F#2P#3S哇啊啊，快住手～！！！\x02",
    )

    OP_7C(0x0, 0x96, 0xBB8, 0x3E8)
    CloseMessageWindow()
    OP_59()
    Fade(250)
    SetChrChipByIndex(0x18, 36)
    SetChrSubChip(0x18, 0)
    Sleep(250)
    OP_43(0x17, 0x3, 0x0, 0x36)
    Sleep(2000)

    label("loc_7AFD")

    Return()

    # Function_53_7052 end

    def Function_54_7AFE(): pass

    label("Function_54_7AFE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C2E")

    def lambda_7B0D():
        OP_8E(0xFE, 0x119CC, 0xFA, 0xB054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7B0D)
    WaitChrThread(0x18, 0x1)

    def lambda_7B2D():
        OP_8F(0xFE, 0x11E7C, 0xFA, 0xB054, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7B2D)
    WaitChrThread(0x17, 0x1)
    OP_8C(0x18, 270, 500)
    Sleep(1000)

    def lambda_7B59():
        OP_8F(0xFE, 0x11AD0, 0xFA, 0xB48C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7B59)
    WaitChrThread(0x17, 0x1)

    def lambda_7B79():
        OP_8F(0xFE, 0x115E4, 0xFA, 0xB054, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7B79)
    WaitChrThread(0x17, 0x1)
    OP_8C(0x18, 90, 500)
    Sleep(1000)

    def lambda_7BA5():
        OP_8F(0xFE, 0x11A58, 0xFA, 0xAD5C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7BA5)
    WaitChrThread(0x17, 0x1)

    def lambda_7BC5():
        OP_8F(0xFE, 0x11E7C, 0xFA, 0xB054, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7BC5)
    WaitChrThread(0x17, 0x1)

    def lambda_7BE5():
        OP_8E(0xFE, 0x119CC, 0xFA, 0xAB2C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7BE5)
    WaitChrThread(0x18, 0x1)

    def lambda_7C05():
        OP_8F(0xFE, 0x11E18, 0xFA, 0xAB2C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_7C05)
    WaitChrThread(0x17, 0x1)
    OP_8C(0x18, 270, 500)
    Sleep(1000)
    Jump("Function_54_7AFE")

    label("loc_7C2E")

    Return()

    # Function_54_7AFE end

    def Function_55_7C2F(): pass

    label("Function_55_7C2F")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_7C3B")
    Jump("loc_7E75")

    label("loc_7C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_7D67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7CCE")
    TurnDirection(0x151, 0x103, 400)
    Sleep(200)

    ChrTalk(    #222
        0x151,
        (
            "#1653F雪拉扎德小姐……\x02\x03",

            "你没坐过飞艇吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 400)
    Sleep(200)

    ChrTalk(    #223
        0x103,
        (
            "#1644F当、当然坐过了。\x01",
            "那还用说！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D64")

    label("loc_7CCE")

    TurnDirection(0x151, 0x103, 400)
    Sleep(200)

    ChrTalk(    #224
        0x151,
        (
            "#1653F哎呀，这边是……\x02\x03",

            "雪拉扎德小姐，\x01",
            "这前面是飞艇坪哦？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 400)
    Sleep(200)

    ChrTalk(    #225
        0x103,
        (
            "#1647F知、知道啦。\x01",
            "别把我当傻瓜。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7D64")

    Jump("loc_7E75")

    label("loc_7D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_7E75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7DDF")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #226
        0x151,
        (
            "#1653F雪拉扎德小姐……\x02\x03",

            "你想坐飞艇吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x103,
        "#1648F……怎么可能。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7E75")

    label("loc_7DDF")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #228
        0x151,
        (
            "#1653F哎呀，这边是……\x02\x03",

            "雪拉扎德小姐，\x01",
            "这前面是飞艇坪哦？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #229
        0x103,
        (
            "#1642F知、知道啦。\x01",
            "别把我当傻瓜。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7E75")

    OP_90(0xEE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_55_7C2F end

    def Function_56_7E91(): pass

    label("Function_56_7E91")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_7E9D")
    Jump("loc_81C7")

    label("loc_7E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_7FA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7EDF")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #230
        0x151,
        "#1650F……走南边的路吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FA0")

    label("loc_7EDF")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #231
        0x151,
        (
            "#1650F……暂时先回去\x01",
            "走南边的路吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #232
        0x103,
        (
            "#1642F从协会的拐角\x01",
            "就能走上大道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x151,
        "#1651F嗯嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x103,
        "#1646F…………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_7FA0")

    Jump("loc_81C7")

    label("loc_7FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_80AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8028")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #235
        0x151,
        (
            "#1653F冰淇淋店\x01",
            "不在这边哦。\x02\x03",

            "回去吧。\x02",
        )
    )

    Jump("loc_8001")

    label("loc_8001")

    CloseMessageWindow()

    ChrTalk(    #236
        0x103,
        "#1642F（我知道啦……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_80AB")

    label("loc_8028")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #237
        0x151,
        (
            "#1653F雪拉扎德小姐，\x01",
            "不是这边哦。\x02\x03",

            "回去吧。\x02",
        )
    )

    Jump("loc_807E")

    label("loc_807E")

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #238
        0x103,
        "#1646F……是是。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_80AB")

    Jump("loc_81C7")

    label("loc_80AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_81C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_8122")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #239
        0x151,
        (
            "#1653F雪拉扎德小姐，\x01",
            "我们好像走回头路了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x103,
        "#1642F知、知道啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_81C7")

    label("loc_8122")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #241
        0x151,
        (
            "#1653F……雪拉扎德小姐，\x01",
            "你要去哪里？\x02\x03",

            "感觉好像\x01",
            "走回头路了……\x02",
        )
    )

    Jump("loc_818B")

    label("loc_818B")

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #242
        0x103,
        (
            "#1646F……只、只是\x01",
            "偶尔弄错啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_81C7")

    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_56_7E91 end

    def Function_57_81E3(): pass

    label("Function_57_81E3")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_81EF")
    Jump("loc_832C")

    label("loc_81EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_81F9")
    Jump("loc_832C")

    label("loc_81F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_8325")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_828A")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #243
        0x151,
        (
            "#1653F冰淇淋店\x01",
            "不是这边哦。\x02\x03",

            "回去吧。\x02",
        )
    )

    Jump("loc_8257")

    label("loc_8257")

    CloseMessageWindow()

    ChrTalk(    #244
        0x103,
        "#1647F（从刚才就一直这么神气……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8322")

    label("loc_828A")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #245
        0x151,
        (
            "#1653F雪拉扎德小姐，\x01",
            "冰淇淋店\x01",
            "不是这边哦。\x02\x03",

            "回去吧。\x02",
        )
    )

    Jump("loc_82F5")

    label("loc_82F5")

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #246
        0x103,
        "#1646F……是是。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_8322")

    Jump("loc_832C")

    label("loc_8325")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_832C")

    label("loc_832C")

    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_57_81E3 end

    def Function_58_8348(): pass

    label("Function_58_8348")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_8354")
    Jump("loc_8394")

    label("loc_8354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_836B")
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 62)
    Jump("loc_8394")

    label("loc_836B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_838D")
    Call(0, 62)
    OP_90(0xEE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    Jump("loc_8394")

    label("loc_838D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_8394")

    label("loc_8394")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_58_8348 end

    def Function_59_839C(): pass

    label("Function_59_839C")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_83A8")
    Jump("loc_83E8")

    label("loc_83A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_83BF")
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 62)
    Jump("loc_83E8")

    label("loc_83BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_83E1")
    Call(0, 62)
    OP_90(0xEE, 0x5DC, 0x0, 0x0, 0x7D0, 0x0)
    Jump("loc_83E8")

    label("loc_83E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_83E8")

    label("loc_83E8")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_59_839C end

    def Function_60_83F0(): pass

    label("Function_60_83F0")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_83FC")
    Jump("loc_843C")

    label("loc_83FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_8413")
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 62)
    Jump("loc_843C")

    label("loc_8413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_8435")
    Call(0, 62)
    OP_90(0xEE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    Jump("loc_843C")

    label("loc_8435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_843C")

    label("loc_843C")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_60_83F0 end

    def Function_61_8444(): pass

    label("Function_61_8444")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_8450")
    Jump("loc_8490")

    label("loc_8450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_8467")
    OP_CE(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 62)
    Jump("loc_8490")

    label("loc_8467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_8489")
    Call(0, 62)
    OP_90(0xEE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
    Jump("loc_8490")

    label("loc_8489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_8490")

    label("loc_8490")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_61_8444 end

    def Function_62_8498(): pass

    label("Function_62_8498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EA, 0)), scpexpr(EXPR_END)), "loc_84A2")
    Jump("loc_85C1")

    label("loc_84A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 4)), scpexpr(EXPR_END)), "loc_84C3")
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4122   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_85C1")

    label("loc_84C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 3)), scpexpr(EXPR_END)), "loc_85BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_8545")
    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #247
        0x151,
        (
            "#1653F雪拉扎德小姐，\x01",
            "你有什么要买的东西吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x151, 500)
    Sleep(200)

    ChrTalk(    #248
        0x103,
        "#1646F……没什么啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_85B7")

    label("loc_8545")

    TurnDirection(0x151, 0x103, 500)
    Sleep(200)

    ChrTalk(    #249
        0x151,
        (
            "#1650F我已经买好东西了。\x02\x03",

            "赶快去\x01",
            "冰淇淋店吧。\x02",
        )
    )

    Jump("loc_859A")

    label("loc_859A")

    CloseMessageWindow()

    ChrTalk(    #250
        0x103,
        "#1645F呃……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_85B7")

    Jump("loc_85C1")

    label("loc_85BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E9, 2)), scpexpr(EXPR_END)), "loc_85C1")

    label("loc_85C1")

    Return()

    # Function_62_8498 end

    def Function_63_85C2(): pass

    label("Function_63_85C2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(70000, 250, 45560, 0)
    OP_67(0, 7420, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x10E, 30)
    SetChrSubChip(0x10E, 0)
    SetChrPos(0x10E, 70000, 750, 49840, 180)
    ClearChrFlags(0x37, 0x80)
    SetChrPos(0x37, 70000, 250, 48340, 180)
    OP_43(0x37, 0x3, 0x0, 0x41)
    Sleep(100)
    OP_43(0x10E, 0x3, 0x0, 0x42)
    FadeToBright(2000, 0)
    OP_6B(2960, 2000)
    OP_0D()
    WaitChrThread(0x37, 0x3)
    Sleep(500)

    ChrTalk(    #251
        0x37,
        (
            "#276F附近好像没什么人。\x02\x03",

            "#277F……就在这里吧。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10E, 0x3)

    NpcTalk(    #252
        0x10E,
        "修女尤莉亚",
        "嗯、嗯嗯…………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10E, 270, 400)
    Sleep(300)
    OP_20(0xBB8)

    def lambda_86F2():
        OP_6D(68460, 250, 46040, 3000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_86F2)

    def lambda_870A():
        OP_6C(315000, 3000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_870A)

    def lambda_871A():

        label("loc_871A")

        TurnDirection(0xFE, 0x10E, 500)
        OP_48()
        Jump("loc_871A")

    QueueWorkItem2(0x37, 2, lambda_871A)

    def lambda_872B():
        OP_8E(0xFE, 0x104BE, 0xFA, 0xB1BC, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_872B)
    WaitChrThread(0x10E, 0x1)
    Sleep(500)
    Fade(500)
    OP_22(0xCB, 0x0, 0x50)
    SetChrChipByIndex(0x10E, 31)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(1000)

    NpcTalk(    #253
        0x10E,
        "尤莉亚上尉",
        "#465F#5P呼………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10E, 90, 500)
    Sleep(200)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10E, 32)
    SetChrSubChip(0x10E, 0)
    SetChrPos(0x10E, 66200, 250, 45500, 90)
    SetChrFlags(0x10E, 0x4)
    OP_0D()
    Sleep(300)
    OP_44(0x37, 0x2)
    Sleep(300)

    NpcTalk(    #254
        0x10E,
        "尤莉亚上尉",
        (
            "#464F#5P……让你看到\x01",
            "我丢脸的样子了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x37,
        "#270F#12P哪里……\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_1D(0x1)

    def lambda_883B():
        OP_6D(65620, 500, 46040, 2000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_883B)

    def lambda_8853():
        OP_67(0, 6460, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_8853)

    def lambda_886B():
        OP_8E(0xFE, 0x104BE, 0xFA, 0xAD70, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_886B)
    WaitChrThread(0x37, 0x1)
    Sleep(300)
    OP_8C(0x37, 90, 500)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x37, 34)
    SetChrSubChip(0x37, 0)
    SetChrPos(0x37, 66200, 500, 44400, 90)
    SetChrFlags(0x37, 0x4)
    OP_0D()
    Sleep(500)

    ChrTalk(    #256
        0x37,
        (
            "#277F#6P我也习惯\x01",
            "到处东躲西藏了。\x02\x03",

            "#272F基本上都是因为\x01",
            "奥利维尔那家伙惹的祸。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #257
        0x10E,
        "尤莉亚上尉",
        (
            "#460F#5P哈哈，是这样吗。\x02\x03",

            "#465F………………不过，\x01",
            "这次真是很难堪。\x02\x03",

            "#464F这点程度的骚动\x01",
            "就把休息日搞得一团乱。\x02\x03",

            "对她们的行为束手无策，\x01",
            "只能打扮成这样跑出来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x37,
        (
            "#270F#6P………………………………\x02\x03",

            "#272F……我觉得\x01",
            "这不是上尉的错…………\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #259
        0x10E,
        "尤莉亚上尉",
        (
            "#464F#5P不，并不是这样……\x02\x03",

            "即使身为亲卫队队员，\x01",
            "我也是一无是处。\x02\x03",

            "#465F……发生政变事件的时候\x01",
            "也是这样。\x02\x03",

            "都是因为我的无能，\x01",
            "才让殿下被敌方抓走。\x02\x03",

            "……王都被『结社』\x01",
            "袭击的时候也是。\x02\x03",

            "殿下身陷险境，\x01",
            "我却不能陪在她身边。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #260
        0x10E,
        "尤莉亚上尉",
        (
            "#464F#5P比谁都更应该在她身边的我，\x01",
            "却在事后的联络中才得知经过……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8BDF():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x10E, 0, lambda_8BDF)
    Sleep(1000)

    NpcTalk(    #261
        0x10E,
        "尤莉亚上尉",
        (
            "#464F#5P我…………\x01",
            "我这个人真是……！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x37, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x37)
    Sleep(500)
    SetChrSubChip(0x37, 1)
    Sleep(500)

    ChrTalk(    #262
        0x37,
        (
            "#277F#6P……唉，不必在意。\x02\x03",

            "科洛蒂娅殿下\x01",
            "不是平安无事吗。\x02\x03",

            "#278F任何人都不是万能的……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #263
        0x10E,
        "尤莉亚上尉",
        (
            "#465F#5P………………这个，\x01",
            "我也知道。\x02\x03",

            "#464F但是，\x01",
            "这样的我却被登在杂志封面上，\x01",
            "在世间引起了轰动。\x02\x03",

            "被捧为阻止了『异变』的功臣，\x01",
            "甚至还得到了晋升。\x02\x03",

            "这么没用的我却…………\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x10E, 66200, 250, 45600, 90)
    SetChrPos(0x37, 66200, 500, 44500, 90)
    OP_6D(64819, 250, 45310, 0)
    OP_67(0, 6430, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(269000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #264
        0x10E,
        "尤莉亚上尉",
        (
            "#465F#12P………这样也好。\x02\x03",

            "被人们吹捧\x01",
            "并没有什么关系。\x02\x03",

            "晋升也本是值得高兴的事。\x02\x03",

            "#464F但是这样一来，\x01",
            "交给我的任务更加繁重了。\x02\x03",

            "……而我却离\x01",
            "殿下越来越远…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x37,
        "#272F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #266
        0x10E,
        "尤莉亚上尉",
        (
            "#464F#12P…………真羡慕少校您……\x02\x03",

            "#465F您理所当然地\x01",
            "担当奥利维特皇子的护卫。\x02\x03",

            "虽然平时不现身，\x01",
            "但在重要的局面必定陪伴身侧。\x02\x03",

            "而且不仅仅是表面的护卫，\x01",
            "还以各种形式对他进行辅助。\x02\x03",

            "#464F……相比之下，\x01",
            "我甚至在殿下烦恼的时候\x01",
            "都没办法陪她说说话。\x02\x03",

            "殿下身负\x01",
            "继承王位的重责，\x01",
            "在那么烦恼的时候……\x02",
        )
    )

    Jump("loc_909B")

    label("loc_909B")

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    SetChrPos(0x10E, 66200, 250, 45500, 90)
    SetChrPos(0x37, 66200, 500, 44400, 90)
    OP_6D(65620, 500, 46040, 0)
    OP_67(0, 6460, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x37, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x37)
    Sleep(500)

    ChrTalk(    #267
        0x37,
        (
            "#272F#6P……上尉，\x01",
            "这种话由我来说\x01",
            "可能不大合适……\x02\x03",

            "#270F…………可是，\x01",
            "那不是很幸福的事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    SetChrSubChip(0x10E, 2)

    NpcTalk(    #268
        0x10E,
        "尤莉亚上尉",
        (
            "#463F#11P咦…………！？\x02\x03",

            "……少校，\x01",
            "这是什么意思…………？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x37,
        (
            "#272F#6P…………不，\x01",
            "要是得罪的话，还请原谅……\x02\x03",

            "#277F不过，\x01",
            "我是从一出生开始就已经被赋予了\x01",
            "保护那个赖皮蛋的义务。\x02\x03",

            "所以，反倒有点羡慕\x01",
            "上尉的忠诚呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #270
        0x10E,
        "尤莉亚上尉",
        (
            "#462F#11P奥利维特皇子的……\x02\x03",

            "啊啊，\x01",
            "记得穆拉少校出身的范德尔家……\x02",
        )
    )

    Jump("loc_9324")

    label("loc_9324")

    CloseMessageWindow()

    ChrTalk(    #271
        0x37,
        (
            "#277F#6P……是守护皇族的武将家族。\x02\x03",

            "#278F真是的，\x01",
            "出生在这种家庭\x01",
            "真是倒霉啊。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #272
        0x10E,
        "尤莉亚上尉",
        (
            "#461F#11P哈哈…………\x01",
            "这的确是重任啊。\x02\x03",

            "#460F再加上，\x01",
            "面对的又是那位奥利维特皇子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x37,
        (
            "#274F#6P是啊，您想像得一点不错。\x02",

            "x03#272F#6P……………………………………\x02",

            "\",
        )
    )

    CloseMessageWindow()
    OP_62(0x37, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x37)
    Sleep(500)
    SetChrSubChip(0x37, 0)
    Sleep(500)

    ChrTalk(    #274
        0x37,
        (
            "#277F#6P……上尉，\x01",
            "能为自己所珍视的人效劳，\x01",
            "难道不是幸福的事情吗？\x02\x03",

            "虽然这只是\x01",
            "深为主子所苦的\x01",
            "我个人的意见。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x10E, 0)
    Sleep(800)

    NpcTalk(    #275
        0x10E,
        "尤莉亚上尉",
        (
            "#465F#5P……不，确实………………\x02\x03",

            "或许这样的烦恼\x01",
            "也可以称得上是奢侈。\x02\x03",

            "#464F虽然不知道无法守护\x01",
            "在殿下身边的我能不能被称为是\x01",
            "亲卫队的队士……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)

    ChrTalk(    #276
        0x37,
        (
            "#278F#6P…………上尉。\x02\x03",

            "我告诉你一个\x01",
            "转换心情的好办法吧。\x02",
        )
    )

    OP_63(0x10E)
    Sleep(500)
    CloseMessageWindow()
    OP_59()
    SetChrPos(0x10E, 66200, 250, 45500, 68)

    def lambda_960F():
        OP_6D(65730, 250, 45870, 1200)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_960F)

    def lambda_9627():
        OP_6C(293000, 1200)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_9627)
    Fade(500)
    SetChrChipByIndex(0x37, 33)
    SetChrSubChip(0x37, 0)
    SetChrPos(0x37, 66750, 250, 44400, 80)
    ClearChrFlags(0x37, 0x4)
    OP_0D()

    def lambda_965D():
        OP_8F(0xFE, 0x10B94, 0xFA, 0xB02C, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_965D)
    Sleep(800)
    OP_62(0x10E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    WaitChrThread(0x37, 0x1)
    Fade(500)
    SetChrChipByIndex(0x10E, 31)
    SetChrSubChip(0x10E, 0)
    SetChrPos(0x10E, 66750, 250, 45500, 80)
    ClearChrFlags(0x10E, 0x4)
    OP_0D()
    TurnDirection(0x10E, 0x37, 400)
    Sleep(500)

    NpcTalk(    #277
        0x10E,
        "尤莉亚上尉",
        "#463F#5P转换心情……是吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x37, 0x10E, 400)
    Sleep(500)

    ChrTalk(    #278
        0x37,
        (
            "#278F#6P啊啊，不过……\x02\x03",

            "#277F希望这只是非官方的行为。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9752():
        OP_6B(3160, 3000)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_9752)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_63_85C2 end

    def Function_64_977F(): pass

    label("Function_64_977F")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #279
        (
            "\x07\x05『导力式时钟第２号机』\x01",
            "　七耀历１１６３年·蔡斯技术工房制造\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_64_977F end

    def Function_65_97E7(): pass

    label("Function_65_97E7")


    def lambda_97ED():
        OP_8E(0xFE, 0x11170, 0xFA, 0xAD34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x37, 1, lambda_97ED)
    WaitChrThread(0x37, 0x1)
    Sleep(300)
    OP_8C(0x37, 225, 500)
    Sleep(700)
    OP_8C(0x37, 135, 500)
    Sleep(700)
    OP_8C(0x37, 180, 500)
    Sleep(300)
    Return()

    # Function_65_97E7 end

    def Function_66_9831(): pass

    label("Function_66_9831")


    def lambda_9837():
        OP_8E(0xFE, 0x11170, 0xFA, 0xB310, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_9837)
    WaitChrThread(0x10E, 0x1)
    Sleep(300)
    OP_8C(0x10E, 0, 600)
    Sleep(700)
    OP_8C(0x10E, 315, 500)
    Sleep(700)
    OP_8C(0x10E, 45, 500)
    Sleep(700)
    OP_8C(0x10E, 0, 500)
    Sleep(300)
    Return()

    # Function_66_9831 end

    def Function_67_9887(): pass

    label("Function_67_9887")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #280
        "\x07\x05门上了锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_67_9887 end

    def Function_68_98D8(): pass

    label("Function_68_98D8")

    SetPlaceName(0xBA)
    Return()

    # Function_68_98D8 end

    def Function_69_98DC(): pass

    label("Function_69_98DC")

    SetPlaceName(0xB1)
    Return()

    # Function_69_98DC end

    def Function_70_98E0(): pass

    label("Function_70_98E0")

    SetPlaceName(0xBB)
    Return()

    # Function_70_98E0 end

    def Function_71_98E4(): pass

    label("Function_71_98E4")

    SetPlaceName(0xBC)
    Return()

    # Function_71_98E4 end

    def Function_72_98E8(): pass

    label("Function_72_98E8")

    SetPlaceName(0xBD)
    Return()

    # Function_72_98E8 end

    def Function_73_98EC(): pass

    label("Function_73_98EC")

    TalkBegin(0xFF)
    Sleep(500)
    TalkEnd(0xFF)
    Return()

    # Function_73_98EC end

    SaveToFile()

Try(main)
