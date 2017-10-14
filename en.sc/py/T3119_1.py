from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T3119_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3119_1 ._SN',
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

    EventBegin(0x0)
    OP_59()
    Fade(1000)
    SetChrPos(0x101, -560, 0, 5410, 0)
    SetChrPos(0xF7, 50, 0, 4460, 0)
    SetChrPos(0xF8, -1250, 0, 4210, 0)
    SetChrPos(0xF9, -520, 0, 3020, 0)
    OP_6D(-560, 0, 5410, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #0
        0x101,
        (
            "#1020FH-Hey, this...\x02\x03",

            "Why the heck is something like\x01",
            "this written in the Capel?!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DC")

    ChrTalk(    #1
        0x107,
        (
            "#065FMmmm, most likely someone\x01",
            "stole the password and changed\x01",
            "some data.\x02\x03",

            "If you use administrator-level\x01",
            "access, then anyone can enter\x01",
            "data, so...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)

    ChrTalk(    #2
        0x101,
        "#1004FS-So, like, anyone can do that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x107,
        (
            "#561FN-No, most people can't.\x01",
            "Nope, nope, nope.\x02\x03",

            "I know I'm saying it, but I can\x01",
            "hardly believe it myself...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_440")

    label("loc_2DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38E")

    ChrTalk(    #4
        0x104,
        (
            "#032FHow such a thing was accomplished,\x01",
            "I do not know, but the data appears to\x01",
            "have been overwritten.\x02\x03",

            "#031FHahaha. Even for my enemy, I must\x01",
            "say, 'bravo!'\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_440")

    label("loc_38E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_440")

    ChrTalk(    #5
        0x105,
        (
            "#042FHmmm... I couldn't tell you how,\x01",
            "but the data itself was overwritten.\x02\x03",

            "I highly doubt any amateur could\x01",
            "lay their hands on this machine so\x01",
            "easily, but...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4C1")

    ChrTalk(    #6
        0x106,
        (
            "#551FGeez, is there anything this\x01",
            "nutcase doesn't have up his sleeve?\x02\x03",

            "#050FWhatever. You wrote that down,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_533")

    label("loc_4C1")


    ChrTalk(    #7
        0x103,
        (
            "#025FMy, my. He really IS a bottomless\x01",
            "bag of tricks.\x02\x03",

            "#020FPutting that aside...you wrote that\x01",
            "down, right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_533")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #8
        0x101,
        (
            "#1006FYeah, of course.\x02\x03",

            "#1015FOur next stop's somewhere\x01",
            "in the town.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_609")
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #9
        0x105,
        (
            "#040FI believe we're searching for\x01",
            "'Three Hatted Brothers.'\x02\x03",

            "It must be a metaphor of some kind.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x105, 400)
    Jump("loc_67F")

    label("loc_609")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_67F")
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #10
        0x104,
        (
            "#030FWe now seek the 'Three Hatted Brothers.'\x02\x03",

            "Doubtlessly a metaphor for something.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x104, 400)

    label("loc_67F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6C9")

    ChrTalk(    #11
        0x106,
        (
            "#050FAll right, that's plenty to\x01",
            "work off of.\x02\x03",

            "Let's move.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_71A")

    label("loc_6C9")


    ChrTalk(    #12
        0x103,
        (
            "#020FMmm, that's plenty enough\x01",
            "to go on, thankfully.\x02\x03",

            "Let's head into town.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_71A")

    EventEnd(0x0)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
