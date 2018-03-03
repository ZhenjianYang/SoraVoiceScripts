from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R2201   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2201.x',
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
        'Fisher',                               # 9
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
        Unknown_3A              = 101,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01200 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01200P._CP',             # 00
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_D2",           # 00, 0
        "Function_1_EF",           # 01, 1
        "Function_2_F0",           # 02, 2
        "Function_3_119",          # 03, 3
        "Function_4_768",          # 04, 4
        "Function_5_C61",          # 05, 5
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    OP_B1("R2201_1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_EE")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_EE")

    Return()

    # Function_0_D2 end

    def Function_1_EF(): pass

    label("Function_1_EF")

    Return()

    # Function_1_EF end

    def Function_2_F0(): pass

    label("Function_2_F0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D6(0x0)
    OP_E3(0x0, 0xC, 1, 0x0)
    ClearParty()
    AddParty(0x0, 0xEE, 0xFF)
    OP_28(0x1E, 0x4, 0x8)
    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_F0 end

    def Function_3_119(): pass

    label("Function_3_119")

    OP_72(0x0, 0x0)
    ExitThread()
    OP_72(0x1, 0x0)
    ExitThread()
    OP_72(0x2, 0x0)
    ExitThread()
    OP_72(0x3, 0x0)
    ExitThread()
    OP_72(0x4, 0x0)
    ExitThread()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, 65099, -6000, -25940, 294)
    SetChrPos(0x10, 63790, -6000, -24800, 146)
    OP_6D(64629, -6000, -25100, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_77(0xCC, 0x8E, 0x5A, 0x0, 0x0)
    OP_C4(0x0, 0x800)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x20000000)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0 op#A op#5
        "\x07\x00#15A～Final Chapter - Battle at Azelia Bay～\x05\x02",
    )

    CloseMessageWindow()
    Sleep(3000)
    OP_56(0x0)
    Sleep(1000)
    OP_23(0x1C8)
    OP_75(0xFF, 0x11, 0x5)
    OP_75(0xFF, 0x12, 0x5)
    OP_75(0xFF, 0x1A, 0x5)
    OP_75(0xFF, 0x1B, 0x5)
    FadeToBright(3000, 0)
    OP_1E()
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, 80)
    Sleep(2000)

    AnonymousTalk(    #1
        (
            "\x07\x00Along the shore off Gull Seaside Way, near Ruan...\x02\x01",

            "...the decisive moment that Norche had foretold\x01",
            "was finally to come.\x02\x01",

            "Whether their meeting was a coincidence or fated\x01",
            "all along, no one could possibly say...\x02\x01",

            "Estelle was idly walking along shore for no particularly\x01",
            "adequate reason, when all of a sudden, a single small\x01",
            "yacht drew closer and closer.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #2
        (
            "\x07\x00The yacht eased as close to the shore as it could\x01",
            "safely get, and from on top of it stepped a fine\x01",
            "man.\x02\x01",

            "He was a gentleman in a tuxedo, the sea extending\x01",
            "into the distance behind him making for an equally\x01",
            "elegant backdrop.\x02\x01",

            "As soon as she saw him, she knew he was the leader\x01",
            "Norche had spoke of.\x02\x01",

            "Mr. Fisher, bearer of the title Avid Angler and known\x01",
            "by the nickname of Fishing Baron.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_22(0x1C8, 0x1, 0x64)
    FadeToBright(1000, 0)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
    OP_75(0xFF, 0x11, 0x3)
    OP_75(0xFF, 0x12, 0x3)
    OP_75(0xFF, 0x1A, 0x3)
    OP_75(0xFF, 0x1B, 0x3)
    Sleep(4000)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #3
        0x10,
        "...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        "That lure! That ROD!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1011FA-Are you the Fisherman's Guild's president?\x01",
            "I'm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        "No! There is no need for words now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "I have been awaiting this moment for longer\x01",
            "than you can possibly imagine!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "I challenge you to a 15-round anglers' duel!\x01",
            "Immediately!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1016FF-Fifteen?!\x02\x03",

            "We're gonna be here all day, aren't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        "Let the battle begin!\x02",
    )

    CloseMessageWindow()
    OP_C4(0x1, 0x20000000)
    OP_23(0x1C8)
    Sleep(300)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_20(0xBB8)
    OP_21()
    Return()

    # Function_3_119 end

    def Function_4_768(): pass

    label("Function_4_768")

    OP_1D(0xC0)
    OP_AD(0x240139, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_781")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C60")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        330,
        0,
        (
            "Start\x01",      # 0
            "Rules\x01",      # 1
            "Quit\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0xFF)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7D5"),
        (1, "loc_7FF"),
        (2, "loc_C1E"),
        (SWITCH_DEFAULT, "loc_C5D"),
    )


    label("loc_7D5")

    OP_AE(0x1F4)
    Sleep(1000)
    Call(0, 5)
    OP_1D(0xC0)
    OP_AD(0x240139, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C5D")

    label("loc_7FF")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "Estelle and Mr. Fisher will face off in a 15-round duel of the century.\x01",
            "Both will take turns at fishing, and whoever has the most points at the\x01",
            "end of the 15 rounds will be declared the winner.\x01\x01",
            "When it is Estelle's turn, you will be prompted to choose a rod and a bait\x01",
            "to use. Certain baits can only be used with certain rods.\x01\x01",
            "After choosing, the game begins. When the ! mark appears, quickly press\x01",
            "confirm to catch the fish.\x01\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "Certain fish can only be caught with certain baits, and in addition, some\x01",
            "fish can be used as bait to catch other fish.\x01\x01",
            "Different varieties of fish are worth different amounts of points, making\x01",
            "trying to catch more valuable ones the key to success.\x01\x01",
            "More valuable ones are also more likely to escape, but don't let that deter\x01",
            "you.\x01\x01",
            "―――――――――――――――――――――――――――#20W\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_C5D")

    label("loc_C1E")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_C51")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_C5A")

    label("loc_C51")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_C5A")

    Jump("loc_C5D")

    label("loc_C5D")

    Jump("loc_781")

    label("loc_C60")

    Return()

    # Function_4_768 end

    def Function_5_C61(): pass

    label("Function_5_C61")

    OP_AE(0x1F4)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(58740, -6720, -62720, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, 60130, -6720, -62280, 243)
    SetChrPos(0x10, 64900, -6760, -69120, 243)
    OP_48()
    OP_3E(0x24F, 1)
    OP_3E(0x252, 1)
    OP_3E(0x253, 1)
    OP_3E(0x3DB, 10)
    OP_3E(0x3DC, 10)
    OP_22(0x1C8, 0x1, 0x64)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_C0(0x1B, 0x2, 0xFFFFF470, 0xFFFFF830, 0x7EF4, 0xE1, 0xFFFFF45C, 0xFFFFF448, 0x72C4)"), scpexpr(EXPR_END)), "loc_D3E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D48")

    label("loc_D3E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D48")

    EventBegin(0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, 65099, -6000, -25940, 294)
    SetChrPos(0x10, 63790, -6000, -24800, 146)
    OP_6D(64629, -6000, -25100, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    Sleep(3000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_DC9"),
        (0, "loc_F54"),
        (SWITCH_DEFAULT, "loc_F57"),
    )


    label("loc_DC9")

    FadeToBright(1000, 0)
    OP_1E()
    Sleep(1000)

    ChrTalk(    #13
        0x101,
        "#1007FI-I lost...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        "Bwahaha! I knew I was the strongest angler of all!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "But you are welcome to challenge me again whenever\x01",
            "you see fit. I welcome all attempts to claim my\x01",
            "title!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_20(0x7D0)
    OP_0D()
    OP_23(0x1C8)
    Sleep(1000)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "\x18\x07\x05Try again?\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "Try Again\x01",       # 0
            "Leave Door\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_F1B"),
        (0, "loc_F45"),
        (SWITCH_DEFAULT, "loc_F54"),
    )


    label("loc_F1B")

    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_F36")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_F3F")

    label("loc_F36")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_F3F")

    Jump("loc_F54")

    label("loc_F45")

    OP_D6(0x1)
    OP_D6(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_F54")

    Jump("loc_F57")

    label("loc_F57")

    FadeToBright(1000, 0)
    OP_1E()
    OP_C4(0x0, 0x20000000)
    Sleep(1000)

    ChrTalk(    #17
        0x10,
        (
            "Unbelievable... I had no idea you would\x01",
            "prove to be quite so skilled...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "Clearly the time for adults to be leading\x01",
            "the way has passed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        "I asked that you accept this.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10, 0xFB54, 0xFFFFE890, 0xFFFF9DAE, 0x7D0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05Fisher handed over a rainbow-colored fishing line.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_8F(0x10, 0xF92E, 0xFFFFE890, 0xFFFF9F20, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #21
        0x101,
        "#1008FWow... This is so pretty! Thank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "I can hardly believe the time has finally come for\x01",
            "the three famed fishing tackles to be gathered in\x01",
            "the hands of one owner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        "You said your name was Estelle, yes?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1011FY-Yeah. I did, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        "I've made up my mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "Starting today, you will be the new leader\x01",
            "of the Fisherman's Guild!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1004F...Dwuh?\x02\x03",

            "#1005FWHAT?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "As for me...I suppose I'll assume the title of\x01",
            "honorary president from this day forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "This is the time for young people like you to\x01",
            "take the center stage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "I hope you will dedicate yourself as best you\x01",
            "can to spreading and furthering fishing culture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1004FH-Hold on! You can't just shove that kind of\x01",
            "responsibility on someone! I'm not gonna be\x01",
            "the leader!\x02",
        )
    )

    CloseMessageWindow()
    OP_C4(0x1, 0x20000000)
    FadeToDark(2000, 0, -1)
    OP_23(0x1C8)
    Sleep(1500)
    OP_C4(0x0, 0x800)
    Sleep(1500)
    FadeToDark(0, 0, -1)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #33
        (
            "\x07\x00After roughly an hour of continuous negotiations in\x01",
            "which neither of them wished to back down...\x02\x01",

            "...Estelle was able to convince Mr. Fisher that the burden\x01",
            "of being leader was too great for her, and she was granted\x01",
            "an honorary member of the guild instead.\x02\x01",

            "But while Estelle's duels were over, news of what had\x01",
            "happened spread like wildfire among fishermen,\x01",
            "spawning legends that would persist much longer.\x02\x01",

            "Henceforth, whenever they spoke of Estelle, they spoke\x01",
            "of her with a new nickname...\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #34
        (
            "\x07\x00A fitting nickname for one who had triumphed in such\x01",
            "challenging anglers' duels...\x02\x01",

            "...Estelle the Supreme Fisher.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C4(0x1, 0x800)
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_F7(0xB, 0x2, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x00Side Story [Legendary Angler Estelle] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1E, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1760")
    Sleep(3000)
    OP_28(0x1E, 0x4, 0x20)
    OP_28(0x1E, 0x4, 0x10)
    OP_3E(0x12C, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #36
        "\x07\x05Received \x1F\x2C\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #37
        "\x07\x05Received \x07\x025,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_1760")

    Sleep(2000)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_177B")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_1784")

    label("loc_177B")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_1784")

    Return()

    # Function_5_C61 end

    SaveToFile()

Try(main)
