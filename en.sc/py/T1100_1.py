from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1100_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1100_1 ._SN',
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
        "Function_1_1101",         # 01, 1
        "Function_2_1239",         # 02, 2
        "Function_3_12F0",         # 03, 3
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_336")

    ChrTalk(    #0
        0x101,
        (
            "#1002FWait a minute!\x01",
            "Do you think this might be it?\x02\x03",

            "The place mentioned on the card.\x02",
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
    Jump("loc_332")

    label("loc_19E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_220")

    ChrTalk(    #3
        0x108,
        (
            "#072FIt is possible, but now's not the time.\x02\x03",

            "We must get to Ravennue immediately.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #4
        0x101,
        "#1002FRight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_332")

    label("loc_220")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B3")

    ChrTalk(    #5
        0x104,
        (
            "#030FIt's quite possible.\x02\x03",

            "Now, however, is not the time to ponder.\x01",
            "We must go to Ravennue at once.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #6
        0x101,
        "#1002FRight.\x02",
    )

    CloseMessageWindow()
    Jump("loc_332")

    label("loc_2B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_332")

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
        "#1002FRight.\x02",
    )

    CloseMessageWindow()

    label("loc_332")

    TalkEnd(0xFF)
    Return()

    label("loc_336")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 65390, 3000, 33170, 0)
    SetChrPos(0xF7, 65090, 3000, 31150, 0)
    SetChrPos(0xF8, 66060, 3000, 31080, 0)
    SetChrPos(0xF9, 65600, 3000, 30290, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39E")
    SetChrPos(0x4, 64830, 3000, 29670, 0)

    label("loc_39E")

    OP_6D(65390, 3000, 32689, 0)
    OP_67(0, 7650, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_452")

    ChrTalk(    #9
        0x105,
        (
            "#042FThe hint was, 'RICUL, back the in flower.'\x02\x03",

            "And, 'The end of everything is the beginning.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE")

    label("loc_452")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CF")

    ChrTalk(    #10
        0x107,
        (
            "#062FThe hint was, 'RICUL, back the in flower,'\x01",
            "right?\x02\x03",

            "And, 'The end of everything is the beginning.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE")

    label("loc_4CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_553")

    ChrTalk(    #11
        0x104,
        (
            "#035FThe hint we were given was,\x01",
            "'RICUL, back the in flower.'\x02\x03",

            "And, 'The end of everything is the beginning.'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE")

    label("loc_553")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DE")

    ChrTalk(    #12
        0x103,
        (
            "#026FThe card had two hints.\x01",
            "The first, 'RICUL, back the in flower.'\x02\x03",

            "Second, 'The end of everything is the beginning.'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DE")

    OP_8C(0x101, 180, 400)

    ChrTalk(    #13
        0x101,
        (
            "#1015F#4PIt must be a hint to read them in reverse.\x02\x03",

            "So we have to read the entire phrase backwards.\x01",
            "'RICUL' must be special, though, since it's all in\x01",
            "caps. We probably just reverse the letters there.\x02\x03",

            "You end up with 'Flower in the back, LUCIR.'\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_744")

    ChrTalk(    #14
        0x106,
        (
            "#051FAhh, I get it.\x02\x03",

            "You say 'Lucir' in Bose, and it's gotta\x01",
            "be this place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_855")

    label("loc_744")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_796")

    ChrTalk(    #15
        0x103,
        (
            "#021FNow I see.\x02\x03",

            "Lucir in Bose can only refer to one thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_855")

    label("loc_796")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7EC")

    ChrTalk(    #16
        0x108,
        (
            "#070FRight, of course.\x02\x03",

            "In Bose, 'Lucir' can only be one thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_855")

    label("loc_7EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_855")

    ChrTalk(    #17
        0x104,
        (
            "#030FThe answer is clear.\x02\x03",

            "For what other 'Lucir' lies within the\x01",
            "walls of this city?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_855")

    OP_8C(0x101, 0, 400)

    ChrTalk(    #18
        0x101,
        (
            "#1006F#6PRight, so the card mentions a flower.\x02\x03",

            "Let's take a look.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8AA():

        label("loc_8AA")

        TurnDirection(0xF7, 0x101, 400)
        OP_48()
        Jump("loc_8AA")

    QueueWorkItem2(0xF7, 1, lambda_8AA)

    def lambda_8BB():

        label("loc_8BB")

        TurnDirection(0xF8, 0x101, 400)
        OP_48()
        Jump("loc_8BB")

    QueueWorkItem2(0xF8, 1, lambda_8BB)

    def lambda_8CC():

        label("loc_8CC")

        TurnDirection(0xF9, 0x101, 400)
        OP_48()
        Jump("loc_8CC")

    QueueWorkItem2(0xF9, 1, lambda_8CC)

    def lambda_8DD():
        OP_6D(65470, 3000, 35800, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_8DD)
    OP_8E(0x101, 0xFF6E, 0xBB8, 0x8B9C, 0x7D0, 0x0)
    Sleep(1000)
    WaitChrThread(0xF7, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #19
        "\x07\x05There was a card attached to the pot.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #20
        0x101,
        "#1018F#6PYes! Found it.\x02",
    )

    CloseMessageWindow()
    Sleep(600)
    OP_8C(0x101, 180, 400)

    def lambda_998():
        OP_6D(65470, 3000, 32689, 2000)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_998)
    OP_8E(0x101, 0xFF6E, 0xBB8, 0x8192, 0x7D0, 0x0)
    WaitChrThread(0xF7, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F5")

    ChrTalk(    #21
        0x104,
        "#031FAnother riddle solved.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7D")

    label("loc_9F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A27")

    ChrTalk(    #22
        0x108,
        "#070FAnd that's our answer.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7D")

    label("loc_A27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A58")

    ChrTalk(    #23
        0x103,
        "#020FOne more riddle down.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A7D")

    label("loc_A58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7D")

    ChrTalk(    #24
        0x106,
        "#051FThere we go!\x02",
    )

    CloseMessageWindow()

    label("loc_A7D")


    ChrTalk(    #25
        0x101,
        "#1006F#4POkay, let's see here.\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 8)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "\x07\x05'Your second key is the following spell--\x01",
            "FTHKC2E\x01",
            "View the opened book.'\x02\x03",

            "'And remember always this wisdom! Those who\x01",
            "seek the truth must forever look a step ahead.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x101,
        (
            "#1019F#4PWhat the hell?\x02\x03",

            "'FTHKC2E'? That's our hint?\x01",
            "Pure gibberish?\x02\x03",

            "Thanks, man, now you're also giving\x01",
            "me a headache.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xF7, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CF7")

    ChrTalk(    #28
        0x105,
        (
            "#047FThere must be some kind of trick to\x01",
            "reading it, like the last one.\x02\x03",

            "#042FI would guess that 'look a step ahead'\x01",
            "is an important hint for that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED2")

    label("loc_CF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D7B")

    ChrTalk(    #29
        0x107,
        (
            "#064FThere's gotta be some kind of trick\x01",
            "to reading it, like last time!\x02\x03",

            "Maybe 'look a step ahead' is a hint?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED2")

    label("loc_D7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E2B")

    ChrTalk(    #30
        0x104,
        (
            "#030FI think the riddle lies in the phrase\x01",
            "itself, and how it is read, as in the last.\x02\x03",

            "The 'look a step ahead' portion is\x01",
            "doubtlessly an important hint.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ED2")

    label("loc_E2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED2")

    ChrTalk(    #31
        0x103,
        (
            "#027FI would bet it's just like the last one--\x01",
            "it's all in how you read the phrase.\x02\x03",

            "That 'look a step ahead' portion is also\x01",
            "important, I'd wager.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ED2")

    OP_59()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()

    ChrTalk(    #32
        0x101,
        (
            "#1015F#4POne way or another, how about we just\x01",
            "look around the town?\x02\x03",

            "Maybe we'll figure something out if we\x01",
            "wander a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FC0")

    ChrTalk(    #33
        0x106,
        (
            "#050FYeah, just sittin' here ain't gonna do\x01",
            "much for us.\x02\x03",

            "Let's get movin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D0")

    label("loc_FC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1017")

    ChrTalk(    #34
        0x103,
        (
            "#020FI suppose thinking with our feet might help.\x02\x03",

            "Let's be off.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D0")

    label("loc_1017")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_107A")

    ChrTalk(    #35
        0x108,
        (
            "#070FYes, motion of the body does inspire\x01",
            "motion of the mind.\x02\x03",

            "Let's be off!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D0")

    label("loc_107A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10D0")

    ChrTalk(    #36
        0x104,
        (
            "#030FIndeed, inspiration may come to us\x01",
            "as we walk.\x02\x03",

            "Let's be off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10D0")


    ChrTalk(    #37
        0x101,
        "#1000F#4PYeah, let's go.\x02",
    )

    CloseMessageWindow()
    OP_28(0x78, 0x1, 0x4)
    OP_28(0x78, 0x1, 0x8)
    OP_64(0x0, 0x1)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    def Function_1_1101(): pass

    label("Function_1_1101")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x381), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_110E")
    Return()

    label("loc_110E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x79, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1120")
    Return()

    label("loc_1120")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xF)"), scpexpr(EXPR_END)), "loc_115B")
    Call(1, 2)
    Jump("loc_1232")

    label("loc_115B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xE)"), scpexpr(EXPR_END)), "loc_116A")
    Call(1, 3)
    Jump("loc_1232")

    label("loc_116A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CD(0xFF)"), scpexpr(EXPR_END)), "loc_11DC")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #38
        "\x07\x05Tried showing them the photograph, but they didn't recognize her.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1232")

    label("loc_11DC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        "\x07\x05There's no one to show the photograph to nearby.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_1232")

    OP_0D()
    ClearMapFlags(0x80)
    Return()

    # Function_1_1101 end

    def Function_2_1239(): pass

    label("Function_2_1239")

    TalkBegin(0xF)

    ChrTalk(    #40
        0xF,
        (
            "My, what a lovely little girl!\x01",
            "Sadly, I don't recognize her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xF,
        (
            "Perhaps you would have more luck in\x01",
            "the North Block, though? You'll find more\x01",
            "people there at this hour.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xF)
    Return()

    # Function_2_1239 end

    def Function_3_12F0(): pass

    label("Function_3_12F0")

    TalkBegin(0xE)

    ChrTalk(    #42
        0xE,
        "A girl orphaned during the war?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xE,
        (
            "A sad and familiar story, unfortunately.\x01",
            "Alas, I fear I don't know her. Good luck\x01",
            "to you, though.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_3_12F0 end

    SaveToFile()

Try(main)
