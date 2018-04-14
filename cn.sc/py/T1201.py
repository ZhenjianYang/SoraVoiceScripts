from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '莱森村长',                             # 9
        '罗亚',                                 # 10
        '菲戈',                                 # 11
        '贝斯卡',                               # 12
        '库赖老人',                             # 13
        '巴德斯',                               # 14
        '拉文努山道方向',                       # 15
        '拉文努废坑方向',                       # 16
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
        "Function_10_950",         # 0A, 10
        "Function_11_AF1",         # 0B, 11
        "Function_12_CD5",         # 0C, 12
        "Function_13_D9A",         # 0D, 13
        "Function_14_F88",         # 0E, 14
        "Function_15_1051",        # 0F, 15
        "Function_16_147B",        # 10, 16
        "Function_17_1E74",        # 11, 17
        "Function_18_1F49",        # 12, 18
        "Function_19_2426",        # 13, 19
        "Function_20_299D",        # 14, 20
        "Function_21_29E3",        # 15, 21
        "Function_22_2AE0",        # 16, 22
        "Function_23_2BDB",        # 17, 23
        "Function_24_2BDF",        # 18, 24
        "Function_25_2BE3",        # 19, 25
        "Function_26_2BE7",        # 1A, 26
        "Function_27_30A2",        # 1B, 27
        "Function_28_30A8",        # 1C, 28
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 5)), scpexpr(EXPR_END)), "loc_93D")

    ChrTalk(    #0
        0xFE,
        (
            "这里没事的，\x01",
            "阿加特就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "他好像一脸\x01",
            "很沉重的表情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_94C")

    label("loc_93D")

    Call(0, 16)
    OP_8C(0x8, 180, 0)
    OP_4B(0x8, 255)

    label("loc_94C")

    TalkEnd(0x8)
    Return()

    # Function_9_8EC end

    def Function_10_950(): pass

    label("Function_10_950")

    TalkBegin(0xC)
    OP_63(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_960")
    Jump("loc_AED")

    label("loc_960")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_A4E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9C1")

    ChrTalk(    #2
        0xFE,
        (
            "必须要和年轻人一起\x01",
            "好好考虑将来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "要重建果树园\x01",
            "需要所有人的团结啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A4B")

    label("loc_9C1")


    ChrTalk(    #4
        0xFE,
        "唉……真难受啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "但是，光是叹息\x01",
            "什么也无法开始。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "支撑村子的\x01",
            "果树园不行了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "必须要和年轻人一起\x01",
            "好好考虑将来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_A4B")

    Jump("loc_AED")

    label("loc_A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_AED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_A91")

    ChrTalk(    #8
        0xFE,
        "呼，真残酷……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_AED")

    label("loc_A91")


    ChrTalk(    #10
        0xFE,
        "呼，真残酷……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "至今一直倾注了心血\x01",
            "培育出来的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_AED")

    TalkEnd(0xC)
    Return()

    # Function_10_950 end

    def Function_11_AF1(): pass

    label("Function_11_AF1")

    TalkBegin(0xB)
    OP_63(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_B01")
    Jump("loc_CD1")

    label("loc_B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_BF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_B6A")

    ChrTalk(    #13
        0xFE,
        (
            "我也有保护自己\x01",
            "家人生活的义务。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "那果树园该怎么办，\x01",
            "首先要和村里的人谈谈才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF0")

    label("loc_B6A")


    ChrTalk(    #15
        0xFE,
        "呼……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "虽然难过……\x01",
            "但现在不是消沉的时候。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "为了家人\x01",
            "必须考虑将来的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "果树园该怎么办，\x01",
            "需要和村里人好好谈谈。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_BF0")

    Jump("loc_CD1")

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_CD1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_C3B")

    ChrTalk(    #19
        0xFE,
        (
            "现在应该\x01",
            "考虑将来的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "……首先是收拾善后。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CD1")

    label("loc_C3B")


    ChrTalk(    #21
        0xFE,
        (
            "好、好不容易引进的\x01",
            "导力式拖拉机……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "……总、总之现在\x01",
            "要先收拾善后才行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "考虑将来的事\x01",
            "等做完这个再说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_CD1")

    TalkEnd(0xB)
    Return()

    # Function_11_AF1 end

    def Function_12_CD5(): pass

    label("Function_12_CD5")

    TalkBegin(0x9)
    OP_63(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_D96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D2D")

    ChrTalk(    #25
        0xFE,
        "我妻子和孩子都在柏斯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "这里收拾完了\x01",
            "我打算马上去那边。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D96")

    label("loc_D2D")


    ChrTalk(    #27
        0xFE,
        (
            "柏斯那边\x01",
            "似乎也遭到了龙的破坏。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "我妻子和孩子都在柏斯。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "这里收拾完了\x01",
            "我打算马上去那边。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D96")

    TalkEnd(0x9)
    Return()

    # Function_12_CD5 end

    def Function_13_D9A(): pass

    label("Function_13_D9A")

    TalkBegin(0xA)
    OP_63(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_DAA")
    Jump("loc_F84")

    label("loc_DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_E8A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E09")

    ChrTalk(    #30
        0xFE,
        (
            "鲁伊他们是战后\x01",
            "才出生的一代嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "可能的话真不想\x01",
            "让他们有这种遭遇……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E87")

    label("loc_E09")


    ChrTalk(    #32
        0xFE,
        (
            "托付给酒馆的\x01",
            "鲁伊真令人担心……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "他好像看到了龙的样子，\x01",
            "变得非常胆怯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "真不想让那孩子\x01",
            "留下这么可怕的回忆……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_E87")

    Jump("loc_F84")

    label("loc_E8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_F84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EE1")

    ChrTalk(    #35
        0xFE,
        (
            "多亏了阿加特\x01",
            "才防止了火势扩大。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "没想到他竟然\x01",
            "用剑砍倒大树。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F84")

    label("loc_EE1")


    ChrTalk(    #37
        0xFE,
        (
            "正在果园进行灭火的时候\x01",
            "阿加特突然赶来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "用那巨大的剑\x01",
            "砍倒了大树。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "多亏有他，\x01",
            "火势没有再扩大……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "不、不过实在是太可怕了，\x01",
            "都被吓的腿软了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F84")

    TalkEnd(0xA)
    Return()

    # Function_13_D9A end

    def Function_14_F88(): pass

    label("Function_14_F88")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_F95")
    Jump("loc_104D")

    label("loc_F95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_F9F")
    Jump("loc_104D")

    label("loc_F9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_104D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_FDE")

    ChrTalk(    #41
        0xFE,
        "好过分……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "果树园被弄得乱七八糟……\x02",
    )

    CloseMessageWindow()
    Jump("loc_104D")

    label("loc_FDE")


    ChrTalk(    #43
        0xFE,
        "好过分……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "果树园被弄得乱七八糟……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "连贝斯卡的\x01",
            "拖拉机都……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "可恶的龙……\x01",
            "绝对饶不了你。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_104D")

    TalkEnd(0xD)
    Return()

    # Function_14_F88 end

    def Function_15_1051(): pass

    label("Function_15_1051")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_106E")
    Call(0, 21)

    label("loc_106E")

    OP_6D(-1780, 0, 9660, 0)
    OP_67(0, 7460, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(171000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -1220, 0, 7010, 0)
    SetChrPos(0x107, -2340, 0, 6850, 0)
    SetChrPos(0xF8, -1430, 0, 5450, 0)
    SetChrPos(0xF9, -2520, 0, 5280, 0)

    def lambda_10F5():
        OP_8E(0xFE, 0xFFFFFB3C, 0x0, 0x2B02, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10F5)
    Sleep(100)

    def lambda_1115():
        OP_8E(0xFE, 0xFFFFF6DC, 0x0, 0x2A62, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1115)
    Sleep(100)

    def lambda_1135():
        OP_8E(0xFE, 0xFFFFFA6A, 0x0, 0x24EA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_1135)
    Sleep(100)

    def lambda_1155():
        OP_8E(0xFE, 0xFFFFF628, 0x0, 0x2440, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_1155)
    OP_C8(0x200, 0x46, "C_PLAC15._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 45, 400)

    ChrTalk(    #47
        0x101,
        "#1020F#5P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_11CB():
        OP_6D(20180, 0, 8950, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11CB)

    def lambda_11E3():
        OP_67(0, 11500, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11E3)

    def lambda_11FB():
        OP_6B(2200, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11FB)

    def lambda_120B():
        OP_6C(30000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_120B)

    def lambda_121B():
        OP_6E(412, 10000)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_121B)
    OP_8C(0x101, 90, 400)

    def lambda_1232():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1232)
    Sleep(100)

    def lambda_1245():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1245)
    Sleep(100)

    def lambda_1258():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1258)
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
        "#1026F#6P这、这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x107,
        "#065F#6P好、好过分……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1390")

    ChrTalk(    #50
        0x103,
        (
            "#022F#6P……总之，先找到\x01",
            "给我们联络的村长吧。\x02\x03",

            "他应该知道龙和\x01",
            "阿加特的去向。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_1390")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F3")

    ChrTalk(    #51
        0x105,
        (
            "#043F#6P……总之，先找到\x01",
            "给我们联络的村长吧。\x02\x03",

            "他应该知道龙和\x01",
            "阿加特的去向。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_144F")

    label("loc_13F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_144F")

    ChrTalk(    #52
        0x104,
        (
            "#032F#6P总之先找到\x01",
            "给我们联络的村长吧。\x02\x03",

            "他应该知道龙和\x01",
            "阿加特的去向吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_144F")


    ChrTalk(    #53
        0x101,
        "#1003F#6P嗯……对呢。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A14)
    OP_28(0x94, 0x1, 0x2)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_15_1051 end

    def Function_16_147B(): pass

    label("Function_16_147B")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_149C")
    Call(0, 21)
    FadeToBright(0, 0)
    Sleep(200)

    label("loc_149C")

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
        "#1002F#4P村长先生！\x02",
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
        "#5P噢……你们是那时的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "#5P从柏斯市的协会\x01",
            "特地来的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1601")

    ChrTalk(    #57
        0x103,
        "#020F#4P嗯嗯，是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1004F#4P我们的事，\x01",
            "您还记得啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1639")

    label("loc_1601")


    ChrTalk(    #59
        0x101,
        (
            "#1004F#4P嗯，是这样的……\x02\x03",

            "我们的事，\x01",
            "您还记得啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16EB")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇前篇完成了山道的魔兽剿灭】\x01",      # 0
            "【◇前篇没完成山道的魔兽剿灭】\x01",      # 1
            "【◇什么也没有变更】\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_16D2"),
        (1, "loc_16DA"),
        (SWITCH_DEFAULT, "loc_16E2"),
    )


    label("loc_16D2")

    OP_28(0xE, 0x4, 0x10)
    Jump("loc_16E2")

    label("loc_16DA")

    OP_28(0xE, 0x3, 0x10)
    Jump("loc_16E2")

    label("loc_16E2")

    FadeToBright(300, 0)

    label("loc_16EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_174D")

    ChrTalk(    #60
        0x8,
        (
            "#5P啊啊，你们帮忙剿灭魔兽和解决了\x01",
            "那次的空贼事件嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        "#5P怎么可能会忘记呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1796")

    label("loc_174D")


    ChrTalk(    #62
        0x8,
        (
            "#5P啊啊，空贼事件的时候\x01",
            "连军队都来了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        "#5P怎么可能会忘记呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1796")


    ChrTalk(    #64
        0x101,
        (
            "#1025F#4P是吗……\x02\x03",

            "#1020F先、先不说这个了！\x01",
            "龙跑到哪儿去了！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x107,
        (
            "#063F#6P还、还有阿加特哥哥\x01",
            "去哪里了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        "#5P唔、唔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "#5P烧毁了果树园之后\x01",
            "龙就飞到北方去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        (
            "#5P就在那之后，阿加特突然出现\x01",
            "帮忙灭火……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "#5P可是火灭了之后，不知何时\x01",
            "他就不见了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x107,
        "#065F#6P！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1015F#4P会不会是\x01",
            "去她妹妹那里了？\x02\x03",

            "她住在村子里吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#5P是吗……\x01",
            "阿加特是这么说的吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#1026F#4P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x107,
        (
            "#065F#6P那个那个……\x01",
            "是怎么回事～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#5P之前我确认过了，阿加特\x01",
            "不在米夏身边。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        "#5P当然，他也没回家。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 1)), scpexpr(EXPR_END)), "loc_1B21")

    ChrTalk(    #78
        0x101,
        (
            "#1015F#4P这、这样啊……\x02\x03",

            "#1007F那果然\x01",
            "是去追龙了吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #79
        0x101,
        (
            "#1020F#4P（等、等一下……！）\x02\x03",

            "（米夏……\x01",
            "　记得是刚刚看到的……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #80
        0x107,
        "#064F#6P怎么了，姐姐？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x101, 0x107, 600)

    ChrTalk(    #81
        0x101,
        (
            "#1016F#2P不、不，没什么。\x02\x03",

            "#1003F（总、总之，\x01",
            "　应该先找到阿加特……）\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    OP_8C(0x107, 270, 400)
    Jump("loc_1B5D")

    label("loc_1B21")


    ChrTalk(    #82
        0x101,
        (
            "#1015F#4P这、这样啊……\x02\x03",

            "#1007F那果然\x01",
            "是去追龙了吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B5D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1BB0")

    ChrTalk(    #83
        0x103,
        (
            "#022F#4P这边往北……\x01",
            "是空贼们藏着定期船的废坑方向吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BE9")

    label("loc_1BB0")


    ChrTalk(    #84
        0x103,
        (
            "#022F#4P这边往北……\x01",
            "是特务兵作为基地的废坑方向吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BE9")

    Jump("loc_1C75")

    label("loc_1BEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C30")

    ChrTalk(    #85
        0x104,
        (
            "#032F#4P根据王国地图，北边\x01",
            "好像有连续的山道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C75")

    label("loc_1C30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C75")

    ChrTalk(    #86
        0x105,
        (
            "#042F#4P这边往北……\x01",
            "是曾经有七耀石矿山的地方吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C75")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CB7")

    ChrTalk(    #87
        0x108,
        (
            "#070F#4P喔……老人家。\x01",
            "有什么可以帮忙的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D38")

    label("loc_1CB7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CF7")

    ChrTalk(    #88
        0x105,
        (
            "#043F#4P那个……现在\x01",
            "有什么可以帮忙的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D38")

    label("loc_1CF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D38")

    ChrTalk(    #89
        0x104,
        (
            "#030F#4P呼……老人家。\x01",
            "还有地方需要人手的吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D38")


    ChrTalk(    #90
        0x8,
        "#5P啊啊，不必费心。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#5P火总算是扑灭了，\x01",
            "现在就剩收拾善后了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#5P比起这个……\x01",
            "阿加特更重要，那就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "#5P他的表情看起来相当沉重，\x01",
            "不知道会做出什么乱来的事情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1002F#4P明、明白了。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 500)
    Sleep(300)

    ChrTalk(    #95
        0x101,
        (
            "#1005F#5P大家，赶快\x01",
            "去北边山道找找吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 500)

    ChrTalk(    #96
        0x107,
        "#062F#3P嗯、嗯！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A15)
    OP_28(0x94, 0x1, 0x4)
    OP_28(0x94, 0x1, 0x8)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_16_147B end

    def Function_17_1E74(): pass

    label("Function_17_1E74")

    EventBegin(0x0)
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

    def lambda_1F01():
        OP_6D(-16410, -4000, 57810, 12000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1F01)
    OP_6C(298000, 12000)

    def lambda_1F22():
        OP_6E(230, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F22)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T1210   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_17_1E74 end

    def Function_18_1F49(): pass

    label("Function_18_1F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_END)), "loc_221A")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F71")
    Call(0, 22)
    FadeToBright(0, 0)
    Sleep(200)

    label("loc_1F71")


    ChrTalk(    #97
        0x101,
        (
            "#1015F（嗯，姑且算是给提妲\x01",
            "　传了话，不过……）\x02\x03",

            "（还有什么事没做吗？）\x02",
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
            "【回柏斯市】\x01",        # 0
            "【还不能回去】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2040")
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Jump("loc_2217")

    label("loc_2040")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2101")

    ChrTalk(    #98
        0x103,
        (
            "#020F#6P好了，太阳也下山了，\x01",
            "差不多该回柏斯了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218E")

    label("loc_2101")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2149")

    ChrTalk(    #99
        0x108,
        (
            "#070F#6P好了，太阳也下山了，\x01",
            "差不多该回柏斯了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_218E")

    label("loc_2149")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_218E")

    ChrTalk(    #100
        0x104,
        (
            "#030F#6P好了，太阳也下山了，\x01",
            "差不多该回柏斯了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218E")


    ChrTalk(    #101
        0x101,
        (
            "#1006F#2P嗯，是啊。\x02\x03",

            "晚上会收到将军的联络，\x01",
            "要赶快返回柏斯才行。\x02",
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

    label("loc_2217")

    Jump("loc_2425")

    label("loc_221A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_2425")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_231C")
    TurnDirection(0x101, 0x0, 400)

    ChrTalk(    #102
        0x101,
        (
            "#1004F啊，回柏斯之前\x01",
            "要跟提妲说一声才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x101, 400)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (2, "loc_2285"),
        (7, "loc_22AA"),
        (3, "loc_22CF"),
        (4, "loc_22F4"),
        (SWITCH_DEFAULT, "loc_2319"),
    )


    label("loc_2285")


    ChrTalk(    #103
        0x103,
        (
            "#023F西北有间\x01",
            "小小的民房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2319")

    label("loc_22AA")


    ChrTalk(    #104
        0x108,
        (
            "#073F西北有间\x01",
            "小小的民房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2319")

    label("loc_22CF")


    ChrTalk(    #105
        0x104,
        (
            "#033F西北有间\x01",
            "小小的民房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2319")

    label("loc_22F4")


    ChrTalk(    #106
        0x105,
        (
            "#044F西北有间\x01",
            "小小的民房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2319")

    label("loc_2319")

    Jump("loc_2405")

    label("loc_231C")

    TurnDirection(0x101, 0x1, 400)

    ChrTalk(    #107
        0x101,
        (
            "#1004F啊，回柏斯之前\x01",
            "要跟提妲说一声才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1, 0x101, 400)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_END)),
        (2, "loc_2371"),
        (7, "loc_2396"),
        (3, "loc_23BB"),
        (4, "loc_23E0"),
        (SWITCH_DEFAULT, "loc_2405"),
    )


    label("loc_2371")


    ChrTalk(    #108
        0x103,
        (
            "#020F西北有间\x01",
            "小小的民房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2405")

    label("loc_2396")


    ChrTalk(    #109
        0x108,
        (
            "#070F西北有间\x01",
            "小小的民房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2405")

    label("loc_23BB")


    ChrTalk(    #110
        0x104,
        (
            "#030F西北有间\x01",
            "小小的民房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2405")

    label("loc_23E0")


    ChrTalk(    #111
        0x105,
        (
            "#040F西北有间\x01",
            "小小的民房吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2405")

    label("loc_2405")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2425")

    Return()

    # Function_18_1F49 end

    def Function_19_2426(): pass

    label("Function_19_2426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28D1")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 5)), scpexpr(EXPR_END)), "loc_27A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A0")
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #112
        (
            "\x07\x05七耀历１１９２年\x01",
            "由于战火而失去的\x01",
            "６个善良的灵魂，长眠与此。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #113
        (
            "\x07\x05雷夫、阿贝尔、尼高尔、\x01",
            "维姆、依蕾娜、米夏。\x01",
            "愿你们在女神的怀抱中得到安宁。\x02",
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
            "#1020F#4P（等、等一下……！）\x02\x03",

            "（米夏……\x01",
            "　刚才村长说过的……）\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #115
        0x107,
        "#064F#6P怎么了，姐姐？\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)
    TurnDirection(0x101, 0x107, 600)

    ChrTalk(    #116
        0x101,
        (
            "#1016F#5P不，不，没什么。\x02\x03",

            "#1003F（虽、虽然在意……\x01",
            "　但现在要先追上阿加特才行……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A81)
    Jump("loc_279F")

    label("loc_26A0")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #117
        (
            "\x07\x05七耀历１１９２年\x01",
            "由于战火而失去的\x01",
            "６个善良的灵魂，长眠与此。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #118
        (
            "\x07\x05雷夫、阿贝尔、尼高尔、\x01",
            "维姆、依蕾娜、米夏。\x01",
            "愿你们在女神的怀抱中得到安宁。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #119
        0x101,
        (
            "#1003F#4P（虽、虽然在意……\x01",
            "　但现在要先追上阿加特才行……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_279F")

    Jump("loc_28C7")

    label("loc_27A2")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #120
        (
            "\x07\x05七耀历１１９２年\x01",
            "由于战火而失去的\x01",
            "６个善良的灵魂，长眠与此。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #121
        (
            "\x07\x05雷夫、阿贝尔、尼高尔、\x01",
            "维姆、依蕾娜、米夏。\x01",
            "愿你们在女神的怀抱中得到安宁。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #122
        0x101,
        (
            "#1015F#6P（咦，米夏\x01",
            "　好像在哪儿听说过……）\x02\x03",

            "#1002F（……唔，不好！\x01",
            "　要赶快找村长问话才行！）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A81)

    label("loc_28C7")

    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_299C")

    label("loc_28D1")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #123
        (
            "\x07\x05七耀历１１９２年\x01",
            "由于战火而失去的\x01",
            "６个善良的灵魂，长眠与此。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #124
        (
            "\x07\x05雷夫、阿贝尔、尼高尔、\x01",
            "维姆、依蕾娜、米夏。\x01",
            "愿你们在女神的怀抱中得到安宁。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)

    label("loc_299C")

    Return()

    # Function_19_2426 end

    def Function_20_299D(): pass

    label("Function_20_299D")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #125
        "\x07\x05门上着锁。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_20_299D end

    def Function_21_29E3(): pass

    label("Function_21_29E3")

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
        (0, "loc_2A9A"),
        (1, "loc_2AA0"),
        (SWITCH_DEFAULT, "loc_2AA6"),
    )


    label("loc_2A9A")

    OP_A2(0x1200)
    Jump("loc_2AA6")

    label("loc_2AA0")

    OP_A2(0x1201)
    Jump("loc_2AA6")

    label("loc_2AA6")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x6, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_21_29E3 end

    def Function_22_2AE0(): pass

    label("Function_22_2AE0")

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
        (0, "loc_2B97"),
        (1, "loc_2B9D"),
        (SWITCH_DEFAULT, "loc_2BA3"),
    )


    label("loc_2B97")

    OP_A2(0x1200)
    Jump("loc_2BA3")

    label("loc_2B9D")

    OP_A2(0x1201)
    Jump("loc_2BA3")

    label("loc_2BA3")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x3, 0x0, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_22_2AE0 end

    def Function_23_2BDB(): pass

    label("Function_23_2BDB")

    SetPlaceName(0x2E)
    Return()

    # Function_23_2BDB end

    def Function_24_2BDF(): pass

    label("Function_24_2BDF")

    SetPlaceName(0x2D)
    Return()

    # Function_24_2BDF end

    def Function_25_2BE3(): pass

    label("Function_25_2BE3")

    SetPlaceName(0x2F)
    Return()

    # Function_25_2BE3 end

    def Function_26_2BE7(): pass

    label("Function_26_2BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D68")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C39")

    ChrTalk(    #126
        0x101,
        (
            "#1015F这边已经没事了。\x01",
            "得赶快去阿加特家里才是。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D48")

    label("loc_2C39")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C7C")

    ChrTalk(    #127
        0x103,
        (
            "#020F去废坑那边也无济于事。\x01",
            "赶快去阿加特家吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D48")

    label("loc_2C7C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CBD")

    ChrTalk(    #128
        0x105,
        (
            "#040F废坑方向已经没事了。\x01",
            "赶快去阿加特家吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D48")

    label("loc_2CBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D02")

    ChrTalk(    #129
        0x104,
        (
            "#030F这边已经没事了。\x01",
            "赶快去看看阿加特的情况吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D48")

    label("loc_2D02")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D48")

    ChrTalk(    #130
        0x108,
        (
            "#070F废坑这边已经没事了。\x01",
            "赶快去看看阿加特的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D48")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EE5")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB8")

    ChrTalk(    #131
        0x101,
        (
            "#1016F这边是废坑方向吧。\x01",
            "回柏斯得去南门才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC5")

    label("loc_2DB8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DFF")

    ChrTalk(    #132
        0x103,
        (
            "#020F这边的出口是废坑那边。\x01",
            "回柏斯的话要去南门吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC5")

    label("loc_2DFF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E40")

    ChrTalk(    #133
        0x105,
        (
            "#040F这边是废坑方向吧。\x01",
            "回柏斯得去南门才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC5")

    label("loc_2E40")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E85")

    ChrTalk(    #134
        0x104,
        (
            "#030F这边是废坑方向。\x01",
            "回柏斯得从南门出去才行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC5")

    label("loc_2E85")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EC5")

    ChrTalk(    #135
        0x108,
        (
            "#070F这边是废坑那边吧。\x01",
            "回柏斯的话要去南门吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC5")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_2EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30A1")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F3D")

    ChrTalk(    #136
        0x101,
        (
            "#1002F没时间四处闲逛了吧。\x01",
            "先得去找村长了解情况才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3081")

    label("loc_2F3D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F86")

    ChrTalk(    #137
        0x103,
        (
            "#022F没时间四处闲逛了。\x01",
            "先得去找村长了解情况才行哟。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3081")

    label("loc_2F86")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FC1")

    ChrTalk(    #138
        0x105,
        (
            "#042F没时间绕道了吧。\x01",
            "赶快去找村长吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3081")

    label("loc_2FC1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3000")

    ChrTalk(    #139
        0x104,
        (
            "#032F没时间四处闲逛了吧。\x01",
            "赶快去找村长吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3081")

    label("loc_3000")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3043")

    ChrTalk(    #140
        0x107,
        (
            "#063F四处闲逛可不行哦。\x01",
            "……先要找到村长才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3081")

    label("loc_3043")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3081")

    ChrTalk(    #141
        0x108,
        (
            "#072F没时间四处闲逛了吧。\x01",
            "先得去找村长问话。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3081")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)

    label("loc_30A1")

    Return()

    # Function_26_2BE7 end

    def Function_27_30A2(): pass

    label("Function_27_30A2")

    ClearMapFlags(0x2000000)
    Return()

    # Function_27_30A2 end

    def Function_28_30A8(): pass

    label("Function_28_30A8")

    EventBegin(0x1)

    ChrTalk(    #142
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_30D4():
        OP_6D(35190, -3850, 5430, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_30D4)

    def lambda_30EC():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_30EC)

    def lambda_30FC():
        OP_6C(225000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_30FC)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #143
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3183")
    OP_C0(0xE, 0xA, 0x88F4, 0xFFFFF0F6, 0x2044, 0xB4, 0x88C2, 0xFFFFEF98, 0x1446)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_3192")

    label("loc_3183")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3192")
    EventEnd(0x1)

    label("loc_3192")

    Return()

    # Function_28_30A8 end

    SaveToFile()

Try(main)
