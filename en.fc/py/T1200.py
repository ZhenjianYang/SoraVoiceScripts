from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1200   ._SN',
        MapName             = 'Bose',
        Location            = 'T1200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Vince',                                # 9
        'Fran',                                 # 10
        'Lewey',                                # 11
        'Lore',                                 # 12
        'Figaro',                               # 13
        'Pesca',                                # 14
        'Melony',                               # 15
        'Gray',                                 # 16
        'Estelle',                              # 17
        'Elder Reisen',                         # 18
        'Chicken',                              # 19
        'Chicken',                              # 20
        'Chicken',                              # 21
        'Chicken',                              # 22
        'Ravennue Trail',                       # 23
        'Abandoned Mine Trail',                 # 24
    )

    DeclEntryPoint(
        Unknown_00              = -1600,
        Unknown_04              = 0,
        Unknown_08              = 8800,
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
        'ED6_DT07/CH01060 ._CH',             # 00
        'ED6_DT07/CH01070 ._CH',             # 01
        'ED6_DT07/CH01470 ._CH',             # 02
        'ED6_DT07/CH01120 ._CH',             # 03
        'ED6_DT07/CH01020 ._CH',             # 04
        'ED6_DT07/CH01140 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT07/CH01000 ._CH',             # 07
        'ED6_DT07/CH00107 ._CH',             # 08
        'ED6_DT07/CH01490 ._CH',             # 09
        'ED6_DT07/CH00100 ._CH',             # 0A
        'ED6_DT07/CH01720 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT07/CH01060P._CP',             # 00
        'ED6_DT07/CH01070P._CP',             # 01
        'ED6_DT07/CH01470P._CP',             # 02
        'ED6_DT07/CH01120P._CP',             # 03
        'ED6_DT07/CH01020P._CP',             # 04
        'ED6_DT07/CH01140P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT07/CH01000P._CP',             # 07
        'ED6_DT07/CH00107P._CP',             # 08
        'ED6_DT07/CH01490P._CP',             # 09
        'ED6_DT07/CH00100P._CP',             # 0A
        'ED6_DT07/CH01720P._CP',             # 0B
    )

    DeclNpc(
        X                   = 4720,
        Z                   = 0,
        Y                   = 28930,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 2730,
        Z                   = 0,
        Y                   = 27400,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 2610,
        Z                   = 0,
        Y                   = 28970,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 25370,
        Z                   = -4000,
        Y                   = 9110,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 14250,
        Z                   = -4000,
        Y                   = 21420,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 20710,
        Z                   = -4000,
        Y                   = 9840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 18930,
        Z                   = -4000,
        Y                   = 15140,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 26300,
        Z                   = -4000,
        Y                   = 19500,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
    )

    DeclNpc(
        X                   = 4000,
        Z                   = 0,
        Y                   = 12000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 33000,
        Z                   = 8000,
        Y                   = 36660,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = 0,
        Z                   = -4000,
        Y                   = 0,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = -4000,
        Y                   = 0,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = -4000,
        Y                   = 0,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = -4000,
        Y                   = 0,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 7,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        X                   = 3260,
        Y                   = 7000,
        Z                   = 66870,
        Range               = 9230,
        Unknown_10          = 0x2710,
        Unknown_14          = 0x10C52,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 5000,
        Y                   = 0,
        Z                   = 34240,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 5150,
        Y                   = 4550,
        Z                   = 41780,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 5310,
        Y                   = 0,
        Z                   = 23020,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 26,
    )

    DeclEvent(
        X                   = 6000,
        Y                   = 4400,
        Z                   = 54640,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
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
        TalkFunctionIndex   = 21,
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
        TalkFunctionIndex   = 24,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3F2",          # 00, 0
        "Function_1_587",          # 01, 1
        "Function_2_5B8",          # 02, 2
        "Function_3_735",          # 03, 3
        "Function_4_782",          # 04, 4
        "Function_5_817",          # 05, 5
        "Function_6_884",          # 06, 6
        "Function_7_8D1",          # 07, 7
        "Function_8_A23",          # 08, 8
        "Function_9_AAF",          # 09, 9
        "Function_10_AD5",         # 0A, 10
        "Function_11_1161",        # 0B, 11
        "Function_12_16AB",        # 0C, 12
        "Function_13_3019",        # 0D, 13
        "Function_14_37F0",        # 0E, 14
        "Function_15_4099",        # 0F, 15
        "Function_16_4A3D",        # 10, 16
        "Function_17_4EAF",        # 11, 17
        "Function_18_5392",        # 12, 18
        "Function_19_5894",        # 13, 19
        "Function_20_5A57",        # 14, 20
        "Function_21_6209",        # 15, 21
        "Function_22_6251",        # 16, 22
        "Function_23_6A72",        # 17, 23
        "Function_24_6E92",        # 18, 24
        "Function_25_6F9C",        # 19, 25
        "Function_26_6FA0",        # 1A, 26
        "Function_27_6FA4",        # 1B, 27
    )


    def Function_0_3F2(): pass

    label("Function_0_3F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_42E")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    Jump("loc_51B")

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_44C")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_51B")

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_488")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_51B")

    label("loc_488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_49C")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    Jump("loc_51B")

    label("loc_49C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_4C1")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrPos(0xA, 35020, -3850, 8540, 180)
    Jump("loc_51B")

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_4EB")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)
    SetChrPos(0xA, 35020, -3850, 8540, 180)
    SetChrFlags(0xA, 0x10)
    Jump("loc_51B")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_51B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x1000)"), scpexpr(EXPR_END)), "loc_505")
    SetChrFlags(0xC, 0x80)
    Jump("loc_516")

    label("loc_505")

    SetChrPos(0xC, 4840, 8000, 66800, 180)

    label("loc_516")

    SetChrFlags(0xA, 0x10)

    label("loc_51B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52C")
    ClearChrFlags(0x11, 0x80)

    label("loc_52C")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_53C"),
        (109, "loc_565"),
        (SWITCH_DEFAULT, "loc_586"),
    )


    label("loc_53C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E")
    OP_A2(0x31A)
    Event(0, 20)
    Jump("loc_562")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_562")
    Event(0, 19)

    label("loc_562")

    Jump("loc_586")

    label("loc_565")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_583")
    OP_28(0xE, 0x1, 0x1000)
    Event(0, 23)

    label("loc_583")

    Jump("loc_586")

    label("loc_586")

    Return()

    # Function_0_3F2 end

    def Function_1_587(): pass

    label("Function_1_587")

    OP_16(0x2, 0xFA0, 0xFFFE5638, 0xFFFE98A0, 0x30043)
    OP_72(0x6, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B2")
    OP_72(0xA, 0x4)
    Jump("loc_5B7")

    label("loc_5B2")

    OP_71(0xA, 0x4)

    label("loc_5B7")

    Return()

    # Function_1_587 end

    def Function_2_5B8(): pass

    label("Function_2_5B8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5DD")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_71F")

    label("loc_5DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F6")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_71F")

    label("loc_5F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_60F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_71F")

    label("loc_60F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_628")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_71F")

    label("loc_628")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_641")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_71F")

    label("loc_641")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_71F")

    label("loc_65A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_673")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_71F")

    label("loc_673")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68C")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_71F")

    label("loc_68C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A5")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_71F")

    label("loc_6A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BE")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_71F")

    label("loc_6BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D7")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_71F")

    label("loc_6D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F0")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_71F")

    label("loc_6F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_709")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_71F")

    label("loc_709")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_71F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_734")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_71F")

    label("loc_734")

    Return()

    # Function_2_5B8 end

    def Function_3_735(): pass

    label("Function_3_735")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_781")
    OP_8E(0xFE, 0x13C4, 0x0, 0x6ED2, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 500)
    Sleep(1000)
    OP_8E(0xFE, 0xF96, 0x0, 0x72C4, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 500)
    Sleep(1000)
    Jump("Function_3_735")

    label("loc_781")

    Return()

    # Function_3_735 end

    def Function_4_782(): pass

    label("Function_4_782")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_816")
    OP_8E(0xFE, 0xDC0, 0x0, 0x6E0A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 500)
    Sleep(1000)
    OP_8E(0xFE, 0x105E, 0x0, 0x6B44, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 500)
    Sleep(1000)
    OP_8E(0xFE, 0xEB0, 0x0, 0x65D6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xBC2, 0x0, 0x6770, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 500)
    Sleep(1000)
    OP_8E(0xFE, 0xAAA, 0x0, 0x6B08, 0x7D0, 0x0)
    Jump("Function_4_782")

    label("loc_816")

    Return()

    # Function_4_782 end

    def Function_5_817(): pass

    label("Function_5_817")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_883")
    OP_8E(0xFE, 0x631A, 0xFFFFF060, 0x2B48, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x7224, 0xFFFFF060, 0x2120, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x597E, 0xFFFFF060, 0x15EA, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Sleep(1000)
    Jump("Function_5_817")

    label("loc_883")

    Return()

    # Function_5_817 end

    def Function_6_884(): pass

    label("Function_6_884")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8D0")
    OP_8E(0xFE, 0x4222, 0xFFFFF060, 0x3E8A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 500)
    Sleep(1000)
    OP_8E(0xFE, 0x53A2, 0xFFFFF060, 0x3638, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 500)
    Sleep(1000)
    Jump("Function_6_884")

    label("loc_8D0")

    Return()

    # Function_6_884 end

    def Function_7_8D1(): pass

    label("Function_7_8D1")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x4)
    OP_8D(0xFE, 12660, 3550, 26000, 18020, 0)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8FF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A22")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E7")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x3174), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_PUSH_LONG, 0xDDE), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x6590), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_LONG, 0x4664), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9BC")
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x0, 0)
    ClearChrFlags(0xFE, 0x20)

    def lambda_9A9():
        OP_94(0x0, 0xFE, 0xB4, 0x12C, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A9)
    Jump("loc_9DF")

    label("loc_9BC")


    def lambda_9C2():
        OP_8D(0xFE, 12660, 3550, 26000, 18020, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C2)
    Sleep(200)

    label("loc_9DF")

    Sleep(30)
    Jump("loc_A1F")

    label("loc_9E7")

    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A1F")
    OP_44(0xFE, 0x2)

    def lambda_A07():
        OP_8D(0xFE, 12660, 3550, 26000, 18020, 1500)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A07)

    label("loc_A1F")

    Jump("loc_8FF")

    label("loc_A22")

    Return()

    # Function_7_8D1 end

    def Function_8_A23(): pass

    label("Function_8_A23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AAE")
    OP_43(0xFE, 0x2, 0x0, 0x9)
    OP_22(0x191, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AAE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x38B, 1)"), scpexpr(EXPR_END)), "loc_AAE")
    TalkBegin(0xFE)
    OP_A2(0x9)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x00Found \x07\x02Fresh Eggs\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFE)

    label("loc_AAE")

    Return()

    # Function_8_A23 end

    def Function_9_AAF(): pass

    label("Function_9_AAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ACA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_48()
    Jump("Function_9_AAF")

    label("loc_ACA")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_9_AAF end

    def Function_10_AD5(): pass

    label("Function_10_AD5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_BCD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6E")
    OP_A2(0x0)

    ChrTalk(    #1
        0xFE,
        "I sure wish I were born in Bose!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "There are no orchards in Bose, so\x01",
            "I wouldn't be stuck helping like\x01",
            "this all the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCA")

    label("loc_B6E")


    ChrTalk(    #3
        0xFE,
        (
            "If I had been born in Bose, I wouldn't\x01",
            "be stuck helping around the orchards\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCA")

    Jump("loc_115D")

    label("loc_BCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_C37")

    ChrTalk(    #4
        0xFE,
        (
            "Even adults have their own kinda\x01",
            "problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "It must be tough being grown\x01",
            "up sometimes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_115D")

    label("loc_C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_CB4")

    ChrTalk(    #6
        0xFE,
        (
            "Old man Gray and Pesca were\x01",
            "just fighting again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "We've been seeing those two going\x01",
            "at it a lot recently.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_115D")

    label("loc_CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_E56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD0")
    OP_A2(0x0)

    ChrTalk(    #8
        0xFE,
        (
            "I heard this from Lewey, so don't\x01",
            "get mad at me if I'm wrong...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "But aren't you guys from the\x01",
            "Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "That's awesome! So even girls\x01",
            "can be bracers too, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "I always thought that you couldn't\x01",
            "be a bracer unless you were tough\x01",
            "like Agate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E53")

    label("loc_DD0")


    ChrTalk(    #12
        0xFE,
        (
            "So, even girls can be bracers\x01",
            "too, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I always thought that you couldn't\x01",
            "be a bracer unless you were tough\x01",
            "like Agate.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E53")

    Jump("loc_115D")

    label("loc_E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_1071")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA3")
    OP_A2(0x0)

    ChrTalk(    #14
        0xFE,
        (
            "I think it's partly Lewey's fault that\x01",
            "people don't believe him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "When he first talked about seeing\x01",
            "some suspicious silhouettes, he\x01",
            "said he thought they were dragons.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "And dragons are creatures from ancient times,\x01",
            "right? So saying something like that is not\x01",
            "going to help people believe your story.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_106E")

    label("loc_FA3")


    ChrTalk(    #17
        0xFE,
        (
            "I think it's partly Lewey's fault that\x01",
            "people don't believe him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Dragons are creatures from ancient times,\x01",
            "right? So, saying something like that is\x01",
            "not going to help people believe your story.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_106E")

    Jump("loc_115D")

    label("loc_1071")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_10C6")

    ChrTalk(    #19
        0xFE,
        "Lewey hasn't come over recently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "I wonder if something happened.\x02",
    )

    CloseMessageWindow()
    Jump("loc_115D")

    label("loc_10C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_115D")

    ChrTalk(    #21
        0xFE,
        (
            "Since this is Lewey we're talking about,\x01",
            "he's probably mistaken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "He's probably just been looking at the\x01",
            "stars too much if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115D")

    TalkEnd(0x8)
    Return()

    # Function_10_AD5 end

    def Function_11_1161(): pass

    label("Function_11_1161")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_126D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120A")
    OP_A2(0x1)

    ChrTalk(    #23
        0xFE,
        (
            "I think if Vince had been born into a\x01",
            "merchant family things would have\x01",
            "been a real mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "For starters, he doesn't even like\x01",
            "to study.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126A")

    label("loc_120A")


    ChrTalk(    #25
        0xFE,
        (
            "I'm sure if Vince had been born into a\x01",
            "merchant family things would have\x01",
            "been a real mess.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126A")

    Jump("loc_16A7")

    label("loc_126D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_12C0")

    ChrTalk(    #26
        0xFE,
        (
            "Since we all live in the same village,\x01",
            "we should try and get along.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A7")

    label("loc_12C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1313")

    ChrTalk(    #27
        0xFE,
        "Pesca just moved here recently.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "Usually he's kind and serious.\x02",
    )

    CloseMessageWindow()
    Jump("loc_16A7")

    label("loc_1313")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_143E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EA")
    OP_A2(0x1)

    ChrTalk(    #29
        0xFE,
        "What's Vince's new theory now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "This is the time for us women\x01",
            "to shine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Even Lore's wife is the queen\x01",
            "of the house.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "And for heaven's sake, we even\x01",
            "have Her Majesty the Queen.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143B")

    label("loc_13EA")


    ChrTalk(    #33
        0xFE,
        "What's Vince's new theory now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "This is the time for us women\x01",
            "to shine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_143B")

    Jump("loc_16A7")

    label("loc_143E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_15CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1523")
    OP_A2(0x1)

    ChrTalk(    #35
        0xFE,
        "I think it's just like he says...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I've heard that when our fathers were\x01",
            "children, there was a dragon still\x01",
            "around here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "I'd love to see a dragon for real,\x01",
            "even if only just one time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15CC")

    label("loc_1523")


    ChrTalk(    #38
        0xFE,
        (
            "I've heard that when our fathers were\x01",
            "children, there was a dragon still\x01",
            "around here somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "I'd love to see a dragon for real,\x01",
            "even if only just one time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15CC")

    Jump("loc_16A7")

    label("loc_15CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_1665")

    ChrTalk(    #40
        0xFE,
        "Huh...? Are you guys visitors?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "If you're looking for the village\x01",
            "elder's house it's just up that\x01",
            "hill in the back of the village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A7")

    label("loc_1665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_16A7")

    ChrTalk(    #42
        0xFE,
        "So who are you guys anyway?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        "Merchants from Bose?\x02",
    )

    CloseMessageWindow()

    label("loc_16A7")

    TalkEnd(0x9)
    Return()

    # Function_11_1161 end

    def Function_12_16AB(): pass

    label("Function_12_16AB")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_1B69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x71, 6)), scpexpr(EXPR_END)), "loc_17FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1799")
    OP_A2(0x2)

    ChrTalk(    #44
        0xFE,
        (
            "There was a big war in this area\x01",
            "a long time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "And a lot of people from the\x01",
            "village here died.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I wish we could just get along\x01",
            "with the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Because I hate it when people\x01",
            "are sad...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FC")

    label("loc_1799")


    ChrTalk(    #48
        0xFE,
        (
            "I wish we could just get along\x01",
            "with the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Because I hate it when people\x01",
            "are sad...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FC")

    Jump("loc_1B66")

    label("loc_17FF")

    OP_A2(0x38E)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #50
        0xFE,
        "Oh! Hi, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#001FHi, Lewey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "I was shocked to see the army\x01",
            "haul you guys off after you went\x01",
            "up to the abandoned mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Especially, after you didn't do\x01",
            "anything wrong either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Are you guys okay? Did those\x01",
            "soldiers do anything bad to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#506FI'm sorry if we had you worried\x01",
            "there...\x02\x03",

            "#006FBut we're okay. As you can see\x01",
            "we're alive and kicking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "I am glad you guys are all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "So what I saw was actually an\x01",
            "airship then, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Thanks for proving that I wasn't\x01",
            "just telling a tall tale!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#505FSure...\x02\x03",

            "But I'm sure the Royal Army would have\x01",
            "proved your story sooner or later, so I've\x01",
            "got mixed feelings about the whole ordeal...\x02\x03",

            "Considering that we were mistaken\x01",
            "for sky bandits and then arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        (
            "#010FWell, even if you didn't go out in style\x01",
            "at least you kept your promise...\x02\x03",

            "And isn't that enough?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B66")

    Jump("loc_3015")

    label("loc_1B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_1F3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE5")
    OP_A2(0x2)
    OP_A2(0x38E)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #61
        0xFE,
        "Oh! Hi, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#001FHi, Lewey!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I was shocked to see the army\x01",
            "haul you guys off after you went\x01",
            "up to the abandoned mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Especially, after you didn't do\x01",
            "anything wrong either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Are you guys okay? Did those\x01",
            "soldiers do anything bad to you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#506FI'm sorry if we had you worried\x01",
            "there...\x02\x03",

            "#006FBut we're okay. As you can see\x01",
            "we're alive and kicking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "I am glad you guys are all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "So what I saw was actually an\x01",
            "airship then, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Thanks for proving that I wasn't\x01",
            "just telling a tall tale!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#505FSure...\x02\x03",

            "But I'm sure the Royal Army would have\x01",
            "proved your story sooner or later, so I've\x01",
            "got mixed feelings about the whole ordeal...\x02\x03",

            "Considering that we were mistaken\x01",
            "for sky bandits and then arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        (
            "#010FWell, even if you didn't go out in style\x01",
            "at least you kept your promise...\x02\x03",

            "And isn't that enough?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F37")

    label("loc_1EE5")


    ChrTalk(    #72
        0xFE,
        (
            "I want to thank you guys for proving\x01",
            "that I wasn't just telling a tall tale!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F37")

    Jump("loc_3015")

    label("loc_1F3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_209E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2081")
    OP_A2(0x2)

    ChrTalk(    #73
        0xFE,
        "Hi, you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "Did you find something out?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#006FI can't say for sure...\x02\x03",

            "But I don't think the thing you\x01",
            "saw was a dream.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #76
        0xFE,
        "Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#006FWe're going to do a little more investigating,\x01",
            "so please give us a bit longer to see what\x01",
            "we come up with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "Okay! Good luck, you guys!\x02",
    )

    CloseMessageWindow()
    Jump("loc_209B")

    label("loc_2081")


    ChrTalk(    #79
        0xFE,
        "Good luck, you guys!\x02",
    )

    CloseMessageWindow()

    label("loc_209B")

    Jump("loc_3015")

    label("loc_209E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_2122")

    ChrTalk(    #80
        0xFE,
        (
            "The two shadows I saw flying in the\x01",
            "sky went north until I couldn't see\x01",
            "them anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "I know I wasn't dreaming!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3015")

    label("loc_2122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_2FDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F92")
    OP_A2(0x31C)
    OP_28(0x36, 0x1, 0x8)
    OP_28(0x36, 0x1, 0x10)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(34870, -3850, 9830, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    SetChrPos(0x101, 35122, -3850, 10423, 180)
    SetChrPos(0x102, 35484, -3850, 11571, 180)
    SetChrPos(0x103, 34518, -3850, 11700, 180)
    TurnDirection(0xFE, 0x101, 0)
    OP_0D()

    ChrTalk(    #82
        0xFE,
        (
            "Huh? I haven't seen you guys\x01",
            "around here before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Are you merchants, here to buy\x01",
            "fruit?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#006FActually, no. We're here for a\x01",
            "different reason.\x02\x03",

            "As a matter of fact, we're bracers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "Bracers? You mean like Agate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "I don't know, you don't look all\x01",
            "that strong to me...especially\x01",
            "'cause you're a girl.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #87
        0x101,
        (
            "#007FUgh... Why don't you tell me\x01",
            "how you really feel...?\x02\x03",

            "#006FBut after seeing my great skill with\x01",
            "a staff, do you think you can still\x01",
            "call me weak?!\x02",
        )
    )

    CloseMessageWindow()
    Fade(1500)
    SetChrChipByIndex(0x101, 10)
    OP_6C(0, 1500)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 8)
    OP_22(0x7E, 0x1, 0x64)

    def lambda_23CE():

        label("loc_23CE")

        OP_99(0xFE, 0x0, 0x7, 0xBB8)
        OP_48()
        Jump("loc_23CE")

    QueueWorkItem2(0x101, 0, lambda_23CE)
    Sleep(2000)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x1F40)
    Sleep(1000)

    ChrTalk(    #88
        0xFE,
        (
            "Wow! That's amazing!\x01",
            "It's like a tornado!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_23(0x7E)
    OP_99(0x101, 0x0, 0xA, 0x7D0)
    OP_22(0x1F4, 0x0, 0x64)
    OP_99(0x101, 0xB, 0x13, 0x7D0)
    Sleep(300)

    ChrTalk(    #89
        0x101,
        (
            "#502FHeheheh. I hope you've\x01",
            "learned your lesson that looks\x01",
            "can be deceiving.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    OP_6C(135000, 0)
    OP_0D()

    ChrTalk(    #90
        0x101,
        (
            "#001FNow how about another amazing\x01",
            "demonstration with my staff...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        (
            "#017FEstelle...be careful. Wasn't it just\x01",
            "yesterday that you hit yourself in\x01",
            "the face doing that?\x02\x03",

            "#010FAnyway, are you Lewey, by chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "Uh, yeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        "But how do you know my name?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x102,
        (
            "#010FWe heard from the village elder.\x01",
            "He said you saw some kind of\x01",
            "flying shadow.\x02\x03",

            "Do you think you could tell us a\x01",
            "little bit more about what you\x01",
            "saw that night?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        "Sure, if you want...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "But the soldiers from the army\x01",
            "already searched the place and\x01",
            "didn't find anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        (
            "#010FThat's fine, we're not worried about\x01",
            "that. Do you think you could just\x01",
            "tell us what you saw?\x02\x03",

            "In as much detail as you can\x01",
            "remember?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "O-Okay, I'll try...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "You see...I like watching the\x01",
            "stars at night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "So I often sneak out of my house at\x01",
            "night to come here and look at the\x01",
            "stars.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "And the other night when I was out\x01",
            "here looking up at the stars I saw\x01",
            "two shadows moving across the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#004FNow hold on a minute here...\x02\x03",

            "You say you saw TWO shadows?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "Yeah, that's right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "And they were different sizes, too.\x01",
            "Kind of like a mom leading a kid.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#002FTwo shadows, two sizes...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x103,
        (
            "#022FThat's consistent with an airliner and\x01",
            "the sky bandit airship, if you think\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x102,
        (
            "#012FYeah, the aircraft we ran across\x01",
            "in the woods was definitely smaller\x01",
            "than a typical airliner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "And the two shadows just kept on\x01",
            "flying north...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "Until I couldn't see them anymore.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        "#002FSo, north is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        (
            "#020FThere's a trail that continues\x01",
            "behind the village.\x02\x03",

            "And it leads to an old Septium mine\x01",
            "which was abandoned some time ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "The soldiers from the army supposedly\x01",
            "searched the trail, but didn't come up\x01",
            "with anything...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "That's why they said I must have\x01",
            "just been dreaming...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "And then they laughed at me like\x01",
            "I didn't know what I was talking\x01",
            "about.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #116
        "\x07\x05The little boy's eyes started to well up with tears.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #117
        0x101,
        (
            "#004FAh, enough of that. You're a boy,\x01",
            "right? And boys don't cry!\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x101, 0xFE, 0x320, 0xBB8, 0x0)
    Sleep(400)

    ChrTalk(    #118
        0x101,
        (
            "#006FWe're not like those stupid soldiers.\x02\x03",

            "We don't think you're telling a lie\x01",
            "either, and we're going to prove it!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #119
        0xFE,
        "R-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        (
            "#006FDarn straight!\x01",
            "You just leave it to us!\x02\x03",

            "So no more crying, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "O-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "You're a real nice person!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x103,
        (
            "#027F(Ha ha. As usual, she's got a\x01",
            "knack with the kids.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x102,
        "#019F(Yeah...maybe it's a virtue.)\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #125
        0x101,
        (
            "#501FHuh? Why are you looking at me\x01",
            "like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        (
            "#010FI-It's nothing.\x02\x03",

            "Let's focus on the task at hand.\x01",
            "It looks like we've got stuff to do!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#006FRight!\x02\x03",

            "Let's hurry and get onto the trail\x01",
            "behind the village and see what\x01",
            "we can find!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Jump("loc_2FD9")

    label("loc_2F92")


    ChrTalk(    #128
        0xFE,
        "*sniffle* Nobody believes me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "It wasn't a dream, either...\x02",
    )

    CloseMessageWindow()

    label("loc_2FD9")

    Jump("loc_3015")

    label("loc_2FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_3015")

    ChrTalk(    #130
        0xFE,
        (
            "I know what I saw and I told them\x01",
            "so, too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3015")

    TalkEnd(0xA)
    Return()

    # Function_12_16AB end

    def Function_13_3019(): pass

    label("Function_13_3019")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_30EC")

    ChrTalk(    #131
        0xFE,
        (
            "I sure hope that Pesca and Gray\x01",
            "can come to an understanding at\x01",
            "the next village meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "I think if those two could learn to\x01",
            "cooperate, the village orchards\x01",
            "would become more prosperous.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37EC")

    label("loc_30EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_31F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_319F")
    OP_A2(0x3)

    ChrTalk(    #133
        0xFE,
        (
            "We are going to have the village elder\x01",
            "open a meeting to discuss policy\x01",
            "regarding orchard cultivation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "I hope there'll be some sort of\x01",
            "development.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31EF")

    label("loc_319F")


    ChrTalk(    #135
        0xFE,
        "I wonder what Pomme is up to.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "I hope he's getting along well in Bose.\x02",
    )

    CloseMessageWindow()

    label("loc_31EF")

    Jump("loc_37EC")

    label("loc_31F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_33AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32C1")
    OP_A2(0x3)

    ChrTalk(    #137
        0xFE,
        "I get what Gray is trying to say...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "But I think that Pesca has the best\x01",
            "idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "I think we should sit down and discuss\x01",
            "this, as it really is important to the\x01",
            "whole village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A9")

    label("loc_32C1")


    ChrTalk(    #140
        0xFE,
        (
            "If we don't take care of this problem\x01",
            "now, I'll be left with a bad aftertaste,\x01",
            "and I won't be able to go to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Maybe I should suggest to the village\x01",
            "elder that we sit down and talk about\x01",
            "orchard cultivation policies...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33A9")

    Jump("loc_37EC")

    label("loc_33AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_3574")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34F0")
    OP_A2(0x3)

    ChrTalk(    #142
        0xFE,
        (
            "Gray and Pesca were at each\x01",
            "others' throats again today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "Gray has been growing fruit well before\x01",
            "orchard cultivation spread throughout\x01",
            "the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "And it's thanks to him that we were\x01",
            "able to reestablish the village after\x01",
            "the mine shut down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "Maybe that's why he's not very\x01",
            "flexible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3571")

    label("loc_34F0")


    ChrTalk(    #146
        0xFE,
        (
            "Gray and Pesca were at each\x01",
            "others' throats again today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "There are a number of things that\x01",
            "he's unwilling to budge on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3571")

    Jump("loc_37EC")

    label("loc_3574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_37A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36EC")
    OP_A2(0x3)

    ChrTalk(    #148
        0xFE,
        (
            "I'm actually looking to get out of\x01",
            "the orchard business and start\x01",
            "again as a merchant in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "But there are still a number of problems\x01",
            "hanging over this village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "And if we can't find a way to resolve\x01",
            "them I just won't be able to leave\x01",
            "this place with a clear conscience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "That's why my wife and son have\x01",
            "gone ahead to Bose without me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37A3")

    label("loc_36EC")


    ChrTalk(    #152
        0xFE,
        (
            "I'm actually looking to get out of\x01",
            "the orchard business and start\x01",
            "again as a merchant in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "My wife and son have already gone\x01",
            "ahead to Bose and are waiting\x01",
            "there for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A3")

    Jump("loc_37EC")

    label("loc_37A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_37EC")

    ChrTalk(    #154
        0xFE,
        (
            "Man, I just can't get Gray to listen\x01",
            "to any common sense.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37EC")

    TalkEnd(0xB)
    Return()

    # Function_13_3019 end

    def Function_14_37F0(): pass

    label("Function_14_37F0")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_3D9E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CF5")
    OP_28(0xE, 0x1, 0x2000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_3A6E")
    OP_28(0xE, 0x1, 0x4000)

    ChrTalk(    #155
        0xC,
        (
            "Sorry, but the trail behind the\x01",
            "village is off limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xC,
        (
            "If you have any questions about why,\x01",
            "please talk to the village elder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        (
            "#000FIf you mean the request to the guild,\x01",
            "we've already talked to the village\x01",
            "elder about it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #158
        0xC,
        "Huh? So what you're saying is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xC,
        (
            "You guys are here with the Bracer\x01",
            "Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x103,
        "#020FYou got it.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(    #161
        0xC,
        (
            "Oh man, have I been waiting\x01",
            "for you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xC,
        (
            "Please hurry up and take care\x01",
            "of the monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xC,
        (
            "The season to plant saplings\x01",
            "is almost upon us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 400)

    ChrTalk(    #164
        0xC,
        (
            "Anyway, be careful out there and\x01",
            "good luck! We are counting on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CF2")

    label("loc_3A6E")

    OP_28(0xE, 0x1, 0x4000)

    ChrTalk(    #165
        0xC,
        (
            "I'm sorry, but you can't go beyond\x01",
            "this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xC,
        (
            "I shouldn't be telling you this, but there's been\x01",
            "some rumors going around that there's a vicious\x01",
            "monster out there on the trail behind the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#000FYeah, and we already talked to\x01",
            "the village elder about it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #168
        0xC,
        "Really...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xC,
        (
            "So does that mean you're with\x01",
            "the Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x103,
        "#020FYep, that's right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(    #171
        0xC,
        (
            "Oh man. It's a good thing you're\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xC,
        (
            "The season to plant saplings\x01",
            "is almost upon us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xC,
        (
            "It would help out a lot if you could\x01",
            "exterminate this monster before\x01",
            "things get really busy around here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 400)

    ChrTalk(    #174
        0xC,
        "Anyway, be cautious out there.\x02",
    )

    CloseMessageWindow()

    label("loc_3CF2")

    Jump("loc_3D9B")

    label("loc_3CF5")


    ChrTalk(    #175
        0xFE,
        (
            "The season to plant saplings\x01",
            "is almost upon us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xFE,
        (
            "I hope you can take care of this\x01",
            "monster before things get really\x01",
            "busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        "Anyway, be cautious out there.\x02",
    )

    CloseMessageWindow()

    label("loc_3D9B")

    Jump("loc_4095")

    label("loc_3D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FD6")
    OP_A2(0x4)
    OP_28(0xE, 0x1, 0x4000)

    ChrTalk(    #178
        0xC,
        (
            "I'm sorry, but you can't go beyond\x01",
            "this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xC,
        (
            "I shouldn't be telling you this, but there's been\x01",
            "some rumors going around that there's a vicious\x01",
            "monster out there on the trail behind the village.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F1D")

    ChrTalk(    #180
        0x101,
        (
            "#004FSeriously...?! Are people really saying\x01",
            "stuff like that?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #181
        0xC,
        (
            "It would be great if they were just\x01",
            "rumors, but they seem to be true.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F1D")

    TurnDirection(0xC, 0x0, 400)

    ChrTalk(    #182
        0xC,
        (
            "I should probably refer you to the\x01",
            "village elder about the details though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xC,
        (
            "I hear he's requested that the guild\x01",
            "exterminate the monster just to be\x01",
            "on the safe side.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4095")

    label("loc_3FD6")


    ChrTalk(    #184
        0xC,
        (
            "This place is off limits. You'll\x01",
            "need to talk to the village elder\x01",
            "for further details.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    ChrTalk(    #185
        0xC,
        (
            "Look, you can see that roof over\x01",
            "there, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xC,
        "That's the village elder's house.\x02",
    )

    CloseMessageWindow()

    label("loc_4095")

    TalkEnd(0xC)
    Return()

    # Function_14_37F0 end

    def Function_15_4099(): pass

    label("Function_15_4099")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_4215")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4187")
    OP_A2(0x5)

    ChrTalk(    #187
        0xFE,
        (
            "Maybe I should suggest my own ideas\x01",
            "at the village meeting this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "I know things always turn into a\x01",
            "big argument with Gray, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xFE,
        (
            "I think we need to sit down and\x01",
            "talk with cool heads for once...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4212")

    label("loc_4187")


    ChrTalk(    #190
        0xFE,
        (
            "I know things always turn into a\x01",
            "big argument with Gray, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "I think we need to sit down and\x01",
            "talk with cool heads for once...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4212")

    Jump("loc_4A39")

    label("loc_4215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_43E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43AA")
    OP_A2(0x5)

    ChrTalk(    #192
        0xFE,
        (
            "I don't think we should just\x01",
            "continue on in the old ways...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "I think we need to find a more inventive\x01",
            "approach where we can achieve a\x01",
            "constant output of products.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "You can see how all the fruit\x01",
            "producing trees are short, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        "That was something I suggested.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "I figured if we didn't have to deal with\x01",
            "high places, we wouldn't need so\x01",
            "many hands to do the work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43E0")

    label("loc_43AA")


    ChrTalk(    #197
        0xFE,
        (
            "Man, I wish I could just get\x01",
            "Gray to understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43E0")

    Jump("loc_4A39")

    label("loc_43E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_464C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45B3")
    OP_A2(0x5)

    ChrTalk(    #198
        0xFE,
        (
            "It's not like I want to turn everything\x01",
            "into a mechanized cultivation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0xFE,
        (
            "To begin with, orchard cultivation is\x01",
            "difficult to do with machines anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xFE,
        (
            "Even if we used orbal machines to help\x01",
            "us out, a large portion of the work would\x01",
            "still rely on things done by hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "And as it stands we don't have\x01",
            "enough people here in the village\x01",
            "to do everything by hand. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "This is why I think we should use\x01",
            "machines where we need them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4649")

    label("loc_45B3")


    ChrTalk(    #203
        0xFE,
        (
            "I've tried to speak with Gray about\x01",
            "this a number of times...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xFE,
        (
            "But he stubbornly insists that I'm\x01",
            "wrong without even looking into\x01",
            "the facts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4649")

    Jump("loc_4A39")

    label("loc_464C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_47C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_473C")
    OP_A2(0x5)

    ChrTalk(    #205
        0xFE,
        (
            "Gray thinks that the only reason\x01",
            "why I want to use machines is\x01",
            "so that I can be lazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xFE,
        "He completely misunderstands me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "I think we should use a number\x01",
            "of cultivation technologies to\x01",
            "improve the process.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47BF")

    label("loc_473C")


    ChrTalk(    #208
        0xFE,
        (
            "Gray thinks that the only reason\x01",
            "why I want to use machines is\x01",
            "so that I can be lazy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        "He completely misunderstands me...\x02",
    )

    CloseMessageWindow()

    label("loc_47BF")

    Jump("loc_4A39")

    label("loc_47C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_49AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48E1")
    OP_A2(0x5)

    ChrTalk(    #210
        0xFE,
        (
            "I moved to this village a number of\x01",
            "years ago because I wanted to be\x01",
            "an orchard farmer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        (
            "I even purchased a new set of orbal\x01",
            "farming equipment, which I've been\x01",
            "studying how to use all my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xFE,
        (
            "I'm going to grow and produce more\x01",
            "fruit than anyone else!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49AB")

    label("loc_48E1")


    ChrTalk(    #213
        0xFE,
        (
            "I moved to this village a number of\x01",
            "years ago because I wanted to be\x01",
            "an orchard farmer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "I even purchased a new set of orbal\x01",
            "farming equipment, which I've been\x01",
            "studying how to use all my life.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49AB")

    Jump("loc_4A39")

    label("loc_49AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4A39")

    ChrTalk(    #215
        0xFE,
        (
            "Hi there, did you come to see the\x01",
            "orchards?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "It's not like they're going anywhere\x01",
            "soon, so take your time and look\x01",
            "around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A39")

    TalkEnd(0xD)
    Return()

    # Function_15_4099 end

    def Function_16_4A3D(): pass

    label("Function_16_4A3D")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_4AC3")

    ChrTalk(    #217
        0xFE,
        (
            "My husband, who's gone out to a\x01",
            "meeting, is late getting home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        (
            "I sure hope he can work things\x01",
            "out with Gray...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EAB")

    label("loc_4AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_4B56")

    ChrTalk(    #219
        0xFE,
        "I'm always on my husband's side.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "And it's because we can trust in\x01",
            "each other like this that we can\x01",
            "live like this as a couple.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EAB")

    label("loc_4B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4BF1")

    ChrTalk(    #221
        0xFE,
        (
            "I really want people to somehow be able\x01",
            "to understand my husband's ideas.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "I think in the end it's in the best\x01",
            "interest of the village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EAB")

    label("loc_4BF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_4CF3")

    ChrTalk(    #223
        0xFE,
        (
            "I really love raising fruit myself,\x01",
            "so I'm glad that I came along with\x01",
            "my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "It's been a while coming, but gradually\x01",
            "we've been able to confide in the other\x01",
            "villagers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "But Gray is someone we've never\x01",
            "been able to get close to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EAB")

    label("loc_4CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_4DB2")

    ChrTalk(    #226
        0xFE,
        (
            "I think it's as my husband says,\x01",
            "Gray just misunderstands us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "I think if we had a chance to really sit\x01",
            "down and talk to him he would\x01",
            "understand where we're coming from...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EAB")

    label("loc_4DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_4E52")

    ChrTalk(    #228
        0xFE,
        (
            "My husband Pesca is really dedicated\x01",
            "to his research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "He works by day in the orchard,\x01",
            "and researches various means of\x01",
            "cultivation by night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EAB")

    label("loc_4E52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_4EAB")

    ChrTalk(    #230
        0xFE,
        "It's almost lunchtime.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "I'd better finish up these few jobs\x01",
            "here myself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EAB")

    TalkEnd(0xE)
    Return()

    # Function_16_4A3D end

    def Function_17_4EAF(): pass

    label("Function_17_4EAF")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x67, 2)), scpexpr(EXPR_END)), "loc_4F1F")

    ChrTalk(    #232
        0xFE,
        (
            "I'm going to have to keep an eye on\x01",
            "these young upstarts and their ways\x01",
            "of cultivating fruit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_538E")

    label("loc_4F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 3)), scpexpr(EXPR_END)), "loc_4FD6")

    ChrTalk(    #233
        0xFE,
        (
            "Raising fruit naturally on trees one\x01",
            "by one is the best way as far as I'm\x01",
            "concerned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "And it's because I take so much\x01",
            "care and time that the fruit is so\x01",
            "delicious.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_538E")

    label("loc_4FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 5)), scpexpr(EXPR_END)), "loc_51A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50DD")
    OP_A2(0x7)

    ChrTalk(    #235
        0xFE,
        (
            "Pesca relies too much on those\x01",
            "orbment-run machines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "And look what it's brought him:\x01",
            "fruit that tastes much less\x01",
            "delicious than mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "I just don't know how I feel about\x01",
            "shipping out something like that\x01",
            "from Ravennue Village...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51A2")

    label("loc_50DD")


    ChrTalk(    #238
        0xFE,
        (
            "Look what Pesca's machines have\x01",
            "brought him: fruit that tastes much\x01",
            "less delicious than mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "I just don't know how I feel about\x01",
            "shipping out something like that\x01",
            "from Ravennue Village...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51A2")

    Jump("loc_538E")

    label("loc_51A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 4)), scpexpr(EXPR_END)), "loc_5273")

    ChrTalk(    #240
        0xFE,
        (
            "These youngins' ways of cultivation\x01",
            "are nothing less than crude...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "Thinking only about production\x01",
            "instead of quality of taste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xFE,
        (
            "It's utterly deplorable in every sense\x01",
            "of the word...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_538E")

    label("loc_5273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_END)), "loc_532B")

    ChrTalk(    #243
        0xFE,
        (
            "I've been growing fruit here even since\x01",
            "this village was alive with its mining\x01",
            "industry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xFE,
        (
            "When it comes to growing delicious\x01",
            "fruit, I have no equal in this village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_538E")

    label("loc_532B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 1)), scpexpr(EXPR_END)), "loc_538E")

    ChrTalk(    #245
        0xFE,
        (
            "This year's weather is good, and it looks\x01",
            "like any kind of fruit will ripen up nicely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_538E")

    TalkEnd(0xF)
    Return()

    # Function_17_4EAF end

    def Function_18_5392(): pass

    label("Function_18_5392")

    TalkBegin(0x11)
    EventBegin(0x0)
    Fade(1000)
    OP_6D(31970, 8000, 37320, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2920, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 32990, 8000, 38280, 180)
    SetChrPos(0x102, 33860, 8000, 39820, 180)
    SetChrPos(0x103, 31890, 8000, 39180, 180)
    OP_8C(0x11, 0, 400)
    OP_0D()

    ChrTalk(    #246
        0x101,
        "#000F#2PSo this is where you are, Elder Reisen.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        "#1POh, it's you young bracers, is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x103,
        (
            "#020FWell, this is a rather extravagant grave\x01",
            "for a small village like this, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "#1PIt was erected to mourn all those\x01",
            "souls we lost 10 years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "#1PSince the Bose region is nearest\x01",
            "to the Empire, it was in the thick\x01",
            "of the fray...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "#1PAnd this village lost a number of\x01",
            "good people in the hostilities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x101,
        "#003F#2PThat's terrible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x102,
        "#013F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "#1PHa ha. There is no need for you to\x01",
            "get somber too, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "#1PThese days, cleaning this monument\x01",
            "is just one of my daily routines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xFE,
        (
            "#1PBut I guess you wouldn't have come\x01",
            "up here if you didn't think there was\x01",
            "something I could help you with, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x101,
        (
            "#501F#2POh, right. There was something\x01",
            "we wanted to talk to you about.\x02\x03",

            "But before that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0x103,
        (
            "#020FWould you mind if we paid our\x01",
            "respects as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x102,
        (
            "#015F#2PI know we don't have any flowers\x01",
            "to give, but we'd at least like to\x01",
            "offer up a prayer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "#1POh, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        (
            "#1PNo, of course I don't mind. I'm sure\x01",
            "all those looking down from above\x01",
            "would be overjoyed by the gesture.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FA)
    FadeToDark(2000, 0, -1)
    NewScene("ED6_DT01/T1210   ._SN", 100, 0, 0)
    IdleLoop()
    TalkEnd(0x11)
    Return()

    # Function_18_5392 end

    def Function_19_5894(): pass

    label("Function_19_5894")

    OP_A2(0x368)
    OP_28(0x36, 0x1, 0x2)
    EventBegin(0x0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    SetChrPos(0x101, 560, 0, 13490, 225)
    SetChrPos(0x102, 510, 0, 11530, 0)
    SetChrPos(0x103, -820, 0, 12480, 90)
    OP_6D(110, 0, 13180, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #262
        0x103,
        (
            "#020F#3PAll right...\x02\x03",

            "Let's see what we can find out\x01",
            "about the sighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x101,
        (
            "#501FSo what do you suggest?\x01",
            "Should we just go talk to\x01",
            "all the villagers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x102,
        (
            "#010FPeople would be suspicious of\x01",
            "us if we did that all of a sudden.\x02\x03",

            "I think we should talk to the\x01",
            "village elder first and see what\x01",
            "he has to say about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x101,
        "#006FOkay.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_19_5894 end

    def Function_20_5A57(): pass

    label("Function_20_5A57")

    EventBegin(0x0)
    OP_6B(3800, 0)
    OP_6C(90000, 0)
    OP_6D(23730, 0, 31170, 0)
    SetChrPos(0x101, 560, 0, 13490, 0)
    SetChrPos(0x102, 510, 0, 11530, 0)
    SetChrPos(0x103, -820, 0, 12480, 0)
    StopSound(0x9470, 0x30D40, 0x0)
    FadeToBright(2000, 0)

    def lambda_5ACB():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5ACB)
    OP_6D(820, 0, 19100, 8000)
    Fade(2000)
    OP_6D(110, 0, 13180, 0)
    OP_6B(2800, 0)
    StopSound(0x9470, 0x186A0, 0x1F40)
    OP_0D()

    ChrTalk(    #266
        0x101,
        (
            "#000F#4PSo this is Ravennue Village,\x01",
            "huh? This sure is a peaceful\x01",
            "place.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #267
        0x101,
        "#000FLook, there's an orchard.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)
    OP_8C(0x103, 90, 400)

    ChrTalk(    #268
        0x103,
        (
            "#020F#3PThe village is known for its production\x01",
            "of fruit, but it used to have a rich\x01",
            "mining history.\x02\x03",

            "I've heard there's an old abandoned\x01",
            "septium mine to the north of here.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C52():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5C52)
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #269
        0x102,
        (
            "#010FYou seem to know a lot about\x01",
            "the place. Have you been here\x01",
            "before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x103,
        (
            "#020F#3PYeah, when I was training to\x01",
            "become a senior bracer.\x02\x03",

            "During that time I covered the\x01",
            "whole kingdom on foot without\x01",
            "an airliner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        (
            "#004FWhy? An airliner would have been\x01",
            "so much more convenient.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x103,
        (
            "#026F#3P'Airliners are certainly convenient,\x01",
            "but they only go to the five major cities.'\x02\x03",

            "'If you get used to their convenience,\x01",
            "your attention won't reach other places.'\x02\x03",

            "'You should first travel on foot and\x01",
            "see the places you should protect\x01",
            "with your own eyes.'\x02\x03",

            "#020F...is pretty much the way your father,\x01",
            "recommended me to go about my training.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x101,
        "#501FDad really said that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x102,
        (
            "#010FThere's certainly the possibility that if an\x01",
            "incident occurs in a place you're unfamiliar\x01",
            "with, you could end up getting there too late.\x02\x03",

            "Also, it would be pretty advantageous to know\x01",
            "the geography when chasing a criminal...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_607B")

    ChrTalk(    #275
        0x103,
        (
            "#021F#3PHeehee. That's exactly right.\x02\x03",

            "It might be a good idea for you\x01",
            "two to take on that challenge\x01",
            "if you have some time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6206")

    label("loc_607B")

    OP_A2(0x368)
    OP_28(0x36, 0x1, 0x2)

    ChrTalk(    #276
        0x103,
        (
            "#021F#3PHeehee. That's exactly right.\x02\x03",

            "#020FWell, be that as it may...\x02\x03",

            "Let's see what we can find out\x01",
            "about the sighting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x101,
        (
            "#000FSo what do you suggest?\x01",
            "Should we just go talk to\x01",
            "all the villagers?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x102,
        (
            "#010FPeople would be suspicious of\x01",
            "us if we did that all of a sudden.\x02\x03",

            "I think we should talk to the\x01",
            "village elder first and see what\x01",
            "he has to say about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x101,
        "#006FOkay.\x02",
    )

    CloseMessageWindow()

    label("loc_6206")

    EventEnd(0x0)
    Return()

    # Function_20_5A57 end

    def Function_21_6209(): pass

    label("Function_21_6209")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #280
        "\x07\x05It's locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_21_6209 end

    def Function_22_6251(): pass

    label("Function_22_6251")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6266")
    Return()

    label("loc_6266")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_674F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_674C")
    OP_28(0xE, 0x1, 0x2000)
    TalkBegin(0xC)
    EventBegin(0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_64BC")
    OP_28(0xE, 0x1, 0x4000)

    ChrTalk(    #281
        0xC,
        (
            "Sorry, but no one's allowed\x01",
            "beyond this gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xC,
        (
            "I already told you that there have\x01",
            "been rumors of a vicious monster\x01",
            "out there, remember?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x101,
        (
            "#000FI know, but the village elder\x01",
            "asked us to take care of it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #284
        0xC,
        "What...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xC,
        (
            "So does that mean you're with\x01",
            "the Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x103,
        "#020FYep, that's right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(    #287
        0xC,
        "Oh, man. Am I glad you're here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xC,
        (
            "Please see if you can hurry up and\x01",
            "do something about this creature.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xC,
        (
            "The season to plant saplings\x01",
            "is almost upon us.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 400)

    ChrTalk(    #290
        0xC,
        (
            "Anyway, be careful out there\x01",
            "and good luck.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6747")

    label("loc_64BC")

    OP_28(0xE, 0x1, 0x4000)

    ChrTalk(    #291
        0xC,
        (
            "I'm sorry to say this, but no one's\x01",
            "allowed beyond this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xC,
        (
            "I shouldn't be telling you this, but there have\x01",
            "been rumors going around that there's a vicious\x01",
            "monster out on the trail behind the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x101,
        (
            "#000FYeah, and we already talked to\x01",
            "the village elder about it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #294
        0xC,
        "What...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xC,
        (
            "So does that mean you're with\x01",
            "the Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x103,
        "#020FYep, that's right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(    #297
        0xC,
        (
            "Oh, man. It's a good thing you're\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xC,
        (
            "The season to plant saplings\x01",
            "is almost upon us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xC,
        (
            "It would help out a lot if you could\x01",
            "exterminate this monster before\x01",
            "things get really busy around here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x0, 400)

    ChrTalk(    #300
        0xC,
        "Anyway, be cautious out there.\x02",
    )

    CloseMessageWindow()

    label("loc_6747")

    EventEnd(0x3)
    TalkEnd(0xC)

    label("loc_674C")

    Jump("loc_6A71")

    label("loc_674F")

    TalkBegin(0xC)
    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6994")
    OP_A2(0x4)
    OP_28(0xE, 0x1, 0x4000)

    ChrTalk(    #301
        0xC,
        (
            "I'm sorry to say this, but no one's\x01",
            "allowed beyond this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xC,
        (
            "I shouldn't be telling you this, but there have\x01",
            "been rumors going around that there's a vicious\x01",
            "monster out on the trail behind the village.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68DB")

    ChrTalk(    #303
        0x101,
        (
            "#004FSeriously...?! Are people really saying\x01",
            "stuff like that?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #304
        0xC,
        (
            "It would be great if they were just\x01",
            "rumors, but they seem to be true.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68DB")

    TurnDirection(0xC, 0x0, 400)

    ChrTalk(    #305
        0xC,
        (
            "I should probably refer you to the\x01",
            "village elder about the details though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xC,
        (
            "I hear he's requested that the guild\x01",
            "exterminate the monster just to be\x01",
            "on the safe side.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A53")

    label("loc_6994")


    ChrTalk(    #307
        0xC,
        (
            "This place is off limits. You'll need\x01",
            "to talk to the village elder for further\x01",
            "details.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xC, 180, 400)

    ChrTalk(    #308
        0xC,
        (
            "Look, you can see that roof\x01",
            "over there, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xC,
        "That's the village elder's house.\x02",
    )

    CloseMessageWindow()

    label("loc_6A53")

    OP_90(0x0, 0x0, 0x0, 0xFFFFF830, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    TalkEnd(0xC)

    label("loc_6A71")

    Return()

    # Function_22_6251 end

    def Function_23_6A72(): pass

    label("Function_23_6A72")

    FadeToBright(1000, 0)
    SetMapFlags(0x400000)
    EventBegin(0x0)
    OP_6C(45000, 0)
    OP_6D(9600, 8000, 68460, 0)

    def lambda_6AA2():
        OP_6D(7080, 8000, 66150, 3000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6AA2)
    SetChrPos(0xC, 5430, 8000, 66280, 180)
    SetChrPos(0x101, 7080, 8000, 68150, 180)
    SetChrPos(0x102, 7580, 8000, 69650, 180)
    SetChrPos(0x103, 6530, 8000, 69110, 180)

    def lambda_6AFE():
        OP_90(0x101, 0x0, 0x0, 0xFFFFF830, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AFE)
    Sleep(400)

    def lambda_6B1E():
        OP_90(0x102, 0x0, 0x0, 0xFFFFF768, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B1E)
    Sleep(400)

    def lambda_6B3E():
        OP_90(0x103, 0x0, 0x0, 0xFFFFF8F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B3E)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0xC, 400)
    WaitChrThread(0xC, 0x1)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xC, 0x101, 400)
    OP_4A(0xC, 255)

    ChrTalk(    #310
        0xC,
        "Oh...it's you guys?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)
    TurnDirection(0x103, 0xC, 400)
    WaitChrThread(0x102, 0x1)
    TurnDirection(0x102, 0xC, 400)

    ChrTalk(    #311
        0xC,
        "I-I just felt some sort of tremor, so...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xC,
        (
            "The monster came out after all,\x01",
            "did it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x101,
        "#502F#4PTee hee. And we took care of it too!\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #314
        0xC,
        "A-Are you serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0x103,
        (
            "#020FYep. Consider that monster exterminated.\x02\x03",

            "It was a bit feisty, but not a\x01",
            "problem in the end.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(    #316
        0xC,
        "Thank Aidios! This is wonderful news.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xC,
        (
            "It would've been a real mess if\x01",
            "we had monster trouble pop up\x01",
            "any later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xC,
        (
            "I'll hurry and let the village elder\x01",
            "know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #319
        0xC,
        "You guys really did us a favor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xC,
        (
            "I know there's not much to see in\x01",
            "the village, but please enjoy the\x01",
            "relaxing atmosphere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x101,
        "#001F#4PWe'll do that. Thanks.\x02",
    )

    CloseMessageWindow()
    OP_8E(0xC, 0xE88, 0x1F40, 0xFBD6, 0xBB8, 0x0)
    OP_8E(0xC, 0xFFFFF827, 0x1770, 0xF8DE, 0xBB8, 0x0)

    def lambda_6E68():
        OP_92(0x102, 0x101, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6E68)
    OP_92(0x103, 0x101, 0x0, 0xBB8, 0x0)
    SetChrFlags(0xC, 0x80)
    ClearMapFlags(0x400000)
    EventEnd(0x0)
    Return()

    # Function_23_6A72 end

    def Function_24_6E92(): pass

    label("Function_24_6E92")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #322
        (
            "\x07\x05Septian Calendar 1192: Here rest the souls of\x01",
            "six righteous people who lost their lives in the\x01",
            "flames of war.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #323
        (
            "\x07\x05Leif, Abel, Nicole, Wilhelm, Irena, and Mischa.\x01",
            "May you all find rest with the Goddess.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_6E92 end

    def Function_25_6F9C(): pass

    label("Function_25_6F9C")

    SetPlaceName(0x2E)
    Return()

    # Function_25_6F9C end

    def Function_26_6FA0(): pass

    label("Function_26_6FA0")

    SetPlaceName(0x2D)
    Return()

    # Function_26_6FA0 end

    def Function_27_6FA4(): pass

    label("Function_27_6FA4")

    SetPlaceName(0x2F)
    Return()

    # Function_27_6FA4 end

    SaveToFile()

Try(main)
