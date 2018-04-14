from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2510   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2510.x',
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
        '科林兹校长',                           # 9
        '乔儿',                                 # 10
        '汉斯',                                 # 11
        '珐奥娜',                               # 12
        '拉迪奥老师',                           # 13
        '碧欧拉老师',                           # 14
        '米丽亚老师',                           # 15
        '雪拉扎德',                             # 16
        '阿加特',                               # 17
        '罗迪',                                 # 18
        '雅莉丝',                               # 19
        '黛拉',                                 # 20
        '罗基克',                               # 21
        '塞尔玛',                               # 22
        '莉秋儿',                               # 23
        '巴托姆',                               # 24
        '基诺奇奥',                             # 25
        '妮吉塔',                               # 26
        '亚吉鲁',                               # 27
        '米克',                                 # 28
        '莫妮卡',                               # 29
        '德尼斯',                               # 30
        '蕾娜',                                 # 31
        '基尔巴特',                             # 32
        '坎诺',                                 # 33
        '帕布尔',                               # 34
        '强化猎兵',                             # 35
        '强化猎兵',                             # 36
        '强化猎兵',                             # 37
        '强化猎兵',                             # 38
        '目标用照相机',                         # 39
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
        'ED6_DT07/CH02600 ._CH',             # 00
        'ED6_DT07/CH02603 ._CH',             # 01
        'ED6_DT07/CH02390 ._CH',             # 02
        'ED6_DT07/CH02550 ._CH',             # 03
        'ED6_DT07/CH02490 ._CH',             # 04
        'ED6_DT07/CH01663 ._CH',             # 05
        'ED6_DT07/CH01210 ._CH',             # 06
        'ED6_DT07/CH01213 ._CH',             # 07
        'ED6_DT07/CH01430 ._CH',             # 08
        'ED6_DT07/CH01433 ._CH',             # 09
        'ED6_DT07/CH00020 ._CH',             # 0A
        'ED6_DT07/CH00050 ._CH',             # 0B
        'ED6_DT07/CH01360 ._CH',             # 0C
        'ED6_DT07/CH01590 ._CH',             # 0D
        'ED6_DT07/CH01370 ._CH',             # 0E
        'ED6_DT07/CH01080 ._CH',             # 0F
        'ED6_DT07/CH01090 ._CH',             # 10
        'ED6_DT07/CH01590 ._CH',             # 11
        'ED6_DT07/CH01580 ._CH',             # 12
        'ED6_DT27/CH03750 ._CH',             # 13
        'ED6_DT07/CH01580 ._CH',             # 14
        'ED6_DT07/CH01090 ._CH',             # 15
        'ED6_DT27/CH03610 ._CH',             # 16
        'ED6_DT07/CH01370 ._CH',             # 17
        'ED6_DT07/CH01360 ._CH',             # 18
        'ED6_DT07/CH01370 ._CH',             # 19
        'ED6_DT26/CH20501 ._CH',             # 1A
    )

    AddCharChipPat(
        'ED6_DT07/CH02600P._CP',             # 00
        'ED6_DT07/CH02603P._CP',             # 01
        'ED6_DT07/CH02390P._CP',             # 02
        'ED6_DT07/CH02550P._CP',             # 03
        'ED6_DT07/CH02490P._CP',             # 04
        'ED6_DT07/CH01663P._CP',             # 05
        'ED6_DT07/CH01210P._CP',             # 06
        'ED6_DT07/CH01213P._CP',             # 07
        'ED6_DT07/CH01430P._CP',             # 08
        'ED6_DT07/CH01433P._CP',             # 09
        'ED6_DT07/CH00020P._CP',             # 0A
        'ED6_DT07/CH00050P._CP',             # 0B
        'ED6_DT07/CH01360P._CP',             # 0C
        'ED6_DT07/CH01590P._CP',             # 0D
        'ED6_DT07/CH01370P._CP',             # 0E
        'ED6_DT07/CH01080P._CP',             # 0F
        'ED6_DT07/CH01090P._CP',             # 10
        'ED6_DT07/CH01590P._CP',             # 11
        'ED6_DT07/CH01580P._CP',             # 12
        'ED6_DT27/CH03750P._CP',             # 13
        'ED6_DT07/CH01580P._CP',             # 14
        'ED6_DT07/CH01090P._CP',             # 15
        'ED6_DT27/CH03610P._CP',             # 16
        'ED6_DT07/CH01370P._CP',             # 17
        'ED6_DT07/CH01360P._CP',             # 18
        'ED6_DT07/CH01370P._CP',             # 19
        'ED6_DT26/CH20501P._CP',             # 1A
    )

    DeclNpc(
        X                   = 116010,
        Z                   = 200,
        Y                   = 4800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
    )

    DeclNpc(
        X                   = 30700,
        Z                   = 0,
        Y                   = 55110,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 31,
    )

    DeclNpc(
        X                   = 41200,
        Z                   = 0,
        Y                   = 7500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
    )

    DeclNpc(
        X                   = 87640,
        Z                   = 200,
        Y                   = 2820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 89300,
        Z                   = 0,
        Y                   = 1960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 86880,
        Z                   = 0,
        Y                   = 4250,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 85540,
        Z                   = 0,
        Y                   = 4250,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 85540,
        Z                   = 0,
        Y                   = 4250,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 29880,
        Z                   = 0,
        Y                   = -280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 2630,
        Z                   = 0,
        Y                   = 1500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 37090,
        Z                   = 0,
        Y                   = 1590,
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
        X                   = 4800,
        Z                   = 250,
        Y                   = 28940,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 43890,
        Z                   = 0,
        Y                   = 34970,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 36990,
        Z                   = 0,
        Y                   = 30690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 47460,
        Z                   = 0,
        Y                   = 32880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 93000,
        Z                   = 0,
        Y                   = 31990,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 95320,
        Z                   = 250,
        Y                   = 33480,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 44150,
        Z                   = 0,
        Y                   = 270,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -4120,
        Z                   = 0,
        Y                   = 5200,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 28,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 29,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 30,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 32,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 33,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 51000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 83,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 84,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 1400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 85,
    )

    DeclEvent(
        X                   = 58990,
        Y                   = 0,
        Z                   = 31330,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 86,
    )

    DeclEvent(
        X                   = 33000,
        Y                   = 0,
        Z                   = 31400,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 87,
    )


    DeclActor(
        TriggerX            = 41150,
        TriggerZ            = 0,
        TriggerY            = 5500,
        TriggerRange        = 400,
        ActorX              = 41200,
        ActorZ              = 1700,
        ActorY              = 7500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 26,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 116010,
        TriggerZ            = 0,
        TriggerY            = 2750,
        TriggerRange        = 400,
        ActorX              = 116010,
        ActorZ              = 1700,
        ActorY              = 4800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 51020,
        TriggerZ            = 0,
        TriggerY            = 31860,
        TriggerRange        = 800,
        ActorX              = 51020,
        ActorZ              = 1500,
        ActorY              = 31860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 82,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_66E",          # 00, 0
        "Function_1_DB4",          # 01, 1
        "Function_2_E4E",          # 02, 2
        "Function_3_E72",          # 03, 3
        "Function_4_E96",          # 04, 4
        "Function_5_EBA",          # 05, 5
        "Function_6_EDE",          # 06, 6
        "Function_7_FB3",          # 07, 7
        "Function_8_FD7",          # 08, 8
        "Function_9_16FD",         # 09, 9
        "Function_10_17FF",        # 0A, 10
        "Function_11_1A5A",        # 0B, 11
        "Function_12_1D0F",        # 0C, 12
        "Function_13_1F6E",        # 0D, 13
        "Function_14_28C7",        # 0E, 14
        "Function_15_2DBD",        # 0F, 15
        "Function_16_308F",        # 10, 16
        "Function_17_37F3",        # 11, 17
        "Function_18_3A1F",        # 12, 18
        "Function_19_3C94",        # 13, 19
        "Function_20_3DFC",        # 14, 20
        "Function_21_401C",        # 15, 21
        "Function_22_40C0",        # 16, 22
        "Function_23_4162",        # 17, 23
        "Function_24_4431",        # 18, 24
        "Function_25_4AB7",        # 19, 25
        "Function_26_4D59",        # 1A, 26
        "Function_27_4FDF",        # 1B, 27
        "Function_28_5683",        # 1C, 28
        "Function_29_5711",        # 1D, 29
        "Function_30_5766",        # 1E, 30
        "Function_31_5869",        # 1F, 31
        "Function_32_58C4",        # 20, 32
        "Function_33_5A04",        # 21, 33
        "Function_34_5BFC",        # 22, 34
        "Function_35_63BA",        # 23, 35
        "Function_36_68C3",        # 24, 36
        "Function_37_6963",        # 25, 37
        "Function_38_69EB",        # 26, 38
        "Function_39_6C37",        # 27, 39
        "Function_40_6F17",        # 28, 40
        "Function_41_7410",        # 29, 41
        "Function_42_7419",        # 2A, 42
        "Function_43_786B",        # 2B, 43
        "Function_44_79A0",        # 2C, 44
        "Function_45_79A9",        # 2D, 45
        "Function_46_7DB9",        # 2E, 46
        "Function_47_7EEE",        # 2F, 47
        "Function_48_7EF7",        # 30, 48
        "Function_49_82BC",        # 31, 49
        "Function_50_83F1",        # 32, 50
        "Function_51_8440",        # 33, 51
        "Function_52_8494",        # 34, 52
        "Function_53_84E8",        # 35, 53
        "Function_54_853C",        # 36, 54
        "Function_55_8B71",        # 37, 55
        "Function_56_8BD4",        # 38, 56
        "Function_57_8C3C",        # 39, 57
        "Function_58_8CA4",        # 3A, 58
        "Function_59_8CF8",        # 3B, 59
        "Function_60_9602",        # 3C, 60
        "Function_61_964A",        # 3D, 61
        "Function_62_9697",        # 3E, 62
        "Function_63_96E4",        # 3F, 63
        "Function_64_9731",        # 40, 64
        "Function_65_973A",        # 41, 65
        "Function_66_9C41",        # 42, 66
        "Function_67_9D73",        # 43, 67
        "Function_68_9DBE",        # 44, 68
        "Function_69_9E1D",        # 45, 69
        "Function_70_9E68",        # 46, 70
        "Function_71_9EC7",        # 47, 71
        "Function_72_A5AB",        # 48, 72
        "Function_73_A5FA",        # 49, 73
        "Function_74_A64E",        # 4A, 74
        "Function_75_A6A2",        # 4B, 75
        "Function_76_A6F6",        # 4C, 76
        "Function_77_ADE0",        # 4D, 77
        "Function_78_AE2F",        # 4E, 78
        "Function_79_AE83",        # 4F, 79
        "Function_80_AED7",        # 50, 80
        "Function_81_AF2B",        # 51, 81
        "Function_82_AFC4",        # 52, 82
        "Function_83_B050",        # 53, 83
        "Function_84_B054",        # 54, 84
        "Function_85_B058",        # 55, 85
        "Function_86_B05C",        # 56, 86
        "Function_87_B060",        # 57, 87
    )


    def Function_0_66E(): pass

    label("Function_0_66E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_72E")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrPos(0x20, -1060, 0, 2530, 180)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x21, -1080, 0, 1310, 0)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x15, -3670, 0, 33860, 90)
    SetChrPos(0x16, 2300, 0, 34190, 180)
    ClearChrFlags(0x16, 0x80)
    OP_43(0x16, 0x0, 0x6, 0x2)
    SetChrPos(0x18, 92160, 0, 34030, 0)
    SetChrPos(0x19, 92160, 0, 35490, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71F")
    SetChrFlags(0x18, 0x10)
    Jump("loc_726")

    label("loc_71F")

    OP_8C(0x19, 0, 0)

    label("loc_726")

    SetChrFlags(0x19, 0x10)
    Jump("loc_C31")

    label("loc_72E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_A47")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrPos(0xB, 114760, 0, 5010, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_END)), "loc_79A")
    SetChrPos(0xA, 3470, 0, 2580, 180)
    SetChrPos(0x9, 3500, 0, 1470, 0)
    Jump("loc_7BC")

    label("loc_79A")

    SetChrPos(0xA, 3470, 0, 2580, 270)
    SetChrPos(0x9, 3500, 0, 1470, 270)

    label("loc_7BC")

    SetChrPos(0x20, -240, 0, 3050, 90)
    SetChrPos(0x12, -550, 0, 1740, 90)
    SetChrPos(0x21, 350, 0, 1140, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_43(0x12, 0x0, 0x6, 0x2)
    SetChrPos(0x14, 260, 0, 32820, 225)
    SetChrPos(0x1A, 170, 0, 30840, 0)
    SetChrPos(0x15, -1090, 0, 33310, 180)
    SetChrPos(0x1C, -1100, 0, 31200, 45)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x18, 92640, 0, 35500, 0)
    SetChrPos(0x17, 91490, 0, 35490, 0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 1)), scpexpr(EXPR_END)), "loc_8B0")
    SetChrPos(0x1D, 94990, 250, 35500, 233)
    SetChrPos(0x1E, 94520, 250, 33430, 270)
    Jump("loc_8D2")

    label("loc_8B0")

    SetChrPos(0x1D, 94550, 250, 34350, 180)
    SetChrPos(0x1E, 94520, 250, 33430, 0)

    label("loc_8D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x416, 7)), scpexpr(EXPR_END)), "loc_930")
    SetChrPos(0x22, 42290, 0, 3240, 180)
    SetChrPos(0x23, 39710, 0, 1520, 180)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x2)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 10)
    ClearChrFlags(0x23, 0x1)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 26)
    SetChrSubChip(0x23, 13)
    Jump("loc_9E9")

    label("loc_930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 0)), scpexpr(EXPR_END)), "loc_98E")
    SetChrPos(0x22, 54400, 0, 970, 90)
    SetChrPos(0x23, 55400, 0, -1460, 90)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x2)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 9)
    ClearChrFlags(0x23, 0x1)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 26)
    SetChrSubChip(0x23, 12)
    Jump("loc_9E9")

    label("loc_98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 1)), scpexpr(EXPR_END)), "loc_9E9")
    SetChrPos(0x22, 28800, 0, 700, 270)
    SetChrPos(0x23, 29240, 0, -1490, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x2)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 10)
    ClearChrFlags(0x23, 0x1)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 26)
    SetChrSubChip(0x23, 12)

    label("loc_9E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 7)), scpexpr(EXPR_END)), "loc_A44")
    SetChrPos(0x24, 39960, 0, 29850, 0)
    SetChrPos(0x25, 42350, 0, 29860, 0)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x24, 0x1)
    SetChrFlags(0x24, 0x2)
    SetChrChipByIndex(0x24, 26)
    SetChrSubChip(0x24, 10)
    ClearChrFlags(0x25, 0x1)
    SetChrFlags(0x25, 0x2)
    SetChrChipByIndex(0x25, 26)
    SetChrSubChip(0x25, 13)

    label("loc_A44")

    Jump("loc_C31")

    label("loc_A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_AF2")
    SetChrPos(0xD, 5370, 250, 33230, 90)
    SetChrPos(0xE, 84100, 0, 4951, 0)
    SetChrPos(0x14, -3980, 0, 35495, 0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrPos(0x13, 43530, 0, 1620, 270)
    OP_43(0x13, 0x0, 0x0, 0x2)
    SetChrPos(0x1A, 38230, 0, 1730, 180)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x19, 86480, 0, 28510, 270)
    SetChrPos(0x18, 85350, 0, 28510, 90)
    SetChrFlags(0x19, 0x10)
    Jump("loc_C31")

    label("loc_AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_AFC")
    Jump("loc_C31")

    label("loc_AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_BBA")
    SetChrPos(0x18, 88900, 0, 34610, 180)
    SetChrPos(0x19, 88910, 0, 33380, 0)
    SetChrFlags(0x19, 0x10)
    SetChrFlags(0x18, 0x10)
    SetChrPos(0x17, 92170, 0, 30030, 270)
    SetChrPos(0x15, 42770, 0, 5270, 0)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xD, 84430, 200, 1120, 90)
    SetChrFlags(0xD, 0x10)
    OP_44(0xD, 0x0)
    SetChrChipByIndex(0xD, 7)
    SetChrSubChip(0xD, 0)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0xE, 0x40)
    SetChrPos(0xE, 84510, 200, 2890, 90)
    SetChrFlags(0xE, 0x10)
    OP_44(0xE, 0x0)
    SetChrChipByIndex(0xE, 9)
    SetChrSubChip(0xE, 0)
    SetChrFlags(0x11, 0x80)
    Jump("loc_C31")

    label("loc_BBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_C31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_BD0")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_BD5")

    label("loc_BD0")

    ClearChrFlags(0x10, 0x80)

    label("loc_BD5")

    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xE, 0x10)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x9, 82950, 0, 4700, 90)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x0, 0x6, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x6)
    OP_43(0x18, 0x0, 0x0, 0x7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1C")
    SetChrFlags(0x17, 0x10)

    label("loc_C1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2C")
    SetChrFlags(0x1B, 0x10)
    Jump("loc_C31")

    label("loc_C2C")

    SetChrFlags(0x1B, 0x80)

    label("loc_C31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_C47")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 34)
    Jump("loc_DB3")

    label("loc_C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_C5D")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 35)
    Jump("loc_DB3")

    label("loc_C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_C73")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 36)
    Jump("loc_DB3")

    label("loc_C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_C89")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 37)
    Jump("loc_DB3")

    label("loc_C89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_C9F")
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 38)
    Jump("loc_DB3")

    label("loc_C9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_CB5")
    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 39)
    Jump("loc_DB3")

    label("loc_CB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_CCB")
    OP_A3(0x10F6)
    SetMapFlags(0x10000000)
    Event(0, 40)
    Jump("loc_DB3")

    label("loc_CCB")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_CF3"),
        (103, "loc_D0B"),
        (106, "loc_D23"),
        (111, "loc_D3B"),
        (114, "loc_D53"),
        (116, "loc_D6B"),
        (123, "loc_D83"),
        (121, "loc_D9B"),
        (SWITCH_DEFAULT, "loc_DB3"),
    )


    label("loc_CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D08")
    SetMapFlags(0x10000000)
    Event(0, 47)

    label("loc_D08")

    Jump("loc_DB3")

    label("loc_D0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D20")
    SetMapFlags(0x10000000)
    Event(0, 44)

    label("loc_D20")

    Jump("loc_DB3")

    label("loc_D23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D38")
    SetMapFlags(0x10000000)
    Event(0, 41)

    label("loc_D38")

    Jump("loc_DB3")

    label("loc_D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D50")
    SetMapFlags(0x10000000)
    Event(0, 59)

    label("loc_D50")

    Jump("loc_DB3")

    label("loc_D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D68")
    SetMapFlags(0x10000000)
    Event(0, 54)

    label("loc_D68")

    Jump("loc_DB3")

    label("loc_D6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D80")
    SetMapFlags(0x10000000)
    Event(0, 64)

    label("loc_D80")

    Jump("loc_DB3")

    label("loc_D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D98")
    SetMapFlags(0x10000000)
    Event(0, 71)

    label("loc_D98")

    Jump("loc_DB3")

    label("loc_D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DB0")
    SetMapFlags(0x10000000)
    Event(0, 76)

    label("loc_DB0")

    Jump("loc_DB3")

    label("loc_DB3")

    Return()

    # Function_0_66E end

    def Function_1_DB4(): pass

    label("Function_1_DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_DBE")
    Jump("loc_DF5")

    label("loc_DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_DCC")
    OP_64(0x0, 0x1)
    Jump("loc_DF5")

    label("loc_DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_DDA")
    OP_64(0x1, 0x1)
    Jump("loc_DF5")

    label("loc_DDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_DE4")
    Jump("loc_DF5")

    label("loc_DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_DEE")
    Jump("loc_DF5")

    label("loc_DEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_DF5")

    label("loc_DF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E0D")
    OP_B1("t2510_y")
    Jump("loc_E16")

    label("loc_E0D")

    OP_B1("t2510_n")

    label("loc_E16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_E20")
    Jump("loc_E4D")

    label("loc_E20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x403, 7)), scpexpr(EXPR_END)), "loc_E38")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_E4D")

    label("loc_E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 3)), scpexpr(EXPR_END)), "loc_E4D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_E4D")

    Return()

    # Function_1_DB4 end

    def Function_2_E4E(): pass

    label("Function_2_E4E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E71")
    OP_8D(0xFE, 39890, 1860, 43300, -1658, 2000)
    Jump("Function_2_E4E")

    label("loc_E71")

    Return()

    # Function_2_E4E end

    def Function_3_E72(): pass

    label("Function_3_E72")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E95")
    OP_8D(0xFE, 36600, 27090, 39800, 31770, 1500)
    Jump("Function_3_E72")

    label("loc_E95")

    Return()

    # Function_3_E72 end

    def Function_4_E96(): pass

    label("Function_4_E96")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EB9")
    OP_8D(0xFE, 2080, 5500, 3800, -580, 2000)
    Jump("Function_4_E96")

    label("loc_EB9")

    Return()

    # Function_4_E96 end

    def Function_5_EBA(): pass

    label("Function_5_EBA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EDD")
    OP_8D(0xFE, 28190, -1470, 31790, 1270, 1000)
    Jump("Function_5_EBA")

    label("loc_EDD")

    Return()

    # Function_5_EBA end

    def Function_6_EDE(): pass

    label("Function_6_EDE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FB2")
    OP_8C(0xFE, 90, 400)

    label("loc_EEE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F37")
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F34")
    OP_63(0xFE)
    OP_8C(0xFE, 180, 400)
    Jump("loc_F37")

    label("loc_F34")

    Jump("loc_EEE")

    label("loc_F37")

    OP_8E(0xFE, 0x17458, 0xFA, 0x7814, 0x3E8, 0x0)
    OP_8C(0xFE, 90, 400)

    label("loc_F52")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F9B")
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F98")
    OP_63(0xFE)
    OP_8C(0xFE, 0, 400)
    Jump("loc_F9B")

    label("loc_F98")

    Jump("loc_F52")

    label("loc_F9B")

    OP_8E(0xFE, 0x17458, 0xFA, 0x82C8, 0x3E8, 0x0)
    Jump("Function_6_EDE")

    label("loc_FB2")

    Return()

    # Function_6_EDE end

    def Function_7_FB3(): pass

    label("Function_7_FB3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FD6")
    OP_8D(0xFE, 92190, 29990, 93420, 33800, 1000)
    Jump("Function_7_FB3")

    label("loc_FD6")

    Return()

    # Function_7_FB3 end

    def Function_8_FD7(): pass

    label("Function_8_FD7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_105B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_100E")

    ChrTalk(    #0
        0xFE,
        (
            "啊啊～今天又是\x01",
            "劳累的一天啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1058")

    label("loc_100E")

    OP_A2(0x12)

    ChrTalk(    #1
        0xFE,
        "哟，你们的调查有进展吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "忙到现在还没吃饭吗？\x01",
            "还真是辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1058")

    Jump("loc_16F9")

    label("loc_105B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_16F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 3)), scpexpr(EXPR_END)), "loc_10DB")

    ChrTalk(    #3
        0xFE,
        (
            "校舍后面\x01",
            "平时都空无一人，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "想想的话也确实是\x01",
            "妖怪最喜欢的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "可恶啊，\x01",
            "看来以后不能去那里了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F9")

    label("loc_10DB")

    OP_A2(0x1233)
    OP_28(0x83, 0x1, 0x10)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -3000, 0, 4850, 270)
    SetChrPos(0x105, -2500, 0, 5500, 270)
    ClearChrFlags(0xFE, 0x10)
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x26, 0x0)
    OP_0D()

    ChrTalk(    #6
        0xFE,
        (
            "啊啊～\x01",
            "都快饿死了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 90, 400)

    ChrTalk(    #7
        0xFE,
        "……啊？有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1000F啊，嗯……\x02\x03",

            "其实是有点事\x01",
            "想问你。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05艾丝蒂尔表示自己正在调查\x01",
            "考试期间发生的奇异事件。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #10
        0xFE,
        "奇异的事情吗……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1002F嗯，比如说有没有看到什么奇怪的东西，\x01",
            "或听到可疑的声响之类的？\x02\x03",

            "只要是奇怪的东西，\x01",
            "什么都可以。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "奇怪的东西……吗？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0xFE,
        (
            "……真是的，本来都\x01",
            "不愿再想起那件讨厌的事情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x105,
        "#044F#1P嗯？到底是什么事情呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "啊啊，这件事我还\x01",
            "没和任何人说过呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "其实我……\x01",
            "看到过奇怪的人影。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1002F…………嗯！？\x02\x03",

            "……可以再说的详细一点吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "啊、啊啊，当然没问题。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "我在回家之前\x01",
            "先到校舍后面转了转。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "因为学校考试，这里也没什么人，\x01",
            "气氛非常不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "随便走了走，\x01",
            "正准备要回去时…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "忽然发现有个白色的人影\x01",
            "飘在空中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "我绝对没有看错，\x01",
            "那肯定是个人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1015F（白色的人影吗……\x01",
            "　与另外的证言相符。）\x02\x03",

            "#1002F……那…之后又怎样了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "那家伙…\x01",
            "之后就飞进了后门里边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "然后就那样\x01",
            "消失不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#1002F原来如此……\x01",
            "消失在后门那边了吗…？\x02\x03",

            "嗯，这些话要好好\x01",
            "记在手册上。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x105,
        "#040F#1P啊啊，这很重要的证言。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "……那么我可以走了吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "我的肚子从刚才开始\x01",
            "就饿得快受不了了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1004F啊啊，真不好意思。\x02\x03",

            "#1006F非常感谢您的帮忙，\x01",
            "这些情报对我们非常有用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "呵呵，虽然不知道发生了什么事，\x01",
            "你们加油吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_168B():

        label("loc_168B")

        TurnDirection(0x101, 0x1B, 400)
        OP_48()
        Jump("loc_168B")

    QueueWorkItem2(0x101, 1, lambda_168B)

    def lambda_169C():

        label("loc_169C")

        TurnDirection(0x105, 0x1B, 400)
        OP_48()
        Jump("loc_169C")

    QueueWorkItem2(0x105, 1, lambda_169C)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFFF01A, 0x0, 0x50, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF380, 0x0, 0xFFFFFA6A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFDB2, 0x0, 0xFFFFFA42, 0x7D0, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x105, 0x1)
    SetChrFlags(0xFE, 0x80)
    EventEnd(0x0)

    label("loc_16F9")

    TalkEnd(0xFE)
    Return()

    # Function_8_FD7 end

    def Function_9_16FD(): pass

    label("Function_9_16FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 0)), scpexpr(EXPR_END)), "loc_174A")

    ChrTalk(    #33
        0xFE,
        (
            "罗基克那小子\x01",
            "好像害怕得要死，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "呼呼呼……\x01",
            "真是丢脸啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FB")

    label("loc_174A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_179E")

    ChrTalk(    #35
        0xFE,
        (
            "好像有什么东西\x01",
            "潜藏在旧校舍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "或许是亡灵之类的东西\x01",
            "也说不定啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FB")

    label("loc_179E")

    OP_A2(0x11)

    ChrTalk(    #37
        0xFE,
        (
            "好像有什么东西\x01",
            "潜藏在旧校舍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "也许是亡灵之类的东西\x01",
            "也说不定啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "呼呼呼……\x02",
    )

    CloseMessageWindow()

    label("loc_17FB")

    TalkEnd(0xFE)
    Return()

    # Function_9_16FD end

    def Function_10_17FF(): pass

    label("Function_10_17FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1877")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1818")
    Call(0, 12)
    Jump("loc_1874")

    label("loc_1818")


    ChrTalk(    #40
        0xFE,
        (
            "没想到男人\x01",
            "竟然会这么笨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "难道不知道这样会\x01",
            "让别人很担心的吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "（嘟哝）……\x02",
    )

    CloseMessageWindow()

    label("loc_1874")

    Jump("loc_1A56")

    label("loc_1877")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1919")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_18C5")

    ChrTalk(    #43
        0xFE,
        (
            "为什么你要\x01",
            "那么轻易就答应啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "以后再想反悔也晚了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1916")

    label("loc_18C5")

    OP_A2(0x10)

    ChrTalk(    #45
        0xFE,
        (
            "家庭教师～？\x01",
            "那也是应试对策吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "你…接下那么大的事情\x01",
            "真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1916")

    Jump("loc_1A56")

    label("loc_1919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_19C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1972")

    ChrTalk(    #47
        0xFE,
        (
            "正确答案是１吧？\x01",
            "不是３啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "这种问题都能搞错，\x01",
            "真是败给你了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C1")

    label("loc_1972")

    OP_A2(0x10)

    ChrTalk(    #49
        0xFE,
        (
            "正确答案是１吧？\x01",
            "不是３啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "真是的……为什么你会\x01",
            "这么粗心大意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19C1")

    Jump("loc_1A56")

    label("loc_19C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_1A56")
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_1A15")

    ChrTalk(    #51
        0xFE,
        (
            "考试期间什么事情\x01",
            "也没有发生哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "大家都在忙着念书。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A56")

    label("loc_1A15")

    OP_A2(0x10)

    ChrTalk(    #53
        0xFE,
        "啊，有什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "奇怪的事情吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "好像没什么呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1A56")

    TalkEnd(0xFE)
    Return()

    # Function_10_17FF end

    def Function_11_1A5A(): pass

    label("Function_11_1A5A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1AF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A73")
    Call(0, 12)
    Jump("loc_1AED")

    label("loc_1A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_1AB0")

    ChrTalk(    #56
        0xFE,
        "啊……怎么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "我说了什么\x01",
            "不该说的话吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AED")

    label("loc_1AB0")


    ChrTalk(    #58
        0xFE,
        (
            "妮吉塔那家伙……\x01",
            "为什么要发火啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "嗯、嗯～不明白。\x02",
    )

    CloseMessageWindow()

    label("loc_1AED")

    Jump("loc_1D0B")

    label("loc_1AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 1)), scpexpr(EXPR_END)), "loc_1B60")

    ChrTalk(    #60
        0xFE,
        (
            "虽然在这种地方干等着很无聊，\x01",
            "不过还是听从专业人士的意见吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "请一定把其它的学生\x01",
            "也救出来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D0B")

    label("loc_1B60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1C13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_1BBF")

    ChrTalk(    #62
        0xFE,
        (
            "家庭教师的责任可是\x01",
            "非常重大的啊～～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "接下这任务以后\x01",
            "还真是挺不安的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C10")

    label("loc_1BBF")

    OP_A2(0xE)

    ChrTalk(    #64
        0xFE,
        (
            "我开始担任假期时的\x01",
            "家庭教师了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "因为要迎接考试，\x01",
            "责任可是很重大的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C10")

    Jump("loc_1D0B")

    label("loc_1C13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_1C7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_1C49")

    ChrTalk(    #66
        0xFE,
        (
            "真是败了……\x01",
            "本来是很有自信的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C79")

    label("loc_1C49")

    OP_A2(0xE)

    ChrTalk(    #67
        0xFE,
        "啊～！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "那题的答案真的\x01",
            "不是３啊？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C79")

    Jump("loc_1D0B")

    label("loc_1C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_1D0B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_1CBF")

    ChrTalk(    #69
        0xFE,
        "考试期间里发生的怪事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "好像没什么啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D0B")

    label("loc_1CBF")

    OP_A2(0xE)

    ChrTalk(    #71
        0xFE,
        "嗯？有什么事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "……考试期间中的\x01",
            "奇怪事件吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "好像没有啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1D0B")

    TalkEnd(0xFE)
    Return()

    # Function_11_1A5A end

    def Function_12_1D0F(): pass

    label("Function_12_1D0F")

    OP_4A(0x18, 255)
    OP_4A(0x19, 255)

    ChrTalk(    #74
        0x18,
        (
            "呼～当人质\x01",
            "也是很辛苦的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x18,
        (
            "是因为太紧张了吗…\x01",
            "肩膀都觉得酸痛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x19,
        "算了，这个无所谓啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x19,
        (
            "２个人能平安获救\x01",
            "就已经很幸运了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x18,
        "确实如此，不过……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x18,
        (
            "我们也想和你们一起\x01",
            "同那些家伙战斗啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x18,
        (
            "如果大家一起冲上去\x01",
            "那些坏蛋就……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x19,
        "………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x18,
        "……啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x18,
        (
            "妮吉塔……\x01",
            "怎么了……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #84
        0x19,
        (
            "#3S笨蛋！\x01",
            "你在说什么啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #85
        0x18,
        "哇哇……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x19,
        (
            "勤务员先生\x01",
            "被击伤了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x19,
        (
            "你明明知道\x01",
            "却还说那种蠢话？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x18,
        (
            "哇，那个…\x01",
            "我明白的，不过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x18,
        (
            "那、那个，妮吉塔。\x01",
            "为什么发这么大的火？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x19, 0, 400)

    ChrTalk(    #90
        0x19,
        "不…不知道！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x19,
        "你、你自己想吧！\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)
    OP_A2(0x20C4)
    ClearChrFlags(0x18, 0x10)
    OP_4B(0x18, 255)
    OP_4B(0x19, 255)
    Return()

    # Function_12_1D0F end

    def Function_13_1F6E(): pass

    label("Function_13_1F6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 1)), scpexpr(EXPR_END)), "loc_200A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FD4")

    ChrTalk(    #92
        0xFE,
        (
            "米克真是很\x01",
            "幸运呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "要不是他遇到大家的话，\x01",
            "现在还不知道会怎样呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)
    Jump("loc_2007")

    label("loc_1FD4")


    ChrTalk(    #94
        0xFE,
        (
            "米克真是很\x01",
            "幸运呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "总之应该感谢他才对。\x02",
    )

    CloseMessageWindow()

    label("loc_2007")

    Jump("loc_28C3")

    label("loc_200A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2149")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_20BB")

    ChrTalk(    #96
        0xFE,
        (
            "那么说来，科洛丝。\x01",
            "你现在正在放假是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "其实我这些日子一直在\x01",
            "努力练习剑术……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "假期结束后\x01",
            "请一定和我再战一场吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x105,
        "#040F嗯嗯～我也不会输的哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2146")

    label("loc_20BB")

    OP_A2(0xD)

    ChrTalk(    #100
        0xFE,
        "我也听到事件的传闻了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "好像是有可疑的人物\x01",
            "潜藏在旧校舍了对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "可是…藏在那种地方\x01",
            "究竟要做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "真是无法理解啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2146")

    Jump("loc_28C3")

    label("loc_2149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_21DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2192")

    ChrTalk(    #104
        0xFE,
        (
            "太阳已经快要\x01",
            "下山了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "差不多\x01",
            "该准备回去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D7")

    label("loc_2192")

    OP_A2(0xD)

    ChrTalk(    #106
        0xFE,
        (
            "考试总算是\x01",
            "熬过去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "嗯，这次我的成绩\x01",
            "应该还过得去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D7")

    Jump("loc_28C3")

    label("loc_21DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_28C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_2246")

    ChrTalk(    #108
        0xFE,
        (
            "要是还有问题的话\x01",
            "随时可以来找我问。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #109
        0xFE,
        (
            "那么，科洛丝，\x01",
            "下次社团活动时再见吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C3")

    label("loc_2246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 2)), scpexpr(EXPR_END)), "loc_22AE")

    ChrTalk(    #110
        0xFE,
        (
            "那个白色人影的事情\x01",
            "我还没对任何人说过呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "只靠揣测来说明事情\x01",
            "可不能称作科学的态度。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28C3")

    label("loc_22AE")

    OP_A2(0x1232)
    OP_28(0x83, 0x1, 0x8)
    OP_A2(0xD)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 46020, 0, 32509, 90)
    SetChrPos(0x105, 46140, 0, 33370, 90)
    ClearChrFlags(0xFE, 0x10)
    OP_51(0x26, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x26, 0x0)
    OP_0D()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x105, 400)
    Sleep(400)

    ChrTalk(    #112
        0xFE,
        (
            "啊，科洛丝。\x01",
            "考试怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x105,
        (
            "#045F啊，还好吧……\x02\x03",

            "#040F对了，巴托姆…\x01",
            "可以向你打听一些事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "当然，什么事呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        "#1015F嗯，其实呢……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #116
        (
            "\x07\x05艾丝蒂尔表示自己正在调查\x01",
            "考试期间发生的奇异事件。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #117
        0xFE,
        "嗯…奇怪的事情吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "想想的话…\x01",
            "说起来确实有……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        (
            "#1011F啊，就算不知道真相\x01",
            "也没有关系哦。\x02\x03",

            "总之，请把你遇到的事\x01",
            "如实地告诉我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "那样的话，\x01",
            "我就试着说说看了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #121
        0xFE,
        "其实…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "……我看见了在天空飞舞的人影。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(20)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #123
        0x105,
        "#042F…………！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#1002F……可以把当时的\x01",
            "情景详细说给我们听听吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "嗯，那是考试当天的晚上。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "我留在教室\x01",
            "念书……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "忽然就感觉窗外\x01",
            "好像有什么动静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "本来还以为是风吹进来了，\x01",
            "就起来去关窗户……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "结果却发现外边\x01",
            "飘浮着白色的人影。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1015F白色的人影……吗。\x02\x03",

            "#1002F那，之后那个人影\x01",
            "怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "不好意思，那就不清楚了，\x01",
            "因为很快就消失了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "我记得好像是消失在\x01",
            "正东方向了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x105,
        (
            "#042F正东方向的话……\x01",
            "那不就是旧校舍那边吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#1002F嗯，应该是吧……\x02\x03",

            "不过，我记得不是\x01",
            "太清楚了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "嗯嗯，这是很有趣的现象。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "我想以后好好研究一下，\x01",
            "先简单记录在笔记本上了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        "#1004F研、研究～！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #138
        0x105,
        (
            "#041F巴托姆\x01",
            "是理科班的学生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        "#1001F啊哈哈，原来是这样啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xFE, 400)

    ChrTalk(    #140
        0xFE,
        "这些情报对你们有用吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        (
            "#1000F嗯，非常有用。\x01",
            "是很重要的证言啊。\x02\x03",

            "马上记在\x01",
            "手册上吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x105,
        (
            "#040F巴托姆，\x01",
            "实在是感激不尽。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "哪里，不用客气。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 0, 400)
    EventEnd(0x0)

    label("loc_28C3")

    TalkEnd(0xFE)
    Return()

    # Function_13_1F6E end

    def Function_14_28C7(): pass

    label("Function_14_28C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2A7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29FC")
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #144
        0xFE,
        (
            "啊～艾丝蒂尔，\x01",
            "约修亚………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "那个，承蒙帮助，\x01",
            "真是太谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        "#1000F哪里，没事就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x102,
        "#1040F这次真是天降横祸啊，\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #148
        0xFE,
        "真是的～\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "不过，原来科洛丝前辈\x01",
            "就是科洛蒂娅公主殿下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "比起这次的事件，\x01",
            "这个反而更让我吃惊呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x20C3)
    Jump("loc_2A79")

    label("loc_29FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2A79")

    ChrTalk(    #151
        0xFE,
        (
            "科洛丝前辈竟然\x01",
            "就是科洛蒂娅公主殿下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "平时从来都在一起活动，\x01",
            "却从来没有注意到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "哈，我真是\x01",
            "迟钝啊。\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()

    label("loc_2A79")

    Jump("loc_2DB9")

    label("loc_2A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_2B7F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_2AEB")

    ChrTalk(    #154
        0xFE,
        (
            "这次我已经拼命努力了，\x01",
            "大概可以取得好成绩吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "嘿嘿～不过和前辈\x01",
            "肯定是无法相比的啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7C")

    label("loc_2AEB")

    OP_A2(0xC)

    ChrTalk(    #156
        0xFE,
        (
            "哈～不管怎么说，\x01",
            "考试总算是结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "这次我已经拼命努力了，\x01",
            "大概可以取得好成绩吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #158
        0xFE,
        (
            "不过和科洛丝前辈\x01",
            "肯定是无法相比的啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7C")

    Jump("loc_2DB9")

    label("loc_2B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_2DB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 6)), scpexpr(EXPR_END)), "loc_2BD8")

    ChrTalk(    #159
        0xFE,
        (
            "没记得有什么\x01",
            "奇怪的事情发生哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "哈～没能帮上学姐\x01",
            "真是遗憾啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DB9")

    label("loc_2BD8")

    OP_A2(0x1236)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x105, 0)
    Sleep(400)

    ChrTalk(    #161
        0xFE,
        (
            "啊，科洛丝前辈。\x01",
            "是有什么东西忘了吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x105,
        (
            "#040F不，只是有点事情\x01",
            "要在学校里调查。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "啊～是什么事呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        "#1015F这个嘛……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #165
        (
            "\x07\x05艾丝蒂尔表示自己正在调查\x01",
            "考试期间发生的奇异事件。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #166
        0xFE,
        "哎！？怪异的事件吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "嗯……\x01",
            "完全没有发现哦～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "嗯嗯～真是抱歉。\x01",
            "没能帮上你的忙……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        (
            "#1000F哪里的话，不用介意啦。\x02\x03",

            "好，再去找别人问问吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x105,
        "#040F莉秋儿，谢谢你啦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #171
        0xFE,
        "哪里，别客气。\x02",
    )

    CloseMessageWindow()

    label("loc_2DB9")

    TalkEnd(0xFE)
    Return()

    # Function_14_28C7 end

    def Function_15_2DBD(): pass

    label("Function_15_2DBD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2EA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E54")

    ChrTalk(    #172
        0xFE,
        (
            "事件虽然顺利解决了，\x01",
            "但接下来也很麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "没有导力器的生活\x01",
            "大家都是第一次经历。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "很多不便之处\x01",
            "一时还很难适应呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_2EA4")

    label("loc_2E54")


    ChrTalk(    #175
        0xFE,
        (
            "没有导力器的生活\x01",
            "大家都是第一次经历。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "很多不便之处\x01",
            "一时还很难适应呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA4")

    Jump("loc_308B")

    label("loc_2EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 0)), scpexpr(EXPR_END)), "loc_2EF5")

    ChrTalk(    #177
        0xFE,
        (
            "其它的各位\x01",
            "也都平安无事吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "艾丝蒂尔，你们\x01",
            "也要小心啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308B")

    label("loc_2EF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_2FE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_2F58")

    ChrTalk(    #179
        0xFE,
        (
            "我和从王都来的叔叔\x01",
            "约定在卢安见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        (
            "他会依约前来吗…\x01",
            "还真是有些不安啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FE0")

    label("loc_2F58")

    OP_A2(0xB)

    ChrTalk(    #181
        0xFE,
        (
            "叔叔要从王都\x01",
            "到卢安来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        (
            "我们已经好久没见了，\x01",
            "所以这次准备在卢安见面…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "不过叔叔这个人比较怪，\x01",
            "我担心他不会依约前来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FE0")

    Jump("loc_308B")

    label("loc_2FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_308B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_301B")

    ChrTalk(    #184
        0xFE,
        (
            "考试中什么特别的事情\x01",
            "也没发生哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_308B")

    label("loc_301B")

    OP_A2(0xB)

    ChrTalk(    #185
        0xFE,
        (
            "是……？\x01",
            "奇怪的事情……吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xFE,
        (
            "啊，真不巧，\x01",
            "我完全不知道呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xFE,
        (
            "不好意思，你们还是去\x01",
            "问问其它人吧，\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308B")

    TalkEnd(0xFE)
    Return()

    # Function_15_2DBD end

    def Function_16_308F(): pass

    label("Function_16_308F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_32D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x418, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_328D")

    ChrTalk(    #188
        0xFE,
        "啊，各位游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "真了不起，你们把事件\x01",
            "顺利解决了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        "真不知该怎么感谢你们才好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        (
            "#1001F哪里哪里，\x01",
            "这是我们应该做的。\x02\x03",

            "#1011F哎，怎么样了？\x01",
            "稍微冷静一点了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #192
        0xFE,
        "哈、哈哈，当然了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "沉着冷静\x01",
            "可是我的代名词啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x101,
        (
            "#1028F嘿～是吗。\x02\x03",

            "#1015F#1S虽、虽然有点\x01",
            "害怕，不过……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #195
        0xFE,
        "呜……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x102,
        (
            "#1035F（艾丝蒂尔……\x01",
            "  不要莽撞行事哦。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x101,
        "#1008F（啊，情况果然不容乐观吗？）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xFE,
        (
            "不管怎样\x01",
            "大家没事就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "那、那么\x01",
            "我就先失礼了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20C2)
    Jump("loc_32D5")

    label("loc_328D")


    ChrTalk(    #200
        0xFE,
        (
            "我只、只不过是保持着\x01",
            "应有的警戒心而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "绝、绝没有\x01",
            "害怕的哦！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32D5")

    Jump("loc_37EF")

    label("loc_32D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 0)), scpexpr(EXPR_END)), "loc_337D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_333F")

    ChrTalk(    #202
        0xFE,
        (
            "按、按照指示，\x01",
            "我们就在这里待命。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xFE,
        (
            "所、所以拜托你们\x01",
            "快点把我们救出来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_337A")

    label("loc_333F")


    ChrTalk(    #204
        0xFE,
        (
            "越、越快越好！\x01",
            "快点把我们救出来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        "拜、拜托了。\x02",
    )

    CloseMessageWindow()

    label("loc_337A")

    Jump("loc_37EF")

    label("loc_337D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_34B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_33C5")

    ChrTalk(    #206
        0xFE,
        (
            "那么，\x01",
            "我也该去社团了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        "大家也许都着急了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_34B0")

    label("loc_33C5")

    TurnDirection(0xFE, 0x105, 0)
    OP_A2(0xA)

    ChrTalk(    #208
        0xFE,
        (
            "科洛丝，我听说了啊。\x01",
            "你开始休假了是吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x105,
        (
            "#040F嗯，考试结束了，\x01",
            "现在就开始休息了。\x02\x03",

            "等假期过完后再见吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "嗯，多保重吧，\x01",
            "期待下次见面。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "我准备在放假期间\x01",
            "帮忙做些选举活动的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        "那么，休假结束后再见了。\x02",
    )

    CloseMessageWindow()

    label("loc_34B0")

    Jump("loc_37EF")

    label("loc_34B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_3607")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_351C")

    ChrTalk(    #213
        0xFE,
        (
            "在我看来，两个候选人\x01",
            "的政策都有些不足。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "不过综合比较的话\x01",
            "还是诺曼更加有利些。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3604")

    label("loc_351C")

    OP_A2(0xA)

    ChrTalk(    #215
        0xFE,
        (
            "卢安市的选举活动\x01",
            "好像正在火热进行中呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "但在我来看，无论哪个候选人\x01",
            "都有政策上的欠缺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "波尔多斯一方的策略是发展港口式经济，\x01",
            "而诺曼一方是主张走观光路线。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "我曾经向爸爸波尔多斯\x01",
            "提过多次建议……\x01",
            "但一点改善也没有。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3604")

    Jump("loc_37EF")

    label("loc_3607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_37EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x247, 0)), scpexpr(EXPR_END)), "loc_3660")

    ChrTalk(    #219
        0xFE,
        (
            "就我所知\x01",
            "没发生什么奇怪的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "你们还是去问问\x01",
            "其它的学生吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37EF")

    label("loc_3660")

    OP_A2(0x1238)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #221
        0xFE,
        (
            "呀，科洛丝。\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x105,
        (
            "#040F嗯，其实有点事\x01",
            "想向你打听一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0xFE,
        "哦，是什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x101,
        "#1002F嗯，是这样的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #225
        (
            "\x07\x05艾丝蒂尔表示自己正在调查\x01",
            "考试期间发生的奇异事件。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #226
        0xFE,
        "啊，奇怪的事情……吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "不好意思，没发现什么。\x01",
            "没能帮上忙，真是抱歉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        (
            "#1000F哪里的话，不用介意啦。\x02\x03",

            "那么，多谢帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        "有什么需要的话请再来。\x02",
    )

    CloseMessageWindow()

    label("loc_37EF")

    TalkEnd(0xFE)
    Return()

    # Function_16_308F end

    def Function_17_37F3(): pass

    label("Function_17_37F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_38B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_383A")

    ChrTalk(    #230
        0xFE,
        "罗基克，你好慢啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "大家都已经\x01",
            "去练习了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38B3")

    label("loc_383A")

    OP_A2(0x9)

    ChrTalk(    #232
        0xFE,
        "接下来是吹奏部的练习了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "已经到了集合时间了，\x01",
            "却还是没几个人来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "难得有个亚吉鲁\x01",
            "按照规定的时间来了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38B3")

    Jump("loc_3A1B")

    label("loc_38B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_3963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_390D")

    ChrTalk(    #235
        0xFE,
        (
            "明天起\x01",
            "社团活动又要开始忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "大概有很多天\x01",
            "不能按时回去了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3960")

    label("loc_390D")

    OP_A2(0x9)

    ChrTalk(    #237
        0xFE,
        "啊，已经这个时间了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        (
            "明天起\x01",
            "吹奏音乐部会很忙，\x01",
            "今天又不能早回去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3960")

    Jump("loc_3A1B")

    label("loc_3963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_3A1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_39BA")

    ChrTalk(    #239
        0xFE,
        (
            "和平时的考试\x01",
            "简直没有区别啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "从早到晚的念书\x01",
            "已经够累人了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A1B")

    label("loc_39BA")

    OP_A2(0x9)

    ChrTalk(    #241
        0xFE,
        "奇怪的事情吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "嗯…和平时的考试\x01",
            "简直没有区别啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "从早到晚的念书\x01",
            "已经够累人了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A1B")

    TalkEnd(0xFE)
    Return()

    # Function_17_37F3 end

    def Function_18_3A1F(): pass

    label("Function_18_3A1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_END)), "loc_3AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A7D")

    ChrTalk(    #244
        0xFE,
        (
            "各、各位！\x01",
            "请多关照！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "虽、虽然没有信心，\x01",
            "但我会努力等的！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_3AA6")

    label("loc_3A7D")


    ChrTalk(    #246
        0xFE,
        (
            "虽、虽然没有信心，\x01",
            "但我会努力等的！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AA6")

    Jump("loc_3C90")

    label("loc_3AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_3B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3B09")

    ChrTalk(    #247
        0xFE,
        (
            "啊～但是在放假之前\x01",
            "应该可以拿到考试的成绩了吧～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        "啊啊～真是不想看啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B62")

    label("loc_3B09")

    OP_A2(0x8)

    ChrTalk(    #249
        0xFE,
        (
            "嘿嘿，今天的\x01",
            "课总算完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "只要想着马上就可以放假了，\x01",
            "念书也就不那么辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B62")

    Jump("loc_3C90")

    label("loc_3B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_3BB1")

    ChrTalk(    #251
        0xFE,
        (
            "那么，接下来\x01",
            "要做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xFE,
        (
            "偶尔把房间装饰\x01",
            "一下也不错啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C90")

    label("loc_3BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_3C90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_3C14")

    ChrTalk(    #253
        0xFE,
        (
            "考试结束之后\x01",
            "就稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "嘿嘿，和妈妈说好了\x01",
            "要一起去王都购物呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C90")

    label("loc_3C14")

    OP_A2(0x8)

    ChrTalk(    #255
        0xFE,
        (
            "哎？考试期间的\x01",
            "奇怪事件吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "嗯…如果是说可爱的东西\x01",
            "我倒天天都在找……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        (
            "但要说奇怪的事情\x01",
            "就一点也记不得了～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C90")

    TalkEnd(0xFE)
    Return()

    # Function_18_3A1F end

    def Function_19_3C94(): pass

    label("Function_19_3C94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_3D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3CF1")

    ChrTalk(    #258
        0xFE,
        "哈，学院祭真开心啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "嗯，下次学院祭之前\x01",
            "就享受一下社团活动吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D43")

    label("loc_3CF1")

    OP_A2(0x7)

    ChrTalk(    #260
        0xFE,
        "啊，学院祭真开心啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "能再那样和大家一起热闹\x01",
            "不知要等到什么时候了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D43")

    Jump("loc_3DF8")

    label("loc_3D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_3DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3D95")

    ChrTalk(    #262
        0xFE,
        (
            "终于……\x01",
            "考试终于结束了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "啊～希望不要\x01",
            "不及格啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DF8")

    label("loc_3D95")

    OP_A2(0x7)

    ChrTalk(    #264
        0xFE,
        (
            "呼啊啊啊啊～……\x01",
            "考试终于结束了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "哎？什么？\x01",
            "考试中的奇怪事件？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xFE,
        "没什么印象了…\x02",
    )

    CloseMessageWindow()

    label("loc_3DF8")

    TalkEnd(0xFE)
    Return()

    # Function_19_3C94 end

    def Function_20_3DFC(): pass

    label("Function_20_3DFC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_END)), "loc_3EC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7C")

    ChrTalk(    #267
        0x9,
        (
            "#640F没关系，我明白的。\x02\x03",

            "贸然行动的话\x01",
            "只会成为你们的累赘呢。\x02\x03",

            "#648F总之，就拜托你们把\x01",
            "犯人打败了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_3EC0")

    label("loc_3E7C")


    ChrTalk(    #268
        0x9,
        (
            "#645F都、都说了没问题了！\x02\x03",

            "就算是我，在这种时候\x01",
            "也不会乱来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EC0")

    Jump("loc_4018")

    label("loc_3EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3F34")

    ChrTalk(    #269
        0xFE,
        (
            "#642F不过话说回来……\x02\x03",

            "雪拉扎德姐姐\x01",
            "身材还真是棒啊。\x02\x03",

            "#645F呼啊～我也好想\x01",
            "变成她那样子啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FC2")

    label("loc_3F34")


    ChrTalk(    #270
        0xFE,
        (
            "#642F不过话说回来……\x02\x03",

            "阿加特先生\x01",
            "还真是强壮啊～\x02\x03",

            "#647F虽然柔弱型的美少年也不错，\x01",
            "但男人果然还是强壮型最好……\x02\x03",

            "嗯～美学的世界果然深奥…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FC2")

    Jump("loc_4018")

    label("loc_3FC5")

    OP_A2(0x5)

    ChrTalk(    #271
        0xFE,
        (
            "#640F啊，二位。\x01",
            "探听的怎么样啦？\x02\x03",

            "#648F这边交给我们，\x01",
            "学生们就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4018")

    TalkEnd(0xFE)
    Return()

    # Function_20_3DFC end

    def Function_21_401C(): pass

    label("Function_21_401C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_406F")

    ChrTalk(    #272
        0xFE,
        (
            "#050F没有听别人说过\x01",
            "类似的传闻吗？\x02\x03",

            "即使是一些微不足道的也可以。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40BC")

    label("loc_406F")

    OP_A2(0x4)

    ChrTalk(    #273
        0xFE,
        (
            "#050F没有什么奇怪的事件吗？\x02\x03",

            "只要是感觉在意的事，\x01",
            "随便什么也都可以。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40BC")

    TalkEnd(0xFE)
    Return()

    # Function_21_401C end

    def Function_22_40C0(): pass

    label("Function_22_40C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_4111")

    ChrTalk(    #274
        0xFE,
        (
            "#020F类似的传闻也\x01",
            "没有听到过吗？\x02\x03",

            "哪怕只是一点小事也没关系哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_415E")

    label("loc_4111")

    OP_A2(0x4)

    ChrTalk(    #275
        0xFE,
        (
            "#020F没发生什么奇怪的事件吗？\x02\x03",

            "只要是感觉在意的事，\x01",
            "不管什么都可以。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_415E")

    TalkEnd(0xFE)
    Return()

    # Function_22_40C0 end

    def Function_23_4162(): pass

    label("Function_23_4162")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_4234")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_41C4")

    ChrTalk(    #276
        0xFE,
        (
            "这次我们班\x01",
            "也是斗志十足。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "嗯，在考试成绩中\x01",
            "应该就可以显现出结果了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4231")

    label("loc_41C4")

    OP_A2(0x3)

    ChrTalk(    #278
        0xFE,
        "好！评分终于结束了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "这次我们班\x01",
            "干得真不错嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xFE,
        (
            "在超过碧欧拉老师的班之前\x01",
            "还要继续努力才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4231")

    Jump("loc_442D")

    label("loc_4234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_43AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_42C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4287")

    ChrTalk(    #281
        0xFE,
        (
            "算了，现在不是想\x01",
            "那种事的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        "还是赶快工作吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_42C6")

    label("loc_4287")


    ChrTalk(    #283
        0xFE,
        (
            "话说回来，现在的\x01",
            "男孩子还真不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        "还是赶快工作吧。\x02",
    )

    CloseMessageWindow()

    label("loc_42C6")

    Jump("loc_43A9")

    label("loc_42C9")

    OP_A2(0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_432F")

    ChrTalk(    #285
        0xFE,
        (
            "刚才来的那个游击士……\x01",
            "身材实在很棒呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "而且如此的招摇，   \x01",
            "到底想要干什么啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43A9")

    label("loc_432F")


    ChrTalk(    #287
        0xFE,
        (
            "刚才来的那个游击士……\x01",
            "总之真的很有男子气概呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "火红色的头发，\x01",
            "还有发达的二头肌…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        "呵呵呵～还真是吸引人呢。\x02",
    )

    CloseMessageWindow()

    label("loc_43A9")

    Jump("loc_442D")

    label("loc_43AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_442D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_43F6")

    ChrTalk(    #290
        0xFE,
        (
            "也没有听学生们\x01",
            "提起过……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        "没有其它的事情了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_442D")

    label("loc_43F6")

    OP_A2(0x3)

    ChrTalk(    #292
        0xFE,
        "啊，奇怪的事件吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        "抱歉，什么也没有呢。\x02",
    )

    CloseMessageWindow()

    label("loc_442D")

    TalkEnd(0xFE)
    Return()

    # Function_23_4162 end

    def Function_24_4431(): pass

    label("Function_24_4431")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_4707")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B5")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #294
        0xFE,
        (
            "艾丝蒂尔，约修亚，\x01",
            "你们干得太好了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "呵呵呵～不愧是我教导过的孩子。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x102,
        (
            "#1040F在学院逗留的时候\x01",
            "真是多亏了您的照顾。\x02\x03",

            "老师教过的课程\x01",
            "直到现在都记得很清楚。\x02\x03",

            "连艾丝蒂尔\x01",
            "也都非常怀念呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #297
        0x101,
        (
            "#1004F哎………………………\x01",
            "……………………………\x02\x03",

            "#1016F………啊……嗯，对！\x01",
            "是那样是那样！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x102, 0x101, 400)
    Sleep(400)

    ChrTalk(    #298
        0x102,
        (
            "#1048F（难道……\x01",
            "你已经不记得了吗？）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #299
        0x101,
        (
            "#1008F（只、只是一时\x01",
            "　想不起来了而已。)\x02\x03",

            "（突、突然说出\x01",
            "　那么久之前的事情…）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "哎呀，你们在说什么悄悄话？\x01",
            "也让老师听听吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #301
        0x101,
        (
            "#1016F啊哈哈……\x01",
            "没、没说什么啦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x102,
        "#1052F（真是的……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20C8)
    Jump("loc_4704")

    label("loc_46B5")


    ChrTalk(    #303
        0xFE,
        (
            "艾丝蒂尔，约修亚，\x01",
            "你们干得太好了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        "呵呵呵～不愧是我教导过的孩子。\x02",
    )

    CloseMessageWindow()

    label("loc_4704")

    Jump("loc_4AB3")

    label("loc_4707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_482B")
    TurnDirection(0xFE, 0x105, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_476D")

    ChrTalk(    #305
        0xFE,
        (
            "假期结束后\x01",
            "还要打起精神来学校啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "那么，希望你们\x01",
            "过个有意义的假期。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4828")

    label("loc_476D")

    OP_A2(0x2)

    ChrTalk(    #307
        0xFE,
        (
            "啊，科洛丝。\x01",
            "我还以为你已经走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        (
            "假期结束后\x01",
            "一定要打起精神来学校啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        "好吗？这是约定哦～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x105,
        (
            "#040F好的，约定了。\x02\x03",

            "碧欧拉老师也要多保重啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        (
            "嗯，有意义的\x01",
            "假期吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4828")

    Jump("loc_4AB3")

    label("loc_482B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_48D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_487B")

    ChrTalk(    #312
        0xFE,
        "考试已经够累人了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0xFE,
        (
            "不管学生还是老师\x01",
            "都有些睡眠不足。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_48CD")

    label("loc_487B")

    OP_A2(0x2)

    ChrTalk(    #314
        0xFE,
        (
            "呜～都已经这个点了，\x01",
            "但评分还是没完成。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xFE,
        "啊～真想早点评完去喝一杯啊。\x02",
    )

    CloseMessageWindow()

    label("loc_48CD")

    Jump("loc_4AB3")

    label("loc_48D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_4AB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_492A")
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #316
        0xFE,
        (
            "积极参加社会活动\x01",
            "是好事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xFE,
        (
            "请加油吧！\x01",
            "老师也会支持你的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AB3")

    label("loc_492A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x246, 7)), scpexpr(EXPR_END)), "loc_4988")

    ChrTalk(    #318
        0xFE,
        (
            "好了～稍微休息了一下，\x01",
            "又该回到工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xFE,
        (
            "呼～不过评分\x01",
            "还真是辛苦的工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AB3")

    label("loc_4988")

    OP_A2(0x2)
    OP_A2(0x1237)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #320
        0xFE,
        (
            "啊，科洛丝。\x01",
            "有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x105,
        "#040F不，其实是……\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #322
        0xFE,
        (
            "啊，是刚才乔儿\x01",
            "说的那件事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xFE,
        (
            "听说你们在搜寻\x01",
            "可疑的人物…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x105,
        (
            "#040F嗯～请让我帮忙\x01",
            "一起进行调查吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "呵呵，积极参加社会活动\x01",
            "是好事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        (
            "请加油吧！\x01",
            "老师也会支持你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x105,
        "#041F是，谢谢您。\x02",
    )

    CloseMessageWindow()

    label("loc_4AB3")

    TalkEnd(0xFE)
    Return()

    # Function_24_4431 end

    def Function_25_4AB7(): pass

    label("Function_25_4AB7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_4B73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B2F")

    ChrTalk(    #328
        0xFE,
        (
            "勤务员先生的样子\x01",
            "似乎也稳定下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0xFE,
        "呼，没出大事就好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xFE,
        (
            "不如过一会儿\x01",
            "去看看他吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_4B70")

    label("loc_4B2F")


    ChrTalk(    #331
        0xFE,
        (
            "勤务员先生的样子\x01",
            "似乎也稳定下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        "呼，没出大事就好。\x02",
    )

    CloseMessageWindow()

    label("loc_4B70")

    Jump("loc_4D55")

    label("loc_4B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_4BF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4BA9")

    ChrTalk(    #333
        0xFE,
        (
            "这次考试\x01",
            "大家的成绩都相当好哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BEE")

    label("loc_4BA9")

    OP_A2(0x1)

    ChrTalk(    #334
        0xFE,
        (
            "这次考试\x01",
            "大家的成绩都相当好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xFE,
        (
            "看来学生们\x01",
            "也都很努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BEE")

    Jump("loc_4D55")

    label("loc_4BF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_4CB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4C4C")

    ChrTalk(    #336
        0xFE,
        (
            "米克本来\x01",
            "就是个很用功的学生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xFE,
        (
            "唯一的问题就是\x01",
            "他那消极的人生观。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CAD")

    label("loc_4C4C")

    OP_A2(0x1)

    ChrTalk(    #338
        0xFE,
        (
            "呀……？\x01",
            "这份考卷…没有写名字啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xFE,
        "嗯～编号是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0xFE,
        (
            "……嗯，看来是\x01",
            "米克的卷子啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CAD")

    Jump("loc_4D55")

    label("loc_4CB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_4D55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4D0A")

    ChrTalk(    #341
        0xFE,
        (
            "考试结束对学生们来说\x01",
            "就好像是无罪释放一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xFE,
        "哈～真羡慕他们。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D55")

    label("loc_4D0A")

    OP_A2(0x1)

    ChrTalk(    #343
        0xFE,
        (
            "还没来得及评分的卷子\x01",
            "就先收起来好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xFE,
        (
            "今天就先改到\x01",
            "这里吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D55")

    TalkEnd(0xFE)
    Return()

    # Function_25_4AB7 end

    def Function_26_4D59(): pass

    label("Function_26_4D59")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_4E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DE2")

    ChrTalk(    #345
        0xB,
        (
            "学生们很快就恢复\x01",
            "正常的校园生活了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xB,
        (
            "刚才的事件好像已经\x01",
            "忘得一干二净了一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xB,
        (
            "呵呵～年轻\x01",
            "真是好啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_4E20")

    label("loc_4DE2")


    ChrTalk(    #348
        0xB,
        (
            "学生们看起来\x01",
            "已经完全恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xB,
        (
            "呵呵～年轻\x01",
            "真是好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E20")

    Jump("loc_4FDB")

    label("loc_4E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 5)), scpexpr(EXPR_END)), "loc_4E74")

    ChrTalk(    #350
        0xB,
        (
            "武装的犯人们\x01",
            "应该还潜藏在校园里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xB,
        "各位，无论如何要小心啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4FDB")

    label("loc_4E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_4F13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4EC7")

    ChrTalk(    #352
        0xB,
        (
            "校长在不久前\x01",
            "外出了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xB,
        (
            "好像是有什么事，\x01",
            "具体就不清楚了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F10")

    label("loc_4EC7")

    OP_A2(0x0)

    ChrTalk(    #354
        0xB,
        (
            "啊，科洛丝。\x01",
            "现在已经放假了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xB,
        (
            "注意身体，\x01",
            "好好休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F10")

    Jump("loc_4FDB")

    label("loc_4F13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 2)), scpexpr(EXPR_END)), "loc_4F2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4F24")
    Jump("loc_4F27")

    label("loc_4F24")

    OP_A2(0x0)

    label("loc_4F27")

    Jump("loc_4FDB")

    label("loc_4F2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_4F53")

    ChrTalk(    #356
        0xB,
        (
            "辛苦了。\x01",
            "还在进行调查吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FDB")

    label("loc_4F53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_4FDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_4F91")

    ChrTalk(    #357
        0xB,
        (
            "我们已经接到通知了。\x01",
            "你们就随意调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FDB")

    label("loc_4F91")

    OP_A2(0x0)

    ChrTalk(    #358
        0xB,
        "啊，你们是游击士吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0xB,
        (
            "我们已经接到通知了。\x01",
            "你们就随意调查吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FDB")

    TalkEnd(0xB)
    Return()

    # Function_26_4D59 end

    def Function_27_4FDF(): pass

    label("Function_27_4FDF")

    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_500F")
    SetChrSubChip(0x8, 1)
    Jump("loc_5035")

    label("loc_500F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0x14A), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5030")
    SetChrSubChip(0x8, 2)
    Jump("loc_5035")

    label("loc_5030")

    SetChrSubChip(0x8, 0)

    label("loc_5035")

    OP_8C(0x8, 180, 0)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_5343")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529F")

    ChrTalk(    #360
        0x8,
        (
            "#783F艾丝蒂尔，约修亚。\x01",
            "这次真是辛苦你们了。\x02\x03",

            "#780F全靠你们，\x01",
            "学生们才能平安获救。\x02\x03",

            "身为学院的代表，\x01",
            "请允许我向你们表示诚挚的谢意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        (
            "#1025F能把事情平安解决，\x01",
            "我也松了口气。\x02\x03",

            "学院竟然会遭到袭击，\x01",
            "真是做梦也想不到啊…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x102,
        (
            "#1043F是啊……\x01",
            "看来我的想法太天真了。\x02\x03",

            "#1035F在这种状况下，\x01",
            "哪里都不是绝对安全的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x8,
        (
            "#782F是『结社』吗……\x02\x03",

            "这次事件的幕后黑手\x01",
            "似乎是一群身份不明的家伙啊。\x02\x03",

            "如果没有你们游击士的帮助，\x01",
            "这次的危机根本不可能顺利解决。\x02\x03",

            "为了早日恢复治安，\x01",
            "今后大家也要一起加油。\x02\x03",

            "这也是为了支持一个人在\x01",
            "王都努力的科洛丝…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x101,
        "#1006F嗯！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x102,
        "#1040F我们会竭尽全力的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x20F3)
    Jump("loc_5340")

    label("loc_529F")


    ChrTalk(    #366
        0x8,
        (
            "#780F这次事件的幕后黑手\x01",
            "似乎是一群身份不明的家伙。\x02\x03",

            "今后也需要你们游击士\x01",
            "多多帮忙了。\x02\x03",

            "一天也好，希望能早日恢复治安…\x01",
            "在王都的科洛丝\x01",
            "也一定是那样希望的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5340")

    Jump("loc_567A")

    label("loc_5343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 5)), scpexpr(EXPR_END)), "loc_543A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53DA")

    ChrTalk(    #367
        0x8,
        (
            "#780F犯人在寻找王室的公主，\x01",
            "但却没注意到是科洛丝。\x02\x03",

            "这样的话，很可能\x01",
            "会波及其它的女学生。\x02\x03",

            "抱歉，不过希望\x01",
            "诸位能够事先小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_5437")

    label("loc_53DA")


    ChrTalk(    #368
        0x8,
        (
            "#780F犯人在搜寻公主的过程中\x01",
            "可能会危害到其它女学生。\x02\x03",

            "抱歉，不过希望\x01",
            "诸位务必小心行事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5437")

    Jump("loc_567A")

    label("loc_543A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x244, 1)), scpexpr(EXPR_END)), "loc_552B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_5494")

    ChrTalk(    #369
        0x8,
        (
            "#780F最好赶快回到\x01",
            "学生会室。\x02\x03",

            "要是等到天黑之后，\x01",
            "就会有很多不便了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5528")

    label("loc_5494")

    OP_A2(0x6)

    ChrTalk(    #370
        0x8,
        "#780F调查进展得如何了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x105,
        (
            "#040F啊，是的，现在我们\x01",
            "要回学生会室了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x8,
        (
            "#780F那么，动作快一点吧，\x02\x03",

            "要是等到天黑之后，\x01",
            "调查就难以继续了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5528")

    Jump("loc_567A")

    label("loc_552B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 6)), scpexpr(EXPR_END)), "loc_567A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24C, 4)), scpexpr(EXPR_END)), "loc_5592")

    ChrTalk(    #373
        0x8,
        (
            "#780F要是还有什么需要帮忙的，\x01",
            "不要客气，尽管开口就是了。\x02\x03",

            "我们一定会全力协助的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_567A")

    label("loc_5592")

    OP_A2(0x1264)

    ChrTalk(    #374
        0x8,
        (
            "#780F调查好像已经开始了啊。\x02\x03",

            "科洛丝也\x01",
            "开始帮忙了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x105,
        (
            "#040F是的，毕竟这次的\x01",
            "事件关系到我们的校园…\x02\x03",

            "身为学院的学生，\x01",
            "我也想贡献出自己的力量。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x8,
        (
            "#780F要是有需要的话，\x01",
            "不要客气，尽管开口就是了。\x02\x03",

            "我们一定会全力协助的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_567A")

    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_27_4FDF end

    def Function_28_5683(): pass

    label("Function_28_5683")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 0)), scpexpr(EXPR_END)), "loc_570D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56F3")

    ChrTalk(    #377
        0xFE,
        (
            "要是有弓箭的话，\x01",
            "我也想参加战斗的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xFE,
        (
            "这里就拜托你们了！\x01",
            "加油了！各位游击士！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x15)
    Jump("loc_570D")

    label("loc_56F3")


    ChrTalk(    #379
        0xFE,
        "加油了！各位游击士！\x02",
    )

    CloseMessageWindow()

    label("loc_570D")

    TalkEnd(0xFE)
    Return()

    # Function_28_5683 end

    def Function_29_5711(): pass

    label("Function_29_5711")

    TalkBegin(0xFE)

    ChrTalk(    #380
        0xFE,
        (
            "米克的话果然\x01",
            "还是根据结果来下定论的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0xFE,
        (
            "哼、哼……\x01",
            "我才不会感谢呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_5711 end

    def Function_30_5766(): pass

    label("Function_30_5766")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_580D")

    ChrTalk(    #382
        0xFE,
        (
            "虽然很想尽快\x01",
            "确认小姐的安全…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xFE,
        (
            "不过现在的当务之急\x01",
            "还是解救学院的全体成员。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0xFE,
        (
            "在这里拜托\x01",
            "诸位了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0xFE,
        (
            "……请一定把其它的学生\x01",
            "也解救出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x16)
    Jump("loc_5865")

    label("loc_580D")


    ChrTalk(    #386
        0xFE,
        (
            "现在的当务之急\x01",
            "还是解救学院的全体成员……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0xFE,
        (
            "……请一定把其它的学生\x01",
            "也解救出来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5865")

    TalkEnd(0xFE)
    Return()

    # Function_30_5766 end

    def Function_31_5869(): pass

    label("Function_31_5869")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_END)), "loc_58C0")

    ChrTalk(    #388
        0xA,
        (
            "#732F那么，\x01",
            "等事情解决之后再来吧。\x02\x03",

            "艾丝蒂尔，约修亚……\x01",
            "路上要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58C0")

    TalkEnd(0xFE)
    Return()

    # Function_31_5869 end

    def Function_32_58C4(): pass

    label("Function_32_58C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_59B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_596C")

    ChrTalk(    #389
        0xFE,
        (
            "啊，各位游击士。\x01",
            "刚才真是谢谢大家了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0xFE,
        (
            "能把事情平安解决\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0xFE,
        (
            "虽然接下来还有不少困难，\x01",
            "但只要大家一起努力\x01",
            "就一定能克服的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_59AE")

    label("loc_596C")


    ChrTalk(    #392
        0xFE,
        (
            "各位游击士。\x01",
            "今天谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0xFE,
        (
            "能把事情平安解决\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59AE")

    Jump("loc_5A00")

    label("loc_59B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_END)), "loc_5A00")

    ChrTalk(    #394
        0xFE,
        (
            "呼嗯……\x01",
            "拜托饶了我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0xFE,
        (
            "那些家伙为什么\x01",
            "要做出这么过分的事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A00")

    TalkEnd(0xFE)
    Return()

    # Function_32_58C4 end

    def Function_33_5A04(): pass

    label("Function_33_5A04")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_5B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B24")

    ChrTalk(    #396
        0xFE,
        (
            "艾丝蒂尔，约修亚。\x01",
            "真是谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0xFE,
        (
            "虽然不是什么值钱的东西，\x01",
            "但还是请你们收下。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #398
        "\x07\x00得到了\x1F\x45\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x245, 1)
    OP_A2(0x10C0)
    OP_0D()

    ChrTalk(    #399
        0xFE,
        (
            "以后有空的话，把这次的事件\x01",
            "写成小说应该也不错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xFE,
        (
            "不过这个想法，\x01",
            "也得等到恢复正常生活才行…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B8A")

    label("loc_5B24")


    ChrTalk(    #401
        0xFE,
        (
            "以后有空的话，把这次的事件\x01",
            "写成小说应该也不错吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0xFE,
        (
            "不过这个想法，\x01",
            "也得等到恢复正常生活才行…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B8A")

    Jump("loc_5BF8")

    label("loc_5B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x404, 6)), scpexpr(EXPR_END)), "loc_5BF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BDB")

    ChrTalk(    #403
        0xFE,
        (
            "我们就在这里\x01",
            "等着你们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xFE,
        "各位，你们要小心啊……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x14)
    Jump("loc_5BF8")

    label("loc_5BDB")


    ChrTalk(    #405
        0xFE,
        (
            "我们就在这里\x01",
            "待机不动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BF8")

    TalkEnd(0xFE)
    Return()

    # Function_33_5A04 end

    def Function_34_5BFC(): pass

    label("Function_34_5BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C0D")
    Call(0, 81)

    label("loc_5C0D")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x101, 116390, 0, 2740, 0)
    SetChrPos(0xF7, 115500, 0, 2730, 0)
    SetChrPos(0x105, 117550, 0, 3240, 270)
    SetChrPos(0x104, 116430, 0, 1630, 0)
    SetChrPos(0x127, 115580, 0, 1650, 0)
    SetChrPos(0x9, 117660, 0, 4320, 270)
    SetChrPos(0xA, 118370, 0, 3940, 270)
    OP_6D(116710, 0, 460, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_6D(116480, 0, 3910, 2000)
    OP_0D()

    ChrTalk(    #406
        0x8,
        (
            "#783F#5P原来如此，我明白了。\x02\x03",

            "#780F你们是为了搜索\x01",
            "在卢安各处出没的『白影』\x01",
            "而到学院来调查的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x101,
        "#1002F#4P对，就是这样。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5DD9")

    ChrTalk(    #408
        0x106,
        (
            "#050F#6P协会派我们到\x01",
            "学院来进行调查。\x02\x03",

            "调查时大概要向学生们进行询问，\x01",
            "您可以准许吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E35")

    label("loc_5DD9")


    ChrTalk(    #409
        0x103,
        (
            "#020F#6P协会派我们到\x01",
            "学院中进行调查……\x02\x03",

            "并且还要对学生们进行一些询问，\x01",
            "您可以准许吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E35")


    ChrTalk(    #410
        0x8,
        (
            "#782F#5P不不，其实这件事\x01",
            "我本来也是要拜托你们的。\x02\x03",

            "虽然不知道那个『白影』\x01",
            "究竟是什么……\x02\x03",

            "但恐怕会影响到选举，\x01",
            "因此不能放任不管。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x101,
        (
            "#1016F#4P呼……\x01",
            "非常感谢。\x02\x03",

            "#1015F那么，在校园里有没有关于『白影』的\x01",
            "古怪的传闻呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x8,
        (
            "#780F#5P没有……\x01",
            "我没有听到任何有关的报告。\x02\x03",

            "你们学生会那里呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x9,
        (
            "#645F#2P嗯……我们也没有\x01",
            "听到这方面的消息呢。\x02\x03",

            "#640F不过，毕竟现在\x01",
            "是考试期间。\x02\x03",

            "有可能是大家没空来\x01",
            "这里商谈吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x8,
        "#782F#5P原来如此……有这种可能。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 400)

    def lambda_6003():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_6003)
    Sleep(50)

    def lambda_6016():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6016)
    Sleep(50)

    def lambda_6029():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_6029)

    ChrTalk(    #415
        0x101,
        "#1004F#6P嗯？怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x105,
        (
            "#542F#2P王立学院的定期测试\x01",
            "是关系到能否晋级的重要考试…\x02\x03",

            "所以就算真有学生看见了那些东西，\x01",
            "也只能暂且不作考虑，\x01",
            "集中精力准备考试。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0xA,
        (
            "#734F#2P如果是我的话也会这样的。\x02\x03",

            "比其那些虚无缥缈的幻觉，\x01",
            "我宁愿花时间\x01",
            "背几条算式。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x101,
        (
            "#1007F#6P哎哎～……\x01",
            "是这么回事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0x127,
        (
            "#153F#6P啊～最近的学生\x01",
            "还真是爱用功啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xA,
        (
            "#732F#2P不过，考试就在今天结束，\x01",
            "大家也算是彻底解放了……\x02\x03",

            "如果有奇怪传闻的话，\x01",
            "从今天开始应该就会流传开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x104,
        (
            "#035F#4P这种东西一旦广泛流传成了校园怪谈，\x01",
            "真实性恐怕就会大大降低……\x02\x03",

            "#030F因此现在正是直接寻找目击者\x01",
            "进行询问的最好时机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x8,
        (
            "#780F#5P唔，那你们就赶快\x01",
            "在校园中进行调查吧！\x02\x03",

            "乔儿、汉斯，\x01",
            "还有科洛丝，你们也一起帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x105,
        "#041F#2P是！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xA,
        "#730F#2P明白了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 225, 400)

    ChrTalk(    #425
        0x9,
        (
            "#644F#5P那么，要调查的话\x01",
            "我们最好先找个集合的据点。\x02\x03",

            "说不定会得到什么情报，\x01",
            "就定在学生会室吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x101,
        "#1006F#6PＴＨＡＮＫ　ＹＯＵ～真是帮了大忙了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2511   ._SN", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_34_5BFC end

    def Function_35_63BA(): pass

    label("Function_35_63BA")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x1F, 115970, 0, 2750, 0)
    ClearChrFlags(0x1F, 0x80)
    OP_6D(116530, 0, 4170, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #427
        0x8,
        (
            "#782F#5P基尔巴特……\x01",
            "这到底是怎么回事。\x02\x03",

            "你为什么要做出这样的事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x1F,
        (
            "#1226F#4P哼哼……目的有２个。\x02\x03",

            "#1220F第一，我已接到上级的指示，\x01",
            "要在全国范围内造成\x01",
            "更大的混乱。\x02\x03",

            "有情有义的我自然要选择\x01",
            "深切怀念的母校作为舞台。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x8,
        (
            "#783F#5P……你变了，基尔巴特。\x02\x03",

            "#782F学生时代的你是那么\x01",
            "坚定地追求自己的政治之道……\x02\x03",

            "当初的那些热情和信念，\x01",
            "难道都已经丢掉了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x1F,
        (
            "#1221F#4P理想终究只是理想，\x01",
            "现实可是无比丑陋的啊。\x02\x03",

            "米拉和权力就是一切……\x01",
            "这是担任戴尔蒙市长的秘书时，\x01",
            "我所悟出的道理。\x02\x03",

            "#1226F本想找机会把那市长整下台，\x01",
            "然后自己坐上他的位子……\x02\x03",

            "谁知道突然冒出了那群游击士，\x01",
            "把我的计划全盘打乱了。\x02\x03",

            "#1220F不过无所谓了，现在的我\x01",
            "已经用另一种方式将权力握在手中了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x8,
        "#783F#5P你太愚蠢了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x1F,
        (
            "#1226F#4P哼哼哼……\x01",
            "随你怎么说吧。\x02\x03",

            "#1221F至于我的另一个目的……\x01",
            "那就是利贝尔王室的公主了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x8,
        "#782F#5P！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x1F,
        (
            "#1221F#4P听说她也是\x01",
            "这所学院的学生。\x02\x03",

            "只是还不知道究竟是哪个学生，\x01",
            "您能告诉我吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x8,
        (
            "#783F#5P……你到底在说什么？\x01",
            "我一点也听不懂。\x02\x03",

            "#782F我可以明确地告诉你……\x01",
            "学院中根本就没有\x01",
            "你说的那个人。\x02\x03",

            "你的情报似乎有误啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x1F,
        (
            "#1221F#4P哈哈，想把我当成\x01",
            "傻瓜一样愚弄过去吗？\x02\x03",

            "#1226F算了，反正还有的是时间，\x02\x03",

            "我自己慢慢找就是了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x8,
        "#782F#5P嗯……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/T2500   ._SN", 129, 0, 0)
    IdleLoop()
    Return()

    # Function_35_63BA end

    def Function_36_68C3(): pass

    label("Function_36_68C3")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_6D(87050, 0, 7080, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)

    def lambda_6920():
        OP_6D(86660, 0, 2460, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6920)
    OP_67(0, 6180, -10000, 3000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F6)
    NewScene("ED6_DT21/T2500   ._SN", 129, 0, 0)
    IdleLoop()
    Return()

    # Function_36_68C3 end

    def Function_37_6963(): pass

    label("Function_37_6963")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x1A, 0x80)
    OP_6D(41510, -250, -3520, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_6D(41760, 0, 9240, 4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10F7)
    NewScene("ED6_DT21/T2500   ._SN", 129, 0, 0)
    IdleLoop()
    Return()

    # Function_37_6963 end

    def Function_38_69EB(): pass

    label("Function_38_69EB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x102, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x20, 255)
    OP_4A(0x12, 255)
    OP_4A(0x21, 255)
    SetChrPos(0xA, 3470, 0, 2580, 180)
    SetChrPos(0x9, 3500, 0, 1470, 0)
    SetChrPos(0x20, -240, 0, 3050, 180)
    SetChrPos(0x12, -650, 0, 2060, 90)
    SetChrPos(0x21, 350, 0, 1140, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6D(-3290, 0, 2710, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_6ABC():
        OP_6D(4140, 0, 2560, 3000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_6ABC)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xA, 0x0)
    OP_22(0x71, 0x0, 0x5F)
    Sleep(1000)
    OP_62(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #438
        0xA,
        "#732F#5P什么……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x9,
        (
            "#642F#4P刚才……\x01",
            "好像有什么声音？\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x5F)
    Sleep(1000)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0xA, 0, 400)

    ChrTalk(    #440
        0xA,
        "#732F#4P……是这边吗？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xA, 0x1)

    def lambda_6BA8():

        label("loc_6BA8")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_6BA8")

    QueueWorkItem2(0x9, 1, lambda_6BA8)
    Sleep(100)

    def lambda_6BBE():
        OP_6D(2420, 0, 5620, 2500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6BBE)
    OP_8E(0xA, 0x820, 0x0, 0x157C, 0x7D0, 0x0)
    OP_8C(0xA, 0, 400)
    WaitChrThread(0x102, 0x1)
    Sleep(500)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #441
        0xA,
        "#733F#4P什……！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10FE)
    OP_A2(0x10F8)
    NewScene("ED6_DT21/T2500   ._SN", 128, 0, 0)
    IdleLoop()
    Return()

    # Function_38_69EB end

    def Function_39_6C37(): pass

    label("Function_39_6C37")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    OP_D2(0x7036E, 0x70373, 0x1B)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x20, 255)
    OP_4A(0x12, 255)
    OP_4A(0x21, 255)
    SetChrPos(0xA, 2080, 0, 5500, 0)
    SetChrPos(0x9, 2600, 0, 4850, 0)
    SetChrPos(0x20, -240, 0, 3050, 180)
    SetChrPos(0x12, -650, 0, 2060, 90)
    SetChrPos(0x21, 350, 0, 1140, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6D(2170, 0, 5050, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_6D08():
        OP_8F(0xFE, 0x74E, 0x0, 0x15E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6D08)
    Sleep(100)
    OP_8F(0xA, 0x4B0, 0x0, 0x1612, 0x3E8, 0x0)
    OP_8C(0xA, 45, 400)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #442
        0x9,
        (
            "#646F#2P（安静些，汉斯……\x01",
            "  窗外边有人吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0xA,
        (
            "#732F#6P（喂，不要推。）\x02\x03",

            "#730F（那个……\x01",
            "  绝对不要大声叫啊？）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 45, 400)

    def lambda_6DC8():
        OP_8F(0xFE, 0x97E, 0x0, 0x1504, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6DC8)
    Sleep(50)
    OP_8F(0xA, 0x6D6, 0x0, 0x1554, 0x3E8, 0x0)
    OP_8C(0xA, 0, 400)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #444
        0x9,
        (
            "#644F#2P（好啦好啦。）\x02\x03",

            "（我堂堂学生会长乔儿大人\x01",
            "  怎么可能因为这些琐碎小事\x01",
            "  而大声尖叫呢……）\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xA, 45, 400)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #445
        "\x07\x05汉斯捂住了乔儿的嘴。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #446
        0x9,
        "#643F#4S#2P（～～～呜！！！）\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_A2(0x10FE)
    OP_A2(0x10F9)
    NewScene("ED6_DT21/T2500   ._SN", 128, 0, 0)
    IdleLoop()
    Return()

    # Function_39_6C37 end

    def Function_40_6F17(): pass

    label("Function_40_6F17")

    EventBegin(0x0)
    SetChrFlags(0x102, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x20, 255)
    OP_4A(0x12, 255)
    OP_4A(0x21, 255)
    SetChrPos(0xA, 1750, 0, 5460, 0)
    SetChrPos(0x9, 2430, 0, 5380, 0)
    SetChrPos(0x20, -240, 0, 3050, 180)
    SetChrPos(0x12, -650, 0, 2060, 90)
    SetChrPos(0x21, 350, 0, 1140, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6D(2170, 0, 5050, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(500)

    ChrTalk(    #447
        0xA,
        (
            "#730F#6P（原来如此……）\x02\x03",

            "（总之就是为了解放学院\x01",
            "  而来这里作战的啊。）\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(70, 0, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #448
        (
            "\x07\x00#1040F（就是这样。）\x02\x03",

            "（请把这消息告诉给大家吧，\x01",
            "  这样可以让大家安心些。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #449
        0x9,
        (
            "#644F#4P（是吗，那可得救了。）\x02\x03",

            "（有没有什么\x01",
            "　我们可以帮得上忙的？）\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(70, 0, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #450
        (
            "#1043F（这样吗……）\x02\x03",

            "#1042F（我想要一份学院内\x01",
            " 　所有学生和职员的名单。）\x02\x03",

            "（这样在救助时就会心中有数了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #451
        0x9,
        "#647F#4P（原来如此。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0xA,
        (
            "#730F#6P（ＯＫ。\x01",
            "　等我写给你。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #453
        (
            "\x07\x05乔儿和汉斯把记有学院中\x01",
            "学生和职员名单的笔记本\x01",
            "从窗缝中交给了约修亚。\x02\x03",

            "笔记本上写有全部人质的名单。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_28(0xC1, 0x4, 0x2)
    OP_28(0xC1, 0x4, 0x8)
    OP_28(0xC1, 0x1, 0x1)
    OP_28(0xC1, 0x1, 0x4)
    OP_28(0xC1, 0x1, 0x10)
    OP_28(0xC1, 0x1, 0x40)
    OP_28(0xC1, 0x1, 0x100)
    OP_28(0xC1, 0x1, 0x400)
    OP_28(0xC1, 0x1, 0x1000)
    OP_28(0xC1, 0x1, 0x4000)
    SetMessageWindowPos(70, 0, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #454
        (
            "\x07\x00#1053F（……谢了。）\x02\x03",

            "#1040F（再过不久，\x01",
            "　我们就会开始正式行动。）\x02\x03",

            "（在那之前，请大家先忍耐一阵。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #455
        0x9,
        "#644F#4P（嗯嗯，明白了。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0xA,
        (
            "#732F#6P（倒是你们，\x01",
            "　一定要小心行事啊！）\x02\x03",

            "#734F（还有啊……等事情解决以后，\x01",
            "　一起去食堂吃饭如何？）\x02\x03",

            "#730F（我可还有一大堆事情\x01",
            "　想要审问你这小子呢！）\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(70, 0, -1, -1)
    SetChrName("约修亚")

    AnonymousTalk(    #457
        (
            "#1054F（哈哈……明白了。\x01",
            "　到时一定还请手下留情啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FE)
    OP_A2(0x10FA)
    NewScene("ED6_DT21/T2500   ._SN", 128, 0, 0)
    IdleLoop()
    Return()

    # Function_40_6F17 end

    def Function_41_7410(): pass

    label("Function_41_7410")

    Call(0, 42)
    Call(0, 43)
    Return()

    # Function_41_7410 end

    def Function_42_7419(): pass

    label("Function_42_7419")

    EventBegin(0x0)
    OP_D2(0x270327, 0x270331, 0x1B)
    OP_D2(0x270110, 0x270120, 0x1C)
    OP_D2(0x270111, 0x270121, 0x1D)
    OP_D2(0x270130, 0x270140, 0x1E)
    OP_D2(0x270131, 0x270141, 0x1F)
    OP_D2(0x70326, 0x7032D, 0x20)
    OP_D2(0x70327, 0x7032E, 0x21)
    OP_D2(0x70318, 0x7031F, 0x22)
    OP_D2(0x70319, 0x70320, 0x23)
    OP_D2(0x26000E, 0x260013, 0x24)
    OP_D2(0x26000D, 0x260012, 0x25)
    OP_D2(0x270313, 0x27031D, 0x26)
    OP_D2(0x270326, 0x270330, 0x27)
    OP_D2(0x270312, 0x27031C, 0x28)
    SetChrPos(0x101, 59470, 0, -750, 270)
    SetChrPos(0x102, 59520, 0, 670, 270)
    SetChrPos(0x10A, 60580, 0, -780, 270)
    SetChrPos(0x10E, 60740, 0, 980, 270)
    OP_6D(61210, 0, 1040, 0)
    OP_67(0, 5170, -10000, 0)
    OP_6B(2070, 0)
    OP_6C(45000, 0)
    OP_6E(388, 0)
    SetChrPos(0x22, 50890, 0, 160, 0)
    SetChrPos(0x23, 46610, 0, -730, 90)
    ClearChrFlags(0x23, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #458
        0x22,
        "#2P你们是……！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrPos(0x22, 46610, 0, 600, 90)
    ClearChrFlags(0x22, 0x80)

    def lambda_75FC():
        OP_6D(57420, 0, 710, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_75FC)

    def lambda_7614():
        OP_67(0, 6150, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7614)

    def lambda_762C():
        OP_6B(1560, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_762C)

    def lambda_763C():
        OP_6E(530, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_763C)
    SetChrChipByIndex(0x22, 27)
    SetChrFlags(0x22, 0x1000)

    def lambda_7656():
        OP_8E(0xFE, 0xCE9A, 0x0, 0x258, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_7656)
    Sleep(100)
    SetChrChipByIndex(0x23, 38)
    SetChrFlags(0x23, 0x1000)

    def lambda_7680():
        OP_8E(0xFE, 0xCE9A, 0x0, 0xFFFFFD26, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_7680)
    WaitChrThread(0x22, 0x1)
    SetChrChipByIndex(0x22, 39)
    WaitChrThread(0x23, 0x1)
    SetChrChipByIndex(0x23, 40)
    WaitChrThread(0x23, 0x1)
    WaitChrThread(0x101, 0x1)
    Sleep(300)

    ChrTalk(    #459
        0x22,
        "#6P游、游击士吗！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 28)
    SetChrChipByIndex(0x102, 30)
    SetChrChipByIndex(0x10A, 32)
    SetChrChipByIndex(0x10E, 34)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10A, 0)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #460
        0x101,
        "#1005F#2P要来了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0x102,
        "#1042F#5P……解决他们！\x02",
    )

    CloseMessageWindow()

    def lambda_7748():
        OP_6D(57500, 0, 830, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7748)

    def lambda_7760():
        OP_6B(1300, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7760)

    def lambda_7770():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7770)
    Sleep(30)

    def lambda_7790():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7790)
    Sleep(30)
    SetChrChipByIndex(0x22, 27)
    SetChrFlags(0x22, 0x1000)

    def lambda_77BA():
        OP_90(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_77BA)

    def lambda_77D5():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_77D5)
    Sleep(30)

    def lambda_77F5():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_77F5)
    SetChrChipByIndex(0x23, 38)
    SetChrFlags(0x23, 0x1000)

    def lambda_781A():
        OP_90(0xFE, 0xBB8, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_781A)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x22, 0xFF)
    OP_44(0x23, 0xFF)
    Battle(0x79D, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_7865"),
        (SWITCH_DEFAULT, "loc_786A"),
    )


    label("loc_7865")

    OP_B4(0x0)
    Jump("loc_786A")

    label("loc_786A")

    Return()

    # Function_42_7419 end

    def Function_43_786B(): pass

    label("Function_43_786B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x22, 0x0)
    OP_44(0x23, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    Sleep(500)
    OP_6D(57200, 0, 140, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x22, 54400, 0, 970, 90)
    SetChrPos(0x23, 55400, 0, -1460, 90)
    SetChrPos(0x0, 57200, 0, 140, 270)
    SetChrPos(0x1, 57200, 0, 140, 270)
    SetChrPos(0x2, 57200, 0, 140, 270)
    SetChrPos(0x3, 57200, 0, 140, 270)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x2)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 9)
    ClearChrFlags(0x23, 0x1)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 26)
    SetChrSubChip(0x23, 12)
    OP_A2(0x2024)
    OP_A2(0x20B8)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_43_786B end

    def Function_44_79A0(): pass

    label("Function_44_79A0")

    Call(0, 45)
    Call(0, 46)
    Return()

    # Function_44_79A0 end

    def Function_45_79A9(): pass

    label("Function_45_79A9")

    EventBegin(0x0)
    OP_D2(0x270327, 0x270331, 0x1B)
    OP_D2(0x270110, 0x270120, 0x1C)
    OP_D2(0x270111, 0x270121, 0x1D)
    OP_D2(0x270130, 0x270140, 0x1E)
    OP_D2(0x270131, 0x270141, 0x1F)
    OP_D2(0x70326, 0x7032D, 0x20)
    OP_D2(0x70327, 0x7032E, 0x21)
    OP_D2(0x70318, 0x7031F, 0x22)
    OP_D2(0x70319, 0x70320, 0x23)
    OP_D2(0x26000E, 0x260013, 0x24)
    OP_D2(0x26000D, 0x260012, 0x25)
    OP_D2(0x270313, 0x27031D, 0x26)
    OP_D2(0x270326, 0x270330, 0x27)
    OP_D2(0x270312, 0x27031C, 0x28)
    SetChrPos(0x101, 24400, 0, -750, 90)
    SetChrPos(0x102, 24400, 0, 540, 90)
    SetChrPos(0x10A, 22950, 0, -1000, 90)
    SetChrPos(0x10E, 22950, 0, 390, 90)
    OP_6D(24680, 0, 950, 0)
    OP_67(0, 5520, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(45000, 0)
    OP_6E(301, 0)
    SetChrPos(0x22, 36490, 0, 600, 270)
    SetChrPos(0x23, 36490, 0, -730, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #462
        0x22,
        "你们……！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_7B76():
        OP_6D(27430, 0, 790, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7B76)

    def lambda_7B8E():
        OP_6B(2050, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7B8E)

    def lambda_7B9E():
        OP_6E(416, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7B9E)
    SetChrChipByIndex(0x22, 27)

    def lambda_7BB3():
        OP_8E(0xFE, 0x7602, 0x0, 0x258, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_7BB3)
    Sleep(100)
    SetChrChipByIndex(0x23, 38)

    def lambda_7BD8():
        OP_8E(0xFE, 0x7602, 0x0, 0xFFFFFD26, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_7BD8)
    WaitChrThread(0x22, 0x1)
    SetChrChipByIndex(0x22, 39)
    WaitChrThread(0x23, 0x1)
    SetChrChipByIndex(0x23, 40)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #463
        0x23,
        "#2P游、游击士吗！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 28)
    SetChrChipByIndex(0x102, 30)
    SetChrChipByIndex(0x10A, 32)
    SetChrChipByIndex(0x10E, 34)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10A, 0)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #464
        0x101,
        "#1005F#6P要来了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0x102,
        "#1042F#6P……解决他们！\x02",
    )

    CloseMessageWindow()

    def lambda_7C96():
        OP_6D(27140, 0, 340, 250)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7C96)

    def lambda_7CAE():
        OP_6B(1800, 250)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7CAE)

    def lambda_7CBE():
        OP_90(0xFE, 0x9C4, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7CBE)
    Sleep(30)

    def lambda_7CDE():
        OP_90(0xFE, 0x9C4, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7CDE)
    Sleep(30)
    SetChrChipByIndex(0x22, 27)
    SetChrFlags(0x22, 0x1000)

    def lambda_7D08():
        OP_90(0xFE, 0xFFFFF63C, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_7D08)

    def lambda_7D23():
        OP_90(0xFE, 0x9C4, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_7D23)
    Sleep(30)

    def lambda_7D43():
        OP_90(0xFE, 0x9C4, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_7D43)
    SetChrChipByIndex(0x23, 38)
    SetChrFlags(0x23, 0x1000)

    def lambda_7D68():
        OP_90(0xFE, 0xFFFFF63C, 0x0, 0x0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_7D68)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x22, 0xFF)
    OP_44(0x23, 0xFF)
    Battle(0x79D, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_7DB3"),
        (SWITCH_DEFAULT, "loc_7DB8"),
    )


    label("loc_7DB3")

    OP_B4(0x0)
    Jump("loc_7DB8")

    label("loc_7DB8")

    Return()

    # Function_45_79A9 end

    def Function_46_7DB9(): pass

    label("Function_46_7DB9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x22, 0x0)
    OP_44(0x23, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    Sleep(500)
    OP_6D(28050, 0, -20, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x22, 28800, 0, 700, 270)
    SetChrPos(0x23, 29240, 0, -1490, 270)
    SetChrPos(0x0, 27220, 0, -10, 90)
    SetChrPos(0x1, 27220, 0, -10, 90)
    SetChrPos(0x2, 27220, 0, -10, 90)
    SetChrPos(0x3, 27220, 0, -10, 90)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x2)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 10)
    ClearChrFlags(0x23, 0x1)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 26)
    SetChrSubChip(0x23, 12)
    OP_A2(0x2024)
    OP_A2(0x20B9)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_46_7DB9 end

    def Function_47_7EEE(): pass

    label("Function_47_7EEE")

    Call(0, 48)
    Call(0, 49)
    Return()

    # Function_47_7EEE end

    def Function_48_7EF7(): pass

    label("Function_48_7EF7")

    EventBegin(0x0)
    OP_D2(0x270327, 0x270331, 0x1B)
    OP_D2(0x270110, 0x270120, 0x1C)
    OP_D2(0x270111, 0x270121, 0x1D)
    OP_D2(0x270130, 0x270140, 0x1E)
    OP_D2(0x270131, 0x270141, 0x1F)
    OP_D2(0x70326, 0x7032D, 0x20)
    OP_D2(0x70327, 0x7032E, 0x21)
    OP_D2(0x70318, 0x7031F, 0x22)
    OP_D2(0x70319, 0x70320, 0x23)
    OP_D2(0x26000E, 0x260013, 0x24)
    OP_D2(0x26000D, 0x260012, 0x25)
    OP_D2(0x270313, 0x27031D, 0x26)
    OP_D2(0x270326, 0x270330, 0x27)
    OP_D2(0x270312, 0x27031C, 0x28)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    SetChrPos(0x22, 41170, 0, 4220, 90)
    SetChrPos(0x23, 42610, 0, 4220, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrChipByIndex(0x22, 37)
    SetChrSubChip(0x22, 0)
    SetChrChipByIndex(0x23, 36)
    SetChrSubChip(0x23, 0)
    OP_6D(42710, 0, 5190, 0)
    OP_67(0, 5580, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_8035():
        OP_6D(42460, 0, 490, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8035)

    def lambda_804D():
        OP_6E(302, 1500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_804D)
    SetChrChipByIndex(0x101, 28)
    SetChrChipByIndex(0x102, 30)
    SetChrChipByIndex(0x10A, 32)
    SetChrChipByIndex(0x10E, 34)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x10A, 0)
    SetChrSubChip(0x10E, 0)
    OP_43(0x101, 0x1, 0x0, 0x32)
    OP_43(0x102, 0x1, 0x0, 0x33)
    OP_43(0x10A, 0x1, 0x0, 0x34)
    OP_43(0x10E, 0x1, 0x0, 0x35)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)

    def lambda_80BD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_80BD)
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)

    def lambda_80E7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_80E7)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x10E, 0x1)

    ChrTalk(    #466
        0x22,
        "#5P你们……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0x23,
        "#5P游、游击士！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x22, 39)
    SetChrSubChip(0x22, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x23, 40)
    SetChrSubChip(0x23, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #468
        0x101,
        "#1006F#6P速战速决！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0x102,
        "#1046F#4P……解决他们！\x02",
    )

    CloseMessageWindow()

    def lambda_8199():
        OP_6D(42680, 0, 1100, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8199)

    def lambda_81B1():
        OP_6B(2420, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_81B1)

    def lambda_81C1():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_81C1)
    Sleep(30)

    def lambda_81E1():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_81E1)
    Sleep(30)
    SetChrChipByIndex(0x22, 27)
    SetChrFlags(0x22, 0x1000)

    def lambda_820B():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_820B)

    def lambda_8226():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_8226)
    Sleep(30)

    def lambda_8246():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_8246)
    SetChrChipByIndex(0x23, 38)
    SetChrFlags(0x23, 0x1000)

    def lambda_826B():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_826B)
    WaitChrThread(0x101, 0x3)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x22, 0xFF)
    OP_44(0x23, 0xFF)
    Battle(0x79D, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_82B6"),
        (SWITCH_DEFAULT, "loc_82BB"),
    )


    label("loc_82B6")

    OP_B4(0x0)
    Jump("loc_82BB")

    label("loc_82BB")

    Return()

    # Function_48_7EF7 end

    def Function_49_82BC(): pass

    label("Function_49_82BC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x22, 0x0)
    OP_44(0x23, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    Sleep(500)
    OP_6D(41790, 0, 1060, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x22, 42290, 0, 3240, 180)
    SetChrPos(0x23, 39710, 0, 1520, 180)
    SetChrPos(0x0, 41790, 0, 1060, 0)
    SetChrPos(0x1, 41790, 0, 1060, 0)
    SetChrPos(0x2, 41790, 0, 1060, 0)
    SetChrPos(0x3, 41790, 0, 1060, 0)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x2)
    SetChrChipByIndex(0x22, 26)
    SetChrSubChip(0x22, 10)
    ClearChrFlags(0x23, 0x1)
    SetChrFlags(0x23, 0x2)
    SetChrChipByIndex(0x23, 26)
    SetChrSubChip(0x23, 13)
    OP_A2(0x2024)
    OP_A2(0x20B7)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_49_82BC end

    def Function_50_83F1(): pass

    label("Function_50_83F1")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 41710, -500, -5250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8418():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8418)
    OP_8E(0xFE, 0xA2EE, 0xFFFFFF06, 0xFFFFF4D4, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_50_83F1 end

    def Function_51_8440(): pass

    label("Function_51_8440")

    Sleep(80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 42810, -500, -5250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_846C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_846C)
    OP_8E(0xFE, 0xA73A, 0xFFFFFF06, 0xFFFFF4D4, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_51_8440 end

    def Function_52_8494(): pass

    label("Function_52_8494")

    Sleep(200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 41090, -500, -5250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_84C0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_84C0)
    OP_8E(0xFE, 0xA082, 0xFFFFFF06, 0xFFFFEF98, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_52_8494 end

    def Function_53_84E8(): pass

    label("Function_53_84E8")

    Sleep(350)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 42620, -500, -5250, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8514():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8514)
    OP_8E(0xFE, 0xA67C, 0xFFFFFF06, 0xFFFFEFC0, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_53_84E8 end

    def Function_54_853C(): pass

    label("Function_54_853C")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_6D(116200, 10, 5150, 0)
    OP_67(0, 5900, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0xB, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_85B2():
        OP_6D(117060, 0, 4540, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_85B2)

    def lambda_85CA():
        OP_6E(282, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_85CA)
    OP_43(0x101, 0x1, 0x0, 0x37)
    OP_43(0x102, 0x1, 0x0, 0x38)
    OP_43(0x10A, 0x1, 0x0, 0x39)
    OP_43(0x10E, 0x1, 0x0, 0x3A)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_862E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_862E)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #470
        0x8,
        "#780F#5P噢噢……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0xB,
        "#5P大家……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0x101,
        "#1006F#6P嘿嘿，我们来帮忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #473
        0x102,
        "#1035F#4P……好久不见了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x8,
        (
            "#783F#5P艾丝蒂尔，约修亚。\x01",
            "你们竟然来了……\x02\x03",

            "#780F后面的各位\x01",
            "也是协会的游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #475
        0x10E,
        (
            "#843F#4P是的。\x01",
            "在下是克鲁茨·纳尔当。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #476
        0x10A,
        (
            "#1310F#6P初次见面！\x01",
            "我是亚妮拉丝·艾尔菲德。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #477
        "\x07\x05将事情的经过和学院解放计划做了说明。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #478
        0x8,
        (
            "#783F#5P是吗……非常感谢。\x02\x03",

            "#782F率领士兵侵袭这里的人是谁\x01",
            "你们知道了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0x101,
        (
            "#1007F#6P不就是前市长秘书基尔巴特吗？\x02\x03",

            "#1019F听说那个家伙\x01",
            "打起了科洛丝的主意……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0x8,
        (
            "#782F#5P嗯～不过他好像\x01",
            "并不知道科洛丝\x01",
            "就是公主，\x02\x03",

            "只不过是得到了\x01",
            "公主在这间学院\x01",
            "就读的情报而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0x101,
        (
            "#1015F#6P这、这个嘛……\x02\x03",

            "但想想那个怪盗，\x01",
            "他就算不知道也不奇怪。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #482
        0x102,
        (
            "#1035F#2P执行者和普通战斗员的\x01",
            "权限有着天壤之别。\x02\x03",

            "#1040F像这种情报应该\x01",
            "不会告诉他的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #483
        0x101,
        "#1016F#6P原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #484
        0x10A,
        (
            "#817F#6P不过，那样的话……\x02\x03",

            "#812F其它的女学生很可能\x01",
            "也会被牵连进来的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #485
        0x10E,
        "#842F#4P啊啊，确实有那种危险性。\x02",
    )

    CloseMessageWindow()

    def lambda_89F9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_89F9)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #486
        0x8,
        (
            "#783F#5P我也很担心这一点呢……\x02\x03",

            "#782F抱歉，\x01",
            "只能拜托你们多费心了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0x101,
        "#1002F#6P嗯，明白了！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #488
        (
            "\x07\x05取出游击士手册，\x01",
            "在科林兹校长、珐奥娜\x01",
            "的名字上做了标记。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2025)
    OP_28(0xC0, 0x1, 0x100)
    OP_28(0xC1, 0x2, 0x1)
    OP_28(0xC1, 0x1, 0x2)
    Fade(500)
    OP_6D(116280, 0, 2740, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 116280, 0, 2740, 0)
    SetChrPos(0x1, 116280, 0, 2740, 0)
    SetChrPos(0x2, 116280, 0, 2740, 0)
    SetChrPos(0x3, 116280, 0, 2740, 0)
    OP_4B(0xB, 255)
    OP_0D()
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_54_853C end

    def Function_55_8B71(): pass

    label("Function_55_8B71")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 117010, 0, -3090, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8B98():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8B98)
    OP_8E(0xFE, 0x1C93A, 0x0, 0x546, 0xFA0, 0x0)
    OP_8E(0xFE, 0x1C322, 0x0, 0xABE, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_55_8B71 end

    def Function_56_8BD4(): pass

    label("Function_56_8BD4")

    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 117010, 0, -3090, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8C00():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8C00)
    OP_8E(0xFE, 0x1C93A, 0x0, 0x546, 0xFA0, 0x0)
    OP_8E(0xFE, 0x1C764, 0x0, 0xA78, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_56_8BD4 end

    def Function_57_8C3C(): pass

    label("Function_57_8C3C")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 117010, 0, -3090, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8C68():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8C68)
    OP_8E(0xFE, 0x1C93A, 0x0, 0x2E4, 0xFA0, 0x0)
    OP_8E(0xFE, 0x1C64C, 0x0, 0x690, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_57_8C3C end

    def Function_58_8CA4(): pass

    label("Function_58_8CA4")

    Sleep(1200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 117010, 0, -3090, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_8CD0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8CD0)
    OP_8E(0xFE, 0x1CA8E, 0x0, 0x622, 0xFA0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_58_8CA4 end

    def Function_59_8CF8(): pass

    label("Function_59_8CF8")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_6D(2620, 0, 5110, 0)
    OP_67(0, 4990, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(45000, 0)
    OP_6E(295, 0)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x20, 255)
    OP_4A(0x12, 255)
    OP_4A(0x21, 255)
    SetChrPos(0xA, 1470, 0, 5490, 0)
    SetChrPos(0x9, 2500, 0, 5490, 0)
    SetChrPos(0x20, -240, 0, 3050, 180)
    SetChrPos(0x12, -650, 0, 2060, 90)
    SetChrPos(0x21, 350, 0, 1140, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xC0, 0x0, 0x64)
    Sleep(500)

    def lambda_8DE7():
        OP_6D(3110, 0, 3980, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8DE7)

    def lambda_8DFF():
        OP_6E(327, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8DFF)
    OP_43(0x101, 0x1, 0x0, 0x3C)
    OP_43(0x102, 0x1, 0x0, 0x3D)
    OP_43(0x10A, 0x1, 0x0, 0x3E)
    OP_43(0x10E, 0x1, 0x0, 0x3F)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_8E42():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8E42)
    Sleep(100)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_8E6C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8E6C)
    Sleep(100)
    OP_62(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_8E96():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_8E96)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_8EC0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8EC0)
    Sleep(50)
    OP_62(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_8EEA():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8EEA)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #489
        0x9,
        "#641F#5P啊！你们两个终于来了啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0xA,
        (
            "#731F#5P哎呀～等啊等啊\x01",
            "都已经等得不耐烦了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0x101,
        (
            "#1008F#6P嘿嘿……\x01",
            "抱歉，久等啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #492
        0x102,
        "#1040F#4P那之后情况有什么变化吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0x9,
        "#645F#5P嗯，其实呢……\x02",
    )

    CloseMessageWindow()

    def lambda_8FC2():
        OP_6D(3880, 0, 3670, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8FC2)

    def lambda_8FDA():
        OP_8F(0xFE, 0xD34, 0x0, 0x1108, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8FDA)
    Sleep(100)
    OP_8E(0xA, 0x956, 0x0, 0x14AA, 0xBB8, 0x0)
    OP_8E(0xA, 0x988, 0x0, 0x116C, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #494
        0x9,
        (
            "#642F#5P（刚才基尔巴特来了一趟，\x01",
            "  问王家的公主在不在这里。）\x02\x03",

            "（还说如果主动坦白的话\x01",
            "  可以得到特别待遇。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0x101,
        "#1019F#6P（哎呀呀～……）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0x102,
        "#1035F#4P（……还真是个彻底的蠢材啊。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #497
        0xA,
        (
            "#734F#5P（嗯，总之我们就把他\x01",
            "  搪塞过去了……）\x02\x03",

            "#732F（不过说不定他还会\x01",
            "干出什么事呢。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0x101,
        "#1002F#6P（嗯，我们会留意他的。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0x20,
        "#6P喂，喂……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0x21,
        (
            "#6P那个，我们\x01",
            "现在能做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_91A2():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_91A2)

    def lambda_91B0():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_91B0)
    Sleep(80)

    def lambda_91C3():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_91C3)

    def lambda_91D1():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_91D1)
    Sleep(80)

    def lambda_91E4():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_91E4)
    OP_8C(0xA, 225, 400)

    ChrTalk(    #501
        0x101,
        (
            "#1004F#2P啊，不好意思。\x02\x03",

            "#1006F在危机彻底解除之前，\x01",
            "大家先待在这里别动可以吗？\x02\x03",

            "外边的战斗现在还没结束呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0x21,
        "#6P明白啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #503
        0x20,
        (
            "#6P呼……\x01",
            "拜托饶了我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0x12,
        (
            "#6P真、真是紧张，\x01",
            "但我会努力等的！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0x102,
        (
            "#1040F#2P抱歉，我们会尽快\x01",
            "将事情解决的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)

    ChrTalk(    #506
        0x102,
        "#1042F#4P汉斯、乔儿，你们也……\x02",
    )

    CloseMessageWindow()

    def lambda_931A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_931A)
    Sleep(50)

    def lambda_932D():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_932D)
    Sleep(50)

    def lambda_9340():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9340)
    Sleep(50)

    def lambda_9353():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9353)
    Sleep(50)

    def lambda_9366():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_9366)
    Sleep(50)
    OP_8C(0x10E, 0, 400)

    ChrTalk(    #507
        0x9,
        (
            "#644F#5P是是，我们明白。\x02\x03",

            "#648F不会给你们添麻烦的，\x01",
            "只会成为你们的累赘呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0xA,
        (
            "#730F#5P等事情都搞定后再来吧。\x02\x03",

            "到时的善后工作\x01",
            "留给我们做就ＯＫ了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0x102,
        "#1049F#4P嗯，到时就拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #510
        0x101,
        "#1006F#6P好了，那一会儿再见了！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #511
        (
            "\x07\x05取出游击士手册，\x01",
            "在乔儿、汉斯、坎诺、雅莉丝、\x01",
            "帕布尔的名字上做了标记。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2026)
    OP_28(0xC0, 0x1, 0x200)
    OP_28(0xC1, 0x2, 0x4000)
    OP_28(0xC1, 0x1, 0x8000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(2970, 0, 170, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0xA, 3470, 0, 2580, 180)
    SetChrPos(0x9, 3500, 0, 1470, 0)
    SetChrPos(0x20, -240, 0, 3050, 90)
    SetChrPos(0x12, -650, 0, 2060, 90)
    SetChrPos(0x21, 350, 0, 1140, 90)
    SetChrPos(0x0, 2970, 0, 170, 180)
    SetChrPos(0x1, 2970, 0, 170, 180)
    SetChrPos(0x2, 2970, 0, 170, 180)
    SetChrPos(0x3, 2970, 0, 170, 180)
    OP_69(0x0, 0x0)
    OP_4B(0xA, 255)
    OP_4B(0x9, 255)
    OP_4B(0x20, 255)
    OP_4B(0x12, 255)
    OP_4B(0x21, 255)
    OP_8C(0x20, 180, 0)
    OP_8C(0x12, 90, 0)
    OP_8C(0x21, 0, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_59_8CF8 end

    def Function_60_9602(): pass

    label("Function_60_9602")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 3040, 0, -2940, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9629():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9629)
    OP_8E(0xFE, 0x97E, 0x0, 0xAD2, 0xFA0, 0x0)
    Return()

    # Function_60_9602 end

    def Function_61_964A(): pass

    label("Function_61_964A")

    Sleep(400)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 3040, 0, -2940, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9676():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9676)
    OP_8E(0xFE, 0xD98, 0x0, 0xA6E, 0xFA0, 0x0)
    Return()

    # Function_61_964A end

    def Function_62_9697(): pass

    label("Function_62_9697")

    Sleep(800)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 3040, 0, -2940, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_96C3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_96C3)
    OP_8E(0xFE, 0x884, 0x0, 0x53C, 0xFA0, 0x0)
    Return()

    # Function_62_9697 end

    def Function_63_96E4(): pass

    label("Function_63_96E4")

    Sleep(1200)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 3040, 0, -2940, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_9710():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9710)
    OP_8E(0xFE, 0xD48, 0x0, 0x546, 0xFA0, 0x0)
    Return()

    # Function_63_96E4 end

    def Function_64_9731(): pass

    label("Function_64_9731")

    Call(0, 65)
    Call(0, 66)
    Return()

    # Function_64_9731 end

    def Function_65_973A(): pass

    label("Function_65_973A")

    EventBegin(0x0)
    OP_D2(0x270327, 0x270331, 0x1B)
    OP_D2(0x270110, 0x270120, 0x1C)
    OP_D2(0x270111, 0x270121, 0x1D)
    OP_D2(0x270130, 0x270140, 0x1E)
    OP_D2(0x270131, 0x270141, 0x1F)
    OP_D2(0x70326, 0x7032D, 0x20)
    OP_D2(0x70327, 0x7032E, 0x21)
    OP_D2(0x70318, 0x7031F, 0x22)
    OP_D2(0x70319, 0x70320, 0x23)
    OP_D2(0x26000E, 0x260013, 0x24)
    OP_D2(0x26000D, 0x260012, 0x25)
    OP_D2(0x270313, 0x27031D, 0x26)
    OP_D2(0x270327, 0x270331, 0x27)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_6D(44540, 0, 38690, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x24, 36)
    SetChrChipByIndex(0x25, 37)
    SetChrPos(0x24, 32720, 0, 29970, 90)
    SetChrPos(0x25, 51040, 0, 29970, 270)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    FadeToBright(1000, 0)

    def lambda_9854():
        OP_6D(41850, 0, 30040, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9854)

    def lambda_986C():
        OP_8E(0xFE, 0x9FBA, 0x0, 0x7512, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_986C)

    def lambda_9887():
        OP_8E(0xFE, 0xA6EA, 0x0, 0x7512, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_9887)
    WaitChrThread(0x24, 0x1)
    WaitChrThread(0x25, 0x1)
    SetChrSubChip(0x24, 0)
    SetChrSubChip(0x25, 0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #512
        0x24,
        (
            "#6P喂……\x01",
            "你有没有听到外面有枪声？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0x25,
        "#2P……你也听到了吗。\x02",
    )

    CloseMessageWindow()

    def lambda_98FE():
        OP_6D(42070, 0, 27750, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_98FE)

    def lambda_9916():
        OP_8E(0xFE, 0x9E7A, 0x0, 0x6874, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9916)
    Sleep(100)

    def lambda_9936():
        OP_8E(0xFE, 0xA5BE, 0x0, 0x6892, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_9936)
    WaitChrThread(0x24, 0x1)
    WaitChrThread(0x25, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #514
        0x24,
        (
            "#5P不过正门的防线\x01",
            "看起来还没有被突破啊……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x101, 46770, -2000, 38650, 270)

    ChrTalk(    #515
        0x101,
        "#4P那只是佯攻而已。\x02",
    )

    CloseMessageWindow()
    OP_62(0x24, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_99F2():
        OP_6D(42800, 0, 31350, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_99F2)

    def lambda_9A0A():
        OP_67(0, 6030, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9A0A)

    def lambda_9A22():
        OP_6E(337, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9A22)

    def lambda_9A32():
        OP_6B(2500, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_9A32)

    def lambda_9A42():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9A42)
    OP_43(0x101, 0x1, 0x0, 0x43)
    Sleep(250)

    def lambda_9A5C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_9A5C)
    OP_43(0x102, 0x1, 0x0, 0x44)
    Sleep(250)
    OP_43(0x10A, 0x1, 0x0, 0x45)
    Sleep(250)
    OP_43(0x10E, 0x1, 0x0, 0x46)
    WaitChrThread(0x102, 0x2)

    ChrTalk(    #516
        0x25,
        "#4P什…么…！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0x24,
        (
            "#6P怎、怎么会！？\x01",
            "你们是怎么进来的！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #518
        0x101,
        "#1029F#6P哼哼，答案很简单……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0x10A,
        "#816F#5P因为我们是游击士！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #520
        0x102,
        "#1048F#6P（根本就是答非所问嘛……）\x02",
    )

    CloseMessageWindow()

    def lambda_9B3B():
        OP_6D(42340, 0, 30650, 280)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9B3B)

    def lambda_9B53():
        OP_6B(2320, 280)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9B53)
    OP_0D()

    def lambda_9B64():
        OP_94(0x0, 0xFE, 0x0, 0x9C4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B64)
    Sleep(30)
    SetChrChipByIndex(0x24, 38)
    SetChrFlags(0x24, 0x1000)

    def lambda_9B89():
        OP_94(0x0, 0xFE, 0x0, 0x9C4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_9B89)

    def lambda_9B9F():
        OP_94(0x0, 0xFE, 0x0, 0x9C4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9B9F)
    Sleep(30)
    SetChrChipByIndex(0x25, 39)
    SetChrFlags(0x25, 0x1000)

    def lambda_9BC4():
        OP_94(0x0, 0xFE, 0x0, 0x9C4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 3, lambda_9BC4)

    def lambda_9BDA():
        OP_94(0x0, 0xFE, 0x0, 0x9C4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_9BDA)
    Sleep(30)

    def lambda_9BF5():
        OP_94(0x0, 0xFE, 0x0, 0x9C4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_9BF5)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10E, 0xFF)
    OP_44(0x24, 0xFF)
    OP_44(0x25, 0xFF)
    Battle(0x79F, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_9C3B"),
        (SWITCH_DEFAULT, "loc_9C40"),
    )


    label("loc_9C3B")

    OP_B4(0x0)
    Jump("loc_9C40")

    label("loc_9C40")

    Return()

    # Function_65_973A end

    def Function_66_9C41(): pass

    label("Function_66_9C41")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x24, 0x0)
    OP_44(0x25, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)
    OP_44(0x10E, 0x1)
    OP_44(0x102, 0x1)
    Sleep(500)
    OP_6D(41850, 0, 31500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x10A, 65535)
    SetChrChipByIndex(0x10E, 65535)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x24, 39960, 0, 29850, 0)
    SetChrPos(0x25, 42350, 0, 29860, 0)
    ClearChrFlags(0x24, 0x1)
    SetChrFlags(0x24, 0x2)
    SetChrChipByIndex(0x24, 26)
    SetChrSubChip(0x24, 12)
    ClearChrFlags(0x25, 0x1)
    SetChrFlags(0x25, 0x2)
    SetChrChipByIndex(0x25, 26)
    SetChrSubChip(0x25, 10)
    SetChrPos(0x0, 41850, 0, 31500, 180)
    SetChrPos(0x1, 41850, 0, 31500, 180)
    SetChrPos(0x2, 41850, 0, 31500, 180)
    SetChrPos(0x3, 41850, 0, 31500, 180)
    OP_69(0x0, 0x0)
    OP_A2(0x2027)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_66_9C41 end

    def Function_67_9D73(): pass

    label("Function_67_9D73")

    SetChrChipByIndex(0x101, 28)
    SetChrPos(0xFE, 46560, -2000, 38540, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xA316, 0x0, 0x9646, 0x1770, 0x0)
    OP_8E(0xFE, 0x9FA6, 0x0, 0x834A, 0x1770, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_67_9D73 end

    def Function_68_9DBE(): pass

    label("Function_68_9DBE")

    SetChrChipByIndex(0x102, 30)
    SetChrPos(0xFE, 46560, -2000, 38540, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xA316, 0x0, 0x9646, 0x1770, 0x0)
    OP_8E(0xFE, 0x9F1A, 0x0, 0x8912, 0x1770, 0x0)
    OP_8E(0xFE, 0xA4C4, 0x0, 0x8318, 0x1770, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_68_9DBE end

    def Function_69_9E1D(): pass

    label("Function_69_9E1D")

    SetChrChipByIndex(0x10A, 32)
    SetChrPos(0xFE, 46560, -2000, 38540, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xA316, 0x0, 0x9646, 0x1770, 0x0)
    OP_8E(0xFE, 0x9FD8, 0x0, 0x8836, 0x1770, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_69_9E1D end

    def Function_70_9E68(): pass

    label("Function_70_9E68")

    SetChrChipByIndex(0x10E, 34)
    SetChrPos(0xFE, 46560, -2000, 38540, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xA316, 0x0, 0x9646, 0x1770, 0x0)
    OP_8E(0xFE, 0x9F24, 0x0, 0x8E94, 0x1770, 0x0)
    OP_8E(0xFE, 0xA56E, 0x0, 0x88E0, 0x1770, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_70_9E68 end

    def Function_71_9EC7(): pass

    label("Function_71_9EC7")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_6D(500, 0, 33070, 0)
    OP_67(0, 6800, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(272, 0)
    OP_4A(0x14, 255)
    OP_4A(0x1A, 255)
    OP_4A(0x15, 255)
    OP_4A(0x1C, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xC0, 0x0, 0x64)
    Sleep(500)

    def lambda_9F49():
        OP_6D(2270, 0, 33520, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9F49)

    def lambda_9F61():
        OP_67(0, 6160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9F61)

    def lambda_9F79():
        OP_6B(3040, 2000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9F79)

    def lambda_9F89():
        OP_6E(267, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_9F89)
    OP_43(0x101, 0x1, 0x0, 0x48)
    OP_43(0x10A, 0x1, 0x0, 0x49)
    OP_43(0x102, 0x1, 0x0, 0x4A)
    OP_43(0x10E, 0x1, 0x0, 0x4B)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_9FCC():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_9FCC)
    Sleep(100)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_9FF6():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_9FF6)
    Sleep(100)
    OP_62(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_A020():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A020)
    Sleep(100)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_A04A():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A04A)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #521
        0x14,
        "#6P你、你们是……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0x15,
        (
            "#6P艾丝蒂尔，还有…\x01",
            "约修亚！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #523
        0x101,
        "#1008F#5P嘿嘿，好久不见啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #524
        0x102,
        "#1054F#2P好久不见了，各位。\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #525
        0x14,
        (
            "#6P你、你们为什么\x01",
            "会在这里呢！？\x02\x03",

            "难、难道\x01",
            "你们也是他们一伙的吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x14, 400)

    ChrTalk(    #526
        0x1C,
        (
            "#6P罗基克你真是笨啦，\x01",
            "这怎么可能嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #527
        0x1A,
        (
            "#6P各位游击士，\x01",
            "你们是来救我们的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1C, 90, 400)

    ChrTalk(    #528
        0x101,
        "#1006F#5P嗯，正是。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #529
        (
            "\x07\x05将作战计划，以及解救人质\x01",
            "的经过向大家说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #530
        0x14,
        (
            "#6P是、是吗……\x01",
            "不好意思啊，搞错了……\x02\x03",

            "那么……！\x01",
            "我们现在该怎么做才好！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #531
        0x10E,
        (
            "#843F#2P在事态彻底平息之前，\x01",
            "请大家先在这里不要动。\x02\x03",

            "#840F贸然跑出去的话\x01",
            "很有可能会被卷入战斗中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #532
        0x14,
        (
            "#6P可、可是，在这里待着的话\x01",
            "也有可能会被他们抓住的啊……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #533
        0x10A,
        (
            "#818F#2P嗯，虽然确实有这种可能，\x01",
            "但总比到外边安全吧？\x02\x03",

            "#819F外边现在到处是流弹和装甲兽，\x01",
            "你可不想被那些猛兽吞下肚吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #534
        0x14,
        "#6P哇、哇啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #535
        0x101,
        (
            "#1016F#6P好了啦～亚妮拉丝。\x01",
            "你怎么可以吓唬人嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #536
        0x102,
        (
            "#1040F#2P不过情况就是这样，请各位\x01",
            "先待在这里不要动，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #537
        0x15,
        "#6P是……明白了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #538
        0x1C,
        "#6P要加油啊！各位游击士！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #539
        (
            "\x07\x05取出游击士手册，\x01",
            "在罗基克、亚吉鲁、莫妮卡、塞尔玛\x01",
            "的名字上做了标记。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2028)
    OP_28(0xC0, 0x1, 0x400)
    OP_28(0xC1, 0x2, 0x400)
    OP_28(0xC1, 0x1, 0x800)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(2880, 0, 31810, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 2880, 0, 31810, 180)
    SetChrPos(0x1, 2880, 0, 31810, 180)
    SetChrPos(0x2, 2880, 0, 31810, 180)
    SetChrPos(0x3, 2880, 0, 31810, 180)
    OP_69(0x0, 0x0)
    OP_8C(0x14, 225, 0)
    OP_8C(0x1A, 0, 0)
    OP_8C(0x15, 180, 0)
    OP_8C(0x1C, 45, 0)
    OP_4B(0x14, 255)
    OP_4B(0x1A, 255)
    OP_4B(0x15, 255)
    OP_4B(0x1C, 255)
    OP_0D()
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_71_9EC7 end

    def Function_72_A5AB(): pass

    label("Function_72_A5AB")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 2960, 0, 27000, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A5D2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A5D2)
    OP_8E(0xFE, 0x870, 0x0, 0x7F76, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_72_A5AB end

    def Function_73_A5FA(): pass

    label("Function_73_A5FA")

    Sleep(300)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 2960, 0, 27000, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A626():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A626)
    OP_8E(0xFE, 0xD34, 0x0, 0x80DE, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_73_A5FA end

    def Function_74_A64E(): pass

    label("Function_74_A64E")

    Sleep(600)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 2960, 0, 27000, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A67A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A67A)
    OP_8E(0xFE, 0x87A, 0x0, 0x7AE4, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_74_A64E end

    def Function_75_A6A2(): pass

    label("Function_75_A6A2")

    Sleep(900)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 2960, 0, 27000, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_A6CE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A6CE)
    OP_8E(0xFE, 0xCE4, 0x0, 0x7B84, 0xFA0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_75_A6A2 end

    def Function_76_A6F6(): pass

    label("Function_76_A6F6")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x10A, 0x80)
    SetChrFlags(0x10E, 0x80)
    OP_6D(94250, 0, 35630, 0)
    OP_67(0, 5240, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(268, 0)
    OP_4A(0x18, 255)
    OP_4A(0x17, 255)
    OP_4A(0x1D, 255)
    OP_4A(0x1E, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_22(0xC0, 0x0, 0x64)
    Sleep(500)

    def lambda_A778():
        OP_6D(94080, 0, 35020, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A778)

    def lambda_A790():
        OP_6E(277, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_A790)
    OP_43(0x101, 0x1, 0x0, 0x4D)
    OP_43(0x10A, 0x1, 0x0, 0x4F)
    OP_43(0x102, 0x1, 0x0, 0x4E)
    OP_43(0x10E, 0x1, 0x0, 0x50)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_A7D3():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A7D3)
    Sleep(100)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_A7FD():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_A7FD)
    Sleep(100)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_A827():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A827)
    Sleep(100)
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_A851():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A851)
    Sleep(1000)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #540
        0x1E,
        "#5P你们是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #541
        0x101,
        "#1002F大家没事吧！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #542
        0x102,
        (
            "#1040F好像没有\x01",
            "受伤的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #543
        0x18,
        (
            "#5P艾丝蒂尔……\x01",
            "连约修亚也在！？\x02\x03",

            "为什么会在这里！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #544
        0x101,
        "#1006F嗯，是这样……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #545
        (
            "\x07\x05把至今为止的作战状况\x01",
            "向基诺奇奥等人说明了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #546
        0x17,
        (
            "#5P原来如此……\x01",
            "原来是那样的吗？\x02\x03",

            "这样的话真是该\x01",
            "感谢米克啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #547
        0x1D,
        (
            "#5P哼、哼……\x01",
            "那家伙不但平时上课总是偷懒，\x01",
            "这次又一个人逃跑，\x02\x03",

            "简直是笑柄啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x1D, 400)

    ChrTalk(    #548
        0x18,
        "#5P别胡说了！德尼斯。\x02",
    )

    CloseMessageWindow()

    def lambda_AA16():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_AA16)
    Sleep(100)

    def lambda_AA29():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_AA29)
    Sleep(100)

    def lambda_AA3C():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA3C)
    Sleep(100)

    def lambda_AA4F():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA4F)
    Sleep(100)
    OP_8C(0x10A, 45, 400)

    ChrTalk(    #549
        0x1E,
        (
            "#4P在这样的紧急情况下，\x01",
            "他的行动非常正确合理。\x02\x03",

            "多亏了他，艾丝蒂尔她们\x01",
            "才会及时赶来救我们。\x02\x03",

            "再继续这样侮辱和贬低他，\x01",
            "反而会降低自己的价值哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #550
        0x1D,
        "#5P唔、唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #551
        0x101,
        "#1016F#6P好了好了，大家都冷静。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #552
        0x102,
        (
            "#1040F#4P总之，在确认情况彻底安全之前，\x01",
            "希望大家待在这里别动，\x02\x03",

            "可以吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 180, 400)

    ChrTalk(    #553
        0x18,
        "#5P可、可是……\x02",
    )

    CloseMessageWindow()

    def lambda_AB9F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_AB9F)
    Sleep(100)

    def lambda_ABB2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ABB2)
    Sleep(100)

    def lambda_ABC5():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ABC5)
    Sleep(100)

    def lambda_ABD8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_ABD8)
    Sleep(100)

    def lambda_ABEB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_ABEB)
    Sleep(500)

    ChrTalk(    #554
        0x18,
        "#5P……我明白了，没问题。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 180, 400)
    OP_8C(0x1E, 225, 400)

    ChrTalk(    #555
        0x1E,
        (
            "#5P……其它的学生\x01",
            "也请你们解救出来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 45, 400)

    ChrTalk(    #556
        0x101,
        "#1006F#6P嗯，就交给我们吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #557
        (
            "\x07\x05取出游击士手册，\x01",
            "在基诺奇奥、巴托姆、德尼斯、蕾娜\x01",
            "的名字上做了标记。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_A2(0x2029)
    OP_28(0xC0, 0x1, 0x800)
    OP_28(0xC1, 0x2, 0x1000)
    OP_28(0xC1, 0x1, 0x2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(92940, 0, 32090, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 92940, 0, 32090, 180)
    SetChrPos(0x1, 92940, 0, 32090, 180)
    SetChrPos(0x2, 92940, 0, 32090, 180)
    SetChrPos(0x3, 92940, 0, 32090, 180)
    OP_69(0x0, 0x0)
    OP_8C(0x17, 90, 0)
    OP_8C(0x18, 270, 0)
    SetChrPos(0x1D, 94990, 250, 35500, 233)
    SetChrPos(0x1E, 94520, 250, 33430, 270)
    OP_4B(0x18, 255)
    OP_4B(0x17, 255)
    OP_4B(0x1D, 255)
    OP_4B(0x1E, 255)
    OP_0D()
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_76_A6F6 end

    def Function_77_ADE0(): pass

    label("Function_77_ADE0")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 92950, 0, 26920, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_AE07():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AE07)
    OP_8E(0xFE, 0x168B4, 0x0, 0x821E, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_77_ADE0 end

    def Function_78_AE2F(): pass

    label("Function_78_AE2F")

    Sleep(300)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 92950, 0, 26920, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_AE5B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AE5B)
    OP_8E(0xFE, 0x16CBA, 0x0, 0x81C4, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_78_AE2F end

    def Function_79_AE83(): pass

    label("Function_79_AE83")

    Sleep(600)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 92950, 0, 26920, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_AEAF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AEAF)
    OP_8E(0xFE, 0x16800, 0x0, 0x7D31, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_79_AE83 end

    def Function_80_AED7(): pass

    label("Function_80_AED7")

    Sleep(900)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 92950, 0, 26920, 0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_AF03():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AF03)
    OP_8E(0xFE, 0x16D00, 0x0, 0x7D31, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_80_AED7 end

    def Function_81_AF2B(): pass

    label("Function_81_AF2B")

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
        (0, "loc_AFA5"),
        (1, "loc_AFAB"),
        (SWITCH_DEFAULT, "loc_AFB1"),
    )


    label("loc_AFA5")

    OP_A2(0x1200)
    Jump("loc_AFB1")

    label("loc_AFAB")

    OP_A2(0x1201)
    Jump("loc_AFB1")

    label("loc_AFB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_AFBF")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_AFC3")

    label("loc_AFBF")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_AFC3")

    Return()

    # Function_81_AF2B end

    def Function_82_AFC4(): pass

    label("Function_82_AFC4")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #558
        (
            "\x07\x05　　走　\x01",
            "　　廊　\x01",
            "　　里　\x01",
            "　　请　\x01",
            "　　安　\x01",
            "　学静　\x01",
            "　生！　\x01",
            "　指　　\x01",
            "　导　　\x01",
            "　部　　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_82_AFC4 end

    def Function_83_B050(): pass

    label("Function_83_B050")

    SetPlaceName(0x6F)
    Return()

    # Function_83_B050 end

    def Function_84_B054(): pass

    label("Function_84_B054")

    SetPlaceName(0x5E)
    Return()

    # Function_84_B054 end

    def Function_85_B058(): pass

    label("Function_85_B058")

    SetPlaceName(0x6E)
    Return()

    # Function_85_B058 end

    def Function_86_B05C(): pass

    label("Function_86_B05C")

    SetPlaceName(0x74)
    Return()

    # Function_86_B05C end

    def Function_87_B060(): pass

    label("Function_87_B060")

    SetPlaceName(0x73)
    Return()

    # Function_87_B060 end

    SaveToFile()

Try(main)
