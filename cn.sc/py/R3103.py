from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '派斯队长',                             # 10
        '测量仪',                               # 11
        '魔兽',                                 # 12
        '魔兽',                                 # 13
        '魔兽',                                 # 14
        '魔兽',                                 # 15
        '魔兽',                                 # 16
        '魔兽',                                 # 17
        '',                                     # 18
        '蔡斯方向',                             # 19
        '沃尔费堡垒方向',                       # 20
        '',                                     # 21
        '',                                     # 22
        '',                                     # 23
        '',                                     # 24
        '',                                     # 25
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
        "Function_4_9C8",          # 04, 4
        "Function_5_ADF",          # 05, 5
        "Function_6_BF6",          # 06, 6
        "Function_7_DB1",          # 07, 7
        "Function_8_122A",         # 08, 8
        "Function_9_1D24",         # 09, 9
        "Function_10_1EBC",        # 0A, 10
        "Function_11_30EF",        # 0B, 11
        "Function_12_3233",        # 0C, 12
        "Function_13_3359",        # 0D, 13
        "Function_14_33AB",        # 0E, 14
        "Function_15_33FD",        # 0F, 15
        "Function_16_344F",        # 10, 16
        "Function_17_34A1",        # 11, 17
        "Function_18_34F3",        # 12, 18
        "Function_19_3520",        # 13, 19
        "Function_20_354D",        # 14, 20
        "Function_21_357A",        # 15, 21
        "Function_22_35A7",        # 16, 22
        "Function_23_35D4",        # 17, 23
        "Function_24_366D",        # 18, 24
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

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D7")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_84A():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_84A)

    def lambda_865():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_865)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x214, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_8B2"),
        (2, "loc_8C4"),
        (1, "loc_8D4"),
        (SWITCH_DEFAULT, "loc_8D7"),
    )


    label("loc_8B2")

    OP_A2(0x1509)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_8D7")

    label("loc_8C4")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_8D4")

    OP_B4(0x0)
    Return()

    label("loc_8D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x12D, 1)"), scpexpr(EXPR_END)), "loc_926")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\x2D\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1508)
    Jump("loc_988")

    label("loc_926")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "宝箱里装有\x1F\x2D\x01\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x2D\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_988")

    Jump("loc_9BA")

    label("loc_98B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9BA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7F8 end

    def Function_4_9C8(): pass

    label("Function_4_9C8")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x205, 1)"), scpexpr(EXPR_END)), "loc_A37")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\x05\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x150A)
    Jump("loc_A9D")

    label("loc_A37")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\x05\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x05\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_A9D")

    Jump("loc_AD1")

    label("loc_AA0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AD1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_9C8 end

    def Function_5_ADF(): pass

    label("Function_5_ADF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_B4E")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\xF9\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x150C)
    Jump("loc_BB4")

    label("loc_B4E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\xF9\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF9\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_BB4")

    Jump("loc_BE8")

    label("loc_BB7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BE8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_ADF end

    def Function_6_BF6(): pass

    label("Function_6_BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41F, 5)), scpexpr(EXPR_END)), "loc_BFE")
    Return()

    label("loc_BFE")

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
        "\x07\x05大型魔兽正在四处游荡中。\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "【消灭它】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_CE3"),
        (SWITCH_DEFAULT, "loc_D06"),
    )


    label("loc_CE3")

    Fade(500)
    OP_89(0x0, 1900, 0, -31840, 132)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_D06")

    Battle(0xEF4, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, 1900, 0, -31840, 132)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_D3F"),
        (1, "loc_D42"),
        (SWITCH_DEFAULT, "loc_D45"),
    )


    label("loc_D3F")

    EventEnd(0x0)
    Return()

    label("loc_D42")

    OP_B4(0x0)
    Return()

    label("loc_D45")

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
        "\x07\x05消灭了通缉魔兽！\x02",
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

    # Function_6_BF6 end

    def Function_7_DB1(): pass

    label("Function_7_DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC2")
    Call(0, 23)

    label("loc_DC2")

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

    def lambda_E54():
        OP_94(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E54)
    Sleep(50)

    def lambda_E6F():
        OP_94(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_E6F)
    Sleep(50)

    def lambda_E8A():
        OP_94(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_E8A)
    Sleep(50)

    def lambda_EA5():
        OP_94(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EA5)

    def lambda_EBB():
        OP_6D(21860, -140, 18000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_EBB)
    OP_0D()
    SetChrPos(0x9, 22030, -60, 30800, 180)
    Sleep(1000)

    ChrTalk(    #12
        0x9,
        "喂，你们几个！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xF7, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_F4B():
        OP_67(0, 7500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F4B)

    def lambda_F63():
        OP_6D(21860, -140, 19500, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_F63)
    ClearChrFlags(0x9, 0x80)

    def lambda_F80():
        OP_94(0x0, 0x9, 0x0, 0x2328, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F80)

    def lambda_F96():
        OP_8C(0x105, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F96)

    def lambda_FA4():
        OP_8C(0x104, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FA4)
    Sleep(200)

    def lambda_FB7():
        OP_8C(0x101, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FB7)

    def lambda_FC5():
        OP_8C(0xF7, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_FC5)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #13
        0x9,
        "#5P太好了，赶上了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1004F#2P咦，是队长先生？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        "#044F#2P怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        (
            "#5P我把刚才谈的事\x01",
            "通知了雷斯顿要塞，\x01",
            "却听到了意外的信息。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        "#5P我认为必须要告知你们才行。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#1015F#2P意外的信息……？\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_10D5")

    ChrTalk(    #19
        0x106,
        (
            "#057F要告知我们？\x01",
            "难道说…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F5")

    label("loc_10D5")


    ChrTalk(    #20
        0x103,
        (
            "#022F要告知我们？\x01",
            "难道说…\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10F5")


    ChrTalk(    #21
        0x9,
        "#5P嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x9,
        (
            "#5P就在刚才，圣海姆门\x01",
            "似乎发生了局部性的地震。\x02",
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
        "#1005F#2P#3S你、你说什么～！？\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        (
            "\x07\x05听到通知的艾丝蒂尔她们\x01",
            "火速赶到了圣海姆门。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    NewScene("ED6_DT21/T3401   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_7_DB1 end

    def Function_8_122A(): pass

    label("Function_8_122A")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1241")
    Call(0, 23)
    Call(0, 24)

    label("loc_1241")

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
        "#1004F#5P啊……\x02",
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

    def lambda_1336():
        OP_6D(-17060, 30, 41950, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1336)

    def lambda_134E():
        OP_67(0, 8000, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_134E)

    def lambda_1366():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_1366)

    def lambda_1376():
        OP_6E(360, 6000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_1376)
    Sleep(4500)
    SetChrPos(0x101, -31130, -30, 40660, 90)
    SetChrPos(0x107, -31130, -60, 41260, 90)
    SetChrPos(0xF7, -32130, -30, 40260, 90)
    SetChrPos(0xF9, -32130, -30, 41360, 90)

    def lambda_13CF():
        OP_8E(0xFE, 0xFFFFA97A, 0xFFFFFFCE, 0x9D12, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13CF)
    Sleep(200)

    def lambda_13EF():
        OP_8E(0xFE, 0xFFFFA5A6, 0xFFFFFFD8, 0xA12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_13EF)
    Sleep(100)

    def lambda_140F():
        OP_8E(0xFE, 0xFFFFA448, 0xFFFFFFCE, 0x988A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_140F)
    Sleep(200)

    def lambda_142F():
        OP_8E(0xFE, 0xFFFFA0C4, 0xFFFFFFCE, 0x9CA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_142F)
    WaitChrThread(0xF7, 0x1)
    Fade(1000)
    OP_6D(-23130, -70, 40230, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1545")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在第一部中找到过资料室的书（第二本）】\x01",        # 0
            "【◇在第一部中没找到过资料室的书（第二本）】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1533"),
        (1, "loc_153C"),
        (SWITCH_DEFAULT, "loc_1545"),
    )


    label("loc_1533")

    OP_28(0x2F, 0x1, 0x8)
    Jump("loc_1545")

    label("loc_153C")

    OP_28(0x2F, 0x2, 0x8)
    Jump("loc_1545")

    label("loc_1545")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2F, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_15BC")

    ChrTalk(    #26
        0x101,
        (
            "#1006F#5P对了，这里以前\x01",
            "藏着资料室的书呢……\x02\x03",

            "是『巨石阵』啊。\x01",
            "唔～和过去一样，还是那么神秘的石柱。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_160C")

    label("loc_15BC")


    ChrTalk(    #27
        0x101,
        (
            "#1011F#5P听到『巨石阵』\x01",
            "我还以为是什么呢……\x02\x03",

            "唔～真是根颇有来历的石柱啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_160C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1673")

    ChrTalk(    #28
        0x105,
        (
            "#040F我在书里读到过\x01",
            "关于这根石柱的事。\x02\x03",

            "好像它还是在塞姆里亚文明\x01",
            "出现前建造的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16D4")

    label("loc_1673")


    ChrTalk(    #29
        0x104,
        (
            "#030F嗯，我想大概是比\x01",
            "塞姆里亚文明更早的遗迹吧。\x02\x03",

            "好像只是单纯地将岩石\x01",
            "切割并且竖起来而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_17BC")

    ChrTalk(    #30
        0x106,
        (
            "#053F#6P塞姆里亚文明……\x01",
            "那个繁荣的古代导力技术文明？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #31
        0x101,
        (
            "#1006F#2P『四轮之塔』和\x01",
            "王城地下的『封印区域』\x01",
            "都是塞姆里亚文明的产物吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 0, 400)
    OP_8C(0x107, 180, 400)

    ChrTalk(    #32
        0x106,
        (
            "#051F#4P嗯，好像是的。\x02\x03",

            "这确实是和那些\x01",
            "完全无关的东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189A")

    label("loc_17BC")


    ChrTalk(    #33
        0x103,
        (
            "#026F#6P塞姆里亚文明……\x01",
            "那个繁荣的古代导力技术文明是吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #34
        0x101,
        (
            "#1006F#2P『四轮之塔』和\x01",
            "王城地下的『封印区域』\x01",
            "都是塞姆里亚文明的产物吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 0, 400)
    OP_8C(0x107, 180, 400)

    ChrTalk(    #35
        0x103,
        (
            "#027F#4P嗯，没错。\x02\x03",

            "这确实是和那些\x01",
            "完全无关的东西呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189A")


    ChrTalk(    #36
        0x107,
        (
            "#560F#5P爷爷说\x01",
            "这个地方可以清晰地\x01",
            "检测到七耀脉的流动。\x02\x03",

            "他还说这石柱也可能\x01",
            "是带着某种宗教\x01",
            "意义被建造的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1015F#2P原来如此，也就是说\x01",
            "很适合用来调查七耀脉的流动啰。\x02\x03",

            "不过，测量仪应该\x01",
            "设置在什么地方呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 90, 400)

    ChrTalk(    #38
        0x107,
        "#064F#5P嗯，这个嘛……\x02",
    )

    CloseMessageWindow()

    def lambda_1996():

        label("loc_1996")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_1996")

    QueueWorkItem2(0x101, 3, lambda_1996)

    def lambda_19A7():

        label("loc_19A7")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_19A7")

    QueueWorkItem2(0xF7, 3, lambda_19A7)

    def lambda_19B8():

        label("loc_19B8")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_19B8")

    QueueWorkItem2(0xF9, 3, lambda_19B8)

    def lambda_19C9():
        OP_6D(-17140, 30, 41840, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19C9)

    def lambda_19E1():
        OP_6E(326, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19E1)
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
            "#060F#5P地面也很结实，\x01",
            "也不像是遗迹的地基……\x02\x03",

            "方位的确认……也没问题了。\x02",
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
            "#061F#5P姐姐。\x01",
            "我想这里应该可以哦。\x02\x03",

            "现在就开始设置测量仪吗？\x02",
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
            "【设置测量仪】\x01",      # 0
            "【先不设置】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C09")

    ChrTalk(    #41
        0x107,
        (
            "#061F#5P那么\x01",
            "进行设置工作了哦。\x02\x03",

            "请稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D14")

    label("loc_1C09")


    ChrTalk(    #42
        0x107,
        (
            "#064F#5P哎……先不设置吗？\x02\x03",

            "#060F那就等准备好以后\x01",
            "再来这个地方调查吧。\x02\x03",

            "到时再进行设置工作。\x02",
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

    label("loc_1D14")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 10)
    Return()

    # Function_8_122A end

    def Function_9_1D24(): pass

    label("Function_9_1D24")

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
            "【设置测量仪】\x01",      # 0
            "【先不设置】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E42")

    ChrTalk(    #43
        0x107,
        (
            "#061F#6P那么\x01",
            "进行设置工作了哦。\x02\x03",

            "请稍等一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EAC")

    label("loc_1E42")

    OP_8C(0x107, 45, 400)

    ChrTalk(    #44
        0x107,
        (
            "#064F#6P咦……不设置吗？\x02\x03",

            "#060F那就等准备好以后\x01",
            "再来这个地方调查吧。\x02\x03",

            "到时再进行设置工作。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_1EAC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 10)
    Return()

    # Function_9_1D24 end

    def Function_10_1EBC(): pass

    label("Function_10_1EBC")

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
        "#061F#6P嗯，这样就好了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_209A")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇第一次设置测量仪】\x01",                            # 0
            "【◇已经在卡鲁迪亚隧道设置了测量仪】\x01",              # 1
            "【◇设置了雷斯顿要塞的测量仪】\x01",                    # 2
            "【◇卡鲁迪亚隧道和雷斯顿要塞已设置了测量仪】\x01",      # 3
            "【◇不变更】\x01",                                      # 4
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_206A"),
        (1, "loc_2076"),
        (2, "loc_2082"),
        (3, "loc_208E"),
        (SWITCH_DEFAULT, "loc_209A"),
    )


    label("loc_206A")

    OP_A3(0x1419)
    OP_A3(0x141B)
    OP_A3(0x141F)
    Jump("loc_209A")

    label("loc_2076")

    OP_A3(0x1419)
    OP_A2(0x141B)
    OP_A3(0x141F)
    Jump("loc_209A")

    label("loc_2082")

    OP_A3(0x1419)
    OP_A3(0x141B)
    OP_A2(0x141F)
    Jump("loc_209A")

    label("loc_208E")

    OP_A3(0x1419)
    OP_A2(0x141B)
    OP_A2(0x141F)
    Jump("loc_209A")

    label("loc_209A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24E2")

    ChrTalk(    #46
        0x101,
        (
            "#1004F#5P哟，组合起来的话\x01",
            "原来是这样的啊。\x02\x03",

            "#1015F不过……\x01",
            "这个像盘子一样的东西是什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 45, 400)

    ChrTalk(    #47
        0x107,
        (
            "#060F#6P它叫抛物面天线，\x01",
            "是个可以集中导力波的天线。\x02\x03",

            "通过它可以把强力的导力波\x01",
            "传送到很远的地方……\x02\x03",

            "即使在卡鲁迪亚隧道这种地方\x01",
            "也都一样可以传送到呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22D9")

    ChrTalk(    #48
        0x104,
        (
            "#033F哦……\x01",
            "那可是很厉害的东西啊。\x02\x03",

            "#030F那么…\x01",
            "在市场中也能买到这东西吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x104, 400)

    ChrTalk(    #49
        0x107,
        (
            "#560F#2P啊，我也不是\x01",
            "很清楚呢，\x02\x03",

            "不过爷爷的发明一般在问世\x01",
            "半年后就会在市面贩卖了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x104,
        "#031F呼，这真令人期待。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_22D6")

    ChrTalk(    #51
        0x103,
        "#027F#2P哎呀……和你的『本职』有关吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x104,
        "#035F#5P我听不懂你在说什么呢。\x02",
    )

    CloseMessageWindow()

    label("loc_22D6")

    Jump("loc_242A")

    label("loc_22D9")


    ChrTalk(    #53
        0x105,
        (
            "#044F那个，提妲。\x02\x03",

            "我以前听说过，导力波遇到障碍物\x01",
            "就会减弱，不过……\x02\x03",

            "这个装置为什么在洞窟这样的地方\x01",
            "也可以使用呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x105, 400)

    ChrTalk(    #54
        0x107,
        (
            "#560F#2P那个，这天线\x01",
            "会赋予导力波指向性，\x01",
            "所以可以顺利进行传送。\x02\x03",

            "即使是像洞窟那种地方，\x01",
            "导力波似乎也能藉由墙壁反射\x01",
            "一路传送到出口。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x105,
        (
            "#040F原来如此……\x02\x03",

            "#041F不愧是拉赛尔博士啊，\x01",
            "天才的称号名不虚传。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_242A")


    ChrTalk(    #56
        0x101,
        (
            "#1007F#5P唔，到现在还感觉不到\x01",
            "这东西到底有多厉害……\x02\x03",

            "#1006F不过这样一来就可以\x01",
            "把地震情报传送出去了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 45, 400)

    ChrTalk(    #57
        0x107,
        (
            "#560F#6P啊，不。\x01",
            "现在还没有启动，\x02\x03",

            "那我现在就按下开关了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252A")

    label("loc_24E2")


    ChrTalk(    #58
        0x101,
        (
            "#1006F#5P那么只剩下\x01",
            "打开开关了对吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x107,
        "#560F#6P嗯，请等一下……\x02",
    )

    CloseMessageWindow()

    label("loc_252A")

    OP_8C(0x107, 90, 400)
    Sleep(300)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x7D0)

    def lambda_255D():
        OP_6D(-13490, -80, 37160, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_255D)
    SetChrFlags(0xF7, 0x800)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2615")
    OP_43(0x106, 0x1, 0x0, 0xB)
    Sleep(800)

    ChrTalk(    #60 op#A
        0x106,
        "#054F#5P#3S#10A呀！\x02",
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
        "#065F#5P啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1020F#5P什么！？\x02",
    )

    CloseMessageWindow()
    OP_99(0x106, 0x7, 0x0, 0x5DC)
    SetChrChipByIndex(0x106, 20)
    SetChrSubChip(0x106, 0)
    Jump("loc_2699")

    label("loc_2615")

    OP_43(0x103, 0x1, 0x0, 0xC)
    Sleep(800)

    ChrTalk(    #63 op#A
        0x103,
        "#024F#5P#3S#10A嘿！\x02",
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
        "#065F#5P啊！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#1020F#5P什么！？\x02",
    )

    CloseMessageWindow()

    label("loc_2699")

    ClearChrFlags(0xF7, 0x800)
    OP_8C(0x101, 0, 500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 22)
    SetChrSubChip(0x101, 0)
    OP_0D()

    def lambda_26C0():
        OP_6D(-13490, -80, 38160, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_26C0)

    def lambda_26D8():
        OP_6B(3400, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_26D8)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2794")

    ChrTalk(    #66
        0x104,
        (
            "#032F#6P哟……\x01",
            "这是从哪儿冒出来的。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x104, 23)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x107, 31)
    SetChrSubChip(0x107, 0)
    OP_0D()
    Jump("loc_27D3")

    label("loc_2794")


    ChrTalk(    #67
        0x105,
        "#042F#6P我们被包围了呢……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x105, 24)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x107, 31)
    SetChrSubChip(0x107, 0)
    OP_0D()

    label("loc_27D3")

    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2821")

    ChrTalk(    #68
        0x106,
        (
            "#054F#5P看来它们的目标\x01",
            "是装置中的结晶回路。\x02\x03",

            "击溃它们吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2860")

    label("loc_2821")


    ChrTalk(    #69
        0x103,
        (
            "#024F#5P看来它们的目标\x01",
            "是装置中的结晶回路。\x02\x03",

            "击退它们吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2860")


    def lambda_2866():
        OP_6B(2700, 500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2866)
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

    def lambda_29A2():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29A2)
    Sleep(80)

    def lambda_29B5():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_29B5)
    Sleep(120)

    def lambda_29C8():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_29C8)
    WaitChrThread(0xF9, 0x1)
    Sleep(200)

    def lambda_29E0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29E0)
    Sleep(80)

    def lambda_29F3():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_29F3)
    Sleep(120)

    def lambda_2A06():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2A06)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)
    OP_8C(0x101, 225, 400)
    TurnDirection(0xF7, 0x107, 400)
    TurnDirection(0xF9, 0x107, 400)

    ChrTalk(    #70
        0x101,
        (
            "#1007F#5P唉……\x01",
            "总算轰走了。\x02\x03",

            "#1015F唔，第一次见到\x01",
            "这样的猿羊……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2AB0")

    ChrTalk(    #71
        0x106,
        (
            "#552F大概就是艾南先生所说的\x01",
            "新品种的魔兽吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AE2")

    label("loc_2AB0")


    ChrTalk(    #72
        0x103,
        (
            "#025F大概就是艾南先生\x01",
            "所说的新种类的魔兽吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AE2")


    ChrTalk(    #73
        0x107,
        "#561F#5P真、真吓人……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B67")

    ChrTalk(    #74
        0x104,
        (
            "#033F提妲，你没事吧？\x02\x03",

            "#031F受伤的话我来帮你包扎，\x01",
            "不用客气，只管跟大哥哥说就是了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BB3")

    label("loc_2B67")


    ChrTalk(    #75
        0x105,
        (
            "#043F提妲你没受伤吧？\x02\x03",

            "如果有擦伤什么的我帮你包扎，\x01",
            "不用客气尽管说哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BB3")

    TurnDirection(0x107, 0xF9, 400)

    ChrTalk(    #76
        0x107,
        (
            "#067F#2P嘿嘿，我没事的～\x01",
            "因为大家都在保护我。\x02\x03",

            "#560F比起这个……\x01",
            "还是得赶紧打开开关才行。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D63")

    ChrTalk(    #77
        0x107,
        "#061F#6P呼，启动完成。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    ChrTalk(    #78
        0x101,
        (
            "#1006F#5P辛苦了，提妲。\x02\x03",

            "#1015F不过要是刚才的魔兽\x01",
            "来袭击装置怎么办？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 45, 400)

    ChrTalk(    #79
        0x107,
        (
            "#560F#6P啊，那个不用担心。\x02\x03",

            "因为装置具备了\x01",
            "类似路灯的驱赶魔兽功能。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#1011F#5P是吗，那我就放心了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D9C")

    label("loc_2D63")


    ChrTalk(    #81
        0x107,
        "#061F#6P呼，启动完成。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        "#1011F#5P辛苦了，提妲。\x02",
    )

    CloseMessageWindow()

    label("loc_2D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2DE3")

    ChrTalk(    #83
        0x106,
        (
            "#051F好，就这样\x01",
            "把剩下的测量仪也设置好吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E11")

    label("loc_2DE3")


    ChrTalk(    #84
        0x103,
        (
            "#027F好，就这样\x01",
            "继续设置剩余的测量仪吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E11")

    OP_8C(0x107, 180, 400)

    def lambda_2E1E():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2E1E)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #85
        0x101,
        "#1006F#5P明白！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3045")

    label("loc_2E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x283, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2EFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2E93")

    ChrTalk(    #86
        0x106,
        (
            "#051F好，这是第二个了吧。\x02\x03",

            "去把最后一个也搞定吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC8")

    label("loc_2E93")


    ChrTalk(    #87
        0x103,
        (
            "#526F那这是第二个了吧。\x02\x03",

            "马上去设置最后一个吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC8")

    OP_8C(0x107, 180, 400)

    def lambda_2ED5():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2ED5)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #88
        0x101,
        "#1006F#5PＯＫ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3045")

    label("loc_2EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2F85")

    ChrTalk(    #89
        0x106,
        (
            "#051F好，这样一来所有的\x01",
            "测量仪都设置完毕了。\x02\x03",

            "老爷子还在等着我们，\x01",
            "赶快去中央工房的演算室吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)

    def lambda_2F73():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2F73)
    OP_8C(0x101, 180, 400)
    Jump("loc_3013")

    label("loc_2F85")


    ChrTalk(    #90
        0x103,
        (
            "#026F那么，这样一来所有的\x01",
            "测量仪都设置完毕了呢。\x02\x03",

            "#020F拉赛尔博士还在等着我们，\x01",
            "现在就回中央工房的演算室吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x107, 180, 400)

    def lambda_3004():
        OP_8C(0xF9, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_3004)
    OP_8C(0x101, 180, 400)

    label("loc_3013")


    ChrTalk(    #91
        0x101,
        (
            "#1006F#5PＯＫ！\x01",
            "就在中央工房的５楼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x87, 0x1, 0x200)

    label("loc_3045")

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

    # Function_10_1EBC end

    def Function_11_30EF(): pass

    label("Function_11_30EF")

    LoadEffect(0x1, "battle\\\\damage1.eff")
    SetChrPos(0xB, -15020, 500, 29210, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 27)

    def lambda_3126():
        OP_8E(0xFE, 0xFFFFCACC, 0x1F4, 0x8A48, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_3126)

    def lambda_3141():

        label("loc_3141")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_3141")

    QueueWorkItem2(0xB, 3, lambda_3141)
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

    def lambda_3184():
        OP_99(0x106, 0x0, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x106, 3, lambda_3184)
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

    def lambda_3212():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3212)
    WaitChrThread(0xB, 0x2)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0x106, 0x1000)
    Return()

    # Function_11_30EF end

    def Function_12_3233(): pass

    label("Function_12_3233")

    LoadEffect(0x1, "battle\\\\damage1.eff")
    SetChrPos(0xB, -15020, 500, 29210, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 27)

    def lambda_326A():

        label("loc_326A")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_326A")

    QueueWorkItem2(0xB, 3, lambda_326A)

    def lambda_327D():
        OP_8E(0xFE, 0xFFFFCACC, 0x1F4, 0x8A48, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_327D)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x103, 29)
    OP_0D()
    Sleep(200)
    OP_8C(0x103, -180, 600)
    SetChrChipByIndex(0x103, 21)
    SetChrSubChip(0x103, 0)
    OP_22(0x1F6, 0x0, 0x64)

    def lambda_32C3():
        OP_99(0x103, 0x0, 0x9, 0x9C4)
        ExitThread()

    QueueWorkItem(0x103, 3, lambda_32C3)
    Sleep(150)
    OP_44(0xB, 0x0)
    OP_44(0xB, 0x3)
    PlayEffect(0x1, 0xFF, 0xB, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xB, 30)
    SetChrSubChip(0xB, 0)
    OP_22(0x209, 0x0, 0x64)
    OP_8F(0xB, 0xFFFFC752, 0x1F4, 0x7C88, 0x4E20, 0x0)

    def lambda_333D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_333D)
    WaitChrThread(0xB, 0x2)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x20)
    Return()

    # Function_12_3233 end

    def Function_13_3359(): pass

    label("Function_13_3359")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -16470, 170, 27650, 315)
    SetChrChipByIndex(0xFE, 27)
    OP_8E(0xFE, 0xFFFFC306, 0x0, 0x7B2A, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)

    def lambda_339D():

        label("loc_339D")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_339D")

    QueueWorkItem2(0xFE, 3, lambda_339D)
    Return()

    # Function_13_3359 end

    def Function_14_33AB(): pass

    label("Function_14_33AB")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -23080, -30, 31340, 23)
    SetChrChipByIndex(0xFE, 27)
    OP_8E(0xFE, 0xFFFFB8B6, 0x0, 0x89F8, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)

    def lambda_33EF():

        label("loc_33EF")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_33EF")

    QueueWorkItem2(0xFE, 3, lambda_33EF)
    Return()

    # Function_14_33AB end

    def Function_15_33FD(): pass

    label("Function_15_33FD")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -22800, -20, 42870, 122)
    SetChrChipByIndex(0xFE, 27)
    OP_8E(0xFE, 0xFFFFB956, 0x0, 0x9C40, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)

    def lambda_3441():

        label("loc_3441")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3441")

    QueueWorkItem2(0xFE, 3, lambda_3441)
    Return()

    # Function_15_33FD end

    def Function_16_344F(): pass

    label("Function_16_344F")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -9450, -50, 48040, 199)
    SetChrChipByIndex(0xFE, 27)
    OP_8E(0xFE, 0xFFFFD0C6, 0x0, 0xA712, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)

    def lambda_3493():

        label("loc_3493")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3493")

    QueueWorkItem2(0xFE, 3, lambda_3493)
    Return()

    # Function_16_344F end

    def Function_17_34A1(): pass

    label("Function_17_34A1")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrPos(0xFE, -250, -20, 34650, 281)
    SetChrChipByIndex(0xFE, 27)
    OP_8E(0xFE, 0xFFFFDB70, 0x0, 0x89BC, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 26)
    SetChrSubChip(0xFE, 0)

    def lambda_34E5():

        label("loc_34E5")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_34E5")

    QueueWorkItem2(0xFE, 3, lambda_34E5)
    Return()

    # Function_17_34A1 end

    def Function_18_34F3(): pass

    label("Function_18_34F3")

    SetChrChipByIndex(0xFE, 27)

    def lambda_34FE():

        label("loc_34FE")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_34FE")

    QueueWorkItem2(0xFE, 3, lambda_34FE)
    OP_8E(0xFE, 0xFFFFC8CE, 0xFFFFFFBA, 0x8A3E, 0x1388, 0x0)
    Return()

    # Function_18_34F3 end

    def Function_19_3520(): pass

    label("Function_19_3520")

    SetChrChipByIndex(0xFE, 27)

    def lambda_352B():

        label("loc_352B")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_352B")

    QueueWorkItem2(0xFE, 3, lambda_352B)
    OP_8E(0xFE, 0xFFFFBE1A, 0xFFFFFFBA, 0x8D0E, 0x1388, 0x0)
    Return()

    # Function_19_3520 end

    def Function_20_354D(): pass

    label("Function_20_354D")

    SetChrChipByIndex(0xFE, 27)

    def lambda_3558():

        label("loc_3558")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_3558")

    QueueWorkItem2(0xFE, 3, lambda_3558)
    OP_8E(0xFE, 0xFFFFC1F8, 0x0, 0x9736, 0x1388, 0x0)
    Return()

    # Function_20_354D end

    def Function_21_357A(): pass

    label("Function_21_357A")

    SetChrChipByIndex(0xFE, 27)

    def lambda_3585():

        label("loc_3585")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_3585")

    QueueWorkItem2(0xFE, 3, lambda_3585)
    OP_8E(0xFE, 0xFFFFCE8C, 0x0, 0xA032, 0x1388, 0x0)
    Return()

    # Function_21_357A end

    def Function_22_35A7(): pass

    label("Function_22_35A7")

    SetChrChipByIndex(0xFE, 27)

    def lambda_35B2():

        label("loc_35B2")

        OP_99(0xFE, 0x0, 0x7, 0x9C4)
        OP_48()
        Jump("loc_35B2")

    QueueWorkItem2(0xFE, 3, lambda_35B2)
    OP_8E(0xFE, 0xFFFFD04E, 0xFFFFFFCE, 0x8BF6, 0x1388, 0x0)
    Return()

    # Function_22_35A7 end

    def Function_23_35D4(): pass

    label("Function_23_35D4")

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
        (0, "loc_364E"),
        (1, "loc_3654"),
        (SWITCH_DEFAULT, "loc_365A"),
    )


    label("loc_364E")

    OP_A2(0x1200)
    Jump("loc_365A")

    label("loc_3654")

    OP_A2(0x1201)
    Jump("loc_365A")

    label("loc_365A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3668")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_366C")

    label("loc_3668")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_366C")

    Return()

    # Function_23_35D4 end

    def Function_24_366D(): pass

    label("Function_24_366D")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_36A7")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_36C1")

    label("loc_36A7")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_36C1")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_24_366D end

    SaveToFile()

Try(main)
