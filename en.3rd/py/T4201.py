from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4201   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4201.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Princess Klaudia',                     # 9
        'Sieg',                                 # 10
        'Tea',                                  # 11
        'Tea',                                  # 12
        'Tea Set',                              # 13
        'Cake',                                 # 14
        'Cake',                                 # 15
        'Secretary Lechter',                    # 16
        'Target Camera',                        # 17
    )

    DeclEntryPoint(
        Unknown_00              = -2780,
        Unknown_04              = 12000,
        Unknown_08              = 63200,
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
        'ED6_DT27/CH03960 ._CH',             # 00
        'ED6_DT07/CH02323 ._CH',             # 01
        'ED6_DT26/CH20774 ._CH',             # 02
        'ED6_DT06/CH20020 ._CH',             # 03
        'ED6_DT07/CH02093 ._CH',             # 04
        'ED6_DT07/CH02320 ._CH',             # 05
        'ED6_DT26/CH20254 ._CH',             # 06
        'ED6_DT26/CH20805 ._CH',             # 07
        'ED6_DT26/CH20806 ._CH',             # 08
        'ED6_DT26/CH20807 ._CH',             # 09
        'ED6_DT26/CH20773 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT27/CH03960P._CP',             # 00
        'ED6_DT07/CH02323P._CP',             # 01
        'ED6_DT26/CH20774P._CP',             # 02
        'ED6_DT06/CH20020P._CP',             # 03
        'ED6_DT07/CH02093P._CP',             # 04
        'ED6_DT07/CH02320P._CP',             # 05
        'ED6_DT26/CH20254P._CP',             # 06
        'ED6_DT26/CH20805P._CP',             # 07
        'ED6_DT26/CH20806P._CP',             # 08
        'ED6_DT26/CH20807P._CP',             # 09
        'ED6_DT26/CH20773P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638403,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1F6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1638403,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1F6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1703939,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1F6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1F6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1F6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_222",          # 00, 0
        "Function_1_292",          # 01, 1
        "Function_2_2B5",          # 02, 2
        "Function_3_2CB",          # 03, 3
        "Function_4_16ED",         # 04, 4
        "Function_5_17EF",         # 05, 5
        "Function_6_1945",         # 06, 6
        "Function_7_19DC",         # 07, 7
        "Function_8_2F10",         # 08, 8
        "Function_9_3B3D",         # 09, 9
    )


    def Function_0_222(): pass

    label("Function_0_222")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_24A")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_24A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_291")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_275")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_291")

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_291")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)

    label("loc_291")

    Return()

    # Function_0_222 end

    def Function_1_292(): pass

    label("Function_1_292")

    OP_B1("t4201_n")
    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_72(0x1002, 0x0)
    ExitThread()
    OP_6F(0x2, 0)
    Return()

    # Function_1_292 end

    def Function_2_2B5(): pass

    label("Function_2_2B5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2B5")

    label("loc_2CA")

    Return()

    # Function_2_2B5 end

    def Function_3_2CB(): pass

    label("Function_3_2CB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x0C\x18It was at that moment that I made a decision\x01",
            "in my heart:\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x0C\x18I would do all I could to support Her Highness,\x01",
            "this nation's future queen.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x0C\x18...But to that end, I also resolved to accept\x01",
            "whatever promotions I received.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "\x07\x0C\x18No doubt the further I moved up the ranks,\x01",
            "the more my chances to actually meet with\x01",
            "her would decrease...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x0C\x18...but even if we can't meet in person--even if\x01",
            "I have to do it from afar--I want to be able to\x01",
            "support her.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x0C\x18Perhaps this decision is a selfish one, but I do\x01",
            "hope you can forgive me for making it,\x01",
            "Your Highness.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_6D(13000, 14000, 78580, 0)
    OP_67(0, 6320, -10000, 0)
    OP_6B(3240, 0)
    OP_6C(90000, 0)
    OP_6E(280, 0)
    OP_1D(0x75)
    Sleep(2000)
    SetChrPos(0x10E, 14000, 14000, 78580, 270)

    def lambda_5A0():
        OP_8E(0xFE, 0x0, 0x36B0, 0x132E0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_5A0)

    def lambda_5BB():
        OP_6D(260, 14000, 78800, 6000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_5BB)

    def lambda_5D3():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_5D3)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x10E, 0x1)
    Sleep(500)
    OP_8C(0x10E, 0, 400)
    Sleep(500)

    NpcTalk(    #6
        0x10E,
        "Captain Schwarz",
        (
            "#176FI feel somewhat reluctant to disturb Her Majesty\x01",
            "while she's busy working, but...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_66F():
        OP_8E(0xFE, 0x0, 0x36B0, 0x138BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_66F)
    Sleep(500)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x10, 0, 16000, 92000, 180)
    SetChrPos(0x11, -4180, 18400, 86040, 180)

    NpcTalk(    #7
        0x10,
        "Girl's Voice",
        "#100P...Is that you, Julia?\x02",
    )

    CloseMessageWindow()

    def lambda_6E9():
        OP_8E(0xFE, 0x0, 0x3E80, 0x15B44, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6E9)
    WaitChrThread(0x10E, 0x1)
    OP_62(0x10E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_720():
        OP_6D(720, 15500, 86740, 2000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_720)

    def lambda_738():
        OP_6C(34000, 2000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_738)

    def lambda_748():
        OP_67(0, 3980, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_748)

    def lambda_760():
        OP_6B(3240, 2000)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_760)
    WaitChrThread(0x18, 0x0)
    Sleep(500)

    ChrTalk(    #8
        0x11,
        "#311F#6PScree! ☆\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x10, 0x1)

    NpcTalk(    #9
        0x10E,
        "Captain Schwarz",
        (
            "#173FY-Your Highness?! Sieg?!\x02\x03",

            "H-How come you're back here already?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_80C():
        OP_8E(0xFE, 0x0, 0x36B0, 0x14410, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_80C)

    def lambda_827():
        OP_6D(2250, 14000, 83190, 3000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_827)

    def lambda_83F():
        OP_6C(53000, 3000)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_83F)

    def lambda_84F():
        OP_67(0, 4019, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_84F)
    WaitChrThread(0x18, 0x1)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #10
        0x10,
        (
            "#1872F#5POh, did you think I was still over at the villa?\x02\x03",

            "#1815FHeehee. I expected to be, too, but there weren't\x01",
            "many people there today, so I was able to leave\x01",
            "earlier than expected.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x10E,
        "Captain Schwarz",
        "#170F#12PAhh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#1814F#5PI'm just as surprised to see you here, actually.\x01",
            "I thought you'd been given a day off today?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x10E,
        "Captain Schwarz",
        (
            "#173F#12PO-Oh, you knew?\x02\x03",

            "#179FHaha. Indeed, I had.\x02\x03",

            "#171FI ended up running into a friend I don't have\x01",
            "many opportunities to spend time with...\x02\x03",

            "The time we spent together simply flew by.\x02\x03",

            "I owe my deepest thanks to Her Majesty for\x01",
            "giving me the opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        "#1818F#5PI'm happy to hear that.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #15
        0x10,
        (
            "#1873F#5PUmm... Julia?\x02\x03",

            "#1872FI realize this may feel a little out of nowhere,\x01",
            "but I wanted to thank you for always supporting\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #16
        0x10E,
        "Captain Schwarz",
        "#173F#12PGoodness... That IS out of nowhere.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#1819F#5PBut it's something I should have done ages ago.\x01",
            "I can't believe it's taken me this long to state\x01",
            "the obvious. \x02\x03",

            "Everything my parents would otherwise have\x01",
            "taught me, you ended up doing in their place.\x02\x03",

            "#1873FHow to fight, how to act, how to think... It's like I'm\x01",
            "only now starting to realize just how much of what\x01",
            "makes me myself are things I learned from you.\x02\x03",

            "#1818FI feel like I've grown up always seeing you as a role\x01",
            "model.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)

    ChrTalk(    #18
        0x10,
        (
            "#1815F#5PI remember Grandmother laughing at me at one\x01",
            "point about how similar I am to you, too.\x02\x03",

            "Even in the little things, like how I walk and move,\x01",
            "she says I'm just like you.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #19
        0x10E,
        "Captain Schwarz",
        "#173F#12P#40W...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_62(0x10, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #20
        0x10,
        (
            "#1814F#5PJulia?\x02\x03",

            "Is something the matter?\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10E)
    Sleep(500)

    NpcTalk(    #21
        0x10E,
        "Captain Schwarz",
        (
            "#179F#12PNo...\x02\x03",

            "(All this time, I really have been right by\x01",
            "her side...)\x02\x03",

            "(I've spent all this time worrying because \x01",
            "I couldn't see her by mine, but as far as\x01",
            "she was concerned, I was always there.)\x02\x03",

            "#175F(I truly am beyond help...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        "#1813F#5PErm...?\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_103D():
        OP_6D(2250, 14000, 83890, 1500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_103D)

    def lambda_1055():
        OP_6B(3140, 1500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1055)

    def lambda_1065():
        OP_8E(0xFE, 0x0, 0x36B0, 0x13C54, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1065)
    WaitChrThread(0x18, 0x0)
    WaitChrThread(0x10E, 0x1)
    Sleep(500)

    NpcTalk(    #23
        0x10E,
        "Captain Schwarz",
        (
            "#176F#12P...Kloe, may I say something?\x02\x03",

            "#178FI don't believe I'll be able to wait upon you as\x01",
            "I always have any longer.\x02\x03",

            "But even now, I wish to do all I can to protect\x01",
            "and support you.\x02\x03",

            "#179FI wish to continue being your retainer, your\x01",
            "friend...and your sister as well.\x02\x03",

            "#170FSo...please try not to overexert yourself during\x01",
            "my absence.\x02\x03",

            "And even if I'm not able to be near you all the\x01",
            "time, I still want you to know that you can\x01",
            "always call upon me if you need me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#1814F#5PYeah...\x02\x03",

            "#1873FHeehee. Of course I will.\x02\x03",

            "Although, I can't promise I won't find\x01",
            "myself unintentionally taking advantage\x01",
            "of your kindness when I do.\x02\x03",

            "#1818FI'm always happy to have you to depend\x01",
            "on.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #25
        0x10E,
        "Captain Schwarz",
        "#171F#12PAnd I'll always be glad you feel that way.\x02",
    )

    CloseMessageWindow()

    def lambda_1395():
        OP_6B(3040, 3000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_1395)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_44(0x18, 0xFF)
    OP_6D(10240, 18000, 100140, 0)
    OP_67(0, 5360, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(55000, 0)
    OP_6E(280, 0)
    SetChrPos(0x11, 9680, 18640, 99540, 270)
    SetChrFlags(0x10E, 0x4)
    SetChrPos(0x10E, 9680, 18000, 102240, 225)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, -7540, 18000, 101460, 90)
    OP_43(0x10E, 0x3, 0x0, 0x5)
    OP_43(0x10, 0x3, 0x0, 0x4)

    def lambda_1441():
        OP_6B(3600, 30000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_1441)
    FadeToBright(2000, 0)
    WaitChrThread(0x10E, 0x3)
    OP_43(0x10E, 0x0, 0x0, 0x6)
    Sleep(2000)
    Sleep(300)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #26
        (
            "\x07\x00#40WThat afternoon, they were able to enjoy a few\x01",
            "relaxing cups of tea together.\x02\x03",

            "Despite her initial resistance, Julia's day off proved\x01",
            "to be much more enjoyable than she had expected...\x02\x03",

            "...and it seemed inevitable that the fragrance of\x01",
            "the tea that she drank that day would remain in\x01",
            "her memories forever.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_C4(0x1, 0x20000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_F7(0x9, 0x1, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #27
        "\x07\x00Side Story [Julia's Day Off] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_E6(0x1, 0x0)
    Call(6, 25)
    OP_C2(0x1, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xD, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16CD")
    Sleep(1000)
    OP_28(0xD, 0x4, 0x10)
    OP_28(0xD, 0x4, 0x20)
    OP_3E(0x2D5, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #28
        "\x07\x05Received \x1F\xD5\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    AddMira(3000)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #29
        "\x07\x05Received \x07\x023,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_16CD")

    OP_A2(0x2505)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 7)), scpexpr(EXPR_END)), "loc_16E3")
    NewScene("ED6_DT21/U4203   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_16EC")

    label("loc_16E3")

    NewScene("ED6_DT21/U4200   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_16EC")

    Return()

    # Function_3_2CB end

    def Function_4_16ED(): pass

    label("Function_4_16ED")


    def lambda_16F3():
        OP_8E(0xFE, 0x1B1C, 0x4650, 0x18C54, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_16F3)
    WaitChrThread(0x10, 0x1)

    def lambda_1713():
        OP_8E(0xFE, 0x1B1C, 0x4650, 0x18434, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1713)
    WaitChrThread(0x10, 0x1)

    def lambda_1733():
        OP_8E(0xFE, 0x1CD4, 0x4650, 0x18434, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1733)
    WaitChrThread(0x10, 0x1)
    Sleep(500)
    Fade(250)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 8460, 18560, 99880, 0)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, 9100, 18560, 98940, 0)
    Sleep(500)

    def lambda_178E():
        OP_8E(0xFE, 0x1CD4, 0x4650, 0x188D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_178E)
    WaitChrThread(0x10, 0x1)

    def lambda_17AE():
        OP_8E(0xFE, 0x1F54, 0x4650, 0x188D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_17AE)
    WaitChrThread(0x10, 0x1)
    Fade(250)
    SetChrPos(0x10, 8600, 18400, 100600, 180)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 2)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Return()

    # Function_4_16ED end

    def Function_5_17EF(): pass

    label("Function_5_17EF")


    def lambda_17F5():
        OP_8E(0xFE, 0x25D0, 0x4650, 0x18A24, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_17F5)
    WaitChrThread(0x10E, 0x1)
    OP_8C(0x10E, 225, 400)
    Sleep(500)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 9140, 18520, 100160, 0)
    Sleep(500)
    OP_8C(0x10E, 90, 400)

    def lambda_1843():
        OP_8E(0xFE, 0x29B8, 0x4650, 0x18A24, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1843)
    WaitChrThread(0x10E, 0x1)

    def lambda_1863():
        OP_8E(0xFE, 0x29B8, 0x4650, 0x17AE8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1863)
    WaitChrThread(0x10E, 0x1)

    def lambda_1883():
        OP_8E(0xFE, 0x1E00, 0x4650, 0x17AE8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1883)
    WaitChrThread(0x10E, 0x1)

    def lambda_18A3():
        OP_8E(0xFE, 0x1E00, 0x4650, 0x17F5C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_18A3)
    WaitChrThread(0x10E, 0x1)
    OP_8C(0x10E, 45, 400)
    Sleep(500)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 8500, 18520, 98950, 0)
    Sleep(500)

    def lambda_18EA():

        label("loc_18EA")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_18EA")

    QueueWorkItem2(0x10E, 2, lambda_18EA)
    WaitChrThread(0x10, 0x3)
    OP_44(0x10E, 0x2)

    def lambda_1904():
        OP_8E(0xFE, 0x1F54, 0x4650, 0x17E1C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10E, 1, lambda_1904)
    WaitChrThread(0x10E, 0x1)
    Fade(250)
    SetChrPos(0x10E, 9000, 18140, 98220, 0)
    SetChrChipByIndex(0x10E, 4)
    SetChrSubChip(0x10E, 0)
    OP_0D()
    Sleep(300)
    Return()

    # Function_5_17EF end

    def Function_6_1945(): pass

    label("Function_6_1945")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_19DB")
    OP_62(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(500)
    OP_62(0x10E, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    OP_62(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(700)
    OP_62(0x10E, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)
    OP_62(0x10, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(400)
    OP_62(0x10E, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1600)
    Jump("Function_6_1945")

    label("loc_19DB")

    Return()

    # Function_6_1945 end

    def Function_7_19DC(): pass

    label("Function_7_19DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(45500, 16000, 80800, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_6D(27160, 16000, 77540, 0)
    OP_67(0, 8350, -10000, 0)
    OP_6B(3520, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 42720, 16000, 80320, 90)

    def lambda_1A92():
        OP_6D(44170, 16000, 81200, 5000)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1A92)

    def lambda_1AAA():
        OP_67(0, 7500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1AAA)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x17, 0x1)
    Fade(500)
    OP_6D(44170, 16000, 81200, 0)
    OP_67(0, 7000, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #30
        0x17,
        "#1885F#6P...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    OP_51(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x11, 59550, 16000, 80000, 270)
    SetChrChipByIndex(0x11, 5)
    SetChrSubChip(0x11, 0)
    OP_22(0x197, 0x0, 0x64)
    Sleep(500)
    OP_62(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1B7C():
        OP_6D(49750, 16000, 81310, 1500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1B7C)

    def lambda_1B94():
        OP_67(0, 6800, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1B94)
    Sleep(1000)
    OP_22(0x8C, 0x0, 0x64)
    ClearChrFlags(0x11, 0x1)
    OP_43(0x11, 0x0, 0x0, 0x2)

    def lambda_1BC2():
        OP_8E(0xFE, 0xAB54, 0x445C, 0x130B0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1BC2)
    Sleep(1000)

    def lambda_1BE2():
        OP_6D(44170, 16000, 81200, 2500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1BE2)

    def lambda_1BFA():
        OP_67(0, 7000, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_1BFA)
    WaitChrThread(0x11, 0x1)
    OP_97(0x11, 0xAB54, 0x137B8, 0x57E40, 0x1B58, 0x1)
    OP_97(0x11, 0xAB54, 0x137B8, 0x41EB0, 0x1388, 0x1)
    SetChrChipByIndex(0x11, 6)
    SetChrSubChip(0x11, 0)
    OP_8C(0x11, 270, 400)
    OP_8F(0x11, 0xAAF0, 0x3E80, 0x13880, 0x7D0, 0x0)
    Fade(500)
    SetChrFlags(0x11, 0x1)
    OP_44(0x11, 0x0)
    SetChrPos(0x11, 43860, 16480, 80000, 270)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #31
        0x11,
        "#311F#11PScree!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x17,
        (
            "#1881F#6PHey-hey, buddy.\x02\x03",

            "#1887FYou haven't changed a bit, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x11,
        (
            "#310F#11PScree scree scree.\x02\x03",

            "Screeeee. Scree scree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x17,
        (
            "#1886F#6PReally? Sounds like a ton's happened, huh?\x02\x03",

            "#1885FBut it's nice to see you and your master are\x01",
            "doing all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x11,
        "#311F#11PScree. ♪\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 29720, 14000, 69740, 45)

    NpcTalk(    #36
        0x10,
        "Girl's Voice",
        "#2P...Lechter?\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x17, 270, 400)

    def lambda_1E18():

        label("loc_1E18")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_1E18")

    QueueWorkItem2(0x17, 2, lambda_1E18)
    Fade(500)
    OP_6D(34340, 16000, 74200, 0)
    OP_67(0, 6140, -10000, 0)
    OP_6B(2840, 0)
    OP_6C(0, 0)
    OP_6E(280, 0)

    def lambda_1E6B():
        OP_8E(0xFE, 0x87A0, 0x3E80, 0x123F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1E6B)

    def lambda_1E86():
        OP_6D(41740, 16000, 80750, 6500)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_1E86)
    WaitChrThread(0x10, 0x1)

    def lambda_1EA3():
        OP_8E(0xFE, 0xA082, 0x3E80, 0x13420, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1EA3)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #37
        0x17,
        (
            "#1885F#11PWell, well. Good day to you, Your Highness.\x02\x03",

            "#1880FI pray I'm not causing any trouble by taking a\x01",
            "tour of the castle like this.\x02\x03",

            "#1881FThe view from this terrace certainly is beautiful,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        (
            "#1819F#6PWhat happened to you, Lechter?\x02\x03",

            "#1813FHow did you end up working for\x01",
            "Chancellor Osborne?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #39
        0x17,
        (
            "#1886F#11PHmm? I'm sorry. I haven't the faintest idea\x01",
            "what you mean.\x02\x03",

            "#1880FAre you perchance mistaking me for someone\x01",
            "else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x10,
        (
            "#1817F#6PYour name is Lechter Arundel.\x02\x03",

            "You were the Student Council president at Jenis\x01",
            "Royal Academy, which you attended before leaving\x01",
            "suddenly two years ago.\x02\x03",

            "#1812FSo no. I am not mistaking you for someone else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x17,
        (
            "#1884F#11PAh, but that's where you're wrong! Because my\x01",
            "name is actually Lech Terarundel.\x02\x03",

            "#1882FI can certainly see how our names could become\x01",
            "mixed up, however. They ARE scarily close.\x02\x03",

            "#1881FStill, now you know. Please, just call me Lech.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #42
        0x10,
        "#1812F#6PDon't try and joke around with me, Lechter!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #43
        0x10,
        (
            "#1816F#6PDo you have any idea how worried all of us were\x01",
            "when you just disappeared without a word?!\x02\x03",

            "You submitted your notice to leave the academy\x01",
            "and then were never seen again!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x17,
        "#1882F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#1813F#6PEven the otherwise calm Leo let out a cry of\x01",
            "anger when he found out!\x02\x03",

            "And all Lucy could do was give a sad smile and\x01",
            "say, 'This is just like him,' the whole time with\x01",
            "tears in her eyes!\x02\x03",

            "#1819FJill and Hans were heartbroken. And so was I!\x02\x03",

            "Yet after all that...\x02\x03",

            "#1816FAfter all this time, you finally show yourself,\x01",
            "knowing full well that I'm here, and THIS is how\x01",
            "you act? By pretending you're someone else?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x17,
        "#1885F#11P...Haha...\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #47
        0x17,
        "#1881F#4S#11PHahahahaha!#2S\x02",
    )

    OP_7C(0x32, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        "#1812F#6PLECHTER!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x17,
        (
            "#1885F#11PSorry, sorry. No need for the scary glare.\x02\x03",

            "#1887FYou're still taking things way too seriously.\x02\x03",

            "Looks like it'll take more than stepping up as\x01",
            "crown princess to change that part of you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #50
        0x10,
        "#1872F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x17,
        (
            "#1885F#11PBut you know? Seeing you makes me feel kinda\x01",
            "relieved.\x02\x03",

            "#1887FI always figured if someone like you became\x01",
            "crown princess, you'd have virtually no freedom\x01",
            "to do anything other than work.\x02\x03",

            "But from all that's reached my ears, it sounds\x01",
            "like you're actually doing all right for yourself.\x02\x03",

            "#1881FAnd you even made some great new friends\x01",
            "after I left the academy, didn't you? Nice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10,
        (
            "#1872F#6PHeehee...\x02\x03",

            "#1815FI sure did.\x02\x03",

            "#1819FNonetheless, it's thanks to you that I was able to\x01",
            "change at all. You were the one who gave me the\x01",
            "first push in the right direction.\x02\x03",

            "I never got the chance to thank you properly after\x01",
            "you left...\x02\x03",

            "#1818F...but all this time, I've always been grateful to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x17,
        (
            "#1885F#11PWell, consider me honored.\x02\x03",

            "#1887FDo I get a kiss in return?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        (
            "#1815F#6PYou do not.\x02\x03",

            "#1818FI may feel respect towards you, but nothing\x01",
            "romantic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x17,
        (
            "#1886F#11PAww. That's a bummer.\x02\x03",

            "#1885FThere was me, all taken in by how pretty you'd\x01",
            "become, wondering if this could be the start of\x01",
            "something downright magical...\x02\x03",

            "#1887F...and what happens instead? My dreams of\x01",
            "romance and sweet smooches are crushed to\x01",
            "nothing before they can even begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x10,
        (
            "#1815F#6PHeehee. I know you don't mean a word of that,\x01",
            "you know.\x02\x03",

            "#1872FYou're looking very sharp yourself, though.\x01",
            "It's surprising to see.\x02\x03",

            "Every time I've seen you before today, it was\x01",
            "in that heavily-frayed uniform worn in the most\x01",
            "sloppy way imaginable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x17,
        (
            "#1884F#11PI think you'll find I was merely making a fashion \x01",
            "statement!\x02\x03",

            "#1882FThat wasn't laziness or slobbishness! Every part of\x01",
            "it was carefully calculated and considered to have\x01",
            "maximum effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        (
            "#1819F#6P...The scary thing is, I actually believe you.\x02\x03",

            "You always seemed as if you cared for nothing but\x01",
            "having fun and causing trouble, yet when it came\x01",
            "down to it, you were wise beyond your years.\x02\x03",

            "#1817FAnd I've finally seen part of the reason behind that\x01",
            "today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x17,
        "#1882F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "#1819F#6PI'll ask you again, Lechter...\x02\x03",

            "#1813FHow did you end up working for\x01",
            "Chancellor Osborne like this?\x02\x03",

            "Just what happened to you between\x01",
            "you submitting your notice to leave\x01",
            "the academy and now?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2EEE():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2EEE)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4221   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_19DC end

    def Function_8_2F10(): pass

    label("Function_8_2F10")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(41740, 16000, 80750, 0)
    OP_67(0, 6140, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(0, 0)
    OP_6E(280, 0)
    OP_43(0x11, 0x3, 0x0, 0x9)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 42720, 16000, 80320, 225)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 43860, 16480, 80000, 270)
    SetChrChipByIndex(0x11, 1)
    SetChrSubChip(0x11, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 41090, 16000, 78880, 45)

    def lambda_2FC6():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_2FC6)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #61
        0x17,
        (
            "#1883F#11POopsie. I think it's probably about time\x01",
            "for the airship to arrive.\x02\x03",

            "#1885FI'm gonna have to stop you there and get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        "#1814F#6PWha...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 135, 400)
    Sleep(300)

    ChrTalk(    #63
        0x17,
        (
            "#1881F#5PSee ya, Sieg.\x02\x03",

            "#1887FNext time I see you, I'll bring you some Erebonian\x01",
            "salami as a souvenir, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x11,
        "#311F#11PScree. ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#1813F#6PW-Wait!\x02\x03",

            "Are you planning to just disappear without\x01",
            "telling me anything a second time?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x17)
    Sleep(500)
    OP_44(0x11, 0x3)

    ChrTalk(    #66
        0x17,
        (
            "#1885F#5POh. Got an important question for you.\x02\x03",

            "Did you fall in love with someone while\x01",
            "I was away?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x10,
        "#1814F#6PU-Uh...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x17, 225, 400)
    Sleep(300)

    ChrTalk(    #68
        0x17,
        (
            "#1887F#11PHit the nail on the head, huh?\x02\x03",

            "#1881FAww! That's so cute! First love, right?\x02\x03",

            "How's that feel? Heart all aflutter one minute,\x01",
            "end of the world the next?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        (
            "#1812F#6PDon't you dare start teasing me!\x02\x03",

            "#1870F...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #70
        0x10,
        (
            "#1815F#6PBut you're right, though. I did.\x02\x03",

            "#1872FHe rejected me in this very spot not that\x01",
            "long ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #71
        0x17,
        (
            "#1883F#11PWait. You're joking, right?\x02\x03",

            "There's a coincidence I DIDN'T see coming!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10,
        (
            "#1873F#6PHeehee. I'm not so sure about that.\x02\x03",

            "#1818FIt feels like you know everything sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x17,
        (
            "#1885F#11PHeh. I'm not some kind of all-knowing, all-seeing\x01",
            "divinity.\x02\x03",

            "#1887FThat's what makes the world so interesting to me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3516():
        OP_6D(41200, 16000, 80200, 1200)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3516)

    def lambda_352E():
        OP_8E(0xFE, 0xA280, 0x3E80, 0x135C4, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_352E)
    Sleep(500)
    OP_8C(0x11, 225, 400)
    WaitChrThread(0x17, 0x1)
    Sleep(500)
    Fade(1000)

    def lambda_3564():
        OP_6B(2700, 500)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3564)
    OP_22(0x8F, 0x0, 0x64)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 0)
    SetChrFlags(0x17, 0x8)
    ClearChrFlags(0x17, 0x1)
    OP_0D()
    Sleep(300)
    OP_99(0x10, 0x0, 0x6, 0x3E8)
    OP_99(0x10, 0x3, 0x6, 0x3E8)
    Sleep(500)

    ChrTalk(    #74
        0x10,
        "#1814F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x17,
        (
            "#1885F#11P...I'm happy for you, Kloe.\x02\x03",

            "Knowing the pain of lost love's what makes a girl\x01",
            "blossom, in my humble opinion.\x02\x03",

            "#1887FDo you feel like the whole experience let you get\x01",
            "a step closer to the person you want to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        (
            "#1870F#6P...Well...\x02\x03",

            "#1873F...\x02\x03",

            "#1819FWhat about you?\x02\x03",

            "Do you feel you're getting closer to becoming\x01",
            "the person that you want to be?\x02\x03",

            "By being at the chancellor's side?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x17,
        "#1882F#11P...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    ClearChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x17, 0x8)
    SetChrFlags(0x17, 0x1)
    OP_0D()

    def lambda_378A():
        OP_6D(41300, 16000, 80300, 1000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_378A)

    def lambda_37A2():
        OP_8F(0xFE, 0xA438, 0x3E80, 0x13718, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_37A2)
    WaitChrThread(0x17, 0x1)
    Sleep(500)

    ChrTalk(    #78
        0x17,
        (
            "#1885F#11PKinda hard to do that when I don't have\x01",
            "a 'person I want to be' to begin with.\x02\x03",

            "I'm just stickin' with him because it feels\x01",
            "like it'll be fun. That's all.\x02\x03",

            "#1882FI've been doing it since before I joined the\x01",
            "academy, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        "#1814F#6P...You have?\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_38D7():

        label("loc_38D7")

        TurnDirection(0xFE, 0x17, 500)
        OP_48()
        Jump("loc_38D7")

    QueueWorkItem2(0x10, 2, lambda_38D7)

    def lambda_38E8():
        OP_8E(0xFE, 0x9D94, 0x3E80, 0x13718, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_38E8)
    WaitChrThread(0x17, 0x1)

    def lambda_3908():
        OP_6D(40700, 16000, 79700, 1300)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3908)

    def lambda_3920():
        OP_8E(0xFE, 0x98E4, 0x3E80, 0x13268, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3920)
    WaitChrThread(0x17, 0x1)
    Sleep(500)

    ChrTalk(    #80
        0x17,
        (
            "#1886F#5PThat prince is proving surprisingly capable,\x01",
            "but he still isn't a match for the chancellor.\x02\x03",

            "#1885FTell him to watch his back, all right?\x02\x03",

            "#1887FSo that he doesn't get swallowed up by that\x01",
            "monster after he gets tired of dancing.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(200)
    SetChrFlags(0x17, 0x20)
    SetChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 9)
    SetChrSubChip(0x17, 0)
    Sleep(200)
    SetChrSubChip(0x17, 1)
    Sleep(200)
    SetChrSubChip(0x17, 2)
    Sleep(400)

    def lambda_3A6B():
        OP_6D(37700, 16000, 76700, 3000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3A6B)

    def lambda_3A83():

        label("loc_3A83")

        OP_99(0xFE, 0x2, 0x9, 0x5DC)
        OP_48()
        Jump("loc_3A83")

    QueueWorkItem2(0x17, 2, lambda_3A83)

    def lambda_3A96():
        OP_8F(0xFE, 0x7814, 0x36B0, 0x11346, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3A96)
    WaitChrThread(0x18, 0x0)
    Sleep(2000)

    def lambda_3ABB():
        OP_6D(40000, 16000, 79000, 2000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3ABB)
    WaitChrThread(0x18, 0x0)
    OP_44(0x10, 0x2)
    Sleep(500)

    ChrTalk(    #81
        0x10,
        "#1813F#11P#40W...Goodbye, Lechter...\x02",
    )

    CloseMessageWindow()

    def lambda_3B0B():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_3B0B)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4105   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2F10 end

    def Function_9_3B3D(): pass

    label("Function_9_3B3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3B53")
    OP_22(0xB5, 0x0, 0x64)
    Sleep(2500)
    Jump("Function_9_3B3D")

    label("loc_3B53")

    Return()

    # Function_9_3B3D end

    SaveToFile()

Try(main)
