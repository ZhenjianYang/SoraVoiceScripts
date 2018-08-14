from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0700   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0700.x',
        MapIndex            = 9,
        MapDefaultBGM       = "ed60010",
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
        '艾丝蒂尔',                             # 9
        '约修亚',                               # 10
        '卡西乌斯',                             # 11
        '阿兰',                                 # 12
        '赛希莉亚号',                           # 13
        '赛希莉亚号影',                         # 14
        '雪拉扎德',                             # 15
        '鲁克',                                 # 16
        '帕特',                                 # 17
        '克露莎',                               # 18
        '爱娜',                                 # 19
        '伊莉莎',                               # 20
        '缇欧',                                 # 21
        '斯蒂娜',                               # 22
        '埃尔格',                               # 23
        '迪拜恩教区长',                         # 24
        '克劳斯市长',                           # 25
        '利吉',                                 # 26
        '里农',                                 # 27
        '基蒂',                                 # 28
        '布露姆老奶奶',                         # 29
        '菲特 ',                                # 30
        '尤妮',                                 # 31
        '梅尔达斯',                             # 32
        '佛莱迪',                               # 33
        '潘杜老人',                             # 34
        '德瑟鲁',                               # 35
        '托露塔',                               # 36
        '加通老大',                             # 37
        '阿鲁姆',                               # 38
        '艾娅莉',                               # 39
        '伊娜',                                 # 40
        '安莉尔',                               # 41
        '福克纳',                               # 42
        '玛茜婆婆',                             # 43
        '威诺',                                 # 44
        '拉欧老人',                             # 45
        '弗兰兹',                               # 46
        '汉娜',                                 # 47
        '查儿',                                 # 48
        '维鲁',                                 # 49
        '目标用照相机',                         # 50
        '',                                     # 51
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
        'ED6_DT27/CH03000 ._CH',             # 00
        'ED6_DT27/CH03200 ._CH',             # 01
        'ED6_DT07/CH02000 ._CH',             # 02
        'ED6_DT07/CH00020 ._CH',             # 03
        'ED6_DT07/CH01160 ._CH',             # 04
        'ED6_DT07/CH01060 ._CH',             # 05
        'ED6_DT07/CH01070 ._CH',             # 06
        'ED6_DT07/CH02560 ._CH',             # 07
        'ED6_DT07/CH02490 ._CH',             # 08
        'ED6_DT07/CH02480 ._CH',             # 09
        'ED6_DT07/CH01690 ._CH',             # 0A
        'ED6_DT07/CH01680 ._CH',             # 0B
        'ED6_DT07/CH01400 ._CH',             # 0C
        'ED6_DT07/CH02350 ._CH',             # 0D
        'ED6_DT07/CH01760 ._CH',             # 0E
        'ED6_DT07/CH01040 ._CH',             # 0F
        'ED6_DT07/CH01770 ._CH',             # 10
        'ED6_DT07/CH01010 ._CH',             # 11
        'ED6_DT07/CH01020 ._CH',             # 12
        'ED6_DT07/CH01170 ._CH',             # 13
        'ED6_DT07/CH01000 ._CH',             # 14
        'ED6_DT07/CH01250 ._CH',             # 15
        'ED6_DT07/CH01280 ._CH',             # 16
        'ED6_DT07/CH01130 ._CH',             # 17
        'ED6_DT07/CH01530 ._CH',             # 18
        'ED6_DT07/CH01140 ._CH',             # 19
        'ED6_DT07/CH01150 ._CH',             # 1A
        'ED6_DT07/CH01030 ._CH',             # 1B
        'ED6_DT27/CH03880 ._CH',             # 1C
        'ED6_DT07/CH01270 ._CH',             # 1D
        'ED6_DT07/CH01110 ._CH',             # 1E
        'ED6_DT07/CH01560 ._CH',             # 1F
        'ED6_DT07/CH01020 ._CH',             # 20
        'ED6_DT07/CH01290 ._CH',             # 21
    )

    AddCharChipPat(
        'ED6_DT27/CH03000P._CP',             # 00
        'ED6_DT27/CH03200P._CP',             # 01
        'ED6_DT07/CH02000P._CP',             # 02
        'ED6_DT07/CH00020P._CP',             # 03
        'ED6_DT07/CH01160P._CP',             # 04
        'ED6_DT07/CH01060P._CP',             # 05
        'ED6_DT07/CH01070P._CP',             # 06
        'ED6_DT07/CH02560P._CP',             # 07
        'ED6_DT07/CH02490P._CP',             # 08
        'ED6_DT07/CH02480P._CP',             # 09
        'ED6_DT07/CH01690P._CP',             # 0A
        'ED6_DT07/CH01680P._CP',             # 0B
        'ED6_DT07/CH01400P._CP',             # 0C
        'ED6_DT07/CH02350P._CP',             # 0D
        'ED6_DT07/CH01760P._CP',             # 0E
        'ED6_DT07/CH01040P._CP',             # 0F
        'ED6_DT07/CH01770P._CP',             # 10
        'ED6_DT07/CH01010P._CP',             # 11
        'ED6_DT07/CH01020P._CP',             # 12
        'ED6_DT07/CH01170P._CP',             # 13
        'ED6_DT07/CH01000P._CP',             # 14
        'ED6_DT07/CH01250P._CP',             # 15
        'ED6_DT07/CH01280P._CP',             # 16
        'ED6_DT07/CH01130P._CP',             # 17
        'ED6_DT07/CH01530P._CP',             # 18
        'ED6_DT07/CH01140P._CP',             # 19
        'ED6_DT07/CH01150P._CP',             # 1A
        'ED6_DT07/CH01030P._CP',             # 1B
        'ED6_DT27/CH03880P._CP',             # 1C
        'ED6_DT07/CH01270P._CP',             # 1D
        'ED6_DT07/CH01110P._CP',             # 1E
        'ED6_DT07/CH01560P._CP',             # 1F
        'ED6_DT07/CH01020P._CP',             # 20
        'ED6_DT07/CH01290P._CP',             # 21
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
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x1E1,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x1E1,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1E1,
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
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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
        NpcIndex            = 0x1E1,
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


    ScpFunction(
        "Function_0_6FA",          # 00, 0
        "Function_1_719",          # 01, 1
        "Function_2_8C7",          # 02, 2
        "Function_3_A44",          # 03, 3
        "Function_4_AA3",          # 04, 4
        "Function_5_34BF",         # 05, 5
        "Function_6_37B9",         # 06, 6
        "Function_7_3ADC",         # 07, 7
        "Function_8_609E",         # 08, 8
        "Function_9_60FE",         # 09, 9
        "Function_10_617C",        # 0A, 10
        "Function_11_61C7",        # 0B, 11
        "Function_12_6215",        # 0C, 12
        "Function_13_622A",        # 0D, 13
        "Function_14_6293",        # 0E, 14
        "Function_15_6301",        # 0F, 15
    )


    def Function_0_6FA(): pass

    label("Function_0_6FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_718")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_718")

    Return()

    # Function_0_6FA end

    def Function_1_719(): pass

    label("Function_1_719")

    OP_51(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x21, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x22, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x23, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2C, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2D, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2E, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x30, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x31, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x32, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x33, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x34, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x35, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x36, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x37, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x38, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_719 end

    def Function_2_8C7(): pass

    label("Function_2_8C7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EC")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_A2E")

    label("loc_8EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_905")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_A2E")

    label("loc_905")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91E")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_A2E")

    label("loc_91E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_937")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_A2E")

    label("loc_937")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_950")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_A2E")

    label("loc_950")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_969")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_A2E")

    label("loc_969")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_982")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_A2E")

    label("loc_982")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_A2E")

    label("loc_99B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B4")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_A2E")

    label("loc_9B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CD")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_A2E")

    label("loc_9CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E6")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_A2E")

    label("loc_9E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FF")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_A2E")

    label("loc_9FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A18")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_A2E")

    label("loc_A18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2E")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_A2E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A43")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_A2E")

    label("loc_A43")

    Return()

    # Function_2_8C7 end

    def Function_3_A44(): pass

    label("Function_3_A44")

    OP_82(0x81, 0x2)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\x65\x03\x07\x00。\x02",
    )

    Jump("loc_A7D")

    label("loc_A7D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_E3(0x4, 0x13, 0x1)
    OP_3E(0x365, 1)
    OP_64(0x0, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_3_A44 end

    def Function_4_AA3(): pass

    label("Function_4_AA3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 36140, 0, 35830, 180)
    OP_72(0x40F, 0x0)
    ExitThread()
    OP_A1(0x14, 0xF)
    SetChrPos(0x14, 56000, -3075, 35200, 0)
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_A1(0x15, 0xC)
    SetChrPos(0x15, 55800, -3070, 35000, 0)
    OP_6F(0xF, 1)
    OP_70(0xF, 0x1)
    ClearChrFlags(0x16, 0x80)
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
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 43740, 4000, 32990, 270)
    SetChrPos(0x11, 43720, 4000, 34060, 270)
    SetChrPos(0x12, 43100, 4000, 35150, 180)
    OP_71(0x40A, 0x0)
    ExitThread()
    SetChrPos(0x16, 42000, 4000, 33240, 90)
    SetChrPos(0x1A, 42090, 4000, 32280, 90)
    SetChrPos(0x1E, 40950, 4000, 31260, 45)
    SetChrPos(0x1D, 41060, 4000, 32380, 90)
    SetChrPos(0x1B, 44300, 4000, 35440, 180)
    SetChrPos(0x1C, 44300, 4000, 36700, 180)
    SetChrPos(0x1F, 40950, 4000, 34330, 90)
    SetChrPos(0x20, 40940, 4000, 33340, 90)
    SetChrPos(0x19, 42040, 4000, 34900, 135)
    SetChrPos(0x17, 42330, 4000, 31310, 45)
    SetChrPos(0x18, 43030, 4000, 30800, 0)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x2D, 42920, 4000, 39540, 180)
    SetChrPos(0x2E, 43580, 4000, 39510, 180)
    SetChrPos(0x23, 39520, 4000, 35140, 90)
    SetChrPos(0x22, 40510, 4000, 35190, 90)
    SetChrPos(0x27, 41440, 4000, 39940, 180)
    SetChrPos(0x28, 43500, 4000, 36830, 180)
    SetChrPos(0x35, 40870, 4000, 28980, 45)
    SetChrPos(0x36, 42200, 4000, 28940, 0)
    SetChrPos(0x37, 42020, 4000, 30060, 45)
    SetChrPos(0x38, 40850, 4000, 30090, 45)
    SetChrPos(0x21, 44310, 4000, 38580, 180)
    SetChrPos(0x24, 40160, 4000, 36500, 90)
    SetChrPos(0x25, 39240, 4000, 37340, 135)
    SetChrPos(0x26, 38860, 4000, 36350, 90)
    SetChrPos(0x29, 41840, 4000, 39070, 180)
    SetChrPos(0x2A, 40700, 4000, 37860, 135)
    SetChrPos(0x2B, 41440, 4000, 37460, 135)
    SetChrPos(0x2C, 39180, 4000, 38430, 135)
    SetChrPos(0x2F, 41780, 4000, 36080, 135)
    SetChrPos(0x30, 42090, 4000, 37260, 135)
    SetChrPos(0x31, 42510, 4000, 38350, 180)
    SetChrPos(0x32, 40390, 4000, 38960, 135)
    SetChrPos(0x33, 39090, 4000, 39260, 135)
    SetChrPos(0x34, 43240, 4000, 37580, 180)
    OP_C4(0x0, 0x800)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #1 op#A op#5
        "\x18\x07\x00#35A#40W――And The Last Day...#200W\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_C4(0x1, 0x800)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x75, 0x1, 0x32)
    OP_6D(33900, 6950, 10430, 0)
    OP_67(0, 7770, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(44000, 0)
    OP_6E(501, 0)
    OP_1D(0x1)

    def lambda_EFF():
        OP_6D(41200, 6950, 32130, 6000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_EFF)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10, 0x0)
    Fade(1000)
    OP_24(0x75, 0x46)
    OP_6D(43390, 4000, 34380, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(44000, 0)
    OP_6E(361, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #2
        0x10,
        (
            "#1008F#11P……大家……\x01\x02\x03",

            "#1012F谢谢你们来送行。\x02\x03",

            "居然来了这么多人，\x01",
            "真是有点吃惊呢。\x02\x03",

            "#1017F嗯，虽然事出突然……\x01",
            "不过我和约修亚\x01",
            "打算去外国了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x11,
        (
            "#1053F#5P两人一起旅行，\x01",
            "到各地去履行\x01",
            "游击士的职责。\x02\x03",

            "#1043F……大概，会是很漫长的旅程。\x02\x03",

            "因为想把大陆\x01",
            "所有的地方都周游一遍。\x02\x03",

            "#1041F不过，\x01",
            "总有一天一定会回到洛连特来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#1016F#11P嗯……\x02\x03",

            "为了让大家看到成熟的样子，\x01",
            "我们会尽自己最大的努力。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0xBF, 0x0, 0x64)
    OP_43(0x101, 0x3, 0x0, 0x6)
    Sleep(3000)
    OP_43(0x0, 0x0, 0x0, 0xF)
    OP_44(0x101, 0x3)
    Sleep(1500)

    ChrTalk(    #5
        0x12,
        (
            "#83F#5P唉，可是你们啊，\x01",
            "也不和我商量一下就决定……\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_6D(41950, 4000, 34200, 0)
    OP_67(0, 6380, -10000, 0)
    OP_6B(2320, 0)
    OP_6C(270000, 0)
    OP_6E(361, 0)
    SetChrPos(0x12, 42800, 4000, 35050, 135)
    SetChrPos(0x19, 41150, 4000, 35520, 135)

    def lambda_120C():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_120C)
    Sleep(100)

    def lambda_121F():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_121F)
    Sleep(100)
    OP_8C(0x16, 45, 400)
    Sleep(300)

    ChrTalk(    #6
        0x16,
        "#023F#5P哎呀，是这样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x12,
        (
            "#80F#11P是啊……\x01",
            "好不容易才安排出休息时间。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x11,
        (
            "#1052F#6P抱歉，父亲。\x01",
            "突然就做了决定……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#1012F#6P不过，\x01",
            "这是我们俩商量后决定的事……\x02\x03",

            "#1025F所以……如果您能给予信任，\x01",
            "我们就再开心不过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x12,
        (
            "#85F#11P嗯，既然如此我也不说什么了。\x02\x03",

            "#80F在这片广阔的大陆上，\x01",
            "做你们想做的事去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        "#1017F#6P…………嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        "#1054F#6P…………是！\x02",
    )

    CloseMessageWindow()

    def lambda_13F2():
        OP_6D(41200, 4000, 32950, 1500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_13F2)

    def lambda_140A():
        OP_6C(258000, 1500)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_140A)
    OP_8C(0x16, 90, 400)
    Sleep(100)

    def lambda_1426():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1426)
    Sleep(100)

    def lambda_1439():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1439)
    Sleep(100)

    def lambda_144C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_144C)

    def lambda_145A():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_145A)

    def lambda_1468():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x36, 1, lambda_1468)
    WaitChrThread(0x39, 0x0)
    Sleep(500)

    ChrTalk(    #13
        0x16,
        (
            "#026F#5P你们俩也是个中老手了，\x01",
            "我就不说什么琐碎的注意事项了。\x02\x03",

            "#027F……今后你们应该学习的东西，\x01",
            "应该了解的事情，\x01",
            "就靠你们自己来判断了。\x02\x03",

            "要多多锻炼自己的眼光哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        (
            "#1053F#12P是。\x01",
            "我们会铭记在心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x1A,
        (
            "#740F#5P在利贝尔内外，\x01",
            "游击士身处的环境\x01",
            "虽然有很大差距……\x02\x03",

            "#741F不过基本守则是差不多的。\x01",
            "就和教给你们的一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#1006F#6P嗯，遇到困难的时候\x01",
            "我们会想想所学的事情的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x16,
        (
            "#526F#5P呵呵，你们一定没问题。\x01",
            "因为是我教出来的学生嘛。\x02\x03",

            "#525F充满信心放手去干吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "#1041F#12P雪拉姐姐，爱娜小姐……\x02\x03",

            "#1053F一直承蒙照顾，\x01",
            "真是谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#1017F#6P嘿嘿，\x01",
            "给你们添了不少的麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x16,
        (
            "#021F#5P呵呵，别在意别在意。\x01",
            "这都是为了可爱的妹妹嘛。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x1D, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #21
        0x1D,
        (
            "#5P艾丝蒂尔，\x01",
            "注意不能喝生水哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x1D,
        (
            "#5P扣子要扣好。\x01",
            "睡前要刷牙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x1D,
        "#5P唔，还有就是……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1E, 45, 400)

    ChrTalk(    #24
        0x1E,
        "#5P喂、喂……斯蒂娜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x1E,
        (
            "#5P艾丝蒂尔\x01",
            "也不是小孩子了，\x01",
            "不用这么担心啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x1D,
        (
            "#5P听好了吗，艾丝蒂尔。\x01",
            "不好好做的话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x1D,
        "#5P#3S阿姨就会跑到你梦里哦！！#2S\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "#1054F#12P哈哈哈……\x01",
            "这还真没法当玩笑呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #29
        0x10,
        "#1016F#6P我、我会注意的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1E, 90, 400)

    ChrTalk(    #30
        0x1E,
        "#5P约修亚，艾丝蒂尔就拜托你了哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x1E,
        (
            "#5P还有……我们家的兼职\x01",
            "一直都为你空着哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x1E,
        "#5P明白吗，一定要回来哦！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 225, 400)
    Sleep(300)

    ChrTalk(    #33
        0x11,
        (
            "#1053F#12P……好。\x02\x03",

            "#1041F叔叔，阿姨，\x01",
            "请你们保重。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1B, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #34
        0x1B,
        (
            "#11P呜，呜……\x01",
            "呜～，艾丝蒂尔～～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x1B,
        (
            "#11P可、可千万不能，\x01",
            "忘了我哦～～。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A7E():
        OP_6D(42850, 4000, 35770, 1500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_1A7E)

    def lambda_1A96():
        OP_6C(305000, 1500)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_1A96)

    def lambda_1AA6():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1AA6)
    Sleep(100)

    def lambda_1AB9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1AB9)
    Sleep(100)

    def lambda_1ACC():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1ACC)
    Sleep(100)
    WaitChrThread(0x39, 0x0)

    def lambda_1AE4():
        OP_8F(0xFE, 0xAD0C, 0xFA0, 0x8D68, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_1AE4)
    WaitChrThread(0x1C, 0x0)
    Sleep(300)

    ChrTalk(    #36
        0x1C,
        "#11P啊啊，好了，不哭不哭。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "#1016F#6P哈、哈哈……\x02\x03",

            "#1017F等安顿下来，\x01",
            "一定马上给你写信。\x02\x03",

            "缇欧……\x01",
            "伊莉莎就拜托你照顾了哦。\x02",
        )
    )

    Jump("loc_1BAF")

    label("loc_1BAF")

    CloseMessageWindow()

    ChrTalk(    #38
        0x1C,
        "#11P好的好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x1C,
        (
            "#11P……艾丝蒂尔也是，\x01",
            "一定要好好\x01",
            "抓紧约修亚哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        "#1044F#5P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "#1016F#6P嘿嘿……\x01",
            "谢谢你的忠告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x38,
        (
            "#11P约修亚哥哥，\x01",
            "艾丝蒂尔姐姐……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C88():
        OP_6D(41000, 4000, 31450, 1500)
        ExitThread()

    QueueWorkItem(0x39, 0, lambda_1C88)

    def lambda_1CA0():
        OP_6C(270000, 1500)
        ExitThread()

    QueueWorkItem(0x39, 1, lambda_1CA0)

    def lambda_1CB0():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1CB0)
    Sleep(100)

    def lambda_1CC3():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1CC3)

    def lambda_1CD1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1CD1)
    WaitChrThread(0x39, 0x0)
    Sleep(300)

    ChrTalk(    #43
        0x37,
        "#1P约、约修亚……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x37,
        "#1P呜呜、呜呜呜…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x35,
        (
            "#5P哎呀，\x01",
            "我们家的双胞胎也快哭出来了。\x02",
        )
    )

    Jump("loc_1D5E")

    label("loc_1D5E")

    CloseMessageWindow()

    ChrTalk(    #46
        0x36,
        "#1P不过也没办法呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x36,
        (
            "#1P还是小婴儿的时候\x01",
            "就一直承蒙你们照顾嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        (
            "#1016F#6P啊哈哈，\x01",
            "确实差不多每天都去玩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        (
            "#1041F#12P叔叔，阿姨，\x01",
            "还有维鲁和查儿。\x02\x03",

            "#1049F…………要保重哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x38,
        "#5P嗯、嗯……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x37,
        "#1P约修亚……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(43820, 4000, 34400, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(44000, 0)
    OP_6E(361, 0)
    SetChrPos(0x19, 42040, 4000, 34900, 135)
    SetChrPos(0x12, 43100, 4000, 35150, 180)
    OP_0D()
    Sleep(500)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #52
        (
            "\x07\x05前往柏斯方向的定期船，\x01",
            "赛希莉亚号即将启航。\x02\x03",

            "请旅客立即登船。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_1F5F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1F5F)
    Sleep(100)

    def lambda_1F72():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1F72)
    Sleep(100)

    ChrTalk(    #53
        0x16,
        (
            "#524F#6P哎呀呀……\x01",
            "已经到时间了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x20,
        "#600F#6P那么，你们俩多保重。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        "#1017F#11P……嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x11,
        "#1053F#5P市长先生也要多保重。\x02",
    )

    CloseMessageWindow()

    def lambda_2027():
        OP_6D(44150, 4000, 33400, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2027)

    def lambda_203F():

        label("loc_203F")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_203F")

    QueueWorkItem2(0x16, 1, lambda_203F)

    def lambda_2050():

        label("loc_2050")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2050")

    QueueWorkItem2(0x1A, 1, lambda_2050)

    def lambda_2061():

        label("loc_2061")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2061")

    QueueWorkItem2(0x1E, 1, lambda_2061)

    def lambda_2072():

        label("loc_2072")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2072")

    QueueWorkItem2(0x1D, 1, lambda_2072)

    def lambda_2083():

        label("loc_2083")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2083")

    QueueWorkItem2(0x1B, 1, lambda_2083)

    def lambda_2094():

        label("loc_2094")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2094")

    QueueWorkItem2(0x1C, 1, lambda_2094)

    def lambda_20A5():

        label("loc_20A5")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_20A5")

    QueueWorkItem2(0x1F, 1, lambda_20A5)

    def lambda_20B6():

        label("loc_20B6")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_20B6")

    QueueWorkItem2(0x20, 1, lambda_20B6)

    def lambda_20C7():

        label("loc_20C7")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_20C7")

    QueueWorkItem2(0x19, 1, lambda_20C7)

    def lambda_20D8():

        label("loc_20D8")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_20D8")

    QueueWorkItem2(0x17, 1, lambda_20D8)

    def lambda_20E9():

        label("loc_20E9")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_20E9")

    QueueWorkItem2(0x18, 1, lambda_20E9)

    def lambda_20FA():

        label("loc_20FA")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_20FA")

    QueueWorkItem2(0x35, 1, lambda_20FA)

    def lambda_210B():

        label("loc_210B")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_210B")

    QueueWorkItem2(0x36, 1, lambda_210B)

    def lambda_211C():

        label("loc_211C")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_211C")

    QueueWorkItem2(0x37, 1, lambda_211C)

    def lambda_212D():

        label("loc_212D")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_212D")

    QueueWorkItem2(0x38, 1, lambda_212D)

    def lambda_213E():

        label("loc_213E")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_213E")

    QueueWorkItem2(0x22, 1, lambda_213E)

    def lambda_214F():

        label("loc_214F")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_214F")

    QueueWorkItem2(0x23, 1, lambda_214F)

    def lambda_2160():

        label("loc_2160")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2160")

    QueueWorkItem2(0x2F, 1, lambda_2160)

    def lambda_2171():

        label("loc_2171")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2171")

    QueueWorkItem2(0x32, 1, lambda_2171)

    def lambda_2182():

        label("loc_2182")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2182")

    QueueWorkItem2(0x26, 1, lambda_2182)

    def lambda_2193():

        label("loc_2193")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_2193")

    QueueWorkItem2(0x2A, 1, lambda_2193)

    def lambda_21A4():

        label("loc_21A4")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_21A4")

    QueueWorkItem2(0x2B, 1, lambda_21A4)
    OP_43(0x10, 0x0, 0x0, 0xA)
    OP_43(0x11, 0x0, 0x0, 0xB)
    Sleep(1000)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x12)

    ChrTalk(    #57 op#A
        0x12,
        "#82F#5P#20A…………约修亚。\x02",
    )

    Sleep(500)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x10, 0x0)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 315, 400)
    Sleep(500)

    ChrTalk(    #58
        0x12,
        "#85F#5P你已经下定决心了吗？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #59
        0x11,
        (
            "#1041F#5P…………嗯。\x02\x03",

            "#1053F父亲，我……\x01",
            "想成为约修亚·布莱特。\x02\x03",

            "为此，我打算周游大陆。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #60
        0x11,
        (
            "#1043F#12P如何才能保持自我，\x01",
            "是必须靠自己去把握的。\x02\x03",

            "对，必须自己怀有这种希望。\x02\x03",

            "#1053F我想作为约修亚·布莱特\x01",
            "而存在于此。\x02\x03",

            "我想留在艾丝蒂尔和父亲身边。\x01",
            "在这个城市的人民中间。\x01",
            "在这个温暖的世界中生活。\x02\x03",

            "#1041F所以……\x01",
            "我要再一次，\x01",
            "看清属于自己的道路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x12,
        (
            "#80F#5P…………是吗。\x02\x03",

            "#81F呵呵，\x01",
            "你现在的表情很不错嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x11,
        (
            "#1054F#12P哈哈…………\x02\x03",

            "#1053F……谢谢。\x01",
            "这是最好的夸奖。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #63
        0x10,
        (
            "#1007F#11P真是的……\x01",
            "我们家的这些男人啊。\x02\x03",

            "#1019F还是老样子，\x01",
            "只会说些只有自己明白的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #64
        0x10,
        (
            "#1006F#11P……喂喂，约修亚。\x01",
            "再不快点就把你丢下了哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #65
        0x11,
        "#1049F#6P好好。\x02",
    )

    CloseMessageWindow()

    def lambda_25D1():

        label("loc_25D1")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_25D1")

    QueueWorkItem2(0x12, 1, lambda_25D1)

    def lambda_25E2():
        OP_6D(48590, 4000, 31980, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_25E2)
    OP_8C(0x10, 90, 400)

    def lambda_2601():
        OP_8E(0xFE, 0xCF08, 0x1022, 0x7918, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2601)

    def lambda_261C():
        OP_8E(0xFE, 0xCF08, 0x1022, 0x7918, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_261C)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x16, 0x1)
    OP_44(0x1A, 0x1)
    OP_44(0x1E, 0x1)
    OP_44(0x1D, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x1C, 0x1)
    OP_44(0x1F, 0x1)
    OP_44(0x20, 0x1)
    OP_44(0x19, 0x1)
    OP_44(0x17, 0x1)
    OP_44(0x18, 0x1)
    OP_44(0x35, 0x1)
    OP_44(0x36, 0x1)
    OP_44(0x37, 0x1)
    OP_44(0x38, 0x1)
    OP_44(0x22, 0x1)
    OP_44(0x23, 0x1)
    OP_44(0x2F, 0x1)
    OP_44(0x32, 0x1)
    OP_44(0x26, 0x1)
    OP_44(0x2A, 0x1)
    OP_44(0x2B, 0x1)
    SetChrPos(0x10, 53660, 4130, 30220, 270)
    SetChrPos(0x11, 53740, 4130, 31140, 270)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    OP_72(0x40A, 0x0)
    ExitThread()
    SetChrPos(0x16, 43540, 4000, 30950, 90)
    SetChrPos(0x12, 43160, 4000, 32119, 90)
    SetChrPos(0x1A, 42790, 4000, 30400, 90)
    SetChrPos(0x17, 43600, 4000, 29910, 90)
    SetChrPos(0x18, 43220, 4000, 29340, 90)
    SetChrPos(0x19, 43940, 4000, 28350, 90)
    SetChrPos(0x1B, 42720, 4000, 32960, 90)
    SetChrPos(0x1C, 42680, 4000, 33840, 90)
    SetChrPos(0x35, 41010, 4000, 32229, 90)
    SetChrPos(0x36, 41110, 4000, 31080, 90)
    SetChrPos(0x37, 42010, 4000, 31420, 90)
    SetChrPos(0x38, 41980, 4000, 32259, 90)
    SetChrPos(0x1E, 42060, 4000, 29640, 90)
    SetChrPos(0x1D, 42230, 4000, 28560, 90)
    SetChrPos(0x1F, 40750, 4000, 30070, 90)
    SetChrPos(0x20, 40670, 4000, 29150, 90)
    SetChrPos(0x22, 41250, 4000, 33520, 90)
    SetChrPos(0x23, 41370, 4000, 34320, 90)
    SetChrPos(0x32, 40040, 4000, 34890, 90)
    SetChrPos(0x25, 42090, 4000, 34950, 90)
    SetChrPos(0x26, 43240, 4000, 34520, 90)
    SetChrPos(0x28, 43480, 4000, 36760, 90)
    SetChrPos(0x27, 43320, 4000, 37670, 90)
    SetChrPos(0x2D, 43000, 4000, 39160, 90)
    SetChrPos(0x2E, 43010, 4000, 39830, 90)
    SetChrPos(0x21, 42210, 4000, 37270, 90)
    SetChrPos(0x2F, 41020, 4000, 36130, 90)
    SetChrPos(0x30, 41820, 4000, 36360, 90)
    SetChrPos(0x33, 39660, 4000, 36180, 90)
    SetChrPos(0x2C, 39810, 4000, 37000, 90)
    SetChrPos(0x29, 40170, 4000, 38030, 90)
    SetChrPos(0x24, 41370, 4000, 38160, 90)
    SetChrPos(0x2A, 41330, 4000, 38970, 90)
    SetChrPos(0x2B, 41330, 4000, 40000, 90)
    SetChrPos(0x34, 39690, 4000, 39230, 90)
    SetChrPos(0x31, 42390, 4000, 38320, 90)
    SetChrPos(0x13, 39360, 4000, 37960, 90)
    OP_6D(46470, 3930, 32210, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(315000, 0)
    OP_6E(384, 0)
    OP_6D(46620, 4180, 31500, 0)
    OP_67(0, 3480, -10000, 0)
    OP_6B(3850, 0)
    OP_6C(283000, 0)
    OP_6E(223, 0)
    OP_6D(46380, 4140, 31540, 0)
    OP_67(0, 3450, -10000, 0)
    OP_6B(3710, 0)
    OP_6C(279000, 0)
    OP_6E(223, 0)
    SetChrPos(0x101, 52700, 4130, 30780, 0)
    SetChrFlags(0x101, 0x80)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #66
        0x10,
        "#1018F#6P那，大家再见了！\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(    #67
        0x17,
        "#5P……艾、艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x17,
        (
            "#5P下、下次见面的时候\x01",
            "我也会成为游击士的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        "#1016F#6P啊哈哈，那真是令人期待呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x17,
        "#5P啊，你没当真吧！？\x02",
    )

    CloseMessageWindow()

    def lambda_2B20():
        OP_96(0xFE, 0xAA50, 0xFA0, 0x74D6, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2B20)

    ChrTalk(    #71
        0x17,
        (
            "#5P我、我是真心\x01",
            "要当游击士的！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 0x1)
    OP_62(0x18, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)

    ChrTalk(    #72
        0x18,
        (
            "#5P还、还有我……\x01",
            "我也想当游击士！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x18,
        "#5P所以……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x11,
        "#1041F#12P嗯，我们一定会回来的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10,
        (
            "#1012F#6P鲁克，帕特。\x01",
            "下次见面就是同事了呢。\x02\x03",

            "#1006F我也很期待哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x17,
        "#5P嗯、嗯！\x02",
    )

    CloseMessageWindow()
    OP_6D(44600, 4130, 31790, 1500)
    Sleep(500)

    ChrTalk(    #77
        0x12,
        (
            "#85F#5P艾丝蒂尔，约修亚……\x01",
            "这里是你们的归处。\x02\x03",

            "#80F……别忘了哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        "#1053F#11P嗯，父亲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        "#1017F#5P一定不会忘记的。\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #80
        0x10,
        "#1018F#1P#3S我们走了！\x02",
    )

    Sleep(50)

    ChrTalk(    #81
        0x11,
        "#1041F#2P#3S我们走了！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_56(0x1)
    OP_59()
    Sleep(300)
    OP_22(0xE2, 0x0, 0x64)
    Sleep(1000)
    OP_24(0x75, 0x64)
    Sleep(1000)
    OP_22(0x78, 0x0, 0x64)
    OP_B0(0xD, 0x64)
    OP_6F(0xD, 0)
    OP_70(0xD, 0x12C)
    Sleep(1800)
    OP_22(0x76, 0x0, 0x64)
    OP_B0(0xF, 0x32)
    OP_6F(0xF, 1)
    OP_70(0xF, 0x3C)
    OP_73(0xF)
    Sleep(1000)
    OP_23(0x75)
    OP_22(0x77, 0x1, 0x64)
    Fade(500)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(45940, -5080, 40300, 0)
    OP_67(0, 9350, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(315000, 0)
    OP_6E(621, 0)
    OP_43(0x101, 0x3, 0x0, 0x5)

    def lambda_2E27():
        OP_8F(0xFE, 0xDAC0, 0xFFFFF7E5, 0x8980, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2E27)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xF, 61)
    OP_70(0xF, 0xA0)
    OP_73(0xF)
    OP_71(0x200F, 0x0)
    ExitThread()
    OP_6F(0xF, 161)
    OP_70(0xF, 0x104)
    WaitChrThread(0x14, 0x0)
    OP_0D()

    def lambda_2E72():

        label("loc_2E72")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2E72")

    QueueWorkItem2(0x12, 1, lambda_2E72)

    def lambda_2E83():

        label("loc_2E83")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2E83")

    QueueWorkItem2(0x16, 1, lambda_2E83)

    def lambda_2E94():

        label("loc_2E94")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2E94")

    QueueWorkItem2(0x1A, 1, lambda_2E94)

    def lambda_2EA5():

        label("loc_2EA5")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2EA5")

    QueueWorkItem2(0x1E, 1, lambda_2EA5)

    def lambda_2EB6():

        label("loc_2EB6")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2EB6")

    QueueWorkItem2(0x1D, 1, lambda_2EB6)

    def lambda_2EC7():

        label("loc_2EC7")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2EC7")

    QueueWorkItem2(0x1B, 1, lambda_2EC7)

    def lambda_2ED8():

        label("loc_2ED8")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2ED8")

    QueueWorkItem2(0x1C, 1, lambda_2ED8)

    def lambda_2EE9():

        label("loc_2EE9")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2EE9")

    QueueWorkItem2(0x1F, 1, lambda_2EE9)

    def lambda_2EFA():

        label("loc_2EFA")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2EFA")

    QueueWorkItem2(0x20, 1, lambda_2EFA)

    def lambda_2F0B():

        label("loc_2F0B")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2F0B")

    QueueWorkItem2(0x19, 1, lambda_2F0B)

    def lambda_2F1C():

        label("loc_2F1C")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2F1C")

    QueueWorkItem2(0x35, 1, lambda_2F1C)

    def lambda_2F2D():

        label("loc_2F2D")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2F2D")

    QueueWorkItem2(0x36, 1, lambda_2F2D)

    def lambda_2F3E():

        label("loc_2F3E")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2F3E")

    QueueWorkItem2(0x37, 1, lambda_2F3E)

    def lambda_2F4F():

        label("loc_2F4F")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2F4F")

    QueueWorkItem2(0x38, 1, lambda_2F4F)

    def lambda_2F60():

        label("loc_2F60")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2F60")

    QueueWorkItem2(0x22, 1, lambda_2F60)

    def lambda_2F71():

        label("loc_2F71")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2F71")

    QueueWorkItem2(0x23, 1, lambda_2F71)

    def lambda_2F82():

        label("loc_2F82")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2F82")

    QueueWorkItem2(0x2F, 1, lambda_2F82)

    def lambda_2F93():

        label("loc_2F93")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2F93")

    QueueWorkItem2(0x32, 1, lambda_2F93)

    def lambda_2FA4():

        label("loc_2FA4")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2FA4")

    QueueWorkItem2(0x25, 1, lambda_2FA4)

    def lambda_2FB5():

        label("loc_2FB5")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2FB5")

    QueueWorkItem2(0x26, 1, lambda_2FB5)

    def lambda_2FC6():

        label("loc_2FC6")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2FC6")

    QueueWorkItem2(0x2A, 1, lambda_2FC6)

    def lambda_2FD7():

        label("loc_2FD7")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2FD7")

    QueueWorkItem2(0x2B, 1, lambda_2FD7)

    def lambda_2FE8():

        label("loc_2FE8")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2FE8")

    QueueWorkItem2(0x34, 1, lambda_2FE8)

    def lambda_2FF9():

        label("loc_2FF9")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_2FF9")

    QueueWorkItem2(0x33, 1, lambda_2FF9)

    def lambda_300A():

        label("loc_300A")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_300A")

    QueueWorkItem2(0x31, 1, lambda_300A)

    def lambda_301B():

        label("loc_301B")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_301B")

    QueueWorkItem2(0x30, 1, lambda_301B)

    def lambda_302C():

        label("loc_302C")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_302C")

    QueueWorkItem2(0x2F, 1, lambda_302C)

    def lambda_303D():

        label("loc_303D")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_303D")

    QueueWorkItem2(0x2E, 1, lambda_303D)

    def lambda_304E():

        label("loc_304E")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_304E")

    QueueWorkItem2(0x2D, 1, lambda_304E)

    def lambda_305F():

        label("loc_305F")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_305F")

    QueueWorkItem2(0x2C, 1, lambda_305F)

    def lambda_3070():

        label("loc_3070")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_3070")

    QueueWorkItem2(0x27, 1, lambda_3070)

    def lambda_3081():

        label("loc_3081")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_3081")

    QueueWorkItem2(0x28, 1, lambda_3081)

    def lambda_3092():

        label("loc_3092")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_3092")

    QueueWorkItem2(0x29, 1, lambda_3092)

    def lambda_30A3():

        label("loc_30A3")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_30A3")

    QueueWorkItem2(0x21, 1, lambda_30A3)

    def lambda_30B4():
        OP_6D(45940, -5080, 49300, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_30B4)

    def lambda_30CC():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_30CC)

    def lambda_30E7():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_30E7)
    Sleep(200)

    def lambda_3107():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3107)

    def lambda_3122():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3122)
    Sleep(200)

    def lambda_3142():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3142)

    def lambda_315D():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_315D)
    Sleep(200)

    def lambda_317D():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_317D)

    def lambda_3198():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3198)
    Sleep(200)
    OP_43(0x17, 0x0, 0x0, 0x8)
    OP_43(0x18, 0x0, 0x0, 0x9)

    def lambda_31C6():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_31C6)

    def lambda_31E1():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_31E1)
    Sleep(200)

    def lambda_3201():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3201)

    def lambda_321C():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_321C)
    Sleep(200)

    def lambda_323C():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_323C)

    def lambda_3257():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3257)
    Sleep(200)

    def lambda_3277():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3277)

    def lambda_3292():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3292)
    Sleep(200)

    def lambda_32B2():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_32B2)

    def lambda_32CD():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_32CD)
    Sleep(200)

    def lambda_32ED():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_32ED)

    def lambda_3308():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3308)
    Sleep(200)

    def lambda_3328():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3328)

    def lambda_3343():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3343)
    Sleep(200)

    def lambda_3363():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x106738, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3363)

    def lambda_337E():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x106738, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_337E)
    Sleep(200)

    def lambda_339E():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_339E)

    def lambda_33B9():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_33B9)
    Sleep(200)

    def lambda_33D9():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_33D9)

    def lambda_33F4():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_33F4)
    Sleep(200)

    def lambda_3414():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3414)

    def lambda_342F():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_342F)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    Sleep(300)
    OP_24(0x77, 0x50)
    Sleep(300)
    OP_24(0x77, 0x46)
    Sleep(100)
    FadeToDark(2000, 0, -1)
    Sleep(200)
    OP_24(0x77, 0x3C)
    Sleep(300)
    OP_24(0x77, 0x32)
    Sleep(300)
    OP_24(0x77, 0x28)
    Sleep(300)
    OP_24(0x77, 0x1E)
    Sleep(300)
    OP_23(0x77)
    OP_0D()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0x40D, 0x0)
    ExitThread()
    SetMapFlags(0x2000000)
    OP_A2(0x250A)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_AA3 end

    def Function_5_34BF(): pass

    label("Function_5_34BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_37B8")
    OP_62(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    Sleep(100)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x2C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x2D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x2E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x2F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x31, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x26, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x29, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    Sleep(200)
    OP_62(0x32, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x33, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x34, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x35, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x36, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x37, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x38, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("Function_5_34BF")

    label("loc_37B8")

    Return()

    # Function_5_34BF end

    def Function_6_37B9(): pass

    label("Function_6_37B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3ADB")
    OP_62(0x16, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x17, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x18, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x1C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x1D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x2A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x2C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x2D, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x2E, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x2F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x31, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x25, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x26, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x19, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x1A, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x1B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x27, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x29, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x28, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    Sleep(200)
    OP_62(0x32, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x33, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x34, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x35, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x36, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x37, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x38, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x1F, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x20, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x22, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(200)
    OP_62(0x23, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jump("Function_6_37B9")

    label("loc_3ADB")

    Return()

    # Function_6_37B9 end

    def Function_7_3ADC(): pass

    label("Function_7_3ADC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 36140, 0, 35830, 180)
    OP_72(0x40F, 0x0)
    ExitThread()
    OP_A1(0x14, 0xF)
    SetChrPos(0x14, 56000, -3075, 35200, 0)
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_A1(0x15, 0xC)
    SetChrPos(0x15, 55800, -3070, 35000, 0)
    OP_6F(0xF, 1)
    OP_70(0xF, 0x1)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x16, 43310, 4000, 32130, 270)
    SetChrPos(0x1A, 43360, 4000, 30880, 270)
    SetChrPos(0x19, 43180, 4000, 28810, 270)
    SetChrPos(0x1B, 42150, 4000, 29690, 270)
    SetChrPos(0x1C, 42220, 4000, 28730, 270)
    SetChrPos(0x1D, 41020, 4000, 29970, 270)
    SetChrPos(0x1E, 41040, 4000, 29000, 270)
    SetChrPos(0x1F, 44000, 4000, 33920, 270)
    SetChrPos(0x20, 44130, 4000, 33080, 270)
    SetChrPos(0x21, 43790, 4000, 35600, 225)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    ClearChrFlags(0x32, 0x80)
    ClearChrFlags(0x33, 0x80)
    ClearChrFlags(0x34, 0x80)
    ClearChrFlags(0x35, 0x80)
    ClearChrFlags(0x36, 0x80)
    ClearChrFlags(0x37, 0x80)
    ClearChrFlags(0x38, 0x80)
    SetChrPos(0x22, 39620, 4000, 35330, 225)
    SetChrPos(0x23, 40480, 4000, 35190, 225)
    SetChrPos(0x24, 40160, 4000, 36500, 225)
    SetChrPos(0x25, 39240, 4000, 37340, 225)
    SetChrPos(0x26, 38860, 4000, 36350, 225)
    SetChrPos(0x27, 41100, 4000, 34450, 225)
    SetChrPos(0x28, 40810, 4000, 33360, 225)
    SetChrPos(0x29, 41840, 4000, 39070, 225)
    SetChrPos(0x2A, 40700, 4000, 37860, 225)
    SetChrPos(0x2B, 41440, 4000, 37460, 225)
    SetChrPos(0x2C, 39180, 4000, 38430, 225)
    SetChrPos(0x2D, 42000, 4000, 34240, 225)
    SetChrPos(0x2E, 42420, 4000, 33780, 225)
    SetChrPos(0x2F, 41780, 4000, 36080, 225)
    SetChrPos(0x30, 42090, 4000, 37260, 180)
    SetChrPos(0x31, 42510, 4000, 38350, 225)
    SetChrPos(0x32, 40390, 4000, 38960, 225)
    SetChrPos(0x33, 39090, 4000, 39260, 225)
    SetChrPos(0x34, 43240, 4000, 37580, 225)
    SetChrPos(0x35, 42100, 4000, 32540, 270)
    SetChrPos(0x36, 42120, 4000, 31510, 270)
    SetChrPos(0x37, 41020, 4000, 32100, 270)
    SetChrPos(0x38, 40820, 4000, 31060, 270)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 34900, 0, 130, 0)
    SetChrPos(0x11, 34180, 0, -860, 0)
    SetChrPos(0x12, 35160, 0, -1350, 0)

    def lambda_3E76():
        OP_8E(0xFE, 0x870A, 0x0, 0x21F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3E76)
    Sleep(100)

    def lambda_3E96():
        OP_8E(0xFE, 0x83F4, 0x0, 0x1D88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_3E96)
    Sleep(100)

    def lambda_3EB6():
        OP_8E(0xFE, 0x8840, 0x0, 0x1B94, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_3EB6)
    OP_6D(35380, 0, 11930, 0)
    OP_67(0, 7370, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(44000, 0)
    OP_6E(339, 0)

    def lambda_3F0E():
        OP_6B(2520, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3F0E)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x17, 34520, 0, 25380, 180)
    SetChrPos(0x18, 35890, 0, 25130, 180)

    def lambda_3F59():
        OP_8E(0xFE, 0x8692, 0x0, 0x3AAC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_3F59)
    Sleep(100)

    def lambda_3F79():
        OP_8E(0xFE, 0x8A5C, 0x0, 0x3A2A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3F79)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x0, 0x2)

    ChrTalk(    #82
        0x17,
        "#5P嘿嘿，终于来了啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x18,
        (
            "#2P真是的，好慢哦。\x01",
            "哥哥姐姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10,
        "#1000F#6P鲁克，帕特！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x11,
        "#1040F#4P你们来送行吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x17,
        "#5P可不只是我们哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x18,
        "#2P嗯，来这边！\x02",
    )

    CloseMessageWindow()
    OP_43(0x17, 0x0, 0x0, 0xD)
    OP_43(0x18, 0x0, 0x0, 0xE)
    Sleep(1500)

    def lambda_4076():
        OP_6D(36710, 0, 27640, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_4076)

    def lambda_408E():
        OP_67(0, 7420, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_408E)

    def lambda_40A6():
        OP_6B(2420, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_40A6)

    def lambda_40B6():
        OP_8E(0xFE, 0x8A52, 0x0, 0x6856, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_40B6)
    Sleep(150)

    def lambda_40D6():
        OP_8E(0xFE, 0x873C, 0x0, 0x637E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_40D6)
    Sleep(300)

    def lambda_40F6():
        OP_8E(0xFE, 0x8B2E, 0x0, 0x61E4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_40F6)
    WaitChrThread(0x10, 0x0)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x0, 0x0)
    Sleep(1000)

    ChrTalk(    #88
        0x10,
        "#1000F#4P啊……！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)

    ChrTalk(    #89
        0x11,
        (
            "#1040F#6P哈哈……\x02\x03",

            "……这可真厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(42400, 2000, 35220, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(44000, 0)
    OP_6E(358, 0)

    def lambda_41D2():
        OP_6D(42400, 4400, 35220, 2500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_41D2)
    OP_0D()
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #90
        0x1D,
        "#2P艾丝蒂尔，约修亚君！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x1E,
        "#2P哈哈，等好久了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x22,
        "#5P呀，你们好！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x2C,
        "#5P姑且把大家都带来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x21,
        (
            "#5P嗯嗯。\x01",
            "幸亏天气这么好呢。\x02",
        )
    )

    Jump("loc_4286")

    label("loc_4286")

    CloseMessageWindow()

    ChrTalk(    #95
        0x2D,
        "#5P我们也祝福你们！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x2E,
        "#2P呜呼呼，祝你们幸福。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x36,
        (
            "#2P真是见外啊。\x01",
            "至少要打个招呼嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x35, 0x38, 400)
    Sleep(200)

    ChrTalk(    #98
        0x35,
        "#5P喏，是约修亚他们哦。\x02",
    )

    CloseMessageWindow()
    OP_96(0x38, 0x9F74, 0x1194, 0x7954, 0x12C, 0x1770)

    ChrTalk(    #99
        0x38,
        "#2P哇ー，是艾丝蒂尔姐姐！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x37,
        "#5P约修亚……加油哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x2F,
        "#2P哎呀～，游击士～。\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #102
        0x30,
        "喵～呜。\x02",
    )

    Jump("loc_43A8")

    label("loc_43A8")

    CloseMessageWindow()
    SetChrPos(0x10, 36460, 0, 33620, 90)
    SetChrPos(0x11, 35410, 0, 33510, 90)
    SetChrPos(0x12, 35820, 0, 32360, 90)
    Sleep(300)
    Fade(500)
    OP_6D(37330, 0, 34840, 0)
    OP_67(0, 5830, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(44000, 0)
    OP_6E(358, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #103
        0x10,
        "#1000F#5P大、大家……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x11,
        (
            "#1040F#6P几、几乎\x01",
            "所有居民都来了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x12,
        "#80F#4P呼，真是包场了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x13,
        (
            "#5P好了，出航准备就绪了哦。\x02\x03",

            "乘船手续\x01",
            "还是先办好吧。\x02",
        )
    )

    Jump("loc_44DC")

    label("loc_44DC")

    CloseMessageWindow()

    def lambda_44E3():
        OP_6D(37510, 0, 36000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_44E3)

    def lambda_44FB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_44FB)
    Sleep(100)

    def lambda_450E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_450E)
    Sleep(100)
    OP_8C(0x12, 0, 400)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #107
        0x10,
        "#1000F#4P啊，阿兰先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x11,
        (
            "#1040F#6P那么，\x01",
            "赶快办手续吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x10,
        "#1000F#4P嗯。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x10, 43740, 4000, 32990, 270)
    SetChrPos(0x11, 43720, 4000, 34060, 270)
    SetChrPos(0x12, 44090, 4000, 35540, 225)
    OP_71(0x40A, 0x0)
    ExitThread()
    SetChrPos(0x16, 42000, 4000, 33240, 90)
    SetChrPos(0x1A, 42090, 4000, 32280, 90)
    SetChrPos(0x1E, 40950, 4000, 31260, 90)
    SetChrPos(0x1D, 41060, 4000, 32380, 90)
    SetChrPos(0x1B, 43100, 4000, 35150, 180)
    SetChrPos(0x1C, 42040, 4000, 34900, 135)
    SetChrPos(0x1F, 40950, 4000, 34330, 90)
    SetChrPos(0x20, 40940, 4000, 33340, 90)
    SetChrPos(0x19, 43180, 4000, 28810, 0)
    SetChrPos(0x17, 42330, 4000, 31310, 45)
    SetChrPos(0x18, 43030, 4000, 30800, 0)
    SetChrPos(0x2D, 42920, 4000, 39540, 180)
    SetChrPos(0x2E, 43580, 4000, 39510, 180)
    SetChrPos(0x23, 39520, 4000, 35140, 90)
    SetChrPos(0x22, 40510, 4000, 35190, 90)
    SetChrPos(0x27, 41440, 4000, 39940, 180)
    SetChrPos(0x28, 43500, 4000, 36830, 180)
    SetChrPos(0x35, 42020, 4000, 30060, 0)
    SetChrPos(0x36, 42200, 4000, 28940, 0)
    SetChrPos(0x37, 40850, 4000, 30090, 45)
    SetChrPos(0x38, 40870, 4000, 28980, 45)
    SetChrPos(0x21, 44310, 4000, 38580, 180)
    SetChrPos(0x24, 40160, 4000, 36500, 90)
    SetChrPos(0x25, 39240, 4000, 37340, 135)
    SetChrPos(0x26, 38860, 4000, 36350, 90)
    SetChrPos(0x29, 41840, 4000, 39070, 180)
    SetChrPos(0x2A, 40700, 4000, 37860, 135)
    SetChrPos(0x2B, 41440, 4000, 37460, 135)
    SetChrPos(0x2C, 39180, 4000, 38430, 135)
    SetChrPos(0x2F, 41780, 4000, 36080, 135)
    SetChrPos(0x30, 42090, 4000, 37260, 135)
    SetChrPos(0x31, 42510, 4000, 38350, 180)
    SetChrPos(0x32, 40390, 4000, 38960, 135)
    SetChrPos(0x33, 39090, 4000, 39260, 135)
    SetChrPos(0x34, 43240, 4000, 37580, 180)
    OP_6D(43390, 4000, 34380, 0)
    OP_67(0, 6110, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(44000, 0)
    OP_6E(361, 0)
    OP_22(0x75, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #110
        0x10,
        (
            "#1000F#2P各位，谢谢你们来送行。\x02\x03",

            "居然来了这么多人\x01",
            "真是有点吃惊呢。\x02\x03",

            "嗯，虽然事出突然……\x01",
            "不过我和约修亚\x01",
            "我们决定去帝国了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x11,
        (
            "#1040F#5P打算一边履行协会的职责，\x01",
            "一边在帝国边境旅行。\x02\x03",

            "并不是因为\x01",
            "有什么特别的任务，\x01",
            "请不必担心。\x02\x03",

            "所以不知道今后会怎样，\x01",
            "不过我们一定会回洛连特来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10,
        (
            "#1000F#2P嗯……\x02\x03",

            "为了让大家看到成熟的样子\x01",
            "我们会尽自己最大的努力。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xBF, 0x0, 0x64)
    Sleep(3000)
    OP_43(0x0, 0x0, 0x0, 0xF)
    Sleep(200)

    ChrTalk(    #113
        0x16,
        (
            "#020F#6P呵呵，你们一定没问题的。\x02\x03",

            "充满信心放手去干吧㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x11,
        "#1040F#5P是，雪拉姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        (
            "#1000F#2P雪拉姐……\x02\x03",

            "一直承蒙你多照顾了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x16,
        (
            "#020F#6P呵呵，别摆出这种表情嘛。\x02\x03",

            "反正一定还会再见的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x10,
        "#1000F#2P……嗯、嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x1A,
        (
            "#740F#6P你们会长成什么样，\x01",
            "我很期待哦。\x02\x03",

            "路上可要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x10,
        "#1000F#2P谢谢，爱娜姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x11,
        "#1040F#5P承蒙照顾了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x1D,
        (
            "#6P艾丝蒂尔，\x01",
            "注意不能喝生水哦？\x02\x03",

            "还、还有长霉的面包\x01",
            "也绝对不能吃哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1E, 0, 400)
    Sleep(200)

    ChrTalk(    #122
        0x1E,
        (
            "#4P喂、喂……斯蒂娜。\x02\x03",

            "都不是小孩子了，\x01",
            "这点小事艾丝蒂尔\x01",
            "都知道的啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1D, 180, 400)

    ChrTalk(    #123
        0x1D,
        "#5P就、就算知道也担心啊！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1D, 90, 400)
    Sleep(200)

    ChrTalk(    #124
        0x1D,
        (
            "#6P啊啊，\x01",
            "阿姨也想跟去照顾你们啊！\x02",
        )
    )

    Jump("loc_4CA0")

    label("loc_4CA0")

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #125
        0x10,
        (
            "#1000F#2P哎、哎呀……\x01",
            "斯蒂娜阿姨真是的。\x02\x03",

            "不过，我一定会小心的。\x01",
            "毕竟是第一次去的地方嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1E, 90, 400)

    ChrTalk(    #126
        0x1D,
        (
            "#6P呜呜……\x01",
            "要健健康康的回来哦？\x02\x03",

            "约修亚君……\x01",
            "艾丝蒂尔就拜托你了哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x1E,
        "#6P啊啊，全靠你了约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x11,
        (
            "#1040F#5P是……\x02\x03",

            "阿姨你们也要多保重。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x1B,
        (
            "#5P呜、呜……\x01",
            "呜～，艾丝蒂尔～～。\x02\x03",

            "可、可千万不能，\x01",
            "忘了我哦～～。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E14():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4E14)
    Sleep(100)

    def lambda_4E27():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4E27)
    Sleep(100)
    OP_8C(0x1C, 90, 400)

    ChrTalk(    #130
        0x1C,
        (
            "#6P我、我说伊莉莎。\x01",
            "你干嘛哭这么厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x10,
        (
            "#1000F#2P哈、哈哈……\x02\x03",

            "等安顿下来，\x01",
            "一定马上给你写信哦。\x02\x03",

            "缇欧……\x01",
            "伊莉莎就拜托你照顾了哦。\x02",
        )
    )

    Jump("loc_4EE2")

    label("loc_4EE2")

    CloseMessageWindow()
    OP_8C(0x1C, 135, 400)

    ChrTalk(    #132
        0x1C,
        (
            "#6P呜，嗯……艾丝蒂尔也是。\x02\x03",

            "一定要好好\x01",
            "抓紧约修亚哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x11,
        "#1040F#2P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x10,
        (
            "#1000F#2P哎嘿嘿……\x01",
            "谢谢你的忠告。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x20,
        "#600F#6P那么，你们俩保重了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x1F,
        (
            "#6P无论什么时候\x01",
            "也绝对不能迷失自我哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4FC5():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4FC5)
    Sleep(100)
    OP_8C(0x10, 270, 400)

    ChrTalk(    #137
        0x11,
        (
            "#1040F#5P市长先生，教区长先生……\x02\x03",

            "之前也给你们两人\x01",
            "真是谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x10,
        (
            "#1000F#2P嗯……\x01",
            "要多多保重哦。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #139
        (
            "\x07\x05前往柏斯方向的定期船，\x01",
            "赛希莉亚号即将升空。\x02\x03",

            "需要乘坐的旅客请立即登艇。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #140
        0x10,
        "#1000F#2P啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 400)
    Sleep(300)

    ChrTalk(    #141
        0x12,
        "#80F#5P唔，差不多到时间了吗。\x02",
    )

    CloseMessageWindow()

    def lambda_511E():
        OP_6D(45030, 4000, 35310, 1500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_511E)
    OP_8C(0x11, 0, 400)
    OP_8C(0x10, 0, 400)
    WaitChrThread(0x0, 0x0)

    ChrTalk(    #142
        0x11,
        "#1040F#6P那么，爸爸……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x12,
        "#80F#5P啊啊，去吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x10,
        "#1000F#4P……嗯，那么再见了。\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    def lambda_51AD():
        OP_6D(48590, 4000, 31980, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_51AD)
    OP_43(0x10, 0x0, 0x0, 0xA)
    OP_43(0x11, 0x0, 0x0, 0xB)

    def lambda_51D3():

        label("loc_51D3")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_51D3")

    QueueWorkItem2(0x12, 1, lambda_51D3)

    def lambda_51E4():

        label("loc_51E4")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_51E4")

    QueueWorkItem2(0x16, 1, lambda_51E4)

    def lambda_51F5():

        label("loc_51F5")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_51F5")

    QueueWorkItem2(0x1A, 1, lambda_51F5)

    def lambda_5206():

        label("loc_5206")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_5206")

    QueueWorkItem2(0x1E, 1, lambda_5206)

    def lambda_5217():

        label("loc_5217")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_5217")

    QueueWorkItem2(0x1D, 1, lambda_5217)

    def lambda_5228():

        label("loc_5228")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_5228")

    QueueWorkItem2(0x1B, 1, lambda_5228)

    def lambda_5239():

        label("loc_5239")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_5239")

    QueueWorkItem2(0x1C, 1, lambda_5239)

    def lambda_524A():

        label("loc_524A")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_524A")

    QueueWorkItem2(0x1F, 1, lambda_524A)

    def lambda_525B():

        label("loc_525B")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_525B")

    QueueWorkItem2(0x20, 1, lambda_525B)

    def lambda_526C():

        label("loc_526C")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_526C")

    QueueWorkItem2(0x19, 1, lambda_526C)

    def lambda_527D():

        label("loc_527D")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_527D")

    QueueWorkItem2(0x17, 1, lambda_527D)

    def lambda_528E():

        label("loc_528E")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_528E")

    QueueWorkItem2(0x18, 1, lambda_528E)

    def lambda_529F():

        label("loc_529F")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_529F")

    QueueWorkItem2(0x35, 1, lambda_529F)

    def lambda_52B0():

        label("loc_52B0")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_52B0")

    QueueWorkItem2(0x36, 1, lambda_52B0)

    def lambda_52C1():

        label("loc_52C1")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_52C1")

    QueueWorkItem2(0x37, 1, lambda_52C1)

    def lambda_52D2():

        label("loc_52D2")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_52D2")

    QueueWorkItem2(0x38, 1, lambda_52D2)

    def lambda_52E3():

        label("loc_52E3")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_52E3")

    QueueWorkItem2(0x22, 1, lambda_52E3)

    def lambda_52F4():

        label("loc_52F4")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_52F4")

    QueueWorkItem2(0x23, 1, lambda_52F4)

    def lambda_5305():

        label("loc_5305")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_5305")

    QueueWorkItem2(0x2F, 1, lambda_5305)

    def lambda_5316():

        label("loc_5316")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_5316")

    QueueWorkItem2(0x32, 1, lambda_5316)

    def lambda_5327():

        label("loc_5327")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_5327")

    QueueWorkItem2(0x26, 1, lambda_5327)

    def lambda_5338():

        label("loc_5338")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_5338")

    QueueWorkItem2(0x2A, 1, lambda_5338)

    def lambda_5349():

        label("loc_5349")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_5349")

    QueueWorkItem2(0x2B, 1, lambda_5349)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x1)
    OP_44(0x16, 0x1)
    OP_44(0x1A, 0x1)
    OP_44(0x1E, 0x1)
    OP_44(0x1D, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x1C, 0x1)
    OP_44(0x1F, 0x1)
    OP_44(0x20, 0x1)
    OP_44(0x19, 0x1)
    OP_44(0x17, 0x1)
    OP_44(0x18, 0x1)
    OP_44(0x35, 0x1)
    OP_44(0x36, 0x1)
    OP_44(0x37, 0x1)
    OP_44(0x38, 0x1)
    OP_44(0x22, 0x1)
    OP_44(0x23, 0x1)
    OP_44(0x2F, 0x1)
    OP_44(0x32, 0x1)
    OP_44(0x26, 0x1)
    OP_44(0x2A, 0x1)
    OP_44(0x2B, 0x1)
    SetChrPos(0x10, 53660, 4130, 30220, 270)
    SetChrPos(0x11, 53740, 4130, 31140, 270)
    SetChrSubChip(0x10, 0)
    SetChrSubChip(0x11, 0)
    OP_72(0x40A, 0x0)
    ExitThread()
    SetChrPos(0x16, 43540, 4000, 30950, 90)
    SetChrPos(0x12, 43160, 4000, 32119, 90)
    SetChrPos(0x1A, 42790, 4000, 30400, 90)
    SetChrPos(0x17, 43600, 4000, 29910, 90)
    SetChrPos(0x18, 43220, 4000, 29340, 90)
    SetChrPos(0x19, 43940, 4000, 28350, 90)
    SetChrPos(0x1B, 42720, 4000, 32960, 90)
    SetChrPos(0x1C, 42680, 4000, 33840, 90)
    SetChrPos(0x35, 41010, 4000, 32229, 90)
    SetChrPos(0x36, 41110, 4000, 31080, 90)
    SetChrPos(0x37, 42010, 4000, 31420, 90)
    SetChrPos(0x38, 41980, 4000, 32259, 90)
    SetChrPos(0x1E, 42060, 4000, 29640, 90)
    SetChrPos(0x1D, 42230, 4000, 28560, 90)
    SetChrPos(0x1F, 40750, 4000, 30070, 90)
    SetChrPos(0x20, 40670, 4000, 29150, 90)
    SetChrPos(0x22, 41250, 4000, 33520, 90)
    SetChrPos(0x23, 41370, 4000, 34320, 90)
    SetChrPos(0x32, 40040, 4000, 34890, 90)
    SetChrPos(0x25, 42090, 4000, 34950, 90)
    SetChrPos(0x26, 43240, 4000, 34520, 90)
    SetChrPos(0x28, 43480, 4000, 36760, 90)
    SetChrPos(0x27, 43320, 4000, 37670, 90)
    SetChrPos(0x2D, 43000, 4000, 39160, 90)
    SetChrPos(0x2E, 43010, 4000, 39830, 90)
    SetChrPos(0x21, 42210, 4000, 37270, 90)
    SetChrPos(0x2F, 41020, 4000, 36130, 90)
    SetChrPos(0x30, 41820, 4000, 36360, 90)
    SetChrPos(0x33, 39660, 4000, 36180, 90)
    SetChrPos(0x2C, 39810, 4000, 37000, 90)
    SetChrPos(0x29, 40170, 4000, 38030, 90)
    SetChrPos(0x24, 41370, 4000, 38160, 90)
    SetChrPos(0x2A, 41330, 4000, 38970, 90)
    SetChrPos(0x2B, 41330, 4000, 40000, 90)
    SetChrPos(0x34, 39690, 4000, 39230, 90)
    SetChrPos(0x31, 42390, 4000, 38320, 90)
    SetChrPos(0x13, 39360, 4000, 37960, 90)
    OP_6D(46470, 3930, 32210, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(315000, 0)
    OP_6E(384, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #145
        0x10,
        "#1000F#5P那么，大家再见了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x1A,
        "#740F嗯嗯，加油哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x16,
        "#020F要保重身体哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x11,
        "#1040F#5P是，我们会小心的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x10,
        (
            "#1000F#5P雪拉姐也是……\x02\x03",

            "别喝得太多哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x16,
        (
            "#020F呵呵，\x01",
            "担心的话不如下次陪我喝啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x18,
        (
            "你们两人都要加油哦！\x01",
            "我会支持你们的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x17,
        (
            "艾丝蒂尔！\x02\x03",

            "下、下次见面的时候\x01",
            "我也会成为游击士的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x19,
        (
            "#5P要是上了《帝国时报》\x01",
            "一定要联络我哦？\x02\x03",

            "克露莎\x01",
            "一定会去看的㈱\x02",
        )
    )

    Jump("loc_5860")

    label("loc_5860")

    CloseMessageWindow()

    ChrTalk(    #154
        0x11,
        "#1040F#5P哈哈，知道啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x10,
        "#1000F#5P大家都要保重哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x12,
        (
            "#80F艾丝蒂尔，约修亚……\x02\x03",

            "……一定要回来哦。\x02\x03",

            "这里可是\x01",
            "你们的故乡啊。\x02",
        )
    )

    Jump("loc_58FD")

    label("loc_58FD")

    CloseMessageWindow()

    ChrTalk(    #157
        0x11,
        (
            "#1040F#5P嗯，爸爸……\x02\x03",

            "我们一定会回来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x10,
        (
            "#1000F#5P哎嘿嘿……\x02\x03",

            "嗯，两人一起回来。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_22(0xE2, 0x0, 0x64)
    Sleep(2000)
    OP_22(0x78, 0x0, 0x64)
    OP_B0(0xD, 0x64)
    OP_6F(0xD, 0)
    OP_70(0xD, 0x12C)
    Sleep(1800)
    OP_22(0x76, 0x0, 0x64)
    OP_B0(0xF, 0x32)
    OP_6F(0xF, 1)
    OP_70(0xF, 0x3C)
    OP_73(0xF)
    Sleep(1000)
    OP_23(0x75)
    OP_22(0x77, 0x1, 0x64)
    Fade(500)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_6D(45940, -5080, 40300, 0)
    OP_67(0, 9350, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(315000, 0)
    OP_6E(621, 0)

    def lambda_5A06():
        OP_8F(0xFE, 0xDAC0, 0xFFFFF7E5, 0x8980, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_5A06)
    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xF, 61)
    OP_70(0xF, 0xA0)
    OP_73(0xF)
    OP_71(0x200F, 0x0)
    ExitThread()
    OP_6F(0xF, 161)
    OP_70(0xF, 0x104)
    WaitChrThread(0x14, 0x0)
    OP_0D()

    def lambda_5A51():

        label("loc_5A51")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5A51")

    QueueWorkItem2(0x12, 1, lambda_5A51)

    def lambda_5A62():

        label("loc_5A62")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5A62")

    QueueWorkItem2(0x16, 1, lambda_5A62)

    def lambda_5A73():

        label("loc_5A73")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5A73")

    QueueWorkItem2(0x1A, 1, lambda_5A73)

    def lambda_5A84():

        label("loc_5A84")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5A84")

    QueueWorkItem2(0x1E, 1, lambda_5A84)

    def lambda_5A95():

        label("loc_5A95")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5A95")

    QueueWorkItem2(0x1D, 1, lambda_5A95)

    def lambda_5AA6():

        label("loc_5AA6")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5AA6")

    QueueWorkItem2(0x1B, 1, lambda_5AA6)

    def lambda_5AB7():

        label("loc_5AB7")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5AB7")

    QueueWorkItem2(0x1C, 1, lambda_5AB7)

    def lambda_5AC8():

        label("loc_5AC8")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5AC8")

    QueueWorkItem2(0x1F, 1, lambda_5AC8)

    def lambda_5AD9():

        label("loc_5AD9")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5AD9")

    QueueWorkItem2(0x20, 1, lambda_5AD9)

    def lambda_5AEA():

        label("loc_5AEA")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5AEA")

    QueueWorkItem2(0x19, 1, lambda_5AEA)

    def lambda_5AFB():

        label("loc_5AFB")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5AFB")

    QueueWorkItem2(0x35, 1, lambda_5AFB)

    def lambda_5B0C():

        label("loc_5B0C")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5B0C")

    QueueWorkItem2(0x36, 1, lambda_5B0C)

    def lambda_5B1D():

        label("loc_5B1D")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5B1D")

    QueueWorkItem2(0x37, 1, lambda_5B1D)

    def lambda_5B2E():

        label("loc_5B2E")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5B2E")

    QueueWorkItem2(0x38, 1, lambda_5B2E)

    def lambda_5B3F():

        label("loc_5B3F")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5B3F")

    QueueWorkItem2(0x22, 1, lambda_5B3F)

    def lambda_5B50():

        label("loc_5B50")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5B50")

    QueueWorkItem2(0x23, 1, lambda_5B50)

    def lambda_5B61():

        label("loc_5B61")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5B61")

    QueueWorkItem2(0x2F, 1, lambda_5B61)

    def lambda_5B72():

        label("loc_5B72")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5B72")

    QueueWorkItem2(0x32, 1, lambda_5B72)

    def lambda_5B83():

        label("loc_5B83")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5B83")

    QueueWorkItem2(0x25, 1, lambda_5B83)

    def lambda_5B94():

        label("loc_5B94")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5B94")

    QueueWorkItem2(0x26, 1, lambda_5B94)

    def lambda_5BA5():

        label("loc_5BA5")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5BA5")

    QueueWorkItem2(0x2A, 1, lambda_5BA5)

    def lambda_5BB6():

        label("loc_5BB6")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5BB6")

    QueueWorkItem2(0x2B, 1, lambda_5BB6)

    def lambda_5BC7():

        label("loc_5BC7")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5BC7")

    QueueWorkItem2(0x34, 1, lambda_5BC7)

    def lambda_5BD8():

        label("loc_5BD8")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5BD8")

    QueueWorkItem2(0x33, 1, lambda_5BD8)

    def lambda_5BE9():

        label("loc_5BE9")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5BE9")

    QueueWorkItem2(0x31, 1, lambda_5BE9)

    def lambda_5BFA():

        label("loc_5BFA")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5BFA")

    QueueWorkItem2(0x30, 1, lambda_5BFA)

    def lambda_5C0B():

        label("loc_5C0B")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5C0B")

    QueueWorkItem2(0x2F, 1, lambda_5C0B)

    def lambda_5C1C():

        label("loc_5C1C")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5C1C")

    QueueWorkItem2(0x2E, 1, lambda_5C1C)

    def lambda_5C2D():

        label("loc_5C2D")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5C2D")

    QueueWorkItem2(0x2D, 1, lambda_5C2D)

    def lambda_5C3E():

        label("loc_5C3E")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5C3E")

    QueueWorkItem2(0x2C, 1, lambda_5C3E)

    def lambda_5C4F():

        label("loc_5C4F")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5C4F")

    QueueWorkItem2(0x27, 1, lambda_5C4F)

    def lambda_5C60():

        label("loc_5C60")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5C60")

    QueueWorkItem2(0x28, 1, lambda_5C60)

    def lambda_5C71():

        label("loc_5C71")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5C71")

    QueueWorkItem2(0x29, 1, lambda_5C71)

    def lambda_5C82():

        label("loc_5C82")

        TurnDirection(0xFE, 0x14, 400)
        OP_48()
        Jump("loc_5C82")

    QueueWorkItem2(0x21, 1, lambda_5C82)

    def lambda_5C93():
        OP_6D(45940, -5080, 49300, 5000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_5C93)

    def lambda_5CAB():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5CAB)

    def lambda_5CC6():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5CC6)
    Sleep(200)

    def lambda_5CE6():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5CE6)

    def lambda_5D01():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5D01)
    Sleep(200)

    def lambda_5D21():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5D21)

    def lambda_5D3C():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5D3C)
    Sleep(200)

    def lambda_5D5C():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5D5C)

    def lambda_5D77():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5D77)
    Sleep(200)
    OP_43(0x17, 0x0, 0x0, 0x8)
    OP_43(0x18, 0x0, 0x0, 0x9)

    def lambda_5DA5():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5DA5)

    def lambda_5DC0():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5DC0)
    Sleep(200)

    def lambda_5DE0():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5DE0)

    def lambda_5DFB():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5DFB)
    Sleep(200)

    def lambda_5E1B():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5E1B)

    def lambda_5E36():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5E36)
    Sleep(200)

    def lambda_5E56():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5E56)

    def lambda_5E71():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5E71)
    Sleep(200)

    def lambda_5E91():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5E91)

    def lambda_5EAC():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5EAC)
    Sleep(200)

    def lambda_5ECC():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5ECC)

    def lambda_5EE7():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5EE7)
    Sleep(200)

    def lambda_5F07():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5F07)

    def lambda_5F22():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5F22)
    Sleep(200)

    def lambda_5F42():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x106738, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5F42)

    def lambda_5F5D():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x106738, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5F5D)
    Sleep(200)

    def lambda_5F7D():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5F7D)

    def lambda_5F98():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5F98)
    Sleep(200)

    def lambda_5FB8():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5FB8)

    def lambda_5FD3():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5FD3)
    Sleep(200)

    def lambda_5FF3():
        OP_8F(0xFE, 0xD6D8, 0x7F8, 0x19A28, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5FF3)

    def lambda_600E():
        OP_8F(0xFE, 0xD6D8, 0xFFFFFFD8, 0x19A28, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_600E)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    Sleep(300)
    OP_24(0x77, 0x50)
    Sleep(300)
    OP_24(0x77, 0x46)
    Sleep(100)
    FadeToDark(2000, 0, -1)
    Sleep(200)
    OP_24(0x77, 0x3C)
    Sleep(300)
    OP_24(0x77, 0x32)
    Sleep(300)
    OP_24(0x77, 0x28)
    Sleep(300)
    OP_24(0x77, 0x1E)
    Sleep(300)
    OP_23(0x77)
    OP_0D()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0x40D, 0x0)
    ExitThread()
    SetMapFlags(0x2000000)
    OP_A2(0x250A)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_3ADC end

    def Function_8_609E(): pass

    label("Function_8_609E")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 315, 400)
    OP_8E(0xFE, 0xA74E, 0xFA0, 0x7A26, 0x1388, 0x0)
    OP_8E(0xFE, 0xAB54, 0xFA0, 0x7CA6, 0x1388, 0x0)
    OP_8E(0xFE, 0xADB6, 0xFAA, 0xB5B8, 0x1388, 0x0)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_8_609E end

    def Function_9_60FE(): pass

    label("Function_9_60FE")

    Sleep(300)
    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xAA78, 0xFA0, 0x7454, 0x1388, 0x0)
    OP_8E(0xFE, 0xA74E, 0xFA0, 0x7A26, 0x1388, 0x0)
    OP_8E(0xFE, 0xAB54, 0xFA0, 0x7CA6, 0x1388, 0x0)
    OP_8E(0xFE, 0xAC80, 0xFA0, 0xB068, 0x1388, 0x0)
    Sleep(300)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_9_60FE end

    def Function_10_617C(): pass

    label("Function_10_617C")

    OP_8C(0xFE, 225, 400)
    OP_43(0x18, 0x0, 0x0, 0xC)
    OP_8E(0xFE, 0xA8A2, 0xFA0, 0x7D50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA8A2, 0xFA0, 0x7918, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB2AC, 0x1068, 0x7918, 0x7D0, 0x0)
    Return()

    # Function_10_617C end

    def Function_11_61C7(): pass

    label("Function_11_61C7")

    Sleep(300)
    OP_8C(0xFE, 180, 400)
    Sleep(300)
    OP_8E(0xFE, 0xA992, 0xFA0, 0x807A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA8A2, 0xFA0, 0x7D50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA8A2, 0xFA0, 0x7918, 0x7D0, 0x0)
    Return()

    # Function_11_61C7 end

    def Function_12_6215(): pass

    label("Function_12_6215")

    OP_8F(0xFE, 0xA85C, 0xFA0, 0x73F0, 0x5DC, 0x0)
    Return()

    # Function_12_6215 end

    def Function_13_622A(): pass

    label("Function_13_622A")

    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x8804, 0x0, 0x6716, 0x1770, 0x0)
    OP_8E(0xFE, 0x8188, 0x0, 0x825A, 0x1770, 0x0)
    OP_8E(0xFE, 0x820A, 0x7D0, 0x9934, 0x1770, 0x0)
    OP_8E(0xFE, 0x951A, 0xFA0, 0x997A, 0x1770, 0x0)
    SetChrPos(0xFE, 42290, 4000, 30690, 270)
    Return()

    # Function_13_622A end

    def Function_14_6293(): pass

    label("Function_14_6293")

    Sleep(200)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0x8C14, 0x0, 0x64E6, 0x1770, 0x0)
    OP_8E(0xFE, 0x8188, 0x0, 0x825A, 0x1770, 0x0)
    OP_8E(0xFE, 0x820A, 0x7D0, 0x9934, 0x1770, 0x0)
    OP_8E(0xFE, 0x951A, 0xFA0, 0x997A, 0x1770, 0x0)
    SetChrPos(0xFE, 43090, 4000, 29830, 270)
    Return()

    # Function_14_6293 end

    def Function_15_6301(): pass

    label("Function_15_6301")

    OP_24(0xBF, 0x5A)
    Sleep(100)
    OP_24(0xBF, 0x50)
    Sleep(100)
    OP_24(0xBF, 0x46)
    Sleep(100)
    OP_24(0xBF, 0x3C)
    Sleep(100)
    OP_24(0xBF, 0x32)
    Sleep(100)
    OP_24(0xBF, 0x1E)
    Sleep(100)
    OP_24(0xBF, 0x14)
    Sleep(100)
    OP_24(0xBF, 0xA)
    Sleep(100)
    OP_24(0xBF, 0x0)
    OP_23(0xBF)
    Return()

    # Function_15_6301 end

    SaveToFile()

Try(main)
