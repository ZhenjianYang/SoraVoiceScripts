from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1201   ._SN',
        MapName             = 'Bose',
        Location            = 'T1201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60026",
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
        'Elder Reisen',                         # 9
        'Lore',                                 # 10
        'Figaro',                               # 11
        'Pesca',                                # 12
        'Gray',                                 # 13
        'Vince',                                # 14
        'Ravennue Trail',                       # 15
        'Abandoned Mine Trail',                 # 16
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
        'ED6_DT07/CH01490 ._CH',             # 00
        'ED6_DT07/CH01120 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01140 ._CH',             # 03
        'ED6_DT07/CH01030 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01060 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH01490P._CP',             # 00
        'ED6_DT07/CH01120P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01140P._CP',             # 03
        'ED6_DT07/CH01030P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01060P._CP',             # 06
    )

    DeclNpc(
        X                   = 24310,
        Z                   = -4000,
        Y                   = 16670,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 26100,
        Z                   = -4000,
        Y                   = 12970,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 20640,
        Z                   = -4000,
        Y                   = 19180,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 19590,
        Z                   = -4000,
        Y                   = 16200,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 17380,
        Z                   = -4000,
        Y                   = 9850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 8,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 22560,
        Z                   = -530,
        Y                   = 26920,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -2080,
        Z                   = 0,
        Y                   = -80,
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
        X                   = 7170,
        Z                   = 8000,
        Y                   = 78890,
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
        X                   = -3900,
        Y                   = -1000,
        Z                   = 6200,
        Range               = -100,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1FA4,
        Unknown_18          = 0x0,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = 5000,
        Y                   = 0,
        Z                   = 34240,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 5150,
        Y                   = 4550,
        Z                   = 41780,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 5310,
        Y                   = 0,
        Z                   = 23020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = 6000,
        Y                   = 4400,
        Z                   = 54640,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 3260,
        Y                   = 7000,
        Z                   = 66870,
        Range               = 9230,
        Unknown_10          = 0x2710,
        Unknown_14          = 0x10C52,
        Unknown_18          = 0x0,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = -3900,
        Y                   = -100,
        Z                   = 7250,
        Range               = -100,
        Unknown_10          = 0x76C,
        Unknown_14          = 0x203A,
        Unknown_18          = 0x0,
        Unknown_1C          = 27,
    )

    DeclEvent(
        X                   = 5100,
        Y                   = 8000,
        Z                   = 67350,
        Range               = 9000,
        Unknown_10          = 0x2710,
        Unknown_14          = 0x10AFE,
        Unknown_18          = 0x0,
        Unknown_1C          = 27,
    )


    DeclActor(
        TriggerX            = -7280,
        TriggerZ            = 4460,
        TriggerY            = 54000,
        TriggerRange        = 800,
        ActorX              = -7280,
        ActorZ              = 5460,
        ActorY              = 54000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 33020,
        TriggerZ            = 8000,
        TriggerY            = 35080,
        TriggerRange        = 1000,
        ActorX              = 33020,
        ActorZ              = 9200,
        ActorY              = 35080,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_32A",          # 00, 0
        "Function_1_381",          # 01, 1
        "Function_2_57D",          # 02, 2
        "Function_3_6FA",          # 03, 3
        "Function_4_71F",          # 04, 4
        "Function_5_77F",          # 05, 5
        "Function_6_7E6",          # 06, 6
        "Function_7_825",          # 07, 7
        "Function_8_88C",          # 08, 8
        "Function_9_8EC",          # 09, 9
        "Function_10_985",         # 0A, 10
        "Function_11_C18",         # 0B, 11
        "Function_12_EAA",         # 0C, 12
        "Function_13_1023",        # 0D, 13
        "Function_14_1396",        # 0E, 14
        "Function_15_149A",        # 0F, 15
        "Function_16_19C8",        # 10, 16
        "Function_17_2654",        # 11, 17
        "Function_18_272B",        # 12, 18
        "Function_19_2DFA",        # 13, 19
        "Function_20_3469",        # 14, 20
        "Function_21_34B8",        # 15, 21
        "Function_22_35B4",        # 16, 22
        "Function_23_36AE",        # 17, 23
        "Function_24_36B2",        # 18, 24
        "Function_25_36B6",        # 19, 25
        "Function_26_36BA",        # 1A, 26
        "Function_27_3E1B",        # 1B, 27
        "Function_28_3E21",        # 1C, 28
    )


    def Function_0_32A(): pass

    label("Function_0_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_33E")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_34A")

    label("loc_33E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_34A")
    SetChrFlags(0xD, 0x10)

    label("loc_34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_360")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_380")

    label("loc_360")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_36C"),
        (SWITCH_DEFAULT, "loc_380"),
    )


    label("loc_36C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D")
    SetMapFlags(0x10000000)
    Event(0, 15)

    label("loc_37D")

    Jump("loc_380")

    label("loc_380")

    Return()

    # Function_0_32A end

    def Function_1_381(): pass

    label("Function_1_381")

    OP_16(0x2, 0xFA0, 0xFFFE5638, 0xFFFE98A0, 0x230043)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3A6")
    OP_B1("t1201_n")
    Jump("loc_560")

    label("loc_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 3)), scpexpr(EXPR_END)), "loc_3CE")
    OP_B1("t1201_y")
    OP_10(0x8, 0x0)
    OP_82(0x86, 0x0)
    OP_82(0x87, 0x0)
    OP_82(0x88, 0x0)
    OP_82(0x89, 0x0)
    OP_82(0x8A, 0x0)
    OP_82(0x8B, 0x0)
    Jump("loc_560")

    label("loc_3CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_560")
    OP_B1("t1201_n")
    LoadEffect(0x0, "map\\mpsmk0.eff")
    LoadEffect(0x1, "map\\mpsmk1.eff")
    LoadEffect(0x2, "map\\mpsmk2.eff")
    LoadEffect(0x3, "map\\mpsmk3.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 17810, -3200, 13650, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 28240, -4000, 6260, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 17940, -3500, 24500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 14180, -3300, 7940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 16920, -3300, 16420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0xFF, 0xFF, 21000, -4000, 7530, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_570")
    OP_72(0x6, 0x10)
    Jump("loc_574")

    label("loc_570")

    OP_64(0x0, 0x1)

    label("loc_574")

    SetMapFlags(0x2000000)
    OP_82(0x8C, 0x2)
    Return()

    # Function_1_381 end

    def Function_2_57D(): pass

    label("Function_2_57D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A2")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_6E4")

    label("loc_5A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BB")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_6E4")

    label("loc_5BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D4")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_6E4")

    label("loc_5D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5ED")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_6E4")

    label("loc_5ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_606")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_6E4")

    label("loc_606")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61F")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_6E4")

    label("loc_61F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_638")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_6E4")

    label("loc_638")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_651")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_6E4")

    label("loc_651")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66A")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_6E4")

    label("loc_66A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_683")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_6E4")

    label("loc_683")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_6E4")

    label("loc_69C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B5")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_6E4")

    label("loc_6B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CE")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_6E4")

    label("loc_6CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E4")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_6E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_6E4")

    label("loc_6F9")

    Return()

    # Function_2_57D end

    def Function_3_6FA(): pass

    label("Function_3_6FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_71E")
    OP_8C(0xFE, 180, 400)
    Sleep(2000)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    Jump("Function_3_6FA")

    label("loc_71E")

    Return()

    # Function_3_6FA end

    def Function_4_71F(): pass

    label("Function_4_71F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_77E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_742")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_742")

    OP_8E(0xFE, 0x5424, 0xFFFFF060, 0x23F0, 0x7D0, 0x0)
    Sleep(1000)
    OP_8E(0xFE, 0x4FA6, 0xFFFFF060, 0x3750, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    Jump("Function_4_71F")

    label("loc_77E")

    Return()

    # Function_4_71F end

    def Function_5_77F(): pass

    label("Function_5_77F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A2")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_7A2")

    OP_8E(0xFE, 0x69FA, 0xFFFFF060, 0x2F62, 0x3E8, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x65F4, 0xFFFFF060, 0x32AA, 0x3E8, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    Jump("Function_5_77F")

    label("loc_7E5")

    Return()

    # Function_5_77F end

    def Function_6_7E6(): pass

    label("Function_6_7E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_824")
    OP_8C(0xFE, 0, 400)
    Sleep(2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_815")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_815")

    OP_8C(0xFE, 315, 400)
    Sleep(2000)
    Jump("Function_6_7E6")

    label("loc_824")

    Return()

    # Function_6_7E6 end

    def Function_7_825(): pass

    label("Function_7_825")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_88B")
    OP_8E(0xFE, 0x4C86, 0xFFFFF060, 0x3F48, 0x3E8, 0x0)
    OP_8C(0xFE, 225, 400)
    Sleep(2000)
    OP_8E(0xFE, 0x5136, 0xFFFFF060, 0x37B4, 0x3E8, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87C")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_87C")

    OP_8C(0xFE, 270, 400)
    Sleep(2000)
    Jump("Function_7_825")

    label("loc_88B")

    Return()

    # Function_7_825 end

    def Function_8_88C(): pass

    label("Function_8_88C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8EB")
    OP_8E(0xFE, 0x3CBE, 0xFFFFF060, 0x2346, 0x3E8, 0x0)
    Sleep(2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C8")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_8C8")

    OP_8E(0xFE, 0x43E4, 0xFFFFF060, 0x267A, 0x3E8, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(2000)
    Jump("Function_8_88C")

    label("loc_8EB")

    Return()

    # Function_8_88C end

    def Function_9_8EC(): pass

    label("Function_9_8EC")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 5)), scpexpr(EXPR_END)), "loc_972")

    ChrTalk(    #0
        0xFE,
        (
            "Don't worry about us, we'll be fine.\x01",
            "Please, find Agate and help him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "The look on his face was so tormented...\x02",
    )

    CloseMessageWindow()
    Jump("loc_981")

    label("loc_972")

    Call(0, 16)
    OP_8C(0x8, 180, 0)
    OP_4B(0x8, 255)

    label("loc_981")

    TalkEnd(0x8)
    Return()

    # Function_9_8EC end

    def Function_10_985(): pass

    label("Function_10_985")

    TalkBegin(0xC)
    OP_63(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_995")
    Jump("loc_C14")

    label("loc_995")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_B5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A39")

    ChrTalk(    #2
        0xFE,
        (
            "We need to speak with our young\x01",
            "people and decide where we go from\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "If we mean to rebuild the orchards,\x01",
            "we must all do so together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B5A")

    label("loc_A39")


    ChrTalk(    #4
        0xFE,
        (
            "Oh, Aidios, grant us strength.\x01",
            "Great challenges lie before us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "But they are challenges we must\x01",
            "and will overcome!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Ravennue can't sustain itself without\x01",
            "the orchards, so we must do what we\x01",
            "can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "We need to speak with our young\x01",
            "people and decide where we go from\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_B5A")

    Jump("loc_C14")

    label("loc_B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_C14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_B9D")

    ChrTalk(    #8
        0xFE,
        "Oh, Aidios, grant us strength...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_C14")

    label("loc_B9D")


    ChrTalk(    #10
        0xFE,
        "Oh, Aidios, grant us strength...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "All the trees that we poured our\x01",
            "love and life into...all gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_C14")

    TalkEnd(0xC)
    Return()

    # Function_10_985 end

    def Function_11_C18(): pass

    label("Function_11_C18")

    TalkBegin(0xB)
    OP_63(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_C28")
    Jump("loc_EA6")

    label("loc_C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_DB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_CBA")

    ChrTalk(    #13
        0xFE,
        (
            "I have an obligation to provide for\x01",
            "my family.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "First, we need to talk, as a village,\x01",
            "about the future of our orchards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DAF")

    label("loc_CBA")


    ChrTalk(    #15
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "It's hard not to, but right now isn't\x01",
            "the time to wallow in depression.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "For the sake of my family, I have\x01",
            "to focus on moving forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "The village needs to come together\x01",
            "and talk about what to do about the\x01",
            "orchards.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_DAF")

    Jump("loc_EA6")

    label("loc_DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_EA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E21")

    ChrTalk(    #19
        0xFE,
        "I'll think about the future later.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "For now, I just need to think about\x01",
            "the present.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA6")

    label("loc_E21")


    ChrTalk(    #21
        0xFE,
        "M-My tractor... We'd just...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "A-Anyway, right now we need to\x01",
            "clean up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "We'll think about what to do later.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_EA6")

    TalkEnd(0xB)
    Return()

    # Function_11_C18 end

    def Function_12_EAA(): pass

    label("Function_12_EAA")

    TalkBegin(0x9)
    OP_63(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_101F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F39")

    ChrTalk(    #25
        0xFE,
        "My wife and son are in Bose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Once we're done cleaning up here,\x01",
            "I'm going to rush over there as fast\x01",
            "as I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101F")

    label("loc_F39")


    ChrTalk(    #27
        0xFE,
        (
            "I heard the dragon hit Bose, too.\x01",
            "I'm worried, damn it, but I can't\x01",
            "abandon the folks here, either...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "My wife and son are in Bose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Once we're done cleaning up here,\x01",
            "I'm going to rush over there as fast\x01",
            "as I can.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_101F")

    TalkEnd(0x9)
    Return()

    # Function_12_EAA end

    def Function_13_1023(): pass

    label("Function_13_1023")

    TalkBegin(0xA)
    OP_63(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1033")
    Jump("loc_1392")

    label("loc_1033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_11BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_10E1")

    ChrTalk(    #30
        0xFE,
        (
            "Lewey and the other children were born\x01",
            "after the war, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I'd hoped we could spare them from ever\x01",
            "having to go through something like this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B7")

    label("loc_10E1")


    ChrTalk(    #32
        0xFE,
        (
            "I left Lewey at the bar, but I'm worried\x01",
            "about him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "He saw all of it. The destruction, the dragon\x01",
            "torching the orchards in all its fury...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I always hoped we could spare the\x01",
            "children such horrors.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_11B7")

    Jump("loc_1392")

    label("loc_11BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1392")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1271")

    ChrTalk(    #35
        0xFE,
        (
            "It was thanks to Agate that we were\x01",
            "able to stop the spread of the fire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Last thing I expected him to use\x01",
            "that sword for was chop down the\x01",
            "trees, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1392")

    label("loc_1271")


    ChrTalk(    #37
        0xFE,
        (
            "While we were fighting the fires,\x01",
            "Agate arrived from out of the blue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "He used that huge sword of his\x01",
            "to cut down some burning trees,\x01",
            "roots and all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Thanks to that, the fire didn't\x01",
            "spread any farther.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "I'll admit, all I could do was just\x01",
            "stand there and stare in awe!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1392")

    TalkEnd(0xA)
    Return()

    # Function_13_1023 end

    def Function_14_1396(): pass

    label("Function_14_1396")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_13A3")
    Jump("loc_1496")

    label("loc_13A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_13AD")
    Jump("loc_1496")

    label("loc_13AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1496")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1405")

    ChrTalk(    #41
        0xFE,
        "This is terrible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "The orchards...\x01",
            "The orchards are ruined!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1496")

    label("loc_1405")


    ChrTalk(    #43
        0xFE,
        "This is terrible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "The orchards...\x01",
            "The orchards are ruined!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "It even got Pesca's tractor...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "Damn you, dragon... Damn you!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1496")

    TalkEnd(0xD)
    Return()

    # Function_14_1396 end

    def Function_15_149A(): pass

    label("Function_15_149A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B7")
    Call(0, 21)

    label("loc_14B7")

    OP_6D(-1780, 0, 9660, 0)
    OP_67(0, 7460, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(171000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1220, 0, 7010, 0)
    SetChrPos(0x107, -2340, 0, 6850, 0)
    SetChrPos(0xF8, -1430, 0, 5450, 0)
    SetChrPos(0xF9, -2520, 0, 5280, 0)

    def lambda_153E():
        OP_8E(0xFE, 0xFFFFFB3C, 0x0, 0x2B02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_153E)
    Sleep(100)

    def lambda_155E():
        OP_8E(0xFE, 0xFFFFF6DC, 0x0, 0x2A62, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_155E)
    Sleep(100)

    def lambda_157E():
        OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x24EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_157E)
    Sleep(100)

    def lambda_159E():
        OP_8E(0xFE, 0xFFFFF628, 0x0, 0x2440, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_159E)
    OP_C8(0x200, 0x46, "C_PLAC15._CH", 0x1, 0x7D0)
    OP_DE("Ravennue Village")
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 45, 400)

    ChrTalk(    #47
        0x101,
        "#1020F#5PNo way...\x02",
    )

    CloseMessageWindow()

    def lambda_1629():
        OP_6D(20180, 0, 8950, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1629)

    def lambda_1641():
        OP_67(0, 11500, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1641)

    def lambda_1659():
        OP_6B(2200, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1659)

    def lambda_1669():
        OP_6C(30000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1669)

    def lambda_1679():
        OP_6E(412, 10000)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1679)
    OP_8C(0x101, 90, 400)

    def lambda_1690():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1690)
    Sleep(100)

    def lambda_16A3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_16A3)
    Sleep(100)

    def lambda_16B6():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_16B6)
    WaitChrThread(0x101, 0x2)
    Sleep(2000)
    SetChrPos(0x101, 8930, 0, 9620, 90)
    SetChrPos(0x107, 8540, 0, 10360, 90)
    SetChrPos(0xF8, 9090, 0, 8720, 90)
    SetChrPos(0xF9, 8170, 0, 11260, 90)
    Fade(500)
    OP_6D(9120, 0, 10270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #48
        0x101,
        "#1026F#6PThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x107,
        "#065F#6PIt's awful!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1834")

    ChrTalk(    #50
        0x103,
        (
            "#022F#6PLet's try and find the village elder.\x01",
            "He's the one who contacted us.\x02\x03",

            "If anyone knows where Agate and the dragon\x01",
            "went, it will probably be him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1996")

    label("loc_1834")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18EA")

    ChrTalk(    #51
        0x105,
        (
            "#043F#6PI think...for the moment, the best thing\x01",
            "we can do is try to find the village elder.\x02\x03",

            "He should, hopefully, know what happened\x01",
            "to the dragon and Agate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1996")

    label("loc_18EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1996")

    ChrTalk(    #52
        0x104,
        (
            "#032F#6PWe should begin by finding the head\x01",
            "of this village, I think.\x02\x03",

            "If anyone knows where our Raven-knight and\x01",
            "flying legend fled to, it will be him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1996")


    ChrTalk(    #53
        0x101,
        "#1003F#6PYeah...let's look.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A14)
    OP_28(0x94, 0x1, 0x2)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_15_149A end

    def Function_16_19C8(): pass

    label("Function_16_19C8")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19E9")
    Call(0, 21)
    FadeToBright(0, 0)
    Sleep(200)

    label("loc_19E9")

    Fade(1000)
    OP_6D(25120, -4000, 16950, 0)
    OP_67(0, 6370, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 26060, -4000, 17030, 270)
    SetChrPos(0x107, 26140, -4000, 15780, 270)
    SetChrPos(0xF8, 27550, -4000, 16800, 270)
    SetChrPos(0xF9, 27620, -4000, 15500, 270)
    OP_8C(0x8, 270, 0)
    OP_0D()

    ChrTalk(    #54
        0x101,
        "#1002F#4PSir!\x02",
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    OP_63(0x8)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 90, 400)

    ChrTalk(    #55
        0x8,
        "#6PHmmm...? I remember you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "#6PHave you come all the way from the\x01",
            "guild in Bose?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B64")

    ChrTalk(    #57
        0x103,
        "#020F#2PYes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#1004F#4PYou remember us, sir?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B9F")

    label("loc_1B64")


    ChrTalk(    #59
        0x101,
        (
            "#1004F#4PYeah, that's right...\x02\x03",

            "You remember us, sir?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C76")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as cleared monster hunt on mountain roads in FC\x01",            # 0
            "Set as did not clear monster hunt on mountain roads in FC\x01",      # 1
            "No change\x01",                                                      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C5D"),
        (1, "loc_1C65"),
        (SWITCH_DEFAULT, "loc_1C6D"),
    )


    label("loc_1C5D")

    OP_28(0xE, 0x4, 0x10)
    Jump("loc_1C6D")

    label("loc_1C65")

    OP_28(0xE, 0x3, 0x10)
    Jump("loc_1C6D")

    label("loc_1C6D")

    FadeToBright(300, 0)

    label("loc_1C76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1D0C")

    ChrTalk(    #60
        0x8,
        (
            "#6PYes, you slew those monsters for us,\x01",
            "and you helped with the bandits as well!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        "#6PIt'd be hard to forget you after all that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D83")

    label("loc_1D0C")


    ChrTalk(    #62
        0x8,
        (
            "#6PYes, well, even the army showed up for that\x01",
            "bandit mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        "#6PIt'd be hard to forget any of you after that.\x02",
    )

    CloseMessageWindow()

    label("loc_1D83")


    ChrTalk(    #64
        0x101,
        (
            "#1025F#4PI see...\x02\x03",

            "#1020FOh, no, never mind that!\x01",
            "Where did the dragon go?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x107,
        "#063F#2PAnd, um, um, Agate! Where's Agate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        "#6PAh, um, yes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        "#6PAfter burning the orchards, the dragon flew north.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        (
            "#6PAgate showed up right afterwards and\x01",
            "helped put out the fire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        "#6P...but when it was over, he simply...vanished.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x107,
        "#065F#2PAgate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1015F#4PAre you sure he didn't go off\x01",
            "to find his sister?\x02\x03",

            "She lives here, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        "#6PHis...what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#6PI see. So that's what Agate tells people,\x01",
            "is it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1026F#4PPardon...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x107,
        "#065F#2PUm, um... What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#6PI did check earlier.\x01",
            "Agate is...not with Mischa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        "#6PHe's not at his house, either.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 1)), scpexpr(EXPR_END)), "loc_21AB")

    ChrTalk(    #78
        0x101,
        (
            "#1015F#4PI see...\x02\x03",

            "#1007FSo he must've gone after the dra--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #79
        0x101,
        (
            "#1020F#4P(Wait, hold on!)\x02\x03",

            "('Mischa'... I'm sure I've seen that...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #80
        0x107,
        "#064F#5PEstelle? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x101, 0x107, 600)

    ChrTalk(    #81
        0x101,
        (
            "#1016F#4PUh, no, it's nothing.\x02\x03",

            "#1003F(Anyway...finding Agate's gotta come first.)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    OP_8C(0x107, 270, 400)
    Jump("loc_21F4")

    label("loc_21AB")


    ChrTalk(    #82
        0x101,
        (
            "#1015F#4PI see...\x02\x03",

            "#1007FSo he must've gone after the dragon, then.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2279")

    ChrTalk(    #83
        0x103,
        (
            "#022F#2PNorth of here... That must mean the abandoned\x01",
            "mine where the bandits were hiding that one time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E2")

    label("loc_2279")


    ChrTalk(    #84
        0x103,
        (
            "#022F#2PNorth of here... That must mean the abandoned\x01",
            "mine the Intelligence Division was hiding in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E2")

    Jump("loc_23B7")

    label("loc_22E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2359")

    ChrTalk(    #85
        0x104,
        (
            "#032F#2PIf I recall the map of Liberl correctly,\x01",
            "there should be a mine to the north\x01",
            "of here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23B7")

    label("loc_2359")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23B7")

    ChrTalk(    #86
        0x105,
        (
            "#042F#2PNorth of here... That would lead to the old\x01",
            "Ravennue septium mine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2410")

    ChrTalk(    #87
        0x108,
        (
            "#070F#2PHmm. Sir Elder! Is there anything\x01",
            "we can do to assist you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B3")

    label("loc_2410")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2467")

    ChrTalk(    #88
        0x105,
        (
            "#043F#2PPardon me, Elder Reisen...\x01",
            "Can we be of help in any way?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B3")

    label("loc_2467")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B3")

    ChrTalk(    #89
        0x104,
        (
            "#030F#2PHm. My good sir, do you require\x01",
            "any aid from us?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24B3")


    ChrTalk(    #90
        0x8,
        "#6POh, no, you don't need to fret over us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#6PWe managed to get the fires out,\x01",
            "so all that's left now is cleaning\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        "#6PMore importantly...please, help Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "#6PWhen he's in...this sort of state,\x01",
            "there's no telling what he might do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1002F#4PG-Got it!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 500)
    Sleep(300)

    ChrTalk(    #95
        0x101,
        (
            "#1005F#6PEveryone, come on! Let's search the\x01",
            "road leading to that mine!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 500)

    ChrTalk(    #96
        0x107,
        "#062F#5POkay!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A15)
    OP_28(0x94, 0x1, 0x4)
    OP_28(0x94, 0x1, 0x8)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_16_19C8 end

    def Function_17_2654(): pass

    label("Function_17_2654")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_44(0x8, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_6D(18470, -4000, 12420, 0)
    OP_67(0, 13920, -10000, 0)
    OP_6B(4470, 0)
    OP_6C(317000, 0)
    OP_6E(255, 0)
    StopSound(0x7D00, 0x3D090, 0x0)
    FadeToBright(1000, 0)

    def lambda_26E2():
        OP_6D(-16410, -4000, 57810, 12000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_26E2)
    OP_6C(298000, 12000)

    def lambda_2703():
        OP_6E(230, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2703)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1210   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_17_2654 end

    def Function_18_272B(): pass

    label("Function_18_272B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_END)), "loc_2A7C")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2753")
    Call(0, 22)
    FadeToBright(0, 0)
    Sleep(200)

    label("loc_2753")


    ChrTalk(    #97
        0x101,
        (
            "#1015F(So, lesse, I've told the story to Tita...)\x02\x03",

            "(Is there anything else we need to do?)\x02",
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
            "Return to the City of Bose\x01",      # 0
            "Stay A While\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2841")
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_2A79")

    label("loc_2841")

    Fade(1000)
    OP_6D(-2410, 0, 7020, 0)
    OP_67(0, 7660, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -2130, 0, 7650, 180)
    SetChrPos(0xF7, -1120, 0, 6000, 0)
    SetChrPos(0xF8, -2480, 0, 5960, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2910")

    ChrTalk(    #98
        0x103,
        (
            "#020FRight, then. Let's get back to\x01",
            "Bose before the sun sets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29BC")

    label("loc_2910")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2965")

    ChrTalk(    #99
        0x108,
        (
            "#070FAll right! Let us return to the city\x01",
            "before the sun sets.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29BC")

    label("loc_2965")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29BC")

    ChrTalk(    #100
        0x104,
        (
            "#030FCome, then! Let us away to the city\x01",
            "before the coming of dusk.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29BC")


    ChrTalk(    #101
        0x101,
        (
            "#1006F#4PGood idea.\x02\x03",

            "We'll probably hear back from the general tonight,\x01",
            "so we'd better hurry back to the guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1104   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2A79")

    Jump("loc_2DF9")

    label("loc_2A7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_2DF9")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C37")
    TurnDirection(0x101, 0x0, 400)

    ChrTalk(    #102
        0x101,
        (
            "#1004FOh, I should tell Tita the whole story before\x01",
            "we go back to Bose.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x101, 400)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (2, "loc_2B05"),
        (7, "loc_2B46"),
        (3, "loc_2B88"),
        (4, "loc_2BE3"),
        (SWITCH_DEFAULT, "loc_2C34"),
    )


    label("loc_2B05")


    ChrTalk(    #103
        0x103,
        (
            "#023FTita should be in the small house to the\x01",
            "northwest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C34")

    label("loc_2B46")


    ChrTalk(    #104
        0x108,
        (
            "#073FShe should be in that small house northwest\x01",
            "of here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C34")

    label("loc_2B88")


    ChrTalk(    #105
        0x104,
        (
            "#033FOur mechanical cherub will likely be in the\x01",
            "small residence to the northwest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C34")

    label("loc_2BE3")


    ChrTalk(    #106
        0x105,
        (
            "#044FWe should likely find her in the small\x01",
            "home just northwest of here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C34")

    label("loc_2C34")

    Jump("loc_2DD9")

    label("loc_2C37")

    TurnDirection(0x101, 0x1, 400)

    ChrTalk(    #107
        0x101,
        (
            "#1004FOh, I should tell Tita the whole story before\x01",
            "we go back to Bose.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1, 0x101, 400)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_END)),
        (2, "loc_2CAA"),
        (7, "loc_2CEB"),
        (3, "loc_2D2D"),
        (4, "loc_2D88"),
        (SWITCH_DEFAULT, "loc_2DD9"),
    )


    label("loc_2CAA")


    ChrTalk(    #108
        0x103,
        (
            "#020FTita should be in the small house to the\x01",
            "northwest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD9")

    label("loc_2CEB")


    ChrTalk(    #109
        0x108,
        (
            "#070FShe should be in that small house northwest\x01",
            "of here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD9")

    label("loc_2D2D")


    ChrTalk(    #110
        0x104,
        (
            "#030FOur mechanical cherub will likely be in the\x01",
            "small residence to the northwest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD9")

    label("loc_2D88")


    ChrTalk(    #111
        0x105,
        (
            "#040FWe should likely find her in the small home\x01",
            "just northwest of here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DD9")

    label("loc_2DD9")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2DF9")

    Return()

    # Function_18_272B end

    def Function_19_2DFA(): pass

    label("Function_19_2DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_337C")
    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, 33350, 8000, 36400, 180)
    SetChrPos(0x107, 33770, 8000, 37410, 180)
    SetChrPos(0xF8, 32590, 8000, 37110, 180)
    SetChrPos(0xF9, 33210, 8000, 38210, 180)
    OP_6D(33180, 8000, 36770, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 5)), scpexpr(EXPR_END)), "loc_31FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30CB")
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #112
        (
            "\x07\x05The six good souls lost in the fires of war sleep here.\x01",
            "《Septian Calendar 1192》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #113
        (
            "\x07\x05Lief, Abel, Nicole, Vim, Ileana, Mischa.\x01",
            "May you rest peacefully by the Goddess' side.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #114
        0x101,
        (
            "#1020F#6P(Wait a second...!)\x02\x03",

            "(Mischa... That's the person the elder talked\x01",
            "about a bit ago...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #115
        0x107,
        "#064F#6PWhat is it, Estelle?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x101, 0x107, 600)

    ChrTalk(    #116
        0x101,
        (
            "#1016F#3PN-No, it's nothing.\x02\x03",

            "#1003F(I'm really curious now, but we need to\x01",
            "chase after Agate first.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A81)
    Jump("loc_31F9")

    label("loc_30CB")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #117
        (
            "\x07\x05The six good souls lost in the fires of war sleep here.\x01",
            "《Septian Calendar 1192》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #118
        (
            "\x07\x05Lief, Abel, Nicole, Vim, Ileana, Mischa.\x01",
            "May you rest peacefully by the Goddess' side.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #119
        0x101,
        (
            "#1003F#6P(I'm really curious now, but we need to\x01",
            "chase after Agate first.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31F9")

    Jump("loc_3372")

    label("loc_31FC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #120
        (
            "\x07\x05The six good souls lost in the fires of war sleep here.\x01",
            "《Septian Calendar 1192》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #121
        (
            "\x07\x05Lief, Abel, Nicole, Vim, Ileana, Mischa.\x01",
            "May you rest peacefully by the Goddess' side.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #122
        0x101,
        (
            "#1015F#6P(Huh, Mischa.\x01",
            "I feel like I've heard that name...)\x02\x03",

            "#1002F(Crap! I need to get over to the village elder\x01",
            "and hear what he has to say!)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A81)

    label("loc_3372")

    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_3468")

    label("loc_337C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #123
        (
            "\x07\x05The six good souls lost in the fires of war sleep here.\x01",
            "《Septian Calendar 1192》\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #124
        (
            "\x07\x05Lief, Abel, Nicole, Vim, Ileana, Mischa.\x01",
            "May you rest peacefully by the Goddess' side.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_3468")

    Return()

    # Function_19_2DFA end

    def Function_20_3469(): pass

    label("Function_20_3469")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #125
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_3469 end

    def Function_21_34B8(): pass

    label("Function_21_34B8")

    FadeToDark(0, 0, -1)
    OP_6D(-32830, 0, 10760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
        (0, "loc_356E"),
        (1, "loc_3574"),
        (SWITCH_DEFAULT, "loc_357A"),
    )


    label("loc_356E")

    OP_A2(0x1200)
    Jump("loc_357A")

    label("loc_3574")

    OP_A2(0x1201)
    Jump("loc_357A")

    label("loc_357A")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x6, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_21_34B8 end

    def Function_22_35B4(): pass

    label("Function_22_35B4")

    FadeToDark(0, 0, -1)
    OP_6D(-32830, 0, 10760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
        (0, "loc_366A"),
        (1, "loc_3670"),
        (SWITCH_DEFAULT, "loc_3676"),
    )


    label("loc_366A")

    OP_A2(0x1200)
    Jump("loc_3676")

    label("loc_3670")

    OP_A2(0x1201)
    Jump("loc_3676")

    label("loc_3676")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x3, 0x0, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_22_35B4 end

    def Function_23_36AE(): pass

    label("Function_23_36AE")

    SetPlaceName(0x2E)
    Return()

    # Function_23_36AE end

    def Function_24_36B2(): pass

    label("Function_24_36B2")

    SetPlaceName(0x2D)
    Return()

    # Function_24_36B2 end

    def Function_25_36B6(): pass

    label("Function_25_36B6")

    SetPlaceName(0x2F)
    Return()

    # Function_25_36B6 end

    def Function_26_36BA(): pass

    label("Function_26_36BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_38F8")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3742")

    ChrTalk(    #126
        0x101,
        (
            "#1015FRight, there's no reason for us\x01",
            "to head to the mines at this point.\x01",
            "Let's get to Agate's house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D8")

    label("loc_3742")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_379E")

    ChrTalk(    #127
        0x103,
        (
            "#020FWe have no more business at the mines.\x01",
            "Let's get to Agate's house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D8")

    label("loc_379E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3813")

    ChrTalk(    #128
        0x105,
        (
            "#040FThere's no reason for us to head\x01",
            "to the mines at this point. We should\x01",
            "go to Agate's house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D8")

    label("loc_3813")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_387F")

    ChrTalk(    #129
        0x104,
        (
            "#030FThe mines hold little value for us at\x01",
            "this point. We should head to Agate's\x01",
            "house.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38D8")

    label("loc_387F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38D8")

    ChrTalk(    #130
        0x108,
        (
            "#070FWe have no more business at the\x01",
            "mines. Let's get to Agate's house.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D8")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_38F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B78")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_397A")

    ChrTalk(    #131
        0x101,
        (
            "#1016FWait, this way leads to the mines,\x01",
            "not Bose. We need to go through the\x01",
            "south exit, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B58")

    label("loc_397A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39FB")

    ChrTalk(    #132
        0x103,
        (
            "#020FThis way will take us toward the old\x01",
            "mines. We should use the south exit\x01",
            "if we want to go back to Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B58")

    label("loc_39FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A7C")

    ChrTalk(    #133
        0x105,
        (
            "#040FThis road leads to the old mines.\x01",
            "We need to use the road to the south\x01",
            "if we want to head back to Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B58")

    label("loc_3A7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD7")

    ChrTalk(    #134
        0x104,
        (
            "#030FThis route will lead us to the old mines.\x01",
            "Bose lies to the south.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B58")

    label("loc_3AD7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B58")

    ChrTalk(    #135
        0x108,
        (
            "#070FThis takes us to the abandoned mines.\x01",
            "We should use the road to the south if\x01",
            "we want to head back to Bose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B58")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_3B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E1A")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C02")

    ChrTalk(    #136
        0x101,
        (
            "#1002FWhat am I thinking? We don't have\x01",
            "time to mess around. We need to find\x01",
            "the village elder, pronto!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DFA")

    label("loc_3C02")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C67")

    ChrTalk(    #137
        0x103,
        (
            "#022FWe do NOT have time for dilly-dallying.\x01",
            "We must find Elder Reisen, at once!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DFA")

    label("loc_3C67")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CC6")

    ChrTalk(    #138
        0x105,
        (
            "#042FWe have no time to lose. We must find\x01",
            "Elder Reisen as soon as we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DFA")

    label("loc_3CC6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D3E")

    ChrTalk(    #139
        0x104,
        (
            "#032FThis is no time to get sidetracked.\x01",
            "We should locate the village elder as\x01",
            "soon as as possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DFA")

    label("loc_3D3E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D9B")

    ChrTalk(    #140
        0x107,
        (
            "#063FWe can't waste any time! We need\x01",
            "to find the leader of the village!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3DFA")

    label("loc_3D9B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DFA")

    ChrTalk(    #141
        0x108,
        (
            "#072FWe've got no time to waste.\x01",
            "We need to find the village elder,\x01",
            "and fast.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DFA")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_3E1A")

    Return()

    # Function_26_36BA end

    def Function_27_3E1B(): pass

    label("Function_27_3E1B")

    ClearMapFlags(0x2000000)
    Return()

    # Function_27_3E1B end

    def Function_28_3E21(): pass

    label("Function_28_3E21")

    EventBegin(0x1)

    ChrTalk(    #142
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_3E4D():
        OP_6D(35190, -3850, 5430, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_3E4D)

    def lambda_3E65():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3E65)

    def lambda_3E75():
        OP_6C(225000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_3E75)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #143
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F1B")
    OP_C0(0xE, 0xA, 0x88F4, 0xFFFFF0F6, 0x2044, 0xB4, 0x88C2, 0xFFFFEF98, 0x1446)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_3F2A")

    label("loc_3F1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F2A")
    EventEnd(0x1)

    label("loc_3F2A")

    Return()

    # Function_28_3E21 end

    SaveToFile()

Try(main)
