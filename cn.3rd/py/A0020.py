from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 调试地图

    CreateScenaFile(
        FileName            = 'A0020   ._SN',
        MapName             = 'map1',
        Location            = 'T0030.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 55,
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
        '03000 艾丝蒂尔',                       # 9
        '03010 约修亚',                         # 10
        '03020 雪拉',                           # 11
        '03030 奥利维尔',                       # 12
        '03040 科洛丝',                         # 13
        '03050 阿加特',                         # 14
        '03060 提妲',                           # 15
        '03070 金',                             # 16
        '03080 凯文',                           # 17
        '03090 亚妮拉丝',                       # 18
        '03100 乔丝特',                         # 19
        '03110 理查德',                         # 20
        '03120 凯诺娜',                         # 21
        '03130 克鲁茨',                         # 22
        '03150 莉丝',                           # 23
        '03180 库拉茨',                         # 24
        '03190 卡露娜',                         # 25
        '03200 没有纹章的约修亚',               # 26
        '03210 礼服科洛丝',                     # 27
        '03500 瘦狼瓦鲁特',                     # 28
        '03510 『歼灭天使』玲',                 # 29
        '03520 幻惑之铃露茜奥拉',               # 30
        '03530 布卢布兰伯爵',                   # 31
        '03540 剑帝莱恩哈特',                   # 32
        '03550 研究服怀斯曼',                   # 33
        '03560 机器约修亚',                     # 34
        '03570 穆拉',                           # 35
        '03580 尤莉亚上尉',                     # 36
        '03590 希德中校',                       # 37
        '03600 小丑肯帕雷拉',                   # 38
        '03610 强化猎兵A',                      # 39
        '03620 强化猎兵B',                      # 40
        '03630 猎兵克鲁茨',                     # 41
        '03640 猎兵卡露娜',                     # 42
        '03650 强化猎兵约修亚',                 # 43
        '03670 军服卡西乌斯',                   # 44
        '03680 军服奥利维尔',                   # 45
        '03690 投狱版理查德',                   # 46
        '03940 露菲娜',                         # 47
        '03950 奥斯本',                         # 48
        '03960 科洛蒂娅',                       # 49
        '03970 提妲父亲',                       # 50
        '03980 提妲母亲\u3000',                 # 51
        '03990 礼服的尤莉亚',                   # 52
        'CH00000前篇艾丝蒂尔',                  # 53
        'CH00010前篇约修亚',                    # 54
        '',                                     # 55
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
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 315,
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
        'ED6_DT07/CH00000 ._CH',             # 00
        'ED6_DT07/CH00010 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00050 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT07/CH00070 ._CH',             # 07
        'ED6_DT27/CH03080 ._CH',             # 08
        'ED6_DT27/CH03090 ._CH',             # 09
        'ED6_DT27/CH03100 ._CH',             # 0A
        'ED6_DT07/CH02030 ._CH',             # 0B
        'ED6_DT07/CH02030 ._CH',             # 0C
        'ED6_DT27/CH03130 ._CH',             # 0D
        'ED6_DT27/CH03150 ._CH',             # 0E
        'ED6_DT07/CH00000 ._CH',             # 0F
        'ED6_DT07/CH00010 ._CH',             # 10
        'ED6_DT27/CH03200 ._CH',             # 11
        'ED6_DT27/CH03210 ._CH',             # 12
        'ED6_DT07/CH01260 ._CH',             # 13
        'ED6_DT07/CH01240 ._CH',             # 14
        'ED6_DT27/CH03500 ._CH',             # 15
        'ED6_DT27/CH03510 ._CH',             # 16
        'ED6_DT27/CH03520 ._CH',             # 17
        'ED6_DT27/CH03530 ._CH',             # 18
        'ED6_DT27/CH03540 ._CH',             # 19
        'ED6_DT27/CH03550 ._CH',             # 1A
        'ED6_DT27/CH03560 ._CH',             # 1B
        'ED6_DT27/CH03570 ._CH',             # 1C
        'ED6_DT27/CH03580 ._CH',             # 1D
        'ED6_DT27/CH03590 ._CH',             # 1E
        'ED6_DT27/CH03600 ._CH',             # 1F
        'ED6_DT27/CH03610 ._CH',             # 20
        'ED6_DT27/CH03620 ._CH',             # 21
        'ED6_DT27/CH03630 ._CH',             # 22
        'ED6_DT27/CH03640 ._CH',             # 23
        'ED6_DT27/CH03650 ._CH',             # 24
        'ED6_DT27/CH03670 ._CH',             # 25
        'ED6_DT27/CH03680 ._CH',             # 26
        'ED6_DT27/CH03690 ._CH',             # 27
        'ED6_DT27/CH03940 ._CH',             # 28
        'ED6_DT27/CH03950 ._CH',             # 29
        'ED6_DT27/CH03960 ._CH',             # 2A
        'ED6_DT27/CH03970 ._CH',             # 2B
        'ED6_DT27/CH03980 ._CH',             # 2C
        'ED6_DT27/CH03990 ._CH',             # 2D
    )

    AddCharChipPat(
        'ED6_DT07/CH00000P._CP',             # 00
        'ED6_DT07/CH00010P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00050P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT07/CH00070P._CP',             # 07
        'ED6_DT27/CH03080P._CP',             # 08
        'ED6_DT27/CH03090P._CP',             # 09
        'ED6_DT27/CH03100P._CP',             # 0A
        'ED6_DT07/CH02030P._CP',             # 0B
        'ED6_DT07/CH02030P._CP',             # 0C
        'ED6_DT27/CH03130P._CP',             # 0D
        'ED6_DT27/CH03150P._CP',             # 0E
        'ED6_DT07/CH00000P._CP',             # 0F
        'ED6_DT07/CH00010P._CP',             # 10
        'ED6_DT27/CH03200P._CP',             # 11
        'ED6_DT27/CH03210P._CP',             # 12
        'ED6_DT07/CH01260P._CP',             # 13
        'ED6_DT07/CH01240P._CP',             # 14
        'ED6_DT27/CH03500P._CP',             # 15
        'ED6_DT27/CH03510P._CP',             # 16
        'ED6_DT27/CH03520P._CP',             # 17
        'ED6_DT27/CH03530P._CP',             # 18
        'ED6_DT27/CH03540P._CP',             # 19
        'ED6_DT27/CH03550P._CP',             # 1A
        'ED6_DT27/CH03560P._CP',             # 1B
        'ED6_DT27/CH03570P._CP',             # 1C
        'ED6_DT27/CH03580P._CP',             # 1D
        'ED6_DT27/CH03590P._CP',             # 1E
        'ED6_DT27/CH03600P._CP',             # 1F
        'ED6_DT27/CH03610P._CP',             # 20
        'ED6_DT27/CH03620P._CP',             # 21
        'ED6_DT27/CH03630P._CP',             # 22
        'ED6_DT27/CH03640P._CP',             # 23
        'ED6_DT27/CH03650P._CP',             # 24
        'ED6_DT27/CH03670P._CP',             # 25
        'ED6_DT27/CH03680P._CP',             # 26
        'ED6_DT27/CH03690P._CP',             # 27
        'ED6_DT27/CH03940P._CP',             # 28
        'ED6_DT27/CH03950P._CP',             # 29
        'ED6_DT27/CH03960P._CP',             # 2A
        'ED6_DT27/CH03970P._CP',             # 2B
        'ED6_DT27/CH03980P._CP',             # 2C
        'ED6_DT27/CH03990P._CP',             # 2D
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 36000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 40000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 36000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 8000,
        Z                   = 0,
        Y                   = 40000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 28,
        ChipIndex           = 0x1C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 36000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 40000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 31,
        ChipIndex           = 0x1F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 33,
        ChipIndex           = 0x21,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 34,
        ChipIndex           = 0x22,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 34,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 35,
        ChipIndex           = 0x23,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 35,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 36,
        ChipIndex           = 0x24,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 36,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 38,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 36000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 38,
        ChipIndex           = 0x26,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 39,
    )

    DeclNpc(
        X                   = 16000,
        Z                   = 0,
        Y                   = 40000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 39,
        ChipIndex           = 0x27,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 40,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 40,
        ChipIndex           = 0x28,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 41,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 41,
        ChipIndex           = 0x29,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 42,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 42,
        ChipIndex           = 0x2A,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 43,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 16000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 43,
        ChipIndex           = 0x2B,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 44,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 20000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 44,
        ChipIndex           = 0x2C,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 24000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 45,
        ChipIndex           = 0x2D,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 46,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 53,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 54,
    )


    ScpFunction(
        "Function_0_7DA",          # 00, 0
        "Function_1_7E0",          # 01, 1
        "Function_2_7E1",          # 02, 2
        "Function_3_7FA",          # 03, 3
        "Function_4_A73",          # 04, 4
        "Function_5_C19",          # 05, 5
        "Function_6_C9E",          # 06, 6
        "Function_7_D8B",          # 07, 7
        "Function_8_EC0",          # 08, 8
        "Function_9_100E",         # 09, 9
        "Function_10_112E",        # 0A, 10
        "Function_11_11ED",        # 0B, 11
        "Function_12_12D2",        # 0C, 12
        "Function_13_142F",        # 0D, 13
        "Function_14_144D",        # 0E, 14
        "Function_15_146B",        # 0F, 15
        "Function_16_15B2",        # 10, 16
        "Function_17_1688",        # 11, 17
        "Function_18_16FB",        # 12, 18
        "Function_19_176E",        # 13, 19
        "Function_20_182D",        # 14, 20
        "Function_21_18EC",        # 15, 21
        "Function_22_19DF",        # 16, 22
        "Function_23_1B1E",        # 17, 23
        "Function_24_1BAB",        # 18, 24
        "Function_25_1C38",        # 19, 25
        "Function_26_1C56",        # 1A, 26
        "Function_27_1CCD",        # 1B, 27
        "Function_28_1CE6",        # 1C, 28
        "Function_29_1D04",        # 1D, 29
        "Function_30_1D22",        # 1E, 30
        "Function_31_1D40",        # 1F, 31
        "Function_32_1DBA",        # 20, 32
        "Function_33_1DD3",        # 21, 33
        "Function_34_1DEC",        # 22, 34
        "Function_35_1E5F",        # 23, 35
        "Function_36_1E9C",        # 24, 36
        "Function_37_1F37",        # 25, 37
        "Function_38_1FAA",        # 26, 38
        "Function_39_2041",        # 27, 39
        "Function_40_211A",        # 28, 40
        "Function_41_217B",        # 29, 41
        "Function_42_221E",        # 2A, 42
        "Function_43_2273",        # 2B, 43
        "Function_44_22D4",        # 2C, 44
        "Function_45_22ED",        # 2D, 45
        "Function_46_238B",        # 2E, 46
        "Function_47_2436",        # 2F, 47
        "Function_48_2454",        # 30, 48
        "Function_49_2472",        # 31, 49
        "Function_50_24E0",        # 32, 50
        "Function_51_24F9",        # 33, 51
        "Function_52_2512",        # 34, 52
        "Function_53_253D",        # 35, 53
        "Function_54_27E4",        # 36, 54
        "Function_55_2A11",        # 37, 55
    )


    def Function_0_7DA(): pass

    label("Function_0_7DA")

    OP_3E(0x383, 1)
    Return()

    # Function_0_7DA end

    def Function_1_7E0(): pass

    label("Function_1_7E0")

    Return()

    # Function_1_7E0 end

    def Function_2_7E1(): pass

    label("Function_2_7E1")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "喝～\x02",
    )

    Jump("loc_7F5")

    label("loc_7F5")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_2_7E1 end

    def Function_3_7FA(): pass

    label("Function_3_7FA")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        (
            "#5P#1000F普通\x01",
            "面向＃５Ｐ\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "#11P#1001F笑容\x01",
            "面向＃１１Ｐ\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "#6P#1002F认真\x01",
            "面向＃６Ｐ\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "#12P#1003F悲哀１\x01",
            "面向＃１２Ｐ\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "#1004F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "#1005F愤怒１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "#1006F普通（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "#1007F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "#1008F害羞１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "#1009F愤怒２（唔）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "#1010F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "#1011F普通（张嘴）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "#1012F闭目笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "#1013F害羞２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "#1014F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "#1015F嗯～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "#1016F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "#1017F害羞３\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "#1018F笑颜２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "#1019F盯着看\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "#1020F严重惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "#1021F痛苦\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "#1022F叫喊２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "#1023F哭喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "#1024F空虚\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "#1025F苦笑２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "#1026F忧郁悲伤惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "#1027F悲哀２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_7FA end

    def Function_4_A73(): pass

    label("Function_4_A73")

    TalkBegin(0xFE)

    ChrTalk(    #29
        0xFE,
        (
            "#1030F普通Ａ\x01",
            "A前半部分用\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "#1031F笑容Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "#1032F认真Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "#1033F悲哀Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "#1034F惊愕Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "#1035F闭目Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "#1036F愤怒Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "#1037F痛苦Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "#1038F瞪视Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "#1039F哭泣Ａ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "#1040F普通Ｂ\x01",
            "B后半用\x02",
        )
    )

    Jump("loc_B6E")

    label("loc_B6E")

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "#1041F笑颜Ｂ１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "#1042F认真Ｂ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "#1043F悲哀Ｂ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "#1044F惊愕Ｂ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "#1046F愤怒Ｂ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "#1047F痛苦Ｂ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "#1048F盯着看Ｂ\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "#1049F笑颜Ｂ２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_A73 end

    def Function_5_C19(): pass

    label("Function_5_C19")

    TalkBegin(0xFE)

    ChrTalk(    #48
        0xFE,
        "#020F普通\x02",
    )

    Jump("loc_C32")

    label("loc_C32")

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "#870F小雪拉普通\x02\x03",

            "#871F笑颜\x02\x03",

            "#872F苦笑\x02\x03",

            "#873F困惑\x02\x03",

            "#874F慌张（啊哇哇）\x02",
        )
    )

    Jump("loc_C99")

    label("loc_C99")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_C19 end

    def Function_6_C9E(): pass

    label("Function_6_C9E")

    TalkBegin(0xFE)

    ChrTalk(    #50
        0xFE,
        "#030F普通\x02",
    )

    Jump("loc_CB7")

    label("loc_CB7")

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "#031F笑容\x02",
    )

    Jump("loc_CCE")

    label("loc_CCE")

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "#032F认真\x02",
    )

    Jump("loc_CE5")

    label("loc_CE5")

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "#033F惊愕\x02",
    )

    Jump("loc_CFC")

    label("loc_CFC")

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "#034F叹息\x02",
    )

    Jump("loc_D13")

    label("loc_D13")

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "#035F瞑目\x02",
    )

    Jump("loc_D2A")

    label("loc_D2A")

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "#036F慌张\x02",
    )

    Jump("loc_D41")

    label("loc_D41")

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "#037F喝醉\x02",
    )

    Jump("loc_D58")

    label("loc_D58")

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "#038F烂醉\x02",
    )

    Jump("loc_D6F")

    label("loc_D6F")

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "#039F痛苦\x02",
    )

    Jump("loc_D86")

    label("loc_D86")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_C9E end

    def Function_7_D8B(): pass

    label("Function_7_D8B")

    TalkBegin(0xFE)

    ChrTalk(    #60
        0xFE,
        "#040F普通\x02",
    )

    Jump("loc_DA4")

    label("loc_DA4")

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "#041F笑容１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "#042F认真\x02",
    )

    Jump("loc_DCE")

    label("loc_DCE")

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "#043F悲哀１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "#044F惊愕\x02",
    )

    Jump("loc_DF8")

    label("loc_DF8")

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "#045F困惑\x02",
    )

    Jump("loc_E0F")

    label("loc_E0F")

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "#046F发怒\x02",
    )

    Jump("loc_E26")

    label("loc_E26")

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "#047F瞑目\x02",
    )

    Jump("loc_E3D")

    label("loc_E3D")

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        "#048F笑容２（小姐ver）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "#049F悲哀２（深刻）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "#540F赤面\x02",
    )

    Jump("loc_E8D")

    label("loc_E8D")

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "#541F痛苦\x02",
    )

    Jump("loc_EA4")

    label("loc_EA4")

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "#542F苦笑\x02",
    )

    Jump("loc_EBB")

    label("loc_EBB")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_D8B end

    def Function_8_EC0(): pass

    label("Function_8_EC0")

    TalkBegin(0xFE)

    ChrTalk(    #73
        0xFE,
        "#050F普通\x02",
    )

    Jump("loc_ED9")

    label("loc_ED9")

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "#051F笑容\x02",
    )

    Jump("loc_EF0")

    label("loc_EF0")

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "#052F惊愕\x02",
    )

    Jump("loc_F07")

    label("loc_F07")

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "#053F瞑目\x02",
    )

    Jump("loc_F1E")

    label("loc_F1E")

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "#054F发怒\x02",
    )

    Jump("loc_F35")

    label("loc_F35")

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "#055F困惑\x02",
    )

    Jump("loc_F4C")

    label("loc_F4C")

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "#056F痛\x02",
    )

    Jump("loc_F5E")

    label("loc_F5E")

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "#057F杀意\x02",
    )

    Jump("loc_F75")

    label("loc_F75")

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "#058F毒\x02",
    )

    Jump("loc_F87")

    label("loc_F87")

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "#059F苦痛\x02",
    )

    Jump("loc_F9E")

    label("loc_F9E")

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "#550F可恶～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "#551F笑容２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "#552F悲哀\x02",
    )

    Jump("loc_FDD")

    label("loc_FDD")

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "#553F空虚\x02",
    )

    Jump("loc_FF4")

    label("loc_FF4")

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "#554F空虚微笑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_EC0 end

    def Function_9_100E(): pass

    label("Function_9_100E")

    TalkBegin(0xFE)

    ChrTalk(    #88
        0xFE,
        "#060F普通１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "#061F笑容１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "#062F认真\x02",
    )

    Jump("loc_104D")

    label("loc_104D")

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "#063F悲哀\x02",
    )

    Jump("loc_1064")

    label("loc_1064")

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "#064F惊愕\x02",
    )

    Jump("loc_107B")

    label("loc_107B")

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "#065F困惑\x02",
    )

    Jump("loc_1092")

    label("loc_1092")

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "#066F笑容２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "#067F害羞\x02",
    )

    Jump("loc_10BC")

    label("loc_10BC")

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "#068F发怒\x02",
    )

    Jump("loc_10D3")

    label("loc_10D3")

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "#069F哭泣\x02",
    )

    Jump("loc_10EA")

    label("loc_10EA")

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "#560F普通２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "#561F叹息\x02",
    )

    Jump("loc_1114")

    label("loc_1114")

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "#562F害羞困惑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_100E end

    def Function_10_112E(): pass

    label("Function_10_112E")

    TalkBegin(0xFE)

    ChrTalk(    #101
        0xFE,
        "#070F普通\x02",
    )

    Jump("loc_1147")

    label("loc_1147")

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "#071F笑容\x02",
    )

    Jump("loc_115E")

    label("loc_115E")

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "#072F认真\x02",
    )

    Jump("loc_1175")

    label("loc_1175")

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "#073F惊愕\x02",
    )

    Jump("loc_118C")

    label("loc_118C")

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "#074F瞑目\x02",
    )

    Jump("loc_11A3")

    label("loc_11A3")

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "#075F叹息\x02",
    )

    Jump("loc_11BA")

    label("loc_11BA")

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "#076F叫喊\x02",
    )

    Jump("loc_11D1")

    label("loc_11D1")

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "#077F痛苦\x02",
    )

    Jump("loc_11E8")

    label("loc_11E8")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_112E end

    def Function_11_11ED(): pass

    label("Function_11_11ED")

    TalkBegin(0xFE)

    ChrTalk(    #109
        0xFE,
        "#1060F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "#1061F笑颜１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "#1062F笑颜２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "#1063F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "#1064F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "#1065F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "#1066F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        "#1067F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "#1068F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "#1069F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "#1070F痛苦\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "#1071F笑颜３\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_11ED end

    def Function_12_12D2(): pass

    label("Function_12_12D2")

    TalkBegin(0xFE)

    ChrTalk(    #121
        0xFE,
        "#810F普通\x02",
    )

    Jump("loc_12EB")

    label("loc_12EB")

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "#811F笑颜１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        "#812F认真\x02",
    )

    Jump("loc_1315")

    label("loc_1315")

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "#813F悲哀\x02",
    )

    Jump("loc_132C")

    label("loc_132C")

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "#814F惊愕\x02",
    )

    Jump("loc_1343")

    label("loc_1343")

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "#815F叫喊\x02",
    )

    Jump("loc_135A")

    label("loc_135A")

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "#816F自信\x02",
    )

    Jump("loc_1371")

    label("loc_1371")

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "#817F闭目\x02",
    )

    Jump("loc_1388")

    label("loc_1388")

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "#818F嗯～\x02",
    )

    Jump("loc_139F")

    label("loc_139F")

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "#819F苦笑１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "#1310F笑颜２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "#1311F做梦的感觉\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "#1312F痛苦\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "#1313F空虚\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "#1314F苦笑２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "#1315F苦笑３\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_12D2 end

    def Function_13_142F(): pass

    label("Function_13_142F")

    TalkBegin(0xFE)

    ChrTalk(    #137
        0xFE,
        "#210F普通\x02",
    )

    Jump("loc_1448")

    label("loc_1448")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_142F end

    def Function_14_144D(): pass

    label("Function_14_144D")

    TalkBegin(0xFE)

    ChrTalk(    #138
        0xFE,
        "#110F普通\x02",
    )

    Jump("loc_1466")

    label("loc_1466")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_144D end

    def Function_15_146B(): pass

    label("Function_15_146B")

    TalkBegin(0xFE)

    ChrTalk(    #139
        0xFE,
        "#1180F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        "#1181F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        "#1182F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "#1183F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "#1184F惊愕１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        "#1185F惊愕２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "#1186F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "#1187F差一点\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "#1188F大笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "#1189F痛苦\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "#1320F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        "#1321F转移视线\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        "#1322F咦！理查德大人！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "#1323F理查德大人…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "#1324F理查德大人～！！(哭号)\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_146B end

    def Function_16_15B2(): pass

    label("Function_16_15B2")

    TalkBegin(0xFE)

    ChrTalk(    #154
        0xFE,
        "#840F普通\x02",
    )

    Jump("loc_15CB")

    label("loc_15CB")

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "#841F笑颜\x02",
    )

    Jump("loc_15E2")

    label("loc_15E2")

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "#842F认真\x02",
    )

    Jump("loc_15F9")

    label("loc_15F9")

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "#843F闭目\x02",
    )

    Jump("loc_1610")

    label("loc_1610")

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "#844F悲哀\x02",
    )

    Jump("loc_1627")

    label("loc_1627")

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "#845F苦笑\x02",
    )

    Jump("loc_163E")

    label("loc_163E")

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "#846F叫喊\x02",
    )

    Jump("loc_1655")

    label("loc_1655")

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "#847F痛苦\x02",
    )

    Jump("loc_166C")

    label("loc_166C")

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "#848F空虚\x02",
    )

    Jump("loc_1683")

    label("loc_1683")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_15B2 end

    def Function_17_1688(): pass

    label("Function_17_1688")

    TalkBegin(0xFE)

    ChrTalk(    #163
        0xFE,
        "#1440F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "#1450F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "#1460F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        "#1470F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        "#1480F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "#1490F普通\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1688 end

    def Function_18_16FB(): pass

    label("Function_18_16FB")

    TalkBegin(0xFE)

    ChrTalk(    #169
        0xFE,
        "#1160F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "#1161F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "#1162F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        "#1163F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        "#1164F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "#1165F闭目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_16FB end

    def Function_19_176E(): pass

    label("Function_19_176E")

    TalkBegin(0xFE)

    ChrTalk(    #175
        0xFE,
        "#820F普通\x02",
    )

    Jump("loc_1787")

    label("loc_1787")

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "#821F笑颜\x02",
    )

    Jump("loc_179E")

    label("loc_179E")

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "#822F认真\x02",
    )

    Jump("loc_17B5")

    label("loc_17B5")

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "#823F闭目\x02",
    )

    Jump("loc_17CC")

    label("loc_17CC")

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "#824F悲哀\x02",
    )

    Jump("loc_17E3")

    label("loc_17E3")

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "#825F苦笑\x02",
    )

    Jump("loc_17FA")

    label("loc_17FA")

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        "#826F痛苦\x02",
    )

    Jump("loc_1811")

    label("loc_1811")

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "#827F空虚\x02",
    )

    Jump("loc_1828")

    label("loc_1828")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_176E end

    def Function_20_182D(): pass

    label("Function_20_182D")

    TalkBegin(0xFE)

    ChrTalk(    #183
        0xFE,
        "#830F普通\x02",
    )

    Jump("loc_1846")

    label("loc_1846")

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        "#831F笑颜\x02",
    )

    Jump("loc_185D")

    label("loc_185D")

    CloseMessageWindow()

    ChrTalk(    #185
        0xFE,
        "#832F认真\x02",
    )

    Jump("loc_1874")

    label("loc_1874")

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "#833F闭目\x02",
    )

    Jump("loc_188B")

    label("loc_188B")

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "#834F悲哀\x02",
    )

    Jump("loc_18A2")

    label("loc_18A2")

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        "#835F苦笑\x02",
    )

    Jump("loc_18B9")

    label("loc_18B9")

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        "#836F痛苦\x02",
    )

    Jump("loc_18D0")

    label("loc_18D0")

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "#837F空虚\x02",
    )

    Jump("loc_18E7")

    label("loc_18E7")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_182D end

    def Function_21_18EC(): pass

    label("Function_21_18EC")

    TalkBegin(0xFE)

    ChrTalk(    #191
        0xFE,
        "#250F普通（无目）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        "#251F普通\x02",
    )

    Jump("loc_191E")

    label("loc_191E")

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        "#252F笑颜（无目）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "#253F笑颜\x02",
    )

    Jump("loc_194E")

    label("loc_194E")

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        "#254F认真（无目）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        "#255F认真\x02",
    )

    Jump("loc_197E")

    label("loc_197E")

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        "#256F悲哀\x02",
    )

    Jump("loc_1995")

    label("loc_1995")

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        "#257F闭目\x02",
    )

    Jump("loc_19AC")

    label("loc_19AC")

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "#258F叫喊\x02",
    )

    Jump("loc_19C3")

    label("loc_19C3")

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        "#259F痛苦\x02",
    )

    Jump("loc_19DA")

    label("loc_19DA")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_18EC end

    def Function_22_19DF(): pass

    label("Function_22_19DF")

    TalkBegin(0xFE)

    ChrTalk(    #201
        0xFE,
        "#260F普通\x02",
    )

    Jump("loc_19F8")

    label("loc_19F8")

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        "#261F笑颜１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        "#262F认真\x02",
    )

    Jump("loc_1A22")

    label("loc_1A22")

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        "#263F察觉到的脸\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "#264F惊愕\x02",
    )

    Jump("loc_1A50")

    label("loc_1A50")

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        "#265F笑颜２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "#266F愠怒的脸\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        "#267F嗯～\x02",
    )

    Jump("loc_1A8F")

    label("loc_1A8F")

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "#268F有企图的脸\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        "#269F有企图的笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "#1300F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "#1301F愤怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "#1302F杀意\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "#1303F痛苦\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "#1304F微笑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_19DF end

    def Function_23_1B1E(): pass

    label("Function_23_1B1E")

    TalkBegin(0xFE)

    ChrTalk(    #216
        0xFE,
        "#240F普通\x02",
    )

    Jump("loc_1B37")

    label("loc_1B37")

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        "#241F笑颜\x02",
    )

    Jump("loc_1B4E")

    label("loc_1B4E")

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        "#242F认真\x02",
    )

    Jump("loc_1B65")

    label("loc_1B65")

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        "#243F惊愕\x02",
    )

    Jump("loc_1B7C")

    label("loc_1B7C")

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        "#244F闭目\x02",
    )

    Jump("loc_1B93")

    label("loc_1B93")

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        "#245F痛苦？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_1B1E end

    def Function_24_1BAB(): pass

    label("Function_24_1BAB")

    TalkBegin(0xFE)

    ChrTalk(    #222
        0xFE,
        "#230F普通\x02",
    )

    Jump("loc_1BC4")

    label("loc_1BC4")

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        "#231F笑颜\x02",
    )

    Jump("loc_1BDB")

    label("loc_1BDB")

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        "#232F认真\x02",
    )

    Jump("loc_1BF2")

    label("loc_1BF2")

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        "#233F惊愕？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        "#234F叫喊\x02",
    )

    Jump("loc_1C1C")

    label("loc_1C1C")

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "#235F痛苦\x02",
    )

    Jump("loc_1C33")

    label("loc_1C33")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_1BAB end

    def Function_25_1C38(): pass

    label("Function_25_1C38")

    TalkBegin(0xFE)

    ChrTalk(    #228
        0xFE,
        "#120F嗷—\x02",
    )

    Jump("loc_1C51")

    label("loc_1C51")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_1C38 end

    def Function_26_1C56(): pass

    label("Function_26_1C56")

    TalkBegin(0xFE)

    ChrTalk(    #229
        0xFE,
        "#1150F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        "#1151F笑颜１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        "#1152F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        "#1153F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        "#1154F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        "#1155F笑颜２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_1C56 end

    def Function_27_1CCD(): pass

    label("Function_27_1CCD")

    TalkBegin(0xFE)

    ChrTalk(    #235
        0xFE,
        "#1140F嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_1CCD end

    def Function_28_1CE6(): pass

    label("Function_28_1CE6")

    TalkBegin(0xFE)

    ChrTalk(    #236
        0xFE,
        "#270F嗷—\x02",
    )

    Jump("loc_1CFF")

    label("loc_1CFF")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_1CE6 end

    def Function_29_1D04(): pass

    label("Function_29_1D04")

    TalkBegin(0xFE)

    ChrTalk(    #237
        0xFE,
        "#170F嗷—\x02",
    )

    Jump("loc_1D1D")

    label("loc_1D1D")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_1D04 end

    def Function_30_1D22(): pass

    label("Function_30_1D22")

    TalkBegin(0xFE)

    ChrTalk(    #238
        0xFE,
        "#700F嗷—\x02",
    )

    Jump("loc_1D3B")

    label("loc_1D3B")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_1D22 end

    def Function_31_1D40(): pass

    label("Function_31_1D40")

    TalkBegin(0xFE)

    ChrTalk(    #239
        0xFE,
        "#850F普通\x02",
    )

    Jump("loc_1D59")

    label("loc_1D59")

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        "#851F笑颜\x02",
    )

    Jump("loc_1D70")

    label("loc_1D70")

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        "#852F认真\x02",
    )

    Jump("loc_1D87")

    label("loc_1D87")

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "#853F闭目\x02",
    )

    Jump("loc_1D9E")

    label("loc_1D9E")

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        "#854F微笑\x02",
    )

    Jump("loc_1DB5")

    label("loc_1DB5")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_1D40 end

    def Function_32_1DBA(): pass

    label("Function_32_1DBA")

    TalkBegin(0xFE)

    ChrTalk(    #244
        0xFE,
        "喝～\x02",
    )

    Jump("loc_1DCE")

    label("loc_1DCE")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_1DBA end

    def Function_33_1DD3(): pass

    label("Function_33_1DD3")

    TalkBegin(0xFE)

    ChrTalk(    #245
        0xFE,
        "喝～\x02",
    )

    Jump("loc_1DE7")

    label("loc_1DE7")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_1DD3 end

    def Function_34_1DEC(): pass

    label("Function_34_1DEC")

    TalkBegin(0xFE)

    ChrTalk(    #246
        0xFE,
        "#1210F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        "#1211F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        "#1212F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        "#1213F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        "#1190F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        "#1191F闭目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_1DEC end

    def Function_35_1E5F(): pass

    label("Function_35_1E5F")

    TalkBegin(0xFE)

    ChrTalk(    #252
        0xFE,
        "#1200F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        "#1201F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        "#1202F闭目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_1E5F end

    def Function_36_1E9C(): pass

    label("Function_36_1E9C")

    TalkBegin(0xFE)

    ChrTalk(    #255
        0xFE,
        "#1130F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        "#1131F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        "#1132F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        "#1133F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        "#1134F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "#1135F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        "#1136F悲哀２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        "#1137F笑颜２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_1E9C end

    def Function_37_1F37(): pass

    label("Function_37_1F37")

    TalkBegin(0xFE)

    ChrTalk(    #263
        0xFE,
        "#1160F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        "#1161F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        "#1162F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        "#1163F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "#1164F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        "#1165F闭目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_1F37 end

    def Function_38_1FAA(): pass

    label("Function_38_1FAA")

    TalkBegin(0xFE)

    ChrTalk(    #269
        0xFE,
        "#1120F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        "#1121F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        "#1122F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        "#1123F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        "#1124F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        "#1125F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        "#1126F愤怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        "#1127F叫喊\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_1FAA end

    def Function_39_2041(): pass

    label("Function_39_2041")

    TalkBegin(0xFE)

    ChrTalk(    #277
        0xFE,
        "#890F普通\x02",
    )

    Jump("loc_205A")

    label("loc_205A")

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        "#891F笑颜\x02",
    )

    Jump("loc_2071")

    label("loc_2071")

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "#892F认真\x02",
    )

    Jump("loc_2088")

    label("loc_2088")

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        "#893F叹息\x02",
    )

    Jump("loc_209F")

    label("loc_209F")

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        "#894F闭目\x02",
    )

    Jump("loc_20B6")

    label("loc_20B6")

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        "#895F恶普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        "#896F恶笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "#897F恶认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        "#898F恶惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        "#899F恶闭目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_2041 end

    def Function_40_211A(): pass

    label("Function_40_211A")

    TalkBegin(0xFE)

    ChrTalk(    #287
        0xFE,
        "#1170F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "#1171F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        "#1172F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        "#1173F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        "#1174F悲哀\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_211A end

    def Function_41_217B(): pass

    label("Function_41_217B")

    TalkBegin(0xFE)

    ChrTalk(    #292
        0xFE,
        "#880F普通\x02",
    )

    Jump("loc_2194")

    label("loc_2194")

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        "#881F笑颜\x02",
    )

    Jump("loc_21AB")

    label("loc_21AB")

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        "#882F认真\x02",
    )

    Jump("loc_21C2")

    label("loc_21C2")

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "#883F惊愕\x02",
    )

    Jump("loc_21D9")

    label("loc_21D9")

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        "#884F闭目\x02",
    )

    Jump("loc_21F0")

    label("loc_21F0")

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        "#885F叫喊\x02",
    )

    Jump("loc_2207")

    label("loc_2207")

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        "#886F啧\x02",
    )

    Jump("loc_2219")

    label("loc_2219")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_217B end

    def Function_42_221E(): pass

    label("Function_42_221E")

    TalkBegin(0xFE)

    ChrTalk(    #299
        0xFE,
        "#1100F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        "#1101F认真·惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        "#1102F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        "#1103F叫喊\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_221E end

    def Function_43_2273(): pass

    label("Function_43_2273")

    TalkBegin(0xFE)

    ChrTalk(    #303
        0xFE,
        "#1110F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        "#1111F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        "#1112F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        "#1113F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        "#1114F叫喊\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_2273 end

    def Function_44_22D4(): pass

    label("Function_44_22D4")

    TalkBegin(0xFE)

    ChrTalk(    #308
        0xFE,
        "喝～\x02",
    )

    Jump("loc_22E8")

    label("loc_22E8")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_44_22D4 end

    def Function_45_22ED(): pass

    label("Function_45_22ED")

    TalkBegin(0xFE)

    ChrTalk(    #309
        0xFE,
        "#860F普通\x02",
    )

    Jump("loc_2306")

    label("loc_2306")

    CloseMessageWindow()

    ChrTalk(    #310
        0xFE,
        "#861F笑颜１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        "#862F认真\x02",
    )

    Jump("loc_2330")

    label("loc_2330")

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        "#863F闭目\x02",
    )

    Jump("loc_2347")

    label("loc_2347")

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        "#864F惊愕\x02",
    )

    Jump("loc_235E")

    label("loc_235E")

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        "#865F笑颜２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        "#866F小姐笑颜\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_22ED end

    def Function_46_238B(): pass

    label("Function_46_238B")

    TalkBegin(0xFE)

    ChrTalk(    #316
        0xFE,
        "#1220F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        "#1221F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xFE,
        "#1222F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        "#1223F悲哀（转移视线）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xFE,
        "#1224F困惑（惊愕）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        "#1225F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0xFE,
        "#1226F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        "#1227F苦痛\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_46_238B end

    def Function_47_2436(): pass

    label("Function_47_2436")

    TalkBegin(0xFE)

    ChrTalk(    #324
        0xFE,
        "#190F嗷—\x02",
    )

    Jump("loc_244F")

    label("loc_244F")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_47_2436 end

    def Function_48_2454(): pass

    label("Function_48_2454")

    TalkBegin(0xFE)

    ChrTalk(    #325
        0xFE,
        "#200F嗷—\x02",
    )

    Jump("loc_246D")

    label("loc_246D")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_48_2454 end

    def Function_49_2472(): pass

    label("Function_49_2472")

    TalkBegin(0xFE)

    ChrTalk(    #326
        0xFE,
        (
            "#870F小雪拉普通\x02\x03",

            "#871F笑颜\x02\x03",

            "#872F苦笑\x02\x03",

            "#873F困惑\x02\x03",

            "#874F慌张（啊哇哇）\x02",
        )
    )

    Jump("loc_24DB")

    label("loc_24DB")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_49_2472 end

    def Function_50_24E0(): pass

    label("Function_50_24E0")

    TalkBegin(0xFE)

    ChrTalk(    #327
        0xFE,
        "喝～\x02",
    )

    Jump("loc_24F4")

    label("loc_24F4")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_50_24E0 end

    def Function_51_24F9(): pass

    label("Function_51_24F9")

    TalkBegin(0xFE)

    ChrTalk(    #328
        0xFE,
        "喝～\x02",
    )

    Jump("loc_250D")

    label("loc_250D")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_51_24F9 end

    def Function_52_2512(): pass

    label("Function_52_2512")

    TalkBegin(0xFE)

    ChrTalk(    #329
        0xFE,
        "#1190F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xFE,
        "#1191F闭目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_52_2512 end

    def Function_53_253D(): pass

    label("Function_53_253D")

    TalkBegin(0xFE)

    ChrTalk(    #331
        0xFE,
        "#000F普通１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        "#001F笑容\x02",
    )

    Jump("loc_2569")

    label("loc_2569")

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        "#002F认真\x02",
    )

    Jump("loc_2580")

    label("loc_2580")

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        "#003F悲哀\x02",
    )

    Jump("loc_2597")

    label("loc_2597")

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        "#004F惊愕\x02",
    )

    Jump("loc_25AE")

    label("loc_25AE")

    CloseMessageWindow()

    ChrTalk(    #336
        0xFE,
        "#005F发怒１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        "#006F普通２（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xFE,
        "#007F叹息\x02",
    )

    Jump("loc_25F3")

    label("loc_25F3")

    CloseMessageWindow()

    ChrTalk(    #339
        0xFE,
        "#008F害羞\x02",
    )

    Jump("loc_260A")

    label("loc_260A")

    CloseMessageWindow()

    ChrTalk(    #340
        0xFE,
        "#009F发怒２（唔）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xFE,
        "#500F瞑目\x02",
    )

    Jump("loc_263A")

    label("loc_263A")

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        "#501F悠闲\x02",
    )

    Jump("loc_2651")

    label("loc_2651")

    CloseMessageWindow()

    ChrTalk(    #343
        0xFE,
        "#502F哼哼\x02",
    )

    Jump("loc_2668")

    label("loc_2668")

    CloseMessageWindow()

    ChrTalk(    #344
        0xFE,
        "#503F害羞２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xFE,
        "#504F叫喊\x02",
    )

    Jump("loc_2692")

    label("loc_2692")

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        "#505F嗯～\x02",
    )

    Jump("loc_26A9")

    label("loc_26A9")

    CloseMessageWindow()

    ChrTalk(    #347
        0xFE,
        "#506F苦笑\x02",
    )

    Jump("loc_26C0")

    label("loc_26C0")

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        "#507F挑拨\x02",
    )

    Jump("loc_26D7")

    label("loc_26D7")

    CloseMessageWindow()

    ChrTalk(    #349
        0xFE,
        "#508F笑容２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        "#509F眯缝眼\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        "#580F严重惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xFE,
        "#581F苦痛\x02",
    )

    Jump("loc_2729")

    label("loc_2729")

    CloseMessageWindow()

    ChrTalk(    #353
        0xFE,
        "#582F叫喊２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xFE,
        "#583F怒泣(ED用)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xFE,
        "#584F吃药后１(ED用)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xFE,
        "#585F吃药后２(ED用)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xFE,
        "#586F苦笑２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xFE,
        "#587F空虚悲伤惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0xFE,
        "#588F悲哀２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xFE,
        "#589F号泣\x02",
    )

    Jump("loc_27DF")

    label("loc_27DF")

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_53_253D end

    def Function_54_27E4(): pass

    label("Function_54_27E4")

    TalkBegin(0xFE)

    ChrTalk(    #361
        0xFE,
        "#010F普通\x02",
    )

    Jump("loc_27FD")

    label("loc_27FD")

    CloseMessageWindow()

    ChrTalk(    #362
        0xFE,
        "#011F笑容１（有企图）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xFE,
        "#012F认真\x02",
    )

    Jump("loc_2831")

    label("loc_2831")

    CloseMessageWindow()

    ChrTalk(    #364
        0xFE,
        "#013F悲哀\x02",
    )

    Jump("loc_2848")

    label("loc_2848")

    CloseMessageWindow()

    ChrTalk(    #365
        0xFE,
        "#014F惊愕\x02",
    )

    Jump("loc_285F")

    label("loc_285F")

    CloseMessageWindow()

    ChrTalk(    #366
        0xFE,
        "#015F瞑目\x02",
    )

    Jump("loc_2876")

    label("loc_2876")

    CloseMessageWindow()

    ChrTalk(    #367
        0xFE,
        "#016F发怒\x02",
    )

    Jump("loc_288D")

    label("loc_288D")

    CloseMessageWindow()

    ChrTalk(    #368
        0xFE,
        "#017F叹息\x02",
    )

    Jump("loc_28A4")

    label("loc_28A4")

    CloseMessageWindow()

    ChrTalk(    #369
        0xFE,
        "#018F害羞（发牢骚）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xFE,
        "#019F笑容２（发怒）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xFE,
        "#510F杀意\x02",
    )

    Jump("loc_28F1")

    label("loc_28F1")

    CloseMessageWindow()

    ChrTalk(    #372
        0xFE,
        "#511F真的害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xFE,
        "#512F笑容３\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0xFE,
        "#513F苦痛\x02",
    )

    Jump("loc_2930")

    label("loc_2930")

    CloseMessageWindow()

    ChrTalk(    #375
        0xFE,
        "#514F暗示解除\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xFE,
        "#515F暗示解除后叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xFE,
        "#516F暗示解除后发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xFE,
        "#517FED笑容４\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0xFE,
        "#518FED普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xFE,
        "#519FED低头\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        "#590FED低头惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xFE,
        "#591F暗示解除后叫喊２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xFE,
        "#592FED笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0xFE,
        "#593FED瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_54_27E4 end

    def Function_55_2A11(): pass

    label("Function_55_2A11")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x383), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A79")
    EventBegin(0x0)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #385
        0x0,
        "使用道具试试哦！\x02",
    )

    Sleep(500)
    EventEnd(0x0)

    label("loc_2A79")

    Return()

    # Function_55_2A11 end

    SaveToFile()

Try(main)
