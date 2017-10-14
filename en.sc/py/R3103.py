from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'R3103   ._SN',
        MapName             = 'Zeiss',
        Location            = 'R3103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60029",
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
        '',                                     # 9
        'CWO Pace',                             # 10
        'Measuring Device',                     # 11
        'Monster',                              # 12
        'Monster',                              # 13
        'Monster',                              # 14
        'Monster',                              # 15
        'Monster',                              # 16
        'Monster',                              # 17
        '',                                     # 18
        'Zeiss',                                # 19
        'Wolf Fort',                            # 20
        '',                                     # 21
        '',                                     # 22
        '',                                     # 23
        '',                                     # 24
        '',                                     # 25
        '',                                     # 26
        '',                                     # 27
        '',                                     # 28
        '',                                     # 29
        '',                                     # 30
        '',                                     # 31
        '',                                     # 32
        '',                                     # 33
        '',                                     # 34
        '',                                     # 35
        '',                                     # 36
        '',                                     # 37
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
        'ED6_DT09/CH10610 ._CH',             # 00
        'ED6_DT09/CH10611 ._CH',             # 01
        'ED6_DT09/CH10080 ._CH',             # 02
        'ED6_DT09/CH10081 ._CH',             # 03
        'ED6_DT09/CH10120 ._CH',             # 04
        'ED6_DT09/CH10121 ._CH',             # 05
        'ED6_DT09/CH10140 ._CH',             # 06
        'ED6_DT09/CH10141 ._CH',             # 07
        'ED6_DT09/CH10620 ._CH',             # 08
        'ED6_DT09/CH10621 ._CH',             # 09
        'ED6_DT09/CH10600 ._CH',             # 0A
        'ED6_DT09/CH10601 ._CH',             # 0B
        'ED6_DT09/CH10400 ._CH',             # 0C
        'ED6_DT09/CH10401 ._CH',             # 0D
        'ED6_DT09/CH11210 ._CH',             # 0E
        'ED6_DT09/CH11211 ._CH',             # 0F
        'ED6_DT09/CH11250 ._CH',             # 10
        'ED6_DT09/CH11251 ._CH',             # 11
        'ED6_DT07/CH01310 ._CH',             # 12
        'ED6_DT07/CH00065 ._CH',             # 13
        'ED6_DT07/CH00152 ._CH',             # 14
        'ED6_DT07/CH00122 ._CH',             # 15
        'ED6_DT27/CH04000 ._CH',             # 16
        'ED6_DT07/CH00130 ._CH',             # 17
        'ED6_DT07/CH00140 ._CH',             # 18
        'ED6_DT06/CH20020 ._CH',             # 19
        'ED6_DT29/CH13070 ._CH',             # 1A
        'ED6_DT29/CH13071 ._CH',             # 1B
        'ED6_DT07/CH00150 ._CH',             # 1C
        'ED6_DT07/CH00120 ._CH',             # 1D
        'ED6_DT29/CH13073 ._CH',             # 1E
        'ED6_DT07/CH00160 ._CH',             # 1F
        'ED6_DT29/CH12110 ._CH',             # 20
    )

    AddCharChipPat(
        'ED6_DT09/CH10610P._CP',             # 00
        'ED6_DT09/CH10611P._CP',             # 01
        'ED6_DT09/CH10080P._CP',             # 02
        'ED6_DT09/CH10081P._CP',             # 03
        'ED6_DT09/CH10120P._CP',             # 04
        'ED6_DT09/CH10121P._CP',             # 05
        'ED6_DT09/CH10140P._CP',             # 06
        'ED6_DT09/CH10141P._CP',             # 07
        'ED6_DT09/CH10620P._CP',             # 08
        'ED6_DT09/CH10621P._CP',             # 09
        'ED6_DT09/CH10600P._CP',             # 0A
        'ED6_DT09/CH10601P._CP',             # 0B
        'ED6_DT09/CH10400P._CP',             # 0C
        'ED6_DT09/CH10401P._CP',             # 0D
        'ED6_DT09/CH11210P._CP',             # 0E
        'ED6_DT09/CH11211P._CP',             # 0F
        'ED6_DT09/CH11250P._CP',             # 10
        'ED6_DT09/CH11251P._CP',             # 11
        'ED6_DT07/CH01310P._CP',             # 12
        'ED6_DT07/CH00065P._CP',             # 13
        'ED6_DT07/CH00152P._CP',             # 14
        'ED6_DT07/CH00122P._CP',             # 15
        'ED6_DT27/CH04000P._CP',             # 16
        'ED6_DT07/CH00130P._CP',             # 17
        'ED6_DT07/CH00140P._CP',             # 18
        'ED6_DT06/CH20020P._CP',             # 19
        'ED6_DT29/CH13070P._CP',             # 1A
        'ED6_DT29/CH13071P._CP',             # 1B
        'ED6_DT07/CH00150P._CP',             # 1C
        'ED6_DT07/CH00120P._CP',             # 1D
        'ED6_DT29/CH13073P._CP',             # 1E
        'ED6_DT07/CH00160P._CP',             # 1F
        'ED6_DT29/CH12110P._CP',             # 20
    )

    DeclNpc(
        X                   = -12550,
        Z                   = 1000,
        Y                   = 46450,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 7230,
        Z                   = -10,
        Y                   = -35710,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 32,
        ChipIndex           = 0x20,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -53110,
        Z                   = 0,
        Y                   = -14880,
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
        X                   = 22050,
        Z                   = -10,
        Y                   = 35970,
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


    DeclMonster(
        X                   = -30730,
        Z                   = -20,
        Y                   = 28880,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -27870,
        Z                   = 80,
        Y                   = 46700,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20F,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14660,
        Z                   = -80,
        Y                   = 32810,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24060,
        Z                   = 70,
        Y                   = -7910,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10150,
        Z                   = 10,
        Y                   = -20920,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 13270,
        Z                   = -30,
        Y                   = -23320,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15990,
        Z                   = -10,
        Y                   = 1090,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 31250,
        Z                   = 30,
        Y                   = -6140,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 39280,
        Z                   = 20,
        Y                   = -27110,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 23510,
        Z                   = 40,
        Y                   = -36040,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 10940,
        Z                   = 10,
        Y                   = -46410,
        Unknown_0C          = 180,
        Unknown_0E          = 16,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x211,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10090,
        Z                   = 10,
        Y                   = -39590,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -25680,
        Z                   = -40,
        Y                   = -25220,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -29830,
        Z                   = -90,
        Y                   = -39580,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -30430,
        Z                   = -80,
        Y                   = -45390,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -21410,
        Z                   = -50,
        Y                   = -50290,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -22480,
        Z                   = 30,
        Y                   = -37550,
        Unknown_0C          = 180,
        Unknown_0E          = 10,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x20E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 7230,
        Y                   = -500,
        Z                   = -35710,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = -12960,
        TriggerZ            = -20,
        TriggerY            = 45920,
        TriggerRange        = 1000,
        ActorX              = -12550,
        ActorZ              = -20,
        ActorY              = 46450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -24020,
        TriggerZ            = -10,
        TriggerY            = -43750,
        TriggerRange        = 1000,
        ActorX              = -24580,
        ActorZ              = -10,
        ActorY              = -43380,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17230,
        TriggerZ            = 10,
        TriggerY            = -7630,
        TriggerRange        = 1000,
        ActorX              = 17890,
        ActorZ              = 10,
        ActorY              = -7630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12880,
        TriggerZ            = -70,
        TriggerY            = 37960,
        TriggerRange        = 2000,
        ActorX              = -12880,
        ActorZ              = -70,
        ActorY              = 37960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_5BE",          # 00, 0
        "Function_1_5F7",          # 01, 1
        "Function_2_7E2",          # 02, 2
        "Function_3_7F8",          # 03, 3
        "Function_4_A25",          # 04, 4
        "Function_5_B52",          # 05, 5
        "Function_6_CDC",          # 06, 6
        "Function_7_EAB",          # 07, 7
        "Function_8_1390",         # 08, 8
        "Function_9_2126",         # 09, 9
        "Function_10_22F4",        # 0A, 10
        "Function_11_398E",        # 0B, 11
        "Function_12_3AD2",        # 0C, 12
        "Function_13_3BF8",        # 0D, 13
        "Function_14_3C4A",        # 0E, 14
        "Function_15_3C9C",        # 0F, 15
        "Function_16_3CEE",        # 10, 16
        "Function_17_3D40",        # 11, 17
        "Function_18_3D92",        # 12, 18
        "Function_19_3DBF",        # 13, 19
        "Function_20_3DEC",        # 14, 20
        "Function_21_3E19",        # 15, 21
        "Function_22_3E46",        # 16, 22
        "Function_23_3E73",        # 17, 23
        "Function_24_3F0B",        # 18, 24
    )


    def Function_0_5BE(): pass

    label("Function_0_5BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D1")
    Event(0, 7)
    Jump("loc_5F6")

    label("loc_5D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F6")
    Event(0, 8)

    label("loc_5F6")

    Return()

    # Function_0_5BE end

    def Function_1_5F7(): pass

    label("Function_1_5F7")

    OP_16(0x2, 0xFA0, 0xFFFE0048, 0xFFFE13D0, 0x230030)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_624")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)

    label("loc_624")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_636")
    OP_10(0x1, 0x0)
    OP_10(0x4, 0x1)

    label("loc_636")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E5")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x104, 0x1C), scpexpr(EXPR_PUSH_LONG, 0x5B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E5")
    OP_CE(0x0, (scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_694")
    OP_28(0x6E, 0x1, 0x40)
    Jump("loc_6E5")

    label("loc_694")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A9")
    OP_28(0x6E, 0x1, 0x20)
    Jump("loc_6E5")

    label("loc_6A9")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BE")
    OP_28(0x6E, 0x1, 0x10)
    Jump("loc_6E5")

    label("loc_6BE")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D3")
    OP_28(0x6E, 0x1, 0x8)
    Jump("loc_6E5")

    label("loc_6D3")

    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E5")
    OP_28(0x6E, 0x1, 0x4)

    label("loc_6E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F7")
    OP_6F(0x0, 0)
    Jump("loc_6FE")

    label("loc_6F7")

    OP_6F(0x0, 60)

    label("loc_6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_710")
    OP_6F(0x1, 0)
    Jump("loc_717")

    label("loc_710")

    OP_6F(0x1, 60)

    label("loc_717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_729")
    OP_6F(0x2, 0)
    Jump("loc_730")

    label("loc_729")

    OP_6F(0x2, 60)

    label("loc_730")

    OP_51(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_759")
    OP_65(0x3, 0x1)
    Jump("loc_75D")

    label("loc_759")

    OP_64(0x3, 0x1)

    label("loc_75D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_792")
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_792")
    OP_22(0x9E, 0x1, 0x55)

    label("loc_792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7AD")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    label("loc_7AD")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_7B9"),
        (SWITCH_DEFAULT, "loc_7C6"),
    )


    label("loc_7B9")

    ClearChrFlags(0x12, 0x1)
    ClearChrFlags(0x13, 0x1)
    Jump("loc_7C6")

    label("loc_7C6")

    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E1")
    ClearChrFlags(0x11, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_7E1")

    Return()

    # Function_1_5F7 end

    def Function_2_7E2(): pass

    label("Function_2_7E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7F7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_7E2")

    label("loc_7F7")

    Return()

    # Function_2_7E2 end

    def Function_3_7F8(): pass

    label("Function_3_7F8")

    OP_EA(0x2, 0xA, 0x2, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_993")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E2")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_84F():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_84F)

    def lambda_86A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_86A)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x214, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_8BD"),
        (2, "loc_8CF"),
        (1, "loc_8DF"),
        (SWITCH_DEFAULT, "loc_8E2"),
    )


    label("loc_8BD")

    OP_A2(0x1509)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_8E2")

    label("loc_8CF")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_8DF")

    OP_B4(0x0)
    Return()

    label("loc_8E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x12D, 1)"), scpexpr(EXPR_END)), "loc_92E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "Found \x1F\x2D\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1508)
    Jump("loc_990")

    label("loc_92E")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "Found \x1F\x2D\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x2D\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_990")

    Jump("loc_A17")

    label("loc_993")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        (
            "\x07\x05You try watering the chest to see if\x01",
            "something will sprout, but the only thing\x01",
            "that grows is the smell.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A17")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7F8 end

    def Function_4_A25(): pass

    label("Function_4_A25")

    OP_EA(0x2, 0xF0, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_A96")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "Found \x1F\x05\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x150A)
    Jump("loc_AFA")

    label("loc_A96")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "Found \x1F\x05\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x05\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_AFA")

    Jump("loc_B44")

    label("loc_AFD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05<YOU HAVE ACTIVATED THE STARING CONTEST>\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B44")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_A25 end

    def Function_5_B52(): pass

    label("Function_5_B52")

    OP_EA(0x2, 0xF1, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_BC3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "Found \x1F\xF9\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x150C)
    Jump("loc_C27")

    label("loc_BC3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "Found \x1F\xF9\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF9\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_C27")

    Jump("loc_CCE")

    label("loc_C2A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05You've already looted this chest. You might\x01",
            "have might have forgotten, but don't think you\x01",
            "can just come waltzing back and apologize.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CCE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_B52 end

    def Function_6_CDC(): pass

    label("Function_6_CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41F, 5)), scpexpr(EXPR_END)), "loc_CE4")
    Return()

    label("loc_CE4")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05A large monster is prowling around.\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Exterminate\x01",      # 0
            "Leave Alone\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_DD8"),
        (SWITCH_DEFAULT, "loc_DFB"),
    )


    label("loc_DD8")

    Fade(500)
    OP_89(0x0, 1900, 0, -31840, 132)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_DFB")

    Battle(0xEF4, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, 1900, 0, -31840, 132)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_E34"),
        (1, "loc_E37"),
        (SWITCH_DEFAULT, "loc_E3A"),
    )


    label("loc_E34")

    EventEnd(0x0)
    Return()

    label("loc_E37")

    OP_B4(0x0)
    Return()

    label("loc_E3A")

    EventBegin(0x1)
    SetChrFlags(0x11, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05Exterminated monster!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x20FD)
    OP_28(0xBC, 0x4, 0x10)
    OP_28(0xBC, 0x4, 0x2)
    OP_28(0xBC, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_6_CDC end

    def Function_7_EAB(): pass

    label("Function_7_EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EBC")
    Call(0, 23)

    label("loc_EBC")

    EventBegin(0x0)
    SetChrPos(0x101, 23150, -80, 21080, 180)
    SetChrPos(0xF7, 21650, -80, 21380, 180)
    SetChrPos(0x105, 23090, -90, 22650, 180)
    SetChrPos(0x104, 21790, -90, 22950, 180)
    OP_6D(21860, -140, 20000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)

    def lambda_F4E():
        OP_94(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F4E)
    Sleep(50)

    def lambda_F69():
        OP_94(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_F69)
    Sleep(50)

    def lambda_F84():
        OP_94(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F84)
    Sleep(50)

    def lambda_F9F():
        OP_94(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F9F)

    def lambda_FB5():
        OP_6D(21860, -140, 18000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_FB5)
    OP_0D()
    SetChrPos(0x9, 22030, -60, 30800, 180)
    Sleep(1000)

    ChrTalk(    #12
        0x9,
        "Hey, you lot!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xF7, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1044():
        OP_67(0, 7500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1044)

    def lambda_105C():
        OP_6D(21860, -140, 19500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_105C)
    ClearChrFlags(0x9, 0x80)

    def lambda_1079():
        OP_94(0x0, 0x9, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1079)

    def lambda_108F():
        OP_8C(0x105, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_108F)

    def lambda_109D():
        OP_8C(0x104, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_109D)
    Sleep(200)

    def lambda_10B0():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10B0)

    def lambda_10BE():
        OP_8C(0xF7, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_10BE)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #13
        0x9,
        "#6PGood, I made it in time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1004F#4PHuh? What do you mean, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        "#044F#4PHas something happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "#6PI contacted Leiston about what we\x01",
            "talked about previously and heard\x01",
            "something surprising.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        (
            "#6PI figured it was up to me\x01",
            "to let you all know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#1015F#4PSurprising what now...?\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_122F")

    ChrTalk(    #19
        0x106,
        "#057FWait, don't tell me...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1250")

    label("loc_122F")


    ChrTalk(    #20
        0x103,
        "#022FWait, don't tell me...\x02",
    )

    CloseMessageWindow()

    label("loc_1250")


    ChrTalk(    #21
        0x9,
        "#6PYeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "#6PThere was just an earthquake at\x01",
            "the Sanktheim Gate.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #23
        0x101,
        "#1005F#4P#3SWHAT?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05Hearing this, Estelle's group rushed to the Sanktheim Gate.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    NewScene("ED6_DT21/T3401   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_7_EAB end

    def Function_8_1390(): pass

    label("Function_8_1390")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A7")
    Call(0, 23)
    Call(0, 24)

    label("loc_13A7")

    OP_6D(-39970, -60, 33280, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -42890, -60, 32770, 90)
    SetChrPos(0x107, -43000, 80, 33740, 90)
    SetChrPos(0xF7, -44370, 130, 32299, 90)
    SetChrPos(0xF9, -44370, -80, 33600, 90)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x1418)

    ChrTalk(    #25
        0x101,
        "#1004F#5POh!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(1000)
    OP_6D(-17020, 10, 41980, 0)
    OP_67(0, 11580, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(17000, 0)
    OP_6E(541, 0)
    Sleep(1000)

    def lambda_1499():
        OP_6D(-17060, 30, 41950, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1499)

    def lambda_14B1():
        OP_67(0, 8000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_14B1)

    def lambda_14C9():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_14C9)

    def lambda_14D9():
        OP_6E(360, 6000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_14D9)
    Sleep(4500)
    SetChrPos(0x101, -31130, -30, 40660, 90)
    SetChrPos(0x107, -31130, -60, 41260, 90)
    SetChrPos(0xF7, -32130, -30, 40260, 90)
    SetChrPos(0xF9, -32130, -30, 41360, 90)

    def lambda_1532():
        OP_8E(0xFE, 0xFFFFA97A, 0xFFFFFFCE, 0x9D12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1532)
    Sleep(200)

    def lambda_1552():
        OP_8E(0xFE, 0xFFFFA5A6, 0xFFFFFFD8, 0xA12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1552)
    Sleep(100)

    def lambda_1572():
        OP_8E(0xFE, 0xFFFFA448, 0xFFFFFFCE, 0x988A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_1572)
    Sleep(200)

    def lambda_1592():
        OP_8E(0xFE, 0xFFFFA0C4, 0xFFFFFFCE, 0x9CA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1592)
    WaitChrThread(0xF7, 0x1)
    Fade(1000)
    OP_6D(-23130, -70, 40230, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E3")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as found the second book in the records room in the previous game\x01",             # 0
            "Set as did not find the second book in the records room in the previous game\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16D1"),
        (1, "loc_16DA"),
        (SWITCH_DEFAULT, "loc_16E3"),
    )


    label("loc_16D1")

    OP_28(0x2F, 0x1, 0x8)
    Jump("loc_16E3")

    label("loc_16DA")

    OP_28(0x2F, 0x2, 0x8)
    Jump("loc_16E3")

    label("loc_16E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_1779")

    ChrTalk(    #26
        0x101,
        (
            "#1006F#6PThat's right, this is where that book\x01",
            "from the records room was hidden.\x02\x03",

            "The Stone Circle is still spooky\x01",
            "as ever, I see.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1819")

    label("loc_1779")


    ChrTalk(    #27
        0x101,
        (
            "#1011F#6PI wondered what this place would\x01",
            "be like when I heard it was called\x01",
            "the Stone Circle...\x02\x03",

            "It feels like these pillars are\x01",
            "meant to mean something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1819")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1893")

    ChrTalk(    #28
        0x105,
        (
            "#040FI read about these pillars once.\x02\x03",

            "Apparently, they're believed to\x01",
            "predate even ancient Zemuria.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1944")

    label("loc_1893")


    ChrTalk(    #29
        0x104,
        (
            "#030FThey seem to have been erected\x01",
            "with purpose, but I believe they predate\x01",
            "even ancient Zemuria.\x02\x03",

            "They ARE quite simple... Someone\x01",
            "simply split stones and stood them up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1A79")

    ChrTalk(    #30
        0x106,
        (
            "#053F#6PZemurians... The ancient people who lived\x01",
            "on orbal energy and then vanished...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #31
        0x101,
        (
            "#1006F#4PThe Tetracyclic Towers and the Sealed\x01",
            "Area beneath Grancel Castle are both\x01",
            "Zemurian, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 0, 400)
    OP_8C(0x107, 180, 400)

    ChrTalk(    #32
        0x106,
        (
            "#051F#4PYeah, apparently.\x02\x03",

            "It's true this thing isn't remotely like those.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BCB")

    label("loc_1A79")


    ChrTalk(    #33
        0x103,
        (
            "#026F#6PThe Zemurians... The ancient culture that\x01",
            "prospered on orbal power and disappeared...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #34
        0x101,
        (
            "#1006F#4PThe Tetracyclic Towers and the Sealed\x01",
            "Area beneath Grancel Castle are both\x01",
            "Zemurian, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 0, 400)
    OP_8C(0x107, 180, 400)

    ChrTalk(    #35
        0x103,
        (
            "#027F#4PSo we believe, at least.\x02\x03",

            "This little circle certainly doesn't\x01",
            "seem similar to those grand places.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BCB")


    ChrTalk(    #36
        0x107,
        (
            "#560F#6PGrandpa told me once that there's\x01",
            "a really strong septium vein running\x01",
            "beneath this area.\x02\x03",

            "He thought this place might've been\x01",
            "important to a religion a really long\x01",
            "time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1015F#4PWhich means it's a good place for\x01",
            "examining the flow of a septium vein.\x01",
            "I get it.\x02\x03",

            "Where should we put the measuring\x01",
            "instrument, though?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 400)

    ChrTalk(    #38
        0x107,
        "#064F#6PHmmmmm, lesse...\x02",
    )

    CloseMessageWindow()

    def lambda_1D49():

        label("loc_1D49")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_1D49")

    QueueWorkItem2(0x101, 3, lambda_1D49)

    def lambda_1D5A():

        label("loc_1D5A")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_1D5A")

    QueueWorkItem2(0xF7, 3, lambda_1D5A)

    def lambda_1D6B():

        label("loc_1D6B")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_1D6B")

    QueueWorkItem2(0xF9, 3, lambda_1D6B)

    def lambda_1D7C():
        OP_6D(-17140, 30, 41840, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D7C)

    def lambda_1D94():
        OP_6E(326, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D94)
    OP_8E(0x107, 0xFFFFB1E0, 0xA, 0xA12C, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0x107, 0, 400)
    Sleep(500)
    OP_8C(0x107, 180, 400)
    Sleep(500)
    OP_8E(0x107, 0xFFFFC022, 0xFFFFFFE2, 0xBA18, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0x107, 90, 400)
    Sleep(500)
    OP_8C(0x107, 270, 400)
    Sleep(500)
    OP_8E(0x107, 0xFFFFD31E, 0xFFFFFFE2, 0xA7EE, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0x107, 0, 400)
    Sleep(500)
    OP_8C(0x107, 180, 400)
    Sleep(500)
    OP_8E(0x107, 0xFFFFC9A0, 0xFFFFFFB0, 0x9448, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0x107, 270, 400)
    Sleep(500)
    OP_8C(0x107, 90, 400)
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 19)
    OP_0D()
    OP_44(0x101, 0x3)
    OP_44(0xF7, 0x3)
    OP_44(0xF9, 0x3)

    ChrTalk(    #39
        0x107,
        (
            "#060F#5PThe ground here looks pretty solid,\x01",
            "and it's not in the ruins...\x02\x03",

            "Direction...is good!\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #40
        0x107,
        (
            "#061F#2PEstelle! It'll work great right here!\x02\x03",

            "Should we set it up?\x02",
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
            "Set Up Instrument\x01",      # 0
            "Not Yet\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FEA")

    ChrTalk(    #41
        0x107,
        (
            "#061F#2POkay, I'll start setting it up.\x02\x03",

            "Gimme juuuust a minute...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2116")

    label("loc_1FEA")


    ChrTalk(    #42
        0x107,
        (
            "#064F#2PUm, we're not gonna set it up yet?\x02\x03",

            "#060FWell, once you're ready,\x01",
            "just examine this area again.\x02\x03",

            "I'll set it up then!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-22150, -50, 40210, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -22150, -50, 40210, 90)
    SetChrPos(0x1, -22150, -50, 40210, 90)
    SetChrPos(0x2, -22150, -50, 40210, 90)
    SetChrPos(0x3, -22150, -50, 40210, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_65(0x3, 0x1)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    label("loc_2116")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 10)
    Return()

    # Function_8_1390 end

    def Function_9_2126(): pass

    label("Function_9_2126")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -13030, -30, 39230, 180)
    SetChrPos(0xF7, -13550, -60, 36810, 0)
    SetChrPos(0xF9, -15000, -20, 38280, 90)
    SetChrPos(0x107, -13800, -80, 38110, 90)
    OP_6D(-13490, -80, 38160, 0)
    OP_67(0, 8580, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Up Instrument\x01",      # 0
            "Not Yet\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2257")

    ChrTalk(    #43
        0x107,
        (
            "#061F#6POkay, I'll start setting it up.\x02\x03",

            "Gimme juuuust a minute...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E4")

    label("loc_2257")

    OP_8C(0x107, 45, 400)

    ChrTalk(    #44
        0x107,
        (
            "#064F#6PUm, we're not gonna set it up yet?\x02\x03",

            "#060FWell, once you're ready,\x01",
            "just examine this area again.\x02\x03",

            "I'll set it up then!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_22E4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 10)
    Return()

    # Function_9_2126 end

    def Function_10_22F4(): pass

    label("Function_10_22F4")

    FadeToDark(1000, 0, -1)
    SetChrPos(0x101, -13030, -30, 39230, 180)
    SetChrPos(0xF7, -13550, -60, 36810, 0)
    SetChrPos(0xF9, -15000, -20, 38280, 90)
    SetChrPos(0x107, -13800, -80, 38110, 90)
    OP_6D(-13490, -80, 38160, 0)
    OP_67(0, 8580, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #45
        0x107,
        "#061F#6PAll done!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F1")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Make This The First Instrument Set\x01",                          # 0
            "Make Kaldia Tunnel Instrument Already Set\x01",                   # 1
            "Make Leiston Fortress Instrument Already Set\x01",                # 2
            "Make Kaldia Tunnel and Leiston Instruments Already Set\x01",      # 3
            "No Change\x01",                                                   # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24C1"),
        (1, "loc_24CD"),
        (2, "loc_24D9"),
        (3, "loc_24E5"),
        (SWITCH_DEFAULT, "loc_24F1"),
    )


    label("loc_24C1")

    OP_A3(0x1419)
    OP_A3(0x141B)
    OP_A3(0x141F)
    Jump("loc_24F1")

    label("loc_24CD")

    OP_A3(0x1419)
    OP_A2(0x141B)
    OP_A3(0x141F)
    Jump("loc_24F1")

    label("loc_24D9")

    OP_A3(0x1419)
    OP_A3(0x141B)
    OP_A2(0x141F)
    Jump("loc_24F1")

    label("loc_24E5")

    OP_A3(0x1419)
    OP_A2(0x141B)
    OP_A2(0x141F)
    Jump("loc_24F1")

    label("loc_24F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B2F")

    ChrTalk(    #46
        0x101,
        (
            "#1004F#6PWhoa, so this is what it looks like\x01",
            "when it's all together? Wow!\x02\x03",

            "#1015FWhat's, um...this dish-like thing?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 45, 400)

    ChrTalk(    #47
        0x107,
        (
            "#060F#6POh, that's a kind of antenna for\x01",
            "broadcasting orbal-waves called\x01",
            "a parabolic antenna!\x02\x03",

            "It puts out really powerful orbal waves\x01",
            "that can cover really long distances...\x02\x03",

            "It can even broadcast from inside\x01",
            "a place like the Kaldia Tunnel!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2861")

    ChrTalk(    #48
        0x104,
        (
            "#033FHmmmm... A most impressive tool.\x02\x03",

            "#030FI don't recall seeing anything like\x01",
            "this at the corner tool shop...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x104, 400)

    ChrTalk(    #49
        0x107,
        (
            "#560F#4PUm, well, I don't think it's\x01",
            "for sale anywhere yet...\x02\x03",

            "It's one of Grandpa's inventions, though,\x01",
            "so I bet the central factory will start\x01",
            "selling them pretty soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x104,
        "#031FMmm. Lovely.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_285E")

    ChrTalk(    #51
        0x103,
        (
            "#027F#4POlivier, is that your...interest in\x01",
            "technology showing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x104,
        (
            "#035F#6PWhy, whatever do you mean, dear\x01",
            "Schera? I certainly don't know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_285E")

    Jump("loc_2A29")

    label("loc_2861")


    ChrTalk(    #53
        0x105,
        (
            "#044FUm, Tita?\x02\x03",

            "I'd heard that orbal waves weaken\x01",
            "as they pass through obstacles.\x02\x03",

            "Can this dish really transmit through\x01",
            "the Kaldia Tunnel?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x105, 400)

    ChrTalk(    #54
        0x107,
        (
            "#560F#4POh, um, according to Grandpa,\x01",
            "the antenna can direct orbal waves.\x02\x03",

            "So even if you're in a cave, you can\x01",
            "reflect it down the tunnel and bounce\x01",
            "it off the walls until it reaches the exit!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x105,
        (
            "#040FI see! My goodness...\x02\x03",

            "#041FProfessor Russell really is as much\x01",
            "of a genius as he's ever been.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A29")


    ChrTalk(    #56
        0x101,
        (
            "#1007F#6PI guess I'm too much of a country girl\x01",
            "to appreciate how incredible it is...\x02\x03",

            "#1006FThis thing'll transmit earthquake\x01",
            "info back to us, though, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 45, 400)

    ChrTalk(    #57
        0x107,
        (
            "#560F#6PUm, not yet.\x01",
            "I haven't started it up yet.\x02\x03",

            "Just need to flip the switch...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B84")

    label("loc_2B2F")


    ChrTalk(    #58
        0x101,
        (
            "#1006F#6PWell, flip that switch\x01",
            "as hard as you can!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x107,
        "#560F#6PFlipping...n--\x02",
    )

    CloseMessageWindow()

    label("loc_2B84")

    OP_8C(0x107, 90, 400)
    Sleep(300)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x7D0)

    def lambda_2BB7():
        OP_6D(-13490, -80, 37160, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2BB7)
    SetChrFlags(0xF7, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2C70")
    OP_43(0x106, 0x1, 0x0, 0xB)
    Sleep(800)

    ChrTalk(    #60 op#A
        0x106,
        "#054F#5P#3S#15ATch!\x02",
    )

    Sleep(500)
    OP_8C(0xF9, 180, 400)
    Sleep(50)
    OP_8C(0x107, 180, 400)
    CloseMessageWindow()
    WaitChrThread(0x106, 0x1)
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #61
        0x107,
        "#065F#6PWaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1020F#6PWhat th-!\x02",
    )

    CloseMessageWindow()
    OP_99(0x106, 0x7, 0x0, 0x5DC)
    SetChrChipByIndex(0x106, 20)
    SetChrSubChip(0x106, 0)
    Jump("loc_2CF5")

    label("loc_2C70")

    OP_43(0x103, 0x1, 0x0, 0xC)
    Sleep(800)

    ChrTalk(    #63 op#A
        0x103,
        "#024F#6P#3S#15AAgh!\x02",
    )

    Sleep(500)
    OP_8C(0xF9, 180, 400)
    Sleep(50)
    OP_8C(0x107, 180, 400)
    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)
    OP_62(0x107, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #64
        0x107,
        "#065F#6PWaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#1020F#6PWhat th-!\x02",
    )

    CloseMessageWindow()

    label("loc_2CF5")

    ClearChrFlags(0xF7, 0x800)
    OP_8C(0x101, 0, 500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 22)
    SetChrSubChip(0x101, 0)
    OP_0D()

    def lambda_2D1C():
        OP_6D(-13490, -80, 38160, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D1C)

    def lambda_2D34():
        OP_6B(3400, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2D34)
    OP_8C(0xF9, 270, 400)
    OP_1D(0x29)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_43(0xB, 0x0, 0x0, 0xD)
    OP_43(0xC, 0x0, 0x0, 0xE)
    OP_43(0xD, 0x0, 0x0, 0xF)
    OP_43(0xE, 0x0, 0x0, 0x10)
    OP_43(0xF, 0x0, 0x0, 0x11)
    WaitChrThread(0xB, 0x0)
    WaitChrThread(0xC, 0x0)
    WaitChrThread(0xD, 0x0)
    WaitChrThread(0xE, 0x0)
    WaitChrThread(0xF, 0x0)
    WaitChrThread(0x101, 0x3)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DF4")

    ChrTalk(    #66
        0x104,
        "#032F#6PHmph. Such a monstrous display.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x104, 23)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x107, 31)
    SetChrSubChip(0x107, 0)
    OP_0D()
    Jump("loc_2E35")

    label("loc_2DF4")


    ChrTalk(    #67
        0x105,
        "#042F#6PWe're surrounded...!\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x105, 24)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x107, 31)
    SetChrSubChip(0x107, 0)
    OP_0D()

    label("loc_2E35")

    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2EA7")

    ChrTalk(    #68
        0x106,
        (
            "#054F#5PSon of a... They're after the\x01",
            "quartz in the device!\x02\x03",

            "Only one thing to do!\x01",
            "SHRED 'EM!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F1C")

    label("loc_2EA7")


    ChrTalk(    #69
        0x103,
        (
            "#024F#6PThey must be attracted to the\x01",
            "inactive quartz in the device!\x02\x03",

            "We've no other choice.\x01",
            "Defend yourselves!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F1C")


    def lambda_2F22():
        OP_6B(2700, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2F22)
    OP_43(0xB, 0x0, 0x0, 0x12)
    OP_43(0xC, 0x0, 0x0, 0x13)
    OP_43(0xD, 0x0, 0x0, 0x14)
    OP_43(0xE, 0x0, 0x0, 0x15)
    OP_43(0xF, 0x0, 0x0, 0x16)
    Sleep(500)
    OP_44(0x101, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    Battle(0x21C, 0x0, 0x1, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0x107, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF7, 0)
    SetChrSubChip(0x107, 0)
    SetChrSubChip(0xF9, 0)
    OP_6D(-13490, -80, 38160, 0)
    OP_67(0, 8580, -10000, 0)
    OP_6B(3120, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    SetChrPos(0x101, -13030, -30, 39530, 0)
    SetChrPos(0xF7, -13550, -60, 36810, 180)
    SetChrPos(0xF9, -15000, -20, 38280, 270)
    SetChrPos(0x107, -13800, -80, 38110, 180)
    OP_1D(0x1D)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_305E():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_305E)
    Sleep(80)

    def lambda_3071():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3071)
    Sleep(120)

    def lambda_3084():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3084)
    WaitChrThread(0xF9, 0x1)
    Sleep(200)

    def lambda_309C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_309C)
    Sleep(80)

    def lambda_30AF():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_30AF)
    Sleep(120)

    def lambda_30C2():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_30C2)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)
    OP_8C(0x101, 225, 400)
    TurnDirection(0xF7, 0x107, 400)
    TurnDirection(0xF9, 0x107, 400)

    ChrTalk(    #70
        0x101,
        (
            "#1007F#6PHoo boy... I think we got them all...\x02\x03",

            "#1015FThose were definitely the nastiest Creepy\x01",
            "Sheep-like thingies I've EVER fought.\x01",
            "Those darn dirty, calculating...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_31DE")

    ChrTalk(    #71
        0x106,
        (
            "#552FProbably one of the new monsters\x01",
            "Elnan was on about.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3228")

    label("loc_31DE")


    ChrTalk(    #72
        0x103,
        (
            "#025FThose monsters must be one of\x01",
            "the new breeds Elnan mentioned...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3228")


    ChrTalk(    #73
        0x107,
        "#561F#6PThat was scary...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32CE")

    ChrTalk(    #74
        0x104,
        (
            "#033FTita, are you injured?\x02\x03",

            "#031FIf you get hurt, I'll be happy to treat you.\x01",
            "Just let big brother Olivier know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_333A")

    label("loc_32CE")


    ChrTalk(    #75
        0x105,
        (
            "#043FTita, did they hurt you?\x02\x03",

            "Just let me know if you get even\x01",
            "a scratch. I'll be happy to treat you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_333A")

    TurnDirection(0x107, 0xF9, 400)

    ChrTalk(    #76
        0x107,
        (
            "#067F#4PAhaha! I'm okay!\x01",
            "You all protected me!\x02\x03",

            "#560FMore importantly,\x01",
            "I need to flip the switch!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 400)
    OP_8C(0x101, 180, 400)
    Fade(500)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 19)
    OP_0D()
    Sleep(1000)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x5, 0x4)
    OP_72(0x6, 0x4)
    OP_22(0x9E, 0x1, 0x64)
    OP_24(0x9E, 0x55)
    Sleep(2000)
    Fade(500)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_354D")

    ChrTalk(    #77
        0x107,
        "#061F#6PYay! ♪ Now it works!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    ChrTalk(    #78
        0x101,
        (
            "#1006F#6PGood work, Tita!\x02\x03",

            "#1015FIsn't it just going to get attacked\x01",
            "by crazed sheep-things again\x01",
            "once we leave, though?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 45, 400)

    ChrTalk(    #79
        0x107,
        (
            "#560F#6POh, it'll be okay!\x02\x03",

            "Once it's on, it actually repels\x01",
            "monsters like the street lamps!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#1011F#6POh, okay. No worries, then!\x02",
    )

    CloseMessageWindow()
    Jump("loc_358F")

    label("loc_354D")


    ChrTalk(    #81
        0x107,
        "#061F#6PYay! ♪ Now it works!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#1011F#6PGood work, Tita!\x02",
    )

    CloseMessageWindow()

    label("loc_358F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3665")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_35E8")

    ChrTalk(    #83
        0x106,
        (
            "#051FAll right, let's get the rest\x01",
            "of them set up like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3631")

    label("loc_35E8")


    ChrTalk(    #84
        0x103,
        (
            "#027FNow then, we have two more\x01",
            "to set up, so let's get to it, hmm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3631")

    OP_8C(0x107, 180, 400)

    def lambda_363E():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_363E)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #85
        0x101,
        "#1006F#6PRight!\x02",
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_3665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3751")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_36C6")

    ChrTalk(    #86
        0x106,
        (
            "#051FAnyway, that's two devices down.\x02\x03",

            "Let's go set up the last one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_371E")

    label("loc_36C6")


    ChrTalk(    #87
        0x103,
        (
            "#526FThat's two instruments in place,\x01",
            "either way.\x02\x03",

            "Shall we go place the last one?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_371E")

    OP_8C(0x107, 180, 400)

    def lambda_372B():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_372B)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #88
        0x101,
        "#1006F#6POkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_38E4")

    label("loc_3751")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_37F7")

    ChrTalk(    #89
        0x106,
        (
            "#051FWe've got all the devices in\x01",
            "place now, too.\x02\x03",

            "Let's get back to Gramps in the\x01",
            "Operations room at the central factory.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)

    def lambda_37E5():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_37E5)
    OP_8C(0x101, 180, 400)
    Jump("loc_38AD")

    label("loc_37F7")


    ChrTalk(    #90
        0x103,
        (
            "#026FRight, then, that's the last\x01",
            "instrument in place.\x02\x03",

            "#020FLet's return to the Operations room in the\x01",
            "factory and check in with Professor Russell.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)

    def lambda_389E():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_389E)
    OP_8C(0x101, 180, 400)

    label("loc_38AD")


    ChrTalk(    #91
        0x101,
        "#1006F#6PRight. Fifth floor of the factory!\x02",
    )

    CloseMessageWindow()
    OP_28(0x87, 0x1, 0x200)

    label("loc_38E4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-14030, -80, 38070, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -14030, -80, 38070, 100)
    SetChrPos(0x1, -14030, -80, 38070, 100)
    SetChrPos(0x2, -14030, -80, 38070, 100)
    SetChrPos(0x3, -14030, -80, 38070, 100)
    OP_64(0x3, 0x1)
    OP_A2(0x1419)
    OP_28(0x87, 0x1, 0x10)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_22F4 end

    def Function_11_398E(): pass

    label("Function_11_398E")

    LoadEffect(0x1, "battle\\\\damage1.eff")
    SetChrPos(0xB, -15020, 500, 29210, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 27)

    def lambda_39C5():
        OP_8E(0xFE, 0xFFFFCACC, 0x1F4, 0x8A48, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_39C5)

    def lambda_39E0():

        label("loc_39E0")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_39E0")

    QueueWorkItem2(0xB, 3, lambda_39E0)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x106, 28)
    OP_0D()
    Sleep(130)
    OP_8C(0x106, -180, 600)
    SetChrChipByIndex(0x106, 20)
    SetChrSubChip(0x106, 0)
    OP_22(0x1F9, 0x0, 0x64)
    SetChrFlags(0x106, 0x1000)

    def lambda_3A23():
        OP_99(0x106, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_3A23)
    Sleep(80)
    OP_8F(0x106, 0xFFFFCA5E, 0xFFFFFFBA, 0x8CA0, 0x3A98, 0x0)
    Sleep(220)
    OP_44(0xB, 0x0)
    OP_44(0xB, 0x3)
    PlayEffect(0x1, 0xFF, 0xB, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 30)
    SetChrSubChip(0xB, 0)
    OP_8F(0xB, 0xFFFFC752, 0xFFFFFF92, 0x7C88, 0x4E20, 0x0)

    def lambda_3AB1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3AB1)
    WaitChrThread(0xB, 0x2)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0x106, 0x1000)
    Return()

    # Function_11_398E end

    def Function_12_3AD2(): pass

    label("Function_12_3AD2")

    LoadEffect(0x1, "battle\\\\damage1.eff")
    SetChrPos(0xB, -15020, 500, 29210, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 27)

    def lambda_3B09():

        label("loc_3B09")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_3B09")

    QueueWorkItem2(0xB, 3, lambda_3B09)

    def lambda_3B1C():
        OP_8E(0xFE, 0xFFFFCACC, 0x1F4, 0x8A48, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_3B1C)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 29)
    OP_0D()
    Sleep(200)
    OP_8C(0x103, -180, 600)
    SetChrChipByIndex(0x103, 21)
    SetChrSubChip(0x103, 0)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_3B62():
        OP_99(0x103, 0x0, 0x9, 0x9C4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_3B62)
    Sleep(150)
    OP_44(0xB, 0x0)
    OP_44(0xB, 0x3)
    PlayEffect(0x1, 0xFF, 0xB, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 30)
    SetChrSubChip(0xB, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_8F(0xB, 0xFFFFC752, 0x1F4, 0x7C88, 0x4E20, 0x0)

    def lambda_3BDC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3BDC)
    WaitChrThread(0xB, 0x2)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x20)
    Return()

    # Function_12_3AD2 end

    def Function_13_3BF8(): pass

    label("Function_13_3BF8")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -16470, 170, 27650, 315)
    SetChrChipByIndex(0xFE, 27)
    OP_8E(0xFE, 0xFFFFC306, 0x0, 0x7B2A, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)

    def lambda_3C3C():

        label("loc_3C3C")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3C3C")

    QueueWorkItem2(0xFE, 3, lambda_3C3C)
    Return()

    # Function_13_3BF8 end

    def Function_14_3C4A(): pass

    label("Function_14_3C4A")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -23080, -30, 31340, 23)
    SetChrChipByIndex(0xFE, 27)
    OP_8E(0xFE, 0xFFFFB8B6, 0x0, 0x89F8, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)

    def lambda_3C8E():

        label("loc_3C8E")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3C8E")

    QueueWorkItem2(0xFE, 3, lambda_3C8E)
    Return()

    # Function_14_3C4A end

    def Function_15_3C9C(): pass

    label("Function_15_3C9C")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -22800, -20, 42870, 122)
    SetChrChipByIndex(0xFE, 27)
    OP_8E(0xFE, 0xFFFFB956, 0x0, 0x9C40, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)

    def lambda_3CE0():

        label("loc_3CE0")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3CE0")

    QueueWorkItem2(0xFE, 3, lambda_3CE0)
    Return()

    # Function_15_3C9C end

    def Function_16_3CEE(): pass

    label("Function_16_3CEE")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -9450, -50, 48040, 199)
    SetChrChipByIndex(0xFE, 27)
    OP_8E(0xFE, 0xFFFFD0C6, 0x0, 0xA712, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)

    def lambda_3D32():

        label("loc_3D32")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3D32")

    QueueWorkItem2(0xFE, 3, lambda_3D32)
    Return()

    # Function_16_3CEE end

    def Function_17_3D40(): pass

    label("Function_17_3D40")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -250, -20, 34650, 281)
    SetChrChipByIndex(0xFE, 27)
    OP_8E(0xFE, 0xFFFFDB70, 0x0, 0x89BC, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)

    def lambda_3D84():

        label("loc_3D84")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3D84")

    QueueWorkItem2(0xFE, 3, lambda_3D84)
    Return()

    # Function_17_3D40 end

    def Function_18_3D92(): pass

    label("Function_18_3D92")

    SetChrChipByIndex(0xFE, 27)

    def lambda_3D9D():

        label("loc_3D9D")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_3D9D")

    QueueWorkItem2(0xFE, 3, lambda_3D9D)
    OP_8E(0xFE, 0xFFFFC8CE, 0xFFFFFFBA, 0x8A3E, 0x1388, 0x0)
    Return()

    # Function_18_3D92 end

    def Function_19_3DBF(): pass

    label("Function_19_3DBF")

    SetChrChipByIndex(0xFE, 27)

    def lambda_3DCA():

        label("loc_3DCA")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_3DCA")

    QueueWorkItem2(0xFE, 3, lambda_3DCA)
    OP_8E(0xFE, 0xFFFFBE1A, 0xFFFFFFBA, 0x8D0E, 0x1388, 0x0)
    Return()

    # Function_19_3DBF end

    def Function_20_3DEC(): pass

    label("Function_20_3DEC")

    SetChrChipByIndex(0xFE, 27)

    def lambda_3DF7():

        label("loc_3DF7")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_3DF7")

    QueueWorkItem2(0xFE, 3, lambda_3DF7)
    OP_8E(0xFE, 0xFFFFC1F8, 0x0, 0x9736, 0x1388, 0x0)
    Return()

    # Function_20_3DEC end

    def Function_21_3E19(): pass

    label("Function_21_3E19")

    SetChrChipByIndex(0xFE, 27)

    def lambda_3E24():

        label("loc_3E24")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_3E24")

    QueueWorkItem2(0xFE, 3, lambda_3E24)
    OP_8E(0xFE, 0xFFFFCE8C, 0x0, 0xA032, 0x1388, 0x0)
    Return()

    # Function_21_3E19 end

    def Function_22_3E46(): pass

    label("Function_22_3E46")

    SetChrChipByIndex(0xFE, 27)

    def lambda_3E51():

        label("loc_3E51")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_3E51")

    QueueWorkItem2(0xFE, 3, lambda_3E51)
    OP_8E(0xFE, 0xFFFFD04E, 0xFFFFFFCE, 0x8BF6, 0x1388, 0x0)
    Return()

    # Function_22_3E46 end

    def Function_23_3E73(): pass

    label("Function_23_3E73")

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
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3EEC"),
        (1, "loc_3EF2"),
        (SWITCH_DEFAULT, "loc_3EF8"),
    )


    label("loc_3EEC")

    OP_A2(0x1200)
    Jump("loc_3EF8")

    label("loc_3EF2")

    OP_A2(0x1201)
    Jump("loc_3EF8")

    label("loc_3EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3F06")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3F0A")

    label("loc_3F06")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3F0A")

    Return()

    # Function_23_3E73 end

    def Function_24_3F0B(): pass

    label("Function_24_3F0B")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3F45")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_3F5F")

    label("loc_3F45")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_3F5F")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_24_3F0B end

    SaveToFile()

Try(main)
