from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0012_1 ._SN',
        MapName             = 'event',
        Location            = 'E0012.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 29200, 0, -7430, 270)
    SetChrPos(0x102, 30010, 0, -8090, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F4")
    SetChrPos(0x107, 29960, 0, -6410, 225)

    label("loc_F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_113")
    SetChrPos(0x106, 31010, 0, -7540, 270)

    label("loc_113")

    OP_6D(28990, 0, -7070, 2000)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#000FFaye... Can I talk to you\x01",
            "for a minute?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x10)
    TalkBegin(0xA)
    OP_4A(0xA, 255)
    ClearChrFlags(0xA, 0x10)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #1
        0xFE,
        "Hmm? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#000FSorry to bug you when\x01",
            "you're so busy...\x02\x03",

            "#000FI have something I'm supposed\x01",
            "to deliver to you.\x02\x03",

            "Here you go.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        "\x07\x00Handed over \x07\x02Letter to Faye\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_3F(0x35E, 1)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #4
        0xFE,
        "What...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Wait... Is this from Private Brahm\x01",
            "at the Wolf Fort?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#000FYeah...\x02\x03",

            "#002F(Okay! Now's the perfect time\x01",
            "to give her the gift!)\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A1")
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #7
        0x101,
        (
            "#008F(...Or it would be, if I hadn't\x01",
            "forgotten to buy it!)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)
    Jump("loc_7E1")

    label("loc_3A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42C")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Work Gloves]\x01",      # 0
            "[Cancel]\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_41D"),
        (1, "loc_423"),
        (SWITCH_DEFAULT, "loc_429"),
    )


    label("loc_41D")

    OP_A2(0x6)
    Jump("loc_429")

    label("loc_423")

    OP_A2(0x9)
    Jump("loc_429")

    label("loc_429")

    Jump("loc_7E1")

    label("loc_42C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B9")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Seasonal Tart]\x01",      # 0
            "[Cancel]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4AA"),
        (1, "loc_4B0"),
        (SWITCH_DEFAULT, "loc_4B6"),
    )


    label("loc_4AA")

    OP_A2(0x7)
    Jump("loc_4B6")

    label("loc_4B0")

    OP_A2(0x9)
    Jump("loc_4B6")

    label("loc_4B6")

    Jump("loc_7E1")

    label("loc_4B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_548")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Woolly Knit-Hat]\x01",      # 0
            "[Cancel]\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_539"),
        (1, "loc_53F"),
        (SWITCH_DEFAULT, "loc_545"),
    )


    label("loc_539")

    OP_A2(0x8)
    Jump("loc_545")

    label("loc_53F")

    OP_A2(0x9)
    Jump("loc_545")

    label("loc_545")

    Jump("loc_7E1")

    label("loc_548")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EC")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Work Gloves]\x01",        # 0
            "[Seasonal Tart]\x01",      # 1
            "[Cancel]\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5D7"),
        (1, "loc_5DD"),
        (2, "loc_5E3"),
        (SWITCH_DEFAULT, "loc_5E9"),
    )


    label("loc_5D7")

    OP_A2(0x6)
    Jump("loc_5E9")

    label("loc_5DD")

    OP_A2(0x7)
    Jump("loc_5E9")

    label("loc_5E3")

    OP_A2(0x9)
    Jump("loc_5E9")

    label("loc_5E9")

    Jump("loc_7E1")

    label("loc_5EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_692")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Work Gloves]\x01",          # 0
            "[Woolly Knit-Hat]\x01",      # 1
            "[Cancel]\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_67D"),
        (1, "loc_683"),
        (2, "loc_689"),
        (SWITCH_DEFAULT, "loc_68F"),
    )


    label("loc_67D")

    OP_A2(0x6)
    Jump("loc_68F")

    label("loc_683")

    OP_A2(0x8)
    Jump("loc_68F")

    label("loc_689")

    OP_A2(0x9)
    Jump("loc_68F")

    label("loc_68F")

    Jump("loc_7E1")

    label("loc_692")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x14D)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_40(0x1B2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_40(0x14A)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73A")
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Seasonal Tart]\x01",        # 0
            "[Woolly Knit-Hat]\x01",      # 1
            "[Cancel]\x01",               # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_725"),
        (1, "loc_72B"),
        (2, "loc_731"),
        (SWITCH_DEFAULT, "loc_737"),
    )


    label("loc_725")

    OP_A2(0x7)
    Jump("loc_737")

    label("loc_72B")

    OP_A2(0x8)
    Jump("loc_737")

    label("loc_731")

    OP_A2(0x9)
    Jump("loc_737")

    label("loc_737")

    Jump("loc_7E1")

    label("loc_73A")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Work Gloves]\x01",          # 0
            "[Seasonal Tart]\x01",        # 1
            "[Woolly Knit-Hat]\x01",      # 2
            "[Cancel]\x01",               # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7CC"),
        (1, "loc_7CF"),
        (2, "loc_7D5"),
        (3, "loc_7DB"),
        (SWITCH_DEFAULT, "loc_7E1"),
    )


    label("loc_7CC")

    OP_A2(0x6)

    label("loc_7CF")

    OP_A2(0x7)
    Jump("loc_7E1")

    label("loc_7D5")

    OP_A2(0x8)
    Jump("loc_7E1")

    label("loc_7DB")

    OP_A2(0x9)
    Jump("loc_7E1")

    label("loc_7E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_AAC")

    ChrTalk(    #8
        0x101,
        (
            "#000FAnd this is a present to\x01",
            "go with it.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #9
        "\x07\x00Handed over \x07\x02Work Gloves\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #10
        0xFE,
        (
            "Work gloves? What kind of\x01",
            "gift are these meant to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "W-Well... I'll accept them...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 400)

    ChrTalk(    #12
        0xFE,
        (
            "*sigh* I just don't think he\x01",
            "really gets me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #14
        0x101,
        (
            "#509F(Ack...)\x02\x03",

            "(Well, that was a lousy present...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #15
        0xFE,
        "...Oh, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Now's really not the time to\x01",
            "be discussing such things,\x01",
            "is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Thank you for taking the\x01",
            "time to deliver it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Well...\x01",
            "I should get back to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#506FS-Sure.\x01",
            "See you later.\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x14D, 1)
    OP_28(0x31, 0x1, 0x40)
    OP_2B(0x31, 0x2)
    Jump("loc_123E")

    label("loc_AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_D8E")

    ChrTalk(    #20
        0x101,
        "#000FAnd this is a present to go with it.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #21
        "\x07\x00Handed over \x07\x02Seasonal Tart\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #22
        0xFE,
        (
            "Th-Thank you...\x01",
            "It's very nice...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "It's just that I'm trying to\x01",
            "cut back on sweets.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "And he still sent me this...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 400)

    ChrTalk(    #25
        0xFE,
        (
            "*sigh* I guess it just shows that\x01",
            "he doesn't really listen to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #27
        0x101,
        (
            "#509F(Ack...)\x02\x03",

            "(Well, that was a lousy present...)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #28
        0xFE,
        "...Oh, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Now's really not the time to\x01",
            "be discussing such things,\x01",
            "is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "Thank you for taking the\x01",
            "time to deliver it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Well...\x01",
            "I should get back to work.\x02",
        )
    )

    CloseMessageWindow()
    OP_3F(0x1B2, 1)
    OP_28(0x31, 0x1, 0x80)
    OP_2B(0x31, 0x2)
    Jump("loc_123E")

    label("loc_D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_FD4")

    ChrTalk(    #32
        0x101,
        "#000FAnd this is a present to go with it.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #33
        "\x07\x00Handed over \x07\x02Woolly Knit-Hat\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)

    ChrTalk(    #34
        0xFE,
        "Oh, how cute.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "I see, now. Finally...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "I know he still thinks\x01",
            "about me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "But I just wish he'd come\x01",
            "sooner...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Sleep(800)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #40
        0xFE,
        "...Oh, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Now's really not the time to\x01",
            "be discussing such things,\x01",
            "is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Thank you for taking the\x01",
            "time to deliver it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Well...\x01",
            "I should get back to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#000FSure. See you later.\x02",
    )

    CloseMessageWindow()
    OP_3F(0x14A, 1)
    OP_28(0x31, 0x1, 0x20)
    OP_2B(0x31, 0x4)
    Jump("loc_123E")

    label("loc_FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_1015")

    ChrTalk(    #45
        0x101,
        (
            "#505F(Hmm... Not bad, but it \x01",
            "wasn't quite perfect.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1015")

    Sleep(400)

    ChrTalk(    #46
        0xFE,
        "Hmm...okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "He's trying, in his own special\x01",
            "way, to show me that he still\x01",
            "thinks about me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 270, 400)

    ChrTalk(    #48
        0xFE,
        (
            "But he sends me a letter\x01",
            "now, of all things...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #50
        0x101,
        (
            "#509F(Ack...)\x02\x03",

            "(Maybe I should have given\x01",
            "her a present... )\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0xFE, 90, 400)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #51
        0xFE,
        "...Oh, I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Now's really not the time to\x01",
            "be discussing such things,\x01",
            "is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Thank you for taking the\x01",
            "time to deliver it to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Well...\x01",
            "I should get back to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#506FS-Sure.\x01",
            "See you later.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x31, 0x1, 0x100)

    label("loc_123E")

    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #56
        "\x07\x00Quest \x07\x02[Messenger of Love] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x35E, 1)
    OP_28(0x31, 0x4, 0x10)
    OP_28(0x31, 0x1, 0x10)
    OP_A2(0x5)
    Sleep(50)
    EventEnd(0x4)
    OP_4B(0xA, 255)
    Return()

    # Function_2_AC end

    SaveToFile()

Try(main)
