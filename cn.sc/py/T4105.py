from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4105   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4105.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '菲丝',                                 # 9
        '卡鲁尼洛',                             # 10
        '蒂法露',                               # 11
        '修理员佩顿',                           # 12
        '鲁特尔',                               # 13
        '安敦',                                 # 14
        '利库斯',                               # 15
        '基蒂',                                 # 16
        '尼莫',                                 # 17
        '卡拉莉丝',                             # 18
        '村中的老年男性',                       # 19
        '村中的老年女性',                       # 20
        '村中的中年男性',                       # 21
        '村中的中年女性',                       # 22
        '村中的青年男性',                       # 23
        '村中的青年女性',                       # 24
        '飞船乘客',                             # 25
        '飞船乘客',                             # 26
        '飞船乘客',                             # 27
        '飞船乘客',                             # 28
        '飞船乘客',                             # 29
        '飞船乘客',                             # 30
        '飞船乘客',                             # 31
        '飞船乘客',                             # 32
        '奥利维尔',                             # 33
        '科洛丝',                               # 34
        '提妲',                                 # 35
        '金',                                   # 36
        '穆拉',                                 # 37
        '玲',                                   # 38
        '奈尔',                                 # 39
        '朵洛希',                               # 40
        '格雷特纳号的影子',                     # 41
        '格雷特纳号',                           # 42
        '雪拉扎德',                             # 43
        '阿加特',                               # 44
        '凯文神父',                             # 45
        '地名用假人',                           # 46
        '王都格兰赛尔·东街区',                 # 47
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
        'ED6_DT07/CH01540 ._CH',             # 00
        'ED6_DT07/CH01000 ._CH',             # 01
        'ED6_DT07/CH01010 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01050 ._CH',             # 06
        'ED6_DT07/CH00030 ._CH',             # 07
        'ED6_DT07/CH00040 ._CH',             # 08
        'ED6_DT07/CH00060 ._CH',             # 09
        'ED6_DT07/CH00070 ._CH',             # 0A
        'ED6_DT27/CH03570 ._CH',             # 0B
        'ED6_DT27/CH03510 ._CH',             # 0C
        'ED6_DT07/CH02060 ._CH',             # 0D
        'ED6_DT07/CH02070 ._CH',             # 0E
        'ED6_DT07/CH00020 ._CH',             # 0F
        'ED6_DT07/CH00050 ._CH',             # 10
        'ED6_DT27/CH03080 ._CH',             # 11
        'ED6_DT06/CH20063 ._CH',             # 12
        'ED6_DT06/CH20064 ._CH',             # 13
        'ED6_DT06/CH20038 ._CH',             # 14
        'ED6_DT26/CH20311 ._CH',             # 15
        'ED6_DT07/CH01450 ._CH',             # 16
        'ED6_DT07/CH01550 ._CH',             # 17
        'ED6_DT07/CH01140 ._CH',             # 18
        'ED6_DT07/CH01770 ._CH',             # 19
        'ED6_DT07/CH01470 ._CH',             # 1A
        'ED6_DT07/CH01590 ._CH',             # 1B
        'ED6_DT07/CH01480 ._CH',             # 1C
        'ED6_DT07/CH01490 ._CH',             # 1D
        'ED6_DT07/CH01200 ._CH',             # 1E
        'ED6_DT07/CH01230 ._CH',             # 1F
        'ED6_DT07/CH01150 ._CH',             # 20
        'ED6_DT07/CH01460 ._CH',             # 21
        'ED6_DT07/CH01470 ._CH',             # 22
    )

    AddCharChipPat(
        'ED6_DT07/CH01540P._CP',             # 00
        'ED6_DT07/CH01000P._CP',             # 01
        'ED6_DT07/CH01010P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01050P._CP',             # 06
        'ED6_DT07/CH00030P._CP',             # 07
        'ED6_DT07/CH00040P._CP',             # 08
        'ED6_DT07/CH00060P._CP',             # 09
        'ED6_DT07/CH00070P._CP',             # 0A
        'ED6_DT27/CH03570P._CP',             # 0B
        'ED6_DT27/CH03510P._CP',             # 0C
        'ED6_DT07/CH02060P._CP',             # 0D
        'ED6_DT07/CH02070P._CP',             # 0E
        'ED6_DT07/CH00020P._CP',             # 0F
        'ED6_DT07/CH00050P._CP',             # 10
        'ED6_DT27/CH03080P._CP',             # 11
        'ED6_DT06/CH20063P._CP',             # 12
        'ED6_DT06/CH20064P._CP',             # 13
        'ED6_DT06/CH20038P._CP',             # 14
        'ED6_DT26/CH20311P._CP',             # 15
        'ED6_DT07/CH01450P._CP',             # 16
        'ED6_DT07/CH01550P._CP',             # 17
        'ED6_DT07/CH01140P._CP',             # 18
        'ED6_DT07/CH01770P._CP',             # 19
        'ED6_DT07/CH01470P._CP',             # 1A
        'ED6_DT07/CH01590P._CP',             # 1B
        'ED6_DT07/CH01480P._CP',             # 1C
        'ED6_DT07/CH01490P._CP',             # 1D
        'ED6_DT07/CH01200P._CP',             # 1E
        'ED6_DT07/CH01230P._CP',             # 1F
        'ED6_DT07/CH01150P._CP',             # 20
        'ED6_DT07/CH01460P._CP',             # 21
        'ED6_DT07/CH01470P._CP',             # 22
    )

    DeclNpc(
        X                   = 58770,
        Z                   = 250,
        Y                   = 137000,
        Direction           = 281,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 83950,
        Z                   = 1500,
        Y                   = 142840,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 82520,
        Z                   = 1500,
        Y                   = 142760,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 72500,
        Z                   = -10000,
        Y                   = 163540,
        Direction           = 76,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 68650,
        Z                   = 250,
        Y                   = 147890,
        Direction           = 87,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 55860,
        Z                   = 250,
        Y                   = 134560,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 54740,
        Z                   = 250,
        Y                   = 134560,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 56060,
        Z                   = 250,
        Y                   = 145340,
        Direction           = 169,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 64980,
        Z                   = 250,
        Y                   = 147870,
        Direction           = 92,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 66300,
        Z                   = 250,
        Y                   = 147820,
        Direction           = 253,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
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
        Direction           = 180,
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
        X                   = 53780,
        Z                   = 250,
        Y                   = 136340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 62390,
        Z                   = 0,
        Y                   = 144850,
        Direction           = 246,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 60950,
        Z                   = 0,
        Y                   = 143420,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 53110,
        Z                   = 250,
        Y                   = 145310,
        Direction           = 322,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 62500,
        Z                   = -3000,
        Y                   = 170810,
        Direction           = 101,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 57230,
        Z                   = 250,
        Y                   = 138300,
        Direction           = 134,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 66300,
        Z                   = 250,
        Y                   = 147820,
        Direction           = 253,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 64980,
        Z                   = 250,
        Y                   = 147870,
        Direction           = 92,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 51050,
        Z                   = 0,
        Y                   = 83440,
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
        X                   = 48500,
        Y                   = -200,
        Z                   = 94500,
        Range               = 53500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x17318,
        Unknown_18          = 0x0,
        Unknown_1C          = 39,
    )


    DeclActor(
        TriggerX            = 56800,
        TriggerZ            = 250,
        TriggerY            = 136940,
        TriggerRange        = 800,
        ActorX              = 58770,
        ActorZ              = 1750,
        ActorY              = 137000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53710,
        TriggerZ            = 250,
        TriggerY            = 137720,
        TriggerRange        = 800,
        ActorX              = 53710,
        ActorZ              = 2450,
        ActorY              = 137720,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 44,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 71160,
        TriggerZ            = -10000,
        TriggerY            = 151550,
        TriggerRange        = 800,
        ActorX              = 71160,
        ActorZ              = -8500,
        ActorY              = 151550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 45,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_72E",          # 00, 0
        "Function_1_807",          # 01, 1
        "Function_2_8A8",          # 02, 2
        "Function_3_8BE",          # 03, 3
        "Function_4_8C3",          # 04, 4
        "Function_5_100A",         # 05, 5
        "Function_6_109E",         # 06, 6
        "Function_7_1168",         # 07, 7
        "Function_8_1261",         # 08, 8
        "Function_9_1268",         # 09, 9
        "Function_10_12BC",        # 0A, 10
        "Function_11_12F3",        # 0B, 11
        "Function_12_1347",        # 0C, 12
        "Function_13_136B",        # 0D, 13
        "Function_14_1388",        # 0E, 14
        "Function_15_13D1",        # 0F, 15
        "Function_16_13FD",        # 10, 16
        "Function_17_1450",        # 11, 17
        "Function_18_14EB",        # 12, 18
        "Function_19_1524",        # 13, 19
        "Function_20_154E",        # 14, 20
        "Function_21_1572",        # 15, 21
        "Function_22_158F",        # 16, 22
        "Function_23_2A6F",        # 17, 23
        "Function_24_2AB6",        # 18, 24
        "Function_25_2AFD",        # 19, 25
        "Function_26_2B44",        # 1A, 26
        "Function_27_2B8B",        # 1B, 27
        "Function_28_2BD2",        # 1C, 28
        "Function_29_2C19",        # 1D, 29
        "Function_30_2C35",        # 1E, 30
        "Function_31_2C7D",        # 1F, 31
        "Function_32_2E10",        # 20, 32
        "Function_33_2E71",        # 21, 33
        "Function_34_35D1",        # 22, 34
        "Function_35_3626",        # 23, 35
        "Function_36_368F",        # 24, 36
        "Function_37_36F3",        # 25, 37
        "Function_38_3743",        # 26, 38
        "Function_39_5319",        # 27, 39
        "Function_40_54C9",        # 28, 40
        "Function_41_5550",        # 29, 41
        "Function_42_55C9",        # 2A, 42
        "Function_43_564E",        # 2B, 43
        "Function_44_5669",        # 2C, 44
        "Function_45_5716",        # 2D, 45
    )


    def Function_0_72E(): pass

    label("Function_0_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_75B")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    Jump("loc_806")

    label("loc_75B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 2)), scpexpr(EXPR_END)), "loc_7DC")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x19, 0x10)
    SetChrFlags(0x1A, 0x10)
    SetChrFlags(0x1C, 0x10)
    SetChrPos(0x9, 61450, -3000, 162010, 6)
    SetChrPos(0xA, 61450, -3000, 163810, 180)
    Jump("loc_806")

    label("loc_7DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7F8")
    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    Event(0, 38)
    Jump("loc_806")

    label("loc_7F8")

    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_806")

    Return()

    # Function_0_72E end

    def Function_1_807(): pass

    label("Function_1_807")

    OP_16(0x2, 0xFA0, 0xFFFF5808, 0x7148, 0x23005F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_82C")
    OP_B1("T4105_1")
    Jump("loc_85F")

    label("loc_82C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 4)), scpexpr(EXPR_END)), "loc_83F")
    OP_B1("T4105_2")
    Jump("loc_85F")

    label("loc_83F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_856")
    OP_B1("T4105_1")
    Jump("loc_85F")

    label("loc_856")

    OP_B1("T4105_3")

    label("loc_85F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 3)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_878")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_878")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_891")
    OP_71(0x5, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    Jump("loc_8A7")

    label("loc_891")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 2)), scpexpr(EXPR_END)), "loc_8A7")
    OP_71(0x5, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)

    label("loc_8A7")

    Return()

    # Function_1_807 end

    def Function_2_8A8(): pass

    label("Function_2_8A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8BD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_8A8")

    label("loc_8BD")

    Return()

    # Function_2_8A8 end

    def Function_3_8BE(): pass

    label("Function_3_8BE")

    Call(0, 4)
    Return()

    # Function_3_8BE end

    def Function_4_8C3(): pass

    label("Function_4_8C3")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_8D4")
    Call(0, 22)
    Jump("loc_1006")

    label("loc_8D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_END)), "loc_8F0")

    ChrTalk(    #0
        0x8,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1006")

    label("loc_8F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 4)), scpexpr(EXPR_END)), "loc_FDB")
    EventBegin(0x0)
    Fade(1000)
    ClearMapFlags(0x1)
    OP_6D(57940, 250, 137110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 56920, 250, 136300, 85)
    SetChrPos(0xF7, 56810, 250, 137100, 79)
    TurnDirection(0x8, 0xF7, 0)
    OP_0D()

    ChrTalk(    #1
        0x8,
        (
            "欢迎光临。\x01",
            "要搭乘定期船吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "搭乘时需要\x01",
            "办理登船手续，\x01",
            "所以到时请把票给我。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A2E")
    TurnDirection(0x106, 0x101, 500)
    TurnDirection(0x101, 0x106, 500)

    ChrTalk(    #3
        0x106,
        (
            "#050F#5P如果办好了手续，那在船到之前\x01",
            "在这里等着就可以了。\x02\x03",

            "不需要买什么东西了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A7F")

    label("loc_A2E")

    TurnDirection(0x103, 0x101, 500)
    TurnDirection(0x101, 0x103, 500)

    ChrTalk(    #4
        0x103,
        (
            "#020F#5P办完手续后可以\x01",
            "在这里等船来。\x02\x03",

            "不需要买什么东西了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A7F")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有点事】\x01",          # 0
            "【办理乘船手续】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AE5"),
        (1, "loc_B2B"),
        (SWITCH_DEFAULT, "loc_FD8"),
    )


    label("loc_AE5")

    TurnDirection(0xF7, 0x8, 500)
    OP_8C(0x101, 85, 500)

    ChrTalk(    #5
        0x8,
        "明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "那么，在需要搭乘时\x01",
            "请再来找我。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_FD8")

    label("loc_B2B")

    TurnDirection(0xF7, 0x8, 500)
    OP_8C(0x101, 85, 500)

    ChrTalk(    #7
        0x8,
        "明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "那么请在这张单子上\x01",
            "签个字。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1011F啊，好的好的。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_BB0")

    ChrTalk(    #10
        0x106,
        "#6P#053F…………（刷刷写字声）\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD4")

    label("loc_BB0")


    ChrTalk(    #11
        0x103,
        "#6P#027F呼呼哼哼⊙(刷刷写字声)\x02",
    )

    CloseMessageWindow()

    label("loc_BD4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #12
        "\x07\x05艾丝蒂尔等人办完了乘船手续。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_3F(0x3F2, 2)

    ChrTalk(    #13
        0x8,
        "好，可以了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "那么在定期船到达之前\x01",
            "请在飞船坪内等候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1000F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    TurnDirection(0x101, 0xF7, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CC2")

    ChrTalk(    #16
        0x106,
        (
            "#051F#5P那么在船到来之前\x01",
            "到长椅上坐会儿吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CEF")

    label("loc_CC2")


    ChrTalk(    #17
        0x103,
        (
            "#021F#5P那么我们就坐在\x01",
            "长椅上等船来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CEF")

    FadeToDark(2000, 0, -1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_0D()
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    OP_71(0x9, 0x4)
    ClearMapFlags(0x10)
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x75, 0x0, 0x64)
    Sleep(1000)
    Sleep(500)
    ClearMapFlags(0x10)
    OP_48()
    OP_89(0x101, 83040, 1500, 143200, 4)
    OP_89(0xF7, 83180, 1700, 141880, 192)
    OP_6D(83210, 1700, 140260, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_DA5():
        OP_8E(0xF7, 0x142BC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_DA5)

    def lambda_DC0():
        OP_8E(0x101, 0x142BC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DC0)

    def lambda_DDB():
        OP_6D(82850, 1700, 135080, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DDB)
    Sleep(4000)
    ClearMapFlags(0x1)
    Fade(1000)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0xF7, 0x8)
    OP_6D(87540, 1500, 134660, 0)
    OP_67(0, 12280, -10000, 0)
    OP_6B(6180, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x28, 0x4)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x4)
    SetChrFlags(0x29, 0x40)
    OP_A1(0x28, 0xB)
    OP_A1(0x29, 0xA)
    OP_72(0xB, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0x9, 0x4)
    SetChrPos(0x28, 87000, -5300, 131150, 90)
    SetChrPos(0x29, 87000, -5300, 131150, 90)
    OP_48()
    OP_0D()
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x64)
    Sleep(3000)
    OP_6F(0xA, 2)
    OP_70(0xA, 0x64)
    OP_22(0x76, 0x0, 0x64)
    OP_73(0xA)
    OP_23(0x75)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xA, 100)
    OP_6F(0xB, 100)
    OP_70(0xA, 0xC8)
    OP_70(0xB, 0xC8)
    OP_73(0xB)
    OP_6F(0xA, 200)
    OP_6F(0xB, 200)
    OP_70(0xA, 0x12C)
    OP_70(0xB, 0x12C)

    def lambda_F0B():
        OP_8F(0xFE, 0x186A0, 0x1F4, 0x20026, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_F0B)

    def lambda_F26():
        OP_8F(0xFE, 0x186A0, 0x1F4, 0x20026, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_F26)
    WaitChrThread(0x29, 0x1)
    Fade(1000)
    OP_6D(108820, 1500, 134250, 0)
    OP_67(0, 9790, -10000, 0)
    OP_6B(7800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)

    def lambda_F88():
        OP_8F(0xFE, 0x2450E, 0x5DC, 0x20026, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 3, lambda_F88)

    def lambda_FA3():
        OP_8F(0xFE, 0x2450E, 0x5DC, 0x20026, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_FA3)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    WaitChrThread(0x29, 0x3)
    NewScene("ED6_DT21/E0000   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_FD8")

    label("loc_FD8")

    Jump("loc_1006")

    label("loc_FDB")


    ChrTalk(    #18
        0x8,
        (
            "需要购买船票的客人请去\x01",
            "那边的建筑物～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1006")

    TalkEnd(0x8)
    Return()

    # Function_4_8C3 end

    def Function_5_100A(): pass

    label("Function_5_100A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1075")

    ChrTalk(    #19
        0xFE,
        (
            "唔，嗯……\x01",
            "机械部分无任何异常。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "导力压的调整也完成了……\x01",
            "这、这下，全部都结束了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109A")

    label("loc_1075")


    ChrTalk(    #21
        0xFE,
        (
            "唔，嗯……\x01",
            "……下一班定期船……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109A")

    TalkEnd(0xFE)
    Return()

    # Function_5_100A end

    def Function_6_109E(): pass

    label("Function_6_109E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1119")

    ChrTalk(    #22
        0xFE,
        (
            "最后的总检查\x01",
            "是维修主任您的工作吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "对了，不要对我这么客气。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "真是的……\x01",
            "为什么每次都变成这样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1164")

    label("loc_1119")


    ChrTalk(    #25
        0xFE,
        (
            "真让人着急……\x01",
            "赛希莉亚号刚刚才飞走吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "接下来是林德号、林德号！\x02",
    )

    CloseMessageWindow()

    label("loc_1164")

    TalkEnd(0xFE)
    Return()

    # Function_6_109E end

    def Function_7_1168(): pass

    label("Function_7_1168")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_122F")

    ChrTalk(    #27
        0xFE,
        (
            "不得了不得了，\x01",
            "新引擎的性能真令人吃惊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "不过看来还需要不断通过\x01",
            "飞行实验来收集数据。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "要最大限度地发挥动力\x01",
            "就必须考虑机体的协调性。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "我想过一阵就\x01",
            "去请教请教拉赛尔博士。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_125D")

    label("loc_122F")


    ChrTalk(    #31
        0xFE,
        "快了，快了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "只要新型引擎完成……\x02",
    )

    CloseMessageWindow()

    label("loc_125D")

    TalkEnd(0xFE)
    Return()

    # Function_7_1168 end

    def Function_8_1261(): pass

    label("Function_8_1261")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_8_1261 end

    def Function_9_1268(): pass

    label("Function_9_1268")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_12B8")

    ChrTalk(    #33
        0xFE,
        (
            "果然男人还是要\x01",
            "自己来开拓道路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "所以呢，\x01",
            "该是旅行的时候了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12B8")

    TalkEnd(0xFE)
    Return()

    # Function_9_1268 end

    def Function_10_12BC(): pass

    label("Function_10_12BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_12EF")

    ChrTalk(    #35
        0xFE,
        (
            "哈哈，和安敦在一起\x01",
            "真不会感到无聊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EF")

    TalkEnd(0xFE)
    Return()

    # Function_10_12BC end

    def Function_11_12F3(): pass

    label("Function_11_12F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1343")

    ChrTalk(    #36
        0xFE,
        (
            "我终于找到了\x01",
            "自己想做的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "所以为了学习，\x01",
            "我准备去柏斯。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1343")

    TalkEnd(0xFE)
    Return()

    # Function_11_12F3 end

    def Function_12_1347(): pass

    label("Function_12_1347")

    TalkBegin(0xFE)

    ChrTalk(    #38
        0xFE,
        (
            "呵呵，你要\x01",
            "好好看家哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1347 end

    def Function_13_136B(): pass

    label("Function_13_136B")

    TalkBegin(0xFE)

    ChrTalk(    #39
        0xFE,
        "妈妈，你放心吧！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_136B end

    def Function_14_1388(): pass

    label("Function_14_1388")

    TalkBegin(0xFE)

    ChrTalk(    #40
        0xFE,
        (
            "我是第一次一个人\x01",
            "坐飞船……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "什、什么啊，\x01",
            "我可没有紧张。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_1388 end

    def Function_15_13D1(): pass

    label("Function_15_13D1")

    TalkBegin(0xFE)

    ChrTalk(    #42
        0xFE,
        (
            "爷～爷，我\x01",
            "想坐那～边的飞～船！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_13D1 end

    def Function_16_13FD(): pass

    label("Function_16_13FD")

    TalkBegin(0xFE)

    ChrTalk(    #43
        0xFE,
        (
            "听、听话，那可是\x01",
            "女王陛下的飞船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "如果能乘坐的话，\x01",
            "我倒也想坐坐。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_13FD end

    def Function_17_1450(): pass

    label("Function_17_1450")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 3)), scpexpr(EXPR_END)), "loc_14A8")

    ChrTalk(    #45
        0xFE,
        "怎、怎么了……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "刚才出来的那两个人\x01",
            "表情恐怖的互相瞪着对方……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E7")

    label("loc_14A8")


    ChrTalk(    #47
        0xFE,
        (
            "呼……这就是\x01",
            "飞船公社的总公司啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "相当不错的建筑。\x02",
    )

    CloseMessageWindow()

    label("loc_14E7")

    TalkEnd(0xFE)
    Return()

    # Function_17_1450 end

    def Function_18_14EB(): pass

    label("Function_18_14EB")

    TalkBegin(0xFE)

    ChrTalk(    #49
        0xFE,
        "哟，这就是埃尔赛尤啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "好漂亮的飞船……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_14EB end

    def Function_19_1524(): pass

    label("Function_19_1524")

    TalkBegin(0xFE)

    ChrTalk(    #51
        0xFE,
        (
            "搭下一班飞船\x01",
            "几点能到蔡斯呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_1524 end

    def Function_20_154E(): pass

    label("Function_20_154E")

    TalkBegin(0xFE)

    ChrTalk(    #52
        0xFE,
        (
            "听着，你\x01",
            "一定要乖乖的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_154E end

    def Function_21_1572(): pass

    label("Function_21_1572")

    TalkBegin(0xFE)

    ChrTalk(    #53
        0xFE,
        "嗯，一言为定～！\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_1572 end

    def Function_22_158F(): pass

    label("Function_22_158F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15AF")
    Call(0, 40)
    Call(0, 42)
    FadeToBright(0, 0)

    label("loc_15AF")

    Fade(1000)
    OP_6D(57660, 250, 137100, 0)
    OP_67(0, 8420, -10000, 0)
    OP_6B(2690, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 56940, 250, 136330, 90)
    SetChrPos(0xF7, 56900, 250, 137490, 90)
    SetChrPos(0xF8, 55560, 250, 135910, 90)
    SetChrPos(0xF9, 55480, 250, 137370, 90)
    OP_8C(0x8, 276, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1833")
    OP_A2(0x163E)

    ChrTalk(    #54
        0x8,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "你们是去柏斯的\x01",
            "游击士吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#1011F啊，嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "艾南先生已经\x01",
            "替你们付过旅费了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        "要办理搭乘手续吗？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF7, 180, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1743")

    ChrTalk(    #59
        0x106,
        (
            "#050F#5P如果办好了手续，那在船到之前\x01",
            "在这里等着就可以了。\x02\x03",

            "我们已经在格兰赛尔\x01",
            "没有事留下了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A9")

    label("loc_1743")


    ChrTalk(    #60
        0x103,
        (
            "#020F#5P如果办好了手续，那在船到之前\x01",
            "在这里等着就可以了。\x02\x03",

            "在格兰赛尔\x01",
            "已经没有什么还需要做的吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17A9")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【还有事情】\x01",          # 0
            "【办理乘船手续】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1830")

    ChrTalk(    #61
        0x8,
        (
            "那么请在方便的时候\x01",
            "再来找我。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_1830")

    Jump("loc_18DB")

    label("loc_1833")


    ChrTalk(    #62
        0x8,
        (
            "哎呀……\x01",
            "要办理搭乘手续吗？\x02",
        )
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
            "【还有事情】\x01",          # 0
            "【办理乘船手续】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18DB")

    ChrTalk(    #63
        0x8,
        (
            "那么请在方便的时候\x01",
            "再来找我。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_18DB")


    ChrTalk(    #64
        0x8,
        "明白了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF7, 90, 400)

    ChrTalk(    #65
        0x8,
        (
            "那么，我和协会联系一下，\x01",
            "请其他人也来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #66
        (
            "\x07\x05艾丝蒂尔一行人办理完乘船手续之后\x01",
            "就在原地等待飞船起飞。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Call(0, 31)
    OP_6D(87590, 1500, 142760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(150000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 91000, 1500, 143280, 270)
    SetChrPos(0x103, 91860, 1500, 142720, 270)
    SetChrPos(0x106, 91910, 1500, 143800, 270)
    SetChrPos(0x105, 93140, 1500, 142720, 270)
    SetChrPos(0x107, 92990, 1500, 143800, 270)
    SetChrPos(0x108, 94220, 1500, 142720, 270)
    SetChrPos(0x104, 94240, 1500, 143800, 270)
    SetChrPos(0x12, 82860, 1500, 143460, 180)
    SetChrPos(0x13, 84050, 1500, 143590, 270)
    SetChrPos(0x14, 86810, 1500, 143690, 270)
    SetChrPos(0x15, 88180, 1500, 143410, 270)
    SetChrPos(0x16, 85280, 1500, 143380, 270)
    SetChrPos(0x17, 89440, 1500, 143050, 270)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    OP_6F(0xA, 60)
    OP_6F(0x5, 100)
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x75, 0x1, 0x5A)
    Sleep(3000)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(1000)
    OP_71(0x9, 0x4)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x1)
    Sleep(1500)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 100)
    OP_70(0x5, 0xC8)
    OP_73(0x5)
    OP_43(0x12, 0x1, 0x0, 0x17)
    Sleep(500)
    OP_43(0x13, 0x1, 0x0, 0x17)
    Sleep(800)
    OP_43(0x16, 0x1, 0x0, 0x17)
    Sleep(600)
    OP_43(0x14, 0x1, 0x0, 0x17)
    Sleep(100)
    OP_43(0x15, 0x1, 0x0, 0x17)
    Sleep(500)
    OP_43(0x17, 0x1, 0x0, 0x17)
    Sleep(500)

    def lambda_1BAC():
        OP_8E(0xFE, 0x14564, 0x5DC, 0x22FB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BAC)
    Sleep(500)

    def lambda_1BCC():
        OP_6D(83300, 1500, 143110, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BCC)

    def lambda_1BE4():
        OP_8E(0xFE, 0x14C94, 0x5DC, 0x22D80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BE4)
    Sleep(200)

    def lambda_1C04():
        OP_8E(0xFE, 0x14CEE, 0x5DC, 0x231B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1C04)
    Sleep(100)

    def lambda_1C24():
        OP_8E(0xFE, 0x150E0, 0x5DC, 0x231B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1C24)
    Sleep(100)

    def lambda_1C44():
        OP_8E(0xFE, 0x15112, 0x5DC, 0x22D80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C44)
    Sleep(100)

    def lambda_1C64():
        OP_8E(0xFE, 0x15572, 0x5DC, 0x231B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C64)
    Sleep(100)

    def lambda_1C84():
        OP_8E(0xFE, 0x1559A, 0x5DC, 0x22D80, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1C84)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 180, 400)
    SetChrPos(0x26, 73360, 1500, 142950, 90)
    SetChrPos(0x27, 73360, 1500, 143830, 90)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)

    NpcTalk(    #67
        0x26,
        "男人的声音",
        "#1P赶上了吗……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 270, 400)

    def lambda_1DC4():
        OP_6D(81000, 1500, 142960, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DC4)

    def lambda_1DDC():
        OP_67(0, 7210, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1DDC)

    def lambda_1DF4():
        OP_6C(225000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1DF4)

    def lambda_1E04():
        OP_6B(2270, 3000)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_1E04)

    def lambda_1E14():
        OP_6E(362, 3000)
        ExitThread()

    QueueWorkItem(0x26, 3, lambda_1E14)

    def lambda_1E24():
        OP_8E(0xFE, 0x135F6, 0x5DC, 0x22E66, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_1E24)
    Sleep(500)

    def lambda_1E44():
        OP_8E(0xFE, 0x133E4, 0x5DC, 0x231D6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1E44)
    WaitChrThread(0x26, 0x1)
    WaitChrThread(0x26, 0x2)

    ChrTalk(    #68
        0x101,
        (
            "#1004F#6P咦，奈尔……\x01",
            "朵洛希也在？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x27,
        "#154F#4P小艾……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x26,
        (
            "#145F#5P呼～我去了协会，\x01",
            "听说已经出发了。\x02\x03",

            "#140F我就急着追来了，\x01",
            "还好赶上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1015F#6P咦，怎么了？\x02\x03",

            "关于昨晚的事件\x01",
            "我们应该聊过了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x26,
        "#142F#5P不……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x26, 135, 400)
    Sleep(500)
    TurnDirection(0x26, 0x101, 400)
    Sleep(500)

    ChrTalk(    #73
        0x26,
        (
            "#140F#5P我有点私人的事情\x01",
            "要跟你说。\x02\x03",

            "起飞之前\x01",
            "能跟我们待一会儿吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1004F#6P我？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #75
        0x101,
        "#1015F#5P那么，雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x103,
        (
            "#027F没关系。\x01",
            "你们聊吧。\x02\x03",

            "我们就先进去\x01",
            "帮你找座位了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1006F#5P嗯，拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x105,
        (
            "#040F#5P祝你们愉快。\x01",
            "奈尔先生，朵洛希小姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x107,
        "#061F#5P再见！\x02",
    )

    CloseMessageWindow()

    def lambda_2085():
        OP_8E(0xFE, 0x13D4E, 0x5DC, 0x22FB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2085)

    def lambda_20A0():
        OP_6D(79800, 1500, 143330, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_20A0)

    def lambda_20B8():
        OP_6B(2100, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_20B8)
    OP_43(0x103, 0x1, 0x0, 0x18)
    Sleep(800)
    OP_43(0x106, 0x1, 0x0, 0x19)
    Sleep(300)
    OP_43(0x107, 0x1, 0x0, 0x1A)
    Sleep(800)
    OP_43(0x105, 0x1, 0x0, 0x1B)
    Sleep(300)
    OP_43(0x108, 0x1, 0x0, 0x1C)
    Sleep(500)
    OP_43(0x104, 0x1, 0x0, 0x1D)
    Sleep(4000)

    ChrTalk(    #80
        0x101,
        (
            "#1011F#6P没太多时间了，\x01",
            "有什么话赶紧说吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #81
        0x101,
        (
            "#1019F#5P咦，奥利维尔为什么\x01",
            "还留在这里不走？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x104,
        (
            "#035F呵呵，你就把我\x01",
            "当作路边的\x01",
            "小石子吧。\x02\x03",

            "#030F好了，快开始吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1007F#5P这个男人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x26,
        (
            "#142F真是颗自说自话的\x01",
            "小石子啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x103, 0x80)
    SetChrPos(0x103, 83210, 1500, 134330, 0)
    OP_8E(0x103, 0x143AC, 0x6A4, 0x22880, 0xFA0, 0x0)

    ChrTalk(    #85
        0x103,
        (
            "#027F#5P我还在想怎么突然找不到你了，\x01",
            "果然在这里啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x103, 0x104, 0x1F4, 0xBB8, 0x0)

    ChrTalk(    #86
        0x104,
        "#036F等、等等，雪拉……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x103,
        (
            "#021F#5P好了好了，我们\x01",
            "快去自己的座位吧～\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)

    def lambda_22E2():

        label("loc_22E2")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_22E2")

    QueueWorkItem2(0x101, 1, lambda_22E2)

    def lambda_22F3():

        label("loc_22F3")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_22F3")

    QueueWorkItem2(0x26, 1, lambda_22F3)

    def lambda_2304():

        label("loc_2304")

        TurnDirection(0xFE, 0x104, 0)
        OP_48()
        Jump("loc_2304")

    QueueWorkItem2(0x27, 1, lambda_2304)
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_2327():
        OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2327)
    Sleep(100)

    def lambda_2347():
        OP_8C(0x104, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2347)

    def lambda_2355():
        OP_8F(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2355)
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0x104, 20)
    SetChrSubChip(0x104, 5)
    OP_6D(80980, 1500, 139850, 2000)
    WaitChrThread(0x103, 0x1)
    SetChrFlags(0x103, 0x80)
    WaitChrThread(0x104, 0x1)
    SetChrFlags(0x104, 0x80)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x26, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x101, 0x1)
    OP_44(0x26, 0x1)
    OP_44(0x27, 0x1)
    OP_6D(79960, 1500, 143070, 1500)
    TurnDirection(0x26, 0x101, 400)

    ChrTalk(    #88
        0x26,
        (
            "#142F#5P怎么说呢，\x01",
            "那位老兄还真是一成不变……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x26, 400)

    ChrTalk(    #89
        0x101,
        "#1016F#6P哈哈，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x27,
        "#154F#4P………………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x27, 400)

    ChrTalk(    #91
        0x101,
        (
            "#1015F#6P朵洛希。\x01",
            "你好像无精打采的。\x02\x03",

            "我记得你去柏斯\x01",
            "地区采访了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x27, 0x101, 400)
    Sleep(500)

    ChrTalk(    #92
        0x27,
        (
            "#154F嗯、嗯……\x01",
            "是今早回来的……\x02\x03",

            "我、我说～小艾……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#1006F#6P啊，我想起来了！\x02\x03",

            "我记得你们去了\x01",
            "迷雾峡谷的空贼老巢。\x02\x03",

            "听说那里现在是军队的\x01",
            "飞行训练基地……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #94
        0x101,
        "#1004F#6P咦，这么说……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x26,
        (
            "#140F#5P你终于注意到了啊。\x02\x03",

            "那就是昨晚被空贼团的\x01",
            "余党袭击的基地。\x02\x03",

            "空贼艇被夺时\x01",
            "这家伙正好在场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#1002F#6P这、这样啊……\x02\x03",

            "#1011F那你们是特地\x01",
            "来提供消息的？\x02\x03",

            "#1001F嘿嘿，你还挺聪明的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x26,
        (
            "#145F#5P嗯，虽然确实可以\x01",
            "说是提供消息……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1004F#6P咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x26,
        (
            "#142F#5P算了。\x01",
            "朵洛希，把东西拿出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x27,
        "#154F好、好的……\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_8E(0x27, 0x13A6A, 0x5DC, 0x22FBA, 0x5DC, 0x0)
    Sleep(500)

    ChrTalk(    #101
        0x27,
        (
            "#155F#2P我说啊～小艾。\x02\x03",

            "你可别太\x01",
            "往坏处想哦～\x02\x03",

            "照片是不一定会\x01",
            "反映所有的真实情况的～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1008F#6P怎、怎么了啊？\x01",
            "表情这么凝重……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x27,
        (
            "#154F#2P这……\x01",
            "就是我昨天拍的照片～\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #104
        "\x07\x05艾丝蒂尔从朵洛希那里拿到一张照片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x41A, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_AD(0x240091, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    SetMessageWindowPos(100, 320, -1, -1)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #105
        (
            "\x07\x00#1015F#6P这是……\x01",
            "空贼艇和那个男人婆。\x02\x03",

            "那么，这边的人是……\x02\x03",

            "………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetChrName("艾丝蒂尔")

    AnonymousTalk(    #106
        "\x07\x00#1004F#3S咦。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrPos(0x27, 79680, 1500, 144000, 90)
    OP_AE(0x1F4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #107
        0x26,
        (
            "#142F#5P……现在我们还不准备\x01",
            "将这张照片提供给王国军。\x02\x03",

            "当然也不会刊登。\x02\x03",

            "应该怎么做\x01",
            "由你来判断。\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x26, 0x3, 0x0, 0x1E)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Call(0, 32)
    Sleep(1000)
    OP_AD(0x2400B0, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_28(0xA9, 0x4, 0x40)
    OP_28(0xAA, 0x4, 0x40)
    OP_28(0xAB, 0x4, 0x40)
    OP_28(0xAC, 0x4, 0x40)
    OP_A2(0x1683)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x125), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存】\x01",            # 0
            "【进入下一章】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A39")
    ShowSaveMenu()

    label("loc_2A39")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A3(0x1683)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_158F end

    def Function_23_2A6F(): pass

    label("Function_23_2A6F")

    OP_8E(0xFE, 0x143AC, 0x5DC, 0x23064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_23_2A6F end

    def Function_24_2AB6(): pass

    label("Function_24_2AB6")

    OP_8E(0xFE, 0x143AC, 0x5DC, 0x23064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_24_2AB6 end

    def Function_25_2AFD(): pass

    label("Function_25_2AFD")

    OP_8E(0xFE, 0x143AC, 0x5DC, 0x23064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_25_2AFD end

    def Function_26_2B44(): pass

    label("Function_26_2B44")

    OP_8E(0xFE, 0x143AC, 0x5DC, 0x23064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_2B44 end

    def Function_27_2B8B(): pass

    label("Function_27_2B8B")

    OP_8E(0xFE, 0x143AC, 0x5DC, 0x23064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_27_2B8B end

    def Function_28_2BD2(): pass

    label("Function_28_2BD2")

    OP_8E(0xFE, 0x143AC, 0x5DC, 0x23064, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x20A6C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x143AC, 0x5DC, 0x1FDF6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_28_2BD2 end

    def Function_29_2C19(): pass

    label("Function_29_2C19")

    OP_8E(0xFE, 0x143F2, 0x5DC, 0x2335C, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_29_2C19 end

    def Function_30_2C35(): pass

    label("Function_30_2C35")

    Sleep(600)
    OP_24(0x75, 0x50)
    Sleep(300)
    OP_24(0x75, 0x46)
    Sleep(300)
    OP_24(0x75, 0x3C)
    Sleep(300)
    OP_24(0x75, 0x32)
    Sleep(300)
    OP_24(0x75, 0x28)
    Sleep(300)
    OP_24(0x75, 0x1E)
    Sleep(300)
    OP_24(0x75, 0x14)
    Sleep(300)
    OP_23(0x75)
    Return()

    # Function_30_2C35 end

    def Function_31_2C7D(): pass

    label("Function_31_2C7D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CB6")
    AddParty(0x5, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2CB6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2CDB")
    AddParty(0x2, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2CDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D28")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D10")
    AddParty(0x6, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2D28")

    label("loc_2D10")

    AddParty(0x6, 0xFB, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2D28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D9D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D5D")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2D9D")

    label("loc_2D5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D85")
    AddParty(0x3, 0xFB, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2D9D")

    label("loc_2D85")

    AddParty(0x3, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2D9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2DEA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DD2")
    AddParty(0x4, 0xFB, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jump("loc_2DEA")

    label("loc_2DD2")

    AddParty(0x4, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2DEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E0F")
    AddParty(0x7, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2E0F")

    Return()

    # Function_31_2C7D end

    def Function_32_2E10(): pass

    label("Function_32_2E10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E20")
    RemoveParty(0x5, 0xFF)

    label("loc_2E20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E30")
    RemoveParty(0x2, 0xFF)

    label("loc_2E30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E40")
    RemoveParty(0x6, 0xFF)

    label("loc_2E40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E50")
    RemoveParty(0x3, 0xFF)

    label("loc_2E50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E60")
    RemoveParty(0x4, 0xFF)

    label("loc_2E60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_2E70")
    RemoveParty(0x7, 0xFF)

    label("loc_2E70")

    Return()

    # Function_32_2E10 end

    def Function_33_2E71(): pass

    label("Function_33_2E71")

    ClearMapFlags(0x1)
    ClearMapFlags(0x80)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x9, 0x4)
    ClearMapFlags(0x10)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_6D(83480, 1500, 131810, 0)
    OP_67(0, 15200, -10000, 0)
    OP_6B(7000, 0)
    OP_6C(30000, 0)
    OP_6E(262, 0)
    OP_6F(0x5, 100)
    OP_6F(0xA, 410)
    SetChrFlags(0x28, 0x4)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x4)
    SetChrFlags(0x29, 0x40)
    OP_A1(0x28, 0xB)
    OP_A1(0x29, 0xA)
    OP_72(0xB, 0x4)
    OP_72(0xA, 0x4)
    OP_6F(0xA, 390)
    OP_70(0xA, 0x12C)
    FadeToBright(3000, 0)
    SetChrPos(0x28, 87000, -5100, 130500, 90)
    SetChrPos(0x29, 87000, 5500, 130500, 90)

    def lambda_2F75():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F75)

    def lambda_2F85():
        OP_67(0, 11200, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F85)

    def lambda_2F9D():
        OP_6B(3500, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2F9D)
    OP_43(0x2D, 0x0, 0x0, 0x2B)

    def lambda_2FB4():
        OP_8F(0xFE, 0x153D8, 0xFFFFE9EE, 0x1FDC4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_2FB4)
    WaitChrThread(0x29, 0x2)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(100)
    OP_72(0xA, 0x20)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0xA, 80)
    OP_70(0xA, 0x1)
    Sleep(2700)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 100)
    OP_70(0x5, 0x0)
    Sleep(3000)
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0xA, 411)
    OP_70(0xA, 0x1C2)
    OP_73(0xA)
    Sleep(300)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)
    SetChrFlags(0x16, 0x40)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x10A, 0x20)
    SetChrBattleFlags(0x12, 0x20)
    SetChrBattleFlags(0x13, 0x20)
    SetChrBattleFlags(0x14, 0x20)
    SetChrBattleFlags(0x15, 0x20)
    SetChrBattleFlags(0x16, 0x20)
    OP_48()
    OP_89(0x12, 86970, 1700, 130570, 189)
    OP_89(0x13, 89160, 1500, 133510, 189)
    OP_89(0x14, 86970, 1700, 130570, 189)
    OP_89(0x15, 86970, 1700, 130570, 189)
    OP_89(0x16, 89160, 1500, 133510, 189)
    OP_89(0x101, 86970, 1700, 130570, 189)
    OP_89(0x10A, 86970, 1700, 130570, 189)
    OP_43(0x12, 0x1, 0x0, 0x23)
    Sleep(1000)
    OP_43(0x13, 0x1, 0x0, 0x22)
    Sleep(2000)
    OP_43(0x14, 0x1, 0x0, 0x23)
    Sleep(1000)
    OP_43(0x15, 0x1, 0x0, 0x23)
    Sleep(1000)
    OP_43(0x16, 0x1, 0x0, 0x22)
    Sleep(2000)
    OP_43(0x10A, 0x1, 0x0, 0x24)
    Sleep(800)
    OP_43(0x101, 0x1, 0x0, 0x25)
    Sleep(4000)
    Fade(1000)
    OP_6D(82440, 1500, 142990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x10A, 0x1)
    Sleep(500)

    ChrTalk(    #108
        0x10A,
        (
            "#819F呼～\x02\x03",

            "在飞船上呆了大半天的，\x01",
            "果真是累人啊。\x02\x03",

            "#810F赶紧去向协会报到和\x01",
            "汇报完成训练的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1015F#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x10A,
        "#814F艾丝蒂尔？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1025F#5P嗯、嗯……\x02\x03",

            "对了。\x01",
            "还要和艾南先生打招呼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10A,
        (
            "#810F那个……莫非。\x02\x03",

            "艾丝蒂尔你在紧张？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1007F#5P嗯、嗯，不知道为什么……\x02\x03",

            "#1026F在参加训练之前\x01",
            "从没这种感觉……\x02\x03",

            "想到今后就要\x01",
            "以正游击士的身份工作了，\x01",
            "总觉得平静不下来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x10A,
        (
            "#810F是吗。\x02\x03",

            "#1314F这大概……\x01",
            "就是所谓的兴奋难耐吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#1004F#5P兴、兴奋难耐？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x10A,
        (
            "#816F艾丝蒂尔，你在这\x01",
            "一个月的训练中变强了。\x02\x03",

            "不仅是力量，\x01",
            "我觉得应该还包括知识、\x01",
            "谨慎度和判断力。\x02\x03",

            "#817F揭开神秘组织的阴谋、\x01",
            "带回约修亚……\x02\x03",

            "#816F你大概是预先感知\x01",
            "到了这些事的困难程度吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        (
            "#1004F#5P啊……\x02\x03",

            "#1000F嗯。\x01",
            "被你这么一说，我也觉得可能是这样。\x02\x03",

            "#1007F唉……我真是个傻瓜。\x02\x03",

            "就好像不知道自己要登的山\x01",
            "有多高的登山员一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x10A,
        "#1314F你不想登了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#1006F#5P当然不是！\x01",
            "相反，比之前更有干劲了。\x02\x03",

            "不管是多高的山，到头来\x01",
            "还是只能一步一步向上登。\x02\x03",

            "#1018F就算是爬，我也要\x01",
            "爬到山顶！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x10A,
        (
            "#811F呵呵，这就对了。\x02\x03",

            "#1310F那么赶快\x01",
            "回协会报告吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        "#1006F#5P嗯，明白！\x02",
    )

    CloseMessageWindow()
    FadeToBright(1500, 0)
    OP_0D()
    NewScene("ED6_DT21/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_33_2E71 end

    def Function_34_35D1(): pass

    label("Function_34_35D1")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x14438, 0x6A4, 0x20832, 0x7D0, 0x0)
    OP_8C(0xFE, 11, 1000)
    OP_8E(0xFE, 0x1446A, 0x640, 0x22ED4, 0x7D0, 0x0)
    OP_8C(0xFE, 278, 1000)
    OP_8E(0xFE, 0x110DA, 0x640, 0x22ED4, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_34_35D1 end

    def Function_35_3626(): pass

    label("Function_35_3626")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x14938, 0x6A4, 0x1FD6A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x142B2, 0x6A4, 0x2071A, 0x7D0, 0x0)
    OP_8C(0xFE, 11, 1000)
    OP_8E(0xFE, 0x1446A, 0x640, 0x22ED4, 0x7D0, 0x0)
    OP_8C(0xFE, 278, 1000)
    OP_8E(0xFE, 0x110DA, 0x640, 0x22ED4, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_35_3626 end

    def Function_36_368F(): pass

    label("Function_36_368F")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x1491A, 0x640, 0x1FFCC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x14406, 0x5DC, 0x2097C, 0x7D0, 0x0)
    OP_8C(0xFE, 11, 1000)
    OP_8E(0xFE, 0x1446A, 0x640, 0x22ED4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13E8E, 0x5DC, 0x22ED4, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 500)
    Return()

    # Function_36_368F end

    def Function_37_36F3(): pass

    label("Function_37_36F3")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x14820, 0x640, 0x1FFCC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x14406, 0x5DC, 0x2097C, 0x7D0, 0x0)
    OP_8C(0xFE, 11, 1000)
    OP_8E(0xFE, 0x1446A, 0x640, 0x22ED4, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 500)
    Return()

    # Function_37_36F3 end

    def Function_38_3743(): pass

    label("Function_38_3743")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_22(0x75, 0x0, 0x64)
    OP_71(0x9, 0x4)
    ClearMapFlags(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_376F")
    Call(0, 40)

    label("loc_376F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3781")
    AddParty(0x2, 0xF7, 0xFF)
    AddParty(0x5, 0xF8, 0xFF)
    Jump("loc_3789")

    label("loc_3781")

    AddParty(0x5, 0xF7, 0xFF)
    AddParty(0x2, 0xF8, 0xFF)

    label("loc_3789")

    OP_6D(83200, 1500, 143040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 83490, 1700, 143700, 180)
    SetChrPos(0xF7, 82560, 1700, 143700, 180)
    SetChrPos(0xF8, 83490, 1700, 142100, 360)
    SetChrPos(0x10A, 82560, 1700, 142100, 360)
    SetChrPos(0x17, 81620, 1500, 115180, 360)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6C(135000, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3C1C")

    ChrTalk(    #122
        0x106,
        (
            "#053F那我们就\x01",
            "先行一步了。\x02\x03",

            "#050F……喂，艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        "#1011F#6P嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x106,
        (
            "#050F有时候勉强打起精神\x01",
            "也许是一种必要……\x02\x03",

            "不过你是一个女人。\x02\x03",

            "偶尔也应该依赖一下别人，\x01",
            "吐露下自己的苦衷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#1026F#6P咦……\x02\x03",

            "#1002F什、什么啊！\x01",
            "因为我是女人你就瞧不起我？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x106,
        (
            "#053F不，我没这个意思。\x02\x03",

            "#552F只不过男人是一种愚蠢的动物，\x01",
            "总会不自觉地意气用事。\x02\x03",

            "我，还有大叔都这样……\x01",
            "约修亚大概也一样吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#1026F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x106,
        (
            "#051F愚蠢的意气用事，\x01",
            "只有这一点死也治不好。\x02\x03",

            "所以，你作为女人，\x01",
            "没必要和我们逞强。\x02\x03",

            "有时也可以依靠一下别人，\x01",
            "按照自己的方式生活。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1017F#6P阿加特……\x02\x03",

            "嗯，我会记在心里。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x106, 400)

    ChrTalk(    #130
        0x103,
        (
            "#027F呵呵，想不到你也会\x01",
            "说出这么体贴人的话。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x106, 400)

    ChrTalk(    #131
        0x10A,
        (
            "#1310F没错没错。\x01",
            "我都有点吃惊了。\x02\x03",

            "#811F想不到阿加特前辈\x01",
            "也会对女孩子温柔……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x103, 400)

    ChrTalk(    #132
        0x106,
        "#054F喂，你这是什么意思啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x10A,
        "#1315F哈哈，开玩笑的啦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x103, 400)

    def lambda_3BCE():
        TurnDirection(0x106, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3BCE)
    Sleep(100)

    def lambda_3BE1():
        TurnDirection(0x103, 0x10A, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3BE1)
    Sleep(300)

    ChrTalk(    #134
        0x10A,
        (
            "#1314F……艾丝蒂尔。\x01",
            "要暂时离别了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3ECE")

    label("loc_3C1C")


    ChrTalk(    #135
        0x103,
        (
            "#021F那我们就\x01",
            "先行一步了。\x02\x03",

            "#020F艾丝蒂尔……\x01",
            "你难得回来一次，\x01",
            "却不能多聊聊，真是遗憾啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#1016F#6P嗯……我也是。\x02\x03",

            "#1011F不过爱娜小姐那边似乎也很麻烦，\x01",
            "没办法了。\x02\x03",

            "替我向洛连特的各位问好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x103,
        (
            "#020F嗯，明白了。\x02\x03",

            "艾丝蒂尔。\x01",
            "我知道你已经没问题了……\x02\x03",

            "不过还是别太着急了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#1026F#6P雪拉姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x103,
        (
            "#026F塔罗牌显示\x01",
            "你和约修亚的关系\x01",
            "并没有断。\x02\x03",

            "#020F所以啦，不必担心。\x01",
            "要相信你和约修亚之间的羁绊。\x02\x03",

            "那样的话，你就一定能找到自己的道路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        (
            "#1017F#6P嗯…明白了。\x02\x03",

            "谢谢，雪拉姐。\x01",
            "你的话给我很多勇气。\x02\x03",

            "#1003F我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x103,
        (
            "#021F好了好了，别一副这样的表情。\x02\x03",

            "#027F你已经是正游击士了吧？\x01",
            "要挺起胸膛前进。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#1017F#6P……嗯，我知道。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x10A,
        (
            "#1314F呵呵……\x02\x03",

            "艾丝蒂尔。\x01",
            "要暂时离别了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ECE")


    ChrTalk(    #144
        0x101,
        (
            "#1017F#6P亚妮拉丝……\x02\x03",

            "真的谢谢你陪我\x01",
            "一起训练。\x02\x03",

            "其实是雪拉姐拜托你\x01",
            "陪我一起的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x103,
        "#023F咦……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3F4D")
    TurnDirection(0x103, 0x101, 400)
    TurnDirection(0x106, 0x103, 400)

    label("loc_3F4D")


    ChrTalk(    #146
        0x10A,
        (
            "#1315F嘿嘿，看来是穿帮了。\x02\x03",

            "#810F嗯，如果有个\x01",
            "不太了解约修亚的人在你\x01",
            "身边的话，有助于你整理情绪。\x02\x03",

            "雪拉前辈就是这么说着拜托我的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x101,
        "#1001F#6P嘿嘿，我就知道。\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x103, 0x10A, 800)
    Sleep(500)

    ChrTalk(    #148
        0x103,
        (
            "#024F等、等等……\x01",
            "你怎么都给说出来了？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x103, 400)

    ChrTalk(    #149
        0x10A,
        "#819F好了啦，这也没什么吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_407A")
    TurnDirection(0x103, 0x101, 400)
    TurnDirection(0x10A, 0x106, 400)

    label("loc_407A")

    Sleep(400)

    ChrTalk(    #150
        0x10A,
        (
            "#816F……不过，不仅如此，\x01",
            "我自己也确实得到了锻炼。\x02\x03",

            "与艾丝蒂尔一起训练\x01",
            "我真是受益匪浅。\x02\x03",

            "#811F所以我也要谢谢你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        "#1017F#6P亚妮拉丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x10A,
        (
            "#1316F另、另外，那个……\x02\x03",

            "我接下来要说的话\x01",
            "你可能会感觉有点奇怪……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1011F#6P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x10A,
        (
            "#1314F虽然我认为我们已经是朋友了……\x02\x03",

            "不过我想让自己和艾丝蒂尔的\x01",
            "关系再进一步。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        "#1011F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #156
        0x101,
        "#1004F#6P#4S哎哎！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4243")
    TurnDirection(0x103, 0x10A, 400)

    label("loc_4243")


    ChrTalk(    #157
        0x103,
        (
            "#023F等、等等……\x01",
            "你怎么突然这么说！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x103, 400)

    ChrTalk(    #158
        0x10A,
        (
            "#812F前辈，请不要阻止我！\x02\x03",

            "我可是认真的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x103,
        "#025F认、认真……（晕眩中）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x106,
        "#552F（真是的，在想什么啊……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_42FE")
    TurnDirection(0x10A, 0x103, 400)
    Jump("loc_430C")

    label("loc_42FE")

    TurnDirection(0x10A, 0x106, 400)
    TurnDirection(0x103, 0x106, 400)

    label("loc_430C")


    ChrTalk(    #161
        0x10A,
        (
            "#1311F那个，我虽然比艾丝蒂尔\x01",
            "年长两岁……\x02\x03",

            "不过应该算是\x01",
            "同辈的游击士。\x02\x03",

            "#1314F而且这种事\x01",
            "年龄也不是问题……\x02\x03",

            "所以……你觉得怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        (
            "#1008F#6P那、那个……！\x02\x03",

            "#1013F我、我虽然很高兴，\x01",
            "不过还是感觉有点那个～吃惊！\x02\x03",

            "而且我还有约修亚，\x01",
            "不管从哪方面说也都不太方便吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10A,
        (
            "#814F约修亚？\x02\x03",

            "我和艾丝蒂尔成为\x01",
            "竞争对手，\x01",
            "有什么不方便的？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    OP_63(0x103)
    OP_63(0x106)

    ChrTalk(    #164
        0x101,
        (
            "#1004F#6P……………………\x01",
            "…………竞争对手？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x10A,
        (
            "#811F嗯嗯。\x01",
            "#816F年龄接近、武艺相当。\x02\x03",

            "我想彼此要是能\x01",
            "互相切磋和勉励就好了……\x02\x03",

            "#1316F是不是……给你添麻烦了？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #166
        0x101,
        (
            "#1016F#6P啊、啊哈哈……\x01",
            "原来是这个意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x103,
        (
            "#025F唉……\x01",
            "还是一样地让人摸不着头脑。\x02\x03",

            "真没想到是这么回事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x10A,
        "#814F？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#1012F#6P嗯……\x01",
            "不过，如果是这样的话。\x02\x03",

            "#1006F不成器的艾丝蒂尔·布莱特，\x01",
            "虽然初出茅庐……\x02\x03",

            "#1018F不过还是非常愿意\x01",
            "把亚妮拉丝当作竞争对手!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x10A,
        (
            "#811F太好了！\x02\x03",

            "#1310F总之就是看哪一方先赶上\x01",
            "前辈们的竞争⊙\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        (
            "#1006F#6P正合我意！\x02\x03",

            "我绝对不会输！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x103,
        (
            "#027F呵呵……真拿你们没办法。\x02\x03",

            "看来我们也\x01",
            "不能松懈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x106,
        (
            "#051F嘿嘿，没错。\x02\x03",

            "没有比初生的牛犊\x01",
            "更可怕的了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #174
        (
            "\x07\x05前往洛连特的定期飞船\x01",
            "『赛希莉亚号』即将升空。\x02\x03",

            "需要乘坐的旅客请立即登船。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrFlags(0x10A, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4A0E")

    ChrTalk(    #175
        0x106,
        "#052F哟，时间已经到了啊。\x02",
    )

    CloseMessageWindow()

    def lambda_47F6():
        OP_6D(82810, 1580, 137840, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_47F6)

    def lambda_480E():
        OP_67(0, 6980, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_480E)

    def lambda_4826():
        OP_6B(3130, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4826)
    OP_8C(0x106, 180, 400)

    def lambda_483D():
        OP_8E(0x106, 0x14334, 0x6A4, 0x21F2A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_483D)
    Sleep(500)
    OP_8C(0x10A, 180, 400)

    def lambda_4864():
        OP_8E(0x10A, 0x1438E, 0x5DC, 0x20F9E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_4864)

    def lambda_487F():
        OP_8E(0x101, 0x14622, 0x5DC, 0x22DD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_487F)
    Sleep(200)

    def lambda_489F():
        OP_8E(0x103, 0x14280, 0x5DC, 0x22DD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_489F)
    WaitChrThread(0x106, 0x1)

    def lambda_48BF():
        OP_8E(0x106, 0x146C2, 0x60E, 0x20904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_48BF)
    Sleep(1000)

    def lambda_48DF():
        OP_8E(0x106, 0x145C8, 0x60E, 0x20B70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_48DF)

    def lambda_48FA():
        OP_8E(0x10A, 0x1428A, 0x60E, 0x20B34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_48FA)
    WaitChrThread(0x106, 0x1)
    TurnDirection(0x106, 0x101, 500)
    WaitChrThread(0x10A, 0x1)

    def lambda_4926():
        OP_8E(0x10A, 0x14244, 0x60E, 0x2097C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_4926)
    WaitChrThread(0x10A, 0x1)
    TurnDirection(0x10A, 0x101, 500)
    Sleep(500)

    ChrTalk(    #176
        0x106,
        (
            "#051F#6P那么再见了。\x02\x03",

            "我们彼此如果有什么新动向，\x01",
            "都要通过协会支部\x01",
            "进行联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x103,
        "#020F#2P嗯，我知道了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1018F#1P再见！\x01",
            "阿加特、亚妮拉丝！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x10A,
        (
            "#811F#4P嗯！\x01",
            "艾丝蒂尔你们也要保重！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C56")

    label("loc_4A0E")


    ChrTalk(    #180
        0x103,
        "#023F哎呀，时间已经到了啊。\x02",
    )

    CloseMessageWindow()

    def lambda_4A35():
        OP_6D(82810, 1580, 137840, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A35)

    def lambda_4A4D():
        OP_67(0, 6980, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A4D)

    def lambda_4A65():
        OP_6B(3130, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4A65)
    OP_8C(0x103, 180, 400)

    def lambda_4A7C():
        OP_8E(0x103, 0x14334, 0x6A4, 0x21F2A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4A7C)
    Sleep(500)
    OP_8C(0x10A, 180, 400)

    def lambda_4AA3():
        OP_8E(0x10A, 0x1438E, 0x5DC, 0x20F9E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_4AA3)

    def lambda_4ABE():
        OP_8E(0x101, 0x14622, 0x5DC, 0x22DD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4ABE)
    Sleep(200)

    def lambda_4ADE():
        OP_8E(0x106, 0x14280, 0x5DC, 0x22DD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_4ADE)
    WaitChrThread(0x106, 0x1)

    def lambda_4AFE():
        OP_8E(0x103, 0x146C2, 0x60E, 0x20904, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4AFE)
    Sleep(1000)

    def lambda_4B1E():
        OP_8E(0x103, 0x145C8, 0x60E, 0x20B70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4B1E)

    def lambda_4B39():
        OP_8E(0x10A, 0x1428A, 0x60E, 0x20B34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_4B39)
    WaitChrThread(0x103, 0x1)
    TurnDirection(0x103, 0x101, 500)
    WaitChrThread(0x10A, 0x1)

    def lambda_4B65():
        OP_8E(0x10A, 0x14244, 0x60E, 0x2097C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_4B65)
    WaitChrThread(0x10A, 0x1)
    TurnDirection(0x10A, 0x101, 500)
    Sleep(500)

    ChrTalk(    #181
        0x103,
        (
            "#020F#6P那么要跟你们两个说再见了。\x02\x03",

            "我们彼此如果有什么新动向，\x01",
            "都要通过协会支部\x01",
            "进行联络。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x106,
        "#051F#2P嗯，明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#1018F#1P再见！\x01",
            "雪拉姐、亚妮拉丝！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x10A,
        (
            "#811F#4P嗯！\x01",
            "艾丝蒂尔你们也要保重！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C56")

    Sleep(100)
    Fade(1000)
    SetChrFlags(0x10A, 0x8)
    SetChrFlags(0xF8, 0x8)
    OP_6D(82160, 1700, 131180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3430, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x28, 0x4)
    SetChrFlags(0x28, 0x40)
    SetChrFlags(0x29, 0x4)
    SetChrFlags(0x29, 0x40)
    OP_A1(0x28, 0xB)
    OP_A1(0x29, 0xA)
    OP_72(0xB, 0x4)
    OP_72(0xA, 0x4)
    SetChrPos(0x28, 87000, -5200, 130500, 90)
    SetChrPos(0x29, 87000, -5200, 130500, 90)
    OP_0D()
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x64)
    Sleep(3000)
    OP_6F(0xA, 2)
    OP_70(0xA, 0x64)
    OP_22(0x76, 0x0, 0x64)
    OP_73(0xA)
    OP_8C(0x101, 145, 0)
    OP_8C(0xF7, 145, 0)
    OP_23(0x75)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xA, 100)
    OP_6F(0xB, 100)
    OP_70(0xA, 0xC8)
    OP_70(0xB, 0xC8)
    OP_73(0xB)
    OP_6F(0xA, 200)
    OP_6F(0xB, 200)
    OP_70(0xA, 0x12C)
    OP_70(0xB, 0x12C)

    def lambda_4D77():
        OP_8F(0xFE, 0x186A0, 0x1F4, 0x20026, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_4D77)

    def lambda_4D92():
        OP_8F(0xFE, 0x186A0, 0x1F4, 0x20026, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_4D92)
    Sleep(1000)
    Fade(1000)
    OP_6D(91460, 1500, 134290, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(6440, 0)
    OP_6C(146000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x29, 0x1)
    Fade(1000)
    OP_6D(108820, 1500, 134250, 0)
    OP_67(0, 9790, -10000, 0)
    OP_6B(7800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)

    def lambda_4E3B():
        OP_8F(0xFE, 0x2450E, 0x5DC, 0x20026, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 3, lambda_4E3B)

    def lambda_4E56():
        OP_8F(0xFE, 0x2450E, 0x5DC, 0x20026, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 3, lambda_4E56)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    WaitChrThread(0x29, 0x3)
    OP_0D()
    OP_23(0x77)
    OP_72(0x9, 0x4)
    Sleep(1000)
    SetChrPos(0x101, 83630, 1500, 142960, 270)
    SetChrPos(0xF7, 82000, 1500, 142960, 90)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5056")

    ChrTalk(    #185
        0x101,
        (
            "#1011F#5P那么……\x02\x03",

            "我们办好登船手续，\x01",
            "然后等待去卢安的船着陆吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x103,
        (
            "#026F是啊，反方向的船\x01",
            "也快来了……\x02\x03",

            "#020F隔了一个月没来，\x01",
            "要不先回王都买点东西？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        (
            "#1016F#5P啊，不用了不用了。\x01",
            "在卢安也能买东西。\x02\x03",

            "#1006F赶紧办理登船手续吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x103,
        (
            "#021F呵呵，知道了。\x02\x03",

            "#020F船票在飞船公社的\x01",
            "等候厅就能够买到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        "#1006F#5P嗯，明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5228")

    label("loc_5056")


    ChrTalk(    #190
        0x101,
        (
            "#1000F#5P那么……\x02\x03",

            "我们办好登船手续，\x01",
            "然后等去卢安的船吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x106,
        (
            "#051F对了，反方向的\x01",
            "定期船也快到达了吧。\x02\x03",

            "不过你离开都一个月了，\x01",
            "想不想买点东西？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#1011F#5P嗯～确实\x01",
            "想去逛逛百货商店什么的。\x02\x03",

            "阿加特你怎么想？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x106,
        (
            "#051F我无所谓的。\x02\x03",

            "打扮什么的\x01",
            "是女人的需要。\x02\x03",

            "你来决定吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        (
            "#1016F#5P这样啊……嘿嘿。\x02\x03",

            "#1015F嗯，这样啊。\x01",
            "在卢安也能买东西……\x02\x03",

            "#1006F赶紧办理登船手续吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x106,
        (
            "#051F是吗？明白了。\x02\x03",

            "船票在飞船公社的\x01",
            "等候厅能够买到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#1006F#5P嗯，明白。\x02",
    )

    CloseMessageWindow()

    label("loc_5228")

    Sleep(100)
    OP_A2(0x1202)
    OP_28(0x81, 0x4, 0x2)
    OP_28(0x81, 0x4, 0x8)
    OP_28(0x81, 0x1, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_525C")
    OP_28(0x81, 0x1, 0x8)
    OP_28(0x81, 0x1, 0x10)
    OP_28(0x81, 0x1, 0x20)
    Jump("loc_5275")

    label("loc_525C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5275")
    OP_28(0x81, 0x1, 0x1)
    OP_28(0x81, 0x1, 0x2)
    OP_28(0x81, 0x1, 0x4)

    label("loc_5275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5285")
    RemoveParty(0x9, 0xFF)
    RemoveParty(0x5, 0xFF)
    Jump("loc_528B")

    label("loc_5285")

    RemoveParty(0x9, 0xFF)
    RemoveParty(0x2, 0xFF)

    label("loc_528B")

    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x19, 0x10)
    SetChrFlags(0x1A, 0x10)
    SetChrFlags(0x1C, 0x10)
    SetChrPos(0x9, 61450, -3000, 162010, 6)
    SetChrPos(0xA, 61450, -3000, 163810, 180)
    EventEnd(0x0)
    SetMapFlags(0x1)
    ClearMapFlags(0x80)
    Return()

    # Function_38_3743 end

    def Function_39_5319(): pass

    label("Function_39_5319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54C8")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 4)), scpexpr(EXPR_END)), "loc_53CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5383")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #197
        0x106,
        (
            "#050F怎么了？你要去城里？\x02\x03",

            "乘船手续可以在\x01",
            "公社外的柜台处办理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53CA")

    label("loc_5383")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #198
        0x103,
        (
            "#020F咦？你要去城里？\x02\x03",

            "乘船手续可以在\x01",
            "公社外的柜台处办理。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53CA")

    Jump("loc_54AD")

    label("loc_53CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5442")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #199
        0x106,
        (
            "#052F怎么？还是\x01",
            "想在城里买东西吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #200
        0x101,
        (
            "#1016F啊，不是的。\x02\x03",

            "#1006F赶快去等候厅\x01",
            "买票吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54AD")

    label("loc_5442")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #201
        0x103,
        (
            "#023F咦？你还是\x01",
            "想在城里买东西吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #202
        0x101,
        (
            "#1016F啊，不是的。\x02\x03",

            "#1006F赶快去等候厅\x01",
            "买票吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54AD")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_54C8")

    Return()

    # Function_39_5319 end

    def Function_40_54C9(): pass

    label("Function_40_54C9")

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
        (0, "loc_5543"),
        (1, "loc_5549"),
        (SWITCH_DEFAULT, "loc_554F"),
    )


    label("loc_5543")

    OP_A2(0x1200)
    Jump("loc_554F")

    label("loc_5549")

    OP_A2(0x1201)
    Jump("loc_554F")

    label("loc_554F")

    Return()

    # Function_40_54C9 end

    def Function_41_5550(): pass

    label("Function_41_5550")

    ClearMapFlags(0x1)
    OP_6D(12790, 0, 144090, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_558F")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_55A9")

    label("loc_558F")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_55A9")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_41_5550 end

    def Function_42_55C9(): pass

    label("Function_42_55C9")

    ClearMapFlags(0x1)
    OP_6D(12790, 0, 144090, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_560E")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_562E")

    label("loc_560E")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)

    label("loc_562E")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_42_55C9 end

    def Function_43_564E(): pass

    label("Function_43_564E")

    Sleep(2000)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x3E8)
    Return()

    # Function_43_564E end

    def Function_44_5669(): pass

    label("Function_44_5669")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #203
        (
            "\x07\x05定期船飞船坪\x01",
            "≡　前往洛连特市\x01",
            "≡　前往蔡斯市\x01",
            "≡　去卡尔瓦德共和国\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #204
        (
            "\x07\x05※请勿携带易燃物和危险品\x01",
            "　　　　『利贝尔飞船公社』\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_44_5669 end

    def Function_45_5716(): pass

    label("Function_45_5716")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #205
        (
            "\x07\x05　　　飞船坪塔台　　　　\x01",
            "　※无关人员禁止入内　　\x01",
            "   『利贝尔飞船公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_45_5716 end

    SaveToFile()

Try(main)
