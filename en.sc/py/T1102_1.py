from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1102_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1102_1 ._SN',
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
        "Function_1_1DA9",         # 01, 1
        "Function_2_1DBB",         # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_346")

    ChrTalk(    #0
        0x101,
        (
            "#1002FWait a minute.\x01",
            "The place mentioned on the card.\x02\x03",

            "Do you think this might be it?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E")

    ChrTalk(    #1
        0x103,
        (
            "#022FIt is possible, but...\x02\x03",

            "We can continue that case later.\x01",
            "We need to get to Ravennue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #2
        0x101,
        "#1002FAh, right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_342")

    label("loc_19E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_225")

    ChrTalk(    #3
        0x108,
        (
            "#072FIt is possible, but now is not the time.\x02\x03",

            "We must get to Ravennue immediately.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #4
        0x101,
        "#1002FAh, right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_342")

    label("loc_225")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BF")

    ChrTalk(    #5
        0x104,
        (
            "#030FIt is quite possible.\x02\x03",

            "Now, however, is not the time to ponder.\x01",
            "We must away to Ravennue at once.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #6
        0x101,
        "#1002FAh, right.\x02",
    )

    CloseMessageWindow()
    Jump("loc_342")

    label("loc_2BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_342")

    ChrTalk(    #7
        0x105,
        (
            "#042FYes, it might be.\x02\x03",

            "But that case can wait, can't it?\x01",
            "We must get to Ravennue.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #8
        0x101,
        "#1002FAh, right.\x02",
    )

    CloseMessageWindow()

    label("loc_342")

    TalkEnd(0xFF)
    Return()

    label("loc_346")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 23790, -3000, 12560, 135)
    SetChrPos(0xF7, 22600, -3000, 12510, 135)
    SetChrPos(0xF8, 23080, -3000, 13980, 135)
    SetChrPos(0xF9, 21720, -3000, 13710, 135)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AE")
    SetChrPos(0x4, 21150, -3000, 12710, 135)

    label("loc_3AE")

    SetChrPos(0x19, 36190, -3000, 13170, 270)
    OP_6D(26500, -3000, 9360, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2950, 0)
    OP_6C(166000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_6D(23790, -3000, 12560, 2000)

    ChrTalk(    #9
        0x101,
        (
            "#1011FThe 'reverently-held casket,' huh?\x02\x03",

            "Calling it a coffin's a bit of a stretch,\x01",
            "but it IS being held like it was holy!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EE")

    ChrTalk(    #10
        0x106,
        (
            "#050FYeah, but there's a problem.\x02\x03",

            "I don't see that bozo's card anywhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_640")

    label("loc_4EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55E")

    ChrTalk(    #11
        0x103,
        (
            "#020FIt does seem like our answer.\x02\x03",

            "The only problem is that I don't see a\x01",
            "card anywhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_640")

    label("loc_55E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C9")

    ChrTalk(    #12
        0x108,
        (
            "#070FIt does seem like the best answer.\x02\x03",

            "I don't see any of his cards on it,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_640")

    label("loc_5C9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_640")

    ChrTalk(    #13
        0x104,
        (
            "#030FIt's the sort of answer my rival\x01",
            "would come up with.\x02\x03",

            "Curiously, however, I do not see a card.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_640")


    ChrTalk(    #14
        0x101,
        (
            "#1015FHmmm, that IS weird.\x02\x03",

            "I'm sure this is it, though.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 300, 400)

    ChrTalk(    #15
        0x101,
        (
            "#1018FWait, I know!\x01",
            "I bet it's on the bottom of that thing!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_750")

    ChrTalk(    #16
        0x107,
        (
            "#063FIt might be, but, um.\x02\x03",

            "That little hole isn't big enough to\x01",
            "crawl under to look...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D1")

    label("loc_750")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DD")

    ChrTalk(    #17
        0x105,
        (
            "#043FIt might be, but there's a problem.\x02\x03",

            "There's no way any of us would possibly\x01",
            "fit under that little crack to look.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D1")

    label("loc_7DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_872")

    ChrTalk(    #18
        0x104,
        (
            "#030FBut we face a dilemma.\x02\x03",

            "Unless we are capable of transfiguring\x01",
            "ourselves into mice, none of us can get\x01",
            "under it to check.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D1")

    label("loc_872")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8D1")

    ChrTalk(    #19
        0x108,
        (
            "#070FIt might be.\x02\x03",

            "We would need to actually get under it\x01",
            "to check, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D1")


    ChrTalk(    #20
        0x101,
        "#1007FYeah, good point.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(    #21
        0x101,
        (
            "#1003FThis container HAS to be it, too.\x01",
            "Lesse...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #22
        0x19,
        "Man's Voice",
        "#2PHey, HEY! What do you think you're doing?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_991")
    OP_62(0xF6, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9CF")

    label("loc_991")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF6)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B8")
    OP_62(0xF6, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_9CF")

    label("loc_9B8")

    OP_62(0xF6, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_9CF")

    Sleep(150)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9FB")
    OP_62(0xF7, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A39")

    label("loc_9FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A22")
    OP_62(0xF7, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A39")

    label("loc_A22")

    OP_62(0xF7, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A60")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A9E")

    label("loc_A60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A87")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_A9E")

    label("loc_A87")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_A9E")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACA")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B08")

    label("loc_ACA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF1")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B08")

    label("loc_AF1")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B08")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B51")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B3A")
    OP_62(0x4, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_B51")

    label("loc_B3A")

    OP_62(0x4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_B51")

    Sleep(1000)

    def lambda_B5C():
        OP_8C(0x2, 90, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_B5C)
    Sleep(100)

    def lambda_B6F():
        OP_8C(0x3, 90, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_B6F)

    def lambda_B7D():
        OP_8C(0x1, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_B7D)
    Sleep(100)

    def lambda_B90():
        OP_8C(0x0, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB2")

    def lambda_BAA():
        OP_8C(0x4, 90, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_BAA)

    label("loc_BB2")


    def lambda_BB8():
        OP_6C(225000, 4000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_BB8)
    OP_43(0x101, 0x2, 0x1, 0x1)
    OP_8E(0x19, 0x639C, 0xFFFFF448, 0x3322, 0xBB8, 0x0)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BFD")
    OP_44(0x4, 0x1)

    label("loc_BFD")

    OP_4A(0x19, 255)

    ChrTalk(    #23
        0x19,
        (
            "You were messing with machinery on MY\x01",
            "maintenance deck, weren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x19,
        "What in hell were you trying to do?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1009F#4PWe weren't 'messing' with anything!\x02\x03",

            "We're trying to investigate this container!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x19,
        "Investigate? What?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D6B")

    ChrTalk(    #27
        0x106,
        "#050FI think this'll explain.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05Agate showed Lakely his bracer emblem.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_F0C")

    label("loc_D6B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DFE")

    ChrTalk(    #29
        0x103,
        "#020FI think this will explain things, sir.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x05Scherazard showed Lakely her bracer emblem.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_F0C")

    label("loc_DFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E8E")

    ChrTalk(    #31
        0x108,
        "#070FAh, right, this should explain who we are.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05Zin showed Lakely his bracer emblem.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_F0C")

    label("loc_E8E")


    ChrTalk(    #33
        0x101,
        "#1002FOh, right, lemme explain who we are.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x05Estelle showed Lakely her bracer emblem.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_F0C")


    ChrTalk(    #35
        0x19,
        "Ah, you lot!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x19,
        "Has a case led you to my dock?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        (
            "#1002F#4PRight to the middle of it, in fact.\x02\x03",

            "#1011FOh, right! I wanted to ask.\x02\x03",

            "Can we use that machine?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x19,
        "You bet you can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x19,
        (
            "And what are you looking to do,\x01",
            "exactly?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#1002F#4PWe just need to take a look at the\x01",
            "bottom of that container.\x02\x03",

            "Could you lift it just enough for\x01",
            "us to take a look?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x19,
        "Sure, I suppose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x19,
        "Wait here a second.\x02",
    )

    CloseMessageWindow()

    def lambda_10AB():

        label("loc_10AB")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_10AB")

    QueueWorkItem2(0x0, 1, lambda_10AB)

    def lambda_10BC():

        label("loc_10BC")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_10BC")

    QueueWorkItem2(0x1, 1, lambda_10BC)

    def lambda_10CD():

        label("loc_10CD")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_10CD")

    QueueWorkItem2(0x2, 1, lambda_10CD)

    def lambda_10DE():

        label("loc_10DE")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_10DE")

    QueueWorkItem2(0x3, 1, lambda_10DE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1106")

    def lambda_10FB():

        label("loc_10FB")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_10FB")

    QueueWorkItem2(0x4, 1, lambda_10FB)

    label("loc_1106")


    def lambda_110C():
        OP_6C(155000, 4000)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_110C)

    def lambda_111C():
        OP_6D(26860, -3000, 9620, 4000)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_111C)
    OP_8C(0x19, 135, 400)
    OP_8E(0x19, 0x6D4C, 0xFFFFF448, 0x2A26, 0x7D0, 0x0)
    OP_8C(0x19, 225, 400)
    OP_8E(0x19, 0x6C16, 0xFFFFF448, 0x28F0, 0x3E8, 0x0)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x10)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    OP_8E(0x19, 0x6A68, 0xFFFFF6A0, 0x249A, 0x3E8, 0x0)
    OP_8C(0x19, 315, 400)
    OP_8E(0x19, 0x6932, 0xFFFFF5D8, 0x25B2, 0x3E8, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11C2")
    OP_44(0x4, 0x1)

    label("loc_11C2")

    Sleep(1000)
    Sleep(100)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(400)
    OP_22(0xCF, 0x1, 0x55)

    ChrTalk(    #43
        0x19,
        "All right, here we go!\x02",
    )

    CloseMessageWindow()
    OP_24(0xCF, 0x64)
    OP_B0(0xD, 0xA)
    OP_70(0xD, 0x1E)
    OP_73(0xD)
    OP_22(0x9A, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #44
        0x19,
        "All right, it's locked and safe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x19,
        "You should be able to get a look now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1006F#2PThanks, mister.\x01",
            "C'mon, let's see if there's anything there.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x620C, 0xFFFFF448, 0x2AEE, 0x7D0, 0x0)
    Sleep(500)
    OP_8C(0x101, 270, 400)
    Sleep(200)
    OP_8C(0x101, 90, 400)
    Sleep(500)
    OP_8C(0x101, 120, 400)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #47
        (
            "\x07\x05There was, indeed, a note attached to the bottom of the\x01",
            "container.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #48
        0x101,
        "#1006F#2PAnd here it is!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x5CEE, 0xFFFFF448, 0x3110, 0x7D0, 0x0)
    OP_8C(0x101, 120, 400)

    ChrTalk(    #49
        0x101,
        (
            "#1018F#2PThank you, sir.\x01",
            "That's all we needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x19,
        (
            "Great. Let me get this container\x01",
            "back down, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_B0(0xD, 0xA)
    OP_6F(0xD, 30)
    OP_70(0xD, 0x0)
    OP_73(0xD)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x9D)
    OP_23(0xCF)
    Sleep(400)
    Fade(1000)
    OP_6C(225000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2950, 0)
    OP_6E(262, 0)
    SetChrPos(0x19, 27780, -3000, 10390, 30)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x10)

    def lambda_148F():

        label("loc_148F")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_148F")

    QueueWorkItem2(0x0, 1, lambda_148F)

    def lambda_14A0():

        label("loc_14A0")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_14A0")

    QueueWorkItem2(0x1, 1, lambda_14A0)

    def lambda_14B1():

        label("loc_14B1")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_14B1")

    QueueWorkItem2(0x2, 1, lambda_14B1)

    def lambda_14C2():

        label("loc_14C2")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_14C2")

    QueueWorkItem2(0x3, 1, lambda_14C2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14EA")

    def lambda_14DF():

        label("loc_14DF")

        TurnDirection(0xFE, 0x19, 400)
        OP_48()
        Jump("loc_14DF")

    QueueWorkItem2(0x4, 1, lambda_14DF)

    label("loc_14EA")


    def lambda_14F0():
        OP_6D(23760, -3000, 13010, 3000)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_14F0)
    OP_8E(0x19, 0x6A2C, 0xFFFFF448, 0x2D78, 0x7D0, 0x0)
    OP_8E(0x19, 0x639C, 0xFFFFF448, 0x3322, 0x7D0, 0x0)
    TurnDirection(0x19, 0x101, 400)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1551")
    OP_44(0x4, 0x1)

    label("loc_1551")

    WaitChrThread(0x2A, 0x1)
    WaitChrThread(0x2A, 0x2)

    ChrTalk(    #51
        0x19,
        "Seems you found what you were looking for.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15CC")

    ChrTalk(    #52
        0x104,
        "#030FOur thanks for your aid, my good man.\x02",
    )

    CloseMessageWindow()
    Jump("loc_166D")

    label("loc_15CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1601")

    ChrTalk(    #53
        0x108,
        "#070FThank you for helping us!\x02",
    )

    CloseMessageWindow()
    Jump("loc_166D")

    label("loc_1601")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_163A")

    ChrTalk(    #54
        0x103,
        "#525FHYou have our gratitude, sir.\x02",
    )

    CloseMessageWindow()
    Jump("loc_166D")

    label("loc_163A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_166D")

    ChrTalk(    #55
        0x106,
        "#051FThanks for helpin' us out.\x02",
    )

    CloseMessageWindow()

    label("loc_166D")


    ChrTalk(    #56
        0x19,
        "Haha, don't worry. It was no big deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x19,
        (
            "Anyway, I don't know what you're\x01",
            "investigating, but good luck with it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x19,
        "Well, I need to get back to work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#1001F#4POf course! Thanks again!\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x2, 0x1, 0x2)
    OP_8E(0x19, 0x8D5E, 0xFFFFF448, 0x3372, 0x7D0, 0x0)

    ChrTalk(    #60
        0x101,
        "#1011FPhew! I'm glad he was willing to help.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17CA")
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #61
        0x108,
        "#070FIndeed. Time to continue the job, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18B6")

    label("loc_17CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1813")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #62
        0x106,
        "#050FYeah. And now, time to get on with it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18B6")

    label("loc_1813")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1869")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #63
        0x103,
        (
            "#020FMmhmm. And now I think it's time we\x01",
            "got on with it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18B6")

    label("loc_1869")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18B6")
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #64
        0x104,
        "#030FAh, but do not leave us in suspense, Estelle.\x02",
    )

    CloseMessageWindow()

    label("loc_18B6")


    def lambda_18BC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18BC)

    def lambda_18CA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_18CA)

    def lambda_18D8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_18D8)

    def lambda_18E6():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_18E6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1908")

    def lambda_1900():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_1900)

    label("loc_1908")

    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF7, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_192D")
    WaitChrThread(0x4, 0x1)

    label("loc_192D")


    ChrTalk(    #65
        0x101,
        "#1000F#6PRight, the card.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    Fade(500)
    SetChrChipByIndex(0x101, 32)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #66
        (
            "\x07\x05'The door has been thrown open.\x01",
            "Seek ye the proof of vanity?\x01",
            "Find it in the words of the Goddess.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()

    ChrTalk(    #67
        0x101,
        (
            "#1000F#6PThat's it.\x02\x03",

            "#1000FLooks like we're just about done.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AAB")

    ChrTalk(    #68
        0x107,
        (
            "#060FYeah, I guess so!\x02\x03",

            "'Words of the Goddess'...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB1")

    label("loc_1AAB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AF4")

    ChrTalk(    #69
        0x105,
        (
            "#040FAt last, hmm??\x02\x03",

            "So, 'words of the Goddess'...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB1")

    label("loc_1AF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B51")

    ChrTalk(    #70
        0x104,
        (
            "#030FHeh, at long last.\x02\x03",

            "So we seek the 'words of the Goddess,'\x01",
            "do we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB1")

    label("loc_1B51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BB1")

    ChrTalk(    #71
        0x108,
        (
            "#070FIt's about time, I'd say!\x02\x03",

            "Now we must find the 'words of the Goddess.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB1")


    ChrTalk(    #72
        0x101,
        (
            "#1015F#6PWell. You say 'Goddess' and there's really\x01",
            "only one place I can think of.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C54")

    ChrTalk(    #73
        0x106,
        (
            "#050FYep, gotta be it.\x02\x03",

            "Let's get over there.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_1D60")

    label("loc_1C54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C9A")

    ChrTalk(    #74
        0x103,
        (
            "#020FIt must be, yes.\x02\x03",

            "Let's go at once.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_1D60")

    label("loc_1C9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CF5")

    ChrTalk(    #75
        0x108,
        (
            "#070FThe only real answer, isn't it?\x02\x03",

            "Let's go there at once.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    Jump("loc_1D60")

    label("loc_1CF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D60")

    ChrTalk(    #76
        0x104,
        (
            "#030FAh, yes. There is but one answer.\x02\x03",

            "Let us go and bring an end to our quest.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    label("loc_1D60")


    ChrTalk(    #77
        0x101,
        "#1006F#6POff we go!\x02",
    )

    CloseMessageWindow()
    OP_4B(0x19, 255)
    ClearChrFlags(0x19, 0x10)
    SetChrPos(0x19, 27300, -10000, 26800, 315)
    OP_28(0x78, 0x1, 0x40)
    OP_28(0x78, 0x1, 0x80)
    OP_A2(0x11)
    OP_64(0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_1DA9(): pass

    label("Function_1_1DA9")

    OP_6D(23760, -3000, 13010, 2000)
    Return()

    # Function_1_1DA9 end

    def Function_2_1DBB(): pass

    label("Function_2_1DBB")

    OP_6D(27220, -3000, 13160, 2000)
    Sleep(1000)
    OP_6D(22860, -3000, 13110, 2000)
    Return()

    # Function_2_1DBB end

    SaveToFile()

Try(main)
