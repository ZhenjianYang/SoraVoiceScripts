from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1101_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        "Function_1_309",          # 01, 1
        "Function_2_321",          # 02, 2
    )


    def Function_0_66(): pass

    label("Function_0_66")

    TalkBegin(0x14)

    ChrTalk(    #0
        0xFE,
        "Are you ready to go?\x02",
    )

    CloseMessageWindow()

    label("loc_83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FB")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Yep, we're good to go.]\x01",      # 0
            "[Sorry, not yet.]\x01",             # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_100"),
        (1, "loc_256"),
        (SWITCH_DEFAULT, "loc_2F8"),
    )


    label("loc_100")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_28(0x10, 0x4, 0x8)
    OP_28(0x10, 0x1, 0x4)

    ChrTalk(    #1
        0x101,
        "#006FYep, we're good to go.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #2
        0xFE,
        "Great, I'm ready myself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "All right, then. I'll leave the\x01",
            "rest up to you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #4
        0x103,
        (
            "#020FThe Krone Pass is to the west\x01",
            "of here.\x02\x03",

            "It's pretty far, so let's not get\x01",
            "careless along the way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 400)

    ChrTalk(    #5
        0x102,
        "#010FUnderstood.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #6
        0x101,
        "#000FLet's get going, shall we?\x02",
    )

    CloseMessageWindow()
    Call(1, 1)
    Jump("loc_2F8")

    label("loc_256")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)

    ChrTalk(    #7
        0x101,
        (
            "#000FSorry, not yet.\x01",
            "We need a little more time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #8
        0xFE,
        "Please make it quick.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I've got an important business\x01",
            "deal to take care of.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F8")

    label("loc_2F8")

    Jump("loc_83")

    label("loc_2FB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x14)
    Return()

    # Function_0_66 end

    def Function_1_309(): pass

    label("Function_1_309")

    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0x34, 0x3)
    NewScene("ED6_DT01/R1200   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_1_309 end

    def Function_2_321(): pass

    label("Function_2_321")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrPos(0x101, 24400, 0, 46300, 270)
    SetChrPos(0x102, 25400, 0, 45300, 270)
    SetChrPos(0x103, 24500, 0, 44300, 270)
    OP_69(0x14, 0x0)
    TalkBegin(0x14)
    FadeToBright(1000, 0)
    OP_0D()
    TurnDirection(0x101, 0x14, 400)

    ChrTalk(    #10
        0x101,
        (
            "#501FSorry, Mr. Hardt. We still have\x01",
            "some preparations to make for\x01",
            "the trip.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x101, 400)

    ChrTalk(    #11
        0x14,
        (
            "I'll be waiting here, so please\x01",
            "try to be quick about it.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    TalkEnd(0x14)
    Return()

    # Function_2_321 end

    SaveToFile()

Try(main)
