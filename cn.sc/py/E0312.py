from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0312   ._SN',
        MapName             = 'Event',
        Location            = 'E0312.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/E0312   ._SN',
            'ED6_DT21/E0312_1 ._SN',
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
        '拉赛尔博士',                           # 9
        '雪拉扎德',                             # 10
        '阿加特',                               # 11
        '提妲',                                 # 12
        '金',                                   # 13
        '凯文神父',                             # 14
        '乔丝特',                               # 15
        '雨果',                                 # 16
        '露依赛',                               # 17
        '亲卫队队员',                           # 18
        '亲卫队队员',                           # 19
        '雷伊',                                 # 20
        '库莱泽',                               # 21
        '修理员佩顿',                           # 22
        '菲',                                   # 23
        '安东尼',                               # 24
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
        'ED6_DT07/CH02020 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH00050 ._CH',             # 02
        'ED6_DT07/CH00060 ._CH',             # 03
        'ED6_DT07/CH00070 ._CH',             # 04
        'ED6_DT27/CH03080 ._CH',             # 05
        'ED6_DT27/CH03100 ._CH',             # 06
        'ED6_DT07/CH01680 ._CH',             # 07
        'ED6_DT07/CH01430 ._CH',             # 08
        'ED6_DT07/CH01320 ._CH',             # 09
        'ED6_DT07/CH01220 ._CH',             # 0A
        'ED6_DT07/CH01450 ._CH',             # 0B
        'ED6_DT07/CH01550 ._CH',             # 0C
        'ED6_DT07/CH01700 ._CH',             # 0D
        'ED6_DT07/CH00170 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02020P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH00050P._CP',             # 02
        'ED6_DT07/CH00060P._CP',             # 03
        'ED6_DT07/CH00070P._CP',             # 04
        'ED6_DT27/CH03080P._CP',             # 05
        'ED6_DT27/CH03100P._CP',             # 06
        'ED6_DT07/CH01680P._CP',             # 07
        'ED6_DT07/CH01430P._CP',             # 08
        'ED6_DT07/CH01320P._CP',             # 09
        'ED6_DT07/CH01220P._CP',             # 0A
        'ED6_DT07/CH01450P._CP',             # 0B
        'ED6_DT07/CH01550P._CP',             # 0C
        'ED6_DT07/CH01700P._CP',             # 0D
        'ED6_DT07/CH00170P._CP',             # 0E
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 360,
        Z                   = 0,
        Y                   = 63980,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -5140,
        Z                   = 0,
        Y                   = 65400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -2670,
        Z                   = 0,
        Y                   = 5340,
        Direction           = 180,
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
        X                   = -2680,
        Z                   = 0,
        Y                   = 5370,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -5340,
        Z                   = 0,
        Y                   = 60180,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = -5340,
        Z                   = 0,
        Y                   = 58780,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = -30,
        Z                   = 0,
        Y                   = 60960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 400,
        Z                   = 0,
        Y                   = 63980,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -6120,
        Z                   = 0,
        Y                   = 62560,
        Direction           = 233,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )


    DeclEvent(
        X                   = -2680,
        Y                   = -1000,
        Z                   = 5370,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 42,
    )


    DeclActor(
        TriggerX            = -5110,
        TriggerZ            = 0,
        TriggerY            = 65500,
        TriggerRange        = 400,
        ActorX              = -5410,
        ActorZ              = 1500,
        ActorY              = 65800,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2980,
        TriggerZ            = 0,
        TriggerY            = 66830,
        TriggerRange        = 800,
        ActorX              = -2980,
        ActorZ              = 1000,
        ActorY              = 66830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 39,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 60000,
        TriggerZ            = 0,
        TriggerY            = -36460,
        TriggerRange        = 1200,
        ActorX              = 60000,
        ActorZ              = 2080,
        ActorY              = -36230,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 40,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2370,
        TriggerZ            = 0,
        TriggerY            = 60960,
        TriggerRange        = 800,
        ActorX              = -30,
        ActorZ              = 1500,
        ActorY              = 60960,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 41,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 62910,
        TriggerZ            = 0,
        TriggerY            = 4740,
        TriggerRange        = 1200,
        ActorX              = 62910,
        ActorZ              = 800,
        ActorY              = 4740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 40,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3F6",          # 00, 0
        "Function_1_87A",          # 01, 1
        "Function_2_A61",          # 02, 2
        "Function_3_BDE",          # 03, 3
        "Function_4_C02",          # 04, 4
        "Function_5_247B",         # 05, 5
        "Function_6_2693",         # 06, 6
        "Function_7_2921",         # 07, 7
        "Function_8_4279",         # 08, 8
        "Function_9_4759",         # 09, 9
        "Function_10_5941",        # 0A, 10
        "Function_11_5CAA",        # 0B, 11
        "Function_12_5E58",        # 0C, 12
        "Function_13_5F4B",        # 0D, 13
        "Function_14_60B3",        # 0E, 14
        "Function_15_61DD",        # 0F, 15
        "Function_16_6BC3",        # 10, 16
        "Function_17_6F09",        # 11, 17
        "Function_18_71F0",        # 12, 18
        "Function_19_7C25",        # 13, 19
        "Function_20_7CC1",        # 14, 20
        "Function_21_7ECA",        # 15, 21
        "Function_22_820A",        # 16, 22
        "Function_23_8503",        # 17, 23
        "Function_24_8606",        # 18, 24
        "Function_25_868D",        # 19, 25
        "Function_26_871A",        # 1A, 26
        "Function_27_8DBE",        # 1B, 27
        "Function_28_8DEB",        # 1C, 28
        "Function_29_8E2A",        # 1D, 29
        "Function_30_8E69",        # 1E, 30
        "Function_31_8EA8",        # 1F, 31
        "Function_32_8EE7",        # 20, 32
        "Function_33_8F15",        # 21, 33
        "Function_34_8F31",        # 22, 34
        "Function_35_8F4D",        # 23, 35
        "Function_36_8F69",        # 24, 36
        "Function_37_94F2",        # 25, 37
        "Function_38_9824",        # 26, 38
        "Function_39_9DA0",        # 27, 39
        "Function_40_9DF2",        # 28, 40
        "Function_41_9E99",        # 29, 41
        "Function_42_9E9E",        # 2A, 42
    )


    def Function_0_3F6(): pass

    label("Function_0_3F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_59C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_420")
    SetChrPos(0xB, -2830, 0, 65940, 90)
    ClearChrFlags(0xB, 0x80)

    label("loc_420")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_443")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_443")

    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48C")
    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_489")
    SetChrPos(0x9, -5340, 0, 59510, 270)
    ClearChrFlags(0x9, 0x80)

    label("loc_489")

    Jump("loc_599")

    label("loc_48C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AD")
    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_599")

    label("loc_4AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A")
    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4EE")
    SetChrPos(0xB, -3510, 0, 5330, 0)
    ClearChrFlags(0xB, 0x80)

    label("loc_4EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_511")
    SetChrPos(0xE, -5340, 0, 60030, 270)
    ClearChrFlags(0xE, 0x80)

    label("loc_511")

    SetChrPos(0x12, 63010, 0, -39310, 270)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_599")

    label("loc_52A")

    ClearChrFlags(0x16, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_552")
    SetChrPos(0xE, -5340, 0, 60030, 270)
    ClearChrFlags(0xE, 0x80)

    label("loc_552")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_583")
    OP_44(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 15)
    SetChrPos(0xA, 61300, 250, -40950, 0)

    label("loc_583")

    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)

    label("loc_599")

    Jump("loc_85A")

    label("loc_59C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_663")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C9")
    SetChrPos(0x8, -5200, 0, 65530, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    Jump("loc_5DF")

    label("loc_5C9")

    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)

    label("loc_5DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_602")
    SetChrPos(0xB, -860, 0, 64200, 45)
    ClearChrFlags(0xB, 0x80)

    label("loc_602")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_625")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_625")

    SetChrPos(0x13, -6370, 0, 61080, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x14, -5350, 0, 59530, 270)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_85A")

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_6F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_690")
    SetChrPos(0x8, -5200, 0, 65530, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    Jump("loc_6A6")

    label("loc_690")

    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)

    label("loc_6A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6C9")
    SetChrPos(0xB, -860, 0, 64200, 45)
    ClearChrFlags(0xB, 0x80)

    label("loc_6C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6EC")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_6EC")

    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_85A")

    label("loc_6F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_787")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_726")
    SetChrPos(0x8, -5200, 0, 65530, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    Jump("loc_73C")

    label("loc_726")

    SetChrPos(0x8, -950, 0, 65390, 0)
    ClearChrFlags(0x8, 0x80)

    label("loc_73C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_75F")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_75F")

    SetChrPos(0x14, -6310, 0, 61050, 180)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_85A")

    label("loc_787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_806")
    SetChrPos(0x8, -6370, 0, 61080, 180)
    ClearChrFlags(0x8, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C7")
    SetChrPos(0xB, -4420, 0, 62290, 225)
    ClearChrFlags(0xB, 0x80)

    label("loc_7C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7EA")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_7EA")

    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_85A")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_81F")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_85A")

    label("loc_81F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_85A")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xC, 0)
    SetChrPos(0xC, 62250, 0, -39280, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)

    label("loc_85A")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_866"),
        (SWITCH_DEFAULT, "loc_879"),
    )


    label("loc_866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_876")
    Event(0, 26)

    label("loc_876")

    Jump("loc_879")

    label("loc_879")

    Return()

    # Function_0_3F6 end

    def Function_1_87A(): pass

    label("Function_1_87A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_898")
    OP_4F(0x3B, (scpexpr(EXPR_PUSH_LONG, 0x227), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x3C, (scpexpr(EXPR_PUSH_LONG, 0x10A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_898")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C8")
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_8BC")
    OP_B1("E0312_1")
    Jump("loc_8C5")

    label("loc_8BC")

    OP_B1("E0312_2")

    label("loc_8C5")

    Jump("loc_8E9")

    label("loc_8C8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E0")
    OP_B1("E0312_2")
    Jump("loc_8E9")

    label("loc_8E0")

    OP_B1("E0312_1")

    label("loc_8E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_912")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_91F")

    label("loc_912")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91F")
    OP_22(0x7A, 0x1, 0x46)

    label("loc_91F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_94A")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x7A, 0x1, 0x46)

    label("loc_94A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_96B")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x3E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_96B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_97A")
    OP_72(0x5, 0x4)
    Jump("loc_9B8")

    label("loc_97A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_992")
    OP_64(0x0, 0x1)
    OP_72(0x5, 0x4)
    Jump("loc_9B8")

    label("loc_992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_9A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A1")

    label("loc_9A1")

    OP_72(0x5, 0x4)
    Jump("loc_9B8")

    label("loc_9A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_9B8")
    OP_64(0x0, 0x1)
    OP_64(0x3, 0x1)

    label("loc_9B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_9FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CA")
    Jump("loc_9FC")

    label("loc_9CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D5")
    Jump("loc_9FC")

    label("loc_9D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E0")
    Jump("loc_9FC")

    label("loc_9E0")

    OP_D2(0x70053, 0x7005B, 0xF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9FC")
    SetChrChipByIndex(0xA, 15)

    label("loc_9FC")

    Jump("loc_A60")

    label("loc_9FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_A13")
    OP_D2(0x600FC, 0x60101, 0xF)
    Jump("loc_A60")

    label("loc_A13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_A27")
    OP_D2(0x600FC, 0x60101, 0xF)
    Jump("loc_A60")

    label("loc_A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_A3B")
    OP_D2(0x600FC, 0x60101, 0xF)
    Jump("loc_A60")

    label("loc_A3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_A4F")
    OP_D2(0x600FC, 0x60101, 0xF)
    Jump("loc_A60")

    label("loc_A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_END)), "loc_A59")
    Jump("loc_A60")

    label("loc_A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_A60")

    label("loc_A60")

    Return()

    # Function_1_87A end

    def Function_2_A61(): pass

    label("Function_2_A61")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A86")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_BC8")

    label("loc_A86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9F")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_BC8")

    label("loc_A9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB8")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_BC8")

    label("loc_AB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD1")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_BC8")

    label("loc_AD1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEA")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_BC8")

    label("loc_AEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B03")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_BC8")

    label("loc_B03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1C")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_BC8")

    label("loc_B1C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B35")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_BC8")

    label("loc_B35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4E")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_BC8")

    label("loc_B4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B67")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_BC8")

    label("loc_B67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B80")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_BC8")

    label("loc_B80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B99")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_BC8")

    label("loc_B99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB2")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_BC8")

    label("loc_BB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC8")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_BC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BDD")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_BC8")

    label("loc_BDD")

    Return()

    # Function_2_A61 end

    def Function_3_BDE(): pass

    label("Function_3_BDE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C01")
    OP_8D(0xFE, -7430, 62910, -5150, 62070, 1000)
    Jump("Function_3_BDE")

    label("loc_C01")

    Return()

    # Function_3_BDE end

    def Function_4_C02(): pass

    label("Function_4_C02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x456, 0)), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x31, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x456, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C51")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x417, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C46")
    Call(0, 38)
    TalkEnd(0xFE)
    Return()

    label("loc_C46")

    Call(0, 36)
    TalkEnd(0xFE)
    Return()

    label("loc_C51")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【上前说话】\x01",          # 0
            "【请求制作武器】\x01",      # 1
            "【什么也不做】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD7")
    EventBegin(0x0)
    Fade(500)
    OP_6D(-770, 0, 64560, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1430, 0, 64099, 0)
    SetChrPos(0x102, -550, 0, 64099, 0)
    SetChrPos(0xF8, -1450, 0, 63100, 0)
    SetChrPos(0xF9, -550, 0, 63100, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()

    ChrTalk(    #0
        0x8,
        "#100F哦，决定要制作什么武器了吗？\x02",
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
            "【麒麟具】\x01",                # 0
            "【凤凰剑（凤·凰）】\x01",      # 1
            "【停止】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Call(0, 37)
    TalkEnd(0xFE)
    Return()

    label("loc_DD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DE8")
    TalkEnd(0xFE)
    Return()

    label("loc_DE8")

    FadeToBright(300, 0)

    label("loc_DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_E77")

    ChrTalk(    #1
        0x8,
        (
            "#100F呵呵，这回可真是\x01",
            "让我积累了宝贵的经验呢。\x02\x03",

            "毕竟很少有机会\x01",
            "能够处理古代金属啊。\x02\x03",

            "看来今后的研究也\x01",
            "更加令人投入了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2477")

    label("loc_E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8A")
    Call(0, 22)
    Jump("loc_2477")

    label("loc_E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_END)), "loc_2215")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x3FE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_40(0x3FF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x400, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x401, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x402, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x403, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x404, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x405, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x406, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x407, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x408, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x408, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F2B")
    Call(0, 23)
    Jump("loc_2212")

    label("loc_F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_11F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_106E")

    ChrTalk(    #2
        0x8,
        (
            "#100F接下来要开始进行\x01",
            "最终的飞翔引擎检查。\x02\x03",

            "通过的话，修理就算是完成了。\x01",
            "可以保证最低限度的飞行能力。\x02\x03",

            "#104F当然，如果能修好左侧的\x01",
            "舷外支架是再好不过了……\x02\x03",

            "#100F考虑到也许无法修复，\x01",
            "所以只是想先做一个测试。\x02\x03",

            "我正在进行中枢塔\x01",
            "搜索结束后的返航准备工作。\x02\x03",

            "那么……\x01",
            "提妲就拜托你们照顾了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1195")

    label("loc_106E")


    ChrTalk(    #3
        0x8,
        (
            "#100F接下来要开始进行\x01",
            "最终的飞翔引擎检查。\x02\x03",

            "通过的话，修理就算是完成了。\x01",
            "可以保证最低限度的飞行能力。\x02\x03",

            "#104F当然，如果能修好左侧的\x01",
            "舷外支架是再好不过了……\x02\x03",

            "#100F考虑到也许无法修复，\x01",
            "所以只是想先做一个测试。\x02\x03",

            "我正在进行中枢塔\x01",
            "搜索结束后的返航准备工作。\x02\x03",

            "那么……\x01",
            "你们一定要平安无事地回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1195")

    OP_A2(0x3)
    Jump("loc_11F6")

    label("loc_119B")


    ChrTalk(    #4
        0xFE,
        (
            "#100F我正在进行中枢塔\x01",
            "搜索结束后的返航准备工作。\x02\x03",

            "所以……\x01",
            "你们一定要平安无事地回来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F6")

    Jump("loc_2212")

    label("loc_11F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_12FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129D")

    ChrTalk(    #5
        0x8,
        (
            "#104F说不定舷外支架\x01",
            "会无法顺利回收……\x02\x03",

            "#100F届时我打算只拆下飞翔引擎，\x01",
            "然后装设在埃尔赛尤号上。\x02\x03",

            "我想应该还可以作为\x01",
            "辅助的推进器来使用。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_12FC")

    label("loc_129D")


    ChrTalk(    #6
        0x8,
        (
            "#100F说不定舷外支架\x01",
            "会无法顺利回收……\x02\x03",

            "为了预防这种情况发生，\x01",
            "我打算先准备一套替代方案。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12FC")

    Jump("loc_2212")

    label("loc_12FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45A, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15FD")

    ChrTalk(    #7
        0x8,
        (
            "#100F哦，你们几个。\x02\x03",

            "怎么样？\x01",
            "有没有什么有趣的发现啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1015F嗯，虽然不知道\x01",
            "算不算有趣啦……\x02\x03",

            "不过的确发现了一件让人在意的东西。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #9
        0x8,
        (
            "#103F喔……\x01",
            "发现了什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        "#1035F嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05将发现了再次发行『福音』的终端，\x01",
            "并要求输入居民姓名一事向博士说明了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #12
        0x8,
        (
            "#104F原来如此……\x02\x03",

            "#100F为了再次发行『福音』\x01",
            "必须输入登录者的姓名啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1003F嗯，是这样没错……\x02\x03",

            "#1007F不过即使是博士，\x01",
            "也不会认识以前的居民吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #14
        0x8,
        (
            "#104F那当然。\x01",
            "我可没有那么长寿。\x02\x03",

            "#102F不过，数据水晶里\x01",
            "应该记录着过去所发生的事。\x02\x03",

            "看看『卡佩尔』的分析资料的话，\x01",
            "或许能够得到什么提示也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        (
            "#1044F原来如此……\x01",
            "确实很有可能呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1015F数据水晶吗……\x02\x03",

            "嗯，反正也没其它线索，\x01",
            "要立刻调查一下看看吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x14)
    OP_A2(0x22D2)
    Jump("loc_2212")

    label("loc_15FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_1B0A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_197A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1910")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_172A")

    ChrTalk(    #17
        0x8,
        (
            "#100F数据水晶中\x01",
            "记录着过去所发生的事。\x02\x03",

            "看看『卡佩尔』的分析资料的话，\x01",
            "或许能够得到什么提示也说不定。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x14)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x10B, 400)
    Sleep(400)

    ChrTalk(    #18
        0x8,
        (
            "#103F咦，那不是……\x02\x03",

            "#101F什么嘛，那不是空贼姑娘吗。\x01",
            "实在是好久不见了啊。\x02\x03",

            "上回最后一次见面是\x01",
            "在雷斯顿要塞的地下吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_178C")

    label("loc_172A")

    TurnDirection(0x8, 0x10B, 0)

    ChrTalk(    #19
        0x8,
        (
            "#101F哦，是空贼姑娘啊。\x01",
            "似乎好久不见了啊。\x02\x03",

            "上回最后一次见面是\x01",
            "在雷斯顿要塞的地下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_178C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1802")

    ChrTalk(    #20
        0x10B,
        (
            "#214F空，空贼姑娘是什么！\x01",
            "不要取这种奇怪的简称啦。\x02\x03",

            "#413F真是的，孙女是那副样子，\x01",
            "做爷爷的也是这样……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183A")

    label("loc_1802")


    ChrTalk(    #21
        0x10B,
        (
            "#214F空，空贼姑娘是什么！\x01",
            "不要取这种奇怪的简称啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183A")


    ChrTalk(    #22
        0x8,
        (
            "#100F别说这些无关紧要的事了。\x02\x03",

            "话说回来，我倒是听说\x01",
            "你们的飞艇也坠落了。\x02\x03",

            "虽然我不太了解帝国制的导力引擎，\x01",
            "不过多少可以给你们些维修的建议。\x02\x03",

            "要是遇到麻烦\x01",
            "就尽管来问我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10B,
        (
            "#213F啊，嗯……\x01",
            "我们会的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22C2)
    Jump("loc_1977")

    label("loc_1910")

    TurnDirection(0x8, 0x10B, 0)

    ChrTalk(    #24
        0x8,
        (
            "#100F听说你们的飞艇\x01",
            "也坠落了。\x02\x03",

            "要是遇到麻烦\x01",
            "就随时来问我吧。\x01",
            "我会给你们一些修理上的建议。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1977")

    Jump("loc_1B07")

    label("loc_197A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_19EF")

    ChrTalk(    #25
        0x8,
        (
            "#100F数据水晶中\x01",
            "记录着过去所发生的事。\x02\x03",

            "看看『卡佩尔』的分析资料的话，\x01",
            "或许能够得到什么提示也说不定。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B07")

    label("loc_19EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA2")

    ChrTalk(    #26
        0x8,
        (
            "#100F哦，你们几个。\x01",
            "听说你们救了空贼团的小姑娘吧。\x02\x03",

            "关于那个帝国制造的飞艇\x01",
            "我也有很多想要调查的地方。\x02\x03",

            "#104F嗯，真想找时间促膝而坐，\x01",
            "好好地跟她聊聊这个话题呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_1B07")

    label("loc_1AA2")


    ChrTalk(    #27
        0x8,
        (
            "#100F关于帝国制造的飞艇\x01",
            "我也还有很多部分不太清楚。\x02\x03",

            "真想找时间跟空贼姑娘\x01",
            "好好地聊聊这个话题呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B07")

    Jump("loc_2212")

    label("loc_1B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1D2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CBE")

    ChrTalk(    #28
        0x8,
        (
            "#100F导力引擎总算是发动起来了，\x01",
            "但为了慎重起见，先把功率调低。\x02\x03",

            "待稍微观察一下情况后，\x01",
            "再切换到普通驱动。\x02\x03",

            "大家就暂时在紧急照明下\x01",
            "忍耐着点进行作业吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#1040F……明白了。\x01",
            "在这种状态下\x01",
            "不能要求太高呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1015F是啊……\x01",
            "必须尽量努力才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C67")

    ChrTalk(    #31
        0x8,
        (
            "#100F你们几个\x01",
            "也要多加小心啊。\x02\x03",

            "提妲\x01",
            "就拜托你们照顾了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CB8")

    label("loc_1C67")


    ChrTalk(    #32
        0x8,
        (
            "#100F你们几个\x01",
            "也要多加小心啊。\x02\x03",

            "如果有什么有趣的发现，\x01",
            "请马上过来告诉我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CB8")

    OP_A2(0x22C1)
    Jump("loc_1D29")

    label("loc_1CBE")


    ChrTalk(    #33
        0x8,
        (
            "#100F目前这个阶段依然还在\x01",
            "观察导力引擎的状况如何。\x02\x03",

            "没有问题的话将会从舰内照明\x01",
            "开始逐步提升输出功率。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D29")

    Jump("loc_2212")

    label("loc_1D2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_1EDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D42")
    Call(0, 5)
    Jump("loc_1EDA")

    label("loc_1D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1DD6")

    ChrTalk(    #34
        0x8,
        (
            "#100F我还要再持续\x01",
            "进行一下装置的研究。\x02\x03",

            "需要武器或是结晶回路时，\x01",
            "找那边的佩顿商量就好了。\x02\x03",

            "那里有我从中央工房\x01",
            "收集而来的精选物品哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EDA")

    label("loc_1DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E79")

    ChrTalk(    #35
        0x8,
        (
            "#100F距离『装置』的试制品完成\x01",
            "只差最后一步了。\x02\x03",

            "当你们从塔返回的时候，\x01",
            "应该就会成形了才对。\x02\x03",

            "#101F哎呀呀，松了一口气。\x01",
            "看这个样子似乎来得及呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_1EDA")

    label("loc_1E79")


    ChrTalk(    #36
        0x8,
        (
            "#100F距离『装置』的试作品完成\x01",
            "只差最后一步了。\x02\x03",

            "当你们从塔返回的时候，\x01",
            "应该就会成形了才对。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDA")

    Jump("loc_2212")

    label("loc_1EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_207A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF3")
    Call(0, 5)
    Jump("loc_2077")

    label("loc_1EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FE8")

    ChrTalk(    #37
        0x8,
        (
            "#100F关于笼罩在塔顶的结界，\x01",
            "目前还不清楚详细情况如何。\x02\x03",

            "如果数据水晶的解读顺利，\x01",
            "我想或许会得到什么线索……\x02\x03",

            "总而言之，除了『装置』之外，\x01",
            "今后也要同时去进行这方面的研究。\x02\x03",

            "无论是『里塔』还是结界，\x01",
            "都必定是内容充实的研究课题。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2077")

    label("loc_1FE8")


    ChrTalk(    #38
        0x8,
        (
            "#100F无论是『里塔』还是结界，\x01",
            "都必定是内容充实的研究课题。\x02\x03",

            "#104F实话说，我真想亲自前去\x01",
            "观察那些现象呢……\x02\x03",

            "#102F哼，要是再年轻十岁的话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2077")

    Jump("loc_2212")

    label("loc_207A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_2212")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2090")
    Call(0, 5)
    Jump("loc_2212")

    label("loc_2090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_212C")

    ChrTalk(    #39
        0x8,
        (
            "#100F这阵子我会在这里\x01",
            "继续进行装置的研究。\x02\x03",

            "需要武器或是结晶回路时，\x01",
            "找那边的佩顿商量就好了。\x02\x03",

            "也请你们几个务必试试看\x01",
            "第三级的结晶孔强化哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2212")

    label("loc_212C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21AF")

    ChrTalk(    #40
        0x8,
        (
            "#100F资料水晶的分析\x01",
            "我打算先交给『卡佩尔』处理。\x02\x03",

            "毕竟除了『四轮之塔』的调查外，\x01",
            "我还得同时开发那个『装置』呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2212")

    label("loc_21AF")


    ChrTalk(    #41
        0x8,
        (
            "#100F如果获得了新的水晶，\x01",
            "请拿来我这里吧。\x02\x03",

            "我会立刻装在『卡佩尔』上，\x01",
            "让它开始进行自动分析。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2212")

    Jump("loc_2477")

    label("loc_2215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23E9")

    ChrTalk(    #42
        0x8,
        (
            "#100F怎么了，你们几个。\x02\x03",

            "莫非要进行\x01",
            "导力器的调整吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1011F嗯，也算是啦……\x02\x03",

            "博士你们在做什么呢？\x01",
            "大家都聚在这种地方。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #44
        0x8,
        (
            "#100F嗯，我正在\x01",
            "听取大家的意见。\x02\x03",

            "因为刚才在研究中的『某装置』里\x01",
            "发现了一些必须要解决的问题。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2330")

    ChrTalk(    #45
        0x107,
        "#064F某装置……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_234C")

    label("loc_2330")


    ChrTalk(    #46
        0x102,
        "#1044F是某装置……吗。\x02",
    )

    CloseMessageWindow()

    label("loc_234C")


    ChrTalk(    #47
        0x101,
        "#1015F好令人在意的说法呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#104F不好意思，\x01",
            "目前只能透露这么多。\x02\x03",

            "毕竟这或许只是\x01",
            "我们杞人忧天的想法吧。\x02\x03",

            "#101F总而言之请期待\x01",
            "完成的那一刻吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E29)
    Jump("loc_2477")

    label("loc_23E9")


    ChrTalk(    #49
        0x8,
        (
            "#100F这阵子我会在这里\x01",
            "继续进行装置的研究。\x02\x03",

            "需要武器或是结晶回路时，\x01",
            "找那边的佩顿商量就好了。\x02\x03",

            "那里有我从中央工房\x01",
            "收集而来的精选物品哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2477")

    TalkEnd(0xFE)
    Return()

    # Function_4_C02 end

    def Function_5_247B(): pass

    label("Function_5_247B")


    ChrTalk(    #50
        0x8,
        (
            "#100F嗯？怎么了？\x02\x03",

            "关于数据水晶\x01",
            "还有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1011F不，那个已经明白了……\x02\x03",

            "#1015F不过进行自动解析时，\x01",
            "博士在做些什么事呢？\x02\x03",

            "虽然说工作交给了『卡佩尔』处理，\x01",
            "可是看上去还是很忙的样子。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #52
        0x8,
        (
            "#100F嗯，其实我正在\x01",
            "忙着修正理论。\x02\x03",

            "因为刚才在研究中的『某装置』里\x01",
            "发现了一些必须要解决的问题。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25D5")

    ChrTalk(    #53
        0x107,
        "#064F某装置……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_25F1")

    label("loc_25D5")


    ChrTalk(    #54
        0x102,
        "#1044F是某装置……吗。\x02",
    )

    CloseMessageWindow()

    label("loc_25F1")


    ChrTalk(    #55
        0x101,
        "#1015F好、好令人在意的说法呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "#104F不好意思，\x01",
            "目前只能透露这么多。\x02\x03",

            "毕竟这或许只是\x01",
            "我们杞人忧天的想法吧。\x02\x03",

            "#101F总而言之请期待\x01",
            "完成的那一刻吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x1E2A)
    Return()

    # Function_5_247B end

    def Function_6_2693(): pass

    label("Function_6_2693")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2723")
    Jump("loc_2765")

    label("loc_2723")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_273F")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2765")

    label("loc_273F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_275B")
    OP_51(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2765")

    label("loc_275B")

    OP_51(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2765")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_27E8"),
        (1, "loc_28F5"),
        (2, "loc_2915"),
        (SWITCH_DEFAULT, "loc_2918"),
    )


    label("loc_27E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2887")

    ChrTalk(    #57
        0xA,
        (
            "#053F修理也告一段落了，\x01",
            "暂时休息一下吧。\x02\x03",

            "#050F一旦展开中枢塔的搜索，\x01",
            "敌人的抵抗也会逐渐猛烈起来……\x02\x03",

            "可以休息的时候\x01",
            "就必须好好地休息才行。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x10)
    Jump("loc_28F2")

    label("loc_2887")


    ChrTalk(    #58
        0xA,
        (
            "#050F修理也告一段落了，\x01",
            "暂时休息一下吧。\x02\x03",

            "敌人的抵抗也会逐渐猛烈起来……\x01",
            "能休息时就必须好好休息才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F2")

    Jump("loc_2918")

    label("loc_28F5")


    ChrTalk(    #59
        0xA,
        "#050F要更换成员吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 21)
    Jump("loc_2918")

    label("loc_2915")

    Jump("loc_2918")

    label("loc_2918")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_6_2693 end

    def Function_7_2921(): pass

    label("Function_7_2921")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2982"),
        (1, "loc_4252"),
        (2, "loc_4272"),
        (SWITCH_DEFAULT, "loc_4275"),
    )


    label("loc_2982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_END)), "loc_2A1A")

    ChrTalk(    #60
        0x107,
        (
            "#060F关于塞姆里亚石确切的构成，\x01",
            "爷爷似乎也还不清楚。\x02\x03",

            "他说资料既然已经回收，\x01",
            "之后再慢慢地分析就好了。\x02\x03",

            "嘿嘿，回到工房后\x01",
            "又要开始忙碌了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_424F")

    label("loc_2A1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 2)), scpexpr(EXPR_END)), "loc_2FD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x448, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D38")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #61
        0xB,
        (
            "#064F咦……\x01",
            "姐姐，哥哥。\x02\x03",

            "……你们怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1025F嗯，我们\x01",
            "有件事想告诉提妲。\x02\x03",

            "#1003F……玲她…………\x01",
            "以执行者的身份出现了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #63
        0xB,
        "#065F啊？……小玲吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x102,
        (
            "#1040F嗯……\x01",
            "不过她平安无事，请放心。\x02\x03",

            "在和我们战斗之后，\x01",
            "她就离开那个地方了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xB,
        (
            "#064F……这、这样啊。\x02\x03",

            "#561F太、太好了……\x01",
            "她平安无事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1015F虽然不知道她有没有\x01",
            "真正理解到我们的心意……\x02\x03",

            "不过那女孩似乎\x01",
            "自己开始思考些什么了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        (
            "#1040F她在朝着好的方向发展，\x01",
            "我想这一点是绝对错不了哦。\x02\x03",

            "玲是个聪明的女孩，\x01",
            "总有一天会觉察到的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #68
        0xB,
        (
            "#560F嗯、嗯！\x01",
            "一定会的。\x02\x03",

            "#066F真希望有一天……\x01",
            "还可以和她一起玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1017F嗯，绝对可以再见面的。\x01",
            "只要相信就会成真……不是吗。\x02\x03",

            "因为我和约修亚一样\x01",
            "也是这么重逢的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x102,
        "#1049F哈哈，说得也是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xB,
        "#560F啊……嗯！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22A3)
    Jump("loc_2DA8")

    label("loc_2D38")


    ChrTalk(    #72
        0xB,
        (
            "#060F加入『结社』\x01",
            "是一个错误……\x02\x03",

            "玲她自己\x01",
            "一定会察觉到这点的。\x02\x03",

            "要是将来有一天\x01",
            "能够再一起去买东西就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DA8")

    Jump("loc_2FD3")

    label("loc_2DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F54")

    ChrTalk(    #73
        0xB,
        (
            "#063F虽然不知道玲\x01",
            "跑去了哪里……\x02\x03",

            "但她一定会靠着\x01",
            "自己的力量察觉到错误吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x102,
        (
            "#1040F她在朝着好的方向发展，\x01",
            "我想这一点是绝对错不了哦。\x02\x03",

            "玲是个聪明的女孩，\x01",
            "总有一天会觉察到的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #75
        0xB,
        (
            "#560F嗯、嗯！\x01",
            "一定会的。\x02\x03",

            "#066F真希望有一天……\x01",
            "还可以和她一起玩。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#1017F嗯，绝对可以再见面的。\x01",
            "只要相信就会成真……不是吗。\x02\x03",

            "因为我和约修亚一样\x01",
            "也是这么重逢的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        "#1049F哈哈，说得也是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xB,
        "#560F啊……嗯！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22A3)
    Jump("loc_2FD3")

    label("loc_2F54")


    ChrTalk(    #79
        0xB,
        (
            "#560F玲她一定会靠着\x01",
            "自己的力量察觉到错误吧？\x02\x03",

            "我也要像姐姐一样\x01",
            "去试着相信玲。\x02\x03",

            "#067F然后，将来有一天\x01",
            "再和她一起去买东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FD3")

    Jump("loc_424F")

    label("loc_2FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_308F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_303D")

    ChrTalk(    #80
        0xB,
        (
            "#060F飞翔引擎的测试……\x01",
            "不知道能不能顺利通过。\x02\x03",

            "#067F唉……\x01",
            "心里觉得好紧张。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_308C")

    label("loc_303D")


    ChrTalk(    #81
        0xB,
        (
            "#060F飞翔引擎的测试……\x01",
            "不知道能不能顺利通过。\x02\x03",

            "#067F既、既紧张又兴奋……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_308C")

    Jump("loc_424F")

    label("loc_308F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_3640")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3240")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #82
        0xB,
        (
            "#064F啊，空贼姐姐……\x02\x03",

            "#560F那个那个……\x01",
            "我叫提妲。\x02\x03",

            "今、今后\x01",
            "请多多指教。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 2)), scpexpr(EXPR_END)), "loc_3176")

    ChrTalk(    #83
        0x10B,
        (
            "#413F我说啊，\x01",
            "我的名字叫乔丝特。\x02\x03",

            "你们所有人可不可以\x01",
            "别再用奇怪的称呼叫我了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31B1")

    label("loc_3176")


    ChrTalk(    #84
        0x10B,
        (
            "#213F空、空贼姐姐？\x02\x03",

            "#215F我说啊，\x01",
            "我的名字是乔丝特。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31B1")

    OP_62(0xB, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #85
        0xB,
        (
            "#065F啊……！？\x01",
            "对不起空贼姐姐……\x02\x03",

            "#067F……不是的，\x01",
            "是乔丝特小姐对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x10B,
        "#216F（你、你是故意的吧？）\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x22A2)
    Jump("loc_363D")

    label("loc_3240")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32B7")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #87
        0xB,
        (
            "#560F那个，乔丝特小姐。\x01",
            "今后请你多多指教。\x02\x03",

            "大、大家能够和睦相处\x01",
            "果然还是比较开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_363D")

    label("loc_32B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_352A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x459, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34A9")

    ChrTalk(    #88
        0xB,
        "#560F啊，欢迎回来。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1006F提妲也辛苦了。\x01",
            "你看起来非常努力呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #90
        0xB,
        (
            "#060F嗯，我正在检查照明设备。\x02\x03",

            "虽然切换成普通照明了，\x01",
            "但是万一因此加重负荷就不好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        (
            "#1040F原来如此……\x01",
            "修理的状况怎么样？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #92
        0xB,
        (
            "#060F爷爷他们\x01",
            "已经开始调整飞翔引擎了。\x02\x03",

            "听说在调整结束之后，准备\x01",
            "进行引擎的仿真升空测试。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_343F")

    ChrTalk(    #93
        0x10B,
        (
            "#213F哦，好厉害啊。\x01",
            "已经做到这个地步了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3470")

    label("loc_343F")


    ChrTalk(    #94
        0x102,
        (
            "#1040F不愧是博士……\x01",
            "已经进行到这个程度了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3470")


    ChrTalk(    #95
        0xB,
        (
            "#067F嘿嘿，只差一点点哦。\x02\x03",

            "我也会努力帮忙的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22CD)
    Jump("loc_3527")

    label("loc_34A9")


    ChrTalk(    #96
        0xB,
        (
            "#060F爷爷他们\x01",
            "已经开始调整飞翔引擎了。\x02\x03",

            "听说在调整结束之后，准备\x01",
            "进行引擎的仿真升空测试。\x02\x03",

            "距离可以起飞\x01",
            "只差一小步了哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3527")

    Jump("loc_363D")

    label("loc_352A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35E6")

    ChrTalk(    #97
        0xB,
        (
            "#060F预计再等一下就要\x01",
            "切换回原来的照明系统。\x02\x03",

            "所以现在正在为此\x01",
            "进行导力系统的检查……\x02\x03",

            "这个步骤结束后，\x01",
            "就可以连接结晶回路了。\x02\x03",

            "#067F到时会变得很明亮，\x01",
            "大家拭目以待吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_363D")

    label("loc_35E6")


    ChrTalk(    #98
        0xB,
        (
            "#060F预计再等一下就要\x01",
            "切换回原来的照明系统。\x02\x03",

            "到时会变得很明亮，\x01",
            "大家拭目以待吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_363D")

    Jump("loc_424F")

    label("loc_3640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_39C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3967")
    TurnDirection(0xB, 0x101, 0)

    ChrTalk(    #99
        0xB,
        (
            "#060F啊，姐姐是你们。\x02\x03",

            "正如爷爷所说的，\x01",
            "导力引擎好像没有问题。\x02\x03",

            "其它飞翔引擎的情况\x01",
            "必须等检查后才会知道……\x02\x03",

            "不过也许比预想中更快\x01",
            "就可以起飞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1006F啊，这可真是个好消息。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        (
            "#1040F真是个让人开心的消息呢。\x02\x03",

            "……提妲\x01",
            "也要努力帮忙哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(    #102
        0xB,
        (
            "#560F嗯，那当然！\x02\x03",

            "#067F啊哈～，想不到竟然可以\x01",
            "接触『埃尔赛尤』的飞翔引擎……\x02\x03",

            "嘿、嘿嘿嘿……\x01",
            "真是好开心呀～⊙\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(60)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3827")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_3865")

    label("loc_3827")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_384E")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_3865")

    label("loc_384E")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_3865")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_388C")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_38CA")

    label("loc_388C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38B3")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_38CA")

    label("loc_38B3")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_38CA")

    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3922")

    ChrTalk(    #103
        0x106,
        (
            "#551F看起来好像\x01",
            "变了一个人似的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1016F啊、啊哈哈……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3961")

    label("loc_3922")


    ChrTalk(    #105
        0x101,
        (
            "#1016F啊、啊哈哈……\x02\x03",

            "……似乎燃起了\x01",
            "她对于机械的狂热呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3961")

    OP_A2(0x22C0)
    Jump("loc_39BE")

    label("loc_3967")


    ChrTalk(    #106
        0xB,
        (
            "#067F啊哈～，『埃尔赛尤』的\x01",
            "导力引擎和结晶回路吗～\x02\x03",

            "嘿、嘿嘿嘿……\x01",
            "真是好开心呀⊙\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BE")

    Jump("loc_424F")

    label("loc_39C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_3AF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ABD")
    TurnDirection(0xB, 0x101, 0)

    ChrTalk(    #107
        0xB,
        (
            "#063F啊……\x01",
            "姐姐，哥哥……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1010F没关系……\x01",
            "我知道你想说什么。\x02\x03",

            "#1000F玲的事情\x01",
            "就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#1040F虽然不知道\x01",
            "能不能顺利解决……\x02\x03",

            "但无论如何，现在\x01",
            "只能尽一切最大的努力了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(    #110
        0xB,
        "#063F嗯、嗯……拜托了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1E41)
    Jump("loc_3AEE")

    label("loc_3ABD")

    TurnDirection(0xB, 0x101, 0)

    ChrTalk(    #111
        0xB,
        (
            "#063F姐姐，哥哥……\x01",
            "玲就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AEE")

    Jump("loc_424F")

    label("loc_3AF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_3D80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D1C")

    ChrTalk(    #112
        0xB,
        "#060F啊，姐姐是你们。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1001F嗨，提妲。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x103,
        "#020F博士的研究进展如何？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 400)

    ChrTalk(    #115
        0xB,
        (
            "#063F嗯、嗯嗯……\x02\x03",

            "#561F似乎就连神通广大的爷爷\x01",
            "也正在为结界烦恼。\x02\x03",

            "他说还是不明白它的原理……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#1015F是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        (
            "#1043F结界与执行者的目的\x01",
            "应该有着某种关联才对……\x02\x03",

            "用普通的方法\x01",
            "看来还是行不通的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x103,
        (
            "#020F算了，在这里\x01",
            "发牢骚也无济于事。\x02\x03",

            "研究就交给博士，\x01",
            "我们几个向着塔进发吧。\x02\x03",

            "如果塔的调查有所进展，\x01",
            "应该会找到研究的线索才对。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #119
        0x101,
        (
            "#1011F啊，嗯……\x01",
            "还有数据水晶。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #120
        0x102,
        (
            "#1040F说得也是。\x01",
            "目前就集中在塔的调查上吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E2B)
    Jump("loc_3D7D")

    label("loc_3D1C")


    ChrTalk(    #121
        0xB,
        (
            "#063F似乎就连神通广大的爷爷\x01",
            "也正在为结界烦恼。\x02\x03",

            "要是姐姐你们在调查中\x01",
            "可以找到线索就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D7D")

    Jump("loc_424F")

    label("loc_3D80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_3D8A")
    Jump("loc_424F")

    label("loc_3D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_424F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4206")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E45")

    ChrTalk(    #122
        0xB,
        "#060F阿、阿加特哥哥……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x106,
        (
            "#051F哟，小鬼。\x02\x03",

            "你这么迫不及待地\x01",
            "跑来给爷爷添麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xB,
        (
            "#063F我、我不是在添麻烦啊！\x02\x03",

            "我、我只是看一下\x01",
            "研究的情况而已。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3EC3")

    label("loc_3E45")


    ChrTalk(    #125
        0xB,
        "#060F啊，姐姐，是你们……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1001F啊哈哈，这么快\x01",
            "就跑到博士这里来了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xB,
        (
            "#560F嗯、嗯……\x02\x03",

            "我来看一下\x01",
            "研究的情况。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 1)), scpexpr(EXPR_END)), "loc_3F31")

    ChrTalk(    #128
        0x102,
        (
            "#1043F塔的现象分析以及\x01",
            "那个『装置』的开发吗……\x02\x03",

            "同时指挥着两项工作\x01",
            "看来就算是博士也会很辛苦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4034")

    label("loc_3F31")


    ChrTalk(    #129
        0x102,
        (
            "#1040F已经开始对塔的现象\x01",
            "着手进行分析了吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x102, 400)

    ChrTalk(    #130
        0xB,
        (
            "#060F嗯，正在分析中……\x02\x03",

            "#561F不过爷爷似乎\x01",
            "还在进行着别的研究。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        "#1004F别、别的研究？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x102,
        (
            "#1044F不光是分析现象而已，\x01",
            "一方面也在进行别的研究吗？\x02\x03",

            "同时指挥着两项工作，\x01",
            "看来就算是博士也会很辛苦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4034")

    TurnDirection(0xB, 0x102, 400)

    ChrTalk(    #133
        0xB,
        (
            "#060F嗯，所以说……\x02\x03",

            "如果有我能做的事，\x01",
            "我会非常乐意帮忙的。\x02\x03",

            "当然，我也会帮姐姐你们\x01",
            "进行调查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        (
            "#1006F好啊。\x01",
            "就这么决定吧。\x02\x03",

            "需要提妲帮忙的时候\x01",
            "我们会过来找你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x102,
        (
            "#1049F说得也是。\x01",
            "而且博士这边也需要助手。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C6")

    ChrTalk(    #136
        0x106,
        (
            "#552F是啊，如果不管管老爷子的话，\x01",
            "搞不好他的两项研究会变成三项呢。\x02\x03",

            "……还是好好地看着他吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xB,
        (
            "#560F嘿嘿，也对……\x02\x03",

            "阿加特哥哥……\x01",
            "你也要多加小心哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4200")

    label("loc_41C6")


    ChrTalk(    #138
        0xB,
        (
            "#560F嗯、嗯！　我会努力的。\x02\x03",

            "姐姐你们要\x01",
            "多加小心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4200")

    OP_A2(0x1E2C)
    Jump("loc_424F")

    label("loc_4206")


    ChrTalk(    #139
        0xB,
        (
            "#060F虽然我正在担任\x01",
            "爷爷的助手……\x02\x03",

            "不过需要我的话\x01",
            "请随时跟我说哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_424F")

    Jump("loc_4275")

    label("loc_4252")


    ChrTalk(    #140
        0xB,
        "#060F要更换成员吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 21)
    Jump("loc_4275")

    label("loc_4272")

    Jump("loc_4275")

    label("loc_4275")

    TalkEnd(0xFE)
    Return()

    # Function_7_2921 end

    def Function_8_4279(): pass

    label("Function_8_4279")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_42A1")

    ChrTalk(    #141
        0xFE,
        "#070F◆没有台词。\x02",
    )

    CloseMessageWindow()
    Call(0, 21)
    Jump("loc_4755")

    label("loc_42A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_4755")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46DC")

    def lambda_42B6():
        TurnDirection(0xC, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_42B6)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #142
        0xC,
        (
            "#070F哟，这不是艾丝蒂尔吗。\x02\x03",

            "怎么跑到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1000F金先生也是。\x01",
            "在这种地方做什么呢？\x02\x03",

            "#1018F啊，莫非是在睡午觉？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xC,
        (
            "#071F哈哈，那倒也不错，\x01",
            "不过我正想稍微训练一下。\x02\x03",

            "一直待在狭小的地方不动，\x01",
            "总觉得老是无法平静下来。\x02\x03",

            "#070F话说回来，你好像\x01",
            "也正在四处散步啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#1007F我也很不擅长待在\x01",
            "同一个地方不动……\x02\x03",

            "#1015F不过虽说是训练……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(500)

    ChrTalk(    #146
        0x101,
        (
            "#1015F……在这里运动\x01",
            "不会太过狭窄吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xC,
        (
            "#070F怎么会，并非只有运动\x01",
            "才可以算得上是训练。\x02\x03",

            "只要有了这样的空间，\x01",
            "可以做的事情很多呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)

    ChrTalk(    #148
        0x101,
        "#1000F咦，比如说呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xC,
        (
            "#074F瞑想或呼吸法这些就不用提了，\x01",
            "形态的复习也是一种重要的锻炼。\x02\x03",

            "我们游击士\x01",
            "动不动就进行实战，很容易崩溃的。\x02\x03",

            "#070F有时候回归到基础层面，\x01",
            "调整好自我也是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        (
            "#1013F的确，我最近好像\x01",
            "的确没怎么做形态练习。    \x02\x03",

            "听金先生这么一说，\x01",
            "有点着急呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xC,
        (
            "#070F哈哈，别那么在意。\x01",
            "我刚才说的只是一般的理论。\x02\x03",

            "不过，要是你有这个想法的话，\x01",
            "试着专心练习一下没有坏处的。\x02\x03",

            "如果不嫌弃，\x01",
            "我很愿意当你练习的对手。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#1001F嘿嘿，到时候\x01",
            "就拜托你了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xC,
        "#070F嗯，我很期待。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xC, 0)
    OP_A2(0x1A22)
    Jump("loc_4755")

    label("loc_46DC")


    def lambda_46E2():
        TurnDirection(0xC, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_46E2)
    SetChrChipByIndex(0xC, 4)
    SetChrSubChip(0xC, 0)
    WaitChrThread(0xC, 0x1)

    ChrTalk(    #154
        0xC,
        (
            "#070F我打算在这里\x01",
            "继续练习一阵子。\x02\x03",

            "在龙出现之前\x01",
            "让身体慢慢地热起来。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 90, 400)
    SetChrChipByIndex(0xC, 14)
    SetChrSubChip(0xC, 0)

    label("loc_4755")

    TalkEnd(0xFE)
    Return()

    # Function_8_4279 end

    def Function_9_4759(): pass

    label("Function_9_4759")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_47BA"),
        (1, "loc_590A"),
        (2, "loc_593A"),
        (SWITCH_DEFAULT, "loc_593D"),
    )


    label("loc_47BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_492F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48B8")

    ChrTalk(    #155
        0xD,
        (
            "#1060F剩下的探索地点是中枢塔……\x01",
            "感觉终于要迎接最后结局了呢。\x02\x03",

            "『结社』的那些家伙\x01",
            "应该也会认真起来了，\x01",
            "用一般的方法大概行不通……\x02\x03",

            "好了，既然已经走到这一步\x01",
            "我们就要朝着圆满的结局去努力。\x02\x03",

            "早点找到『辉之环』\x01",
            "大家一起返回地面吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_492C")

    label("loc_48B8")


    ChrTalk(    #156
        0xD,
        (
            "#1060F剩下的探索地点是中枢塔……\x01",
            "有种要迎接最后结局的感觉呢。\x02\x03",

            "不嫌弃的话，我会贡献一份力量。\x01",
            "欢迎随时来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_492C")

    Jump("loc_5907")

    label("loc_492F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_4A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49FA")

    ChrTalk(    #157
        0xD,
        (
            "#1060F听说空贼团那些家伙\x01",
            "要跟我们一起合作。\x02\x03",

            "嗯，我倒是很赞成。\x01",
            "毕竟同伴越多越好嘛。\x02\x03",

            "其实，我也正在考虑\x01",
            "自己可以帮上什么忙。\x02\x03",

            "像是提供药品之类的，\x01",
            "总之先从这些方面开始做起吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_4A62")

    label("loc_49FA")


    ChrTalk(    #158
        0xD,
        (
            "#1060F我自己也在考虑\x01",
            "能够对空贼团进行哪些协助。\x02\x03",

            "像是提供药品之类的，\x01",
            "总之先从这些方面开始做起吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A62")

    Jump("loc_5907")

    label("loc_4A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_4D71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x454, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BBC")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #159
        0xD,
        (
            "#1060F你叫乔丝特对吧？\x02\x03",

            "我叫凯文·格拉汉姆。\x01",
            "是七耀教会的神父。\x02\x03",

            "#1061F我最欢迎可爱的女孩子，\x01",
            "所以今后就请多多指教啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x10B,
        (
            "#215F嗯、嗯……\x01",
            "多多指教倒是无妨……\x02\x03",

            "#212F……不过你真的是神父吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xD,
        (
            "#1060F嗯！如假包换。\x02\x03",

            "#1064F……喂，什么嘛，\x01",
            "那摆明就是怀疑的眼神。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x10B,
        "#212F（盯─────……）\x02",
    )

    CloseMessageWindow()
    OP_A2(0xD)
    OP_A2(0x22A4)
    Jump("loc_4D6E")

    label("loc_4BBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C59")
    TurnDirection(0xFE, 0x10B, 0)

    ChrTalk(    #163
        0xD,
        (
            "#1064F我说啊，我可是\x01",
            "如假包换的神父啊。\x02\x03",

            "#1068F唉，居然被一个小女孩怀疑，\x01",
            "我真是太悲哀了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10B,
        "#413F（果、果然很可疑……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_4D6E")

    label("loc_4C59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D04")

    ChrTalk(    #165
        0xD,
        (
            "#1063F大概是体力劳动太多的缘故，\x01",
            "受伤的人相当多。\x02\x03",

            "不过，虽说只是擦伤而已，\x01",
            "大家还是要多加小心才行。\x02\x03",

            "不知道得坚持到什么时候，\x01",
            "而且药还是必须省着点用。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_4D6E")

    label("loc_4D04")


    ChrTalk(    #166
        0xD,
        (
            "#1063F大概是体力劳动太多的缘故，\x01",
            "受伤的人相当多。\x02\x03",

            "不过，虽说只是擦伤而已，\x01",
            "大家还是要多加小心才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D6E")

    Jump("loc_5907")

    label("loc_4D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_4E92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E2D")

    ChrTalk(    #167
        0xD,
        (
            "#1062F哟，是艾丝蒂尔你们啊。\x02\x03",

            "医务室也刚好\x01",
            "收拾完毕了。\x02\x03",

            "#1066F由于迫降时的冲击，\x01",
            "导致架子内部全都倒塌了。\x02\x03",

            "不过，如果身体不舒服的话\x01",
            "可别客气，尽管来找我就是了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_4E8F")

    label("loc_4E2D")


    ChrTalk(    #168
        0xD,
        (
            "#1060F如果身体不舒服的话，\x01",
            "随时来找我就是了。\x02\x03",

            "干我们这一行的，\x01",
            "再怎么说，身体也都是本钱啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E8F")

    Jump("loc_5907")

    label("loc_4E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_5300")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5218")

    ChrTalk(    #169
        0xD,
        (
            "#1067F哎呀呀……\x01",
            "最后的执行者是那个小姑娘吗？\x02\x03",

            "我还在心里暗自想着，\x01",
            "她要是这次不会出现就好了……\x02\x03",

            "#1068F嗯，天底下毕竟\x01",
            "不会有这么顺利的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#1003F嗯……\x01",
            "一开始我也那么想……\x02\x03",

            "#1002F不过换个角度来看，\x01",
            "这也许这是个很好的机会。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #171
        0xD,
        "#1064F咦……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        (
            "#1015F我们希望她能退出结社，\x01",
            "同时也有很多话想对她说……\x02\x03",

            "像这种想要传达什么事情时候，\x01",
            "直接见面是无疑最好的方法了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xD,
        (
            "#1066F哈哈，原来如此。\x01",
            "这种想法也是很有道理呢。\x02\x03",

            "#1071F不愧是艾丝蒂尔。\x01",
            "思考方式相当地乐观呢。\x02\x03",

            "哎～，真是越来越………………\x01",
            "……………………………………\x02\x03",

            "#1063F……咳咳，没什么没什么。\x01",
            "只是不自觉就按平常的方式说话。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #174
        0x101,
        "#1011F越来越……怎样呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xD,
        "#1068F啊，你就别去在意了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x102,
        "#1048F对不起，凯文先生……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(    #177
        0xD,
        (
            "#1066F没关系没关系。\x01",
            "反正是我不好。\x02\x03",

            "原谅我吧，\x01",
            "下次我会注意气氛的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1019F……又是男人之间\x01",
            "在悄悄地互通声气。\x02\x03",

            "看起来真的好恶心……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    OP_A2(0x1E2E)
    Jump("loc_52FD")

    label("loc_5218")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_52A5")

    ChrTalk(    #179
        0xD,
        (
            "#1060F不过，不管怎么说，\x01",
            "像艾丝蒂尔这样乐观积极的\x01",
            "思考方式是相当不错的呢。\x02\x03",

            "哎，面对这样积极的女孩，\x01",
            "大哥哥丝毫没有抵抗力啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52FD")

    label("loc_52A5")


    ChrTalk(    #180
        0xD,
        (
            "#1060F艾丝蒂尔说得对，\x01",
            "我们要积极地行动下去。\x02\x03",

            "光是想着坏的一面\x01",
            "是完全无济于事的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52FD")

    Jump("loc_5907")

    label("loc_5300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_5427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53DB")

    ChrTalk(    #181
        0xD,
        (
            "#1064F不过，想不到居然能够\x01",
            "一个人独自登上里塔……\x02\x03",

            "真是一位\x01",
            "可怕的大姐姐呢。\x02\x03",

            "#1064F看来我们这些男生\x01",
            "也必须多加小心才行啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(    #182
        0xD,
        "#1061F……对吧，约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x102,
        "#1048F……为、为什么问我？\x02",
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_5424")

    label("loc_53DB")


    ChrTalk(    #184
        0xD,
        (
            "#1060F想不到居然能够\x01",
            "一个人独自登上里塔。\x02\x03",

            "女人的执念真是可怕极了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5424")

    Jump("loc_5907")

    label("loc_5427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_557B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5506")

    ChrTalk(    #185
        0xD,
        (
            "#1063F在塔内延伸开来的『里塔』\x01",
            "以及塔顶的『福音β』吗……\x02\x03",

            "虽然还不清楚敌人的目的，\x01",
            "不过感觉是越来越可疑了。\x02\x03",

            "#1062F总之，这种时候\x01",
            "必须要互相帮助才行。\x02\x03",

            "我也已经准备好了，\x01",
            "需要的时候随时跟我说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xC)
    Jump("loc_5578")

    label("loc_5506")


    ChrTalk(    #186
        0xD,
        (
            "#1063F在塔内延伸开来的『里塔』\x01",
            "以及塔顶的『福音β』吗……\x02\x03",

            "虽然还不清楚敌人的目的，\x01",
            "不过感觉是越来越可疑了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5578")

    Jump("loc_5907")

    label("loc_557B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_5907")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58B1")

    ChrTalk(    #187
        0xD,
        (
            "#1062F哦，是艾丝蒂尔你们。\x01",
            "现在要前往塔内吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#1006F嗯，准备好就出发。\x02\x03",

            "凯文先生在做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #189
        0xD,
        (
            "#1060F我刚刚参观完\x01",
            "这艘船上的医疗设施。\x02\x03",

            "毕竟等到要使用的时候\x01",
            "再开始准备就太晚了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x102,
        (
            "#1049F想不到您也具备现代医学的知识，\x01",
            "真不愧是『星杯骑士』呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x102, 400)

    ChrTalk(    #191
        0xD,
        (
            "#1066F哈哈，竟然会受到这种恭维。\x01",
            "其实我只是赶鸭子上架而已啊。\x02\x03",

            "再说，我也不是\x01",
            "负责掌管这个房间的人。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5738")

    ChrTalk(    #192
        0x105,
        "#047F是啊，您说得没错呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_57BB")

    label("loc_5738")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5760")

    ChrTalk(    #193
        0x108,
        "#070F啊，是啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_57BB")

    label("loc_5760")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5790")

    ChrTalk(    #194
        0x103,
        "#026F嗯，跟您说的一样……\x02",
    )

    CloseMessageWindow()
    Jump("loc_57BB")

    label("loc_5790")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_57BB")

    ChrTalk(    #195
        0x106,
        "#050F嗯嗯，完全正确……\x02",
    )

    CloseMessageWindow()

    label("loc_57BB")


    ChrTalk(    #196
        0x101,
        (
            "#1002F为了不麻烦神父治疗，\x01",
            "进行搜索时必须谨慎点才行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x102,
        (
            "#1042F嗯，小心翼翼地前进吧。\x02\x03",

            "而且也不知道塔本身\x01",
            "还隐藏着什么样的危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xD,
        (
            "#1060F没错没错，这种\x01",
            "小心谨慎的心态是最重要的。\x02\x03",

            "无论如何，大家都不要勉强，\x01",
            "一起平平安安地回来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E2D)
    Jump("loc_5907")

    label("loc_58B1")


    ChrTalk(    #199
        0xD,
        (
            "#1060F这个地方若是派不上用场，\x01",
            "那就再好不过了。\x02\x03",

            "艾丝蒂尔你们\x01",
            "也一定要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5907")

    Jump("loc_593D")

    label("loc_590A")


    ChrTalk(    #200
        0xD,
        (
            "#1060F好了，来了。\x01",
            "要调换成员是吧。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 21)
    Jump("loc_593D")

    label("loc_593A")

    Jump("loc_593D")

    label("loc_593D")

    TalkEnd(0xFE)
    Return()

    # Function_9_4759 end

    def Function_10_5941(): pass

    label("Function_10_5941")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_59A2"),
        (1, "loc_5C78"),
        (2, "loc_5CA3"),
        (SWITCH_DEFAULT, "loc_5CA6"),
    )


    label("loc_59A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_5AC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A58")

    ChrTalk(    #201
        0xE,
        (
            "#210F『山猫号』的修理\x01",
            "似乎也进展顺利。\x02\x03",

            "航行控制的问题\x01",
            "在接受拉赛尔博士的建议后，\x01",
            "好像也已经设法解决了哦。\x02\x03",

            "真不愧是王国第一的学者，\x01",
            "连吉尔哥也深感佩服呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xF)
    Jump("loc_5AC6")

    label("loc_5A58")


    ChrTalk(    #202
        0xE,
        (
            "#210F『山猫号』的修理\x01",
            "似乎也进展顺利。\x02\x03",

            "航行控制的问题\x01",
            "在接受拉赛尔博士的建议后，\x01",
            "好像也已经设法解决了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AC6")

    Jump("loc_5C75")

    label("loc_5AC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_5C75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x459, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C10")

    ChrTalk(    #203
        0xE,
        (
            "#210F喂，你们几个。\x02\x03",

            "虽说我是联络员，\x01",
            "不过有事也要让我帮忙啊。\x02\x03",

            "而且你们还救了大哥他们，\x01",
            "我可不想再继续欠人情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        (
            "#1007F呼，该说你这个人\x01",
            "好强还是固执好呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x102,
        (
            "#1040F不过，多亏有你帮忙。\x02\x03",

            "因为我们游击士\x01",
            "没办法帮忙维护装备。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x102, 400)

    ChrTalk(    #206
        0xE,
        (
            "#414F…………啊…………………\x02\x03",

            "#415F嗯、嗯！就交给我吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22CE)
    Jump("loc_5C75")

    label("loc_5C10")


    ChrTalk(    #207
        0xE,
        (
            "#210F虽说我是联络员\x01",
            "不过有事也要让我帮忙啊。\x02\x03",

            "而且你们还救了大哥他们，\x01",
            "我可不想再继续欠人情了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C75")

    Jump("loc_5CA6")

    label("loc_5C78")


    ChrTalk(    #208
        0xE,
        (
            "#210F嘿嘿，\x01",
            "果然没有我不行呢。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 21)
    Jump("loc_5CA6")

    label("loc_5CA3")

    Jump("loc_5CA6")

    label("loc_5CA6")

    TalkEnd(0xFE)
    Return()

    # Function_10_5941 end

    def Function_11_5CAA(): pass

    label("Function_11_5CAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_5E54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DEE")

    ChrTalk(    #209
        0xFE,
        (
            "虽然之前反复进行过\x01",
            "挑战性能极限的测试……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "但是测试终究是测试。\x01",
            "与实战中的机动完全是两回事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "新型引擎究竟能发挥多大作用，\x01",
            "我们开发者也是怀着\x01",
            "期待与不安各半的心情啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "不过，只要顺利完成本次作战，\x01",
            "这个引擎也就可以独当一面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "就让我像送别离巢的雏鸟那样，\x01",
            "来记录下最后的数据吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_5E54")

    label("loc_5DEE")


    ChrTalk(    #214
        0xFE,
        (
            "虽说之前反复进行了测试\x01",
            "但实战毕竟是完全不同的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "我们开发者也是怀着\x01",
            "期待与不安各半的心情啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E54")

    TalkEnd(0xFE)
    Return()

    # Function_11_5CAA end

    def Function_12_5E58(): pass

    label("Function_12_5E58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_5F47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F03")

    ChrTalk(    #216
        0xFE,
        (
            "好了……\x01",
            "计量器的检查完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "毕竟作战中的引擎状态\x01",
            "可不是每天都能测量到的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "为了今后导力引擎的开发，\x01",
            "必须好好利用这次机会才行呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_5F47")

    label("loc_5F03")


    ChrTalk(    #219
        0xFE,
        (
            "好了……\x01",
            "计量器的检查完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "那么，接下来\x01",
            "就等龙出现了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F47")

    TalkEnd(0xFE)
    Return()

    # Function_12_5E58 end

    def Function_13_5F4B(): pass

    label("Function_13_5F4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60A0")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #221
        0xFE,
        "喵～～～\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #222
        0x101,
        "#1004F啊，安东尼！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FF5")

    ChrTalk(    #223
        0x107,
        (
            "#067F嘿嘿嘿……\x01",
            "很吃惊吧？\x02\x03",

            "不管怎么看\x01",
            "都像是雷伊哥哥带来的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_601E")

    label("loc_5FF5")


    ChrTalk(    #224
        0x102,
        (
            "#1044F是中央工房的人\x01",
            "带来的吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_601E")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #225
        0xFE,
        "喵？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x101,
        (
            "#1016F唔～为什么会在\x01",
            "这种紧张的形势下再次见面呢。\x02\x03",

            "呼，不管怎么说，\x01",
            "这阵子还请多关照了。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #227
        0xFE,
        "喵～\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1E4C)
    Jump("loc_60AF")

    label("loc_60A0")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #228
        0xFE,
        "喵？\x02",
    )

    CloseMessageWindow()

    label("loc_60AF")

    TalkEnd(0xFE)
    Return()

    # Function_13_5F4B end

    def Function_14_60B3(): pass

    label("Function_14_60B3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_61D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_617D")

    ChrTalk(    #229
        0xFE,
        (
            "哦……\x01",
            "你就是大家所说的游击士吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "没想到那个摩尔根将军\x01",
            "竟然会提议让游击士同行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "啊，王国军的风气\x01",
            "也有了很大变化呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "这就是准将的组织改革\x01",
            "正在逐步推行的证据。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_61D9")

    label("loc_617D")


    ChrTalk(    #233
        0xFE,
        (
            "没想到那个摩尔根将军\x01",
            "竟然会提议让游击士同行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "啊，王国军的风气\x01",
            "也有了很大变化呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61D9")

    TalkEnd(0xFE)
    Return()

    # Function_14_60B3 end

    def Function_15_61DD(): pass

    label("Function_15_61DD")

    TalkBegin(0xFE)
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_6287")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6257")

    ChrTalk(    #235
        0xFE,
        (
            "呼嗯～嗯……\x01",
            "嗬，已经到换岗的时间了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "虽然完全没睡，\x01",
            "不过还是得赶快上岗……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_6284")

    label("loc_6257")


    ChrTalk(    #237
        0xFE,
        (
            "呼嗯～嗯……\x01",
            "嗬，已经到换岗的时间了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6284")

    Jump("loc_6BBF")

    label("loc_6287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_6446")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6380")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6327")

    ChrTalk(    #238
        0xFE,
        (
            "哦，公主殿下……\x01",
            "每次都让您受累了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "陛下托付的使命\x01",
            "看来也快要完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "那，最后一座塔\x01",
            "也请您鼓足干劲完成任务吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_637D")

    label("loc_6327")


    ChrTalk(    #241
        0xFE,
        (
            "陛下托付的使命\x01",
            "看来也快要完成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "那，最后一座塔\x01",
            "也请您鼓足干劲完成任务吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_637D")

    Jump("loc_6443")

    label("loc_6380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_640D")

    ChrTalk(    #243
        0xFE,
        (
            "哎呀呀，\x01",
            "看来整件事情就快要结束了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "好了，一鼓作气\x01",
            "把它解决掉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "结局圆满即是一切圆满，\x01",
            "过去的人经常这么说的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_6443")

    label("loc_640D")


    ChrTalk(    #246
        0xFE,
        (
            "一鼓作气\x01",
            "把它解决掉吧。\x01",
            "结局圆满即是一切圆满啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6443")

    Jump("loc_6BBF")

    label("loc_6446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_6660")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6561")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64FA")

    ChrTalk(    #247
        0xFE,
        (
            "继蔡斯之后，卢安也\x01",
            "出现了结社的爪牙吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "总觉得整个王国里\x01",
            "好像都潜藏着敌人的爪牙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "公主殿下也要多加小心哦。\x01",
            "不知道敌人会躲在哪里。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_655E")

    label("loc_64FA")


    ChrTalk(    #250
        0xFE,
        (
            "总觉得整个王国里\x01",
            "好像都潜藏着敌人的爪牙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "公主殿下也要多加小心哦。\x01",
            "不知道敌人会躲在哪里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_655E")

    Jump("loc_665D")

    label("loc_6561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6603")

    ChrTalk(    #252
        0xFE,
        (
            "总觉得整个王国里\x01",
            "都潜藏着结社的爪牙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "这种气氛与情报部\x01",
            "发动政变时很相似。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "真是的，为什么这些\x01",
            "图谋不轨的家伙们总是\x01",
            "不断地涌现出来呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_665D")

    label("loc_6603")


    ChrTalk(    #255
        0xFE,
        (
            "总觉得整个王国里\x01",
            "都潜藏着结社的爪牙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "这种气氛与情报部\x01",
            "发动政变时越来越相似了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_665D")

    Jump("loc_6BBF")

    label("loc_6660")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_694E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_66D7")

    ChrTalk(    #257
        0xFE,
        (
            "把古代的结晶回路\x01",
            "装配在导力器中……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        (
            "实在令人难以想象啊。\x01",
            "真是个不得了的老头子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_67C0")

    label("loc_66D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6768")

    ChrTalk(    #259
        0xFE,
        (
            "哎呀，公主殿下……\x01",
            "来工作室有什么事情吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "拉赛尔博士正在里面\x01",
            "分析那个黑色机器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "这里乱七八糟的\x01",
            "请留意不要被绊倒了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_67C0")

    label("loc_6768")


    ChrTalk(    #262
        0xFE,
        (
            "拉赛尔博士正在工作室里\x01",
            "分析那个黑色机器。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xFE,
        (
            "里面乱七八糟的\x01",
            "请留意不要被绊倒了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67C0")

    Jump("loc_694B")

    label("loc_67C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_6827")

    ChrTalk(    #264
        0xFE,
        (
            "把古代的结晶回路\x01",
            "装配在导力器中……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "实在令人难以想象啊。\x01",
            "真是个不得了的老头子。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_694B")

    label("loc_6827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68F3")

    ChrTalk(    #266
        0xFE,
        (
            "刚才博士好像拿着一个\x01",
            "奇怪的黑东西进去了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "难道说那个就是\x01",
            "你们在塔里发现的东西吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "结社想用那种东西\x01",
            "来做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xFE,
        (
            "希望博士的研究能进展顺利，\x01",
            "早日弄清敌人的目的就好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_694B")

    label("loc_68F3")


    ChrTalk(    #270
        0xFE,
        (
            "结社想用那黑色机器\x01",
            "来做什么呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        (
            "完全不明白敌人的目的，\x01",
            "心情实在是非常糟糕啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_694B")

    Jump("loc_6BBF")

    label("loc_694E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_6BBF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6A86")

    ChrTalk(    #272
        0xFE,
        (
            "哎呀呀……\x01",
            "没想到公主殿下亲临。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xFE,
        (
            "莫非您打算和游击士\x01",
            "一起进入塔内吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x105,
        (
            "#040F是啊，我是这个打算。\x02\x03",

            "现在不是一个人\x01",
            "置身事外的时候了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "呼～，不愧是公主殿下。\x01",
            "实在是很了不起的决心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        (
            "既然如此，请您先在\x01",
            "工作室调整好装备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "佩顿那家伙\x01",
            "似乎在准备什么的样子。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_6AE0")

    label("loc_6A86")


    ChrTalk(    #278
        0xFE,
        (
            "若要前往塔内，请先在\x01",
            "工作室调整好装备吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "战斗并不是光靠意志\x01",
            "和气势就能取胜的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6AE0")

    Jump("loc_6BBF")

    label("loc_6AE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B61")

    ChrTalk(    #280
        0xFE,
        "哦，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "从这里进去是工作室，\x01",
            "往另一边走的话就是货舱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "如果要用升降机，\x01",
            "就去货舱那边看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xB)
    Jump("loc_6BBF")

    label("loc_6B61")


    ChrTalk(    #283
        0xFE,
        (
            "这个房间就是工作室，\x01",
            "往另一边走的话就是货舱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "如果要用升降机，\x01",
            "就去货舱那边看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BBF")

    TalkEnd(0xFE)
    Return()

    # Function_15_61DD end

    def Function_16_6BC3(): pass

    label("Function_16_6BC3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_6D8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D06")

    ChrTalk(    #285
        0xFE,
        (
            "理论的补充修正总算完成了，\x01",
            "这下『装置』的制造也有了头绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "不过，虽然说理论已经完成了，\x01",
            "但还只是数学公式的程度而已……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        (
            "可笑的是，我们目前\x01",
            "也不明白这公式的意义。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "我们证明了其正确性，\x01",
            "却不知道我们证明的是什么东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "这虽然是一件相当讽刺的事情，\x01",
            "但在导力理论界里却是常有的事。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_6D8A")

    label("loc_6D06")


    ChrTalk(    #290
        0xFE,
        (
            "理论的补充修正总算完成了，\x01",
            "这下『装置』的制造也有了头绪。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "是啊，这是一个艰难的研究项目\x01",
            "不过也因此度过了一段充实的时光呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D8A")

    Jump("loc_6F05")

    label("loc_6D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_6F05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E9D")

    ChrTalk(    #292
        0xFE,
        (
            "实验室终于开始\x01",
            "培育新的农作物了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        (
            "可我听说这里在进行一项有趣的研究，\x01",
            "于是就急急忙忙地跑到这船上来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "不过，从博士的话来看\x01",
            "我的决定似乎是正确的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "真想不到居然要\x01",
            "从正面挑战那个问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        (
            "呵呵，看来这将会是\x01",
            "一项很刺激的计划哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_6F05")

    label("loc_6E9D")


    ChrTalk(    #297
        0xFE,
        (
            "真想不到居然要\x01",
            "从正面挑战那个问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "哎呀，不愧是拉赛尔博士。\x01",
            "与那边的研究人员有着不同的志向。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F05")

    TalkEnd(0xFE)
    Return()

    # Function_16_6BC3 end

    def Function_17_6F09(): pass

    label("Function_17_6F09")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_6F83")

    ChrTalk(    #299
        0xFE,
        (
            "研究也总算是\x01",
            "渐入佳境了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xFE,
        (
            "不知道什么原因，\x01",
            "好像需要大量试制品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xFE,
        (
            "所以现在准备要\x01",
            "紧急进行组装。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71EC")

    label("loc_6F83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_70A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7035")

    ChrTalk(    #302
        0xFE,
        (
            "理论方面就交给博士和雷伊，\x01",
            "我就专心负责回路的试作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xFE,
        (
            "要让这项工作成功\x01",
            "不仅需要理论，也需要技术。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        (
            "所以拥有维修员经验的我\x01",
            "才会被特地请来这里哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_70A1")

    label("loc_7035")


    ChrTalk(    #305
        0xFE,
        (
            "理论方面就交给博士和雷伊，\x01",
            "我就专心负责回路的试作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "这项工作不仅需要理论\x01",
            "也很需要技术人员的能力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70A1")

    Jump("loc_71EC")

    label("loc_70A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_71EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7162")

    ChrTalk(    #307
        0xFE,
        (
            "以博士的研究小组成员名义\x01",
            "接受征召，实在是无上的光荣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xFE,
        (
            "我会竭尽自己所能，\x01",
            "决不拖累研究的进度，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xFE,
        (
            "因为我还想将这一次的所见所闻\x01",
            "说给在卢安等我的弟弟豆豆听呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_71EC")

    label("loc_7162")


    ChrTalk(    #310
        0xFE,
        (
            "我会好好地努力，然后把这一次的\x01",
            "所见所闻说给在卢安等我的弟弟豆豆听哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0xFE,
        (
            "要是跟豆豆说我乘坐了『埃尔赛尤』，\x01",
            "想必那家伙会很羡慕吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71EC")

    TalkEnd(0xFE)
    Return()

    # Function_17_6F09 end

    def Function_18_71F0(): pass

    label("Function_18_71F0")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_7273")

    ChrTalk(    #312
        0x15,
        (
            "第三级改造的事情……\x01",
            "你们应该听博士说过了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x15,
        "我准备好了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x15,
        (
            "由于ＥＰ值也会提升，\x01",
            "请各位积极地去尝试吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x12)

    label("loc_7273")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",            # 0
            "改造·换钱\x01",      # 1
            "买东西\x01",          # 2
            "离开\x01",            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_72DC")
    OP_A9(0x2E)
    Jump("loc_72DE")

    label("loc_72DC")

    OP_A9(0x28)

    label("loc_72DE")

    TalkEnd(0x15)
    Return()

    label("loc_72E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7307")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_72FE")
    OP_A9(0x2D)
    Jump("loc_7300")

    label("loc_72FE")

    OP_A9(0x29)

    label("loc_7300")

    TalkEnd(0x15)
    Return()

    label("loc_7307")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7321")
    FadeToBright(300, 0)
    TalkEnd(0x15)
    Return()

    label("loc_7321")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_741E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73AF")

    ChrTalk(    #315
        0x15,
        "大家辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x15,
        (
            "在进行对中枢塔的搜索之前\x01",
            "请先检查各自的装备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x15,
        (
            "否则战斗开始之后\x01",
            "再后悔就为时已晚了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_741B")

    label("loc_73AF")


    ChrTalk(    #318
        0x15,
        (
            "在进行对中枢塔的搜索之前\x01",
            "请先检查各自的装备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x15,
        (
            "依照人形兵器的种类改变\x01",
            "装饰品的搭配也是很有效的哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_741B")

    Jump("loc_7C21")

    label("loc_741E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_END)), "loc_7528")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74D7")

    ChrTalk(    #320
        0x15,
        (
            "哎呀～，舰内突然就\x01",
            "明亮起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x15,
        (
            "灰暗的心情也随之一扫而空，\x01",
            "灯光果然很重要呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x15,
        (
            "那么，我也来调整心态，\x01",
            "好好地努力工作吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x15,
        (
            "如果有事\x01",
            "尽管来叫我啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_7525")

    label("loc_74D7")


    ChrTalk(    #324
        0x15,
        (
            "哎呀～，舰内突然就\x01",
            "明亮起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x15,
        (
            "我也来调整心态，\x01",
            "好好地努力工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7525")

    Jump("loc_7C21")

    label("loc_7528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_77A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76C5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_760C")
    TurnDirection(0x15, 0x10B, 0)

    ChrTalk(    #326
        0x15,
        "啊，你是乔丝特小姐……吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #327
        0x15,
        (
            "我们也准备了\x01",
            "适合你使用的防具哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0x15,
        (
            "出发之前\x01",
            "请记得先调整好装备。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #329
        0x10B,
        (
            "#211F嘿嘿，准备得挺周到的嘛。\x02\x03",

            "嗯，如果有了这个心思\x01",
            "我会请你们带我去看的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x22C5)
    Jump("loc_76BF")

    label("loc_760C")


    ChrTalk(    #330
        0x15,
        (
            "听说空贼小姐\x01",
            "正在寻找她的兄弟们呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0x15,
        (
            "带她去进行探索的时候，\x01",
            "请千万要检查好装备哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x15,
        "特别是护具要仔细检查。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x15,
        (
            "因为用枪的人，有时候身上\x01",
            "并没有穿戴着合适的防具……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_76BF")

    OP_A2(0x9)
    Jump("loc_779E")

    label("loc_76C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_772D")
    TurnDirection(0x15, 0x10B, 0)

    ChrTalk(    #334
        0x15,
        (
            "我想我所挑选的防具\x01",
            "一定会适合她的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x15,
        (
            "若是方便的话，\x01",
            "请一定要过来看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_779E")

    label("loc_772D")


    ChrTalk(    #336
        0x15,
        (
            "带空贼小姐\x01",
            "去进行探索的时候，\x01",
            "请千万要检查好装备哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x15,
        (
            "因为用枪的人，有时候身上\x01",
            "并没有穿戴着合适的防具。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_779E")

    Jump("loc_7C21")

    label("loc_77A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_7886")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_783D")

    ChrTalk(    #338
        0x15,
        (
            "哎呀～导力器可以运作，\x01",
            "真是一件很棒的事呢～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x15,
        (
            "这样一来，我也可以进行\x01",
            "久违的结晶回路合成了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x15,
        (
            "好了，如果需要什么\x01",
            "请尽管说。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_7883")

    label("loc_783D")


    ChrTalk(    #341
        0x15,
        (
            "总觉得好久没有\x01",
            "合成结晶回路了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x15,
        (
            "如果需要什么\x01",
            "请尽管说啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7883")

    Jump("loc_7C21")

    label("loc_7886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_798F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_791E")

    ChrTalk(    #343
        0x15,
        (
            "还剩一座塔……\x01",
            "这么一来调查也接近尾声了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x15,
        (
            "接下来的战斗\x01",
            "想必会十分严酷吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x15,
        (
            "请不要忘记进行\x01",
            "导力器的调整和装备的检查。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_798C")

    label("loc_791E")


    ChrTalk(    #346
        0x15,
        (
            "塔的调查也终于接近尾声了……\x01",
            "战斗想必也会比以前更加严酷。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x15,
        (
            "请不要忘记进行\x01",
            "导力器的调整和装备的检查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_798C")

    Jump("loc_7C21")

    label("loc_798F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_7AA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A5C")

    ChrTalk(    #348
        0x15,
        "辛苦大家了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x15,
        (
            "博士的研究\x01",
            "似乎碰上了一些问题呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x15,
        (
            "刚才研究人员们\x01",
            "出去休息了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x15,
        (
            "唉，过于刨根究底\x01",
            "反而会使事情的进展停滞不前……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x15,
        (
            "诸位，也偶尔到休息室去\x01",
            "歇口气如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_7AA4")

    label("loc_7A5C")


    ChrTalk(    #353
        0x15,
        (
            "博士的研究\x01",
            "似乎碰上了一些问题呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x15,
        (
            "刚才研究人员们\x01",
            "出去休息了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AA4")

    Jump("loc_7C21")

    label("loc_7AA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_7BB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B3F")

    ChrTalk(    #355
        0x15,
        (
            "博士他们似乎\x01",
            "正在忙于研究呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x15,
        (
            "虽然我也看过了\x01",
            "『装置』的设计图……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x15,
        (
            "但很遗憾，我完全无法理解。\x01",
            "最尖端的研究好厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_7BAF")

    label("loc_7B3F")


    ChrTalk(    #358
        0x15,
        (
            "博士他们正在研究的『装置』，\x01",
            "好像是件很了不得的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x15,
        (
            "很遗憾，虽说看了结构图\x01",
            "我仍然搞不懂它的机能。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BAF")

    Jump("loc_7C21")

    label("loc_7BB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_7C21")

    ChrTalk(    #360
        0x15,
        (
            "需要调整导力器或结晶回路时\x01",
            "请跟我说一声吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x15,
        (
            "这里武器和防具也很齐全，\x01",
            "应该可以进行一般的准备。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C21")

    TalkEnd(0x15)
    Return()

    # Function_18_71F0 end

    def Function_19_7C25(): pass

    label("Function_19_7C25")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_7CBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C8A")

    ChrTalk(    #362
        0xFE,
        "导力引擎……驱动率固定在５０％。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0xFE,
        (
            "导力压正常……\x01",
            "随时可以开始测试。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)
    Jump("loc_7CBD")

    label("loc_7C8A")


    ChrTalk(    #364
        0xFE,
        (
            "驱动率固定在５０％……\x01",
            "导力压正常，没有问题。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CBD")

    TalkEnd(0xFE)
    Return()

    # Function_19_7C25 end

    def Function_20_7CC1(): pass

    label("Function_20_7CC1")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "队伍编成\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7D22"),
        (1, "loc_7E98"),
        (2, "loc_7EC0"),
        (SWITCH_DEFAULT, "loc_7EC3"),
    )


    label("loc_7D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x458, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E48")

    ChrTalk(    #365
        0x9,
        (
            "#023F哎呀，你们几个。\x01",
            "还没出发？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x101,
        "#1015F嗯，还在做各种准备。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x102,
        (
            "#1040F雪拉姐\x01",
            "在整理房间吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #368
        0x9,
        (
            "#020F嗯嗯，算是吧。\x02\x03",

            "修理我也帮不上忙，\x01",
            "整个人闲得发慌呢。\x02\x03",

            "#525F干脆拿着鞭子\x01",
            "去监督那群男人好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x101,
        "#1001F啊哈哈，那样倒也不错。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x102,
        "#1048F还、还请手下留情啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22C3)
    Jump("loc_7E95")

    label("loc_7E48")


    ChrTalk(    #371
        0x9,
        (
            "#020F那么……\x01",
            "现在该做些什么呢。\x02\x03",

            "要是能找到\x01",
            "什么能帮上忙的事就好了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7E95")

    Jump("loc_7EC6")

    label("loc_7E98")


    ChrTalk(    #372
        0x9,
        "#020F哎呀？要更换成员了吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 21)
    Jump("loc_7EC6")

    label("loc_7EC0")

    Jump("loc_7EC6")

    label("loc_7EC3")

    Jump("loc_7EC6")

    label("loc_7EC6")

    TalkEnd(0xFE)
    Return()

    # Function_20_7CC1 end

    def Function_21_7ECA(): pass

    label("Function_21_7ECA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_7F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_7EF8")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    Jump("loc_7F13")

    label("loc_7EF8")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)

    label("loc_7F13")

    Jump("loc_7F94")

    label("loc_7F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_7F39")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    Jump("loc_7F94")

    label("loc_7F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_7F5A")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    Jump("loc_7F94")

    label("loc_7F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_7F7B")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    Jump("loc_7F94")

    label("loc_7F7B")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)

    label("loc_7F94")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_80EE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7FEA")
    SetChrPos(0xB, -2830, 0, 65940, 90)
    ClearChrFlags(0xB, 0x80)

    label("loc_7FEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_800D")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_800D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_803B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8038")
    SetChrPos(0x9, -5340, 0, 59510, 270)
    ClearChrFlags(0x9, 0x80)

    label("loc_8038")

    Jump("loc_80EB")

    label("loc_803B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x445, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8046")
    Jump("loc_80EB")

    label("loc_8046")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8097")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8071")
    SetChrPos(0xE, -5340, 0, 60030, 270)
    ClearChrFlags(0xE, 0x80)

    label("loc_8071")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8094")
    SetChrPos(0xB, -3510, 0, 5330, 0)
    ClearChrFlags(0xB, 0x80)

    label("loc_8094")

    Jump("loc_80EB")

    label("loc_8097")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_80BA")
    SetChrPos(0xE, -5340, 0, 60030, 270)
    ClearChrFlags(0xE, 0x80)

    label("loc_80BA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_80EB")
    OP_44(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 15)
    SetChrPos(0xA, 61300, 250, -40950, 0)

    label("loc_80EB")

    Jump("loc_8208")

    label("loc_80EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_813E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8118")
    SetChrPos(0xB, -860, 0, 64200, 45)
    ClearChrFlags(0xB, 0x80)

    label("loc_8118")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_813B")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_813B")

    Jump("loc_8208")

    label("loc_813E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_818E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8168")
    SetChrPos(0xB, -860, 0, 64200, 45)
    ClearChrFlags(0xB, 0x80)

    label("loc_8168")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_818B")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_818B")

    Jump("loc_8208")

    label("loc_818E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_81BB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_81B8")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_81B8")

    Jump("loc_8208")

    label("loc_81BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_8208")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_81E5")
    SetChrPos(0xB, -4420, 0, 62290, 225)
    ClearChrFlags(0xB, 0x80)

    label("loc_81E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8208")
    SetChrPos(0xD, 62920, 0, 8020, 0)
    ClearChrFlags(0xD, 0x80)

    label("loc_8208")

    OP_0D()
    Return()

    # Function_21_7ECA end

    def Function_22_820A(): pass

    label("Function_22_820A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_822F")
    Call(0, 24)
    Call(0, 25)
    FadeToBright(0, 0)
    Sleep(100)

    label("loc_822F")

    Fade(1000)
    OP_6D(-5110, 0, 64310, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -4820, 0, 63930, 0)
    SetChrPos(0x102, -5720, 0, 63930, 0)
    SetChrPos(0xF8, -4070, 0, 64340, 315)
    SetChrPos(0xF9, -6300, 0, 64440, 45)
    OP_4A(0x8, 255)

    def lambda_82BF():

        label("loc_82BF")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_82BF")

    QueueWorkItem2(0x101, 1, lambda_82BF)

    def lambda_82D0():

        label("loc_82D0")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_82D0")

    QueueWorkItem2(0x102, 1, lambda_82D0)

    def lambda_82E1():

        label("loc_82E1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_82E1")

    QueueWorkItem2(0xF8, 1, lambda_82E1)

    def lambda_82F2():

        label("loc_82F2")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_82F2")

    QueueWorkItem2(0xF9, 1, lambda_82F2)
    OP_0D()
    TurnDirection(0x8, 0x101, 400)
    Sleep(700)

    ChrTalk(    #373
        0x8,
        (
            "#101F哦哦，来得正是时候。\x02\x03",

            "我刚刚把数据水晶\x01",
            "装在了『卡佩尔』上面。\x02\x03",

            "之后只要放着它不管\x01",
            "应该就会得到自动分析的结果。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x101,
        "#1011F#4P这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x102,
        (
            "#1040F自动分析\x01",
            "需要多长时间呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x8,
        (
            "#100F与受损程度有关\x01",
            "不能一概而论。\x02\x03",

            "有时需要花费好几天\x01",
            "所以你们就耐心地等待吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x102,
        "#1040F原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x101,
        (
            "#1015F#4P嗯，既然这样，\x01",
            "光是着急也没有用呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x8,
        (
            "#100F那么，如果获得新的水晶，\x01",
            "请拿来我这里。\x02\x03",

            "我会立刻装在『卡佩尔』上，\x01",
            "让它开始进行自动分析。\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFFC4A, 0x0, 0xFF6E, 0x7D0, 0x0)
    OP_8C(0x8, 0, 400)
    OP_4B(0x8, 255)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    ClearChrFlags(0x8, 0x10)
    OP_65(0x0, 0x1)
    OP_A2(0x1E0B)
    EventEnd(0x0)
    Return()

    # Function_22_820A end

    def Function_23_8503(): pass

    label("Function_23_8503")


    ChrTalk(    #380
        0x8,
        (
            "#101F哦，你们好像又获得\x01",
            "新的数据水晶了呢。\x02\x03",

            "我马上把它装在『卡佩尔』上，\x01",
            "让它来进行自动分析。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x101,
        "#1006F嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #382
        "\x07\x05交出了新获得的数据水晶。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x3FE, 1)
    OP_3F(0x3FF, 1)
    OP_3F(0x400, 1)
    OP_3F(0x401, 1)
    OP_3F(0x402, 1)
    OP_3F(0x403, 1)
    OP_3F(0x404, 1)
    OP_3F(0x405, 1)
    OP_3F(0x406, 1)
    OP_3F(0x407, 1)
    OP_3F(0x408, 1)
    OP_3F(0x409, 1)
    OP_3F(0x412, 1)
    OP_3F(0x413, 1)
    OP_3F(0x414, 1)
    Return()

    # Function_23_8503 end

    def Function_24_8606(): pass

    label("Function_24_8606")

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
        (0, "loc_8680"),
        (1, "loc_8686"),
        (SWITCH_DEFAULT, "loc_868C"),
    )


    label("loc_8680")

    OP_A2(0x1200)
    Jump("loc_868C")

    label("loc_8686")

    OP_A2(0x1201)
    Jump("loc_868C")

    label("loc_868C")

    Return()

    # Function_24_8606 end

    def Function_25_868D(): pass

    label("Function_25_868D")

    FadeToDark(0, 0, -1)
    OP_6D(-18870, 0, -1650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_25_868D end

    def Function_26_871A(): pass

    label("Function_26_871A")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_6D(3300, 2800, 6000, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8778")
    Call(0, 24)
    Call(0, 25)

    label("loc_8778")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrPos(0x8, -1060, 150, 7570, 0)
    OP_4A(0x8, 255)

    def lambda_87A7():
        OP_6D(1600, 0, 1900, 4500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_87A7)
    FadeToBright(1000, 0)
    OP_43(0x101, 0x1, 0x0, 0x1C)
    Sleep(100)
    OP_43(0x102, 0x1, 0x0, 0x1D)
    Sleep(100)
    OP_43(0xF8, 0x1, 0x0, 0x1E)
    Sleep(100)
    OP_43(0xF9, 0x1, 0x0, 0x1F)
    OP_0D()
    OP_43(0x8, 0x1, 0x0, 0x1B)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x12, 15)
    SetChrSubChip(0x12, 0)
    OP_4A(0x12, 0)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_8820():

        label("loc_8820")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_8820")

    QueueWorkItem2(0x8, 1, lambda_8820)
    Sleep(1000)

    ChrTalk(    #383
        0x8,
        (
            "#103F哦哦，你们几个。\x01",
            "来得正好。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_886E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_886E)
    Sleep(120)

    def lambda_8881():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8881)

    def lambda_888F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_888F)
    Sleep(120)

    def lambda_88A2():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_88A2)

    ChrTalk(    #384
        0x101,
        "#1011F啊，拉赛尔博士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x102,
        "#1044F#2P找我们有什么事吗？\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0x20)

    def lambda_88F4():
        OP_6D(-260, 0, 4050, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_88F4)

    def lambda_890C():
        OP_67(0, 7140, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_890C)

    def lambda_8924():
        OP_6B(2680, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8924)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0x21)
    Sleep(400)
    OP_43(0xF8, 0x1, 0x0, 0x22)
    Sleep(600)
    OP_43(0xF9, 0x1, 0x0, 0x23)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x102, 0x2)

    ChrTalk(    #386
        0x8,
        (
            "#100F嗯，其实呢……\x02\x03",

            "在分析数据水晶的时候\x01",
            "发现了一些有趣的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x101,
        "#1015F有趣的事？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x8,
        (
            "#104F嗯，我们之前就已经知道\x01",
            "古代也有类似结晶回路的东西……\x02\x03",

            "#100F而现在终于发现了\x01",
            "将古代的结晶回路装配在\x01",
            "现代的导力器之中的方法。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A87")
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #389
        0x107,
        "#064F真、真的吗，爷爷。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8ABD")

    label("loc_8A87")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #390
        0x101,
        "#1004F是、是真的吗？\x02",
    )

    CloseMessageWindow()

    label("loc_8ABD")


    ChrTalk(    #391
        0x8,
        (
            "#101F呵呵，你们以为我是谁？\x02\x03",

            "#100F……只不过，以你们现在的\x01",
            "结晶孔是无法做到这一点的。\x02\x03",

            "所以针对结晶孔的强化……\x01",
            "第三级的结晶孔改造就势在必行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x102,
        (
            "#1044F#2P也就是说……\x02\x03",

            "可以超越目前的极限，\x01",
            "对结晶孔进行\x01",
            "更进一步的强化是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x8,
        (
            "#100F嗯，是的。\x02\x03",

            "改造的准备已经做好了，\x01",
            "有机会去问问工房那边吧。\x02\x03",

            "等找到了类似那样的结晶回路之后\x01",
            "一定要试试第三级的改造。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x101,
        "#1006F嗯，明白了！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x102,
        "#1040F#2P到时就让我们多加利用吧。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8CB3")

    ChrTalk(    #396
        0x8,
        (
            "#100F我会继续进行分析。\x02\x03",

            "提妲那孩子\x01",
            "就请你们多多关照了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8CE8")

    label("loc_8CB3")


    ChrTalk(    #397
        0x8,
        (
            "#100F我会继续进行分析。\x02\x03",

            "塔的探索就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8CE8")

    OP_8E(0x8, 0xFFFFFBDC, 0x96, 0x1D92, 0x7D0, 0x0)
    OP_6F(0x1, 15)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    Sleep(500)
    SetChrPos(0x8, -950, 0, 65390, 0)
    OP_4B(0x8, 255)
    OP_A2(0x12)
    OP_A2(0x1E4D)
    Fade(500)
    OP_6D(-1060, 0, 2880, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1060, 0, 2880, 180)
    SetChrPos(0x1, -1060, 0, 2880, 180)
    SetChrPos(0x2, -1060, 0, 2880, 180)
    SetChrPos(0x3, -1060, 0, 2880, 180)
    OP_43(0x12, 0x1, 0x0, 0x2A)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_26_871A end

    def Function_27_8DBE(): pass

    label("Function_27_8DBE")

    Sleep(500)
    OP_6F(0x1, 0)
    OP_70(0x1, 0xF)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFBDC, 0x0, 0x11C6, 0x7D0, 0x0)
    Return()

    # Function_27_8DBE end

    def Function_28_8DEB(): pass

    label("Function_28_8DEB")

    SetChrPos(0xFE, 2700, 800, 4000, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x3E8, 0x0)
    OP_90(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_28_8DEB end

    def Function_29_8E2A(): pass

    label("Function_29_8E2A")

    SetChrPos(0xFE, 2700, 1800, 5000, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x3E8, 0x0)
    OP_90(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_29_8E2A end

    def Function_30_8E69(): pass

    label("Function_30_8E69")

    SetChrPos(0xFE, 3400, 1800, 4500, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF254, 0x3E8, 0x0)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_30_8E69 end

    def Function_31_8EA8(): pass

    label("Function_31_8EA8")

    SetChrPos(0xFE, 3400, 2800, 5500, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFF254, 0x3E8, 0x0)
    OP_90(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_31_8EA8 end

    def Function_32_8EE7(): pass

    label("Function_32_8EE7")

    OP_44(0x8, 0x1)

    def lambda_8EF1():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8EF1)
    OP_8E(0xFE, 0xFFFFF9C0, 0x0, 0xD52, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_32_8EE7 end

    def Function_33_8F15(): pass

    label("Function_33_8F15")

    OP_8E(0xFE, 0xFFFFFDC6, 0x0, 0xD52, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_33_8F15 end

    def Function_34_8F31(): pass

    label("Function_34_8F31")

    OP_8E(0xFE, 0xFFFFF8EE, 0x0, 0x96A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_34_8F31 end

    def Function_35_8F4D(): pass

    label("Function_35_8F4D")

    OP_8E(0xFE, 0xFFFFFE70, 0x0, 0x96A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_35_8F4D end

    def Function_36_8F69(): pass

    label("Function_36_8F69")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-770, 0, 64560, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1430, 0, 64099, 0)
    SetChrPos(0x102, -550, 0, 64099, 0)
    SetChrPos(0xF8, -1450, 0, 63100, 0)
    SetChrPos(0xF9, -550, 0, 63100, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()

    ChrTalk(    #398
        0x8,
        "#100F嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #399
        0x101,
        (
            "#1011F嗯，有个东西\x01",
            "想要麻烦您调查一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x102,
        "#1040F其实，就是这个……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #401
        "\x1F\x18\x04\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x418, 1)

    ChrTalk(    #402
        0x8,
        (
            "#100F哦，这不是\x01",
            "数据水晶吗。\x02\x03",

            "嗯，似乎找不到\x01",
            "什么破损的迹象。\x02\x03",

            "#101F稍等一下。\x01",
            "我马上替你们分析。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(-5110, 0, 64310, 0)
    SetChrPos(0x101, -4820, 0, 63930, 0)
    SetChrPos(0x102, -5720, 0, 63930, 0)
    SetChrPos(0xF8, -4070, 0, 64340, 315)
    SetChrPos(0xF9, -6300, 0, 64440, 45)
    SetChrPos(0x8, -5200, 0, 65530, 0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_0D()
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #403
        0x8,
        (
            "#103F原来如此，\x01",
            "这个东西相当不简单呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x101,
        "#1004F里、里面是什么内容？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(    #405
        0x8,
        (
            "#100F似乎是关于\x01",
            "古代武器制造方法的记录。\x02\x03",

            "看来好像要使用一种名叫\x01",
            "塞姆里亚石的特殊金属……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x101,
        (
            "#1015F塞姆里亚石……\x01",
            "好像在哪里听过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x102,
        (
            "#1042F对了……\x02\x03",

            "#1040F那时候在王都的咖啡屋\x01",
            "老板给我们的金属\x01",
            "不就叫这个吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x101,
        (
            "#1004F啊，的确如此！\x02\x03",

            "#1001F……就是这种\x01",
            "奇怪的金属。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #409
        "\x1F\x17\x04\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x417, 1)

    ChrTalk(    #410
        0x8,
        (
            "#103F哦，这真是太好了。\x02\x03",

            "#101F有了这东西或许就好办多了。\x02\x03",

            "#100F也许用这边的设施\x01",
            "马上就能造出来呢。\x02\x03",

            "但是，在那之前必须\x01",
            "让你们做一个选择。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x101,
        "#1015F选择？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x8,
        (
            "#100F其实这里记录了两种武器\x01",
            "的制造方法……\x02\x03",

            "但是从金属的量来看，\x01",
            "只够做其中一种。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x101,
        (
            "#1004F是吗？\x02\x03",

            "#1007F唔，真难办呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x8,
        (
            "#100F要制作哪一种，\x01",
            "就交由你们来决定吧。\x02\x03",

            "#101F如何\x01",
            "想要制作哪一种呢？\x02",
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
            "【麒麟具】\x01",                # 0
            "【凤凰剑（凤·凰）】\x01",      # 1
            "【放弃】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Call(0, 37)
    OP_A2(0x22B1)
    Return()

    # Function_36_8F69 end

    def Function_37_94F2(): pass

    label("Function_37_94F2")

    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9510"),
        (1, "loc_9510"),
        (2, "loc_9759"),
        (SWITCH_DEFAULT, "loc_9821"),
    )


    label("loc_9510")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_954F")

    # ChrTalk(    #415
        # 0x101,
        # (
            # "#1001F嗯，那么……\x01",
            # "我就要这个『麒麟具』。\x02",
        # )
    # )

    # CloseMessageWindow()
    Jump("loc_9582")

    label("loc_954F")


    # ChrTalk(    #416
        # 0x102,
        # (
            # "#1040F嗯嗯。那么……\x01",
            # "请为我做这个『凤凰剑』。\x02",
        # )
    # )

    # CloseMessageWindow()

    label("loc_9582")


    ChrTalk(    #417
        0x8,
        (
            "#100F嗯，我明白了。\x01",
            "我马上着手制作。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xB7, 0x0, 0x64)
    Sleep(2000)
    OP_6D(-770, 0, 64560, 0)
    SetChrPos(0x101, -1430, 0, 64099, 0)
    SetChrPos(0x102, -550, 0, 64099, 0)
    SetChrPos(0xF8, -1450, 0, 63100, 0)
    SetChrPos(0xF9, -550, 0, 63100, 0)
    SetChrPos(0x8, -950, 0, 65390, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #418
        0x8,
        "#101F好了，完成了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96A0")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #419
        "\x07\x00得到了\x1F\x1B\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x1B, 1)
    Jump("loc_96E6")

    label("loc_96A0")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #420
        "\x07\x00得到了\x1F\x31\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x31, 1)

    label("loc_96E6")


    ChrTalk(    #421
        0x101,
        "#1001F多谢了，拉赛尔博士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x102,
        (
            "#1040F我们一定\x01",
            "会好好地使用它的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x8,
        (
            "#100F嗯，今后探索时\x01",
            "也要当心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_9821")

    label("loc_9759")


    ChrTalk(    #424
        0x101,
        (
            "#1016F嗯，真伤脑筋。\x01",
            "可以暂时保留一下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x8,
        (
            "#100F没问题。\x01",
            "考虑好之后再来就好了。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_6D(-2960, 0, 62700, 0)
    SetChrPos(0x8, -950, 0, 65390, 0)
    SetChrPos(0x101, -2960, 0, 62700, 0)
    SetChrPos(0x102, -2960, 0, 62700, 0)
    SetChrPos(0xF8, -2960, 0, 62700, 0)
    SetChrPos(0xF9, -2960, 0, 62700, 0)
    OP_0D()
    Jump("loc_9821")

    label("loc_9821")

    EventEnd(0x0)
    Return()

    # Function_37_94F2 end

    def Function_38_9824(): pass

    label("Function_38_9824")

    EventBegin(0x0)
    Fade(500)
    OP_6D(-770, 0, 64560, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1430, 0, 64099, 0)
    SetChrPos(0x102, -550, 0, 64099, 0)
    SetChrPos(0xF8, -1450, 0, 63100, 0)
    SetChrPos(0xF9, -550, 0, 63100, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()

    ChrTalk(    #426
        0x8,
        "#100F嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0x101,
        (
            "#1011F嗯，有个东西\x01",
            "想要麻烦您调查一下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x102,
        "#1040F其实，就是这个……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #429
        "\x1F\x18\x04\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x418, 1)

    ChrTalk(    #430
        0x8,
        (
            "#100F哦，这不是\x01",
            "数据水晶吗。\x02\x03",

            "嗯，似乎找不到\x01",
            "什么破损的迹象。\x02\x03",

            "#101F稍等一下。\x01",
            "我马上替你们分析。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(-5110, 0, 64310, 0)
    SetChrPos(0x101, -4820, 0, 63930, 0)
    SetChrPos(0x102, -5720, 0, 63930, 0)
    SetChrPos(0xF8, -4070, 0, 64340, 315)
    SetChrPos(0xF9, -6300, 0, 64440, 45)
    SetChrPos(0x8, -5200, 0, 65530, 0)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_0D()
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #431
        0x8,
        (
            "#103F原来如此，\x01",
            "这个东西相当不简单呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x101,
        "#1004F里、里面是什么内容？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(    #433
        0x8,
        (
            "#100F似乎是关于\x01",
            "古代武器制造方法的记录。\x02\x03",

            "看来好像要使用一种名叫\x01",
            "塞姆里亚石的特殊金属……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x101,
        (
            "#1015F塞姆里亚石……\x01",
            "记得我们应该有才对。\x02\x03",

            "#1001F……就是这个\x01",
            "有些奇怪的金属吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #435
        "\x1F\x17\x04\x07\x00交出了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x417, 2)

    ChrTalk(    #436
        0x8,
        (
            "#103F哦，这真是太好了。\x02\x03",

            "#101F有了这东西或许就好办多了。\x02\x03",

            "#100F也许用这边的设施\x01",
            "马上就能造出来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x101,
        (
            "#1001F真的吗？\x01",
            "那么就拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x8,
        "#100F嗯，我明白了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x22B1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xB7, 0x0, 0x64)
    Sleep(2000)
    OP_6D(-770, 0, 64560, 0)
    SetChrPos(0x101, -1430, 0, 64099, 0)
    SetChrPos(0x102, -550, 0, 64099, 0)
    SetChrPos(0xF8, -1450, 0, 63100, 0)
    SetChrPos(0xF9, -550, 0, 63100, 0)
    SetChrPos(0x8, -950, 0, 65390, 180)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #439
        0x8,
        "#101F好了，完成了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #440
        "\x07\x00得到了\x1F\x1B\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #441
        "\x07\x00得到了\x1F\x31\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x31, 1)
    OP_3E(0x1B, 1)

    ChrTalk(    #442
        0x101,
        "#1001F多谢了，拉赛尔博士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x102,
        (
            "#1040F我们一定\x01",
            "会好好地使用它的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0x8,
        (
            "#100F嗯，今后探索时\x01",
            "也要当心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    EventEnd(0x0)
    Return()

    # Function_38_9824 end

    def Function_39_9DA0(): pass

    label("Function_39_9DA0")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #445
        (
            "\x07\x05　　　机关室\x01",
            "※无关人员禁止入内\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_39_9DA0 end

    def Function_40_9DF2(): pass

    label("Function_40_9DF2")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9E7D")
    SoundLoad(13)
    OP_20(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_9E7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9E97")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_9E97")

    Return()

    # Function_40_9DF2 end

    def Function_41_9E99(): pass

    label("Function_41_9E99")

    Call(0, 18)
    Return()

    # Function_41_9E99 end

    def Function_42_9E9E(): pass

    label("Function_42_9E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EA7")
    Return()

    label("loc_9EA7")

    SetChrChipByIndex(0x12, 15)
    SetChrSubChip(0x12, 0)
    OP_4A(0x12, 0)
    Sleep(2000)
    SetChrChipByIndex(0x12, 9)
    SetChrSubChip(0x12, 0)
    OP_4B(0x12, 0)
    Return()

    # Function_42_9E9E end

    SaveToFile()

Try(main)
