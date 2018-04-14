from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3200   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T3200   ._SN',
            'ED6_DT21/T3200_1 ._SN',
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
        '毛婆婆',                               # 9
        '艾德',                                 # 10
        '艾缇',                                 # 11
        '孩子',                                 # 12
        '孩子',                                 # 13
        '游客',                                 # 14
        '游客',                                 # 15
        '游客',                                 # 16
        '拉克',                                 # 17
        '库安',                                 # 18
        '法尔茨',                               # 19
        '格温副队长',                           # 20
        '士兵科尔比',                           # 21
        '士兵阿曼德',                           # 22
        '莉西亚',                               # 23
        '猿羊',                                 # 24
        '猿羊',                                 # 25
        '猿羊',                                 # 26
        '猿羊',                                 # 27
        '猿羊',                                 # 28
        '猿羊',                                 # 29
        '村民',                                 # 30
        '村民',                                 # 31
        '村民',                                 # 32
        '村民',                                 # 33
        '村民',                                 # 34
        '村民',                                 # 35
        '赫雷思老人',                           # 36
        '托兰特平原道方向',                     # 37
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
        'ED6_DT07/CH02430 ._CH',             # 00
        'ED6_DT07/CH01270 ._CH',             # 01
        'ED6_DT07/CH01130 ._CH',             # 02
        'ED6_DT07/CH01270 ._CH',             # 03
        'ED6_DT07/CH01070 ._CH',             # 04
        'ED6_DT07/CH01200 ._CH',             # 05
        'ED6_DT07/CH01210 ._CH',             # 06
        'ED6_DT07/CH01220 ._CH',             # 07
        'ED6_DT07/CH01160 ._CH',             # 08
        'ED6_DT07/CH01060 ._CH',             # 09
        'ED6_DT07/CH01140 ._CH',             # 0A
        'ED6_DT09/CH10140 ._CH',             # 0B
        'ED6_DT09/CH10141 ._CH',             # 0C
        'ED6_DT07/CH01000 ._CH',             # 0D
        'ED6_DT07/CH01010 ._CH',             # 0E
        'ED6_DT07/CH01020 ._CH',             # 0F
        'ED6_DT07/CH01030 ._CH',             # 10
        'ED6_DT07/CH01040 ._CH',             # 11
        'ED6_DT07/CH01050 ._CH',             # 12
        'ED6_DT26/CH20253 ._CH',             # 13
        'ED6_DT26/CH20248 ._CH',             # 14
        'ED6_DT26/CH20251 ._CH',             # 15
        'ED6_DT26/CH20249 ._CH',             # 16
        'ED6_DT26/CH20250 ._CH',             # 17
        'ED6_DT26/CH20257 ._CH',             # 18
        'ED6_DT09/CH11150 ._CH',             # 19
        'ED6_DT09/CH11151 ._CH',             # 1A
        'ED6_DT29/CH12070 ._CH',             # 1B
        'ED6_DT29/CH12071 ._CH',             # 1C
        'ED6_DT07/CH01640 ._CH',             # 1D
        'ED6_DT07/CH01150 ._CH',             # 1E
    )

    AddCharChipPat(
        'ED6_DT07/CH02430P._CP',             # 00
        'ED6_DT07/CH01270P._CP',             # 01
        'ED6_DT07/CH01130P._CP',             # 02
        'ED6_DT07/CH01270P._CP',             # 03
        'ED6_DT07/CH01070P._CP',             # 04
        'ED6_DT07/CH01200P._CP',             # 05
        'ED6_DT07/CH01210P._CP',             # 06
        'ED6_DT07/CH01220P._CP',             # 07
        'ED6_DT07/CH01160P._CP',             # 08
        'ED6_DT07/CH01060P._CP',             # 09
        'ED6_DT07/CH01140P._CP',             # 0A
        'ED6_DT09/CH10140P._CP',             # 0B
        'ED6_DT09/CH10141P._CP',             # 0C
        'ED6_DT07/CH01000P._CP',             # 0D
        'ED6_DT07/CH01010P._CP',             # 0E
        'ED6_DT07/CH01020P._CP',             # 0F
        'ED6_DT07/CH01030P._CP',             # 10
        'ED6_DT07/CH01040P._CP',             # 11
        'ED6_DT07/CH01050P._CP',             # 12
        'ED6_DT26/CH20253P._CP',             # 13
        'ED6_DT26/CH20248P._CP',             # 14
        'ED6_DT26/CH20251P._CP',             # 15
        'ED6_DT26/CH20249P._CP',             # 16
        'ED6_DT26/CH20250P._CP',             # 17
        'ED6_DT26/CH20257P._CP',             # 18
        'ED6_DT09/CH11150P._CP',             # 19
        'ED6_DT09/CH11151P._CP',             # 1A
        'ED6_DT29/CH12070P._CP',             # 1B
        'ED6_DT29/CH12071P._CP',             # 1C
        'ED6_DT07/CH01640P._CP',             # 1D
        'ED6_DT07/CH01150P._CP',             # 1E
    )

    DeclNpc(
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 12020,
        Z                   = 2000,
        Y                   = 16870,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 12020,
        Z                   = 2000,
        Y                   = 14160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 21790,
        Z                   = 2000,
        Y                   = 5570,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 22880,
        Z                   = 2000,
        Y                   = 9470,
        Direction           = 303,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 8760,
        Z                   = 2000,
        Y                   = 13310,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 38180,
        Z                   = 6000,
        Y                   = 49000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 29,
        ChipIndex           = 0x1D,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 49580,
        Z                   = 2500,
        Y                   = -2390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 30,
        ChipIndex           = 0x1E,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 67620,
        Z                   = 3420,
        Y                   = 25770,
        Direction           = 195,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 66090,
        Z                   = 3020,
        Y                   = 25680,
        Direction           = 162,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 62800,
        Z                   = 3020,
        Y                   = 25140,
        Direction           = 156,
        Unknown2            = 0,
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 61950,
        Z                   = 3020,
        Y                   = 23550,
        Direction           = 98,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 73010,
        Z                   = 3020,
        Y                   = 25590,
        Direction           = 215,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 67620,
        Z                   = 3420,
        Y                   = 25770,
        Direction           = 195,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 13520,
        Z                   = 2500,
        Y                   = 13590,
        Direction           = 312,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -30790,
        Z                   = -2000,
        Y                   = 15330,
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
        X                   = 28950,
        Y                   = 1000,
        Z                   = 4030,
        Range               = 2500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 37,
    )

    DeclEvent(
        X                   = 980,
        Y                   = -250,
        Z                   = 18420,
        Range               = 1250,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 38,
    )

    DeclEvent(
        X                   = 42330,
        Y                   = 5750,
        Z                   = 36020,
        Range               = 1250,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 39,
    )


    DeclActor(
        TriggerX            = 40000,
        TriggerZ            = 6000,
        TriggerY            = 49730,
        TriggerRange        = 800,
        ActorX              = 40000,
        ActorZ              = 7000,
        ActorY              = 49730,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 43290,
        TriggerZ            = 6250,
        TriggerY            = 35890,
        TriggerRange        = 800,
        ActorX              = 43290,
        ActorZ              = 6500,
        ActorY              = 35890,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 22,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53100,
        TriggerZ            = 0,
        TriggerY            = 3880,
        TriggerRange        = 1000,
        ActorX              = 48680,
        ActorZ              = 0,
        ActorY              = 2470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 36,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_60E",          # 00, 0
        "Function_1_787",          # 01, 1
        "Function_2_A5F",          # 02, 2
        "Function_3_BDC",          # 03, 3
        "Function_4_C39",          # 04, 4
        "Function_5_CA8",          # 05, 5
        "Function_6_D17",          # 06, 6
        "Function_7_DC7",          # 07, 7
        "Function_8_E3C",          # 08, 8
        "Function_9_EEB",          # 09, 9
        "Function_10_F84",         # 0A, 10
        "Function_11_12E4",        # 0B, 11
        "Function_12_1529",        # 0C, 12
        "Function_13_1779",        # 0D, 13
        "Function_14_196A",        # 0E, 14
        "Function_15_1B77",        # 0F, 15
        "Function_16_1C77",        # 10, 16
        "Function_17_1D2D",        # 11, 17
        "Function_18_30DE",        # 12, 18
        "Function_19_3123",        # 13, 19
        "Function_20_317E",        # 14, 20
        "Function_21_31D4",        # 15, 21
        "Function_22_33A5",        # 16, 22
        "Function_23_346B",        # 17, 23
        "Function_24_3705",        # 18, 24
        "Function_25_3762",        # 19, 25
        "Function_26_37C4",        # 1A, 26
        "Function_27_380B",        # 1B, 27
        "Function_28_387A",        # 1C, 28
        "Function_29_38D2",        # 1D, 29
        "Function_30_391E",        # 1E, 30
        "Function_31_3994",        # 1F, 31
        "Function_32_39C4",        # 20, 32
        "Function_33_39F4",        # 21, 33
        "Function_34_3A67",        # 22, 34
        "Function_35_3B00",        # 23, 35
        "Function_36_3B66",        # 24, 36
        "Function_37_3C69",        # 25, 37
        "Function_38_3C6D",        # 26, 38
        "Function_39_3C71",        # 27, 39
    )


    def Function_0_60E(): pass

    label("Function_0_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_65E")
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x10, 14240, 2500, 16350, 90)
    SetChrPos(0x11, 14240, 2500, 17460, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_656")
    Jump("loc_65B")

    label("loc_656")

    ClearChrFlags(0x16, 0x80)

    label("loc_65B")

    Jump("loc_74A")

    label("loc_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_68F")
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x10, 12150, 2000, 16180, 90)
    SetChrPos(0x11, 12150, 2000, 15380, 90)
    Jump("loc_74A")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_6E7")
    SetChrPos(0x12, 15380, 2000, 12210, 0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x10, 12150, 2000, 20300, 90)
    SetChrPos(0x11, 12150, 2000, 19500, 90)
    SetChrPos(0x9, 21950, 2000, 14600, 270)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_74A")

    label("loc_6E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_735")
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x10, 12150, 2000, 15860, 180)
    SetChrPos(0x11, 12150, 2000, 15150, 0)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    OP_43(0x10, 0x0, 0x0, 0x4)
    OP_43(0x11, 0x0, 0x0, 0x5)
    ClearChrFlags(0x23, 0x80)
    Jump("loc_74A")

    label("loc_735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_74A")
    OP_43(0x10, 0x0, 0x0, 0x3)
    OP_43(0x11, 0x0, 0x0, 0x3)

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_75B")
    OP_A3(0x10F0)
    Event(1, 0)
    Jump("loc_786")

    label("loc_75B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_771")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 23)
    Jump("loc_786")

    label("loc_771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_786")
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_786")

    Return()

    # Function_0_60E end

    def Function_1_787(): pass

    label("Function_1_787")

    OP_16(0x2, 0xFA0, 0xFFFE8130, 0xFFFE5E08, 0x230054)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D4")
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x89, 0x0)
    OP_82(0x8A, 0x0)
    OP_82(0x8B, 0x0)
    OP_82(0x8C, 0x0)
    OP_82(0x8D, 0x0)
    OP_82(0x8E, 0x0)
    OP_82(0x8F, 0x0)

    label("loc_7D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E8")
    OP_72(0x3, 0x10)
    OP_65(0x1, 0x1)
    Jump("loc_7EC")

    label("loc_7E8")

    OP_64(0x1, 0x1)

    label("loc_7EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_7F6")
    Jump("loc_A3F")

    label("loc_7F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_A2E")
    PlayEffect(0x91, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x92, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x93, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x94, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x95, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x96, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x97, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x98, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x99, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x9A, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundDistance(0x10B, 0x41E6, 0x9C4, 0x42EA, 0x7D0, 0x61A8, 0x64, 0x0)
    Jump("loc_A3F")

    label("loc_A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_A38")
    Jump("loc_A3F")

    label("loc_A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_A3F")

    label("loc_A3F")

    OP_72(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A53")
    OP_65(0x0, 0x1)
    Jump("loc_A5E")

    label("loc_A53")

    OP_64(0x0, 0x1)
    OP_6F(0xB, 120)

    label("loc_A5E")

    Return()

    # Function_1_787 end

    def Function_2_A5F(): pass

    label("Function_2_A5F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A84")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_BC6")

    label("loc_A84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9D")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_BC6")

    label("loc_A9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB6")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_BC6")

    label("loc_AB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACF")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_BC6")

    label("loc_ACF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE8")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_BC6")

    label("loc_AE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B01")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_BC6")

    label("loc_B01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_BC6")

    label("loc_B1A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B33")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_BC6")

    label("loc_B33")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_BC6")

    label("loc_B4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B65")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_BC6")

    label("loc_B65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7E")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_BC6")

    label("loc_B7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B97")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_BC6")

    label("loc_B97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB0")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_BC6")

    label("loc_BB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC6")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_BC6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BDB")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_BC6")

    label("loc_BDB")

    Return()

    # Function_2_A5F end

    def Function_3_BDC(): pass

    label("Function_3_BDC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C38")
    OP_8E(0xFE, 0x2EF4, 0x7D0, 0x573A, 0x1388, 0x0)
    OP_8E(0xFE, 0x57F8, 0x7D0, 0x573A, 0x1388, 0x0)
    OP_8E(0xFE, 0x57F8, 0x7D0, 0x2E54, 0x1388, 0x0)
    OP_8E(0xFE, 0x2EF4, 0x7D0, 0x2E54, 0x1388, 0x0)
    Jump("Function_3_BDC")

    label("loc_C38")

    Return()

    # Function_3_BDC end

    def Function_4_C39(): pass

    label("Function_4_C39")

    OP_43(0xFE, 0x1, 0x0, 0x2)

    label("loc_C40")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CA7")
    Sleep(400)
    OP_8F(0xFE, 0x2F76, 0x7D0, 0x45C4, 0x1770, 0x0)
    OP_8F(0xFE, 0x2F76, 0x7D0, 0x3DF4, 0x1770, 0x0)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0xFE, 0x0, 0x1E, 0x3E8, 0x7D0)
    OP_A2(0x8)
    OP_A6(0x9)
    OP_A3(0x9)
    Jump("loc_C40")

    label("loc_CA7")

    Return()

    # Function_4_C39 end

    def Function_5_CA8(): pass

    label("Function_5_CA8")

    OP_43(0xFE, 0x1, 0x0, 0x2)

    label("loc_CAF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D16")
    Sleep(400)
    OP_8F(0xFE, 0x2F76, 0x7D0, 0x335E, 0x1770, 0x0)
    OP_8F(0xFE, 0x2F76, 0x7D0, 0x3B2E, 0x1770, 0x0)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0xFE, 0x1E, 0xA, 0x3E8, 0x7D0)
    OP_A2(0x9)
    OP_A6(0x8)
    OP_A3(0x8)
    Jump("loc_CAF")

    label("loc_D16")

    Return()

    # Function_5_CA8 end

    def Function_6_D17(): pass

    label("Function_6_D17")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DBB")
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(10)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_D21")

    label("loc_DBB")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_D17 end

    def Function_7_DC7(): pass

    label("Function_7_DC7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E3B")
    OP_8E(0xFE, 0xFFFFDAE4, 0xFFFFF830, 0x32E6, 0x7D0, 0x0)
    Sleep(2600)
    OP_8C(0xFE, 0, 400)
    OP_8E(0xFE, 0xFFFFDAE4, 0xFFFFF830, 0x422C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2238, 0x7D0, 0x413C, 0x7D0, 0x0)
    Sleep(2600)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x2238, 0x7D0, 0x33FE, 0x7D0, 0x0)
    Jump("Function_7_DC7")

    label("loc_E3B")

    Return()

    # Function_7_DC7 end

    def Function_8_E3C(): pass

    label("Function_8_E3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_EA1")

    ChrTalk(    #0
        0x9,
        (
            "不过还真没想到温泉\x01",
            "会被煮得沸沸腾腾的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "呼，还真不知道\x01",
            "接下来会发生什么呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EE7")

    label("loc_EA1")


    ChrTalk(    #2
        0x9,
        "源泉的调查就拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "这样下去的话，\x01",
            "我们没法营业了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_EE7")

    TalkEnd(0xFE)
    Return()

    # Function_8_E3C end

    def Function_9_EEB(): pass

    label("Function_9_EEB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F2A")

    ChrTalk(    #4
        0xFE,
        (
            "哟！\x01",
            "使出必杀技了吗？！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "哈哈。\x01",
            "真过瘾。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F80")

    label("loc_F2A")


    ChrTalk(    #6
        0xFE,
        (
            "哈哈。\x01",
            "好像在玩武术大会的游戏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "这个村的孩子们\x01",
            "是在悠闲的环境中成长起来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F80")

    TalkEnd(0xFE)
    Return()

    # Function_9_EEB end

    def Function_10_F84(): pass

    label("Function_10_F84")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1060")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1009")

    ChrTalk(    #8
        0xFE,
        (
            "太好了……\x01",
            "泵好像修好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "不过，其他的导力器\x01",
            "看来还不能动弹。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "中央工房的人现在\x01",
            "也一定很忙吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_105D")

    label("loc_1009")


    ChrTalk(    #11
        0xFE,
        (
            "泵虽然修好了，不过\x01",
            "其他的导力器还是不动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "中央工房的人现在\x01",
            "也一定很忙吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_105D")

    Jump("loc_12E0")

    label("loc_1060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_10B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A4")

    ChrTalk(    #13
        0xFE,
        "水变冷了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "泵的导力器也\x01",
            "停住了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_10B6")

    label("loc_10A4")


    ChrTalk(    #15
        0xFE,
        "水变冷了……\x02",
    )

    CloseMessageWindow()

    label("loc_10B6")

    Jump("loc_12E0")

    label("loc_10B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_114B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10FC")

    ChrTalk(    #16
        0xFE,
        (
            "呼～太好了～\x01",
            "我还在想要是一直\x01",
            "那样该怎么办。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1148")

    label("loc_10FC")


    ChrTalk(    #17
        0xFE,
        "温泉能恢复真是太好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "如果只有热水澡的话\x01",
            "客人也一定不会来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1148")

    Jump("loc_12E0")

    label("loc_114B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1185")

    ChrTalk(    #19
        0xFE,
        "开水咕噜咕噜地响着。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "还、还有这种事。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E0")

    label("loc_1185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_121E")
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11CC")

    ChrTalk(    #21
        0xFE,
        "还没完呢！\x02",
    )

    CloseMessageWindow()
    OP_43(0xFE, 0x2, 0x0, 0x6)
    OP_95(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x7D0)
    Jump("loc_1213")

    label("loc_11CC")


    ChrTalk(    #22
        0xFE,
        "接招吧！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "剑技·八叶灭杀！！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    OP_43(0xFE, 0x2, 0x0, 0x6)
    OP_95(0xFE, 0x0, 0x3E8, 0x0, 0x7D0, 0x7D0)

    label("loc_1213")

    OP_4B(0x10, 255)
    OP_4B(0x11, 255)
    Jump("loc_12E0")

    label("loc_121E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_12E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_127D")

    ChrTalk(    #24
        0xFE,
        (
            "竟然能获得大赛冠军，\x01",
            "游击士真了不起啊～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "好～接下来我来\x01",
            "扮演游击士。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E0")

    label("loc_127D")


    ChrTalk(    #26
        0xFE,
        (
            "诞辰庆典时的利贝尔通讯上\x01",
            "登了武术大赛的内容！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "说游击士队获得了冠军。\x01",
            "游击士果然强啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_12E0")

    TalkEnd(0x10)
    Return()

    # Function_10_F84 end

    def Function_11_12E4(): pass

    label("Function_11_12E4")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1333")

    ChrTalk(    #28
        0xFE,
        (
            "嘿嘿，亚尔摩果然\x01",
            "离不开温泉啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "只有这个\x01",
            "真是无可替代。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1525")

    label("loc_1333")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_137C")

    ChrTalk(    #30
        0xFE,
        (
            "上回是沸腾，\x01",
            "这次又变冷了吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "……这温泉真任性啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1525")

    label("loc_137C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_140B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_13C2")

    ChrTalk(    #32
        0xFE,
        (
            "游击士果然了不起啊。\x01",
            "这武术大赛冠军可不是盖的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1408")

    label("loc_13C2")


    ChrTalk(    #33
        0xFE,
        (
            "好像这次游击士\x01",
            "也为我们解决了问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "嘿嘿，果然了不起啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1408")

    Jump("loc_1525")

    label("loc_140B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1450")

    ChrTalk(    #35
        0xFE,
        (
            "这、这样下去\x01",
            "就没法做温泉蛋了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "很快就煮凝固了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1525")

    label("loc_1450")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_14D3")
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1498")

    ChrTalk(    #37
        0xFE,
        (
            "接下来是分身战技！\x01",
            "哼哼，你能看穿吗～～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C8")

    label("loc_1498")


    ChrTalk(    #38
        0xFE,
        (
            "接招，机枪速射！！\x01",
            "哒哒哒哒哒哒～～～！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_14C8")

    OP_4B(0x10, 255)
    OP_4B(0x11, 255)
    Jump("loc_1525")

    label("loc_14D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1525")

    ChrTalk(    #39
        0xFE,
        (
            "嘿嘿，游击士是好，不过\x01",
            "特务部队也很酷哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "反派角色也别有风味啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1525")

    TalkEnd(0x11)
    Return()

    # Function_11_12E4 end

    def Function_12_1529(): pass

    label("Function_12_1529")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1651")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_157C")

    ChrTalk(    #41
        0xFE,
        "这、这是爆炸性新闻！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "得、得赶快准备\x01",
            "照相机来摄影……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_164E")

    label("loc_157C")


    ChrTalk(    #43
        0xFE,
        "这、这是爆炸性新闻！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "得、得赶快准备\x01",
            "照相机来摄影……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "不、不，你等等\x01",
            "应该先记录情况吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "呼～冷静一点～～\x01",
            "冷静地考虑问题～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "嗯、嗯……\x01",
            "还是应该先拍照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "好、好……\x01",
            "总、总之先拍！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_164E")

    Jump("loc_1775")

    label("loc_1651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1775")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_16C6")

    ChrTalk(    #49
        0xFE,
        (
            "每次来这个村庄都能感到\x01",
            "其东方风格设计的妙趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "哈哈，有机会的话也想\x01",
            "放下工作来享受一下啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1775")

    label("loc_16C6")


    ChrTalk(    #51
        0xFE,
        (
            "我是负责利贝尔通讯\x01",
            "文化栏的记者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "每次来这个村庄都能感到\x01",
            "其东方风格设计的妙趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "我以前也写过\x01",
            "这里的旅馆……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "不过这次是准备为了饮食和\x01",
            "体育来这里采访的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1775")

    TalkEnd(0x12)
    Return()

    # Function_12_1529 end

    def Function_13_1779(): pass

    label("Function_13_1779")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_184D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1802")

    ChrTalk(    #55
        0xFE,
        (
            "呼，看来泵\x01",
            "开始动了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "不过我记得这里的设备也\x01",
            "应该是导力驱动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "……到底是\x01",
            "怎么让它动起来的呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_184A")

    label("loc_1802")


    ChrTalk(    #58
        0xFE,
        (
            "这里的泵也\x01",
            "应该是导力驱动的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "呼，那么是怎样\x01",
            "让它动起来的呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_184A")

    Jump("loc_1966")

    label("loc_184D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1966")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1924")

    ChrTalk(    #60
        0xFE,
        (
            "我们是从沃尔费堡垒\x01",
            "被派遣来的巡逻部队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "总之现在亚尔摩村\x01",
            "还保持着平静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "虽然很遗憾，温泉的泵也\x01",
            "好像停下来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "不过好在是不影响日常生活的设施。\x01",
            "就算保持那样也没什么问题吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1966")

    label("loc_1924")


    ChrTalk(    #64
        0xFE,
        (
            "温泉的泵也\x01",
            "好像停下来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "这也是那个\x01",
            "停止现象造成的吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1966")

    TalkEnd(0xFE)
    Return()

    # Function_13_1779 end

    def Function_14_196A(): pass

    label("Function_14_196A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1A5C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0B")

    ChrTalk(    #66
        0xFE,
        (
            "副队长也感到奇怪，\x01",
            "为什么泵会动了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "如果能让那个动起来，真\x01",
            "希望能让我们的枪恢复正常啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "因为不能使用枪\x01",
            "是很令人不安的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1A59")

    label("loc_1A0B")


    ChrTalk(    #69
        0xFE,
        (
            "因为不能使用枪\x01",
            "是很令人不安的\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "不过在市民面前\x01",
            "不能露出半点这种情绪。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A59")

    Jump("loc_1B73")

    label("loc_1A5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1B73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B15")

    ChrTalk(    #71
        0xFE,
        (
            "我们是从雷斯顿要塞\x01",
            "被派遣来的增援部队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "现在在和沃尔费堡垒的副队长\x01",
            "一起在村里巡逻。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "亚尔摩村比我们\x01",
            "想象的要安定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "不愧是一直\x01",
            "都很平静的地方啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1B73")

    label("loc_1B15")


    ChrTalk(    #75
        0xFE,
        (
            "我们是从雷斯顿要塞\x01",
            "被派遣来的增援部队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "现在在和沃尔费堡垒的副队长\x01",
            "一起在村里巡逻。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B73")

    TalkEnd(0xFE)
    Return()

    # Function_14_196A end

    def Function_15_1B77(): pass

    label("Function_15_1B77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1BD4")

    ChrTalk(    #77
        0xFE,
        (
            "水泵小屋的修理\x01",
            "好像结束了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "这种时候还要到处跑，\x01",
            "游击士真不容易啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C73")

    label("loc_1BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C3C")

    ChrTalk(    #79
        0xFE,
        "前边是源泉所在的后山哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "因为是个危险的地方，\x01",
            "慎重起见，还是警戒起来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_1C73")

    label("loc_1C3C")


    ChrTalk(    #81
        0xFE,
        (
            "前边是源泉所在的后山哦。\x01",
            "是个危险的地方，请小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C73")

    TalkEnd(0xFE)
    Return()

    # Function_15_1B77 end

    def Function_16_1C77(): pass

    label("Function_16_1C77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1D29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CDF")

    ChrTalk(    #82
        0xFE,
        (
            "我是来看看澡堂的，\x01",
            "泵好像真的修好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "好～这样一来\x01",
            "一定能恢复营业了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_1D29")

    label("loc_1CDF")


    ChrTalk(    #84
        0xFE,
        (
            "我们是打工的，\x01",
            "所以客人少的话会很危险哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "真希望客人\x01",
            "快点回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D29")

    TalkEnd(0xFE)
    Return()

    # Function_16_1C77 end

    def Function_17_1D2D(): pass

    label("Function_17_1D2D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D4E")
    Call(0, 34)
    Call(0, 35)

    label("loc_1D4E")

    SetChrPos(0x101, -23960, -2000, 14980, 90)
    SetChrPos(0x107, -23740, -2000, 16230, 90)
    SetChrPos(0xF7, -25260, -2000, 15090, 90)
    SetChrPos(0xF9, -25290, -2000, 16370, 90)
    SetChrPos(0x8, -6810, -1250, 14740, 270)
    ClearChrFlags(0x8, 0x80)
    OP_6D(-21340, -2000, 15680, 0)
    OP_67(0, 8800, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(45000, 0)
    OP_6E(275, 0)

    def lambda_1DEB():
        OP_6D(-19340, -2000, 15680, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DEB)

    def lambda_1E03():
        OP_8E(0xFE, 0xFFFFB208, 0xFFFFF830, 0x3A84, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1E03)
    Sleep(100)

    def lambda_1E23():
        OP_8E(0xFE, 0xFFFFB2E4, 0xFFFFF830, 0x3F66, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1E23)
    Sleep(100)

    def lambda_1E43():
        OP_8E(0xFE, 0xFFFFACF4, 0xFFFFF830, 0x3AF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_1E43)
    Sleep(100)

    def lambda_1E63():
        OP_8E(0xFE, 0xFFFFACD6, 0xFFFFF830, 0x3FF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_1E63)
    OP_C8(0x80, 0x46, "C_PLAC10._CH", 0x1, 0x7D0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x107, 0x0)

    NpcTalk(    #86
        0x8,
        "老婆婆的声音",
        "#3P哟，你们来了啊。\x02",
    )

    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF9, 0x0)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FC0")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇已经和毛婆婆重逢】\x01",      # 0
            "【◇尚未和毛婆婆重逢】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1FAB"),
        (1, "loc_1FB1"),
        (SWITCH_DEFAULT, "loc_1FB7"),
    )


    label("loc_1FAB")

    OP_A2(0x1482)
    Jump("loc_1FB7")

    label("loc_1FB1")

    OP_A3(0x1482)
    Jump("loc_1FB7")

    label("loc_1FB7")

    FadeToBright(300, 0)

    label("loc_1FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E5")

    ChrTalk(    #87
        0x101,
        "#1004F#6P……毛婆婆！？\x02",
    )

    CloseMessageWindow()

    def lambda_1FEB():
        OP_6D(-11110, -2000, 15260, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_1FEB)
    WaitChrThread(0x0, 0x0)

    def lambda_2008():
        OP_6D(-12380, -2000, 15930, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2008)

    def lambda_2020():
        OP_67(0, 12500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2020)

    def lambda_2038():
        OP_6B(2590, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2038)

    def lambda_2048():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2048)

    def lambda_2058():
        OP_8E(0x8, 0xFFFFD364, 0xFFFFF830, 0x3CA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2058)

    def lambda_2073():
        OP_8E(0xFE, 0xFFFFCD60, 0xFFFFF830, 0x3A84, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2073)
    Sleep(100)

    def lambda_2093():
        OP_8E(0xFE, 0xFFFFCE3C, 0xFFFFF830, 0x3F66, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2093)
    Sleep(100)

    def lambda_20B3():
        OP_8E(0xFE, 0xFFFFC84C, 0xFFFFF830, 0x3AF2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_20B3)
    Sleep(100)

    def lambda_20D3():
        OP_8E(0xFE, 0xFFFFC82E, 0xFFFFF830, 0x3FF2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_20D3)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #88
        0x8,
        (
            "#680F哟，艾丝蒂尔，好久不见。\x02\x03",

            "与以前来的时候相比\x01",
            "一下子变得更像大人了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1016F#6P嘿嘿……是吗。\x02\x03",

            "#1025F那个，其实我们过来\x01",
            "是有事情要办的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x8,
        (
            "#682F嗯，工房长刚才\x01",
            "就已经联系过我了。\x02\x03",

            "好像是蔡斯的很多地方\x01",
            "都发生了奇怪的地震是吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_236F")

    label("loc_21E5")


    ChrTalk(    #91
        0x107,
        "#560F#6P 毛婆婆！\x02",
    )

    CloseMessageWindow()

    def lambda_2202():
        OP_6D(-11110, -2000, 15260, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_2202)
    WaitChrThread(0x0, 0x0)

    def lambda_221F():
        OP_6D(-12380, -2000, 15930, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_221F)

    def lambda_2237():
        OP_67(0, 12500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2237)

    def lambda_224F():
        OP_6B(2590, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_224F)

    def lambda_225F():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_225F)

    def lambda_226F():
        OP_8E(0x8, 0xFFFFD364, 0xFFFFF830, 0x3CA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_226F)

    def lambda_228A():
        OP_8E(0xFE, 0xFFFFCD60, 0xFFFFF830, 0x3A84, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_228A)
    Sleep(100)

    def lambda_22AA():
        OP_8E(0xFE, 0xFFFFCE3C, 0xFFFFF830, 0x3F66, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_22AA)
    Sleep(100)

    def lambda_22CA():
        OP_8E(0xFE, 0xFFFFC84C, 0xFFFFF830, 0x3AF2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_22CA)
    Sleep(100)

    def lambda_22EA():
        OP_8E(0xFE, 0xFFFFC82E, 0xFFFFF830, 0x3FF2, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_22EA)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #92
        0x8,
        (
            "#680F哟，提妲、艾丝蒂尔。\x02\x03",

            "刚才工房长\x01",
            "很快就联系我了。\x02\x03",

            "好像是蔡斯的很多地方\x01",
            "都发生了奇怪的地震是吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_236F")


    ChrTalk(    #93
        0x101,
        (
            "#1007F#6P是吗……\x01",
            "嗯，那话说起来就方便了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        (
            "#682F其实就在刚才，我们\x01",
            "这边也发生了奇怪的事。\x02\x03",

            "正准备要联系你们\x01",
            "游击士协会呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x107,
        "#064F#6P呜哎……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1005F#6P莫非，是地震！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        (
            "#685F不巧，倒不是地震……\x02\x03",

            "#682F百闻不如一见。\x01",
            "好了，你们亲自去确认一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)

    def lambda_248B():
        OP_90(0x8, 0x4E20, 0x0, 0xFFFFFF38, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_248B)

    def lambda_24A6():
        OP_6D(17080, 2500, 17170, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24A6)

    def lambda_24BE():
        OP_67(0, 8820, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_24BE)

    def lambda_24D6():
        OP_6B(3120, 11000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_24D6)

    def lambda_24E6():
        OP_6C(57000, 11000)
        ExitThread()

    QueueWorkItem(0x107, 3, lambda_24E6)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(100)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    def lambda_2524():
        OP_90(0xFE, 0x4E20, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2524)
    Sleep(200)

    def lambda_2544():
        OP_90(0xFE, 0x4E20, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2544)
    Sleep(100)

    def lambda_2564():
        OP_90(0xFE, 0x4E20, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2564)
    Sleep(100)

    def lambda_2584():
        OP_90(0xFE, 0x4E20, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2584)
    WaitChrThread(0x101, 0x2)
    OP_44(0x8, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF9, 0x1)
    OP_8C(0x101, 90, 0)
    OP_8C(0x107, 90, 0)
    OP_8C(0xF7, 90, 0)
    OP_8C(0xF9, 90, 0)

    def lambda_25D4():
        OP_8E(0xFE, 0x35AC, 0x9C4, 0x3E4E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_25D4)

    def lambda_25EF():
        OP_8F(0xFE, 0x36BA, 0x9C4, 0x40BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_25EF)

    def lambda_260A():
        OP_8F(0xFE, 0x366A, 0x9C4, 0x4538, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_260A)

    def lambda_2625():
        OP_8F(0xFE, 0x32A0, 0x9C4, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2625)

    def lambda_2640():
        OP_8F(0xFE, 0x3278, 0x9C4, 0x418C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2640)
    WaitChrThread(0x8, 0x1)

    def lambda_2660():
        OP_8C(0xFE, 275, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2660)

    def lambda_266E():
        OP_8E(0xFE, 0x35CA, 0x9C4, 0x38D6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_266E)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 0, 400)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF9, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #98
        0x101,
        "#1020F#5P这、这是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x107,
        "#065F#5P沸腾起来了……\x02",
    )

    CloseMessageWindow()

    def lambda_2748():
        OP_6D(15000, 2500, 16149, 1300)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2748)

    def lambda_2760():
        OP_67(0, 8500, -10000, 1300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2760)

    def lambda_2778():
        OP_6B(2870, 1300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2778)

    def lambda_2788():
        OP_8C(0x107, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2788)

    def lambda_2796():
        OP_8C(0xF7, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2796)
    OP_8C(0x101, 180, 400)
    OP_8C(0xF9, 180, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_27E0")

    ChrTalk(    #100
        0x106,
        "#057F到底是怎么回事？\x02",
    )

    CloseMessageWindow()
    Jump("loc_27FD")

    label("loc_27E0")


    ChrTalk(    #101
        0x103,
        "#022F这到底是怎么回事？\x02",
    )

    CloseMessageWindow()

    label("loc_27FD")


    ChrTalk(    #102
        0x8,
        (
            "#685F原因我也不清楚……\x02\x03",

            "#682F在接到工房长先生的联络之前不久，\x01",
            "外面突然变得很嘈杂。\x02\x03",

            "我就出来看了个究竟，\x01",
            "结果就发现已经变成这样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x107,
        (
            "#065F莫、莫非是\x01",
            "泵装置坏掉了？\x02\x03",

            "比如说发热系统出了故障……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        (
            "#682F不，我刚才去看了，\x01",
            "正常得和平时没两样。\x02\x03",

            "大概是源泉的温度\x01",
            "一下子变高了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#1015F#5P这不是很少见吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "#685F我迁居这里已经５０年了，\x01",
            "不过碰到这么奇怪的事还是第一次。\x02\x03",

            "#682F总觉得有一种不祥的预感。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A10")

    ChrTalk(    #107
        0x104,
        (
            "#035F呼，说不定和那些\x01",
            "地震有关系。\x02\x03",

            "#030F比如说七耀脉的活性化──使得\x01",
            "源泉的温度上升了之类的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A74")

    label("loc_2A10")


    ChrTalk(    #108
        0x105,
        (
            "#047F……这可能和那些\x01",
            "地震有关系。\x02\x03",

            "#042F比如说七耀脉的活性化──使得\x01",
            "源泉的温度上升了之类的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A74")


    ChrTalk(    #109
        0x107,
        (
            "#065F我、我觉得\x01",
            "很有可能。\x02\x03",

            "如果温度再这么继续上升的话\x01",
            "问题可能就严重了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#1005F#5P这……不是很麻烦么……\x01",
            "必须马上查找到原因！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2B43")

    ChrTalk(    #111
        0x106,
        (
            "#050F喂，婆婆。\x01",
            "源泉在哪里？\x02\x03",

            "我们可以去确认一下吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B7F")

    label("loc_2B43")


    ChrTalk(    #112
        0x103,
        (
            "#020F我说，婆婆。\x01",
            "源泉在哪里？\x02\x03",

            "我们可以去确认一下吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B7F")


    ChrTalk(    #113
        0x8,
        (
            "#680F我就知道你们会这么想，\x01",
            "所以早就准备好了这个。\x02\x03",

            "#681F好，收下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3692, 0x9C4, 0x3DB8, 0x7D0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #114
        "\x1F\xF5\x03\x07\x00收下了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F5, 1)
    OP_8F(0x8, 0x35CA, 0x9C4, 0x3BC4, 0x3E8, 0x0)

    ChrTalk(    #115
        0x101,
        "#1004F#5P这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "#680F#4P这是在水泵小屋左手边的\x01",
            "栅门钥匙。\x02\x03",

            "里面就是亚尔摩温泉\x01",
            "源泉涌出的洞窟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        "#1018F#5P真的！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x107,
        "#560F还有那样的洞窟啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2CFE")

    ChrTalk(    #119
        0x106,
        "#051F嘿嘿，多谢帮忙了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D1F")

    label("loc_2CFE")


    ChrTalk(    #120
        0x103,
        "#021F呵呵，真是帮了我们了。\x02",
    )

    CloseMessageWindow()

    label("loc_2D1F")


    ChrTalk(    #121
        0x8,
        (
            "#681F#4P哪里的话。\x01",
            "是我们在请求你们帮忙啊。\x02\x03",

            "#680F沸腾得这么厉害，\x01",
            "很快就会没客人来了。\x01",
            "而且也不能打扫卫生。\x02\x03",

            "总之，就拜托你们在调查地震之余，\x01",
            "也把这件事情解决吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        "#1006F#5P嗯，交给我们吧！\x02",
    )

    CloseMessageWindow()
    OP_A3(0x0)
    OP_8C(0x8, 180, 400)
    OP_43(0x8, 0x1, 0x0, 0x12)

    def lambda_2DFE():
        OP_6D(18120, 2000, 11950, 3000)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2DFE)

    def lambda_2E16():
        OP_67(0, 8820, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2E16)

    def lambda_2E2E():
        OP_6C(90000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2E2E)
    Sleep(1000)

    def lambda_2E43():

        label("loc_2E43")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2E43")

    QueueWorkItem2(0x101, 2, lambda_2E43)
    Sleep(200)

    def lambda_2E59():

        label("loc_2E59")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2E59")

    QueueWorkItem2(0x107, 2, lambda_2E59)
    Sleep(200)

    def lambda_2E6F():

        label("loc_2E6F")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2E6F")

    QueueWorkItem2(0xF7, 2, lambda_2E6F)
    Sleep(200)

    def lambda_2E85():

        label("loc_2E85")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2E85")

    QueueWorkItem2(0xF9, 2, lambda_2E85)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x8, 0x1)
    WaitChrThread(0x8, 0x2)
    WaitChrThread(0x8, 0x3)
    OP_44(0x101, 0x2)
    OP_44(0x107, 0x2)
    OP_44(0xF7, 0x2)
    OP_44(0xF9, 0x2)

    def lambda_2EBA():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EBA)
    Sleep(100)

    def lambda_2ECD():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2ECD)
    Sleep(100)

    def lambda_2EE0():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2EE0)
    Sleep(100)

    def lambda_2EF3():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2EF3)

    def lambda_2F01():
        OP_6D(13550, 2500, 16850, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F01)

    def lambda_2F19():
        OP_6C(85000, 2000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_2F19)
    Sleep(1000)

    def lambda_2F2E():
        OP_8C(0x101, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F2E)
    Sleep(50)

    def lambda_2F41():
        OP_8C(0xF7, 45, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2F41)
    Sleep(50)

    def lambda_2F54():
        OP_8C(0x107, 225, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2F54)
    Sleep(50)
    OP_8C(0xF9, 120, 400)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FE1")

    ChrTalk(    #123
        0x104,
        (
            "#035F源泉涌出的洞窟吗，\x01",
            "有可能就是地震的震源地啊……\x02\x03",

            "#030F呼，进去之前应该\x01",
            "要做好万全的准备。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3043")

    label("loc_2FE1")


    ChrTalk(    #124
        0x105,
        (
            "#047F源泉涌出的洞窟吗，\x01",
            "有可能就是地震的震源地啊……\x02\x03",

            "#042F进去之前应该\x01",
            "先做好充分的准备哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3043")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_308F")

    ChrTalk(    #125
        0x106,
        (
            "#057F#4P嗯……\x01",
            "十有八九，敌人就在里面。\x02\x03",

            "#057F打起精神来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30CC")

    label("loc_308F")


    ChrTalk(    #126
        0x103,
        (
            "#022F#4P嗯……\x01",
            "十有八九，敌人就在里面。\x02\x03",

            "打起精神来吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30CC")

    OP_A2(0x1421)
    OP_28(0x88, 0x1, 0x2)
    OP_28(0x88, 0x1, 0x4)
    EventEnd(0x0)
    Return()

    # Function_17_1D2D end

    def Function_18_30DE(): pass

    label("Function_18_30DE")

    OP_8E(0xFE, 0x357A, 0x9C4, 0x357A, 0x7D0, 0x0)
    OP_A2(0x0)
    OP_8E(0xFE, 0x3E30, 0x9C4, 0x3502, 0x7D0, 0x0)
    OP_8E(0xFE, 0x4D62, 0x7D0, 0x1C7A, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_30DE end

    def Function_19_3123(): pass

    label("Function_19_3123")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3137")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_19_3123")

    label("loc_3137")

    Sleep(500)
    OP_8E(0xFE, 0x3796, 0x9C4, 0x35A2, 0x6A4, 0x0)
    OP_8E(0xFE, 0x3E80, 0x9C4, 0x3552, 0x6A4, 0x0)
    OP_8E(0xFE, 0x3DD6, 0x7D0, 0x212A, 0x6A4, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_3123 end

    def Function_20_317E(): pass

    label("Function_20_317E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3192")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_20_317E")

    label("loc_3192")

    OP_8E(0xFE, 0x3796, 0x9C4, 0x35A2, 0x6A4, 0x0)
    OP_8E(0xFE, 0x3E80, 0x9C4, 0x3552, 0x6A4, 0x0)
    OP_8E(0xFE, 0x3DD6, 0x7D0, 0x212A, 0x6A4, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_20_317E end

    def Function_21_31D4(): pass

    label("Function_21_31D4")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #127
        "\x07\x05栅门锁着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 1)), scpexpr(EXPR_END)), "loc_3398")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用钥匙】\x01",      # 0
            "【不使用】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3392")
    EventBegin(0x0)
    Fade(1000)
    LoadEffect(0x1, "map\\\\t32key00.eff")
    OP_6D(40670, 6000, 49640, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 40430, 6000, 48600, 360)
    SetChrPos(0x107, 40580, 6000, 47300, 360)
    SetChrPos(0xF7, 39450, 6000, 48600, 360)
    SetChrPos(0xF9, 39490, 6000, 47300, 360)
    OP_0D()
    OP_22(0x73, 0x0, 0x64)
    OP_72(0xB, 0x800)
    OP_6F(0xB, 1)
    PlayEffect(0x1, 0x0, 0xFF, 40000, 6500, 50100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x10C, 0x0, 0x64)
    OP_B0(0xB, 0x1A)
    OP_6F(0xB, 1)
    OP_70(0xB, 0xA)
    OP_73(0xB)
    Sleep(1000)
    OP_6F(0xB, 10)
    OP_70(0xB, 0x46)
    OP_73(0xB)
    OP_6F(0xB, 120)
    OP_64(0x0, 0x1)
    OP_A2(0x1422)
    EventEnd(0x0)
    Jump("loc_3395")

    label("loc_3392")

    TalkEnd(0xFF)

    label("loc_3395")

    Jump("loc_33A4")

    label("loc_3398")

    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_33A4")

    Return()

    # Function_21_31D4 end

    def Function_22_33A5(): pass

    label("Function_22_33A5")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #128
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F3")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_33F3")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用水泵小屋的钥匙】\x01",      # 0
            "【不使用】\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_345E")
    OP_A2(0x2008)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_64(0x1, 0x1)
    OP_71(0x3, 0x10)
    Jump("loc_345E")

    label("loc_345E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_22_33A5 end

    def Function_23_346B(): pass

    label("Function_23_346B")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(17090, 2500, 16680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_22(0xE3, 0x0, 0x64)
    Sleep(500)
    PlayEffect(0x8E, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x8D, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_355E():
        OP_6D(17090, 2500, 16680, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_355E)

    def lambda_3576():
        OP_67(0, 8130, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3576)

    def lambda_358E():
        OP_6C(76000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_358E)
    OP_43(0x10, 0x1, 0x0, 0x18)
    OP_43(0x11, 0x1, 0x0, 0x19)
    OP_43(0xB, 0x1, 0x0, 0x1A)
    OP_43(0xC, 0x1, 0x0, 0x1B)
    OP_43(0x1D, 0x1, 0x0, 0x1C)
    OP_43(0x1E, 0x1, 0x0, 0x1D)
    OP_43(0x1F, 0x1, 0x0, 0x1E)
    OP_43(0x20, 0x1, 0x0, 0x1F)
    OP_43(0x21, 0x1, 0x0, 0x20)
    OP_43(0x22, 0x1, 0x0, 0x21)
    Sleep(8000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(70100, 1000, 24730, 0)
    OP_67(0, 7650, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(32000, 0)
    OP_6E(285, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_22(0xE3, 0x0, 0x64)
    Sleep(500)
    PlayEffect(0x8F, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T3221   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_23_346B end

    def Function_24_3705(): pass

    label("Function_24_3705")

    SetChrPos(0xFE, 6370, 1250, 16280, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x27EC, 0x7D0, 0x3F7A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x37AA, 0x9C4, 0x4628, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(800)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_24_3705 end

    def Function_25_3762(): pass

    label("Function_25_3762")

    Sleep(500)
    SetChrPos(0xFE, 6330, 1250, 15290, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x2526, 0x7D0, 0x3ADE, 0xBB8, 0x0)
    OP_8E(0xFE, 0x37A0, 0x9C4, 0x43B2, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(800)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_25_3762 end

    def Function_26_37C4(): pass

    label("Function_26_37C4")

    Sleep(2500)
    SetChrPos(0xFE, 18640, 2000, 9920, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4736, 0x9C4, 0x3598, 0xBB8, 0x0)
    Sleep(800)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_26_37C4 end

    def Function_27_380B(): pass

    label("Function_27_380B")

    Sleep(3000)
    SetChrPos(0xFE, 14660, 2000, 26670, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x398A, 0x7D0, 0x57E4, 0xBB8, 0x0)
    OP_8E(0xFE, 0x4286, 0x7D0, 0x580C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x42D6, 0x9C4, 0x4F1A, 0xBB8, 0x0)
    Sleep(800)
    OP_62(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_27_380B end

    def Function_28_387A(): pass

    label("Function_28_387A")

    Sleep(3000)
    SetChrPos(0xFE, 6540, 1500, 14110, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x2594, 0x7D0, 0x3728, 0x5DC, 0x0)
    OP_8E(0xFE, 0x2E68, 0x7D0, 0x3DF4, 0x5DC, 0x0)
    OP_8E(0xFE, 0x33C2, 0x9C4, 0x3E08, 0x5DC, 0x0)
    Return()

    # Function_28_387A end

    def Function_29_38D2(): pass

    label("Function_29_38D2")

    Sleep(1000)
    SetChrPos(0xFE, 12940, 2000, 8490, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x3412, 0x7D0, 0x2BE8, 0x3E8, 0x0)
    Sleep(800)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Return()

    # Function_29_38D2 end

    def Function_30_391E(): pass

    label("Function_30_391E")

    Sleep(3000)
    SetChrPos(0xFE, 20900, 2000, 8650, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x517C, 0x7D0, 0x2B52, 0x7D0, 0x0)
    OP_8E(0xFE, 0x459C, 0x7D0, 0x2DBE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x3F6F, 0x9C4, 0x3584, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(800)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Return()

    # Function_30_391E end

    def Function_31_3994(): pass

    label("Function_31_3994")

    Sleep(5000)
    SetChrPos(0xFE, 20010, 2000, 6870, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4DD0, 0x7D0, 0x2DFA, 0x7D0, 0x0)
    Return()

    # Function_31_3994 end

    def Function_32_39C4(): pass

    label("Function_32_39C4")

    Sleep(4000)
    SetChrPos(0xFE, 14510, 2000, 9450, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x38AE, 0x7D0, 0x2E68, 0x7D0, 0x0)
    Return()

    # Function_32_39C4 end

    def Function_33_39F4(): pass

    label("Function_33_39F4")

    Sleep(4000)
    OP_72(0x2, 0x10)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x1D)
    OP_73(0x2)
    SetChrPos(0xFE, 21250, 2500, 25000, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x50DC, 0x7D0, 0x565E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x497A, 0x7D0, 0x5636, 0x7D0, 0x0)
    OP_8E(0xFE, 0x47AE, 0x9C4, 0x515E, 0x7D0, 0x0)
    Return()

    # Function_33_39F4 end

    def Function_34_3A67(): pass

    label("Function_34_3A67")

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
        (0, "loc_3AE1"),
        (1, "loc_3AE7"),
        (SWITCH_DEFAULT, "loc_3AED"),
    )


    label("loc_3AE1")

    OP_A2(0x1200)
    Jump("loc_3AED")

    label("loc_3AE7")

    OP_A2(0x1201)
    Jump("loc_3AED")

    label("loc_3AED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3AFB")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3AFF")

    label("loc_3AFB")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3AFF")

    Return()

    # Function_34_3A67 end

    def Function_35_3B00(): pass

    label("Function_35_3B00")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3B3A")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_3B54")

    label("loc_3B3A")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_3B54")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_35_3B00 end

    def Function_36_3B66(): pass

    label("Function_36_3B66")

    EventBegin(0x1)

    ChrTalk(    #129
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_3B92():
        OP_6D(48400, 0, 3440, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3B92)

    def lambda_3BAA():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_3BAA)

    def lambda_3BC2():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3BC2)

    def lambda_3BD2():
        OP_6C(135000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_3BD2)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #130
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C59")
    OP_C0(0xE, 0x22, 0xCF58, 0x0, 0x1126, 0x10E, 0xBE28, 0x0, 0x9A6)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_3C68")

    label("loc_3C59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3C68")
    EventEnd(0x1)

    label("loc_3C68")

    Return()

    # Function_36_3B66 end

    def Function_37_3C69(): pass

    label("Function_37_3C69")

    SetPlaceName(0x88)
    Return()

    # Function_37_3C69 end

    def Function_38_3C6D(): pass

    label("Function_38_3C6D")

    SetPlaceName(0x87)
    Return()

    # Function_38_3C6D end

    def Function_39_3C71(): pass

    label("Function_39_3C71")

    SetPlaceName(0x89)
    Return()

    # Function_39_3C71 end

    SaveToFile()

Try(main)
