from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2500   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2500.x',
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
        '雷克特',                               # 9
        '乔儿',                                 # 10
        '汉斯',                                 # 11
        '基库',                                 # 12
        '艾福托老师',                           # 13
        '巴克斯',                               # 14
        '利库斯',                               # 15
        '罗伊斯',                               # 16
        '罗基克',                               # 17
        '芙拉瑟',                               # 18
        '蕾娜',                                 # 19
        '德尼斯',                               # 20
        '弗雷',                                 # 21
        '坎诺',                                 # 22
        '雅莉丝',                               # 23
        '罗迪',                                 # 24
        '米克',                                 # 25
        '目标用照相机',                         # 26
        '',                                     # 27
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
        'ED6_DT07/CH01590 ._CH',             # 00
        'ED6_DT07/CH01090 ._CH',             # 01
        'ED6_DT07/CH01370 ._CH',             # 02
        'ED6_DT07/CH01360 ._CH',             # 03
        'ED6_DT07/CH01080 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH01580 ._CH',             # 06
        'ED6_DT07/CH01093 ._CH',             # 07
        'ED6_DT07/CH02670 ._CH',             # 08
        'ED6_DT07/CH02390 ._CH',             # 09
        'ED6_DT07/CH02550 ._CH',             # 0A
        'ED6_DT07/CH02320 ._CH',             # 0B
        'ED6_DT07/CH02323 ._CH',             # 0C
        'ED6_DT06/CH20051 ._CH',             # 0D
        'ED6_DT07/CH00043 ._CH',             # 0E
        'ED6_DT26/CH20254 ._CH',             # 0F
        'ED6_DT07/CH01460 ._CH',             # 10
        'ED6_DT26/CH20783 ._CH',             # 11
        'ED6_DT07/CH01583 ._CH',             # 12
        'ED6_DT26/CH20776 ._CH',             # 13
        'ED6_DT26/CH20777 ._CH',             # 14
        'ED6_DT26/CH20778 ._CH',             # 15
        'ED6_DT07/CH00044 ._CH',             # 16
        'ED6_DT26/CH20786 ._CH',             # 17
    )

    AddCharChipPat(
        'ED6_DT07/CH01590P._CP',             # 00
        'ED6_DT07/CH01090P._CP',             # 01
        'ED6_DT07/CH01370P._CP',             # 02
        'ED6_DT07/CH01360P._CP',             # 03
        'ED6_DT07/CH01080P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH01580P._CP',             # 06
        'ED6_DT07/CH01093P._CP',             # 07
        'ED6_DT07/CH02670P._CP',             # 08
        'ED6_DT07/CH02390P._CP',             # 09
        'ED6_DT07/CH02550P._CP',             # 0A
        'ED6_DT07/CH02320P._CP',             # 0B
        'ED6_DT07/CH02323P._CP',             # 0C
        'ED6_DT06/CH20051P._CP',             # 0D
        'ED6_DT07/CH00043P._CP',             # 0E
        'ED6_DT26/CH20254P._CP',             # 0F
        'ED6_DT07/CH01460P._CP',             # 10
        'ED6_DT26/CH20783P._CP',             # 11
        'ED6_DT07/CH01583P._CP',             # 12
        'ED6_DT26/CH20776P._CP',             # 13
        'ED6_DT26/CH20777P._CP',             # 14
        'ED6_DT26/CH20778P._CP',             # 15
        'ED6_DT07/CH00044P._CP',             # 16
        'ED6_DT26/CH20786P._CP',             # 17
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
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
        X                   = 29230,
        Z                   = -2000,
        Y                   = 35060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 35340,
        Z                   = 0,
        Y                   = 75590,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 28510,
        Z                   = -1750,
        Y                   = 59190,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 44890,
        Z                   = 0,
        Y                   = 53100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 37100,
        Z                   = 0,
        Y                   = 77390,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 25960,
        Z                   = 0,
        Y                   = 65180,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 24550,
        Z                   = 0,
        Y                   = 65180,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 41920,
        Z                   = 0,
        Y                   = 25060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = 35560,
        Z                   = 0,
        Y                   = 77450,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 23,
    )

    DeclNpc(
        X                   = 30160,
        Z                   = -2000,
        Y                   = 45970,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 45040,
        Z                   = 0,
        Y                   = 54220,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 62660,
        Z                   = 0,
        Y                   = 75310,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 41480,
        Z                   = 0,
        Y                   = 77530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
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


    DeclActor(
        TriggerX            = 13590,
        TriggerZ            = 0,
        TriggerY            = 45970,
        TriggerRange        = 800,
        ActorX              = 13590,
        ActorZ              = 1100,
        ActorY              = 45970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 49,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 59440,
        TriggerZ            = 9000,
        TriggerY            = 17860,
        TriggerRange        = 1000,
        ActorX              = 59440,
        ActorZ              = 9500,
        ActorY              = 17860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 50,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33510,
        TriggerZ            = 0,
        TriggerY            = 79330,
        TriggerRange        = 800,
        ActorX              = 33510,
        ActorZ              = 500,
        ActorY              = 79330,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 51,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 13590,
        TriggerZ            = 0,
        TriggerY            = 45970,
        TriggerRange        = 800,
        ActorX              = 13590,
        ActorZ              = 1100,
        ActorY              = 45970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 38,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_43A",          # 00, 0
        "Function_1_73C",          # 01, 1
        "Function_2_928",          # 02, 2
        "Function_3_AA5",          # 03, 3
        "Function_4_B02",          # 04, 4
        "Function_5_B26",          # 05, 5
        "Function_6_B4A",          # 06, 6
        "Function_7_B6E",          # 07, 7
        "Function_8_BCB",          # 08, 8
        "Function_9_BF4",          # 09, 9
        "Function_10_C18",         # 0A, 10
        "Function_11_C3C",         # 0B, 11
        "Function_12_C60",         # 0C, 12
        "Function_13_E1C",         # 0D, 13
        "Function_14_114E",        # 0E, 14
        "Function_15_1304",        # 0F, 15
        "Function_16_1541",        # 10, 16
        "Function_17_162E",        # 11, 17
        "Function_18_191D",        # 12, 18
        "Function_19_1BD2",        # 13, 19
        "Function_20_1D32",        # 14, 20
        "Function_21_1E50",        # 15, 21
        "Function_22_1F77",        # 16, 22
        "Function_23_20E7",        # 17, 23
        "Function_24_21F0",        # 18, 24
        "Function_25_23C7",        # 19, 25
        "Function_26_2569",        # 1A, 26
        "Function_27_2625",        # 1B, 27
        "Function_28_2B28",        # 1C, 28
        "Function_29_2BF9",        # 1D, 29
        "Function_30_2ED3",        # 1E, 30
        "Function_31_3DC4",        # 1F, 31
        "Function_32_4D2B",        # 20, 32
        "Function_33_53D9",        # 21, 33
        "Function_34_62B4",        # 22, 34
        "Function_35_62D4",        # 23, 35
        "Function_36_62F9",        # 24, 36
        "Function_37_633A",        # 25, 37
        "Function_38_71A4",        # 26, 38
        "Function_39_732F",        # 27, 39
        "Function_40_79F4",        # 28, 40
        "Function_41_7AA6",        # 29, 41
        "Function_42_7BA3",        # 2A, 42
        "Function_43_8AA9",        # 2B, 43
        "Function_44_8BA8",        # 2C, 44
        "Function_45_8CA3",        # 2D, 45
        "Function_46_8D1B",        # 2E, 46
        "Function_47_8E0D",        # 2F, 47
        "Function_48_8EB7",        # 30, 48
        "Function_49_8F05",        # 31, 49
        "Function_50_9209",        # 32, 50
        "Function_51_9221",        # 33, 51
    )


    def Function_0_43A(): pass

    label("Function_0_43A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_459")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (130, "loc_452"),
        (SWITCH_DEFAULT, "loc_459"),
    )


    label("loc_452")

    Event(0, 44)
    Jump("loc_459")

    label("loc_459")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_646")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_50A")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 23000, 0, 35340, 0)
    OP_43(0x15, 0x0, 0x0, 0x7)
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49B")
    SetChrFlags(0x18, 0x10)

    label("loc_49B")

    OP_43(0x18, 0x0, 0x0, 0x8)
    ClearChrFlags(0x1C, 0x80)
    OP_43(0x1C, 0x0, 0x0, 0x8)
    ClearChrFlags(0x1F, 0x80)
    OP_62(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_507")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x1)
    SetChrPos(0x10, 49120, 9000, 20740, 0)
    OP_62(0x10, 0x0, 1800, 0x8, 0x9, 0xC8, 0x0)
    SetChrChipByIndex(0x10, 19)
    SetChrSubChip(0x10, 0)

    label("loc_507")

    Jump("loc_646")

    label("loc_50A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_514")
    Jump("loc_646")

    label("loc_514")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_578")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 28130, -2000, 44180, 180)
    OP_43(0x15, 0x0, 0x0, 0x6)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 35370, 0, 17310, 90)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, 60700, 0, 50820, 0)
    OP_43(0x1E, 0x0, 0x0, 0xA)
    Jump("loc_646")

    label("loc_578")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_5D5")
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 20890, 0, 29430, 0)
    OP_43(0x14, 0x0, 0x0, 0x4)
    ClearChrFlags(0x15, 0x80)
    OP_43(0x15, 0x0, 0x0, 0x5)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 35370, 0, 17310, 90)
    ClearChrFlags(0x1E, 0x80)
    Jump("loc_646")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_646")
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x20, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_605")
    ClearChrFlags(0x14, 0x80)
    OP_43(0x14, 0x0, 0x0, 0x3)

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 2)), scpexpr(EXPR_END)), "loc_646")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 61450, 0, 36510, 270)
    OP_43(0x12, 0x0, 0x0, 0x9)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 39400, 0, 18670, 270)
    OP_43(0x11, 0x0, 0x0, 0xB)

    label("loc_646")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_6A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_66F")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    Event(0, 43)
    Jump("loc_6A1")

    label("loc_66F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_685")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 42)
    Jump("loc_6A1")

    label("loc_685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_6A1")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 39)

    label("loc_6A1")

    Jump("loc_73B")

    label("loc_6A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_6C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_6BE")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 37)

    label("loc_6BE")

    Jump("loc_73B")

    label("loc_6C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_6DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_6DB")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 31)

    label("loc_6DB")

    Jump("loc_73B")

    label("loc_6DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_729")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_707")
    OP_A3(0x2505)
    OP_A2(0x0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 30)
    Jump("loc_726")

    label("loc_707")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_726")
    OP_A3(0x2504)
    OP_A2(0x0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 29)

    label("loc_726")

    Jump("loc_73B")

    label("loc_729")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 27)

    label("loc_73B")

    Return()

    # Function_0_43A end

    def Function_1_73C(): pass

    label("Function_1_73C")

    OP_16(0x2, 0xFA0, 0xFFFEA840, 0xFFFEBFB0, 0x23004C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_76D")
    OP_B1("t2500_y")
    Jump("loc_776")

    label("loc_76D")

    OP_B1("t2500_n")

    label("loc_776")

    OP_A3(0x0)
    Jump("loc_785")

    label("loc_77C")

    OP_B1("t2500_n")

    label("loc_785")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_797")
    OP_72(0x1021, 0x0)
    ExitThread()

    label("loc_797")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x83), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B3")
    OP_11(0xA4, 0xFF, 0xDC, 0x9470, 0x1ADB0, 0x0)

    label("loc_7B3")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83E")
    OP_72(0x1021, 0x0)
    ExitThread()
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_813")
    OP_62(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_813")
    OP_62(0x10, 0x0, 1800, 0x8, 0x9, 0xC8, 0x0)

    label("loc_813")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_827")
    OP_64(0x0, 0x1)
    OP_65(0x3, 0x1)

    label("loc_827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_83E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 3)), scpexpr(EXPR_END)), "loc_83E")
    OP_65(0x2, 0x1)

    label("loc_83E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_852")
    OP_1B(0x1E, 0x0, 0x2D)
    Jump("loc_85B")

    label("loc_852")

    OP_71(0x42E, 0x0)
    ExitThread()
    OP_10(0x1E, 0x0)

    label("loc_85B")

    OP_71(0x409, 0x0)
    ExitThread()
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0x40D, 0x0)
    ExitThread()
    OP_71(0x40E, 0x0)
    ExitThread()
    OP_71(0x40F, 0x0)
    ExitThread()
    OP_71(0x410, 0x0)
    ExitThread()
    OP_71(0x411, 0x0)
    ExitThread()
    OP_71(0x412, 0x0)
    ExitThread()
    OP_71(0x413, 0x0)
    ExitThread()
    OP_71(0x414, 0x0)
    ExitThread()
    OP_71(0x415, 0x0)
    ExitThread()
    OP_71(0x416, 0x0)
    ExitThread()
    OP_71(0x417, 0x0)
    ExitThread()
    OP_71(0x418, 0x0)
    ExitThread()
    OP_71(0x419, 0x0)
    ExitThread()
    OP_71(0x41A, 0x0)
    ExitThread()
    OP_71(0x41B, 0x0)
    ExitThread()
    OP_71(0x41C, 0x0)
    ExitThread()
    OP_71(0x41D, 0x0)
    ExitThread()
    OP_71(0x41E, 0x0)
    ExitThread()
    OP_71(0x41F, 0x0)
    ExitThread()
    OP_71(0x420, 0x0)
    ExitThread()
    OP_71(0x423, 0x0)
    ExitThread()
    OP_71(0x424, 0x0)
    ExitThread()
    OP_71(0x425, 0x0)
    ExitThread()
    OP_71(0x426, 0x0)
    ExitThread()
    OP_71(0x427, 0x0)
    ExitThread()
    OP_71(0x428, 0x0)
    ExitThread()
    OP_71(0x429, 0x0)
    ExitThread()
    OP_71(0x42A, 0x0)
    ExitThread()
    OP_71(0x42B, 0x0)
    ExitThread()
    OP_71(0x42C, 0x0)
    ExitThread()
    Return()

    # Function_1_73C end

    def Function_2_928(): pass

    label("Function_2_928")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_A8F")

    label("loc_94D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_966")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_A8F")

    label("loc_966")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_A8F")

    label("loc_97F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_998")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_A8F")

    label("loc_998")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B1")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_A8F")

    label("loc_9B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9CA")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_A8F")

    label("loc_9CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E3")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_A8F")

    label("loc_9E3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FC")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_A8F")

    label("loc_9FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A15")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_A8F")

    label("loc_A15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A2E")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_A8F")

    label("loc_A2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A47")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_A8F")

    label("loc_A47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A60")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_A8F")

    label("loc_A60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A79")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_A8F")

    label("loc_A79")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_A8F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AA4")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_A8F")

    label("loc_AA4")

    Return()

    # Function_2_928 end

    def Function_3_AA5(): pass

    label("Function_3_AA5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B01")
    OP_8E(0xFE, 0x7238, 0xFFFFF830, 0x88F4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x7238, 0xFFFFF830, 0xDDB8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x97F4, 0xFFFFF830, 0xDDB8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x97F4, 0xFFFFF830, 0x88F4, 0x7D0, 0x0)
    Jump("Function_3_AA5")

    label("loc_B01")

    Return()

    # Function_3_AA5 end

    def Function_4_B02(): pass

    label("Function_4_B02")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B25")
    OP_8D(0xFE, 23400, 28220, 20230, 31360, 2000)
    Jump("Function_4_B02")

    label("loc_B25")

    Return()

    # Function_4_B02 end

    def Function_5_B26(): pass

    label("Function_5_B26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B49")
    OP_8D(0xFE, 36420, 76870, 33680, 73630, 2000)
    Jump("Function_5_B26")

    label("loc_B49")

    Return()

    # Function_5_B26 end

    def Function_6_B4A(): pass

    label("Function_6_B4A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B6D")
    OP_8D(0xFE, 29400, 42790, 27350, 46370, 2000)
    Jump("Function_6_B4A")

    label("loc_B6D")

    Return()

    # Function_6_B4A end

    def Function_7_B6E(): pass

    label("Function_7_B6E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BCA")
    OP_8E(0xFE, 0x59D8, 0x0, 0xF6AE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB0CC, 0x0, 0xF6AE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB0CC, 0x0, 0x709E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x59D8, 0x0, 0x709E, 0x7D0, 0x0)
    Jump("Function_7_B6E")

    label("loc_BCA")

    Return()

    # Function_7_B6E end

    def Function_8_BCB(): pass

    label("Function_8_BCB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BF3")
    OP_8C(0xFE, 90, 400)
    OP_8C(0xFE, 180, 400)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 0, 400)
    Jump("Function_8_BCB")

    label("loc_BF3")

    Return()

    # Function_8_BCB end

    def Function_9_BF4(): pass

    label("Function_9_BF4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C17")
    OP_8D(0xFE, 59880, 38950, 64269, 33940, 2000)
    Jump("Function_9_BF4")

    label("loc_C17")

    Return()

    # Function_9_BF4 end

    def Function_10_C18(): pass

    label("Function_10_C18")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C3B")
    OP_8D(0xFE, 60140, 50160, 62310, 53370, 2000)
    Jump("Function_10_C18")

    label("loc_C3B")

    Return()

    # Function_10_C18 end

    def Function_11_C3C(): pass

    label("Function_11_C3C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C5F")
    OP_8D(0xFE, 40550, 17520, 37680, 20650, 2000)
    Jump("Function_11_C3C")

    label("loc_C5F")

    Return()

    # Function_11_C3C end

    def Function_12_C60(): pass

    label("Function_12_C60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_C6D")
    Jump("loc_E18")

    label("loc_C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_C77")
    Jump("loc_E18")

    label("loc_C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_C81")
    Jump("loc_E18")

    label("loc_C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_D2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_CD5")

    ChrTalk(    #0
        0xFE,
        (
            "刚才感觉好像\x01",
            "稍微看到一眼似的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "哎～逃得倒是够快！\x02",
    )

    CloseMessageWindow()
    Jump("loc_D28")

    label("loc_CD5")


    ChrTalk(    #2
        0xFE,
        (
            "你、你们也在\x01",
            "找那个男的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "我也正打算教训他，\x01",
            "却到处都找不到……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_D28")

    Jump("loc_E18")

    label("loc_D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_E18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_D97")

    ChrTalk(    #4
        0xFE,
        (
            "这么说来，\x01",
            "那家伙好像又惹了什么事啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "唔唔，\x01",
            "怎么教训他才好呢……\x02",
        )
    )

    Jump("loc_D93")

    label("loc_D93")

    CloseMessageWindow()
    Jump("loc_E18")

    label("loc_D97")


    ChrTalk(    #6
        0xFE,
        (
            "一年级的学生们\x01",
            "差不多也该习惯校园生活了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "从这个时期开始\x01",
            "会出现不少懈怠起来的家伙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "必须要严厉管教才行。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_E18")

    TalkEnd(0xFE)
    Return()

    # Function_12_C60 end

    def Function_13_E1C(): pass

    label("Function_13_E1C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_E29")
    Jump("loc_114A")

    label("loc_E29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_E33")
    Jump("loc_114A")

    label("loc_E33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_F2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_E94")

    ChrTalk(    #9
        0xFE,
        (
            "前任那个学生会长，\x01",
            "一直干得很好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "唉，工作一点\x01",
            "进展都没有啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F2C")

    label("loc_E94")


    ChrTalk(    #11
        0xFE,
        (
            "刚才那个\x01",
            "学生会长又来了。\x02",
        )
    )

    Jump("loc_EC0")

    label("loc_EC0")

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "好不容易考完试了，\x01",
            "他却强行让我\x01",
            "给他画一幅素描…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "呜呜，\x01",
            "后来还要让我上色。\x02",
        )
    )

    Jump("loc_F28")

    label("loc_F28")

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_F2C")

    Jump("loc_114A")

    label("loc_F2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_105A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_F8C")

    ChrTalk(    #14
        0xFE,
        (
            "啊啊，\x01",
            "那个奇怪的歌声不绝于耳……\x02",
        )
    )

    Jump("loc_F6E")

    label("loc_F6E")

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "谁来救救我啊～！！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1057")

    label("loc_F8C")


    ChrTalk(    #16
        0xFE,
        (
            "刚才啊，\x01",
            "那个学生会长过来了。\x02",
        )
    )

    Jump("loc_FBC")

    label("loc_FBC")

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "然后就在我耳边\x01",
            "一直小声唱着很奇怪的歌。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "什么『月亮的丝线』啦\x01",
            "『长胡子的骑士』什么的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "搞得我一直三心二意，\x01",
            "根本就画不了画了嘛！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1057")

    Jump("loc_114A")

    label("loc_105A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_114A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_10BB")

    ChrTalk(    #20
        0xFE,
        (
            "直到去年\x01",
            "这里还有喷泉呢。\x02",
        )
    )

    Jump("loc_1094")

    label("loc_1094")

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "我非常喜欢那个，\x01",
            "可是却……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_114A")

    label("loc_10BB")


    ChrTalk(    #22
        0xFE,
        (
            "直到去年啊，\x01",
            "这里还有喷泉呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "因为是中世纪时的东西，\x01",
            "所以已经相当破旧了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "唉唉，\x01",
            "在拆毁之前我还画了素描呢……\x02",
        )
    )

    Jump("loc_1146")

    label("loc_1146")

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_114A")

    TalkEnd(0xFE)
    Return()

    # Function_13_E1C end

    def Function_14_114E(): pass

    label("Function_14_114E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_115B")
    Jump("loc_1300")

    label("loc_115B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_1165")
    Jump("loc_1300")

    label("loc_1165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_116F")
    Jump("loc_1300")

    label("loc_116F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_1179")
    Jump("loc_1300")

    label("loc_1179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_1300")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_11E5")

    ChrTalk(    #25
        0x11,
        (
            "#643F说到社会系……\x02\x03",

            "#640F经常去旧校舍的那个学长，\x01",
            "好像就是社会系的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1300")

    label("loc_11E5")


    ChrTalk(    #26
        0x11,
        (
            "#643F啊，科洛丝……\x02\x03",

            "#1890F真的不用帮忙吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x105,
        (
            "#543F嗯。\x02\x03",

            "#542F只不过是给社会系的各位\x01",
            "派发资料而已嘛。\x02",
        )
    )

    Jump("loc_1274")

    label("loc_1274")

    CloseMessageWindow()

    ChrTalk(    #28
        0x11,
        (
            "#645F啊…………\x02\x03",

            "#648F要是忙不过来，可要说一声啊。\x02\x03",

            "我们也\x01",
            "正在找人呢。\x02\x03",

            "反正是顺便……好吗？\x02",
        )
    )

    Jump("loc_12FC")

    label("loc_12FC")

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_1300")

    TalkEnd(0xFE)
    Return()

    # Function_14_114E end

    def Function_15_1304(): pass

    label("Function_15_1304")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_13DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1359")

    ChrTalk(    #29
        0xFE,
        (
            "雷克特同学\x01",
            "经常帮忙打杂呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "…………在上课的时候。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13DB")

    label("loc_1359")


    ChrTalk(    #31
        0xFE,
        (
            "雷克特同学\x01",
            "经常帮忙打杂呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "虽然有人说他坏话，\x01",
            "我却觉得他是个好人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "虽然偶尔也会\x01",
            "顺手牵羊拿走一些备用品。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_13DB")

    Jump("loc_153D")

    label("loc_13DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_13E8")
    Jump("loc_153D")

    label("loc_13E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1485")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_144B")

    ChrTalk(    #34
        0xFE,
        (
            "虽然没在这附近\x01",
            "见过凶暴的魔兽……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "不过还是\x01",
            "小心为好哦。\x02",
        )
    )

    Jump("loc_1447")

    label("loc_1447")

    CloseMessageWindow()
    Jump("loc_1482")

    label("loc_144B")


    ChrTalk(    #36
        0xFE,
        "哦，要到学院外面去吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "要小心魔兽哦。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1482")

    Jump("loc_153D")

    label("loc_1485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_153D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_14BB")

    ChrTalk(    #38
        0xFE,
        (
            "不知道是不是\x01",
            "还在这附近呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_152E")

    label("loc_14BB")


    ChrTalk(    #39
        0xFE,
        "咦？　雷克特同学？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "他刚才还在\x01",
            "那边的长椅上看书呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "……这么说来，\x01",
            "不知什么时候就不见了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_152E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153D")
    OP_A2(0x2F83)
    OP_65(0x2, 0x1)

    label("loc_153D")

    TalkEnd(0xFE)
    Return()

    # Function_15_1304 end

    def Function_16_1541(): pass

    label("Function_16_1541")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_162A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_15B1")

    ChrTalk(    #42
        0xFE,
        (
            "这么说来，\x01",
            "刚才米丽亚老师从这里跑过去了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "看她气势汹汹的，\x01",
            "发生什么事了吗。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_162A")

    label("loc_15B1")


    ChrTalk(    #44
        0xFE,
        "考试之后食堂里面挤满了人。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "所以干脆就这样\x01",
            "消磨一下时间算了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "呼哇～…………\x01",
            "能这么悠闲真是好啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_162A")

    TalkEnd(0xFE)
    Return()

    # Function_16_1541 end

    def Function_17_162E(): pass

    label("Function_17_162E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_1919")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 6)), scpexpr(EXPR_END)), "loc_16F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1698")

    ChrTalk(    #47
        0xFE,
        "这星期我是值日生呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "负责的地方太大，\x01",
            "导致我社团活动都要迟到了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F1")

    label("loc_1698")


    ChrTalk(    #49
        0xFE,
        (
            "雅莉丝和我\x01",
            "是本周的值日生哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "社团活动\x01",
            "可能要稍微迟到些了。\x02",
        )
    )

    Jump("loc_16ED")

    label("loc_16ED")

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_16F1")

    Jump("loc_1919")

    label("loc_16F4")


    ChrTalk(    #51
        0xFE,
        (
            "咦，科洛丝。\x01",
            "你加入学生会了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        (
            "#044F啊，不是。\x01",
            "我没有加入……\x02\x03",

            "#045F不过因为一些原因，\x01",
            "现在正在给他们帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "啊啊，是这样吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "抱歉，\x01",
            "感觉你和平常有点不同。\x02",
        )
    )

    Jump("loc_17B6")

    label("loc_17B6")

    CloseMessageWindow()

    ChrTalk(    #55
        0x105,
        "#044F…………咦？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "哈哈哈，\x01",
            "所以就以为你肯定加入学生会了。\x02",
        )
    )

    Jump("loc_180A")

    label("loc_180A")

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "那个，今天有什么事……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x105,
        (
            "#044F啊，嗯……\x02\x03",

            "#040F在这附近，\x01",
            "有没有见过雷克特学长？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "雷克特学长……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "没有，\x01",
            "经过这里的好像\x01",
            "只有勤务员巴克斯先生哦。\x02",
        )
    )

    Jump("loc_18C6")

    label("loc_18C6")

    CloseMessageWindow()

    ChrTalk(    #61
        0x105,
        (
            "#047F是吗……\x02\x03",

            "#040F嗯，\x01",
            "真是太谢谢了。\x02",
        )
    )

    Jump("loc_18FD")

    label("loc_18FD")

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "哪里，彼此彼此。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F76)

    label("loc_1919")

    TalkEnd(0xFE)
    Return()

    # Function_17_162E end

    def Function_18_191D(): pass

    label("Function_18_191D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_1BC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 7)), scpexpr(EXPR_END)), "loc_1A1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1994")

    ChrTalk(    #63
        0xFE,
        (
            "反正已经入部了，\x01",
            "就打算认真练习一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "不过……\x01",
            "这个就是练习吗？？\x02",
        )
    )

    Jump("loc_1990")

    label("loc_1990")

    CloseMessageWindow()
    Jump("loc_1A17")

    label("loc_1994")


    ChrTalk(    #65
        0xFE,
        (
            "弗雷同学好像是\x01",
            "列曼自治州来的交换留学生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "而且听说他还相当优秀。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "我、我并不是冲着这个原因\x01",
            "……才入部的哦！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_1A17")

    Jump("loc_1BC9")

    label("loc_1A1A")

    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #68
        0xFE,
        "哎、哎呀，科洛丝同学……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x105,
        (
            "#044F啊，罗基克同学。\x02\x03",

            "怎么了，\x01",
            "呆在这种地方。\x02",
        )
    )

    Jump("loc_1AA0")

    label("loc_1AA0")

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "没、没什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "这次我加入了\x01",
            "吹奏乐社团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "今天是第一次练习。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x105,
        (
            "#040F是这样啊。\x02\x03",

            "#041F呵呵，加油吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "啊、啊啊……当然。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "对了，科洛丝同学……\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0xFE,
        "哎，没什么……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "下、下次考试\x01",
            "也要一起加油哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x105,
        "#040F呵呵，是啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F77)

    label("loc_1BC9")

    ClearChrFlags(0xFE, 0x10)
    TalkEnd(0xFE)
    Return()

    # Function_18_191D end

    def Function_19_1BD2(): pass

    label("Function_19_1BD2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_1D2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1C35")

    ChrTalk(    #79
        0xFE,
        "我已经很生气了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "既然如此，部长也好什么也好\x01",
            "我就当给你们看看吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D2E")

    label("loc_1C35")


    ChrTalk(    #81
        0xFE,
        (
            "虽然都说了绝对不当部长，\x01",
            "可是蕾娜还是\x01",
            "不停地来劝说。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "还有刚才，\x01",
            "打着呵欠走过去的那位……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "明明什么内情都不清楚，\x01",
            "就说『不行不行，\x01",
            "你肯定不行』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "……真是令人生气。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "既然如此，部长也好什么也好\x01",
            "我就当给你们看看吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)

    label("loc_1D2E")

    TalkEnd(0xFE)
    Return()

    # Function_19_1BD2 end

    def Function_20_1D32(): pass

    label("Function_20_1D32")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_1E4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_1D9F")

    ChrTalk(    #86
        0xFE,
        (
            "算了。\x01",
            "只要有个好结果就行。\x02",
        )
    )

    Jump("loc_1D6E")

    label("loc_1D6E")

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "这个关键词\x01",
            "就留到下次有机会再说好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E4C")

    label("loc_1D9F")


    ChrTalk(    #88
        0xFE,
        (
            "芙拉瑟似乎也终于\x01",
            "下定决心当部长了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "其实作为最后的手段\x01",
            "我还特地留了一个\x01",
            "关键词没说出来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "可是却被刚才那个人\x01",
            "把功劳抢走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "……真是可惜。\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)

    label("loc_1E4C")

    TalkEnd(0xFE)
    Return()

    # Function_20_1D32 end

    def Function_21_1E50(): pass

    label("Function_21_1E50")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1F73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_1EDB")

    ChrTalk(    #92
        0xFE,
        (
            "每年这个时候，\x01",
            "中央工房都有面向普通民众的公开讲座。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "可以听到最新的研究进展呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "呵呵，真是期待啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F73")

    label("loc_1EDB")


    ChrTalk(    #95
        0xFE,
        (
            "下周开始会在蔡斯中央工房\x01",
            "召开面向普通民众的公开讲座。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "考试也结束了，\x01",
            "下次休假的时候就去听听看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "偶尔去这种地方看看\x01",
            "也不错呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xD)

    label("loc_1F73")

    TalkEnd(0xFE)
    Return()

    # Function_21_1E50 end

    def Function_22_1F77(): pass

    label("Function_22_1F77")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_20E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_1FED")

    ChrTalk(    #98
        0x12,
        (
            "#735F他也真会给人添麻烦啊……\x02\x03",

            "#734F无论怎么想，\x01",
            "都是在拿我们\x01",
            "开玩笑不是吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E3")

    label("loc_1FED")


    ChrTalk(    #99
        0x12,
        (
            "#733F啊，是科洛丝吗。\x02\x03",

            "#732F你在这附近有没有\x01",
            "看到一个吊儿郎当的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x105,
        "#044F吊儿郎当的人……是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x12,
        (
            "#734F啊，\x01",
            "没有印象就算了。\x02\x03",

            "#736F真奇怪啊……\x01",
            "不是在这附近的话……\x02",
        )
    )

    Jump("loc_20C7")

    label("loc_20C7")

    CloseMessageWindow()

    ChrTalk(    #102
        0x105,
        "#042F？？？\x02",
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_20E3")

    TalkEnd(0xFE)
    Return()

    # Function_22_1F77 end

    def Function_23_20E7(): pass

    label("Function_23_20E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_21EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_21BD")

    ChrTalk(    #103
        0xFE,
        (
            "列曼自治州\x01",
            "好像有个叫广播体操的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "大家一起围着很大的\x01",
            "导力广播喇叭做体操哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "啊，你知道导力广播吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "那是通信局向居民\x01",
            "播送的音乐之类的节目，\x01",
            "大家可以一起听哦～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EC")

    label("loc_21BD")


    ChrTalk(    #107
        0xFE,
        "广播体操～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "一、二、一、二！\x02",
    )

    CloseMessageWindow()
    OP_A2(0xF)

    label("loc_21EC")

    TalkEnd(0xFE)
    Return()

    # Function_23_20E7 end

    def Function_24_21F0(): pass

    label("Function_24_21F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_22ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_2253")

    ChrTalk(    #109
        0xFE,
        (
            "刚才雷克特学长\x01",
            "在和一只白色的鸟嬉戏呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "嗯，是啊。在考试的时候。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22EA")

    label("loc_2253")


    ChrTalk(    #111
        0xFE,
        (
            "刚才雷克特学长\x01",
            "在和一只白色的鸟嬉戏呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "我偶然从窗户看到，\x01",
            "所以考试结束后就到这里来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "唉～，\x01",
            "好像已经走了的样子。\x02",
        )
    )

    Jump("loc_22E6")

    label("loc_22E6")

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_22EA")

    Jump("loc_23C3")

    label("loc_22ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_23C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_234F")

    ChrTalk(    #114
        0xFE,
        (
            "唉，\x01",
            "露西同学无论做什么都像模像样的。\x02",
        )
    )

    Jump("loc_232D")

    label("loc_232D")

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "是不是有什么秘诀呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_23C3")

    label("loc_234F")


    ChrTalk(    #116
        0xFE,
        (
            "刚才露西同学\x01",
            "到校舍里面去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "看起来好像\x01",
            "很累的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "那种略带忧郁的感觉\x01",
            "真是太棒了啊～㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)

    label("loc_23C3")

    TalkEnd(0xFE)
    Return()

    # Function_24_21F0 end

    def Function_25_23C7(): pass

    label("Function_25_23C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_2565")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_END)), "loc_24A0")
    OP_63(0xFE)

    ChrTalk(    #119
        0xFE,
        (
            "说不定露西学姐\x01",
            "已经有喜欢的人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "到、到底是谁！？\x01",
            "啊啊，好想知道…………！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "……不过还是不要对汉斯说吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "等他也去告白，然后受打击后一蹶不振就好了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2565")

    label("loc_24A0")

    OP_63(0xFE)

    ChrTalk(    #123
        0xFE,
        (
            "这之前，\x01",
            "我对露西学姐告白了。\x02",
        )
    )

    Jump("loc_24D3")

    label("loc_24D3")

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "……结果她说『对不起』。\x01",
            "瞬间就被甩了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "不过那个时候她的表情……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "露西学姐该不是\x01",
            "已经有喜欢的人了吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_A2(0x11)

    label("loc_2565")

    TalkEnd(0xFE)
    Return()

    # Function_25_23C7 end

    def Function_26_2569(): pass

    label("Function_26_2569")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_2621")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_25C4")

    ChrTalk(    #127
        0xFE,
        "啊啊，真是累啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "就在这边\x01",
            "随便偷会儿懒好了。\x02",
        )
    )

    Jump("loc_25C0")

    label("loc_25C0")

    CloseMessageWindow()
    Jump("loc_2621")

    label("loc_25C4")


    ChrTalk(    #129
        0xFE,
        (
            "啊…………\x01",
            "我记得你是新来的那个同学。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "怎么啦，\x01",
            "没事就别理我啊。\x02",
        )
    )

    Jump("loc_261D")

    label("loc_261D")

    CloseMessageWindow()
    OP_A2(0x12)

    label("loc_2621")

    TalkEnd(0xFE)
    Return()

    # Function_26_2569 end

    def Function_27_2625(): pass

    label("Function_27_2625")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #131
        "\x07\x00#40W春天―――\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #132
        "\x07\x00#40W……今年的春天来的很迟。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x800)
    Sleep(1000)
    OP_6D(58000, 0, 46000, 0)
    OP_67(0, 7820, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(90000, 0)
    OP_6E(540, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x9470, 0x1C138, 0x0)
    SetChrPos(0x105, 11400, 0, 46000, 90)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 49420, 8700, 20980, 90)
    SetChrChipByIndex(0x10, 19)
    SetChrSubChip(0x10, 4)
    OP_1D(0xE)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_C8(0x200, 0x46, "C_PLAC06._CH", 0x1, 0x7D0)

    def lambda_2754():
        OP_6D(19660, 0, 44000, 10000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_2754)

    def lambda_276C():
        OP_67(0, 6260, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_276C)

    def lambda_2784():
        OP_6C(125000, 10000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_2784)
    WaitChrThread(0x21, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #133
        (
            "\x07\x00#40W木莲花也一朵接一朵露出白色的容颜，\x01",
            "在慵懒的春天小睡着。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #134
        (
            "\x07\x00#40W而这个杰尼丝王立学院，\x01",
            "也有一个稍微迟来的人…………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    WaitChrThread(0x21, 0x0)
    OP_6D(18000, 0, 46000, 0)
    OP_67(0, 4500, -10000, 0)
    OP_6B(4250, 0)
    OP_6C(90000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #135
        0x105,
        "插班生",
        "#542F这里就是杰尼丝王立学院………\x02",
    )

    Jump("loc_28E3")

    label("loc_28E3")

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    NpcTalk(    #136
        0x105,
        "插班生",
        "#047F呼…………\x02",
    )

    Jump("loc_292E")

    label("loc_292E")

    CloseMessageWindow()
    Sleep(500)

    NpcTalk(    #137
        0x105,
        "插班生",
        "#042F好的……！\x02",
    )

    Jump("loc_295F")

    label("loc_295F")

    CloseMessageWindow()

    def lambda_2966():
        OP_8E(0xFE, 0x319C, 0x0, 0xB3B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2966)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    OP_70(0x21, 0x3C)
    OP_73(0x21)
    StopSound(0x9470, 0x2D2A8, 0x4650)
    OP_43(0x105, 0x3, 0x0, 0x1C)
    Sleep(2000)
    Fade(1500)
    OP_6D(21500, 0, 46720, 0)
    OP_67(0, 5620, -10000, 0)
    OP_6B(3460, 0)
    OP_6C(305000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_29F1():
        OP_6D(30960, -2000, 37400, 8000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_29F1)

    def lambda_2A09():
        OP_6B(3860, 8000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2A09)

    def lambda_2A19():
        OP_6E(454, 8000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_2A19)
    WaitChrThread(0x21, 0x0)
    Sleep(1000)

    NpcTalk(    #138
        0x10,
        "谜样男子",
        (
            "#1770F#5P……哦…………\x02\x03",

            "那就是传说中的插班生啊。\x02",
        )
    )

    Jump("loc_2A86")

    label("loc_2A86")

    CloseMessageWindow()
    Sleep(1500)
    OP_22(0x196, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x8C, 0x0, 0x64)
    OP_62(0x10, 0xFFFFFEA2, 1750, 0x26, 0x27, 0xC8, 0x1)
    Sleep(1500)
    SetChrSubChip(0x10, 3)
    Sleep(150)
    SetChrSubChip(0x10, 2)
    Sleep(300)

    NpcTalk(    #139
        0x10,
        "谜样男子",
        (
            "#1776F鹰……？\x02\x03",

            "#1775F不，是隼吧……\x02",
        )
    )

    Jump("loc_2B12")

    label("loc_2B12")

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_27_2625 end

    def Function_28_2B28(): pass

    label("Function_28_2B28")


    def lambda_2B2E():
        OP_8E(0xFE, 0x7030, 0xFFFFF830, 0xB3B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B2E)
    WaitChrThread(0x105, 0x1)

    def lambda_2B4E():
        OP_8E(0xFE, 0x7030, 0xFFFFF830, 0xDCB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B4E)
    WaitChrThread(0x105, 0x1)

    def lambda_2B6E():
        OP_8E(0xFE, 0x9740, 0xFFFFF830, 0xDCB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B6E)
    WaitChrThread(0x105, 0x1)

    def lambda_2B8E():
        OP_8E(0xFE, 0x9740, 0xFFFFF830, 0xB540, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B8E)
    WaitChrThread(0x105, 0x1)

    def lambda_2BAE():
        OP_8E(0xFE, 0xBC5C, 0x190, 0xB540, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2BAE)
    WaitChrThread(0x105, 0x1)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_70(0x0, 0x3C)
    OP_73(0x0)

    def lambda_2BDE():
        OP_8E(0xFE, 0xC544, 0x1F4, 0xB540, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2BDE)
    WaitChrThread(0x105, 0x1)
    Return()

    # Function_28_2B28 end

    def Function_29_2BF9(): pass

    label("Function_29_2BF9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(33900, 0, 44000, 0)
    OP_67(0, 8200, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(410, 0)
    SetChrPos(0x105, 49500, 500, 19240, 270)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x14, 0x80)

    def lambda_2C78():
        OP_6D(44500, 0, 20400, 8000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_2C78)

    def lambda_2C90():
        OP_67(0, 6600, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_2C90)

    def lambda_2CA8():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_2CA8)

    def lambda_2CB8():
        OP_6E(300, 8000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_2CB8)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x21, 0x0)
    OP_72(0x1008, 0x0)
    ExitThread()
    OP_70(0x8, 0x3C)
    OP_73(0x8)

    def lambda_2CE7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2CE7)

    def lambda_2CF9():
        OP_8E(0xFE, 0xA2A8, 0x0, 0x4B28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2CF9)
    Sleep(1000)
    OP_72(0x8, 0x8)
    ExitThread()
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #140
        0x105,
        (
            "#044F#11P…………咦、咦？\x02\x03",

            "#043F我的资料不见了…………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x105, 181, 500)
    Sleep(800)
    OP_8C(0x105, 0, 500)
    Sleep(800)

    ChrTalk(    #141
        0x105,
        (
            "#049F#11P（是、是忘在\x01",
            "  教室里了吗……？）\x02\x03",

            "#042F（嗯，一定是的。\x01",
            "  得回去拿才行……）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 315, 500)

    def lambda_2E3D():
        OP_8E(0xFE, 0x9A4C, 0x0, 0x5384, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2E3D)
    WaitChrThread(0x105, 0x1)

    def lambda_2E5D():
        OP_8E(0xFE, 0x9A4C, 0x0, 0x67E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2E5D)
    WaitChrThread(0x105, 0x1)

    def lambda_2E7D():
        OP_8E(0xFE, 0xB5A4, 0x0, 0x7148, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2E7D)
    WaitChrThread(0x105, 0x1)

    def lambda_2E9D():
        OP_8E(0xFE, 0xB5A4, 0x0, 0xA7F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2E9D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x105, 0x3)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2510   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_2BF9 end

    def Function_30_2ED3(): pass

    label("Function_30_2ED3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x2000000)
    OP_6D(53700, 170, 44000, 0)
    OP_67(0, 5170, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(135000, 0)
    OP_6E(286, 0)
    SetChrPos(0x105, 50500, 500, 46000, 270)
    SetChrFlags(0x14, 0x80)

    def lambda_2F3D():
        OP_6D(48700, 0, 45000, 5000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_2F3D)
    FadeToBright(2000, 0)
    Sleep(3000)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x3C)
    OP_73(0x0)

    def lambda_2F73():
        OP_8E(0xFE, 0xBA54, 0xFA, 0xB3B0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2F73)
    WaitChrThread(0x105, 0x1)
    OP_72(0x0, 0x8)
    ExitThread()
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #142
        0x105,
        (
            "#047F#5P……唉…………\x02\x03",

            "…………………………\x02\x03",

            "#049F……有点累了呢……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3030():
        OP_6D(45720, 0, 44680, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3030)

    def lambda_3048():
        OP_67(0, 5180, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3048)

    def lambda_3060():
        OP_6C(125000, 3000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_3060)

    def lambda_3070():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_3070)

    def lambda_3080():
        OP_8E(0xFE, 0xAB2C, 0xFFFFFF06, 0xAE24, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3080)
    WaitChrThread(0x105, 0x1)
    Sleep(500)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x105, 43820, -300, 44580, 270)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 14)
    Sleep(500)
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #143
        0x105,
        "#049F#5P……唉…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 45640, 0, 35640, 0)

    def lambda_3139():
        OP_8E(0xFE, 0xB248, 0x0, 0xA6B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3139)
    WaitChrThread(0x10, 0x1)
    TurnDirection(0x10, 0x105, 400)
    Sleep(300)

    NpcTalk(    #144
        0x10,
        "谜样男子",
        "#1770F#11P哟，插班生同学。\x02",
    )

    Jump("loc_319A")

    label("loc_319A")

    CloseMessageWindow()
    OP_63(0x105)
    OP_62(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x105, 1)
    Sleep(300)

    ChrTalk(    #145
        0x105,
        (
            "#044F#6P…………啊……\x02\x03",

            "#043F哎，你是学生会长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146 op#A
        0x10,
        "#1775F#5P#10A我叫雷克特。\x02",
    )


    def lambda_3234():
        OP_8E(0xFE, 0xB248, 0x0, 0xB3B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3234)
    WaitChrThread(0x10, 0x1)
    SetChrSubChip(0x105, 0)

    def lambda_3259():
        OP_8E(0xFE, 0xAC94, 0x0, 0xB3B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3259)
    WaitChrThread(0x10, 0x1)
    CloseMessageWindow()

    ChrTalk(    #147
        0x10,
        (
            "#1773F#5P哦哦，\x01",
            "今天的晚霞真美啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x105,
        (
            "#044F#5P啊…………\x01",
            "是，是的……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x10, 43820, -300, 46000, 270)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 20)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(800)

    ChrTalk(    #149
        0x10,
        "#1770F#6P怎么样，对这个学院的感想。\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)
    Fade(300)
    SetChrSubChip(0x105, 2)
    Sleep(500)

    ChrTalk(    #150
        0x105,
        (
            "#044F#11P……啊，是。\x02\x03",

            "#543F嗯、嗯……\x02\x03",

            "是个非常好的地方。\x01",
            "设备也很齐全……\x02\x03",

            "#542F对想专心于学业的人来说\x01",
            "是个很棒的环境。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)

    ChrTalk(    #151
        0x10,
        (
            "#1777F#6P………………哼哼……\x02\x03",

            "#1771F#3S哈哈哈！#2000W #2S\x01",
            "#20W……原来如此，这样的回答吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x105,
        (
            "#044F#11P？？？\x02\x03",

            "#043F哎，那、那个……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x10,
        (
            "#1775F#6P哎呀，\x01",
            "我是问校园生活方面啦。\x02\x03",

            "#1779F看起来\x01",
            "你并不是很开心的样子？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #154
        0x105,
        (
            "#049F#5P嗯、嗯…………\x02\x03",

            "#047F那个，\x01",
            "因、因为还不习惯，\x01",
            "也有一点不太顺利的事……\x02\x03",

            "#042F但是我会努力的……！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0xAA, 1650, 0x18, 0x1B, 0x12C, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #155
        0x10,
        (
            "#1774F#6P唉…………你啊……\x02\x03",

            "#1773F难道就是为了做这种事\x01",
            "才来这里的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_59()
    Fade(200)
    SetChrSubChip(0x105, 2)
    Sleep(400)

    ChrTalk(    #156
        0x105,
        "#044F#11P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x10,
        "#1775F#6P呼…………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #158
        0x10,
        (
            "#1778F#6P哎呀～，你可真是个死板的人啊～。\x02\x03",

            "#1771F就不会偶尔放松一下吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #159
        0x105,
        (
            "#043F#11P那个，哎，什么……！？\x01",
            "我、我……那、那个……\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x10, 19)
    SetChrSubChip(0x10, 3)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 44120, -300, 46000, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #160
        0x10,
        (
            "#1770F#6P我啊……\x01",
            "姑且也算是学生会长嘛～。\x02\x03",

            "#1775F怎么样？　学生会。\x01",
            "还挺好玩的哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x105,
        "#044F#11P…………这是在邀请吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x10,
        (
            "#1772F#6P不如和我们一起流淌\x01",
            "青春的汗水吧！？（毫无任何语气地）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x105,
        "#042F#11P……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10,
        "#1771F#6P咦，没听到吗。\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #165
        0x105,
        (
            "#049F#5P（这、这个人……\x01",
            "  既然是学生会长\x01",
            "  应该是很厉害的人吧。）\x02\x03",

            "（但、但是……\x01",
            "  呃～怎么说呢……）\x02\x03",

            "#043F（不如说是，那个，\x01",
            "　完全不可靠的感觉……）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #166
        0x10,
        (
            "#1776F#6P唉……说起来，\x01",
            "米丽亚一直要我去上课真是烦死人了。\x02\x03",

            "#1775F下次该怎么\x01",
            "瞒过去才好呢～……\x02\x03",

            "米丽亚那家伙\x01",
            "一生气就会发飙……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #167
        0x105,
        (
            "#047F#5P（……看起来果然\x01",
            "　不可靠…………）\x02\x03",

            "#043F…………那、那个。\x01",
            "我差不多该回宿舍了……\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x105, 44180, 0, 44580, 270)
    ClearChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    Sleep(500)
    Sleep(200)

    ChrTalk(    #168
        0x10,
        "#1774F#6P你站在这个角度……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(200)
    SetChrSubChip(0x10, 3)
    Sleep(400)

    ChrTalk(    #169
        0x10,
        "#1772F#6P#3S……让我看到了！#2S\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_8C(0x105, 350, 600)
    SetChrFlags(0x105, 0x1000)

    def lambda_3B6B():
        OP_8F(0xFE, 0xAC94, 0x0, 0xA924, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3B6B)
    WaitChrThread(0x105, 0x1)
    ClearChrFlags(0x105, 0x1000)
    Sleep(500)

    ChrTalk(    #170
        0x105,
        "#046F#11P#3S失陪了！#2S\x02",
    )

    OP_7C(0x0, 0x50, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_3BCA():
        OP_6D(43820, -2000, 41200, 1000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3BCA)

    def lambda_3BE2():
        OP_6B(2940, 1000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3BE2)

    def lambda_3BF2():
        OP_8E(0xFE, 0x98E4, 0xFFFFF830, 0xA924, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3BF2)
    WaitChrThread(0x105, 0x1)
    SetChrSubChip(0x10, 2)

    def lambda_3C17():
        OP_8E(0xFE, 0x98E4, 0xFFFFF830, 0x9984, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3C17)

    ChrTalk(    #171 op#A
        0x10,
        "#1775F#5P#15A那边是男生宿舍。\x02",
    )

    Sleep(1000)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x105, 0x1)

    ChrTalk(    #172
        0x105,
        "#047F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 340, 400)
    Sleep(300)

    def lambda_3CBA():
        OP_6D(43820, -2000, 48200, 4000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3CBA)

    def lambda_3CD2():
        OP_8E(0xFE, 0x98E4, 0xFFFFF830, 0xDF20, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3CD2)
    WaitChrThread(0x105, 0x1)

    def lambda_3CF2():
        OP_8E(0xFE, 0x8430, 0xFFFFF830, 0xDF20, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3CF2)
    Sleep(1000)
    Fade(100)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #173
        0x10,
        (
            "#1775F#12P哎呀哎呀……\x02\x03",

            "#1770F真是要人照顾的家伙……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #174
        "\x07\x00数日之后，放学后…………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x800)
    OP_A2(0x2504)
    OP_A2(0x2F6B)
    NewScene("ED6_DT21/T2511   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_30_2ED3 end

    def Function_31_3DC4(): pass

    label("Function_31_3DC4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(40060, -2000, 32479, 0)
    OP_67(0, 7700, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(135000, 0)
    OP_6E(304, 0)
    SetChrChipByIndex(0x105, 14)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x105, 39560, -1750, 32980, 0)
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x11, 34760, 0, 24860, 0)
    SetChrPos(0x12, 33640, 0, 24860, 0)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)

    def lambda_3E7E():
        OP_67(0, 5700, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_3E7E)
    FadeToBright(2000, 0)

    def lambda_3E9F():
        OP_8E(0xFE, 0x87C8, 0xFFFFF830, 0x84D0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3E9F)
    Sleep(150)

    def lambda_3EBF():
        OP_8E(0xFE, 0x8368, 0xFFFFF830, 0x823C, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3EBF)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)

    def lambda_3EE4():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3EE4)
    Sleep(100)
    TurnDirection(0x12, 0x105, 400)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)
    OP_62(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_3F2C():
        OP_8E(0xFE, 0x9240, 0xFFFFF830, 0x84D0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3F2C)
    Sleep(100)

    def lambda_3F4C():
        OP_8E(0xFE, 0x8F20, 0xFFFFF830, 0x823C, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3F4C)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #175
        0x11,
        (
            "#643F#6P咦……科洛丝？\x02\x03",

            "你在这种地方做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105)
    Sleep(500)
    SetChrSubChip(0x105, 1)
    Sleep(300)

    ChrTalk(    #176
        0x105,
        (
            "#044F#5P啊，乔儿同学、汉斯同学……\x02\x03",

            "#542F嗯，\x01",
            "因为正好有点空……\x02",
        )
    )

    Jump("loc_4018")

    label("loc_4018")

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #177
        0x12,
        "#733F#12P所以就在预习吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x11,
        (
            "#643F#6P哇，好厉害啊。\x02\x03",

            "#648F不愧是通过了\x01",
            "超级难的插班考试的人啊～……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x105,
        (
            "#043F#5P嗯、嗯……\x02\x03",

            "其实也没那么………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x11,
        (
            "#644F#6P啊，对了。\x02\x03",

            "我说，科洛丝，\x01",
            "你见到雷克特学长了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x105,
        (
            "#044F#5P雷克特学长吗……？\x02\x03",

            "#042F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #182
        0x11,
        (
            "#647F#6P那、那个…………\x02\x03",

            "#1892F难不成\x01",
            "那家伙对你做了什么……？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #183
        0x105,
        (
            "#047F……………………不是。\x02\x03",

            "#047F没什么大不了的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_426B():
        OP_6D(40830, -2000, 32580, 600)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_426B)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_42A7():

        label("loc_42A7")

        TurnDirection(0xFE, 0x105, 500)
        OP_48()
        Jump("loc_42A7")

    QueueWorkItem2(0x11, 2, lambda_42A7)

    def lambda_42B8():

        label("loc_42B8")

        TurnDirection(0xFE, 0x105, 500)
        OP_48()
        Jump("loc_42B8")

    QueueWorkItem2(0x12, 2, lambda_42B8)

    def lambda_42C9():
        OP_8F(0xFE, 0x9BB4, 0xFFFFF830, 0x8A20, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_42C9)

    def lambda_42E4():
        OP_8F(0xFE, 0x97CC, 0xFFFFF830, 0x8A20, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_42E4)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    OP_44(0x11, 0x2)
    OP_44(0x12, 0x2)
    WaitChrThread(0x21, 0x0)
    Sleep(300)

    ChrTalk(    #184
        0x11,
        (
            "#1893F#6P实、实在对不起！\x02\x03",

            "我们的学生会长\x01",
            "又给你添麻烦了……！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x12,
        (
            "#734F#6P真是不知道该怎么向你道歉才好。\x02\x03",

            "为了保证以后绝对不会再发生这种事，\x01",
            "我会彻底地管教他……！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x11,
        (
            "#645F#6P关于这件事\x01",
            "请您大人大量饶了他吧……！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)
    OP_96(0x105, 0x9A88, 0xFFFFF830, 0x83A4, 0x64, 0xFA0)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    Sleep(500)

    ChrTalk(    #187
        0x105,
        (
            "#043F#11P那、那个……\x01",
            "我并没打算追究什么……\x02\x03",

            "#045F……呃，那个，\x01",
            "真的是没什么大不了的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x11,
        "#643F#6P咦，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x105,
        (
            "#542F#11P是、是的。\x02\x03",

            "……只是跟我\x01",
            "开了点玩笑而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x11,
        (
            "#645F#6P呼～，吓死我了……\x02\x03",

            "刚才那一瞬间，\x01",
            "我眼前真是一片漆黑呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x12,
        (
            "#734F#6P真是的。\x01",
            "就像脊髓反射一般地道歉了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x11,
        "#645F#1P呼～………………\x02",
    )


    ChrTalk(    #193
        0x12,
        "#734F呼～………………\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #194
        0x105,
        "#045F#11P哈，哈哈…………\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #195
        0x105,
        (
            "#049F#11P…………那个……\x02\x03",

            "#043F雷克特学长\x01",
            "经常会惹出\x01",
            "什么麻烦来吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x11,
        (
            "#640F#6P嗯？　啊啊…………\x02\x03",

            "#645F与其说惹出麻烦，\x01",
            "不如说他那性格本身就是个问题啦。\x02\x03",

            "这几个星期内\x01",
            "都不知道逃跑过多少次了。\x02\x03",

            "#646F而且还到处\x01",
            "给别人添麻烦。\x02\x03",

            "不断有人来投诉，\x01",
            "我们真是应付得焦头烂额……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x12,
        (
            "#734F#6P『尽一切可能迅速拘捕』\x01",
            "是我们学生会的基本方针。\x02\x03",

            "不过现在感觉也不像是学生会了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x105,
        "#049F#11P是这样吗……\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #199
        0x11,
        "#643F#6P科洛丝，怎么了？\x02",
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #200
        0x105,
        (
            "#045F#11P不，没有。\x01",
            "没什么事。\x02\x03",

            "#044F啊，说起来……\x02\x03",

            "雷克特学长，\x01",
            "刚才好像在\x01",
            "社团大楼的屋顶上睡觉呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #201
        0x11,
        "#642F#6P咦，这是真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x12,
        (
            "#733F#6P屋顶上吗……\x01",
            "真是没注意到啊……\x02\x03",

            "#731F科洛丝，亏你找得到呢。\x01",
            "这次欠你个人情！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x105,
        (
            "#045F#11P啊，是……\x02\x03",

            "#540F（其实是基库\x01",
            "  找到的……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A23():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4A23)
    Sleep(200)
    TurnDirection(0x12, 0x11, 500)
    Sleep(300)

    ChrTalk(    #204
        0x11,
        (
            "#1891F#5P汉斯，\x01",
            "这次一定要抓住那家伙！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x12,
        "#732F#12P好。\x02",
    )

    CloseMessageWindow()

    def lambda_4A8F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_4A8F)
    Sleep(200)
    OP_8C(0x12, 180, 500)
    Sleep(300)

    ChrTalk(    #206
        0x11,
        (
            "#641F#6P谢谢哦，科洛丝。\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x12,
        "#730F#6P那就回头见！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x105,
        "#542F#11P啊，好的。\x02",
    )

    CloseMessageWindow()

    def lambda_4B23():

        label("loc_4B23")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_4B23")

    QueueWorkItem2(0x105, 2, lambda_4B23)

    def lambda_4B34():
        OP_8E(0xFE, 0x8908, 0xFFFFF830, 0x8A20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4B34)
    Sleep(100)

    def lambda_4B54():
        OP_8E(0xFE, 0x8908, 0xFFFFF830, 0x8A20, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4B54)
    WaitChrThread(0x12, 0x1)

    def lambda_4B74():
        OP_8E(0xFE, 0x8908, 0xFFFFF830, 0x5F50, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_4B74)
    WaitChrThread(0x11, 0x1)

    def lambda_4B94():
        OP_8E(0xFE, 0x8908, 0xFFFFF830, 0x5F50, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4B94)
    Sleep(2000)
    OP_44(0x105, 0x2)
    OP_8C(0x105, 180, 400)
    Sleep(1500)

    def lambda_4BC4():
        OP_6D(40800, -2000, 32500, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_4BC4)
    WaitChrThread(0x21, 0x0)
    Sleep(500)

    ChrTalk(    #209
        0x105,
        (
            "#047F#6P雷克特学长……\x02\x03",

            "#049F看起来，\x01",
            "果然是个随便的人啊……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #210
        0x105,
        (
            "#047F#6P（不过，那个时候确实……）\x02\x03",

            "（……是这样问我的吧……？）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4CAE():
        OP_6B(2600, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_4CAE)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x21, 0xFF)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #211
        "\x07\x0C\x18你难道就是为了做这种事才来这里的吗？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(1000)
    Call(0, 32)
    Return()

    # Function_31_3DC4 end

    def Function_32_4D2B(): pass

    label("Function_32_4D2B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(164)
    OP_11(0xFF, 0xFF, 0xFF, 0x9470, 0x1C138, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x11, 31900, 0, 19000, 90)
    SetChrPos(0x12, 31900, 0, 19000, 90)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 48740, 8700, 20900, 270)
    OP_62(0x10, 0xFFFFFEA2, 1800, 0x8, 0x9, 0xC8, 0x0)
    SetChrChipByIndex(0x10, 19)
    SetChrSubChip(0x10, 0)
    OP_6D(49100, 500, 19000, 0)
    OP_67(0, 4240, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(90000, 0)
    OP_6E(350, 0)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_4E11():
        OP_6D(47600, 9000, 22000, 4000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_4E11)

    def lambda_4E29():
        OP_67(0, 8840, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4E29)

    def lambda_4E41():
        OP_6C(135000, 4000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_4E41)

    def lambda_4E51():
        OP_6E(250, 4000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_4E51)
    WaitChrThread(0x21, 0x0)
    Sleep(1000)

    def lambda_4E6B():
        OP_6D(56500, 9000, 18360, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_4E6B)

    def lambda_4E83():
        OP_67(0, 7220, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_4E83)

    def lambda_4E9B():
        OP_6C(110000, 3000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_4E9B)

    def lambda_4EAB():
        OP_6E(264, 3000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_4EAB)
    WaitChrThread(0x21, 0x0)
    Sleep(500)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x11, 60500, 6800, 16860, 290)
    SetChrPos(0x12, 60500, 6800, 16860, 290)
    OP_63(0x10)
    SetChrFlags(0x10, 0x8)
    OP_96(0x11, 0xEC54, 0x1E78, 0x41DC, 0x3E8, 0xFA0)
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #212
        0x11,
        "#1891F（………………有了！！）\x02",
    )

    CloseMessageWindow()
    OP_96(0x11, 0xEC54, 0x1A90, 0x41DC, 0xA, 0xFA0)
    Sleep(500)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x11, 0xE6DC, 0x2328, 0x4498, 0xBB8, 0x1194)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_4FAF():
        OP_6D(51700, 9000, 20600, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_4FAF)

    def lambda_4FC7():
        OP_6C(65000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_4FC7)

    def lambda_4FD7():
        OP_8E(0xFE, 0xC92C, 0x2328, 0x5078, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4FD7)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x12, 0xE6DC, 0x2328, 0x4498, 0xBB8, 0x1388)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_5013():
        OP_8E(0xFE, 0xC8F0, 0x2328, 0x4BDC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5013)
    WaitChrThread(0x11, 0x1)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    WaitChrThread(0x12, 0x1)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #213
        0x11,
        "#643F啊………………！\x02",
    )

    CloseMessageWindow()
    OP_43(0x11, 0x3, 0x0, 0x22)
    OP_43(0x12, 0x3, 0x0, 0x23)
    WaitChrThread(0x12, 0x3)

    ChrTalk(    #214
        0x12,
        "#733F不、不在…………！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x11,
        (
            "#642F刚、刚才\x01",
            "还在这里的啊！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x12,
        "#732F怎、怎么逃走的啊！？\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #217
        0x11,
        "#1891F唉，到底跑到哪里去了！\x02",
    )

    CloseMessageWindow()

    def lambda_515C():
        OP_8E(0xFE, 0xC350, 0x2328, 0x5208, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_515C)
    Sleep(100)
    OP_43(0x12, 0x3, 0x0, 0x23)
    WaitChrThread(0x11, 0x1)
    OP_43(0x11, 0x3, 0x0, 0x22)
    WaitChrThread(0x11, 0x3)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #218
        0x11,
        "#643F#5P啊……\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x105, 33380, -2000, 35840, 180)
    OP_43(0x105, 0x3, 0x0, 0x24)

    def lambda_51E3():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_51E3)

    def lambda_51F1():
        OP_8C(0xFE, 270, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_51F1)

    def lambda_51FF():
        OP_6D(46060, 9000, 21580, 5000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_51FF)

    def lambda_5217():
        OP_6C(324000, 5000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_5217)
    Sleep(3000)

    def lambda_522C():
        OP_8F(0xFE, 0xC350, 0x2328, 0x4DE4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_522C)
    WaitChrThread(0x21, 0x0)
    Sleep(300)

    ChrTalk(    #219
        0x11,
        "#640F是科洛丝……\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #220
        0x11,
        (
            "#641F对了，\x01",
            "问问科洛丝看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x12,
        (
            "#733F#6P嗯？　啊啊…………\x02\x03",

            "#730F说不定是个好主意。\x02\x03",

            "刚才她也看穿了\x01",
            "雷克特学长隐藏的地方……\x02\x03",

            "头脑聪明的科洛丝\x01",
            "一定能成为战斗力吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x11,
        "#644F好，去看看吧！\x02",
    )

    CloseMessageWindow()
    OP_44(0x11, 0x2)
    OP_44(0x12, 0x2)

    def lambda_5383():
        OP_8E(0xFE, 0xE038, 0x2328, 0x526C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5383)
    Sleep(400)

    def lambda_53A3():
        OP_8E(0xFE, 0xE038, 0x2328, 0x4DE4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_53A3)
    Sleep(400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x105, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    Call(0, 33)
    Return()

    # Function_32_4D2B end

    def Function_33_53D9(): pass

    label("Function_33_53D9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_11(0xFF, 0xFF, 0xFF, 0x9470, 0x1C138, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_6D(53100, 0, 27240, 0)
    OP_67(0, 6260, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(120000, 0)
    OP_6E(306, 0)
    SetChrPos(0x105, 43360, 0, 28060, 90)
    SetChrPos(0x12, 52820, 500, 22500, 350)
    SetChrPos(0x11, 53020, 500, 22500, 350)

    def lambda_5487():
        OP_8E(0xFE, 0xC4B8, 0x0, 0x6D9C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5487)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_70(0x7, 0x3C)
    OP_73(0x0)

    def lambda_54C1():
        OP_8E(0xFE, 0xCE54, 0x0, 0x6EB4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_54C1)
    Sleep(400)

    def lambda_54E1():
        OP_8E(0xFE, 0xCF1C, 0x0, 0x6A40, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_54E1)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)
    OP_23(0x6)
    WaitChrThread(0x12, 0x1)

    def lambda_551C():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_551C)
    WaitChrThread(0x11, 0x1)

    def lambda_552F():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_552F)

    ChrTalk(    #223
        0x12,
        "#731F#5P……科洛丝！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)

    ChrTalk(    #224
        0x105,
        (
            "#044F#12P乔儿同学，汉斯同学……？\x02\x03",

            "难道……\x01",
            "他不在屋顶上吗？\x02",
        )
    )

    Jump("loc_55B8")

    label("loc_55B8")

    CloseMessageWindow()

    ChrTalk(    #225
        0x11,
        (
            "#647F#5P不、不是，\x01",
            "虽然是在那里找到了……\x02\x03",

            "#646F但是一瞬间没看到\x01",
            "就给他逃掉了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x12,
        (
            "#734F#5P真奇怪啊……\x02\x03",

            "在那屋顶上，\x01",
            "应该是\x01",
            "无处可逃才对啊……\x02",
        )
    )

    Jump("loc_5674")

    label("loc_5674")

    CloseMessageWindow()

    ChrTalk(    #227
        0x105,
        (
            "#043F#12P啊…………\x01",
            "屋顶上是吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x11,
        (
            "#640F#5P所以，那个……\x02\x03",

            "科洛丝，你对那家伙的藏身之处\x01",
            "有没有什么……线索？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x12,
        (
            "#732F#5P无论多细小都没关系。\x02\x03",

            "…………拜托了！\x01",
            "想到的话就告诉我们吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x105,
        (
            "#044F#12P啊，好的…………\x02\x03",

            "#047F（看来真的很烦恼呢……）\x02\x03",

            "#542F那么，就……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #231
        0x11,
        (
            "#643F#5P科洛丝，\x01",
            "你知道他在哪里吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x105,
        (
            "#045F#12P哎……不是我……\x02\x03",

            "我问一下基库看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(50)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x105, 345, 400)
    Sleep(500)

    ChrTalk(    #233
        0x105,
        "#042F#11P……基库！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x13, 0x4)
    SetChrPos(0x13, 40440, 6000, 40960, 180)
    OP_22(0x197, 0x0, 0x64)
    Sleep(500)
    OP_22(0x8C, 0x0, 0x64)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_8E(0x13, 0xC030, 0x514, 0x6A7C, 0x2328, 0x0)
    OP_97(0x13, 0xC4B8, 0x6D9C, 0xFFFD8F00, 0x157C, 0x1)
    SetChrChipByIndex(0x13, 15)
    SetChrSubChip(0x13, 0)
    OP_8C(0x13, 225, 400)
    OP_8F(0x13, 0xC56C, 0xC8, 0x6EC8, 0x3E8, 0x0)
    Fade(500)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x105, 13)
    SetChrSubChip(0x105, 0)
    OP_0D()
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #234
        0x11,
        "#643F哇、哇……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x12,
        (
            "#733F#5P白色的隼……！？\x02\x03",

            "是科洛丝的宠物吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x105,
        (
            "#045F#12P不是，基库是……\x02\x03",

            "#542F可以说是我的朋友啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x13,
        "#311F#5P啾～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x11,
        (
            "#641F#5P哈、哈哈哈……\x01",
            "……是这样啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x105,
        (
            "#042F#12P基库，\x01",
            "你见到雷克特学长了吗？\x02\x03",

            "喏，就是之前睡在屋顶上的\x01",
            "那个吊儿郎当的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x13,
        (
            "#310F#5P啾？\x02\x03",

            "啾，啾——。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x105,
        (
            "#044F#12P咦…………？\x01",
            "跟丢了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x13,
        "#310F#5P啾、啾～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x105,
        (
            "#045F#12P没关系啦，基库。\x01",
            "别在意。\x02\x03",

            "#542F对不起哦，谢谢你了。\x02",
        )
    )

    Jump("loc_5BDD")

    label("loc_5BDD")

    CloseMessageWindow()

    ChrTalk(    #244
        0x13,
        "#311F#5P啾……\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    OP_0D()

    def lambda_5C1A():

        label("loc_5C1A")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_5C1A")

    QueueWorkItem2(0x11, 2, lambda_5C1A)

    def lambda_5C2B():

        label("loc_5C2B")

        TurnDirection(0xFE, 0x13, 500)
        OP_48()
        Jump("loc_5C2B")

    QueueWorkItem2(0x12, 2, lambda_5C2B)
    OP_22(0x8C, 0x0, 0x64)
    OP_8F(0x13, 0xC65C, 0x514, 0x7058, 0x3E8, 0x0)
    SetChrChipByIndex(0x13, 11)
    SetChrSubChip(0x13, 0)
    OP_8C(0x13, 300, 400)
    OP_8E(0x13, 0x9F4C, 0x1770, 0xAA64, 0x2328, 0x0)
    OP_44(0x11, 0x2)
    OP_44(0x12, 0x2)
    SetChrFlags(0x13, 0x80)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #245
        0x105,
        (
            "#047F#12P竟然连基库\x01",
            "也无法捕捉到他……\x02\x03",

            "#042F真是个相当敏捷的人啊……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5D01():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5D01)
    Sleep(200)
    TurnDirection(0x11, 0x105, 500)

    ChrTalk(    #246
        0x12,
        (
            "#735F#5P……不、不对，比起这个来\x01",
            "你能跟隼说话更令人吃惊啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x11,
        (
            "#645F#5P真、真是的……\x02\x03",

            "#649F科洛丝还真是个\x01",
            "神秘的转学生啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 75, 400)
    Sleep(300)

    ChrTalk(    #248
        0x105,
        "#043F#12P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x11,
        (
            "#643F#5P啊，这不是什么坏话啦。\x02\x03",

            "#648F只是觉得你很厉害……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x12,
        (
            "#730F#5P嗯，的确是特殊能力啊。\x02\x03",

            "#734F不过现在的关键还是\x01",
            "无法找到雷克特学长……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x105,
        (
            "#049F#12P…………是啊……\x02\x03",

            "#047F既然基库看不见，\x01",
            "那他是不是在屋里呢。\x02\x03",

            "#040F恐怕是这个时间段\x01",
            "没有人去的地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x11,
        (
            "#642F#5P原、原来如此……\x01",
            "这样的话大概就能限定范围了。\x02\x03",

            "#647F嗯，首先是空教室，\x01",
            "加上宿舍和礼堂……然后是旧校舍……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x12,
        (
            "#734F#5P呜呜，\x01",
            "这样范围还是很大啊…………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x105,
        (
            "#045F#12P那、那个。\x02\x03",

            "#542F……我也来帮忙好吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x11,
        (
            "#643F#5P咦…………可以吗？\x02\x03",

            "科洛丝，\x01",
            "你没有什么要紧的事要做吗……\x02",
        )
    )

    Jump("loc_6071")

    label("loc_6071")

    CloseMessageWindow()

    ChrTalk(    #256
        0x105,
        (
            "#543F#12P没有，\x01",
            "本来只是想参观一下社团来着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x12,
        (
            "#735F#5P唔，\x01",
            "拜托科洛丝的话有点过意不去……\x02\x03",

            "#730F不过你能帮忙的话就太好了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x11,
        (
            "#644F#5P反倒是我们\x01",
            "巴不得麻烦你呢。\x02\x03",

            "科洛丝，真的没问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x105,
        (
            "#041F#12P嗯。\x01",
            "没关系的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x11,
        (
            "#641F太好了，\x01",
            "那么就三个人一起去找吧！\x02\x03",

            "#1891F这次一定要绑着\x01",
            "他的脖子把他拉回来！\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x11, 0x80)
    AddParty(0x3A, 0xFF, 0xFF)
    SetChrFlags(0x12, 0x80)
    AddParty(0x51, 0xFF, 0xFF)
    OP_6D(50660, 0, 28060, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x105, 50660, 0, 28060, 270)
    SetChrPos(0x13B, 50360, 0, 28060, 90)
    SetChrPos(0x152, 50360, 0, 28060, 90)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x13B, 65535)
    SetChrChipByIndex(0x152, 65535)
    SetChrSubChip(0x105, 0)
    SetChrSubChip(0x13B, 0)
    SetChrSubChip(0x152, 0)
    OP_69(0x0, 0x0)
    OP_71(0x1007, 0x0)
    ExitThread()
    OP_71(0x1008, 0x0)
    ExitThread()
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_33_53D9 end

    def Function_34_62B4(): pass

    label("Function_34_62B4")

    OP_8C(0x11, 335, 500)
    Sleep(600)
    OP_8C(0x11, 245, 500)
    Sleep(600)
    OP_8C(0x11, 290, 500)
    Return()

    # Function_34_62B4 end

    def Function_35_62D4(): pass

    label("Function_35_62D4")

    Sleep(300)
    OP_8C(0x12, 245, 500)
    Sleep(600)
    OP_8C(0x12, 335, 500)
    Sleep(600)
    OP_8C(0x12, 290, 500)
    Return()

    # Function_35_62D4 end

    def Function_36_62F9(): pass

    label("Function_36_62F9")


    def lambda_62FF():
        OP_8E(0xFE, 0x8264, 0x0, 0x7120, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_62FF)
    WaitChrThread(0x105, 0x1)

    def lambda_631F():
        OP_8E(0xFE, 0xCEE0, 0x0, 0x7120, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_631F)
    WaitChrThread(0x105, 0x1)
    Return()

    # Function_36_62F9 end

    def Function_37_633A(): pass

    label("Function_37_633A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrPos(0x12, 52640, 500, 22500, 350)
    SetChrPos(0x11, 52840, 500, 22500, 350)
    SetChrPos(0x105, 53320, 500, 22500, 350)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    OP_6D(54100, 0, 27240, 0)
    OP_67(0, 6260, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(120000, 0)
    OP_6E(306, 0)
    OP_6F(0x1, 60)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    OP_72(0x1007, 0x0)
    ExitThread()
    OP_70(0x7, 0x3C)
    OP_73(0x0)

    def lambda_63FE():
        OP_8E(0xFE, 0xCE68, 0x0, 0x724C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_63FE)
    Sleep(500)

    def lambda_641E():
        OP_8E(0xFE, 0xCDA0, 0x0, 0x6810, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_641E)
    Sleep(1000)

    def lambda_643E():
        OP_8E(0xFE, 0xD048, 0x0, 0x69C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_643E)
    WaitChrThread(0x12, 0x1)
    OP_72(0x7, 0x8)
    ExitThread()
    OP_6F(0x7, 60)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x7, 0x0)

    def lambda_6477():
        OP_8E(0xFE, 0xCB34, 0x0, 0x6FE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_6477)
    WaitChrThread(0x11, 0x1)

    def lambda_6497():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6497)
    WaitChrThread(0x12, 0x1)

    def lambda_64AA():
        OP_8C(0xFE, 120, 500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_64AA)
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #261
        0x11,
        "#645F#6P啊啊，好累……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x12,
        (
            "#735F#6P找雷克特学长很累，\x01",
            "他去出席学生会也会把人弄得很累……\x02\x03",

            "#738F唯一的救赎\x01",
            "就是能见到露西学姐了。\x02\x03",

            "因为考试期间\x01",
            "都没有见到嘛……㈱\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x12, 400)
    Sleep(300)

    ChrTalk(    #263
        0x11,
        (
            "#649F#5P…………喂喂，\x01",
            "今天早上你不是还做过必胜祈祷，\x01",
            "难道没有见到吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x12, 400)
    Sleep(300)

    ChrTalk(    #264
        0x105,
        (
            "#041F#11P呵呵，\x01",
            "我也看到了哦？\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_71(0x7, 0x8)
    ExitThread()
    OP_70(0x7, 0x3C)
    OP_73(0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 53060, 500, 22500, 350)
    OP_4A(0x10, 255)

    def lambda_6647():
        OP_8E(0xFE, 0xCF44, 0x1F4, 0x5E74, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6647)
    WaitChrThread(0x10, 0x1)
    Sleep(300)

    ChrTalk(    #265
        0x10,
        (
            "#1773F#11P你、你们……\x02\x03",

            "#1771F好像很闲嘛。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_66AA():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_66AA)
    Sleep(100)

    def lambda_66BD():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_66BD)
    Sleep(100)
    TurnDirection(0x12, 0x10, 400)
    Sleep(300)
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #266
        0x11,
        (
            "#646F#6P至少比学长要忙。\x02\x03",

            "现在要去找各社团的部长\x01",
            "制订预算计划才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x10,
        (
            "#1775F#11P是～吗。\x01",
            "那就交给科洛丝吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x105,
        "#044F#6P咦…………？\x02",
    )

    CloseMessageWindow()

    def lambda_67A2():
        OP_8E(0xFE, 0xD00C, 0x0, 0x6554, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_67A2)
    WaitChrThread(0x10, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #269
        "\x07\x05雷克特把信封交给了科洛丝。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #270
        0x105,
        "#045F#6P哎……这个是……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x10,
        (
            "#1774F#11P这东西好像\x01",
            "必须交给卢安市长才行。\x02\x03",

            "#1779F雷欧很啰嗦的。\x01",
            "……科洛丝，你去吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x11,
        (
            "#647F#6P……这个，\x01",
            "本来是雷克特学长的工作吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x10,
        "#1771F#11P不是～啊，怎～么～可～能……\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #274
        0x10,
        (
            "#1773F#11P科洛丝，你……\x02\x03",

            "头上粘着羽毛呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x105,
        "#044F#6P咦……！\x02",
    )

    CloseMessageWindow()

    def lambda_6984():
        OP_8E(0xFE, 0xD00C, 0x0, 0x6720, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6984)
    WaitChrThread(0x10, 0x1)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #276
        "\x07\x05雷克特掸了掸科洛丝的头。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_69EA():
        OP_8F(0xFE, 0xD00C, 0x0, 0x6554, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_69EA)
    WaitChrThread(0x10, 0x1)
    Sleep(300)

    ChrTalk(    #277
        0x10,
        (
            "#1775F#11P……是基库那家伙吧。\x02\x03",

            "#1776F说起来，\x01",
            "那家伙好像说过\x01",
            "差不多该到换毛的季节了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x105,
        (
            "#540F#6P（什、什么时候\x01",
            "　粘上的呢……）\x02\x03",

            "（难道考试的时候也是？\x01",
            "　好、好丢脸……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #279
        0x105,
        (
            "#044F#6P学长，\x01",
            "你知道基库的事吗！？\x02\x03",

            "而、而且说什么“那家伙好像说过”……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 500)
    Sleep(300)

    ChrTalk(    #280
        0x10,
        "#1775F#5P啊，那封信就拜托你了～。\x02",
    )

    CloseMessageWindow()

    def lambda_6B97():
        OP_8E(0xFE, 0xCF44, 0x1F4, 0x57E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6B97)
    WaitChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    OP_72(0x7, 0x8)
    ExitThread()
    OP_6F(0x7, 60)
    OP_22(0x7, 0x0, 0x64)
    OP_70(0x7, 0x0)
    Sleep(1300)

    ChrTalk(    #281
        0x105,
        (
            "#042F#5P（真是个\x01",
            "　奇怪的家伙呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x11)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #282
        0x11,
        (
            "#645F#6P科洛丝，那个……\x02\x03",

            "那家伙可是把工作\x01",
            "全部推给你了哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x12,
        (
            "#734F#6P还有，虽然难以启齿……\x02\x03",

            "你头上并没有粘着什么羽毛哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 350, 600)
    Sleep(300)

    ChrTalk(    #284
        0x105,
        (
            "#044F#11P#3S！！！#2S\x02\x03",

            "#540F又被戏弄了……\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #285
        0x11,
        (
            "#646F#6P好啦，科洛丝，\x01",
            "赶快追上去还给他啦。\x02\x03",

            "这种事情，\x01",
            "本来就不该科洛丝做的嘛！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x12,
        (
            "#735F#6P不，就算现在追上去\x01",
            "也不知道抓不抓得到他了……\x02\x03",

            "#736F是啊，有这个时间差的话，\x01",
            "少说也得用五个小时才能抓到了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0x105,
        (
            "#045F#11P那、那个……\x02\x03",

            "还是我去吧。\x01",
            "这样比较快……\x02\x03",

            "#542F只要交给\x01",
            "卢安市市长就可以了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x11,
        (
            "#645F#6P唉，\x01",
            "本来打算让科洛丝\x01",
            "帮我们的忙的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x105,
        "#045F#11P对不起，乔儿同学。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x11,
        (
            "#648F#6P哎呀，没什么没什么。\x02\x03",

            "#640F倒是科洛丝，你认识路吗？\x01",
            "卢安市长邸是在……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x105,
        (
            "#542F#11P啊，我知道。\x01",
            "以前我去过的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x11,
        "#643F#6P咦，是吗？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x12,
        (
            "#731F#6P科洛丝应该没问题吧。\x02\x03",

            "#730F不过也要小心魔兽哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x105,
        "#040F#11P好的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x11,
        (
            "#644F#6P那么，就在此暂时分别了。\x02\x03",

            "#648F待会儿见哦，科洛丝！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x12,
        "#730F#6P早点回来哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x105,
        "#041F#11P好的。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 345, 400)

    def lambda_70AB():
        OP_8E(0xFE, 0xCE68, 0x1F4, 0x86C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_70AB)
    Sleep(400)
    OP_8C(0x12, 345, 500)

    def lambda_70D2():
        OP_8E(0xFE, 0xCEE0, 0x0, 0x75BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_70D2)
    WaitChrThread(0x12, 0x1)
    OP_22(0x6, 0x0, 0x64)

    def lambda_70F7():
        OP_8E(0xFE, 0xCEE0, 0x1F4, 0x86C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_70F7)
    WaitChrThread(0x12, 0x1)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x1007, 0x0)
    ExitThread()
    OP_71(0x7, 0x8)
    ExitThread()
    OP_6F(0x1, 0)
    OP_6D(52800, 0, 27220, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x105, 52800, 0, 27220, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_37_633A end

    def Function_38_71A4(): pass

    label("Function_38_71A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 5)), scpexpr(EXPR_END)), "loc_724F")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(12760, 0, 44640, 0)
    OP_67(0, 7020, -10000, 0)
    OP_6B(2860, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x105, 15300, 0, 46000, 270)
    OP_0D()
    OP_72(0x1021, 0x0)
    ExitThread()
    OP_70(0x21, 0x3C)
    OP_73(0x21)

    def lambda_7217():
        OP_90(0xFE, 0xFFFFB1E0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7217)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x105, 0xFF)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T2100   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_732B")

    label("loc_724F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_72AD")

    ChrTalk(    #298
        0x105,
        (
            "#040F得去申请外出许可呢。\x02\x03",

            "去跟校长\x01",
            "说明一下情况吧。\x02",
        )
    )

    Jump("loc_72A9")

    label("loc_72A9")

    CloseMessageWindow()
    Jump("loc_732B")

    label("loc_72AD")


    ChrTalk(    #299
        0x105,
        (
            "#044F啊，这么说来……\x02\x03",

            "要出学院的时候\x01",
            "必须取得外出许可才行。\x02\x03",

            "#040F……去跟校长\x01",
            "说明一下情况吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_732B")

    TalkEnd(0xFF)
    Return()

    # Function_38_71A4 end

    def Function_39_732F(): pass

    label("Function_39_732F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #300
        "\x07\x00#3S雷克特～…………！！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x40)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x10, 45960, 0, 61200, 180)
    SetChrPos(0x11, 45960, 0, 61200, 180)
    SetChrPos(0x105, 61540, 0, 22500, 0)
    SetChrChipByIndex(0x105, 22)
    SetChrSubChip(0x105, 0)
    SetChrFlags(0x105, 0x8)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)
    OP_6D(45900, 0, 47400, 0)
    OP_67(0, 4500, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(45000, 0)
    OP_6E(356, 0)
    OP_1D(0xE)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_43(0x10, 0x3, 0x0, 0x28)
    Sleep(2000)
    OP_43(0x11, 0x3, 0x0, 0x29)
    Sleep(1000)

    def lambda_7444():
        OP_6D(45900, 0, 33400, 4000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_7444)
    Sleep(400)

    ChrTalk(    #301 op#A op#5
        0x11,
        (
            "#1891F#30A#6P今天一定要给我\x01",
            "好好地工作。\x05\x02\x03",

            "#18A死心吧！！\x02",
        )
    )

    WaitChrThread(0x21, 0x0)

    def lambda_74B2():
        OP_6D(62500, 0, 23800, 3300)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_74B2)

    def lambda_74CA():
        OP_67(0, 6820, -10000, 3300)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_74CA)

    def lambda_74E2():
        OP_6C(120000, 3300)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_74E2)

    def lambda_74F2():
        OP_6B(2580, 3300)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_74F2)
    WaitChrThread(0x10, 0x3)
    WaitChrThread(0x11, 0x3)
    OP_22(0x7D, 0x0, 0x64)

    NpcTalk(    #302
        0x105,
        "声音",
        "#3S#2P呀……\x02",
    )

    Jump("loc_7529")

    label("loc_7529")


    ChrTalk(    #303
        0x11,
        "#3S#1P哇……！\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)

    def lambda_755A():
        OP_96(0xFE, 0xF064, 0x0, 0x63D8, 0x320, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_755A)
    OP_56(0x1)
    OP_59()
    WaitChrThread(0x11, 0x1)

    def lambda_7580():
        OP_6D(60880, 0, 22420, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_7580)

    def lambda_7598():
        OP_67(0, 6600, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_7598)

    def lambda_75B0():
        OP_6C(220000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_75B0)

    def lambda_75C0():
        OP_6B(2260, 2000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_75C0)
    Sleep(700)
    ClearChrFlags(0x105, 0x8)
    Sleep(150)
    SetChrFlags(0x105, 0x800)
    WaitChrThread(0x21, 0x0)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_75FB():
        OP_8E(0xFE, 0xF064, 0x0, 0x5FF0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_75FB)

    ChrTalk(    #304
        0x11,
        "#643F科、科洛丝！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #305
        0x11,
        "#642F没事吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x105,
        "#045F#5P……嗯、嗯。\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(700)
    ClearChrFlags(0x105, 0x800)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    SetChrPos(0x105, 61540, 0, 22500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #307
        0x105,
        (
            "#042F#5P夹击作战\x01",
            "看来失败了呢……\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #308
        0x10,
        "声音",
        "#6P哈哈，愚蠢的家伙们。\x02",
    )

    Jump("loc_76F6")

    label("loc_76F6")

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_7726():
        OP_6D(58540, 6300, 20240, 2000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_7726)

    def lambda_773E():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_773E)

    def lambda_7756():
        OP_6B(2160, 2000)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_7756)

    def lambda_7766():
        OP_8C(0xFE, 220, 400)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7766)
    Sleep(100)

    def lambda_7779():
        OP_8C(0xFE, 220, 400)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_7779)
    WaitChrThread(0x21, 0x0)
    Sleep(300)

    ChrTalk(    #309
        0x11,
        "#1891F#5P居、居然在那种地方……！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0x105,
        "#042F#5P真是敏捷啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x10,
        (
            "#1778F哼，\x01",
            "尽情懊悔自己思虑的浅薄吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 220, 500)

    def lambda_781D():
        OP_8E(0xFE, 0xD7DC, 0x2328, 0x404C, 0xED8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_781D)
    WaitChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x11, 61540, 0, 24560, 220)
    Fade(1000)
    OP_6D(60880, 0, 22420, 0)
    OP_67(0, 6600, -10000, 0)
    OP_6C(220000, 0)
    OP_6B(2260, 0)
    Sleep(1000)

    ChrTalk(    #312
        0x11,
        (
            "#646F#6P混帐…………！\x02\x03",

            "#1891F#3S说什么\x01",
            "莫名其妙的话～！！#2S\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 315, 500)

    def lambda_78E9():
        OP_8E(0xFE, 0xE3D0, 0x0, 0x6A7C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_78E9)
    WaitChrThread(0x11, 0x1)

    def lambda_7909():
        OP_8E(0xFE, 0xB504, 0x0, 0x6A7C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7909)
    Sleep(500)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    OP_8C(0x105, 40, 400)
    Sleep(500)
    WaitChrThread(0x11, 0x1)
    SetChrFlags(0x11, 0x80)

    ChrTalk(    #313
        0x105,
        (
            "#047F#5P……既然是那个学长，\x01",
            "肯定会弄出什么花样来吧。\x02\x03",

            "看起来不在，实际上在。\x01",
            "看起来在，实际上不在……\x02\x03",

            "#040F…………稍微找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_39_732F end

    def Function_40_79F4(): pass

    label("Function_40_79F4")


    def lambda_79FA():
        OP_8E(0xFE, 0xB388, 0x0, 0x733C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_79FA)
    WaitChrThread(0x10, 0x1)

    def lambda_7A1A():
        OP_8E(0xFE, 0xB964, 0x0, 0x6D60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7A1A)
    WaitChrThread(0x10, 0x1)

    def lambda_7A3A():
        OP_8E(0xFE, 0xEA74, 0x0, 0x6D60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7A3A)
    WaitChrThread(0x10, 0x1)

    def lambda_7A5A():
        OP_8E(0xFE, 0xF244, 0x0, 0x6590, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7A5A)
    WaitChrThread(0x10, 0x1)

    def lambda_7A7A():
        OP_8E(0xFE, 0xF244, 0x0, 0x4C2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7A7A)
    WaitChrThread(0x10, 0x1)
    SetChrPos(0x10, 59480, 9000, 21480, 40)
    Return()

    # Function_40_79F4 end

    def Function_41_7AA6(): pass

    label("Function_41_7AA6")


    def lambda_7AAC():
        OP_8E(0xFE, 0xB388, 0x0, 0x733C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7AAC)
    Sleep(1000)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(2000)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x11, 0x1)

    def lambda_7B11():
        OP_8E(0xFE, 0xB964, 0x0, 0x6D60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7B11)
    WaitChrThread(0x11, 0x1)

    def lambda_7B31():
        OP_8E(0xFE, 0xEA74, 0x0, 0x6D60, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7B31)
    Sleep(1500)
    OP_62(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    WaitChrThread(0x11, 0x1)

    def lambda_7B68():
        OP_8E(0xFE, 0xF244, 0x0, 0x6590, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7B68)
    WaitChrThread(0x11, 0x1)

    def lambda_7B88():
        OP_8E(0xFE, 0xF244, 0x0, 0x571C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7B88)
    WaitChrThread(0x11, 0x1)
    Return()

    # Function_41_7AA6 end

    def Function_42_7BA3(): pass

    label("Function_42_7BA3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_63(0x10)
    OP_6D(48450, 9000, 25150, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(300000, 0)
    OP_6E(304, 0)
    OP_11(0xF5, 0xF5, 0xFF, 0x9470, 0x2BF20, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, 50000, 9000, 20820, 90)
    SetChrPos(0x105, 56900, 9000, 19020, 270)
    OP_4A(0x10, 255)
    SetChrFlags(0x15, 0x80)
    FadeToBright(2000, 0)
    OP_0D()

    NpcTalk(    #314
        0x105,
        "声音",
        (
            "…………果然\x01",
            "是在这里呢。\x02",
        )
    )

    Jump("loc_7C6E")

    label("loc_7C6E")

    CloseMessageWindow()
    OP_59()
    OP_20(0xBB8)

    def lambda_7C7B():
        OP_6D(49430, 9000, 23670, 2000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7C7B)

    def lambda_7C93():
        OP_8F(0xFE, 0xCE40, 0x2328, 0x4E84, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7C93)
    WaitChrThread(0x105, 0x1)
    TurnDirection(0x105, 0x10, 400)
    WaitChrThread(0x105, 0x2)
    Sleep(500)

    ChrTalk(    #315
        0x10,
        (
            "#1770F#5P哦哦，科洛丝吗。\x02\x03",

            "#1775F今天也是好天气啊～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x105,
        (
            "#047F#6P……又说这种话。\x02\x03",

            "#042F既然有空就去工作吧。\x01",
            "你可是给大家添了很多麻烦哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x10,
        (
            "#1774F#5P不，我现在超级忙。\x02\x03",

            "#1772F我正在预测１０年后的天气。\x01",
            "你可别打扰我哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0x105,
        "#045F#6P（又在做莫名其妙的事情…… ）\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #319
        0x105,
        (
            "#542F#6P（不过，\x01",
            "  这种时候的雷克特学长……）\x02\x03",

            "（听人说话的时候\x01",
            "  倒是意外地认真啊。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7E93():
        OP_6D(48730, 9000, 23940, 1600)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7E93)

    def lambda_7EAB():
        OP_8E(0xFE, 0xC8F0, 0x2328, 0x5208, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7EAB)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 0, 400)
    Sleep(500)
    OP_1D(0x75)
    WaitChrThread(0x105, 0x2)
    Sleep(500)

    ChrTalk(    #320
        0x105,
        (
            "#543F#6P……那个，雷克特学长。\x02\x03",

            "#048F谢谢你。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x10, 0xFFFFFEA2, 1750, 0x0, 0x1, 0xC8, 0x2)
    Sleep(800)
    SetChrSubChip(0x10, 1)
    Sleep(100)
    SetChrSubChip(0x10, 2)
    Sleep(300)

    ChrTalk(    #321
        0x10,
        "#1773F#5P……嗯？　你说什么呢？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x105,
        (
            "#543F#6P很多方面。\x02\x03",

            "我都受到了学长\x01",
            "很多帮助呢。\x02\x03",

            "#542F不过，\x01",
            "你却总是随便应付一下就马上逃走……\x02\x03",

            "从那以后我一直在想。\x01",
            "我还一次都没好好跟你道过谢呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(300)
    SetChrSubChip(0x10, 3)
    Sleep(500)

    ChrTalk(    #323
        0x10,
        (
            "#1775F#5P嗯嗯～，\x01",
            "完全不知道你在说什么啊～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x105,
        "#048F#6P呵呵…………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x105, 51640, 9000, 20870, 0)
    SetChrFlags(0x105, 0x2)
    SetChrChipByIndex(0x105, 23)
    SetChrSubChip(0x105, 0)
    OP_0D()

    def lambda_80D2():
        OP_6B(2650, 25000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_80D2)
    Sleep(500)

    ChrTalk(    #325
        0x105,
        (
            "#542F#6P……学长，你以前问过我吧。\x01",
            "问我为了什么才来到这里。\x02\x03",

            "#047F我……不喜欢以前的生活。\x02\x03",

            "只是受周围的影响随波逐流而已。\x01",
            "没有一样自己能够抓住的东西。\x02\x03",

            "我讨厌这样的自己。\x01",
            "我觉得很空虚。\x02\x03",

            "#049F所以，\x01",
            "从来不试图去思考类似学长提出的问题。\x02\x03",

            "我觉得如果承认了自己的软弱，\x01",
            "就无法再保持坚强……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)

    ChrTalk(    #326
        0x105,
        (
            "#045F#6P但是，我现在已经不空虚了。\x02\x03",

            "#542F来到这个学院，认识了学长和大家，\x01",
            "让我学到了很多东西。\x02\x03",

            "而且也用自己的力量\x01",
            "抓住了最重要的东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x10,
        "#1775F#5P哦～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x105,
        (
            "#543F#6P……所以，\x01",
            "真是谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0xFFFFFEA2, 1750, 0x18, 0x1B, 0xC8, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #329
        0x10,
        (
            "#1773F#5P…………科洛丝。\x02\x03",

            "#1771F你果然是个死板的人啊～。\x01",
            "竟然烦恼这种事？\x02\x03",

            "连空之女神都要吓一跳了～☆\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xF, 0x0, 0x64)
    OP_62(0x10, 0xFFFFFEA2, 1750, 0x8, 0x9, 0xC8, 0x2)
    Sleep(1000)

    ChrTalk(    #330
        0x105,
        "#045F#6P又在取笑我……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x105, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x105)
    Sleep(500)
    OP_59()
    Fade(300)
    SetChrSubChip(0x105, 1)
    Sleep(500)

    ChrTalk(    #331
        0x105,
        (
            "#542F#6P学长又怎么样呢？\x02\x03",

            "为什么来这个学院？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x10,
        (
            "#1773F#5P…………嗯？\x02\x03",

            "#1776F啊啊，那是因为……\x02\x03",

            "#1775F反正，因为有空嘛～。\x01",
            "又没什么别的事好做。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x105,
        (
            "#543F#6P呵呵，是吗……\x02\x03",

            "#040F那么，\x01",
            "总而言之先工作吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrPos(0x105, 51440, 9000, 21000, 0)
    SetChrSubChip(0x105, 0)
    ClearChrFlags(0x105, 0x2)
    SetChrChipByIndex(0x105, 65535)
    SetChrSubChip(0x105, 0)
    OP_0D()
    OP_8C(0x105, 270, 500)

    def lambda_8593():
        OP_6D(49000, 9000, 25440, 1500)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_8593)

    def lambda_85AB():
        OP_6C(315000, 1500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_85AB)

    def lambda_85BB():
        OP_8F(0xFE, 0xC670, 0x2328, 0x51E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_85BB)
    WaitChrThread(0x105, 0x1)
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 21)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x105, 50700, 9000, 20960, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #334
        0x10,
        "#1773F#5P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x105,
        (
            "#042F#12P明天就是学生大会了。\x01",
            "今天之内就要全部干完哦。\x02\x03",

            "桌子上的资料都堆积如山了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 90, 400)
    Sleep(300)
    OP_62(0x10, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #336 op#A
        0x10,
        "#1773F#5P#12A喂，喂……！？\x02",
    )


    def lambda_86D9():
        OP_8F(0xFE, 0xC9F4, 0x2328, 0x51E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_86D9)

    def lambda_86F4():
        OP_8F(0xFE, 0xC738, 0x2328, 0x5154, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_86F4)
    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #337
        0x10,
        (
            "#1772F#5P等一下，科洛丝。\x02\x03",

            "听我解释你就会明白的……！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x105,
        "#041F#5P不～行！\x02",
    )

    CloseMessageWindow()

    def lambda_8780():
        OP_8F(0xFE, 0xEB28, 0x2328, 0x51E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8780)

    def lambda_879B():
        OP_8F(0xFE, 0xE86C, 0x2328, 0x5154, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_879B)
    Sleep(1000)

    ChrTalk(    #339 op#A
        0x10,
        "#1P#22A放、放我一马吧～……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)
    Sleep(300)

    def lambda_87EF():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_87EF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x800)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #340
        (
            "\x18\x07\x0C#40W这就是……\x01",
            "我向他——雷克特·亚兰德尔\x01",
            "第一次也是最后一次道谢的机会。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #341
        (
            "\x18\x07\x0C#40W在那之后，他在当年的学院祭翌日\x01",
            "突然提出了退学申请，然后就失踪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #342
        (
            "\x18\x07\x0C#40W（顺带一提，他在学生会举办的话剧\x01",
            "#5W  #40W上演到高潮的场景时突然乱入，\x01",
            "#5W  #40W又可笑又可气地搞砸了场。）\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #343
        "\x18\x07\x0C#40W然而两年后──\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #344
        (
            "\x18\x07\x0C#40W我在意想不到的地方\x01",
            "与他重逢了──\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_C4(0x1, 0x800)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #345
        "\x07\x00Episode『飘落的羽翼』　～Fin～\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A9C")
    Sleep(1000)
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x5, 0x4, 0x20)
    OP_3E(0x2CD, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #346
        "\x07\x00得到了\x1F\xCD\x02\x07\x00。\x02",
    )

    Jump("loc_8A65")

    label("loc_8A65")

    CloseMessageWindow()
    AddMira(6000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #347
        "\x07\x00得到了\x07\x02６０００米拉\x07\x00。\x02",
    )

    Jump("loc_8A90")

    label("loc_8A90")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_8A9C")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_42_7BA3 end

    def Function_43_8AA9(): pass

    label("Function_43_8AA9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x105, 57990, 9000, 18750, 270)
    OP_6D(58320, 9000, 18760, 0)
    OP_67(0, 7390, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(314000, 0)
    OP_6E(297, 0)
    Sleep(1000)

    def lambda_8B0E():
        OP_6D(54100, 9000, 19210, 2500)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_8B0E)

    def lambda_8B26():
        OP_6B(2550, 2500)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_8B26)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x21, 0x0)
    Sleep(500)

    ChrTalk(    #348
        0x105,
        (
            "#543F#12P（……果然，\x01",
            "  好像不在这里呢。）\x02\x03",

            "#040F（还是去别处找找看吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_A2(0x2FA7)
    EventEnd(0x0)
    Return()

    # Function_43_8AA9 end

    def Function_44_8BA8(): pass

    label("Function_44_8BA8")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(17840, 0, 45920, 0)
    SetChrPos(0x3, 17230, 0, 46030, 90)
    SetChrPos(0x2, 17890, 0, 46670, 90)
    SetChrPos(0x1, 17890, 0, 45370, 90)
    SetChrPos(0x0, 18510, 0, 46030, 90)
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Call(0, 46)
    Call(0, 47)
    Fade(500)
    OP_6D(20220, 0, 46020, 0)
    SetChrPos(0x0, 20220, 0, 46020, 90)
    SetChrPos(0x1, 20220, 0, 46020, 90)
    SetChrPos(0x2, 20220, 0, 46020, 90)
    SetChrPos(0x3, 20220, 0, 46020, 90)
    EventEnd(0x0)
    Return()

    # Function_44_8BA8 end

    def Function_45_8CA3(): pass

    label("Function_45_8CA3")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_6D(17840, 0, 45920, 0)
    SetChrPos(0x0, 17230, 0, 46030, 270)
    SetChrPos(0x1, 17890, 0, 46670, 270)
    SetChrPos(0x2, 17890, 0, 45370, 270)
    SetChrPos(0x3, 18510, 0, 46030, 270)
    OP_0D()
    Call(0, 46)
    Call(0, 48)
    NewScene("ED6_DT21/C4102   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_45_8CA3 end

    def Function_46_8D1B(): pass

    label("Function_46_8D1B")

    LoadEffect(0x0, "map\\mp049_21.eff")
    PlayEffect(0x0, 0xFF, 0x0, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x2, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x3, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Return()

    # Function_46_8D1B end

    def Function_47_8E0D(): pass

    label("Function_47_8E0D")


    def lambda_8E13():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8E13)

    def lambda_8E25():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8E25)

    def lambda_8E37():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_8E37)

    def lambda_8E49():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_8E49)
    Sleep(2500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E71")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_8E71")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E88")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_8E88")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E9F")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_8E9F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8EB6")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_8EB6")

    Return()

    # Function_47_8E0D end

    def Function_48_8EB7(): pass

    label("Function_48_8EB7")


    def lambda_8EBD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8EBD)

    def lambda_8ECF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8ECF)

    def lambda_8EE1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_8EE1)

    def lambda_8EF3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_8EF3)
    Sleep(2000)
    Return()

    # Function_48_8EB7 end

    def Function_49_8F05(): pass

    label("Function_49_8F05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_9025")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_8F7D")

    ChrTalk(    #349
        0x105,
        (
            "#047F……学长应该会\x01",
            "故意藏在能让人\x01",
            "找得到的地方。\x02\x03",

            "#042F他一定还躲在\x01",
            "这所学院里面！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9022")

    label("loc_8F7D")


    ChrTalk(    #350
        0x105,
        (
            "#047F雷克特学长………\x01",
            "应该没有出学院吧。\x02\x03",

            "#049F虽然好像偶尔\x01",
            "会去卢安的城镇上玩……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x105)

    ChrTalk(    #351
        0x105,
        "#047F呼，真是任性啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_9022")

    Jump("loc_9205")

    label("loc_9025")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_9178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9083")

    ChrTalk(    #352
        0x105,
        (
            "#040F我想他应该没有到学院外面去。\x02\x03",

            "再在屋子里面找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9175")

    label("loc_9083")


    ChrTalk(    #353
        0x105,
        (
            "#047F我想他应该\x01",
            "没有到学院外面去。\x02\x03",

            "#040F如果是那样，\x01",
            "基库一定会找到他的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x152,
        (
            "#733F隼的视力，\x01",
            "好、好厉害啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x13B,
        (
            "#640F要到学院外面去的话，\x01",
            "我们也必须申请外出许可。\x02\x03",

            "还是暂且在屋子里面找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_9175")

    Jump("loc_9205")

    label("loc_9178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_9205")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_91B3")

    ChrTalk(    #356
        0x105,
        "#047F……现在没有出去的必要。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9205")

    label("loc_91B3")


    ChrTalk(    #357
        0x105,
        (
            "#047F似乎没有学生\x01",
            "到学院外面去。\x02\x03",

            "#040F现在没有出去的必要。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_9205")

    TalkEnd(0xFF)
    Return()

    # Function_49_8F05 end

    def Function_50_9209(): pass

    label("Function_50_9209")

    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2511   ._SN", 112, 0, 0)
    IdleLoop()
    TalkEnd(0xFF)
    Return()

    # Function_50_9209 end

    def Function_51_9221(): pass

    label("Function_51_9221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9272")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #358
        "\x07\x05还保留着一定温度…………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_9379")

    label("loc_9272")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #359
        "\x07\x05还保留着一定温度…………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #360
        0x13B,
        (
            "#647F应该还在这附近吧。\x02\x03",

            "#649F呼，总算追上了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x152,
        (
            "#735F终于到了算总帐的时候了。\x02\x03",

            "#732F做好心理准备吧。\x01",
            "……雷克特学长！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x105,
        "#045F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_9379")

    TalkEnd(0xFF)
    Return()

    # Function_51_9221 end

    SaveToFile()

Try(main)
