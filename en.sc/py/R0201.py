from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R0201   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0201.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'CWO Ashton',                           # 9
        'Soldier',                              # 10
        'Soldier',                              # 11
        'Soldier',                              # 12
        'Soldier',                              # 13
        'Soldier',                              # 14
        'Soldier',                              # 15
        'Soldier',                              # 16
        'Soldier',                              # 17
        'Soldier',                              # 18
        'Soldier',                              # 19
        'Soldier',                              # 20
        'Soldier',                              # 21
        'Fog',                                  # 22
        'Rolent',                               # 23
        'Verte Bridge - Checkpoint',            # 24
        'Perzel Farm',                          # 25
        'Death Specular',                       # 26
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
        '',                                     # 38
        '',                                     # 39
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
        'ED6_DT29/CH12400 ._CH',             # 0E
        'ED6_DT29/CH12401 ._CH',             # 0F
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
        'ED6_DT29/CH12400P._CP',             # 0E
        'ED6_DT29/CH12401P._CP',             # 0F
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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

    DeclNpc(
        X                   = -186100,
        Z                   = 40,
        Y                   = -22120,
        Direction           = 213,
        Unknown2            = 14,
        Unknown3            = 917504,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        X                   = -186100,
        Y                   = -1040,
        Z                   = -22120,
        Range               = 2000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 4,
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
        TalkFunctionIndex   = 5,
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
        TalkFunctionIndex   = 6,
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
        TalkFunctionIndex   = 7,
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
        TalkFunctionIndex   = 41,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_586",          # 00, 0
        "Function_1_5CA",          # 01, 1
        "Function_2_7EB",          # 02, 2
        "Function_3_801",          # 03, 3
        "Function_4_899",          # 04, 4
        "Function_5_A68",          # 05, 5
        "Function_6_BE1",          # 06, 6
        "Function_7_D0B",          # 07, 7
        "Function_8_E34",          # 08, 8
        "Function_9_156C",         # 09, 9
        "Function_10_1A30",        # 0A, 10
        "Function_11_1FDC",        # 0B, 11
        "Function_12_2CF4",        # 0C, 12
        "Function_13_2D24",        # 0D, 13
        "Function_14_2D54",        # 0E, 14
        "Function_15_2D84",        # 0F, 15
        "Function_16_2DB4",        # 10, 16
        "Function_17_2DD0",        # 11, 17
        "Function_18_2E00",        # 12, 18
        "Function_19_2E30",        # 13, 19
        "Function_20_2E60",        # 14, 20
        "Function_21_2E90",        # 15, 21
        "Function_22_2EC0",        # 16, 22
        "Function_23_2EF0",        # 17, 23
        "Function_24_2F0C",        # 18, 24
        "Function_25_2F28",        # 19, 25
        "Function_26_2FFC",        # 1A, 26
        "Function_27_3016",        # 1B, 27
        "Function_28_3030",        # 1C, 28
        "Function_29_304A",        # 1D, 29
        "Function_30_3064",        # 1E, 30
        "Function_31_307E",        # 1F, 31
        "Function_32_30AC",        # 20, 32
        "Function_33_30DA",        # 21, 33
        "Function_34_3108",        # 22, 34
        "Function_35_3136",        # 23, 35
        "Function_36_3164",        # 24, 36
        "Function_37_3192",        # 25, 37
        "Function_38_31C0",        # 26, 38
        "Function_39_31EE",        # 27, 39
        "Function_40_3289",        # 28, 40
        "Function_41_32DB",        # 29, 41
    )


    def Function_0_586(): pass

    label("Function_0_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A0")
    Event(0, 10)
    Jump("loc_5B6")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B2")
    Event(0, 9)
    Jump("loc_5B6")

    label("loc_5B2")

    Event(0, 8)

    label("loc_5B6")

    Jump("loc_5C9")

    label("loc_5B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C9")
    Event(0, 11)

    label("loc_5C9")

    Return()

    # Function_0_586 end

    def Function_1_5CA(): pass

    label("Function_1_5CA")

    OP_16(0x2, 0xFA0, 0xFFFB54B0, 0xFFFD8730, 0x23000C)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F7")
    OP_6F(0x0, 0)
    Jump("loc_5FE")

    label("loc_5F7")

    OP_6F(0x0, 60)

    label("loc_5FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_610")
    OP_6F(0x1, 0)
    Jump("loc_617")

    label("loc_610")

    OP_6F(0x1, 60)

    label("loc_617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_629")
    OP_6F(0x2, 0)
    Jump("loc_630")

    label("loc_629")

    OP_6F(0x2, 60)

    label("loc_630")

    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_720")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_66A")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    OP_C4(0x0, 0x4)
    Jump("loc_720")

    label("loc_66A")

    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)
    OP_43(0x15, 0x0, 0x0, 0x3)

    label("loc_720")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_73E")
    SetChrFlags(0x19, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jump("loc_750")

    label("loc_73E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_750")
    ClearChrFlags(0x19, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_750")

    OP_51(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    Return()

    # Function_1_5CA end

    def Function_2_7EB(): pass

    label("Function_2_7EB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_800")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_7EB")

    label("loc_800")

    Return()

    # Function_2_7EB end

    def Function_3_801(): pass

    label("Function_3_801")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_898")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x22AB0), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_835")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_84A")

    label("loc_835")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x37), scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_84A")
    OP_4F(0x37, (scpexpr(EXPR_PUSH_LONG, 0x7D00), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_84A")

    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x22AB0), scpexpr(EXPR_NEG), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x65), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMUL), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_87B")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x13880), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_890")

    label("loc_87B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x38), scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_890")
    OP_4F(0x38, (scpexpr(EXPR_PUSH_LONG, 0x222E0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_890")

    Sleep(10)
    Jump("Function_3_801")

    label("loc_898")

    Return()

    # Function_3_801 end

    def Function_4_899(): pass

    label("Function_4_899")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31F, 5)), scpexpr(EXPR_END)), "loc_8A1")
    Return()

    label("loc_8A1")

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

    AnonymousTalk(    #0
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
        (1, "loc_995"),
        (SWITCH_DEFAULT, "loc_9B8"),
    )


    label("loc_995")

    Fade(500)
    OP_89(0x0, -191670, 190, -27970, 45)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_9B8")

    Battle(0xEEB, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -191670, 190, -27970, 45)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_9F1"),
        (1, "loc_9F4"),
        (SWITCH_DEFAULT, "loc_9F7"),
    )


    label("loc_9F1")

    EventEnd(0x0)
    Return()

    label("loc_9F4")

    OP_B4(0x0)
    Return()

    label("loc_9F7")

    EventBegin(0x1)
    SetChrFlags(0x19, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05Exterminated monster!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x18FD)
    OP_28(0xAF, 0x4, 0x10)
    OP_28(0xAF, 0x4, 0x2)
    OP_28(0xAF, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_4_899 end

    def Function_5_A68(): pass

    label("Function_5_A68")

    OP_EA(0x2, 0xC2, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B40")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xA7, 1)"), scpexpr(EXPR_END)), "loc_AD9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "Found \x1F\xA7\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1922)
    Jump("loc_B3D")

    label("loc_AD9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "Found \x1F\xA7\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xA7\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_B3D")

    Jump("loc_BD3")

    label("loc_B40")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05You find a message scratched along the\x01",
            "bottom: 'Loot this chest and do your worst.\x01",
            "But be warned, for ye be cursed.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BD3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_A68 end

    def Function_6_BE1(): pass

    label("Function_6_BE1")

    OP_EA(0x2, 0xC3, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CB9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x200, 1)"), scpexpr(EXPR_END)), "loc_C52")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "Found \x1F\x00\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1923)
    Jump("loc_CB6")

    label("loc_C52")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "Found \x1F\x00\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x00\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_CB6")

    Jump("loc_CFD")

    label("loc_CB9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05You obtain 80,000,000 imaginary mira.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_CFD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_BE1 end

    def Function_7_D0B(): pass

    label("Function_7_D0B")

    OP_EA(0x2, 0xC4, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_D7C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "Found \x1F\xF6\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1924)
    Jump("loc_DE0")

    label("loc_D7C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "Found \x1F\xF6\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xF6\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_DE0")

    Jump("loc_E26")

    label("loc_DE3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05FUN FACT: That didn't belong to you.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_E26")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_D0B end

    def Function_8_E34(): pass

    label("Function_8_E34")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E5E")
    Call(0, 39)
    FadeToBright(0, 0)
    Call(0, 40)

    label("loc_E5E")

    OP_6D(-140320, 20, -17700, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -134560, 0, -17700, 270)
    SetChrPos(0x103, -134560, 0, -18700, 270)
    SetChrPos(0xF8, -133560, 0, -17450, 270)
    SetChrPos(0xF9, -133560, 0, -18950, 270)

    def lambda_EE5():
        OP_90(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_EE5)
    Sleep(100)

    def lambda_F05():
        OP_90(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F05)
    Sleep(200)

    def lambda_F25():
        OP_90(0xFE, 0xFFFFE69C, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_F25)
    Sleep(100)

    def lambda_F45():
        OP_90(0xFE, 0xFFFFE69C, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_F45)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xF9, 0x1)

    ChrTalk(    #11
        0x101,
        "#1004F#6PHey!\x02",
    )

    CloseMessageWindow()

    def lambda_F82():
        OP_8E(0xFE, 0xFFFDBF98, 0x0, 0xFFFFBADC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F82)
    Sleep(100)

    def lambda_FA2():
        OP_8E(0xFE, 0xFFFDBF66, 0x0, 0xFFFFB65E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FA2)
    Sleep(200)

    def lambda_FC2():
        OP_8E(0xFE, 0xFFFDC6B4, 0x0, 0xFFFFBC44, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_FC2)
    Sleep(100)

    def lambda_FE2():
        OP_8E(0xFE, 0xFFFDC632, 0x0, 0xFFFFB744, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_FE2)

    def lambda_FFD():
        OP_6D(-146390, 0, -17590, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FFD)

    def lambda_1015():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1015)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x103, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    OP_8C(0x101, 295, 400)
    Sleep(50)
    OP_8C(0x103, 270, 400)
    Sleep(30)
    OP_8C(0xF8, 270, 400)
    Sleep(50)
    OP_8C(0xF9, 240, 400)
    Sleep(400)
    OP_8C(0x101, 270, 400)
    Sleep(50)
    OP_8C(0x103, 295, 400)
    Sleep(30)
    OP_8C(0xF8, 240, 400)
    Sleep(50)
    OP_8C(0xF9, 270, 400)
    Sleep(400)
    OP_8C(0x101, 240, 400)
    Sleep(50)
    OP_8C(0x103, 240, 400)
    Sleep(30)
    OP_8C(0xF8, 270, 400)
    Sleep(50)
    OP_8C(0xF9, 295, 400)
    Sleep(400)
    OP_8C(0x101, 270, 400)
    Sleep(50)
    OP_8C(0x103, 295, 400)
    Sleep(30)
    OP_8C(0xF8, 295, 400)
    Sleep(50)
    OP_8C(0xF9, 240, 400)
    Sleep(400)
    OP_8C(0x101, 90, 400)
    Sleep(50)
    OP_8C(0x103, 90, 400)
    Sleep(30)
    OP_8C(0xF8, 270, 400)
    Sleep(50)
    OP_8C(0xF9, 270, 400)
    Sleep(400)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1168")

    ChrTalk(    #12
        0x107,
        "#560FWow! It's all bright all of a sudden!\x02",
    )

    CloseMessageWindow()
    Jump("loc_126A")

    label("loc_1168")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A6")

    ChrTalk(    #13
        0x106,
        "#051FHuh. Well, that's a lot less foggy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_126A")

    label("loc_11A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11ED")

    ChrTalk(    #14
        0x104,
        (
            "#030FHm. The sun now shows her\x01",
            "lovely face to us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126A")

    label("loc_11ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1235")

    ChrTalk(    #15
        0x105,
        (
            "#048FHow wonderful.\x01",
            "The fog seems to have cleared.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126A")

    label("loc_1235")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126A")

    ChrTalk(    #16
        0x108,
        "#070FHey, it's a lot brighter now.\x02",
    )

    CloseMessageWindow()

    label("loc_126A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12CA")

    ChrTalk(    #17
        0x107,
        (
            "#061FI guess this is as far as the fog goes?\x01",
            "It kinda just...ends, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1440")

    label("loc_12CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1332")

    ChrTalk(    #18
        0x106,
        (
            "#051FLooks like this is as far as it goes.\x01",
            "Sorta a quick end to the fog, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1440")

    label("loc_1332")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137A")

    ChrTalk(    #19
        0x104,
        (
            "#030FIt seems the fog ends here...\x01",
            "quite abruptly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1440")

    label("loc_137A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13DA")

    ChrTalk(    #20
        0x105,
        (
            "#048FThis seems to be as far as the fog goes.\x01",
            "It does end quickly, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1440")

    label("loc_13DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1440")

    ChrTalk(    #21
        0x108,
        (
            "#070FGuess this is as far as the fog cover goes.\x01",
            "Kind of a sharp end to it, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1440")


    ChrTalk(    #22
        0x103,
        (
            "#026FSo along the Milch Main Road, the fog clears\x01",
            "around 80 selge from the city.\x02\x03",

            "#022FAnd there are monsters creeping about in\x01",
            "the fog as well. This could be a threat\x01",
            "to travelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1015F#6PYeah, that's true...\x02\x03",

            "Let's hurry and check the other roads\x01",
            "so we can tell Aina.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x180F)
    OP_28(0x8F, 0x2, 0x10)
    OP_28(0x8F, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_8_E34 end

    def Function_9_156C(): pass

    label("Function_9_156C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1596")
    Call(0, 39)
    FadeToBright(0, 0)
    Call(0, 40)

    label("loc_1596")

    OP_6D(-140320, 20, -17700, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -137560, 0, -17700, 270)
    SetChrPos(0x103, -137560, 0, -18700, 270)
    SetChrPos(0xF8, -136560, 0, -17450, 270)
    SetChrPos(0xF9, -136560, 0, -18950, 270)

    def lambda_161D():
        OP_8E(0xFE, 0xFFFDBF98, 0x0, 0xFFFFBADC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_161D)
    Sleep(100)

    def lambda_163D():
        OP_8E(0xFE, 0xFFFDBF66, 0x0, 0xFFFFB65E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_163D)
    Sleep(200)

    def lambda_165D():
        OP_8E(0xFE, 0xFFFDC6B4, 0x0, 0xFFFFBC44, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_165D)
    Sleep(100)

    def lambda_167D():
        OP_8E(0xFE, 0xFFFDC632, 0x0, 0xFFFFB744, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_167D)

    def lambda_1698():
        OP_6D(-146390, 0, -17590, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1698)

    def lambda_16B0():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_16B0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1703")

    ChrTalk(    #24
        0x107,
        "#061FYay, the fog's cleared! ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_17D5")

    label("loc_1703")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1736")

    ChrTalk(    #25
        0x106,
        "#051FAnd we're outta the fog.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17D5")

    label("loc_1736")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1771")

    ChrTalk(    #26
        0x104,
        "#030FAh, the fog ends here, it seems.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17D5")

    label("loc_1771")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A0")

    ChrTalk(    #27
        0x105,
        "#048FThe fog has cleared.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17D5")

    label("loc_17A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D5")

    ChrTalk(    #28
        0x108,
        "#070FLooks like the fog's cleared.\x02",
    )

    CloseMessageWindow()

    label("loc_17D5")


    ChrTalk(    #29
        0x103,
        (
            "#026FSo along the Milch Main Road, the fog clears\x01",
            "around eighty selge from the city.\x02\x03",

            "#022FAnd there are monsters creeping about in\x01",
            "the fog as well. This could be a threat\x01",
            "to travelers.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1941")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as investigated Malga Trail\x01",        # 0
            "Set as investigated Elize Highway\x01",      # 1
            "No change\x01",                              # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_192F"),
        (1, "loc_1938"),
        (SWITCH_DEFAULT, "loc_1941"),
    )


    label("loc_192F")

    OP_A3(0x180E)
    OP_A2(0x1810)
    Jump("loc_1941")

    label("loc_1938")

    OP_A2(0x180E)
    OP_A3(0x1810)
    Jump("loc_1941")

    label("loc_1941")

    TurnDirection(0x101, 0x103, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_END)), "loc_19B9")

    ChrTalk(    #30
        0x101,
        (
            "#1006F#6PYeah, let's make sure we tell Aina.\x02\x03",

            "All that's left is just the Elize Highway,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A1E")

    label("loc_19B9")


    ChrTalk(    #31
        0x101,
        (
            "#1006F#6PYeah, let's make sure we tell Aina.\x02\x03",

            "All that's left is just the Malga Trail,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A1E")

    OP_A2(0x180F)
    OP_28(0x8F, 0x2, 0x10)
    OP_28(0x8F, 0x1, 0x20)
    EventEnd(0x0)
    Return()

    # Function_9_156C end

    def Function_10_1A30(): pass

    label("Function_10_1A30")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A5A")
    Call(0, 39)
    FadeToBright(0, 0)
    Call(0, 40)

    label("loc_1A5A")

    OP_6D(-140320, 20, -17700, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(3180, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -137560, 0, -17700, 270)
    SetChrPos(0x103, -137560, 0, -18700, 270)
    SetChrPos(0xF8, -136560, 0, -17450, 270)
    SetChrPos(0xF9, -136560, 0, -18950, 270)

    def lambda_1AE1():
        OP_8E(0xFE, 0xFFFDBF98, 0x0, 0xFFFFBADC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AE1)
    Sleep(100)

    def lambda_1B01():
        OP_8E(0xFE, 0xFFFDBF66, 0x0, 0xFFFFB65E, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B01)
    Sleep(200)

    def lambda_1B21():
        OP_8E(0xFE, 0xFFFDC6B4, 0x0, 0xFFFFBC44, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1B21)
    Sleep(100)

    def lambda_1B41():
        OP_8E(0xFE, 0xFFFDC632, 0x0, 0xFFFFB744, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1B41)

    def lambda_1B5C():
        OP_6D(-146390, 0, -17590, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B5C)

    def lambda_1B74():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1B74)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BC7")

    ChrTalk(    #32
        0x107,
        "#061FYay, the fog's cleared! ♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C99")

    label("loc_1BC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BFA")

    ChrTalk(    #33
        0x106,
        "#051FAnd we're outta the fog.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C99")

    label("loc_1BFA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C35")

    ChrTalk(    #34
        0x104,
        "#030FAh, the fog ends here, it seems.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C99")

    label("loc_1C35")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C64")

    ChrTalk(    #35
        0x105,
        "#048FThe fog has cleared.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C99")

    label("loc_1C64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C99")

    ChrTalk(    #36
        0x108,
        "#070FLooks like the fog's cleared.\x02",
    )

    CloseMessageWindow()

    label("loc_1C99")


    ChrTalk(    #37
        0x103,
        (
            "#026FSo along the Milch Main Road, the fog clears\x01",
            "around 80 selge from the city.\x02\x03",

            "#022FAnd there are monsters creeping about in\x01",
            "the fog as well. This could be a threat\x01",
            "to travelers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1015F#6PYeah, that's true...\x02\x03",

            "And we've checked all three roads now,\x01",
            "so...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #39
        0x101,
        (
            "#1006F#6PTime to head back and report\x01",
            "to Aina, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E8C")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as haven't visited Bright house\x01",      # 0
            "Set as visited Bright house\x01",              # 1
            "No change\x01",                                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E80"),
        (1, "loc_1E86"),
        (SWITCH_DEFAULT, "loc_1E8C"),
    )


    label("loc_1E80")

    OP_A3(0x180D)
    Jump("loc_1E8C")

    label("loc_1E86")

    OP_A2(0x180D)
    Jump("loc_1E8C")

    label("loc_1E8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F62")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #40
        0x103,
        (
            "#023FWell, we can, but didn't you want to go\x01",
            "home for a little while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1004F#6POh, yeah! I almost forgot.\x02\x03",

            "#1008FLet's stop by on our way back\x01",
            "to the guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8F, 0x2, 0x10)
    OP_28(0x8F, 0x1, 0x20)
    OP_28(0x8F, 0x1, 0x800)
    OP_28(0x8F, 0x1, 0x1000)
    Jump("loc_1FD6")

    label("loc_1F62")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #42
        0x103,
        (
            "#021FUnless you can think of any other\x01",
            "pressing business, I'd say that's\x01",
            "right.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8F, 0x2, 0x10)
    OP_28(0x8F, 0x1, 0x20)
    OP_28(0x8F, 0x1, 0x200)
    OP_28(0x8F, 0x1, 0x400)

    label("loc_1FD6")

    OP_A2(0x180F)
    EventEnd(0x0)
    Return()

    # Function_10_1A30 end

    def Function_11_1FDC(): pass

    label("Function_11_1FDC")

    EventBegin(0x0)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrPos(0x101, -141380, 0, -19300, 270)
    SetChrPos(0x103, -141280, 0, -17970, 270)
    SetChrPos(0x107, -139730, 50, -17680, 270)
    SetChrPos(0x105, -139950, 20, -19100, 270)
    OP_6D(-142040, 0, -19080, 0)
    OP_67(0, 7030, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #43
        0x101,
        "#1004F#6POh, hey!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, -159130, 0, -15030, 135)
    SetChrPos(0x9, -161380, 10, -15080, 135)
    SetChrPos(0xA, -159660, 20, -13430, 135)
    SetChrPos(0xB, -162790, -10, -14750, 90)
    SetChrPos(0xC, -161600, -10, -12770, 90)
    SetChrPos(0xD, -164800, 10, -14940, 90)
    SetChrPos(0xE, -164010, -10, -12600, 90)
    SetChrPos(0xF, -166820, 0, -15120, 90)
    SetChrPos(0x10, -165800, 20, -12760, 90)
    SetChrPos(0x11, -168710, 0, -15170, 90)
    SetChrPos(0x12, -167690, 0, -12810, 90)
    SetChrPos(0x13, -171010, -20, -15140, 90)
    SetChrPos(0x14, -170070, 0, -12990, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    def lambda_21E5():
        OP_6D(-161370, 10, -15120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21E5)

    def lambda_21FD():
        OP_67(0, 9470, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21FD)
    Sleep(1200)
    OP_43(0x8, 0x0, 0x0, 0xC)
    Sleep(300)
    OP_43(0x9, 0x0, 0x0, 0xD)
    OP_43(0xA, 0x0, 0x0, 0xE)
    OP_43(0xB, 0x0, 0x0, 0xF)
    OP_43(0xC, 0x0, 0x0, 0x10)
    OP_43(0xD, 0x0, 0x0, 0x11)
    OP_43(0xE, 0x0, 0x0, 0x12)
    OP_43(0xF, 0x0, 0x0, 0x13)
    OP_43(0x10, 0x0, 0x0, 0x14)
    OP_43(0x11, 0x0, 0x0, 0x15)
    OP_43(0x12, 0x0, 0x0, 0x16)
    OP_43(0x13, 0x0, 0x0, 0x17)
    OP_43(0x14, 0x0, 0x0, 0x18)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    def lambda_2289():
        OP_6D(-153200, 0, -18030, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2289)
    WaitChrThread(0x8, 0x0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #44
        0x8,
        "#5PWho's--\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    Sleep(500)

    ChrTalk(    #45
        0x8,
        "#6P...Men, halt.\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, -143870, 0, -17360, 270)
    SetChrPos(0x103, -143760, 0, -16219, 270)
    SetChrPos(0x107, -142530, 0, -16120, 270)
    SetChrPos(0x105, -142450, 0, -17250, 270)

    def lambda_2321():
        OP_8E(0xFE, 0xFFFDAE4A, 0x0, 0xFFFFB988, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2321)
    Sleep(100)

    def lambda_2341():
        OP_8E(0xFE, 0xFFFDAE9A, 0x0, 0xFFFFBED8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2341)
    Sleep(100)

    def lambda_2361():
        OP_8E(0xFE, 0xFFFDB3AE, 0x0, 0xFFFFBA28, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2361)
    Sleep(100)

    def lambda_2381():
        OP_8E(0xFE, 0xFFFDB3E0, 0x0, 0xFFFFBF78, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2381)
    OP_8C(0x8, 90, 400)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x101, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2451")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as haven't met Mr. Ashton again yet\x01",      # 0
            "Set as have met Ashton again\x01",                 # 1
            "No change\x01",                                    # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2445"),
        (1, "loc_244B"),
        (SWITCH_DEFAULT, "loc_2451"),
    )


    label("loc_2445")

    OP_A3(0x1887)
    Jump("loc_2451")

    label("loc_244B")

    OP_A2(0x1887)
    Jump("loc_2451")

    label("loc_2451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FB")

    ChrTalk(    #46
        0x101,
        (
            "#1011F#6PMr. Ashton, hi!\x01",
            "It's really been a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "#4PIt has indeed, Estelle.\x01",
            "And you too, Scherazard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#4PYou're on some guild work,\x01",
            "I take it?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2581")

    label("loc_24FB")


    ChrTalk(    #49
        0x101,
        "#1011F#6PMr. Ashton! Hi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#4PEstelle, hello.\x01",
            "And Scherazard's with you, I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        "#4PYou're on some guild work, I take it?\x02",
    )

    CloseMessageWindow()

    label("loc_2581")


    ChrTalk(    #52
        0x101,
        (
            "#1025F#6PYeah, we are. You see--\x02\x03",

            "Wait. Squads coming to guard Rolent!\x01",
            "Is that...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        "#4PYes, that's us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#4PWe'll be protecting the city,\x01",
            "along with reinforcements from\x01",
            "the Haken Gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1017F#6PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x103,
        "#021FThank you, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "#4PNot at all. The duty of the Royal Army is\x01",
            "to protect Her Majesty's subjects.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        "#4PHow is Rolent looking?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#1015F#6PWell, the fog's getting thicker, but there\x01",
            "haven't been any new coma cases.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0x101,
        "#1020F#6PErm! Oh, I'm sorry, Mr. Ashton!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        "#4P...Yes, about Luke.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x8,
        (
            "#4PFrom what I've been told, he simply isn't\x01",
            "waking up. There's no threat to his health\x01",
            "otherwise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "#4PYou don't need to avoid the topic\x01",
            "for my sake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#1026F#6PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "#4PRight now, we both need to focus on\x01",
            "our jobs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#4PI suspect that's the best way we can\x01",
            "help save Luke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1025F#6PMr. Ashton...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x103,
        (
            "#026FThat's very true.\x02\x03",

            "#020FAshton, please take care of the city for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        "#4PAbsolutely. Leave it to us.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)
    Sleep(500)

    ChrTalk(    #70
        0x8,
        (
            "#6PMen, listen up!\x01",
            "Rolent is directly ahead!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "#6PI want patrol teams to begin their rounds\x01",
            "the instant our boots hit the pavement!\x01",
            "Is that clear?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetChrName("Soldiers")
    SetMessageWindowPos(350, 80, -1, -1)

    AnonymousTalk(    #72
        "\x07\x00#4SYES, SIR!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0x8, 90, 400)
    Sleep(200)
    OP_43(0x101, 0x3, 0x0, 0x19)
    WaitChrThread(0x101, 0x3)
    OP_43(0x8, 0x0, 0x0, 0x1A)

    def lambda_2A75():
        OP_6D(-147740, 0, -17850, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A75)
    OP_43(0x9, 0x0, 0x0, 0x1B)
    OP_43(0xA, 0x0, 0x0, 0x1C)
    OP_43(0xB, 0x0, 0x0, 0x1D)
    OP_43(0xC, 0x0, 0x0, 0x1E)
    OP_43(0xD, 0x0, 0x0, 0x1F)
    OP_43(0xE, 0x0, 0x0, 0x20)
    OP_43(0xF, 0x0, 0x0, 0x21)
    OP_43(0x10, 0x0, 0x0, 0x22)
    OP_43(0x11, 0x0, 0x0, 0x23)
    OP_43(0x12, 0x0, 0x0, 0x24)
    OP_43(0x13, 0x0, 0x0, 0x25)
    OP_43(0x14, 0x0, 0x0, 0x26)
    WaitChrThread(0x14, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0x105, 0x1)

    def lambda_2AF6():
        OP_6D(-150960, 10, -15560, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2AF6)
    Sleep(1000)

    def lambda_2B13():
        OP_8C(0x101, 45, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B13)
    Sleep(50)

    def lambda_2B26():
        OP_8C(0x105, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B26)
    Sleep(50)

    def lambda_2B39():
        OP_8C(0x103, 180, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B39)
    Sleep(50)
    OP_8C(0x107, 215, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #73
        0x107,
        "#063FUm, is that Luke's...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#1007FYeah... Mr. Ashton is Luke's father.\x02\x03",

            "#1003FI'm sure he's really beside himself with worry,\x01",
            "but he's trying not to show it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x105,
        (
            "#043F#6PHe seems like a very strong\x01",
            "kind of man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x103,
        (
            "#026FHe is. We'll have to do our best, too.\x02\x03",

            "#020FCome on. Perzel Farm isn't too far ahead,\x01",
            "if I remember correctly.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    OP_A2(0x181F)
    OP_28(0x91, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_11_1FDC end

    def Function_12_2CF4(): pass

    label("Function_12_2CF4")

    OP_8E(0xFE, 0xFFFD9F0E, 0x0, 0xFFFFBB90, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDA86E, 0x0, 0xFFFFBA8C, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_12_2CF4 end

    def Function_13_2D24(): pass

    label("Function_13_2D24")

    OP_8E(0xFE, 0xFFFD9680, 0x0, 0xFFFFB87A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDA0C6, 0xFFFFFFF6, 0xFFFFB7D0, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_13_2D24 end

    def Function_14_2D54(): pass

    label("Function_14_2D54")

    OP_8E(0xFE, 0xFFFD9C0C, 0x0, 0xFFFFBF6E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFDA1E8, 0x0, 0xFFFFBE92, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_14_2D54 end

    def Function_15_2D84(): pass

    label("Function_15_2D84")

    OP_8E(0xFE, 0xFFFD94F0, 0x0, 0xFFFFB816, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD9978, 0xFFFFFFF6, 0xFFFFB780, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_15_2D84 end

    def Function_16_2DB4(): pass

    label("Function_16_2DB4")

    OP_8E(0xFE, 0xFFFD9B6C, 0x0, 0xFFFFBF28, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_16_2DB4 end

    def Function_17_2DD0(): pass

    label("Function_17_2DD0")

    OP_8E(0xFE, 0xFFFD867C, 0xFFFFFFF6, 0xFFFFC6F8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD93A6, 0x0, 0xFFFFBA6E, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_17_2DD0 end

    def Function_18_2E00(): pass

    label("Function_18_2E00")

    OP_8E(0xFE, 0xFFFD8A82, 0x14, 0xFFFFCD7E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD963A, 0x0, 0xFFFFC220, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_18_2E00 end

    def Function_19_2E30(): pass

    label("Function_19_2E30")

    OP_8E(0xFE, 0xFFFD867C, 0xFFFFFFF6, 0xFFFFC6F8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD8EE2, 0x0, 0xFFFFBE9C, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_19_2E30 end

    def Function_20_2E60(): pass

    label("Function_20_2E60")

    OP_8E(0xFE, 0xFFFD8A82, 0x14, 0xFFFFCD7E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD9248, 0x0, 0xFFFFC626, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_20_2E60 end

    def Function_21_2E90(): pass

    label("Function_21_2E90")

    OP_8E(0xFE, 0xFFFD867C, 0xFFFFFFF6, 0xFFFFC6F8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD8B04, 0x0, 0xFFFFC248, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_21_2E90 end

    def Function_22_2EC0(): pass

    label("Function_22_2EC0")

    OP_8E(0xFE, 0xFFFD8A82, 0x14, 0xFFFFCD7E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFD8EB0, 0x14, 0xFFFFCA72, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_22_2EC0 end

    def Function_23_2EF0(): pass

    label("Function_23_2EF0")

    OP_8E(0xFE, 0xFFFD864A, 0xFFFFFFF6, 0xFFFFC6DA, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_23_2EF0 end

    def Function_24_2F0C(): pass

    label("Function_24_2F0C")

    OP_8E(0xFE, 0xFFFD89B0, 0xA, 0xFFFFCE6E, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_24_2F0C end

    def Function_25_2F28(): pass

    label("Function_25_2F28")


    def lambda_2F2E():
        OP_8E(0xFE, 0xFFFDB138, 0x28, 0xFFFFC6E4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2F2E)
    Sleep(50)

    def lambda_2F4E():
        OP_8E(0xFE, 0xFFFDB674, 0x14, 0xFFFFC75C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2F4E)
    Sleep(200)

    def lambda_2F6E():
        OP_8E(0xFE, 0xFFFDB156, 0xA, 0xFFFFC2B6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F6E)
    Sleep(50)

    def lambda_2F8E():
        OP_8E(0xFE, 0xFFFDB674, 0xA, 0xFFFFC31A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2F8E)
    WaitChrThread(0x103, 0x1)

    def lambda_2FAE():

        label("loc_2FAE")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2FAE")

    QueueWorkItem2(0x103, 1, lambda_2FAE)
    WaitChrThread(0x107, 0x1)

    def lambda_2FC4():

        label("loc_2FC4")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2FC4")

    QueueWorkItem2(0x107, 1, lambda_2FC4)
    WaitChrThread(0x101, 0x1)

    def lambda_2FDA():

        label("loc_2FDA")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2FDA")

    QueueWorkItem2(0x101, 1, lambda_2FDA)
    WaitChrThread(0x105, 0x1)

    def lambda_2FF0():

        label("loc_2FF0")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_2FF0")

    QueueWorkItem2(0x105, 1, lambda_2FF0)
    Return()

    # Function_25_2F28 end

    def Function_26_2FFC(): pass

    label("Function_26_2FFC")

    OP_8E(0xFE, 0xFFFE023C, 0x14, 0xFFFFB8E8, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_2FFC end

    def Function_27_3016(): pass

    label("Function_27_3016")

    OP_8E(0xFE, 0xFFFDFE04, 0x1E, 0xFFFFB6AE, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_27_3016 end

    def Function_28_3030(): pass

    label("Function_28_3030")

    OP_8E(0xFE, 0xFFFDFF1C, 0x14, 0xFFFFBD2A, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_28_3030 end

    def Function_29_304A(): pass

    label("Function_29_304A")

    OP_8E(0xFE, 0xFFFDF828, 0x28, 0xFFFFB730, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_304A end

    def Function_30_3064(): pass

    label("Function_30_3064")

    OP_8E(0xFE, 0xFFFDF90E, 0x14, 0xFFFFBD5C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_30_3064 end

    def Function_31_307E(): pass

    label("Function_31_307E")

    OP_8E(0xFE, 0xFFFD99AA, 0xFFFFFFF6, 0xFFFFB712, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF828, 0x28, 0xFFFFB730, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_31_307E end

    def Function_32_30AC(): pass

    label("Function_32_30AC")

    OP_8E(0xFE, 0xFFFD9A5E, 0x0, 0xFFFFBE6A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF90E, 0x14, 0xFFFFBD5C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_32_30AC end

    def Function_33_30DA(): pass

    label("Function_33_30DA")

    OP_8E(0xFE, 0xFFFD99AA, 0xFFFFFFF6, 0xFFFFB712, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF828, 0x28, 0xFFFFB730, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_33_30DA end

    def Function_34_3108(): pass

    label("Function_34_3108")

    OP_8E(0xFE, 0xFFFD9A5E, 0x0, 0xFFFFBE6A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF90E, 0x14, 0xFFFFBD5C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_34_3108 end

    def Function_35_3136(): pass

    label("Function_35_3136")

    OP_8E(0xFE, 0xFFFD99AA, 0xFFFFFFF6, 0xFFFFB712, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF828, 0x28, 0xFFFFB730, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_35_3136 end

    def Function_36_3164(): pass

    label("Function_36_3164")

    OP_8E(0xFE, 0xFFFD9A5E, 0x0, 0xFFFFBE6A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF90E, 0x14, 0xFFFFBD5C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_36_3164 end

    def Function_37_3192(): pass

    label("Function_37_3192")

    OP_8E(0xFE, 0xFFFD99AA, 0xFFFFFFF6, 0xFFFFB712, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF828, 0x28, 0xFFFFB730, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_37_3192 end

    def Function_38_31C0(): pass

    label("Function_38_31C0")

    OP_8E(0xFE, 0xFFFD9A5E, 0x0, 0xFFFFBE6A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFDF90E, 0x14, 0xFFFFBD5C, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_38_31C0 end

    def Function_39_31EE(): pass

    label("Function_39_31EE")

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
        (0, "loc_326A"),
        (1, "loc_3270"),
        (SWITCH_DEFAULT, "loc_3276"),
    )


    label("loc_326A")

    OP_A2(0x1200)
    Jump("loc_3276")

    label("loc_3270")

    OP_A2(0x1201)
    Jump("loc_3276")

    label("loc_3276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3284")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3288")

    label("loc_3284")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3288")

    Return()

    # Function_39_31EE end

    def Function_40_3289(): pass

    label("Function_40_3289")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_40_3289 end

    def Function_41_32DB(): pass

    label("Function_41_32DB")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #77
        "\x07\x05South: Perzel Farm\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_41_32DB end

    SaveToFile()

Try(main)
