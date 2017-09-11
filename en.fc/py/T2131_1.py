from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T2131_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T2131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_6C3",          # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_28(0x20, 0x1, 0x8)
    Fade(1000)
    SetChrPos(0x102, 25900, 0, 26500, 315)
    SetChrPos(0x101, 27000, 0, 26500, 315)
    SetChrPos(0x105, 27500, 0, 27100, 270)
    OP_51(0x9, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6158), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6DC4), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x9, 0x7D0)

    ChrTalk(    #0
        0x101,
        (
            "#006FA red and black waltz...?\x02\x03",

            "I can't imagine it means anything\x01",
            "but roulette.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #1
        0x102,
        (
            "#010FI think you're right.\x02\x03",

            "Let's check it out.\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #2
        0x8,
        (
            "Is there something you're looking\x01",
            "for, sir and madams?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D2():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D2)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #3
        0x102,
        (
            "#010FSorry, but we'll be done in just\x01",
            "a moment.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21C():

        label("loc_21C")

        TurnDirection(0x101, 0x102, 0)
        OP_48()
        Jump("loc_21C")

    QueueWorkItem2(0x101, 1, lambda_21C)

    def lambda_22D():

        label("loc_22D")

        TurnDirection(0x105, 0x102, 0)
        OP_48()
        Jump("loc_22D")

    QueueWorkItem2(0x105, 1, lambda_22D)

    def lambda_23E():

        label("loc_23E")

        TurnDirection(0x8, 0x102, 0)
        OP_48()
        Jump("loc_23E")

    QueueWorkItem2(0x8, 1, lambda_23E)
    SetChrFlags(0x102, 0x40)
    OP_8E(0x102, 0x6572, 0x0, 0x6A4A, 0x7D0, 0x0)
    OP_8C(0x102, 315, 400)
    OP_44(0x101, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x8, 0x1)
    Sleep(600)
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #4
        0x102,
        (
            "#012FAh-ha. Found it.\x02\x03",

            "A card is glued flat to the surface.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x105,
        (
            "#040FSo...it should have the next\x01",
            "message, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 400)

    ChrTalk(    #6
        0x102,
        "#010FYeah, let's take a look.\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #7
        (
            "\x07\x00'Ah, seeker. The eyes of Aidios see only the truth,\x01",
            "and pass it on to you. Rest at the land harbor and\x01",
            "look to the one-eyed lion. Do so, and the blue light\x01",
            "will be revealed.\x01\x01",
            "-Phantom Thief B'\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)

    def lambda_432():

        label("loc_432")

        TurnDirection(0x105, 0x102, 0)
        OP_48()
        Jump("loc_432")

    QueueWorkItem2(0x105, 1, lambda_432)

    def lambda_443():

        label("loc_443")

        TurnDirection(0x8, 0x102, 0)
        OP_48()
        Jump("loc_443")

    QueueWorkItem2(0x8, 1, lambda_443)
    OP_8E(0x102, 0x652C, 0x0, 0x6784, 0x7D0, 0x0)

    def lambda_468():
        TurnDirection(0x102, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_468)
    TurnDirection(0x101, 0x102, 400)
    OP_44(0x105, 0x1)
    OP_44(0x8, 0x1)
    Sleep(400)

    ChrTalk(    #8
        0x101,
        (
            "#006FOkay, I've added it to my\x01",
            "Bracer Notebook.\x02\x03",

            "The important parts are probably the\x01",
            "'land harbor' and the 'one-eyed lion.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x105,
        "#043F'One-eyed' this time...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#010FIt's always made more sense once\x01",
            "we got there before... I doubt this\x01",
            "time will be any different.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #11
        0x101,
        (
            "#006FYeah, I guess we need to get\x01",
            "a move on. A madman's clues\x01",
            "MUST be followed, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #12
        0x8,
        "???\x02",
    )

    CloseMessageWindow()

    def lambda_627():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_627)

    def lambda_635():
        TurnDirection(0x105, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_635)
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #13
        0x101,
        "#001FSorry to cause all the fuss!\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_8C(0x8, 0, 0)
    OP_4B(0x8, 255)
    OP_64(0x0, 0x1)
    OP_51(0x1, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x102, 0x40)
    EventEnd(0x0)
    Return()

    # Function_0_66 end

    def Function_1_6C3(): pass

    label("Function_1_6C3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05There are some fishing rods propped against the rack.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_73C")
    OP_28(0x21, 0x1, 0x1000)
    Jump("loc_908")

    label("loc_73C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x332)"), scpexpr(EXPR_END)), "loc_7A7")
    Sleep(400)

    ChrTalk(    #15
        0x101,
        (
            "#000FIf we're done using it, we need to\x01",
            "take this fishing rod back to the\x01",
            "shopkeeper.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_908")

    label("loc_7A7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_7F9")
    Sleep(400)

    ChrTalk(    #16
        0x101,
        (
            "#007FOkay, this time, I want to actually\x01",
            "catch something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_908")

    label("loc_7F9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_806")
    Jump("loc_908")

    label("loc_806")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x21, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_8BE")
    Sleep(400)
    OP_28(0x21, 0x1, 0x1000)

    ChrTalk(    #17
        0x101,
        (
            "#501FDo you think we could\x01",
            "borrow one of these?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#010FWe'll have to ask the shopkeeper.\x02\x03",

            "The bartender was on the first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#000FOh, right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_908")

    label("loc_8BE")

    Sleep(400)
    OP_28(0x21, 0x1, 0x1000)

    ChrTalk(    #20
        0x101,
        (
            "#501FI wonder if we'll be able to\x01",
            "borrow one for a bit...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_908")

    TalkEnd(0xFF)
    Return()

    # Function_1_6C3 end

    SaveToFile()

Try(main)
