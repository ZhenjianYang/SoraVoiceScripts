from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2512   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2512.x',
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Logic',                                # 9
        'Hans',                                 # 10
        'Lucy',                                 # 11
        'Ms. Millia',                           # 12
        'Mr. Effort',                           # 13
        'Thelma',                               # 14
        'Dennis',                               # 15
        'Alice',                                # 16
        'Mickey',                               # 17
        'Target Camera',                        # 18
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
        'ED6_DT07/CH01080 ._CH',             # 00
        'ED6_DT07/CH02550 ._CH',             # 01
        'ED6_DT07/CH02690 ._CH',             # 02
        'ED6_DT07/CH01430 ._CH',             # 03
        'ED6_DT07/CH01460 ._CH',             # 04
        'ED6_DT07/CH01090 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01590 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01080P._CP',             # 00
        'ED6_DT07/CH02550P._CP',             # 01
        'ED6_DT07/CH02690P._CP',             # 02
        'ED6_DT07/CH01430P._CP',             # 03
        'ED6_DT07/CH01460P._CP',             # 04
        'ED6_DT07/CH01090P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01590P._CP',             # 07
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -120030,
        Z                   = 0,
        Y                   = 30750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 29010,
        Z                   = 0,
        Y                   = 28300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -61790,
        Z                   = 0,
        Y                   = -1780,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -29380,
        Z                   = 0,
        Y                   = 880,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -60240,
        Z                   = 0,
        Y                   = 24290,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 5,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -29120,
        Z                   = 0,
        Y                   = 24590,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 6,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_22A",          # 00, 0
        "Function_1_303",          # 01, 1
        "Function_2_30D",          # 02, 2
        "Function_3_48A",          # 03, 3
        "Function_4_4AE",          # 04, 4
        "Function_5_4D2",          # 05, 5
        "Function_6_4F6",          # 06, 6
        "Function_7_51A",          # 07, 7
        "Function_8_741",          # 08, 8
        "Function_9_A96",          # 09, 9
        "Function_10_D03",         # 0A, 10
        "Function_11_F6A",         # 0B, 11
        "Function_12_1165",        # 0C, 12
        "Function_13_139C",        # 0D, 13
        "Function_14_14B8",        # 0E, 14
        "Function_15_15C4",        # 0F, 15
        "Function_16_1746",        # 10, 16
        "Function_17_1C59",        # 11, 17
        "Function_18_20F5",        # 12, 18
    )


    def Function_0_22A(): pass

    label("Function_0_22A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_27B")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 1620, 0, -4100, 90)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -720, 0, -4100, 270)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_2D2")

    label("loc_27B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_28A")
    ClearChrFlags(0x13, 0x80)
    Jump("loc_2D2")

    label("loc_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_29E")
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_2D2")

    label("loc_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_2D2")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 1480, 0, -2400, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8")
    SetChrFlags(0x10, 0x10)

    label("loc_2C8")

    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)

    label("loc_2D2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_302")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_302")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_302")
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_302")

    Return()

    # Function_0_22A end

    def Function_1_303(): pass

    label("Function_1_303")

    OP_B1("t2512_n")
    Return()

    # Function_1_303 end

    def Function_2_30D(): pass

    label("Function_2_30D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_474")

    label("loc_332")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_474")

    label("loc_34B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_364")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_474")

    label("loc_364")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37D")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_474")

    label("loc_37D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_396")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_474")

    label("loc_396")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_474")

    label("loc_3AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C8")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_474")

    label("loc_3C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E1")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_474")

    label("loc_3E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FA")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_474")

    label("loc_3FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_413")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_474")

    label("loc_413")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42C")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_474")

    label("loc_42C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_445")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_474")

    label("loc_445")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45E")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_474")

    label("loc_45E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_474")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_474")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_489")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_474")

    label("loc_489")

    Return()

    # Function_2_30D end

    def Function_3_48A(): pass

    label("Function_3_48A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AD")
    OP_8D(0xFE, -1040, -3130, -430, -5120, 2000)
    Jump("Function_3_48A")

    label("loc_4AD")

    Return()

    # Function_3_48A end

    def Function_4_4AE(): pass

    label("Function_4_4AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D1")
    OP_8D(0xFE, 1840, -4950, 1050, -3130, 2000)
    Jump("Function_4_4AE")

    label("loc_4D1")

    Return()

    # Function_4_4AE end

    def Function_5_4D2(): pass

    label("Function_5_4D2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F5")
    OP_8D(0xFE, -59450, 25230, -61220, 23390, 2000)
    Jump("Function_5_4D2")

    label("loc_4F5")

    Return()

    # Function_5_4D2 end

    def Function_6_4F6(): pass

    label("Function_6_4F6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_519")
    OP_8D(0xFE, -30480, 23230, -28100, 25610, 1500)
    Jump("Function_6_4F6")

    label("loc_519")

    Return()

    # Function_6_4F6 end

    def Function_7_51A(): pass

    label("Function_7_51A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_73D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 0)), scpexpr(EXPR_END)), "loc_739")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5D0")

    ChrTalk(    #0
        0xFE,
        (
            "The upcoming examinations will be vital to our\x01",
            "futures, and I have no intention of being bested\x01",
            "by anyone in them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "I hope you feel the same way!\x02",
    )

    CloseMessageWindow()
    Jump("loc_736")

    label("loc_5D0")


    ChrTalk(    #2
        0xFE,
        (
            "A kind senior student has agreed to lend me some\x01",
            "reference books to aid me in my studies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "He's in the process of choosing some fitting ones\x01",
            "for me this very moment, I believe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I have no intention of not delivering to my full\x01",
            "potential during the examinations, and I hope\x01",
            "you feel the same way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Make sure you study thoroughly for them!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_736")

    Jump("loc_73D")

    label("loc_739")

    Call(0, 16)

    label("loc_73D")

    TalkEnd(0xFE)
    Return()

    # Function_7_51A end

    def Function_8_741(): pass

    label("Function_8_741")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_74E")
    Jump("loc_A92")

    label("loc_74E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_758")
    Jump("loc_A92")

    label("loc_758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_762")
    Jump("loc_A92")

    label("loc_762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_903")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_840")

    ChrTalk(    #6
        0xFE,
        (
            "If you want to score well on an examination,\x01",
            "it's never too early to start studying. That's\x01",
            "key to doing well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I should probably start by making some summaries\x01",
            "first. Those will be very helpful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_900")

    label("loc_840")


    ChrTalk(    #8
        0xFE,
        (
            "Haha. It's almost time for the examinations to\x01",
            "begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I should probably start seriously studying for\x01",
            "them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "If you want to score well, it's never too early\x01",
            "to start studying.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_900")

    Jump("loc_A92")

    label("loc_903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_A92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_996")
    OP_8C(0xFE, 0, 0)

    ChrTalk(    #11
        0xFE,
        "Hmm... Whiiich should I go with...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "This one? No, this one might be a little too \x01",
            "difficult for him right now...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A92")

    label("loc_996")


    ChrTalk(    #13
        0xFE,
        (
            "Logic asked if he could borrow some of my \x01",
            "reference books, so I'm in the process of\x01",
            "choosing ones to give him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "He really is alarmingly dedicated to his studies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Haha. That's no bad thing, though. On the\x01",
            "contrary, I think it's great.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_A92")

    TalkEnd(0xFE)
    Return()

    # Function_8_741 end

    def Function_9_A96(): pass

    label("Function_9_A96")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_CDA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EF, 4)), scpexpr(EXPR_END)), "loc_BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_B27")

    ChrTalk(    #16
        0x11,
        (
            "#730FLucy and I are going to stay here and search\x01",
            "for a while longer.\x02\x03",

            "Maybe you should go and check up on Jill?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF3")

    label("loc_B27")


    ChrTalk(    #17
        0x11,
        (
            "#730FLechter's not here...\x02\x03",

            "#736F...Then again, what if he is and just wants us to\x01",
            "THINK he's not here so that we'll mosey our way\x01",
            "elsewhere?\x02\x03",

            "#734FUgh. This is why he's such a pain to deal with!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_BF3")

    Jump("loc_CD7")

    label("loc_BF6")


    ChrTalk(    #18
        0x11,
        (
            "#733FOh. 'Sup, Kloe?\x02\x03",

            "#732F...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x105,
        "#044FUmm... Is something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#735FOh, no. It's nothing.\x02\x03",

            "#730FIt looks like Lechter isn't here.\x02\x03",

            "Maybe you should go and see what Jill is up to?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F7C)

    label("loc_CD7")

    Jump("loc_CFF")

    label("loc_CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_CE4")
    Jump("loc_CFF")

    label("loc_CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_CEE")
    Jump("loc_CFF")

    label("loc_CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_CF8")
    Jump("loc_CFF")

    label("loc_CF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_CFF")

    label("loc_CFF")

    TalkEnd(0xFE)
    Return()

    # Function_9_A96 end

    def Function_10_D03(): pass

    label("Function_10_D03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_E05")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D8F")

    ChrTalk(    #21
        0xFE,
        (
            "We've still got lessons for a while longer,\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I kind of feel like I'm the only one excited\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E02")

    label("loc_D8F")


    ChrTalk(    #23
        0xFE,
        "It's almost time for the holidays! Yaaay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "I'd better start thinking about how I should\x01",
            "spend them. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_E02")

    Jump("loc_F66")

    label("loc_E05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 6)), scpexpr(EXPR_END)), "loc_E0F")
    Jump("loc_F66")

    label("loc_E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_E19")
    Jump("loc_F66")

    label("loc_E19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_E23")
    Jump("loc_F66")

    label("loc_E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5EC, 5)), scpexpr(EXPR_END)), "loc_F66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E97")

    ChrTalk(    #25
        0xFE,
        "Lucy sure is gorgeous, isn't she?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I wish I had hair as soft and silky looking\x01",
            "as hers...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F66")

    label("loc_E97")


    ChrTalk(    #27
        0xFE,
        "Lucy sure is gorgeous, isn't she?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "She's here as an exchange student from the\x01",
            "Principality of Remiferia to the north. I wonder \x01",
            "if all the girls there are as pretty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "I sure wish I was... ㈱\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_F66")

    TalkEnd(0xFE)
    Return()

    # Function_10_D03 end

    def Function_11_F6A(): pass

    label("Function_11_F6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 4)), scpexpr(EXPR_END)), "loc_1161")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1012")

    ChrTalk(    #30
        0xFE,
        "...I'm not here being lazy, for the record.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I'm just way too angry to be grading papers right\x01",
            "now, so I came here to cool off. Uuuuuurgh!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1161")

    label("loc_1012")


    ChrTalk(    #32
        0xFE,
        (
            "I was in the faculty lounge grading papers until not\x01",
            "long ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "...but then that damned Lechter just showed up\x01",
            "out of nowhere!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "He's all, like, 'Hey, Millia! What'cha doing?'\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "'Oh, grading papers already, huh? Must suck\x01",
            "being a teacher! ☆'\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0xFE,
        "It sucks when YOU'RE THERE JUDGING ME!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1161")

    TalkEnd(0xFE)
    Return()

    # Function_11_F6A end

    def Function_12_1165(): pass

    label("Function_12_1165")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_1398")
    OP_8C(0xFE, 270, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1257")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x05Mr. Effort has both of his eyes closed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_11E4():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_11E4)

    ChrTalk(    #38
        0xFE,
        "Y-You monster!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "Noooooo!\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #40
        0x105,
        "#047F(Just what did Lechter say to him...?)\x02",
    )

    CloseMessageWindow()
    OP_44(0xFE, 0x3)
    Jump("loc_1398")

    label("loc_1257")

    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_128B():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_128B)

    ChrTalk(    #41
        0xFE,
        "N-No, Lechter! That's not me! I swear!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x105,
        "#044FU-Umm...\x02",
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x105, 400)
    Sleep(300)

    ChrTalk(    #43
        0xFE,
        "O-Oh, it's you... Don't scare me like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "I thought you were him...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x105,
        (
            "#045F(Here we have another of Lechter's victims,\x01",
            "I see...)\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xFE, 0x3)
    OP_A2(0x5)

    label("loc_1398")

    TalkEnd(0xFE)
    Return()

    # Function_12_1165 end

    def Function_13_139C(): pass

    label("Function_13_139C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_14B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1440")

    ChrTalk(    #46
        0xFE,
        (
            "At first, my parents were dead set against\x01",
            "me coming here, but I'm so glad I was able\x01",
            "to in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "Studying is so much FUN. Heehee.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14B4")

    label("loc_1440")


    ChrTalk(    #48
        0xFE,
        (
            "I should probably start doing some prep work\x01",
            "for tomorrow's classes now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "Heehee. Studying is such FUN.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_14B4")

    TalkEnd(0xFE)
    Return()

    # Function_13_139C end

    def Function_14_14B8(): pass

    label("Function_14_14B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 7)), scpexpr(EXPR_END)), "loc_15C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1526")

    ChrTalk(    #50
        0x12,
        (
            "#1793F...There's no sign of him anywhere.\x02\x03",

            "What should I even do when I find him...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C0")

    label("loc_1526")


    ChrTalk(    #51
        0x12,
        (
            "#1790F...? Hi there, Kloe.\x02\x03",

            "#1790FHave you found any sign of Lechter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        "#045FI wish I could say yes, but unfortunately not...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x12,
        "#1795FOh...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_15C0")

    TalkEnd(0xFE)
    Return()

    # Function_14_14B8 end

    def Function_15_15C4(): pass

    label("Function_15_15C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5ED, 3)), scpexpr(EXPR_END)), "loc_1742")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1676")

    ChrTalk(    #54
        0xFE,
        (
            "Ugh... Why does he have to hang out in front\x01",
            "of the dorm, anyway?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "I hope he's not waiting for me because\x01",
            "he knows I skipped class that one time...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1742")

    label("loc_1676")


    ChrTalk(    #56
        0xFE,
        (
            "I'm starving, so I wanna head over to the\x01",
            "cafeteria and get some grub...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "...but Mr. Effort's hanging around outside\x01",
            "the dorm, so I'm stuck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "I'll be in trouble if he finds me... Waaah...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_1742")

    TalkEnd(0xFE)
    Return()

    # Function_15_15C4 end

    def Function_16_1746(): pass

    label("Function_16_1746")

    EventBegin(0x0)
    OP_C4(0x0, 0x20000000)
    Fade(1000)
    OP_6D(700, 0, -2400, 0)
    OP_67(0, 5720, -10000, 0)
    OP_6B(3100, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x105, 1480, 0, -3900, 0)
    SetChrSubChip(0x10, 0)
    Sleep(1000)
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x10, 0x105, 400)
    Sleep(300)

    ChrTalk(    #59
        0x10,
        "#11PHmm... I know you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "#11PKloe Rinz, wasn't it? Do you have some business\x01",
            "with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x105,
        (
            "#045F#6PWell, not personally, no...\x02\x03",

            "#542FI've been entrusted with the task of giving\x01",
            "a printout to you by Ms. Wiola.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #62
        "\x07\x05Kloe handed Logic a printout.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #63
        0x10,
        "#11POh, this is a list of this year's credits.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10, 0, 500)
    Sleep(100)

    ChrTalk(    #64
        0x10,
        "#5PWh-What?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#5PJoint classes seem to be worth an awful lot while\x01",
            "we're first years...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        (
            "#5PWait. Physical education is worth\x01",
            "FIVE WHOLE CREDITS?!\x02\x03",

            "Aidios, help me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x105,
        (
            "#542F#6P(Erm...)\x02\x03",

            "(I suppose I should probably leave him\x01",
            "alone for a while...)\x02\x03",

            "#045FWell, if you'll excuse me...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 180, 600)

    def lambda_1A7F():
        OP_8E(0xFE, 0x5C8, 0x0, 0xFFFFEA84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1A7F)
    Sleep(100)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_8C(0x10, 180, 600)

    ChrTalk(    #68
        0x10,
        "#11PW-Wait a moment!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0x1)

    ChrTalk(    #69
        0x105,
        "#044F#6P...Y-Yes?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x105, 0, 400)
    Sleep(300)

    ChrTalk(    #70
        0x10,
        "#11POh, no.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10,
        (
            "#11PIt's just that according to this printout,\x01",
            "our examinations will be taking place in\x01",
            "six weeks' time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        "#11PMake sure you study thoroughly for them!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        (
            "#11PI don't want to hear any excuses\x01",
            "if you don't strive for the top!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x105,
        (
            "#044F#6PA-Absolutely.\x02\x03",

            "#543FI'll devote myself fully to my studies.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F68)
    OP_8C(0x10, 0, 400)
    ClearChrFlags(0x10, 0x10)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Return()

    # Function_16_1746 end

    def Function_17_1C59(): pass

    label("Function_17_1C59")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    OP_6D(-840, 0, -2820, 0)
    OP_67(0, 4920, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_4A(0x11, 255)
    OP_4A(0x12, 255)
    SetChrPos(0x11, 1620, 0, -4100, 90)
    SetChrPos(0x12, -720, 0, -4100, 270)
    SetChrFlags(0x105, 0x8)

    def lambda_1CEC():
        OP_6B(3100, 6000)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_1CEC)
    FadeToBright(1000, 0)
    OP_43(0x12, 0x3, 0x0, 0x12)
    Sleep(200)
    OP_8C(0x11, 45, 500)
    Sleep(800)
    OP_8C(0x11, 135, 500)
    Sleep(800)
    OP_8C(0x11, 45, 500)
    Sleep(800)
    OP_8C(0x11, 90, 500)
    Sleep(1000)
    OP_62(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x11)
    Sleep(500)

    ChrTalk(    #75
        0x11,
        (
            "#737F#5P(I'm all alone with Lucy... This is like a dream\x01",
            "come true...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x11, 0x12, 400)
    Sleep(300)

    ChrTalk(    #76
        0x11,
        "#738F#12POh, Luuuuuucy...\x02",
    )

    CloseMessageWindow()
    OP_44(0x12, 0x3)
    OP_62(0x12, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x12, 0x11, 400)
    Sleep(300)

    ChrTalk(    #77
        0x12,
        "#1790F#5PWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        (
            "#739F#12PHeheh... I just wanted to ask you something.\x02\x03",

            "#738FWhat do you think the most important thing\x01",
            "in the world is?\x02\x03",

            "It's #200WL O V E#120W..#20W. Right? ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x12,
        (
            "#1794F#5PHmm...\x02\x03",

            "If you ask me, it's probably...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)

    ChrTalk(    #80
        0x12,
        "#1792F#5P#80WHmm...#20W Strength, I suppose?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x11,
        "#731F#12P...Bwuh?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x12, 180, 400)
    Sleep(300)

    ChrTalk(    #82
        0x12,
        (
            "#1793F#5P*sigh* Speaking of strength...\x02\x03",

            "...I feel like smacking Lechter upside the\x01",
            "head right now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x11,
        (
            "#735F#12PWell...\x02\x03",

            "#737F(If you need someone to hit, you can smack\x01",
            "me around much as you like!)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x105, 0x8)
    OP_6D(0, -250, -7230, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_4B(0x11, 255)
    OP_4B(0x12, 255)
    SetChrPos(0x11, 1620, 0, -4100, 90)
    SetChrPos(0x12, -720, 0, -4100, 270)
    Sleep(500)
    FadeToBright(2000, 0)
    OP_0D()
    OP_A2(0x2F70)
    EventEnd(0x0)
    Return()

    # Function_17_1C59 end

    def Function_18_20F5(): pass

    label("Function_18_20F5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2149")
    OP_8C(0x12, 225, 500)
    Sleep(800)
    OP_8C(0x12, 315, 500)
    Sleep(800)
    OP_8C(0x12, 270, 500)
    Sleep(1200)
    OP_8C(0x12, 315, 500)
    Sleep(800)
    OP_8C(0x12, 225, 500)
    Sleep(800)
    OP_8C(0x12, 270, 500)
    Sleep(1200)
    Jump("Function_18_20F5")

    label("loc_2149")

    Return()

    # Function_18_20F5 end

    SaveToFile()

Try(main)
