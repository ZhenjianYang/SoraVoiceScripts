from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0410   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0410.x',
        MapIndex            = 13,
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
        'Tio',                                  # 9
        'Will',                                 # 10
        'Chere',                                # 11
        'Franz',                                # 12
        'Hannah',                               # 13
        'Father Kevin',                         # 14
        'Will',                                 # 15
        'Chere',                                # 16
        'Franz',                                # 17
        'Hannah',                               # 18
        '皿',                                   # 19
        '皿',                                   # 20
        '皿',                                   # 21
        '皿',                                   # 22
        '皿',                                   # 23
        'サラダ',                               # 24
        'パン',                                 # 25
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
        'ED6_DT26/CH20331 ._CH',             # 00
        'ED6_DT26/CH20336 ._CH',             # 01
        'ED6_DT27/CH03080 ._CH',             # 02
        'ED6_DT06/CH20020 ._CH',             # 03
        'ED6_DT26/CH20313 ._CH',             # 04
        'ED6_DT26/CH20314 ._CH',             # 05
        'ED6_DT07/CH02480 ._CH',             # 06
        'ED6_DT07/CH01060 ._CH',             # 07
        'ED6_DT07/CH01070 ._CH',             # 08
        'ED6_DT07/CH01020 ._CH',             # 09
        'ED6_DT07/CH01030 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT26/CH20331P._CP',             # 00
        'ED6_DT26/CH20336P._CP',             # 01
        'ED6_DT27/CH03080P._CP',             # 02
        'ED6_DT06/CH20020P._CP',             # 03
        'ED6_DT26/CH20313P._CP',             # 04
        'ED6_DT26/CH20314P._CP',             # 05
        'ED6_DT07/CH02480P._CP',             # 06
        'ED6_DT07/CH01060P._CP',             # 07
        'ED6_DT07/CH01070P._CP',             # 08
        'ED6_DT07/CH01020P._CP',             # 09
        'ED6_DT07/CH01030P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = 35040,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 1320,
        Z                   = 0,
        Y                   = 37500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 80,
        Z                   = 0,
        Y                   = 32400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 500,
        Z                   = 0,
        Y                   = 35060,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -76340,
        Z                   = 0,
        Y                   = 31640,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 458753,
        ChipIndex           = 0x1,
        NpcIndex            = 0x187,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -73490,
        Z                   = 0,
        Y                   = 31660,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1507329,
        ChipIndex           = 0x1,
        NpcIndex            = 0x187,
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
        Unknown3            = 196611,
        ChipIndex           = 0x3,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196611,
        ChipIndex           = 0x3,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196611,
        ChipIndex           = 0x3,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196611,
        ChipIndex           = 0x3,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 196611,
        ChipIndex           = 0x3,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 458755,
        ChipIndex           = 0x3,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1769475,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_322",          # 00, 0
        "Function_1_472",          # 01, 1
        "Function_2_4C7",          # 02, 2
        "Function_3_644",          # 03, 3
        "Function_4_1090",         # 04, 4
        "Function_5_1B91",         # 05, 5
        "Function_6_20DE",         # 06, 6
        "Function_7_25EB",         # 07, 7
        "Function_8_28DE",         # 08, 8
        "Function_9_2C63",         # 09, 9
        "Function_10_336F",        # 0A, 10
        "Function_11_33C1",        # 0B, 11
        "Function_12_3413",        # 0C, 12
        "Function_13_3485",        # 0D, 13
        "Function_14_34D7",        # 0E, 14
        "Function_15_353E",        # 0F, 15
        "Function_16_355F",        # 10, 16
        "Function_17_35A7",        # 11, 17
        "Function_18_4B94",        # 12, 18
        "Function_19_4BCD",        # 13, 19
        "Function_20_4C06",        # 14, 20
        "Function_21_4DC7",        # 15, 21
    )


    def Function_0_322(): pass

    label("Function_0_322")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_335")
    Jump("loc_3F9")

    label("loc_335")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F9")
    SetChrPos(0xD, -75610, 0, 2580, 270)
    OP_44(0xA, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0x8, 0xFF)
    SetChrPos(0x8, -77060, 0, 3150, 180)
    SetChrPos(0xA, -73600, 0, 2980, 180)
    SetChrPos(0x9, -72950, 0, 2980, 180)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0xA, 1)
    SetChrSubChip(0xA, 55)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 71)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 39)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)

    label("loc_3F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_42F")
    SetChrPos(0xB, -39020, 0, 33240, 180)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 3820, 0, 24640, 155)
    Jump("loc_43B")

    label("loc_42F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_43B")
    SetChrFlags(0xB, 0x80)

    label("loc_43B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_455")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 20)
    Jump("loc_471")

    label("loc_455")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_471")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_471")
    Event(0, 9)

    label("loc_471")

    Return()

    # Function_0_322 end

    def Function_1_472(): pass

    label("Function_1_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_487")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_487")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49A")
    Jump("loc_4C6")

    label("loc_49A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C6")
    OP_6F(0x5, 20)
    OP_6F(0x6, 20)
    OP_6F(0x7, 20)
    OP_6F(0x8, 20)

    label("loc_4C6")

    Return()

    # Function_1_472 end

    def Function_2_4C7(): pass

    label("Function_2_4C7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EC")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_62E")

    label("loc_4EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_505")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_62E")

    label("loc_505")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51E")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_62E")

    label("loc_51E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_537")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_62E")

    label("loc_537")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_550")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_62E")

    label("loc_550")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_569")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_62E")

    label("loc_569")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_582")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_62E")

    label("loc_582")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_62E")

    label("loc_59B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B4")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_62E")

    label("loc_5B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5CD")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_62E")

    label("loc_5CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5E6")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_62E")

    label("loc_5E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FF")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_62E")

    label("loc_5FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_618")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_62E")

    label("loc_618")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_62E")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_62E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_643")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_62E")

    label("loc_643")

    Return()

    # Function_2_4C7 end

    def Function_3_644(): pass

    label("Function_3_644")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_FDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD1")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #0
        0xFE,
        "Oh, hey, you two! You're back?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        "#1000FYeah. We're here on a bit of guild work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        "#1040FIt's been a while.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #3
        0xFE,
        (
            "Yeah, it has been, but you\x01",
            "both seem to be doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Rolent may just have a bright future\x01",
            "ahead of it after all!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_783")

    ChrTalk(    #5
        0x103,
        "#021FThat would be nice.\x02",
    )

    CloseMessageWindow()

    label("loc_783")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_819")

    ChrTalk(    #6
        0x106,
        (
            "#555FYou're overstatin' it, old man.\x02\x03",

            "#051FIt's true that these two've really\x01",
            "pulled their weight, but they ain't\x01",
            "miracle workers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_819")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_86B")

    ChrTalk(    #7
        0x108,
        (
            "#071FHaha. I guess there's a lot of\x01",
            "hometown pride in you two.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_883")
    TurnDirection(0xFE, 0x108, 400)
    Jump("loc_8B0")

    label("loc_883")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_89B")
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_8B0")

    label("loc_89B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8B0")
    TurnDirection(0xFE, 0x103, 400)

    label("loc_8B0")


    ChrTalk(    #8
        0xFE,
        "Well, we're all in a bit of a fix here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "It's only natural to put our hopes on\x01",
            "the bracers from our own backyard.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #10
        0xFE,
        "At least our situation is manageable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Farming was always classically done\x01",
            "by hand, so we just have to relearn the\x01",
            "old ways. Might be good for us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1015FThat's true. There weren't really\x01",
            "machines back then to help like\x01",
            "we have now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Of course, with the scheduled liners\x01",
            "not running, I can't really move anything\x01",
            "I do farm, but I'll still do what I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "We're all hoping the darn things get\x01",
            "restored soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1006FYeah...\x02\x03",

            "It's definitely a big problem, but we're\x01",
            "doing what we can, too, to get it sorted\x01",
            "as quickly as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#1040FIt's nice to see you so dedicated\x01",
            "to your work, and to Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "Yeah, well. You know how it is.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20AA)
    Jump("loc_FD9")

    label("loc_BD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_E01")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D54")

    ChrTalk(    #18
        0xFE,
        (
            "Of course, Hannah's having a rough\x01",
            "time of it, since she can't use her oven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Guess tonight we'll have no choice\x01",
            "but to cook on the hearth like in the\x01",
            "old days.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "The kids prefer it that way anyway,\x01",
            "so it's no big deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "I'm sure they'll be running around without\x01",
            "a care no matter how they get their food.\x01",
            "And we're just grateful they're getting it!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_DFE")

    label("loc_D54")


    ChrTalk(    #22
        0xFE,
        (
            "Of course, Hannah's having a rough\x01",
            "time of it, since she can't use her oven.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Guess tonight we'll have no choice\x01",
            "but to cook on the hearth like in the\x01",
            "old days.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DFE")

    Jump("loc_FD9")

    label("loc_E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3C")

    ChrTalk(    #24
        0xFE,
        (
            "We can keep the farm running by\x01",
            "hand for the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Still, if the scheduled liners don't resume\x01",
            "service soon, we won't be able to ship our\x01",
            "vegetables anywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "Look. Just look at this pile of produce here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "If the liners stay out of service,\x01",
            "these'll all just rot and go to waste.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_FD9")

    label("loc_F3C")


    ChrTalk(    #28
        0xFE,
        (
            "The hardest part is that I can't export\x01",
            "our wares to the Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "So I'm really hoping things will go back\x01",
            "to normal soon. I guess we all are.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD9")

    Jump("loc_108C")

    label("loc_FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_108C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 7)), scpexpr(EXPR_END)), "loc_1088")

    ChrTalk(    #30
        0xFE,
        (
            "If the guild's launching an investigation,\x01",
            "the fog must be really bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "My deliveries are already done for today,\x01",
            "but tomorrow's another story...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_108C")

    label("loc_1088")

    Call(0, 5)

    label("loc_108C")

    TalkEnd(0xB)
    Return()

    # Function_3_644 end

    def Function_4_1090(): pass

    label("Function_4_1090")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1596")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C6")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #32
        0xFE,
        (
            "Oh, my...\x01",
            "If it isn't Estelle and Joshua!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1001FHello, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        "#1040FHow is everything?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #35
        0xFE,
        (
            "Well, I'm fine, but my family is\x01",
            "having a hard time of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Everything powered by orbments has\x01",
            "shut down, so none of my cooking\x01",
            "equipment is working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "This morning's breakfast was cold\x01",
            "sandwiches, of all things!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "All those poor guardsmen are\x01",
            "here, too, and I've no way to make\x01",
            "them something hot. I feel so bad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1015FI dunno...\x02\x03",

            "If you ask me, your sandwiches are\x01",
            "pretty darn good!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        "#1040FI have to agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "Haha, oh, stop!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "All right, drop on by again when you\x01",
            "get some free time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "I'll make sure I've got plenty of\x01",
            "sandwiches for you, on the house!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1001FOkay! We've totally got a deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        "#1040FWe'll come back for sure. Thank you!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20AB)
    Jump("loc_1593")

    label("loc_13C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_14AD")

    ChrTalk(    #46
        0xFE,
        (
            "Chere and Will have really been\x01",
            "pitching in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I'm sure they must realize how tough\x01",
            "we've got it right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "Haha, I never thought the loss of\x01",
            "orbment functionality would help\x01",
            "bring us all together like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1593")

    label("loc_14AD")


    ChrTalk(    #49
        0xFE,
        (
            "It's really tough having all my orbal\x01",
            "cooking instruments out of commission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "I can't make anything that requires\x01",
            "controlled heating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "*sigh* I suppose I'll just have to make\x01",
            "some kind of potted dish over the hearth.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1593")

    Jump("loc_1B8D")

    label("loc_1596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_1AF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34C, 7)), scpexpr(EXPR_END)), "loc_169A")

    ChrTalk(    #52
        0xFE,
        (
            "For as young as you are, you're remarkably\x01",
            "good at holding back your true desires.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "But sometimes, it's more polite to\x01",
            "give in and tell people what you want!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Just close your mouth and accept what\x01",
            "you're being offered. No 'buts!'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AF6")

    label("loc_169A")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #55
        0xFE,
        "Thanks for coming, you two.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "I know how much we owe you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "As my way of saying thanks,\x01",
            "please accept this. It's our own\x01",
            "special blend of tea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1008FN-No... I couldn't!\x02\x03",

            "Kevin's the one who did all the work,\x01",
            "ma'am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "Haha. You're just like him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        "That priest said the same thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#1016FAhaha... Did he, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "It's not as if we're strangers, you know.\x01",
            "You don't need to be so formal with me,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "When you're being offered something out of\x01",
            "the goodness of someone's heart, there's\x01",
            "nothing at all wrong with just taking it!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #64
        0x103,
        (
            "#020FGo ahead, Estelle.\x02\x03",

            "I understand you're just trying to be\x01",
            "polite, but this is Hannah. She's not\x01",
            "going to judge you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1015FY-Yeah...\x02\x03",

            "#1000FOkay, then.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #66
        "\x07\x00Received #415i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x19F, 1)

    ChrTalk(    #67
        0xFE,
        (
            "When you get tired, drink that and\x01",
            "it'll put some spirit back in you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        "#1018FWow! Thanks, Hannah!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xFE, 400)

    ChrTalk(    #69
        0x103,
        (
            "#021FThanks, indeed! We appreciate your\x01",
            "thoughtfulness.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #70
        0xFE,
        "It's the least I could do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "If you have the time, please do\x01",
            "come by and visit again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A67)

    label("loc_1AF6")

    Jump("loc_1B8D")

    label("loc_1AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_1B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 7)), scpexpr(EXPR_END)), "loc_1B89")

    ChrTalk(    #72
        0xFE,
        (
            "The fog wasn't this bad when we\x01",
            "went out for deliveries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I'd better make sure the kids don't\x01",
            "go outside the fence...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B8D")

    label("loc_1B89")

    Call(0, 5)

    label("loc_1B8D")

    TalkEnd(0xC)
    Return()

    # Function_4_1090 end

    def Function_5_1B91(): pass

    label("Function_5_1B91")

    OP_4A(0xC, 255)
    OP_4A(0xB, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xB)"), scpexpr(EXPR_END)), "loc_1C32")

    ChrTalk(    #74
        0xB,
        "Why, if it isn't Estelle!\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xC)
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #75
        0xC,
        "Did you say Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xC,
        "Oh, my, my, it is! It's been ages.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 400)
    Jump("loc_1CB4")

    label("loc_1C32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xC)"), scpexpr(EXPR_END)), "loc_1CB4")

    ChrTalk(    #77
        0xC,
        "Oh, if it isn't Estelle!\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xB)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #78
        0xB,
        (
            "My, it's been a while!\x01",
            "Things going well?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    label("loc_1CB4")


    ChrTalk(    #79
        0x101,
        "#1017FHeheh, it HAS been some time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xB,
        "Come from Rolent?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xB,
        (
            "I bet it was hard to see with that\x01",
            "fog on the highways.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #82
        0x101,
        (
            "#1015FActually, we're out here investigating\x01",
            "that fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xC,
        "Are you, now? Well, good luck with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xC,
        (
            "Really earning your keep as a bracer,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x103, 400)

    ChrTalk(    #85
        0xC,
        (
            "Perhaps that's due to your wonderful\x01",
            "mentor's guidance, hmm?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xC, 400)

    ChrTalk(    #86
        0x103,
        (
            "#021FIt's more thanks to her own efforts.\x02\x03",

            "I did oversee her training, but I hardly\x01",
            "taught her anything at all. She managed\x01",
            "to become the pistol she is all on her own.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #87
        0x101,
        (
            "#1008FThat's not true at all!\x02\x03",

            "You've always been there for me, Schera.\x01",
            "You taught me a lot of what I know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xB,
        (
            "Well, one way or another, it's an impressive\x01",
            "feat. You're doing your job like a real\x01",
            "professional. Like you were born for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xB,
        (
            "You keep on doing us proud out there, you\x01",
            "hear? Us hometown folks will cheer you on\x01",
            "the whole way!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #90
        0x101,
        "#1006FThanks! I won't let you down. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xC,
        (
            "Be sure you watch out for your health,\x01",
            "though! You're still a growing girl.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20C3():
        OP_8C(0xC, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_20C3)
    OP_8C(0xB, 180, 400)
    OP_4B(0xC, 255)
    OP_4B(0xB, 255)
    OP_A2(0x189F)
    Return()

    # Function_5_1B91 end

    def Function_6_20DE(): pass

    label("Function_6_20DE")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_247D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 6)), scpexpr(EXPR_END)), "loc_21B0")

    ChrTalk(    #92
        0xD,
        (
            "#1068FMan, why's it gotta be a forest?\x01",
            "The way things are now, this ain't\x01",
            "gonna be fun.\x02\x03",

            "It was easy enough to get lost\x01",
            "even without the fog...\x02\x03",

            "#1066FYou guys better be extra careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_247A")

    label("loc_21B0")


    ChrTalk(    #93
        0xD,
        (
            "#1060FHey, you guys!\x02\x03",

            "Finished your report to the guild, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1002FYeah. How's everyone doing?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #95
        0xD,
        (
            "#1060FDon't worry about 'em. They're just sleeping.\x02\x03",

            "Any progress on the investigation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x103,
        (
            "#022FWe can't be certain, but we've\x01",
            "pinpointed a location of interest.\x02\x03",

            "Won't be easy going, but we have to\x01",
            "at least check it out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#1015FIt's the large forest in the southeast,\x01",
            "Mistwald.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xD,
        (
            "#1065FMistwald, huh? Largest forested\x01",
            "region in all of Liberl, right?\x02\x03",

            "#1063FSounds like you already know what\x01",
            "you're in for, so there ain't much more\x01",
            "for me to say.\x02\x03",

            "Just be careful. Your line of sight's\x01",
            "the biggest issue, for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        "#1006FTake care of everyone here, Kevin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xD,
        "#1060FNo problem.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x189E)

    label("loc_247A")

    Jump("loc_25E7")

    label("loc_247D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_25E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2582")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2502")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #101
        0xD,
        (
            "#1060FAll part of the job description.\x02\x03",

            "Just leave this to me and head off\x01",
            "to the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257F")

    label("loc_2502")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #102
        0xD,
        (
            "#1064FWhat is it, Estelle?\x01",
            "Still haven't been to the guildhouse?\x02\x03",

            "#1060FYou just leave everything here to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_257F")

    Jump("loc_25E7")

    label("loc_2582")


    ChrTalk(    #103
        0xD,
        (
            "#1060FAll part of the job description.\x02\x03",

            "Just leave this to me and head off\x01",
            "to the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E7")

    TalkEnd(0xD)
    Return()

    # Function_6_20DE end

    def Function_7_25EB(): pass

    label("Function_7_25EB")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_28DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2710")
    OP_62(0xFE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x102, 0)
    Sleep(1000)

    ChrTalk(    #104
        0xFE,
        "Ah, Joshua! Are you here to play?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#1040FHey, Will. Good to see you!\x02\x03",

            "I'm afraid I can't play right now,\x01",
            "though. I'm still on the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "Aww, that's boring...\x01",
            "You can play a little! C'mon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x102,
        "#1049FHaha. Maybe later.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x20AD)
    Jump("loc_28DA")

    label("loc_2710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_286D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2756")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #108
        0xFE,
        "Joshua, come play again real soon, okay?\x02",
    )

    CloseMessageWindow()
    Jump("loc_286A")

    label("loc_2756")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2804")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #109
        0xFE,
        "Oh, Joshua! And Estelle, too!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "I'm helping Dad out with his work,\x01",
            "just like you guys!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "With the orbments all busted,\x01",
            "we all gotta pitch in.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_286A")

    label("loc_2804")


    ChrTalk(    #112
        0xFE,
        "I'm helping Dad out with his work too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "With the orbments all busted,\x01",
            "we all gotta pitch in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_286A")

    Jump("loc_28DA")

    label("loc_286D")

    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #114
        0xFE,
        (
            "Joshua, come play again real soon,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "And make sure you don't have any\x01",
            "work when you do!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28DA")

    TalkEnd(0xE)
    Return()

    # Function_7_25EB end

    def Function_8_28DE(): pass

    label("Function_8_28DE")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A75")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #116
        0xFE,
        "Oh... Joshua...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        "#1040FHey, Chere. Have you been well?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "Y-Yeah. I'm doing okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "I'm helping Mom right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "Lots of stuff isn't working,\x01",
            "so she's got it pretty rough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        "#1040FSounds like it. Sorry to hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "Umm, Joshua, are you workin'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        (
            "#1040FYeah, a bit...\x02\x03",

            "But I'll come play again soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "O-Okay! I can't wait to see you again.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    OP_A2(0x20AC)
    Jump("loc_2C5F")

    label("loc_2A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_2C07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2AD5")
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #125
        0xFE,
        "Joshua, come play again, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "I can't wait to see you again.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C04")

    label("loc_2AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BA2")

    ChrTalk(    #127
        0xFE,
        "Umm, Joshua...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        "Some soldiers came by the house last night.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "Me and Mom made some sandwiches.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "The soldiers were really happy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "I-I'll make one for you next time, okay?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2C04")

    label("loc_2BA2")


    ChrTalk(    #132
        0xFE,
        "The soldiers really liked the sandwich I made.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "I'll make one for you next time, Joshua.\x02",
    )

    CloseMessageWindow()

    label("loc_2C04")

    Jump("loc_2C5F")

    label("loc_2C07")

    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #134
        0xFE,
        "Joshua, come play again sometime, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "I can't wait to see you again.\x02",
    )

    CloseMessageWindow()

    label("loc_2C5F")

    TalkEnd(0xF)
    Return()

    # Function_8_28DE end

    def Function_9_2C63(): pass

    label("Function_9_2C63")

    EventBegin(0x0)
    SetChrPos(0x18, 400, 800, 27970, 0)
    SetChrPos(0x17, -910, 800, 27970, 0)
    SetChrPos(0x12, -1340, 800, 28000, 0)
    SetChrPos(0x13, -940, 800, 27500, 0)
    SetChrPos(0x14, 890, 800, 27500, 0)
    SetChrPos(0x15, -760, 800, 28500, 0)
    SetChrPos(0x16, 830, 800, 28500, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_4A(0xB, 255)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0x8, 255)
    OP_4A(0xC, 255)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrPos(0xB, -2170, 0, 28020, 90)
    SetChrPos(0xA, -960, 200, 26970, 0)
    SetChrPos(0x9, 940, 200, 27000, 0)
    SetChrPos(0x8, 1730, 0, 31540, 270)
    SetChrPos(0xC, 1220, 0, 36190, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrPos(0x101, -5790, 0, 24110, 90)
    SetChrPos(0x103, -5790, 0, 24110, 90)
    SetChrPos(0x107, -5790, 0, 24110, 90)
    SetChrPos(0x105, -5790, 0, 24110, 90)
    SetChrChipByIndex(0xB, 0)
    SetChrSubChip(0xB, 5)
    SetChrChipByIndex(0xA, 0)
    SetChrSubChip(0xA, 27)
    SetChrChipByIndex(0x9, 0)
    SetChrSubChip(0x9, 35)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x8, 16)
    SetChrChipByIndex(0xC, 0)
    SetChrSubChip(0xC, 9)
    OP_6D(-5540, 0, 24290, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    Sleep(500)

    def lambda_2EA0():
        OP_6D(-3970, 0, 25940, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2EA0)
    OP_43(0x101, 0x1, 0x0, 0xA)
    Sleep(500)
    OP_43(0x103, 0x1, 0x0, 0xB)
    Sleep(500)
    OP_43(0x105, 0x1, 0x0, 0xD)
    Sleep(500)
    OP_43(0x107, 0x1, 0x0, 0xC)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #136
        0x101,
        "#1020F#6PNo...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x107, 0x1)

    def lambda_2F06():
        OP_6D(-2470, 0, 27900, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F06)

    def lambda_2F1E():
        OP_8E(0xFE, 0xFFFFF808, 0x0, 0x68BA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F1E)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #137
        0x101,
        "#1020F#6PMr. Perzel?!\x02",
    )

    CloseMessageWindow()

    def lambda_2F5E():
        OP_8C(0xFE, 100, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F5E)
    Sleep(500)

    ChrTalk(    #138
        0x101,
        "#1020F#6PChere! Will!\x02",
    )

    CloseMessageWindow()
    OP_43(0x103, 0x1, 0x0, 0xE)
    OP_43(0x107, 0x1, 0x0, 0x10)
    OP_43(0x105, 0x1, 0x0, 0xF)

    def lambda_2FA1():
        OP_6D(-40, 0, 31820, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2FA1)
    OP_8E(0x101, 0xFFFFF380, 0x0, 0x69E6, 0x1388, 0x0)
    OP_8E(0x101, 0xFFFFF3EE, 0x0, 0x749A, 0x1388, 0x0)
    OP_8E(0x101, 0xFFFFF772, 0x0, 0x79B8, 0x1388, 0x0)
    OP_8E(0x101, 0xFFFFFFBA, 0x0, 0x7DAA, 0x1388, 0x0)
    OP_8C(0x101, 90, 600)
    Sleep(500)
    OP_8C(0x101, 0, 600)
    Sleep(500)
    OP_8C(0x101, 90, 600)
    Sleep(500)

    ChrTalk(    #139
        0x101,
        (
            "#1020F#6PMrs. Perzel! TIO!\x02\x03",

            "#1027FNo... Nooooo...\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD1, 0x0, 0x50)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 4)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(1500)

    ChrTalk(    #140
        0x105,
        (
            "#049F#5PI'm sorry, Estelle...\x01",
            "They're all asleep.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)
    Sleep(500)

    ChrTalk(    #141
        0x107,
        "#561F#5PThe ones over here are, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1003FNooo...\x02\x03",

            "#1027FWe...failed again...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x105,
        "#043F#5PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x107,
        "#063FI'm sorry...\x02",
    )

    CloseMessageWindow()
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    ClearChrFlags(0x103, 0x80)

    def lambda_315F():
        OP_6D(320, 0, 28710, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_315F)

    def lambda_3177():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3177)
    OP_8E(0x103, 0x410, 0x0, 0x5F5A, 0x9C4, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(200)

    ChrTalk(    #145
        0x103,
        (
            "#522F#5PDamn it all.\x02\x03",

            "It looks like whoever is doing\x01",
            "this knew what we were planning.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3202():

        label("loc_3202")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_3202")

    QueueWorkItem2(0x105, 1, lambda_3202)
    Sleep(100)

    def lambda_3218():

        label("loc_3218")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_3218")

    QueueWorkItem2(0x107, 1, lambda_3218)
    Sleep(400)

    ChrTalk(    #146
        0x105,
        "#042F#6PThat woman in black?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x103,
        "#022F#5PThere's no doubt in my mind.\x02",
    )

    CloseMessageWindow()

    def lambda_327A():
        OP_6D(-40, 0, 31820, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_327A)
    OP_8E(0x103, 0xEEC, 0x0, 0x61A8, 0xBB8, 0x0)
    OP_8E(0x103, 0xEEC, 0x0, 0x7896, 0xBB8, 0x0)
    TurnDirection(0x103, 0x101, 400)
    OP_44(0x105, 0x1)
    OP_44(0x107, 0x1)
    OP_8C(0x105, 0, 400)
    OP_8C(0x107, 0, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #148
        0x103,
        (
            "#022F#2PEstelle, let's carry them to bed.\x02\x03",

            "Can you show us where their\x01",
            "rooms are?\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x101, 0x0, 0x7, 0x3E8)
    Sleep(500)

    ChrTalk(    #149
        0x101,
        "#1027F#6PAh, yeah...\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    Call(0, 17)
    Return()

    # Function_9_2C63 end

    def Function_10_336F(): pass

    label("Function_10_336F")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3385():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3385)
    OP_8E(0xFE, 0xFFFFEF8E, 0x0, 0x5E10, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFF722, 0x0, 0x63D8, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_336F end

    def Function_11_33C1(): pass

    label("Function_11_33C1")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_33D7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_33D7)
    OP_8E(0xFE, 0xFFFFEF8E, 0x0, 0x5E10, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFFA92, 0x0, 0x5E4C, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_11_33C1 end

    def Function_12_3413(): pass

    label("Function_12_3413")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_3429():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3429)
    OP_8E(0xFE, 0xFFFFEF8E, 0x0, 0x5E10, 0x9C4, 0x0)
    OP_72(0x0, 0x800)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFF466, 0x0, 0x61BC, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_71(0x0, 0x800)
    Return()

    # Function_12_3413 end

    def Function_13_3485(): pass

    label("Function_13_3485")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_349B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_349B)
    OP_8E(0xFE, 0xFFFFEF8E, 0x0, 0x5E10, 0x9C4, 0x0)
    OP_8E(0xFE, 0xFFFFF68C, 0x0, 0x5CE4, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_3485 end

    def Function_14_34D7(): pass

    label("Function_14_34D7")

    Sleep(1000)
    OP_8C(0xFE, 130, 400)
    OP_8E(0xFE, 0x41A, 0x0, 0x564A, 0xBB8, 0x0)
    OP_8C(0xFE, 220, 400)
    Sleep(500)
    OP_8C(0xFE, 130, 400)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_8E(0xFE, 0x3AC, 0x0, 0x4D30, 0xBB8, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0x103, 0x80)
    Return()

    # Function_14_34D7 end

    def Function_15_353E(): pass

    label("Function_15_353E")

    Sleep(2000)
    OP_8E(0xFE, 0xFFFFF7D6, 0x0, 0x6A2C, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_353E end

    def Function_16_355F(): pass

    label("Function_16_355F")

    Sleep(1500)
    OP_8E(0xFE, 0xFFFFFFB0, 0x0, 0x64F0, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF92, 0x0, 0x68A6, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_16_355F end

    def Function_17_35A7(): pass

    label("Function_17_35A7")

    SetChrPos(0xB, -76340, 0, 31640, 180)
    SetChrPos(0xC, -73490, 0, 31660, 180)
    SetChrPos(0x8, -77060, 0, 3150, 180)
    SetChrPos(0xA, -73600, 0, 2980, 180)
    SetChrPos(0x9, -72950, 0, 2980, 180)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, -75750, 0, 2700, 270)
    SetChrPos(0x103, -74780, 0, 2600, 90)
    SetChrPos(0x105, -75080, 0, 31410, 270)
    SetChrPos(0x107, -74700, 0, 32159, 90)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0xC, 0x4)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xB, 1)
    SetChrSubChip(0xB, 7)
    SetChrChipByIndex(0xA, 1)
    SetChrSubChip(0xA, 55)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 71)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 39)
    SetChrChipByIndex(0xC, 1)
    SetChrSubChip(0xC, 23)
    OP_6F(0x5, 60)
    OP_6F(0x6, 60)
    OP_6F(0x7, 60)
    OP_6F(0x8, 60)
    OP_6D(-75020, 0, 33060, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_1D(0x53)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1500)
    Fade(1000)
    OP_6D(-76380, 0, 4030, 0)
    OP_67(0, 4730, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #150
        0x103,
        (
            "#025F#6PRight, they're in bed, at least.\x02\x03",

            "#522FI wish I had some idea what\x01",
            "to do now, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        "#1027F#6P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x103, 0x101, 500)
    Sleep(500)

    ChrTalk(    #152
        0x103,
        (
            "#022F#4PEstelle.\x02\x03",

            "I know this is a shock,\x01",
            "but you MUST put it aside.\x02\x03",

            "If you can't, you won't be\x01",
            "able to help them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        (
            "#1027F#6PBut...it's all because I'm no\x01",
            "good at this...\x02\x03",

            "I'm not even half the bracer my\x01",
            "father is...\x02\x03",

            "I've put everyone in so much\x01",
            "danger because I'm useless...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x103,
        "#023F#4P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 600)
    Sleep(500)

    ChrTalk(    #155
        0x101,
        (
            "#1023F#6PDamn it... Damn it!\x01",
            "I've acted all strong and confident...\x02\x03",

            "But... But it's all just an act!\x02\x03",

            "How am I supposed to fix something\x01",
            "like this?!\x02\x03",

            "#1027FI... I...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x103,
        (
            "#522F#4P...\x02\x03",

            "#026FEstelle.\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)

    def lambda_3A26():
        OP_6B(2900, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3A26)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 5)
    OP_0D()

    def lambda_3A46():
        OP_99(0xFE, 0x0, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3A46)
    Sleep(300)
    OP_22(0xA5, 0x0, 0x64)
    WaitChrThread(0x103, 0x1)
    Sleep(500)
    OP_99(0x103, 0x8, 0xE, 0x5DC)
    Sleep(500)

    ChrTalk(    #157
        0x101,
        "#1026F#6PHuh...?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x107, -67520, 0, -1240, 270)
    SetChrPos(0x105, -67520, 0, -1240, 270)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #158
        0x105,
        "#5PAh, Scherazard?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x107,
        "#1PEstelle!\x02",
    )

    CloseMessageWindow()
    OP_43(0x107, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0x105, 0x1, 0x0, 0x13)
    Sleep(1000)

    ChrTalk(    #160
        0x103,
        (
            "#022F#4PWe're all a pack of fools,\x01",
            "Estelle.\x02\x03",

            "I make mistakes constantly\x01",
            "myself, but that doesn't mean\x01",
            "I'm going to give up.\x02\x03",

            "Agate, Zin...and yes, even\x01",
            "Cassius.\x02\x03",

            "We all do what we can, even\x01",
            "as we're painfully aware of our\x01",
            "own shortcomings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1026F#6PEven...Dad...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x103,
        (
            "#522F#4PI wonder...do you remember?\x02\x03",

            "How Cassius didn't make it in\x01",
            "time when...when your mother\x01",
            "died.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        "#1026F#6PAh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x103,
        (
            "#022F#4PHe's never forgiven himself for that,\x01",
            "but he still overcame it to walk the\x01",
            "path of a bracer.\x02\x03",

            "He never stopped moving forward and\x01",
            "always did what he could to protect the\x01",
            "people most important to him.\x02\x03",

            "Even in the army, he's still striding\x01",
            "forward, day by day, even if he's\x01",
            "uncertain.\x02\x03",

            "#026FSo, Estelle, what will you do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x101,
        "#1003F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x103,
        (
            "#022F#4PYou don't need to overthink it.\x02\x03",

            "Just go with what your feelings\x01",
            "deep inside tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#1003F#6P...\x02\x03",

            "I don't...really have an answer,\x01",
            "but...\x02\x03",

            "#1026FI want to keep moving forward.\x02\x03",

            "To protect the people important\x01",
            "to me...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #168
        0x101,
        (
            "#1005F#6PEven if I'm an idiot right\x01",
            "now, I can't stop just because\x01",
            "I screwed up!\x02",
        )
    )

    OP_7C(0x0, 0x32, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #169
        0x103,
        "#524F#4PHeh... That's my Estelle.\x02",
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x103, 0x2)
    SetChrChipByIndex(0x103, 65535)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #170
        0x101,
        (
            "#1025F#6PSorry, Schera.\x02\x03",

            "Guess I'm just an annoying\x01",
            "little sister, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x103,
        (
            "#027F#4PDon't worry, honey.\x02\x03",

            "Besides, the bigger a pain the\x01",
            "kid is, the cuter they are when\x01",
            "they're all grown up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        "#1015F#6PEr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x107,
        "#061FHeehee!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x105,
        "#041F#5PHaha...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #175
        0x101,
        (
            "#1008F#4POh! Uh, sorry, you two.\x02\x03",

            "I didn't mean to make a big scene\x01",
            "or anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x107,
        (
            "#560FUm, I was a bit surprised, but...\x02\x03",

            "I never realized how close you\x01",
            "and Schera are, Estelle!\x02\x03",

            "#067FHaha! I'm kinda jealous, now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x105,
        (
            "#048F#5PIt was inspiring to watch,\x01",
            "actually.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        "#1013F#4PAww, hey...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #179
        0x101,
        (
            "#1015F#6PBut, Schera, really, what do we do?\x02\x03",

            "We need to get back to the\x01",
            "guildhouse, but...I can't just leave\x01",
            "Tio and everyone like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x103,
        (
            "#522F#4PIt IS a problem...\x02\x03",

            "One of us is going to have to\x01",
            "stay here, but--\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xD, -68520, 0, -1240, 270)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    NpcTalk(    #181
        0xD,
        "Man's Voice",
        "#1PNo worries, I got that covered!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_437C():

        label("loc_437C")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_437C")

    QueueWorkItem2(0x101, 1, lambda_437C)

    def lambda_438D():

        label("loc_438D")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_438D")

    QueueWorkItem2(0x103, 1, lambda_438D)

    def lambda_439E():

        label("loc_439E")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_439E")

    QueueWorkItem2(0x105, 1, lambda_439E)

    def lambda_43AF():

        label("loc_43AF")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_43AF")

    QueueWorkItem2(0x107, 1, lambda_43AF)

    def lambda_43C0():
        OP_6D(-75100, 0, 2370, 1800)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_43C0)
    OP_4A(0xD, 255)
    ClearChrFlags(0xD, 0x80)

    def lambda_43E1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_43E1)
    OP_8E(0xD, 0xFFFEEE90, 0x0, 0xFFFFFBF0, 0x9C4, 0x0)
    OP_8E(0xD, 0xFFFEE526, 0x0, 0xB4, 0x9C4, 0x0)
    TurnDirection(0xD, 0x101, 400)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x107, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #182
        0x105,
        "#044F#5PAh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x107,
        "#064F#3PWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x103,
        "#023FIs that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xD,
        (
            "#1062F#5PHello, laaadies! It's Kevin!\x01",
            "Remember, priest, Gralsritter,\x01",
            "mad heroism?\x02\x03",

            "Man, we JUST met in Grancel.\x01",
            "Wasn't expecting to see you again.\x02\x03",

            "#1061FHand of Aidios at work, I tell ya!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1020F#6PWh-Wh-Wh...\x02\x03",

            "What are YOU doing here, Kevin?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0xD,
        (
            "#1066F#5PAh, well, it's pretty simple.\x02\x03",

            "Last night we got a panicked report\x01",
            "about fog, illness, and possibly the end\x01",
            "of the world from Father Divine.\x02\x03",

            "#1065FSo, in my capacity as one of the\x01",
            "Gralsritter, I decided to pop on over\x01",
            "and see what was what.\x02\x03",

            "Wasn't quite expecting to have to hack\x01",
            "my way through monster-infested, foggy\x01",
            "roads. I only got here late this morning.\x02\x03",

            "#1062FWhen I checked in at the local Bracer\x01",
            "Guild, I heard Estelle's team was over\x01",
            "here workin', so--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#1007F#6POkay, okay, I think I get the idea.\x02\x03",

            "#1019FMeaning the 'hand of Aidios'\x01",
            "wasn't involved at all and you're\x01",
            "being a creepy stalker again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0xD,
        (
            "#1066F#5PHaha... Nooo, no, what gave\x01",
            "you that idea...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x103,
        (
            "#020FPutting that aside, what do you\x01",
            "mean when you say, 'no worries'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xD,
        (
            "#1060F#5POh, right. Well, I did overhear\x01",
            "you guys talkin' about staying\x01",
            "behind.\x02\x03",

            "You all go back. I got this covered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        "#1004F#6PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x105,
        "#542F#5PAre you sure, Father?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xD,
        (
            "#1071FHey, this sort of thing is part\x01",
            "of a priest's job.\x02\x03",

            "I do have some medical training,\x01",
            "so leave your friends to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x107,
        "#560F#3PThank you, Father Graham!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x103,
        (
            "#021FI'm definitely willing to\x01",
            "chalk this one in the 'divine providence'\x01",
            "column at this point.\x02\x03",

            "#020FAll right, let's get back to Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x101,
        (
            "#1025F#6POkay!\x02\x03",

            "Kevin, please take care of everyone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xD,
        "#1060F#5PLeave it to me!\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_6D(-73890, 0, 410, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x107, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrPos(0x0, -73890, 0, 410, 90)
    SetChrPos(0x1, -73890, 0, 410, 90)
    SetChrPos(0x2, -73890, 0, 410, 90)
    SetChrPos(0x3, -73890, 0, 410, 90)
    OP_69(0x0, 0x0)
    SetChrPos(0xD, -75610, 0, 2580, 270)
    OP_4B(0xD, 255)
    OP_A2(0x1822)
    OP_A2(0x0)
    OP_28(0x91, 0x1, 0x8)
    OP_28(0x91, 0x1, 0x10)
    OP_28(0x91, 0x1, 0x20)
    Sleep(500)
    OP_21()
    OP_1D(0xF)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_35A7 end

    def Function_18_4B94(): pass

    label("Function_18_4B94")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4BA5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BA5)
    OP_8E(0xFE, 0xFFFED9DC, 0x0, 0x262, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_4B94 end

    def Function_19_4BCD(): pass

    label("Function_19_4BCD")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4BDE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BDE)
    OP_8E(0xFE, 0xFFFEDFC2, 0x0, 0xDC, 0xFA0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_19_4BCD end

    def Function_20_4C06(): pass

    label("Function_20_4C06")

    EventBegin(0x0)
    OP_DB()
    OP_4A(0xD, 255)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0xD, -74400, 0, 300, 315)
    SetChrPos(0xB, -75940, 0, 930, 135)
    SetChrPos(0xC, -75950, 0, 180, 135)
    SetChrPos(0xA, -75640, 0, 1920, 135)
    SetChrPos(0x9, -74730, 0, 2000, 135)
    SetChrPos(0x8, -75270, 0, 2740, 135)
    SetChrChipByIndex(0xB, 9)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xA, 8)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0x9, 7)
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x8, 6)
    SetChrSubChip(0x8, 0)
    SetChrChipByIndex(0xC, 10)
    SetChrSubChip(0xC, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_6D(-72650, 0, 450, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)

    def lambda_4D1A():
        OP_6D(-75540, 0, 1480, 3000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4D1A)
    FadeToBright(2000, 0)
    OP_62(0xD, 0x0, 2100, 0x26, 0x27, 0xFA, 0x0)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_8C(0xD, 270, 400)
    Sleep(200)
    OP_62(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_8C(0xD, 0, 400)
    Sleep(1000)
    OP_62(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_43(0x9, 0x1, 0x0, 0x15)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_63(0xD)
    OP_DC()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_20_4C06 end

    def Function_21_4DC7(): pass

    label("Function_21_4DC7")

    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)
    OP_95(0xA, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(1000)
    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(500)
    OP_95(0xA, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_8C(0xD, 270, 400)
    Return()

    # Function_21_4DC7 end

    SaveToFile()

Try(main)
