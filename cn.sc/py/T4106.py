from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4106   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4106.x',
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
        '接待员菲丝',                           # 9
        '卡鲁尼洛',                             # 10
        '蒂法露',                               # 11
        '修理员佩顿',                           # 12
        '鲁特尔',                               # 13
        '阿尔丹',                               # 14
        '安敦',                                 # 15
        '利库斯',                               # 16
        '基蒂',                                 # 17
        '村中的老年男性',                       # 18
        '村中的老年女性',                       # 19
        '村中的中年男性',                       # 20
        '村中的中年女性',                       # 21
        '村中的青年男性',                       # 22
        '村中的青年女性',                       # 23
        '奥利维尔',                             # 24
        '科洛丝',                               # 25
        '提妲',                                 # 26
        '金',                                   # 27
        '穆拉',                                 # 28
        '玲',                                   # 29
        '奈尔',                                 # 30
        '朵洛希',                               # 31
        '格雷特纳号的影子',                     # 32
        '格雷特纳号',                           # 33
        '雪拉扎德',                             # 34
        '阿加特',                               # 35
        '凯文神父',                             # 36
        '王都格兰赛尔·东街区',                 # 37
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
        TalkScenaIndex      = 4,
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
        X                   = 62500,
        Z                   = -3000,
        Y                   = 169170,
        Direction           = 76,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        TalkScenaIndex      = 10,
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
        TalkScenaIndex      = 11,
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
        NpcIndex            = 0x189,
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
        NpcIndex            = 0x189,
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
        X                   = 73400,
        Y                   = 0,
        Z                   = 140700,
        Range               = 76300,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x23730,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
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
        TalkFunctionIndex   = 33,
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
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_5A6",          # 00, 0
        "Function_1_721",          # 01, 1
        "Function_2_7C1",          # 02, 2
        "Function_3_7D7",          # 03, 3
        "Function_4_7DC",          # 04, 4
        "Function_5_9D7",          # 05, 5
        "Function_6_BF6",          # 06, 6
        "Function_7_EB6",          # 07, 7
        "Function_8_EBD",          # 08, 8
        "Function_9_10D5",         # 09, 9
        "Function_10_1443",        # 0A, 10
        "Function_11_144A",        # 0B, 11
        "Function_12_1451",        # 0C, 12
        "Function_13_1458",        # 0D, 13
        "Function_14_1AAD",        # 0E, 14
        "Function_15_1B0A",        # 0F, 15
        "Function_16_1B69",        # 10, 16
        "Function_17_1BDC",        # 11, 17
        "Function_18_1C4F",        # 12, 18
        "Function_19_1CC2",        # 13, 19
        "Function_20_1D35",        # 14, 20
        "Function_21_1D94",        # 15, 21
        "Function_22_208B",        # 16, 22
        "Function_23_2ED2",        # 17, 23
        "Function_24_315A",        # 18, 24
        "Function_25_37FC",        # 19, 25
        "Function_26_4449",        # 1A, 26
        "Function_27_44D2",        # 1B, 27
        "Function_28_44EE",        # 1C, 28
        "Function_29_45A1",        # 1D, 29
        "Function_30_4628",        # 1E, 30
        "Function_31_46A1",        # 1F, 31
        "Function_32_4726",        # 20, 32
        "Function_33_4741",        # 21, 33
        "Function_34_47EE",        # 22, 34
    )


    def Function_0_5A6(): pass

    label("Function_0_5A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5BF")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_65D")

    label("loc_5BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_608")
    SetChrPos(0x9, 81810, 1500, 142750, 183)
    SetChrPos(0xA, 72490, -10000, 161070, 110)
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_605")
    SetChrPos(0xD, 57130, 250, 138200, 135)

    label("loc_605")

    Jump("loc_65D")

    label("loc_608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_63D")
    SetChrPos(0x9, 81810, 1500, 142750, 183)
    SetChrPos(0xA, 53400, 250, 145320, 183)
    SetChrFlags(0xB, 0x80)
    Jump("loc_65D")

    label("loc_63D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_64C")
    SetChrFlags(0xB, 0x80)
    Jump("loc_65D")

    label("loc_64C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_65D")
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xB, 0x80)

    label("loc_65D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_685")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_B1("T4106_4")
    Event(0, 24)
    Jump("loc_6CB")

    label("loc_685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_6AD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    OP_B1("T4106_4")
    Event(0, 25)
    Jump("loc_6CB")

    label("loc_6AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CB")
    SetMapFlags(0x10000000)
    OP_B1("T4106_1")
    Event(0, 13)

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_720")
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x40)
    SetChrPos(0x17, 81740, 1500, 143050, 90)
    SetChrPos(0x1B, 83170, 1500, 143050, 270)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x1B, 0x0, 0x0, 0x2)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)

    label("loc_720")

    Return()

    # Function_0_5A6 end

    def Function_1_721(): pass

    label("Function_1_721")

    OP_16(0x2, 0xFA0, 0xFFFF5808, 0x7148, 0x23005F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74B")
    OP_B1("T4106_4")
    Jump("loc_7C0")

    label("loc_74B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_781")
    OP_B1("T4106_2")
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    OP_72(0xC, 0x4)
    OP_72(0xD, 0x4)
    OP_71(0x9, 0x4)
    Jump("loc_7C0")

    label("loc_781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A1")
    OP_B1("T4106_6")
    Jump("loc_7C0")

    label("loc_7A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_7C0")
    OP_B1("T4106_1")
    OP_71(0x5, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)

    label("loc_7C0")

    Return()

    # Function_1_721 end

    def Function_2_7C1(): pass

    label("Function_2_7C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_7C1")

    label("loc_7D6")

    Return()

    # Function_2_7C1 end

    def Function_3_7D7(): pass

    label("Function_3_7D7")

    Call(0, 4)
    Return()

    # Function_3_7D7 end

    def Function_4_7DC(): pass

    label("Function_4_7DC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_841")

    ChrTalk(    #0
        0x8,
        (
            "当前由于导力全部停止工作\x01",
            "飞船无法运行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "退票工作\x01",
            "在这边受理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "非常抱歉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D3")

    label("loc_841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_84B")
    Jump("loc_9D3")

    label("loc_84B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_8E8")

    ChrTalk(    #3
        0x8,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_8BE")

    ChrTalk(    #4
        0x8,
        (
            "由东边绕行的定期船，\x01",
            "林德号马上就要起飞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "请准备搭乘的客人\x01",
            "抓紧时间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8E5")

    label("loc_8BE")


    ChrTalk(    #6
        0x8,
        (
            "由东边绕行的定期船，\x01",
            "林德号到达。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E5")

    Jump("loc_9D3")

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_937")

    ChrTalk(    #7
        0x8,
        (
            "真对不起，本日的定期船\x01",
            "航行全部结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "欢迎下次光临。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D3")

    label("loc_937")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_972")

    ChrTalk(    #9
        0x8,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "需要买票的乘客\x01",
            "请到这边来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D3")

    label("loc_972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_9D3")

    ChrTalk(    #11
        0x8,
        (
            "十分感谢您\x01",
            "搭乘定期飞行船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "找公司办理业务的客人，\x01",
            "请到那边的建筑物中的接待点。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D3")

    TalkEnd(0x8)
    Return()

    # Function_4_7DC end

    def Function_5_9D7(): pass

    label("Function_5_9D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A61")

    ChrTalk(    #13
        0xFE,
        (
            "赛希莉亚号和林德号\x01",
            "好像分别停在\x01",
            "柏斯和洛连特\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "这样的话也没办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "只好将错就错\x01",
            "一边进行飞船坪的修整一边等候吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF2")

    label("loc_A61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_ABB")

    ChrTalk(    #16
        0xFE,
        "这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "到修整林德号\x01",
            "的时间了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "蒂法露去哪儿了？\x01",
            "已经走了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF2")

    label("loc_ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_AC5")
    Jump("loc_BF2")

    label("loc_AC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_B00")

    ChrTalk(    #19
        0xFE,
        "这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "蒂法露去哪儿了？\x01",
            "已经走了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF2")

    label("loc_B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B58")

    ChrTalk(    #21
        0xFE,
        "嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "本来是准备\x01",
            "请蒂法露加班来着，\x01",
            "但不太好意思，结果就没说。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF2")

    label("loc_B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_B9B")

    ChrTalk(    #23
        0xFE,
        (
            "哎呀，检、检查表\x01",
            "忘记交了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "得赶快制作才行……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BF2")

    label("loc_B9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_BF2")

    ChrTalk(    #25
        0xFE,
        (
            "哎～蒂法露\x01",
            "接下来的工作是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "啊，对了，导力插头\x01",
            "不是可以拜托订货吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF2")

    TalkEnd(0xFE)
    Return()

    # Function_5_9D7 end

    def Function_6_BF6(): pass

    label("Function_6_BF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C76")

    ChrTalk(    #27
        0xFE,
        (
            "我还以为维修主任\x01",
            "会比平时更惊慌失措呢\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "没想到被逼到绝境时\x01",
            "反而这么冷静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "要是总是这么稳重，\x01",
            "就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB2")

    label("loc_C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_D82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_D1E")

    ChrTalk(    #30
        0xFE,
        (
            "『ＸＧ－０２』\x01",
            "查看了样品引擎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "虽然在佩顿那里\x01",
            "看到过作法，\x01",
            "可是没想到居然能做成那么小……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "嘻嘻，看来，可以对工作起到很好的激励作用哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D7F")

    label("loc_D1E")


    ChrTalk(    #33
        0xFE,
        "对不起，能不扰乱我吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "已经决定\x01",
            "立即使用这边的航道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "必须得开始对各处的检查了…\x02",
    )

    CloseMessageWindow()

    label("loc_D7F")

    Jump("loc_EB2")

    label("loc_D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DDB")

    ChrTalk(    #36
        0xFE,
        "今天的工作结束了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "好了，要不要回去冲个凉\x01",
            "然后和朋友去喝两杯呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB2")

    label("loc_DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_E6A")

    ChrTalk(    #38
        0xFE,
        (
            "唉，『埃尔赛尤』不在\x01",
            "还真是寂寞呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "专职修理工佩顿\x01",
            "就不能快点回来吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "只有我和维修主任两个人的话，\x01",
            "完全没有干劲嘛……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB2")

    label("loc_E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_EB2")

    ChrTalk(    #41
        0xFE,
        (
            "我们的维修主任\x01",
            "一如既往的软弱靠不住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "真是没有办法……\x02",
    )

    CloseMessageWindow()

    label("loc_EB2")

    TalkEnd(0xFE)
    Return()

    # Function_6_BF6 end

    def Function_7_EB6(): pass

    label("Function_7_EB6")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_7_EB6 end

    def Function_8_EBD(): pass

    label("Function_8_EBD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_F73")

    ChrTalk(    #43
        0xFE,
        "现在要返回蔡斯了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "和爱尔莎大使纠缠了好久\x01",
            "终于要答应让我们买定期船了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "『近期内会同意的』\x01",
            "她是这么说的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "嗬，这么困难的贸易谈判\x01",
            "还真是第一次见……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D1")

    label("loc_F73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FD5")

    ChrTalk(    #47
        0xFE,
        (
            "今天的计划\x01",
            "也被爱尔莎大使顶回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "那个人，总是很敏锐地\x01",
            "击中我们的要害～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D1")

    label("loc_FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_105C")

    ChrTalk(    #49
        0xFE,
        (
            "不过终于要同意\x01",
            "让共和国购买定期船了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "关于价格\x01",
            "和对方一直谈不拢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "那个女共和国大使……\x01",
            "是个不容小视的干将呢\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D1")

    label("loc_105C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_10D1")

    ChrTalk(    #52
        0xFE,
        (
            "马上有一个和共和国大使馆\x01",
            "的贸易谈判。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "我们去和共和国大使交涉,\x01",
            "并请求购买\x01",
            "与飞船定期船同型号的商品。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D1")

    TalkEnd(0xFE)
    Return()

    # Function_8_EBD end

    def Function_9_10D5(): pass

    label("Function_9_10D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_129E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_1241")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11CE")

    ChrTalk(    #54
        0xFE,
        "不、不好了！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "刚才我偷听了\x01",
            "从莱普尼兹号下来的修理员的谈话……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "听说正在雷斯顿要塞\x01",
            "进行替换『埃尔赛尤』引擎的工作！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "不能这样做啊。\x01",
            "我必须马上返回蔡斯！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "等等，『埃尔赛尤』！\x01",
            "这次一定要抓住你！！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_123E")

    label("loc_11CE")


    ChrTalk(    #59
        0xFE,
        (
            "这么说来，刚才运走一个\x01",
            "我从没见过的引擎……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "那是什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "……啊，更重要的是\x01",
            "必须尽快搭乘林德号！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_123E")

    Jump("loc_129B")

    label("loc_1241")


    ChrTalk(    #62
        0xFE,
        (
            "这边的航道\x01",
            "好像也在做着陆准备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "什么啊……\x01",
            "是军用艇的紧急着陆吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        "还是……\x02",
    )

    CloseMessageWindow()

    label("loc_129B")

    Jump("loc_143F")

    label("loc_129E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_131A")

    ChrTalk(    #65
        0xFE,
        (
            "真奇怪啊。\x01",
            "我试着做了大量调查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "『埃尔赛尤』现在并没有停在\x01",
            "任何一个飞船坪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "难道去国外了吗。\x02",
    )

    CloseMessageWindow()
    Jump("loc_143F")

    label("loc_131A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_137C")

    ChrTalk(    #68
        0xFE,
        (
            "『埃尔赛尤』\x01",
            "到哪里去了呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "事已至此，一定要查明它的去处\x01",
            "哪怕追到天涯海角！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143F")

    label("loc_137C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_143F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F4")

    ChrTalk(    #70
        0xFE,
        "为什么，为什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "好不容易，来到了王都……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "为什么『埃尔赛尤』\x01",
            "不在这里啊───！？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_143F")

    label("loc_13F4")


    ChrTalk(    #73
        0xFE,
        "好不容易，来到了王都……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "为什么『埃尔赛尤』\x01",
            "不在这里啊───！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_143F")

    TalkEnd(0xFE)
    Return()

    # Function_9_10D5 end

    def Function_10_1443(): pass

    label("Function_10_1443")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_10_1443 end

    def Function_11_144A(): pass

    label("Function_11_144A")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_11_144A end

    def Function_12_1451(): pass

    label("Function_12_1451")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_12_1451 end

    def Function_13_1458(): pass

    label("Function_13_1458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1469")
    Call(0, 29)

    label("loc_1469")

    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_11(0xFF, 0xFF, 0xFF, 0x13880, 0x55730, 0x0)
    StopSound(0xEA60, 0x55730, 0x0)
    StopSound(0xAFC8, 0x55730, 0x2710)
    OP_6D(58630, 40000, 116260, 0)
    OP_67(0, 45000, -50000, 0)
    OP_6B(800, 0)
    OP_6C(60000, 0)
    OP_6E(250, 0)
    OP_A1(0x1F, 0xA)
    OP_72(0xA, 0x4)
    OP_72(0xA, 0x20)
    SetChrPos(0x1F, 87140, 15900, 130979, 90)
    SetChrFlags(0x1F, 0x4)
    OP_A1(0x20, 0xB)
    OP_71(0xB, 0x2)
    OP_72(0xB, 0x4)
    SetChrPos(0x20, 87140, 5900, 130979, 90)
    SetChrFlags(0x20, 0x4)
    OP_71(0x9, 0x4)
    OP_6F(0x5, 100)
    OP_6F(0xA, 60)
    OP_6F(0xB, 0)
    OP_22(0x79, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1571")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_1575")

    label("loc_1571")

    AddParty(0x2, 0xF7, 0xFF)

    label("loc_1575")

    OP_43(0x101, 0x0, 0x0, 0x15)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 0x0)
    Fade(1000)
    OP_6D(83040, 1500, 131020, 0)
    OP_67(0, 6970, -10000, 0)
    OP_6B(3820, 0)
    OP_6C(148000, 0)
    OP_6E(262, 0)
    StopSound(0x88B8, 0x55730, 0x0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0xA, 411)
    OP_70(0xA, 0x1C2)
    Sleep(1300)
    OP_43(0x11, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_43(0x12, 0x1, 0x0, 0xE)
    Sleep(800)
    OP_43(0x13, 0x1, 0x0, 0xE)
    Sleep(800)
    OP_43(0x14, 0x1, 0x0, 0xE)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x0, 0xF)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0x10)
    Sleep(800)
    OP_43(0x18, 0x1, 0x0, 0x11)
    Sleep(800)
    OP_43(0x17, 0x1, 0x0, 0x12)
    Sleep(800)
    OP_43(0x19, 0x1, 0x0, 0x13)
    Sleep(800)
    OP_43(0x1A, 0x1, 0x0, 0x14)
    Sleep(500)

    def lambda_1685():
        OP_6D(79270, 1500, 142560, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1685)
    WaitChrThread(0x1A, 0x1)

    ChrTalk(    #75
        0x101,
        (
            "#1006F好了……\x01",
            "又返回王都了呢。\x02\x03",

            "无论如何\x01",
            "先去游击士协会吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_171A")

    ChrTalk(    #76
        0x106,
        (
            "#051F对啊，听听艾南那边\x01",
            "的所谓的军队意见吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_174C")

    label("loc_171A")


    ChrTalk(    #77
        0x103,
        (
            "#020F好的，听听艾南那边\x01",
            "的所谓的军队意见吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_174C")


    ChrTalk(    #78
        0x17,
        (
            "#033F对了，今天那只白色的船\x01",
            "没停泊在飞船坪呢。\x02\x03",

            "它是叫『埃尔赛尤』吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        "#1015F咦？\x02",
    )

    CloseMessageWindow()

    def lambda_17AE():
        OP_8C(0xFE, 360, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17AE)
    Sleep(50)

    def lambda_17C1():
        OP_8C(0xFE, 360, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_17C1)
    Sleep(50)

    def lambda_17D4():
        OP_8C(0xFE, 360, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_17D4)
    Sleep(50)

    def lambda_17E7():
        OP_8C(0xFE, 360, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_17E7)
    Sleep(500)
    Fade(1000)
    OP_6D(79890, 1500, 146670, 0)
    OP_67(0, 7730, -10000, 0)
    OP_6B(1930, 0)
    OP_6C(33000, 0)
    OP_6E(589, 0)
    OP_0D()

    ChrTalk(    #80
        0x101,
        "#1004F#6P啊，真的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x1A,
        (
            "#070F我没记错的话那是王室的巡洋舰吧。\x02\x03",

            "到哪里\x01",
            "执行任务去了吧？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(79270, 1500, 142560, 0)
    OP_67(0, 6970, -10000, 0)
    OP_6B(3820, 0)
    OP_6C(148000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_18E2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18E2)
    Sleep(50)

    def lambda_18F5():
        OP_8C(0xFE, 177, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_18F5)
    Sleep(50)

    def lambda_1908():
        OP_8C(0xFE, 177, 400)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_1908)
    Sleep(50)

    def lambda_191B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_191B)
    Sleep(500)

    ChrTalk(    #82
        0x18,
        (
            "#040F『埃尔赛尤』\x01",
            "刚好去了雷斯顿要塞。\x02\x03",

            "听说要在那里装载\x01",
            "刚刚完成的新型引擎。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x19,
        (
            "#061F啊，维修长他们也\x01",
            "乘工房船\x01",
            "去雷斯顿要塞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1004F咦～是这样的吗？\x02\x03",

            "#1006F也就是说，那条很帅气的船\x01",
            "要升级得更厉害了？\x02\x03",

            "不知会变成什么样子，值得期待。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x19,
        (
            "#560F只是换个引擎而已,\x01",
            "我想外表不会有什么变化……\x02\x03",

            "#061F不过会变成世界上最快的船，\x01",
            "这一点应该是毫无疑问的⊙\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_1458 end

    def Function_14_1AAD(): pass

    label("Function_14_1AAD")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x10522, 0x5DC, 0x22FA6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_1AAD end

    def Function_15_1B0A(): pass

    label("Function_15_1B0A")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x130A6, 0x5DC, 0x22ED4, 0x7D0, 0x0)
    OP_8C(0xFE, 102, 400)
    Return()

    # Function_15_1B0A end

    def Function_16_1B69(): pass

    label("Function_16_1B69")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13C54, 0x5DC, 0x22EE8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13448, 0x5DC, 0x22B50, 0x7D0, 0x0)
    OP_8C(0xFE, 357, 400)
    Return()

    # Function_16_1B69 end

    def Function_17_1BDC(): pass

    label("Function_17_1BDC")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13C54, 0x5DC, 0x22EE8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13380, 0x5DC, 0x23212, 0x7D0, 0x0)
    OP_8C(0xFE, 177, 400)
    Return()

    # Function_17_1BDC end

    def Function_18_1C4F(): pass

    label("Function_18_1C4F")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13C54, 0x5DC, 0x22EE8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13808, 0x5DC, 0x22B8C, 0x7D0, 0x0)
    OP_8C(0xFE, 357, 400)
    Return()

    # Function_18_1C4F end

    def Function_19_1CC2(): pass

    label("Function_19_1CC2")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13C54, 0x5DC, 0x22EE8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13858, 0x5DC, 0x23208, 0x7D0, 0x0)
    OP_8C(0xFE, 201, 400)
    Return()

    # Function_19_1CC2 end

    def Function_20_1D35(): pass

    label("Function_20_1D35")

    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87110, 1500, 130990, 270)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x1FF9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0x143FC, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    OP_8E(0xFE, 0x13C54, 0x5DC, 0x22EE8, 0x7D0, 0x0)
    OP_8C(0xFE, 261, 400)
    Return()

    # Function_20_1D35 end

    def Function_21_1D94(): pass

    label("Function_21_1D94")


    def lambda_1D9A():
        OP_6D(58630, 30000, 116260, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1D9A)

    def lambda_1DB2():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1DB2)

    def lambda_1DCD():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1DCD)
    Sleep(100)

    def lambda_1DED():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1DED)
    Sleep(100)

    def lambda_1E0D():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1E0D)
    Sleep(100)

    def lambda_1E2D():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1E2D)
    Sleep(100)

    def lambda_1E4D():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1E4D)
    Sleep(100)

    def lambda_1E6D():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1E6D)
    Sleep(100)

    def lambda_1E8D():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1E8D)
    Sleep(100)

    def lambda_1EAD():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1EAD)
    Sleep(100)
    Sleep(4000)

    def lambda_1ED2():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1ED2)

    def lambda_1EED():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1EED)
    Sleep(300)

    def lambda_1F0D():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1F0D)
    Sleep(300)

    def lambda_1F2D():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1F2D)
    Sleep(300)

    def lambda_1F4D():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1F4D)
    Sleep(300)

    def lambda_1F6D():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1F6D)
    Sleep(300)

    def lambda_1F8D():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1F8D)
    Sleep(300)

    def lambda_1FAD():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1FAD)
    Sleep(300)

    def lambda_1FCD():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1FCD)
    Sleep(300)

    def lambda_1FED():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1FED)

    def lambda_2008():
        OP_8F(0xFE, 0x15464, 0xFFFFE9EE, 0x1FFA3, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2008)
    WaitChrThread(0x1F, 0x1)
    WaitChrThread(0x20, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x1F, 87140, -5650, 130979, 90)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x1)
    Sleep(1300)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 100)
    OP_70(0x5, 0xC8)
    Sleep(2500)
    OP_44(0x0, 0x1)
    Return()

    # Function_21_1D94 end

    def Function_22_208B(): pass

    label("Function_22_208B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2098")
    Return()

    label("loc_2098")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20B8")
    Call(0, 29)
    Call(0, 30)
    FadeToBright(0, 0)

    label("loc_20B8")

    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #86
        (
            "\x07\x05前往蔡斯方向的定期飞船\x01",
            "『林德号』就要起飞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("女性的声音")

    AnonymousTalk(    #87
        "\x07\x05需要乘坐的旅客请立即登船。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(1000)
    OP_71(0x9, 0x4)
    OP_6F(0x5, 1)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x40)
    OP_4A(0x17, 255)
    OP_4A(0x1B, 255)
    SetChrPos(0x17, 82970, 1500, 143180, 180)
    SetChrPos(0x1B, 82970, 1500, 139130, 180)

    def lambda_2193():
        OP_8E(0xFE, 0x1446A, 0x5DC, 0x20B70, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2193)
    OP_6D(82960, 1500, 138300, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    OP_22(0x75, 0x0, 0x64)
    OP_0D()
    WaitChrThread(0x1B, 0x1)
    OP_8C(0x1B, 0, 400)
    Sleep(500)

    ChrTalk(    #88
        0x1B,
        (
            "#270F再见了，奥利维尔。\x02\x03",

            "我不在的这段期间\x01",
            "可别搞出什么问题来啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x17,
        (
            "#037F#1P哼，放心好了。\x02\x03",

            "我做过什么\x01",
            "让心爱的你担心的事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x1B,
        (
            "#272F过了这阵子\x01",
            "我也担心不起来了。\x02\x03",

            "你起码保证别出什么问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x17,
        "#031F#1P嗯，妥善处理吧。\x02",
    )

    CloseMessageWindow()
    OP_A1(0x1F, 0xA)
    OP_72(0xA, 0x4)
    OP_72(0xA, 0x20)
    SetChrPos(0x1F, 87140, -5650, 130979, 90)
    SetChrFlags(0x1F, 0x4)
    OP_A1(0x20, 0xB)
    SetChrPos(0x20, 87140, -5650, 130979, 90)
    SetChrFlags(0x20, 0x4)
    Fade(500)
    OP_72(0xB, 0x4)
    OP_0D()
    Call(0, 23)
    Sleep(1000)
    OP_6D(82970, 1500, 143180, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(151000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 76000, 1500, 142810, 90)
    SetChrPos(0x107, 76000, 1500, 143700, 90)
    SetChrPos(0xF7, 76000, 1500, 144000, 90)
    SetChrPos(0xF9, 76000, 1500, 142470, 90)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #92
        0x101,
        "#1P喂，奥利维尔！\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x17, 0x101, 400)

    def lambda_23FB():
        OP_6D(82140, 1500, 142960, 2500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_23FB)

    def lambda_2413():
        OP_8E(0xFE, 0x1398E, 0x5DC, 0x22DDA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2413)
    Sleep(100)

    def lambda_2433():
        OP_8E(0xFE, 0x139F2, 0x5DC, 0x23154, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2433)
    Sleep(700)

    def lambda_2453():
        OP_8E(0xFE, 0x135EC, 0x5DC, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2453)
    Sleep(100)

    def lambda_2473():
        OP_8E(0xFE, 0x135EC, 0x5DC, 0x22C86, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2473)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #93
        0x17,
        (
            "#033F#5P哟，是你们。\x02\x03",

            "#031F难道是舍不得我\x01",
            "所以找到这里来了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        (
            "#1007F#2P怎么可能嘛。\x02\x03",

            "#1015F不过……\x01",
            "刚才那是穆拉吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2542")

    ChrTalk(    #95
        0x106,
        (
            "#052F为什么帝国军人\x01",
            "在使用飞船？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_256A")

    label("loc_2542")


    ChrTalk(    #96
        0x103,
        (
            "#023F为什么帝国的军人\x01",
            "在使用飞船？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_256A")


    ChrTalk(    #97
        0x17,
        (
            "#030F#5P啊，好像是因为军务\x01",
            "要去柏斯地区。\x02\x03",

            "不是有空贼团\x01",
            "用过的飞艇吗？\x02\x03",

            "好像打算回收那个。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1004F#2P空贼团的飞艇\x01",
            "是那个绿色的小型艇吧。\x02\x03",

            "但是，为什么是穆拉去？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x17,
        (
            "#035F#5P或许你已经知道\x01",
            "那艘飞艇是埃雷波尼亚制的。\x02\x03",

            "使用它的空贼团\x01",
            "好像至今没被捉住。\x02\x03",

            "#030F作为帝国政府，想要回收证据\x01",
            "以此配合搜查……\x02\x03",

            "据说这样试探过王国。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1015F#2P嗯？\x01",
            "真是难以理解的理由。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x17,
        (
            "#031F#5P唉，空贼团\x01",
            "是埃雷波尼亚原贵族这事\x01",
            "传出去不大好听。\x02\x03",

            "大概是想尽可能在缔结互不侵犯条约之前\x01",
            "把事情不了了之地蒙混过去吧。\x02\x03",

            "在共和国深入人心之前。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1015F#2P据说空贼团是原帝国贵族……\x02\x03",

            "#1020F哎，那个男人婆是……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x17,
        (
            "#033F#5P咦，你不知道吗？\x02\x03",

            "#030F据说是帝国北部\x01",
            "一个叫做卡普亚男爵家的小领主。\x02\x03",

            "据说数年前，由于负债累累\x01",
            "而卖掉了领土。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1015F#2P有、有这种事吗……\x02\x03",

            "#1007F怎么说呢……\x01",
            "这些家伙也算有点可怜吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_28C3")

    ChrTalk(    #105
        0x106,
        (
            "#053F嘁，即使这样\x01",
            "仍然让人完全无法同情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28EF")

    label("loc_28C3")


    ChrTalk(    #106
        0x103,
        (
            "#027F是啊，即使这样\x01",
            "也不太令人同情呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28EF")


    ChrTalk(    #107
        0x17,
        (
            "#035F#5P好了，就是这么回事\x01",
            "我是来送行的。\x02\x03",

            "#030F你们在空港做什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1015F#2P啊，其实我们是\x01",
            "是来这里找玲的……\x02\x03",

            "奥利维尔，你看到她了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x17,
        (
            "#033F#5P玲？\x02\x03",

            "那边那个\x01",
            "不是玲吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        "#1004F#2P咦……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 75560, 1500, 143120, 90)

    def lambda_29D9():
        OP_6D(79810, 1500, 142310, 1600)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29D9)

    QueueWorkItem(0x101, 3, None)

    def lambda_29F7():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29F7)
    Sleep(100)

    def lambda_2A0A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2A0A)
    Sleep(100)

    def lambda_2A1D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_2A1D)
    Sleep(100)

    def lambda_2A30():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2A30)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #111
        0x1C,
        "#261F#2P嗯⊙\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x107,
        "#065F#6P玲、玲！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1020F#5P你什么时候……\x02",
    )

    CloseMessageWindow()

    def lambda_2A8A():
        OP_6D(78000, 1500, 142310, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A8A)
    OP_8E(0x101, 0x12D72, 0x5DC, 0x22EDE, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #114
        0x101,
        (
            "#1019F#5P喂，玲！\x02\x03",

            "真是的\x01",
            "你怎么能突然玩失踪呢！\x02\x03",

            "而且牵连那么多人\x01",
            "从我们身边逃跑～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x1C,
        (
            "#268F#2P对不起……\x01",
            "因为我很无聊啊。\x02\x03",

            "#267F那个～\x01",
            "我从百货店买了红茶和小甜饼干哟！\x02\x03",

            "也有大家的份儿，\x01",
            "所以拜托，别生气了好不好？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#1015F#5P哼……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C13")

    ChrTalk(    #117
        0x108,
        (
            "#071F#5P哈哈，因为玲的胡闹，\x01",
            "我们也得到了很多快乐啊。\x02\x03",

            "这下就算扯平了，不也挺好吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C55")

    label("loc_2C13")


    ChrTalk(    #118
        0x105,
        (
            "#048F#5P呵呵，我们也\x01",
            "玩得很开心……\x02\x03",

            "这样的话就算扯平\x01",
            "了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C55")


    ChrTalk(    #119
        0x101,
        (
            "#1007F#5P哈，真是没办法。\x02\x03",

            "#1017F那就\x01",
            "原谅你好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x1C,
        "#265F#2P真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x107,
        "#061F嘿嘿，太好了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2D06")

    ChrTalk(    #122
        0x106,
        (
            "#051F#5P那么\x01",
            "先回游击士协会吧。\x02\x03",

            "说不定\x01",
            "会有什么情报呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D44")

    label("loc_2D06")


    ChrTalk(    #123
        0x103,
        (
            "#021F#5P那么\x01",
            "先回游击士协会吧。\x02\x03",

            "说不定\x01",
            "会有什么情报呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D44")


    def lambda_2D4A():
        OP_6D(79810, 1500, 142310, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D4A)
    TurnDirection(0x101, 0x17, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #124
        0x101,
        "#1006F#2P嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x17,
        "#033F咦，出什么事了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1015F#2P好像是柏斯地区\x01",
            "发生了什么事件。\x02\x03",

            "#1004F唔……\x01",
            "这么说来\x01",
            "穆拉不是去了柏斯吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x17,
        (
            "#032F啊，是啊。\x02\x03",

            "唔……\x01",
            "正想问你详情呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x17, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2E76")

    ChrTalk(    #128
        0x106,
        (
            "#051F#6P好了，回到游击士协会之后\x01",
            "我会给你们大致说明一下的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB5")

    label("loc_2E76")


    ChrTalk(    #129
        0x103,
        (
            "#020F#6P好了，等回到游击士协会之后\x01",
            "我给你做详细的说明吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EB5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T4100   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_22_208B end

    def Function_23_2ED2(): pass

    label("Function_23_2ED2")

    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x64)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x64)
    OP_6F(0xA, 1)
    OP_70(0xA, 0x3C)
    OP_73(0xA)
    Sleep(1000)
    OP_23(0x75)
    OP_22(0x77, 0x1, 0x64)
    OP_6F(0xA, 61)
    OP_70(0xA, 0xA0)
    Fade(1000)
    SetChrFlags(0x1B, 0x80)
    OP_72(0x9, 0x4)
    ClearMapFlags(0x10)
    OP_6D(63630, 30000, 116260, 0)
    OP_67(0, 45000, -50000, 0)
    OP_6B(750, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    OP_73(0x4)
    OP_71(0xA, 0x20)
    OP_6F(0xA, 161)
    OP_70(0xA, 0x104)
    OP_91(0x1F, 0x0, 0x12C, 0x0, 0x12C, 0x0)
    OP_91(0x1F, 0x0, 0x320, 0x0, 0x1F4, 0x0)
    Sleep(2000)

    def lambda_2FB5():
        OP_6D(75000, 30000, 116260, 8000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2FB5)

    def lambda_2FCD():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2FCD)
    OP_94(0x1, 0x1F, 0x0, 0x3E8, 0x3E8, 0x0)

    def lambda_2FF2():
        OP_94(0x1, 0xFE, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_2FF2)
    OP_94(0x1, 0x1F, 0x0, 0x4B0, 0x7D0, 0x0)

    def lambda_3017():
        OP_94(0x1, 0xFE, 0x0, 0x578, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3017)
    OP_94(0x1, 0x1F, 0x0, 0x578, 0xBB8, 0x0)

    def lambda_303C():
        OP_94(0x1, 0xFE, 0x0, 0x640, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_303C)
    OP_94(0x1, 0x1F, 0x0, 0x640, 0xFA0, 0x0)

    def lambda_3061():
        OP_94(0x1, 0xFE, 0x0, 0x708, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3061)
    OP_94(0x1, 0x1F, 0x0, 0x708, 0x1388, 0x0)

    def lambda_3086():
        OP_94(0x1, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3086)
    OP_94(0x1, 0x1F, 0x0, 0x7D0, 0x1770, 0x0)

    def lambda_30AB():
        OP_94(0x1, 0xFE, 0x0, 0x898, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_30AB)
    OP_94(0x1, 0x1F, 0x0, 0x898, 0x1B58, 0x0)
    FadeToDark(2000, 0, -1)

    def lambda_30DA():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_30DA)

    def lambda_30F0():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_30F0)
    OP_24(0x77, 0x5A)
    Sleep(100)
    OP_24(0x77, 0x50)
    Sleep(100)
    OP_24(0x77, 0x46)
    Sleep(100)
    OP_24(0x77, 0x3C)
    Sleep(100)
    OP_24(0x77, 0x32)
    Sleep(100)
    OP_24(0x77, 0x28)
    Sleep(100)
    OP_24(0x77, 0x1E)
    Sleep(100)
    OP_24(0x77, 0x14)
    Sleep(100)
    OP_24(0x77, 0xA)
    Sleep(100)
    OP_23(0x77)
    OP_0D()
    OP_44(0x101, 0x0)
    Return()

    # Function_23_2ED2 end

    def Function_24_315A(): pass

    label("Function_24_315A")

    EventBegin(0x0)
    OP_6D(84620, 1500, 135300, 0)
    OP_67(0, 4280, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(135000, 0)
    OP_6E(364, 0)
    OP_6D(118730, 1500, 138330, 0)
    OP_67(0, 4650, -10000, 0)
    OP_6B(4810, 0)
    OP_6C(261000, 0)
    OP_6E(364, 0)
    StopSound(0x9C40, 0x493E0, 0x0)
    SetChrPos(0x101, 83430, 1700, 133650, 0)
    SetChrPos(0x102, 82500, 1700, 133620, 0)
    SetChrPos(0x21, 83700, 1700, 132200, 0)
    SetChrPos(0x18, 84600, 1700, 133240, 0)
    SetChrPos(0x19, 81670, 1700, 133310, 0)
    SetChrPos(0x22, 81540, 1700, 132400, 0)
    SetChrPos(0x23, 82880, 1700, 131700, 0)
    SetChrPos(0x1A, 84900, 1700, 131800, 0)
    SetChrPos(0x17, 82910, 1700, 141060, 180)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_72(0x5, 0x4)
    OP_71(0x9, 0x4)
    OP_72(0xA, 0x4)
    OP_72(0xB, 0x4)
    OP_6F(0x5, 200)
    OP_6F(0xA, 0)
    OP_75(0xB, 0x0, 0x0)
    OP_74(0xB, 0x0, 0x0)
    FadeToBright(1000, 0)

    def lambda_3308():
        OP_6D(81880, 1500, 137450, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3308)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(84620, 1500, 135300, 0)
    OP_67(0, 5710, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(135000, 0)
    OP_6E(364, 0)
    StopSound(0x9C40, 0x2BF20, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #130
        0x101,
        (
            "#1007F#2P嗯，没想到奥利维尔\x01",
            "竟然要返回帝国了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x21,
        "#524F#2P是啊，真是突然啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x17,
        (
            "#035F其实本来计划\x01",
            "在早些时候就回国的。\x02\x03",

            "#030F由于艾丝蒂尔被抓走\x01",
            "所以延期了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1025F#2P是这样啊……\x01",
            "真对不起，因为我的缘故……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x17,
        (
            "#031F不要放在心上。\x02\x03",

            "多亏等你回来\x01",
            "我才能再次\x01",
            "与亲爱的约修亚相见啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x102,
        (
            "#1049F#2P哈哈，你真是一点儿没变啊。\x02\x03",

            "#1043F……那个，奥利维尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x17,
        "#030F嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x102,
        (
            "#1042F#2P你……\x02\x03",

            "#1035F……不，没什么。\x02\x03",

            "#1040F感谢你在至今为止的旅途中\x01",
            "对艾丝蒂尔的帮助。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x17,
        (
            "#035F呵，是我自愿的啊\x01",
            "不要说那么见外的话。\x02\x03",

            "#037F不过，如果你一定要这么说\x01",
            "那么来个拥抱以示感谢吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1019F#2P你给我适可而止。\x02\x03",

            "#1025F真是的……至少最后该\x01",
            "好好地告别一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x17,
        (
            "#035F哈哈，我一直是\x01",
            "很认真的啊。\x02\x03",

            "#030F艾丝蒂尔，约修亚。\x01",
            "雪拉，还有大家……\x02\x03",

            "虽然会有各种各样的辛劳和危险\x01",
            "大家当心就好了。\x02\x03",

            "#031F奥利维尔会在帝国的天空中\x01",
            "为你们的幸运而祈祷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        "#1006F#2P嗯，谢谢！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x21,
        (
            "#021F#2P呵呵……\x01",
            "你也要当心啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x102,
        "#1054F#2P……保重了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x1A,
        "#071F有机会再一起喝酒吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x22,
        (
            "#051F下次改掉你那\x01",
            "装怪的毛病啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x19,
        (
            "#067F#2P啊哈哈……\x01",
            "那个那个……再见～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x23,
        (
            "#1061F啊，虽然只是短暂的交往\x01",
            "可我非常开心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x18,
        (
            "#048F多保重……\x01",
            "承蒙关照了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_B7(0x3)
    OP_A2(0x10F8)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_24_315A end

    def Function_25_37FC(): pass

    label("Function_25_37FC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_6D(73560, 250, 132340, 0)
    OP_67(0, 8020, -10000, 0)
    OP_6B(5850, 0)
    OP_6C(285000, 0)
    OP_6E(404, 0)
    StopSound(0x9C40, 0x493E0, 0x0)
    SetChrPos(0x17, 82620, 1500, 143550, 135)
    ClearChrFlags(0x17, 0x80)
    OP_A1(0x1F, 0xA)
    OP_72(0xA, 0x4)
    OP_72(0xA, 0x20)
    SetChrPos(0x1F, 89000, 200, 130000, 90)
    SetChrFlags(0x1F, 0x4)
    OP_A1(0x20, 0xB)
    OP_72(0xB, 0x4)
    SetChrFlags(0x20, 0x4)
    SetChrPos(0x20, 89000, -4800, 130000, 90)
    OP_75(0xB, 0x0, 0x0)
    OP_74(0xB, 0x0, 0x0)
    OP_72(0x5, 0x4)
    OP_6F(0x5, 200)
    OP_6F(0xA, 1)
    OP_22(0x75, 0x0, 0x64)

    def lambda_3917():
        OP_6D(93000, 1250, 131420, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3917)

    def lambda_392F():
        OP_67(0, 4500, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_392F)

    def lambda_3947():
        OP_6B(5850, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3947)

    def lambda_3957():
        OP_6C(285000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3957)

    def lambda_3967():
        OP_6E(471, 6000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3967)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x5, 200)
    OP_70(0x5, 0x64)
    Sleep(1000)
    OP_23(0x75)
    OP_22(0x125, 0x0, 0x64)
    OP_43(0x1F, 0x0, 0x0, 0x1C)
    Sleep(3000)
    OP_91(0x1F, 0x0, 0x1F4, 0x0, 0x190, 0x0)
    OP_91(0x1F, 0x0, 0x3E8, 0x0, 0x320, 0x0)
    OP_91(0x1F, 0x0, 0x7D0, 0x0, 0x640, 0x0)
    OP_91(0x1F, 0x0, 0x1F4, 0x0, 0x320, 0x0)
    OP_91(0x1F, 0x0, 0x190, 0x0, 0x190, 0x0)

    def lambda_3A15():
        OP_6D(105490, 1500, 130810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A15)

    def lambda_3A2D():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3A2D)

    def lambda_3A48():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3A48)
    Sleep(200)

    def lambda_3A68():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3A68)

    def lambda_3A83():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3A83)
    Sleep(200)

    def lambda_3AA3():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3AA3)

    def lambda_3ABE():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3ABE)
    Sleep(200)

    def lambda_3ADE():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3ADE)

    def lambda_3AF9():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3AF9)
    Sleep(200)

    def lambda_3B19():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3B19)

    def lambda_3B34():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3B34)
    Sleep(200)

    def lambda_3B54():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3B54)

    def lambda_3B6F():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3B6F)
    Sleep(200)

    def lambda_3B8F():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3B8F)

    def lambda_3BAA():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3BAA)
    Sleep(200)

    def lambda_3BCA():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3BCA)

    def lambda_3BE5():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3BE5)
    Sleep(200)

    def lambda_3C05():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3C05)

    def lambda_3C20():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3C20)
    Sleep(200)

    def lambda_3C40():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3C40)

    def lambda_3C5B():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3C5B)
    Sleep(200)

    def lambda_3C7B():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3C7B)

    def lambda_3C96():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3C96)
    Sleep(200)

    def lambda_3CB6():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3CB6)

    def lambda_3CD1():
        OP_8F(0xFE, 0x3D090, 0x2008, 0x1FBD0, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3CD1)
    Sleep(2800)
    OP_24(0x77, 0x5A)
    OP_24(0x125, 0x5A)
    Sleep(100)
    OP_24(0x77, 0x50)
    OP_24(0x125, 0x50)
    Sleep(100)
    OP_24(0x77, 0x46)
    OP_24(0x125, 0x46)
    Sleep(100)
    OP_24(0x77, 0x3C)
    OP_24(0x125, 0x3C)
    Sleep(100)
    OP_24(0x77, 0x32)
    OP_24(0x125, 0x32)
    Sleep(100)
    OP_24(0x77, 0x28)
    OP_24(0x125, 0x28)
    Sleep(100)
    OP_24(0x77, 0x1E)
    OP_24(0x125, 0x1E)
    Sleep(100)
    OP_23(0x77)
    OP_23(0x125)
    Fade(1000)
    OP_44(0x101, 0x3)
    StopSound(0x9C40, 0x2BF20, 0x0)
    OP_6D(83010, 1500, 142960, 0)
    OP_67(0, 6680, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(134000, 0)
    OP_6E(302, 0)
    OP_8C(0x17, 90, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #149
        0x17,
        (
            "#035F呼……\x01",
            "悠闲的时光看来要结束了啊。\x02\x03",

            "#030F不，也许还有\x01",
            "最后的机会。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x1E, 71940, 750, 143010, 90)
    SetChrChipByIndex(0x1E, 18)
    SetChrPos(0x1D, 71700, 750, 144070, 90)
    ClearChrFlags(0x1D, 0x80)

    def lambda_3E2A():

        label("loc_3E2A")

        OP_9E(0xFE, 0x32, 0x0, 0x1F4, 0x3E8)
        OP_48()
        Jump("loc_3E2A")

    QueueWorkItem2(0x1D, 1, lambda_3E2A)

    NpcTalk(    #150
        0x1E,
        "女孩的声音",
        "#1P等、等一下～！\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3E80():
        TurnDirection(0xFE, 0x1E, 400)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3E80)
    ClearChrFlags(0x1E, 0x80)

    def lambda_3E93():
        OP_6D(81940, 1500, 142800, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3E93)

    def lambda_3EAB():
        OP_8E(0x1E, 0x139E8, 0x5DC, 0x22FCE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3EAB)
    Sleep(500)

    def lambda_3ECB():
        OP_8E(0xFE, 0x1340C, 0x5DC, 0x231FE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_3ECB)
    WaitChrThread(0x1E, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #151
        0x17,
        "#033F#5P咦，你们……\x02",
    )

    WaitChrThread(0x1D, 0x2)
    OP_44(0x1D, 0x1)
    CloseMessageWindow()

    ChrTalk(    #152
        0x1E,
        "#152F#6P啊，走了……\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\\\mp032_00.eff")

    ChrTalk(    #153
        0x1D,
        (
            "#145F呼哧呼哧……\x01",
            "没、没赶得上吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x17,
        (
            "#030F#5P怎么了，各位记者？\x02\x03",

            "又打算像龙事件那时一样\x01",
            "偷偷潜入吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x1D,
        (
            "#141F啊，而且还听说\x01",
            "约修亚回来了呢。\x02\x03",

            "#144F好了，朵洛希。\x01",
            "赶紧拍摄『埃尔赛尤』。\x02\x03",

            "如果使用长焦镜头\x01",
            "应该能拍到很不错的画面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x1E,
        "#151F#6P了解！前辈！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 180, 400)
    OP_43(0x17, 0x0, 0x0, 0x1B)
    Sleep(300)

    def lambda_405E():
        OP_6D(88040, 1500, 142240, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_405E)

    def lambda_4076():
        OP_67(0, 5680, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4076)

    def lambda_408E():
        OP_6B(2700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_408E)

    def lambda_409E():
        OP_8E(0x1E, 0x155F4, 0x5DC, 0x22EF2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_409E)
    Sleep(300)

    def lambda_40BE():
        OP_8E(0x1D, 0x14D0C, 0x5DC, 0x230A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_40BE)
    WaitChrThread(0x1E, 0x0)
    SetChrSubChip(0x1E, 0)
    SetChrChipByIndex(0x1E, 19)
    Sleep(500)
    OP_A2(0x0)
    OP_43(0x1E, 0x1, 0x0, 0x1A)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x1D, 0x0)
    WaitChrThread(0x17, 0x0)
    Sleep(1000)

    ChrTalk(    #157
        0x17,
        "#031F#2P呵呵……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrPos(0x1B, 67260, 0, 143120, 90)
    ClearChrFlags(0x1B, 0x80)
    OP_8C(0x17, 0, 400)
    OP_8E(0x17, 0x1428A, 0x5DC, 0x23050, 0x7D0, 0x0)

    def lambda_4157():
        OP_8E(0x17, 0x1113E, 0x0, 0x22F10, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_4157)
    Sleep(2500)
    OP_A3(0x0)
    Fade(1000)
    OP_6D(73250, 0, 141910, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(2570, 0)
    OP_6C(134000, 0)
    OP_6E(325, 0)
    OP_20(0xBB8)

    def lambda_41C1():
        OP_6D(70250, 0, 141910, 3000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_41C1)
    WaitChrThread(0x17, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x17, 0x1)
    Sleep(500)

    ChrTalk(    #158
        0x1B,
        "#270F……打过招呼了吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x17,
        (
            "#035F#5P嗯，打过了。\x02\x03",

            "#030F那边的准备如何了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x1B,
        (
            "#277F叔父想了些办法。\x02\x03",

            "宰相阁下\x01",
            "似乎也认为正是好时机。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x17,
        (
            "#030F#5P的确，如果是他的话\x01",
            "应该能接受王国的人。\x02\x03",

            "#035F呵呵……事情要变得有趣起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x1B,
        (
            "#272F真是的……\x01",
            "这是什么无聊的爱好啊。\x02\x03",

            "#276F他们惊愕的表情\x01",
            "好像马上就要浮现在眼前了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x17,
        (
            "#031F#5P哈哈哈。\x01",
            "那正是我的目标啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4358():
        OP_6D(71920, 750, 143050, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4358)

    def lambda_4370():
        OP_67(0, 4720, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4370)

    def lambda_4388():
        OP_6B(2570, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4388)

    def lambda_4398():
        OP_6C(122000, 2000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4398)

    def lambda_43A8():
        OP_6E(325, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_43A8)
    OP_8C(0x17, 90, 400)
    WaitChrThread(0x101, 0x1)
    Sleep(300)

    ChrTalk(    #164
        0x17,
        (
            "#030F#2P（下次再相见时\x01",
            "彼此就是冤家对头了。)\x02\x03",

            "#035F（请大家千万不要\x01",
            "被『结社』之类的抢了先啊。)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_0D()
    OP_A2(0x10FF)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_37FC end

    def Function_26_4449(): pass

    label("Function_26_4449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_44D1")
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x1E, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x1E, 0, 1400, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("Function_26_4449")

    label("loc_44D1")

    Return()

    # Function_26_4449 end

    def Function_27_44D2(): pass

    label("Function_27_44D2")

    OP_8E(0xFE, 0x143B6, 0x6A4, 0x22920, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_27_44D2 end

    def Function_28_44EE(): pass

    label("Function_28_44EE")

    OP_22(0x77, 0x0, 0x64)
    OP_6F(0xA, 1)
    OP_70(0xA, 0x96)
    OP_73(0xA)
    OP_6F(0xA, 151)
    OP_70(0xA, 0x14A)
    Sleep(3200)
    OP_75(0xB, 0x0, 0x2)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0xB, 0x0, 0x1)
    Sleep(250)
    OP_74(0xB, 0x0, 0x2)
    Sleep(250)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0xB, 0x0, 0x3)
    Sleep(250)
    OP_74(0xB, 0x0, 0x4)
    Sleep(250)
    OP_22(0xDD, 0x0, 0x64)
    OP_74(0xB, 0x0, 0x5)
    Sleep(250)
    OP_74(0xB, 0x0, 0x6)
    Sleep(250)
    OP_74(0xB, 0x0, 0x7)
    OP_73(0xA)
    OP_71(0xA, 0x20)
    OP_6F(0xA, 330)
    OP_70(0xA, 0x1AE)
    Return()

    # Function_28_44EE end

    def Function_29_45A1(): pass

    label("Function_29_45A1")

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
        (0, "loc_461B"),
        (1, "loc_4621"),
        (SWITCH_DEFAULT, "loc_4627"),
    )


    label("loc_461B")

    OP_A2(0x1200)
    Jump("loc_4627")

    label("loc_4621")

    OP_A2(0x1201)
    Jump("loc_4627")

    label("loc_4627")

    Return()

    # Function_29_45A1 end

    def Function_30_4628(): pass

    label("Function_30_4628")

    ClearMapFlags(0x1)
    OP_6D(12790, 0, 144090, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4667")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_4681")

    label("loc_4667")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_4681")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_30_4628 end

    def Function_31_46A1(): pass

    label("Function_31_46A1")

    ClearMapFlags(0x1)
    OP_6D(12790, 0, 144090, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_46E6")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    Jump("loc_4706")

    label("loc_46E6")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)

    label("loc_4706")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_31_46A1 end

    def Function_32_4726(): pass

    label("Function_32_4726")

    Sleep(2000)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x3E8)
    Return()

    # Function_32_4726 end

    def Function_33_4741(): pass

    label("Function_33_4741")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #165
        (
            "\x07\x05定期船起降坪\x01",
            "≡　前往洛连特市\x01",
            "≡　前往蔡斯市\x01",
            "≡　去卡尔瓦德共和国\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #166
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

    # Function_33_4741 end

    def Function_34_47EE(): pass

    label("Function_34_47EE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #167
        (
            "\x07\x05　　　飞船坪塔台　　　　\x01",
            "　※无关人员禁止入内　　\x01",
            " 『利贝尔飞船公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_34_47EE end

    SaveToFile()

Try(main)
