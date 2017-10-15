from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3118_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3118_1 ._SN',
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
        "Function_1_324",          # 01, 1
        "Function_2_329",          # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x382), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7")
    Return()

    label("loc_B7")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0xE4E5A8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_148")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_IMUL), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_148")
    RunExpression(0x6, (scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x7, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_148")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    LoadEffect(0x0, "map\\\\mp108_00.eff")
    PlayEffect(0x0, 0x0, 0x0, 0, 0, 0, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Sleep(600)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0xF4240), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_RESULT, 0x7), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22D")
    EventBegin(0x1)
    OP_4A(0x9, 1)
    TurnDirection(0x0, 0x9, 400)
    OP_62(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x0)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x0)
    Call(1, 2)
    EventEnd(0x1)
    Jump("loc_31D")

    label("loc_22D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x4C4B40), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_284")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        "\x07\x05Response very nearby!\x02",
    )

    OP_22(0xAA, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_31D")

    label("loc_284")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x989680), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_2DF")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x07\x05Response in the vicinity.\x02",
    )

    OP_22(0xAA, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_31D")

    label("loc_2DF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "\x07\x05No response.\x02",
    )

    OP_22(0xAB, 0x0, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_31D")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_0_AA end

    def Function_1_324(): pass

    label("Function_1_324")

    Call(1, 2)
    Return()

    # Function_1_324 end

    def Function_2_329(): pass

    label("Function_2_329")

    EventBegin(0x0)
    OP_4A(0xA, 255)
    Fade(1000)
    OP_44(0x9, 0x0)
    SetChrPos(0x9, -5510, 0, -3140, 45)
    SetChrPos(0x101, -4640, 0, -2300, 225)
    SetChrPos(0xF7, -5400, 0, -1160, 180)
    SetChrPos(0xF8, -4170, 0, -1020, 225)
    SetChrPos(0xF9, -3520, 0, -2690, 270)
    OP_6D(-5020, 0, -2650, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        "\x07\x00Found #563i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x233, 1)
    OP_28(0x6F, 0x1, 0x400)
    OP_64(0x0, 0x1)

    ChrTalk(    #4
        0x101,
        (
            "#1007F#6PO-Oh, would you look at that.\x02\x03",

            "Antoine, you sneaky little cat!\x01",
            "So you were carrying one of the\x01",
            "parts!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4C8")

    ChrTalk(    #5
        0x106,
        (
            "#051F#3PThat one would've been easy\x01",
            "to miss.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FF")

    label("loc_4C8")


    ChrTalk(    #6
        0x103,
        (
            "#020F#3PThat one would've been very\x01",
            "easy to miss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58F")

    ChrTalk(    #7
        0x107,
        (
            "#560FCome to think of it, Erick said\x01",
            "he played with him for a bit.\x02\x03",

            "Maybe he found the part and\x01",
            "carried it back with him?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69F")

    label("loc_58F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61B")

    ChrTalk(    #8
        0x104,
        (
            "#030FI do recall Erick saying that he\x01",
            "played with him for a time.\x02\x03",

            "Perhaps he found the part and\x01",
            "brought it with him?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69F")

    label("loc_61B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69F")

    ChrTalk(    #9
        0x105,
        (
            "#040FThat's right, Erick said he played\x01",
            "with him for a bit.\x02\x03",

            "I'm sure he found the part and\x01",
            "brought it with him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69F")


    ChrTalk(    #10
        0x101,
        (
            "#1015FI think so, but...\x02\x03",

            "#1016FFor him to bring it with him?\x01",
            "Man.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #11
        0xA,
        "Myaon?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76C")

    ChrTalk(    #12
        0x108,
        (
            "#071FHaha, sorry, sorry.\x02\x03",

            "I'm sure we're just a pain to you,\x01",
            "stealing your toys and all that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_818")

    label("loc_76C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7BF")

    ChrTalk(    #13
        0x105,
        (
            "#041FHeehee. Sorry, Antoine.\x02\x03",

            "We have to take your toy away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_818")

    label("loc_7BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_818")

    ChrTalk(    #14
        0x104,
        (
            "#031FHeh, sorry, little kitten.\x02\x03",

            "I'm afraid we have to take your toy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_818")


    ChrTalk(    #15
        0x101,
        (
            "#1006FWe'll get Erick to make it up to you.\x02\x03",

            "See you later, Antoine.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #16
        0xA,
        "Nya～on.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    OP_43(0x9, 0x0, 0x0, 0x2)
    Return()

    # Function_2_329 end

    SaveToFile()

Try(main)
