from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R0203   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0203.x',
        MapIndex            = 22,
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '阿斯顿队长',                           # 9
        '士兵',                                 # 10
        '士兵',                                 # 11
        '士兵',                                 # 12
        '士兵',                                 # 13
        '士兵',                                 # 14
        '士兵',                                 # 15
        '士兵',                                 # 16
        '士兵',                                 # 17
        '士兵',                                 # 18
        '士兵',                                 # 19
        '士兵',                                 # 20
        '士兵',                                 # 21
        '王国军士官',                           # 22
        '王国军士兵',                           # 23
        '',                                     # 24
        '洛连特方向',                           # 25
        '威尔特桥·关所方向',                   # 26
        '帕赛尔农场方向',                       # 27
        '',                                     # 28
        '',                                     # 29
        '',                                     # 30
        '',                                     # 31
        '',                                     # 32
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
        'ED6_DT09/CH10020 ._CH',             # 00
        'ED6_DT09/CH10021 ._CH',             # 01
        'ED6_DT09/CH10180 ._CH',             # 02
        'ED6_DT09/CH10181 ._CH',             # 03
        'ED6_DT09/CH10260 ._CH',             # 04
        'ED6_DT09/CH10261 ._CH',             # 05
        'ED6_DT09/CH10210 ._CH',             # 06
        'ED6_DT09/CH10211 ._CH',             # 07
        'ED6_DT29/CH12090 ._CH',             # 08
        'ED6_DT29/CH12091 ._CH',             # 09
        'ED6_DT29/CH12130 ._CH',             # 0A
        'ED6_DT29/CH12131 ._CH',             # 0B
        'ED6_DT07/CH01310 ._CH',             # 0C
        'ED6_DT07/CH01640 ._CH',             # 0D
        'ED6_DT07/CH01600 ._CH',             # 0E
        'ED6_DT29/CH13050 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT09/CH10020P._CP',             # 00
        'ED6_DT09/CH10021P._CP',             # 01
        'ED6_DT09/CH10180P._CP',             # 02
        'ED6_DT09/CH10181P._CP',             # 03
        'ED6_DT09/CH10260P._CP',             # 04
        'ED6_DT09/CH10261P._CP',             # 05
        'ED6_DT09/CH10210P._CP',             # 06
        'ED6_DT09/CH10211P._CP',             # 07
        'ED6_DT29/CH12090P._CP',             # 08
        'ED6_DT29/CH12091P._CP',             # 09
        'ED6_DT29/CH12130P._CP',             # 0A
        'ED6_DT29/CH12131P._CP',             # 0B
        'ED6_DT07/CH01310P._CP',             # 0C
        'ED6_DT07/CH01640P._CP',             # 0D
        'ED6_DT07/CH01600P._CP',             # 0E
        'ED6_DT29/CH13050P._CP',             # 0F
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        X                   = -181690,
        Z                   = -310,
        Y                   = -45590,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -181520,
        Z                   = -400,
        Y                   = -47440,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -159140,
        Z                   = -60,
        Y                   = 5400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -131580,
        Z                   = 0,
        Y                   = -18130,
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
        X                   = -224350,
        Z                   = 20,
        Y                   = -16180,
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
        X                   = -184980,
        Z                   = 0,
        Y                   = -81290,
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
        X                   = -160000,
        Z                   = 200,
        Y                   = -2000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x79,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -161000,
        Z                   = 0,
        Y                   = -21000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -155000,
        Z                   = 0,
        Y                   = -44000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -178000,
        Z                   = 500,
        Y                   = -29000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -190000,
        Z                   = 0,
        Y                   = -39000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -205000,
        Z                   = 200,
        Y                   = -55000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -193000,
        Z                   = 200,
        Y                   = -2000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x79,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -207000,
        Z                   = 200,
        Y                   = -6000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -198000,
        Z                   = 300,
        Y                   = -47000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -180000,
        Z                   = -500,
        Y                   = -58000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -159000,
        Z                   = 200,
        Y                   = -59000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -180000,
        Z                   = 0,
        Y                   = -5000,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -172000,
        Z                   = 200,
        Y                   = -43000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x79,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -159140,
        Y                   = -60,
        Z                   = 5400,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = -176080,
        TriggerZ            = 50,
        TriggerY            = 11940,
        TriggerRange        = 1000,
        ActorX              = -176140,
        ActorZ              = 1050,
        ActorY              = 12680,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -211720,
        TriggerZ            = 20,
        TriggerY            = -56010,
        TriggerRange        = 1000,
        ActorX              = -211660,
        ActorZ              = 20,
        ActorY              = -56570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -145080,
        TriggerZ            = 40,
        TriggerY            = -50920,
        TriggerRange        = 1000,
        ActorX              = -144640,
        ActorZ              = 40,
        ActorY              = -51360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -179550,
        TriggerZ            = 0,
        TriggerY            = -15360,
        TriggerRange        = 1500,
        ActorX              = -179550,
        ActorZ              = 1500,
        ActorY              = -15360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_5A6",          # 00, 0
        "Function_1_5EF",          # 01, 1
        "Function_2_72A",          # 02, 2
        "Function_3_97B",          # 03, 3
        "Function_4_AB4",          # 04, 4
        "Function_5_BCB",          # 05, 5
        "Function_6_CE2",          # 06, 6
        "Function_7_DF9",          # 07, 7
        "Function_8_FB4",          # 08, 8
        "Function_9_1143",         # 09, 9
        "Function_10_11C1",        # 0A, 10
        "Function_11_123A",        # 0B, 11
        "Function_12_12D3",        # 0C, 12
        "Function_13_136F",        # 0D, 13
        "Function_14_13C1",        # 0E, 14
    )


    def Function_0_5A6(): pass

    label("Function_0_5A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5D5")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x27, 0x80)

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_5EE")
    OP_A3(0x10F0)
    OP_B5(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)

    label("loc_5EE")

    Return()

    # Function_0_5A6 end

    def Function_1_5EF(): pass

    label("Function_1_5EF")

    OP_16(0x2, 0xFA0, 0xFFFB54B0, 0xFFFD8730, 0x23000C)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_613")
    OP_6F(0x0, 0)
    Jump("loc_61A")

    label("loc_613")

    OP_6F(0x0, 60)

    label("loc_61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62C")
    OP_6F(0x1, 0)
    Jump("loc_633")

    label("loc_62C")

    OP_6F(0x1, 60)

    label("loc_633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_645")
    OP_6F(0x2, 0)
    Jump("loc_64C")

    label("loc_645")

    OP_6F(0x2, 60)

    label("loc_64C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_674")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_674")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)

    label("loc_674")

    OP_51(0x1B, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1D, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x20, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x21, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x22, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x23, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x26, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_B2(0x0, 0x0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_729")
    ClearChrFlags(0x17, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_729")

    Return()

    # Function_1_5EF end

    def Function_2_72A(): pass

    label("Function_2_72A")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_841")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E2")

    ChrTalk(    #0
        0xFE,
        (
            "看来定期船\x01",
            "好像也停开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "哎呀呀，交通工具\x01",
            "都闲下来了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "只是不能使用导力器\x01",
            "就成了这样的状况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "要是现在帝国攻进来\x01",
            "可是片刻也支撑不了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_83E")

    label("loc_7E2")


    ChrTalk(    #4
        0xFE,
        (
            "只是不能使用导力器\x01",
            "就成了这样的状况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "要是现在帝国攻进来\x01",
            "可是片刻也支撑不了啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_83E")

    Jump("loc_977")

    label("loc_841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_977")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_925")

    ChrTalk(    #6
        0xFE,
        (
            "啊，那胸前的纹章，\x01",
            "你们是游击士啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "让你们看见这副模样\x01",
            "真是不好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "我们在撤回基地途中，\x01",
            "引擎的输出突然下降。\x01",
            "于是慌忙着陆了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "救援要是能快点过来就好了，\x01",
            "不过这种状况下应该会延迟吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_977")

    label("loc_925")


    ChrTalk(    #10
        0xFE,
        (
            "多亏附近有农场\x01",
            "可是帮了大忙呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "我和部下一起\x01",
            "承蒙款待，在这里用了晚餐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_977")

    TalkEnd(0x15)
    Return()

    # Function_2_72A end

    def Function_3_97B(): pass

    label("Function_3_97B")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_A4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A04")

    ChrTalk(    #12
        0xFE,
        (
            "真是给这里的农场\x01",
            "添了不少麻烦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "分给我们的奶酪\x01",
            "实在是美味……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "哎，返回基地之前\x01",
            "买一些作为礼物吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_A4A")

    label("loc_A04")


    ChrTalk(    #15
        0xFE,
        (
            "这个农场的奶酪\x01",
            "真是极品啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "到底是洛连特。\x01",
            "食物真是美味啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A4A")

    Jump("loc_AB0")

    label("loc_A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_AB0")

    ChrTalk(    #17
        0xFE,
        (
            "到处都没有异常，\x01",
            "不过飞船就是动不了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "呼，在救援部队到来前，\x01",
            "只能在这里等下去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB0")

    TalkEnd(0x16)
    Return()

    # Function_3_97B end

    def Function_4_AB4(): pass

    label("Function_4_AB4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xA7, 1)"), scpexpr(EXPR_END)), "loc_B23")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x00得到了\x1F\xA7\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1922)
    Jump("loc_B89")

    label("loc_B23")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "宝箱里装有\x1F\xA7\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xA7\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_B89")

    Jump("loc_BBD")

    label("loc_B8C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BBD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_AB4 end

    def Function_5_BCB(): pass

    label("Function_5_BCB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_C3A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x00得到了\x1F\x00\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1923)
    Jump("loc_CA0")

    label("loc_C3A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "宝箱里装有\x1F\x00\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x00\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_CA0")

    Jump("loc_CD4")

    label("loc_CA3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CD4")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_BCB end

    def Function_6_CE2(): pass

    label("Function_6_CE2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_D51")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1924)
    Jump("loc_DB7")

    label("loc_D51")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_DB7")

    Jump("loc_DEB")

    label("loc_DBA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_DEB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_CE2 end

    def Function_7_DF9(): pass

    label("Function_7_DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41F, 1)), scpexpr(EXPR_END)), "loc_E01")
    Return()

    label("loc_E01")

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

    AnonymousTalk(    #28
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
        (1, "loc_EE6"),
        (SWITCH_DEFAULT, "loc_F09"),
    )


    label("loc_EE6")

    Fade(500)
    OP_89(0x0, -160450, 230, -1320, 0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_F09")

    Battle(0xEF0, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -160450, 230, -1320, 0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_F42"),
        (1, "loc_F45"),
        (SWITCH_DEFAULT, "loc_F48"),
    )


    label("loc_F42")

    EventEnd(0x0)
    Return()

    label("loc_F45")

    OP_B4(0x0)
    Return()

    label("loc_F48")

    EventBegin(0x1)
    SetChrFlags(0x17, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05消灭了通缉魔兽！\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x20F9)
    OP_28(0xB8, 0x4, 0x10)
    OP_28(0xB8, 0x4, 0x2)
    OP_28(0xB8, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_7_DF9 end

    def Function_8_FB4(): pass

    label("Function_8_FB4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x9, -165970, -10, -34300, 180)
    SetChrPos(0xC, -161610, 50, -48590, 319)
    SetChrPos(0xD, -159300, 120, -45800, 315)
    SetChrPos(0xE, -157300, 10, -39940, 225)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 12)
    SetChrSubChip(0xE, 0)
    OP_6D(-163100, 100, -41390, 0)
    OP_67(0, 11240, -10000, 0)
    OP_6B(7200, 0)
    OP_6C(78000, 0)
    OP_6E(295, 0)
    StopSound(0x7D00, 0x3F7A0, 0x0)
    OP_43(0x9, 0x1, 0x0, 0x9)
    OP_43(0xC, 0x1, 0x0, 0xA)
    OP_43(0xD, 0x1, 0x0, 0xB)
    OP_62(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x0)
    OP_C8(0x200, 0x46, "C_PLAC24._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)
    StopSound(0x7D00, 0x1FBD0, 0x1B58)

    def lambda_10EF():
        OP_67(0, 13250, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_10EF)

    def lambda_1107():
        OP_6B(3200, 7000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1107)

    def lambda_1117():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_1117)
    Sleep(6000)
    SetMapFlags(0x2000000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0900   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_FB4 end

    def Function_9_1143(): pass

    label("Function_9_1143")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11C0")
    Sleep(400)
    OP_8C(0xFE, 90, 400)
    Sleep(400)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)
    Sleep(400)
    OP_8C(0xFE, 315, 400)
    Sleep(800)
    OP_8C(0xFE, 270, 400)
    Sleep(600)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jump("Function_9_1143")

    label("loc_11C0")

    Return()

    # Function_9_1143 end

    def Function_10_11C1(): pass

    label("Function_10_11C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1239")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 180, 400)
    Sleep(600)
    OP_8C(0xFE, 225, 400)
    Sleep(400)
    OP_8C(0xFE, 270, 400)
    Sleep(800)
    OP_8C(0xFE, 225, 400)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)
    OP_8C(0xFE, 180, 400)
    Sleep(600)
    OP_8C(0xFE, 135, 400)
    Sleep(800)
    Jump("Function_10_11C1")

    label("loc_1239")

    Return()

    # Function_10_11C1 end

    def Function_11_123A(): pass

    label("Function_11_123A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12D2")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFD9694, 0x6E, 0xFFFF5042, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD952C, 0x50, 0xFFFF566E, 0x7D0, 0x0)
    OP_8C(0xFE, 272, 400)
    Sleep(500)
    OP_8E(0xFE, 0xFFFD9694, 0x6E, 0xFFFF5042, 0x7D0, 0x0)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFD91BC, 0x78, 0xFFFF4D18, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    Jump("Function_11_123A")

    label("loc_12D2")

    Return()

    # Function_11_123A end

    def Function_12_12D3(): pass

    label("Function_12_12D3")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_1350"),
        (1, "loc_1356"),
        (SWITCH_DEFAULT, "loc_135C"),
    )


    label("loc_1350")

    OP_A2(0x1200)
    Jump("loc_135C")

    label("loc_1356")

    OP_A2(0x1201)
    Jump("loc_135C")

    label("loc_135C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_136A")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_136E")

    label("loc_136A")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_136E")

    Return()

    # Function_12_12D3 end

    def Function_13_136F(): pass

    label("Function_13_136F")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_13_136F end

    def Function_14_13C1(): pass

    label("Function_14_13C1")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #30
        "\x07\x05南　帕赛尔农场\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_14_13C1 end

    SaveToFile()

Try(main)
