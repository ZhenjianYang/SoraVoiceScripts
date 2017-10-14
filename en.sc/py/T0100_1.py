from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0100_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0100_1 ._SN',
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
        "Function_1_696",          # 01, 1
        "Function_2_705",          # 02, 2
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 62320, 250, 19870, 239)
    SetChrPos(0xF7, 64480, 0, 19260, 270)
    SetChrPos(0xF8, 65420, 0, 20030, 270)
    SetChrPos(0xF9, 65940, 0, 18510, 269)
    OP_6D(62620, 250, 19470, 0)
    OP_67(0, 7170, -10000, 0)
    OP_6B(2940, 0)
    OP_6C(300000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#1011FThis is Elger's forge.\x02\x03",

            "It's not lit... If anything, it's freezing.\x01",
            "But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x103,
        (
            "#027FYou think this is it?\x02\x03",

            "The eight-eyed iron beast?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #2
        0x101,
        (
            "#1015FYeah. I'm not super confident,\x01",
            "but I think so.\x02\x03",

            "#1000FLet's check it anyway.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x40)
    OP_8C(0x101, 239, 400)
    OP_8E(0x101, 0xF1C2, 0xFA, 0x4BB4, 0x3E8, 0x0)
    OP_8C(0x101, 270, 400)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x101)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #3
        "\x07\x05Estelle found a card and a key inside the hearth.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #4
        0x101,
        "#1004FAha! Found it!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)
    Fade(1000)
    SetChrChipByIndex(0x101, 38)
    OP_0D()

    ChrTalk(    #5
        0x101,
        "#1011FOkay, let's see...\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)

    AnonymousTalk(    #6
        (
            "\x07\x05Take this key, and with it throw open the unopening door.\x01",
            "That which you seek lies in the land beyond.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_AE(0x1F4)
    Sleep(550)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #7
        "\x07\x00Received #565i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x235, 1)
    Sleep(400)
    Fade(1000)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #8
        0x101,
        (
            "#1015FSo, we found a key...\x02\x03",

            "#1019FBut...a key to an 'unopening door.'\x01",
            "Fantastic. Thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#022FI would assume this door is somewhere\x01",
            "in the city.\x02\x03",

            "And, as always, it's probably a metaphor.\x01",
            "Let's look for anything that might be\x01",
            "taken as a 'door.'\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_568")

    ChrTalk(    #10
        0x107,
        "#060FYeah, that's probably the quickest way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_61F")

    label("loc_568")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C5")

    ChrTalk(    #11
        0x106,
        (
            "#053FWell, not like we've got a choice.\x02\x03",

            "#050FC'mon, let's get moving.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_61F")

    label("loc_5C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FB")

    ChrTalk(    #12
        0x108,
        "#070FNot like we have a choice.\x02",
    )

    CloseMessageWindow()
    Jump("loc_61F")

    label("loc_5FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_61F")

    ChrTalk(    #13
        0x104,
        "#035FIf we must.\x02",
    )

    CloseMessageWindow()

    label("loc_61F")


    ChrTalk(    #14
        0x101,
        (
            "#1007FPhew! Feels like we're getting\x01",
            "toward the end, at least.\x02\x03",

            "#1006FBack to searching, then!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    OP_28(0x77, 0x1, 0x40)
    OP_64(0x3, 0x1)
    ClearChrFlags(0x101, 0x40)
    EventEnd(0x4)
    Return()

    # Function_0_AA end

    def Function_1_696(): pass

    label("Function_1_696")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Enter Sewers\x01",      # 0
            "Stop\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6ED"),
        (1, "loc_6F9"),
        (SWITCH_DEFAULT, "loc_6F9"),
    )


    label("loc_6ED")

    NewScene("ED6_DT21/C0500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_6FF")

    label("loc_6F9")

    TalkEnd(0xFF)
    Jump("loc_6FF")

    label("loc_6FF")

    Sleep(30)
    Return()

    # Function_1_696 end

    def Function_2_705(): pass

    label("Function_2_705")

    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(75350, 0, 18760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 75350, 0, 18760, 270)
    SetChrPos(0x1, 75350, 0, 18760, 270)
    SetChrPos(0x2, 75350, 0, 18760, 270)
    SetChrPos(0x3, 75350, 0, 18760, 270)
    OP_30(0x0)
    SetMapFlags(0x1)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    ClearMapFlags(0x80)
    Return()

    # Function_2_705 end

    SaveToFile()

Try(main)
