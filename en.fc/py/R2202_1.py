from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2202_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'R2202.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60020",
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
        "Function_1_4B8",          # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    EventBegin(0x0)
    OP_64(0x0, 0x1)
    Fade(1000)
    OP_6C(90000, 0)
    OP_69(0x101, 0x0)
    OP_0D()
    Sleep(800)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x00Found \x07\x02Skull Daggers\x07\x00 and \x07\x02Torn Map\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x335, 1)
    OP_3E(0x2D, 1)
    Sleep(800)

    ChrTalk(    #1
        0x101,
        "#501FWow, awesome daggers!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #2
        0x102,
        (
            "#010FThey seem pretty ancient.\x02\x03",

            "From the look of them, they may even\x01",
            "date back to the Orbal Revolution.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #3
        0x101,
        (
            "#000FWell, what about that piece of\x01",
            "paper?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #4
        0x102,
        "#010FLooks like a piece of a sea chart.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_41D")
    OP_28(0x1E, 0x1, 0x10)
    OP_62(0x101, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #5
        0x101,
        (
            "#004FDo you think...\x02\x03",

            "...maybe this is the treasure that\x01",
            "Jimmy was talking about?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#010FSorry, but I don't think this has\x01",
            "anything to do with it.\x02\x03",

            "#010FI'd say this probably washed ashore\x01",
            "from somewhere else.\x02\x03",

            "It might've been cargo from a\x01",
            "shipwreck.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3A1")
    TurnDirection(0x105, 0x102, 400)

    ChrTalk(    #7
        0x105,
        (
            "#040FYes, I believe you're right.\x02\x03",

            "I heard that such accidents happened\x01",
            "often, long ago.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)
    Jump("loc_41A")

    label("loc_3A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x35)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_41A")
    TurnDirection(0x136, 0x102, 400)

    ChrTalk(    #8
        0x136,
        (
            "#040FYes, I believe you're right.\x02\x03",

            "I heard that such accidents happened\x01",
            "often, long ago.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x136, 400)

    label("loc_41A")

    Jump("loc_423")

    label("loc_41D")

    OP_28(0x1E, 0x1, 0x4000)

    label("loc_423")


    ChrTalk(    #9
        0x101,
        (
            "#505FOh, so before airships, everyone\x01",
            "traveled by water, right?\x02\x03",

            "I wonder if this beach is right on\x01",
            "an old trade route or something,\x01",
            "then...\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Return()

    # Function_0_66 end

    def Function_1_4B8(): pass

    label("Function_1_4B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_40(0x326)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_638")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_581")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #10
        0x105,
        (
            "#040FThis way leads to the Royal Academy...\x02\x03",

            "Is our work situation okay?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #11
        0x101,
        (
            "#000FUh...right.\x02\x03",

            "We should finish everything up\x01",
            "before we go this way.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61A")

    label("loc_581")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #12
        0x102,
        (
            "#010FThis is the Vista Forest Road to\x01",
            "the Royal Academy.\x02\x03",

            "We can go there after we've settled\x01",
            "our current jobs.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #13
        0x101,
        "#000FYeah, okay.\x02",
    )

    CloseMessageWindow()

    label("loc_61A")

    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_70B")

    label("loc_638")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_70B")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_65C")
    TurnDirection(0x102, 0x1, 400)
    Jump("loc_663")

    label("loc_65C")

    TurnDirection(0x102, 0x0, 400)

    label("loc_663")


    ChrTalk(    #14
        0x102,
        (
            "#012FThe Royal Academy is this way.\x02\x03",

            "We need to hurry to the mayor's\x01",
            "estate... We can't waste any time\x01",
            "before the Royal Army gets here.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_70B")

    Return()

    # Function_1_4B8 end

    SaveToFile()

Try(main)
