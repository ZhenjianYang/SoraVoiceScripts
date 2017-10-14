from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4200   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Private Dan',                          # 9
        'Private Aluts',                        # 10
        'Royal Army Soldier',                   # 11
        'Royal Army Soldier',                   # 12
        'Royal Army Soldier',                   # 13
        'Royal Army Soldier',                   # 14
        'Royal Army Soldier',                   # 15
        'Royal Army Soldier',                   # 16
        'Royal Army Soldier',                   # 17
        'Royal Army Soldier',                   # 18
        'Royal Army Soldier',                   # 19
        'Royal Army Soldier',                   # 20
        'Royal Army Soldier',                   # 21
        'Royal Army Soldier',                   # 22
        'Royal Army Soldier',                   # 23
        'Royal Army Soldier',                   # 24
        'Royal Army Soldier',                   # 25
        'Luciola',                              # 26
        'Walter',                               # 27
        'Bleublanc',                            # 28
        'Renne',                                # 29
        'Pale Apache',                          # 30
        'Pale Apache',                          # 31
        'Pale Apache',                          # 32
        'Walter Afterimage',                    # 33
        'Walter Afterimage',                    # 34
        'Tourist',                              # 35
        'Tourist',                              # 36
        'Tourist',                              # 37
        'Tourist',                              # 38
        'Tourist',                              # 39
        'Grancel - North Block',                # 40
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT06/CH20043 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH01050 ._CH',             # 04
        'ED6_DT07/CH01040 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT06/CH20043P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH01050P._CP',             # 04
        'ED6_DT07/CH01040P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
    )

    DeclNpc(
        X                   = -790,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 950,
        Z                   = 0,
        Y                   = 41980,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        NpcIndex            = 0x185,
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
        X                   = 6640,
        Z                   = 0,
        Y                   = 24120,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 470,
        Z                   = 0,
        Y                   = 2060,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 8130,
        Z                   = 0,
        Y                   = 11800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 6210,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -2970,
        Z                   = 0,
        Y                   = 12840,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = -22550,
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
        X                   = -4500,
        Y                   = -2000,
        Z                   = 37000,
        Range               = 4200,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x9470,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -5250,
        Y                   = -1000,
        Z                   = 28530,
        Range               = 4870,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7468,
        Unknown_18          = 0x0,
        Unknown_1C          = 23,
    )


    DeclActor(
        TriggerX            = -11120,
        TriggerZ            = 0,
        TriggerY            = 19460,
        TriggerRange        = 1000,
        ActorX              = -15170,
        ActorZ              = -2000,
        ActorY              = 19020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 34,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_546",          # 00, 0
        "Function_1_63B",          # 01, 1
        "Function_2_79A",          # 02, 2
        "Function_3_917",          # 03, 3
        "Function_4_93B",          # 04, 4
        "Function_5_95F",          # 05, 5
        "Function_6_1C31",         # 06, 6
        "Function_7_2C38",         # 07, 7
        "Function_8_2E58",         # 08, 8
        "Function_9_30EE",         # 09, 9
        "Function_10_3279",        # 0A, 10
        "Function_11_33EC",        # 0B, 11
        "Function_12_36DE",        # 0C, 12
        "Function_13_4425",        # 0D, 13
        "Function_14_4431",        # 0E, 14
        "Function_15_4860",        # 0F, 15
        "Function_16_4A80",        # 10, 16
        "Function_17_4BE9",        # 11, 17
        "Function_18_5534",        # 12, 18
        "Function_19_5562",        # 13, 19
        "Function_20_5590",        # 14, 20
        "Function_21_55E4",        # 15, 21
        "Function_22_5701",        # 16, 22
        "Function_23_5832",        # 17, 23
        "Function_24_615D",        # 18, 24
        "Function_25_64B3",        # 19, 25
        "Function_26_64C9",        # 1A, 26
        "Function_27_6605",        # 1B, 27
        "Function_28_6741",        # 1C, 28
        "Function_29_687D",        # 1D, 29
        "Function_30_6A01",        # 1E, 30
        "Function_31_6B6E",        # 1F, 31
        "Function_32_6CF2",        # 20, 32
        "Function_33_6D78",        # 21, 33
        "Function_34_6DD1",        # 22, 34
    )


    def Function_0_546(): pass

    label("Function_0_546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_55B")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Call(0, 16)

    label("loc_55B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_57B")
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_591")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 21)
    Jump("loc_611")

    label("loc_591")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5A5"),
        (101, "loc_5DB"),
        (102, "loc_5F6"),
        (SWITCH_DEFAULT, "loc_611"),
    )


    label("loc_5A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C5")
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_5D8")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D8")
    OP_A2(0x1627)

    label("loc_5D8")

    Jump("loc_611")

    label("loc_5DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F3")
    SetMapFlags(0x10000000)
    OP_A3(0x203F)
    Event(0, 17)

    label("loc_5F3")

    Jump("loc_611")

    label("loc_5F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60E")
    SetMapFlags(0x10000000)
    OP_A2(0x203F)
    Event(0, 17)

    label("loc_60E")

    Jump("loc_611")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 3)), scpexpr(EXPR_END)), "loc_63A")
    SetChrPos(0x8, -2009, 0, 41980, 180)
    SetChrPos(0x9, 2270, 0, 41980, 180)

    label("loc_63A")

    Return()

    # Function_0_546 end

    def Function_1_63B(): pass

    label("Function_1_63B")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE4A80, 0x230060)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x550), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_662")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_682")
    OP_B1("t4200_y")
    Jump("loc_68B")

    label("loc_682")

    OP_B1("t4200_n")

    label("loc_68B")

    OP_72(0x0, 0x4)
    OP_71(0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_6E7")
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_71(0x1, 0x2)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 4)), scpexpr(EXPR_END)), "loc_6D6")
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 141)
    OP_72(0x2, 0x4)

    label("loc_6D6")

    OP_77(0xFF, 0xBD, 0xA7, 0x0, 0x0)
    Call(0, 15)
    OP_64(0x0, 0x1)

    label("loc_6E7")

    OP_72(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_700")
    Call(0, 22)

    label("loc_700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_711")
    OP_6F(0x0, 450)
    Jump("loc_794")

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_75A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_729")
    OP_6F(0x0, 450)
    Jump("loc_730")

    label("loc_729")

    OP_6F(0x0, 0)

    label("loc_730")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_73C"),
        (SWITCH_DEFAULT, "loc_757"),
    )


    label("loc_73C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_757")
    OP_6F(0x0, 450)
    OP_A2(0x2)
    Jump("loc_757")

    label("loc_757")

    Jump("loc_794")

    label("loc_75A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_END)), "loc_77C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_772")
    OP_6F(0x0, 0)
    Jump("loc_779")

    label("loc_772")

    OP_6F(0x0, 450)

    label("loc_779")

    Jump("loc_794")

    label("loc_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 3)), scpexpr(EXPR_END)), "loc_78D")
    OP_6F(0x0, 450)
    Jump("loc_794")

    label("loc_78D")

    OP_6F(0x0, 0)

    label("loc_794")

    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_63B end

    def Function_2_79A(): pass

    label("Function_2_79A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BF")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_901")

    label("loc_7BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D8")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_901")

    label("loc_7D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F1")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_901")

    label("loc_7F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_80A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_901")

    label("loc_80A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_823")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_901")

    label("loc_823")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_901")

    label("loc_83C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_855")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_901")

    label("loc_855")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_901")

    label("loc_86E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_887")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_901")

    label("loc_887")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A0")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_901")

    label("loc_8A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B9")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_901")

    label("loc_8B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D2")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_901")

    label("loc_8D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EB")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_901")

    label("loc_8EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_901")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_901")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_916")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_901")

    label("loc_916")

    Return()

    # Function_2_79A end

    def Function_3_917(): pass

    label("Function_3_917")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_93A")
    OP_8D(0xFE, 2620, 2600, -590, 3530, 2000)
    Jump("Function_3_917")

    label("loc_93A")

    Return()

    # Function_3_917 end

    def Function_4_93B(): pass

    label("Function_4_93B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_95E")
    OP_8D(0xFE, -1730, 10700, -4110, 14100, 2000)
    Jump("Function_4_93B")

    label("loc_95E")

    Return()

    # Function_4_93B end

    def Function_5_95F(): pass

    label("Function_5_95F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_992")

    ChrTalk(    #0
        0xFE,
        "Oh, you all are... Please, pass.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C2D")

    label("loc_992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_CC0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9C4")

    ChrTalk(    #1
        0xFE,
        "Please, pass.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C2C")

    label("loc_9C4")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x105, 160, 0, 39870, 0)
    SetChrPos(0x101, 80, 0, 38310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0E")
    SetChrPos(0x106, -740, 0, 36890, 0)
    Jump("loc_A1F")

    label("loc_A0E")

    SetChrPos(0x103, -740, 0, 36890, 0)

    label("loc_A1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A40")
    SetChrPos(0xF9, 710, 0, 37200, 0)
    Jump("loc_A51")

    label("loc_A40")

    SetChrPos(0xF8, 710, 0, 37200, 0)

    label("loc_A51")

    OP_6D(1350, 0, 42100, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_8C(0x8, 180, 0)
    SetChrSubChip(0x8, 0)
    OP_8C(0x9, 180, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()

    ChrTalk(    #2
        0x8,
        "#5PPrincess, will you be entering the castle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x105,
        "#041FYes, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        "If it is Her Highness' order...!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)
    Sleep(500)
    OP_22(0xD2, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x0, 450)
    OP_70(0x0, 0x1C2)
    Sleep(6700)
    OP_8C(0x9, 180, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #5
        0x8,
        "#1K#1PPlease, enter!\x02",
    )


    ChrTalk(    #6
        0x9,
        "#1KPlease, enter!\x02",
    )

    OP_56(0x1)
    OP_59()
    Fade(500)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_6D(0, 0, 40470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, 0, 40470, 360)
    SetChrPos(0x1, 0, 0, 40470, 360)
    SetChrPos(0x2, 0, 0, 40470, 360)
    SetChrPos(0x3, 0, 0, 40470, 360)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x2)
    EventEnd(0x0)

    label("loc_C2C")

    Jump("loc_CBD")

    label("loc_C2F")


    ChrTalk(    #7
        0xFE,
        "So Captain Amalthea was finally caught...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I guess this means Her Highness the Queen can\x01",
            "finally focus on the signing ceremony, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBD")

    Jump("loc_1C2D")

    label("loc_CC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_FDB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F77")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E9B")
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #9
        0xFE,
        "Princess, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x105,
        (
            "#040FDan, have you seen a little girl about\x01",
            "this high with a white dress?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "A girl in a dress... I don't remember\x01",
            "letting anyone like that into the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I don't think I saw her when I was patrolling\x01",
            "the square in front of the castle just a bit\x01",
            "ago either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x105,
        "#040FI see... Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "I-I'm very sorry. I wish I could have helped...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x105,
        "#040FNo, I'm sorry to have bothered you on duty.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F71")

    label("loc_E9B")


    ChrTalk(    #16
        0xFE,
        (
            "You're looking for a girl in a white dress,\x01",
            "you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "Hmm... I haven't let her into the castle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I don't think I saw her when I was patrolling\x01",
            "the square in front of the castle just a bit\x01",
            "ago, either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F71")

    OP_A2(0x164C)
    Jump("loc_FD8")

    label("loc_F77")


    ChrTalk(    #19
        0xFE,
        "A girl in a white dress, huh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I think I saw someone like that a few\x01",
            "days ago, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD8")

    Jump("loc_1C2D")

    label("loc_FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_103A")

    ChrTalk(    #21
        0xFE,
        "Princess, good work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "It's already evening, so do be careful as you go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C2D")

    label("loc_103A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1058")

    ChrTalk(    #23
        0xFE,
        "Please, enter!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C2D")

    label("loc_1058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1C2D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1121")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DF")
    TurnDirection(0x8, 0x105, 0)

    ChrTalk(    #24
        0x8,
        "Princess Klaudia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "Should you have business within\x01",
            "the castle just say so any time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_111E")

    label("loc_10DF")


    ChrTalk(    #26
        0x8,
        (
            "Should you have business in\x01",
            "the castle just say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_111E")

    Jump("loc_1C2D")

    label("loc_1121")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 6)), scpexpr(EXPR_END)), "loc_1481")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_143F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1282")
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_4A(0x9, 255)
    TurnDirection(0x9, 0x105, 300)
    Sleep(700)

    ChrTalk(    #27
        0x8,
        "P-Princess?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "Princess Klaudia!\x01",
            "I didn't know you were back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x105,
        (
            "#041FI came on a bit of a different\x01",
            "business this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "I-I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "Should you have business within\x01",
            "the castle just say so any time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x105,
        "#041FYes, thank you.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 300)
    OP_4B(0x9, 255)
    OP_A2(0x1671)
    Jump("loc_143C")

    label("loc_1282")


    ChrTalk(    #33
        0x8,
        (
            "What is it? Do you have business\x01",
            "in the castle after...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x105,
        "#048FIt's been a while, hasn't it, you two.\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_4A(0x9, 255)
    TurnDirection(0x8, 0x105, 300)
    TurnDirection(0x9, 0x105, 300)
    Sleep(400)

    ChrTalk(    #35
        0x8,
        "P-Princess?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "Princess Klaudia!\x01",
            "I didn't know you were back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x105,
        (
            "#041FI came on a bit of a different\x01",
            "business this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        "I-I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "Should you have business within\x01",
            "the castle just say so any time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1016F(V-Very impressive...)\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 300)
    OP_4B(0x9, 255)
    OP_A2(0x1671)

    label("loc_143C")

    Jump("loc_147E")

    label("loc_143F")


    ChrTalk(    #41
        0x8,
        (
            "Should you have business in\x01",
            "the castle just say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_147E")

    Jump("loc_1C2D")

    label("loc_1481")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A06")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D2")
    OP_4A(0x9, 255)
    TurnDirection(0x9, 0x105, 0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #42
        0x8,
        "P-Princess?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "Princess Klaudia!\x01",
            "I didn't know you were back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x105,
        (
            "#041FI came on a bit of a different\x01",
            "business this time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 300)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(700)

    ChrTalk(    #45
        0x8,
        "Oh?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 300)

    ChrTalk(    #46
        0x9,
        (
            "You're the victors of the Martial\x01",
            "Arts Competition, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1006FAhaha, it's been a while.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1631")

    ChrTalk(    #48
        0x108,
        "#071FThanks for your care the other time.\x02",
    )

    CloseMessageWindow()

    label("loc_1631")


    ChrTalk(    #49
        0x8,
        (
            "Well isn't this a surprise!\x01",
            "It's been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "If you have any business in the castle,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1006FYeah, thanks.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 300)
    OP_4B(0x9, 255)
    OP_A2(0x166E)
    OP_A2(0x1671)
    Jump("loc_1A03")

    label("loc_16D2")

    TurnDirection(0x9, 0x0, 0)
    OP_4A(0x9, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #52
        0x8,
        "Ohhh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "You're the victors of the Martial\x01",
            "Arts Competition, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1006FAhaha, it's been a while.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17BD")

    ChrTalk(    #55
        0x108,
        "#071FThanks for your care the other time.\x02",
    )

    CloseMessageWindow()

    label("loc_17BD")


    ChrTalk(    #56
        0x8,
        "Haha... What is it today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "If there's someone you'd like to speak with,\x01",
            "we can contact them immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        "Or would you like to tour the castle grounds?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#1015FNo, not exactly, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x105,
        "#048FIt's been a while, hasn't it, you two.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 0)
    TurnDirection(0x9, 0x105, 0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #61
        0x8,
        "P-Princess?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "Princess Klaudia!\x01",
            "I didn't know you were back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x105,
        (
            "#041FI came on a bit of a different\x01",
            "business this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        "I-I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "Should you have business within\x01",
            "the castle just say so any time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x105,
        "#041FYes, thank you very much.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 300)
    OP_4B(0x9, 255)
    OP_A2(0x166E)
    OP_A2(0x1671)

    label("loc_1A03")

    Jump("loc_1C2D")

    label("loc_1A06")

    TurnDirection(0x9, 0x0, 0)
    OP_4A(0x9, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x8,
        "Ohhh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "You're the victors of the Martial\x01",
            "Arts Competition, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#1006FAhaha, it's been a while.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AF1")

    ChrTalk(    #70
        0x108,
        "#071FThanks for your care the other time.\x02",
    )

    CloseMessageWindow()

    label("loc_1AF1")


    ChrTalk(    #71
        0x8,
        "Haha... What is it today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "If there's someone you'd like to speak with,\x01",
            "we can contact them immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        "Or would you like to tour the castle grounds?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1000FNo, we were just passing by today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "Ah, okay. Well, if anything does come up,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#1001FYeah, thanks.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 300)
    OP_4B(0x9, 255)
    OP_A2(0x166E)

    label("loc_1C2D")

    TalkEnd(0x8)
    Return()

    # Function_5_95F end

    def Function_6_1C31(): pass

    label("Function_6_1C31")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1CB9")

    ChrTalk(    #77
        0xFE,
        "Princess Klaudia should be in the castle, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "She's very busy, I believe, so you may not\x01",
            "be able to meet her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C34")

    label("loc_1CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1FD9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1CF3")

    ChrTalk(    #79
        0xFE,
        "Please, pass through.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F5B")

    label("loc_1CF3")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x105, 160, 0, 39870, 0)
    SetChrPos(0x101, 80, 0, 38310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D3D")
    SetChrPos(0x106, -740, 0, 36890, 0)
    Jump("loc_1D4E")

    label("loc_1D3D")

    SetChrPos(0x103, -740, 0, 36890, 0)

    label("loc_1D4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D6F")
    SetChrPos(0xF9, 710, 0, 37200, 0)
    Jump("loc_1D80")

    label("loc_1D6F")

    SetChrPos(0xF8, 710, 0, 37200, 0)

    label("loc_1D80")

    OP_6D(1350, 0, 42100, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_8C(0x8, 180, 0)
    SetChrSubChip(0x8, 0)
    OP_8C(0x9, 180, 0)
    SetChrSubChip(0x9, 0)
    OP_0D()

    ChrTalk(    #80
        0x8,
        "#5PPrincess, will you be entering the castle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x105,
        "#041FYes, please.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        "If it is Her Highness' order...!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 0, 400)
    Sleep(500)
    OP_22(0xD2, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x0, 450)
    OP_70(0x0, 0x1C2)
    Sleep(6700)
    OP_8C(0x9, 180, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #83
        0x8,
        "#1K#1PPlease, enter!\x02",
    )


    ChrTalk(    #84
        0x9,
        "#1KPlease, enter!\x02",
    )

    OP_56(0x1)
    OP_59()
    Fade(500)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    OP_6D(0, 0, 40470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, 0, 40470, 360)
    SetChrPos(0x1, 0, 0, 40470, 360)
    SetChrPos(0x2, 0, 0, 40470, 360)
    SetChrPos(0x3, 0, 0, 40470, 360)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x2)
    EventEnd(0x0)

    label("loc_1F5B")

    Jump("loc_1FD6")

    label("loc_1F5E")


    ChrTalk(    #85
        0xFE,
        (
            "We got hurt pretty bad by those\x01",
            "Intelligence Division guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "Honestly, I'm super relieved that they're caught.\x02",
    )

    CloseMessageWindow()

    label("loc_1FD6")

    Jump("loc_2C34")

    label("loc_1FD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_201A")

    ChrTalk(    #87
        0xFE,
        (
            "Oh, do you have business at the castle\x01",
            "today too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C34")

    label("loc_201A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2048")

    ChrTalk(    #88
        0xFE,
        "Princess Klaudia, welcome!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C34")

    label("loc_2048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2066")

    ChrTalk(    #89
        0xFE,
        "Please, enter!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C34")

    label("loc_2066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2C34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2136")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20ED")
    TurnDirection(0x9, 0x105, 0)

    ChrTalk(    #90
        0x9,
        "Princess Klaudia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        (
            "Should you have business within\x01",
            "the castle just say so any time!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2133")

    label("loc_20ED")


    ChrTalk(    #92
        0x9,
        (
            "Should you have business within\x01",
            "the castle just say so any time!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2133")

    Jump("loc_2C34")

    label("loc_2136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 6)), scpexpr(EXPR_END)), "loc_2496")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2454")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2297")
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x105, 300)
    Sleep(700)

    ChrTalk(    #93
        0x8,
        "P-Princess?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "Princess Klaudia!\x01",
            "I didn't know you were back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x105,
        (
            "#041FI came on a bit of a different\x01",
            "business this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        "I-I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x8,
        (
            "Should you have business within\x01",
            "the castle just say so any time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x105,
        "#041FYes, thank you.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 300)
    OP_4B(0x8, 255)
    OP_A2(0x1671)
    Jump("loc_2451")

    label("loc_2297")


    ChrTalk(    #99
        0x9,
        (
            "What is it? Do you have business\x01",
            "in the castle after...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x105,
        "#048FIt's been a while, hasn't it, you two.\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x105, 300)
    TurnDirection(0x9, 0x105, 300)
    Sleep(400)

    ChrTalk(    #101
        0x8,
        "P-Princess?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "Princess Klaudia!\x01",
            "I didn't know you were back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x105,
        (
            "#041FI came on a bit of a different\x01",
            "business this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x8,
        "I-I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        (
            "Should you have business within\x01",
            "the castle just say so any time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1016F(V-Very impressive...)\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 300)
    OP_4B(0x8, 255)
    OP_A2(0x1671)

    label("loc_2451")

    Jump("loc_2493")

    label("loc_2454")


    ChrTalk(    #107
        0x9,
        (
            "Should you have business in\x01",
            "the castle just say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2493")

    Jump("loc_2C34")

    label("loc_2496")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A0D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D9")
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x105, 0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #108
        0x8,
        "P-Princess?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x9,
        (
            "Princess Klaudia!\x01",
            "I didn't know you were back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x105,
        (
            "#041FI came on a bit of a different\x01",
            "business this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #111
        0x8,
        "Oh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        (
            "You're the victors of the Martial\x01",
            "Arts Competition, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1006FAhaha, it's been a while.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2638")

    ChrTalk(    #114
        0x108,
        "#071FThanks for your care the other time.\x02",
    )

    CloseMessageWindow()

    label("loc_2638")


    ChrTalk(    #115
        0x8,
        (
            "Well isn't this a surprise!\x01",
            "It's been a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "If you have any business in the castle,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        "#1006FYeah, thanks.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 300)
    OP_4B(0x8, 255)
    OP_A2(0x166E)
    OP_A2(0x1671)
    Jump("loc_2A0A")

    label("loc_26D9")

    TurnDirection(0x8, 0x0, 0)
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #118
        0x8,
        "Ohhh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x9,
        (
            "You're the victors of the Martial\x01",
            "Arts Competition, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#1006FAhaha, it's been a while.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C4")

    ChrTalk(    #121
        0x108,
        "#071FThanks for your care the other time.\x02",
    )

    CloseMessageWindow()

    label("loc_27C4")


    ChrTalk(    #122
        0x8,
        "Haha... What is it today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "If there's someone you'd like to speak with,\x01",
            "we can contact them immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x9,
        "Or would you like to tour the castle grounds?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        "#1015FNo, not exactly, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x105,
        "#048FIt's been a while, hasn't it, you two.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 0)
    TurnDirection(0x9, 0x105, 0)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #127
        0x8,
        "P-Princess?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x9,
        (
            "Princess Klaudia!\x01",
            "I didn't know you were back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x105,
        (
            "#041FI came on a bit of a different\x01",
            "business this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x8,
        "I-I see!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "Should you have business within\x01",
            "the castle just say so any time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x105,
        "#041FYes, thank you very much.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 300)
    OP_4B(0x8, 255)
    OP_A2(0x166E)
    OP_A2(0x1671)

    label("loc_2A0A")

    Jump("loc_2C34")

    label("loc_2A0D")

    TurnDirection(0x8, 0x0, 0)
    OP_4A(0x8, 255)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #133
        0x9,
        "Ohhh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x9,
        (
            "You're the victors of the Martial\x01",
            "Arts Competition, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1006FAhaha, it's been a while.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AF8")

    ChrTalk(    #136
        0x108,
        "#071FThanks for your care the other time.\x02",
    )

    CloseMessageWindow()

    label("loc_2AF8")


    ChrTalk(    #137
        0x8,
        "Haha... What is it today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "If there's someone you'd like to speak with,\x01",
            "we can contact them immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        "Or would you like to tour the castle grounds?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        "#1000FNo, we were just passing by today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        (
            "Ah, okay. Well, if anything does come up,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#1001FYeah, thanks.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 300)
    OP_4B(0x8, 255)
    OP_A2(0x166E)

    label("loc_2C34")

    TalkEnd(0x9)
    Return()

    # Function_6_1C31 end

    def Function_7_2C38(): pass

    label("Function_7_2C38")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C45")
    Jump("loc_2E54")

    label("loc_2C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2CFE")

    ChrTalk(    #143
        0xFE,
        (
            "Seems the last of the Intelligence Division\x01",
            "criminals were caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "It was inevitable, though. After all, Aidios is\x01",
            "watching to make sure they can't do anything\x01",
            "bad.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E54")

    label("loc_2CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2D48")

    ChrTalk(    #145
        0xFE,
        "Valleria Lake is incredibly big...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "Almost like a sea.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E54")

    label("loc_2D48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DA1")

    ChrTalk(    #147
        0xFE,
        (
            "It's been some time since I've relaxed\x01",
            "and watched the setting sun...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E54")

    label("loc_2DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2E13")

    ChrTalk(    #148
        0xFE,
        (
            "Oho, the fish seem to be swimming\x01",
            "along quite cheerily.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "If only I'd brought my fishing rod...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E54")

    label("loc_2E13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2E54")

    ChrTalk(    #150
        0xFE,
        (
            "Hmm, it seems like you could\x01",
            "fish quite well here...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E54")

    TalkEnd(0xFE)
    Return()

    # Function_7_2C38 end

    def Function_8_2E58(): pass

    label("Function_8_2E58")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2E65")
    Jump("loc_30EA")

    label("loc_2E65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2F33")

    ChrTalk(    #151
        0xFE,
        (
            "To think there was a battle between the\x01",
            "Intelligence Division and the Royal Guard...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        "I've come touring at a truly terrible time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "I hope the landing port isn't closed\x01",
            "like before...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30EA")

    label("loc_2F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2FAD")

    ChrTalk(    #154
        0xFE,
        (
            "I wonder if I can't get a glimpse of Princess\x01",
            "Klaudia somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        "I've never actually seen her before.\x02",
    )

    CloseMessageWindow()
    Jump("loc_30EA")

    label("loc_2FAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3011")

    ChrTalk(    #156
        0xFE,
        "This castle gate square is really nice.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "A lovely view, a pleasant breeze...\x02",
    )

    CloseMessageWindow()
    Jump("loc_30EA")

    label("loc_3011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3054")

    ChrTalk(    #158
        0xFE,
        "I took a tour of the castle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        "It was beautiful!\x02",
    )

    CloseMessageWindow()
    Jump("loc_30EA")

    label("loc_3054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_30EA")

    ChrTalk(    #160
        0xFE,
        (
            "This is my first time seeing\x01",
            "Grancel Castle up close.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "Its presence and bearing is far more impressive\x01",
            "in person than in photographs.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30EA")

    TalkEnd(0xFE)
    Return()

    # Function_8_2E58 end

    def Function_9_30EE(): pass

    label("Function_9_30EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_30FB")
    Jump("loc_3275")

    label("loc_30FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3131")

    ChrTalk(    #162
        0xFE,
        "An incident like that at the harbor...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3275")

    label("loc_3131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_3178")

    ChrTalk(    #163
        0xFE,
        (
            "Wonderful! I'd love to go to the harbor\x01",
            "in the evening.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3275")

    label("loc_3178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31EA")

    ChrTalk(    #164
        0xFE,
        (
            "The castle bathed in the setting sun...\x01",
            "How romantic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        "What should I see next, I wonder...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3275")

    label("loc_31EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3216")

    ChrTalk(    #166
        0xFE,
        "The wind here feels amazing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3275")

    label("loc_3216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3275")

    ChrTalk(    #167
        0xFE,
        (
            "He's getting pretty excited since this is\x01",
            "the first vacation we've had in a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3275")

    TalkEnd(0xFE)
    Return()

    # Function_9_30EE end

    def Function_10_3279(): pass

    label("Function_10_3279")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3286")
    Jump("loc_33E8")

    label("loc_3286")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_32C3")

    ChrTalk(    #168
        0xFE,
        "We just went to the harbor on tour yesterday.\x02",
    )

    CloseMessageWindow()
    Jump("loc_33E8")

    label("loc_32C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_330C")

    ChrTalk(    #169
        0xFE,
        (
            "Maybe today we'll go to the\x01",
            "cathedral and Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E8")

    label("loc_330C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3380")

    ChrTalk(    #170
        0xFE,
        (
            "There's so many places to see in the capital.\x01",
            "It's nice, but it makes it hard to visit\x01",
            "them all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33E8")

    label("loc_3380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_33A8")

    ChrTalk(    #171
        0xFE,
        "Now, where to go next...\x02",
    )

    CloseMessageWindow()
    Jump("loc_33E8")

    label("loc_33A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_33E8")

    ChrTalk(    #172
        0xFE,
        (
            "Hey! Hi there.\x01",
            "The capital's an amazing place, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33E8")

    TalkEnd(0xFE)
    Return()

    # Function_10_3279 end

    def Function_11_33EC(): pass

    label("Function_11_33EC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_33F9")
    Jump("loc_36DA")

    label("loc_33F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_34C6")

    ChrTalk(    #173
        0xFE,
        "Ahhhhhhhhhh!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Listen, listen! Yesterday I saw Miss Julia\x01",
            "running off towards the harbor!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "After that, those Intelligence Division goons\x01",
            "were caught, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        "It's so amaziiing!\x02",
    )

    CloseMessageWindow()
    Jump("loc_36DA")

    label("loc_34C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_355C")

    ChrTalk(    #177
        0xFE,
        (
            "I guess becoming a maid's my only\x01",
            "real way of meeting Miss Julia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xFE,
        (
            "But, it doesn't seem like they're\x01",
            "hiring for maids right now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36DA")

    label("loc_355C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3605")

    ChrTalk(    #179
        0xFE,
        (
            "I snuck into the castle and even went\x01",
            "as far as the Royal Guard's post.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0xFE,
        "But, I couldn't find Miss Julia there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xFE,
        "Awww, where did she gooooo?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_36DA")

    label("loc_3605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_368B")

    ChrTalk(    #182
        0xFE,
        (
            "Miss Julia, my idol...\x01",
            "How on earth can I meet you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xFE,
        (
            "I guess sneaking into the grounds\x01",
            "on a tour is the best way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36DA")

    label("loc_368B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_36DA")

    ChrTalk(    #184
        0xFE,
        (
            "I'm a fan of the Royal Guard.\x01",
            "Especially of Miss Julia, of course.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36DA")

    TalkEnd(0xFE)
    Return()

    # Function_11_33EC end

    def Function_12_36DE(): pass

    label("Function_12_36DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36EB")
    Return()

    label("loc_36EB")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CE, 1)), scpexpr(EXPR_END)), "loc_38A8")
    Fade(1000)
    SetChrPos(0x101, 530, 0, 37370, 357)
    SetChrPos(0x105, -430, 0, 38470, 357)
    SetChrPos(0x104, -1680, 0, 36350, 357)
    SetChrPos(0x108, 1800, 0, 36430, 357)
    OP_6D(660, 0, 40390, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(350, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #185
        0x8,
        "Good day, Your Highness!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x9,
        "#6PPlease don't overwork yourself, milady!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x105,
        (
            "#041F#4PHello, Dan. Hello, Aluts.\x01",
            "Don't worry, I'm fine.\x02\x03",

            "#542FEstelle and I have some business in\x01",
            "the castle to attend to.\x02\x03",

            "Could you let us pass, please?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4049")

    label("loc_38A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 6)), scpexpr(EXPR_END)), "loc_3C3B")
    Fade(1000)
    SetChrPos(0x101, 530, 0, 37370, 357)
    SetChrPos(0x105, -430, 0, 36000, 357)
    SetChrPos(0x104, -1680, 0, 36350, 357)
    SetChrPos(0x108, 1800, 0, 36430, 357)
    OP_6D(660, 0, 40390, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(350, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #188
        0x8,
        (
            "Oh, hey!\x01",
            "If it isn't our defenders of the crown!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x8,
        (
            "You guys basically have a free pass in here,\x01",
            "so if you want to see someone, we can get\x01",
            "you in easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x9,
        (
            "#6POr did you just want to have a walk around\x01",
            "the palace? That's okay, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        (
            "#1015F#4PUm, actually, I'm here on bracer\x01",
            "business today...\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x105, 0xFFFFFE52, 0x0, 0x9646, 0x7D0, 0x0)

    ChrTalk(    #192
        0x105,
        (
            "#048F#4PWhich is to say... Hello, Dan, Aluts.\x01",
            "It's been a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #193
        0x8,
        "Y-Your Highness!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x9,
        (
            "#6PPrincess Klaudia!\x01",
            "We were not aware you'd returned!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x105,
        (
            "#041F#4PHaha. Sorry to startle you two.\x01",
            "I'm afraid I'm here on business, though.\x02\x03",

            "#542FEstelle and I have some things in\x01",
            "the castle to attend to.\x02\x03",

            "Could you let us pass, please?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4049")

    label("loc_3C3B")

    Fade(1000)
    SetChrPos(0x101, 530, 0, 37370, 357)
    SetChrPos(0x105, -430, 0, 36000, 357)
    SetChrPos(0x104, -1680, 0, 36350, 357)
    SetChrPos(0x108, 1800, 0, 36430, 357)
    OP_6D(660, 0, 40390, 0)
    OP_67(0, 3780, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(53000, 0)
    OP_6E(350, 0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_0D()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #196
        0x8,
        "Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x9,
        (
            "#6PSay...you're the winners of the\x01",
            "Martial Arts Competition, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        "#1006F#4PAh, haha... Yeah, that's us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x108,
        "#071F#4PThanks for your help back then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x8,
        (
            "Hey, no worries!\x01",
            "So what brings you here today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x8,
        (
            "If you're here to see someone,\x01",
            "that can certainly be arranged.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x9,
        (
            "#6POr did you just want to have a walk around\x01",
            "the palace? That's okay, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        (
            "#1015F#4PUm, actually, I'm here on bracer\x01",
            "business today...\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x105, 0xFFFFFE52, 0x0, 0x9646, 0x7D0, 0x0)

    ChrTalk(    #204
        0x105,
        (
            "#048F#4PWhich is to say... Hello, Dan, Aluts.\x01",
            "It's been a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #205
        0x8,
        "Y-Your Highness!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x9,
        (
            "#6PPrincess Klaudia!\x01",
            "We were not aware you'd returned!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x105,
        (
            "#041F#4PHaha. Sorry to startle you two.\x01",
            "I'm afraid I'm here on business, though.\x02\x03",

            "#542FEstelle and I have some things in\x01",
            "the castle to attend to.\x02\x03",

            "Could you let us pass, please?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4049")


    ChrTalk(    #208
        0x8,
        "Of course, Your Highness!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x9,
        "#6PBy your command, milady!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        "#1016F#4P(Umm...wow.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x104,
        "#031F(Heh. Only slightly popular, isn't she?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x108,
        (
            "#070F#4P(Think I'm starting to get why that\x01",
            "duke guy is so jealous.)\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4127():
        OP_6D(70, 750, 44190, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4127)

    def lambda_413F():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_413F)

    def lambda_414F():
        OP_6E(438, 3000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_414F)
    OP_8E(0x9, 0x6E, 0x2EE, 0xADD4, 0x7D0, 0x0)
    OP_8C(0x9, 0, 400)
    WaitChrThread(0x105, 0x2)

    ChrTalk(    #213
        0x9,
        (
            "Now entering...Pr... Erm!\x01",
            "Ladies Kloe and Estelle and their entourage!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x9,
        "#6POpen the gate!\x02",
    )

    CloseMessageWindow()

    def lambda_41E2():
        OP_6D(70, 3450, 44190, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41E2)

    def lambda_41FA():
        OP_67(0, 7620, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_41FA)

    def lambda_4212():
        OP_8E(0x8, 0xFFFFF704, 0x2EE, 0xAE38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4212)
    OP_8E(0x9, 0x992, 0x2EE, 0xAE38, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    WaitChrThread(0x8, 0x1)
    OP_8C(0x8, 180, 400)
    OP_22(0xD2, 0x0, 0x64)
    Sleep(2000)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1C2)
    OP_73(0x0)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #215
        0x8,
        "#1K#1PPlease, come in!\x02",
    )


    ChrTalk(    #216
        0x9,
        "#1K#2PPlease, come in!\x02",
    )

    OP_56(0x1)
    OP_59()

    ChrTalk(    #217
        0x105,
        "#048F#5PHaha. Thank you, you two.\x02",
    )

    CloseMessageWindow()

    def lambda_42D4():
        OP_6D(530, 0, 40500, 1200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_42D4)

    def lambda_42EC():
        OP_67(0, 6000, -10000, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_42EC)
    Sleep(500)
    OP_8C(0x105, 135, 400)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #218
        0x105,
        (
            "#040F#5PWell, Estelle...welcome back to my house,\x01",
            "as it were. Come on in.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 315, 400)

    ChrTalk(    #219
        0x101,
        "#1008F#2PUh, thanks!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    Fade(500)
    OP_6D(0, 0, 40470, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 0, 0, 40470, 360)
    SetChrPos(0x1, 0, 0, 40470, 360)
    SetChrPos(0x2, 0, 0, 40470, 360)
    SetChrPos(0x3, 0, 0, 40470, 360)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x1623)
    EventEnd(0x0)
    Return()

    # Function_12_36DE end

    def Function_13_4425(): pass

    label("Function_13_4425")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_END)), "loc_442D")
    Return()

    label("loc_442D")

    OP_A2(0x1627)
    Return()

    # Function_13_4425 end

    def Function_14_4431(): pass

    label("Function_14_4431")

    EventBegin(0x0)
    SetChrPos(0x101, -310, 750, 49090, 180)
    SetChrPos(0x105, 720, 750, 48910, 180)
    SetChrPos(0x104, 990, 750, 50200, 180)
    SetChrPos(0x108, -540, 750, 50010, 180)
    OP_6D(120, 750, 45200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_44C3():
        OP_8E(0xFE, 0xFFFFFF2E, 0x2EE, 0xAC3A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44C3)
    Sleep(200)

    def lambda_44E3():
        OP_8E(0xFE, 0x26C, 0x2EE, 0xAB86, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_44E3)
    Sleep(200)

    def lambda_4503():
        OP_8E(0xFE, 0x3DE, 0x2EE, 0xB090, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4503)
    Sleep(200)

    def lambda_4523():
        OP_8E(0xFE, 0xFFFFFDE4, 0x2EE, 0xAFD2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_4523)
    WaitChrThread(0x108, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45DD")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as heard Nial is absent\x01",         # 0
            "Set as not heard Nial's absent\x01",      # 1
            "No change\x01",                           # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_45D1"),
        (1, "loc_45D7"),
        (SWITCH_DEFAULT, "loc_45DD"),
    )


    label("loc_45D1")

    OP_A2(0x1680)
    Jump("loc_45DD")

    label("loc_45D7")

    OP_A3(0x1680)
    Jump("loc_45DD")

    label("loc_45DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 0)), scpexpr(EXPR_END)), "loc_46B4")

    ChrTalk(    #220
        0x104,
        (
            "#030FEvening already... Time does fly when\x01",
            "you're having fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x105,
        "#040FNial should be back by now, hopefully.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        "#1011F#6PYeah, hopefully!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x108,
        (
            "#070F#6PAll right.\x01",
            "Let's get over to that newspaper.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47B2")

    label("loc_46B4")


    ChrTalk(    #224
        0x104,
        (
            "#030FEvening already... Time does fly when\x01",
            "you're having fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x105,
        (
            "#040FThe only letter victim we've yet to\x01",
            "visit is the Liberl News.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x101,
        "#1006F#6PYep!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x108,
        (
            "#070F#6PWell, let's not waste any more time, eh?\x01",
            "Let's get over there and see what's what.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47B2")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x0, 0)
    OP_6D(50, 750, 44240, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -60, 750, 44250, 180)
    SetChrPos(0x1, -60, 750, 44250, 180)
    SetChrPos(0x2, -60, 750, 44250, 180)
    SetChrPos(0x3, -60, 750, 44250, 180)
    OP_69(0x0, 0x0)
    OP_A2(0x1627)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_14_4431 end

    def Function_15_4860(): pass

    label("Function_15_4860")

    LoadEffect(0x0, "map\\\\mpsmk0.eff")
    LoadEffect(0x1, "map\\\\mpfire2.eff")
    LoadEffect(0x2, "map\\\\mpkaji0.eff")
    OP_22(0x87, 0x1, 0x50)
    OP_22(0xAE, 0x1, 0x50)
    PlayEffect(0x2, 0xFF, 0xFF, -150, 250, 42190, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 4900, 3600, 4050, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -100, 3300, -2001, 0, 0, 0, 1400, 1700, 1400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, -7410, 3800, 18520, 0, 0, 0, 1600, 1800, 1600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 6100, 3500, 18170, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -460, 3000, -2230, 0, 0, 0, 2200, 2200, 2200, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 4970, 3000, 4050, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, -7410, 3400, 18520, 0, 0, 0, 1700, 1700, 1700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 6100, 3000, 18170, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_15_4860 end

    def Function_16_4A80(): pass

    label("Function_16_4A80")

    SetChrPos(0xA, -2680, 0, 22070, 315)
    SetChrPos(0xB, -2480, 0, 20750, 180)
    SetChrPos(0xC, -1140, 0, 22210, 0)
    SetChrPos(0xD, -410, 0, 21460, 90)
    SetChrPos(0xE, 310, 0, 20760, 135)
    SetChrPos(0xF, 2220, 0, 22250, 270)
    SetChrPos(0x10, 2740, 0, 22270, 270)
    SetChrPos(0x11, 4170, 0, 21930, 225)
    SetChrPos(0x12, 4430, 0, 21030, 135)
    SetChrPos(0x13, -1230, 0, 19640, 0)
    SetChrPos(0x14, 400, 0, 19130, 270)
    SetChrPos(0x15, -3570, 0, 19150, 0)
    SetChrPos(0x16, -3030, 0, 21970, 270)
    SetChrPos(0x17, 2740, 0, 19290, 0)
    SetChrPos(0x18, -2190, 0, 18550, 135)
    ClearChrFlags(0xA, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x10, 0x1)
    ClearChrFlags(0x11, 0x1)
    ClearChrFlags(0x12, 0x1)
    ClearChrFlags(0x13, 0x1)
    ClearChrFlags(0x14, 0x1)
    ClearChrFlags(0x15, 0x1)
    ClearChrFlags(0x16, 0x1)
    ClearChrFlags(0x17, 0x1)
    ClearChrFlags(0x18, 0x1)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    Return()

    # Function_16_4A80 end

    def Function_17_4BE9(): pass

    label("Function_17_4BE9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D2(0x2701C8, 0x2701CD, 0x2)
    OP_D2(0x2701C6, 0x2701CB, 0x3)
    OP_D2(0x2701C9, 0x2701CE, 0x4)
    OP_D2(0x260003, 0x260008, 0x5)
    OP_D2(0x2601A7, 0x2601AC, 0x6)
    OP_D2(0x2600A0, 0x2600A5, 0x7)
    OP_D2(0x2601A7, 0x2601AC, 0x8)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    SetChrPos(0x1B, -290, 0, 28660, 0)
    SetChrPos(0x1C, -1380, 0, 26510, 0)
    SetChrPos(0x19, -70, 0, 24500, 0)
    SetChrPos(0x1A, 1500, 0, 26000, 0)
    SetChrChipByIndex(0x19, 2)
    SetChrChipByIndex(0x1A, 3)
    SetChrChipByIndex(0x1B, 4)
    SetChrChipByIndex(0x1C, 5)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    OP_6D(640, 0, 18960, 0)
    OP_67(0, 7320, -10000, 0)
    OP_6B(2590, 0)
    OP_6C(33000, 0)
    OP_6E(332, 0)
    LoadEffect(0x3, "scraft\\sc007_10.eff")
    LoadEffect(0x4, "map\\mp002_00.eff")
    OP_C8(0x200, 0x46, "C_PLAC00._CH", 0x0, 0x3E8)
    FadeToBright(1000, 0)

    def lambda_4D5B():
        OP_8E(0xFE, 0xFFFFFE8E, 0x0, 0xA262, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4D5B)

    def lambda_4D76():
        OP_8E(0xFE, 0xFFFFF984, 0x0, 0x9FCE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_4D76)

    def lambda_4D91():
        OP_8E(0xFE, 0xFFFFFEE8, 0x0, 0x9BFA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4D91)

    def lambda_4DAC():
        OP_8E(0xFE, 0x41A, 0x0, 0xA05A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4DAC)

    def lambda_4DC7():
        OP_6D(1440, 750, 44680, 6500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_4DC7)

    def lambda_4DDF():
        OP_67(0, 3770, -10000, 6500)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_4DDF)

    def lambda_4DF7():
        OP_6B(2380, 6500)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_4DF7)

    def lambda_4E07():
        OP_6E(507, 6500)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_4E07)
    WaitChrThread(0x1A, 0x1)
    SetChrChipByIndex(0x1A, 7)
    SetChrSubChip(0x1A, 0)
    WaitChrThread(0x19, 0x3)

    ChrTalk(    #228
        0x1C,
        "#264F#5PAww, the gates are closed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x1B,
        (
            "#230F#5PHmm. Given the age of this entrance,\x01",
            "I would imagine it can be opened manually.\x02\x03",

            "That would prove difficult, however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x19,
        "#244F#2PYes, it'll take quite a bit of pushing.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1C, 90, 400)
    Sleep(300)

    ChrTalk(    #231
        0x1C,
        (
            "#261F#1POooh, oooh! It's time to call in\x01",
            "Pater-Mater, isn't it?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x1A, 0x20)
    OP_8C(0x1A, 270, 400)
    Sleep(300)

    ChrTalk(    #232
        0x1A,
        (
            "#254F#2PHey, now. You call that thing in,\x01",
            "you won't leave anything for the\x01",
            "rest of us to do.\x02\x03",

            "#252FYou all just leave this to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1B, 135, 400)
    OP_8C(0x19, 45, 400)

    ChrTalk(    #233
        0x1C,
        "#267F#1PLeave it to you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x1A,
        "#252F#2PHeh. Just watch.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1A, 0x20)
    OP_8C(0x1A, 0, 400)

    def lambda_504A():
        OP_6D(1050, 750, 46640, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_504A)

    def lambda_5062():
        OP_6B(1950, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5062)

    def lambda_5072():

        label("loc_5072")

        TurnDirection(0xFE, 0x1A, 400)
        OP_48()
        Jump("loc_5072")

    QueueWorkItem2(0x1B, 2, lambda_5072)

    def lambda_5083():

        label("loc_5083")

        TurnDirection(0xFE, 0x1A, 400)
        OP_48()
        Jump("loc_5083")

    QueueWorkItem2(0x1C, 2, lambda_5083)

    def lambda_5094():

        label("loc_5094")

        TurnDirection(0xFE, 0x1A, 400)
        OP_48()
        Jump("loc_5094")

    QueueWorkItem2(0x19, 2, lambda_5094)
    ClearChrFlags(0x1A, 0x20)
    SetChrChipByIndex(0x1A, 3)
    OP_8E(0x1A, 0x12C, 0x2EE, 0xAFDC, 0x7D0, 0x0)
    OP_44(0x1B, 0x2)
    OP_44(0x1C, 0x2)
    OP_44(0x19, 0x2)
    OP_8C(0x1B, 0, 400)
    OP_8C(0x19, 0, 400)
    OP_8C(0x1C, 0, 400)
    WaitChrThread(0x101, 0x1)
    Fade(250)
    SetChrSubChip(0x1A, 0)
    SetChrChipByIndex(0x1A, 8)
    OP_0D()
    Sleep(500)
    OP_99(0x1A, 0x0, 0x2, 0x7D0)
    OP_9F(0x20, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    SetChrPos(0x20, 300, 750, 45020, 0)
    SetChrChipByIndex(0x20, 8)
    SetChrSubChip(0x20, 2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x20)
    SetChrFlags(0x20, 0x40)
    OP_9F(0x21, 0xFF, 0xFF, 0xFF, 0x5A, 0x0)
    SetChrPos(0x21, 300, 750, 45020, 0)
    SetChrChipByIndex(0x21, 8)
    SetChrSubChip(0x21, 2)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x20)
    SetChrFlags(0x21, 0x40)
    Sleep(500)

    def lambda_5180():
        OP_6B(1800, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5180)
    PlayEffect(0x3, 0x0, 0x1A, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)

    ChrTalk(    #235 op#A op#5
        0x1A,
        "#257F#6P#30A#100WKOOOOOOOOOOOH!\x05\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x2)
    Sleep(1500)
    WaitChrThread(0x101, 0x2)
    Sleep(1000)
    ClearMapFlags(0x10)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_5210():
        OP_99(0xFE, 0x2, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_5210)

    def lambda_5220():
        OP_99(0xFE, 0x2, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_5220)

    def lambda_5230():
        OP_99(0xFE, 0x2, 0x6, 0x7D0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_5230)
    OP_43(0x20, 0x0, 0x0, 0x12)
    OP_43(0x21, 0x0, 0x0, 0x13)
    OP_22(0x88, 0x0, 0x64)
    OP_7C(0x12C, 0x64, 0xBB8, 0x12C)
    Sleep(500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    Fade(500)
    Sleep(300)
    OP_43(0x1A, 0x3, 0x0, 0x14)
    SetChrPos(0x1A, 0, 750, 45050, 0)
    SetChrPos(0x20, 0, 750, 45050, 0)
    SetChrPos(0x21, 0, 750, 45050, 0)
    OP_6D(0, 3940, 46030, 0)
    OP_67(0, 3560, -10000, 0)
    OP_6B(1690, 0)
    OP_6C(0, 0)
    OP_6E(566, 0)

    def lambda_52F8():
        OP_6B(1890, 4000)
        ExitThread()

    QueueWorkItem(0x1A, 0, lambda_52F8)
    Sleep(450)
    OP_22(0x13C, 0x0, 0x64)
    Sleep(1350)
    OP_22(0xF6, 0x0, 0x64)
    PlayEffect(0x4, 0x1, 0xFF, 0, 500, 43120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_82(0x1, 0x2)
    WaitChrThread(0x1A, 0x0)
    WaitChrThread(0x1A, 0x3)
    Sleep(500)
    Fade(500)
    OP_6D(1000, 750, 44760, 0)
    OP_67(0, 3770, -10000, 0)
    OP_6B(2050, 0)
    OP_6C(33000, 0)
    OP_6E(507, 0)
    SetMapFlags(0x10)
    SetChrPos(0x1A, 410, 750, 45020, 0)
    SetChrPos(0x20, 300, 750, 45020, 0)
    SetChrPos(0x21, 300, 750, 45020, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #236
        0x1C,
        "#261F#1PWow! That was great, Walter!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x19,
        (
            "#241F#2PAh, yes. One of the Taito style's greatest\x01",
            "techniques.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x1B,
        "#231F#2PHah! Impressive as always, my friend.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    SetChrSubChip(0x1A, 0)
    SetChrChipByIndex(0x1A, 7)
    SetChrFlags(0x1A, 0x20)
    Sleep(300)
    OP_8C(0x1A, 225, 400)
    Sleep(300)

    ChrTalk(    #239
        0x1A,
        (
            "#250F#6PHeh heh. That shit's really only\x01",
            "good for street performances.\x02\x03",

            "#252FNow, one more to go through.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4210   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_4BE9 end

    def Function_18_5534(): pass

    label("Function_18_5534")

    OP_91(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    OP_91(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_5534 end

    def Function_19_5562(): pass

    label("Function_19_5562")

    OP_91(0xFE, 0x0, 0x0, 0x1F4, 0x7D0, 0x0)
    OP_91(0xFE, 0x0, 0x0, 0xFFFFFE0C, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_19_5562 end

    def Function_20_5590(): pass

    label("Function_20_5590")

    OP_72(0x1, 0x20)
    OP_72(0x1, 0x10)
    OP_72(0x1, 0x800)
    OP_B0(0x1, 0x19)
    OP_6F(0x1, 1)
    OP_70(0x1, 0x19)
    OP_73(0x1)
    Sleep(500)
    OP_B0(0x1, 0x23)
    OP_6F(0x1, 25)
    OP_70(0x1, 0x3C)
    OP_73(0x1)
    OP_B0(0x1, 0x28)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x8C)
    OP_73(0x1)
    Return()

    # Function_20_5590 end

    def Function_21_55E4(): pass

    label("Function_21_55E4")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 7)), scpexpr(EXPR_END)), "loc_5671")
    OP_6D(4310, 0, -4910, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 4310, 0, -4910, 0)
    SetChrPos(0x1, 4310, 0, -4910, 0)
    SetChrPos(0x2, 4310, 0, -4910, 0)
    SetChrPos(0x3, 4310, 0, -4910, 0)
    Jump("loc_56F2")

    label("loc_5671")

    OP_6D(-2630, 0, -4930, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -2630, 0, -4930, 0)
    SetChrPos(0x1, -2630, 0, -4930, 0)
    SetChrPos(0x2, -2630, 0, -4930, 0)
    SetChrPos(0x3, -2630, 0, -4930, 0)

    label("loc_56F2")

    OP_69(0x0, 0x0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_21_55E4 end

    def Function_22_5701(): pass

    label("Function_22_5701")

    LoadEffect(0x0, "map\\\\mp003_00.eff")
    OP_D2(0x290188, 0x29018C, 0x2)
    OP_D2(0x270110, 0x270120, 0x8)
    OP_D2(0x270111, 0x270121, 0x9)
    OP_D2(0x270130, 0x270140, 0xA)
    OP_D2(0x270131, 0x270141, 0xB)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_5760"),
        (5, "loc_5777"),
        (6, "loc_578E"),
        (7, "loc_57A5"),
        (SWITCH_DEFAULT, "loc_57BC"),
    )


    label("loc_5760")

    OP_D2(0x701D0, 0x701DC, 0xC)
    OP_D2(0x701D1, 0x701DD, 0xD)
    Jump("loc_57BC")

    label("loc_5777")

    OP_D2(0x70218, 0x70224, 0xC)
    OP_D2(0x70219, 0x70225, 0xD)
    Jump("loc_57BC")

    label("loc_578E")

    OP_D2(0x70230, 0x7023C, 0xC)
    OP_D2(0x70231, 0x7023D, 0xD)
    Jump("loc_57BC")

    label("loc_57A5")

    OP_D2(0x70248, 0x70254, 0xC)
    OP_D2(0x70249, 0x70255, 0xD)
    Jump("loc_57BC")

    label("loc_57BC")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_57D5"),
        (5, "loc_57EC"),
        (6, "loc_5803"),
        (7, "loc_581A"),
        (SWITCH_DEFAULT, "loc_5831"),
    )


    label("loc_57D5")

    OP_D2(0x701D0, 0x701DC, 0xE)
    OP_D2(0x701D1, 0x701DD, 0xF)
    Jump("loc_5831")

    label("loc_57EC")

    OP_D2(0x70218, 0x70224, 0xE)
    OP_D2(0x70219, 0x70225, 0xF)
    Jump("loc_5831")

    label("loc_5803")

    OP_D2(0x70230, 0x7023C, 0xE)
    OP_D2(0x70231, 0x7023D, 0xF)
    Jump("loc_5831")

    label("loc_581A")

    OP_D2(0x70248, 0x70254, 0xE)
    OP_D2(0x70249, 0x70255, 0xF)
    Jump("loc_5831")

    label("loc_5831")

    Return()

    # Function_22_5701 end

    def Function_23_5832(): pass

    label("Function_23_5832")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_583F")
    Return()

    label("loc_583F")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_585F")
    Call(0, 32)
    Call(0, 33)
    FadeToBright(0, 0)

    label("loc_585F")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58BE")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_58FC")

    label("loc_58BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58E5")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_58FC")

    label("loc_58E5")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_58FC")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5928")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5966")

    label("loc_5928")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_594F")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_5966")

    label("loc_594F")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_5966")

    Sleep(1000)

    def lambda_5971():
        OP_6D(2450, 750, 48690, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5971)

    def lambda_5989():
        OP_67(0, 6680, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5989)

    def lambda_59A1():
        OP_6B(2570, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_59A1)

    def lambda_59B1():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_59B1)
    OP_6E(403, 3000)
    Sleep(1000)
    Fade(500)
    OP_6D(490, 0, 35190, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(2270, 0)
    OP_6C(32000, 0)
    OP_6E(358, 0)
    SetChrPos(0x101, -760, 0, 34260, 0)
    SetChrPos(0x102, 620, 0, 34280, 0)
    SetChrPos(0xF8, -1040, 0, 32729, 0)
    SetChrPos(0xF9, 600, 0, 32930, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #240
        0x101,
        "#1020F#6PWhat in the...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x102,
        (
            "#1044F#4PNo large impact points.\x01",
            "I... I think this was broken\x01",
            "with someone's hand.\x02\x03",

            "#1042FThis looks like Walter's handiwork.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B2D")

    ChrTalk(    #242
        0x108,
        "#074F#2PYes... The shattering fist.\x02",
    )

    CloseMessageWindow()

    label("loc_5B2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B4F")

    ChrTalk(    #243
        0x106,
        "#055FAidios...\x02",
    )

    CloseMessageWindow()

    label("loc_5B4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B71")

    ChrTalk(    #244
        0x107,
        "#065FNo way...\x02",
    )

    CloseMessageWindow()

    label("loc_5B71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BB4")

    ChrTalk(    #245
        0x103,
        (
            "#025FWell, I'm nice and properly\x01",
            "terrified now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BB4")


    ChrTalk(    #246
        0x101,
        (
            "#1007F#6PHe really is freakishly strong...\x02\x03",

            "#1005F...Wait, what are we standing\x01",
            "around being impressed for?!\x02\x03",

            "We need to catch up to--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_22(0x77, 0x0, 0x64)
    OP_22(0x135, 0x1, 0x32)
    Sleep(200)
    OP_24(0x135, 0x3C)
    Sleep(200)
    OP_24(0x135, 0x46)
    Sleep(200)
    OP_24(0x135, 0x50)
    Sleep(200)
    OP_24(0x135, 0x5A)
    Sleep(200)
    OP_24(0x135, 0x64)

    ChrTalk(    #247
        0x102,
        "#1046F#4PEstelle! Watch out!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_5CD7():
        OP_96(0xFE, 0x834, 0x0, 0x8458, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5CD7)
    Sleep(50)

    def lambda_5CFA():
        OP_96(0xFE, 0xFFFFF7CC, 0x0, 0x8458, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CFA)
    OP_43(0x1D, 0x0, 0x0, 0x1A)

    def lambda_5D1F():
        OP_96(0xFE, 0xFFFFFB50, 0x0, 0x7724, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5D1F)
    Sleep(50)
    OP_43(0x1E, 0x0, 0x0, 0x1B)

    def lambda_5D49():
        OP_96(0xFE, 0x4B0, 0x0, 0x7724, 0xC8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5D49)
    OP_43(0x1F, 0x0, 0x0, 0x1C)
    SetChrPos(0x1D, 0, 12000, 38000, 180)
    SetChrPos(0x1E, 4000, 12000, 40000, 180)
    SetChrPos(0x1F, -4000, 12000, 40000, 180)
    SetChrChipByIndex(0x1D, 2)
    SetChrChipByIndex(0x1E, 2)
    SetChrChipByIndex(0x1F, 2)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    WaitChrThread(0x1D, 0x0)
    WaitChrThread(0x1E, 0x0)
    WaitChrThread(0x1F, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)
    Fade(500)
    ClearMapFlags(0x10)
    OP_6D(2190, 3130, 40810, 0)
    OP_67(0, 6790, -10000, 0)
    OP_6B(2930, 0)
    OP_6C(45000, 0)
    OP_6E(364, 0)
    SetChrPos(0x101, -670, 0, 30300, 0)
    SetChrPos(0x102, 950, 0, 30290, 0)
    SetChrPos(0xF8, -990, 0, 28900, 0)
    SetChrPos(0xF9, 1050, 0, 29020, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 8)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 10)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 12)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 14)
    OP_43(0x1D, 0x3, 0x0, 0x19)
    OP_43(0x1E, 0x3, 0x0, 0x19)
    OP_43(0x1F, 0x3, 0x0, 0x19)

    def lambda_5EAF():
        OP_8F(0xFE, 0x0, 0x9C4, 0x9470, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_5EAF)
    Sleep(200)

    def lambda_5ECF():
        OP_8F(0xFE, 0xFA0, 0x9C4, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_5ECF)
    Sleep(200)

    def lambda_5EEF():
        OP_8F(0xFE, 0xFFFFF060, 0x9C4, 0x9C40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_5EEF)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_5F14():
        OP_6D(2080, 0, 40810, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F14)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x101, 0x2)
    OP_23(0x77)
    Sleep(1000)

    def lambda_5F42():
        OP_6D(2710, 0, 37470, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5F42)

    def lambda_5F5A():
        OP_67(0, 4840, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F5A)

    def lambda_5F72():
        OP_6B(3540, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F72)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #248
        0x101,
        "#1005F#2POh, come on! Why here?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FD1")

    ChrTalk(    #249
        0x106,
        "#054FTake 'em down!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6021")

    label("loc_5FD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FF5")

    ChrTalk(    #250
        0x108,
        "#076FCome on!\x02",
    )

    CloseMessageWindow()
    Jump("loc_6021")

    label("loc_5FF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6021")

    ChrTalk(    #251
        0x103,
        "#024FLet's get whipping!\x02",
    )

    CloseMessageWindow()

    label("loc_6021")


    def lambda_6027():
        OP_6D(730, 0, 34730, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6027)

    def lambda_603F():
        OP_67(0, 5690, -10000, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_603F)

    def lambda_6057():
        OP_6B(2580, 300)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6057)

    def lambda_6067():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_6067)

    def lambda_6082():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 0, lambda_6082)

    def lambda_609D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_609D)

    def lambda_60B8():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_60B8)

    def lambda_60D3():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_60D3)

    def lambda_60EE():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_60EE)

    def lambda_6109():
        OP_91(0xFE, 0x0, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_6109)
    Sleep(200)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    OP_44(0x1D, 0x0)
    OP_44(0x1E, 0x0)
    OP_44(0x1F, 0x0)
    Battle(0x550, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 24)
    Return()

    # Function_23_5832 end

    def Function_24_615D(): pass

    label("Function_24_615D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x1D, 0x0)
    OP_44(0x1E, 0x0)
    OP_44(0x1F, 0x0)
    OP_44(0x101, 0x0)
    OP_44(0x102, 0x0)
    OP_44(0xF8, 0x0)
    OP_44(0xF9, 0x0)
    LoadEffect(0x1, "map\\\\mpsibuk.eff")
    LoadEffect(0x0, "battle\\\\btbomb00.eff")
    OP_D2(0x290188, 0x29018C, 0x2)
    SetChrPos(0x101, -990, 0, 32820, 270)
    SetChrPos(0x102, 450, 0, 32800, 90)
    SetChrPos(0xF8, -1100, 0, 31260, 270)
    SetChrPos(0xF9, 460, 0, 31240, 90)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 8)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 10)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 12)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 14)
    OP_6D(1820, 0, 35140, 0)
    OP_67(0, 7170, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(44000, 0)
    OP_6E(399, 0)
    SetChrChipByIndex(0x1D, 2)
    SetChrChipByIndex(0x1E, 2)
    SetChrChipByIndex(0x1F, 2)
    OP_43(0x1D, 0x3, 0x0, 0x19)
    OP_43(0x1E, 0x3, 0x0, 0x19)
    OP_43(0x1F, 0x3, 0x0, 0x19)
    SetChrPos(0x1D, 6510, 1500, 36000, 270)
    SetChrPos(0x1E, 6700, 1200, 31600, 270)
    SetChrPos(0x1F, -5430, 1700, 34200, 90)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)

    def lambda_62CE():
        OP_6D(40, 0, 32430, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_62CE)

    def lambda_62E6():
        OP_67(0, 6230, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_62E6)

    def lambda_62FE():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62FE)
    OP_43(0x1D, 0x0, 0x0, 0x1D)
    OP_43(0x1E, 0x0, 0x0, 0x1E)
    OP_43(0x1F, 0x0, 0x0, 0x1F)
    FadeToBright(1000, 0)
    WaitChrThread(0x1D, 0x1)
    WaitChrThread(0x1E, 0x1)
    WaitChrThread(0x1F, 0x1)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    Fade(500)
    OP_6D(-10, 0, 32470, 0)
    OP_67(0, 7480, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_22(0xD5, 0x0, 0x64)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x102, 0)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #252
        0x101,
        "#1005F#6P*huff*...Does this ever end?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 225, 500)

    ChrTalk(    #253
        0x102,
        "#1042F#6PThere's no time! Let's get inside!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x203D)
    Sleep(100)
    Fade(500)
    OP_6D(-480, 0, 33720, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -480, 0, 33720, 0)
    SetChrPos(0x1, -480, 0, 33720, 0)
    SetChrPos(0x2, -480, 0, 33720, 0)
    SetChrPos(0x3, -480, 0, 33720, 0)
    OP_0D()
    Call(0, 15)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_24_615D end

    def Function_25_64B3(): pass

    label("Function_25_64B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_64C8")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_25_64B3")

    label("loc_64C8")

    Return()

    # Function_25_64B3 end

    def Function_26_64C9(): pass

    label("Function_26_64C9")

    PlayEffect(0x0, 0xFF, 0xFF, 2200, 0, 36450, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 1030, 0, 34940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 80, 0, 33190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -1300, 0, 31960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -2130, 0, 30270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    Return()

    # Function_26_64C9 end

    def Function_27_6605(): pass

    label("Function_27_6605")

    PlayEffect(0x0, 0xFF, 0xFF, -1840, 0, 36190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, -580, 0, 34220, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 330, 0, 32790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 1800, 0, 31190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 2680, 0, 30010, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    Return()

    # Function_27_6605 end

    def Function_28_6741(): pass

    label("Function_28_6741")

    PlayEffect(0x0, 0xFF, 0xFF, -80, 0, 36860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 30, 0, 34690, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 60, 0, 32710, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 210, 0, 30920, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFF, 60, 0, 29140, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1F7, 0x0, 0x64)
    Sleep(100)
    Return()

    # Function_28_6741 end

    def Function_29_687D(): pass

    label("Function_29_687D")

    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x20)

    def lambda_688C():
        OP_D1(254, 0, 90000, -45000, 500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_688C)
    OP_44(0xFE, 0x3)

    def lambda_68AA():
        OP_8F(0xFE, 0x196E, 0xFFFFF060, 0x8CA0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_68AA)
    PlayEffect(0x0, 0x0, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0x1, 0xFE, 300, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x0, 0x0, 0xFE, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x0, 0x1, 0xFE, 100, 200, 200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x1)

    def lambda_69AD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_69AD)
    OP_22(0xDC, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0xFE, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 2, 2, 2, 0)
    Sleep(200)
    SetChrFlags(0xFE, 0x80)
    OP_82(0x0, 0x2)
    Return()

    # Function_29_687D end

    def Function_30_6A01(): pass

    label("Function_30_6A01")

    Sleep(400)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x20)

    def lambda_6A15():
        OP_D1(254, 0, 90000, -45000, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6A15)
    OP_44(0xFE, 0x3)

    def lambda_6A33():
        OP_8F(0xFE, 0x1A2C, 0xFFFFF060, 0x7B70, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A33)
    PlayEffect(0x0, 0x2, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0x3, 0xFE, 300, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x0, 0x2, 0xFE, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x0, 0x3, 0xFE, 100, 200, 200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x1)
    PlayEffect(0x1, 0x2, 0xFE, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 2, 2, 2, 0)
    SetChrFlags(0xFE, 0x80)
    OP_82(0x2, 0x2)
    Return()

    # Function_30_6A01 end

    def Function_31_6B6E(): pass

    label("Function_31_6B6E")

    Sleep(600)
    OP_44(0xFE, 0x3)
    SetChrFlags(0xFE, 0x20)

    def lambda_6B82():
        OP_D1(254, 0, 90000, -45000, 500)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6B82)
    OP_44(0xFE, 0x3)

    def lambda_6BA0():
        OP_8F(0xFE, 0xFFFFE4A8, 0xFFFFF060, 0x8598, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6BA0)
    PlayEffect(0x0, 0x4, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x0, 0x5, 0xFE, 300, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x0, 0x4, 0xFE, 0, 0, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x0, 0x5, 0xFE, 100, 200, 200, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x1)

    def lambda_6CA3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6CA3)
    PlayEffect(0x1, 0x4, 0xFE, 0, 1000, 0, 0, 0, 0, 800, 800, 800, 0xFF, 2, 2, 2, 0)
    Sleep(200)
    SetChrFlags(0xFE, 0x80)
    OP_82(0x4, 0x2)
    Return()

    # Function_31_6B6E end

    def Function_32_6CF2(): pass

    label("Function_32_6CF2")

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
        (0, "loc_6D6B"),
        (1, "loc_6D71"),
        (SWITCH_DEFAULT, "loc_6D77"),
    )


    label("loc_6D6B")

    OP_A2(0x1200)
    Jump("loc_6D77")

    label("loc_6D71")

    OP_A2(0x1201)
    Jump("loc_6D77")

    label("loc_6D77")

    Return()

    # Function_32_6CF2 end

    def Function_33_6D78(): pass

    label("Function_33_6D78")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_33_6D78 end

    def Function_34_6DD1(): pass

    label("Function_34_6DD1")

    EventBegin(0x1)

    ChrTalk(    #254
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_6DFD():
        OP_6D(-13180, -1000, 19320, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6DFD)

    def lambda_6E15():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_6E15)

    def lambda_6E25():
        OP_6C(45000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_6E25)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #255
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EDC")
    OP_C0(0xE, 0x2D, 0xFFFFD490, 0x0, 0x4C4A, 0x10E, 0xFFFFC4BE, 0xFFFFF63C, 0x4A4C)
    OP_6D(-9930, 0, 19230, 0)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_6EEB")

    label("loc_6EDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6EEB")
    EventEnd(0x1)

    label("loc_6EEB")

    Return()

    # Function_34_6DD1 end

    SaveToFile()

Try(main)
