from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2511   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2511.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Jill',                                 # 9
        'Hans',                                 # 10
        'Mickey',                               # 11
        'Purity',                               # 12
        'Taylor',                               # 13
        'Roy',                                  # 14
        'Patrick',                              # 15
        'Felicity',                             # 16
        'Reina',                                # 17
        'Deborah',                              # 18
        'Janitor Parkes',                       # 19
        'CH22000',                              # 20
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
        'ED6_DT07/CH02390 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT07/CH01080 ._CH',             # 02
        'ED6_DT07/CH01090 ._CH',             # 03
        'ED6_DT07/CH01370 ._CH',             # 04
        'ED6_DT07/CH01580 ._CH',             # 05
        'ED6_DT07/CH01130 ._CH',             # 06
        'ED6_DT07/CH01020 ._CH',             # 07
        'ED6_DT07/CH00003 ._CH',             # 08
        'ED6_DT07/CH00013 ._CH',             # 09
        'ED6_DT07/CH00043 ._CH',             # 0A
        'ED6_DT07/CH01083 ._CH',             # 0B
        'ED6_DT07/CH01373 ._CH',             # 0C
        'ED6_DT06/CH20021 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02390P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH01080P._CP',             # 02
        'ED6_DT07/CH01090P._CP',             # 03
        'ED6_DT07/CH01370P._CP',             # 04
        'ED6_DT07/CH01580P._CP',             # 05
        'ED6_DT07/CH01130P._CP',             # 06
        'ED6_DT07/CH01020P._CP',             # 07
        'ED6_DT07/CH00003P._CP',             # 08
        'ED6_DT07/CH00013P._CP',             # 09
        'ED6_DT07/CH00043P._CP',             # 0A
        'ED6_DT07/CH01083P._CP',             # 0B
        'ED6_DT07/CH01373P._CP',             # 0C
        'ED6_DT06/CH20021P._CP',             # 0D
    )

    DeclNpc(
        X                   = 30800,
        Z                   = 0,
        Y                   = 55110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 29460,
        Z                   = 0,
        Y                   = 53800,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -3600,
        Z                   = 0,
        Y                   = -6100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -31590,
        Z                   = 0,
        Y                   = 58850,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 4100,
        Z                   = 0,
        Y                   = -4000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -29000,
        Z                   = 0,
        Y                   = 53100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -28800,
        Z                   = 0,
        Y                   = 27800,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 27700,
        Z                   = 0,
        Y                   = 23300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 29700,
        Z                   = 0,
        Y                   = 23300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 3500,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -30000,
        Z                   = 0,
        Y                   = 56000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -31350,
        Z                   = 330,
        Y                   = 23900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835021,
        ChipIndex           = 0xD,
        NpcIndex            = 0x166,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -2200,
        Y                   = 0,
        Z                   = 50000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = -2200,
        Y                   = 0,
        Z                   = 42000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 20,
    )

    DeclEvent(
        X                   = 2130,
        Y                   = 0,
        Z                   = 42010,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 2200,
        Y                   = 0,
        Z                   = 50000,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 22,
    )


    DeclActor(
        TriggerX            = -31560,
        TriggerZ            = 0,
        TriggerY            = 59430,
        TriggerRange        = 800,
        ActorX              = -31560,
        ActorZ              = 1000,
        ActorY              = 59430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3060,
        TriggerZ            = 0,
        TriggerY            = 2500,
        TriggerRange        = 400,
        ActorX              = 3500,
        ActorZ              = 1500,
        ActorY              = 4500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -31350,
        TriggerZ            = 330,
        TriggerY            = 23900,
        TriggerRange        = 500,
        ActorX              = -31350,
        ActorZ              = 500,
        ActorY              = 23900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_386",          # 00, 0
        "Function_1_572",          # 01, 1
        "Function_2_5F2",          # 02, 2
        "Function_3_76F",          # 03, 3
        "Function_4_A6A",          # 04, 4
        "Function_5_C7B",          # 05, 5
        "Function_6_CF2",          # 06, 6
        "Function_7_E29",          # 07, 7
        "Function_8_110C",         # 08, 8
        "Function_9_14E8",         # 09, 9
        "Function_10_1876",        # 0A, 10
        "Function_11_1A5F",        # 0B, 11
        "Function_12_1DB1",        # 0C, 12
        "Function_13_1DB6",        # 0D, 13
        "Function_14_24D4",        # 0E, 14
        "Function_15_252A",        # 0F, 15
        "Function_16_3AE9",        # 10, 16
        "Function_17_3DA9",        # 11, 17
        "Function_18_3E16",        # 12, 18
        "Function_19_3FC8",        # 13, 19
        "Function_20_3FCC",        # 14, 20
        "Function_21_3FD0",        # 15, 21
        "Function_22_3FD4",        # 16, 22
    )


    def Function_0_386(): pass

    label("Function_0_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_400")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 11)
    SetChrPos(0xA, -3680, 200, -5980, 270)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    OP_44(0xA, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -32240, 0, 58170, 270)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 28700, 0, 54820, 90)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 30850, 0, 55030, 270)
    Jump("loc_4F2")

    label("loc_400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_40A")
    Jump("loc_4F2")

    label("loc_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_414")
    Jump("loc_4F2")

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_434")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -31700, 0, 58360, 0)
    Jump("loc_4F2")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_443")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_4F2")

    label("loc_443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_4CD")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 11)
    SetChrPos(0xA, -3680, 200, -5980, 270)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x10)
    OP_44(0xA, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 12)
    SetChrPos(0xC, 4050, 200, -4080, 180)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x10)
    OP_44(0xC, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B8")
    SetChrFlags(0xF, 0x10)

    label("loc_4B8")

    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA")
    SetChrFlags(0x10, 0x10)

    label("loc_4CA")

    Jump("loc_4F2")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_4D7")
    Jump("loc_4F2")

    label("loc_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_4E1")
    Jump("loc_4F2")

    label("loc_4E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_4EB")
    Jump("loc_4F2")

    label("loc_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_4F2")

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_509")
    OP_A3(0x3FA)
    Event(0, 16)
    OP_B1("t2511_n")

    label("loc_509")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (108, "loc_515"),
        (SWITCH_DEFAULT, "loc_571"),
    )


    label("loc_515")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56E")
    OP_A2(0x430)
    OP_28(0x1F, 0x4, 0x40)
    OP_28(0x1D, 0x4, 0x40)
    OP_28(0x22, 0x4, 0x40)
    OP_28(0x23, 0x4, 0x40)
    OP_28(0x24, 0x4, 0x40)
    OP_28(0x1C, 0x4, 0x40)
    OP_28(0x20, 0x4, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x334)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_555")
    OP_28(0x21, 0x4, 0x40)

    label("loc_555")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_565")
    OP_28(0x1E, 0x4, 0x40)

    label("loc_565")

    OP_28(0x26, 0x4, 0x40)
    Event(0, 15)

    label("loc_56E")

    Jump("loc_571")

    label("loc_571")

    Return()

    # Function_0_386 end

    def Function_1_572(): pass

    label("Function_1_572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_593")
    OP_B1("t2511_y")
    Jump("loc_59C")

    label("loc_593")

    OP_B1("t2511_n")

    label("loc_59C")

    OP_64(0x0, 0x1)
    OP_64(0x2, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_5B3")
    OP_65(0x2, 0x1)

    label("loc_5B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_5C7")
    OP_64(0x2, 0x1)
    SetChrFlags(0x13, 0x80)

    label("loc_5C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x20)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x27, 0x1, 0x1000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5F1")
    OP_65(0x0, 0x1)

    label("loc_5F1")

    Return()

    # Function_1_572 end

    def Function_2_5F2(): pass

    label("Function_2_5F2")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_617")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_759")

    label("loc_617")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_630")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_759")

    label("loc_630")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_649")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_759")

    label("loc_649")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_662")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_759")

    label("loc_662")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67B")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_759")

    label("loc_67B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_694")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_759")

    label("loc_694")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6AD")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_759")

    label("loc_6AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C6")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_759")

    label("loc_6C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6DF")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_759")

    label("loc_6DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F8")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_759")

    label("loc_6F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_711")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_759")

    label("loc_711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72A")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_759")

    label("loc_72A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_743")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_759")

    label("loc_743")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_759")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_759")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_759")

    label("loc_76E")

    Return()

    # Function_2_5F2 end

    def Function_3_76F(): pass

    label("Function_3_76F")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_7D8")

    ChrTalk(    #0
        0xFE,
        "Ahhhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Ahhh, it's finally over. I think\x01",
            "I'm going to go home and get\x01",
            "some rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A66")

    label("loc_7D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_8F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_892")
    OP_A2(0x0)

    ChrTalk(    #2
        0xFE,
        (
            "I don't want to have anything\x01",
            "to do with the campus festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I'd rather just spend the\x01",
            "time relaxing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Why should I have to get\x01",
            "roped into this crap?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8F4")

    label("loc_892")


    ChrTalk(    #5
        0xFE,
        (
            "I'd rather just spend the\x01",
            "time relaxing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Why should I have to get\x01",
            "roped into this crap?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F4")

    Jump("loc_A66")

    label("loc_8F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_9EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_98A")
    OP_A2(0x0)

    ChrTalk(    #7
        0xFE,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "Ah, well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Class is dull and the student\x01",
            "council president is annoying,\x01",
            "so I'm just killing time here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9EB")

    label("loc_98A")


    ChrTalk(    #10
        0xFE,
        (
            "Class is dull and the student\x01",
            "council president is annoying,\x01",
            "so I'm just killing time here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9EB")

    Jump("loc_A66")

    label("loc_9EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_A66")

    ChrTalk(    #11
        0xFE,
        (
            "Setting up for the campus festival\x01",
            "is such a pain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Let the people that want to be\x01",
            "involved work on it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A66")

    TalkEnd(0xA)
    Return()

    # Function_3_76F end

    def Function_4_A6A(): pass

    label("Function_4_A6A")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x99, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C07")
    OP_A2(0x4CC)

    ChrTalk(    #13
        0xFE,
        "Let's see...maybe around here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I'm looking around for stuff to help\x01",
            "me with the novel I'm writing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "All the books I've been reading\x01",
            "lately have really inspired me to\x01",
            "write something of my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Here, take a look at this one.\x01",
            "I found it particularly moving.\x02",
        )
    )

    CloseMessageWindow()
    OP_3E(0x217, 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #17
        "\x07\x00Received \x07\x02Carnelia - Chapter 6\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #18
        0xFE,
        "Reading is food for the brain.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C77")

    label("loc_C07")


    ChrTalk(    #19
        0xFE,
        "Let's see...maybe around here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I'm looking around for stuff to help\x01",
            "me with the novel I'm writing.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C77")

    TalkEnd(0xB)
    Return()

    # Function_4_A6A end

    def Function_5_C7B(): pass

    label("Function_5_C7B")

    TalkBegin(0xC)

    ChrTalk(    #21
        0xFE,
        (
            "Everyone in the woodwinds\x01",
            "group is late...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I wonder if I should just start\x01",
            "getting ready on my own...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    # Function_5_C7B end

    def Function_6_CF2(): pass

    label("Function_6_CF2")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DED")
    OP_A2(0x3)
    TurnDirection(0xFE, 0x105, 0)

    ChrTalk(    #23
        0xFE,
        (
            "Oh, hi, Kloe.\x01",
            "Good to see you back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x105,
        (
            "#040FHello, Roy.\x01",
            "You look very busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I'm trying to find something for\x01",
            "my class display.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Ha ha...I'd better get a move on\x01",
            "or else I'll never hear the end of\x01",
            "it from Logic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E25")

    label("loc_DED")


    ChrTalk(    #27
        0xFE,
        (
            "I'm trying to find something for\x01",
            "my class program.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E25")

    TalkEnd(0xD)
    Return()

    # Function_6_CF2 end

    def Function_7_E29(): pass

    label("Function_7_E29")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_F23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDB")
    OP_A2(0x4)

    ChrTalk(    #28
        0xFE,
        "Time for club activities!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "If we rest, we'll lose our edge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Of course, you have to have\x01",
            "SOME rest, no matter how\x01",
            "much you want to practice.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F20")

    label("loc_EDB")


    ChrTalk(    #31
        0xFE,
        "Time for club activities!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "If we rest, we'll lose our edge.\x02",
    )

    CloseMessageWindow()

    label("loc_F20")

    Jump("loc_1108")

    label("loc_F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1108")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FDE")
    OP_A2(0x4)

    ChrTalk(    #33
        0xFE,
        (
            "The festival setup phase is when\x01",
            "the club practices and rests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Today, this is all we have to\x01",
            "practice with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Ha ha...but it's obviously\x01",
            "pretty crucial.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1108")

    label("loc_FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_108C")
    OP_A2(0x5)

    ChrTalk(    #36
        0xFE,
        (
            "I'm in the Fencing Club\x01",
            "with Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "I have to help out with the club\x01",
            "food stand later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I don't like leaving Richelle to\x01",
            "handle it all on her own.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1108")

    label("loc_108C")


    ChrTalk(    #39
        0xFE,
        (
            "Now, I need to go help out with\x01",
            "the club's food stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "I don't like leaving Richelle to\x01",
            "handle it all on her own.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1108")

    TalkEnd(0xE)
    Return()

    # Function_7_E29 end

    def Function_8_110C(): pass

    label("Function_8_110C")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_14E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148C")
    OP_A2(0x6)
    OP_A2(0x7)
    OP_4A(0x10, 255)

    ChrTalk(    #41
        0xF,
        "Ugh...I'm sooooo busy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xF,
        (
            "There's the class display, and I'm going\x01",
            "to be in the play later, PLUS I have to\x01",
            "help with the club's food stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xF,
        (
            "It's getting to be a little bit much,\x01",
            "even for me. I wonder if I should\x01",
            "drop one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10,
        (
            "...Sometimes people don't really\x01",
            "make their meanings clear.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 500)

    ChrTalk(    #45
        0xF,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        (
            "Everyone agreed that it was a lot,\x01",
            "but if we all put in our fair share,\x01",
            "we'd get it taken care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        (
            "But he who has made the least\x01",
            "progress will inevitably be the\x01",
            "one to proclaim how busy he is.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #48
        0xF,
        "What are you getting at?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        (
            "Just that I wonder which one\x01",
            "makes you feel the busiest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10,
        (
            "Of course, I always figured you'd\x01",
            "handle all of them with no problem.\x01",
            "I mean, I...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xF, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0xF,
        (
            "All right, all right!\x01",
            "I get it, already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xF,
        "I'll keep working on all of them!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x10)
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    OP_4B(0x10, 255)
    Jump("loc_14E4")

    label("loc_148C")


    ChrTalk(    #53
        0xFE,
        "I swear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "If Reina keeps this up,\x01",
            "I'm going to set fire\x01",
            "to her panty drawer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14E4")

    TalkEnd(0xF)
    Return()

    # Function_8_110C end

    def Function_9_14E8(): pass

    label("Function_9_14E8")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_1872")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1828")
    TalkBegin(0xF)
    OP_A2(0x6)
    OP_A2(0x7)
    OP_4A(0xF, 255)

    ChrTalk(    #55
        0xF,
        (
            "Ugh...I'm soooo busy. There's the class\x01",
            "display, and I'm in the play later, PLUS I\x01",
            "have to help with the club's food stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xF,
        (
            "All of it's getting to be a little\x01",
            "bit much, even for me. I wonder\x01",
            "if I should drop one of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        (
            "...Sometimes people don't really\x01",
            "make their meanings clear.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 500)

    ChrTalk(    #58
        0xF,
        "Huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "Everyone agreed that it was a lot,\x01",
            "but if we all put in our fair share,\x01",
            "we'd get it taken care of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "But he who has made the least\x01",
            "progress will inevitably be the\x01",
            "one to proclaim how busy he is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xF,
        "What are you getting at?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        (
            "Just that I wonder which one\x01",
            "makes you feel the busiest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "Of course, I always figured you'd\x01",
            "handle all of them with no problem.\x01",
            "I mean, I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xF,
        (
            "All right, all right!\x01",
            "I get it, already!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xF,
        "I'll keep working on all of them!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    OP_4B(0xF, 255)
    TalkEnd(0xF)
    Jump("loc_1872")

    label("loc_1828")


    ChrTalk(    #66
        0xFE,
        (
            "Ha ha...you're plenty capable,\x01",
            "but humility is not your strong\x01",
            "suit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1872")

    TalkEnd(0x10)
    Return()

    # Function_9_14E8 end

    def Function_10_1876(): pass

    label("Function_10_1876")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19D0")
    OP_A2(0x8)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #67
        0xFE,
        (
            "#643FHey, Estelle and Joshua!\x01",
            "Did you guys come here\x01",
            "especially to see me?\x02\x03",

            "#640FIt hasn't been so long, but\x01",
            "there's been lots going on,\x01",
            "both good and bad.\x02\x03",

            "It sure is good to see you two.\x02\x03",

            "Once everything really settles\x01",
            "down for good, we can all\x01",
            "focus on our futures.\x02\x03",

            "#648FI hope you have fun when\x01",
            "you go to Zeiss.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A5B")

    label("loc_19D0")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #68
        0xFE,
        (
            "#640FOnce everything really settles\x01",
            "down for good, we can all\x01",
            "focus on our futures.\x02\x03",

            "I hope you have fun when\x01",
            "you go to Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A5B")

    TalkEnd(0x8)
    Return()

    # Function_10_1876 end

    def Function_11_1A5F(): pass

    label("Function_11_1A5F")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC5")
    OP_A2(0xA)
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #69
        0xFE,
        (
            "#733FWell, if it ain't Joshua and Estelle.\x02\x03",

            "#732FI read in the Liberl News about\x01",
            "Mayor Dalmore and his dirty\x01",
            "little schemes.\x02\x03",

            "I guess that's why he acted all\x01",
            "innocent and benevolent when he\x01",
            "gave his donation at the festival.\x02\x03",

            "And he was even nasty enough to\x01",
            "attack the matron afterwards!\x02\x03",

            "He must really be rotten\x01",
            "to the core...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAD")

    label("loc_1BC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF4")
    OP_A2(0xB)
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #70
        0xFE,
        (
            "#730FAnyway, you two look like you're\x01",
            "headed for Zeiss.\x02\x03",

            "So this really is goodbye,\x01",
            "at least for now...\x02\x03",

            "But if we all live our lives to the\x01",
            "fullest, there's no way this is\x01",
            "the last time we'll meet.\x02\x03",

            "For now, I just wish you the \x01",
            "best of luck in becoming\x01",
            "full-fledged bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAD")

    label("loc_1CF4")

    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #71
        0xFE,
        (
            "#730FIf we all live our lives to the\x01",
            "fullest, there's no way this\x01",
            "is the last time we'll meet.\x02\x03",

            "For now, I just wish you the \x01",
            "best of luck in becoming\x01",
            "full-fledged bracers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DAD")

    TalkEnd(0x9)
    Return()

    # Function_11_1A5F end

    def Function_12_1DB1(): pass

    label("Function_12_1DB1")

    Call(0, 13)
    Return()

    # Function_12_1DB1 end

    def Function_13_1DB6(): pass

    label("Function_13_1DB6")

    TalkBegin(0x11)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                          # 0
            "Shop\x01",                          # 1
            "[Jenis Lunch] - 500 mira\x01",      # 2
            "Leave\x01",                         # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E2F")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x30)
    OP_56(0x0)
    TalkEnd(0x11)
    Return()

    label("loc_1E2F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F35")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EFB")
    SubMira(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #72
        "\x06\x07\x00Ate \x07\x02Jenis Lunch\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x2BC)
    OP_31(0x1, 0xFD, 0x2BC)
    OP_31(0x2, 0xFD, 0x2BC)
    OP_31(0x3, 0xFD, 0x2BC)
    OP_31(0x4, 0xFD, 0x2BC)
    OP_31(0x5, 0xFD, 0x2BC)
    OP_31(0x6, 0xFD, 0x2BC)
    OP_31(0x7, 0xFD, 0x2BC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EED")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x9)"), scpexpr(EXPR_END)), "loc_1EC0")
    Jump("loc_1EED")

    label("loc_1EC0")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #73
        "\x06\x07\x00Learned '\x07\x02Jenis Lunch\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_1EED")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_1F23")

    label("loc_1EFB")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #74
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_1F23")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x11)
    Return()

    label("loc_1F35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F4F")
    FadeToBright(300, 0)
    TalkEnd(0x11)
    Return()

    label("loc_1F4F")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_1F89")

    ChrTalk(    #75
        0x11,
        (
            "Hey there!\x01",
            "What can I do for you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_1F89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_END)), "loc_210F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20C6")

    ChrTalk(    #76
        0x11,
        (
            "I got to see the play earlier.\x01",
            "You folks did a really great job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x11,
        (
            "To thank you for all your hard work on\x01",
            "it, please, take this. It's not much,\x01",
            "but you might find some use for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        "On the house.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x452)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #79
        "\x07\x00Received \x07\x02Vegetable Sandwich\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x193, 1)
    Jump("loc_210C")

    label("loc_20C6")


    ChrTalk(    #80
        0x11,
        (
            "I got to see the play earlier.\x01",
            "You folks did a really great job.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210C")

    Jump("loc_24D0")

    label("loc_210F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 2)), scpexpr(EXPR_END)), "loc_2172")

    ChrTalk(    #81
        0x11,
        "You folks are in the play, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x11,
        (
            "I'm planning to go see it.\x01",
            "I hope it's good!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_2172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 1)), scpexpr(EXPR_END)), "loc_21CE")

    ChrTalk(    #83
        0x11,
        (
            "The place is open today as a\x01",
            "rest area.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x11,
        "Still got the same food though!\x02",
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_21CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_END)), "loc_2268")

    ChrTalk(    #85
        0x11,
        (
            "I'll bet you've been so involved\x01",
            "with setting up that you haven't\x01",
            "been eating so well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x11,
        (
            "Kids like you need to make\x01",
            "sure you eat right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_2268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 7)), scpexpr(EXPR_END)), "loc_22F1")

    ChrTalk(    #87
        0x11,
        "So, how's the festival setup going?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x11,
        (
            "You need to keep your strength\x01",
            "up, so big servings all around.\x01",
            "Come by any time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_22F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 6)), scpexpr(EXPR_END)), "loc_2369")

    ChrTalk(    #89
        0x11,
        "Well, now...classes are almost over.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x11,
        (
            "I should get flooded with hungry\x01",
            "young students here, shortly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_2369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_23E0")

    ChrTalk(    #91
        0x11,
        (
            "Well, if it isn't Kloe. I thought\x01",
            "you'd be in class still.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x11,
        (
            "I'm sorry, hon, but we're not\x01",
            "open yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_23E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_END)), "loc_245A")

    ChrTalk(    #93
        0x11,
        (
            "Oh, aren't you thinking of\x01",
            "enrolling here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x11,
        (
            "Well, you don't have to be a\x01",
            "student to eat here, sweetie.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D0")

    label("loc_245A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_24D0")

    ChrTalk(    #95
        0x11,
        (
            "What'll you have to eat for your\x01",
            "little field trip?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x11,
        (
            "If you're hungry, you don't have\x01",
            "to be shy here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D0")

    TalkEnd(0x11)
    Return()

    # Function_13_1DB6 end

    def Function_14_24D4(): pass

    label("Function_14_24D4")

    TalkBegin(0x12)

    ChrTalk(    #97
        0xFE,
        "Doesn't look like anyone's here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "Is it okay to go ahead and lock up?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x12)
    Return()

    # Function_14_24D4 end

    def Function_15_252A(): pass

    label("Function_15_252A")

    EventBegin(0x0)
    SetMapFlags(0x10000000)
    OP_6D(31070, 0, 57740, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x40)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #99
        0x8,
        (
            "#644F#5P*sigh*...So busy.\x02\x03",

            "The budgets for all of the\x01",
            "concession stands have been\x01",
            "checked over...\x02\x03",

            "No problems with sending out\x01",
            "the invitations...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x9,
        (
            "#734FNow all that's left is the play...\x02\x03",

            "If we can't find anyone to fill the last two\x01",
            "roles, the only option might be for us to fill\x01",
            "them in ourselves...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #101
        0x8,
        (
            "#645F#5POh, no, there's no way YOU'RE acting in the\x01",
            "play.\x02\x03",

            "The horrors I witnessed when we first tried\x01",
            "those costumes on are going to haunt me for the\x01",
            "rest of my life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "#732FDon't remind me... I never want to wear anything\x01",
            "like that ever again.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x102, 24910, 0, 55980, 243)
    SetChrPos(0x101, 24910, 0, 55980, 243)
    SetChrPos(0x105, 24910, 0, 55980, 243)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    ChrTalk(    #103
        0x105,
        "#2PI'm back, Jill. Hello, Hans.\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x8, 0x105, 400)
    TurnDirection(0x9, 0x105, 400)

    def lambda_287A():
        OP_6D(29890, 0, 55890, 1500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_287A)
    ClearChrFlags(0x105, 0x80)

    def lambda_2897():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_2897)
    OP_8E(0x105, 0x6928, 0x0, 0xD99E, 0x7D0, 0x0)

    def lambda_28BD():
        OP_8E(0xFE, 0x6D06, 0x0, 0xD480, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_28BD)
    OP_8C(0x9, 270, 0)
    ClearChrFlags(0x101, 0x80)

    def lambda_28E4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_28E4)
    OP_8E(0x101, 0x6928, 0x0, 0xD99E, 0x7D0, 0x0)

    def lambda_290A():
        OP_8E(0xFE, 0x6996, 0x0, 0xD5AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_290A)
    ClearChrFlags(0x102, 0x80)

    def lambda_292A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_292A)

    def lambda_293C():
        OP_8E(0xFE, 0x6B30, 0x0, 0xD9C6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_293C)
    WaitChrThread(0x105, 0x1)

    def lambda_295C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_295C)
    WaitChrThread(0x101, 0x1)

    def lambda_296F():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_296F)
    WaitChrThread(0x102, 0x1)

    def lambda_2982():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2982)

    def lambda_2990():

        label("loc_2990")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2990")

    QueueWorkItem2(0x102, 1, lambda_2990)

    def lambda_29A1():

        label("loc_29A1")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_29A1")

    QueueWorkItem2(0x101, 1, lambda_29A1)

    def lambda_29B2():

        label("loc_29B2")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_29B2")

    QueueWorkItem2(0x105, 1, lambda_29B2)

    ChrTalk(    #104
        0x8,
        (
            "#642FKloe?!\x02\x03",

            "I heard about the fire.\x01",
            "It must have been awful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "#732FWere the matron and kids\x01",
            "all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x105,
        (
            "#040FYes... They're fine, for now.\x02\x03",

            "#049FThe orphanage was burnt to\x01",
            "the ground, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        "#732FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        (
            "#644FWell, try to keep your spirits up.\x01",
            "Fretting won't do anyone any good.\x02\x03",

            "The best thing we can do is\x01",
            "make the play something the\x01",
            "kids can enjoy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x105,
        (
            "#045FYes, Matron Theresa gave us\x01",
            "the same advice.\x02\x03",

            "So, we'll give it our best.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        (
            "#641FWith your help, I'm sure everything\x01",
            "will turn out fine.\x02\x03",

            "#640FTo think I was stressing about\x01",
            "it just a few minutes ago.\x02\x03",

            "Who are your friends?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#501FNice to meet you.\x01",
            "My name's Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#010FI'm Joshua. It's a pleasure\x01",
            "to make your acquaintance.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #113
        0x8,
        (
            "#643FSo you must be the ones\x01",
            "Kloe spoke of before!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x105,
        (
            "#041FHa ha. I told you I'd bring\x01",
            "them here.\x02\x03",

            "They'll be helping, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x8,
        (
            "#641FOh, that's a relief!\x02\x03",

            "#641FI'm glad to meet both of you.\x02\x03",

            "I'm Jill Ridonor. I'm the head\x01",
            "of the Student Council.\x02\x03",

            "I'll be directing the play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x9,
        (
            "#730FAnd I'm the vice president, Hans.\x02\x03",

            "It's nice to meet you both.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x101,
        "#000FLikewise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x102,
        "#010FGood to meet you, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x8,
        "#644FHmm... Y'know...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x8)

    ChrTalk(    #120
        0x101,
        "#004FWh-What...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x8,
        (
            "#640FWith bracers here, maybe we\x01",
            "can incorporate stunts.\x02\x03",

            "Are you any good with a sword,\x01",
            "Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#008FWeeeell...\x02\x03",

            "My father mainly trained me on\x01",
            "the staff, but I'm not hopeless,\x01",
            "at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x8,
        (
            "#641FOkay, then that settles it.\x02\x03",

            "You'll have a big sword fight\x01",
            "with Kloe.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #124
        0x101,
        "#004FWhoa, whoa, whoa... A sword fight?!\x02",
    )

    CloseMessageWindow()
    OP_44(0x105, 0xFF)
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x105, 400)
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #125
        0x105,
        "#040F#2PShe means in the play, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        (
            "#640FThere's a duel between the two\x01",
            "knights at the climax of the play.\x02\x03",

            "It's a really powerful scene.\x01",
            "Perfect for the final act.\x02\x03",

            "#645FWe don't have any girls who can use\x01",
            "a sword well enough to compete with\x01",
            "Kloe, much less make it look good.\x02\x03",

            "She beat every guy in the fencing\x01",
            "tournament and took the top spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#501FOh, wow!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x8,
        (
            "#649FShe actually beat out Hans in\x01",
            "the final match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x9,
        (
            "#734FThanks for reminding me, Jill...\x02\x03",

            "It's not that I'm no good. It's\x01",
            "just that Kloe is waaay better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x105,
        (
            "#045F#2PI-I'm still only an amateur...\x02\x03",

            "I don't think I'd be any match for\x01",
            "a professional like Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        (
            "#006FAnd again with the modesty!\x02\x03",

            "But hey, if you need my help,\x01",
            "I'm your girl.\x02\x03",

            "#001FWe can do it, Kloe! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x105,
        "#041F#2PI'm sure we can. Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x102,
        (
            "#019F#1PHa ha... You know...\x02\x03",

            "A duel between two female knights\x01",
            "ought to be pretty unique.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)

    ChrTalk(    #134
        0x9,
        (
            "#733FFemale knights?\x02\x03",

            "They're going to be playing\x01",
            "the two MALE knights.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_33F1():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_33F1)
    TurnDirection(0x102, 0x9, 0)
    Sleep(400)

    ChrTalk(    #135
        0x102,
        "#014F#1PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "#649FBut that leaves us without a\x01",
            "role for Joshua...\x02\x03",

            "Oh, my, whatever shall we do?\x01",
            "He deserves to play a 'crucial\x01",
            "role' in this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x9,
        (
            "#731FYes...a crucial role...\x01",
            "I think we may have just\x01",
            "the part for him...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#501F???\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #139
        0x102,
        (
            "#014FUmm... What kind of play is\x01",
            "this, exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x8,
        (
            "#640FIt's called,\x01",
            "'Madrigal of the White Magnolia.'\x02\x03",

            "It's a famous story, set in\x01",
            "a time where there are\x01",
            "nobles and commoners.\x02\x03",

            "#647FA princess is courted by both\x01",
            "a knight of royal blood and\x01",
            "a commoner. \x02\x03",

            "#642FIn spite of their different social\x01",
            "classes, the three have been\x01",
            "friends since childhood.\x02\x03",

            "As you can imagine, this leads\x01",
            "to complications between the\x01",
            "nobles and the commoners.\x02\x03",

            "#648FAnd there's a great happy\x01",
            "ending to the whole thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        "#001FHey, that sounds like fun. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x102,
        (
            "#014FSo then...\x02\x03",

            "Why are the girls playing the\x01",
            "guy roles?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x9,
        (
            "#731FIt's just something to make the\x01",
            "production more interesting\x01",
            "this time.\x02\x03",

            "Having guys and girls switch\x01",
            "roles, that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#004FReally...?\x02\x03",

            "Wow...and the teachers are\x01",
            "okay with this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x8,
        (
            "#644F'End sexual discrimination!\x01",
            "Be free of gender roles!'\x02\x03",

            "Put in that light, the teachers\x01",
            "loved the idea.\x02\x03",

            "#641FPersonally, I just thought people\x01",
            "would get a kick out of it! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x105,
        "#045FJill, you're incorrigible.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x9,
        (
            "#734FYep, though she says she prefers\x01",
            "the title, 'Evil Genius.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#001FHa ha ha.\x01",
            "I'm totally up for this. ☆\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(    #149
        0x102,
        (
            "#018F#1PHey, hold on a second! From\x01",
            "what you're telling me, then...\x02\x03",

            "...the 'crucial role' you need\x01",
            "me to play is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x9,
        (
            "#731FYep, you're really doing us\x01",
            "a massive favor here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x8,
        (
            "#641FThank you for introducing us to\x01",
            "such nice people, Kloe. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x105,
        (
            "#045F#2PUmm... Ha ha ha...\x02\x03",

            "I'm sorry, Joshua...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_28(0x3D, 0x1, 0x20)
    OP_28(0x3D, 0x1, 0x40)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2513   ._SN", 113, 0, 0)
    IdleLoop()
    Return()

    # Function_15_252A end

    def Function_16_3AE9(): pass

    label("Function_16_3AE9")

    EventBegin(0x0)
    OP_6D(6500, 0, -150, 0)
    OP_77(0xFF, 0xC8, 0x96, 0x0, 0x0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x105, 6070, 100, -420, 180)
    SetChrPos(0x101, 6070, 100, -2400, 0)
    SetChrPos(0x8, 5150, 0, -260, 180)
    SetChrChipByIndex(0x101, 8)
    SetChrChipByIndex(0x105, 10)
    SetChrPos(0x102, -230, -250, -7260, 0)
    SetChrPos(0x9, 280, -250, -6290, 0)
    OP_62(0x101, 0x0, 1850, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x105, 0x0, 1850, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    OP_62(0x101, 0x0, 1850, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x105, 0x0, 1850, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)

    def lambda_3C0B():
        OP_6D(5210, 0, -1580, 2000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3C0B)

    def lambda_3C23():
        OP_8E(0xFE, 0x8E8, 0x0, 0xFFFFF8EE, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3C23)
    Sleep(500)

    def lambda_3C43():
        OP_8E(0xFE, 0x8FC, 0x0, 0xFFFFF4AC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C43)
    SetChrSubChip(0x101, 1)
    SetChrSubChip(0x105, 2)

    def lambda_3C68():

        label("loc_3C68")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_3C68")

    QueueWorkItem2(0x8, 1, lambda_3C68)
    WaitChrThread(0x9, 0x1)

    def lambda_3C7E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3C7E)
    WaitChrThread(0x102, 0x1)

    def lambda_3C91():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3C91)
    Sleep(500)
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x102, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    OP_62(0x101, 0x0, 1850, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x105, 0x0, 1850, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()

    AnonymousTalk(    #153
        (
            "\x07\x05As the day wore on, lunch was enjoyed by all over pleasant, silly\x01",
            "conversation--mostly revolving around how Joshua might look in heels.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2513   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3AE9 end

    def Function_17_3DA9(): pass

    label("Function_17_3DA9")

    OP_A3(0xD)
    OP_A3(0xE)
    OP_22(0x11, 0x0, 0x64)
    SetChrFlags(0x13, 0x80)
    OP_64(0x2, 0x1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #154
        "\x07\x00Found \x07\x02Ruan Economics I\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x33D, 1)
    OP_28(0x27, 0x1, 0x40)
    TalkEnd(0xFF)
    Return()

    # Function_17_3DA9 end

    def Function_18_3E16(): pass

    label("Function_18_3E16")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Return Ruan Economics books]\x01",      # 0
            "[Cancel]\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3E8E"),
        (1, "loc_3FA8"),
        (SWITCH_DEFAULT, "loc_3FAB"),
    )


    label("loc_3E8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_END)), "loc_3EEA")
    OP_3F(0x33D, 1)
    OP_28(0x27, 0x1, 0x200)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #155
        "\x07\x00Returned \x07\x02Ruan Economics I\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3EEA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_END)), "loc_3F47")
    OP_3F(0x33E, 1)
    OP_28(0x27, 0x1, 0x400)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #156
        "\x07\x00Returned \x07\x02Ruan Economics II\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3F47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_END)), "loc_3FA5")
    OP_3F(0x33F, 1)
    OP_28(0x27, 0x1, 0x800)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #157
        "\x07\x00Returned \x07\x02Ruan Economics III\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3FA5")

    Jump("loc_3FAB")

    label("loc_3FA8")

    Jump("loc_3FAB")

    label("loc_3FAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x33D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x33E)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x33F)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FC4")
    OP_64(0x0, 0x1)

    label("loc_3FC4")

    TalkEnd(0xFF)
    Return()

    # Function_18_3E16 end

    def Function_19_3FC8(): pass

    label("Function_19_3FC8")

    SetPlaceName(0x71)
    Return()

    # Function_19_3FC8 end

    def Function_20_3FCC(): pass

    label("Function_20_3FCC")

    SetPlaceName(0x72)
    Return()

    # Function_20_3FCC end

    def Function_21_3FD0(): pass

    label("Function_21_3FD0")

    SetPlaceName(0x75)
    Return()

    # Function_21_3FD0 end

    def Function_22_3FD4(): pass

    label("Function_22_3FD4")

    SetPlaceName(0x70)
    Return()

    # Function_22_3FD4 end

    SaveToFile()

Try(main)
