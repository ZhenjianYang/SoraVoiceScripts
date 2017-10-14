from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3120_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3120_1 ._SN',
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
        "Function_1_72C",          # 01, 1
        "Function_2_965",          # 02, 2
        "Function_3_CA2",          # 03, 3
        "Function_4_EB0",          # 04, 4
        "Function_5_1112",         # 05, 5
        "Function_6_1394",         # 06, 6
        "Function_7_1534",         # 07, 7
        "Function_8_17A0",         # 08, 8
        "Function_9_187C",         # 09, 9
        "Function_10_19F5",        # 0A, 10
        "Function_11_1B49",        # 0B, 11
        "Function_12_2AB9",        # 0C, 12
        "Function_13_2D2D",        # 0D, 13
        "Function_14_4327",        # 0E, 14
        "Function_15_4386",        # 0F, 15
        "Function_16_43FA",        # 10, 16
        "Function_17_5C1E",        # 11, 17
        "Function_18_5C3A",        # 12, 18
        "Function_19_5C56",        # 13, 19
        "Function_20_5C72",        # 14, 20
        "Function_21_5C8E",        # 15, 21
        "Function_22_5CBE",        # 16, 22
        "Function_23_88BA",        # 17, 23
        "Function_24_8927",        # 18, 24
        "Function_25_8994",        # 19, 25
        "Function_26_8A01",        # 1A, 26
        "Function_27_8A64",        # 1B, 27
        "Function_28_905D",        # 1C, 28
        "Function_29_9172",        # 1D, 29
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_13A")
    Jump("loc_17C")

    label("loc_13A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_156")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17C")

    label("loc_156")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_172")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17C")

    label("loc_172")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17C")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_239")

    ChrTalk(    #0
        0xE,
        (
            "#030FTo think treasure hunting would end\x01",
            "with us finding an artifact.\x02\x03",

            "To hold faith in any situation...\x01",
            "That, perhaps, is what matters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_358")

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_303")

    ChrTalk(    #1
        0xE,
        (
            "#030FHello, ladies and gentlemen. Good day.\x02\x03",

            "Still, to think treasure hunting would\x01",
            "end with us finding an artifact.\x02\x03",

            "To hold faith in any situation...\x01",
            "That, perhaps, is what matters.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_358")

    label("loc_303")


    ChrTalk(    #2
        0xE,
        (
            "#030FHello, ladies and gentlemen. Good day.\x02\x03",

            "Do you have some business with me?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_358")

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
        (0, "loc_3B7"),
        (1, "loc_42E"),
        (SWITCH_DEFAULT, "loc_42E"),
    )


    label("loc_3B7")


    ChrTalk(    #3
        0xE,
        (
            "#030FHeh, I see.\x02\x03",

            "You need the power of my genius.\x01",
            "Not to worry; I understand entirely.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_427")
    Call(1, 7)
    Jump("loc_42B")

    label("loc_427")

    Call(1, 6)

    label("loc_42B")

    Jump("loc_723")

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_677")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_515")

    ChrTalk(    #4
        0xE,
        (
            "#031FThat's quite all right. I suppose I could\x01",
            "take this as a chance to rest and relax\x01",
            "for a time.\x02\x03",

            "This should also make for a fine\x01",
            "opportunity to deepen the connection\x01",
            "between little Tita and myself.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_674")

    label("loc_515")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5B1")

    ChrTalk(    #5
        0xE,
        (
            "#031FThat's quite all right. I shall remain\x01",
            "on standby here.\x02\x03",

            "In Her Majesty's company, I'm most\x01",
            "certain I shall be well entertained.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_674")

    label("loc_5B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_674")

    ChrTalk(    #6
        0xE,
        (
            "#031FThat's quite all right. I don't mind\x01",
            "indulging in pleasant conversation here\x01",
            "for a while longer.\x02\x03",

            "If only I had a glass of wine to help\x01",
            "the tongue flow more freely. Alas.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_674")

    Jump("loc_720")

    label("loc_677")


    ChrTalk(    #7
        0xE,
        (
            "#030FThat's quite all right. I suppose I could\x01",
            "take this as a chance to rest and relax\x01",
            "for a time.\x02\x03",

            "Should you ever long for my dulcet\x01",
            "tones, simply give the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_720")

    Jump("loc_723")

    label("loc_723")

    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Return()

    # Function_0_AA end

    def Function_1_72C(): pass

    label("Function_1_72C")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xF)
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0x0, 0)
    OP_51(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7BC")
    Jump("loc_7FE")

    label("loc_7BC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7D8")
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7FE")

    label("loc_7D8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7F4")
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7FE")

    label("loc_7F4")

    OP_51(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7FE")

    OP_51(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    ChrTalk(    #8
        0xF,
        (
            "#040FOh, hey, guys.\x02\x03",

            "Anything I can help with?\x02",
        )
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
        (0, "loc_8B6"),
        (1, "loc_8FA"),
        (SWITCH_DEFAULT, "loc_8FA"),
    )


    label("loc_8B6")


    ChrTalk(    #9
        0xF,
        "#040FI'd be more than happy to help.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F3")
    Call(1, 7)
    Jump("loc_8F7")

    label("loc_8F3")

    Call(1, 6)

    label("loc_8F7")

    Jump("loc_95C")

    label("loc_8FA")


    ChrTalk(    #10
        0xF,
        (
            "#040FI'll stay here for a bit, then.\x02\x03",

            "If you need me for anything,\x01",
            "don't hesitate to ask.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_95C")

    label("loc_95C")

    SetChrSubChip(0xF, 0)
    TalkEnd(0xF)
    Return()

    # Function_1_72C end

    def Function_2_965(): pass

    label("Function_2_965")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9F5")
    Jump("loc_A37")

    label("loc_9F5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A11")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A37")

    label("loc_A11")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2D")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A37")

    label("loc_A2D")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A37")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A99")

    ChrTalk(    #11
        0xA,
        (
            "#560FOh, hi, Agate!\x02\x03",

            "Is everything okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AF3")

    label("loc_A99")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACA")

    ChrTalk(    #12
        0xA,
        "#060FHi, Estelle! What's up?\x02",
    )

    CloseMessageWindow()
    Jump("loc_AF3")

    label("loc_ACA")


    ChrTalk(    #13
        0xA,
        (
            "#060FHi, guys!\x02\x03",

            "Is everything okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF3")

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
        (0, "loc_B52"),
        (1, "loc_BCE"),
        (SWITCH_DEFAULT, "loc_BCE"),
    )


    label("loc_B52")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B8F")

    ChrTalk(    #14
        0xA,
        "#060FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BB4")

    label("loc_B8F")


    ChrTalk(    #15
        0xA,
        "#560FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()

    label("loc_BB4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC7")
    Call(1, 7)
    Jump("loc_BCB")

    label("loc_BC7")

    Call(1, 6)

    label("loc_BCB")

    Jump("loc_C99")

    label("loc_BCE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C3E")

    ChrTalk(    #16
        0xA,
        (
            "#064FHuh? Are you sure?\x02\x03",

            "#060FWell, I'll be here. Just call for\x01",
            "me if you need me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C96")

    label("loc_C3E")


    ChrTalk(    #17
        0xA,
        (
            "#064FHuh? Are you sure?\x02\x03",

            "#060FWell, I'll be here. Just call for\x01",
            "me if you need me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C96")

    Jump("loc_C99")

    label("loc_C99")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    # Function_2_965 end

    def Function_3_CA2(): pass

    label("Function_3_CA2")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x11)
    ClearChrFlags(0x11, 0x10)
    TurnDirection(0x11, 0x0, 0)
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D32")
    Jump("loc_D74")

    label("loc_D32")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D4E")
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D74")

    label("loc_D4E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D6A")
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D74")

    label("loc_D6A")

    OP_51(0x11, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x11, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D74")

    OP_51(0x11, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x11, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x10)

    ChrTalk(    #18
        0x11,
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
        (0, "loc_E17"),
        (1, "loc_E5D"),
        (SWITCH_DEFAULT, "loc_E5D"),
    )


    label("loc_E17")


    ChrTalk(    #19
        0x11,
        "#070FNeed me to sub in, huh? I'm game!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E56")
    Call(1, 7)
    Jump("loc_E5A")

    label("loc_E56")

    Call(1, 6)

    label("loc_E5A")

    Jump("loc_EA7")

    label("loc_E5D")


    ChrTalk(    #20
        0x11,
        (
            "#070FChanged your mind? No worries.\x02\x03",

            "I'll be here if you need me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EA7")

    label("loc_EA7")

    SetChrSubChip(0x11, 0)
    TalkEnd(0x11)
    Return()

    # Function_3_CA2 end

    def Function_4_EB0(): pass

    label("Function_4_EB0")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x17)
    ClearChrFlags(0x17, 0x10)
    TurnDirection(0x17, 0x0, 0)
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F40")
    Jump("loc_F82")

    label("loc_F40")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F5C")
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F82")

    label("loc_F5C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F78")
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F82")

    label("loc_F78")

    OP_51(0x17, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x17, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F82")

    OP_51(0x17, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x17, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD0")

    ChrTalk(    #21
        0x17,
        "#020FHm? What is it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FE4")

    label("loc_FD0")


    ChrTalk(    #22
        0x17,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()

    label("loc_FE4")

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
        (0, "loc_1043"),
        (1, "loc_109A"),
        (SWITCH_DEFAULT, "loc_109A"),
    )


    label("loc_1043")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106C")

    ChrTalk(    #23
        0x17,
        "#020FNeed some help?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1080")

    label("loc_106C")


    ChrTalk(    #24
        0x17,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()

    label("loc_1080")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1093")
    Call(1, 7)
    Jump("loc_1097")

    label("loc_1093")

    Call(1, 6)

    label("loc_1097")

    Jump("loc_1109")

    label("loc_109A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F2")

    ChrTalk(    #25
        0x17,
        (
            "#020FI'll hang around here for a bit, then.\x02\x03",

            "Keep up the good work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1106")

    label("loc_10F2")


    ChrTalk(    #26
        0x17,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()

    label("loc_1106")

    Jump("loc_1109")

    label("loc_1109")

    SetChrSubChip(0x17, 0)
    TalkEnd(0x17)
    Return()

    # Function_4_EB0 end

    def Function_5_1112(): pass

    label("Function_5_1112")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x18)
    ClearChrFlags(0x18, 0x10)
    TurnDirection(0x18, 0x0, 0)
    OP_51(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11A2")
    Jump("loc_11E4")

    label("loc_11A2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_11BE")
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11E4")

    label("loc_11BE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11DA")
    OP_51(0x18, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11E4")

    label("loc_11DA")

    OP_51(0x18, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x18, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11E4")

    OP_51(0x18, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x18, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1231")

    ChrTalk(    #27
        0x18,
        "#050FYo, what's up?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1245")

    label("loc_1231")


    ChrTalk(    #28
        0x18,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()

    label("loc_1245")

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
        (0, "loc_129D"),
        (1, "loc_12FA"),
        (SWITCH_DEFAULT, "loc_12FA"),
    )


    label("loc_129D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12CC")

    ChrTalk(    #29
        0x18,
        "#050FYeah, yeah, I got it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E0")

    label("loc_12CC")


    ChrTalk(    #30
        0x18,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()

    label("loc_12E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12F3")
    Call(1, 7)
    Jump("loc_12F7")

    label("loc_12F3")

    Call(1, 6)

    label("loc_12F7")

    Jump("loc_138B")

    label("loc_12FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1374")

    ChrTalk(    #31
        0x18,
        (
            "#051FWhat, changed your mind?\x02\x03",

            "Well, if you ever need somebody to\x01",
            "swing a sword around, gimme a call.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1388")

    label("loc_1374")


    ChrTalk(    #32
        0x18,
        "◆セリフ無し。\x02",
    )

    CloseMessageWindow()

    label("loc_1388")

    Jump("loc_138B")

    label("loc_138B")

    SetChrSubChip(0x18, 0)
    TalkEnd(0x18)
    Return()

    # Function_5_1112 end

    def Function_6_1394(): pass

    label("Function_6_1394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_13D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_13BA")
    OP_C9(0x1, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    Jump("loc_13CF")

    label("loc_13BA")

    OP_C9(0x1, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x3, 0x4, 0x6, 0x7, 0xFFFF)

    label("loc_13CF")

    Jump("loc_13FE")

    label("loc_13D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_13ED")
    OP_C9(0x1, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_13FE")

    label("loc_13ED")

    OP_C9(0x1, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_13FE")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_A3(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_145B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_145B")
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 23530, 200, -2100, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 18)
    OP_A2(0x9)

    label("loc_145B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AE")
    SetChrFlags(0xE, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148D")
    SetChrPos(0xE, 23530, 200, -2100, 0)
    OP_A2(0xA)
    Jump("loc_14A1")

    label("loc_148D")

    SetChrPos(0xE, 23530, 200, 400, 180)
    OP_A3(0xA)

    label("loc_14A1")

    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 6)
    OP_A2(0x9)

    label("loc_14AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1501")
    SetChrFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14E0")
    SetChrPos(0xF, 23530, 200, -2100, 0)
    OP_A2(0xB)
    Jump("loc_14F4")

    label("loc_14E0")

    SetChrPos(0xF, 23530, 200, 400, 180)
    OP_A3(0xB)

    label("loc_14F4")

    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 7)
    OP_A2(0x9)

    label("loc_1501")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1532")
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 23530, 200, 400, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 17)
    OP_A2(0x9)

    label("loc_1532")

    OP_0D()
    Return()

    # Function_6_1394 end

    def Function_7_1534(): pass

    label("Function_7_1534")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_A3(0xD)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15D1")
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x4)
    SetChrChipByIndex(0x17, 15)
    SetChrPos(0x17, 23550, 200, 420, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15B6")
    OP_41(0x2, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_15B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D1")
    OP_41(0x2, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_15D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1634")
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x4)
    SetChrChipByIndex(0x18, 16)
    SetChrPos(0x18, 26270, 200, -480, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1619")
    OP_41(0x5, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_1619")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1634")
    OP_41(0x5, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_1634")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1697")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 17)
    SetChrPos(0xA, 28530, 200, -570, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_167C")
    OP_41(0x6, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_167C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1697")
    OP_41(0x6, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_1697")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_16FA")
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrChipByIndex(0x11, 18)
    SetChrPos(0x11, 23550, 200, -2170, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16DF")
    OP_41(0x7, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_16DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16FA")
    OP_41(0x7, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0xD)

    label("loc_16FA")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_179F")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #33
        (
            "\x07\x05A standby member was equipped with a Zero Field Generator.\x01",
            "It has been recovered and added to party inventory.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_179F")

    Return()

    # Function_7_1534 end

    def Function_8_17A0(): pass

    label("Function_8_17A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_17B1")
    OP_2A(0xBB, 0xBC, 0xFFFF)
    Jump("loc_1878")

    label("loc_17B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_17D2")
    OP_2A(0x6C, 0x6D, 0x6E, 0xA5, 0xA6, 0x6F, 0x70, 0xA7, 0xA8, 0x71, 0xFFFF)
    Jump("loc_1878")

    label("loc_17D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_17F1")
    OP_2A(0x6C, 0x6D, 0x6E, 0xA5, 0xA6, 0x6F, 0x70, 0xA7, 0xA8, 0xFFFF)
    Jump("loc_1878")

    label("loc_17F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_1810")
    OP_2A(0x6C, 0x6D, 0x6E, 0xA5, 0xA6, 0x6F, 0x70, 0xA7, 0xA8, 0xFFFF)
    Jump("loc_1878")

    label("loc_1810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 3)), scpexpr(EXPR_END)), "loc_1827")
    OP_2A(0x6C, 0x6D, 0x6E, 0xA5, 0xA6, 0xFFFF)
    Jump("loc_1878")

    label("loc_1827")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_183E")
    OP_2A(0x6C, 0x6D, 0x6E, 0xA5, 0xA6, 0xFFFF)
    Jump("loc_1878")

    label("loc_183E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #34
        "\x07\x05No jobs are available.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1878")

    TalkEnd(0xFF)
    Return()

    # Function_8_17A0 end

    def Function_9_187C(): pass

    label("Function_9_187C")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    Call(1, 15)

    ChrTalk(    #35
        0x8,
        (
            "#790FSeems you had a look at the bulletin board.\x02\x03",

            "Will you help with the investigation too?\x02",
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
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F0")

    ChrTalk(    #36
        0x101,
        (
            "#1015F#5PI'm afraid we can't...\x02\x03",

            "#1006FWas just kind of interested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "#792FI see. In that case, focus on\x01",
            "the other investigation.\x02\x03",

            "This matter isn't particularly urgent.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x6C, 0x1, 0x8000)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    label("loc_19F0")

    Call(1, 11)
    Return()

    # Function_9_187C end

    def Function_10_19F5(): pass

    label("Function_10_19F5")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    Call(1, 15)

    ChrTalk(    #38
        0x8,
        (
            "#790FSeems like you're pretty interested\x01",
            "in the sign case.\x02\x03",

            "Want to help with the investigation?\x02",
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
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B44")

    ChrTalk(    #39
        0x101,
        "#1015F#5PI'm afraid we can't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "#792FI see. In that case, focus on\x01",
            "the other investigation.\x02\x03",

            "This matter isn't particularly urgent.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    label("loc_1B44")

    Call(1, 11)
    Return()

    # Function_10_19F5 end

    def Function_11_1B49(): pass

    label("Function_11_1B49")

    EventBegin(0x0)

    ChrTalk(    #41
        0x101,
        (
            "#1002F#5PY-Yeah, that's the idea.\x02\x03",

            "So by the sign, do you mean the sign with\x01",
            "the crest that hangs outside the branch?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "#792FYes, that sign was stolen.\x02\x03",

            "There're no particular practical problems as-is,\x01",
            "but the emblem is the symbol of the guild's\x01",
            "mission and duty...\x02\x03",

            "#790FWith that stolen, we can't just sit quietly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1015F#5PI, I see...\x02\x03",

            "Yeah, kinda hard to ignore that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1D2C")

    ChrTalk(    #44
        0x106,
        (
            "#053F#3PHmph, looks like someone's insulted us.\x02\x03",

            "#050F...So, how did it go down?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D98")

    label("loc_1D2C")


    ChrTalk(    #45
        0x103,
        (
            "#025F#3PReally, it looks like someone doesn't think\x01",
            "much of us.\x02\x03",

            "#022FSo, what's the series of events?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D98")


    ChrTalk(    #46
        0x8,
        (
            "#790FIt was discovered yesterday around noon\x01",
            "by branch bracer Wong.\x02\x03",

            "When he came back to report, he\x01",
            "realized the sign was missing.\x02\x03",

            "#792FWe think that the crime happened\x01",
            "during the day then.\x02\x03",

            "I was away at the time on other business,\x01",
            "but a worker in front of the branch witnessed it.\x02\x03",

            "#790FIt seems the criminal was a person in a disguise.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #47
        0x101,
        "#1004F#5PD-Disguise?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F7C")

    ChrTalk(    #48
        0x105,
        (
            "#043FE-Estelle...\x02\x03",

            "Could it be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1020F#5PNo... No way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FD8")

    label("loc_1F7C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FD8")

    ChrTalk(    #50
        0x104,
        (
            "#033FOh, how VERY interesting.\x02\x03",

            "Could it be...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1020F#5PN-No way...\x02",
    )

    CloseMessageWindow()

    label("loc_1FD8")


    ChrTalk(    #52
        0x8,
        (
            "#790FIt seems you have a suspicion.\x02\x03",

            "#792FSo...how about this?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #53
        (
            "\x07\x05'Beauteous princess and her companions.\x01",
            "The soul of gathered heroes is in my hands.'\x02\x03",

            "'Should you desire its release,\x01",
            "you must defeat my curse.'\x02\x03",

            "'The first key is in the city.\x01",
            "Search the back of the [Forty-year-old Man].'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #54
        0x8,
        (
            "#790FThis card was sent shortly after\x01",
            "the crime was discovered.\x02\x03",

            "From the content, I assume it's declaring\x01",
            "responsibility for the crime.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_21E7")

    ChrTalk(    #55
        0x106,
        "#551F#3P...\x02",
    )

    CloseMessageWindow()
    Jump("loc_21F8")

    label("loc_21E7")


    ChrTalk(    #56
        0x103,
        "#025F#3P...\x02",
    )

    CloseMessageWindow()

    label("loc_21F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_222B")

    ChrTalk(    #57
        0x105,
        "#045FIt seems it is certain.\x02",
    )

    CloseMessageWindow()
    Jump("loc_225F")

    label("loc_222B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_225F")

    ChrTalk(    #58
        0x104,
        "#032FNow it seems to be certain.\x02",
    )

    CloseMessageWindow()

    label("loc_225F")


    ChrTalk(    #59
        0x101,
        "#1007F#5P*sigh* I knew it. It's him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x8,
        (
            "#792FBy 'him,' I assume you mean\x01",
            "Phantom Thief Bleublanc?\x02\x03",

            "#790FI have heard about the events in\x01",
            "Ruan from Jean.\x02\x03",

            "I suppose this case marks a challenge\x01",
            "from Phantom Thief B.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23B2")

    ChrTalk(    #61
        0x104,
        (
            "#031FHeh, interesting.\x02\x03",

            "It is a challenge from none other than my rival.\x01",
            "Of course I shall accept.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23B2")


    ChrTalk(    #62
        0x101,
        "#1003F#5PI dunno, it seems one-sided, yeah?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_247F")

    ChrTalk(    #63
        0x106,
        (
            "#050F#3PDon't matter. He picked this fight.\x01",
            "We've gotta take it back.\x02\x03",

            "Anyway, let's start our investigation\x01",
            "with what the card says.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2510")

    label("loc_247F")


    ChrTalk(    #64
        0x103,
        (
            "#022F#3PTrue, it is a very selfish challenge.\x01",
            "We have to accept it, though.\x02\x03",

            "Anyway, let's start our investigation\x01",
            "with what the card says.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2510")

    TurnDirection(0x101, 0xF7, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_260B")

    ChrTalk(    #65
        0x101,
        (
            "#1000F#2PLet's see, the card's words... 'In the city,'\x01",
            "and 'the back of the forty-year-old man, huh.'\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #66
        0x107,
        (
            "#063FHmmm, so we have to find an older person\x01",
            "in the city somewhere? With, um, a card\x01",
            "stuck to his back...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26BD")

    label("loc_260B")


    ChrTalk(    #67
        0x101,
        (
            "#1015F#2PLet's see, the card's words... 'In the city,'\x01",
            "and 'the back of the forty-year-old man,' huh.\x02\x03",

            "If we take it straight as-is, I guess\x01",
            "we gotta look for an older guy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2783")
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #68
        0x104,
        (
            "#032FCertainly looking at it in a literal sense\x01",
            "it would mean that, but...\x02\x03",

            "After the case at the school, I think it's clear\x01",
            "that it won't be so straightforward.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    Jump("loc_2835")

    label("loc_2783")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2835")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #69
        0x105,
        (
            "#042FYes, certainly looking at it directly\x01",
            "it would mean that, but...\x02\x03",

            "After the case at the school, I think\x01",
            "things won't be so straightforward.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    label("loc_2835")


    ChrTalk(    #70
        0x101,
        (
            "#1002F#2PThose messages were all metaphors,\x01",
            "weren't they?\x02\x03",

            "I wonder if this one is too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2908")

    ChrTalk(    #71
        0x106,
        (
            "#053F#3PWell, who knows...\x02\x03",

            "#050FNo point in worryin' 'bout it.\x01",
            "Let's start investigating in the city.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2984")

    label("loc_2908")


    ChrTalk(    #72
        0x103,
        (
            "#026F#3PWell, who knows...\x02\x03",

            "#022FThere's no point in worrying about it, though.\x01",
            "Let's start investigating in the city.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2984")


    ChrTalk(    #73
        0x8,
        (
            "#790FYes, I think that's the only real option.\x02\x03",

            "Well, then, I'll expect good results.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29E5():
        OP_8C(0x1, 0, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_29E5)
    Sleep(50)

    def lambda_29F8():
        OP_8C(0x2, 0, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_29F8)
    Sleep(100)

    def lambda_2A0B():
        OP_8C(0x3, 0, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2A0B)
    OP_8C(0x0, 0, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A66")

    ChrTalk(    #74
        0x104,
        "#031FHeh, leave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1006F#5PLet's be off.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A99")

    label("loc_2A66")


    ChrTalk(    #76
        0x101,
        (
            "#1006F#5PYeah, leave it to us.\x02\x03",

            "Let's be off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A99")

    OP_28(0x6C, 0x1, 0x1)
    OP_28(0x6C, 0x1, 0x2)
    OP_28(0x6C, 0x4, 0x4)
    OP_28(0x6C, 0x4, 0x8)
    OP_A2(0x11)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_11_1B49 end

    def Function_12_2AB9(): pass

    label("Function_12_2AB9")


    ChrTalk(    #77
        0x8,
        (
            "#790FWould you like to check the\x01",
            "contents of the card again?\x02",
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
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CD2")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #78
        (
            "\x07\x05'Beauteous princess and her companions.\x01",
            "The soul of gathered heroes is in my hands.'\x02\x03",

            "'Should you desire its release,\x01",
            "you must defeat my curse.'\x02\x03",

            "'The first key is in the city.\x01",
            "Search the back of the [Forty-year-old Man].'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #79
        0x8,
        (
            "#790FThe points seem to be 'in the city'\x01",
            "and the 'forty-year-old man.'\x02\x03",

            "Well, then, good luck with the investigation.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D2C")

    label("loc_2CD2")


    ChrTalk(    #80
        0x8,
        (
            "#790FWell, then, good luck with the investigation.\x02\x03",

            "I'll be expecting much from you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D2C")

    Return()

    # Function_12_2AB9 end

    def Function_13_2D2D(): pass

    label("Function_13_2D2D")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    SetChrPos(0x8, 3500, 0, 1200, 180)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, 3500, 0, -3440, 0)
    SetChrPos(0x101, 3500, 0, -2210, 180)
    SetChrPos(0xF7, 4300, 0, -1830, 180)
    SetChrPos(0xF8, 2800, 0, -800, 180)
    SetChrPos(0xF9, 4200, 0, -800, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DC2")
    SetChrPos(0xE, 2120, 0, -1810, 135)
    SetChrChipByIndex(0xE, 4)

    label("loc_2DC2")

    OP_6B(2720, 0)
    OP_6D(2650, 0, -1360, 0)
    OP_67(0, 6000, -10000, 0)
    OP_0D()

    ChrTalk(    #81
        0x8,
        (
            "#792F#4PThat was a very near thing.\x02\x03",

            "If you'd opened the chest first,\x01",
            "you'd likely be monster food now.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #82
        0x19,
        "Wh-Whoa! Monster food...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x19,
        (
            "I-I totally regret it, so please\x01",
            "don't scare me like that.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2F74")

    ChrTalk(    #84
        0x106,
        (
            "#050F#4PWe're not tryin' to scare you.\x02\x03",

            "But, you really were saved by\x01",
            "a coincidence this time.\x02\x03",

            "Understand that and make sure\x01",
            "you learn somethin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_301F")

    label("loc_2F74")


    ChrTalk(    #85
        0x103,
        (
            "#020F#4PWe're not trying to scare you.\x02\x03",

            "But, you really were saved by\x01",
            "a coincidence this time.\x02\x03",

            "Understand that and make sure you've\x01",
            "learned something from all this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_301F")


    ChrTalk(    #86
        0x19,
        "G-Got it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x19,
        (
            "Anyway, I'm going to focus on getting\x01",
            "a job for now so I can pay for an escort\x01",
            "next time.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #88
        0x101,
        (
            "#1016F#4PS-So that's how it's gonna be...\x02\x03",

            "You may regret it, but you're\x01",
            "still going into danger, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x19,
        (
            "W-Well, yeah. I gotta.\x01",
            "Treasure hunting's a man's romance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x19,
        (
            "For discoveries like this, a\x01",
            "little danger is unavoidable.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_326C")

    ChrTalk(    #91
        0x104,
        (
            "#030FSpeaking of, what happened\x01",
            "to the discovery this time?\x02\x03",

            "It seems it really was pirate treasure\x01",
            "in the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#1011F#4PAh, right, right.\x02\x03",

            "Anyway, I need to return the treasure\x01",
            "to Jimmy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34A5")

    label("loc_326C")


    ChrTalk(    #93
        0xE,
        (
            "#030FSpeaking of, what happened\x01",
            "to the discovery this time?\x02\x03",

            "It seems it really was pirate treasure\x01",
            "in the end.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #94
        0x101,
        (
            "#1011F#4PAh, right, right.\x02\x03",

            "#1019F...Wait, why are you even here?\x02\x03",

            "Weren't you enjoying a refined\x01",
            "moment on the second floor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xE,
        (
            "#031FWell, I happened to hear the cheerful sound of\x01",
            "your sweet voices below. How could a social\x01",
            "butterfly such as myself resist that siren call?\x02\x03",

            "Now, please continue.\x01",
            "Pretend I'm not here at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        (
            "#1007F#4PIf only...\x02\x03",

            "#1015FAnyway, putting that aside, first I need\x01",
            "to give you back your treasure.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x19, 400)

    label("loc_34A5")

    OP_94(0x1, 0x101, 0x0, 0xC8, 0x3E8, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #97
        "Handed over the #2C#16ISilver Dew Orb#0C.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_94(0x1, 0x101, 0xB4, 0xC8, 0x3E8, 0x0)

    ChrTalk(    #98
        0x19,
        "Th-Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x19,
        (
            "It's like a dream come true to\x01",
            "really find treasure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1015F#4PHmmm, still, I wonder what it really is.\x02\x03",

            "Whatever it is, it sounds pretty incredible,\x01",
            "judging by the letter that was left with it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x19,
        "Th-That's true, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x19,
        "I've never seen anything like this before.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3713")

    ChrTalk(    #103
        0x108,
        (
            "#070FMost likely an artifact.\x02\x03",

            "It's lost its power from the look\x01",
            "of it, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_36C9():
        TurnDirection(0x101, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36C9)

    def lambda_36D7():
        TurnDirection(0xF7, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_36D7)

    def lambda_36E5():
        TurnDirection(0xF8, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_36E5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3709")

    def lambda_3701():
        TurnDirection(0xE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3701)

    label("loc_3709")

    TurnDirection(0xF9, 0x108, 400)
    Jump("loc_3896")

    label("loc_3713")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37D5")

    ChrTalk(    #104
        0x104,
        (
            "#030FIt's most likely an artifact.\x02\x03",

            "From the look of it, however, its power\x01",
            "has long since left it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_37A7():
        TurnDirection(0x101, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37A7)

    def lambda_37B5():
        TurnDirection(0xF7, 0x104, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_37B5)

    def lambda_37C3():
        TurnDirection(0xF8, 0x104, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_37C3)
    TurnDirection(0xF9, 0x104, 400)
    Jump("loc_3896")

    label("loc_37D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3896")

    ChrTalk(    #105
        0x105,
        (
            "#042FMost likely it is...an artifact.\x02\x03",

            "It's lost its power from the look\x01",
            "of it, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_385D():
        TurnDirection(0x101, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_385D)

    def lambda_386B():
        TurnDirection(0xF7, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_386B)

    def lambda_3879():
        TurnDirection(0xF8, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3879)

    def lambda_3887():
        TurnDirection(0xE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3887)
    TurnDirection(0xF9, 0x105, 400)

    label("loc_3896")

    WaitChrThread(0x101, 0x1)
    Sleep(400)

    ChrTalk(    #106
        0x19,
        "Whaaat?! An artifact?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        (
            "#1004FArtifacts are relics from a long time ago,\x01",
            "right?\x02\x03",

            "Even if it doesn't have any power,\x01",
            "isn't it still pretty dangerous?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39DF")

    ChrTalk(    #108
        0x108,
        (
            "#070FMmm, possibly. You should have it examined\x01",
            "by the proper authorities.\x02\x03",

            "It's a bit of a problem to have citizens\x01",
            "possess those things.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B29")

    label("loc_39DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A88")

    ChrTalk(    #109
        0x104,
        (
            "#030FYes, you should go get it investigated\x01",
            "through the proper channels.\x02\x03",

            "I can't really recommend individual\x01",
            "possession of it given their nature.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B29")

    label("loc_3A88")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B29")

    ChrTalk(    #110
        0x105,
        (
            "#047FYes, you should go get it investigated\x01",
            "through the proper channels.\x02\x03",

            "#042FGiven what it is, just holding onto it\x01",
            "isn't a very good idea.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B29")


    ChrTalk(    #111
        0x8,
        (
            "#790FThe closest research facility would be the\x01",
            "History Museum in the capital.\x02\x03",

            "If you wish, I could contact them for you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3BAF():
        TurnDirection(0x101, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BAF)
    Sleep(100)

    def lambda_3BC2():
        OP_8C(0xF7, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3BC2)
    Sleep(50)

    def lambda_3BD5():
        TurnDirection(0xF8, 0x19, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3BD5)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BFE")

    def lambda_3BF1():
        TurnDirection(0xE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3BF1)
    Sleep(50)

    label("loc_3BFE")

    TurnDirection(0xF9, 0x19, 400)

    ChrTalk(    #112
        0x19,
        "P-Please do!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x19,
        (
            "If it's that dangerous, I'd definitely like\x01",
            "to have it looked at.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x8,
        (
            "#790FUnderstood.\x02\x03",

            "Well, then, I will prepare everything,\x01",
            "including your ticket to the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x19,
        "Wooow, thanks! What great service.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "#792FNo, it's a necessary expense.\x02\x03",

            "After all, you're completely broke,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #117
        0x19,
        "Whoa?! H-How did you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1016F#4PAhaha, that's our Kilika.\x02\x03",

            "#1000FBut, the way things are outside right now,\x01",
            "it's probably best for you to take her up\x01",
            "on the offer anyway.\x02\x03",

            "Walking the roads is just way too scary\x01",
            "at the moment.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3E77")

    ChrTalk(    #119
        0x106,
        "#551F#4PYeah, absolutely.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E92")

    label("loc_3E77")


    ChrTalk(    #120
        0x103,
        "#025F#4PYes, I agree.\x02",
    )

    CloseMessageWindow()

    label("loc_3E92")


    ChrTalk(    #121
        0x8,
        (
            "#790F#4PYou can get your ticket from the\x01",
            "receptionist at the landing port.\x02\x03",

            "Well, then, take care on your way\x01",
            "to the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x19,
        "Really, thanks for today.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x1, 0x8000)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F49")
    OP_A2(0x12)

    label("loc_3F49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FCB")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Completed Jimmy Quest in previous game\x01",      # 0
            "No change\x01",                                   # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3FC5"),
        (SWITCH_DEFAULT, "loc_3FCB"),
    )


    label("loc_3FC5")

    OP_A2(0x12)
    Jump("loc_3FCB")

    label("loc_3FCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_END)), "loc_413C")

    ChrTalk(    #123
        0x19,
        "...No, thinking about it, it's not just today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x19,
        "I owe you guys a lot from before too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x19,
        "Here, take this.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #126
        "\x07\x00Received #727i quartz.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x2D7, 1)

    ChrTalk(    #127
        0x19,
        (
            "It's a favorite of mine.\x01",
            "I'd like you to have it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        "#1004F#4PAre you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x19,
        (
            "It's a sign of my thanks for saving my butt\x01",
            "so many times. Please, accept it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_413C")


    ChrTalk(    #130
        0x19,
        "Hope we see each other in the capital!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        (
            "#1006F#4PYeah, got it.\x02\x03",

            "Make sure you deliver that jewel to the museum.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x19,
        "Yeah, leave it to me.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4238")

    ChrTalk(    #133
        0xE,
        (
            "#031FWell, then, if you will pardon me.\x02\x03",

            "Jimmy, good day.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0xE, 400)

    ChrTalk(    #134
        0x19,
        "Yeah, you too.\x02",
    )

    CloseMessageWindow()

    label("loc_4238")


    def lambda_423E():
        OP_6D(1820, 0, -4980, 2500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_423E)
    OP_8C(0x19, 270, 400)
    OP_43(0xE, 0x0, 0x1, 0xE)
    OP_8E(0x19, 0x5AA, 0x0, 0xFFFFE7DC, 0x7D0, 0x0)

    def lambda_4278():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_4278)
    OP_8E(0x19, 0x5AA, 0x0, 0xFFFFE0AC, 0x7D0, 0x0)
    WaitChrThread(0x19, 0x0)
    WaitChrThread(0x8, 0x1)
    OP_28(0x71, 0x4, 0x10)
    OP_28(0x71, 0x1, 0x4)
    OP_28(0x71, 0x1, 0x8)
    OP_28(0x71, 0x1, 0x10)
    OP_69(0x101, 0x7D0)
    WaitChrThread(0xE, 0x0)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #135
        "Quest #2C[Missing Guest] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0xC)
    EventEnd(0x0)
    OP_4B(0x8, 255)
    Return()

    # Function_13_2D2D end

    def Function_14_4327(): pass

    label("Function_14_4327")

    Sleep(400)
    OP_8C(0xE, 315, 500)
    SetChrFlags(0xE, 0x4)
    OP_8E(0xE, 0xFFFFF8D0, 0x0, 0x51E, 0x9C4, 0x0)
    OP_8E(0xE, 0xFFFFF858, 0x0, 0x992, 0x9C4, 0x0)
    OP_8C(0xE, 90, 500)
    ClearChrFlags(0xE, 0x4)
    OP_8E(0xE, 0x9C4, 0x8CA, 0xAAA, 0x9C4, 0x0)
    SetChrFlags(0xE, 0x80)
    Return()

    # Function_14_4327 end

    def Function_15_4386(): pass

    label("Function_15_4386")

    Fade(1000)
    OP_8C(0x8, 180, 0)
    SetChrPos(0x101, 4230, 0, -710, 0)
    SetChrPos(0xF7, 3180, 0, -700, 0)
    SetChrPos(0xF8, 4300, 0, -1950, 0)
    SetChrPos(0xF9, 3380, 0, -2100, 0)
    OP_6D(3550, 0, 330, 0)
    OP_67(0, 6000, -10000, 0)
    OP_0D()
    Return()

    # Function_15_4386 end

    def Function_16_43FA(): pass

    label("Function_16_43FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_440B")
    Call(0, 27)

    label("loc_440B")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    SetChrPos(0x8, 5230, 0, 2029, 0)
    SetChrPos(0x101, 2240, 0, -5100, 0)
    SetChrPos(0xF7, 1230, 0, -5230, 0)
    SetChrPos(0x105, 2170, 0, -6120, 0)
    SetChrPos(0x104, 1010, 0, -6200, 0)
    OP_6D(5230, 0, 2029, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(325000, 0)
    OP_6E(262, 0)
    OP_6D(2240, 0, -5100, 0)
    OP_69(0x8, 0x0)
    LoadEffect(0x0, "map\\\\mp001_01.eff")
    PlayEffect(0x0, 0x0, 0xFF, 4840, 2000, 2560, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1500)

    ChrTalk(    #136
        0x8,
        (
            "#792FSo there was no serious damage\x01",
            "to the central factory... Thank goodness.\x02\x03",

            "#791FThe city has also remained calm for the\x01",
            "most part. I believe there is little to worry\x01",
            "about on that front.\x02\x03",

            "Yes, I understand. Please, continue to do\x01",
            "what you can.\x02\x03",

            "Farewell.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 0x1)
    Sleep(300)
    OP_22(0x83, 0x0, 0x64)
    OP_82(0x0, 0x0)
    Sleep(800)

    ChrTalk(    #137
        0x8,
        (
            "#792FYour timing is quite\x01",
            "serendipitous.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4666():
        OP_6D(2450, 0, -1640, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4666)

    def lambda_467E():
        OP_67(0, 6000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_467E)
    OP_8C(0x8, 270, 400)
    OP_8C(0x8, 180, 400)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4836")

    ChrTalk(    #138
        0x8,
        (
            "#791F#4PThank you for coming, Estelle,\x01",
            "Agate.\x02\x03",

            "I imagine your welcome at the\x01",
            "port was quite warm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1016F#5PAhaha... Yeah, kinda. It's been\x01",
            "a while, Kilika.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_475B():
        OP_6D(3350, 0, 330, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_475B)

    def lambda_4773():
        OP_67(0, 6000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4773)
    OP_43(0x101, 0x1, 0x1, 0x11)
    Sleep(250)
    OP_43(0x8, 0x1, 0x1, 0x15)
    Sleep(250)
    OP_43(0xF7, 0x1, 0x1, 0x12)
    Sleep(250)
    OP_43(0x105, 0x1, 0x1, 0x13)
    Sleep(250)
    OP_43(0x104, 0x1, 0x1, 0x14)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #140
        0x106,
        (
            "#051F#6PAnd as usual, you already know\x01",
            "everything that's happened.\x02\x03",

            "Good to see you again, Kilika.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49BD")

    label("loc_4836")


    ChrTalk(    #141
        0x8,
        (
            "#791F#4PThank you for coming, Estelle,\x01",
            "Scherazard.\x02\x03",

            "I imagine your welcome at the\x01",
            "port was quite warm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1016F#5PAhaha... Yeah, kinda. It's been\x01",
            "a while, Kilika.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_48E7():
        OP_6D(3550, 0, 330, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48E7)

    def lambda_48FF():
        OP_67(0, 6000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_48FF)
    OP_43(0x101, 0x1, 0x1, 0x11)
    Sleep(250)
    OP_43(0x8, 0x1, 0x1, 0x15)
    Sleep(250)
    OP_43(0xF7, 0x1, 0x1, 0x12)
    Sleep(250)
    OP_43(0x105, 0x1, 0x1, 0x13)
    Sleep(250)
    OP_43(0x104, 0x1, 0x1, 0x14)
    WaitChrThread(0x104, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #143
        0x103,
        (
            "#021F#6PAs always, you're two steps\x01",
            "ahead of everyone.\x02\x03",

            "#020FIt's good to see you again, Kilika.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49BD")


    ChrTalk(    #144
        0x8,
        (
            "#791FLikewise. I'm glad to see you here.\x02\x03",

            "And you two would be Olivier Lenheim\x01",
            "and Her Highness Princess Klaudia, I believe.\x01",
            "Or shall I say, Miss Kloe Rinz?\x02\x03",

            "I'm Kilika. I handle reception here at the\x01",
            "Zeiss branch of the guild.\x02\x03",

            "A pleasure to meet you two.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x105,
        "#048F#5PNo, the pleasure is ours.\x02",
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #146
        0x104,
        (
            "#037F#5PMy word, but your beauty eclipses\x01",
            "even what I expected...\x02\x03",

            "Madam, allow your humble servant\x01",
            "Olivier Lenheim to improvise a song t--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x8,
        (
            "#791FAccording to Jean, you've both\x01",
            "officially registered as assistants, yes?\x02\x03",

            "Assistants are free to use the rest\x01",
            "area upstairs, just as normal bracers do.\x02\x03",

            "Feel free to use it to relax, for meetings,\x01",
            "et cetera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x105,
        "#041F#5PThank you!\x02",
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #149
        0x104,
        "#036F#5PEr, yes, but my impro--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x8,
        (
            "#792FIf you wish to play your lute, you\x01",
            "are welcome to play it upstairs.\x02\x03",

            "Do restrain yourself to reasonable\x01",
            "limits, however, if you please.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #151
        0x104,
        "#034F#5PErm... Yes, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#1016F#6P(Wow, uh, I think Kilika might be\x01",
            "even harder on Olivier than Schera...)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4E4A")

    ChrTalk(    #153
        0x106,
        (
            "#551F#6PRight, anyway...\x02\x03",

            "#051FHow are things looking in\x01",
            "terms of work piled up?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4ECA")

    label("loc_4E4A")


    ChrTalk(    #154
        0x103,
        (
            "#021F#6PWell, putting aside our repressed\x01",
            "musician for now...\x02\x03",

            "#020FHow is the job situation looking?\x01",
            "Are we snowed under?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ECA")


    ChrTalk(    #155
        0x8,
        (
            "#792FWe do have some work posted, but\x01",
            "nothing urgent at the moment.\x02\x03",

            "You're welcome to attend to\x01",
            "it as you see fit.\x02\x03",

            "#790FBut... Hmm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#1004F#6PHuh?\x02\x03",

            "What's up, Kilika? You look like\x01",
            "you're thinking about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x8,
        (
            "#791FThis is...not a normal 'job,'\x01",
            "but a request from the guild.\x02\x03",

            "In your position as the group investigating\x01",
            "the Society of Ouroboros, I'd like you to\x01",
            "check on something.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_50EA")

    ChrTalk(    #158
        0x106,
        "#057F#6PWhat d'you...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_510E")

    label("loc_50EA")


    ChrTalk(    #159
        0x103,
        "#022F#6PCheck on something...?\x02",
    )

    CloseMessageWindow()

    label("loc_510E")


    ChrTalk(    #160
        0x101,
        "#1002F#6PUh, this is a bit sudden!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x105,
        "#043F#5PUm... What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "#790FIt's actually what you might expect.\x02\x03",

            "I want you to investigate the\x01",
            "earthquake that just happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#1015F#6PInvestigate the earthquake?\x02\x03",

            "You mean like go around asking about\x01",
            "damage? Well, sure, but what does...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x8,
        (
            "#792FWell, yes, that as well. However...\x02\x03",

            "Three days ago, a similar earthquake\x01",
            "occurred at the Wolf Fort.\x02\x03",

            "It lasted about ten seconds, and\x01",
            "the quake was not strong enough\x01",
            "to cause any real damage.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_534A")

    ChrTalk(    #165
        0x106,
        (
            "#552F#6PJust like the last quake we got.\x01",
            "Great...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5381")

    label("loc_534A")


    ChrTalk(    #166
        0x103,
        (
            "#522F#6PTwo earthquakes, then?\x01",
            "That's worrying...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5381")


    ChrTalk(    #167
        0x8,
        (
            "#790FThere's one particularly odd point,\x01",
            "however.\x02\x03",

            "The earthquake at the Wolf Fort\x01",
            "did not affect the City of Zeiss.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #168
        0x101,
        "#1004F#6PWait, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x104,
        (
            "#032F#5PWell, that IS strange.\x02\x03",

            "If I recall the map correctly, the\x01",
            "Wolf Fort is not far from the city.\x02\x03",

            "An earthquake centered there certainly\x01",
            "should've been felt here in the city,\x01",
            "to at least a small extent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x8,
        (
            "#790FIt was a weak quake, so it is possible\x01",
            "we simply did not notice.\x02\x03",

            "#792FStill, your friend is right.\x01",
            "It does seem unusual...unnatural.\x02\x03",

            "I cannot help but feel a terrible\x01",
            "sense of foreboding about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        (
            "#1007F#6PNo, I think I get it...\x02\x03",

            "#1002FJust like with our 'ghost,' weird stuff\x01",
            "like this makes me curious too.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_56C7")

    ChrTalk(    #172
        0x106,
        (
            "#051F#6PAnyway, sure, we'll take the job.\x02\x03",

            "Guess we should ask around the\x01",
            "city and at the Wolf Fort, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5740")

    label("loc_56C7")


    ChrTalk(    #173
        0x103,
        (
            "#020F#6PWe'll be happy to do what we can,\x01",
            "Kilika.\x02\x03",

            "We should begin by asking around\x01",
            "the city and the fort, I think.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5740")


    ChrTalk(    #174
        0x8,
        (
            "#791FYes. I'll be counting on you.\x02\x03",

            "Mr. Murdock is already gathering\x01",
            "information about the quake in the\x01",
            "city, however.\x02\x03",

            "I expect he'll be thorough, so you\x01",
            "don't need to worry about the city.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#1006F#6POkay, then, so off to the Wolf Fort!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x8,
        (
            "#792FWell...ultimately, this is just my\x01",
            "personal suspicion. Remember,\x01",
            "it's nothing urgent.\x02\x03",

            "Feel free to investigate as you see\x01",
            "fit while working on other jobs.\x02\x03",

            "#791FBesides, I believe you have someone\x01",
            "to say hello to, yes?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1008F#6POh... Umm, yeah...\x02\x03",

            "We saw a new Gospel too,\x01",
            "so we really should go see Tita\x01",
            "and Professor Russell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x105,
        "#542F#5PThat seems like a good idea, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x104,
        (
            "#030F#5PLet us delay our guild work\x01",
            "until we say hello, then.\x02\x03",

            "#031FCome! Let us reunite with\x01",
            "Tita with joyful hugs!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5ACD")

    def lambda_5A45():
        TurnDirection(0x101, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A45)

    def lambda_5A53():
        TurnDirection(0x105, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5A53)
    TurnDirection(0x106, 0x104, 400)

    ChrTalk(    #180
        0x106,
        (
            "#551F#6PWhen the heck did you take\x01",
            "the lead...?\x02\x03",

            "#050FEh, whatever.\x01",
            "Let's get to Gramps' workshop.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B6A")

    label("loc_5ACD")


    def lambda_5AD3():
        TurnDirection(0x103, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5AD3)

    def lambda_5AE1():
        TurnDirection(0x105, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5AE1)
    OP_8C(0x101, 186, 400)

    ChrTalk(    #181
        0x101,
        (
            "#1007F#4PI'll kindly ask you to not hug\x01",
            "anybody, thanks.\x02\x03",

            "#1006FStill, let's head over to Professor\x01",
            "Russell's place!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B6A")

    OP_A2(0x1408)
    OP_28(0x85, 0x4, 0x2)
    OP_28(0x85, 0x4, 0x8)
    OP_28(0x85, 0x1, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_6D(2550, 0, -2610, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2550, 0, -2610, 180)
    SetChrPos(0xF7, 2550, 0, -2610, 180)
    SetChrPos(0x105, 2550, 0, -2610, 180)
    SetChrPos(0x104, 2550, 0, -2610, 180)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_16_43FA end

    def Function_17_5C1E(): pass

    label("Function_17_5C1E")

    OP_8E(0xFE, 0x1086, 0x0, 0xFFFFFD3A, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_17_5C1E end

    def Function_18_5C3A(): pass

    label("Function_18_5C3A")

    OP_8E(0xFE, 0xC6C, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_5C3A end

    def Function_19_5C56(): pass

    label("Function_19_5C56")

    OP_8E(0xFE, 0x10CC, 0x0, 0xFFFFF862, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_19_5C56 end

    def Function_20_5C72(): pass

    label("Function_20_5C72")

    OP_8E(0xFE, 0xD34, 0x0, 0xFFFFF7CC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_20_5C72 end

    def Function_21_5C8E(): pass

    label("Function_21_5C8E")

    OP_8E(0x8, 0x1482, 0x0, 0x532, 0x7D0, 0x0)
    OP_8E(0x8, 0xDAC, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    Return()

    # Function_21_5C8E end

    def Function_22_5CBE(): pass

    label("Function_22_5CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CCF")
    Call(0, 27)

    label("loc_5CCF")

    OP_31(0x6, 0x0, 0x28)
    OP_31(0x6, 0xFE, 0x0)
    OP_41(0x6, 0xBC, 0xFF)
    OP_41(0x6, 0xFF, 0xFF)
    OP_41(0x6, 0x120, 0xFF)
    OP_41(0x6, 0x2C9, 0x0)
    OP_41(0x6, 0x25F, 0x2)
    OP_41(0x6, 0x2D1, 0x3)
    OP_35(0x6, 0x0)
    OP_35(0x6, 0x8C)
    OP_BB(0x6, 0x6, 0x104)
    EventBegin(0x0)
    OP_4A(0x8, 255)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrPos(0xB, 2770, 1050, 100, 0)
    SetChrPos(0xC, 3770, 1050, 100, 0)
    SetChrPos(0xD, 4770, 1050, 100, 0)
    OP_72(0x1, 0x4)
    OP_72(0x2, 0x4)
    OP_72(0x3, 0x4)
    OP_A1(0xB, 0x1)
    OP_A1(0xC, 0x2)
    OP_A1(0xD, 0x3)
    SetChrPos(0x9, 3400, 0, -790, 0)
    SetChrPos(0xA, 4460, 0, -720, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    OP_6D(1770, 0, -2950, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_43(0x101, 0x1, 0x1, 0x17)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x1, 0x18)
    Sleep(500)
    OP_43(0x105, 0x1, 0x1, 0x19)
    Sleep(500)
    OP_43(0x104, 0x1, 0x1, 0x1A)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x101, 0x1)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x104, 0x1)

    ChrTalk(    #182
        0x101,
        "#1004F#5PTita! Professor! What're you doing here?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    OP_8C(0xA, 180, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5EB8")

    ChrTalk(    #183
        0xA,
        "#061F#4POh! Estelle, Agate!\x02",
    )

    CloseMessageWindow()
    Jump("loc_5ED6")

    label("loc_5EB8")


    ChrTalk(    #184
        0xA,
        "#061F#4POh! Estelle! Hi!\x02",
    )

    CloseMessageWindow()

    label("loc_5ED6")


    ChrTalk(    #185
        0x9,
        "#101F#4PHah! Perfect timing.\x02",
    )

    CloseMessageWindow()

    def lambda_5EFE():
        OP_6D(3520, 0, -260, 3000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_5EFE)

    def lambda_5F16():
        OP_6D(3520, 0, -260, 3000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_5F16)

    def lambda_5F2E():
        OP_8E(0xFE, 0x1112, 0x0, 0xFFFFF916, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5F2E)
    Sleep(200)

    def lambda_5F4E():
        OP_8E(0xFE, 0xD02, 0x0, 0xFFFFF7CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_5F4E)
    Sleep(300)

    def lambda_5F6E():
        OP_8E(0xFE, 0x11D0, 0x0, 0xFFFFF4CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5F6E)
    Sleep(200)

    def lambda_5F8E():
        OP_8E(0xFE, 0xDC0, 0x0, 0xFFFFF380, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5F8E)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0xF7, 0x1)
    OP_8C(0xF7, 0, 400)
    WaitChrThread(0x105, 0x1)
    OP_8C(0x105, 0, 400)
    WaitChrThread(0x104, 0x1)
    OP_8C(0x104, 0, 400)
    WaitChrThread(0xA, 0x2)
    WaitChrThread(0xA, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_609D")

    ChrTalk(    #186
        0x106,
        (
            "#051F#3PWe've finished investigating the earthquakes...\x01",
            "so what're these hunks of junk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x9,
        (
            "#104F#4PJunk? How rude.\x02\x03",

            "#100FThese are the 'little things'\x01",
            "I promised you earlier!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_616D")

    label("loc_609D")


    ChrTalk(    #188
        0x101,
        (
            "#1011F#5PWe're done investigating the\x01",
            "earthquakes, but, uh...\x02\x03",

            "What're those machines there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x9,
        (
            "#101F#4PHeheheh! Good of you to ask,\x01",
            "m'dear!\x02\x03",

            "#100FThese are the 'little things' I promised\x01",
            "you earlier!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_616D")


    ChrTalk(    #190
        0x8,
        (
            "#792FWe can get to that in a moment.\x01",
            "First...\x02\x03",

            "#791FYou did, I assume, investigate the\x01",
            "Sanktheim Gate earthquake?\x02\x03",

            "I'd like to hear what you discovered\x01",
            "both there and at the Wolf Fort.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x101,
        "#1002F#5PRight, okay. So...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62FF")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as having heard about Walter in Zeiss\x01",          # 0
            "Set as having not heard about Walter in Zeiss\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_62F3"),
        (1, "loc_62F9"),
        (SWITCH_DEFAULT, "loc_62FF"),
    )


    label("loc_62F3")

    OP_A2(0x1480)
    Jump("loc_62FF")

    label("loc_62F9")

    OP_A3(0x1480)
    Jump("loc_62FF")

    label("loc_62FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6649")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #192
        (
            "\x07\x05Estelle reported what they had learned at the fort\x01",
            "and the gate.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #193
        0x9,
        (
            "#104F#4PHmmmm... So the earthquakes grow\x01",
            "stronger with each occurrence, eh?\x02\x03",

            "#102FThis is quite serious. Assuming the rate\x01",
            "of growth you describe is constant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xA,
        (
            "#063F#2PYeah...\x02\x03",

            "One even stronger than the Sanktheim one\x01",
            "hitting the city would be really, really bad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x8,
        (
            "#792FAnd the man in sunglasses seen at both\x01",
            "locations...\x02\x03",

            "#790FI would say it is all but certain that man\x01",
            "is an agent of Ouroboros.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#1002F#5PSomeone in town saw him too, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0x8,
        (
            "#790FYes. Mr. Murdock heard a report of a\x01",
            "man matching that description while\x01",
            "collecting information in the city for us.\x02\x03",

            "It seems he's also made an appearance\x01",
            "in Zeiss.\x02\x03",

            "Given that, I think helping Professor Russell\x01",
            "with his experiment is in our best interest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68C1")

    label("loc_6649")

    OP_2B(0x85, 0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #198
        (
            "\x07\x05Estelle reported what they had learned at the fort,\x01",
            "the gate, and in the city.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #199
        0x9,
        (
            "#104F#4PHmmmm... So the earthquakes grow\x01",
            "stronger with each occurrence, eh?\x02\x03",

            "#102FThis is quite serious. Assuming the rate\x01",
            "of growth you describe is constant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xA,
        (
            "#063F#2PYeah...\x02\x03",

            "One even stronger than the Sanktheim one\x01",
            "hitting the city would be really, really bad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0x8,
        (
            "#792FAnd the man in sunglasses seen at all\x01",
            "three locations...\x02\x03",

            "#790FI would say it is all but certain that man\x01",
            "is an agent of Ouroboros.\x02\x03",

            "Given that, I think helping Professor\x01",
            "Russell with his experiment is in our\x01",
            "best interest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_68FD")

    ChrTalk(    #202
        0x106,
        "#052F#3PAn experiment? What, with this junk?\x02",
    )

    CloseMessageWindow()
    Jump("loc_6974")

    label("loc_68FD")


    ChrTalk(    #203
        0x103,
        (
            "#027F#3PAhhhh, I see.\x02\x03",

            "Those devices the professor brought\x01",
            "will let us fight back with the power of\x01",
            "science, hmm?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6974")


    ChrTalk(    #204
        0x9,
        (
            "#101F#4PPrecisely so!\x02\x03",

            "#100FThese are septium vein measuring\x01",
            "instruments I developed years ago.\x02\x03",

            "When placed properly on the ground, they can\x01",
            "monitor the flow of a septium vein in real-time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x101,
        (
            "#1016F#5PSeptium... Er...\x02\x03",

            "#1008FI know I always ask these questions,\x01",
            "but, um...what's a 'septium vein'?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xA,
        (
            "#560F#2PThey're huge veins of septium ore\x01",
            "that run deep beneath the surface\x01",
            "of the earth!\x02\x03",

            "The energy flowing along them\x01",
            "slowly moves the surface.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6BFF")

    ChrTalk(    #207
        0x104,
        (
            "#035F#1PIn the distant past, they were referred\x01",
            "to as both 'earth veins' and 'spirit veins.'\x02\x03",

            "#030FAnd I believe in the distant East they're\x01",
            "currently called 'dragon veins,' no?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C97")

    label("loc_6BFF")


    ChrTalk(    #208
        0x103,
        (
            "#020F#3PIn the past, they were referred\x01",
            "to as both 'earth veins' and 'spirit veins.'\x02\x03",

            "And I believe in the East they're\x01",
            "called the 'dragon veins'?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C97")


    ChrTalk(    #209
        0x8,
        (
            "#791FVery knowledgeable. Just so.\x02\x03",

            "The peoples of the east have built their\x01",
            "greatest cities on places where dragon veins\x01",
            "converge since time immemorial.\x02\x03",

            "The ideal has always been to gather the\x01",
            "energy of the land and use it to give strength\x01",
            "to the nation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        "#1011F#5POh, okay then. I learned something!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x105,
        (
            "#043F#5PSo these devices can stop\x01",
            "earthquakes, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x9,
        (
            "#104F#4PNo, I'm afraid not.\x01",
            "These will only monitor the flows passively.\x02\x03",

            "#100FHowever, one leading theory is that\x01",
            "earthquakes are caused in part by septium\x01",
            "vein flows bending the earth.\x02\x03",

            "If we monitor the veins, therefore, we may\x01",
            "be able to discover something about\x01",
            "what's causing these blasted quakes!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0x105,
        (
            "#047F#5PI see.\x02\x03",

            "#040FThat means we need to make sure to set\x01",
            "these up before another earthquake occurs.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_700C")

    ChrTalk(    #214
        0x106,
        (
            "#051F#3PRight. So three devices means three places\x01",
            "you have in mind, right, Gramps?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7072")

    label("loc_700C")


    ChrTalk(    #215
        0x103,
        (
            "#020F#3PGiven that you brought three devices,\x01",
            "I take it you have three spots in mind,\x01",
            "Professor?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7072")


    ChrTalk(    #216
        0x9,
        "#102F#4PI do. Take a look at the map...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    def lambda_70AC():
        TurnDirection(0xA, 0x9, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_70AC)
    TurnDirection(0x101, 0x9, 400)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS134._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS204._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS205._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS206._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(150, 50, -1, -1)
    SetChrName("Professor Russell")

    AnonymousTalk(    #217
        (
            "\x07\x00#104FSo, I need you kids to set these up\x01",
            "in three locations in this region.\x02\x03",

            "#100FFirstly, on the northern Tratt Plains.\x01",
            "Where the Stone Circle is, specifically.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(150, 50, -1, -1)
    SetChrName("Professor Russell")

    AnonymousTalk(    #218
        (
            "\x07\x00#104FNext, smack dab in the middle of the Kaldia\x01",
            "Tunnel. From here, it's near the first bridge.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(150, 50, -1, -1)
    SetChrName("Professor Russell")

    AnonymousTalk(    #219
        "\x07\x00#100FAnd finally, in front of Leiston Fortress.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(150, 50, -1, -1)
    SetChrName("Professor Russell")

    AnonymousTalk(    #220
        (
            "\x07\x00#101FHere, here, and here. That's where\x01",
            "I need you to place the devices.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_C6(0x3, 0x6, 0, 0, 0)

    ChrTalk(    #221
        0x101,
        (
            "#1006F#5POkay, I've got all that down.\x02\x03",

            "So do we just need to set\x01",
            "them on the ground?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x9,
        (
            "#102F#4PI'm afraid it isn't quite that easy.\x02\x03",

            "You'll need to insert the sensor\x01",
            "needle into the ground at the right\x01",
            "angle, and also tune the antenna.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x104,
        (
            "#030F#5PAn antenna?\x01",
            "A transmission device, you mean.\x02\x03",

            "So these devices will transmit\x01",
            "the information gathered to another\x01",
            "location?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x9,
        (
            "#101F#4PHa! You're sharp!\x02\x03",

            "#100FThe antenna will send the data to our\x01",
            "calculating-orbment, the Capel, so we can\x01",
            "easily analyze the septium veins' movements.\x02\x03",

            "With the Capel, we can monitor\x01",
            "all three locations at once!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        (
            "#1007F#5PUh, that sounds pretty cool...I guess.\x02\x03",

            "#1011FWill you be coming with us to\x01",
            "help set this stuff up, Professor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x9,
        (
            "#100F#4PNo, I need to prepare the\x01",
            "Capel for all this.\x02\x03",

            "Tita knows what to do.\x01",
            "She can go with you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)

    ChrTalk(    #227
        0xA,
        "#067F#2PHeehee! I get to work with Estelle again!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7A3E")

    ChrTalk(    #228
        0x101,
        (
            "#1006F#5PAll righty! Tita's worth her weight\x01",
            "in mira, anyway!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #229
        0x101,
        (
            "#1019F#2PAgate, you have no complaints,\x01",
            "RIGHT?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #230
        0x106,
        (
            "#053F#3PWith a look like that...no.\x02\x03",

            "#051FJust don't daydream too much while\x01",
            "fiddling with the machines, shortstuff.\x02\x03",

            "Feel like if we left you to it, you\x01",
            "wouldn't even notice monsters until\x01",
            "you were actually in their mouths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xA,
        (
            "#562F#2PAww, Agate, you're mean!\x02\x03",

            "#560FBut, but, you'd save me if\x01",
            "that happened, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x106,
        "#551F#3PTch. ...Brat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#1001F#2PHa-ha! Tita: cuteness one,\x01",
            "Agate: zeee-ro!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B12")

    label("loc_7A3E")


    ChrTalk(    #234
        0x101,
        (
            "#1006F#5PAll righty! Tita's worth her weight\x01",
            "in mira, anyway!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #235
        0x101,
        "#1011F#2PYou don't mind, right, Schera?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #236
        0x103,
        (
            "#021F#3PNot at all.\x02\x03",

            "#526FWelcome aboard, Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xA,
        "#061F#2PThanks, Ms. Schera!\x02",
    )

    CloseMessageWindow()

    label("loc_7B12")

    OP_44(0x101, 0xFF)
    OP_8C(0x101, 315, 400)
    OP_8C(0xF7, 0, 400)
    OP_8C(0xA, 270, 400)

    ChrTalk(    #238
        0x9,
        (
            "#100F#4PWell, then! I need to start tuning the\x01",
            "Capel.\x02\x03",

            "Once you've placed all the measuring\x01",
            "instruments, head to the Operations\x01",
            "room in the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x101,
        "#1018F#5PWill do!\x02",
    )

    CloseMessageWindow()

    def lambda_7BEA():

        label("loc_7BEA")

        TurnDirection(0xA, 0x9, 400)
        OP_48()
        Jump("loc_7BEA")

    QueueWorkItem2(0xA, 3, lambda_7BEA)

    ChrTalk(    #240
        0xA,
        "#560F#4PWork hard, Grandpa!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 225, 400)

    def lambda_7C23():
        OP_6D(1600, 0, -4670, 3000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_7C23)

    def lambda_7C3B():

        label("loc_7C3B")

        TurnDirection(0x101, 0x9, 400)
        OP_48()
        Jump("loc_7C3B")

    QueueWorkItem2(0x101, 3, lambda_7C3B)

    def lambda_7C4C():

        label("loc_7C4C")

        TurnDirection(0xF7, 0x9, 400)
        OP_48()
        Jump("loc_7C4C")

    QueueWorkItem2(0xF7, 3, lambda_7C4C)

    def lambda_7C5D():

        label("loc_7C5D")

        TurnDirection(0x105, 0x9, 400)
        OP_48()
        Jump("loc_7C5D")

    QueueWorkItem2(0x105, 3, lambda_7C5D)

    def lambda_7C6E():

        label("loc_7C6E")

        TurnDirection(0x104, 0x9, 400)
        OP_48()
        Jump("loc_7C6E")

    QueueWorkItem2(0x104, 3, lambda_7C6E)
    OP_8E(0x9, 0x5A0, 0x0, 0xFFFFF966, 0x9C4, 0x0)
    OP_8E(0x9, 0x5F0, 0x0, 0xFFFFE750, 0x9C4, 0x0)
    OP_8E(0x9, 0x5DC, 0xFFFFFE0C, 0xFFFFE3F4, 0x9C4, 0x0)
    SetChrFlags(0x9, 0x4)

    def lambda_7CC0():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_7CC0)
    OP_8E(0x9, 0x618, 0xFFFFFE0C, 0xFFFFDFC6, 0x9C4, 0x0)
    SetChrFlags(0x9, 0x80)
    WaitChrThread(0x9, 0x3)
    OP_44(0x101, 0x3)
    OP_44(0xF7, 0x3)
    OP_44(0x105, 0x3)
    OP_44(0x104, 0x3)
    OP_44(0xA, 0x3)
    Sleep(500)

    def lambda_7D09():
        OP_6D(3500, 0, -505, 1500)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_7D09)

    def lambda_7D21():
        OP_8C(0xF7, 90, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_7D21)

    def lambda_7D2F():
        OP_8C(0x105, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7D2F)

    def lambda_7D3D():
        OP_8C(0x104, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7D3D)

    def lambda_7D4B():
        OP_8C(0xA, 180, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7D4B)
    OP_8C(0x101, 270, 400)
    WaitChrThread(0x9, 0x3)

    ChrTalk(    #241
        0x101,
        (
            "#1006F#2PSo we need to get all these set\x01",
            "up before the next earthquake.\x02\x03",

            "Let's get to it!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7E89")

    ChrTalk(    #242
        0x106,
        (
            "#052F#6PWhoa, before that.\x02\x03",

            "#051FOur group here's gettin' a little crowded.\x02\x03",

            "Might be a good idea to keep someone\x01",
            "here as backup, and to make sure we\x01",
            "don't go walkin' around with an army.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F3C")

    label("loc_7E89")


    ChrTalk(    #243
        0x103,
        (
            "#023F#6PAh, before that.\x02\x03",

            "#020FCoordinating a group THIS large\x01",
            "would be a little difficult.\x02\x03",

            "We should leave someone here\x01",
            "in reserve while the rest of us handle\x01",
            "the mission.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F3C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #244
        "\x07\x05Your combat party may only be made up of four people.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #245
        (
            "\x07\x05From here on out, when the time comes to form a party,\x01",
            "you may choose members aside from any story-mandated\x01",
            "members.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x1F4)
    Sleep(500)
    FadeToBright(0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_8045")
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)
    Jump("loc_8056")

    label("loc_8045")

    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x3, 0x4, 0xFFFF)

    label("loc_8056")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x80)
    OP_6D(2310, 0, -620, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF7, 3200, 0, -1260, 270)
    SetChrPos(0x101, 4240, 0, -1160, 270)
    SetChrPos(0x107, 4290, 0, -2310, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_810B")
    SetChrPos(0xE, 1680, 0, -1990, 90)
    SetChrPos(0x105, 3020, 0, -2400, 270)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_8132")

    label("loc_810B")

    SetChrPos(0xF, 1680, 0, -1990, 90)
    SetChrPos(0x104, 3020, 0, -2400, 270)
    ClearChrFlags(0xF, 0x80)

    label("loc_8132")

    Sleep(500)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82BB")

    ChrTalk(    #246
        0xE,
        (
            "#035F#6PHm. Well, then, I shall while\x01",
            "away my time upstairs.\x02\x03",

            "#030FShould you require a genius' help,\x01",
            "you need but say the word.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_81E3():

        label("loc_81E3")

        TurnDirection(0x101, 0xE, 400)
        OP_48()
        Jump("loc_81E3")

    QueueWorkItem2(0x101, 3, lambda_81E3)

    def lambda_81F4():

        label("loc_81F4")

        TurnDirection(0xF7, 0xE, 400)
        OP_48()
        Jump("loc_81F4")

    QueueWorkItem2(0xF7, 3, lambda_81F4)

    def lambda_8205():

        label("loc_8205")

        TurnDirection(0x105, 0xE, 400)
        OP_48()
        Jump("loc_8205")

    QueueWorkItem2(0x105, 3, lambda_8205)

    def lambda_8216():

        label("loc_8216")

        TurnDirection(0x107, 0xE, 400)
        OP_48()
        Jump("loc_8216")

    QueueWorkItem2(0x107, 3, lambda_8216)
    OP_8C(0xE, 315, 500)

    def lambda_822E():
        OP_6D(1550, 0, 430, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_822E)
    SetChrFlags(0xE, 0x4)
    OP_8E(0xE, 0xFFFFF8D0, 0x0, 0x51E, 0x9C4, 0x0)
    OP_8E(0xE, 0xFFFFF858, 0x0, 0x992, 0x9C4, 0x0)
    OP_8C(0xE, 90, 500)
    ClearChrFlags(0xE, 0x4)
    OP_8E(0xE, 0x9C4, 0x8CA, 0xAAA, 0x9C4, 0x0)

    def lambda_8293():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_8293)
    OP_8E(0xE, 0xFA0, 0xDAC, 0x99C, 0x9C4, 0x0)
    SetChrFlags(0xE, 0x80)
    Jump("loc_8409")

    label("loc_82BB")


    ChrTalk(    #247
        0xF,
        (
            "#040F#6PVery well. I'll be on the second floor.\x02\x03",

            "#041FIf you need me at any time,\x01",
            "don't hesitate to ask!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    def lambda_8334():

        label("loc_8334")

        TurnDirection(0x101, 0xF, 400)
        OP_48()
        Jump("loc_8334")

    QueueWorkItem2(0x101, 3, lambda_8334)

    def lambda_8345():

        label("loc_8345")

        TurnDirection(0xF7, 0xF, 400)
        OP_48()
        Jump("loc_8345")

    QueueWorkItem2(0xF7, 3, lambda_8345)

    def lambda_8356():

        label("loc_8356")

        TurnDirection(0x104, 0xF, 400)
        OP_48()
        Jump("loc_8356")

    QueueWorkItem2(0x104, 3, lambda_8356)

    def lambda_8367():

        label("loc_8367")

        TurnDirection(0x107, 0xF, 400)
        OP_48()
        Jump("loc_8367")

    QueueWorkItem2(0x107, 3, lambda_8367)
    OP_8C(0xF, 315, 500)

    def lambda_837F():
        OP_6D(1550, 0, 430, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_837F)
    SetChrFlags(0xF, 0x4)
    OP_8E(0xF, 0xFFFFF8D0, 0x0, 0x51E, 0x9C4, 0x0)
    OP_8E(0xF, 0xFFFFF858, 0x0, 0x992, 0x9C4, 0x0)
    OP_8C(0xF, 90, 500)
    ClearChrFlags(0xF, 0x4)
    OP_8E(0xF, 0x9C4, 0x8CA, 0xAAA, 0x9C4, 0x0)

    def lambda_83E4():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_83E4)
    OP_8E(0xF, 0xFA0, 0xDAC, 0x99C, 0x9C4, 0x0)
    SetChrFlags(0xF, 0x80)

    label("loc_8409")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #248
        (
            "\x07\x05Reserve party members will be on the second floor\x01",
            "of the local guildhouse.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #249
        (
            "\x07\x05By speaking with them, you may swap them out with\x01",
            "any party members who aren't mandatory.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_84E9():
        OP_6D(3500, 0, -505, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_84E9)
    OP_44(0x101, 0x3)
    OP_44(0xF7, 0x3)
    OP_44(0xF9, 0x3)
    OP_44(0x107, 0x3)

    def lambda_8511():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_8511)

    def lambda_851F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_851F)

    def lambda_852D():
        OP_8C(0x107, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_852D)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #250
        0x101,
        (
            "#1006F#6PThis should be okay, then.\x02\x03",

            "#1015FLesse, so we need to set up instruments\x01",
            "in the tunnel, on the north plains, and in\x01",
            "front of Leiston Fortress.\x02\x03",

            "Is there any order we should tackle that in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x8,
        (
            "#791FI shall leave that to your judgment.\x02\x03",

            "I will, however, contact Leiston ahead of you.\x02\x03",

            "If we explain our circumstances, I cannot\x01",
            "imagine they will take issue with our\x01",
            "gathering data in front of their gate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x101,
        "#1006F#6PGood idea.\x02",
    )

    CloseMessageWindow()

    def lambda_8703():
        OP_8C(0xF7, 135, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_8703)
    OP_8C(0x101, 270, 400)
    OP_8C(0x107, 315, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_876D")

    ChrTalk(    #253
        0x106,
        (
            "#051F#6PTime to move out, then.\x02\x03",

            "Tita, keep up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x107,
        "#061F#5POkaaay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_87D6")

    label("loc_876D")


    ChrTalk(    #255
        0x103,
        (
            "#020F#6PAway we go, then.\x02\x03",

            "#021FTita, sweetie, we're counting on you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x107,
        "#560F#5PI'll do my best!\x02",
    )

    CloseMessageWindow()

    label("loc_87D6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x1417)
    OP_28(0x87, 0x4, 0x2)
    OP_28(0x87, 0x4, 0x8)
    OP_28(0x87, 0x1, 0x1)
    OP_28(0x87, 0x1, 0x2)
    OP_28(0x87, 0x1, 0x4)
    OP_28(0x87, 0x1, 0x8)
    OP_4B(0x8, 255)
    OP_6D(3170, 0, -2350, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 3170, 0, -2350, 180)
    SetChrPos(0x1, 3170, 0, -2350, 180)
    SetChrPos(0x2, 3170, 0, -2350, 180)
    SetChrPos(0x3, 3170, 0, -2350, 180)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_22_5CBE end

    def Function_23_88BA(): pass

    label("Function_23_88BA")

    SetChrFlags(0x101, 0x4)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, 1480, -500, -8360, 0)
    ClearChrFlags(0x101, 0x80)

    def lambda_88E6():
        OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_88E6)
    OP_8E(0xFE, 0x60E, 0xFFFFFE0C, 0xFFFFE2DC, 0x7D0, 0x0)
    ClearChrFlags(0x101, 0x4)
    OP_8E(0x101, 0x974, 0x0, 0xFFFFED18, 0x7D0, 0x0)
    OP_8C(0x101, 0, 0)
    Return()

    # Function_23_88BA end

    def Function_24_8927(): pass

    label("Function_24_8927")

    SetChrFlags(0xFE, 0x4)
    OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xF7, 1480, -500, -8360, 0)
    ClearChrFlags(0xF7, 0x80)

    def lambda_8953():
        OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_8953)
    OP_8E(0xFE, 0x60E, 0xFFFFFE0C, 0xFFFFE2DC, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0xF7, 0x550, 0x0, 0xFFFFEC82, 0x7D0, 0x0)
    OP_8C(0xF7, 0, 0)
    Return()

    # Function_24_8927 end

    def Function_25_8994(): pass

    label("Function_25_8994")

    SetChrFlags(0xFE, 0x4)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x105, 1480, -500, -8360, 0)
    ClearChrFlags(0x105, 0x80)

    def lambda_89C0():
        OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_89C0)
    OP_8E(0xFE, 0x60E, 0xFFFFFE0C, 0xFFFFE2DC, 0x7D0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    OP_8E(0x105, 0x8DE, 0x0, 0xFFFFE89A, 0x7D0, 0x0)
    OP_8C(0x105, 0, 0)
    Return()

    # Function_25_8994 end

    def Function_26_8A01(): pass

    label("Function_26_8A01")

    OP_9F(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x104, 1480, -500, -8360, 0)
    ClearChrFlags(0x104, 0x80)

    def lambda_8A28():
        OP_9F(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_8A28)
    OP_8E(0xFE, 0x60E, 0xFFFFFE0C, 0xFFFFE2DC, 0x7D0, 0x0)
    OP_8E(0x104, 0x438, 0x0, 0xFFFFE7DC, 0x7D0, 0x0)
    OP_8C(0x104, 0, 0)
    Return()

    # Function_26_8A01 end

    def Function_27_8A64(): pass

    label("Function_27_8A64")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x151, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A85")
    OP_3F(0x151, 1)
    Jump("loc_905C")

    label("loc_8A85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_905C")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #257
        "\x07\x05Choose member to remove Zero Field Generator from.\x02",
    )

    CloseMessageWindow()
    OP_CC(0x0, 0x0, 0xA, 0xA, 0x0)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B02")
    Call(1, 28)
    Jump("loc_8B06")

    label("loc_8B02")

    Call(1, 29)

    label("loc_8B06")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B2D")
    Call(1, 28)
    Jump("loc_8B31")

    label("loc_8B2D")

    Call(1, 29)

    label("loc_8B31")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B58")
    Call(1, 28)
    Jump("loc_8B5C")

    label("loc_8B58")

    Call(1, 29)

    label("loc_8B5C")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8B83")
    Call(1, 28)
    Jump("loc_8B87")

    label("loc_8B83")

    Call(1, 29)

    label("loc_8B87")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(72, 320, 56, 3)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8BCE"),
        (1, "loc_8C14"),
        (2, "loc_8C5A"),
        (3, "loc_8CA0"),
        (SWITCH_DEFAULT, "loc_8CE6"),
    )


    label("loc_8BCE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BF1")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8C11")

    label("loc_8BF1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C11")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C11")

    Jump("loc_8CE6")

    label("loc_8C14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C37")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8C57")

    label("loc_8C37")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C57")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C57")

    Jump("loc_8CE6")

    label("loc_8C5A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C7D")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8C9D")

    label("loc_8C7D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C9D")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C9D")

    Jump("loc_8CE6")

    label("loc_8CA0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x1F), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CC3")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x1F, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8CE3")

    label("loc_8CC3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x3, 0x20), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8CE3")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0x20, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8CE3")

    Jump("loc_8CE6")

    label("loc_8CE6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D2D")

    AnonymousTalk(    #258
        "\x07\x05They are not equipped with a Zero Field Generator.\x02",
    )

    Jump("loc_904D")

    label("loc_8D2D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8D82")

    AnonymousTalk(    #259
        (
            "\x07\x05Estelle removed her Zero Field Generator. \x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_904D")

    label("loc_8D82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8DD5")

    AnonymousTalk(    #260
        (
            "\x07\x05Joshua removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_904D")

    label("loc_8DD5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E2C")

    AnonymousTalk(    #261
        (
            "\x07\x05Scherazard removed her Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_904D")

    label("loc_8E2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E80")

    AnonymousTalk(    #262
        (
            "\x07\x05Olivier removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_904D")

    label("loc_8E80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8ED1")

    AnonymousTalk(    #263
        (
            "\x07\x05Kloe removed her Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_904D")

    label("loc_8ED1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8F23")

    AnonymousTalk(    #264
        (
            "\x07\x05Agate removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_904D")

    label("loc_8F23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FAE")

    AnonymousTalk(    #265
        (
            "\x07\x05Tita removed her Zero Field Generator. Arts/crafts/normal\x01",
            "attacks now unavailable. S-Craft [Cannon Impulse] available.\x02",
        )
    )

    Jump("loc_904D")

    label("loc_8FAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FFE")

    AnonymousTalk(    #266
        (
            "\x07\x05Zin removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )

    Jump("loc_904D")

    label("loc_8FFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_904D")

    AnonymousTalk(    #267
        (
            "\x07\x05Kevin removed his Zero Field Generator.\x01",
            "Arts now unavailable.\x02",
        )
    )


    label("loc_904D")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_8A85")

    label("loc_905C")

    Return()

    # Function_27_8A64 end

    def Function_28_905D(): pass

    label("Function_28_905D")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_908A"),
        (1, "loc_90A5"),
        (2, "loc_90BF"),
        (3, "loc_90DD"),
        (4, "loc_90F8"),
        (5, "loc_9110"),
        (6, "loc_9129"),
        (7, "loc_9141"),
        (8, "loc_9158"),
        (SWITCH_DEFAULT, "loc_9171"),
    )


    label("loc_908A")

    OP_CC(0x1, 0x0, "[Estelle - Equipped]")
    Jump("loc_9171")

    label("loc_90A5")

    OP_CC(0x1, 0x0, "[Joshua - Equipped]")
    Jump("loc_9171")

    label("loc_90BF")

    OP_CC(0x1, 0x0, "[Scherazard - Equipped]")
    Jump("loc_9171")

    label("loc_90DD")

    OP_CC(0x1, 0x0, "[Olivier - Equipped]")
    Jump("loc_9171")

    label("loc_90F8")

    OP_CC(0x1, 0x0, "[Kloe - Equipped]")
    Jump("loc_9171")

    label("loc_9110")

    OP_CC(0x1, 0x0, "[Agate - Equipped]")
    Jump("loc_9171")

    label("loc_9129")

    OP_CC(0x1, 0x0, "[Tita - Equipped]")
    Jump("loc_9171")

    label("loc_9141")

    OP_CC(0x1, 0x0, "[Zin - Equipped]")
    Jump("loc_9171")

    label("loc_9158")

    OP_CC(0x1, 0x0, "[Kevin - Equipped]")
    Jump("loc_9171")

    label("loc_9171")

    Return()

    # Function_28_905D end

    def Function_29_9172(): pass

    label("Function_29_9172")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_919F"),
        (1, "loc_91BE"),
        (2, "loc_91DC"),
        (3, "loc_91FE"),
        (4, "loc_921D"),
        (5, "loc_9239"),
        (6, "loc_9256"),
        (7, "loc_9272"),
        (8, "loc_928D"),
        (SWITCH_DEFAULT, "loc_92AA"),
    )


    label("loc_919F")

    OP_CC(0x1, 0x0, "[Estelle - Not Equipped]")
    Jump("loc_92AA")

    label("loc_91BE")

    OP_CC(0x1, 0x0, "[Joshua - Not Equipped]")
    Jump("loc_92AA")

    label("loc_91DC")

    OP_CC(0x1, 0x0, "[Scherazard - Not Equipped]")
    Jump("loc_92AA")

    label("loc_91FE")

    OP_CC(0x1, 0x0, "[Olivier - Not Equipped]")
    Jump("loc_92AA")

    label("loc_921D")

    OP_CC(0x1, 0x0, "[Kloe - Not Equipped]")
    Jump("loc_92AA")

    label("loc_9239")

    OP_CC(0x1, 0x0, "[Agate - Not Equipped]")
    Jump("loc_92AA")

    label("loc_9256")

    OP_CC(0x1, 0x0, "[Tita - Not Equipped]")
    Jump("loc_92AA")

    label("loc_9272")

    OP_CC(0x1, 0x0, "[Zin - Not Equipped]")
    Jump("loc_92AA")

    label("loc_928D")

    OP_CC(0x1, 0x0, "[Kevin - Not Equipped]")
    Jump("loc_92AA")

    label("loc_92AA")

    Return()

    # Function_29_9172 end

    SaveToFile()

Try(main)
