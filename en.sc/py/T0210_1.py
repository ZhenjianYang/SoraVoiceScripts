from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0210_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0210   ._SN',
            'ED6_DT21/T0210_1 ._SN',
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
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #0
        0x101,
        (
            "#1011FAh, ma'am.\x02\x03",

            "Could we have a moment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Oh, certainly. What is it?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Estelle told the Mrs. Mylene that she was looking for a stew\x01",
            "recipe on behalf of Mr. Radford.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #3
        0xFE,
        "A stew recipe? Hmm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x103,
        "#020FDid you know the recipe, perhaps?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #5
        0xFE,
        (
            "I'm sorry to disappoint you, but I'm just\x01",
            "not very knowledgeable when it comes\x01",
            "to cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I know I've had the stew he's talking\x01",
            "about, but I've no idea how to make it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1007FAwww. That's too bad...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_317")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #8
        0x103,
        (
            "#020FFor now, let's report that\x01",
            "recipe we got.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #9
        0x101,
        "#1015FYeah, no other choice.\x02",
    )

    CloseMessageWindow()
    Jump("loc_676")

    label("loc_317")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_392")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #10
        0x103,
        (
            "#020FShouldn't we just accept it and\x01",
            "go check out Rhett's house?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #11
        0x101,
        "#1015FHmm... Maybe.\x02",
    )

    CloseMessageWindow()
    Jump("loc_676")

    label("loc_392")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CF")

    ChrTalk(    #12
        0x107,
        "#063FWe're not finding any clues, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B3")

    label("loc_3CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_418")

    ChrTalk(    #13
        0x105,
        (
            "#043FWe're not having any luck\x01",
            "with clues, are we?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3")

    label("loc_418")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46D")

    ChrTalk(    #14
        0x104,
        (
            "#032FHmm. All this investigating and\x01",
            "the clues still elude us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B3")

    label("loc_46D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B3")

    ChrTalk(    #15
        0x108,
        (
            "#075FWe're not having any luck with\x01",
            "clues, are we?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B3")

    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #16
        0x103,
        (
            "#020FWell, no point letting it bother us.\x02\x03",

            "We've done what we can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1006FYeah... It'll leave a bad taste in\x01",
            "my mouth if we give up at this point,\x01",
            "though.\x02\x03",

            "Thanks for your help, ma'am.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #18
        0xFE,
        (
            "No, no need for thanks.\x01",
            "I'm sorry I couldn't help more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I'm sure you're quite overburdened,\x01",
            "but we appreciate everything you do.\x01",
            "Keep up the good work, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1006FYes, ma'am. We will.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xFE, 400)

    ChrTalk(    #21
        0x103,
        "#020FIf you'll pardon us.\x02",
    )

    CloseMessageWindow()

    label("loc_676")

    OP_A2(0x6)
    OP_28(0x75, 0x1, 0x40)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
