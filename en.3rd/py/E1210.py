from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E1210   ._SN',
        MapName             = 'event',
        Location            = 'E1210.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
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
        'Squire Marcia',                        # 9
        'Squire Cesar',                         # 10
        'Commander Selnate',                    # 11
        'Squire',                               # 12
        'Squire',                               # 13
        'Squire',                               # 14
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT26/CH20610 ._CH',             # 00
        'ED6_DT26/CH20744 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT26/CH20610P._CP',             # 00
        'ED6_DT26/CH20744P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_17A",          # 00, 0
        "Function_1_19A",          # 01, 1
        "Function_2_1D8",          # 02, 2
        "Function_3_1DE3",         # 03, 3
        "Function_4_1E3C",         # 04, 4
        "Function_5_32E0",         # 05, 5
        "Function_6_332D",         # 06, 6
    )


    def Function_0_17A(): pass

    label("Function_0_17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_18B")
    OP_A3(0x2505)
    Event(0, 4)
    Jump("loc_199")

    label("loc_18B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_199")
    OP_A3(0x2504)
    Event(0, 2)

    label("loc_199")

    Return()

    # Function_0_17A end

    def Function_1_19A(): pass

    label("Function_1_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B3")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B3")

    OP_22(0x7A, 0x1, 0x46)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B0, 2)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D7")
    OP_23(0x1C3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_23(0x7A)

    label("loc_1D7")

    Return()

    # Function_1_19A end

    def Function_2_1D8(): pass

    label("Function_2_1D8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -160, 200, 6650, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -3150, 200, 6970, 315)
    SetChrPos(0x109, -210, 1500, -4500, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(4150, 0, 6650, 0)
    OP_67(0, 4870, -10000, 0)
    OP_6B(3140, 0)
    OP_6C(45000, 0)
    OP_6E(305, 0)

    def lambda_26F():

        label("loc_26F")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_26F")

    QueueWorkItem2(0x109, 3, lambda_26F)
    OP_76(0xFF, 0x7, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)
    OP_43(0x109, 0x0, 0x0, 0x3)
    Sleep(500)

    def lambda_2C1():
        OP_6D(-30, 1500, 5630, 3500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2C1)

    def lambda_2D9():
        OP_67(0, 6180, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2D9)

    def lambda_2F1():
        OP_6B(2600, 3500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2F1)

    def lambda_301():
        OP_6E(325, 3500)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_301)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10, 0x0)
    SetChrSubChip(0x11, 1)
    Sleep(100)
    SetChrSubChip(0x10, 1)
    Sleep(150)

    ChrTalk(    #0
        0x11,
        (
            "#5P#100PCongratulations on completing your operation,\x01",
            "sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "#5P#100PMy thoughts exactly.\x02\x03",

            "That seemed to be a rather easy one for you\x01",
            "in the end, too.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x109,
        "Father Kevin",
        (
            "#1075FCompared to what they're usually like, it was.\x02\x03",

            "#1066FIf I'd had a bit more time, I could've enjoyed some\x01",
            "private time with a real gem of a woman, too...but\x01",
            "I'll have to settle for crying myself to sleep tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x11,
        "#5P#100PNot this again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#5P#100PUnless you want another earful from the\x01",
            "commander, you might want to start taking\x01",
            "your work more seriously.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #5
        0x109,
        "Father Kevin",
        (
            "#1060FI know, I know. Lighten up a little, yeah?\x02\x03",

            "I swear, I'll never get how you hardheaded\x01",
            "types ended up assigned to a slacker like me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x11,
        (
            "#5P#100P*sigh* This may come as a shock, but you ARE\x01",
            "a Dominion, you know. We can't very well have\x01",
            "you acting alone without any form of backup.\x02\x03",

            "As long as you're here and this ship is under\x01",
            "your command, then slacker or not, we're here,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "#5P#100PEven then, you've got a lot less squires in your\x01",
            "service than you should have.\x02\x03",

            "Maybe you should take this chance to gather\x01",
            "up a few more?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #8
        0x109,
        "Father Kevin",
        (
            "#1068FI think I'm gonna have to pass.\x02\x03",

            "#1066FThat'll just make it even harder\x01",
            "for me to work on my own.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        "#5P#100P*sigh* I thought you'd say that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x11,
        (
            "#5P#100PWe'd prefer it if you would actually trust us\x01",
            "to help you a little more, sir...\x02\x03",

            "I mean, all we could do in that Salt Pale\x01",
            "operation was transport the thing.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x109,
        "Father Kevin",
        (
            "#1065FYou say that as if transporting it isn't\x01",
            "a huge responsibility in itself.\x02\x03",

            "#1072F(After all, the last thing we wanted was\x01",
            "him catching wind of it and becoming\x01",
            "wary of us.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x11,
        "#5P#100P...Is something wrong?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #13
        0x109,
        "Father Kevin",
        (
            "#1075FOh, not a thing.\x02\x03",

            "#1060FAnyway, as per the original plan, we need\x01",
            "to get ourselves back to Arteria a.s.a.p.\x02\x03",

            "We should be able to reach there by noon \x01",
            "tomorrow...or today now, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        "#5PGot it.\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "map\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -4400, 1150, 6600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0x11, 0)
    Sleep(50)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    SetChrSubChip(0x10, 0)
    Sleep(1000)

    NpcTalk(    #15
        0x109,
        "Father Kevin",
        "#1063FWhere's it from?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "#5PArteria, apparently.\x02\x03",

            "It's a call from Commander Selnate.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #17
        0x109,
        "Father Kevin",
        (
            "#1064FOh, you are KIDDING me...\x02\x03",

            "#1068F(Getting a call from her right after a mission\x01",
            "is always a bad, bad sign...)\x02\x03",

            "#1060FLet's get this over with. Put her through.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 1)
    Sleep(150)

    ChrTalk(    #18
        0x11,
        "#5P#100PAll right.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 0)
    Sleep(150)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)

    def lambda_CB5():
        OP_6D(1250, 2000, 3510, 3000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_CB5)

    def lambda_CCD():
        OP_67(0, 5340, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_CCD)

    def lambda_CE5():
        OP_6B(3140, 3000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_CE5)

    def lambda_CF5():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_CF5)

    def lambda_D05():
        OP_6E(262, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_D05)
    OP_B0(0x0, 0xA)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x1E)
    Sleep(300)
    OP_22(0x127, 0x0, 0x64)

    def lambda_D31():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D31)
    OP_73(0x0)
    WaitChrThread(0x11, 0x0)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0x0, 0x6, 0x1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("Commander Selnate")

    AnonymousTalk(    #19
        (
            "\x07\x05Evening, Kevin. It sounds like you did well.\x02\x03",

            "Fill me in on the details.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    NpcTalk(    #20
        0x109,
        "Father Kevin",
        (
            "#1060F#6P#100PIt basically went without issue.\x02\x03",

            "The artifact was the Fool's Locket.\x02\x03",

            "There were signs of society involvement,\x01",
            "but it looks like they've cut any ties with\x01",
            "him a long time ago.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("Commander Selnate")

    AnonymousTalk(    #21
        (
            "\x07\x05I see... As I thought, then.\x02\x03",

            "Good work all around. I'd say you deserve a\x01",
            "well-earned rest...but unfortunately, I can't\x01",
            "grant you one right now.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    NpcTalk(    #22
        0x109,
        "Father Kevin",
        "#1068F#6P#100P(Aaaaaand here we go...)\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("Commander Selnate")

    AnonymousTalk(    #23
        "\x07\x05Hmm? Is something the matter?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    NpcTalk(    #24
        0x109,
        "Father Kevin",
        "#1061F#6P#100POh, I'm just dandy. Please continue.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("Commander Selnate")

    AnonymousTalk(    #25
        (
            "\x07\x05Well, then. As much as I hate to spring this on\x01",
            "you immediately after finishing one mission...\x02\x03",

            "...I've got something I'd like you to do for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    NpcTalk(    #26
        0x109,
        "Father Kevin",
        (
            "#1065F#6P#100PHmm...\x02\x03",

            "#1063FRegarding a heretic, I assume?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("Commander Selnate")

    AnonymousTalk(    #27
        (
            "\x07\x05Not this time. All I want you to do is pick\x01",
            "something up.\x02\x03",

            "The object in question is currently being\x01",
            "held underneath Grancel Cathedral.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #28
        0x109,
        "Father Kevin",
        (
            "#1063F#6P#100PGrancel?!\x02\x03",

            "Do you think this object may be somehow\x01",
            "related to the Aureole?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("Commander Selnate")

    AnonymousTalk(    #29
        (
            "\x07\x05It's a distinct possibility.\x02\x03",

            "Can I count on you to handle this?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    NpcTalk(    #30
        0x109,
        "Father Kevin",
        (
            "#1065F#6P#100P...All right.\x02\x03",

            "#1060FThat said, we've already got one artifact on this\x01",
            "ship that needs transporting back, so I'll let the\x01",
            "crew here take that to Arteria.\x02\x03",

            "I'll handle going to Liberl on my own.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("Commander Selnate")

    AnonymousTalk(    #31
        (
            "\x07\x05That's fine with me.\x02\x03",

            "Oh, incidentally...you won't actually be alone.\x01",
            "I've dispatched a rookie squire to aid you.\x02\x03",

            "They'll be serving you from now on, so do play\x01",
            "nice, won't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(300)

    NpcTalk(    #32
        0x109,
        "Father Kevin",
        (
            "#1064F#6P#100PW-Wait a minute! Wait just ONE minute!\x02\x03",

            "You can't just spring a rookie on me outta \x01",
            "nowhere like this!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(290, 170, -1, -1)
    SetChrName("Commander Selnate")

    AnonymousTalk(    #33
        (
            "\x07\x05Heh. Meetings ordained by the Goddess always\x01",
            "come suddenly and unannounced.\x02\x03",

            "Don't worry, though. They won't be a burden. \x01",
            "The abilities they demonstrated during training\x01",
            "were truly something special.\x02\x03",

            "Well, I will be praying for your success.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0x0, 0x6, 0x0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #34
        0x109,
        "Father Kevin",
        "#1064F#6P#100P...*gawp*...\x02",
    )

    CloseMessageWindow()

    def lambda_168E():
        OP_6D(-30, 1500, 5630, 2000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_168E)

    def lambda_16A6():
        OP_67(0, 6180, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_16A6)

    def lambda_16BE():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_16BE)

    def lambda_16CE():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_16CE)

    def lambda_16DE():
        OP_6E(325, 2000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_16DE)
    WaitChrThread(0x10, 0x0)
    SetChrSubChip(0x11, 1)
    Sleep(100)
    SetChrSubChip(0x10, 1)
    Sleep(150)

    ChrTalk(    #35
        0x11,
        "#5P#100PHaha... Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10,
        (
            "#5P#100PC-Congratulations on the new recruit?\x01",
            "We were only just saying you could do\x01",
            "with more squires serving you.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)

    NpcTalk(    #37
        0x109,
        "Father Kevin",
        (
            "#1068FAnd I was SO not down! I can't believe this...\x02\x03",

            "#1067F*sigh* She never changes, I swear.\x02\x03",

            "Oh, if all the people reading that book had\x01",
            "any idea what a hellion she is in real life...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x10,
        "#5P#100POh, Carnelia?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x11,
        (
            "#5P#100PI've always wondered whether publishing it\x01",
            "was really such a good idea, to be honest.\x02\x03",

            "It's a complete advertisement saying we\x01",
            "exist to the world.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #40
        0x109,
        "Father Kevin",
        (
            "#1060FIf anything, I'd say a book that wild just serves\x01",
            "to make people LESS likely to believe we really\x01",
            "exist.\x02\x03",

            "And then the heroine died in it, which obviously\x01",
            "is a big, fat lie.\x02\x03",

            "#1068FIf they'd actually met her, they'd know she's the\x01",
            "kind of woman who could probably take a bullet\x01",
            "to the head and ask for a cigarette first thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x11,
        "#5P#100PHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10,
        (
            "#5P#100PI...think we should probably refrain from\x01",
            "commenting here.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #43
        0x109,
        "Father Kevin",
        (
            "#1060FAnyway...you guys heard her.\x02\x03",

            "I'm gonna leave taking care of everything else\x01",
            "relating to our mission to you guys.\x02\x03",

            "Just follow the money trail--there might still\x01",
            "be hidden accounts we don't know about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        "#5P#100PUnderstood, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        (
            "#5P#100PWhat will you be doing from here?\x02\x03",

            "We'll need to return to Arteria, obviously,\x01",
            "but we can drop you off somewhere.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #46
        0x109,
        "Father Kevin",
        (
            "#1075FYou can put me down in any old state we pass\x01",
            "on the way there.\x02\x03",

            "#1060FPreferably near a town that has international\x01",
            "flights going out of it, I guess.\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    ChrTalk(    #47
        0x10,
        "#5P#100PGot it.\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrSubChip(0x10, 0)
    Sleep(150)

    ChrTalk(    #48
        0x10,
        "#5P#100POh, it looks like the sun's started coming up.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x11, 2)
    Sleep(100)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_2_1D8 end

    def Function_3_1DE3(): pass

    label("Function_3_1DE3")


    def lambda_1DE9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1DE9)
    OP_8F(0xFE, 0xFFFFFF74, 0x5DC, 0xFFFFFC5E, 0x7D0, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    OP_8F(0xFE, 0xFFFFFCE0, 0x7D0, 0x5AA, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFFCAE, 0x7D0, 0xAE6, 0x7D0, 0x0)
    WaitChrThread(0xFE, 0x1)
    Return()

    # Function_3_1DE3 end

    def Function_4_1E3C(): pass

    label("Function_4_1E3C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -160, 200, 6650, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -3150, 200, 6970, 315)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 2920, 200, 6830, 45)
    SetChrFlags(0x12, 0x4)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0x12, 0x1)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -100, 2200, 2400, 0)
    SetChrChipByIndex(0x12, 1)
    SetChrSubChip(0x12, 0)
    OP_43(0x12, 0x0, 0x0, 0x5)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_6F(0x0, 30)
    OP_72(0x800, 0x0)
    ExitThread()
    OP_74(0x0, 0x6, 0x3)

    def lambda_1EF6():

        label("loc_1EF6")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_1EF6")

    QueueWorkItem2(0x13, 3, lambda_1EF6)
    OP_76(0x2, 0x0, 0x1, 0xFFFFFFFD, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_76(0x2, 0x1, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x2, 0x2, 0x1, 0xFFFFFFF8, 0xFFFFFFFC, 0x0, 0x0, 0x0)
    OP_6D(4300, 0, 6750, 0)
    OP_67(0, 4870, -10000, 0)
    OP_6B(3320, 0)
    OP_6C(45000, 0)
    OP_6E(325, 0)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Commander Selnate")

    AnonymousTalk(    #49
        "\x07\x00I think I have a rough idea of the situation now.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    OP_1D(0x76)
    FadeToBright(2000, 0)
    OP_6B(3090, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x12,
        (
            "#1824F#6PWe've been able to confirm the safety of the six\x01",
            "you mentioned.\x02\x03",

            "Prince Olivert Reise Arnor, Mueller Vander...\x02\x03",

            "...Zin Vathek, Josette Capua...\x02\x03",

            "...Estelle and Joshua Bright...\x02\x03",

            "#1820FAll of them have safely returned to our world.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("Kevin's Voice")

    AnonymousTalk(    #51
        (
            "\x07\x05Really? That's a relief...\x02\x03",

            "I was able to confirm the safety of the ones who\x01",
            "ended up in Liberl myself--it was just those six\x01",
            "I was concerned about.\x02\x03",

            "Well, and the two from Ouroboros... But I'm not\x01",
            "sure either of us have any chance of checking up\x01",
            "on those two.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #52
        0x12,
        (
            "#1825F#6PHaha. Unfortunately not.\x02\x03",

            "#1822FStill, this certainly wasn't what I was expecting to\x01",
            "happen when I gave you that mission.\x02\x03",

            "The Aureole left us a nasty little present, didn't it?\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("Kevin's Voice")

    AnonymousTalk(    #53
        (
            "\x07\x05That's one way of putting it...\x02\x03",

            "...Either way, I'll give you my full report as soon\x01",
            "as I'm back.\x02\x03",

            "Wrapping things up on my end seems like it'll\x01",
            "take a little while longer, but hopefully not too\x01",
            "long.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #54
        0x12,
        "#1825F#6PI'm looking forward to it.\x02",
    )

    CloseMessageWindow()
    OP_44(0x12, 0x0)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Sleep(300)

    ChrTalk(    #55
        0x12,
        (
            "#1826F#6P...You know, you've changed since I last\x01",
            "spoke to you. I'm quite surprised.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("Kevin's Voice")

    AnonymousTalk(    #56
        "\x07\x05Huh?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #57
        0x12,
        (
            "#1825F#6PThe Kevin I know wouldn't care to know whether\x01",
            "those he'd been involved with were safe or not.\x02\x03",

            "Or rather, he'd try and suppress those concerns.\x02\x03",

            "#1820FI can only imagine a lot must have happened in\x01",
            "this 'Phantasma.'\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("Kevin's Voice")

    AnonymousTalk(    #58
        (
            "\x07\x05Haha... That's putting it lightly.\x02\x03",

            "I'll fill you in on all of it once I get back,\x01",
            "like I said.\x02\x03",

            "...I've got something I want to tell you on\x01",
            "a personal level, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #59
        0x12,
        (
            "#1823F#6POh? Color me curious.\x02\x03",

            "#1825FRegardless, I'm glad you two returned safely.\x02\x03",

            "#1821FPerhaps we should all go and get some drinks\x01",
            "together after you return.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("Kevin's Voice")

    AnonymousTalk(    #60
        (
            "\x07\x05Haha. I'd be happy to.\x02\x03",

            "...Oh, yeah... I've actually got something\x01",
            "I want to ask.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #61
        0x12,
        "#1820F#6PHmm?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("Kevin's Voice")

    AnonymousTalk(    #62
        (
            "\x07\x05Umm... Well...\x02\x03",

            "...is it possible for a Dominion to change\x01",
            "their title after choosing one?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x12, 0x96, 1500, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2832():
        OP_99(0xFE, 0x6, 0x9, 0x708)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2832)
    Sleep(500)

    ChrTalk(    #63
        0x12,
        "#1823F#6PWhat's this, now?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("Kevin's Voice")

    AnonymousTalk(    #64
        (
            "\x07\x05I just... I've found something other than hunting\x01",
            "heretics I want to do, you see.\x02\x03",

            "I still intend to fulfill my duties as a Dominion to\x01",
            "the fullest, don't worry about that. Just...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x12, 0xFFFFFFCE, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    Sleep(500)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(80)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)

    ChrTalk(    #65
        0x12,
        "#1825F#6P#40W...Haha...Hahaha....\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(4300, 0, 6900, 0)
    ClearChrFlags(0x12, 0x800)
    ClearChrFlags(0x12, 0x1)
    SetChrPos(0x12, -250, 2000, 2600, 45)
    SetChrSubChip(0x12, 16)
    OP_0D()
    OP_43(0x12, 0x0, 0x0, 0x6)
    OP_44(0x13, 0x3)

    ChrTalk(    #66
        0x12,
        "#1827F#6P#4SHahahahahahaha!\x02",
    )

    OP_7C(0x32, 0x32, 0xBB8, 0x1F4)
    CloseMessageWindow()

    def lambda_2AEA():

        label("loc_2AEA")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_2AEA")

    QueueWorkItem2(0x13, 3, lambda_2AEA)
    OP_62(0x13, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x14, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x15, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    SetChrSubChip(0x14, 1)
    Sleep(100)
    SetChrSubChip(0x13, 1)
    Sleep(150)

    ChrTalk(    #67
        0x14,
        "#2PC-Commander...?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("Kevin's Voice")

    AnonymousTalk(    #68
        "\x07\x05Erm... Sooo, that's a 'no,' probably.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #69
        0x12,
        (
            "#1825F#6PHaha... A Dominion wanting to change their title,\x01",
            "eh?\x02\x03",

            "In the thousand years the Gralsritter has existed,\x01",
            "that's not something that has happened often.\x02\x03",

            "#1821F...But it's not entirely unprecedented, either.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("Kevin's Voice")

    AnonymousTalk(    #70
        "\x07\x05Then...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #71
        0x12,
        (
            "#1826F#6PHaha. Go ahead and think up something fitting\x01",
            "for yourself before we next meet.\x02\x03",

            "If you fail to, I'll give you a new one myself as\x01",
            "punishment. And trust me--you won't like it.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("Kevin's Voice")

    AnonymousTalk(    #72
        (
            "\x07\x05If I'd known you were going to say that,\x01",
            "I would've thought of something before\x01",
            "asking!\x02\x03",

            "Well, I guess I'd better get to work on\x01",
            "thinking up something cool.\x02\x03",

            "What do you think of 'Blue Shooting Star'?\x01",
            "Or maybe  'Black Arrow'?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    Sleep(300)
    OP_62(0x13, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x14, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x15, 0xFFFFFF6A, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x12, 0xFFFFFE98, 2200, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x12)
    OP_63(0x13)
    OP_63(0x14)
    OP_63(0x15)
    Sleep(500)
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("Kevin's Voice")

    AnonymousTalk(    #73
        "\x07\x05Wh-What's with the awkward silence?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(120)
    Sleep(300)

    ChrTalk(    #74
        0x12,
        (
            "#1824F#6P...Father Kevin.\x02\x03",

            "#1821FAs your former instructor, allow to me to give\x01",
            "you one piece of heartfelt advice.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 85, -1, -1)
    SetChrName("Kevin's Voice")

    AnonymousTalk(    #75
        "\x07\x05...Sure?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    def lambda_3056():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3056)

    def lambda_3066():
        OP_6B(2900, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3066)
    FadeToDark(2000, 0, -1)
    OP_24(0x7A, 0x3C)
    Sleep(200)
    OP_24(0x7A, 0x32)
    Sleep(200)
    OP_24(0x7A, 0x28)
    Sleep(200)
    OP_24(0x7A, 0x1E)
    Sleep(200)
    OP_24(0x7A, 0x14)
    Sleep(200)
    OP_24(0x7A, 0xA)
    Sleep(200)
    OP_23(0x7A)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    WaitChrThread(0xEE, 0x2)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Commander Selnate")

    AnonymousTalk(    #76
        (
            "\x07\x00Unless you want to live the rest of your life in\x01",
            "abject shame...\x02\x03",

            "...for the love of Aidios, get Ries to help you\x01",
            "choose.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_20(0x1388)
    OP_21()
    Sleep(3000)
    OP_1D(0x1)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x400, 0x0, 0x0, 0x400, 0x400, 0x0, 0x0, 0x280, 0x400, 0xFFFFFF, 0x0, "C_VIS477._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x96, 0x78, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS478._CH")
    OP_C6(0x0, 0x3, -1, 2000, 0)
    OP_C6(0x0, 0x7, 0, -320000, 7000)
    OP_C7(0x0, 0x0, 0x0)
    Sleep(2000)
    OP_C6(0x1, 0x3, -1, 2000, 0)
    Sleep(3000)
    OP_56(0x2)
    OP_C6(0x0, 0x3, 16777215, 2500, 0)
    OP_C6(0x1, 0x3, 16777215, 3000, 0)
    Sleep(4000)
    OP_A2(0x2C27)
    OP_A2(0x2582)
    OP_C4(0x0, 0x10)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x15D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x2502)
    OP_F7(0x8, 0x0, 0x0)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("")

    AnonymousTalk(    #77
        "\x07\x05Save Clear Data?\x18\x02",
    )


    Menu(
        0,
        -1,
        180,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32B4")
    OP_DC(0x0, 0x3)
    ShowSaveMenu()
    EventBegin(0x4)

    label("loc_32B4")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C4(0x1, 0x10)
    OP_A3(0x2582)
    FadeToDark(0, 0, -1)
    OP_56(0x0)
    OP_20(0xBB8)
    OP_21()
    Sleep(3000)
    OP_B4(0x1)
    Return()

    # Function_4_1E3C end

    def Function_5_32E0(): pass

    label("Function_5_32E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_332C")
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    Jump("Function_5_32E0")

    label("loc_332C")

    Return()

    # Function_5_32E0 end

    def Function_6_332D(): pass

    label("Function_6_332D")

    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(60)
    Return()

    # Function_6_332D end

    SaveToFile()

Try(main)
