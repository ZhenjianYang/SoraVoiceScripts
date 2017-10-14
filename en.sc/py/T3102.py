from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3102   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Passenger',                            # 9
        'Passenger',                            # 10
        'Young Girl',                           # 11
        'Passenger',                            # 12
        'Young Boy',                            # 13
        'Passenger',                            # 14
        'Passenger',                            # 15
        'Passenger',                            # 16
        'Gerald',                               # 17
        'Bartholomew',                          # 18
        'Aldan',                                # 19
        'Rehmann',                              # 20
        'Rutherford',                           # 21
        'Noticia',                              # 22
        'Faults',                               # 23
        'Hugo',                                 # 24
        'Maintenance Chief Gustav',             # 25
        'Jimmy',                                # 26
        'Airliner, Cecilia',                    # 27
        'セシリア号影',                         # 28
        'Zeiss - Factory Block',                # 29
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01170 ._CH',             # 02
        'ED6_DT07/CH01130 ._CH',             # 03
        'ED6_DT07/CH01470 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01290 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01020 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT07/CH01140 ._CH',             # 0C
        'ED6_DT07/CH01680 ._CH',             # 0D
        'ED6_DT07/CH02440 ._CH',             # 0E
        'ED6_DT07/CH01180 ._CH',             # 0F
        'ED6_DT07/CH01200 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01170P._CP',             # 02
        'ED6_DT07/CH01130P._CP',             # 03
        'ED6_DT07/CH01470P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01290P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01020P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT07/CH01140P._CP',             # 0C
        'ED6_DT07/CH01680P._CP',             # 0D
        'ED6_DT07/CH02440P._CP',             # 0E
        'ED6_DT07/CH01180P._CP',             # 0F
        'ED6_DT07/CH01200P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        X                   = -20110,
        Z                   = 8000,
        Y                   = 121830,
        Direction           = 177,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -44890,
        Z                   = -4000,
        Y                   = 146670,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -41630,
        Z                   = 8000,
        Y                   = 123450,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -44830,
        Z                   = -4000,
        Y                   = 141220,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -50230,
        Z                   = 8000,
        Y                   = 121120,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -49500,
        Z                   = 8000,
        Y                   = 121470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -50910,
        Z                   = 8000,
        Y                   = 121470,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -46020,
        Z                   = -4000,
        Y                   = 146670,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -39960,
        Z                   = 8000,
        Y                   = 129060,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -44890,
        Z                   = -4000,
        Y                   = 140090,
        Direction           = 90,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
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
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -18770,
        Z                   = 8000,
        Y                   = 89560,
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


    DeclActor(
        TriggerX            = -19980,
        TriggerZ            = 8000,
        TriggerY            = 119710,
        TriggerRange        = 400,
        ActorX              = -20110,
        ActorZ              = 9500,
        ActorY              = 121830,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41010,
        TriggerZ            = 8000,
        TriggerY            = 122500,
        TriggerRange        = 800,
        ActorX              = -41010,
        ActorZ              = 10200,
        ActorY              = 122500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 47,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38900,
        TriggerZ            = 8400,
        TriggerY            = 122040,
        TriggerRange        = 800,
        ActorX              = -38900,
        ActorZ              = 9900,
        ActorY              = 122040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 48,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_43E",          # 00, 0
        "Function_1_56E",          # 01, 1
        "Function_2_63A",          # 02, 2
        "Function_3_7B7",          # 03, 3
        "Function_4_7BC",          # 04, 4
        "Function_5_F8D",          # 05, 5
        "Function_6_16F0",         # 06, 6
        "Function_7_1D27",         # 07, 7
        "Function_8_1E3B",         # 08, 8
        "Function_9_22AC",         # 09, 9
        "Function_10_23A3",        # 0A, 10
        "Function_11_2445",        # 0B, 11
        "Function_12_264F",        # 0C, 12
        "Function_13_2793",        # 0D, 13
        "Function_14_3378",        # 0E, 14
        "Function_15_33FC",        # 0F, 15
        "Function_16_42C8",        # 10, 16
        "Function_17_43C7",        # 11, 17
        "Function_18_440B",        # 12, 18
        "Function_19_4458",        # 13, 19
        "Function_20_44AA",        # 14, 20
        "Function_21_44FC",        # 15, 21
        "Function_22_4562",        # 16, 22
        "Function_23_45C8",        # 17, 23
        "Function_24_45F3",        # 18, 24
        "Function_25_4639",        # 19, 25
        "Function_26_467F",        # 1A, 26
        "Function_27_46C5",        # 1B, 27
        "Function_28_470B",        # 1C, 28
        "Function_29_4785",        # 1D, 29
        "Function_30_47FF",        # 1E, 30
        "Function_31_4879",        # 1F, 31
        "Function_32_48C2",        # 20, 32
        "Function_33_493C",        # 21, 33
        "Function_34_4977",        # 22, 34
        "Function_35_49B2",        # 23, 35
        "Function_36_52AF",        # 24, 36
        "Function_37_59A5",        # 25, 37
        "Function_38_59D3",        # 26, 38
        "Function_39_5A01",        # 27, 39
        "Function_40_5A43",        # 28, 40
        "Function_41_5A85",        # 29, 41
        "Function_42_5AC7",        # 2A, 42
        "Function_43_5B04",        # 2B, 43
        "Function_44_6507",        # 2C, 44
        "Function_45_659F",        # 2D, 45
        "Function_46_660D",        # 2E, 46
        "Function_47_6666",        # 2F, 47
        "Function_48_6721",        # 30, 48
    )


    def Function_0_43E(): pass

    label("Function_0_43E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_491")
    ClearChrFlags(0x18, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_48E")
    SetChrFlags(0x12, 0x80)
    SetChrPos(0x10, -23200, 8000, 121010, 180)
    ClearChrFlags(0x18, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -57460, 4000, 129380, 61)
    OP_8C(0x11, 90, 0)

    label("loc_48E")

    Jump("loc_54A")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E0")
    SetChrPos(0x12, -56860, 4000, 129490, 45)
    SetChrPos(0x14, -42830, 8000, 129500, 0)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x71, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4DD")
    ClearChrFlags(0x19, 0x80)

    label("loc_4DD")

    Jump("loc_54A")

    label("loc_4E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_525")
    SetChrPos(0x11, -44890, -4000, 146670, 270)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x12, -44340, -4000, 151130, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x10)
    Jump("loc_54A")

    label("loc_525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_540")
    SetChrPos(0x12, -47490, -4000, 151130, 270)
    Jump("loc_54A")

    label("loc_540")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_54A")
    Jump("loc_54A")

    label("loc_54A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55C")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)

    label("loc_55C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56D")
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_56D")

    Return()

    # Function_0_43E end

    def Function_1_56E(): pass

    label("Function_1_56E")

    OP_16(0x2, 0xFA0, 0xFFFD6020, 0x4E20, 0x230053)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B4")
    OP_B1("T3102_0")
    OP_6F(0x0, 530)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_5B1")
    OP_64(0x0, 0x1)

    label("loc_5B1")

    Jump("loc_639")

    label("loc_5B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E2")
    OP_B1("T3102_1")
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_6F(0x0, 1001)
    Jump("loc_639")

    label("loc_5E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_60A")
    OP_B1("T3102_2")
    OP_6F(0x4, 1)
    OP_6F(0x3, 200)
    OP_6F(0x0, 1001)
    Jump("loc_639")

    label("loc_60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_61D")
    OP_B1("T3102_0")
    Jump("loc_639")

    label("loc_61D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_630")
    OP_B1("T3102_0")
    Jump("loc_639")

    label("loc_630")

    OP_B1("T3102_1")

    label("loc_639")

    Return()

    # Function_1_56E end

    def Function_2_63A(): pass

    label("Function_2_63A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_7A1")

    label("loc_65F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_678")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_7A1")

    label("loc_678")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_691")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_7A1")

    label("loc_691")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_7A1")

    label("loc_6AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_7A1")

    label("loc_6C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_7A1")

    label("loc_6DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_7A1")

    label("loc_6F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70E")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_7A1")

    label("loc_70E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_727")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_7A1")

    label("loc_727")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_740")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_7A1")

    label("loc_740")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_759")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_7A1")

    label("loc_759")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_772")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_7A1")

    label("loc_772")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_7A1")

    label("loc_78B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A1")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_7A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7A1")

    label("loc_7B6")

    Return()

    # Function_2_63A end

    def Function_3_7B7(): pass

    label("Function_3_7B7")

    Call(0, 4)
    Return()

    # Function_3_7B7 end

    def Function_4_7BC(): pass

    label("Function_4_7BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_981")
    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C4")

    ChrTalk(    #0
        0xFE,
        (
            "The dock functions on orbal technology,\x01",
            "so we can't do a damn thing until things\x01",
            "are back up and running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "That's the downside to getting too high\x01",
            "tech. Might be convenient most of the time,\x01",
            "but you're screwed if things goes awry.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_97B")

    label("loc_8C4")


    ChrTalk(    #2
        0xFE,
        (
            "The dock functions on orbal technology,\x01",
            "so we can't do a damn thing until things\x01",
            "are back up and running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "At least with a normal dock, we could\x01",
            "do some kinda maintenance...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97B")

    TalkEnd(0x10)
    Jump("loc_F8C")

    label("loc_981")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B3C")
    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8D")

    ChrTalk(    #4
        0xFE,
        (
            "When the Orbal Shutdown Phenomenon\x01",
            "started, man! It was horrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I think you could paint a picture of that\x01",
            "moment and put it in the dictionary under\x01",
            "'panic.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Well, I guess I can't talk. I was freaking\x01",
            "out same as everyone else.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_B36")

    label("loc_A8D")


    ChrTalk(    #7
        0xFE,
        (
            "When the Orbal Shutdown Phenomenon\x01",
            "started, man! It was horrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I think you could paint a picture of that\x01",
            "moment and put it in the dictionary under\x01",
            "'panic.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B36")

    TalkEnd(0x10)
    Jump("loc_F8C")

    label("loc_B3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B57")
    OP_4A(0x10, 255)
    Call(0, 35)
    OP_4B(0x10, 255)
    Jump("loc_F8C")

    label("loc_B57")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_C69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BEE")

    ChrTalk(    #9
        0x10,
        "The work will be done at Leiston Fortress.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "I guess they've got their own\x01",
            "circumstances and military secrets\x01",
            "and whatnot.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C66")

    label("loc_BEE")


    ChrTalk(    #11
        0x10,
        (
            "They're finally gonna load the new\x01",
            "engine onto the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "The factory ship's getting ready\x01",
            "as we speak.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_C66")

    Jump("loc_F89")

    label("loc_C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_E6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D39")

    ChrTalk(    #13
        0x10,
        (
            "Thanks to that Liberl News article,\x01",
            "I really get what's going on with that\x01",
            "non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "That's the Liberl News for you!\x01",
            "Real deep, but they're a nice read\x01",
            "at the same time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E68")

    label("loc_D39")


    ChrTalk(    #15
        0x10,
        (
            "Lately, the Liberl News has been\x01",
            "putting a lot of effort into covering\x01",
            "the non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "I feel like I understand the importance\x01",
            "of the pact a whole lot more than\x01",
            "I would've otherwise thanks to that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "I'll be paying close attention to the\x01",
            "signing ceremony that's coming up\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_E68")

    Jump("loc_F89")

    label("loc_E6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_F89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EE9")

    ChrTalk(    #18
        0x10,
        "Boy, that sure was a close one!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "The scariest part of a disaster is\x01",
            "the way people lose their cool.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F89")

    label("loc_EE9")


    ChrTalk(    #20
        0x10,
        "*pheeeew* That was freaky.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "Felt like everyone lost their damn\x01",
            "mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "Well, me jumping in helped prevent\x01",
            "things from getting worse, thankfully.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F89")

    TalkEnd(0x10)

    label("loc_F8C")

    Return()

    # Function_4_7BC end

    def Function_5_F8D(): pass

    label("Function_5_F8D")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1163")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AA")

    ChrTalk(    #23
        0xFE,
        (
            "For now, we just figured it'd be\x01",
            "best to do some good ol' fashioned\x01",
            "maintenance\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Not that 'maintenance' means all\x01",
            "that much besides oilin' some bits\x01",
            "and polishing others...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "But, I'm sure the machines appreciate\x01",
            "it more than us just doing nothing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1160")

    label("loc_10AA")


    ChrTalk(    #26
        0xFE,
        (
            "For now, we just figured it'd be\x01",
            "best to do some good ol' fashioned\x01",
            "maintenance\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Not that 'maintenance' means all\x01",
            "that much besides oilin' some bits\x01",
            "and polishing others...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1160")

    Jump("loc_16EC")

    label("loc_1163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1236")

    ChrTalk(    #28
        0xFE,
        (
            "That phenomenon hit while we\x01",
            "were moving the factory ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "Now it's stuck in that halfway spot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "We've got no way to get down,\x01",
            "and no way to go to fix it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "Geez, NOW what?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_12A2")

    label("loc_1236")


    ChrTalk(    #32
        0xFE,
        (
            "That phenomenon hit while we\x01",
            "were moving the factory ship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "Now it's stuck in that halfway spot.\x02",
    )

    CloseMessageWindow()

    label("loc_12A2")

    Jump("loc_16EC")

    label("loc_12A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_137D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1334")

    ChrTalk(    #34
        0xFE,
        (
            "The Arseille's been loaded with a\x01",
            "brand spankin' new engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Oh, boy! I'd love to get a look at\x01",
            "such a masterpiece.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137A")

    label("loc_1334")


    ChrTalk(    #36
        0xFE,
        "The factory ship's out right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "I wanted to go, too...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_137A")

    Jump("loc_16EC")

    label("loc_137D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1487")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1422")

    ChrTalk(    #38
        0xFE,
        (
            "They're finally going to equip the\x01",
            "new engine model into the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Good luck with the swap-over job.\x01",
            "I'll be here, praying to Aidios.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1484")

    label("loc_1422")


    ChrTalk(    #40
        0xFE,
        (
            "Don't worry--we've already loaded\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "All the goods listed have been\x01",
            "loaded.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1484")

    Jump("loc_16EC")

    label("loc_1487")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1646")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1540")

    ChrTalk(    #42
        0xFE,
        (
            "All right! It's about time to ready\x01",
            "up launch for the factory ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "I wanna get the bare minimum\x01",
            "done before the maintenance chief\x01",
            "shows his mug around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1643")

    label("loc_1540")


    ChrTalk(    #44
        0xFE,
        (
            "All right! It's about time to ready up\x01",
            "launch for the factory ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "They're scheduled to go to Leiston\x01",
            "to swap over the Arseille's engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "The maintenance chief's been over\x01",
            "at the central factory since early\x01",
            "in the morning talking about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1643")

    Jump("loc_16EC")

    label("loc_1646")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_16EC")

    ChrTalk(    #47
        0xFE,
        (
            "Ever since that earthquake,\x01",
            "we've been doubling down on\x01",
            "checking over the facilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Even if there isn't any obvious\x01",
            "damage, we can't get careless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16EC")

    TalkEnd(0x11)
    Return()

    # Function_5_F8D end

    def Function_6_16F0(): pass

    label("Function_6_16F0")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_18CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_179A")

    ChrTalk(    #49
        0xFE,
        (
            "All right! Once I've got a picture of the\x01",
            "Arseille landing, it's on to the capital!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Oh, my beautiful Arseille... I'm coming!\x01",
            "Just you wait!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C7")

    label("loc_179A")


    ChrTalk(    #51
        0xFE,
        (
            "Heehee... I've got a perfect shot\x01",
            "of the factory ship taking off in my\x01",
            "camera! YEEES!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Ahhh... This photographic pilgrimage\x01",
            "has been overflowing with emotion and\x01",
            "excitement at every turn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Crying, laughing, loving from\x01",
            "afar... It's been a hell of a journey,\x01",
            "that much is for certain. \x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_18C7")

    Jump("loc_1D23")

    label("loc_18CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1A09")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1948")

    ChrTalk(    #54
        0xFE,
        (
            "And now I get to see the factory\x01",
            "ship up close and in person...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "*sniffle* I'm so glad I'm alive...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A06")

    label("loc_1948")


    ChrTalk(    #56
        0xFE,
        (
            "This is the central factory's airship,\x01",
            "Leibnitz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "It's got full sets of equipment for\x01",
            "maintenance, production, and transport\x01",
            "of products.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "It's basically a 'flying factory.'\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1A06")

    Jump("loc_1D23")

    label("loc_1A09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1B5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1AA7")

    ChrTalk(    #59
        0xFE,
        (
            "Oh, my! There it is, right on cue!\x01",
            "That overwhelming need to capture\x01",
            "this sweet moment in time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Camera, camera...\x01",
            "Ah, here we are!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B57")

    label("loc_1AA7")


    ChrTalk(    #61
        0xFE,
        "Oooh, that's it! Look, look, look!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "The factory ship I've dreamed of--\x01",
            "the L-Leibnitz!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "It's increeeeeeedible!\x01",
            "So it's docked underground, is it?\x01",
            "I never knew!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1B57")

    Jump("loc_1D23")

    label("loc_1B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1D23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1BFA")

    ChrTalk(    #64
        0xFE,
        (
            "Now's not the time to be scared\x01",
            "of some measly earthquake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I need to get in position to get\x01",
            "a photo before the next airship\x01",
            "arrives.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D23")

    label("loc_1BFA")


    ChrTalk(    #66
        0xFE,
        (
            "*pant* *pant* I-I'm still feelin'\x01",
            "the shakes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "My heart's about the jump\x01",
            "right out of my chest!\x01",
            "That was waaay too scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "Still, you know what? Now's not\x01",
            "the time to be scared of some\x01",
            "measly earthquake!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "I gotta find a position to take\x01",
            "photos before the next airship\x01",
            "arrives.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1D23")

    TalkEnd(0x12)
    Return()

    # Function_6_16F0 end

    def Function_7_1D27(): pass

    label("Function_7_1D27")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1E37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1DB1")

    ChrTalk(    #70
        0xFE,
        "I'm getting nervous...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "We're going to the same place,\x01",
            "so it reminds me of the plan to rescue\x01",
            "the professor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E37")

    label("loc_1DB1")


    ChrTalk(    #72
        0xFE,
        (
            "We're readying the factory\x01",
            "ship to launch right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "It's the first big job in a while,\x01",
            "so I'm getting a little nervous.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1E37")

    TalkEnd(0x13)
    Return()

    # Function_7_1D27 end

    def Function_8_1E3B(): pass

    label("Function_8_1E3B")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_203F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F97")

    ChrTalk(    #74
        0xFE,
        (
            "Lately, there have been a lot of\x01",
            "inquiries related to airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "There have especially been a lot of inquiries\x01",
            "from the Empire and Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "To have this phenomenon happen right after\x01",
            "we were so happy landing that big contract...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "*sigh* So this is what they mean to\x01",
            "have everything go up in smoke, huh...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_203C")

    label("loc_1F97")


    ChrTalk(    #78
        0xFE,
        (
            "Lately, there have been a lot of\x01",
            "inquiries related to airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "With the wave of rising expectations, the shock\x01",
            "when we get blown back is that much worse.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_203C")

    Jump("loc_22A8")

    label("loc_203F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2184")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_210A")

    ChrTalk(    #80
        0xFE,
        (
            "Apparently, right now all orbal\x01",
            "devices aren't operating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "I didn't think I'd see the\x01",
            "day airships couldn't fly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "As someone in that business,\x01",
            "there's no greater shock.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2181")

    label("loc_210A")


    ChrTalk(    #83
        0xFE,
        (
            "Apparently, right now all orbal\x01",
            "devices aren't operating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "I-It isn't going to stay like\x01",
            "this forever, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2181")

    Jump("loc_22A8")

    label("loc_2184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_22A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_21EC")

    ChrTalk(    #85
        0xFE,
        "Today there's no wind, and the weather's good.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        "The perfect day for a flight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A8")

    label("loc_21EC")


    ChrTalk(    #87
        0xFE,
        "Oh, are you also waiting for the Cecilia?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "I'm off on a bit of business to the capital.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Well, it'll be a short journey,\x01",
            "but I hope we'll both have the\x01",
            "chance to enjoy it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_22A8")

    TalkEnd(0x14)
    Return()

    # Function_8_1E3B end

    def Function_9_22AC(): pass

    label("Function_9_22AC")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_239F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_239B")

    ChrTalk(    #90
        0xFE,
        (
            "Goodness, it's just one thing after another.\x01",
            "First the earthquake, now an abnormality\x01",
            "at the hot springs, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "It seems like they might be related,\x01",
            "but I don't have time to check it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "Awwwww, too bad.\x02",
    )

    CloseMessageWindow()
    Jump("loc_239F")

    label("loc_239B")

    Call(0, 11)

    label("loc_239F")

    TalkEnd(0x15)
    Return()

    # Function_9_22AC end

    def Function_10_23A3(): pass

    label("Function_10_23A3")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2441")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_243D")

    ChrTalk(    #93
        0xFE,
        (
            "It seems that the water source in\x01",
            "the mountain's the cause.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "When we get back to the editorial office,\x01",
            "we'll check that out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2441")

    label("loc_243D")

    Call(0, 11)

    label("loc_2441")

    TalkEnd(0x16)
    Return()

    # Function_10_23A3 end

    def Function_11_2445(): pass

    label("Function_11_2445")

    OP_4A(0x15, 255)
    OP_4A(0x16, 255)

    ChrTalk(    #95
        0x15,
        "Faults, did you get the details on Elmo?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x15,
        (
            "I bet you just spent all your\x01",
            "time enjoying the baths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x16,
        "No, no way. It was crazy. Seriously.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x16,
        (
            "Of all things, the hot springs've\x01",
            "suddenly started BOILING...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x15,
        "The hot springs are boiling... Is that true?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x16,
        (
            "Yeah. For now at least I've got\x01",
            "an early scoop put together.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x16,
        (
            "I didn't have much time, though, so it's\x01",
            "not much more than an outline yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x15,
        "All right, well done, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x15,
        "Let's hurry up and turn it into a full article.\x02",
    )

    CloseMessageWindow()
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    OP_A2(0x6)
    OP_A2(0x7)
    Return()

    # Function_11_2445 end

    def Function_12_264F(): pass

    label("Function_12_264F")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_278F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2731")

    ChrTalk(    #104
        0xFE,
        (
            "Anyway, the last thing I want\x01",
            "is to forget something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "This time we'll be doing the work\x01",
            "at Leiston Fortress, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Even if we did forget something,\x01",
            "we won't be able to come back for\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_278F")

    label("loc_2731")


    ChrTalk(    #107
        0xFE,
        "Is the XG-02 loaded safe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Make sure you don't forget\x01",
            "to bring the related parts.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_278F")

    TalkEnd(0x17)
    Return()

    # Function_12_264F end

    def Function_13_2793(): pass

    label("Function_13_2793")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2EBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_28E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2855")

    ChrTalk(    #109
        0x18,
        (
            "#691FSeems like you managed to get\x01",
            "the pump working, huh.\x02\x03",

            "If I could, I'd love to go to Elmo\x01",
            "and have a nice, long soak.\x02\x03",

            "Well, that'll be for another time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_28DD")

    label("loc_2855")


    ChrTalk(    #110
        0x18,
        (
            "#690FOh, man, the ship is right there,\x01",
            "but...\x02\x03",

            "I wonder if we can't figure out a way to board\x01",
            "and at least pull off the equipment.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DD")

    Jump("loc_2EB8")

    label("loc_28E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_END)), "loc_2A1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29C7")

    ChrTalk(    #111
        0x18,
        "#691FHey, find what you were looking for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#1001FYeah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x102,
        "#1040FIt wasn't exactly straightforward, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x18,
        (
            "#691FWell, however it went, I'm glad you found it.\x02\x03",

            "Good luck fixing the pump.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_2A1B")

    label("loc_29C7")


    ChrTalk(    #115
        0x18,
        (
            "#691FWell, however it went, I'm glad you found it.\x02\x03",

            "Good luck fixing the pump.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A1B")

    Jump("loc_2EB8")

    label("loc_2A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_END)), "loc_2A95")

    ChrTalk(    #116
        0x18,
        (
            "#691FThe combustion engine should be\x01",
            "stored in Leiston Fortress.\x02\x03",

            "Sorry, but you mind asking with them?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB8")

    label("loc_2A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AA8")
    Call(0, 43)
    Jump("loc_2EB8")

    label("loc_2AA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_2B28")

    ChrTalk(    #117
        0x18,
        (
            "#691FAt this rate, who knows what's gonna\x01",
            "happen next.\x02\x03",

            "I'm sure we'll need your help,\x01",
            "so we're counting on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EB8")

    label("loc_2B28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E28")
    OP_A2(0x2084)
    OP_A2(0x9)

    ChrTalk(    #118
        0x18,
        "#692FOh, hey, if it isn't the gang!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x101,
        "#1000FHey, Gustav, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x102,
        "#1040FI hope you've been doing well.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x102, 400)

    ChrTalk(    #121
        0x18,
        (
            "#691FOh, it's Joshua.\x02\x03",

            "Haven't seen you in a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1016FWell, a lot happened...\x02\x03",

            "#1000FAnyway, it seems like things are\x01",
            "pretty tough here even now, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CAC")

    ChrTalk(    #123
        0x107,
        "#063FI-It seems like there was some kinda trouble...\x02",
    )

    CloseMessageWindow()

    label("loc_2CAC")

    TurnDirection(0x18, 0x101, 400)

    ChrTalk(    #124
        0x18,
        (
            "#690FWhen the shutdown first hit, yeah.\x01",
            "It was real rough.\x02\x03",

            "Well, the city's finally calmed down now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x102,
        (
            "#1040FI see...\x02\x03",

            "For now, at least, it seems\x01",
            "things are in hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x18,
        (
            "#691FYeah, but at this rate, who\x01",
            "knows what might happen.\x02\x03",

            "#693FI'm sure we'll need your help,\x01",
            "so we're counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#1001FSure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x102,
        "#1040FLooking forward to being of help.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EB8")

    label("loc_2E28")


    ChrTalk(    #129
        0x18,
        (
            "#690FThe port here's a bit of a special construction,\x01",
            "after all.\x02\x03",

            "If orbal power doesn't come back,\x01",
            "we won't be able to work on the ships.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EB8")

    Jump("loc_3374")

    label("loc_2EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 3)), scpexpr(EXPR_END)), "loc_3085")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_301E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_301B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2F5A")

    ChrTalk(    #130
        0x18,
        (
            "#690FApparently there was an earthquake\x01",
            "at Leiston Fortress too.\x02\x03",

            "I hope there wasn't any damage\x01",
            "to the facilities there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_301B")

    label("loc_2F5A")


    ChrTalk(    #131
        0x18,
        (
            "#690FJust a bit ago, we got a message from\x01",
            "the central factory.\x02\x03",

            "Apparently there was an earthquake\x01",
            "at Leiston Fortress.\x02\x03",

            "Man, I hope this doesn't make\x01",
            "the work on the Arseille harder.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_301B")

    Jump("loc_3082")

    label("loc_301E")


    ChrTalk(    #132
        0x18,
        (
            "#690FElmo Village's water source...\x01",
            "Well, that's a bit creepy.\x02\x03",

            "You guys be careful as you go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3082")

    Jump("loc_3374")

    label("loc_3085")


    ChrTalk(    #133
        0x101,
        "#1004FAh, Gustav!\x02",
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x18)
    TurnDirection(0x18, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3101")

    ChrTalk(    #134
        0x18,
        (
            "#691FWell, if it ain't you kids!\x02\x03",

            "It's been a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313A")

    label("loc_3101")


    ChrTalk(    #135
        0x18,
        (
            "#691FWell, if it ain't Estelle!\x02\x03",

            "It's been a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_313A")


    ChrTalk(    #136
        0x101,
        "#1006FYeah, it has. Glad to see you're well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x18,
        (
            "#691FApparently you're investigating the\x01",
            "earthquakes, huh.\x02\x03",

            "Got any clues yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#1015FEr, actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #139
        (
            "\x07\x05Estelle explained that the source of the earthquakes\x01",
            "was Elmo Village.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #140
        0x18,
        (
            "#692FThat sure is creepy.\x02\x03",

            "If you're gonna go investigate,\x01",
            "shouldn't ya hurry?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_32C0")

    ChrTalk(    #141
        0x106,
        "#050FYeah, I agree...\x02",
    )

    CloseMessageWindow()
    Jump("loc_32DA")

    label("loc_32C0")


    ChrTalk(    #142
        0x103,
        "#026FYes, I agree...\x02",
    )

    CloseMessageWindow()

    label("loc_32DA")


    ChrTalk(    #143
        0x101,
        (
            "#1002FYeah, we probably should hurry.\x02\x03",

            "Well, then...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x107, 400)

    ChrTalk(    #144
        0x18,
        (
            "#691FYeah, good luck.\x02\x03",

            "#691FTita, you take care, kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x107,
        "#560FAh, yes!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1483)
    OP_A2(0x9)
    ClearChrFlags(0x18, 0x10)

    label("loc_3374")

    TalkEnd(0x18)
    Return()

    # Function_13_2793 end

    def Function_14_3378(): pass

    label("Function_14_3378")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_33F8")

    ChrTalk(    #146
        0xFE,
        (
            "It's been a while since I rode a scheduled\x01",
            "liner, so I'm looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "Oooh, I hope it comes soon!\x02",
    )

    CloseMessageWindow()

    label("loc_33F8")

    TalkEnd(0x19)
    Return()

    # Function_14_3378 end

    def Function_15_33FC(): pass

    label("Function_15_33FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_340D")
    Call(0, 44)

    label("loc_340D")

    EventBegin(0x0)
    OP_DB()
    ClearMapFlags(0x1)
    ClearMapFlags(0x10)
    OP_6D(-33680, -4000, 150830, 0)
    OP_67(0, 14240, -10000, 0)
    OP_6B(8800, 0)
    OP_6C(44000, 0)
    OP_6E(175, 0)
    OP_A1(0x1A, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x4, 0x20)
    SetChrPos(0x1A, -34000, -150, 148000, 0)
    SetChrFlags(0x1A, 0x4)
    OP_A1(0x1B, 0x5)
    OP_72(0x5, 0x4)
    OP_72(0xA, 0x4)
    SetChrPos(0x1B, -34000, -10150, 148000, 0)
    SetChrFlags(0x1B, 0x4)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x6, 0x4)
    OP_6F(0x3, 100)
    OP_6F(0x4, 60)
    OP_6F(0x5, 0)
    OP_C8(0x200, 0x46, "C_PLAC08._CH", 0x0, 0x5DC)
    OP_DE("Zeiss")
    FadeToBright(1500, 0)

    def lambda_34EB():
        OP_6C(57000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34EB)

    def lambda_34FB():
        OP_6B(6800, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_34FB)
    Call(0, 16)
    Fade(1000)
    OP_6D(-46650, -4000, 144430, 0)
    OP_67(0, 11610, -10000, 0)
    OP_6B(4120, 0)
    OP_6C(314000, 0)
    OP_6E(175, 0)
    OP_6F(0x3, 200)
    OP_6F(0x4, 1)
    OP_6F(0x5, 0)
    OP_0D()
    OP_43(0x8, 0x1, 0x0, 0x11)
    Sleep(500)
    OP_43(0x9, 0x1, 0x0, 0x11)
    Sleep(1000)
    OP_43(0xE, 0x1, 0x0, 0x11)
    Sleep(1000)
    OP_43(0xB, 0x1, 0x0, 0x13)
    Sleep(500)
    OP_43(0xA, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0x14)
    Sleep(1000)
    OP_43(0xD, 0x1, 0x0, 0x15)
    Sleep(500)
    OP_43(0xF, 0x1, 0x0, 0x16)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x0, 0x18)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x19)
    Sleep(500)
    OP_43(0x105, 0x1, 0x0, 0x1A)
    Sleep(500)
    OP_43(0x104, 0x1, 0x0, 0x1B)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x104, 0x1)
    OP_DC()

    ChrTalk(    #148
        0x101,
        (
            "#1006F#3POkay, first stop for us should be\x01",
            "the guildhouse here in Zeiss.\x02\x03",

            "We need to check in with Kilika.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x104,
        (
            "#033F'Kilika'? A rather exotic name for Liberl.\x01",
            "It sounds Eastern.\x02\x03",

            "#031FWhat kind of woman is she, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1007F#3PYou never give up, do you...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3832")

    ChrTalk(    #151
        0x106,
        (
            "#051F#6PLet's just say she isn't your average woman.\x02\x03",

            "She's bolder than Scherazard, as capable of\x01",
            "running a guildhouse as the queen herself,\x01",
            "and she's a master of Eastern martial arts.\x02\x03",

            "#551FIn fact...word of advice? Don't even try unless\x01",
            "you want her to rearrange your face.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3927")

    label("loc_3832")


    ChrTalk(    #152
        0x103,
        (
            "#027F#6PTo put it simply: capable.\x02\x03",

            "She is a flawless administrator, and she's\x01",
            "also a very accomplished martial artist.\x02\x03",

            "#021FShe's also quite lovely, but she doesn't\x01",
            "have time for...ah, 'frippery.' I would\x01",
            "advise caution, my dear Lenheim.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3927")


    ChrTalk(    #153
        0x104,
        (
            "#031FHeh. Now my interest is\x01",
            "positively piqued.\x02\x03",

            "What are we waiting for, then?\x01",
            "Let us away to--\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x85, 0x0, 0x64)
    OP_20(0x5DC)

    def lambda_399D():

        label("loc_399D")

        OP_7C(0xC8, 0x0, 0x7D0, 0xBB8)
        OP_48()
        Jump("loc_399D")

    QueueWorkItem2(0x101, 3, lambda_399D)
    Sleep(500)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_A3(0x0)
    OP_43(0xA, 0x1, 0x0, 0x1D)
    Sleep(200)
    OP_43(0xB, 0x1, 0x0, 0x1F)
    Sleep(200)
    OP_43(0xC, 0x1, 0x0, 0x20)
    Sleep(200)
    OP_43(0xD, 0x1, 0x0, 0x21)
    Sleep(200)
    OP_43(0xF, 0x1, 0x0, 0x22)
    OP_8C(0x104, 140, 400)
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #154
        0x104,
        (
            "#036F#5PWaaaah...!\x02\x03",

            "I-Is this the fury of Kilika?!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 140, 400)

    ChrTalk(    #155
        0x101,
        "#1019F#6PWould you give it a rest already?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 90, 400)

    ChrTalk(    #156
        0x105,
        "#043FIt's...an earthquake?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xC,
        "#5PAaaah! Heeeeeelp!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 184, 400)
    OP_8C(0xF7, 65, 400)

    ChrTalk(    #158
        0xF,
        (
            "#2PThe dock is going to collapse!\x01",
            "RUN FOR YOUR LIVES!\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x10, 255)
    SetChrPos(0x10, -45950, 0, 128050, 0)

    ChrTalk(    #159
        0x10,
        "#2PE-Everyone! PLEASE CALM DOWN!\x02",
    )

    CloseMessageWindow()

    def lambda_3B62():
        OP_6D(-46130, -4000, 138120, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3B62)

    def lambda_3B7A():
        OP_67(0, 11000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3B7A)

    def lambda_3B92():
        OP_6B(4480, 3000)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3B92)

    def lambda_3BA2():
        OP_6C(230000, 3000)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3BA2)
    OP_8E(0x10, 0xFFFF4BF6, 0xFFFFF34E, 0x213A4, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x1)

    def lambda_3BCB():
        OP_8C(0xFE, 184, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3BCB)
    Sleep(100)

    def lambda_3BDE():
        OP_8C(0xFE, 184, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3BDE)

    def lambda_3BEC():
        OP_8C(0xFE, 184, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3BEC)
    WaitChrThread(0x104, 0x1)

    ChrTalk(    #160
        0x10,
        (
            "#6PThe port is designed to endure\x01",
            "high-magnitude earthquakes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x10,
        (
            "#6PIt can easily handle one this\x01",
            "small! Please, don't panic!\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x85, 0x5A)
    OP_44(0x101, 0x3)

    def lambda_3C8C():

        label("loc_3C8C")

        OP_7C(0x64, 0x0, 0x3E8, 0x3E8)
        OP_48()
        Jump("loc_3C8C")

    QueueWorkItem2(0x101, 3, lambda_3C8C)
    Sleep(500)
    OP_24(0x85, 0x4B)
    Sleep(500)
    OP_A2(0x0)
    OP_24(0x85, 0x3C)
    OP_44(0x101, 0x3)

    def lambda_3CC0():

        label("loc_3CC0")

        OP_7C(0x32, 0x0, 0x1F4, 0x3E8)
        OP_48()
        Jump("loc_3CC0")

    QueueWorkItem2(0x101, 3, lambda_3CC0)
    Sleep(500)
    OP_44(0xC, 0x1)
    OP_4A(0xC, 255)
    OP_24(0x85, 0x32)
    Sleep(500)

    def lambda_3CF1():
        TurnDirection(0xFE, 0x10, 200)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3CF1)
    OP_24(0x85, 0x28)
    OP_44(0x101, 0x3)

    def lambda_3D07():

        label("loc_3D07")

        OP_7C(0x19, 0x0, 0xFA, 0x3E8)
        OP_48()
        Jump("loc_3D07")

    QueueWorkItem2(0x101, 3, lambda_3D07)
    Sleep(500)
    OP_44(0xA, 0x1)
    OP_4A(0xA, 255)
    OP_24(0x85, 0x1E)
    Sleep(500)

    def lambda_3D38():
        TurnDirection(0xFE, 0x10, 200)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3D38)
    OP_24(0x85, 0x14)
    OP_44(0x101, 0x3)

    def lambda_3D4E():

        label("loc_3D4E")

        OP_7C(0xC, 0x0, 0x7D, 0x3E8)
        OP_48()
        Jump("loc_3D4E")

    QueueWorkItem2(0x101, 3, lambda_3D4E)
    Sleep(500)
    OP_44(0xB, 0x1)
    OP_4A(0xB, 255)
    OP_24(0x85, 0xA)
    Sleep(500)

    def lambda_3D7F():
        TurnDirection(0xFE, 0x10, 200)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3D7F)
    OP_23(0x85)
    OP_44(0x101, 0x3)
    Sleep(500)
    OP_44(0xD, 0x1)
    OP_4A(0xD, 255)

    def lambda_3DA1():
        TurnDirection(0xFE, 0x10, 200)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3DA1)
    Sleep(500)
    OP_44(0xF, 0x1)
    OP_4A(0xF, 255)

    def lambda_3DBC():
        TurnDirection(0xFE, 0x10, 200)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3DBC)
    Sleep(1000)

    ChrTalk(    #162
        0x101,
        "#1025F#2PI-It stopped...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10,
        "#6PPhew! Thank Aidios that's over...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x10,
        (
            "#6PEveryone, please come to reception in\x01",
            "an orderly fashion. Let's not panic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xD,
        (
            "Hoooo, man... It's been a while\x01",
            "since I was in an earthquake.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xC, 400)
    TurnDirection(0xC, 0xA, 400)

    ChrTalk(    #166
        0xA,
        "#5PHeeeeee, that was SO COOL!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0x10, 180, 400)

    def lambda_3EEA():
        OP_8E(0xFE, 0xFFFF4C6E, 0x0, 0x1EE88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3EEA)
    Sleep(400)
    OP_8C(0xB, 180, 400)

    def lambda_3F11():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3F11)
    Sleep(100)
    OP_8C(0xA, 180, 400)

    def lambda_3F38():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3F38)
    Sleep(200)
    OP_8C(0xC, 180, 400)

    def lambda_3F5F():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3F5F)
    Sleep(200)
    OP_8C(0xD, 180, 400)

    def lambda_3F86():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3F86)
    Sleep(200)
    OP_8C(0xF, 180, 400)

    def lambda_3FAD():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3FAD)
    Sleep(1500)

    def lambda_3FCD():
        OP_6D(-46690, -4000, 143590, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3FCD)

    def lambda_3FE5():
        OP_67(0, 11000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FE5)
    OP_8C(0x101, 45, 400)
    OP_8C(0xF7, 135, 400)
    OP_8C(0x105, 225, 400)
    OP_8C(0x104, 0, 400)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xF, 0x80)

    ChrTalk(    #167
        0x101,
        (
            "#1007FWell, that was a great way of\x01",
            "getting welcomed to Zeiss.\x02\x03",

            "#1019FIt wasn't very strong, but attention, world:\x01",
            "please wait until I'm not on scaffolding\x01",
            "before you shake again. Love, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x105,
        (
            "#045FHaha! I'll sign that letter, too.\x02\x03",

            "#043FIt's rare for us to get an earthquake\x01",
            "in Liberl, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x104,
        "#033F#6PReally? Hmm.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4213")

    ChrTalk(    #170
        0x106,
        (
            "#053F#4PYeah. Hell, I can't remember\x01",
            "the last time I felt one.\x02\x03",

            "#050FLet's get to the guildhouse,\x01",
            "see what the damage is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42A7")

    label("loc_4213")


    ChrTalk(    #171
        0x103,
        (
            "#026F#4PKloe is right. Earthquakes are\x01",
            "very unusual here.\x02\x03",

            "#022FNow we really do need to check in at the\x01",
            "guildhouse to see what the damage is.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42A7")

    OP_4B(0x10, 255)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T3120   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_33FC end

    def Function_16_42C8(): pass

    label("Function_16_42C8")


    def lambda_42CE():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_42CE)

    def lambda_42E9():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFE412, 0x24220, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_42E9)
    WaitChrThread(0x1A, 0x1)

    def lambda_4309():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD85A, 0x24220, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4309)
    WaitChrThread(0x1A, 0x1)

    def lambda_4329():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4329)
    WaitChrThread(0x1A, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x1A, -34000, -11150, 148000, 0)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x1)
    Sleep(1100)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 100)
    OP_70(0x3, 0xC8)
    Sleep(2500)
    OP_6F(0x4, 410)
    OP_70(0x4, 0x1CC)
    OP_22(0x6, 0x0, 0x64)
    Sleep(800)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x4)
    OP_44(0x0, 0x1)
    Return()

    # Function_16_42C8 end

    def Function_17_43C7(): pass

    label("Function_17_43C7")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4CBE, 0x0, 0x1F4A0, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_43C7 end

    def Function_18_440B(): pass

    label("Function_18_440B")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF46F6, 0xFFFFF060, 0x22024, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_18_440B end

    def Function_19_4458(): pass

    label("Function_19_4458")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF49F8, 0xFFFFF060, 0x21C5A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_19_4458 end

    def Function_20_44AA(): pass

    label("Function_20_44AA")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4A70, 0xFFFFF060, 0x220EC, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_20_44AA end

    def Function_21_44FC(): pass

    label("Function_21_44FC")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4D72, 0xFFFFF060, 0x228F8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4F66, 0xFFFFF060, 0x222E0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_21_44FC end

    def Function_22_4562(): pass

    label("Function_22_4562")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4D72, 0xFFFFF060, 0x228F8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4FA2, 0xFFFFF060, 0x226C8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_43(0xFE, 0x3, 0x0, 0x2)
    Return()

    # Function_22_4562 end

    def Function_23_45C8(): pass

    label("Function_23_45C8")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    Return()

    # Function_23_45C8 end

    def Function_24_45F3(): pass

    label("Function_24_45F3")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0x101, 0xFFFF482C, 0xFFFFF060, 0x23104, 0x7D0, 0x0)
    OP_8C(0x101, 90, 400)
    Return()

    # Function_24_45F3 end

    def Function_25_4639(): pass

    label("Function_25_4639")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0xF7, 0xFFFF48E0, 0xFFFFF060, 0x2353C, 0x7D0, 0x0)
    OP_8C(0xF7, 135, 400)
    Return()

    # Function_25_4639 end

    def Function_26_467F(): pass

    label("Function_26_467F")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0x105, 0xFFFF4D7C, 0xFFFFF060, 0x23410, 0x7D0, 0x0)
    OP_8C(0x105, 270, 400)
    Return()

    # Function_26_467F end

    def Function_27_46C5(): pass

    label("Function_27_46C5")

    SetChrPos(0xFE, -37500, -4000, 143810, 270)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4CBE, 0xFFFFF060, 0x231C2, 0x7D0, 0x0)
    OP_8E(0x104, 0xFFFF4CB4, 0xFFFFF060, 0x22F92, 0x7D0, 0x0)
    OP_8C(0x104, 315, 400)
    Return()

    # Function_27_46C5 end

    def Function_28_470B(): pass

    label("Function_28_470B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4784")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4759")
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xFA0, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    Jump("loc_4781")

    label("loc_4759")

    OP_90(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)

    label("loc_4781")

    Jump("Function_28_470B")

    label("loc_4784")

    Return()

    # Function_28_470B end

    def Function_29_4785(): pass

    label("Function_29_4785")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47FE")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47D3")
    OP_90(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xFA0, 0x0)
    Jump("loc_47FB")

    label("loc_47D3")

    OP_90(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)

    label("loc_47FB")

    Jump("Function_29_4785")

    label("loc_47FE")

    Return()

    # Function_29_4785 end

    def Function_30_47FF(): pass

    label("Function_30_47FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4878")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_484D")
    OP_90(0xFE, 0x5DC, 0x0, 0x5DC, 0xFA0, 0x0)
    OP_90(0xFE, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0xFA0, 0x0)
    Jump("loc_4875")

    label("loc_484D")

    OP_90(0xFE, 0x5DC, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_90(0xFE, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x7D0, 0x0)

    label("loc_4875")

    Jump("Function_30_47FF")

    label("loc_4878")

    Return()

    # Function_30_47FF end

    def Function_31_4879(): pass

    label("Function_31_4879")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48C1")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 315, 400)
    Sleep(300)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 0, 400)
    Sleep(300)
    Jump("Function_31_4879")

    label("loc_48C1")

    Return()

    # Function_31_4879 end

    def Function_32_48C2(): pass

    label("Function_32_48C2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_493B")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4910")
    OP_90(0xFE, 0x0, 0x0, 0x5DC, 0xFA0, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFA24, 0xFA0, 0x0)
    Jump("loc_4938")

    label("loc_4910")

    OP_90(0xFE, 0x0, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_90(0xFE, 0x0, 0x0, 0xFFFFFA24, 0x7D0, 0x0)

    label("loc_4938")

    Jump("Function_32_48C2")

    label("loc_493B")

    Return()

    # Function_32_48C2 end

    def Function_33_493C(): pass

    label("Function_33_493C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4976")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 90, 400)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 180, 400)
    Jump("Function_33_493C")

    label("loc_4976")

    Return()

    # Function_33_493C end

    def Function_34_4977(): pass

    label("Function_34_4977")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49B1")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xFE, 180, 400)
    OP_8C(0xFE, 270, 400)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 90, 400)
    Jump("Function_34_4977")

    label("loc_49B1")

    Return()

    # Function_34_4977 end

    def Function_35_49B2(): pass

    label("Function_35_49B2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49D2")
    Call(0, 44)
    Call(0, 45)
    FadeToBright(0, 0)

    label("loc_49D2")

    Fade(1000)
    SetChrPos(0x101, -19580, 8000, 119820, 0)
    SetChrPos(0xF7, -20630, 8000, 119820, 0)
    SetChrPos(0xF8, -19710, 8000, 118700, 0)
    SetChrPos(0xF9, -20720, 8000, 118640, 0)
    OP_6D(-20180, 8000, 120530, 0)
    OP_67(0, 8780, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(315000, 0)
    OP_6E(194, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FCB")
    OP_A2(0x1601)

    ChrTalk(    #172
        0x10,
        "Hey, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x10,
        (
            "You're the party of bracers bound\x01",
            "for Grancel, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        "#1011FYeah, that's us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x10,
        (
            "Kilika sent over the fare\x01",
            "payment already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x10,
        "You guys ready to check in?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4BAB")

    ChrTalk(    #177
        0x106,
        (
            "#050FAs usual, we should stick around and\x01",
            "wait for the ship once we check in.\x02\x03",

            "You sure we're all done here in Zeiss?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C47")

    label("loc_4BAB")


    ChrTalk(    #178
        0x103,
        (
            "#020FJust like last time, it would probably\x01",
            "be best if we stay here and wait for\x01",
            "the ship once we check in.\x02\x03",

            "Are you certain we're done here in Zeiss?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF2")

    ChrTalk(    #179
        0x101,
        (
            "#1015FOh, wait.\x02\x03",

            "We need to return this something-or-other\x01",
            "detector thingy.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CEE")

    ChrTalk(    #180
        0x107,
        "#560FYeah, the alloy detector!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)
    Jump("loc_4D6A")

    label("loc_4CEE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D2E")

    ChrTalk(    #181
        0x104,
        "#030FThe alloy detector, you mean.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    Jump("loc_4D6A")

    label("loc_4D2E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4D6A")

    ChrTalk(    #182
        0x105,
        "#542FYou mean the alloy detector?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    label("loc_4D6A")


    ChrTalk(    #183
        0x101,
        (
            "#1006FYeah, the thingy detector.\x02\x03",

            "We borrowed it at the maintenance desk\x01",
            "on the first floor of the factory, right?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4E30")

    ChrTalk(    #184
        0x106,
        (
            "#051FFactory first floor, maintenance desk.\x02\x03",

            "Let's get moving.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E88")

    label("loc_4E30")


    ChrTalk(    #185
        0x103,
        (
            "#020FFactory first floor, maintenance desk.\x02\x03",

            "Let's go take care of that right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E88")


    ChrTalk(    #186
        0x10,
        (
            "Well, once you're done with\x01",
            "that, just say the word!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_67(0, 11000, -10000, 0)
    OP_6B(3500, 0)
    OP_6E(262, 0)
    EventEnd(0x0)
    Return()

    label("loc_4EF2")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Still Have Stuff To Do\x01",      # 0
            "Check In\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FC8")

    ChrTalk(    #187
        0x10,
        (
            "Well, once you're done with your\x01",
            "business, just say the word!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6B(3500, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6E(262, 0)
    EventEnd(0x0)
    Return()

    label("loc_4FC8")

    Jump("loc_51A4")

    label("loc_4FCB")


    ChrTalk(    #188
        0x10,
        "Hey! Ready to check in?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50CE")

    ChrTalk(    #189
        0x101,
        (
            "#1015FAck, I keep forgetting...\x02\x03",

            "We still need to return the detector\x01",
            "thingy to the factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x10,
        (
            "Well, once you're done with\x01",
            "that, just say the word!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6B(3500, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6E(262, 0)
    EventEnd(0x0)
    Return()

    label("loc_50CE")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Still Have Stuff To Do\x01",      # 0
            "Check In\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51A4")

    ChrTalk(    #191
        0x10,
        (
            "Well, once you're done with your\x01",
            "business, just say the word!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6B(3500, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6E(262, 0)
    EventEnd(0x0)
    Return()

    label("loc_51A4")


    ChrTalk(    #192
        0x10,
        "All right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x10,
        (
            "I'll contact the guild and let 'em\x01",
            "know to send the rest of your party.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #194
        (
            "\x07\x05Estelle's group checked in and waited for the\x01",
            "next passenger ship.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x19, 0x80)
    Call(0, 36)
    Return()

    # Function_35_49B2 end

    def Function_36_52AF(): pass

    label("Function_36_52AF")

    EventBegin(0x0)
    OP_DB()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52D7")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_52D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5301")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52FD")
    AddParty(0x4, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5301")

    label("loc_52FD")

    AddParty(0x4, 0xFB, 0xFF)

    label("loc_5301")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_532B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5327")
    AddParty(0x6, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_532B")

    label("loc_5327")

    AddParty(0x6, 0xFB, 0xFF)

    label("loc_532B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5355")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5351")
    AddParty(0x7, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5355")

    label("loc_5351")

    AddParty(0x7, 0xFB, 0xFF)

    label("loc_5355")

    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_6F(0x4, 100)
    OP_6F(0x3, 100)
    SetChrPos(0x101, -46010, -4000, 151140, 14)
    SetChrPos(0xF7, -47050, -4000, 152510, 87)
    SetChrPos(0x107, -47040, -4000, 153400, 87)
    SetChrPos(0x105, -45400, -4000, 151930, 267)
    SetChrPos(0x104, -45280, -4000, 153160, 267)
    SetChrPos(0x108, -46100, -4000, 154080, 177)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x8, -46990, -4000, 147520, 177)
    SetChrPos(0x9, -46840, -4000, 144960, 357)
    SetChrPos(0xA, -46720, -4000, 146170, 87)
    SetChrPos(0xB, -46700, -4000, 148750, 177)
    SetChrPos(0xC, -46590, -4000, 149930, 177)
    SetChrPos(0xD, -45070, -3800, 144000, 87)
    SetChrPos(0xE, -46280, -4000, 143940, 87)
    OP_6D(-42120, -4000, 150190, 0)
    OP_67(0, 8330, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(62000, 0)
    OP_6E(331, 0)
    SetChrPos(0x1A, -34000, -11150, 148000, 0)
    OP_A1(0x1A, 0x4)
    OP_72(0x4, 0x4)
    SetChrFlags(0x1A, 0x4)
    OP_A1(0x1B, 0x5)
    SetChrPos(0x1B, -34000, -11150, 148000, 0)
    OP_72(0x5, 0x4)
    SetChrFlags(0x1B, 0x4)
    OP_6F(0x4, 60)
    OP_71(0x6, 0x4)
    OP_22(0xE2, 0x0, 0x64)
    OP_22(0x75, 0x0, 0x64)
    Sleep(3000)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x1)
    Sleep(1100)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 100)
    OP_70(0x3, 0xC8)
    Sleep(2500)
    OP_43(0xD, 0x1, 0x0, 0x25)
    Sleep(500)
    OP_43(0xE, 0x1, 0x0, 0x26)
    Sleep(800)
    OP_43(0x9, 0x1, 0x0, 0x27)
    OP_43(0xA, 0x1, 0x0, 0x27)
    Sleep(600)
    OP_43(0x8, 0x1, 0x0, 0x28)
    Sleep(500)
    OP_43(0xB, 0x1, 0x0, 0x29)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0x28)
    Sleep(600)
    OP_8C(0x101, 225, 400)
    OP_43(0x101, 0x1, 0x0, 0x2A)
    Sleep(300)
    OP_8C(0xF7, 180, 400)
    OP_43(0xF7, 0x1, 0x0, 0x2A)
    Sleep(300)
    OP_8C(0x107, 180, 400)
    OP_43(0x107, 0x1, 0x0, 0x2A)
    Sleep(300)
    OP_8C(0x105, 225, 400)
    Sleep(1200)
    OP_43(0x105, 0x1, 0x0, 0x2A)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_43(0x104, 0x1, 0x0, 0x2A)
    Sleep(500)
    OP_43(0x108, 0x1, 0x0, 0x2A)
    Sleep(1000)
    OP_0D()
    OP_6D(-33540, -6900, 151660, 0)
    OP_67(0, 600, -10000, 0)
    OP_6B(4360, 0)
    OP_6C(169000, 0)
    OP_6E(425, 0)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0xFA, 0x1)
    OP_44(0xFB, 0x1)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Sleep(1000)
    OP_22(0xE2, 0x0, 0x64)
    Sleep(1000)

    def lambda_56DF():
        OP_67(0, 3030, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56DF)
    FadeToBright(2000, 0)
    OP_0D()
    Fade(500)
    OP_72(0x6, 0x4)
    OP_0D()
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x64)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0x4, 1)
    OP_70(0x4, 0x3C)
    OP_73(0x4)
    Sleep(1000)
    OP_22(0x77, 0x1, 0x64)
    OP_6F(0x4, 61)
    OP_70(0x4, 0xA0)
    OP_73(0x4)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 161)
    OP_70(0x4, 0x104)
    OP_23(0x75)
    OP_91(0x1A, 0x0, 0x12C, 0x0, 0x12C, 0x0)
    OP_91(0x1A, 0x0, 0x320, 0x0, 0x1F4, 0x0)
    Sleep(2000)

    def lambda_5798():
        OP_6D(-33490, -6100, 161910, 6000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5798)

    def lambda_57B0():
        OP_67(0, 3180, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_57B0)

    def lambda_57C8():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_57C8)
    OP_94(0x1, 0x1A, 0x0, 0x3E8, 0x3E8, 0x0)

    def lambda_57ED():
        OP_94(0x1, 0xFE, 0x0, 0x4B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_57ED)
    OP_94(0x1, 0x1A, 0x0, 0x4B0, 0x7D0, 0x0)

    def lambda_5812():
        OP_94(0x1, 0xFE, 0x0, 0x578, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5812)
    OP_94(0x1, 0x1A, 0x0, 0x578, 0xBB8, 0x0)

    def lambda_5837():
        OP_94(0x1, 0xFE, 0x0, 0x640, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_5837)
    OP_94(0x1, 0x1A, 0x0, 0x640, 0xFA0, 0x0)

    def lambda_585C():
        OP_94(0x1, 0xFE, 0x0, 0x708, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_585C)
    FadeToDark(2000, 0, -1)
    OP_94(0x1, 0x1A, 0x0, 0x708, 0x1388, 0x0)

    def lambda_588B():
        OP_94(0x1, 0xFE, 0x0, 0x7D0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_588B)
    OP_94(0x1, 0x1A, 0x0, 0x7D0, 0x1770, 0x0)

    def lambda_58B0():
        OP_94(0x1, 0xFE, 0x0, 0x898, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_58B0)
    OP_94(0x1, 0x1A, 0x0, 0x898, 0x1B58, 0x0)

    def lambda_58D5():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_58D5)

    def lambda_58EB():
        OP_94(0x1, 0xFE, 0x0, 0xC350, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_58EB)
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
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x6, 0xFF)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x7, 0xFF)
    OP_A2(0x1602)
    OP_A2(0x10F2)
    OP_28(0x6C, 0x4, 0x40)
    OP_28(0x6D, 0x4, 0x40)
    OP_28(0x6E, 0x4, 0x40)
    OP_28(0x6F, 0x4, 0x40)
    OP_28(0x70, 0x4, 0x40)
    OP_28(0x71, 0x4, 0x40)
    OP_28(0xA5, 0x4, 0x40)
    OP_28(0xA6, 0x4, 0x40)
    OP_28(0xA7, 0x4, 0x40)
    OP_28(0xA8, 0x4, 0x40)
    OP_DC()
    NewScene("ED6_DT21/E0001   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_36_52AF end

    def Function_37_59A5(): pass

    label("Function_37_59A5")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF7888, 0xFFFFF060, 0x23186, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF85D0, 0xFFFFF060, 0x246A8, 0x7D0, 0x0)
    Return()

    # Function_37_59A5 end

    def Function_38_59D3(): pass

    label("Function_38_59D3")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF8292, 0xFFFFF060, 0x23186, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF85D0, 0xFFFFF060, 0x246A8, 0x7D0, 0x0)
    Return()

    # Function_38_59D3 end

    def Function_39_5A01(): pass

    label("Function_39_5A01")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF4BC4, 0xFFFFF060, 0x232EE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7EAA, 0xFFFFF060, 0x23186, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF85D0, 0xFFFFF060, 0x246A8, 0x7D0, 0x0)
    Return()

    # Function_39_5A01 end

    def Function_40_5A43(): pass

    label("Function_40_5A43")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF491C, 0xFFFFF060, 0x2324E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7E46, 0xFFFFF060, 0x2314A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF85D0, 0xFFFFF060, 0x246A8, 0x7D0, 0x0)
    Return()

    # Function_40_5A43 end

    def Function_41_5A85(): pass

    label("Function_41_5A85")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF491C, 0xFFFFF060, 0x2324E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF7CB6, 0xFFFFF060, 0x2314A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF85D0, 0xFFFFF060, 0x246A8, 0x7D0, 0x0)
    Return()

    # Function_41_5A85 end

    def Function_42_5AC7(): pass

    label("Function_42_5AC7")

    OP_8E(0xFE, 0xFFFF48EA, 0xFFFFF060, 0x24626, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF49A8, 0xFFFFF060, 0x2330C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF793C, 0xFFFFF060, 0x232EE, 0x7D0, 0x0)
    Return()

    # Function_42_5AC7 end

    def Function_43_5B04(): pass

    label("Function_43_5B04")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B24")
    Call(0, 44)
    Call(0, 46)
    FadeToBright(0, 0)

    label("loc_5B24")

    Fade(1000)
    OP_6D(-38930, 8000, 126550, 0)
    OP_67(0, 5300, -10000, 0)
    OP_6B(3750, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -39260, 8000, 127280, 0)
    SetChrPos(0x102, -40320, 8000, 127230, 0)
    SetChrPos(0xF8, -39030, 8000, 126180, 0)
    SetChrPos(0xF9, -40150, 8000, 126180, 0)
    OP_4A(0x18, 255)
    SetChrSubChip(0x18, 0)
    OP_8C(0x18, 180, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x401, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E69")

    ChrTalk(    #195
        0x18,
        "#692F#5POh, hey, if it isn't the gang!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#1025F#4PHey, Gustav, it's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x102,
        "#1040F#4PI hope you've been doing well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x18,
        (
            "#691F#5POh, it's Joshua.\x02\x03",

            "Haven't seen you in a long time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        (
            "#1016F#4PWell, a lot happened...\x02\x03",

            "#1015FAnyway, it seems like things are\x01",
            "pretty tough here even now, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D4E")

    ChrTalk(    #200
        0x107,
        "#063F#4PI-It seems like there was some kinda trouble...\x02",
    )

    CloseMessageWindow()

    label("loc_5D4E")


    ChrTalk(    #201
        0x18,
        (
            "#691F#5PWhen the shutdown first hit, yeah.\x01",
            "It was real rough.\x02\x03",

            "Well, the city's finally calmed down now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x102,
        (
            "#1035F#4PI see...\x02\x03",

            "#1040FFor now, at least, it seems\x01",
            "things are in hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x18,
        (
            "#691F#5PYeah, somehow...\x02\x03",

            "Putting that aside...\x01",
            "I'm guessin' you need somethin'?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x2084)
    Jump("loc_60B9")

    label("loc_5E69")


    ChrTalk(    #204
        0x18,
        "#691F#5POhh, you guys. You seem as busy as always.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        "#1016F#4PAhaha... you too, Gustav.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x102,
        "#1040F#4PGood work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x18,
        (
            "#690F#5PWell, I'm busy, sure, but most of\x01",
            "it's just respondin' to complaints.\x02\x03",

            "About the only thing I can do with machines\x01",
            "right now is just put some oil on.\x02\x03",

            "I'm gettin' pretty fed up with it,\x01",
            "I don't mind tellin' you.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FFE")

    ChrTalk(    #208
        0x107,
        "#063F#4PTh-That does sound kind of sad.\x02",
    )

    CloseMessageWindow()

    label("loc_5FFE")


    ChrTalk(    #209
        0x101,
        (
            "#1015F#4PI guess it'd be the same as me not being\x01",
            "able to swing my staff around like I wanted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x18,
        (
            "#691F#5PWell, something like that.\x02\x03",

            "Putting that aside...\x01",
            "Did you need somethin'?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60B9")


    ChrTalk(    #211
        0x102,
        "#1040F#4PYes, actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #212
        (
            "\x07\x05Estelle explained the situation to Maintenance Chief Gustav\x01",
            "and asked him to lend them the combustion engine.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #213
        0x18,
        (
            "#692F#5PI see... Good eye, yeah.\x02\x03",

            "#690FIt's not a machine good for much except powerin'\x01",
            "simple stuff, so I wouldn't mind just givin' it\x01",
            "to you, but...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_623C")

    ChrTalk(    #214
        0x106,
        "#052F#4PIs there some problem?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A3")

    label("loc_623C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6271")

    ChrTalk(    #215
        0x103,
        "#023F#4PIs there some problem?\x02",
    )

    CloseMessageWindow()
    Jump("loc_62A3")

    label("loc_6271")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62A3")

    ChrTalk(    #216
        0x108,
        "#073F#4PIs there some problem?\x02",
    )

    CloseMessageWindow()

    label("loc_62A3")


    ChrTalk(    #217
        0x18,
        (
            "#690F#5PWell, you see...\x02\x03",

            "You got bad timing, is all. We just lent\x01",
            "it out to the Royal Army again.\x02\x03",

            "We brought it when we went to\x01",
            "swap the Arseille's engine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0x101,
        "#1015F#4POh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_639A")

    ChrTalk(    #219
        0x107,
        "#064F#4PSo, it'll be at Leiston Fortress?\x02",
    )

    CloseMessageWindow()
    Jump("loc_63DA")

    label("loc_639A")


    ChrTalk(    #220
        0x102,
        (
            "#1044F#4PSo, then, would it be stored\x01",
            "at Leiston Fortress?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63DA")


    ChrTalk(    #221
        0x18,
        (
            "#691F#5PYeah, I'd imagine so.\x02\x03",

            "Sorry, but if you wanna have it,\x01",
            "do you mind askin' them?\x02\x03",

            "It's kinda hard to just make a call\x01",
            "in this situation, if you know what\x01",
            "I mean.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x101,
        "#1006F#4PYeah, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x102,
        (
            "#1040F#4PWe'll make contact with Leiston Fortress\x01",
            "on our side.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x200B)
    OP_28(0xC2, 0x1, 0x8)

    def lambda_64F8():
        OP_8C(0x18, 0, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_64F8)
    OP_4B(0x18, 255)
    EventEnd(0x0)
    Return()

    # Function_43_5B04 end

    def Function_44_6507(): pass

    label("Function_44_6507")

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
        (0, "loc_6580"),
        (1, "loc_6586"),
        (SWITCH_DEFAULT, "loc_658C"),
    )


    label("loc_6580")

    OP_A2(0x1200)
    Jump("loc_658C")

    label("loc_6586")

    OP_A2(0x1201)
    Jump("loc_658C")

    label("loc_658C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_659A")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_659E")

    label("loc_659A")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_659E")

    Return()

    # Function_44_6507 end

    def Function_45_659F(): pass

    label("Function_45_659F")

    ClearMapFlags(0x1)
    OP_6D(0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_65DD")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_65FB")

    label("loc_65DD")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_65FB")

    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_45_659F end

    def Function_46_660D(): pass

    label("Function_46_660D")

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

    # Function_46_660D end

    def Function_47_6666(): pass

    label("Function_47_6666")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #224
        (
            "\x07\x05Airship Arrivals & Departures\x01",
            "⇒ To Grancel\x01",
            "⇒ To Ruan\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #225
        (
            "\x07\x05※Dangerous/combustible objects prohibited.\x01",
            "　　　　《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_47_6666 end

    def Function_48_6721(): pass

    label("Function_48_6721")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #226
        (
            "\x07\x05Traffic Control Tower\x01",
            "※All unauthorized personnel are prohibited.\x01",
            "《Liberl Orbalship Co.》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_48_6721 end

    SaveToFile()

Try(main)
