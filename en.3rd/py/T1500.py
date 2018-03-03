from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1500   ._SN',
        MapName             = 'Bose',
        Location            = 'T1500.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Lloyd',                                # 9
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


    AddCharChip(
        'ED6_DT07/CH01020 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
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
        "Function_1_E6",           # 01, 1
        "Function_2_F0",           # 02, 2
        "Function_3_113",          # 03, 3
        "Function_4_C75",          # 04, 4
        "Function_5_1182",         # 05, 5
        "Function_6_1989",         # 06, 6
    )


    def Function_0_D2(): pass

    label("Function_0_D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_E5")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_E5")

    Return()

    # Function_0_D2 end

    def Function_1_E6(): pass

    label("Function_1_E6")

    OP_B1("T1500_n")
    Return()

    # Function_1_E6 end

    def Function_2_F0(): pass

    label("Function_2_F0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_10A")
    Call(0, 6)

    label("loc_10A")

    Call(0, 3)
    Call(0, 4)
    Return()

    # Function_2_F0 end

    def Function_3_113(): pass

    label("Function_3_113")

    OP_1D(0x14)
    OP_C4(0x1, 0x800)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, 2190, -2000, 42760, 180)
    SetChrPos(0x10, 2280, -2000, 41180, 0)
    OP_6D(2190, -1800, 41900, 0)
    OP_67(0, 8970, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_77(0xCE, 0x98, 0x58, 0x0, 0x0)
    OP_C4(0x0, 0x800)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x0, 0x20000000)
    Sleep(2000)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x00Once upon a time, there was a girl called Estelle\x01",
            "Bright who absolutely loved fishing.\x02\x01",

            "Meanwhile, in Grancel, there existed a group of\x01",
            "dedicated men and women who prided themselves\x01",
            "on the sport. They were called the Fisherman's Guild.\x02\x01",

            "What else could it possibly called but 'fate' were\x01",
            "the two paths to cross?\x02\x01",

            "This is their peculiar story.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1 op#A op#5
        "\x07\x00#15A～Chapter 1 - Our Story Begins at the Lakeside～\x05\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_21()
    OP_56(0x0)
    Sleep(1000)
    OP_1D(0xF)
    OP_75(0xFF, 0x3, 0x5)
    OP_75(0xFF, 0x4, 0x5)
    OP_72(0x802, 0x0)
    ExitThread()
    FadeToBright(3000, 0)
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, 80)
    Sleep(2000)

    AnonymousTalk(    #2
        (
            "\x07\x00At the side of Valleria Lake lies a quiet little\x01",
            "place by the name of the Kingfisher Inn. \x02\x01",

            "Seeking a break from her work, Estelle decided\x01",
            "to visit for some well-deserved relaxation.\x02\x01",

            "At first, she had gotten exactly that.\x02\x01",

            "The fishing lover she was, she decided to borrow\x01",
            "some gear from the inn and make her way out\x01",
            "onto the pier to enjoy some quality time there.\x02\x01",

            "She saw one successful catch after another, and\x01",
            "before long, her bucket was teeming with fish.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #3
        (
            "\x07\x00But then there was Lloyd, a member of that one and\x01",
            "only Fisherman's Guild, who happened to be at that\x01",
            "very same inn and on that very same day. He was\x01",
            "having the opposite of young Estelle's lucky streak.\x02\x01",

            "The moment he had arrived, he had set off in a boat\x01",
            "to begin fishing...\x02\x01",

            "but try as he did, he hadn't managed to catch so\x01",
            "much as a single fish.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #4
        (
            "\x07\x00Now feeling thoroughly defeated, Lloyd motioned\x01",
            "back towards the inn.\x02\x01",

            "Upon his boat approaching the pier, however,\x01",
            "he caught sight of none other than a very pleased\x01",
            "Estelle rejoicing the size of her most recent catch. \x02\x01",

            "This sight was all it took to give rise to Lloyd's\x01",
            "competitive nature.\x02\x01",

            "Now thoroughly fired up, he approached her and\x01",
            "challenged her to a special kind of duel...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(1000)
    OP_22(0x1CC, 0x1, 0x64)
    FadeToBright(1000, 0)
    OP_C4(0x1, 0x800)
    Sleep(500)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x9C4)
    OP_75(0xFF, 0x3, 0x1)
    OP_75(0xFF, 0x4, 0x1)
    OP_71(0x802, 0x0)
    ExitThread()
    Sleep(4000)

    ChrTalk(    #5
        0x10,
        (
            "...And that's why I want to challenge you\x01",
            "to a five-round anglers' duel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1004FA-A what, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        "A five-round anglers' duel!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "It's a special kinda competition we fishermen\x01",
            "take part in where they stake their pride and\x01",
            "honor on the outcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "Once a member of the Fisherman's Guild\x01",
            "mentions those words, there can be no\x01",
            "turning back. The duel must take place!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "So let us do battle, with our finest fishing\x01",
            "tackle on the line!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1019FI feel like I'm getting dragged into something\x01",
            "completely nutso...\x02\x03",

            "#1015FI hate to break it to you, but I don't have any\x01",
            "stellar fishing tackle to bet on this. All my stuff\x01",
            "was borrowed from the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "Then you don't need to bet anything at all!\x01",
            "That's fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "This duel is more for my own good than yours,\x01",
            "and I intend to see it through no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1016FAhaha... Doesn't sound like I've got much choice\x01",
            "but to go along with this, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_C4(0x1, 0x20000000)
    Sleep(300)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_20(0x3E8)
    OP_C4(0x0, 0x10)
    OP_23(0x1CC)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    Sleep(1000)
    Return()

    # Function_3_113 end

    def Function_4_C75(): pass

    label("Function_4_C75")

    FadeToDark(0, 0, -1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1D(0xC0)
    OP_AD(0x240137, 0x0, 0x0, 0x1F4)

    label("loc_C98")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1181")
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
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CF7"),
        (1, "loc_D21"),
        (2, "loc_113F"),
        (SWITCH_DEFAULT, "loc_117E"),
    )


    label("loc_CF7")

    OP_AE(0x1F4)
    Sleep(1000)
    Call(0, 5)
    OP_1D(0xC0)
    OP_AD(0x240137, 0x0, 0x0, 0x1F4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_117E")

    label("loc_D21")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05#0W―――――――――――――――――――――――――――\x01\x01",
            "Estelle and Lloyd will face off in a five-round duel of the century. Both\x01",
            "will take turns at fishing, and whoever has the most points at the end of\x01",
            "the five rounds will be declared the winner.\x01\x01",
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

    AnonymousTalk(    #16
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
    Jump("loc_117E")

    label("loc_113F")

    OP_AE(0x1F4)
    OP_5F(0x0)
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_1172")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_117B")

    label("loc_1172")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_117B")

    Jump("loc_117E")

    label("loc_117E")

    Jump("loc_C98")

    label("loc_1181")

    Return()

    # Function_4_C75 end

    def Function_5_1182(): pass

    label("Function_5_1182")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(-2710, -2000, 30940, 0)
    OP_67(0, 8970, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, -2960, -2000, 32500, 180)
    SetChrPos(0x10, -10780, -2000, 32560, 180)
    OP_48()
    OP_3E(0x24F, 1)
    OP_3E(0x250, 1)
    OP_3E(0x253, 1)
    OP_3E(0x3D4, 3)
    OP_3E(0x3D5, 3)
    OP_3E(0x3D7, 3)
    OP_22(0x1CC, 0x1, 0x64)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_C0(0x1B, 0x0, 0xFFFFF470, 0xFFFFF830, 0x7EF4, 0xB4, 0xFFFFF45C, 0xFFFFF448, 0x72C4)"), scpexpr(EXPR_END)), "loc_125F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1269")

    label("loc_125F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1269")

    EventBegin(0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x101, 2190, -2000, 42760, 180)
    SetChrPos(0x10, 2280, -2000, 41180, 0)
    OP_6D(2190, -1800, 41900, 0)
    OP_67(0, 8970, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(3000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_12EA"),
        (0, "loc_1482"),
        (SWITCH_DEFAULT, "loc_1485"),
    )


    label("loc_12EA")

    FadeToBright(1000, 0)
    OP_1E()
    Sleep(1000)

    ChrTalk(    #17
        0x101,
        "#1003FI-I lost...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        "Whew... I'm glad I got to retain my honor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        "I'll be able to sleep like a baby tonight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1009FI might not've lost anything, but I still feel\x01",
            "like crap for losing...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_20(0x7D0)
    OP_0D()
    OP_23(0x1CC)
    Sleep(1000)
    SetMessageWindowPos(-1, 80, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
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
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_144C"),
        (0, "loc_1473"),
        (SWITCH_DEFAULT, "loc_1482"),
    )


    label("loc_144C")

    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_1467")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_1470")

    label("loc_1467")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_1470")

    Jump("loc_1482")

    label("loc_1473")

    OP_D6(0x1)
    OP_D6(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    label("loc_1482")

    Jump("loc_1485")

    label("loc_1485")

    FadeToBright(1000, 0)
    OP_1E()
    OP_C4(0x0, 0x20000000)
    Sleep(1000)

    ChrTalk(    #22
        0x101,
        "#1018FWoohoo! I won!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        "So I lost...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "What a battle! You fought admirably, Estelle.\x01",
            "There's no shame in losing against someone\x01",
            "as talented as you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        "Here! I want you to have this.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10, 0x8D4, 0xFFFFF830, 0xA30C, 0x7D0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_0D()
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05Lloyd handed Estelle a silver-colored lure.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_8F(0x10, 0x8E8, 0xFFFFF830, 0xA0DC, 0x7D0, 0x0)
    Sleep(500)

    ChrTalk(    #27
        0x101,
        (
            "#1004FA-A lure made out of argem?\x02\x03",

            "I couldn't possibly take this... It looks so\x01",
            "expensive!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "No can do. Those're the rules. I challenged you\x01",
            "to a duel while putting this on the line, and I was\x01",
            "defeated.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "If you refuse to accept it, that will bring me even\x01",
            "greater shame than I already face! \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        "So please! Accept it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1008FW-Well, if you really insist...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToDark(2000, 0, -1)
    OP_23(0x1CC)
    OP_20(0xBB8)
    OP_21()
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #32
        "\x07\x05Thus Estelle accepted the silver lure from Lloyd.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #33
        (
            "\x07\x05And though feeling bliss thanks to her victory,\x01",
            "she was also blissfully unaware of what fate had\x01",
            "in store for her...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C4(0x1, 0x20000000)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D0")
    Sleep(3000)
    OP_28(0x1C, 0x4, 0x10)
    OP_28(0x1C, 0x4, 0x20)
    OP_28(0x1D, 0x4, 0x2)
    OP_3E(0x3A6, 20)
    OP_3E(0x3AA, 20)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #34
        "\x07\x05Received \x07\x02Fishing set\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(5000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #35
        "\x07\x05Received \x07\x025,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_18D0")

    Sleep(2000)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #36
        "\x18\x07\x05Continue to Chapter 2?\x02",
    )

    Sleep(1000)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        200,
        0,
        (
            "Continue\x01",        # 0
            "Leave Door\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1957"),
        (1, "loc_1966"),
        (SWITCH_DEFAULT, "loc_1988"),
    )


    label("loc_1957")

    OP_A2(0x2504)
    NewScene("ED6_DT21/C4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1988")

    label("loc_1966")

    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_197C")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_1985")

    label("loc_197C")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_1985")

    Jump("loc_1988")

    label("loc_1988")

    Return()

    # Function_5_1182 end

    def Function_6_1989(): pass

    label("Function_6_1989")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1993")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AE3")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 60, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "\x18\x07\x05Legendary Angler Estelle\x02",
    )

    OP_CC(0x0, 0x0, 0xFFFF, 0xA0, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1C, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_1A26")
    OP_CC(0x1, 0x0, "Leave the Door")
    OP_CC(0x1, 0x0, "Start from Beginning")
    OP_CC(0x1, 0x0, "Start from Chapter 2")

    label("loc_1A26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1D, 0x0, 0x20)"), scpexpr(EXPR_END)), "loc_1A4C")
    OP_CC(0x1, 0x0, "Start from Final Chapter")

    label("loc_1A4C")

    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_56(0x0)
    OP_5F(0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A7E"),
        (1, "loc_1AA5"),
        (2, "loc_1AB8"),
        (3, "loc_1ACC"),
        (SWITCH_DEFAULT, "loc_1AE0"),
    )


    label("loc_1A7E")

    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_1A99")
    NewScene("ED6_DT21/U4169   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_1AA2")

    label("loc_1A99")

    NewScene("ED6_DT21/U4121   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_1AA2")

    Jump("loc_1AE0")

    label("loc_1AA5")

    OP_20(0x3E8)
    OP_21()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1AE0")

    label("loc_1AB8")

    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/C4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1AE0")

    label("loc_1ACC")

    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1AE0")

    label("loc_1AE0")

    Jump("loc_1993")

    label("loc_1AE3")

    Return()

    # Function_6_1989 end

    SaveToFile()

Try(main)
