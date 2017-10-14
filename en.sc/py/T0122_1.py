from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0122_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0122   ._SN',
            'ED6_DT21/T0122_1 ._SN',
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
    OP_8C(0xFE, 180, 0)
    Fade(1000)
    SetChrPos(0x101, -40360, 0, -4070, 270)
    SetChrPos(0x103, -39740, 0, -4770, 270)
    SetChrPos(0xF8, -38890, 0, -3380, 270)
    SetChrPos(0xF9, -38350, 0, -4310, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B")
    SetChrPos(0xF9, -38890, 0, -3380, 270)
    SetChrPos(0xF8, -38350, 0, -4310, 270)

    label("loc_12B")

    OP_6D(-39690, 0, -3410, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #0
        0xFE,
        "Hmmhmmhmmmmm! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Heheh, sometimes a relaxing\x01",
            "shopping trip is just the ticket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1000F#4PSorry, can we have a moment?\x02\x03",

            "Are you Quint from the\x01",
            "Liberl Orbalship Company?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #3
        0xFE,
        "Huh? Yeah, that's me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "Can I help you with something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1002F#4PYeah, if you've got a sec. There's\x01",
            "something we wanted to ask.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05Estelle explained that she was looking for a wheat-colored\x01",
            "cat.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #7
        0xFE,
        (
            "Searching for a lost cat, huh?\x01",
            "Must be extra hard on a night\x01",
            "like this with all the fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Sorry to say, I can't help. Haven't\x01",
            "seen anything like that cat around\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #9
        0x101,
        "#1004F#4PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x103,
        "#023F#4PYou haven't seen her?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Yeah, I swear on Aidios Herself\x01",
            "that I ain't seen a cat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "I just heard about it secondhand.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B5")

    ChrTalk(    #13
        0x106,
        "#052FWho'd you hear it from?\x02",
    )

    CloseMessageWindow()
    Jump("loc_54D")

    label("loc_4B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4EC")

    ChrTalk(    #14
        0x108,
        "#073FOh? Who'd you hear it from?\x02",
    )

    CloseMessageWindow()
    Jump("loc_54D")

    label("loc_4EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51E")

    ChrTalk(    #15
        0x104,
        "#033FSecondhand? From whom?\x02",
    )

    CloseMessageWindow()
    Jump("loc_54D")

    label("loc_51E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54D")

    ChrTalk(    #16
        0x105,
        "#040FSecondhand? From whom?\x02",
    )

    CloseMessageWindow()

    label("loc_54D")


    ChrTalk(    #17
        0xFE,
        "Zosimov, from the same crew.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I think he said something about\x01",
            "seeing a cat when he was working\x01",
            "in the airfield.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "If you want, I'm sure he'd be happy\x01",
            "to provide more details. He should\x01",
            "still be on the clock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1015F#4PAt the landing port, right? \x02\x03",

            "#1007F*siiiiigh* Aaaand now we have\x01",
            "to turn right back around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#025FIt's not that far. Walk first,\x01",
            "complain later.\x02\x03",

            "#020FWe need to find Zosimov.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_716")

    ChrTalk(    #22
        0x107,
        "#060FMmm! Let's go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C5")

    label("loc_716")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_740")

    ChrTalk(    #23
        0x105,
        "#040FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C5")

    label("loc_740")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77D")

    ChrTalk(    #24
        0x104,
        "#030FHeh. Well, then, shall we be off?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7C5")

    label("loc_77D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C5")

    ChrTalk(    #25
        0x108,
        (
            "#070FAll right, let's head over to the\x01",
            "landing port.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C5")

    OP_28(0x74, 0x1, 0x40)
    OP_28(0x74, 0x1, 0x80)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
