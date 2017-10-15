from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4121_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4121_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AF",           # 01, 1
        "Function_2_B4",           # 02, 2
        "Function_3_B9",           # 03, 3
        "Function_4_2D3",          # 04, 4
        "Function_5_4C8",          # 05, 5
        "Function_6_7F2",          # 06, 6
        "Function_7_A11",          # 07, 7
        "Function_8_D2C",          # 08, 8
        "Function_9_FBB",          # 09, 9
        "Function_10_2074",        # 0A, 10
        "Function_11_2DE2",        # 0B, 11
        "Function_12_367B",        # 0C, 12
        "Function_13_463A",        # 0D, 13
        "Function_14_5E00",        # 0E, 14
        "Function_15_5E7B",        # 0F, 15
        "Function_16_5ED2",        # 10, 16
        "Function_17_5F3E",        # 11, 17
        "Function_18_5F90",        # 12, 18
        "Function_19_604B",        # 13, 19
        "Function_20_615D",        # 14, 20
        "Function_21_61AA",        # 15, 21
        "Function_22_61FE",        # 16, 22
        "Function_23_6234",        # 17, 23
        "Function_24_62B9",        # 18, 24
        "Function_25_631C",        # 19, 25
        "Function_26_6355",        # 1A, 26
        "Function_27_63B3",        # 1B, 27
        "Function_28_63E5",        # 1C, 28
        "Function_29_641A",        # 1D, 29
        "Function_30_6440",        # 1E, 30
        "Function_31_64B7",        # 1F, 31
        "Function_32_64F4",        # 20, 32
        "Function_33_657F",        # 21, 33
        "Function_34_65B7",        # 22, 34
        "Function_35_661C",        # 23, 35
        "Function_36_66C1",        # 24, 36
        "Function_37_68FE",        # 25, 37
        "Function_38_AE7B",        # 26, 38
        "Function_39_B1C1",        # 27, 39
        "Function_40_B2B0",        # 28, 40
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Call(1, 12)
    Return()

    # Function_0_AA end

    def Function_1_AF(): pass

    label("Function_1_AF")

    Call(0, 37)
    Return()

    # Function_1_AF end

    def Function_2_B4(): pass

    label("Function_2_B4")

    Call(1, 9)
    Return()

    # Function_2_B4 end

    def Function_3_B9(): pass

    label("Function_3_B9")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_149")
    Jump("loc_18B")

    label("loc_149")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_165")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18B")

    label("loc_165")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_181")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_18B")

    label("loc_181")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18B")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    ChrTalk(    #0
        0xA,
        "#051FYo, what's up?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "End\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_21D"),
        (SWITCH_DEFAULT, "loc_257"),
    )


    label("loc_21D")


    ChrTalk(    #1
        0xA,
        "#051FYeah, yeah, I got it.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_250")
    Call(0, 5)
    Jump("loc_254")

    label("loc_250")

    Call(0, 4)

    label("loc_254")

    Jump("loc_2CA")

    label("loc_257")


    ChrTalk(    #2
        0xA,
        (
            "#052FWhat, changed your mind?\x02\x03",

            "#050FWell, if you ever need somebody to\x01",
            "swing a sword around, gimme a call.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CA")

    label("loc_2CA")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    # Function_3_B9 end

    def Function_4_2D3(): pass

    label("Function_4_2D3")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_363")
    Jump("loc_3A5")

    label("loc_363")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37F")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A5")

    label("loc_37F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39B")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A5")

    label("loc_39B")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A5")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    ChrTalk(    #3
        0x9,
        "#020FHm? What is it?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "Never mind\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_43F"),
        (SWITCH_DEFAULT, "loc_473"),
    )


    label("loc_43F")


    ChrTalk(    #4
        0x9,
        "#020FNeed some help?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46C")
    Call(0, 5)
    Jump("loc_470")

    label("loc_46C")

    Call(0, 4)

    label("loc_470")

    Jump("loc_4BF")

    label("loc_473")


    ChrTalk(    #5
        0x9,
        (
            "#020FI'll hang around here for a bit, then.\x02\x03",

            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BF")

    label("loc_4BF")

    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Return()

    # Function_4_2D3 end

    def Function_5_4C8(): pass

    label("Function_5_4C8")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_558")
    Jump("loc_59A")

    label("loc_558")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_574")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59A")

    label("loc_574")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_590")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_59A")

    label("loc_590")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_59A")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(    #6
        0xB,
        "#030FGood day.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "Never mind\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_70A")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_635"),
        (SWITCH_DEFAULT, "loc_69C"),
    )


    label("loc_635")


    ChrTalk(    #7
        0xB,
        (
            "#030FAh, of course!\x02\x03",

            "You need the power of my genius.\x01",
            "Not to worry; I understand entirely.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 4)
    Jump("loc_707")

    label("loc_69C")


    ChrTalk(    #8
        0xB,
        (
            "#030FOh? Changed your mind?\x02\x03",

            "Well, should you ever long for my\x01",
            "dulcet tones, simply give the word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_707")

    label("loc_707")

    Jump("loc_7E9")

    label("loc_70A")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_717"),
        (SWITCH_DEFAULT, "loc_77E"),
    )


    label("loc_717")


    ChrTalk(    #9
        0xB,
        (
            "#030FAh, of course!\x02\x03",

            "You need the power of my genius.\x01",
            "Not to worry; I understand entirely.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 2)
    Jump("loc_7E9")

    label("loc_77E")


    ChrTalk(    #10
        0xB,
        (
            "#030FOh? Changed your mind?\x02\x03",

            "Well, should you ever long for my\x01",
            "dulcet tones, simply give the word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E9")

    label("loc_7E9")

    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    # Function_5_4C8 end

    def Function_6_7F2(): pass

    label("Function_6_7F2")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_833")

    ChrTalk(    #11
        0xC,
        (
            "#040FOh, hey, guys.\x02\x03",

            "Anything I can help with?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AA")

    label("loc_833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_876")

    ChrTalk(    #12
        0xC,
        (
            "#040FOh, hey, guys.\x02\x03",

            "Anything I can help with?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AA")

    label("loc_876")


    ChrTalk(    #13
        0xC,
        (
            "#040FOh, hey, guys.\x02\x03",

            "Anything I can help with?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AA")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "Never mind\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_905"),
        (SWITCH_DEFAULT, "loc_9AB"),
    )


    label("loc_905")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_93D")

    ChrTalk(    #14
        0xC,
        "#040FI'd be more than happy to help.\x02",
    )

    CloseMessageWindow()
    Call(0, 4)
    Jump("loc_9A8")

    label("loc_93D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_97A")

    ChrTalk(    #15
        0xC,
        "#040FI'd be more than happy to help.\x02",
    )

    CloseMessageWindow()
    Call(0, 3)
    Jump("loc_9A8")

    label("loc_97A")


    ChrTalk(    #16
        0xC,
        "#040FI'd be more than happy to help.\x02",
    )

    CloseMessageWindow()
    Call(0, 2)

    label("loc_9A8")

    Jump("loc_A0D")

    label("loc_9AB")


    ChrTalk(    #17
        0xC,
        (
            "#040FI'll stay here for a bit, then.\x02\x03",

            "If you need me for anything,\x01",
            "don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A0D")

    label("loc_A0D")

    TalkEnd(0xC)
    Return()

    # Function_6_7F2 end

    def Function_7_A11(): pass

    label("Function_7_A11")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A51")

    ChrTalk(    #18
        0xD,
        (
            "#560FOh, hi, Agate!\x02\x03",

            "Is everything okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AB4")

    label("loc_A51")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A8B")

    ChrTalk(    #19
        0xD,
        "#060FHi, Estelle! What's up?\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB4")

    label("loc_A8B")


    ChrTalk(    #20
        0xD,
        (
            "#060FHi, guys!\x02\x03",

            "Is everything okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB4")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "Never mind\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B0F"),
        (SWITCH_DEFAULT, "loc_C5D"),
    )


    label("loc_B0F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B84")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B58")

    ChrTalk(    #21
        0xD,
        "#060FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B7D")

    label("loc_B58")


    ChrTalk(    #22
        0xD,
        "#560FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()

    label("loc_B7D")

    Call(0, 5)
    Jump("loc_C5A")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_BF4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BC8")

    ChrTalk(    #23
        0xD,
        "#060FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BED")

    label("loc_BC8")


    ChrTalk(    #24
        0xD,
        "#560FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()

    label("loc_BED")

    Call(0, 4)
    Jump("loc_C5A")

    label("loc_BF4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C31")

    ChrTalk(    #25
        0xD,
        "#060FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C56")

    label("loc_C31")


    ChrTalk(    #26
        0xD,
        "#560FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()

    label("loc_C56")

    Call(0, 2)

    label("loc_C5A")

    Jump("loc_D28")

    label("loc_C5D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CCD")

    ChrTalk(    #27
        0xD,
        (
            "#064FHuh? Are you sure?\x02\x03",

            "#060FWell, I'll be here. Just call for\x01",
            "me if you need me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D25")

    label("loc_CCD")


    ChrTalk(    #28
        0xD,
        (
            "#064FHuh? Are you sure?\x02\x03",

            "#060FWell, I'll be here. Just call for\x01",
            "me if you need me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D25")

    Jump("loc_D28")

    label("loc_D28")

    TalkEnd(0xD)
    Return()

    # Function_7_A11 end

    def Function_8_D2C(): pass

    label("Function_8_D2C")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DBC")
    Jump("loc_DFE")

    label("loc_DBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DD8")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DFE")

    label("loc_DD8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DF4")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DFE")

    label("loc_DF4")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DFE")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #29
        0xE,
        "#070FHey, how's it going?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Change Party\x01",      # 0
            "Never mind\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E9D"),
        (SWITCH_DEFAULT, "loc_F88"),
    )


    label("loc_E9D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDC")

    ChrTalk(    #30
        0xE,
        "#070FNeed me to sub in, huh? I'm game!\x02",
    )

    CloseMessageWindow()
    Call(0, 5)
    Jump("loc_F85")

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_F16")

    ChrTalk(    #31
        0xE,
        "#070FNeed me to sub in, huh? I'm game!\x02",
    )

    CloseMessageWindow()
    Call(0, 4)
    Jump("loc_F85")

    label("loc_F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F55")

    ChrTalk(    #32
        0xE,
        "#070FNeed me to sub in, huh? I'm game!\x02",
    )

    CloseMessageWindow()
    Call(0, 3)
    Jump("loc_F85")

    label("loc_F55")


    ChrTalk(    #33
        0xE,
        "#070FNeed me to sub in, huh? I'm game!\x02",
    )

    CloseMessageWindow()
    Call(0, 2)

    label("loc_F85")

    Jump("loc_FB2")

    label("loc_F88")


    ChrTalk(    #34
        0xE,
        "#070FI'll be here if you need me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB2")

    label("loc_FB2")

    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Return()

    # Function_8_D2C end

    def Function_9_FBB(): pass

    label("Function_9_FBB")

    TalkBegin(0x19)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_40(0x415, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1228")
    TurnDirection(0x19, 0x101, 0)

    ChrTalk(    #35
        0x19,
        "...Hmm?\x02",
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0x19,
        (
            "My word! That's a Master Fisher Card!\x01",
            "No doubt about it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1015FUh... Oh, this thing I got from Lloyd.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x19,
        (
            "The Master Fisher Card, which only those\x01",
            "who can fish up a famed Guardian can claim...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x19,
        "...and proof you are a comrade of us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1016FI-Is it?\x02\x03",

            "(That kind of makes me happy,\x01",
            "and also kind of not...)\x01\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x19,
        (
            "Also, Master Fishers can purchase\x01",
            "as much bait as they need here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#1018FReally? That's nice...\x01\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x19,
        "It certainly is! It's a real perk, don'cha know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x19,
        (
            "Should you need bait, just come\x01",
            "speak to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20E7)
    TalkEnd(0x19)
    Return()

    label("loc_1228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41C, 7)), scpexpr(EXPR_END)), "loc_125A")
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1249")
    OP_A9(0xDC)
    TalkEnd(0x19)
    Return()

    label("loc_1249")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125A")
    TalkEnd(0x19)
    Return()

    label("loc_125A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_1264")
    Jump("loc_2070")

    label("loc_1264")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1361")

    ChrTalk(    #45
        0x19,
        (
            "Even if orbments stop, nothing can\x01",
            "cool the passion for fishing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x19,
        (
            "This is exactly the time to get the\x01",
            "citizenry to enjoy fishing and calm\x01",
            "themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x19,
        (
            "They'd also secure food supplies,\x01",
            "so it's two birds with one stone.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1403")

    label("loc_1361")


    ChrTalk(    #48
        0x19,
        (
            "This is exactly the time to get the\x01",
            "citizenry to enjoy fishing and calm\x01",
            "themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x19,
        (
            "They'd also secure food supplies,\x01",
            "so it's two birds with one stone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1403")

    Jump("loc_2070")

    label("loc_1406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_15B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_152F")

    ChrTalk(    #50
        0x19,
        (
            "Our comrade Percy went to investigate\x01",
            "fishing spots in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x19,
        (
            "If he finds some unknown spots,\x01",
            "there might be a top-class fish there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x19,
        (
            "We also have an obligation\x01",
            "to open fishing classes in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x19,
        (
            "His mission is critical for the development\x01",
            "of our society.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_15B4")

    label("loc_152F")


    ChrTalk(    #54
        0x19,
        (
            "Our comrade Percy went to investigate\x01",
            "fishing spots in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x19,
        (
            "His mission is critical for the development\x01",
            "of our society.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B4")

    Jump("loc_2070")

    label("loc_15B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_164B")

    ChrTalk(    #56
        0x19,
        "You seem to be in a rush...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x19,
        (
            "If you cannot control your mind and look\x01",
            "over the fishing spot calmly, you'll never\x01",
            "land more fish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2070")

    label("loc_164B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_1853")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1798")

    ChrTalk(    #58
        0x19,
        (
            "Our group has fought with the Guardians of\x01",
            "Valleria Lake for ten years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x19,
        (
            "It is our deepest desire to see the most\x01",
            "fearsome of beasts pulled up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x19,
        (
            "With you as our comrade, I'm sure\x01",
            "you'll make it happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x19,
        (
            "There is no fish that cannot be caught!\x01",
            "That is the motto of we of the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1850")

    label("loc_1798")


    ChrTalk(    #62
        0x19,
        (
            "With you as our comrade, I'm sure a Guardian\x01",
            "fish shall be snared once and for all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x19,
        (
            "There is no fish that cannot be caught!\x01",
            "That is the motto of we of the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1850")

    Jump("loc_2070")

    label("loc_1853")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_198A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 2)), scpexpr(EXPR_END)), "loc_192F")

    ChrTalk(    #64
        0x19,
        (
            "If you're talking about the girl in the\x01",
            "white dress, she left after asking me a\x01",
            "very odd question.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x19,
        "I believe the question was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x19,
        (
            "'Do you know where the bitter,\x01",
            "spicy, delicious store is?'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1987")

    label("loc_192F")


    ChrTalk(    #67
        0x19,
        "Are you looking for someone?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x19,
        (
            "It's only me and the group here,\x01",
            "I think, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1987")

    Jump("loc_2070")

    label("loc_198A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_1A4F")

    ChrTalk(    #69
        0x19,
        (
            "It's been twenty years since our guild\x01",
            "was founded...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x19,
        (
            "And steadily comrades who share my\x01",
            "ideals have joined us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x19,
        (
            "I'd like to host an event\x01",
            "to celebrate this, but what kind?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2070")

    label("loc_1A4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AD7")

    ChrTalk(    #72
        0x19,
        (
            "We plan on closing early today and\x01",
            "heading out to Valleria Lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x19,
        "Personally, I'm aiming for some sweet Kasagin.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2070")

    label("loc_1AD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1D16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C3C")

    ChrTalk(    #74
        0x19,
        (
            "A non-aggression pact binding these three\x01",
            "countries... A very powerful-sounding idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x19,
        (
            "The time will come for we, the Fisherman's Guild,\x01",
            "to open branches in the Empire and the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x19,
        (
            "When that time comes, we hope to proudly represent\x01",
            "our values on an international scale like you\x01",
            "bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x19,
        "It's my little ambition.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1D13")

    label("loc_1C3C")


    ChrTalk(    #78
        0x19,
        (
            "The time will come for we, the Fisherman's Guild,\x01",
            "to open branches in the Empire and the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x19,
        (
            "When that time comes, we hope to proudly represent\x01",
            "our values on an international scale like you\x01",
            "bracers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D13")

    Jump("loc_2070")

    label("loc_1D16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_1FAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F42")

    ChrTalk(    #80
        0x19,
        "Ahem! Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x19,
        (
            "We, the Fisherman's Guild, are determined and\x01",
            "dedicated in our quest to catch the Guardians\x01",
            "that exists within Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x12F,
        "#264FWhat're 'Guardians'?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x12F, 400)

    ChrTalk(    #83
        0x101,
        (
            "#1015FHmm... Well, basically big fish.\x02\x03",

            "#1000FIt's the reason there are so many\x01",
            "fans of fishing in Liberl.\x02\x03",

            "Renne, did you ever fish with your papa?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12F, 0x101, 400)

    ChrTalk(    #84
        0x12F,
        (
            "#261FHeehee... Oh, Estelle.\x02\x03",

            "Fishing's for kids and guys, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1019FUhhh... I guess.\x02\x03",

            "#1016FBut, I do it. It's pretty fun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x12F,
        (
            "#264FReally? \x02\x03",

            "#265FWell, maybe I'll try it, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x164D)
    Jump("loc_1FAB")

    label("loc_1F42")


    ChrTalk(    #87
        0x19,
        "If you like fishing, you should come here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x19,
        (
            "We always welcome passionate\x01",
            "youths into our ranks!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAB")

    Jump("loc_2070")

    label("loc_1FAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2070")

    ChrTalk(    #89
        0x19,
        "Ahem! Welcome to the Fisherman's Guild!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x19,
        (
            "I am Fisher, or the 'Fishing Baron' as they\x01",
            "call me! Hahaha!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x19,
        (
            "Are you new applicants? If you like fishing,\x01",
            "you're more than welcome!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2070")

    TalkEnd(0x19)
    Return()

    # Function_9_FBB end

    def Function_10_2074(): pass

    label("Function_10_2074")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_2081")
    Jump("loc_2DDE")

    label("loc_2081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_210C")

    ChrTalk(    #92
        0xFE,
        (
            "Even without orbal energy, there's\x01",
            "nothing to worry about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "It's no different than camping out\x01",
            "when chasing a Guardian.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DDE")

    label("loc_210C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_22DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2223")

    ChrTalk(    #94
        0xFE,
        (
            "Yesterday, when I went to the harbor block\x01",
            "I witnessed something crazy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "There was a tank and a giant machine\x01",
            "doll-like thing... I've ain't never seen such a sight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Personally, I'm worried that it might've\x01",
            "disturbed the poor fish in that area.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_22D8")

    label("loc_2223")


    ChrTalk(    #97
        0xFE,
        (
            "Over at the harbor, there was a tank and this\x01",
            "giant machine, doll-like thing. It was terrible!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "Personally, I'm worried that it might have\x01",
            "disturbed the fish in that area.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D8")

    Jump("loc_2DDE")

    label("loc_22DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_239E")

    ChrTalk(    #99
        0xFE,
        (
            "Now, then, tomorrow it's time to hit Valleria\x01",
            "Lake at night for the first time in a while!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "You get bigger fish than you might expect\x01",
            "at the harbor block's warehouse district.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DDE")

    label("loc_239E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_2552")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24B9")

    ChrTalk(    #101
        0xFE,
        (
            "According to the reports, Valleria Lake's\x01",
            "Guardians are in the Bose region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "I'll be flying off to Bose to challenge\x01",
            "one of 'em again soon!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "My line broke just as I was about to reel\x01",
            "one of them beauties in last time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "This time... THIS TIME...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_254F")

    label("loc_24B9")


    ChrTalk(    #105
        0xFE,
        (
            "According to the reports, Valleria Lake's\x01",
            "Guardian is in the Bose region.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "I'll be flying off to Bose to challenge\x01",
            "them again soon, I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_254F")

    Jump("loc_2DDE")

    label("loc_2552")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_27A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 1)), scpexpr(EXPR_END)), "loc_25CF")

    ChrTalk(    #107
        0xFE,
        (
            "A bit ago, a girl in a white, frilly\x01",
            "dress came by the first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "You think she wanted to join?\x02",
    )

    CloseMessageWindow()
    Jump("loc_279D")

    label("loc_25CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2719")

    ChrTalk(    #109
        0xFE,
        (
            "There's a housewife who's been getting\x01",
            "amazingly good ever since she joined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "Her name's Norche, and she joined 'round\x01",
            "the time of the Birthday Celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "Wasn't long ago she fished herself up a Guardian and\x01",
            "earned the same Master Fisher rank as me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "Guess I can't be restin' on my laurels, huh?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_279D")

    label("loc_2719")


    ChrTalk(    #113
        0xFE,
        (
            "There's a housewife who's been getting\x01",
            "amazingly good ever since she joined.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "Guess I can't be resting on my laurels, huh?\x02",
    )

    CloseMessageWindow()

    label("loc_279D")

    Jump("loc_2DDE")

    label("loc_27A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_285B")

    ChrTalk(    #115
        0xFE,
        (
            "We also develop new fishing spots as part\x01",
            "of our attempts to popularize fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Plus, we also do environmental upkeep to\x01",
            "ensure the fishing spots are safe and clean.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DDE")

    label("loc_285B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2923")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28BD")

    ChrTalk(    #117
        0xFE,
        "Oh, no! It's almost evening!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        "To not be fishing now is a waste!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2920")

    label("loc_28BD")


    ChrTalk(    #119
        0xFE,
        (
            "Around this time the fish get active\x01",
            "and it's easier to catch them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        "I can't let this go.\x02",
    )

    CloseMessageWindow()

    label("loc_2920")

    Jump("loc_2DDE")

    label("loc_2923")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_29E5")

    ChrTalk(    #121
        0xFE,
        "Fishing is a fight with nature.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "Even if you use every bit of your talent,\x01",
            "it's common for things to not go as you\x01",
            "think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "Hehehe...\x01",
            "That's what's so great about fishing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DDE")

    label("loc_29E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_2B5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AF9")

    ChrTalk(    #124
        0xFE,
        (
            "I bet you think that Grancel isn't great\x01",
            "for fishing with so few water sources,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "But, surprise! There's a great\x01",
            "little spot right next door!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "Do you know Romal Pond near the royal villa?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "There's a lot of fish in that little spot.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2B5B")

    label("loc_2AF9")


    ChrTalk(    #128
        0xFE,
        "Do you know Romal Pond near the royal villa?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        "There's a lot of fish in that little spot.\x02",
    )

    CloseMessageWindow()

    label("loc_2B5B")

    Jump("loc_2DDE")

    label("loc_2B5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2DDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D52")
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #130
        0xFE,
        "Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "Hey there! Been a while, hasn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#1004FOh, Lloyd! Hey. So you're back from Ruan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "How's the fishing been? Gettin' some\x01",
            "use out of that rod I gave you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        "#1016FK-Kinda. I go in between work when I can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Skilled folk like you are always\x01",
            "welcome at the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "If you ever wannna join, you let\x01",
            "Mr. Fisher know any ol' time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "I'm sure he'll be overjoyed to have a\x01",
            "new comrade.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        "#1008FAhaha... I'll keep that in mind.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x164E)
    Jump("loc_2DDE")

    label("loc_2D52")


    ChrTalk(    #139
        0xFE,
        (
            "Skilled folk like you are always\x01",
            "welcome at the Fisherman's Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "If you ever wannna join, you let\x01",
            "Mr. Fisher know any ol' time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DDE")

    TalkEnd(0xFE)
    Return()

    # Function_10_2074 end

    def Function_11_2DE2(): pass

    label("Function_11_2DE2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_2DEF")
    Jump("loc_3677")

    label("loc_2DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2ECB")

    ChrTalk(    #141
        0xFE,
        (
            "Our society's members are pretty\x01",
            "used to outdoor activities.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "Seems like they're not as bothered as other\x01",
            "people when it comes to roughing it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "Lloyd's even lighting fires rubbing\x01",
            "sticks together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3677")

    label("loc_2ECB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2ED5")
    Jump("loc_3677")

    label("loc_2ED5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_2F4C")

    ChrTalk(    #144
        0xFE,
        (
            "After this, I'll be talking some\x01",
            "plans over with Fisher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        "Apparently he's got a new mission for me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3677")

    label("loc_2F4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_2FA0")

    ChrTalk(    #146
        0xFE,
        (
            "Phew! I thought I was getting hungry.\x01",
            "No wonder. It's already night.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3677")

    label("loc_2FA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_30C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 1)), scpexpr(EXPR_END)), "loc_3013")

    ChrTalk(    #147
        0xFE,
        (
            "Lately it seems like there's more\x01",
            "women interested in fishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "We're happy to have 'em.\x02",
    )

    CloseMessageWindow()
    Jump("loc_30C4")

    label("loc_3013")


    ChrTalk(    #149
        0xFE,
        (
            "Ever since orbal cameras became popular,\x01",
            "you don't see many fish prints.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "But I have to admit, when you make a big\x01",
            "catch, I'd like to leave something like\x01",
            "that behind.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C4")

    Jump("loc_3677")

    label("loc_30C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_30F3")

    ChrTalk(    #151
        0xFE,
        "Where to go fishing today...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3677")

    label("loc_30F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323D")

    ChrTalk(    #152
        0xFE,
        (
            "Beginners brought along on practice\x01",
            "often get seasick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        "The best counter-plan is to get plenty of sleep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "It's also best not to eat too much before\x01",
            "getting aboard the boat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "People who have just started fishing often get\x01",
            "bogged down with advanced preparations\x01",
            "and don't get enough sleep.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_32F7")

    label("loc_323D")


    ChrTalk(    #156
        0xFE,
        (
            "Beginners brought along on practice\x01",
            "often get seasick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "The best counter-plan is to get plenty of sleep.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "It's also best not to eat too much before\x01",
            "getting aboard the boat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F7")

    Jump("loc_3677")

    label("loc_32FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_33D5")

    ChrTalk(    #159
        0xFE,
        (
            "Thinking about it, it was really terrible\x01",
            "on us during the coup d'etat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "Day after day of incredible fishing weather,\x01",
            "but we were forbidden from going out at night...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        "To us, it was like torture.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3677")

    label("loc_33D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_35EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3559")

    ChrTalk(    #162
        0xFE,
        (
            "Fisherman's Guild members are ranked\x01",
            "according to their successes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        (
            "People who manage to land a 'Guardian'\x01",
            "are called Master Fishers and get a\x01",
            "special card.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xFE,
        (
            "People like me who are still newbies are\x01",
            "just 'Amateur Fishers.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "Incidentally the headman of the Fisherman's Guild\x01",
            "has a rank all to his own...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        "It's the 'Avid Angler.' Pretty cool, huh?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_35E7")

    label("loc_3559")


    ChrTalk(    #167
        0xFE,
        (
            "Fisherman's Guild members are ranked\x01",
            "according to their successes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "People like me who are still newbies are\x01",
            "just 'Amateur Fishers.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35E7")

    Jump("loc_3677")

    label("loc_35EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3677")

    ChrTalk(    #169
        0xFE,
        "You know about those Guardian fish?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        (
            "They're special to each region! I'd sure like to\x01",
            "be able to fish one up myself someday.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3677")

    TalkEnd(0xFE)
    Return()

    # Function_11_2DE2 end

    def Function_12_367B(): pass

    label("Function_12_367B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_436D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_384B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as no phones restored yet\x01",                   # 0
            "Set as only Rolent's phone restored\x01",             # 1
            "Set as only Ruan's phone restored\x01",               # 2
            "Set as only Zeiss' phone restored\x01",               # 3
            "Set as Rolent's and Ruan's phones restored\x01",      # 4
            "Set as Rolent's and Zeiss' phones restored\x01",      # 5
            "Set as Ruan's and Zeiss' phones restored\x01",        # 6
            "No change\x01",                                       # 7
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_37F7"),
        (1, "loc_3803"),
        (2, "loc_380F"),
        (3, "loc_381B"),
        (4, "loc_3827"),
        (5, "loc_3833"),
        (6, "loc_383F"),
        (SWITCH_DEFAULT, "loc_384B"),
    )


    label("loc_37F7")

    OP_A3(0x2003)
    OP_A3(0x2001)
    OP_A3(0x2005)
    Jump("loc_384B")

    label("loc_3803")

    OP_A2(0x2003)
    OP_A3(0x2001)
    OP_A3(0x2005)
    Jump("loc_384B")

    label("loc_380F")

    OP_A3(0x2003)
    OP_A2(0x2001)
    OP_A3(0x2005)
    Jump("loc_384B")

    label("loc_381B")

    OP_A3(0x2003)
    OP_A3(0x2001)
    OP_A2(0x2005)
    Jump("loc_384B")

    label("loc_3827")

    OP_A2(0x2003)
    OP_A2(0x2001)
    OP_A3(0x2005)
    Jump("loc_384B")

    label("loc_3833")

    OP_A2(0x2003)
    OP_A3(0x2001)
    OP_A2(0x2005)
    Jump("loc_384B")

    label("loc_383F")

    OP_A3(0x2003)
    OP_A2(0x2001)
    OP_A2(0x2005)
    Jump("loc_384B")

    label("loc_384B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41D8")

    ChrTalk(    #171
        0x8,
        (
            "#763FO-ho...\x02\x03",

            "#760FEstelle, everyone...and Joshua.\x02\x03",

            "Welcome back.\x01",
            "I'm glad you've returned safely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x102,
        (
            "#1040FHello, Elnan.\x01",
            "I'm sorry if I worried you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "#761FNo, hardly.\x01",
            "I'm just glad to see you well.\x02\x03",

            "#760FI hope you'll continue to be a\x01",
            "valuable member of the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1002FSorry to cut in, Elnan, but how're\x01",
            "things here in Grancel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        (
            "#764FYes, well...the city's in chaos thanks to the\x01",
            "sudden shutdown of all orbal devices.\x02\x03",

            "#762FThe local factory is snowed under in\x01",
            "repair requests, as I understand it.\x02\x03",

            "#760FHowever, Queen Alicia has made a proclamation.\x02\x03",

            "She has declared that the government is\x01",
            "devoting every resource to investigating\x01",
            "and reversing the shutdown phenomenon...\x02\x03",

            "...and that citizens should try to continue their\x01",
            "daily lives as best they can. It seems to have\x01",
            "quelled the worst of the panic, for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        (
            "#1018FLooks like Queen Alicia's on\x01",
            "top of it as always!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        (
            "#762FYes... But that giant flying...thing\x01",
            "above Valleria Lake...\x02\x03",

            "The citizens are putting two and two together,\x01",
            "and saying it's the cause of the orbal problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x102,
        "#1042FI see. That's not very surprising.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x8,
        (
            "#762FThe number of people staring at\x01",
            "it in the harbor grows hourly.\x02\x03",

            "Beyond that, the only other major change\x01",
            "is that the gate to Grancel Castle won't\x01",
            "open, courtesy of the orbal suspension.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        (
            "#1015FOkay... Things are calmer here than\x01",
            "I thought they'd be, honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x8,
        (
            "#760FYes. If this situation drags on, however,\x01",
            "I don't think things will remain so...placid.\x02\x03",

            "We need to restore communications across\x01",
            "the country so that we can organize a\x01",
            "solution as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x102,
        (
            "#1035FAnd so we need to restore\x01",
            "the phones in each city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#1006FMeaning our mission is pretty critical.\x02\x03",

            "#1002FLet's get back to it, then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3FC8")

    ChrTalk(    #184
        0x102,
        (
            "#1042FRolent, Ruan, and Zeiss...\x02\x03",

            "It doesn't matter where we start, but we\x01",
            "need to deliver these Zero Field Generators\x01",
            "as soon as we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4136")

    label("loc_3FC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_400A")

    ChrTalk(    #185
        0x102,
        "#1040FWe still have Ruan and Zeiss left.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4136")

    label("loc_400A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_404E")

    ChrTalk(    #186
        0x102,
        "#1040FWe still have Rolent and Zeiss left.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4136")

    label("loc_404E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4091")

    ChrTalk(    #187
        0x102,
        "#1040FWe still have Rolent and Ruan left.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4136")

    label("loc_4091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40C9")

    ChrTalk(    #188
        0x102,
        "#1040FAll that's left is Zeiss.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4136")

    label("loc_40C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4100")

    ChrTalk(    #189
        0x102,
        "#1040FAll that's left is Ruan.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4136")

    label("loc_4100")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4136")

    ChrTalk(    #190
        0x102,
        "#1040FAll that's left is Rolent.\x02",
    )

    CloseMessageWindow()

    label("loc_4136")


    ChrTalk(    #191
        0x101,
        "#1000FYeah, let's hurry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x8,
        (
            "#760FIt is not an overstatement to\x01",
            "say that the future of Liberl\x01",
            "may rest on your shoulders.\x02\x03",

            "Good luck, all of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20DA)
    TalkEnd(0x8)
    Return()

    label("loc_41D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_436D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_42D7")

    ChrTalk(    #193
        0x8,
        (
            "#762FI had the citizens in this area\x01",
            "evacuate into the guild.\x02\x03",

            "The army should be leading evacuation\x01",
            "activity in the other regions as well.\x02\x03",

            "Everyone, head to the castle and\x01",
            "chase down those Enforcers.\x02\x03",

            "#765FTheir goal is likely...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436A")

    label("loc_42D7")


    ChrTalk(    #194
        0x8,
        (
            "#760FIt's not excessive to say that order\x01",
            "in Liberl depends on you.\x02\x03",

            "Please, restore communications between\x01",
            "the branches as soon as possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_436A")

    OP_A2(0x20DB)

    label("loc_436D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43DC")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",             # 0
            "Report\x01",           # 1
            "Call Allies\x01",      # 2
            "Leave\x01",            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jump("loc_43E0")

    label("loc_43DC")

    Call(6, 5)

    label("loc_43E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4511")
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_440A")
    OP_28(0xC3, 0x4, 0x20)

    label("loc_440A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0xCD)"), scpexpr(EXPR_END)), "loc_4490")

    ChrTalk(    #195
        0x8,
        (
            "#760FGood work. It seems you succeeded\x01",
            "at your objectives safely.\x02\x03",

            "If you complete any other tasks,\x01",
            "come report again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4508")

    label("loc_4490")


    ChrTalk(    #196
        0x8,
        (
            "#760FDoesn't seem like you have any\x01",
            "jobs to report right now.\x02\x03",

            "If you complete any other tasks,\x01",
            "come report again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4508")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_4511")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4624")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_461D")

    ChrTalk(    #197
        0x8,
        (
            "#760FYou want me to call everyone here?\x02\x03",

            "Understood. Well, then, let me\x01",
            "put in the word immediately.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #198
        (
            "\x07\x05All branches were contacted and members on standby\x01",
            "were gathered.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_461D")

    TalkEnd(0x8)
    Return()

    label("loc_4624")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4635")
    TalkEnd(0x8)
    Return()

    label("loc_4635")

    Call(1, 13)
    Return()

    # Function_12_367B end

    def Function_13_463A(): pass

    label("Function_13_463A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_4731")

    ChrTalk(    #199
        0x8,
        (
            "#762FI had the citizens in this area\x01",
            "evacuate into the guild.\x02\x03",

            "The army should be leading evacuation\x01",
            "activity in the other regions as well.\x02\x03",

            "Everyone, head to the castle and\x01",
            "chase down those Enforcers.\x02\x03",

            "#765FTheir goal is likely...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFC")

    label("loc_4731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4C73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47E1")

    ChrTalk(    #200
        0x8,
        (
            "#760FIt's not excessive to say that order\x01",
            "in Liberl depends on you.\x02\x03",

            "Rolent, Ruan, Zeiss... Please restore\x01",
            "communications to all our branches.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C70")

    label("loc_47E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48A9")

    ChrTalk(    #201
        0x8,
        (
            "#760FWe still cannot communicate with\x01",
            "the Ruan or Zeiss branches.\x02\x03",

            "It's not excessive to say that order\x01",
            "in Liberl depends on you.\x02\x03",

            "I'm aware it's quite a journey, but please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C70")

    label("loc_48A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4973")

    ChrTalk(    #202
        0x8,
        (
            "#760FWe still cannot communicate with\x01",
            "the Rolent or Zeiss branches.\x02\x03",

            "It's not excessive to say that order\x01",
            "in Liberl depends on you.\x02\x03",

            "I'm aware it's quite a journey, but please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C70")

    label("loc_4973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A3C")

    ChrTalk(    #203
        0x8,
        (
            "#760FWe still cannot communicate with\x01",
            "the Rolent or Ruan branches.\x02\x03",

            "It's not excessive to say that order\x01",
            "in Liberl depends on you.\x02\x03",

            "I'm aware it's quite a journey, but please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C70")

    label("loc_4A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AF9")

    ChrTalk(    #204
        0x8,
        (
            "#760FWe still cannot communicate with the\x01",
            "Zeiss branch.\x02\x03",

            "It's not excessive to say that order\x01",
            "in Liberl depends on you.\x02\x03",

            "I'm aware it's quite a journey, but please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C70")

    label("loc_4AF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BB5")

    ChrTalk(    #205
        0x8,
        (
            "#760FWe still cannot communicate with the\x01",
            "Ruan branch.\x02\x03",

            "It's not excessive to say that order\x01",
            "in Liberl depends on you.\x02\x03",

            "I'm aware it's quite a journey, but please.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C70")

    label("loc_4BB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C70")

    ChrTalk(    #206
        0x8,
        (
            "#760FWe still cannot communicate with the\x01",
            "Rolent branch.\x02\x03",

            "It's not excessive to say that order\x01",
            "in Liberl depends on you.\x02\x03",

            "I'm aware it's quite a journey, but please.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C70")

    Jump("loc_5DFC")

    label("loc_4C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_4D63")

    ChrTalk(    #207
        0x8,
        (
            "#760FNext, please head to the Bose region\x01",
            "where the sky bandits appeared.\x02\x03",

            "I've already contacted the landing port\x01",
            "and organized tickets for you.\x02\x03",

            "As soon as you're ready, please check\x01",
            "in for your flight at the landing port.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFC")

    label("loc_4D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_5A15")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 4)), scpexpr(EXPR_END)), "loc_4E15")

    ChrTalk(    #208
        0x8,
        "#760FEstelle, have you found Renne yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0x101,
        (
            "#1000FNo, not yet. But, I think we'll be able\x01",
            "to track her down soon.\x02\x03",

            "(I need to head to the landing port...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A12")

    label("loc_4E15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 3)), scpexpr(EXPR_END)), "loc_527B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 6)), scpexpr(EXPR_END)), "loc_4ED1")

    ChrTalk(    #210
        0x8,
        (
            "#760FSweets that disappear if you leave them alone...\x02\x03",

            "It might be one of the sweets\x01",
            "sold by a street vendor.\x02\x03",

            "Candy, popcorn, crepes, ice cream...\x02\x03",

            "That's about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5278")

    label("loc_4ED1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5152")

    ChrTalk(    #211
        0x8,
        "#760FEstelle, have you found Renne yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x101,
        "#1000FNo, not yet.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk About Renne\x01",      # 0
            "Don't\x01",                 # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50C7")

    AnonymousTalk(    #213
        "\x07\x05Estelle explained the series of events to Elnan.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #214
        0x8,
        (
            "#764FSweets that disappear if you leave them alone...\x02\x03",

            "#760FWhen you say 'sweets,' there are a lot of\x01",
            "sweet shops on the streets of Grancel. \x02\x03",

            "It might be one of the sweets\x01",
            "sold by a street vendor.\x02\x03",

            "Candy, popcorn, crepes, ice cream...\x02\x03",

            "#761FThat's about it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1686)
    Jump("loc_514C")

    label("loc_50C7")

    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #215
        0x8,
        (
            "#761F...Still, this girl is good at hiding.\x02\x03",

            "#760FI can see why you had a hard time\x01",
            "finding her in the villa.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_514C")

    OP_A2(0x3)
    Jump("loc_5278")

    label("loc_5152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51CD")

    ChrTalk(    #216
        0x8,
        (
            "#761FStill, this girl is good at hiding.\x02\x03",

            "#760FI can see why you had a hard time\x01",
            "finding her in the villa.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5278")

    label("loc_51CD")


    ChrTalk(    #217
        0x8,
        (
            "#760FSweets that disappear if you leave them alone...\x02\x03",

            "It might be one of the sweets\x01",
            "sold by a street vendor.\x02\x03",

            "Candy, popcorn, crepes, ice cream...\x02\x03",

            "That's about it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5278")

    Jump("loc_5A12")

    label("loc_527B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 2)), scpexpr(EXPR_END)), "loc_561B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 5)), scpexpr(EXPR_END)), "loc_530B")

    ChrTalk(    #218
        0x8,
        (
            "#760FA 'bitter, spicy, delicious' store? Hmm...\x02\x03",

            "Actually, didn't you say an acquaintance\x01",
            "treated you to something spicy?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5618")

    label("loc_530B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_554E")

    ChrTalk(    #219
        0x8,
        "#760FHow about it, was Renne there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x101,
        "#1007FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk About Renne\x01",      # 0
            "Don't\x01",                 # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54D9")

    AnonymousTalk(    #221
        "\x07\x05Estelle explained the series of events to Elnan.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #222
        0x8,
        (
            "#764FA 'bitter, spicy, delicious' store? Hmm...\x02\x03",

            "#760FActually, Estelle... \x02\x03",

            "Didn't you say an acquaintance treated you\x01",
            "to something spicy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#1011FAh, you mean Nial.\x02\x03",

            "#1015FThat was at some cafe or bar somewhere,\x01",
            "I think...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1685)
    Jump("loc_5548")

    label("loc_54D9")

    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #224
        0x8,
        (
            "#761FTo be able to run from a bracer...\x01",
            "Renne is quite good.\x02\x03",

            "#760FEveryone, good luck.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5548")

    OP_A2(0x3)
    Jump("loc_5618")

    label("loc_554E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_559B")

    ChrTalk(    #225
        0x8,
        (
            "#761FTo be able to run from a bracer...\x01",
            "Renne is quite good.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5618")

    label("loc_559B")


    ChrTalk(    #226
        0x8,
        (
            "#760FA bitter, spicy, delicious store... Hmm.\x02\x03",

            "Actually, didn't you say an acquaintance\x01",
            "treated you to something spicy?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5618")

    Jump("loc_5A12")

    label("loc_561B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 1)), scpexpr(EXPR_END)), "loc_5980")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 4)), scpexpr(EXPR_END)), "loc_569B")

    ChrTalk(    #227
        0x8,
        (
            "#760FIf it's a building related to fish,\x01",
            "I have an idea.\x02\x03",

            "Check the building next to our guildhouse here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_597D")

    label("loc_569B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58D0")

    ChrTalk(    #228
        0x8,
        "#760FOh, were you able to find Renne?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x101,
        "#1007FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk About Renne\x01",      # 0
            "Don't\x01",                 # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5864")

    AnonymousTalk(    #230
        "\x07\x05Estelle explained the series of events to Elnan.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #231
        0x8,
        (
            "#764FA 'colorless fish,' is it?\x02\x03",

            "#760FI don't know about the 'colorless' bit,\x01",
            "but...\x02\x03",

            "If it's a building related to fish,\x01",
            "I have one idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        "#1004FReally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x8,
        (
            "#761FYes, check the building next to our\x01",
            "guildhouse here.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1684)
    Jump("loc_58CA")

    label("loc_5864")

    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #234
        0x8,
        (
            "#762FIt seems you're having trouble.\x02\x03",

            "Where could Renne have gone, I wonder...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58CA")

    OP_A2(0x3)
    Jump("loc_597D")

    label("loc_58D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_590E")

    ChrTalk(    #235
        0x8,
        "#762FWhere could Renne have gone, I wonder...\x02",
    )

    CloseMessageWindow()
    Jump("loc_597D")

    label("loc_590E")


    ChrTalk(    #236
        0x8,
        (
            "#760FIf it's a building related to fish,\x01",
            "I have an idea.\x02\x03",

            "Check the building next to our guildhouse here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_597D")

    Jump("loc_5A12")

    label("loc_5980")


    ChrTalk(    #237
        0x8,
        (
            "#760FI'll contact the branches in the other\x01",
            "regions and swap information about the\x01",
            "Intelligence Division.\x02\x03",

            "Estelle, please bring back Renne.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A12")

    Jump("loc_5DFC")

    label("loc_5A15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 3)), scpexpr(EXPR_END)), "loc_5A1F")
    Jump("loc_5DFC")

    label("loc_5A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BA8")

    ChrTalk(    #238
        0x8,
        "#760FOh, Estelle. How'd questioning go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        (
            "#1015FEr... I've asked with the castle and\x01",
            "the embassies.\x02\x03",

            "#1000FNow I just need to check in with\x01",
            "Nial at the Liberl News.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5B48")

    ChrTalk(    #240
        0x8,
        (
            "#760FWell, then, once that's done, come back\x01",
            "and report.\x02\x03",

            "Scherazard should be back soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BA2")

    label("loc_5B48")


    ChrTalk(    #241
        0x8,
        (
            "#760FWell, then, once that's done, come back\x01",
            "and report.\x02\x03",

            "Agate should be back soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BA2")

    OP_A2(0x3)
    Jump("loc_5C79")

    label("loc_5BA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5C13")

    ChrTalk(    #242
        0x8,
        (
            "#760FOnce you're done inquiring with\x01",
            "the Liberl News come back.\x02\x03",

            "Agate should be back soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C79")

    label("loc_5C13")


    ChrTalk(    #243
        0x8,
        (
            "#760FOnce you're done inquiring with\x01",
            "the Liberl News come back.\x02\x03",

            "Scherazard should be back soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C79")

    Jump("loc_5DFC")

    label("loc_5C7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_5D6F")

    ChrTalk(    #244
        0x8,
        (
            "#760FAs we discussed, Estelle, please go to\x01",
            "the Imperial and Republican embassies,\x01",
            "Grancel Castle, and the Liberl News.\x02\x03",

            "For the embassies, Zin, Olivier,\x01",
            "we'll be counting on you.\x02\x03",

            "As for Grancel Castle, Princess, if you would.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DFC")

    label("loc_5D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C2, 7)), scpexpr(EXPR_END)), "loc_5D79")
    Jump("loc_5DFC")

    label("loc_5D79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_5DFC")

    ChrTalk(    #245
        0x8,
        (
            "#760FApparently a butler named Raymond is\x01",
            "keeping an eye on the lost child.\x02\x03",

            "Once you get to royal villa, ask for him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DFC")

    TalkEnd(0x8)
    Return()

    # Function_13_463A end

    def Function_14_5E00(): pass

    label("Function_14_5E00")

    TalkBegin(0xFE)

    ChrTalk(    #246
        0xFE,
        "S-Suddenly these red-armored guys attacked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xFE,
        (
            "No matter how used to trouble I am,\x01",
            "this is pretty startling.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_5E00 end

    def Function_15_5E7B(): pass

    label("Function_15_5E7B")

    TalkBegin(0xFE)

    ChrTalk(    #248
        0xFE,
        "*sob* *sob* I can't stop shaking...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        "Those people, they were really...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_5E7B end

    def Function_16_5ED2(): pass

    label("Function_16_5ED2")

    TalkBegin(0xFE)

    ChrTalk(    #250
        0xFE,
        "Wh-Who are they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "Seemed like these four guys in weird\x01",
            "clothes were commanding them, but...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_5ED2 end

    def Function_17_5F3E(): pass

    label("Function_17_5F3E")

    TalkBegin(0xFE)

    ChrTalk(    #252
        0xFE,
        "First orbments stop working and now this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        "It's too terrible...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_5F3E end

    def Function_18_5F90(): pass

    label("Function_18_5F90")

    TalkBegin(0xFE)

    ChrTalk(    #254
        0xFE,
        "They're not troops from the Empire, are they?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        (
            "Stepping on the non-aggression pact we just\x01",
            "signed and doing this... The only people who'd\x01",
            "have the gall are the Imperials!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_5F90 end

    def Function_19_604B(): pass

    label("Function_19_604B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C9, 7)), scpexpr(EXPR_END)), "loc_60F6")

    ChrTalk(    #256
        0xFE,
        (
            "A-Among the people who attacked us,\x01",
            "there was a girl in white clothes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        "The soldiers were done in before I could blink...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #258
        0xFE,
        "D-Did I imagine it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6159")

    label("loc_60F6")


    ChrTalk(    #259
        0xFE,
        (
            "Owwww... Tripped and hurt myself when\x01",
            "I was running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        "I wonder if Dad and Mom are okay...\x02",
    )

    CloseMessageWindow()

    label("loc_6159")

    TalkEnd(0xFE)
    Return()

    # Function_19_604B end

    def Function_20_615D(): pass

    label("Function_20_615D")

    TalkBegin(0xFE)

    ChrTalk(    #261
        0xFE,
        "The Royal Army people brought us here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        "I hope they're okay.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_615D end

    def Function_21_61AA(): pass

    label("Function_21_61AA")

    TalkBegin(0xFE)

    ChrTalk(    #263
        0xFE,
        "Why did those people attack us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        "We haven't been bad or anything...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_61AA end

    def Function_22_61FE(): pass

    label("Function_22_61FE")

    TalkBegin(0xFE)

    ChrTalk(    #265
        0xFE,
        "Damn it! What's gonna happen to my shop?!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_61FE end

    def Function_23_6234(): pass

    label("Function_23_6234")

    TalkBegin(0xFE)

    ChrTalk(    #266
        0xFE,
        (
            "I had to drag Zacharias out of there by force.\x01",
            "The idiot wanted to stay behind in the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        "That was a close call.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_6234 end

    def Function_24_62B9(): pass

    label("Function_24_62B9")

    TalkBegin(0xFE)

    ChrTalk(    #268
        0xFE,
        (
            "The soldiers of the Royal Army taken down by\x01",
            "just four people... I can't believe it...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_62B9 end

    def Function_25_631C(): pass

    label("Function_25_631C")

    TalkBegin(0xFE)

    ChrTalk(    #269
        0xFE,
        (
            "Ah, the capital...\x01",
            "The capital is burning...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_25_631C end

    def Function_26_6355(): pass

    label("Function_26_6355")

    TalkBegin(0xFE)

    ChrTalk(    #270
        0xFE,
        "One of the soldiers told me to evacuate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0xFE,
        "I wonder if that soldier is okay...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_6355 end

    def Function_27_63B3(): pass

    label("Function_27_63B3")

    TalkBegin(0xFE)

    ChrTalk(    #272
        0xFE,
        "Th-This is horrible... Who are they?!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_27_63B3 end

    def Function_28_63E5(): pass

    label("Function_28_63E5")

    TalkBegin(0xFE)

    ChrTalk(    #273
        0xFE,
        "I wonder if Lloyd's okay over in Bose...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_28_63E5 end

    def Function_29_641A(): pass

    label("Function_29_641A")

    TalkBegin(0xFE)

    ChrTalk(    #274
        0xFE,
        "My darling, are you okay?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_29_641A end

    def Function_30_6440(): pass

    label("Function_30_6440")

    TalkBegin(0xFE)

    ChrTalk(    #275
        0xFE,
        (
            "I'm fine, dearest. I'm sure the Aidios or\x01",
            "the queen will do something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        "We simply have to endure it...\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_30_6440 end

    def Function_31_64B7(): pass

    label("Function_31_64B7")

    TalkBegin(0xFE)

    ChrTalk(    #277
        0xFE,
        (
            "H-Help, please! The capital...\x01",
            "The capital is...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_31_64B7 end

    def Function_32_64F4(): pass

    label("Function_32_64F4")

    TalkBegin(0xFE)

    ChrTalk(    #278
        0xFE,
        (
            "The four who commanded the red\x01",
            "troops headed to the castle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "I wonder if the queen and Princess\x01",
            "Klaudia are all right...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_64F4 end

    def Function_33_657F(): pass

    label("Function_33_657F")

    TalkBegin(0xFE)

    ChrTalk(    #280
        0xFE,
        "Sweet Aidios... What the heck is going on?!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_657F end

    def Function_34_65B7(): pass

    label("Function_34_65B7")

    TalkBegin(0xFE)

    ChrTalk(    #281
        0xFE,
        "Is this... Are we at war again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "Even though we just signed a non-aggression\x01",
            "pact...\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_34_65B7 end

    def Function_35_661C(): pass

    label("Function_35_661C")

    TalkBegin(0xFE)

    ChrTalk(    #283
        0xFE,
        (
            "Even should our building burn, the\x01",
            "Fisherman's Guild will never die!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xFE,
        (
            "As long as the passion for fishing in our hearts\x01",
            "burns on, our dream lives on!\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_35_661C end

    def Function_36_66C1(): pass

    label("Function_36_66C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67D1")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Gathered all of Gambler Jack\x01",           # 0
            "Didn't gather all of Gambler Jack\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_673F"),
        (1, "loc_6788"),
        (SWITCH_DEFAULT, "loc_67D1"),
    )


    label("loc_673F")

    OP_3E(0x23A, 1)
    OP_3E(0x23B, 1)
    OP_3E(0x23C, 1)
    OP_3E(0x23D, 1)
    OP_3E(0x23E, 1)
    OP_3E(0x23F, 1)
    OP_3E(0x240, 1)
    OP_3E(0x241, 1)
    OP_3E(0x242, 1)
    OP_3E(0x243, 1)
    OP_3E(0x244, 1)
    OP_3E(0x245, 1)
    OP_3E(0x246, 1)
    OP_3E(0x247, 1)
    Jump("loc_67D1")

    label("loc_6788")

    OP_3F(0x23A, 1)
    OP_3F(0x23B, 1)
    OP_3F(0x23C, 1)
    OP_3F(0x23D, 1)
    OP_3F(0x23E, 1)
    OP_3F(0x23F, 1)
    OP_3F(0x240, 1)
    OP_3F(0x241, 1)
    OP_3F(0x242, 1)
    OP_3F(0x243, 1)
    OP_3F(0x244, 1)
    OP_3F(0x245, 1)
    OP_3F(0x246, 1)
    OP_3F(0x247, 1)
    Jump("loc_67D1")

    label("loc_67D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x23A, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x23B, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23C, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23D, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23E, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x23F, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x240, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x241, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x242, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x243, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x244, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x245, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x246, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x247, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_684E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_684E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x218, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6846")
    OP_A2(0x10C3)
    Call(1, 38)
    TalkEnd(0x2A)
    Return()

    label("loc_6846")

    Call(1, 39)
    TalkEnd(0x2A)
    Return()

    label("loc_684E")


    ChrTalk(    #285
        0xFE,
        (
            "When I was out shopping, suddenly\x01",
            "I got told to evacuate...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        (
            "Well, at times like these there's no point in\x01",
            "running around. Best just to read a book and\x01",
            "calm down.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_36_66C1 end

    def Function_37_68FE(): pass

    label("Function_37_68FE")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6923")
    Call(0, 38)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_691F")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_6923")

    label("loc_691F")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_6923")

    OP_6D(-5500, 0, 20, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -2600, 0, 560, 270)
    SetChrPos(0xC, -1280, 0, 980, 270)
    SetChrPos(0xA, -2600, 0, 1590, 270)
    SetChrPos(0x9, -2600, 0, -590, 270)
    SetChrPos(0xE, -1680, 0, 2260, 270)
    SetChrPos(0xB, -360, 0, 1500, 270)
    SetChrPos(0xD, -1240, 0, -60, 270)
    SetChrPos(0x10, -1480, 0, -1090, 270)
    SetChrPos(0x8, -5700, 0, -130, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x109, 0x80)
    OP_4A(0xA, 255)
    OP_4A(0x9, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0x8, 255)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #287
        0x8,
        (
            "#764F#6PI see...\x02\x03",

            "#760FYes... Understood.\x02\x03",

            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(300)
    OP_8C(0x8, 45, 400)

    def lambda_6AF6():
        OP_6D(-3320, 0, 1160, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_6AF6)
    OP_8E(0x8, 0xFFFFEE80, 0x0, 0x3C0, 0x5DC, 0x0)
    OP_8C(0x8, 90, 400)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #288
        0x101,
        "#1026FElnan, how'd it go?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x8,
        (
            "#760FIt seems as though Ms. Amalthea is willing\x01",
            "to answer questions.\x02\x03",

            "The army said they would contact the guild\x01",
            "when they had something useful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x101,
        "#1025FWell, that's good...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6CB1")

    ChrTalk(    #291
        0x9,
        (
            "#027F#5PIt's hard to believe they actually\x01",
            "got her to talk.\x02\x03",

            "I hope they didn't do anything TOO unpleasant\x01",
            "to her. She still deserves a little\x01",
            "unpleasantness, mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6D26")

    label("loc_6CB1")


    ChrTalk(    #292
        0xA,
        (
            "#051FHeh, so that stubborn ol' mule is finally\x01",
            "willing to spill her guts?\x02\x03",

            "Wonder what kind of trick they used?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D26")


    ChrTalk(    #293
        0xE,
        (
            "#074F#4PWe can leave that to the army, I think.\x02\x03",

            "#072FWe have some things of our own to talk over.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x8,
        (
            "#764FTrue enough...\x02\x03",

            "#760FWell, then! First, allow me to provide you\x01",
            "with your pay for this mission.\x02\x03",

            "This includes everything for all the small,\x01",
            "related tasks you had to undertake as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8D, 0x4, 0x20)
    OP_28(0x89, 0x4, 0x10)
    OP_AF(0xCD, 0x89)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E71")
    OP_2B(0x8C, 0x1)

    label("loc_6E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E7E")
    OP_2B(0x8C, 0x1)

    label("loc_6E7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6E8B")
    OP_2B(0x8C, 0x1)

    label("loc_6E8B")

    OP_28(0x8C, 0x4, 0x10)
    OP_AF(0xCD, 0x8C)
    Sleep(100)
    OP_28(0x8E, 0x4, 0x10)
    OP_AF(0xCD, 0x8E)
    Sleep(100)
    OP_28(0x8A, 0x4, 0x10)
    OP_28(0x8A, 0x4, 0x20)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #295
        0xC,
        (
            "#043FSay... Estelle.\x02\x03",

            "Do you really think Renne could be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x101,
        "#1003F#6PYeah.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    def lambda_6F21():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6F21)

    def lambda_6F2F():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6F2F)

    def lambda_6F3D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6F3D)

    def lambda_6F4B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6F4B)

    def lambda_6F59():
        TurnDirection(0xFE, 0x10, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6F59)

    def lambda_6F67():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6F67)
    Sleep(500)

    ChrTalk(    #297
        0x101,
        (
            "#1025F#6PShe named herself one of the Enforcers,\x01",
            "the...'Angel of Slaughter.'\x02\x03",

            "If she's calling herself that, there's\x01",
            "not really any doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xC,
        "#049FThere isn't, is there...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xD,
        "#063F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x10,
        (
            "#1317F#5PS-Seriously? A little girl like that is one of\x01",
            "the society's crazy murder goons?\x02\x03",

            "And aren't Enforcers supposed to be able\x01",
            "to, like, break you with their pinkie?\x02\x03",

            "You really don't think they're pulling\x01",
            "some kind of trick, here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        (
            "#1003F#6PNo, I'm pretty sure she's telling the truth.\x02\x03",

            "Joshua... Joshua was about Renne's age when\x01",
            "Dad rescued him from the society, and he told\x01",
            "me he was made to kill way before then, even.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x10,
        "#813F#5PYou're kidding me...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7322")

    ChrTalk(    #303
        0x9,
        (
            "#522F#5PEither way, Renne really pulled the wool\x01",
            "over our eyes.\x02\x03",

            "It seems she's the one who gave Amalthea\x01",
            "that Gospel and suggested they try\x01",
            "another coup with that tank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xA,
        (
            "#555FSeems like she sent all those letters, too.\x02\x03",

            "I just don't get it, though. Why?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741B")

    label("loc_7322")


    ChrTalk(    #305
        0xA,
        (
            "#552FEither way, that girl pulled one over on us.\x02\x03",

            "She probably gave Amalthea the Gospel\x01",
            "and suggested they get crazy with that\x01",
            "damned tank...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0x9,
        (
            "#022F#5PShe seems to have been the source\x01",
            "of the letters, as well.\x02\x03",

            "I can't fathom WHY, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_741B")


    ChrTalk(    #307
        0x101,
        (
            "#1015F#6PI'm just guessing here, but...\x02\x03",

            "Maybe she thought it'd be fun?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_75BF")

    ChrTalk(    #308
        0xA,
        "#052FFun?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x101,
        (
            "#1003F#6PRenne put this experiment of hers together\x01",
            "as a 'tea party', right?\x02\x03",

            "And she set things up so that lots of people,\x01",
            "especially us, would participate...\x01",
            "sorta like an invitation.\x02\x03",

            "That's kinda the feeling I get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xA,
        (
            "#055FMan, that's crazy.\x02\x03",

            "I mean, yeah, we're here because of\x01",
            "those letters, sure, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7734")

    label("loc_75BF")


    ChrTalk(    #311
        0x9,
        "#023F#5PHm...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0x101,
        (
            "#1003F#6PRenne put this experiment of hers together\x01",
            "as a 'tea party,' right?\x02\x03",

            "And she set things up so that lots of people,\x01",
            "especially us, would participate...\x01",
            "sorta like an invitation.\x02\x03",

            "That's kinda the feeling I get.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x9,
        (
            "#522F#5PFor the love of Aidios...\x02\x03",

            "We are here thanks to those letters,\x01",
            "but...to orchestrate it all just for her\x01",
            "amusement?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7734")


    ChrTalk(    #314
        0xB,
        (
            "#035FI could easily believe our little kitten\x01",
            "is capable of such guile.\x02\x03",

            "#030FShe was, after all, very clever in\x01",
            "balancing the amount of sleeping\x01",
            "drug she gave to us, as well.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_786C")

    ChrTalk(    #315
        0xA,
        (
            "#057FMeaning we'd arrive at the docks at just\x01",
            "the right time...\x02\x03",

            "She really did put us on some damn\x01",
            "puppet strings.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_78E2")

    label("loc_786C")


    ChrTalk(    #316
        0x9,
        (
            "#022F#5PWhich means she wanted us to arrive at\x01",
            "the docks at just the right time.\x02\x03",

            "That takes serious planning...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78E2")


    ChrTalk(    #317
        0x101,
        (
            "#1015F#6PSo she's definitely the one\x01",
            "who put you guys to sleep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xC,
        (
            "#043FAlmost certainly.\x02\x03",

            "It was just after I ate one of those cookies\x01",
            "Renne got for us at the department store\x01",
            "that my mind went fuzzy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xE,
        (
            "#074F#4PThat was one hell of a failure on our\x01",
            "part.\x02\x03",

            "If she'd used poison, most of us would be\x01",
            "having this conversation at the side of\x01",
            "She Who Dwells Above.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0x101,
        "#1026F#6PYeah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0x8,
        (
            "#765FThe failure there is entirely my own.\x02\x03",

            "As the person in charge of the mission\x01",
            "and the guildhouse, I should have been\x01",
            "far more cautious.\x02\x03",

            "Please, forgive me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #322
        0x101,
        (
            "#1025F#6POh, c'mon, Elnan.\x02\x03",

            "#1007FEveryone's got a bit of blame for this.\x02\x03",

            "I don't think any one of us realized just\x01",
            "how far the society was willing to go...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xD,
        (
            "#561F#2PYeah... That giant archaism...\x02\x03",

            "Even Grandpa would have a really hard\x01",
            "time making something like that.\x02\x03",

            "#062FAnd even then, to...to make it move\x01",
            "like that!\x02\x03",

            "And... And Renne...\x02\x03",

            "#562F...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #324
        0x101,
        "#1026F#6POh, Tita...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #325
        0x101,
        (
            "#1018F#6PC'mon! Cheer up!#2S\x02\x03",

            "Next time we see her, I'm dragging her\x01",
            "out of the society, feet first!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #326
        0xD,
        "#064F#2PWhaaaat...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7D63")

    ChrTalk(    #327
        0xA,
        "#055FWhoa, hang on!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7D7D")

    label("loc_7D63")


    ChrTalk(    #328
        0x9,
        "#023F#5PUm, Estelle?\x02",
    )

    CloseMessageWindow()

    label("loc_7D7D")


    ChrTalk(    #329
        0x101,
        (
            "#1006F#6PFive years ago, Dad rescued Joshua from the\x01",
            "clutches of Ouroboros, and we taught him what\x01",
            "it was to be happy.\x02\x03",

            "I'm Cassius Bright's daughter, so you know what?\x01",
            "I can totally do the same thing!\x02\x03",

            "I'm going to drag Renne out of the Society of\x01",
            "Ouroboros by the scruff of her neck if I have to!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xD,
        (
            "#560F#2PEstelle...\x02\x03",

            "#067FYeah! Yeah, we will!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xC,
        "#048FHaha... That's our Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0x10,
        "#811F#5PYeah! That's the spirit!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0xB,
        "#031FAh! Such indomitable optimism!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #334
        0xA,
        (
            "#556FHeh... You're makin' it sound\x01",
            "easy, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x9,
        "#021F#5PThat's just how our Estelle is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xE,
        (
            "#070F#4PThink even your father would be bowled\x01",
            "over by that much optimism.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x109, -20, -500, -7250, 0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #337
        0x109,
        "Man's Voice",
        (
            "#2PMaaaan, I'll say! I'm practically head over\x01",
            "heels for you at this point!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_80A3():
        OP_6D(-1820, 0, -1810, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_80A3)

    def lambda_80BB():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80BB)

    def lambda_80C9():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_80C9)

    def lambda_80D7():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_80D7)

    def lambda_80E5():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_80E5)

    def lambda_80F3():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_80F3)

    def lambda_8101():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8101)

    def lambda_810F():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_810F)

    def lambda_811D():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_811D)

    def lambda_812B():
        TurnDirection(0xFE, 0x109, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_812B)

    def lambda_8139():

        label("loc_8139")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_8139")

    QueueWorkItem2(0x101, 1, lambda_8139)

    def lambda_814A():

        label("loc_814A")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_814A")

    QueueWorkItem2(0xA, 1, lambda_814A)

    def lambda_815B():

        label("loc_815B")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_815B")

    QueueWorkItem2(0x9, 1, lambda_815B)

    def lambda_816C():

        label("loc_816C")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_816C")

    QueueWorkItem2(0xC, 1, lambda_816C)

    def lambda_817D():

        label("loc_817D")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_817D")

    QueueWorkItem2(0xD, 1, lambda_817D)

    def lambda_818E():

        label("loc_818E")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_818E")

    QueueWorkItem2(0xE, 1, lambda_818E)

    def lambda_819F():

        label("loc_819F")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_819F")

    QueueWorkItem2(0x8, 1, lambda_819F)

    def lambda_81B0():

        label("loc_81B0")

        TurnDirection(0xFE, 0x109, 400)
        OP_48()
        Jump("loc_81B0")

    QueueWorkItem2(0x10, 1, lambda_81B0)
    ClearChrFlags(0x109, 0x80)
    Sleep(1000)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_81D6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_81D6)

    def lambda_81E8():
        OP_8E(0xFE, 0xFFFFFFEC, 0xFFFFFF06, 0xFFFFE958, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_81E8)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #338
        0x101,
        "#1004F#4POh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x8,
        "#761F#6PFather Kevin! We've been waiting for you.\x02",
    )

    CloseMessageWindow()

    def lambda_8251():
        OP_6D(-2800, 0, 240, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8251)

    def lambda_8269():
        OP_8E(0xFE, 0xFFFFF8B2, 0x0, 0xFFFFF74A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8269)
    WaitChrThread(0x109, 0x1)
    TurnDirection(0x109, 0x101, 400)
    Sleep(500)

    ChrTalk(    #340
        0x109,
        (
            "#1068F#5PYeah, sorry I'm late.\x02\x03",

            "Archbishop Currant was, uh, not exactly\x01",
            "thrilled with me.\x02\x03",

            "He got on a really good lecturin' tear,\x01",
            "so he held me back a bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_62(0x109, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #341
        0x109,
        (
            "#1064F#5PUh, what's up? Do I have egg on my\x01",
            "face or something?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)

    ChrTalk(    #342
        0x101,
        (
            "#1019F#4POkay, so you aren't an Ouroboros skull\x01",
            "eater or whatever. But you never did\x01",
            "answer my question.\x02\x03",

            "Who the hell are you REALLY, Kevin?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_84B6")

    ChrTalk(    #343
        0x9,
        (
            "#026F#6PThat IS a good question.\x02\x03",

            "#027FYou never quite managed to give us a straight\x01",
            "answer either, 'Father.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8518")

    label("loc_84B6")


    ChrTalk(    #344
        0xA,
        (
            "#051FHeh, good point.\x02\x03",

            "You've been kinda good at dodging\x01",
            "that particular question, 'Father.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8518")


    ChrTalk(    #345
        0x10,
        (
            "#816F#5PYou aren't really just some wandering\x01",
            "priest, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x109,
        (
            "#1065F#5PI did promise I'd explain everything to you,\x01",
            "Estelle...right. Allow me to re-introduce myself.\x02\x03",

            "#1060FMy name IS Kevin Graham, and I AM a priest...\x01",
            "but I'm a priest of the Gralsritter of the\x01",
            "Septian Church.\x02\x03",

            "A pleasure to properly meet you all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x101,
        "#1002F#4PA 'Gralsritter'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xB,
        (
            "#033F#4POh...? Beg your pardon, but...\x02\x03",

            "#030FI would never have imagined someone as young\x01",
            "as you to be one of the holy Gralsritter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x101,
        "#1004F#6POlivier, you know who they are?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0xB,
        (
            "#035F#4PYou're aware that the church has a duty to take\x01",
            "custody of all ancient Zemurian artifacts, yes?\x02\x03",

            "Investigation and retrieval of such items is\x01",
            "the work of an arm of the church called the\x01",
            "'Gralsritter'...the 'Grail Knights.'\x02\x03",

            "#030FTheir member list is not public knowledge...\x01",
            "but they are said to be artifact experts and\x01",
            "combat masters, to a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x109,
        (
            "#1064F#5PDang, you, uh, know a lot about us!\x02\x03",

            "#1066FI dunno if you'd call me a 'master,' though.\x02\x03",

            "I'm kinda the fresh-faced new guy on the team.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x101,
        (
            "#1015F#4PArtifact retrieval...?\x02\x03",

            "#1004FOh! Now I get it!\x01",
            "That's why you had Mayor Dalmore's staff!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x109,
        (
            "#1060F#5PYeah, the Royal Army gave me that for\x01",
            "safekeeping when I first came to Liberl.\x02\x03",

            "Liberl and the church have an agreement\x01",
            "to hand over all artifacts found, y'see.\x02\x03",

            "#1068FThe whole reason Archbishop Currant was,\x01",
            "uh, kind of ticked off is because I broke\x01",
            "that one, mind you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x101,
        (
            "#1025F#4PNow I see...\x02\x03",

            "Oh, I hope he wasn't too angry.\x01",
            "You really saved us, and there\x01",
            "wasn't any other way!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8B63")

    ChrTalk(    #355
        0x9,
        "#020F#6PYes, we hardly had time to be picky.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8BA5")

    label("loc_8B63")


    ChrTalk(    #356
        0xA,
        (
            "#051FYeah, we didn't have time to be what\x01",
            "I'd call 'choosy.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8BA5")


    ChrTalk(    #357
        0x109,
        (
            "#1066F#5PHeh! Thanks for that.\x02\x03",

            "#1060FAnyway, hopefully we can work together a\x01",
            "bit more in the future, eh?\x02\x03",

            "If you learn anything new about\x01",
            "Ouroboros, let's swap info again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x101,
        (
            "#1004F#4PSay, how DO you know about\x01",
            "Ouroboros, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x109,
        (
            "#1065F#5PWell, the main reason I came to Liberl was\x01",
            "to investigate the society. Let's just say\x01",
            "we've known about them for a while now.\x02\x03",

            "#1063FAnd to be more precise... I came to investigate\x01",
            "the Shining Ring, the Aureole, that they seem\x01",
            "to be after.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x101,
        "#1020F#4P*gasp*!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x9,
        "#023F#6PThe Aureole...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0xC,
        (
            "#047F#4POne of the holy Sept-Terrions granted to the\x01",
            "ancient Zemurians by Aidios Herself...\x02\x03",

            "#042FThe legendary artifact that we thought\x01",
            "slept beneath Grancel Castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x109,
        (
            "#1063F#5PYeah, exactly.\x02\x03",

            "#1065FThere've been some people asking a whooooole\x01",
            "lotta specific questions about the Sept-Terrions\x01",
            "across the entire continent.\x02\x03",

            "That kinda caught the church's eye,\x01",
            "lemme tell you.\x02\x03",

            "#1060FAnd then we learned about the whole hullabaloo\x01",
            "with the ruins beneath Grancel Castle and the\x01",
            "Aureole during the coup.\x02\x03",

            "So they sent me, the fresh-faced, and, uh,\x01",
            "expendable, new guy to see what's what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0xC,
        "#542F#4PSo that's the story.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x101,
        (
            "#1002F#4PSo, hang on, you think the Aureole really\x01",
            "is in Liberl?\x02\x03",

            "When we didn't find it beneath the castle,\x01",
            "I thought it was just a legend after all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_913A")

    ChrTalk(    #366
        0xA,
        (
            "#555FDo we even know what the hell the thing is,\x01",
            "beyond the whole 'Shining Ring' deal?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91A2")

    label("loc_913A")


    ChrTalk(    #367
        0x9,
        (
            "#022F#6PDo we even have any idea what it is,\x01",
            "beyond the legendary description of\x01",
            "a 'Shining Ring'?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91A2")


    ChrTalk(    #368
        0x109,
        (
            "#1065F#5PFigurin' out the truth of the thing is\x01",
            "part of my job.\x02\x03",

            "#1060FSo, yeah. I wanted to come by today and\x01",
            "explain what's up.\x02\x03",

            "If anything more happens, what say we\x01",
            "work together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x101,
        (
            "#1015F#4PNow I get it...\x02\x03",

            "#1006FYeah, all right. I'd be happy to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xE,
        "#070FIt'd be a big help for us, too.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_933F")

    ChrTalk(    #371
        0x9,
        (
            "#027F#6PThis may just be the hand of fate at work.\x01",
            "If something happens, do contact us, Father.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_938E")

    label("loc_933F")


    ChrTalk(    #372
        0xA,
        (
            "#051FYeah, I'm down with that idea.\x01",
            "If anything comes up, give us a buzz.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_938E")


    ChrTalk(    #373
        0x109,
        (
            "#1062F#5PFantastico!\x02\x03",

            "#1061FAll right, think I gotta go get my ear\x01",
            "chewed off some more...\x02\x03",

            "See ya, folks!\x02",
        )
    )

    CloseMessageWindow()
    OP_B7(0x8)
    OP_8C(0x109, 135, 400)

    def lambda_940D():
        OP_6D(-1820, 0, -1810, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_940D)
    OP_8E(0x109, 0xFFFFFF92, 0xFFFFFF06, 0xFFFFE7AA, 0x7D0, 0x0)

    def lambda_9439():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9439)

    def lambda_944B():
        OP_8E(0xFE, 0xFFFFFFF6, 0xFFFFFE0C, 0xFFFFE3AE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_944B)
    WaitChrThread(0x109, 0x1)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    SetChrFlags(0x109, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xC, 0x1)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0x8, 0x1)

    def lambda_949F():
        OP_6D(-3320, 0, 1160, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_949F)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #374
        0x101,
        "#1007F#6PAaaand he's gone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x9,
        (
            "#027F#5PHe's quite good at putting people off-balance...\x01",
            "in a different way than Olivier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xB,
        (
            "#035F#2PHeh. If you ask me, he still needs training.\x02\x03",

            "He could stand to be a bit more elegant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #377
        0x101,
        (
            "#1019F#6PYou realize there is exactly zero elegance\x01",
            "in your stream of constant nonsense, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xC,
        (
            "#049F#2PStill, all this interest in the Aureole...\x02\x03",

            "#043FDo you think this has something to do with\x01",
            "the Gospel experiments the society's been\x01",
            "performing?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 400)
    Sleep(400)

    ChrTalk(    #379
        0x8,
        (
            "#764FFrom what we've heard, it is a\x01",
            "definite possibility.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_96EE():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_96EE)

    def lambda_96FC():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_96FC)
    Sleep(50)

    def lambda_970F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_970F)

    def lambda_971D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_971D)
    Sleep(50)

    def lambda_9730():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9730)

    def lambda_973E():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_973E)
    Sleep(50)

    def lambda_9751():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9751)

    def lambda_975F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_975F)
    Sleep(500)

    ChrTalk(    #380
        0x8,
        (
            "#762FOn that note, that's three of Liberl's\x01",
            "regions that have suffered Gospel-related\x01",
            "experiments now.\x02\x03",

            "I fear that neither Rolent nor Bose will\x01",
            "avoid their touch at this point.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x101,
        (
            "#1002FGood point.\x02\x03",

            "It seems like things are pretty calm here, now.\x01",
            "You think it's time for us to move on?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_98D6")

    ChrTalk(    #382
        0xA,
        (
            "#053FMeaning we should get to either Rolent\x01",
            "or Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_992B")

    label("loc_98D6")


    ChrTalk(    #383
        0x9,
        (
            "#020F#5PWhich means we should get to either Rolent\x01",
            "or Bose as soon as we can...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_992B")

    Sleep(100)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC3, 0x1, 0x64)
    Sleep(500)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 270, 400)

    def lambda_99AC():
        OP_6D(-5500, 0, 20, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_99AC)
    OP_8F(0x8, 0xFFFFE9BC, 0x0, 0xFFFFFF7E, 0x7D0, 0x0)
    Sleep(400)
    WaitChrThread(0x8, 0x2)
    OP_23(0xC3)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\\\mp001_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -6030, 2000, -270, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)

    ChrTalk(    #384
        0x8,
        (
            "#760F#6PHello, yes, this is the Grancel branch\x01",
            "of the Bracer Guild.\x02\x03",

            "...\x02\x03",

            "#763FWhat...? Oh, I see.\x02\x03",

            "#764F...Understood. We'll be on our guard.\x02\x03",

            "Yes, take care.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x1, 0x0)
    Sleep(500)

    ChrTalk(    #385
        0x9,
        "#020F#2PSomething going on, Elnan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0xA,
        (
            "#051F#4PThey finally get something out of\x01",
            "our little coup lover?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)

    def lambda_9B67():
        OP_6D(-3320, 0, 1160, 1500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9B67)
    OP_8E(0x8, 0xFFFFEE80, 0x0, 0x3C0, 0x7D0, 0x0)
    OP_8C(0x8, 90, 400)
    WaitChrThread(0x8, 0x2)

    ChrTalk(    #387
        0x8,
        (
            "#762FNo, this is different...though perhaps\x01",
            "not unrelated.\x02\x03",

            "The sky bandits have appeared in Bose.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(30)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(30)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #388
        0x101,
        "#1005F#3SWHAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0xE,
        (
            "#072FThe Intelligence Division AND the bandits?\x01",
            "Heck of a busy night.\x02\x03",

            "Where did they show up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x8,
        (
            "#762FThe fort they used as a base in the Bose\x01",
            "canyons, apparently.\x02\x03",

            "The army had repurposed it as a training ground...\x02\x03",

            "...but it seems they stole back the ship\x01",
            "they used to use and escaped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x9,
        "#023F#5PYou're kidding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0xB,
        (
            "#033FOho... That would be the one\x01",
            "Mueller went to retrieve.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x101,
        (
            "#1020FW-Wait just a second.\x02\x03",

            "Isn't this like really convenient timing?\x02\x03",

            "Does the society have a hand in this too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x8,
        (
            "#764FI can hardly deny the possibility at\x01",
            "this point.\x02\x03",

            "#762FIn any case, it may be wise for you\x01",
            "to travel to Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x101,
        "#1002FI'll say!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A69A")
    TurnDirection(0x9, 0x101, 400)
    Sleep(500)

    ChrTalk(    #396
        0x9,
        (
            "#020F#5PThat seems as good a plan as any.\x02\x03",

            "We have no real way of knowing when\x01",
            "or where the next crisis will strike.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x101,
        "#1015FYeah...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #398
        0x101,
        "#1004F#4PEr, wait. Schera, you're coming along?\x02",
    )

    CloseMessageWindow()

    def lambda_A06F():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A06F)

    def lambda_A07D():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A07D)
    Sleep(10)

    def lambda_A090():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A090)

    def lambda_A09E():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_A09E)
    Sleep(30)

    def lambda_A0B1():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A0B1)

    def lambda_A0BF():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A0BF)

    ChrTalk(    #399
        0x9,
        (
            "#027F#5PNow that the Intelligence Division has basically\x01",
            "been dealt with, my job is done, more or less.\x02\x03",

            "It's pretty clear the agents of Ouroboros are\x01",
            "beyond any one of us, so I thought I'd tag along\x01",
            "to help out a bit. Unless you object?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x101,
        "#1018F#4PYay! No, no, not at all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0xA,
        (
            "#051FHeh, I'm looking forward to seeing the\x01",
            "Silver Streak in action.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0xB,
        (
            "#037FHa-ha-ha! At last, Schera has come\x01",
            "willingly into my arms!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0xC,
        "#048FThank you, Scherazard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x9,
        "#021F#5PNo, it's no trouble.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #405
        0x101,
        "#1004F#5POh, Anelace, are you coming too?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #406
        0x10,
        (
            "#819F#5PHeehee... Sorry, I'm afraid not.\x02\x03",

            "#816FKurt's group should be getting back\x01",
            "from their training soon.\x02\x03",

            "I'm gonna team up with them again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x101,
        "#1025F#5POh, okay...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 400)

    ChrTalk(    #408
        0xE,
        (
            "#070F#4PTeam up? Does that mean you'll\x01",
            "be working against the society too?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xE, 400)

    ChrTalk(    #409
        0x10,
        (
            "#816F#5PYeah! I think we're going to look into\x01",
            "finding their base.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #410
        0x101,
        "#1004F#5PEr, base?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x8,
        (
            "#764FGiven Ouroboros' movements and actions\x01",
            "to date, they must have SOME sort of\x01",
            "base of operations somewhere in Liberl.\x02\x03",

            "#762FUntil we find that and take it down,\x01",
            "this game of cat and mouse will simply\x01",
            "never end.\x02\x03",

            "I have a feeling we'll be working even\x01",
            "more closely with the army in the weeks\x01",
            "to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0xD,
        (
            "#062FA base... Yeah, for starters, they need\x01",
            "somewhere to store and fix up that huge\x01",
            "archaism.\x02\x03",

            "They'd have to have somewhere pretty\x01",
            "decent just for maintenance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0xA,
        (
            "#051FHeh, makes sense to have two anti-society\x01",
            "teams going, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD0F")

    label("loc_A69A")

    TurnDirection(0xA, 0x101, 400)
    Sleep(500)

    ChrTalk(    #414
        0xA,
        (
            "#051FGood idea, probably.\x02\x03",

            "No way to know where these goons'll hit\x01",
            "next, so we should be on the move.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #415
        0x101,
        "#1015FYeah...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #416
        0x101,
        "#1004FEr, wait. Agate, you're coming along?\x02",
    )

    CloseMessageWindow()

    def lambda_A77E():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A77E)
    Sleep(10)

    def lambda_A791():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_A791)

    def lambda_A79F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A79F)
    Sleep(30)

    def lambda_A7B2():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_A7B2)

    def lambda_A7C0():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A7C0)

    ChrTalk(    #417
        0xA,
        (
            "#051FHey, with the Intelligence Division\x01",
            "all cleaned up, my job is done.\x02\x03",

            "You guys are tryin' to climb a friggin'\x01",
            "mountain, here, so I figured I'd give\x01",
            "you a hand up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x101,
        "#1018FReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #419
        0xD,
        "#061F#5PYay, Agate's coming with us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x9,
        (
            "#027F#5PI'll be counting on the power of that\x01",
            "Heavy Blade of yours, Agate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0xE,
        "#070FWelcome to the team.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xD, 400)

    ChrTalk(    #422
        0xA,
        "#051F#6PYeah, thanks.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #423
        0x101,
        "#1004F#5POh, Anelace, are you coming too?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #424
        0x10,
        (
            "#819F#5PHeehee... Sorry, I'm afraid not.\x02\x03",

            "#816FKurt's group should be getting back\x01",
            "from their training soon.\x02\x03",

            "I'm gonna team up with them again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x101,
        "#1025F#5POh, okay...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x10, 400)

    ChrTalk(    #426
        0xE,
        (
            "#070F#4PTeam up? Does that mean you'll\x01",
            "be working against the society too?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xE, 400)

    ChrTalk(    #427
        0x10,
        (
            "#816F#5PYeah! I think we're going to look into\x01",
            "finding their base.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x101,
        "#1004F#5PEr, base?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #429
        0x8,
        (
            "#764FGiven Ouroboros' movements and actions\x01",
            "to date, they must have SOME sort of\x01",
            "base of operations somewhere in Liberl.\x02\x03",

            "#762FUntil we find that and take it down,\x01",
            "this game of cat and mouse will simply\x01",
            "never end.\x02\x03",

            "I have a feeling we'll be working even\x01",
            "more closely with the army in the weeks\x01",
            "to come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0xC,
        (
            "#040FThe Royal Army seems to be doubling their\x01",
            "efforts against the society, yes.\x02\x03",

            "We'll need their help to put an end to\x01",
            "all this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x9,
        (
            "#027F#5PIt does make sense to have another\x01",
            "anti-society team, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD0F")


    ChrTalk(    #432
        0x101,
        (
            "#1015F#5PWell, I guess Kurt's team is going to\x01",
            "need plenty of firepower too...\x02\x03",

            "#1016FCan't complain about them getting\x01",
            "Anelace, in that case.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #433
        0x10,
        (
            "#819F#5PHaha! Sorry.\x02\x03",

            "#816FOnce we find these snaky jerks, I'm sure\x01",
            "we'll need a lot of help to beat them!\x02\x03",

            "We'll fight them together then, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0x101,
        "#1017F#5PYeah... We will!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0x8, 0xFF)
    OP_A2(0x10F3)
    NewScene("ED6_DT21/C5601   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_37_68FE end

    def Function_38_AE7B(): pass

    label("Function_38_AE7B")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 124010, 0, -3770, 90)
    SetChrPos(0x102, 124010, 0, -2950, 90)
    SetChrPos(0xF8, 122910, 0, -3770, 90)
    SetChrPos(0xF9, 122910, 0, -2950, 90)
    OP_8C(0xFE, 270, 0)
    OP_0D()

    ChrTalk(    #435
        0x101,
        "#1004FAh, do you run the cafe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0xFE,
        (
            "Hey, I came out here shopping, then\x01",
            "suddenly I got told to evacuate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0xFE,
        (
            "I thought this'd be a good time to\x01",
            "read a book and calm down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0x101,
        (
            "#1015F(He already seems as calm as\x01",
            "you can get, to be honest...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x2A,
        "Oh! Why, I know that series.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x2A,
        (
            "Is that Gambler Jack, the series popular in the\x01",
            "harbor area that I've heard so much about,\x01",
            "perhaps?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #441
        0x101,
        "#1004FAh, these novels?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0x2A,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x2A,
        (
            "It's a drama about a gambler with\x01",
            "a curious fate, set in the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0x2A,
        "I've been wanting to read it for a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x101,
        (
            "#1011FOh, yeah?\x02\x03",

            "#1015F(I do owe him a bit...)\x02",
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
            "Hand Over Books\x01",      # 0
            "Don't\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B19A")
    Call(1, 40)
    Jump("loc_B1BE")

    label("loc_B19A")


    ChrTalk(    #446
        0x101,
        "#1016F(Nah, I don't think so.)\x02",
    )

    CloseMessageWindow()

    label("loc_B1BE")

    EventEnd(0x0)
    Return()

    # Function_38_AE7B end

    def Function_39_B1C1(): pass

    label("Function_39_B1C1")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 124010, 0, -3770, 90)
    SetChrPos(0x102, 124010, 0, -2950, 90)
    SetChrPos(0xF8, 122910, 0, -3770, 90)
    SetChrPos(0xF9, 122910, 0, -2950, 90)
    OP_8C(0xFE, 270, 0)
    OP_0D()

    ChrTalk(    #447
        0x2A,
        "Oh, what is it?\x02",
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
            "Hand Over Books\x01",      # 0
            "Don't\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B289")
    Call(1, 40)
    Jump("loc_B2AD")

    label("loc_B289")


    ChrTalk(    #448
        0x101,
        "#1015F(Nah, I don't think so.)\x02",
    )

    CloseMessageWindow()

    label("loc_B2AD")

    EventEnd(0x0)
    Return()

    # Function_39_B1C1 end

    def Function_40_B2B0(): pass

    label("Function_40_B2B0")


    ChrTalk(    #449
        0x101,
        (
            "#1001FAll right, here you go.\x01",
            "It's all yours, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0x2A,
        "Oh, that isn't why I mentioned it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #451
        0x101,
        (
            "#1000FDon't worry about it.\x02\x03",

            "It's thanks for the great curry and\x01",
            "coffee before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x2A,
        "That's very kind of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0x2A,
        "I'd be happy to take them.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #454
        "Handed over all of #2CGambler Jack#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3F(0x23A, 1)
    OP_3F(0x23B, 1)
    OP_3F(0x23C, 1)
    OP_3F(0x23D, 1)
    OP_3F(0x23E, 1)
    OP_3F(0x23F, 1)
    OP_3F(0x240, 1)
    OP_3F(0x241, 1)
    OP_3F(0x242, 1)
    OP_3F(0x243, 1)
    OP_3F(0x244, 1)
    OP_3F(0x245, 1)
    OP_3F(0x246, 1)
    OP_3F(0x247, 1)
    OP_0D()

    ChrTalk(    #455
        0x2A,
        (
            "You have my thanks. I'll start reading\x01",
            "right away to calm myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x2A,
        (
            "Oh, And as a token from my side,\x01",
            "allow me to offer you this.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #457
        "\x07\x00Received #1047i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x417, 1)
    OP_0D()

    ChrTalk(    #458
        0x102,
        "#1044FThis is...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0x2A,
        (
            "When I was still a diplomat,\x01",
            "I picked this up in Arteria.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x101,
        (
            "#1015FArteria... That's where the headquarters\x01",
            "of the Septian Church is, isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0x2A,
        "Yes, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0x2A,
        (
            "In the distant past, back during the Zemurian era,\x01",
            "things were made with this metal, apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #463
        0x102,
        (
            "#1044FThe Zemurian era? It must be incredibly old.\x01",
            "Certainly, I've never seen this alloy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #464
        0x2A,
        "Haha, I don't know how true it is.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0x2A,
        (
            "Incidentally, apparently the techniques\x01",
            "to mold that metal have long been lost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0x101,
        (
            "#1004FHuh, thinking about it, that\x01",
            "makes it pretty incredible.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDE, 7)), scpexpr(EXPR_END)), "loc_B850")

    ChrTalk(    #467
        0x102,
        (
            "#1040FI believe we traded books with you\x01",
            "for a weapon before, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0x2A,
        "Haha, I remember.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #469
        0x2A,
        (
            "This isn't anything that incredible this\x01",
            "time, but perhaps it'll be a good luck\x01",
            "charm for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #470
        0x101,
        "#1001FYeah, thanks!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B8C7")

    label("loc_B850")


    ChrTalk(    #471
        0x2A,
        (
            "Haha, it isn't anything that incredible,\x01",
            "but perhaps it'll be a good luck charm\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #472
        0x101,
        "#1001FYeah, thanks!\x02",
    )

    CloseMessageWindow()

    label("loc_B8C7")

    OP_A2(0x10C4)
    Return()

    # Function_40_B2B0 end

    SaveToFile()

Try(main)
