from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'R1204   ._SN',
        MapName             = 'Bose',
        Location            = 'R1204.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        'Renne',                                # 9
        'Pater-Mater',                          # 10
        'Target Camera',                        # 11
        ' ',                                    # 12
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH03510 ._CH',             # 00
        'ED6_DT27/CH03511 ._CH',             # 01
        'ED6_DT26/CH20662 ._CH',             # 02
        'ED6_DT26/CH20288 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT27/CH03510P._CP',             # 00
        'ED6_DT27/CH03511P._CP',             # 01
        'ED6_DT26/CH20662P._CP',             # 02
        'ED6_DT26/CH20288P._CP',             # 03
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_14A",          # 00, 0
        "Function_1_250",          # 01, 1
        "Function_2_251",          # 02, 2
        "Function_3_35C",          # 03, 3
        "Function_4_205B",         # 04, 4
        "Function_5_2D81",         # 05, 5
        "Function_6_39F6",         # 06, 6
        "Function_7_545E",         # 07, 7
        "Function_8_5A28",         # 08, 8
        "Function_9_6F54",         # 09, 9
        "Function_10_6F9D",        # 0A, 10
        "Function_11_70DE",        # 0B, 11
        "Function_12_70EC",        # 0C, 12
        "Function_13_70FA",        # 0D, 13
        "Function_14_7153",        # 0E, 14
        "Function_15_71B7",        # 0F, 15
        "Function_16_82CD",        # 10, 16
        "Function_17_82EE",        # 11, 17
        "Function_18_8347",        # 12, 18
        "Function_19_A1BE",        # 13, 19
        "Function_20_A217",        # 14, 20
        "Function_21_A270",        # 15, 21
        "Function_22_A2D0",        # 16, 22
        "Function_23_A356",        # 17, 23
    )


    def Function_0_14A(): pass

    label("Function_0_14A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 2)), scpexpr(EXPR_END)), "loc_189")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x250A)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_24F")

    label("loc_189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_END)), "loc_1A9")
    OP_A3(0x2509)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_24F")

    label("loc_1A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_1D2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2508)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_24F")

    label("loc_1D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_1F2")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_24F")

    label("loc_1F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_212")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_24F")

    label("loc_212")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_232")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)
    Jump("loc_24F")

    label("loc_232")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_24F")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_24F")

    Return()

    # Function_0_14A end

    def Function_1_250(): pass

    label("Function_1_250")

    Return()

    # Function_1_250 end

    def Function_2_251(): pass

    label("Function_2_251")

    LoadEffect(0x0, "map\\\\mp207_00.eff")
    LoadEffect(0x1, "map\\\\mp207_01.eff")
    LoadEffect(0x2, "map\\\\mp207_02.eff")
    LoadEffect(0x3, "map\\\\mp207_03.eff")
    OP_6D(0, 0, 10000000, 0)
    OP_67(0, 0, -30000, 0)
    OP_6B(1000, 0)
    OP_6C(0, 0)
    OP_6E(276, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EF")
    Call(0, 3)

    label("loc_2EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300")
    Call(0, 4)

    label("loc_300")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_311")
    Call(0, 5)

    label("loc_311")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_322")
    Call(0, 6)

    label("loc_322")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_333")
    Call(0, 7)

    label("loc_333")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_344")
    Call(0, 8)

    label("loc_344")

    OP_84(0x0)
    OP_84(0x1)
    OP_84(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35B")
    Call(0, 15)

    label("loc_35B")

    Return()

    # Function_2_251 end

    def Function_3_35C(): pass

    label("Function_3_35C")

    EventBegin(0x1)
    OP_6D(0, 0, 10000000, 0)
    OP_67(0, 0, -30000, 0)
    OP_6B(1000, 0)
    OP_6C(0, 0)
    OP_6E(276, 0)
    OP_C4(0x0, 0x20000000)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_C4(0x0, 0x10)
    OP_48()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "#0C#40WI wander indifferently in a place that exists\x01",
            "beyond good and evil; beyond life and death.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #1
        (
            "#0C#40WThere is no fortune or misfortune. \x01",
            "No happiness. No sadness.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #2
        (
            "#0C#40WWhite and black tear into me, heaven and earth\x01",
            "torment me... I've been defiled.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #3
        "#0C#40WWhere does it begin, and where does it end?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #4
        "#0C#40WI don't belong anywhere. I'm not going anywhere.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #5
        "#0C#40WBut the world just keeps on turning around me...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6 op#A op#5
        "#20A#0C#4S1. Paradise#0C\x05\x02",
    )

    Sleep(300)
    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_1D(0xAF)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(80, 110, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #7
        "#12CWhich number would you like today?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 280, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #8
        "#12CFifteen.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 110, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #9
        "#12CCertainly.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #10
        (
            "#12CYou've been nominated, Renne.\x01",
            "Be sure to treat our customer with care.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "#0CThe place was simply known as 'Paradise.'#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #12
        (
            "#0CNo doubt the building itself had a proper name,\x01",
            "but none of us were ever told it.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #13
        (
            "#0CNor were we ever told exactly where in the land\x01",
            "we were, or what we were doing here...#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #14
        "#0COr, indeed, how we ended up there to begin with.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #15
        "#12CMorning.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("???")

    AnonymousTalk(    #16
        "#12C...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #17
        "#12CMorning, Renne.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 300, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #18
        "#12C...?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS570._CH")
    OP_C6(0x1, 0x3, -1, 3000, 0)
    OP_43(0x10, 0x3, 0x0, 0xE)
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    Sleep(3500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Boy")

    AnonymousTalk(    #19
        "#12COh, you've finally woken up.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 320, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #20
        "#12CHi, Cross.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS575._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #21
        "#12CHeehee...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #22
        "#12CWelcome to Paradise, Renne.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #23
        "#0CWelcome to Paradise.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C4(0x1, 0x800)
    FadeToBright(0, 0)
    OP_0D()
    OP_C6(0x0, 0x3, -1, 3000, 0)
    OP_C6(0x1, 0x3, 16777215, 3000, 0)
    FadeToDark(3000, 16777215, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #24
        (
            "#12CI'm going to have to go, Renne. \x01",
            "I've got to go and work.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(120, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #25
        "#12CAgain?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #26
        "#12CYeah. It's fine, though. I'll be back before long.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #27
        (
            "#12CBe a good girl and wait here in the meantime,\x01",
            "okay?#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    FadeToBright(2000, 16777215)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    FadeToBright(1, 0)
    OP_0D()
    OP_C4(0x0, 0x800)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #28
        (
            "#0CCross was always busy with work, and today was no\x01",
            "different.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #29
        (
            "#0CWhat exactly he did and where he did it, I didn't know,\x01",
            "but whatever it was, it was clearly horrible.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #30
        "#0CHe wasn't the only one, either.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #31
        (
            "#0CThe other children were always going out to work,\x01",
            "too.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_82(0x0, 0x0)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS576._CH")
    OP_C6(0x0, 0x3, -1, 1500, 0)
    Sleep(2500)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #32
        "#0CBut for some reason, no one ever called me.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #33
        (
            "#0CThe other children became weaker and more \x01",
            "emaciated by the day, and yet I spent my time\x01",
            "eating delicious food and playing with dolls.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #34
        "#0CI, and only I, was somehow special.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #35
        "#0CCross always referred to me as a princess.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    OP_C6(0x0, 0x3, 8947848, 1000, 0)
    Sleep(2000)
    OP_43(0x10, 0x3, 0x0, 0xE)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS570._CH")
    OP_C6(0x1, 0x3, -1, 2000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS573._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, 290, -1, -1)
    SetChrName("Girl")

    AnonymousTalk(    #36
        (
            "#12CMorning, Renne! It sure is beautiful out today,\x01",
            "huh? Kinda stuffy in here, though. Let's open a\x01",
            "window, okay?#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x0, 0x800)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "#0CThis girl's name is Etta.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #38
        (
            "#0CShe was always smiling and brimming with curiosity,\x01",
            "poking her nose into anything and everything in the\x01",
            "room and earning a scolding from Cross for it.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, 290, -1, -1)
    SetChrName("Etta")

    AnonymousTalk(    #39
        (
            "#12CHey, you wanna play with me? I wanna play with dolls,\x01",
            "too!#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #40
        (
            "#12CI don't mind, but do you even have the time?\x01",
            "Don't you have work later? Or do you not have\x01",
            "to go and wear any weird clothes today?#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 290, -1, -1)
    SetChrName("Etta")

    AnonymousTalk(    #41
        (
            "#12CCross is working at the moment, so I've got\x01",
            "some free time.#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #42
        (
            "#12CHeehee. He's sure been getting nominated a\x01",
            "lot lately. Maybe that's just what people are\x01",
            "into these days?#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #43
        (
            "#0CEtta was a somewhat precocious girl. She loved\x01",
            "making stupid jokes and giggling away at them.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS572._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #44
        (
            "#0CAdje, meanwhile, was more polite and mature.\x01",
            "Perhaps that was why she was nominated by\x01",
            "so many older men.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #45
        (
            "#0CAnother thing that stood out about her was the\x01",
            "way she never once acted like she hated her work;\x01",
            "no matter the day, she always performed with skill\x01",
            "and care.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #46
        (
            "#12CHow come you never seem to hate your work, Adje?\x01",
            "I thought it really hurt?#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("Adje")

    AnonymousTalk(    #47
        (
            "#12C...I'm fine. It's nothing you need to worry about,\x01",
            "Renne.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #48
        (
            "#12CThere's a few tricks that make it really simple to\x01",
            "manage once you know them.#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #49
        (
            "#12CSo don't worry about me. You just focus on being\x01",
            "happy like you always are.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #50
        "#12C...Okay.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("Adje")

    AnonymousTalk(    #51
        "#12CThat's a good girl. If you're happy, I'm happy.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS574._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #52
        (
            "#0CThen there was Quatre, whose small, delicate stature\x01",
            "always ended with him being battered and played with\x01",
            "roughly like he were some sort of doll.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #53
        "#12CDid you seriously end up getting beaten again?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Quatre")

    AnonymousTalk(    #54
        "#12CY-Yeah... I don't know why, either.#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #55
        (
            "#12CThey said it's some kind of new game,\x01",
            "but I don't get it...#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #56
        "#12C...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Quatre")

    AnonymousTalk(    #57
        "#12CDon't worry about me, Renne. I'm fine! Honest.#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #58
        (
            "#12CI'm used to it. It doesn't even hurt me anymore.\x01",
            "As long as I can come back and find you here,\x01",
            "I can deal with anything.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #59
        "#0CQuatre was always bleeding out of our sight.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #60
        "#0CMaybe that was part of his charm.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #61
        (
            "#0CI'm sure beautiful people must shed beautiful\x01",
            "blood.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x7, 0x0, 0x64)
    Sleep(1000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0xFEC0, 0xFE20, 0x140, 0x0, 0x140, 0x1E0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS575._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #62
        (
            "#12CI'm back, Renne. Sorry--that ended up taking\x01",
            "longer than I thought it would.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #63
        (
            "#0CThen, finally, there was Cross. He was basically\x01",
            "our leader.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS572._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS573._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS574._CH")
    OP_C6(0x0, 0x1, 800, 800, 0)
    OP_C6(0x2, 0x1, 600, 600, 0)
    OP_C6(0x3, 0x1, 700, 700, 0)
    OP_C6(0x4, 0x1, 500, 500, 0)
    OP_C6(0x2, 0x0, 300000, 200000, 0)
    OP_C6(0x3, 0x0, -120000, 150000, 0)
    OP_C6(0x4, 0x0, 50000, 250000, 0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    Sleep(1000)
    OP_C6(0x3, 0x3, -1, 1000, 0)
    Sleep(500)
    OP_C6(0x2, 0x3, -1, 1000, 0)
    Sleep(500)
    OP_C6(0x4, 0x3, -1, 1000, 0)
    Sleep(500)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    OP_C6(0x2, 0x3, -7829368, 500, 0)
    OP_C6(0x3, 0x3, -7829368, 500, 0)
    OP_C6(0x4, 0x3, -7829368, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #64
        "#0CCross, Etta, Adje, Quatre, and me...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #65
        (
            "#0CEach of them were so dear to me, and we spent\x01",
            "all the time we could together in this one room.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #66
        (
            "#0CTo my understanding, there were other children\x01",
            "in the building, but they didn't matter to me.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #67
        (
            "#0CThe only ones who did were the four friends\x01",
            "I spent my days with--the four who lived in\x01",
            "Paradise alongside me.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x0, 0x3, 8947848, 2000, 0)
    OP_C6(0x1, 0x3, 8947848, 2000, 0)
    OP_C6(0x2, 0x3, 8947848, 2000, 0)
    OP_C6(0x3, 0x3, 8947848, 2000, 0)
    OP_C6(0x4, 0x3, 8947848, 2000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C7(0x0, 0x3, 0x3)
    OP_C7(0x0, 0x4, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_3_35C end

    def Function_4_205B(): pass

    label("Function_4_205B")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    OP_C4(0x0, 0x10)
    OP_48()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #68 op#A op#5
        "#20A#0C#4S2. Princess#0C\x05\x02",
    )

    Sleep(300)
    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Sleep(500)
    OP_1D(0xB7)
    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0xE)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS570._CH")
    OP_C6(0x1, 0x3, -1, 2000, 0)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    Sleep(500)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #69
        "#12CHey, Cross? What happened to the others?#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #70
        "#12CHow come it's just me and you in here now?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0xFEC0, 0xFE20, 0x140, 0x0, 0x140, 0x1E0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS575._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #71
        "#12CAhaha. What are you talking about, Renne?#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #72
        (
            "#12CWhat others? It's always been just you and me\x01",
            "in here.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #73
        (
            "#12CReally? Are you sure? I feel like there were\x01",
            "more...#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #74
        (
            "#12CNope, there weren't. It's always been just you\x01",
            "and me.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    OP_C6(0x0, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #75
        (
            "#0CIt was only later when I realized it was Cross\x01",
            "who had hidden the others from me.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #76
        (
            "#0CWhether that was so I didn't have to worry about\x01",
            "them or because things had gotten so bad he\x01",
            "didn't even think I should see them, I don't know.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #77
        (
            "#0CBut he always tried to keep my eyes covered from\x01",
            "the harsh reality of what was going on around me,\x01",
            "so I could keep living in blissful ignorance.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS573._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1500)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, 290, -1, -1)
    SetChrName("Etta")

    AnonymousTalk(    #78
        (
            "#12CLet me give you a useful tip, Renne: always be\x01",
            "sure to say, 'It would be my pleasure.'#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #79
        "#12CSaying that makes everyone smile!#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #80
        (
            "#12CNo matter what you have to do or what people do to\x01",
            "you, always respond with, 'It would be my pleasure.'#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #81
        (
            "#12CHeehee. Funny how that works, right? After all,\x01",
            "it's the customers you're pleasing, not you!#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS572._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("Adje")

    AnonymousTalk(    #82
        (
            "#12CLet me give you one, too, then. I use this all the\x01",
            "time.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #83
        (
            "#12CThe best thing to do is try to imagine how your\x01",
            "customer is feeling. Like, this must feel really good\x01",
            "for them, they seem to love me doing this, or...#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #84
        (
            "#12CIt's not enough to make you stop feeling pain,\x01",
            "but it does stop you needing to worry about\x01",
            "doing unpleasant things.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #85
        (
            "#12CAlways try to think about what you can do to make\x01",
            "the customer happy. That's key.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS574._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, 300, -1, -1)
    SetChrName("Quatre")

    AnonymousTalk(    #86
        "#12CW-Well, I suppose I should say something, too...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #87
        (
            "#12CUmm... You should never cry and say you're sorry\x01",
            "to a customer.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #88
        (
            "#12CSaying sorry just makes them want to hurt you\x01",
            "more.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #89
        (
            "#12CNo matter how much it hurts, no matter how sad\x01",
            "you feel, don't ever cry. Don't ever say sorry,\x01",
            "because no one ever forgives you even if you do.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C6(0x1, 0x3, 16777215, 2000, 0)
    Sleep(2000)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS592._CH")
    OP_C6(0x0, 0x3, -1, 1500, 0)
    Sleep(2500)
    SetMessageWindowPos(-1, 330, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #90
        (
            "#12CThanks, everyone. But I can't see myself needing\x01",
            "any of these tips.#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #91
        "#12CI never have to do any work.#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #92
        (
            "#12CAll I have to do is sit in here and hug my dolls.\x01",
            "I never have to leave this room.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 80, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #93
        "#12CAnd that's how it should be.#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #94
        (
            "#12CYou're our princess, and you're really,\x01",
            "really important to us.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #95
        (
            "#12C#40WWe're all here to protect you, and that's why\x01",
            "we make it so you don't need to see a thing.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #96
        "#12C#40W'Renne.'#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C7(0x1, 0xFF, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_205B end

    def Function_5_2D81(): pass

    label("Function_5_2D81")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    OP_C4(0x0, 0x10)
    OP_48()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #97 op#A op#5
        "#20A#0C#4S3. Game#0C\x05\x02",
    )

    Sleep(300)
    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_1D(0xAE)
    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0xE)
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS570._CH")
    OP_C6(0x1, 0x3, -1, 2000, 0)
    Sleep(2000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS575._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #98
        "#12CWhat are you doing, Renne?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #99
        "#12CI'm drawing.#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #100
        (
            "#12CLook! This is a monster. The monster that's got\x01",
            "us locked up in here.#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #101
        (
            "#12CIt's got golden eyes and black scales, and its\x01",
            "mouth's stained red with the blood of all the\x01",
            "people it ate.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #102
        "#12CThe color of sin, huh? How lovely.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #103
        (
            "#12CIts stomach's got to be white, though. Otherwise\x01",
            "you wouldn't know which side was the front.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #104
        "#12CAhaha. That's very true.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #105
        "#12C...?#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #106
        "#12CWhere is everyone? Are they all out working?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #107
        "#12C...Renne.#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #108
        (
            "#12CThere are no 'others.' There's only me and you\x01",
            "here.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x0, 0x0, 0xB)
    PlayEffect(0xCB, 0x3, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    SetMessageWindowPos(100, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #109
        "#12CReally? Are you sure? I don't know...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 250, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #110
        (
            "#12CI'm sure. From the very start, it's just been me\x01",
            "and you.#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #111
        "#12CNo others. Now let's draw together, shall we?#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #112
        (
            "#12CMaybe we could draw a princess next? That'd be\x01",
            "nice.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #113
        (
            "#0CCross was doing a good job at covering my eyes\x01",
            "from reality, but there was one thing he couldn't\x01",
            "completely keep from me:#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #114
        "#0CHe was getting tired.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #115
        (
            "#0CAfter the others disappeared, he started taking on\x01",
            "all of the work himself. And because of that, slowly,\x01",
            "he began to vanish, too.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C7(0x1, 0xFF, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x19, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS578._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x19, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS580._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x19, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS579._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS570._CH")
    OP_43(0x10, 0x3, 0x0, 0xE)
    OP_C6(0x3, 0x3, -1, 2000, 0)
    Sleep(2000)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #116
        (
            "#12CLet's clean you up, Renne. You're really dirty\x01",
            "today.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 330, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #117
        "#12CThanks. You're always so kind.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #118
        "#12C...I'm sorry, Renne.#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #119
        "#12CIf I wasn't so hopeless...#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #120
        "#12CI swore I'd protect you, and yet...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 330, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #121
        (
            "#12CWhat's wrong, Cross? You're not looking too \x01",
            "good...#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #122
        "#12CIt's nothing. I'm fine.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 330, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #123
        "#12C...Cross?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 50, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #124
        "#12C...#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #125
        "#12CI just told you that I'm fine!#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #126
        "#12C#40W...This is all your fault.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 330, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #127
        "#12C...Mine?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(300, 75, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #128
        "#12C#40WYours. Everything is YOUR fault.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(800)
    SetMessageWindowPos(50, 120, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #129
        (
            "#12C#40WYou wasted no time in killing all the others.\x01",
            "Why are you letting me live for so long?#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(800)
    SetMessageWindowPos(-1, 200, -1, -1)
    SetChrName("Cross")

    AnonymousTalk(    #130
        (
            "#2CIt's all your fault. Why haven't you killed me?\x01",
            "It's all your fault. Why haven't you killed me?\x01",
            "It's all your fault. Why haven't you killed me?#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x2, 0x3)
    OP_20(0xBB8)
    OP_21()
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #131
        "#2C#40WI'm already dead as it is... Why won't you kill me?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    OP_C7(0x1, 0xFF, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_5_2D81 end

    def Function_6_39F6(): pass

    label("Function_6_39F6")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    OP_C4(0x0, 0x10)
    OP_48()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #132 op#A op#5
        "#20A#0C#4S4. Renne#0C\x05\x02",
    )

    Sleep(300)
    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #133
        "#0CEventually, my first job came.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #134
        (
            "#0CThere was no one else to take it. \x01",
            "There was no one else to go out in my place.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #135
        (
            "#0CThat's why I had to do it myself. I had to step\x01",
            "outside that room for the first time.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_1D(0xAF)
    Sleep(500)
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS571._CH")
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x32, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS580._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x32, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS577._CH")
    OP_43(0x10, 0x3, 0x0, 0xE)
    OP_C6(0x2, 0x3, -1, 2000, 0)
    Sleep(2000)
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(60, 60, -1, -1)
    SetChrName("Owner")

    AnonymousTalk(    #136
        (
            "#12CYou've been nominated, Renne.\x01",
            "Be sure to treat our customer with care.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #137
        "#12C...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 60, -1, -1)
    SetChrName("Owner")

    AnonymousTalk(    #138
        (
            "#12CWhat are you doing, Renne?\x01",
            "Just do what you usually do.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #139
        "#12C...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 50, -1, -1)
    SetChrName("Customer")

    AnonymousTalk(    #140
        (
            "#12CWhat's going on here? I was led to believe number\x01",
            "fifteen was special. #0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(60, 60, -1, -1)
    SetChrName("Owner")

    AnonymousTalk(    #141
        (
            "#12CShe's not normally like this, I can assure you.\x01",
            "She's usually a good girl... I don't know what's\x01",
            "gotten into her.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #142
        (
            "#12CShe's our little angel, capable of meeting all of\x01",
            "our customers' needs no matter what they may\x01",
            "be.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #143
        (
            "#12CCome on, Renne. Say hello. You've done this\x01",
            "enough times, now.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #144
        (
            "#12CWhat are you going to be today?\x01",
            "A sweet doll? A cool boy?#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #145
        "#12C...That wasn't me.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 60, -1, -1)
    SetChrName("Owner")

    AnonymousTalk(    #146
        "#12C...What?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #147
        (
            "#12CThat wasn't me.\x01",
            "That wasn't me.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 350, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #148
        "#12C#3SThat wasn't me! That wasn't me!#2S#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #149
        "#12C#3SThat wasn't me!#2S#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #150
        "#12C#3SThat wasn't me!#2S#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    OP_C6(0x2, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_82(0x0, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #151
        (
            "#0C#40WSomeone says something. I close my ears like always.\x01",
            "Someone does something. I close my eyes like always.\x01",
            "I do just as I always do.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #152
        (
            "#0C#60WI do just as I always do.\x01",
            "I do just as I always do.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #153
        "#0C#80WI do just as I always do and go out to work.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1, 0)
    OP_0D()
    Sleep(500)
    OP_22(0x165, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #154
        "#17CAh, the water of life.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #155
        (
            "#17CCross once said that even those near to death\x01",
            "could be full of energy again if they drank this.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #156
        (
            "#17CHe said he was made to drink it all the time,\x01",
            "and that its taste was sweet and syrupy. #0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x800)
    Sleep(1000)
    SetMessageWindowPos(80, 110, -1, -1)
    SetChrName("Owner")

    AnonymousTalk(    #157
        (
            "#12CDrink up, Renne. I mixed quite a lot of syrup\x01",
            "in today.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #158
        (
            "#12CDrink up, nicely and slowly. That's it...\x01",
            "That's it... Make sure not to spill any, now.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #159
        "#12CDrink up every last drop.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #160
        "#12C...Well, please take your time.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #161
        (
            "#17C#40WAs the owner went to leave, his head seemed to\x01",
            "distort slightly. Maybe he's getting old, or maybe\x01",
            "he's just wearing a disguise of some kind...#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #162
        "#17C#60W...Oh, the medicine's started kicking in.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_43(0x10, 0x3, 0x0, 0xE)
    FadeToBright(3000, 16777215)
    OP_C6(0x2, 0x3, -1, 3000, 0)
    Sleep(1000)
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    OP_C7(0x0, 0x2, 0x3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    SetMessageWindowPos(330, 100, -1, -1)
    SetChrName("Customer")

    AnonymousTalk(    #163
        (
            "#12CWell, Renne. Why don't we sit and have a little\x01",
            "chat together?#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 280, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #164
        "#12CIt would be my pleasure.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 80, -1, -1)
    SetChrName("Customer")

    AnonymousTalk(    #165
        "#12CYou're always such a good girl.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #166
        "#0C#40WIt would be my pleasure.#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #167
        "#0C#40WIt would be my pleasure.#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #168
        (
            "#0CIt would be my pleasure. It would be my pleasure.\x01",
            "It would be my pleasure. It would be my pleasure.\x01",
            "It would be my pleasure. It would be my pleasure.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x13, 0x0, 0x0, 0xA)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #169
        (
            "#50W#0CMorning, Renne! It sure is beautiful out today, huh?\x01",
            "Kinda stuffy in here, though. Let's open a window,\x01",
            "okay? Hey, you wanna play with me? #30WI wanna\x01",
            "play with dolls, too! #20WCross is working#10W at\x01",
            "the moment, so I've got some free time. Heehee.\x01",
            "He sure seems to be getting nominated a lot lately.\x01",
            "Maybe that's just what people are into these days?\x01",
            "Let me give you a useful tip, Renne: always be sure to\x01",
            "say, 'It would be my pleasure.' Saying that makes\x01",
            "everyone smile! No matter what you have to do or what\x01",
            "people do to you, always say, 'It would be my pleasure.'\x01",
            "Heehee. Funny how that works, right? After all, it's the\x01",
            "customers you're pleasing, not you! We're all here to\x01",
            "protect you and that's why we make it so you don't need\x01",
            "to see a thing. \x01",
            "                                         'Renne'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #170
        (
            "#50W#0C...I'm fine. It's nothing you need to worry about, Renne.\x01",
            "#40WThere's a few tricks that make it really #30Wsimple to\x01",
            "manage once you know them. So don't worry about me.\x01",
            "You just focus on being#20W happy like you always are.\x01",
            "That's a good girl.#10W If you're happy, I'm happy. Let me\x01",
            "give you one, too, then. I use this all the time. The best\x01",
            "thing to do is try to imagine how your customer is feeling.\x01",
            "Like, this must feel really good for them, they seem to love\x01",
            "me doing this, or... It's not enough to make you stop feeling\x01",
            "pain, but it does stop you needing to worry about doing\x01",
            "unpleasant things. Always try to think about what you can do \x01",
            "to make the customer happy. That's key. We're all here to\x01",
            "protect you, and that's why we make it so you don't need to\x01",
            "see a thing.\x01",
            "                                         'Renne'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #171
        (
            "#50W#0CY-Yeah... I don't know why, either... They said#40W it's\x01",
            "some kind of new game, but I don't get it...#30W Don't\x01",
            "worry about me, though. I'm fine! Honest.#20W I'm used\x01",
            "to it. It doesn't even hurt me anymore.#10W As long as I\x01",
            "can come back and find you here, I can deal with anything.\x01",
            "W-Well, I suppose I should say something, too... Umm...\x01",
            "You should never cry and say you're sorry to a customer.\x01",
            "Saying sorry just makes them want to hurt you more. No\x01",
            "matter how much it hurts, no matter how sad you feel,\x01",
            "don't ever cry. Don't ever say sorry, because no one ever\x01",
            "forgives you even if you do. We're all here to protect you,\x01",
            "and make it so you don't need to see a thing. So don't you\x01",
            "worry.                              \x01",
            "                                         'Renne'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #172
        (
            "#40W#0CWhat are you doing, Renne? The color of sin, huh?\x01",
            "How lovely. #30WAhaha. That's very true.#20W ...Renne.\x01",
            "There are no 'others.' There's only me#10W and you here.\x01",
            "I'm sure. From the very start, it's just been me and you.\x01",
            "No others. Now let's draw together, shall we? #5WI just told\x01",
            "you that I'm fine! ...This is all your fault. This is all your fault.\x01",
            "Everything is YOUR fault. You wasted no time in killing all the\x01",
            "others. Why are you letting me live for so long? It's all your\x01",
            "fault. Why haven't you killed me? It's all your fault. Why haven't \x01",
            "you killed me? It's all your fault. Why haven't you killed me?\x01",
            "I'm already dead as it is... Why won't you kill me?#60W\x01",
            "                                         'Renne'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_23(0x18E)
    OP_82(0x0, 0x0)
    OP_44(0x13, 0x0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #173
        "#2CAll of them have gone.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xC1, 0x0, 0x64)
    OP_C6(0x2, 0x3, 16777215, 100, 0)
    Sleep(2000)
    OP_C7(0x1, 0xFF, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_6_39F6 end

    def Function_7_545E(): pass

    label("Function_7_545E")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    OP_48()
    OP_C4(0x0, 0x800)
    Sleep(500)
    OP_22(0x87, 0x0, 0x64)
    Sleep(2000)
    OP_43(0x10, 0x1, 0x0, 0x17)
    Sleep(2000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS581._CH")
    OP_C6(0x0, 0x3, -1, 1500, 0)
    OP_43(0x10, 0x3, 0x0, 0xE)
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 2000)
    PlayEffect(0xC9, 0x1, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 5000)
    OP_E7(0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0)
    OP_E7(0x0, 0x1, 0xFF, 0xFF, 0xFF, 0xFF, 1500)
    Sleep(1000)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(500)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x10, 0x1)
    OP_22(0x226, 0x0, 0x64)
    Sleep(800)
    OP_22(0x38F, 0x0, 0x64)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(300)
    OP_22(0x389, 0x0, 0x64)
    Sleep(500)
    OP_22(0x38F, 0x0, 0x64)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x226, 0x0, 0x64)
    Sleep(500)
    OP_22(0x389, 0x0, 0x64)
    Sleep(800)
    OP_22(0x38F, 0x0, 0x64)
    Sleep(300)
    OP_22(0x38F, 0x0, 0x64)
    Sleep(500)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(300)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    OP_E7(0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 1000)
    OP_C7(0x0, 0x0, 0x3)
    OP_24(0x87, 0x5F)
    Sleep(100)
    OP_24(0x87, 0x5A)
    Sleep(100)
    OP_24(0x87, 0x55)
    Sleep(100)
    OP_24(0x87, 0x50)
    Sleep(100)
    OP_24(0x87, 0x4B)
    Sleep(100)
    OP_24(0x87, 0x46)
    Sleep(1500)
    OP_C7(0x1, 0x0, 0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS582._CH")
    OP_C6(0x0, 0x3, -8947849, 2000, 0)
    OP_82(0x1, 0x0)
    PlayEffect(0xCA, 0x1, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 5000)
    OP_E7(0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0)
    OP_E7(0x0, 0x1, 0xFF, 0xFF, 0xFF, 0xFF, 1500)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(380, 220, -1, -1)
    SetChrName("Silver-Haired Youth")

    AnonymousTalk(    #174
        "#12CWhat in...?#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #175
        "#12CThose subhuman monsters...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 350, -1, -1)
    SetChrName("Black-Haired Boy")

    AnonymousTalk(    #176
        "#12C...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #177
        "#12CCan people even keeping living on like this?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #178
        "#12CCan you even call someone in this state alive?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(380, 220, -1, -1)
    SetChrName("Silver-Haired Youth")

    AnonymousTalk(    #179
        "#12C...#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #180
        (
            "#12CI'm guessing she inflicted all these cross-like\x01",
            "marks on herself.#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #181
        "#12CProbably in order to maintain her own sanity.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 350, -1, -1)
    SetChrName("Black-Haired Boy")

    AnonymousTalk(    #182
        "#12C...#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #183
        "#12CShe wanted to keep living that much...?#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #184
        "#12C(This is a living human...)#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C6(0x0, 0x3, 16777215, 3000, 0)

    def lambda_5919():
        OP_E7(0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 3000)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_5919)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_22(0x166, 0x0, 0x64)
    OP_24(0x87, 0x3C)
    Sleep(100)
    OP_24(0x87, 0x32)
    Sleep(100)
    OP_24(0x87, 0x28)
    Sleep(100)
    OP_24(0x87, 0x1E)
    Sleep(100)
    OP_24(0x87, 0x19)
    Sleep(100)
    OP_24(0x87, 0xA)
    Sleep(100)
    OP_23(0x87)
    Sleep(7000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Black-Haired Boy")

    AnonymousTalk(    #185
        (
            "#12CI want to see what she's like when she's\x01",
            "really alive, Loewe.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #186
        "#12CCan we take her in to the society?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_C7(0x1, 0xFF, 0x0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_7_545E end

    def Function_8_5A28(): pass

    label("Function_8_5A28")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x10)
    OP_48()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #187 op#A op#5
        "#20A#0C#4S5. The Dream Goes On#0C\x05\x02",
    )

    Sleep(300)
    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_1D(0xB2)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #188
        (
            "#0C#40W'You're strong, Renne.'\x01",
            "That was what Joshua told me one day.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #189
        "#0C#40W...It wasn't something I'd heard before, either.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS583._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS584._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS585._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS586._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #190
        "#0C#40WYou're strong, Renne.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)

    AnonymousTalk(    #191
        "#0C#40WYes. I am.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(1000)

    AnonymousTalk(    #192
        (
            "#0CI'm strong. I'm strong.\x01",
            "I'm strong. I'm strong.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(1000)

    AnonymousTalk(    #193
        "#0CI'm strong. I'm strong!#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #194
        (
            "#0CAs an Enforcer candidate, 'Renne' proved to be\x01",
            "exceptionally capable.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C7(0x0, 0x3, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #195
        "#0C#40WThen one day, Joshua disappeared.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #196
        "#0C#40WAnd the world just kept on turning.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_43(0x10, 0x3, 0x0, 0xE)
    PlayEffect(0xC8, 0x0, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 5000)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS587._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS588._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS589._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS590._CH")
    OP_C5(0x4, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS591._CH")
    OP_C6(0x0, 0x3, -1, 1500, 0)
    Sleep(2500)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #197
        "#12C*sigh* Just where has Joshua gone, anyway?#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #198
        (
            "#12CAll he said was that he was going away to do a job\x01",
            "and it was going to take a while...#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #199
        (
            "#12CI wanted him to know that I've become a proper\x01",
            "Enforcer now.#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #200
        (
            "#12CI wanted to introduce him to my real Papa and \x01",
            "Mama, too...#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #201
        "#12C...#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #202
        "#12CHeehee. But I suppose all of that can wait.#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #203
        "#12CHe'll come back eventually. I know he will.#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #204
        (
            "#12CThen he can tell me all about what he did while\x01",
            "he was away.#0C\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #205
        "#12CBut he'll definitely be back... He will...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0x9)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(400, 160, -1, -1)
    SetChrName("Baby")

    AnonymousTalk(    #206
        "#12C...*gurgle*#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #207
        "#12C*gurgle* *gurgle*#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #208
        "#12CA baby?#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #209
        "#12CHeehee. How sweet.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x10, 0x0, 0x0, 0xB)
    PlayEffect(0xCB, 0x3, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #210
        "#12C#40WHe's so cute.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -7829368, 500, 0)
    Sleep(1000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #211
        (
            "#0C#40WA brand new life, clean and pure, untainted by\x01",
            "anything.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #212
        (
            "#0C#40WHe's probably a good child. He'll be raised well,\x01",
            "and grow up to be a fine, respectable adult.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #213
        "#0C#40WUnlike me.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #214
        "#0C#40WThat path was closed to me long ago.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #215
        "#0C#40WI hope you'll find happiness, nameless child.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_43(0x10, 0x0, 0x0, 0xB)
    PlayEffect(0xCB, 0x3, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C4(0x1, 0x800)
    Sleep(500)
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #216
        "#12C#40W...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    CloseMessageWindow()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #217
        "#12C#60W...Wh...y...?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    CloseMessageWindow()
    OP_44(0x10, 0x3)
    OP_C6(0x2, 0x4, 0, 0, 0)
    OP_C6(0x2, 0x3, -1, 1500, 0)
    Sleep(2500)
    SetMessageWindowPos(400, 180, -1, -1)
    SetChrName("Familiar Man")

    AnonymousTalk(    #218
        (
            "#12CHe really is cute, isn't he? He looks just like\x01",
            "his mother.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #219
        "#12CThere, there... That's a good boy...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Familiar Woman")

    AnonymousTalk(    #220
        (
            "#12CHeehee. I still regret what happened to our\x01",
            "last child...#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #221
        (
            "#12C...but it looks like the Goddess didn't abandon\x01",
            "us after all.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 180, -1, -1)
    SetChrName("Familiar Man")

    AnonymousTalk(    #222
        (
            "#12CNow, now. I thought we weren't going to talk\x01",
            "about that anymore?#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #223
        "#12CWe need to leave the past in the past.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Familiar Woman")

    AnonymousTalk(    #224
        (
            "#12CI suppose you're right... It's sad, but it's probably\x01",
            "what she would want, too.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(230, 220, -1, -1)
    SetChrName("Baby")

    AnonymousTalk(    #225
        "#12C*gurgle* *gurgle*#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("Familiar Woman")

    AnonymousTalk(    #226
        "#12CThere we go... Who's a good little baby?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -7829368, 500, 0)
    Sleep(800)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #227
        (
            "#0C#40WRenne.\x01",
            "Impure children.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x1, 0x800)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #228
        (
            "#0C#40WThe past.\x01",
            "'What happened to our last child.'#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #229
        "#0C#40W...Really?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #230
        (
            "#0C#40WThat was what I was?\x01",
            "From the very beginning?#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    AnonymousTalk(    #231
        "#0C#60WI...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #232
        (
            "#0C#40WI was...\x01",
            "I...\x01",
            "From the day I was born, I was...#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(200, 350, -1, -1)
    SetChrName("Young Man's Voice")

    AnonymousTalk(    #233
        "#12C...Renne.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_44(0x13, 0x0)
    OP_C6(0x3, 0x4, 0, 0, 0)
    OP_C6(0x3, 0x3, -1, 1500, 0)
    Sleep(2500)
    SetMessageWindowPos(380, 250, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #234
        "#12C#40W...Oh...#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #235
        "#12C#40W...Loewe...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 200, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #236
        "#12C...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #237
        (
            "#12CAs Enforcers, we have the freedom to do whatever\x01",
            "we want, whenever we want.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #238
        (
            "#12CIt's up to you what you want to do. I won't make\x01",
            "that choice for you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #239
        (
            "#12CI can't help but wonder whether they're even worth\x01",
            "the effort of cutting down, but that is your choice\x01",
            "to make.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 0, 0)
    OP_C6(0x3, 0x3, 16777215, 1000, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x0, 0x1, 0x3)
    OP_C7(0x0, 0x2, 0x3)
    OP_C7(0x0, 0x3, 0x3)
    Sleep(500)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #240
        (
            "#0C#40WI wander indifferently in a place that exists\x01",
            "beyond good and evil; beyond life and death.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #241
        (
            "#0C#40WThere is no fortune or misfortune. \x01",
            "No happiness. No sadness.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #242
        (
            "#0C#40WWhite and black tear into me, heaven and earth\x01",
            "torment me... I've been defiled.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #243
        "#0C#40WWhere does it begin, and where does it end?#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #244
        "#0C#40WI don't belong anywhere. I'm not going anywhere.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #245
        "#0C#40WBut the world just keeps on turning around me...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #246
        (
            "#0C#40WUnbeknownst to me, the world just kept on\x01",
            "turning...#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #247
        "#0C#40WBut that's fine.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #248
        "#0C#40WThe world is always turning for my sake.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #249
        "#0C#40WThat's why...I've got nothing to feel sad about.#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Sleep(500)
    OP_C4(0x1, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #250
        "#12C...Heehee...#0C\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xE)
    OP_C6(0x4, 0x4, 0, 0, 0)
    OP_C6(0x4, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(380, 250, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #251
        "#12CI don't care about some silly imposters.#0C\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #252
        (
            "#12CThey're not my real Papa and Mama.\x01",
            "I have Pater-Mater now.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0x10, 0x3, 0x0, 0xD)
    OP_C6(0x4, 0x3, 16777215, 2000, 0)
    OP_C7(0x0, 0x4, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_C4(0x1, 0x800)
    Sleep(1000)
    OP_C4(0x1, 0x10)
    OP_48()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_8_5A28 end

    def Function_9_6F54(): pass

    label("Function_9_6F54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F9C")
    OP_22(0x184, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x184, 0x0, 0x5A)
    Sleep(1100)
    OP_22(0x184, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x184, 0x0, 0x64)
    Sleep(1200)
    OP_22(0x184, 0x0, 0x5A)
    Sleep(1000)
    OP_22(0x184, 0x0, 0x5A)
    Sleep(1300)
    Jump("Function_9_6F54")

    label("loc_6F9C")

    Return()

    # Function_9_6F54 end

    def Function_10_6F9D(): pass

    label("Function_10_6F9D")

    OP_43(0x10, 0x0, 0x0, 0xB)
    PlayEffect(0xCB, 0x3, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2500)

    label("loc_6FDE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70DD")
    OP_43(0x10, 0x0, 0x0, 0xC)
    PlayEffect(0xCB, 0x3, 0xFF, 320, 240, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7042")
    Sleep(250)
    Jump("loc_70DA")

    label("loc_7042")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7057")
    Sleep(400)
    Jump("loc_70DA")

    label("loc_7057")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_706C")
    Sleep(700)
    Jump("loc_70DA")

    label("loc_706C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7081")
    Sleep(1000)
    Jump("loc_70DA")

    label("loc_7081")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x23), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7096")
    Sleep(1500)
    Jump("loc_70DA")

    label("loc_7096")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70AB")
    Sleep(2000)
    Jump("loc_70DA")

    label("loc_70AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70C0")
    Sleep(3000)
    Jump("loc_70DA")

    label("loc_70C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_70D5")
    Sleep(4000)
    Jump("loc_70DA")

    label("loc_70D5")

    Sleep(5000)

    label("loc_70DA")

    Jump("loc_6FDE")

    label("loc_70DD")

    Return()

    # Function_10_6F9D end

    def Function_11_70DE(): pass

    label("Function_11_70DE")

    OP_22(0x3C0, 0x0, 0x64)
    Sleep(500)
    OP_23(0x3C0)
    Return()

    # Function_11_70DE end

    def Function_12_70EC(): pass

    label("Function_12_70EC")

    OP_22(0x3C0, 0x0, 0x32)
    Sleep(500)
    OP_23(0x3C0)
    Return()

    # Function_12_70EC end

    def Function_13_70FA(): pass

    label("Function_13_70FA")

    OP_24(0x18E, 0x5A)
    Sleep(300)
    OP_24(0x18E, 0x50)
    Sleep(300)
    OP_24(0x18E, 0x46)
    Sleep(300)
    OP_24(0x18E, 0x3C)
    Sleep(300)
    OP_24(0x18E, 0x32)
    Sleep(300)
    OP_24(0x18E, 0x28)
    Sleep(300)
    OP_24(0x18E, 0x1E)
    Sleep(300)
    OP_24(0x18E, 0x14)
    Sleep(300)
    OP_24(0x18E, 0xA)
    Sleep(300)
    OP_24(0x18E, 0x0)
    OP_23(0x18E)
    Return()

    # Function_13_70FA end

    def Function_14_7153(): pass

    label("Function_14_7153")

    OP_22(0x18E, 0x1, 0x0)
    OP_24(0x18E, 0x0)
    Sleep(50)
    OP_24(0x18E, 0xA)
    Sleep(50)
    OP_24(0x18E, 0x14)
    Sleep(50)
    OP_24(0x18E, 0x1E)
    Sleep(50)
    OP_24(0x18E, 0x28)
    Sleep(50)
    OP_24(0x18E, 0x32)
    Sleep(50)
    OP_24(0x18E, 0x3C)
    Sleep(50)
    OP_24(0x18E, 0x46)
    Sleep(50)
    OP_24(0x18E, 0x50)
    Sleep(50)
    OP_24(0x18E, 0x5A)
    Sleep(50)
    OP_24(0x18E, 0x64)
    Return()

    # Function_14_7153 end

    def Function_15_71B7(): pass

    label("Function_15_71B7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp014_00.eff")
    LoadEffect(0x1, "map\\mp295_00.eff")
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, -54650, 100, 42240, 180)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x11, -52420, 100, 44100, 180)
    OP_A1(0x11, 0x0)
    OP_6D(-55520, 100, 44450, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(327000, 0)
    OP_6E(370, 0)
    OP_D8(0x0, 0x1F4)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 520)
    OP_70(0x0, 0x208)
    Sleep(1000)
    PlayEffect(0x0, 0xFF, 0xFF, -54650, 100, 42240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1C9, 0x0, 0x64)
    Sleep(1000)
    FadeToBright(3000, 0)
    OP_6B(2520, 3000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #253
        0x10,
        "#1309F#40W#6P...\x02",
    )

    CloseMessageWindow()

    def lambda_72F6():
        OP_6B(2320, 30000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_72F6)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x27), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_99(0x10, 0x0, 0x6, 0x3E8)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)
    OP_9E(0x10, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(1000)

    ChrTalk(    #254
        0x10,
        "#268F#6P#40W...It's so cold...\x02",
    )

    CloseMessageWindow()
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x18D, 0x1, 0x64)
    PlayEffect(0x1, 0x1, 0x11, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(1000)

    ChrTalk(    #255
        0x10,
        (
            "#264F#6P...\x02\x03",

            "#261FThanks, Pater-Mater.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x1, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x11)
    Sleep(1000)
    OP_62(0x10, 0x0, 1200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #256
        0x10,
        (
            "#263F#6PThat's right. I'm in the right. I'm in the right.\x02\x03",

            "#265FI'm always happy. I'm always having fun.\x02\x03",

            "#261FBecause I'm...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #257
        (
            "#5CThe world doesn't revolve just around you.\x02\x03",

            "And it won't always change just because you\x01",
            "demand it.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(100, 250, -1, -1)

    AnonymousTalk(    #258
        (
            "#5CIt should be obvious. Because I really care about you,\x01",
            "Renne.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #259
        (
            "#5CI won't lecture any more.\x02\x03",

            "Renne, you answer how your heart tells you.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_C4(0x1, 0x800)
    SetChrSubChip(0x10, 21)
    LoadEffect(0x1, "map\\mp021_00.eff")
    LoadEffect(0x2, "map\\mp064_01.eff")
    LoadEffect(0x3, "map\\mp065_01.eff")
    LoadEffect(0x4, "map\\mp064_00.eff")
    LoadEffect(0x5, "map\\mp065_00.eff")
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #260
        0x10,
        "#1309F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    ClearChrFlags(0x10, 0x2)
    ClearChrFlags(0x10, 0x800)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(1500)

    ChrTalk(    #261
        0x10,
        (
            "#1300F#6PIt's almost dawn.\x02\x03",

            "#1302FLet's go.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_44(0x10, 0x2)

    def lambda_77BC():
        OP_6D(-55140, 740, 45990, 5000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_77BC)

    def lambda_77D4():
        OP_6B(2370, 5000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_77D4)

    def lambda_77E4():
        OP_6E(398, 5000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_77E4)
    OP_22(0x113, 0x1, 0x3C)
    OP_22(0x114, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x11, 0, -800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    Play3DEffect(0x4, 0x1, 0x0, "Frame86__jet_0", 0x0, 0xFFFFFE0C, 0x0, 0x3C, 0xFFA6, 0xB4, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Play3DEffect(0x4, 0x2, 0x0, "Frame87__jet_1", 0x0, 0xFFFFFE0C, 0x0, 0x1E, 0x46, 0xFF4C, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(1000)

    def lambda_78A7():
        OP_8F(0xFE, 0xFFFF333C, 0x4B0, 0xAC44, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_78A7)
    Sleep(500)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_B0(0x0, 0x14)
    OP_6F(0x0, 521)
    OP_70(0x0, 0x230)
    OP_73(0x0)
    Fade(500)
    PlayEffect(0x5, 0x1, 0x11, 4950, 2800, 0, 0, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x5, 0x2, 0x11, -4950, 2800, 0, 0, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_D8(0x0, 0x5DC)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 1)
    OP_70(0x0, 0x28)

    def lambda_7969():
        OP_8F(0xFE, 0xFFFF333C, 0x64, 0xAC44, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_7969)
    WaitChrThread(0x11, 0x0)
    OP_22(0xEC, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    OP_22(0x111, 0x0, 0x64)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x5DC)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 461)
    OP_70(0x0, 0x1E0)
    OP_73(0x0)
    WaitChrThread(0x11, 0x0)
    OP_43(0x10, 0x0, 0x0, 0x10)
    OP_6F(0x0, 401)
    OP_70(0x0, 0x1A4)
    OP_73(0x0)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 381)
    OP_70(0x0, 0x1A4)
    WaitChrThread(0x10, 0x0)
    Sleep(300)
    ClearChrFlags(0x10, 0x10)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    OP_8C(0x10, 0, 0)
    Sleep(200)
    SetChrSubChip(0x10, 1)
    Sleep(200)

    def lambda_7A32():
        OP_99(0x10, 0x2, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_7A32)

    def lambda_7A42():
        OP_6D(-54290, 2720, 43500, 1000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7A42)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x10, 0xFFFF286A, 0xDAC, 0xA47E, 0xFA0, 0x1F40)
    ClearChrFlags(0x10, 0x4)
    OP_CF(0x10, 0x0, "Frame85__ren")
    WaitChrThread(0x10, 0x0)
    OP_22(0xA4, 0x0, 0x64)
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_8C(0x10, 315, 400)
    WaitChrThread(0x10, 0x0)
    Sleep(500)
    OP_22(0x114, 0x0, 0x64)
    PlayEffect(0x2, 0x1, 0x11, 4600, 2600, 0, 0, 0, 18, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x11, -4600, 2600, 0, 0, 0, 342, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_7B30():
        OP_6D(-52190, 1000, 47820, 4500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7B30)

    def lambda_7B48():
        OP_67(0, 6920, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7B48)

    def lambda_7B60():
        OP_6B(2860, 4500)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7B60)

    def lambda_7B70():
        OP_6C(23000, 4500)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_7B70)

    def lambda_7B80():
        OP_6E(407, 4500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_7B80)
    OP_43(0x11, 0x0, 0x0, 0x15)

    def lambda_7B97():
        OP_8F(0xFE, 0xFFFF3062, 0x9C4, 0x9F92, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7B97)
    Sleep(300)

    def lambda_7BB7():
        OP_8F(0xFE, 0xFFFF3062, 0x9C4, 0x9F92, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7BB7)
    Sleep(300)

    def lambda_7BD7():
        OP_8F(0xFE, 0xFFFF3062, 0x9C4, 0x9F92, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7BD7)
    OP_24(0x113, 0x50)
    Sleep(2000)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x5DC)
    OP_6F(0x0, 241)
    OP_70(0x0, 0x104)
    WaitChrThread(0x12, 0x0)
    Sleep(500)

    ChrTalk(    #262
        0x10,
        (
            "#1304F#5PWe're going to Crossbell.\x02\x03",

            "Once we're high enough up, switch off your\x01",
            "boosters and switch to your regular flight\x01",
            "engines.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)
    OP_82(0x0, 0x2)
    Sleep(1000)
    OP_24(0x113, 0x5A)
    Sleep(100)
    OP_24(0x113, 0x64)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x11, 0x0)
    Fade(500)
    OP_6D(-62040, 1600, 39420, 0)
    OP_67(0, 4990, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(271000, 0)
    OP_6E(440, 0)

    def lambda_7D15():
        OP_6B(2890, 8000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7D15)
    OP_11(0xF0, 0xE6, 0xB4, 0x14C08, 0x21EF8, 0x0)
    OP_0D()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x3E8)
    OP_6F(0x0, 261)
    OP_70(0x0, 0x118)
    OP_22(0x116, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x3E8)
    OP_6F(0x0, 281)
    OP_70(0x0, 0x12C)
    PlayEffect(0x3, 0x0, 0x11, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x11, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0x11, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x5, 0x11, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x6, 0x11, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x7, 0x11, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x114, 0x0, 0x64)
    Sleep(2000)
    PlayEffect(0x2, 0x0, 0x11, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x11, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x11, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x11, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x11, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x7, 0x11, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)

    def lambda_7FFA():
        OP_6D(-70410, 6250, 39710, 4000)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_7FFA)

    def lambda_8012():
        OP_67(0, 6070, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8012)

    def lambda_802A():
        OP_6B(3440, 6000)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_802A)

    def lambda_803A():
        OP_6C(283000, 6000)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_803A)

    def lambda_804A():
        OP_6E(420, 6000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_804A)

    def lambda_805A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_805A)
    Sleep(100)

    def lambda_807A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_807A)
    Sleep(100)

    def lambda_809A():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_809A)
    Sleep(100)

    def lambda_80BA():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_80BA)
    Sleep(100)

    def lambda_80DA():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_80DA)
    Sleep(100)
    FadeToDark(2000, 0, -1)

    def lambda_8104():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8104)
    Sleep(100)

    def lambda_8124():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x59D8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8124)
    Sleep(100)

    def lambda_8144():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8144)
    Sleep(100)

    def lambda_8164():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x80E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8164)
    Sleep(100)

    def lambda_8184():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x9470, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8184)
    Sleep(100)

    def lambda_81A4():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xA7F8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_81A4)
    Sleep(100)

    def lambda_81C4():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xBB80, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_81C4)
    OP_0D()
    OP_44(0x11, 0x1)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    OP_43(0x10, 0x0, 0x0, 0x13)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_43(0x10, 0x1, 0x0, 0x14)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_F7(0x9, 0xF, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #263
        "\x07\x00Side Story [Paradise] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82C0")
    Sleep(1000)
    OP_28(0xF, 0x4, 0x10)
    OP_28(0xF, 0x4, 0x20)
    OP_3E(0x2E8, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #264
        "\x07\x05Received \x1F\xE8\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_82C0")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7313   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_71B7 end

    def Function_16_82CD(): pass

    label("Function_16_82CD")

    OP_8C(0x10, 90, 400)
    Sleep(300)
    OP_8F(0x10, 0xFFFF327E, 0x64, 0xA118, 0x7D0, 0x0)
    Return()

    # Function_16_82CD end

    def Function_17_82EE(): pass

    label("Function_17_82EE")

    OP_24(0x18D, 0x5A)
    Sleep(150)
    OP_24(0x18D, 0x50)
    Sleep(150)
    OP_24(0x18D, 0x46)
    Sleep(150)
    OP_24(0x18D, 0x3C)
    Sleep(150)
    OP_24(0x18D, 0x32)
    Sleep(150)
    OP_24(0x18D, 0x28)
    Sleep(150)
    OP_24(0x18D, 0x1E)
    Sleep(150)
    OP_24(0x18D, 0x14)
    Sleep(150)
    OP_24(0x18D, 0xA)
    Sleep(150)
    OP_24(0x18D, 0x0)
    OP_23(0x18D)
    Return()

    # Function_17_82EE end

    def Function_18_8347(): pass

    label("Function_18_8347")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Sleep(500)
    OP_1D(0x6E)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #265
        (
            "\x07\x05In one corner of a vast city stood a sturdily-built\x01",
            "mansion.\x02\x03",

            "Its walls, decorated by marble, shone faintly in\x01",
            "the deep darkness, bathed in the cold moonlight.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #266
        (
            "\x07\x05It was a gathering spot for residents of the\x01",
            "criminal underworld, run by an equally unpleasant\x01",
            "organization.\x02\x03",

            "The white prison was filled with exceptionally\x01",
            "young children...\x02\x03",

            "All unfortunate enough to have been given as \x01",
            "offerings to the insatiable lust of those who\x01",
            "patronized the building.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_AD(0x240068, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #267
        (
            "\x07\x05Owing to the physical and mental strains of being\x01",
            "there, most of the children began to grow weaker\x01",
            "and weaker over time...\x02\x03",

            "But one girl, by nothing short of a miracle, was\x01",
            "somehow able to maintain her own sanity, and \x01",
            "endured all that was forced upon her.\x02\x03",

            "She was only five years old at the time, and one\x01",
            "of the many unfortunate souls who ended up there,\x01",
            "presumably abandoned by her parents.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #268
        (
            "\x07\x05One day, as dark fell, the building's gates were\x01",
            "opened once more...\x02\x03",

            "And the carriage of a government official came to\x01",
            "a halt in front of the building.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0xFA, 0x0, 0x64)
    Sleep(3000)
    SetMessageWindowPos(300, 250, -1, -1)
    SetChrName("Owner")

    AnonymousTalk(    #269
        "\x07\x00It's a pleasure to see you again, sir.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 100, -1, -1)
    SetChrName("Government Official")

    AnonymousTalk(    #270
        (
            "\x07\x00Guide me inside at once.\x02\x03",

            "I'm in an excellent mood tonight, I'll have you\x01",
            "know.\x02\x03",

            "I expect to be treated accordingly.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 250, -1, -1)
    SetChrName("Owner")

    AnonymousTalk(    #271
        "\x07\x00As you wish, sir.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1500)
    SetMessageWindowPos(200, 200, -1, -1)
    SetChrName("Owner")

    AnonymousTalk(    #272
        (
            "\x07\x00Now, Renne...\x02\x03",

            "Come and say hello to your favorite gentleman.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS303._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #273
        "\x07\x00...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 60, -1, -1)
    SetChrName("Owner")

    AnonymousTalk(    #274
        (
            "\x07\x00My... How wonderful.\x02\x03",

            "Come along, Renne.\x02\x03",

            "Let me get a good look at that sweet little face\x01",
            "of yours.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #275
        "\x07\x00...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 60, -1, -1)
    SetChrName("Government Official")

    AnonymousTalk(    #276
        (
            "\x07\x00Haha... There's no need to be so afraid.\x02\x03",

            "All you need to do is relax and let whatever\x01",
            "happens...happen.\x02\x03",

            "That way, when you next open your eyes...\x02\x03",

            "It'll aaall be over.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 300, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #277
        "\x07\x00Eeeek!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x7D0)
    OP_22(0x245, 0x0, 0x64)
    OP_22(0x22C, 0x0, 0x64)
    OP_C6(0x0, 0x0, 0, 10000, 50)
    OP_C7(0x0, 0x0, 0x0)
    OP_C6(0x0, 0x0, 0, -10000, 50)
    OP_C7(0x0, 0x0, 0x0)
    OP_C6(0x0, 0x0, 0, 10000, 50)
    OP_C7(0x0, 0x0, 0x0)
    OP_C6(0x0, 0x0, 0, -10000, 50)
    OP_C7(0x0, 0x0, 0x0)
    OP_C6(0x0, 0x0, 0, 10000, 50)
    OP_C7(0x0, 0x0, 0x0)
    OP_C6(0x0, 0x0, 0, -10000, 50)
    OP_C7(0x0, 0x0, 0x0)
    OP_C6(0x0, 0x3, 16777215, 200, 0)
    Sleep(1000)
    OP_1D(0x29)
    OP_43(0x0, 0x1, 0x0, 0x17)
    Sleep(1000)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(500)
    OP_22(0xD6, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x0, 0x1)
    OP_22(0x226, 0x0, 0x64)
    Sleep(800)
    OP_22(0x38F, 0x0, 0x64)
    SetMessageWindowPos(300, 150, -1, -1)
    SetChrName("Man's Scream")

    AnonymousTalk(    #278
        "\x07\x00#3SAaaah!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(300)
    OP_22(0x389, 0x0, 0x64)
    Sleep(500)
    OP_22(0x38F, 0x0, 0x64)
    SetMessageWindowPos(100, 250, -1, -1)
    SetChrName("Man's Scream")

    AnonymousTalk(    #279
        "\x07\x00#3SAaaaah!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x87, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(200, 200, -1, -1)
    SetChrName("Owner")

    AnonymousTalk(    #280
        "\x07\x00Wh-What's happening?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 80, -1, -1)
    SetChrName("Government Official")

    AnonymousTalk(    #281
        "\x07\x00What's going on?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(200, 80, -1, -1)
    SetChrName("Government Official")

    AnonymousTalk(    #282
        "\x07\x00#3SA-Aaaah!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_22(0x226, 0x0, 0x64)
    Sleep(500)
    OP_22(0x389, 0x0, 0x64)
    Sleep(800)
    OP_22(0x38F, 0x0, 0x64)
    Sleep(300)
    OP_22(0x38F, 0x0, 0x64)
    Sleep(500)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(300)
    OP_22(0x20C, 0x0, 0x64)
    Sleep(1000)
    OP_AE(0x5DC)
    Sleep(500)
    OP_AD(0x24006A, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #283
        (
            "\x07\x00...Filthy pigs.\x02\x03",

            "Their screams are as unpleasant as their looks.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 180, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #284
        (
            "\x07\x00...I've finished with the first floor now.\x02\x03",

            "Everyone left has fled to the second floor.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(330, 300, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #285
        (
            "\x07\x00Like cornered rats.\x02\x03",

            "Lead the way, Joshua.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(80, 180, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #286
        "\x07\x00Got it.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(2000)
    OP_20(0x7D0)
    OP_24(0x87, 0x5A)
    Sleep(150)
    OP_24(0x87, 0x50)
    Sleep(150)
    OP_24(0x87, 0x46)
    Sleep(150)
    OP_24(0x87, 0x3C)
    Sleep(150)
    OP_24(0x87, 0x32)
    Sleep(150)
    OP_24(0x87, 0x28)
    Sleep(150)
    OP_24(0x87, 0x1E)
    Sleep(150)
    OP_24(0x87, 0x14)
    Sleep(150)
    OP_24(0x87, 0xA)
    Sleep(150)
    OP_24(0x87, 0x0)
    OP_23(0x87)
    Sleep(500)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #287
        (
            "\x07\x05The assault of the building was carried out by a\x01",
            "mere two members of the society.\x02\x03",

            "Between them, they executed every last member of\x01",
            "the organization that ran it.\x02\x03",

            "The attack was meant to serve as an example to the\x01",
            "rest of the underworld there...\x02\x03",

            "But as an unintended consequence, that young girl\x01",
            "was allowed to escape with her life, albeit only\x01",
            "barely.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    OP_1D(0x73)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #288
        (
            "\x07\x05After being taken in by the group, she proved to\x01",
            "be remarkably skilled...\x02\x03",

            "...and before long, she had risen to being a\x01",
            "candidate for an executive position, and began\x01",
            "receiving formal training.\x02\x03",

            "Having saved her from the hell she was in,\x01",
            "Joshua and Loewe were like brothers to her.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(2000)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #289
        (
            "\x07\x05Not long after joining the Society, Renne heard\x01",
            "that Joshua had left on a special mission.\x02\x03",

            "One that he was going to take quite some time.\x02\x03",

            "Feeling somewhat lonely at the news, she decided\x01",
            "to step out into town for the first time in quite\x01",
            "a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x24006B, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #290
        (
            "\x07\x05And after doing so, something caught her eye.\x02\x03",

            "A familiar man and woman, a baby in the woman's\x01",
            "arms.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 100, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #291
        (
            "\x07\x00...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    SetMessageWindowPos(400, 80, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #292
        "\x07\x00...Well, what will you do?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS306._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS348._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1000)
    SetMessageWindowPos(380, 60, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #293
        "\x07\x00I...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 200, -1, -1)
    SetChrName("Loewe")

    AnonymousTalk(    #294
        (
            "\x07\x00I can't help but wonder whether they are even \x01",
            "worth the effort of cutting down...\x02\x03",

            "But that is your choice to make, not mine.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1500)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(500)
    SetMessageWindowPos(350, 60, -1, -1)
    SetChrName("Renne")

    AnonymousTalk(    #295
        (
            "\x07\x00...No. I'll leave them.\x02\x03",

            "They're not my real Papa and Mama.\x02\x03",

            "I have Pater-Mater now.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_20(0x7D0)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    Sleep(1000)
    OP_C7(0x1, 0xFF, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -54650, 100, 42240, 180)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x11, -52420, 100, 44100, 180)
    OP_A1(0x11, 0x0)
    OP_6D(-55520, 100, 44450, 0)
    OP_67(0, 5260, -10000, 0)
    OP_6B(2520, 0)
    OP_6C(327000, 0)
    OP_6E(370, 0)
    Sleep(1000)
    LoadEffect(0x0, "map\\\\mp014_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -54650, 100, 42240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x1C9, 0x0, 0x64)
    OP_1D(0x54)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #296
        0x10,
        "#260F#6P...Oh...\x02",
    )

    CloseMessageWindow()
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(250)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x27), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x26), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_99(0x10, 0x0, 0x6, 0x3E8)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)
    OP_9E(0x10, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(1000)

    ChrTalk(    #297
        0x10,
        (
            "#260F#6PRight...\x02\x03",

            "I thought it was cold... I guess that's because of\x01",
            "the rain.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x3D4, 0x0, 0x64)
    Sleep(1000)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x1F4)
    OP_6F(0x0, 461)
    OP_70(0x0, 0x1E0)
    OP_73(0x0)
    OP_D8(0x0, 0x1F4)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_6F(0x0, 381)
    OP_70(0x0, 0x1A4)
    Sleep(1000)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #298
        0x10,
        (
            "#260F#6PHeehee. Thanks, Pater-Mater.\x02\x03",

            "Well, let's go, shall we?\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x10, 0xFFFF287E, 0x3C, 0x9A1A, 0x7D0, 0x0)

    def lambda_989E():
        OP_6D(-55780, 1980, 44190, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_989E)
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 1)

    def lambda_98CA():
        OP_99(0x10, 0x0, 0x2, 0x9C4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_98CA)
    SetChrFlags(0x10, 0x4)
    OP_96(0x10, 0xFFFF286A, 0xDAC, 0xA47E, 0xFA0, 0x1F40)
    ClearChrFlags(0x10, 0x4)
    OP_CF(0x10, 0x0, "Frame85__ren")
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x10, 0)
    OP_22(0xA4, 0x0, 0x64)
    SetChrFlags(0x10, 0x10)
    OP_8C(0x10, 180, 0)
    Sleep(500)
    OP_8C(0x10, 0, 400)
    ClearChrFlags(0x10, 0x10)
    WaitChrThread(0x0, 0x0)
    LoadEffect(0x1, "map\\\\mp021_00.eff")
    LoadEffect(0x2, "map\\\\mp064_01.eff")
    LoadEffect(0x3, "map\\\\mp065_01.eff")
    LoadEffect(0x4, "map\\\\mp064_00.eff")
    LoadEffect(0x5, "map\\\\mp065_00.eff")
    Sleep(500)
    OP_22(0x113, 0x1, 0x46)
    OP_22(0x114, 0x0, 0x64)
    PlayEffect(0x1, 0x0, 0x11, 0, -500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xCC, 0x0, 0x64)
    PlayEffect(0x4, 0x1, 0x11, 4950, 2800, 0, 0, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0x11, -4950, 2800, 0, 0, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x2, 0x1, 0x11, 5000, 2500, 0, 0, 0, 20, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x11, -4900, 2500, 0, 0, 0, 340, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_9AC3():
        OP_6D(-52190, 710, 47820, 4500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_9AC3)

    def lambda_9ADB():
        OP_67(0, 6920, -10000, 4500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9ADB)

    def lambda_9AF3():
        OP_6B(2860, 4500)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9AF3)

    def lambda_9B03():
        OP_6C(23000, 4500)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_9B03)

    def lambda_9B13():
        OP_6E(407, 4500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_9B13)
    OP_43(0x11, 0x0, 0x0, 0x15)

    def lambda_9B2A():
        OP_8F(0xFE, 0xFFFF3062, 0x834, 0x9F92, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9B2A)
    Sleep(300)

    def lambda_9B4A():
        OP_8F(0xFE, 0xFFFF3062, 0x834, 0x9F92, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9B4A)
    Sleep(300)

    def lambda_9B6A():
        OP_8F(0xFE, 0xFFFF3062, 0x834, 0x9F92, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9B6A)
    OP_24(0x113, 0x50)
    Sleep(100)
    Sleep(2000)
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x1F4)
    OP_6F(0x0, 241)
    OP_70(0x0, 0x104)
    OP_82(0x0, 0x2)
    Sleep(50)
    PlayEffect(0x2, 0x1, 0x11, 4600, 2600, 0, 0, 0, 18, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x11, -4600, 2600, 0, 0, 0, 342, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_9C22():
        OP_8F(0xFE, 0xFFFF3062, 0x834, 0x9F92, 0x2EE, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9C22)
    OP_24(0x113, 0x5A)
    Sleep(100)
    OP_24(0x113, 0x64)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x0, 0x0)
    Fade(500)
    OP_6D(-62040, 1600, 39420, 0)
    OP_67(0, 4990, -10000, 0)
    OP_6B(2890, 0)
    OP_6C(271000, 0)
    OP_6E(440, 0)
    OP_11(0xF0, 0xE6, 0xB4, 0x14C08, 0x21EF8, 0x0)
    OP_0D()
    OP_72(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x3E8)
    OP_6F(0x0, 261)
    OP_70(0x0, 0x118)
    OP_22(0x116, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x2000, 0x0)
    ExitThread()
    OP_D8(0x0, 0x3E8)
    OP_6F(0x0, 281)
    OP_70(0x0, 0x12C)
    PlayEffect(0x3, 0x0, 0x11, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x11, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x4, 0x11, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x5, 0x11, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x6, 0x11, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x7, 0x11, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x114, 0x0, 0x64)
    Sleep(2000)
    PlayEffect(0x2, 0x0, 0x11, 500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x3, 0x11, -500, -3300, -3600, 0, 80, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x11, 1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x5, 0x11, 400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x6, 0x11, -1000, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x7, 0x11, -400, -2600, -3000, 0, 70, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1, 0x2)
    OP_82(0x2, 0x2)

    def lambda_9F70():
        OP_6D(-62040, 2500, 39670, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_9F70)

    def lambda_9F88():
        OP_67(0, 3700, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_9F88)

    def lambda_9FA0():
        OP_6B(4050, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_9FA0)

    def lambda_9FB0():
        OP_6E(382, 4000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_9FB0)
    Sleep(500)

    def lambda_9FC5():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9FC5)
    Sleep(100)

    def lambda_9FE5():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_9FE5)
    Sleep(100)

    def lambda_A005():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A005)
    Sleep(100)

    def lambda_A025():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A025)
    Sleep(100)

    def lambda_A045():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A045)
    Sleep(100)

    def lambda_A065():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A065)
    Sleep(100)

    def lambda_A085():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x59D8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A085)
    Sleep(100)

    def lambda_A0A5():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A0A5)
    Sleep(100)

    def lambda_A0C5():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x80E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A0C5)
    Sleep(100)

    def lambda_A0E5():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0x9470, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A0E5)
    Sleep(100)

    def lambda_A105():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xA7F8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A105)
    Sleep(100)

    def lambda_A125():
        OP_8F(0xFE, 0xFFFDD762, 0x4268, 0x3DB8, 0xBB80, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A125)
    WaitChrThread(0x11, 0x1)
    OP_43(0x10, 0x0, 0x0, 0x13)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_43(0x10, 0x1, 0x0, 0x14)
    OP_20(0x7D0)
    Sleep(2000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1B1")
    Sleep(1000)
    OP_28(0xF, 0x4, 0x10)
    OP_3E(0x2E8, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #299
        "\x07\x05Received \x1F\xE8\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_A1B1")

    OP_A2(0x2505)
    NewScene("ED6_DT21/M7313   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_8347 end

    def Function_19_A1BE(): pass

    label("Function_19_A1BE")

    OP_24(0x113, 0x5A)
    Sleep(200)
    OP_24(0x113, 0x50)
    Sleep(200)
    OP_24(0x113, 0x46)
    Sleep(200)
    OP_24(0x113, 0x3C)
    Sleep(200)
    OP_24(0x113, 0x32)
    Sleep(200)
    OP_24(0x113, 0x28)
    Sleep(200)
    OP_24(0x113, 0x1E)
    Sleep(200)
    OP_24(0x113, 0x14)
    Sleep(200)
    OP_24(0x113, 0xA)
    Sleep(200)
    OP_24(0x113, 0x0)
    OP_23(0x113)
    Return()

    # Function_19_A1BE end

    def Function_20_A217(): pass

    label("Function_20_A217")

    OP_24(0x1C9, 0x5A)
    Sleep(200)
    OP_24(0x1C9, 0x50)
    Sleep(200)
    OP_24(0x1C9, 0x46)
    Sleep(200)
    OP_24(0x1C9, 0x3C)
    Sleep(200)
    OP_24(0x1C9, 0x32)
    Sleep(200)
    OP_24(0x1C9, 0x28)
    Sleep(200)
    OP_24(0x1C9, 0x1E)
    Sleep(200)
    OP_24(0x1C9, 0x14)
    Sleep(200)
    OP_24(0x1C9, 0xA)
    Sleep(200)
    OP_24(0x1C9, 0x0)
    OP_23(0x1C9)
    Return()

    # Function_20_A217 end

    def Function_21_A270(): pass

    label("Function_21_A270")

    Sleep(1000)

    def lambda_A27B():
        OP_8C(0xFE, 250, 10)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_A27B)
    Sleep(200)

    def lambda_A28E():
        OP_8C(0xFE, 250, 15)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_A28E)
    Sleep(200)

    def lambda_A2A1():
        OP_8C(0xFE, 250, 20)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_A2A1)
    Sleep(500)

    def lambda_A2B4():
        OP_8C(0xFE, 250, 30)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_A2B4)
    Sleep(100)

    def lambda_A2C7():
        OP_8C(0xFE, 250, 40)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_A2C7)
    Return()

    # Function_21_A270 end

    def Function_22_A2D0(): pass

    label("Function_22_A2D0")

    OP_8F(0xFE, 0xFFFF287E, 0x3C, 0x9A1A, 0x7D0, 0x0)
    Sleep(300)
    OP_22(0xA3, 0x0, 0x64)
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 1)

    def lambda_A2FE():
        OP_99(0xFE, 0x0, 0x2, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A2FE)
    OP_96(0xFE, 0xFFFF286A, 0xBEA, 0xA47E, 0xDAC, 0x1F40)
    OP_CF(0xFE, 0x0, "Frame85__ren")
    SetChrSubChip(0xFE, 0)
    SetChrChipByIndex(0xFE, 0)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(300)
    SetChrFlags(0xFE, 0x10)
    OP_8C(0xFE, 180, 400)
    ClearChrFlags(0xFE, 0x10)
    Return()

    # Function_22_A2D0 end

    def Function_23_A356(): pass

    label("Function_23_A356")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A38A")
    OP_22(0x235, 0x0, 0x50)
    Sleep(1000)
    OP_22(0x1F7, 0x0, 0x50)
    Sleep(1000)
    OP_22(0x1F7, 0x0, 0x50)
    Sleep(500)
    OP_22(0x235, 0x0, 0x50)
    Sleep(800)
    Jump("Function_23_A356")

    label("loc_A38A")

    Return()

    # Function_23_A356 end

    SaveToFile()

Try(main)
