from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0120_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0120   ._SN',
            'ED6_DT21/T0120_1 ._SN',
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

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_124")

    ChrTalk(    #0
        0x101,
        (
            "#1011FAh, ma'am.\x02\x03",

            "Actually, there's something\x01",
            "I'd like to ask.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #1
        0xFE,
        (
            "Hmm? Something you want to\x01",
            "ask?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B0")

    label("loc_124")


    ChrTalk(    #2
        0x101,
        "#1011FHey, Stella. Got a sec?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #3
        0xFE,
        "Oh? What's this all of a sudden?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        (
            "#1000FUm, there's something I wanted\x01",
            "to ask you about.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Estelle told Stella that Radford was\x01",
            "looking for a certain stew recipe.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #6
        0x103,
        (
            "#020FThat's the deal, but, any idea\x01",
            "where that recipe would be?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #7
        0xFE,
        (
            "Hmm... I know I ate it when\x01",
            "I was a child, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Unfortunately, I never heard the\x01",
            "details of the recipe itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1020FAwww... Even you don't know?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #10
        0xFE,
        (
            "I've read a lot of cookbooks in\x01",
            "my time, too, but I've never seen\x01",
            "that recipe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "It might be a local dish only\x01",
            "handed down in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1007F*sigh* I see...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_3CA")
    Jump("loc_41C")

    label("loc_3CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x400)"), scpexpr(EXPR_END)), "loc_3D8")
    Jump("loc_41C")

    label("loc_3D8")


    ChrTalk(    #13
        0x103,
        (
            "#025F...Tracking this thing down is\x01",
            "tougher than I'd expected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41C")


    ChrTalk(    #14
        0xFE,
        "Sorry I couldn't be any help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "Say, Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Don't forget to take a break\x01",
            "from work sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#1016FAhaha... I'll be careful.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #18
        0xFE,
        (
            "You too, Schera.\x01",
            "Take care of yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        (
            "#021FYes, ma'am.\x02\x03",

            "Anyway, if you'll pardon us.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_28(0x75, 0x1, 0x20)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
