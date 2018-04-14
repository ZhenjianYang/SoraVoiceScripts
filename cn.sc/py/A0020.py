from ED6SCScenarioHelper import *

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
        EntryFunctionIndex  = 54,
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
        '03180 库拉茨',                         # 23
        '03190 卡露娜',                         # 24
        '03200 没有纹章的约修亚',               # 25
        '03210 礼服科洛丝',                     # 26
        '03500 瘦狼瓦鲁特',                     # 27
        '03510 歼灭天使玲',                     # 28
        '03520 幻惑之铃露茜奥拉',               # 29
        '03530 布卢布兰伯爵',                   # 30
        '03540 剑帝莱恩哈特',                   # 31
        '03550 研究服怀斯曼',                   # 32
        '03560 机器约修亚',                     # 33
        '03570 穆拉',                           # 34
        '03580 尤莉亚上尉',                     # 35
        '03590 希德中校',                       # 36
        '03600 小丑肯帕雷拉',                   # 37
        '03610 强化猎兵A',                      # 38
        '03620 强化猎兵B',                      # 39
        '03630 猎兵克鲁茨',                     # 40
        '03640 猎兵卡露娜',                     # 41
        '03650 强化猎兵约修亚',                 # 42
        '03670 军服卡西乌斯',                   # 43
        '03680 军服奥利维尔',                   # 44
        '03690 投狱版理查德',                   # 45
        '03700 赛克斯中将',                     # 46
        '03710 达维尔帝国大使',                 # 47
        '03720 鲁伊泽共和国大使',               # 48
        '03730 帝国兵',                         # 49
        '03740 莱娜·布莱特',                   # 50
        '03750 猎兵基尔巴特',                   # 51
        '03760 多伦',                           # 52
        '03770 吉尔',                           # 53
        '03780 １３岁雪拉',                     # 54
        '03790 斯丁克',                         # 55
        '03800 帝国兵有武器Ａ',                 # 56
        '03810 帝国兵有武器Ｂ',                 # 57
        '03820 猎兵库拉茨',                     # 58
        'CH00000前篇艾丝蒂尔',                  # 59
        'CH00010前篇约修亚',                    # 60
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
        'ED6_DT27/CH03000 ._CH',             # 00
        'ED6_DT27/CH03010 ._CH',             # 01
        'ED6_DT27/CH03020 ._CH',             # 02
        'ED6_DT27/CH03030 ._CH',             # 03
        'ED6_DT27/CH03040 ._CH',             # 04
        'ED6_DT27/CH03050 ._CH',             # 05
        'ED6_DT27/CH03060 ._CH',             # 06
        'ED6_DT27/CH03070 ._CH',             # 07
        'ED6_DT27/CH03080 ._CH',             # 08
        'ED6_DT27/CH03090 ._CH',             # 09
        'ED6_DT27/CH03100 ._CH',             # 0A
        'ED6_DT27/CH03110 ._CH',             # 0B
        'ED6_DT27/CH03120 ._CH',             # 0C
        'ED6_DT27/CH03130 ._CH',             # 0D
        'ED6_DT07/CH00000 ._CH',             # 0E
        'ED6_DT07/CH00010 ._CH',             # 0F
        'ED6_DT27/CH03200 ._CH',             # 10
        'ED6_DT27/CH03210 ._CH',             # 11
        'ED6_DT07/CH01260 ._CH',             # 12
        'ED6_DT07/CH01240 ._CH',             # 13
        'ED6_DT27/CH03500 ._CH',             # 14
        'ED6_DT27/CH03510 ._CH',             # 15
        'ED6_DT27/CH03520 ._CH',             # 16
        'ED6_DT27/CH03530 ._CH',             # 17
        'ED6_DT27/CH03540 ._CH',             # 18
        'ED6_DT27/CH03550 ._CH',             # 19
        'ED6_DT27/CH03560 ._CH',             # 1A
        'ED6_DT27/CH03570 ._CH',             # 1B
        'ED6_DT27/CH03580 ._CH',             # 1C
        'ED6_DT27/CH03590 ._CH',             # 1D
        'ED6_DT27/CH03600 ._CH',             # 1E
        'ED6_DT27/CH03610 ._CH',             # 1F
        'ED6_DT27/CH03620 ._CH',             # 20
        'ED6_DT27/CH03630 ._CH',             # 21
        'ED6_DT27/CH03640 ._CH',             # 22
        'ED6_DT27/CH03650 ._CH',             # 23
        'ED6_DT27/CH03210 ._CH',             # 24
        'ED6_DT27/CH03670 ._CH',             # 25
        'ED6_DT27/CH03680 ._CH',             # 26
        'ED6_DT27/CH03690 ._CH',             # 27
        'ED6_DT27/CH03700 ._CH',             # 28
        'ED6_DT27/CH03710 ._CH',             # 29
        'ED6_DT27/CH03720 ._CH',             # 2A
        'ED6_DT27/CH03730 ._CH',             # 2B
        'ED6_DT27/CH03740 ._CH',             # 2C
        'ED6_DT27/CH03750 ._CH',             # 2D
        'ED6_DT27/CH03760 ._CH',             # 2E
        'ED6_DT27/CH03770 ._CH',             # 2F
        'ED6_DT27/CH03780 ._CH',             # 30
        'ED6_DT27/CH03790 ._CH',             # 31
        'ED6_DT27/CH03800 ._CH',             # 32
        'ED6_DT27/CH03810 ._CH',             # 33
        'ED6_DT27/CH03820 ._CH',             # 34
    )

    AddCharChipPat(
        'ED6_DT27/CH03000P._CP',             # 00
        'ED6_DT27/CH03010P._CP',             # 01
        'ED6_DT27/CH03020P._CP',             # 02
        'ED6_DT27/CH03030P._CP',             # 03
        'ED6_DT27/CH03040P._CP',             # 04
        'ED6_DT27/CH03050P._CP',             # 05
        'ED6_DT27/CH03060P._CP',             # 06
        'ED6_DT27/CH03070P._CP',             # 07
        'ED6_DT27/CH03080P._CP',             # 08
        'ED6_DT27/CH03090P._CP',             # 09
        'ED6_DT27/CH03100P._CP',             # 0A
        'ED6_DT27/CH03110P._CP',             # 0B
        'ED6_DT27/CH03120P._CP',             # 0C
        'ED6_DT27/CH03130P._CP',             # 0D
        'ED6_DT07/CH00000P._CP',             # 0E
        'ED6_DT07/CH00010P._CP',             # 0F
        'ED6_DT27/CH03200P._CP',             # 10
        'ED6_DT27/CH03210P._CP',             # 11
        'ED6_DT07/CH01260P._CP',             # 12
        'ED6_DT07/CH01240P._CP',             # 13
        'ED6_DT27/CH03500P._CP',             # 14
        'ED6_DT27/CH03510P._CP',             # 15
        'ED6_DT27/CH03520P._CP',             # 16
        'ED6_DT27/CH03530P._CP',             # 17
        'ED6_DT27/CH03540P._CP',             # 18
        'ED6_DT27/CH03550P._CP',             # 19
        'ED6_DT27/CH03560P._CP',             # 1A
        'ED6_DT27/CH03570P._CP',             # 1B
        'ED6_DT27/CH03580P._CP',             # 1C
        'ED6_DT27/CH03590P._CP',             # 1D
        'ED6_DT27/CH03600P._CP',             # 1E
        'ED6_DT27/CH03610P._CP',             # 1F
        'ED6_DT27/CH03620P._CP',             # 20
        'ED6_DT27/CH03630P._CP',             # 21
        'ED6_DT27/CH03640P._CP',             # 22
        'ED6_DT27/CH03650P._CP',             # 23
        'ED6_DT27/CH03210P._CP',             # 24
        'ED6_DT27/CH03670P._CP',             # 25
        'ED6_DT27/CH03680P._CP',             # 26
        'ED6_DT27/CH03690P._CP',             # 27
        'ED6_DT27/CH03700P._CP',             # 28
        'ED6_DT27/CH03710P._CP',             # 29
        'ED6_DT27/CH03720P._CP',             # 2A
        'ED6_DT27/CH03730P._CP',             # 2B
        'ED6_DT27/CH03740P._CP',             # 2C
        'ED6_DT27/CH03750P._CP',             # 2D
        'ED6_DT27/CH03760P._CP',             # 2E
        'ED6_DT27/CH03770P._CP',             # 2F
        'ED6_DT27/CH03780P._CP',             # 30
        'ED6_DT27/CH03790P._CP',             # 31
        'ED6_DT27/CH03800P._CP',             # 32
        'ED6_DT27/CH03810P._CP',             # 33
        'ED6_DT27/CH03820P._CP',             # 34
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
        Y                   = 28000,
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
        X                   = 8000,
        Z                   = 0,
        Y                   = 32000,
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
        Y                   = 36000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 0,
        Y                   = 4000,
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
        X                   = 12000,
        Z                   = 0,
        Y                   = 8000,
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
        Y                   = 12000,
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
        Y                   = 16000,
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
        Y                   = 20000,
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
        Y                   = 24000,
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
        Y                   = 28000,
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
        Y                   = 32000,
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
        Y                   = 36000,
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
        Y                   = 40000,
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
        X                   = 16000,
        Z                   = 0,
        Y                   = 4000,
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
        Y                   = 8000,
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
        Y                   = 12000,
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
        Y                   = 16000,
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
        Y                   = 20000,
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
        Y                   = 24000,
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
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 37,
        ChipIndex           = 0x25,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 37,
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
        TalkScenaIndex      = 38,
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
        TalkScenaIndex      = 39,
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
        TalkScenaIndex      = 40,
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
        TalkScenaIndex      = 41,
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
        TalkScenaIndex      = 42,
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
        TalkScenaIndex      = 43,
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
        TalkScenaIndex      = 44,
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
        TalkScenaIndex      = 45,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 28000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 46,
        ChipIndex           = 0x2E,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 46,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 32000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 47,
        ChipIndex           = 0x2F,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 47,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 36000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 48,
        ChipIndex           = 0x30,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 48,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 40000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 49,
        ChipIndex           = 0x31,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 50,
        ChipIndex           = 0x32,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 49,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 8000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 51,
        ChipIndex           = 0x33,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 50,
    )

    DeclNpc(
        X                   = 24000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 52,
        ChipIndex           = 0x34,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 51,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 0,
        Y                   = 4000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 52,
    )

    DeclNpc(
        X                   = 2000,
        Z                   = 0,
        Y                   = 8000,
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


    ScpFunction(
        "Function_0_8D2",          # 00, 0
        "Function_1_8D8",          # 01, 1
        "Function_2_8D9",          # 02, 2
        "Function_3_8EA",          # 03, 3
        "Function_4_AED",          # 04, 4
        "Function_5_C64",          # 05, 5
        "Function_6_CC5",          # 06, 6
        "Function_7_D62",          # 07, 7
        "Function_8_E47",          # 08, 8
        "Function_9_F35",          # 09, 9
        "Function_10_100B",        # 0A, 10
        "Function_11_108A",        # 0B, 11
        "Function_12_1157",        # 0C, 12
        "Function_13_1264",        # 0D, 13
        "Function_14_127A",        # 0E, 14
        "Function_15_1290",        # 0F, 15
        "Function_16_13B9",        # 10, 16
        "Function_17_1447",        # 11, 17
        "Function_18_14AE",        # 12, 18
        "Function_19_152D",        # 13, 19
        "Function_20_15AC",        # 14, 20
        "Function_21_1661",        # 15, 21
        "Function_22_176A",        # 16, 22
        "Function_23_17CD",        # 17, 23
        "Function_24_1830",        # 18, 24
        "Function_25_1846",        # 19, 25
        "Function_26_18B1",        # 1A, 26
        "Function_27_18C8",        # 1B, 27
        "Function_28_18DE",        # 1C, 28
        "Function_29_18F4",        # 1D, 29
        "Function_30_190A",        # 1E, 30
        "Function_31_195C",        # 1F, 31
        "Function_32_196D",        # 20, 32
        "Function_33_197E",        # 21, 33
        "Function_34_19E5",        # 22, 34
        "Function_35_1A1C",        # 23, 35
        "Function_36_1AA7",        # 24, 36
        "Function_37_1B0E",        # 25, 37
        "Function_38_1B95",        # 26, 38
        "Function_39_1C3C",        # 27, 39
        "Function_40_1C93",        # 28, 40
        "Function_41_1D01",        # 29, 41
        "Function_42_1D4E",        # 2A, 42
        "Function_43_1DA5",        # 2B, 43
        "Function_44_1DB6",        # 2C, 44
        "Function_45_1E2E",        # 2D, 45
        "Function_46_1EC9",        # 2E, 46
        "Function_47_1EDF",        # 2F, 47
        "Function_48_1EF5",        # 30, 48
        "Function_49_1F47",        # 31, 49
        "Function_50_1F58",        # 32, 50
        "Function_51_1F69",        # 33, 51
        "Function_52_1F90",        # 34, 52
        "Function_53_21A1",        # 35, 53
        "Function_54_236C",        # 36, 54
    )


    def Function_0_8D2(): pass

    label("Function_0_8D2")

    OP_3E(0x383, 1)
    Return()

    # Function_0_8D2 end

    def Function_1_8D8(): pass

    label("Function_1_8D8")

    Return()

    # Function_1_8D8 end

    def Function_2_8D9(): pass

    label("Function_2_8D9")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_2_8D9 end

    def Function_3_8EA(): pass

    label("Function_3_8EA")

    TalkBegin(0xFE)

    ChrTalk(    #1
        0xFE,
        "#1000F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "#1001F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "#1002F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "#1003F悲哀１\x02",
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

    # Function_3_8EA end

    def Function_4_AED(): pass

    label("Function_4_AED")

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
        "#1031F笑颜Ａ\x02",
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

    # Function_4_AED end

    def Function_5_C64(): pass

    label("Function_5_C64")

    TalkBegin(0xFE)

    ChrTalk(    #48
        0xFE,
        "#020F通常\x02",
    )

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

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_C64 end

    def Function_6_CC5(): pass

    label("Function_6_CC5")

    TalkBegin(0xFE)

    ChrTalk(    #50
        0xFE,
        "#030F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "#031F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "#032F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "#033F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "#034F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "#035F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "#036F慌张\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "#037F喝醉\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "#038F烂醉\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "#039F痛苦\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_CC5 end

    def Function_7_D62(): pass

    label("Function_7_D62")

    TalkBegin(0xFE)

    ChrTalk(    #60
        0xFE,
        "#040F通常\x02",
    )

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

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "#045F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "#046F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "#047F瞑目\x02",
    )

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

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "#541F痛苦\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "#542F苦笑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_D62 end

    def Function_8_E47(): pass

    label("Function_8_E47")

    TalkBegin(0xFE)

    ChrTalk(    #73
        0xFE,
        "#050F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "#051F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "#052F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "#053F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "#054F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "#055F困惑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "#056F痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "#057F杀意\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "#058F毒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "#059F苦痛\x02",
    )

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

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "#553F空虚\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "#554F空虚微笑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_E47 end

    def Function_9_F35(): pass

    label("Function_9_F35")

    TalkBegin(0xFE)

    ChrTalk(    #88
        0xFE,
        "#060F通常１\x02",
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

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "#063F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "#064F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "#065F困惑\x02",
    )

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

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "#068F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "#069F哭泣\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "#560F通常２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "#561F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        "#562F害羞困惑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_F35 end

    def Function_10_100B(): pass

    label("Function_10_100B")

    TalkBegin(0xFE)

    ChrTalk(    #101
        0xFE,
        "#070F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "#071F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "#072F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "#073F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "#074F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "#075F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "#076F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "#077F痛苦\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_100B end

    def Function_11_108A(): pass

    label("Function_11_108A")

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

    # Function_11_108A end

    def Function_12_1157(): pass

    label("Function_12_1157")

    TalkBegin(0xFE)

    ChrTalk(    #121
        0xFE,
        "#810F普通\x02",
    )

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

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "#813F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "#814F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "#815F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "#816F自信\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "#817F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "#818F嗯～\x02",
    )

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

    # Function_12_1157 end

    def Function_13_1264(): pass

    label("Function_13_1264")

    TalkBegin(0xFE)

    ChrTalk(    #137
        0xFE,
        "#210F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1264 end

    def Function_14_127A(): pass

    label("Function_14_127A")

    TalkBegin(0xFE)

    ChrTalk(    #138
        0xFE,
        "#110F通常\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_127A end

    def Function_15_1290(): pass

    label("Function_15_1290")

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

    # Function_15_1290 end

    def Function_16_13B9(): pass

    label("Function_16_13B9")

    TalkBegin(0xFE)

    ChrTalk(    #154
        0xFE,
        "#840F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "#841F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        "#842F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "#843F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        "#844F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "#845F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        "#846F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "#847F痛苦\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        "#848F空虚\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_13B9 end

    def Function_17_1447(): pass

    label("Function_17_1447")

    TalkBegin(0xFE)

    ChrTalk(    #163
        0xFE,
        "#1160F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        "#1161F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "#1162F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        "#1163F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        "#1164F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        "#1165F闭目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_1447 end

    def Function_18_14AE(): pass

    label("Function_18_14AE")

    TalkBegin(0xFE)

    ChrTalk(    #169
        0xFE,
        "#820F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "#821F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        "#822F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        "#823F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        "#824F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        "#825F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        "#826F痛苦\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "#827F空虚\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_14AE end

    def Function_19_152D(): pass

    label("Function_19_152D")

    TalkBegin(0xFE)

    ChrTalk(    #177
        0xFE,
        "#830F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        "#831F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xFE,
        "#832F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "#833F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        "#834F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "#835F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        "#836F痛苦\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        "#837F空虚\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_152D end

    def Function_20_15AC(): pass

    label("Function_20_15AC")

    TalkBegin(0xFE)

    ChrTalk(    #185
        0xFE,
        "#250F普通（无目）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        "#251F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        "#252F笑颜（无目）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        "#253F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        "#254F认真（无目）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "#255F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        "#256F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        "#257F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        "#258F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "#259F痛苦\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_15AC end

    def Function_21_1661(): pass

    label("Function_21_1661")

    TalkBegin(0xFE)

    ChrTalk(    #195
        0xFE,
        "#260F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        "#261F笑颜１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        "#262F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        "#263F察觉到的脸\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        "#264F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        "#265F笑颜２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        "#266F愠怒的脸\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        "#267F嗯～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        "#268F有企图的脸\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        "#269F有企图的笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "#1300F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        "#1301F愤怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "#1302F杀意\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        "#1303F痛苦\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "#1304F微笑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_1661 end

    def Function_22_176A(): pass

    label("Function_22_176A")

    TalkBegin(0xFE)

    ChrTalk(    #210
        0xFE,
        "#240F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "#241F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "#242F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        "#243F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        "#244F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        "#245F痛苦？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_176A end

    def Function_23_17CD(): pass

    label("Function_23_17CD")

    TalkBegin(0xFE)

    ChrTalk(    #216
        0xFE,
        "#230F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        "#231F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        "#232F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xFE,
        "#233F惊愕？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        "#234F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xFE,
        "#235F痛苦\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_17CD end

    def Function_24_1830(): pass

    label("Function_24_1830")

    TalkBegin(0xFE)

    ChrTalk(    #222
        0xFE,
        "#120F嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_1830 end

    def Function_25_1846(): pass

    label("Function_25_1846")

    TalkBegin(0xFE)

    ChrTalk(    #223
        0xFE,
        "#1150F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        "#1151F笑颜１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        "#1152F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        "#1153F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        "#1154F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        "#1155F笑颜２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_1846 end

    def Function_26_18B1(): pass

    label("Function_26_18B1")

    TalkBegin(0xFE)

    ChrTalk(    #229
        0xFE,
        "#1140F嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_18B1 end

    def Function_27_18C8(): pass

    label("Function_27_18C8")

    TalkBegin(0xFE)

    ChrTalk(    #230
        0xFE,
        "#270F嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_18C8 end

    def Function_28_18DE(): pass

    label("Function_28_18DE")

    TalkBegin(0xFE)

    ChrTalk(    #231
        0xFE,
        "#170F嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_18DE end

    def Function_29_18F4(): pass

    label("Function_29_18F4")

    TalkBegin(0xFE)

    ChrTalk(    #232
        0xFE,
        "#700F嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_18F4 end

    def Function_30_190A(): pass

    label("Function_30_190A")

    TalkBegin(0xFE)

    ChrTalk(    #233
        0xFE,
        "#850F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        "#851F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        "#852F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        "#853F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        "#854F微笑\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_190A end

    def Function_31_195C(): pass

    label("Function_31_195C")

    TalkBegin(0xFE)

    ChrTalk(    #238
        0xFE,
        "嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_195C end

    def Function_32_196D(): pass

    label("Function_32_196D")

    TalkBegin(0xFE)

    ChrTalk(    #239
        0xFE,
        "嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_196D end

    def Function_33_197E(): pass

    label("Function_33_197E")

    TalkBegin(0xFE)

    ChrTalk(    #240
        0xFE,
        "#1210F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        "#1211F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        "#1212F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        "#1213F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        "#1190F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "#1191F闭目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_197E end

    def Function_34_19E5(): pass

    label("Function_34_19E5")

    TalkBegin(0xFE)

    ChrTalk(    #246
        0xFE,
        "#1200F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        "#1201F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        "#1202F闭目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_19E5 end

    def Function_35_1A1C(): pass

    label("Function_35_1A1C")

    TalkBegin(0xFE)

    ChrTalk(    #249
        0xFE,
        "#1130F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        "#1131F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        "#1132F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        "#1133F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        "#1134F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        "#1135F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        "#1136F悲哀２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        "#1137F笑颜２\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_1A1C end

    def Function_36_1AA7(): pass

    label("Function_36_1AA7")

    TalkBegin(0xFE)

    ChrTalk(    #257
        0xFE,
        "#1160F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        "#1161F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        "#1162F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "#1163F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        "#1164F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        "#1165F闭目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_1AA7 end

    def Function_37_1B0E(): pass

    label("Function_37_1B0E")

    TalkBegin(0xFE)

    ChrTalk(    #263
        0xFE,
        "#1120F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        "#1121F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        "#1122F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        "#1123F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "#1124F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        "#1125F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        "#1126F愤怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        "#1127F叫喊\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_37_1B0E end

    def Function_38_1B95(): pass

    label("Function_38_1B95")

    TalkBegin(0xFE)

    ChrTalk(    #271
        0xFE,
        "#890F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        "#891F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        "#892F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        "#893F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        "#894F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        "#895F恶普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        "#896F恶笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xFE,
        "#897F恶认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        "#898F恶惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        "#899F恶闭目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_38_1B95 end

    def Function_39_1C3C(): pass

    label("Function_39_1C3C")

    TalkBegin(0xFE)

    ChrTalk(    #281
        0xFE,
        "#1170F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        "#1171F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xFE,
        "#1172F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "#1173F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        "#1174F悲哀\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_1C3C end

    def Function_40_1C93(): pass

    label("Function_40_1C93")

    TalkBegin(0xFE)

    ChrTalk(    #286
        0xFE,
        "#880F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        "#881F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        "#882F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        "#883F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        "#884F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        "#885F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xFE,
        "#886F啧\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_40_1C93 end

    def Function_41_1D01(): pass

    label("Function_41_1D01")

    TalkBegin(0xFE)

    ChrTalk(    #293
        0xFE,
        "#1100F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        "#1101F认真·惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "#1102F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        "#1103F叫喊\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_1D01 end

    def Function_42_1D4E(): pass

    label("Function_42_1D4E")

    TalkBegin(0xFE)

    ChrTalk(    #297
        0xFE,
        "#1110F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        "#1111F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        "#1112F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        "#1113F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        "#1114F叫喊\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_42_1D4E end

    def Function_43_1DA5(): pass

    label("Function_43_1DA5")

    TalkBegin(0xFE)

    ChrTalk(    #302
        0xFE,
        "嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_43_1DA5 end

    def Function_44_1DB6(): pass

    label("Function_44_1DB6")

    TalkBegin(0xFE)

    ChrTalk(    #303
        0xFE,
        "#860F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        "#861F笑颜１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xFE,
        "#862F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        "#863F闭目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xFE,
        "#864F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        "#865F笑颜２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        "#866F女孩笑颜\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_44_1DB6 end

    def Function_45_1E2E(): pass

    label("Function_45_1E2E")

    TalkBegin(0xFE)

    ChrTalk(    #310
        0xFE,
        "#1220F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        "#1221F笑颜\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xFE,
        "#1222F真剑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        "#1223F悲哀（转移视线）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xFE,
        "#1224F困惑（惊愕）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        "#1225F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xFE,
        "#1226F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        "#1227F苦痛\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_1E2E end

    def Function_46_1EC9(): pass

    label("Function_46_1EC9")

    TalkBegin(0xFE)

    ChrTalk(    #318
        0xFE,
        "#190F嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_46_1EC9 end

    def Function_47_1EDF(): pass

    label("Function_47_1EDF")

    TalkBegin(0xFE)

    ChrTalk(    #319
        0xFE,
        "#200F嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_47_1EDF end

    def Function_48_1EF5(): pass

    label("Function_48_1EF5")

    TalkBegin(0xFE)

    ChrTalk(    #320
        0xFE,
        (
            "#870F小雪拉普通\x02\x03",

            "#871F笑颜\x02\x03",

            "#872F苦笑\x02\x03",

            "#873F困惑\x02\x03",

            "#874F慌张（啊哇哇）\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_48_1EF5 end

    def Function_49_1F47(): pass

    label("Function_49_1F47")

    TalkBegin(0xFE)

    ChrTalk(    #321
        0xFE,
        "嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_49_1F47 end

    def Function_50_1F58(): pass

    label("Function_50_1F58")

    TalkBegin(0xFE)

    ChrTalk(    #322
        0xFE,
        "嗷—\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_50_1F58 end

    def Function_51_1F69(): pass

    label("Function_51_1F69")

    TalkBegin(0xFE)

    ChrTalk(    #323
        0xFE,
        "#1190F普通\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        "#1191F闭目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_51_1F69 end

    def Function_52_1F90(): pass

    label("Function_52_1F90")

    TalkBegin(0xFE)

    ChrTalk(    #325
        0xFE,
        "#000F通常１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        "#001F笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0xFE,
        "#002F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xFE,
        "#003F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        "#004F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xFE,
        "#005F发怒１\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xFE,
        "#006F通常２（自信）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        "#007F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xFE,
        "#008F害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xFE,
        "#009F发怒２（唔）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        "#500F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xFE,
        "#501F悠闲\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        "#502F哼哼\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xFE,
        "#503F害羞２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xFE,
        "#504F叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xFE,
        "#505F嗯～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xFE,
        "#506F苦笑\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        "#507F挑拨\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #343
        0xFE,
        "#508F笑容２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xFE,
        "#509F眯缝眼\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xFE,
        "#580F严重惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xFE,
        "#581F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xFE,
        "#582F叫喊２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xFE,
        "#583F怒泣(ED用)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xFE,
        "#584F吃药后１(ED用)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xFE,
        "#585F吃药后２(ED用)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        "#586F苦笑２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xFE,
        "#587F空虚悲伤惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xFE,
        "#588F悲哀２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xFE,
        "#589F号泣\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_52_1F90 end

    def Function_53_21A1(): pass

    label("Function_53_21A1")

    TalkBegin(0xFE)

    ChrTalk(    #355
        0xFE,
        "#010F通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xFE,
        "#011F笑容１（有企图）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xFE,
        "#012F认真\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0xFE,
        "#013F悲哀\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0xFE,
        "#014F惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xFE,
        "#015F瞑目\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xFE,
        "#016F发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xFE,
        "#017F叹息\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xFE,
        "#018F害羞（发牢骚）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0xFE,
        "#019F笑容２（发怒）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xFE,
        "#510F杀意\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xFE,
        "#511F真的害羞\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0xFE,
        "#512F笑容３\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xFE,
        "#513F苦痛\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0xFE,
        "#514F暗示解除\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xFE,
        "#515F暗示解除后叫喊\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xFE,
        "#516F暗示解除后发怒\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0xFE,
        "#517FED笑容４\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xFE,
        "#518FED通常\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0xFE,
        "#519FED低头\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0xFE,
        "#590FED低头惊愕\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xFE,
        "#591F暗示解除后叫喊２\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0xFE,
        "#592FED笑容\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xFE,
        "#593FED瞑目\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_53_21A1 end

    def Function_54_236C(): pass

    label("Function_54_236C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x383), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23D4")
    EventBegin(0x0)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #379
        0x0,
        "使用道具试试哦！\x02",
    )

    Sleep(500)
    EventEnd(0x0)

    label("loc_23D4")

    Return()

    # Function_54_236C end

    SaveToFile()

Try(main)
