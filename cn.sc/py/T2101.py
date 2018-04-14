from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2101   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        '梅尔茨',                               # 9
        '哈尔德',                               # 10
        '昆茨',                                 # 11
        '布诺安',                               # 12
        '哈古',                                 # 13
        '布兰塔婆婆',                           # 14
        '贝尔夫',                               # 15
        '洛克',                                 # 16
        '波尔多斯',                             # 17
        '加布',                                 # 18
        '皮卡罗',                               # 19
        '汽油罐',                               # 20
        '汽油罐',                               # 21
        '汽油罐',                               # 22
        '市民',                                 # 23
        '市民',                                 # 24
        '市民',                                 # 25
        '市民',                                 # 26
        '市民',                                 # 27
        '市民',                                 # 28
        '市民',                                 # 29
        '市民',                                 # 30
        '市民',                                 # 31
        '市民',                                 # 32
        '市民',                                 # 33
        '中年男子',                             # 34
        '穆拉德老人',                           # 35
        '罗伊德',                               # 36
        '小船',                                 # 37
        '目标用照相机',                         # 38
        '阿伊纳街道方向',                       # 39
        '卢安市·北街区',                       # 40
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
        'ED6_DT07/CH01760 ._CH',             # 00
        'ED6_DT07/CH01120 ._CH',             # 01
        'ED6_DT07/CH01460 ._CH',             # 02
        'ED6_DT07/CH01500 ._CH',             # 03
        'ED6_DT07/CH01020 ._CH',             # 04
        'ED6_DT07/CH01110 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
        'ED6_DT07/CH00472 ._CH',             # 07
        'ED6_DT06/CH20020 ._CH',             # 08
        'ED6_DT07/CH01030 ._CH',             # 09
        'ED6_DT07/CH01080 ._CH',             # 0A
        'ED6_DT07/CH01050 ._CH',             # 0B
        'ED6_DT07/CH01070 ._CH',             # 0C
        'ED6_DT07/CH01100 ._CH',             # 0D
        'ED6_DT07/CH01680 ._CH',             # 0E
        'ED6_DT07/CH01140 ._CH',             # 0F
        'ED6_DT07/CH01150 ._CH',             # 10
        'ED6_DT07/CH01210 ._CH',             # 11
        'ED6_DT07/CH01190 ._CH',             # 12
        'ED6_DT07/CH01000 ._CH',             # 13
        'ED6_DT07/CH01390 ._CH',             # 14
        'ED6_DT07/CH02530 ._CH',             # 15
    )

    AddCharChipPat(
        'ED6_DT07/CH01760P._CP',             # 00
        'ED6_DT07/CH01120P._CP',             # 01
        'ED6_DT07/CH01460P._CP',             # 02
        'ED6_DT07/CH01500P._CP',             # 03
        'ED6_DT07/CH01020P._CP',             # 04
        'ED6_DT07/CH01110P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
        'ED6_DT07/CH00472P._CP',             # 07
        'ED6_DT06/CH20020P._CP',             # 08
        'ED6_DT07/CH01030P._CP',             # 09
        'ED6_DT07/CH01080P._CP',             # 0A
        'ED6_DT07/CH01050P._CP',             # 0B
        'ED6_DT07/CH01070P._CP',             # 0C
        'ED6_DT07/CH01100P._CP',             # 0D
        'ED6_DT07/CH01680P._CP',             # 0E
        'ED6_DT07/CH01140P._CP',             # 0F
        'ED6_DT07/CH01150P._CP',             # 10
        'ED6_DT07/CH01210P._CP',             # 11
        'ED6_DT07/CH01190P._CP',             # 12
        'ED6_DT07/CH01000P._CP',             # 13
        'ED6_DT07/CH01390P._CP',             # 14
        'ED6_DT07/CH02530P._CP',             # 15
    )

    DeclNpc(
        X                   = 31640,
        Z                   = 0,
        Y                   = 10890,
        Direction           = 180,
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
        X                   = 30790,
        Z                   = 0,
        Y                   = 9980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 54040,
        Z                   = 0,
        Y                   = 25560,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 19700,
        Z                   = 0,
        Y                   = 28620,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 35750,
        Z                   = 0,
        Y                   = 25180,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 75930,
        Z                   = 0,
        Y                   = 10740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 41000,
        Z                   = 1050,
        Y                   = 21010,
        Direction           = 180,
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
        X                   = 59750,
        Z                   = 0,
        Y                   = 6040,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 32140,
        Z                   = 0,
        Y                   = 6240,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 51030,
        Z                   = 0,
        Y                   = 25340,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 27010,
        Z                   = 0,
        Y                   = 11360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966088,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1966088,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1966088,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1E6,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xA0,
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
        X                   = 73210,
        Z                   = 0,
        Y                   = -16650,
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
        X                   = 50980,
        Z                   = 400,
        Y                   = 77990,
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
        X                   = 70000,
        Y                   = 0,
        Z                   = -2100,
        Range               = 76500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFFBB4,
        Unknown_18          = 0x0,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 17690,
        Y                   = 2000,
        Z                   = 7750,
        Range               = 16040,
        Unknown_10          = 0xFFFFF8F8,
        Unknown_14          = 0x1036,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 54040,
        Y                   = -1000,
        Z                   = 25560,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 35750,
        Y                   = -1000,
        Z                   = 25180,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = 26200,
        Y                   = -2000,
        Z                   = 14000,
        Range               = 31900,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x3E80,
        Unknown_18          = 0x0,
        Unknown_1C          = 28,
    )

    DeclEvent(
        X                   = 31200,
        Y                   = 0,
        Z                   = 25340,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 77280,
        Y                   = 0,
        Z                   = 22060,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 32,
    )


    DeclActor(
        TriggerX            = 50320,
        TriggerZ            = 1000,
        TriggerY            = 9400,
        TriggerRange        = 800,
        ActorX              = 50320,
        ActorZ              = 2000,
        ActorY              = 9400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 31960,
        TriggerZ            = 1000,
        TriggerY            = 3430,
        TriggerRange        = 800,
        ActorX              = 31960,
        ActorZ              = 2000,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 23540,
        TriggerZ            = 1000,
        TriggerY            = 3430,
        TriggerRange        = 800,
        ActorX              = 23540,
        ActorZ              = 2000,
        ActorY              = 3430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 77600,
        TriggerZ            = 0,
        TriggerY            = 12330,
        TriggerRange        = 800,
        ActorX              = 77900,
        ActorZ              = 1000,
        ActorY              = 12330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1270,
        TriggerZ            = 0,
        TriggerY            = 29530,
        TriggerRange        = 1000,
        ActorX              = -1300,
        ActorZ              = -2000,
        ActorY              = 34150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_6EE",          # 00, 0
        "Function_1_964",          # 01, 1
        "Function_2_A05",          # 02, 2
        "Function_3_B82",          # 03, 3
        "Function_4_BA2",          # 04, 4
        "Function_5_D45",          # 05, 5
        "Function_6_DE1",          # 06, 6
        "Function_7_EA0",          # 07, 7
        "Function_8_12CC",         # 08, 8
        "Function_9_17E1",         # 09, 9
        "Function_10_1CEA",        # 0A, 10
        "Function_11_210E",        # 0B, 11
        "Function_12_21ED",        # 0C, 12
        "Function_13_237B",        # 0D, 13
        "Function_14_2403",        # 0E, 14
        "Function_15_2476",        # 0F, 15
        "Function_16_2A4B",        # 10, 16
        "Function_17_2BF6",        # 11, 17
        "Function_18_2D63",        # 12, 18
        "Function_19_2DA9",        # 13, 19
        "Function_20_301F",        # 14, 20
        "Function_21_3C2E",        # 15, 21
        "Function_22_43D4",        # 16, 22
        "Function_23_539C",        # 17, 23
        "Function_24_5CC5",        # 18, 24
        "Function_25_5D5E",        # 19, 25
        "Function_26_5DB7",        # 1A, 26
        "Function_27_5DBE",        # 1B, 27
        "Function_28_5E38",        # 1C, 28
        "Function_29_66BC",        # 1D, 29
        "Function_30_6709",        # 1E, 30
        "Function_31_6812",        # 1F, 31
        "Function_32_6816",        # 20, 32
    )


    def Function_0_6EE(): pass

    label("Function_0_6EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B9")
    SetChrPos(0x16, 18790, -1800, 11600, 0)
    SetChrPos(0x17, 17990, -1800, 11600, 90)
    SetChrPos(0x18, 17220, -1800, 11420, 90)
    SetChrPos(0x19, 16490, -1800, 11290, 90)
    SetChrPos(0x1A, 15770, -1800, 11470, 90)
    SetChrPos(0x1B, 15050, -1800, 11610, 90)
    SetChrPos(0x1C, 14440, -1800, 10960, 45)
    SetChrPos(0x1D, 14560, -1800, 10210, 0)
    SetChrPos(0x1E, 14410, -1800, 9520, 0)
    SetChrPos(0x1F, 14460, -1800, 8730, 0)
    SetChrPos(0x20, 14350, -1800, 7960, 0)
    SetChrPos(0x21, 14470, -1800, 7260, 0)
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
    SetChrPos(0xA, 22700, -1800, 20620, 180)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x0, 0x2)
    SetChrPos(0xD, 40940, 1050, 21050, 200)
    SetChrPos(0x10, 24760, 0, 24750, 225)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_894")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 31330, 0, 20020, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x10)
    OP_43(0xF, 0x0, 0x0, 0x2)
    SetChrPos(0xF, 54610, 0, 24160, 270)
    SetChrChipByIndex(0xF, 21)

    label("loc_894")

    SetChrPos(0xC, 3800, -1800, 23920, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8B6")
    SetChrFlags(0xC, 0x10)

    label("loc_8B6")

    Jump("loc_950")

    label("loc_8B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_8E5")
    OP_43(0xF, 0x1, 0x0, 0x3)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E2")
    ClearChrFlags(0xA, 0x80)

    label("loc_8E2")

    Jump("loc_950")

    label("loc_8E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_91B")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xB, 17990, 0, 1680, 180)
    SetChrPos(0xA, 50910, 0, 23310, 288)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_950")

    label("loc_91B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_944")
    SetChrPos(0xB, 15930, -1800, 25220, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_950")

    label("loc_944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_950")
    ClearChrFlags(0xA, 0x80)

    label("loc_950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_963")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 21)

    label("loc_963")

    Return()

    # Function_0_6EE end

    def Function_1_964(): pass

    label("Function_1_964")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFE7960, 0x230048)
    OP_22(0x1C5, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_987")
    OP_64(0x4, 0x1)

    label("loc_987")

    OP_72(0x16, 0x10)
    OP_6F(0x16, 60)
    OP_72(0x12, 0x10)
    OP_72(0x14, 0x10)
    OP_72(0x15, 0x10)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FF")
    OP_6F(0x11, 1500)
    OP_72(0x21, 0x2)
    OP_71(0x22, 0x4)
    OP_64(0x3, 0x1)
    OP_71(0x23, 0x4)
    OP_71(0x24, 0x4)
    OP_71(0x25, 0x4)
    OP_71(0x26, 0x4)

    label("loc_9FF")

    OP_1C(0x13, 0x0, 0x1A)
    Return()

    # Function_1_964 end

    def Function_2_A05(): pass

    label("Function_2_A05")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2A")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_B6C")

    label("loc_A2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A43")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_B6C")

    label("loc_A43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_B6C")

    label("loc_A5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A75")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_B6C")

    label("loc_A75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8E")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_B6C")

    label("loc_A8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA7")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_B6C")

    label("loc_AA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC0")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_B6C")

    label("loc_AC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD9")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_B6C")

    label("loc_AD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF2")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_B6C")

    label("loc_AF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B0B")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_B6C")

    label("loc_B0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B24")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_B6C")

    label("loc_B24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3D")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_B6C")

    label("loc_B3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B56")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_B6C")

    label("loc_B56")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6C")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_B6C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B81")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_B6C")

    label("loc_B81")

    Return()

    # Function_2_A05 end

    def Function_3_B82(): pass

    label("Function_3_B82")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BA1")
    OP_99(0xFE, 0x1, 0x7, 0xBB8)
    SetChrSubChip(0xFE, 0)
    Sleep(250)
    Jump("Function_3_B82")

    label("loc_BA1")

    Return()

    # Function_3_B82 end

    def Function_4_BA2(): pass

    label("Function_4_BA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD4")

    label("loc_BAE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BD1")
    OP_8D(0xFE, 48840, 21930, 53280, 24890, 2000)
    Jump("loc_BAE")

    label("loc_BD1")

    Jump("loc_D44")

    label("loc_BD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BED")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_D2F")

    label("loc_BED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C06")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_D2F")

    label("loc_C06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_D2F")

    label("loc_C1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C38")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_D2F")

    label("loc_C38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C51")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_D2F")

    label("loc_C51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_D2F")

    label("loc_C6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C83")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_D2F")

    label("loc_C83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9C")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_D2F")

    label("loc_C9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB5")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_D2F")

    label("loc_CB5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CCE")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_D2F")

    label("loc_CCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE7")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_D2F")

    label("loc_CE7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D00")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_D2F")

    label("loc_D00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D19")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_D2F")

    label("loc_D19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D2F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_D2F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D44")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_D2F")

    label("loc_D44")

    Return()

    # Function_4_BA2 end

    def Function_5_D45(): pass

    label("Function_5_D45")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_DA0")

    ChrTalk(    #0
        0xFE,
        (
            "我们那些家伙一不看着\x01",
            "就会马上偷懒的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "所以要来定期巡视\x01",
            "给他们打气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_DB8")

    ChrTalk(    #2
        0xFE,
        "哼！哼！\x02",
    )

    CloseMessageWindow()
    Jump("loc_DDD")

    label("loc_DB8")

    OP_A2(0x7)

    ChrTalk(    #3
        0xFE,
        "哼！哼！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "还没完呢……！\x02",
    )

    CloseMessageWindow()

    label("loc_DDD")

    TalkEnd(0xFE)
    Return()

    # Function_5_D45 end

    def Function_6_DE1(): pass

    label("Function_6_DE1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_E40")

    ChrTalk(    #5
        0xFE,
        (
            "这种时候，迫不得已\x01",
            "也得出来自己打工了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "只是，在父亲的事务所\x01",
            "工作啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E9C")

    label("loc_E40")

    OP_A2(0x6)

    ChrTalk(    #7
        0xFE,
        (
            "去北街区\x01",
            "找过工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "不过世间还真是残酷啊。\x01",
            "工作只有选举运动\x01",
            "的兼职什么的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9C")

    TalkEnd(0xFE)
    Return()

    # Function_6_DE1 end

    def Function_7_EA0(): pass

    label("Function_7_EA0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_F4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0D")

    ChrTalk(    #9
        0xFE,
        (
            "渡口比以前\x01",
            "更混乱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "以前每家都\x01",
            "有自己的小船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "不用人人\x01",
            "都去坐渡船。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_F49")

    label("loc_F0D")


    ChrTalk(    #12
        0xFE,
        (
            "渡口比以前\x01",
            "更混乱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "真是的，\x01",
            "站在那里都够累了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F49")

    Jump("loc_12C8")

    label("loc_F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1034")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD7")

    ChrTalk(    #14
        0xFE,
        (
            "桥竟然不能动了，\x01",
            "好像返回到从前一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "虽然渡口有免费的船，\x01",
            "但真是不方便啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "太习惯方便的生活了吗。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1031")

    label("loc_FD7")


    ChrTalk(    #17
        0xFE,
        (
            "桥竟然不能动了，\x01",
            "好像返回到从前一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "虽然渡口有免费的船，\x01",
            "但真是不方便啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1031")

    Jump("loc_12C8")

    label("loc_1034")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1134")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_10A1")

    ChrTalk(    #19
        0xFE,
        (
            "从前这一片也是很有活力的。\x01",
            "到处都有摊子和市场呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "那样的光景\x01",
            "现在已经看不到了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1131")

    label("loc_10A1")

    OP_A2(0x5)

    ChrTalk(    #21
        0xFE,
        (
            "从前这一片也是很有活力的。\x01",
            "到处都有摊子和市场呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "这次的选举，港口的年轻人\x01",
            "似乎也都很努力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "那样的光景\x01",
            "现在已经看不到了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1131")

    Jump("loc_12C8")

    label("loc_1134")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_11E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_116A")

    ChrTalk(    #24
        0xFE,
        (
            "年轻人就是要有\x01",
            "那种精神才好啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11DE")

    label("loc_116A")

    OP_A2(0x5)

    ChrTalk(    #25
        0xFE,
        (
            "呀，刚才的骚动\x01",
            "我看到了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "船员们聚在一起\x01",
            "那样的争吵是经常的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "年轻人就是要有\x01",
            "那种精神才好啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11DE")

    Jump("loc_12C8")

    label("loc_11E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1239")

    ChrTalk(    #28
        0xFE,
        (
            "名门戴尔蒙家\x01",
            "也没落了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "所谓时代的转折，\x01",
            "大概就是这种事吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12C8")

    label("loc_1239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 6)), scpexpr(EXPR_END)), "loc_1281")

    ChrTalk(    #30
        0xFE,
        (
            "诺曼的家…\x01",
            "看，就在那里了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 135, 400)

    ChrTalk(    #31
        0xFE,
        "那边的宅子就是。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12C8")

    label("loc_1281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_12C8")

    ChrTalk(    #32
        0xFE,
        (
            "唔，每张都\x01",
            "照得很有风度嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "拍照的人\x01",
            "技术一定很好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12C8")

    TalkEnd(0xFE)
    Return()

    # Function_7_EA0 end

    def Function_8_12CC(): pass

    label("Function_8_12CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12E2")
    Call(0, 20)
    Jump("loc_17DD")

    label("loc_12E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_13FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1343")

    ChrTalk(    #34
        0xFE,
        (
            "还要汽油的话\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "那个油可燃性很强，\x01",
            "不能用在油灯里呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13FC")

    label("loc_1343")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B4")

    ChrTalk(    #36
        0xFE,
        (
            "不过，要是船不来\x01",
            "还真是不妙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "仓库里的物资\x01",
            "很有限……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "……真、真不想\x01",
            "考虑未来啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_13FC")

    label("loc_13B4")


    ChrTalk(    #39
        0xFE,
        (
            "船不来的话\x01",
            "还真是不妙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "……不过，未来的事\x01",
            "还是别去多想吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FC")

    Jump("loc_17DD")

    label("loc_13FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_152A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1460")

    ChrTalk(    #41
        0xFE,
        (
            "还要汽油的话\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "那个油可燃性很强，\x01",
            "不能用在油灯里呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1527")

    label("loc_1460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14DB")

    ChrTalk(    #43
        0xFE,
        (
            "呼～好久没有这样\x01",
            "活动身体了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "搬运那么多货物\x01",
            "真的很辛苦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "唉，起重机不能动啊。\x01",
            "没办法了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1527")

    label("loc_14DB")


    ChrTalk(    #46
        0xFE,
        (
            "１００％人力作业\x01",
            "真是好久没经历过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "唉，平时都是\x01",
            "用起重机的了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1527")

    Jump("loc_17DD")

    label("loc_152A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1616")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1599")

    ChrTalk(    #48
        0xFE,
        (
            "啊～我支持波尔多斯～\x01",
            "请多关照市长候选人波尔多斯～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "开创港口未来！\x01",
            "请多支持波尔多斯～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1613")

    label("loc_1599")

    OP_A2(0x4)

    ChrTalk(    #50
        0xFE,
        (
            "波尔多斯主任是长年\x01",
            "处理港口事物的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "如果他当了市长\x01",
            "应该会重振港口吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "呼，喘口气了，\x01",
            "那么继续喊吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1613")

    Jump("loc_17DD")

    label("loc_1616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_16A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_165A")

    ChrTalk(    #53
        0xFE,
        (
            "应该从更远处\x01",
            "眺望才对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "寿命都缩短了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16A4")

    label("loc_165A")

    OP_A2(0x4)

    ChrTalk(    #55
        0xFE,
        (
            "跑去围观看吵架，\x01",
            "差点被卷进去真把我急坏了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "呼～吓了一大跳。\x02",
    )

    CloseMessageWindow()

    label("loc_16A4")

    Jump("loc_17DD")

    label("loc_16A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1754")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1700")

    ChrTalk(    #57
        0xFE,
        (
            "太偷懒的话\x01",
            "布诺安会生气的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "那家伙要是发起怒来\x01",
            "可恐怖了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1751")

    label("loc_1700")

    OP_A2(0x4)

    ChrTalk(    #59
        0xFE,
        (
            "好，差不多\x01",
            "是下一班船来的时间了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "工作忙里偷闲，\x01",
            "选举运动可真辛苦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1751")

    Jump("loc_17DD")

    label("loc_1754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_17DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_17A3")
    OP_A3(0x4)

    ChrTalk(    #61
        0xFE,
        (
            "啊～支持波尔多斯～\x01",
            "请多支持～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "请多支持波尔多斯～\x02",
    )

    CloseMessageWindow()
    Jump("loc_17DD")

    label("loc_17A3")

    OP_A2(0x4)

    ChrTalk(    #63
        0xFE,
        "嗯～这里人不多啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "现在可能去桥对面\x01",
            "比较好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17DD")

    TalkEnd(0xFE)
    Return()

    # Function_8_12CC end

    def Function_9_17E1(): pass

    label("Function_9_17E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_183A")

    ChrTalk(    #65
        0xFE,
        (
            "渡鸦帮的小子们\x01",
            "好像也开始什么活动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "因为事态紧急\x01",
            "终于醒悟了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE6")

    label("loc_183A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1977")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_18B1")

    ChrTalk(    #67
        0xFE,
        (
            "新市长那家伙\x01",
            "这么快就露出马脚了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "结果，那家伙只会嘴上逞能，\x01",
            "没有了主任就什么也做不了了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1974")

    label("loc_18B1")


    ChrTalk(    #69
        0xFE,
        (
            "由于主任的指示，不管怎样\x01",
            "至少生活物资都进仓库了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "要是燃料和食品都用光了\x01",
            "就真的完蛋了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "话说回来新市长那家伙\x01",
            "到底在哪里干什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "在港口前线指挥全部工作的\x01",
            "都是波尔多斯主任！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1974")

    Jump("loc_1CE6")

    label("loc_1977")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1B63")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1A79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_19E9")

    ChrTalk(    #73
        0xFE,
        (
            "昆茨好像为骚动的事\x01",
            "去道歉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "虽然他也参加了煽动，\x01",
            "其实是彼此彼此吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A76")

    label("loc_19E9")

    OP_A2(0x3)

    ChrTalk(    #75
        0xFE,
        (
            "昆茨好像为骚动的事\x01",
            "去道歉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "虽然他也参加了煽动，\x01",
            "其实是彼此彼此吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "不过，让我们这边的人\x01",
            "先去道歉的\x01",
            "好像是波尔多斯主任。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A76")

    Jump("loc_1B60")

    label("loc_1A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1AD3")

    ChrTalk(    #78
        0xFE,
        (
            "昆茨好像为骚动的事\x01",
            "去道歉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "虽然他也参加了煽动，\x01",
            "其实是彼此彼此吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B60")

    label("loc_1AD3")

    OP_A2(0x3)

    ChrTalk(    #80
        0xFE,
        (
            "昆茨好像为骚动的事\x01",
            "去道歉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "虽然他也参加了煽动，\x01",
            "其实是彼此彼此吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "不过，让我们这边的人\x01",
            "先去道歉的\x01",
            "好像是波尔多斯主任。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B60")

    Jump("loc_1CE6")

    label("loc_1B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1BC4")

    ChrTalk(    #83
        0xFE,
        (
            "为什么幽灵的事\x01",
            "会变成我们的错？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "这种傻事也别一直做嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "哼，真是火大……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CE6")

    label("loc_1BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1C25")

    ChrTalk(    #86
        0xFE,
        (
            "我也希望波尔多斯主任\x01",
            "能当上市长啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "因为没有比他\x01",
            "更有声望的人啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C96")

    label("loc_1C25")

    OP_A2(0x3)

    ChrTalk(    #88
        0xFE,
        (
            "帮忙选举没有错。\x01",
            "不过也要专心点做事啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "说到底在这种地方\x01",
            "大声喊叫有意义吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        "只有海鸥听得到啦。\x02",
    )

    CloseMessageWindow()

    label("loc_1C96")

    Jump("loc_1CE6")

    label("loc_1C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1CE6")

    ChrTalk(    #91
        0xFE,
        (
            "波尔多斯主任\x01",
            "正忙于选举活动呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "现在由我代理\x01",
            "掌管港口现场。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE6")

    TalkEnd(0xFE)
    Return()

    # Function_9_17E1 end

    def Function_10_1CEA(): pass

    label("Function_10_1CEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1DD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D7F")

    ChrTalk(    #93
        0xFE,
        (
            "主任好像打算和诺曼市长\x01",
            "同心协力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "不愧是波尔多斯主任。\x01",
            "器量真大啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "输掉了市长选举，\x01",
            "回想起来还是遗憾啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1DD5")

    label("loc_1D7F")


    ChrTalk(    #96
        0xFE,
        (
            "主任好像打算和诺曼市长\x01",
            "同心协力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "嗯，现在是紧急时刻\x01",
            "不团结一致是不行的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD5")

    Jump("loc_210A")

    label("loc_1DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1E34")

    ChrTalk(    #98
        0xFE,
        (
            "起重机不能启动，\x01",
            "现在只能靠腕力了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "新市长那家伙也出来\x01",
            "帮忙搬运货物了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210A")

    label("loc_1E34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1EE6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1E9A")

    ChrTalk(    #100
        0xFE,
        (
            "不过，差不多\x01",
            "两阵营也该和好了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "这样下去，搞不好\x01",
            "又会发生什么事件的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EE3")

    label("loc_1E9A")

    OP_A2(0x2)

    ChrTalk(    #102
        0xFE,
        (
            "喔，是各位游击士啊。\x01",
            "刚才帮我大忙了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "差点被\x01",
            "当作犯人了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE3")

    Jump("loc_210A")

    label("loc_1EE6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1F41")

    ChrTalk(    #104
        0xFE,
        (
            "喔，是各位游击士啊。\x01",
            "在酒店辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "呼，不管怎么说，\x01",
            "真相大白就好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210A")

    label("loc_1F41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2058")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1FA8")

    ChrTalk(    #106
        0xFE,
        (
            "说起来那些家伙，\x01",
            "连幽灵都要怪到我们头上啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "啊～回想起来\x01",
            "又开始焦躁不安了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2055")

    label("loc_1FA8")

    OP_A2(0x2)

    ChrTalk(    #108
        0xFE,
        (
            "波尔多斯主任叫我来\x01",
            "向诺曼先生道歉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "明明是对方找的麻烦,\x01",
            "为什么要我去谢罪呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "唉，虽然我说过那些贬低他儿子的话，\x01",
            "确实做的不对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "但还是～无法接受啊。\x02",
    )

    CloseMessageWindow()

    label("loc_2055")

    Jump("loc_210A")

    label("loc_2058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2098")

    ChrTalk(    #112
        0xFE,
        (
            "海的男人，波尔多斯～！\x01",
            "市长选举请投波尔多斯1票！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_210A")

    label("loc_2098")

    OP_A2(0x2)

    ChrTalk(    #113
        0xFE,
        (
            "海的男人，波尔多斯～！\x01",
            "市长选举请投波尔多斯1票！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "波尔多斯将保护你的港口！\x01",
            "海的男人波尔多斯请多关照！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210A")

    TalkEnd(0xFE)
    Return()

    # Function_10_1CEA end

    def Function_11_210E(): pass

    label("Function_11_210E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_21E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_217F")

    ChrTalk(    #115
        0x9,
        "这就是有问题的仓库区吗～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x9,
        (
            "如果要作为旅游地来发展，\x01",
            "这里可得想办法处理一下啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21E9")

    label("loc_217F")

    OP_A2(0x1)

    ChrTalk(    #117
        0x9,
        (
            "这就是有问题的仓库区吗～？\x01",
            "好像有不良少年出没呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x9,
        (
            "听说很危险\x01",
            "还找了保镖，\x01",
            "是不是有点夸张了？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E9")

    TalkEnd(0xFE)
    Return()

    # Function_11_210E end

    def Function_12_21ED(): pass

    label("Function_12_21ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_22C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2267")

    ChrTalk(    #119
        0xFE,
        "好啊，辛苦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "刚才去了市长官邸\x01",
            "报告了学院的事件！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "返回协会之前\x01",
            "在这里休息一下呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_22BD")

    label("loc_2267")


    ChrTalk(    #122
        0xFE,
        (
            "刚才去了市长官邸\x01",
            "报告了学院的事件！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "据说平安解决了，\x01",
            "不愧是艾丝蒂尔你们啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22BD")

    Jump("loc_2377")

    label("loc_22C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_22CA")
    Jump("loc_2377")

    label("loc_22CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2377")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_233D")

    ChrTalk(    #124
        0xFE,
        (
            "没想到要在城里\x01",
            "当保镖啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "卢安的治安好像变得很差，\x01",
            "身为地区所属的游击士真该负责啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2377")

    label("loc_233D")

    OP_A2(0x0)

    ChrTalk(    #126
        0xFE,
        "啊，辛苦了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "我正在给\x01",
            "来视察的商人当保镖呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2377")

    TalkEnd(0xFE)
    Return()

    # Function_12_21ED end

    def Function_13_237B(): pass

    label("Function_13_237B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2386")
    Return()

    label("loc_2386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_23A5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23A1")
    Jump("loc_23A2")

    label("loc_23A1")

    Return()

    label("loc_23A2")

    Jump("loc_23C6")

    label("loc_23A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_23B0")
    Return()

    label("loc_23B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_23BF")
    Return()

    label("loc_23BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_23C6")

    label("loc_23C6")

    OP_4A(0xA, 0)

    ChrTalk(    #128 op#A
        0xA,
        (
            "#4A市长候选人波尔多斯！\x01",
            "请多支持波尔多斯！\x02",
        )
    )

    Sleep(2000)
    OP_4B(0xA, 0)
    Return()

    # Function_13_237B end

    def Function_14_2403(): pass

    label("Function_14_2403")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_240E")
    Return()

    label("loc_240E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2418")
    Jump("loc_2441")

    label("loc_2418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2423")
    Return()

    label("loc_2423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2431")
    Jump("loc_2441")

    label("loc_2431")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2441")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2441")
    Return()

    label("loc_2441")

    OP_4A(0xC, 0)

    ChrTalk(    #129 op#A
        0xC,
        (
            "#4A啊～我支持波尔多斯～\x01",
            "请多支持～\x02",
        )
    )

    Sleep(2000)
    OP_4B(0xC, 0)
    Return()

    # Function_14_2403 end

    def Function_15_2476(): pass

    label("Function_15_2476")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24C9")

    ChrTalk(    #130
        0xFE,
        (
            "呀，要找的东西\x01",
            "好像找到了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "看起来挺急的，\x01",
            "要当心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A47")

    label("loc_24C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_27D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2793")
    OP_8C(0xFE, 225, 0)
    OP_4A(0xFE, 255)
    EventBegin(0x0)
    Fade(500)
    OP_6D(25350, 0, 25220, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 26090, 0, 25080, 270)
    SetChrPos(0x102, 26250, 0, 24080, 270)
    SetChrPos(0xF8, 27170, 0, 24990, 270)
    SetChrPos(0xF9, 27360, 0, 23940, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #132
        0x101,
        "#1025F#4P那个～打扰一下。\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)

    ChrTalk(    #133
        0xFE,
        "#5P有什么事吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x102,
        (
            "#1040F#6P是的。\x01",
            "能占用您一点时间吗。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #135
        (
            "\x07\x05艾丝蒂尔等人说明了情况，\x01",
            "并向波尔多斯出示了工房长的介绍信。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #136
        0xFE,
        (
            "#5P呼，我的确是\x01",
            "港湾区的负责人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "#5P不过关于这件事\x01",
            "最好去问问哈古。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#1015F#4P哈古先生？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "#5P啊啊，在我们港口\x01",
            "负责货物销售的人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        "#5P应该在这个堤防深处。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        "#1006F#4P明白，那里的哈古先生对吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        (
            "#1040F#6P马上去找他谈谈。\x02\x03",

            "感谢您的帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "#5P啊啊，当心哦。\x01",
            "可别太慌张掉进海里了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20D5)
    EventEnd(0x0)
    Jump("loc_27CF")

    label("loc_2793")


    ChrTalk(    #144
        0xFE,
        (
            "找东西的事\x01",
            "问问哈古就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "应该在这个堤防\x01",
            "的深处。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27CF")

    Jump("loc_2A47")

    label("loc_27D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_28F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A3")

    ChrTalk(    #146
        0xFE,
        (
            "我和新市长诺曼\x01",
            "保持着良好的关系呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "虽说是市长选举中的对手，\x01",
            "但热爱故乡的心情是一样的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "如果互相配合，\x01",
            "一定能开拓港湾的未来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "当然，目前这个状况\x01",
            "是得想个办法才行呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_28F3")

    label("loc_28A3")


    ChrTalk(    #150
        0xFE,
        (
            "我和新市长诺曼\x01",
            "保持着良好的关系呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "想渡过这个难关\x01",
            "合作比什么都重要。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F3")

    Jump("loc_2A47")

    label("loc_28F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2A47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29F1")

    ChrTalk(    #152
        0xFE,
        (
            "和诺曼市长也谈过了，\x01",
            "总之先把生活物资\x01",
            "聚集到仓库里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "这样的话目前市民的生活\x01",
            "应该能支撑一阵。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "大家对新市长的能力\x01",
            "也相当怀疑……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "但想守护卢安的心情\x01",
            "我和市长都是一样的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "今后也要齐心合力\x01",
            "支撑市民的生活。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_2A47")

    label("loc_29F1")


    ChrTalk(    #157
        0xFE,
        (
            "总之先把生活物资\x01",
            "聚集到仓库里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "这样的话目前市民的生活\x01",
            "应该能支撑一阵。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A47")

    TalkEnd(0xFE)
    Return()

    # Function_15_2476 end

    def Function_16_2A4B(): pass

    label("Function_16_2A4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2B0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ACE")

    ChrTalk(    #159
        0xFE,
        (
            "反正没人在，\x01",
            "正想稍微偷懒一下……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "正好洛克大哥\x01",
            "过来巡视了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "最近大哥真是的，\x01",
            "总紧张兮兮的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_2B09")

    label("loc_2ACE")


    ChrTalk(    #162
        0xFE,
        (
            "真是的，洛克大哥\x01",
            "到底怎么了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "最近紧张兮兮的。\x02",
    )

    CloseMessageWindow()

    label("loc_2B09")

    Jump("loc_2BF2")

    label("loc_2B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2BF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B9E")

    ChrTalk(    #164
        0xFE,
        (
            "桥吊着不能动，\x01",
            "这里无法通行哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "仓库街有渡船出航，\x01",
            "要去北区的话就乘那个吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "附近应该有我们的成员\x01",
            "为你引导的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_2BF2")

    label("loc_2B9E")


    ChrTalk(    #167
        0xFE,
        (
            "想去北区的时候\x01",
            "就使用仓库街的渡口吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "向导的标志\x01",
            "就是这个红色印花大手帕！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BF2")

    TalkEnd(0xFE)
    Return()

    # Function_16_2A4B end

    def Function_17_2BF6(): pass

    label("Function_17_2BF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2CD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C85")

    ChrTalk(    #169
        0xFE,
        (
            "总觉得最近，\x01",
            "城里的人们都好和善。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "刚才又有不认识的女孩子\x01",
            "对我说谢谢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xFE,
        (
            "果然是女神大人\x01",
            "在哪保佑我们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_2CD1")

    label("loc_2C85")


    ChrTalk(    #172
        0xFE,
        (
            "总觉得最近，\x01",
            "城里的人们都好和善。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "果然是女神大人\x01",
            "在哪保佑我们吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD1")

    Jump("loc_2D5F")

    label("loc_2CD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D23")

    ChrTalk(    #174
        0xFE,
        (
            "去北区的小船\x01",
            "在这边出发～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "请按顺序排队\x01",
            "等候～～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_2D5F")

    label("loc_2D23")


    ChrTalk(    #176
        0xFE,
        (
            "去北区的小船\x01",
            "在这边出发～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "市长请客\x01",
            "不用就亏了哦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5F")

    TalkEnd(0xFE)
    Return()

    # Function_17_2BF6 end

    def Function_18_2D63(): pass

    label("Function_18_2D63")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #178
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_2D63 end

    def Function_19_2DA9(): pass

    label("Function_19_2DA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_301E")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x241, 6)), scpexpr(EXPR_END)), "loc_2EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2E50")
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #179
        0x106,
        (
            "#050F还没找贝尔夫那家伙\x01",
            "问亡灵的事呢。\x02\x03",

            "要出城的话先去问问再说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #180
        0x101,
        (
            "#1007F啊，是喔。\x02\x03",

            "#1006F是市长官邸右边的房子吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EDE")

    label("loc_2E50")

    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #181
        0x103,
        (
            "#020F还没找叫贝尔夫的孩子\x01",
            "问白影的事呢。\x02\x03",

            "要出城的话先去问问再说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #182
        0x101,
        (
            "#1007F啊，是喔。\x02\x03",

            "#1006F是市长官邸右边的房子吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EDE")

    Jump("loc_3003")

    label("loc_2EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2F77")
    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #183
        0x106,
        (
            "#050F还没找渡鸦帮那些小子\x01",
            "问亡灵的事呢。\x02\x03",

            "要出城的话先去问问再说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #184
        0x101,
        (
            "#1007F啊，是喔。\x02\x03",

            "#1006F要先去港口的仓库才是。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3003")

    label("loc_2F77")

    TurnDirection(0xF7, 0x101, 400)

    ChrTalk(    #185
        0x103,
        (
            "#020F还没找渡鸦帮的小子们\x01",
            "问白影的事呢。\x02\x03",

            "要出城的话先去问问再说吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #186
        0x101,
        (
            "#1007F啊，是喔。\x02\x03",

            "#1006F要先去港口的仓库才是。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3003")

    OP_90(0x0, 0x0, 0x0, 0x7D0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_301E")

    Return()

    # Function_19_2DA9 end

    def Function_20_301F(): pass

    label("Function_20_301F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3044")
    Call(0, 24)
    Call(0, 25)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_3044")

    Fade(1000)
    OP_6D(4330, -1800, 24700, 0)
    OP_67(0, 6230, -10000, 0)
    OP_6B(3170, 0)
    OP_6C(315000, 0)
    OP_6E(282, 0)
    SetChrPos(0x101, 5170, -1800, 23340, 270)
    SetChrPos(0x102, 5260, -1800, 24300, 270)
    SetChrPos(0xF8, 6400, -1800, 22950, 270)
    SetChrPos(0xF9, 6380, -1800, 24230, 270)
    OP_4A(0xC, 255)
    OP_0D()

    ChrTalk(    #187
        0x101,
        "#1011F#6P那个～打扰一下？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)

    ChrTalk(    #188
        0xC,
        "#5P嗯，什么事？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #189
        (
            "\x07\x05艾丝蒂尔等人说明了情况，\x01",
            "并向哈古出示了工房长的介绍信。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #190
        0xC,
        (
            "#5P汽油啊……\x01",
            "啊啊，确实送来了。\x02\x03",

            "打算送去蔡斯之前\x01",
            "发生了这状况，\x01",
            "就一直保管在仓库了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        "#1006F#6P太好了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x102,
        (
            "#1040F#4P能马上\x01",
            "交给我们吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xC,
        (
            "#5P可以倒是可以……\x01",
            "不过量很多哟？\x02\x03",

            "全部搬出来\x01",
            "应该是不可能的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3290")

    ChrTalk(    #194
        0x103,
        (
            "#026F#6P是啊……\x02\x03",

            "#020F总之先拿我们\x01",
            "拿得动的份量好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_332D")

    label("loc_3290")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32E1")

    ChrTalk(    #195
        0x106,
        (
            "#053F#6P是啊……\x02\x03",

            "#051F嗯，总之先拿我们\x01",
            "拿得动的份量好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_332D")

    label("loc_32E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_332D")

    ChrTalk(    #196
        0x108,
        (
            "#074F#6P是啊……\x02\x03",

            "#070F总之先拿我们\x01",
            "拿得动的份量就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_332D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    OP_6F(0x15, 60)
    SetChrPos(0x13, 24000, 1000, 4010, 315)
    SetChrPos(0x14, 23300, 1000, 4010, 315)
    SetChrPos(0x15, 22600, 1000, 4010, 315)
    OP_A1(0x13, 0x27)
    OP_72(0x27, 0x4)
    OP_A1(0x14, 0x28)
    OP_72(0x28, 0x4)
    OP_A1(0x15, 0x29)
    OP_72(0x29, 0x4)
    OP_6D(24300, 500, 4860, 0)
    OP_67(0, 4760, -10000, 0)
    OP_6B(3720, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 23900, 0, 6280, 180)
    SetChrPos(0x102, 22750, 0, 6280, 180)
    SetChrPos(0xF8, 22200, 0, 7500, 180)
    SetChrPos(0xF9, 23870, 0, 7500, 180)
    SetChrPos(0xC, 23300, 250, 4960, 180)
    FadeToBright(1000, 0)
    OP_0D()
    OP_8C(0xC, 0, 400)

    ChrTalk(    #197
        0xC,
        (
            "#2P嗯……\x01",
            "就先这些吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34A4")

    ChrTalk(    #198
        0x107,
        (
            "#560F#6P嗯，有这些\x01",
            "应该能维持一阵了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34D2")

    label("loc_34A4")


    ChrTalk(    #199
        0x102,
        (
            "#1040F#6P嗯嗯，有这些\x01",
            "应该能维持一阵了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3505")

    ChrTalk(    #200
        0x108,
        "#071F#6P嗯，这点很轻松的吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_356C")

    label("loc_3505")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3539")

    ChrTalk(    #201
        0x106,
        (
            "#051F#6P这点的话\x01",
            "应该能搬动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_356C")

    label("loc_3539")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_356C")

    ChrTalk(    #202
        0x103,
        (
            "#524F#6P呼……\x01",
            "好像肌肉要痛了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_356C")

    Sleep(200)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #203
        "\x07\x00得到３个\x1F\x0C\x04\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x40C, 3)
    OP_71(0x27, 0x4)
    OP_71(0x28, 0x4)
    OP_71(0x29, 0x4)
    Sleep(500)
    OP_6F(0x15, 0)
    OP_70(0x15, 0x0)
    OP_73(0x15)
    SetChrPos(0xC, 23290, 1000, 3980, 180)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xC, 0, 400)

    ChrTalk(    #204
        0xC,
        (
            "#2P好了……\x01",
            "如果还需要\x01",
            "随时都可以来找我。\x02\x03",

            "不过，在此之前没有比\x01",
            "渡过现在这难关更重要的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        "#1007F#6P嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x102,
        "#1040F#6P给您添麻烦了。\x02",
    )

    CloseMessageWindow()

    def lambda_36A3():

        label("loc_36A3")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_36A3")

    QueueWorkItem2(0x101, 1, lambda_36A3)

    def lambda_36B4():

        label("loc_36B4")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_36B4")

    QueueWorkItem2(0x102, 1, lambda_36B4)

    def lambda_36C5():

        label("loc_36C5")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_36C5")

    QueueWorkItem2(0xF8, 1, lambda_36C5)

    def lambda_36D6():

        label("loc_36D6")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_36D6")

    QueueWorkItem2(0xF9, 1, lambda_36D6)

    def lambda_36E7():
        OP_6D(26650, 0, 7870, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36E7)
    OP_8E(0xC, 0x6F54, 0x0, 0x1ED2, 0xBB8, 0x0)
    OP_8E(0xC, 0x6F54, 0x14A, 0x43DA, 0xBB8, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_6D(24210, 0, 5890, 1500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38A3")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇得到了内燃机】\x01",                              # 0
            "【◇没有内燃机但请雾香询问了要塞】\x01",              # 1
            "【◇没有内燃机但向塞缪尔询问过内燃机的事】\x01",      # 2
            "【◇没有内燃机也没有询问要塞但问过维修长】\x01",      # 3
            "【◇没有内燃机没有询问要塞也没问过维修长】\x01",      # 4
            "【◇不变更】\x01",                                    # 5
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3861"),
        (1, "loc_3867"),
        (2, "loc_3876"),
        (3, "loc_3885"),
        (4, "loc_3894"),
        (SWITCH_DEFAULT, "loc_38A3"),
    )


    label("loc_3861")

    OP_A2(0x200F)
    Jump("loc_38A3")

    label("loc_3867")

    OP_A3(0x200F)
    OP_A2(0x200B)
    OP_A2(0x200C)
    OP_A3(0x200E)
    Jump("loc_38A3")

    label("loc_3876")

    OP_A3(0x200F)
    OP_A2(0x200B)
    OP_A3(0x200C)
    OP_A2(0x200E)
    Jump("loc_38A3")

    label("loc_3885")

    OP_A3(0x200F)
    OP_A2(0x200B)
    OP_A3(0x200C)
    OP_A3(0x200E)
    Jump("loc_38A3")

    label("loc_3894")

    OP_A3(0x200F)
    OP_A3(0x200B)
    OP_A3(0x200C)
    OP_A3(0x200E)
    Jump("loc_38A3")

    label("loc_38A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_END)), "loc_3A3E")
    OP_28(0xC2, 0x1, 0x1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_397A")

    def lambda_38C4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_38C4)
    Sleep(100)

    def lambda_38D7():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_38D7)
    Sleep(100)

    def lambda_38EA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_38EA)
    Sleep(100)
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #207
        0x101,
        (
            "#1006F#5P好了……\x01",
            "这样材料就齐了。\x02\x03",

            "赶快返回亚尔摩\x01",
            "开始改造水泵装置吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #208
        0x107,
        (
            "#061F#6P嗯，我\x01",
            "随时准备ＯＫ的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A3B")

    label("loc_397A")


    def lambda_3980():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3980)
    Sleep(100)

    def lambda_3993():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3993)
    Sleep(100)

    def lambda_39A6():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_39A6)
    Sleep(100)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #209
        0x101,
        (
            "#1006F#5P好了……\x01",
            "这样材料就齐了。\x02\x03",

            "#1015F必须要有提妲\x01",
            "才能改造水泵装置吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x102,
        (
            "#1040F#4P是呢。\x02\x03",

            "先返回协会\x01",
            "和提妲会合吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A3B")

    Jump("loc_3C05")

    label("loc_3A3E")


    def lambda_3A44():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3A44)
    Sleep(100)

    def lambda_3A57():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3A57)
    Sleep(100)

    def lambda_3A6A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3A6A)
    Sleep(100)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #211
        0x101,
        (
            "#1006F#5P好了……\x01",
            "这样汽油就ＯＫ了。\x02\x03",

            "#1015F接着是内燃机……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B38")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #212
        0x102,
        (
            "#1040F#4P似乎着陆在托兰特平原的\x01",
            "警备艇在运送那机械。\x02\x03",

            "去那边看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x101,
        "#1006F#5P嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C05")

    label("loc_3B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_END)), "loc_3BA8")

    ChrTalk(    #214
        0x102,
        (
            "#1035F#4P好像又被王国军\x01",
            "借去了。\x02\x03",

            "#1040F只好去雷斯顿要塞\x01",
            "问问看了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        "#1006F#5P是吗，明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C05")

    label("loc_3BA8")


    ChrTalk(    #216
        0x102,
        (
            "#1040F#4P记得保管人\x01",
            "是格斯塔夫维修长吧。\x02\x03",

            "去蔡斯飞船坪看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x101,
        "#1006F#5P嗯，明白。\x02",
    )

    CloseMessageWindow()

    label("loc_3C05")

    OP_A2(0x2011)
    OP_A2(0xB)
    OP_28(0xC2, 0x1, 0x800)
    SetChrPos(0xC, 3800, -1800, 23920, 270)
    ClearChrFlags(0xC, 0x10)
    OP_4B(0xC, 255)
    EventEnd(0x0)
    Return()

    # Function_20_301F end

    def Function_21_3C2E(): pass

    label("Function_21_3C2E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C45")
    Call(0, 24)
    Call(0, 25)

    label("loc_3C45")

    OP_D2(0x270003, 0x270007, 0x16)
    OP_D2(0x270013, 0x270017, 0x17)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_3C72"),
        (5, "loc_3C7F"),
        (6, "loc_3C8C"),
        (7, "loc_3C99"),
        (SWITCH_DEFAULT, "loc_3CA6"),
    )


    label("loc_3C72")

    OP_D2(0x70023, 0x7002B, 0x18)
    Jump("loc_3CA6")

    label("loc_3C7F")

    OP_D2(0x70053, 0x7005B, 0x18)
    Jump("loc_3CA6")

    label("loc_3C8C")

    OP_D2(0x70063, 0x7006B, 0x18)
    Jump("loc_3CA6")

    label("loc_3C99")

    OP_D2(0x70073, 0x7007B, 0x18)
    Jump("loc_3CA6")

    label("loc_3CA6")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_3CBF"),
        (5, "loc_3CCC"),
        (6, "loc_3CD9"),
        (7, "loc_3CE6"),
        (SWITCH_DEFAULT, "loc_3CF3"),
    )


    label("loc_3CBF")

    OP_D2(0x70023, 0x7002B, 0x19)
    Jump("loc_3CF3")

    label("loc_3CCC")

    OP_D2(0x70053, 0x7005B, 0x19)
    Jump("loc_3CF3")

    label("loc_3CD9")

    OP_D2(0x70063, 0x7006B, 0x19)
    Jump("loc_3CF3")

    label("loc_3CE6")

    OP_D2(0x70073, 0x7007B, 0x19)
    Jump("loc_3CF3")

    label("loc_3CF3")

    SetChrChipByIndex(0x101, 22)
    SetChrChipByIndex(0x102, 23)
    SetChrChipByIndex(0xF8, 24)
    SetChrChipByIndex(0xF9, 25)
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
    LoadEffect(0x0, "map\\\\mp013_00.eff")
    PlayEffect(0x0, 0x0, 0x24, 0, -100, 2200, 180, 0, 0, 600, 100, 3000, 0xFF, 0, 0, 0, 0)
    OP_72(0x2A, 0x4)
    OP_71(0x2A, 0x2)
    OP_71(0x2A, 0x40)
    OP_71(0x2A, 0x20)
    OP_B0(0x2A, 0x1E)
    OP_6F(0x2A, 1)
    OP_70(0x2A, 0xF0)
    OP_A1(0x24, 0x2A)
    SetChrFlags(0x24, 0x40)
    SetChrPos(0x24, 4000, -2900, 14170, 180)
    OP_8C(0x24, 90, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x40)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xF9, 0x1)
    ClearChrFlags(0x22, 0x1)
    SetChrFlags(0x22, 0x20)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0xF8, 0x20)
    SetChrFlags(0xF9, 0x20)
    OP_48()
    OP_8C(0x24, 270, 0)
    OP_89(0x101, 4900, -2800, 13940, 90)
    OP_89(0x102, 4900, -2800, 14580, 90)
    OP_89(0xF8, 3550, -2800, 14580, 90)
    OP_89(0xF9, 3550, -2800, 13940, 90)
    OP_89(0x22, 2900, -3000, 13800, 180)
    SetChrBattleFlags(0x22, 0x20)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x102, 0x20)
    SetChrBattleFlags(0xF8, 0x20)
    SetChrBattleFlags(0xF9, 0x20)
    OP_48()
    OP_6D(15100, -1800, 13700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_3EC8():

        label("loc_3EC8")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3EC8")

    QueueWorkItem2(0x16, 1, lambda_3EC8)

    def lambda_3ED9():

        label("loc_3ED9")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3ED9")

    QueueWorkItem2(0x17, 1, lambda_3ED9)

    def lambda_3EEA():

        label("loc_3EEA")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3EEA")

    QueueWorkItem2(0x18, 1, lambda_3EEA)

    def lambda_3EFB():

        label("loc_3EFB")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3EFB")

    QueueWorkItem2(0x19, 1, lambda_3EFB)

    def lambda_3F0C():

        label("loc_3F0C")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3F0C")

    QueueWorkItem2(0x1A, 1, lambda_3F0C)

    def lambda_3F1D():

        label("loc_3F1D")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3F1D")

    QueueWorkItem2(0x1B, 1, lambda_3F1D)

    def lambda_3F2E():

        label("loc_3F2E")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3F2E")

    QueueWorkItem2(0x1C, 1, lambda_3F2E)

    def lambda_3F3F():

        label("loc_3F3F")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3F3F")

    QueueWorkItem2(0x1D, 1, lambda_3F3F)

    def lambda_3F50():

        label("loc_3F50")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3F50")

    QueueWorkItem2(0x1E, 1, lambda_3F50)

    def lambda_3F61():

        label("loc_3F61")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3F61")

    QueueWorkItem2(0x1F, 1, lambda_3F61)

    def lambda_3F72():

        label("loc_3F72")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3F72")

    QueueWorkItem2(0x20, 1, lambda_3F72)

    def lambda_3F83():

        label("loc_3F83")

        TurnDirection(0xFE, 0x24, 400)
        OP_48()
        Jump("loc_3F83")

    QueueWorkItem2(0x21, 1, lambda_3F83)

    def lambda_3F94():
        OP_8F(0xFE, 0x4650, 0xFFFFF4AC, 0x375A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_3F94)

    def lambda_3FAF():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_3FAF)

    def lambda_3FCA():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FCA)

    def lambda_3FE5():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FE5)

    def lambda_4000():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4000)

    def lambda_401B():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_401B)
    Sleep(2000)

    def lambda_403B():
        OP_6D(17380, -1800, 13360, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_403B)
    Sleep(4000)

    def lambda_4058():
        OP_8F(0xFE, 0x46FA, 0xFFFFF4AC, 0x375A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_4058)

    def lambda_4073():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_4073)

    def lambda_408E():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_408E)

    def lambda_40A9():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_40A9)

    def lambda_40C4():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_40C4)

    def lambda_40DF():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_40DF)
    Sleep(2000)

    def lambda_40FF():
        OP_8F(0xFE, 0x46FA, 0xFFFFF4AC, 0x375A, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_40FF)

    def lambda_411A():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_411A)

    def lambda_4135():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4135)

    def lambda_4150():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4150)

    def lambda_416B():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_416B)

    def lambda_4186():
        OP_91(0xFE, 0x36B0, 0x0, 0x0, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_4186)
    WaitChrThread(0x24, 0x1)
    OP_44(0x22, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_82(0x0, 0x2)
    OP_44(0x101, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x24, 0x1)
    OP_44(0x16, 0x1)
    OP_44(0x17, 0x1)
    OP_44(0x18, 0x1)
    OP_44(0x19, 0x1)
    OP_44(0x1A, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x1C, 0x1)
    OP_44(0x1D, 0x1)
    OP_44(0x1E, 0x1)
    OP_44(0x1F, 0x1)
    OP_44(0x20, 0x1)
    OP_44(0x21, 0x1)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrPos(0x0, 18420, 0, 6280, 90)
    SetChrPos(0x1, 18420, 0, 6280, 90)
    SetChrPos(0x2, 18420, 0, 6280, 90)
    SetChrPos(0x3, 18420, 0, 6280, 90)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0xF8, 0x1)
    SetChrFlags(0xF9, 0x1)
    ClearChrFlags(0x22, 0x20)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0xF8, 0x20)
    ClearChrFlags(0xF9, 0x20)
    OP_6D(18420, 0, 6280, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_71(0x2A, 0x4)
    SetChrFlags(0x22, 0x80)
    SetChrPos(0x16, 18790, -1800, 11600, 0)
    SetChrPos(0x17, 17990, -1800, 11600, 90)
    SetChrPos(0x18, 17220, -1800, 11420, 90)
    SetChrPos(0x19, 16490, -1800, 11290, 90)
    SetChrPos(0x1A, 15770, -1800, 11470, 90)
    SetChrPos(0x1B, 15050, -1800, 11610, 90)
    SetChrPos(0x1C, 14440, -1800, 10960, 45)
    SetChrPos(0x1D, 14560, -1800, 10210, 0)
    SetChrPos(0x1E, 14410, -1800, 9520, 0)
    SetChrPos(0x1F, 14460, -1800, 8730, 0)
    SetChrPos(0x20, 14350, -1800, 7960, 0)
    SetChrPos(0x21, 14470, -1800, 7260, 0)
    OP_4B(0x16, 255)
    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    OP_4B(0x19, 255)
    OP_4B(0x1A, 255)
    OP_4B(0x1B, 255)
    OP_4B(0x1C, 255)
    OP_4B(0x1D, 255)
    OP_4B(0x1E, 255)
    OP_4B(0x1F, 255)
    OP_4B(0x20, 255)
    OP_4B(0x21, 255)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_21_3C2E end

    def Function_22_43D4(): pass

    label("Function_22_43D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43E1")
    Return()

    label("loc_43E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 5)), scpexpr(EXPR_END)), "loc_43ED")
    Call(0, 23)
    Return()

    label("loc_43ED")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_440D")
    Call(0, 24)
    Call(0, 25)
    FadeToBright(0, 0)

    label("loc_440D")

    OP_A2(0x2035)
    Fade(1000)
    SetChrPos(0x101, 16260, -1300, 6720, 310)
    SetChrPos(0x102, 16260, -1300, 5650, 310)
    SetChrPos(0xF8, 17170, -550, 6760, 310)
    SetChrPos(0xF9, 17240, -550, 5550, 310)
    OP_6D(17120, -1300, 7040, 0)
    OP_67(0, 4230, -10000, 0)
    OP_6B(2180, 0)
    OP_6C(134000, 0)
    OP_6E(481, 0)
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
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45D4")
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
        (0, "loc_4575"),
        (1, "loc_457B"),
        (SWITCH_DEFAULT, "loc_4581"),
    )


    label("loc_4575")

    OP_A2(0x2001)
    Jump("loc_4581")

    label("loc_457B")

    OP_A3(0x2001)
    Jump("loc_4581")

    label("loc_4581")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_END)), "loc_459C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_459C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_END)), "loc_45AD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_END)), "loc_45BE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_45D1")
    OP_A2(0x2091)
    Jump("loc_45D4")

    label("loc_45D1")

    OP_A3(0x2091)

    label("loc_45D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4851")

    ChrTalk(    #218
        0x101,
        "#1004F#5P这、这怎么了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x102,
        "#1042F#2P好混乱啊……\x02",
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4633():
        OP_6D(17090, -1800, 5230, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4633)
    TurnDirection(0x21, 0x101, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #220
        0x21,
        (
            "#4P怎么，你们也要\x01",
            "前往对面吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(16700, -1050, 7050, 0)
    OP_67(0, 7280, -10000, 0)
    OP_6B(1630, 0)
    OP_6C(56000, 0)
    OP_6E(481, 0)
    OP_0D()

    def lambda_46C3():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_46C3)
    Sleep(100)

    def lambda_46D6():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_46D6)
    Sleep(100)

    def lambda_46E9():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_46E9)
    Sleep(100)
    OP_8C(0xF9, 270, 400)

    ChrTalk(    #221
        0x101,
        "#1004F#5P啊……怎么回事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x21,
        (
            "#6P怎么回事……\x02\x03",

            "伦格兰德大桥吊起来\x01",
            "不动了知道吧？\x02\x03",

            "因为这个，要去对面\x01",
            "只能乘小船了。\x02\x03",

            "而这里就是渡口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        "#1007F#5P是、是这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x102,
        (
            "#1043F#2P那……\x01",
            "还是很不方便啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x21,
        (
            "#6P不方便当然不方便。\x01",
            "说实话，真是受不了啊。\x02\x03",

            "虽然由于新市长的安排\x01",
            "坐船是免费的……\x02\x03",

            "尽管如此，光是排队\x01",
            "就要等上３０分钟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A22")

    label("loc_4851")


    ChrTalk(    #226
        0x101,
        "#1004F#5P这个，难道就是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x102,
        (
            "#1042F#2P嘉恩先生说的\x01",
            "小船渡口呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_48B7():
        OP_6D(17090, -1800, 5230, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_48B7)
    TurnDirection(0x21, 0x101, 400)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #228
        0x21,
        (
            "#4P怎么，你们也\x01",
            "前往对面吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_6D(16700, -1050, 7050, 0)
    OP_67(0, 7280, -10000, 0)
    OP_6B(1630, 0)
    OP_6C(56000, 0)
    OP_6E(481, 0)
    OP_0D()

    def lambda_4945():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4945)
    Sleep(100)

    def lambda_4958():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4958)
    Sleep(100)

    def lambda_496B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_496B)
    Sleep(100)
    OP_8C(0xF9, 270, 400)

    ChrTalk(    #229
        0x101,
        (
            "#1025F#5P啊，嗯。\x01",
            "虽然有这打算……\x02\x03",

            "需要花钱吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x21,
        (
            "#6P不，由于新市长的安排\x01",
            "坐船是免费的……\x02\x03",

            "尽管如此，光是排队\x01",
            "就要等上３０分钟。\x02\x03",

            "说实话，真是受不了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A58")

    ChrTalk(    #231
        0x107,
        (
            "#065F#2P呜哎～……\x01",
            "要那么久吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AB3")

    label("loc_4A58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A87")

    ChrTalk(    #232
        0x103,
        "#025F#2P那可够久的呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AB3")

    label("loc_4A87")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AB3")

    ChrTalk(    #233
        0x106,
        "#052F#2P那可够久的啊……\x02",
    )

    CloseMessageWindow()

    label("loc_4AB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B03")

    ChrTalk(    #234
        0x108,
        (
            "#074F#2P不过，因为是往返航程，\x01",
            "需要这么长时间也没办法呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BA0")

    label("loc_4B03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B53")

    ChrTalk(    #235
        0x106,
        (
            "#053F#2P不过，因为是往返航程，\x01",
            "需要这么长时间也没办法呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BA0")

    label("loc_4B53")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BA0")

    ChrTalk(    #236
        0x103,
        (
            "#025F#2P不过，因为是往返航程，\x01",
            "需要这么长时间也没办法呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BA0")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #237
        0x102,
        (
            "#1042F#4P怎么办，艾丝蒂尔。\x01",
            "我们也前往对面吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #238
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
            "【渡去北街区】\x01",      # 0
            "【先不过去】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D92")

    ChrTalk(    #239
        0x101,
        (
            "#1025F#5P不，先不去了。\x02\x03",

            "做完手上的事之后\x01",
            "再去对面吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x102,
        (
            "#1040F#4P知道了。\x01",
            "那么回去吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(18420, 0, 6280, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 18420, 0, 6280, 90)
    SetChrPos(0x1, 18420, 0, 6280, 90)
    SetChrPos(0x2, 18420, 0, 6280, 90)
    SetChrPos(0x3, 18420, 0, 6280, 90)
    OP_69(0x0, 0x0)
    OP_4B(0x16, 255)
    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    OP_4B(0x19, 255)
    OP_4B(0x1A, 255)
    OP_4B(0x1B, 255)
    OP_4B(0x1C, 255)
    OP_4B(0x1D, 255)
    OP_4B(0x1E, 255)
    OP_4B(0x1F, 255)
    OP_4B(0x20, 255)
    OP_4B(0x21, 255)
    OP_8C(0x21, 0, 0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    label("loc_4D92")

    OP_A2(0x2036)

    ChrTalk(    #241
        0x101,
        (
            "#1007F#5P……没法子。\x01",
            "似乎也没其他的办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
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
    OP_6D(15520, -1550, 8870, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x1A, 18790, -1800, 11600, 0)
    SetChrPos(0x1B, 17990, -1800, 11600, 90)
    SetChrPos(0x1C, 17220, -1800, 11420, 90)
    SetChrPos(0x1D, 16490, -1800, 11290, 90)
    SetChrPos(0x1E, 15770, -1800, 11470, 90)
    SetChrPos(0x1F, 15050, -1800, 11610, 90)
    SetChrPos(0x20, 14440, -1800, 10960, 45)
    SetChrPos(0x21, 14560, -1800, 10210, 0)
    SetChrPos(0x101, 14410, -1800, 9520, 0)
    SetChrPos(0x102, 14460, -1800, 8730, 0)
    SetChrPos(0xF8, 14350, -1800, 7960, 0)
    SetChrPos(0xF9, 14470, -1800, 7260, 0)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(14870, -1800, 11420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x1E, 18790, -1800, 11600, 0)
    SetChrPos(0x1F, 17990, -1800, 11600, 90)
    SetChrPos(0x20, 17220, -1800, 11420, 90)
    SetChrPos(0x21, 16490, -1800, 11290, 90)
    SetChrPos(0x101, 15770, -1800, 11470, 90)
    SetChrPos(0x102, 15050, -1800, 11610, 90)
    SetChrPos(0xF8, 14440, -1800, 10960, 45)
    SetChrPos(0xF9, 14560, -1800, 10210, 0)
    SetChrPos(0x18, 14410, -1800, 9520, 0)
    SetChrPos(0x16, 14460, -1800, 8730, 0)
    SetChrPos(0x19, 14350, -1800, 7960, 0)
    SetChrPos(0x17, 14470, -1800, 7260, 0)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x17, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(17470, -1800, 11460, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 18790, -1800, 11600, 0)
    SetChrPos(0x102, 17990, -1800, 11600, 90)
    SetChrPos(0xF8, 17220, -1800, 11420, 90)
    SetChrPos(0xF9, 16490, -1800, 11290, 90)
    SetChrPos(0x18, 15770, -1800, 11470, 90)
    SetChrPos(0x16, 15050, -1800, 11610, 90)
    SetChrPos(0x19, 14440, -1800, 10960, 45)
    SetChrPos(0x17, 14560, -1800, 10210, 0)
    SetChrPos(0x1A, 14410, -1800, 9520, 0)
    SetChrPos(0x1C, 14460, -1800, 8730, 0)
    SetChrPos(0x1B, 14350, -1800, 7960, 0)
    SetChrPos(0x1D, 14470, -1800, 7260, 0)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1D, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(18450, -1800, 12450, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2220, 0)
    OP_6C(135000, 0)
    OP_6E(381, 0)
    SetChrPos(0x101, 19290, -1800, 11600, 0)
    SetChrPos(0x102, 18490, -1800, 11600, 0)
    SetChrPos(0xF8, 17720, -1800, 11420, 0)
    SetChrPos(0xF9, 16990, -1800, 11290, 0)
    LoadEffect(0x1, "map\\\\mp013_02.eff")
    PlayEffect(0x1, 0x1, 0x24, 0, -200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x2A, 0x4)
    OP_72(0x2A, 0x2)
    OP_71(0x2A, 0x400)
    OP_71(0x2A, 0x40)
    OP_71(0x2A, 0x20)
    OP_B0(0x2A, 0x1E)
    OP_6F(0x2A, 1)
    OP_70(0x2A, 0xF0)
    OP_A1(0x24, 0x2A)
    SetChrFlags(0x24, 0x40)
    SetChrPos(0x24, 18170, -2900, 14170, 90)
    OP_8C(0x24, 90, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x40)
    ClearChrBattleFlags(0x22, 0x20)
    SetChrPos(0x22, 19600, -3000, 14300, 180)
    OP_48()
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #243
        0x22,
        (
            "#6P久等了。\x01",
            "轮到你们了。\x02\x03",

            "赶快上小船吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x101,
        "#1006F#5P啊，嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x102,
        "#1040F#2P那就拜托了。\x02",
    )

    CloseMessageWindow()
    OP_82(0x1, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x1CC, 0x0, 0x64)
    Sleep(2000)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/T2100   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_22_43D4 end

    def Function_23_539C(): pass

    label("Function_23_539C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53BC")
    Call(0, 24)
    Call(0, 25)
    FadeToBright(0, 0)

    label("loc_53BC")

    Fade(1000)
    SetChrPos(0x101, 16260, -1300, 6720, 270)
    SetChrPos(0x102, 16260, -1300, 5650, 270)
    SetChrPos(0xF8, 17170, -550, 6760, 270)
    SetChrPos(0xF9, 17240, -550, 5550, 270)
    OP_6D(16700, -1050, 7050, 0)
    OP_67(0, 7090, -10000, 0)
    OP_6B(1640, 0)
    OP_6C(56000, 0)
    OP_6E(481, 0)
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
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54CE")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #246
        0x102,
        (
            "#1042F怎么办，艾丝蒂尔。\x01",
            "我们也前往对面吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x101,
        "#1015F#5P唔，嗯～……\x02",
    )

    CloseMessageWindow()

    label("loc_54CE")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【渡去北街区】\x01",      # 0
            "【先不过去】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5668")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5599")
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #248
        0x101,
        (
            "#1025F#5P不，先不去了。\x02\x03",

            "做完手上的事之后\x01",
            "再去对面吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x102,
        (
            "#1040F明白了。\x01",
            "那么回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5599")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(18420, 0, 6280, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 18420, 0, 6280, 90)
    SetChrPos(0x1, 18420, 0, 6280, 90)
    SetChrPos(0x2, 18420, 0, 6280, 90)
    SetChrPos(0x3, 18420, 0, 6280, 90)
    OP_69(0x0, 0x0)
    OP_4B(0x16, 255)
    OP_4B(0x17, 255)
    OP_4B(0x18, 255)
    OP_4B(0x19, 255)
    OP_4B(0x1A, 255)
    OP_4B(0x1B, 255)
    OP_4B(0x1C, 255)
    OP_4B(0x1D, 255)
    OP_4B(0x1E, 255)
    OP_4B(0x1F, 255)
    OP_4B(0x20, 255)
    OP_4B(0x21, 255)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    label("loc_5668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D0")
    TurnDirection(0x101, 0x102, 400)
    Sleep(700)

    ChrTalk(    #250
        0x101,
        (
            "#1007F#5P……没法子。\x01",
            "似乎也没其他的办法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x102,
        (
            "#1040F#4P知道了。\x01",
            "那么排队吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56D0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(15520, -1550, 8870, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x1A, 18790, -1800, 11600, 0)
    SetChrPos(0x1B, 17990, -1800, 11600, 90)
    SetChrPos(0x1C, 17220, -1800, 11420, 90)
    SetChrPos(0x1D, 16490, -1800, 11290, 90)
    SetChrPos(0x1E, 15770, -1800, 11470, 90)
    SetChrPos(0x1F, 15050, -1800, 11610, 90)
    SetChrPos(0x20, 14440, -1800, 10960, 45)
    SetChrPos(0x21, 14560, -1800, 10210, 0)
    SetChrPos(0x101, 14410, -1800, 9520, 0)
    SetChrPos(0x102, 14460, -1800, 8730, 0)
    SetChrPos(0xF8, 14350, -1800, 7960, 0)
    SetChrPos(0xF9, 14470, -1800, 7260, 0)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(14870, -1800, 11420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    SetChrPos(0x1E, 18790, -1800, 11600, 0)
    SetChrPos(0x1F, 17990, -1800, 11600, 90)
    SetChrPos(0x20, 17220, -1800, 11420, 90)
    SetChrPos(0x21, 16490, -1800, 11290, 90)
    SetChrPos(0x101, 15770, -1800, 11470, 90)
    SetChrPos(0x102, 15050, -1800, 11610, 90)
    SetChrPos(0xF8, 14440, -1800, 10960, 45)
    SetChrPos(0xF9, 14560, -1800, 10210, 0)
    SetChrPos(0x18, 14410, -1800, 9520, 0)
    SetChrPos(0x16, 14460, -1800, 8730, 0)
    SetChrPos(0x19, 14350, -1800, 7960, 0)
    SetChrPos(0x17, 14470, -1800, 7260, 0)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x17, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(17470, -1800, 11460, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 18790, -1800, 11600, 0)
    SetChrPos(0x102, 17990, -1800, 11600, 90)
    SetChrPos(0xF8, 17220, -1800, 11420, 90)
    SetChrPos(0xF9, 16490, -1800, 11290, 90)
    SetChrPos(0x18, 15770, -1800, 11470, 90)
    SetChrPos(0x16, 15050, -1800, 11610, 90)
    SetChrPos(0x19, 14440, -1800, 10960, 45)
    SetChrPos(0x17, 14560, -1800, 10210, 0)
    SetChrPos(0x1A, 14410, -1800, 9520, 0)
    SetChrPos(0x1C, 14460, -1800, 8730, 0)
    SetChrPos(0x1B, 14350, -1800, 7960, 0)
    SetChrPos(0x1D, 14470, -1800, 7260, 0)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1D, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_6D(18450, -1800, 12450, 0)
    OP_67(0, 4950, -10000, 0)
    OP_6B(2220, 0)
    OP_6C(135000, 0)
    OP_6E(381, 0)
    SetChrPos(0x101, 19290, -1800, 11600, 0)
    SetChrPos(0x102, 18490, -1800, 11600, 0)
    SetChrPos(0xF8, 17720, -1800, 11420, 0)
    SetChrPos(0xF9, 16990, -1800, 11290, 0)
    LoadEffect(0x1, "map\\\\mp013_02.eff")
    PlayEffect(0x1, 0x1, 0x24, 0, -200, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_72(0x2A, 0x4)
    OP_72(0x2A, 0x2)
    OP_71(0x2A, 0x400)
    OP_71(0x2A, 0x40)
    OP_71(0x2A, 0x20)
    OP_B0(0x2A, 0x1E)
    OP_6F(0x2A, 1)
    OP_70(0x2A, 0xF0)
    OP_A1(0x24, 0x2A)
    SetChrFlags(0x24, 0x40)
    SetChrPos(0x24, 18170, -2900, 14170, 90)
    OP_8C(0x24, 90, 0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x40)
    ClearChrBattleFlags(0x22, 0x20)
    SetChrPos(0x22, 19600, -3000, 14200, 180)
    OP_48()
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x406, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C6C")
    OP_A2(0x2036)

    ChrTalk(    #252
        0x22,
        (
            "#6P久等了。\x01",
            "轮到你们了。\x02\x03",

            "赶快上小船吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x101,
        "#1006F#5P啊，嗯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x102,
        "#1040F#2P那就拜托了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5CA0")

    label("loc_5C6C")


    ChrTalk(    #255
        0x22,
        (
            "#6P好，轮到你们了哦。\x02\x03",

            "后面很挤\x01",
            "赶快上小船吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CA0")

    OP_82(0x1, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x1CC, 0x0, 0x64)
    Sleep(2000)
    OP_A2(0x10F5)
    NewScene("ED6_DT21/T2100   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_23_539C end

    def Function_24_5CC5(): pass

    label("Function_24_5CC5")

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
        (0, "loc_5D3F"),
        (1, "loc_5D45"),
        (SWITCH_DEFAULT, "loc_5D4B"),
    )


    label("loc_5D3F")

    OP_A2(0x1200)
    Jump("loc_5D4B")

    label("loc_5D45")

    OP_A2(0x1201)
    Jump("loc_5D4B")

    label("loc_5D4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5D59")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_5D5D")

    label("loc_5D59")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_5D5D")

    Return()

    # Function_24_5CC5 end

    def Function_25_5D5E(): pass

    label("Function_25_5D5E")

    ClearMapFlags(0x1)
    OP_6D(122280, 0, 24310, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_25_5D5E end

    def Function_26_5DB7(): pass

    label("Function_26_5DB7")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_26_5DB7 end

    def Function_27_5DBE(): pass

    label("Function_27_5DBE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #256
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

    # Function_27_5DBE end

    def Function_28_5E38(): pass

    label("Function_28_5E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x248, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5E45")
    Return()

    label("loc_5E45")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E61")
    Call(0, 24)
    FadeToBright(0, 0)

    label("loc_5E61")

    Fade(1000)
    SetChrPos(0x101, 29960, 1050, 15670, 180)
    SetChrPos(0xF7, 29070, 900, 16290, 180)
    SetChrPos(0x23, 24000, 0, 8780, 90)
    ClearChrFlags(0x23, 0x80)

    def lambda_5EA4():

        label("loc_5EA4")

        OP_69(0x25, 0x0)
        OP_48()
        Jump("loc_5EA4")

    QueueWorkItem2(0x25, 1, lambda_5EA4)
    OP_43(0x25, 0x2, 0x0, 0x1D)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)

    def lambda_5EE8():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5EE8)
    Sleep(200)

    def lambda_5F03():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_5F03)

    def lambda_5F19():
        OP_8E(0xFE, 0x72C4, 0x0, 0x224C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_5F19)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #257
        0x101,
        (
            "#1004F啊……！？\x02\x03",

            "难不成是罗伊德大叔？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x23, 0x1)
    OP_44(0x25, 0x1)
    OP_44(0x25, 0x2)
    OP_62(0x23, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x23, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #258
        0x23,
        "噢，原来是你们啊。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x23, 0, 400)

    def lambda_5FCC():
        OP_8E(0xFE, 0x7332, 0x280, 0x33A4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_5FCC)
    OP_6D(29180, 1050, 14710, 2000)

    ChrTalk(    #259
        0x23,
        (
            "怎样，想马上\x01",
            "试试鱼竿吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        (
            "#1015F不，还不行呢。\x02\x03",

            "还有些地方要去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0x23,
        "原来如此，这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x23,
        (
            "这样的话，要不先去\x01",
            "附近的钓鱼点看看吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x23,
        "有个很近的好地方。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #264
        0x101,
        "#1018F真的！？要去！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6115")

    ChrTalk(    #265
        0x106,
        (
            "#552F……喂，不是要去找渡鸦帮\x01",
            "问亡灵的事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6147")

    label("loc_6115")


    ChrTalk(    #266
        0x103,
        (
            "#023F不是要去找渡鸦帮那帮小子\x01",
            "问亡灵的事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6147")

    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0xF7, 400)
    Sleep(1000)

    ChrTalk(    #267
        0x101,
        (
            "#1008F我、我当然知道。\x02\x03",

            "就是，稍微\x01",
            "绕个道而已……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_61CC")

    ChrTalk(    #268
        0x106,
        (
            "#551F唉，真没办法……\x01",
            "赶快搞定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61F8")

    label("loc_61CC")


    ChrTalk(    #269
        0x103,
        (
            "#021F呵呵，真没办法呢。\x01",
            "好吧，陪你去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61F8")


    ChrTalk(    #270
        0x23,
        (
            "哈哈，不必担心。\x01",
            "不会占用多少时间的啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x23,
        (
            "那么，我带你们去吧。\x01",
            "跟我来。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x23, 400)

    ChrTalk(    #272
        0x101,
        "#1001F嗯！！\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(19780, 0, 26480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(96000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1690, 0, 29190, 0)
    SetChrPos(0xF7, -880, 0, 28060, 0)
    SetChrPos(0x23, -310, 0, 29250, 0)

    def lambda_62E7():
        OP_6D(-980, 0, 29260, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_62E7)

    def lambda_62FF():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_62FF)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    Sleep(400)

    ChrTalk(    #273
        0x101,
        "#1011F这里就是那个钓鱼点？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x23,
        "唔，仔细看水面。\x02",
    )

    CloseMessageWindow()
    OP_6D(-1300, -2000, 34150, 2000)

    ChrTalk(    #275
        0x23,
        "#1P看，有波纹吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0x23,
        (
            "#1P出现波纹的地方\x01",
            "就证明一定有鱼哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x23,
        (
            "#1P在水边仔细找找就能看到了，\x01",
            "到各处积极奔走寻找吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x101,
        (
            "#1006FＯＫ。\x01",
            "关键就是注意水面吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(-980, 0, 29260, 0)
    OP_6B(2800, 0)
    OP_6E(262, 0)
    TurnDirection(0x101, 0x23, 0)
    TurnDirection(0x23, 0x101, 0)
    OP_0D()

    ChrTalk(    #279
        0x23,
        "地点就是这样了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x23,
        "接着给你这个吧。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #281
        "\x07\x00得到了５个\x1F\xDB\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3DB, 5)

    ChrTalk(    #282
        0x23,
        "这是钓鱼用的饵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x23,
        (
            "不过店里是买不到的，\x01",
            "所以要自己弄。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0x23,
        (
            "魔兽经常会掉落，\x01",
            "应该难不倒身为游击士的你吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0x101,
        "#1018F啊，这真是帮大忙了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x23,
        (
            "当前要说明的\x01",
            "就是这些了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x23,
        (
            "接下来就\x01",
            "自己多多尝试吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x101,
        (
            "#1006F嗯，知道了。\x01",
            "谢谢您关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x23,
        (
            "不不，这也是\x01",
            "『钓公师团』的职责嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x23,
        (
            "那么，回头见。\x01",
            "期待你出色的钓鱼成果哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_660D():

        label("loc_660D")

        TurnDirection(0xFE, 0x23, 400)
        OP_48()
        Jump("loc_660D")

    QueueWorkItem2(0x101, 1, lambda_660D)

    def lambda_661E():

        label("loc_661E")

        TurnDirection(0xFE, 0x23, 400)
        OP_48()
        Jump("loc_661E")

    QueueWorkItem2(0xF7, 1, lambda_661E)

    def lambda_662F():
        OP_69(0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_662F)
    SetChrFlags(0x23, 0x40)
    OP_8E(0x23, 0x96, 0x0, 0x6DB0, 0x7D0, 0x0)
    OP_8E(0x23, 0xA96, 0x0, 0x6DB0, 0x7D0, 0x0)
    OP_8E(0x23, 0xDCA, 0x0, 0x70F8, 0x7D0, 0x0)
    OP_8E(0x23, 0x14B4, 0x0, 0x7148, 0x7D0, 0x0)
    OP_8E(0x23, 0x173E, 0xFFFFF8F8, 0x6298, 0x7D0, 0x0)
    SetChrFlags(0x23, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    WaitChrThread(0x25, 0x1)
    OP_65(0x4, 0x1)
    OP_A2(0x1242)
    EventEnd(0x0)
    Return()

    # Function_28_5E38 end

    def Function_29_66BC(): pass

    label("Function_29_66BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6708")
    OP_51(0x25, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF7, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_29_66BC")

    label("loc_6708")

    Return()

    # Function_29_66BC end

    def Function_30_6709(): pass

    label("Function_30_6709")

    EventBegin(0x1)

    ChrTalk(    #291
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_6735():
        OP_6D(-1300, 0, 34150, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6735)

    def lambda_674D():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_674D)

    def lambda_675D():
        OP_6C(315000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_675D)
    Sleep(1500)
    SetChrName("")

    AnonymousTalk(    #292
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6802")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_C0(0xE, 0x18, 0xFFFFFC22, 0x0, 0x738C, 0x0, 0xFFFFFAEC, 0xFFFFF448, 0x8566)
    OP_51(0x101, 0x28, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    EventEnd(0x1)
    Jump("loc_6811")

    label("loc_6802")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6811")
    EventEnd(0x1)

    label("loc_6811")

    Return()

    # Function_30_6709 end

    def Function_31_6812(): pass

    label("Function_31_6812")

    SetPlaceName(0x69)
    Return()

    # Function_31_6812 end

    def Function_32_6816(): pass

    label("Function_32_6816")

    SetPlaceName(0x52)
    Return()

    # Function_32_6816 end

    SaveToFile()

Try(main)
