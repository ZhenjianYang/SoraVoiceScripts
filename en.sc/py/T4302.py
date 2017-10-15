from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4302   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4302.x',
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
        'Capital Citizen',                      # 9
        'Capital Citizen',                      # 10
        'Capital Citizen',                      # 11
        'Capital Citizen',                      # 12
        'Capital Citizen',                      # 13
        'Traveler',                             # 14
        'Ham',                                  # 15
        'Eggs',                                 # 16
        'Duke Dunan',                           # 17
        'Butler Phillip',                       # 18
        'Royal Army Officer',                   # 19
        'Guardsman',                            # 20
        'Guardsman',                            # 21
        'Royal Army Soldier',                   # 22
        'Royal Army Soldier',                   # 23
        'Royal Army Soldier',                   # 24
        'Royal Army Soldier',                   # 25
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
        'ED6_DT07/CH01020 ._CH',             # 00
        'ED6_DT07/CH01130 ._CH',             # 01
        'ED6_DT07/CH01170 ._CH',             # 02
        'ED6_DT07/CH01470 ._CH',             # 03
        'ED6_DT07/CH02140 ._CH',             # 04
        'ED6_DT07/CH02470 ._CH',             # 05
        'ED6_DT07/CH01600 ._CH',             # 06
        'ED6_DT07/CH01300 ._CH',             # 07
        'ED6_DT07/CH00322 ._CH',             # 08
        'ED6_DT07/CH00320 ._CH',             # 09
        'ED6_DT07/CH00321 ._CH',             # 0A
        'ED6_DT07/CH01640 ._CH',             # 0B
        'ED6_DT07/CH01003 ._CH',             # 0C
        'ED6_DT07/CH01150 ._CH',             # 0D
        'ED6_DT07/CH01730 ._CH',             # 0E
        'ED6_DT07/CH01731 ._CH',             # 0F
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
        'ED6_DT07/CH01130P._CP',             # 01
        'ED6_DT07/CH01170P._CP',             # 02
        'ED6_DT07/CH01470P._CP',             # 03
        'ED6_DT07/CH02140P._CP',             # 04
        'ED6_DT07/CH02470P._CP',             # 05
        'ED6_DT07/CH01600P._CP',             # 06
        'ED6_DT07/CH01300P._CP',             # 07
        'ED6_DT07/CH00322P._CP',             # 08
        'ED6_DT07/CH00320P._CP',             # 09
        'ED6_DT07/CH00321P._CP',             # 0A
        'ED6_DT07/CH01640P._CP',             # 0B
        'ED6_DT07/CH01003P._CP',             # 0C
        'ED6_DT07/CH01150P._CP',             # 0D
        'ED6_DT07/CH01730P._CP',             # 0E
        'ED6_DT07/CH01731P._CP',             # 0F
    )

    DeclNpc(
        X                   = 7870,
        Z                   = 0,
        Y                   = 39410,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 7190,
        Z                   = 0,
        Y                   = 38470,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 11280,
        Z                   = 20,
        Y                   = 38050,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 11270,
        Z                   = 0,
        Y                   = 36380,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 12000,
        Z                   = 380,
        Y                   = 27330,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x135,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = -9500,
        Z                   = 250,
        Y                   = 43800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 13510,
        Z                   = 0,
        Y                   = 37730,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 12860,
        Z                   = 0,
        Y                   = 36360,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        Direction           = 0,
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
        X                   = -1960,
        Z                   = 0,
        Y                   = 19780,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 1960,
        Z                   = 0,
        Y                   = 19780,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 8860,
        Z                   = 250,
        Y                   = 42720,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -8860,
        Z                   = 250,
        Y                   = 31000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 1920,
        Z                   = 1000,
        Y                   = 57170,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -1920,
        Z                   = 1000,
        Y                   = 57170,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )


    DeclActor(
        TriggerX            = -15850,
        TriggerZ            = 0,
        TriggerY            = 49490,
        TriggerRange        = 1000,
        ActorX              = -15740,
        ActorZ              = -2000,
        ActorY              = 51780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_36E",          # 00, 0
        "Function_1_436",          # 01, 1
        "Function_2_450",          # 02, 2
        "Function_3_5CD",          # 03, 3
        "Function_4_5F1",          # 04, 4
        "Function_5_615",          # 05, 5
        "Function_6_639",          # 06, 6
        "Function_7_65D",          # 07, 7
        "Function_8_706",          # 08, 8
        "Function_9_7AF",          # 09, 9
        "Function_10_812",         # 0A, 10
        "Function_11_865",         # 0B, 11
        "Function_12_AF2",         # 0C, 12
        "Function_13_E2B",         # 0D, 13
        "Function_14_F6E",         # 0E, 14
        "Function_15_10A3",        # 0F, 15
        "Function_16_155D",        # 10, 16
        "Function_17_17C2",        # 11, 17
        "Function_18_1FC7",        # 12, 18
        "Function_19_2387",        # 13, 19
        "Function_20_2713",        # 14, 20
        "Function_21_2D40",        # 15, 21
        "Function_22_2F47",        # 16, 22
        "Function_23_309E",        # 17, 23
        "Function_24_37C9",        # 18, 24
        "Function_25_3A34",        # 19, 25
        "Function_26_3A5D",        # 1A, 26
        "Function_27_50D6",        # 1B, 27
        "Function_28_510B",        # 1C, 28
        "Function_29_5138",        # 1D, 29
        "Function_30_5188",        # 1E, 30
        "Function_31_5220",        # 1F, 31
        "Function_32_52A1",        # 20, 32
    )


    def Function_0_36E(): pass

    label("Function_0_36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_3D6")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B6")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_3D6")

    label("loc_3B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D6")
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3F5")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 24)
    Jump("loc_435")

    label("loc_3F5")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_405"),
        (101, "loc_41D"),
        (SWITCH_DEFAULT, "loc_435"),
    )


    label("loc_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41A")
    SetMapFlags(0x10000000)
    Event(0, 23)

    label("loc_41A")

    Jump("loc_435")

    label("loc_41D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_432")
    SetMapFlags(0x10000000)
    Event(0, 26)

    label("loc_432")

    Jump("loc_435")

    label("loc_435")

    Return()

    # Function_0_36E end

    def Function_1_436(): pass

    label("Function_1_436")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE8900, 0x230061)
    OP_6F(0x1, 60)
    Return()

    # Function_1_436 end

    def Function_2_450(): pass

    label("Function_2_450")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_475")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5B7")

    label("loc_475")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5B7")

    label("loc_48E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5B7")

    label("loc_4A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C0")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5B7")

    label("loc_4C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D9")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5B7")

    label("loc_4D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F2")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5B7")

    label("loc_4F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5B7")

    label("loc_50B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_524")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5B7")

    label("loc_524")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5B7")

    label("loc_53D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_556")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5B7")

    label("loc_556")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5B7")

    label("loc_56F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_588")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5B7")

    label("loc_588")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5B7")

    label("loc_5A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5B7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5CC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B7")

    label("loc_5CC")

    Return()

    # Function_2_450 end

    def Function_3_5CD(): pass

    label("Function_3_5CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F0")
    OP_8D(0xFE, 10600, 38120, 11980, 37360, 3000)
    Jump("Function_3_5CD")

    label("loc_5F0")

    Return()

    # Function_3_5CD end

    def Function_4_5F1(): pass

    label("Function_4_5F1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_614")
    OP_8D(0xFE, 10270, 36610, 11740, 35690, 3000)
    Jump("Function_4_5F1")

    label("loc_614")

    Return()

    # Function_4_5F1 end

    def Function_5_615(): pass

    label("Function_5_615")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_638")
    OP_8D(0xFE, 12960, 38330, 14560, 37580, 3000)
    Jump("Function_5_615")

    label("loc_638")

    Return()

    # Function_5_615 end

    def Function_6_639(): pass

    label("Function_6_639")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_65C")
    OP_8D(0xFE, 12580, 37110, 13800, 35710, 3000)
    Jump("Function_6_639")

    label("loc_65C")

    Return()

    # Function_6_639 end

    def Function_7_65D(): pass

    label("Function_7_65D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_705")
    OP_8E(0xFE, 0x2238, 0xFA, 0xA2A8, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8E(0xFE, 0xD48, 0x0, 0xA2A8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x80C, 0x0, 0x9EC0, 0x7D0, 0x0)
    OP_8E(0xFE, 0x80C, 0x0, 0x82A0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEC4, 0x0, 0x7F08, 0x7D0, 0x0)
    OP_8E(0xFE, 0x2238, 0xFA, 0x7F08, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1500)
    Jump("Function_7_65D")

    label("loc_705")

    Return()

    # Function_7_65D end

    def Function_8_706(): pass

    label("Function_8_706")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7AE")
    OP_8E(0xFE, 0xFFFFDDC8, 0xFA, 0x7F30, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0xFFFFF344, 0xFA, 0x7F30, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF86C, 0x0, 0x8458, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF86C, 0x0, 0x9CA4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF3E4, 0x0, 0xA2D0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFDDC8, 0x0, 0xA2D0, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1500)
    Jump("Function_8_706")

    label("loc_7AE")

    Return()

    # Function_8_706 end

    def Function_9_7AF(): pass

    label("Function_9_7AF")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 1900, 0x30, 0x32, 0x96, 0x0)
    OP_22(0x30, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #0
        0xFE,
        "*chirp chirp chirp chirp chirp chirp chirp*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_9_7AF end

    def Function_10_812(): pass

    label("Function_10_812")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)
    OP_EA(0x0, 0x3, 0x0, 0x0)

    ChrTalk(    #1
        0xFE,
        "*chirp! chirp? chirp!*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_10_812 end

    def Function_11_865(): pass

    label("Function_11_865")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_905")

    ChrTalk(    #2
        0xFE,
        (
            "Eating my wife's sandwich here in\x01",
            "this garden is somehow special.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "It is the most delicious thing in Liberl...\x01",
            "No, the world!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AEE")

    label("loc_905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_99B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_93E")

    ChrTalk(    #4
        0xFE,
        "...Kids are so innocent and happy.\x02",
    )

    CloseMessageWindow()
    Jump("loc_998")

    label("loc_93E")


    ChrTalk(    #5
        0xFE,
        "Huh, what? A girl in a white dress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "Hmm, I'm pretty sure I didn't see her...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_998")

    Jump("loc_AEE")

    label("loc_99B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_AEE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A2C")

    ChrTalk(    #7
        0xFE,
        (
            "As long as you get permission from the villa,\x01",
            "you can eat here in the garden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "It really is a great spot for a picnic.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AEE")

    label("loc_A2C")


    ChrTalk(    #9
        0xFE,
        (
            "As long as you get permission from the villa,\x01",
            "you can eat here in the garden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Don't you think it'd be perfect\x01",
            "for a family group thing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "It really is a great spot for a picnic.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_AEE")

    TalkEnd(0x8)
    Return()

    # Function_11_865 end

    def Function_12_AF2(): pass

    label("Function_12_AF2")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_B7B")

    ChrTalk(    #12
        0xFE,
        (
            "I'm just happy to see everyone\x01",
            "enjoying their food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Heehee. It was worth getting up early\x01",
            "to make it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E27")

    label("loc_B7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_CC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C13")

    ChrTalk(    #14
        0xFE,
        (
            "I've seen a number of girls, but I don't\x01",
            "remember how they all looked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "I'm really sorry. Would you mind asking\x01",
            "someone else?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBE")

    label("loc_C13")


    ChrTalk(    #16
        0xFE,
        "...A girl in a white dress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I've seen a number of girls, but I don't\x01",
            "remember how they all looked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I'm really sorry. Would you mind asking\x01",
            "someone else?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_CBE")

    Jump("loc_E27")

    label("loc_CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_D77")

    ChrTalk(    #19
        0xFE,
        (
            "A wonderful place like this...\x01",
            "Not being able to use it would be terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "They don't charge an entrance fee, so\x01",
            "that's a big help on our family finances.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E27")

    label("loc_D77")


    ChrTalk(    #21
        0xFE,
        (
            "Our family comes out here to the\x01",
            "royal villa often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "After all, the queen was good enough\x01",
            "to open it to us citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "I couldn't bear not to be able to use it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_E27")

    TalkEnd(0x9)
    Return()

    # Function_12_AF2 end

    def Function_13_E2B(): pass

    label("Function_13_E2B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_EAF")

    ChrTalk(    #24
        0xFE,
        (
            "Hey, Mom made us this sandwich,\x01",
            "you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Why are you giving so much\x01",
            "of it to pigeons like that!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6A")

    label("loc_EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_F19")

    ChrTalk(    #26
        0xFE,
        "You can tell if you REALLY listen!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "They're going 'koo, koo' just like\x01",
            "pigeons should.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F6A")

    label("loc_F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_F6A")

    ChrTalk(    #28
        0xFE,
        (
            "You silly, pigeons have been going 'koo, koo,'\x01",
            "since, like, forever.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6A")

    TalkEnd(0xA)
    Return()

    # Function_13_E2B end

    def Function_14_F6E(): pass

    label("Function_14_F6E")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_FE7")

    ChrTalk(    #29
        0xFE,
        "Wh-When I saw the pigeons eyes, I just...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "W-Wait, you were giving them some too, sis!\x02",
    )

    CloseMessageWindow()
    Jump("loc_109F")

    label("loc_FE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_105E")

    ChrTalk(    #31
        0xFE,
        "No way, it sounds like 'poo poo' to me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "I'll try giving them some food,\x01",
            "so listen close this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109F")

    label("loc_105E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_109F")

    ChrTalk(    #33
        0xFE,
        "Hey, Sis.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "The pigeons, they're going 'poo poo.'\x02",
    )

    CloseMessageWindow()

    label("loc_109F")

    TalkEnd(0xB)
    Return()

    # Function_14_F6E end

    def Function_15_10A3(): pass

    label("Function_15_10A3")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1559")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_11C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1129")

    ChrTalk(    #35
        0xFE,
        "Mmm, seems like my hip's feeling better.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I'm a bit late, but time to take to the\x01",
            "road home.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C5")

    label("loc_1129")


    ChrTalk(    #37
        0xFE,
        "Mmm, seems like my hip's feeling better.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I'm a bit late, but time to take to the\x01",
            "road home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Ho ho, today ended up as quite the\x01",
            "long walk.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_11C5")

    Jump("loc_1559")

    label("loc_11C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_139A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1293")

    ChrTalk(    #40
        0xFE,
        (
            "After all, despite how marvelous I look,\x01",
            "I've lived over seventy years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I'm sure I've seen at least one girl in a white\x01",
            "dress, but I couldn't say when or where.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "Ha ha ha.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1397")

    label("loc_1293")


    ChrTalk(    #43
        0xFE,
        "...Have I seen a girl in a white dress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "Well, yes, and...no.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "After all, despite how marvelous I look,\x01",
            "I've lived over seventy years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I'm sure I've seen at least one girl in a white\x01",
            "dress, but I couldn't say when or where.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "Ha ha ha.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1397")

    Jump("loc_1559")

    label("loc_139A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1559")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_143F")

    ChrTalk(    #48
        0xFE,
        (
            "Would you like me to teach\x01",
            "you my secret judo throw?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "You grab their collar with all your might,\x01",
            "and then...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "...Ow ow owww, m-my hip!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1559")

    label("loc_143F")


    ChrTalk(    #51
        0xFE,
        (
            "I heard a fearsome cry by\x01",
            "the thicket near the villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "If it'd been a monster, I would've dragged\x01",
            "it out kicking and screaming...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Then I would've slammed it into the ground\x01",
            "with my judo throw, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Ultimately it was too scared of\x01",
            "me and never showed itself.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1559")

    TalkEnd(0xC)
    Return()

    # Function_15_10A3 end

    def Function_16_155D(): pass

    label("Function_16_155D")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_15FA")

    ChrTalk(    #55
        0xFE,
        (
            "I'd just intended to peek in at the\x01",
            "royal villa, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "It's such a relaxing place. I ended\x01",
            "up staying for quite a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BE")

    label("loc_15FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_166C")

    ChrTalk(    #57
        0xFE,
        (
            "... You're looking for a girl in a\x01",
            "white dress?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "I'm sorry, I don't think I'll be of any help.\x02",
    )

    CloseMessageWindow()
    Jump("loc_17BE")

    label("loc_166C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_17BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_16F5")

    ChrTalk(    #59
        0xFE,
        "There's no trash anywhere in this garden...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "You can tell how good the manners\x01",
            "of those who use the place are.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17BE")

    label("loc_16F5")


    ChrTalk(    #61
        0xFE,
        (
            "Huh, it's simple, but this garden\x01",
            "has a very nice atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "The shrubs and the lawn are very well\x01",
            "tended. It's quite lovely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I'd imagined more of a showy place,\x01",
            "but this isn't bad.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_17BE")

    TalkEnd(0xD)
    Return()

    # Function_16_155D end

    def Function_17_17C2(): pass

    label("Function_17_17C2")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_19BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_18B5")

    ChrTalk(    #64
        0xFE,
        (
            "It's rare to see people visiting the royal\x01",
            "villa in the midst of chaos like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "If you wish to enter, you're welcome inside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Right now it's just a small selection\x01",
            "of staff along with us guards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19BA")

    label("loc_18B5")


    ChrTalk(    #67
        0xFE,
        "Oh, from the looks of you you're bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "It's rare to see people visiting the royal\x01",
            "villa in the midst of chaos like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "If you wish to enter, you're welcome inside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "Right now it's just a small selection\x01",
            "of staff along with us guards.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_19BA")

    Jump("loc_1FC3")

    label("loc_19BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1AB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1A35")

    ChrTalk(    #71
        0xFE,
        (
            "We've been instructed by Colonel\x01",
            "Cid to let bracers enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "Feel free to come in.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AB4")

    label("loc_1A35")


    ChrTalk(    #73
        0xFE,
        "Welcome to the royal villa.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "We've been instructed by Colonel\x01",
            "Cid to let bracers enter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "Feel free to come in.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1AB4")

    Jump("loc_1FC3")

    label("loc_1AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1B68")

    ChrTalk(    #76
        0xFE,
        (
            "Security headquarters was established safely,\x01",
            "and that means we're finally on track for the\x01",
            "signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "Security will be even tighter than before now.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC3")

    label("loc_1B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1C53")

    ChrTalk(    #78
        0xFE,
        (
            "Does it seem like there's more visitors\x01",
            "to the villa than normal today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "It's probably because the villa will be closed\x01",
            "before and after the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "Guess a lot of people are coming in\x01",
            "while they can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC3")

    label("loc_1C53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_1D41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1CB5")

    ChrTalk(    #81
        0xFE,
        "A girl in a white dress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "Sorry, I don't remember every single visitor.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D3E")

    label("loc_1CB5")


    ChrTalk(    #83
        0xFE,
        "A girl in a white dress?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "Well, there's been a lot of people today, so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "Sorry, I don't remember every single visitor.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1D3E")

    Jump("loc_1FC3")

    label("loc_1D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1FC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 5)), scpexpr(EXPR_END)), "loc_1DC0")

    ChrTalk(    #86
        0xFE,
        (
            "It seems like the old man that just rushed\x01",
            "in hurt his hip running from some monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "Is he...okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FC3")

    label("loc_1DC0")


    ChrTalk(    #88
        0xFE,
        "I'd kind of like to ask, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Just a bit ago an old man rushed in\x01",
            "saying he heard a monster howling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Did you find anything odd by\x01",
            "the entrance around here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1015FAh, you mean that big monster, I bet.\x02\x03",

            "#1000FWe took care of it, so there shouldn't\x01",
            "be any problem now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "Oh, is that right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "...Now that you mention it,\x01",
            "you seem to be bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "That's great, I was just thinking we'd\x01",
            "have to investigate and slay it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Thank you for your assistance.\x01",
            "Enjoy your time at the villa.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x165D)

    label("loc_1FC3")

    TalkEnd(0x13)
    Return()

    # Function_17_17C2 end

    def Function_18_1FC7(): pass

    label("Function_18_1FC7")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2055")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2052")

    ChrTalk(    #96
        0xFE,
        (
            "Given the situation, there's no one at the\x01",
            "villa but the guards and some staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "If you'd like, come on in.\x02",
    )

    CloseMessageWindow()

    label("loc_2052")

    Jump("loc_2383")

    label("loc_2055")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_214F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_20B6")

    ChrTalk(    #98
        0xFE,
        "Please, come in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "I've received orders to let you through.\x02",
    )

    CloseMessageWindow()
    Jump("loc_214C")

    label("loc_20B6")


    ChrTalk(    #100
        0xFE,
        (
            "You're the bracers who will be assisting\x01",
            "with the investigation, correct?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "Please, come in.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "I've received orders to let you through.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_214C")

    Jump("loc_2383")

    label("loc_214F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2220")

    ChrTalk(    #103
        0xFE,
        (
            "The royal villa will be acting as security\x01",
            "headquarters until the day of the\x01",
            "signing ceremony itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "The villa will be opened to the citizenry\x01",
            "again after the signing ceremony, I suppose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2383")

    label("loc_2220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_22D7")

    ChrTalk(    #105
        0xFE,
        (
            "In preparation for the pact signing ceremony,\x01",
            "security in the Grancel region will be\x01",
            "heightened soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "This location will only be open\x01",
            "to the citizenry until then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2383")

    label("loc_22D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 5)), scpexpr(EXPR_END)), "loc_231A")

    ChrTalk(    #107
        0xFE,
        "Hmm? A girl?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "...I'm sorry, but I have no idea.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2383")

    label("loc_231A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2383")

    ChrTalk(    #109
        0xFE,
        (
            "The royal villa here is currently\x01",
            "open to citizen visitors.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "Please, feel free to enter.\x02",
    )

    CloseMessageWindow()

    label("loc_2383")

    TalkEnd(0x14)
    Return()

    # Function_18_1FC7 end

    def Function_19_2387(): pass

    label("Function_19_2387")

    TalkBegin(0x15)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2533")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2530")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2455")

    ChrTalk(    #111
        0xFE,
        (
            "Patrols at night with the orbal lights\x01",
            "out like this are kinda scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "If monsters decided to attack from the forest,\x01",
            "they'd have the dark on their side, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2530")

    label("loc_2455")


    ChrTalk(    #113
        0xFE,
        "The day patrol is a cakewalk, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Patrols at night with the orbal lights\x01",
            "out like this are kinda scary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "If monsters decided to attack from the forest,\x01",
            "they'd have the dark on their side, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_2530")

    Jump("loc_270F")

    label("loc_2533")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_270F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_25CC")

    ChrTalk(    #116
        0xFE,
        (
            "It seems the Intelligence Division's attack\x01",
            "here was a feint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "Well, seems like Colonel Cid saw\x01",
            "right through it, though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_270F")

    label("loc_25CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_270F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2659")

    ChrTalk(    #118
        0xFE,
        (
            "Having the duke around would be an\x01",
            "obstruction to security, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "Is it really okay to send him back to Grancel?\x02",
    )

    CloseMessageWindow()
    Jump("loc_270F")

    label("loc_2659")


    ChrTalk(    #120
        0xFE,
        (
            "As you see, Duke Dunan's house arrest\x01",
            "was lifted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "Having the duke around would be an\x01",
            "obstruction to security, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "Is it really okay to send him back to Grancel?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_270F")

    TalkEnd(0x15)
    Return()

    # Function_19_2387 end

    def Function_20_2713(): pass

    label("Function_20_2713")

    TalkBegin(0x16)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_28AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_27D0")

    ChrTalk(    #123
        0xFE,
        (
            "It seems like some communications have been\x01",
            "restored, but information doesn't really reach\x01",
            "the villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "It makes me reeeeeally nervous, I won't lie.\x02",
    )

    CloseMessageWindow()
    Jump("loc_28AC")

    label("loc_27D0")


    ChrTalk(    #125
        0xFE,
        (
            "With orbments not working, what's going\x01",
            "to happen now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "It seems like some communications have been\x01",
            "restored, but information doesn't really reach\x01",
            "the villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "It makes me reeeeeally nervous, I won't lie.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_28AC")

    Jump("loc_2D3C")

    label("loc_28AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2A66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_29B9")

    ChrTalk(    #128
        0xFE,
        (
            "I didn't think we'd end up fighting\x01",
            "the Special Ops guys again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "We managed with numbers, somehow, but\x01",
            "they are some seriously tough customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "When it comes to hand-to-hand combat tactics,\x01",
            "it's hard to match up to them...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A63")

    label("loc_29B9")


    ChrTalk(    #131
        0xFE,
        (
            "We managed with numbers, somehow, but\x01",
            "the special forces guys are impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "When it comes to hand-to-hand combat tactics,\x01",
            "it's hard to match up to them...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2A63")

    Jump("loc_2D3C")

    label("loc_2A66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2D3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_2B6C")

    ChrTalk(    #133
        0xFE,
        (
            "Colonel Cid is a more moderate and\x01",
            "reserved person compared to Colonel\x01",
            "Richard, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "There's rumors that say he's better than\x01",
            "the colonel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "I wonder if General Cassius might not have\x01",
            "a pretty high opinion of Colonel Cid\x01",
            "himself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3C")

    label("loc_2B6C")


    ChrTalk(    #136
        0xFE,
        (
            "Colonel Cid is a more moderate and\x01",
            "reserved person compared to Colonel\x01",
            "Richard, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "There's rumors that say he's better than\x01",
            "the colonel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "During the Hundred Days War, they used the\x01",
            "guard posts to divide the Imperial Army, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "Well, the hottest fighting was at the Sanktheim\x01",
            "Gate, and the reason it held was thanks to\x01",
            "Lieutenant Colonel Cid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "I wonder if General Cassius might not have a\x01",
            "pretty high opinion of Colonel Cid himself.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_2D3C")

    TalkEnd(0x16)
    Return()

    # Function_20_2713 end

    def Function_21_2D40(): pass

    label("Function_21_2D40")

    TalkBegin(0x17)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2DC9")

    ChrTalk(    #141
        0xFE,
        (
            "So the Intelligence Division's finally\x01",
            "all caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "That means the coup d'etat is finally\x01",
            "really over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F43")

    label("loc_2DC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_2F43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2E69")

    ChrTalk(    #143
        0xFE,
        "Ahhh, I feel so much better now!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "In the first place, I don't think the Royal\x01",
            "Guard's got so much time that they can\x01",
            "escort the duke.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F43")

    label("loc_2E69")


    ChrTalk(    #145
        0xFE,
        "Hey, I heard what happened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "Duke Dunan was CONSTANTLY hassling us\x01",
            "with all these stupid orders.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "To lecture him and put him in his place...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "The look on his face!\x01",
            "I'll cherish that moment forever.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_2F43")

    TalkEnd(0x17)
    Return()

    # Function_21_2D40 end

    def Function_22_2F47(): pass

    label("Function_22_2F47")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_309A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2FD5")

    ChrTalk(    #149
        0xFE,
        "The weather's really been great lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "Hopefully the weather holds until\x01",
            "the day of the signing ceremony.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_309A")

    label("loc_2FD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_309A")

    ChrTalk(    #151
        0xFE,
        (
            "I know it's nothing new, but\x01",
            "it must be hard on Phillip.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "If he didn't have some real endurance,\x01",
            "I doubt he could be the butler for\x01",
            "that duke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "He's a really good guy, I think.\x02",
    )

    CloseMessageWindow()

    label("loc_309A")

    TalkEnd(0x18)
    Return()

    # Function_22_2F47 end

    def Function_23_309E(): pass

    label("Function_23_309E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30B5")
    Call(0, 30)
    Call(0, 31)

    label("loc_30B5")

    OP_6D(680, 1000, 52720, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(600, 0)
    OP_C8(0x200, 0x46, "C_PLAC11._CH", 0x1, 0x5DC)
    OP_DE("Erbe Royal Villa")
    FadeToBright(1500, 0)
    SetChrPos(0x101, -240, 0, 26720, 10)
    SetChrPos(0xF7, 780, 0, 26810, 10)
    SetChrPos(0xF8, -1170, 0, 26020, 10)
    SetChrPos(0xF9, 1520, 0, 25840, 10)

    def lambda_316C():
        OP_6D(190, 0, 26660, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_316C)

    def lambda_3184():
        OP_6E(262, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3184)

    def lambda_3194():
        OP_6C(348000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3194)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31D5")

    ChrTalk(    #154
        0x107,
        "#061FWow! It's so pretty!\x02",
    )

    CloseMessageWindow()

    label("loc_31D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3268")

    ChrTalk(    #155
        0x108,
        (
            "#070FThe royal villa...\x01",
            "Brings you back, doesn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#1006F#6PYeah...\x02\x03",

            "#1015FSeems a bit more lively this time,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3306")

    label("loc_3268")


    ChrTalk(    #157
        0x101,
        (
            "#1006F#6PThe royal villa... This is sorta nostalgic,\x01",
            "in a 'that was an awesome adventure'\x01",
            "kind of way.\x02\x03",

            "#1015FSeems a bit more lively this time,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3306")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_337B")

    ChrTalk(    #158
        0x105,
        (
            "#040FThe villa is usually open to the general public.\x02\x03",

            "Many people use it as a place to relax.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3497")

    label("loc_337B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3402")

    ChrTalk(    #159
        0x106,
        (
            "#051FThink I heard once they keep it open to\x01",
            "the public, usually.\x02\x03",

            "Sorta like a royal tourist spot or somethin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3497")

    label("loc_3402")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3497")

    ChrTalk(    #160
        0x103,
        (
            "#020FAs I recall, the villa is typically open\x01",
            "to the public.\x02\x03",

            "It's something of a tourist spot, in part\x01",
            "because it's so relaxing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3497")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35D3")

    ChrTalk(    #161
        0x104,
        (
            "#035FSuch a refined setting!\x01",
            "It speaks to my muse.\x02\x03",

            "#030FPerhaps I should wield my lute in the\x01",
            "service of further rest and healing for\x01",
            "everyone here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        (
            "#1007F#6PYeah, you'll send them into comas,\x01",
            "maybe...\x02\x03",

            "#1011FI see the point about a vacation spot,\x01",
            "though. There's a lot of families here!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3615")

    label("loc_35D3")


    ChrTalk(    #163
        0x101,
        (
            "#1011F#6PHuh, okay. Cool!\x02\x03",

            "There ARE a lot of families here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3615")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3699")

    ChrTalk(    #164
        0x108,
        (
            "#070FI imagine our lost child was with a\x01",
            "family like that.\x02\x03",

            "So let's go find Raymond, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#1006F#6POkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_37C3")

    label("loc_3699")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_372E")

    ChrTalk(    #166
        0x106,
        (
            "#053FI'd bet our lost kid was with a family like that.\x02\x03",

            "#050FSo let's go find this Raymond guy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        "#1006F#6PRight, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_37C3")

    label("loc_372E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37C3")

    ChrTalk(    #168
        0x103,
        (
            "#020FI would imagine our lost child was with\x01",
            "a family like that.\x02\x03",

            "Let's find Raymond and see what's happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x101,
        "#1006F#6POkay!\x02",
    )

    CloseMessageWindow()

    label("loc_37C3")

    OP_A2(0x160C)
    EventEnd(0x0)
    Return()

    # Function_23_309E end

    def Function_24_37C9(): pass

    label("Function_24_37C9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #170
        (
            "\x07\x05The next day, Estelle went to the Erbe Royal Villa\x01",
            "to give Cid the report on the letters.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_DB()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    SetChrPos(0x13, -7380, 0, 36870, 270)
    SetChrPos(0x14, -11200, 0, 36810, 90)
    SetChrPos(0x15, 9950, 0, 36540, 314)
    SetChrPos(0x16, 6560, 0, 39190, 134)
    SetChrPos(0x17, 7820, 0, 31210, 90)
    SetChrPos(0x18, -8590, 0, 31290, 270)
    SetChrChipByIndex(0x13, 8)
    SetChrSubChip(0x13, 0)
    SetChrChipByIndex(0x14, 8)
    SetChrSubChip(0x14, 0)
    SetChrChipByIndex(0x15, 8)
    SetChrSubChip(0x15, 0)
    SetChrChipByIndex(0x16, 8)
    SetChrSubChip(0x16, 0)
    SetChrChipByIndex(0x17, 8)
    SetChrSubChip(0x17, 0)
    SetChrChipByIndex(0x18, 8)
    SetChrSubChip(0x18, 0)
    OP_43(0x13, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x15, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x14, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x17, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x16, 0x0, 0x0, 0x19)
    Sleep(50)
    OP_43(0x18, 0x0, 0x0, 0x19)
    OP_6D(-660, 0, 23220, 0)
    OP_67(0, 6170, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(344000, 0)
    OP_6E(409, 0)
    OP_1D(0x11)
    OP_22(0x1C2, 0x0, 0x64)

    def lambda_39C8():
        OP_6D(680, 1000, 52720, 7000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_39C8)

    def lambda_39E0():
        OP_67(0, 8000, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_39E0)

    def lambda_39F8():
        OP_6C(315000, 8000)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_39F8)

    def lambda_3A08():
        OP_6E(600, 8000)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3A08)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x13, 0x2)
    Sleep(1000)
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4303   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_37C9 end

    def Function_25_3A34(): pass

    label("Function_25_3A34")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3A5C")
    OP_99(0xFE, 0x0, 0x4, 0xA28)
    Sleep(500)
    OP_99(0xFE, 0x4, 0x0, 0xA28)
    Sleep(1500)
    Jump("Function_25_3A34")

    label("loc_3A5C")

    Return()

    # Function_25_3A34 end

    def Function_26_3A5D(): pass

    label("Function_26_3A5D")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A70")
    Call(0, 30)

    label("loc_3A70")

    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x101, 80, 1000, 59650, 180)
    SetChrPos(0xF7, 80, 1000, 59650, 180)
    SetChrPos(0x107, 80, 1000, 59650, 180)
    SetChrPos(0x12F, 80, 1000, 59650, 180)
    SetChrPos(0x10, -220, 0, 44940, 180)
    SetChrPos(0x11, 560, 0, 45120, 180)
    SetChrPos(0x12, 50, 0, 42800, 0)
    SetChrPos(0x13, -750, 0, 42500, 0)
    SetChrPos(0x14, 750, 0, 42500, 0)
    SetChrChipByIndex(0x13, 11)
    SetChrChipByIndex(0x14, 11)
    SetChrSubChip(0x13, 0)
    SetChrSubChip(0x14, 0)
    OP_4A(0x13, 255)
    OP_4A(0x14, 255)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    OP_4A(0x15, 255)
    OP_4A(0x16, 255)
    OP_6D(580, 1000, 56480, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1D)
    OP_73(0x0)

    def lambda_3BB2():
        OP_8E(0xFE, 0x1F4, 0x3E8, 0xD78C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3BB2)
    Sleep(600)

    def lambda_3BD2():
        OP_8E(0xFE, 0xFFFFFE0C, 0x3E8, 0xD78C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_3BD2)
    Sleep(600)

    def lambda_3BF2():
        OP_8E(0xFE, 0xFFFFFE0C, 0x3E8, 0xDC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_3BF2)
    Sleep(600)

    def lambda_3C12():
        OP_8E(0xFE, 0x1F4, 0x3E8, 0xDC14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12F, 0, lambda_3C12)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #171
        0x101,
        "#1004F#5PHey, isn't that...\x02",
    )

    CloseMessageWindow()

    def lambda_3C58():
        OP_6D(470, 0, 44880, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C58)

    def lambda_3C70():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C70)

    def lambda_3C80():
        OP_67(0, 8189, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3C80)
    OP_6B(2450, 3000)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #172
        0x10,
        (
            "#224F#6PWhat is the meaning of this?!\x02\x03",

            "Do you deliberately besmirch ME, Dunan\x01",
            "von Auslese, rightful heir to the throne?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x12,
        "N-No, Your Grace! Not at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x12,
        (
            "In fact, this morning we put a plan into\x01",
            "motion to slay any monsters along the\x01",
            "road to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x12,
        (
            "You will be completely safe with the\x01",
            "allotted escort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x10,
        (
            "#224F#6PTHAT IS NOT THE POINT!\x02\x03",

            "An honor guard of a mere three men is\x01",
            "wholly unacceptable for a man of MY\x01",
            "stature and importance!\x02\x03",

            "I demand at least a full squadron!\x01",
            "Ten men! Go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x12,
        "But, Your Grace...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x13, 400)
    Sleep(500)

    ChrTalk(    #178
        0x11,
        (
            "#722F#4PYour Grace...please do not demand so\x01",
            "much of them.\x02\x03",

            "Her Royal Highness has finally given leave\x01",
            "for us to return.\x02\x03",

            "Please, we should consider\x01",
            "ourselves lucky to have received such\x01",
            "kindness itself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x10,
        (
            "#222F#6PSilence, Phillip!\x02\x03",

            "This 'punishment' was the height of\x01",
            "injustice to begin with!\x02\x03",

            "Given the outrageous grievances levied\x01",
            "against me, I SHOULD demand nothing less\x01",
            "than the whole Royal Guard to meet me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        (
            "#4PWeeeell, we may not be the entire Royal Guard...\x02\x03",

            "...but we could go with you, if you'd like.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_40F2():
        OP_6D(-70, 0, 46500, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_40F2)

    def lambda_410A():
        OP_67(0, 8050, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_410A)

    def lambda_4122():
        OP_6E(300, 4000)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_4122)

    def lambda_4132():
        OP_8E(0xFE, 0xB4, 0x0, 0xB586, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4132)
    Sleep(100)

    def lambda_4152():
        TurnDirection(0x10, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_4152)

    def lambda_4160():
        TurnDirection(0x11, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4160)

    def lambda_416E():
        OP_8E(0xFE, 0xFFFFFC4A, 0x0, 0xB66C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_416E)
    Sleep(50)

    def lambda_418E():
        OP_8E(0xFE, 0xC8, 0xFA, 0xBA54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12F, 1, lambda_418E)
    Sleep(100)

    def lambda_41AE():
        OP_8E(0xFE, 0xFFFFFC7C, 0xFA, 0xBA54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_41AE)
    WaitChrThread(0x101, 0x2)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #181
        0x10,
        "#226F#2PYOU!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x11,
        "#721F#4PMiss Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#1007F*sigh* Haven't changed a bit, have you, Duke,\x01",
            "ol' buddy?\x02\x03",

            "#1019FIt's not very dukely to railroad everyone with\x01",
            "your selfishness. Very YOU, but not very dukely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x10,
        (
            "#226F#2PHow DARE you call me 'buddy,'\x01",
            "you...you impertinent NOBODY!\x02\x03",

            "Why are you even HERE?!\x02\x03",

            "The villa was to be closed off\x01",
            "to the common rabble!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        (
            "#1006FYeah, y'see, we had actual WORK\x01",
            "to do here.\x02\x03",

            "So, goin' for a walk, ol' buddy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x10,
        (
            "#220F#2PMore than a mere stroll, girl.\x01",
            "Prepare to be shocked!\x02\x03",

            "#221FAlicia has come to her senses and released\x01",
            "me from the unjust punishment which bound\x01",
            "me here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        "#1004FThe 'unjust punishment'?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_44C9")

    ChrTalk(    #188
        0x106,
        (
            "#052F#6PWait, they're actually lettin' you outta\x01",
            "house arrest?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4507")

    label("loc_44C9")


    ChrTalk(    #189
        0x103,
        "#023F#6PThey've actually released you from house arrest?\x02",
    )

    CloseMessageWindow()

    label("loc_4507")


    ChrTalk(    #190
        0x11,
        (
            "#720F#4PIndeed. Word arrived from Her Royal\x01",
            "Highness this morning.\x02\x03",

            "She instructed us to depart from the\x01",
            "villa and return to Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_45DC")

    ChrTalk(    #191
        0x106,
        "#051F#6POh, brother. The queen's way, way too nice.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4621")

    label("loc_45DC")


    ChrTalk(    #192
        0x103,
        (
            "#027F#6PHer Majesty's heart really is too big\x01",
            "for her own good.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4621")


    ChrTalk(    #193
        0x101,
        (
            "#1011FHuuuh. Well, good for you, I guess.\x02\x03",

            "#1001FWell, try and keep a clear head so you\x01",
            "don't get played a second time, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x10,
        "#223F#2PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        (
            "#1006FAnd, y'know, don't you think you should\x01",
            "examine your lifestyle a bit?\x02\x03",

            "You're kind of a slacker, buddy.\x02\x03",

            "Maybe you could start with a bit of exercise?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF7, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x107, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x12F, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xF7)
    OP_63(0x10)
    OP_63(0x11)
    OP_63(0x107)
    OP_63(0x12F)
    OP_63(0x12)
    OP_63(0x13)
    OP_63(0x14)

    ChrTalk(    #196
        0x101,
        "#1015FWhat is it? I say something weird?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x11,
        "#720F#4P...No. It is exactly as you say, Miss Estelle.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 400)
    Sleep(500)

    ChrTalk(    #198
        0x11,
        (
            "#722F#4PIf His Grace only had a better hold on\x01",
            "his life, he would not have been so easily\x01",
            "manipulated by Colonel Richard...\x02\x03",

            "Allow me to echo your suggestion...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x10,
        "#226F#2PBaaah! Enough of your lectures!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 600)

    ChrTalk(    #200
        0x10,
        (
            "#224F#5PEnough of this! I shall not remain here\x01",
            "a second longer among such riffraff!\x02\x03",

            "We depart for the capital!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x12,
        "#2PUh, Your Grace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        (
            "#1004FHuh? Weren't you just going on about\x01",
            "not having enough men?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 0, 600)

    ChrTalk(    #203
        0x10,
        (
            "#224F#2PNO!\x02\x03",

            "COME! LET'S GO, MEN!\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x12, 0x1, 0x0, 0x1D)
    Sleep(50)
    OP_43(0x13, 0x1, 0x0, 0x1B)
    OP_43(0x14, 0x1, 0x0, 0x1C)

    def lambda_4A7C():

        label("loc_4A7C")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_4A7C")

    QueueWorkItem2(0x11, 2, lambda_4A7C)
    OP_8C(0x10, 180, 600)
    OP_8E(0x10, 0xFFFFFF24, 0x0, 0x88B8, 0xBB8, 0x0)
    OP_44(0x11, 0x2)
    OP_8C(0x11, 270, 400)
    OP_8C(0x11, 0, 400)

    ChrTalk(    #204
        0x11,
        (
            "#720FMiss Estelle, it may be an old refrain by\x01",
            "now, but thank you.\x02\x03",

            "I'm not sure how to express my gratitude...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        (
            "#1016FHaha! Uh, don't worry about it.\x02\x03",

            "#1006FBut...I dunno. I think you really need\x01",
            "to drop the hammer a bit more, Phillip.\x02\x03",

            "I think he's the way he is because nobody's\x01",
            "ever really even scolded him, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x11,
        "#721FAh... Yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#1006FI don't really think he's THAT rotten, deep...\x01",
            "DEEP down, so I think he can still change.\x02\x03",

            "Don't you think he just needs a hand?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x11,
        "#722FMiss Estelle...your words ring so true...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x10,
        (
            "#5PPhilliiiiiip!\x01",
            "Why are you dawdling with peasants?!\x02\x03",

            "If you keep loitering, we'll depart without you!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 600)
    OP_8C(0x11, 180, 600)

    ChrTalk(    #210
        0x11,
        "#721F#6PEr, yes, Your Grace! I shall be but a moment.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 600)
    OP_8C(0x11, 0, 600)

    ChrTalk(    #211
        0x11,
        "#720FIf you will excuse me...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 270, 600)
    OP_8C(0x11, 180, 600)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    def lambda_4DE3():
        OP_6D(-370, 0, 43300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4DE3)
    OP_8E(0x11, 0xFFFFFF24, 0x0, 0x88B8, 0xBB8, 0x0)
    SetChrFlags(0x11, 0x80)
    Sleep(500)
    OP_6D(-600, 250, 47270, 1600)

    ChrTalk(    #212
        0x101,
        (
            "#1015FY'knooow, I think we probably shoulda\x01",
            "gone with them...but...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4EB7")

    ChrTalk(    #213
        0x106,
        (
            "#051FHaha... Man...\x02\x03",

            "You really are something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EF1")

    label("loc_4EB7")


    ChrTalk(    #214
        0x103,
        (
            "#021FOh, Estelle.\x02\x03",

            "You really are Cassius' daughter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF1")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #215
        0x101,
        "#1004F#4PBwuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x107,
        "#067FHaha! Estelle, you're incredible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x12F,
        (
            "#268FUm, Estelle, I kind of noticed when we first met...\x02\x03",

            "You're kind of, um...too nice, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #218
        0x101,
        "#1015F#6PToo nice? Huh?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5040")

    ChrTalk(    #219
        0x106,
        (
            "#051FIf you don't get it, don't sweat it.\x02\x03",

            "Let's get back to the capital, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5082")

    label("loc_5040")


    ChrTalk(    #220
        0x103,
        (
            "#027FDon't worry too much over it.\x02\x03",

            "Let's return to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5082")

    OP_A2(0x162C)
    OP_44(0x13, 0x1)
    OP_44(0x14, 0x1)
    SetChrPos(0x13, -1960, 0, 19780, 180)
    SetChrPos(0x14, 1960, 0, 19780, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    OP_4B(0x13, 255)
    OP_4B(0x14, 255)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_4B(0x15, 255)
    OP_4B(0x16, 255)
    EventEnd(0x0)
    Return()

    # Function_26_3A5D end

    def Function_27_50D6(): pass

    label("Function_27_50D6")

    OP_8F(0xFE, 0xFFFFF916, 0x0, 0xA690, 0x9C4, 0x0)
    OP_8C(0xFE, 90, 500)
    Sleep(2000)
    OP_8E(0xFE, 0xFFFFFB3C, 0x0, 0x9088, 0x9C4, 0x0)
    Return()

    # Function_27_50D6 end

    def Function_28_510B(): pass

    label("Function_28_510B")

    Sleep(1000)
    OP_8C(0xFE, 270, 500)
    Sleep(1500)
    OP_8C(0xFE, 180, 500)
    OP_8E(0xFE, 0x30C, 0x0, 0x9088, 0x9C4, 0x0)
    Return()

    # Function_28_510B end

    def Function_29_5138(): pass

    label("Function_29_5138")

    OP_8F(0xFE, 0x14, 0x0, 0xA2A8, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 500)
    OP_8F(0xFE, 0x2B2, 0x0, 0xA2A8, 0x9C4, 0x0)
    Sleep(1000)
    OP_8C(0xFE, 180, 500)
    OP_8E(0xFE, 0xFFFFFF24, 0x0, 0x8CA0, 0x9C4, 0x0)
    Return()

    # Function_29_5138 end

    def Function_30_5188(): pass

    label("Function_30_5188")

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
        (0, "loc_5201"),
        (1, "loc_5207"),
        (SWITCH_DEFAULT, "loc_520D"),
    )


    label("loc_5201")

    OP_A2(0x1200)
    Jump("loc_520D")

    label("loc_5207")

    OP_A2(0x1201)
    Jump("loc_520D")

    label("loc_520D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_521B")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_521F")

    label("loc_521B")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_521F")

    Return()

    # Function_30_5188 end

    def Function_31_5220(): pass

    label("Function_31_5220")

    ClearMapFlags(0x1)
    OP_6D(-11230, 0, -25420, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5263")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_5281")

    label("loc_5263")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_5281")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_31_5220 end

    def Function_32_52A1(): pass

    label("Function_32_52A1")

    EventBegin(0x1)

    ChrTalk(    #221
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    AnonymousTalk(    #222
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_539C")

    def lambda_5337():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5337)

    def lambda_5347():
        OP_6C(315000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_5347)
    WaitChrThread(0x1, 0x1)
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    OP_C0(0xE, 0x2F, 0xFFFFC216, 0x0, 0xC152, 0x0, 0xFFFFC284, 0xFFFFFAEC, 0xCA44)
    OP_51(0x101, 0x28, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    EventEnd(0x1)
    Jump("loc_53AB")

    label("loc_539C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_53AB")
    EventEnd(0x1)

    label("loc_53AB")

    Return()

    # Function_32_52A1 end

    SaveToFile()

Try(main)
