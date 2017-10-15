from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C4303   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4303.x',
        MapIndex            = 216,
        MapDefaultBGM       = "ed60033",
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
        'Kevin',                                # 9
        'Julia',                                # 10
        'Reverie',                              # 11
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
        'ED6_DT27/CH03080 ._CH',             # 00
        'ED6_DT27/CH03580 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT27/CH03080P._CP',             # 00
        'ED6_DT27/CH03580P._CP',             # 01
        'ED6_DT27/CH03090P._CP',             # 02
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
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
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_11E",          # 00, 0
        "Function_1_123",          # 01, 1
        "Function_2_124",          # 02, 2
    )


    def Function_0_11E(): pass

    label("Function_0_11E")

    Event(0, 2)
    Return()

    # Function_0_11E end

    def Function_1_123(): pass

    label("Function_1_123")

    Return()

    # Function_1_123 end

    def Function_2_124(): pass

    label("Function_2_124")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x10A, 0x8)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 800, 0, -15000, 0)
    SetChrPos(0x9, -800, 0, -16000, 0)
    SetChrFlags(0x8, 0x40)
    OP_6D(2460, 0, -21910, 0)
    OP_67(0, 10420, -10000, 0)
    OP_6B(4190, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_A1(0xA, 0x9)
    SetChrPos(0xA, 4030, 0, 6430, 63)
    OP_72(0x9, 0x20)
    OP_72(0x9, 0x4)
    OP_72(0x9, 0x2)
    OP_6F(0x9, 843)
    OP_70(0x9, 0x34B)
    OP_72(0x6, 0x20)
    OP_6F(0x6, 240)
    OP_72(0x5, 0x20)
    OP_71(0x5, 0x4)
    OP_72(0x0, 0x20)
    OP_72(0x1, 0x20)
    OP_72(0x2, 0x20)
    OP_72(0x3, 0x20)
    OP_6F(0x0, 3260)
    OP_6F(0x1, 3260)
    OP_6F(0x2, 3260)
    OP_6F(0x3, 3260)

    def lambda_227():
        OP_6D(1480, 0, 1000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_227)

    def lambda_23F():
        OP_67(0, 10420, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23F)

    def lambda_257():
        OP_8E(0x9, 0xFFFFFCE0, 0x0, 0xFFFFFFF6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_257)

    def lambda_272():
        OP_8E(0x8, 0x320, 0x0, 0x5A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_272)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 0x0)
    Fade(500)
    OP_6B(3200, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x8)
    Sleep(500)

    ChrTalk(    #0
        0x8,
        "#1063F#2PWell now, would you look at this...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "#1P#178FI imagine even the church will have\x01",
            "difficulty deciding what to do with\x01",
            "this, yes?\x02\x03",

            "This sort of artifact isn't so much\x01",
            "'big' as it is 'gargantuan.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "#1067F#2PHmm...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 265, 500)
    Sleep(500)

    ChrTalk(    #3
        0x8,
        "#1060F#2PYou mind if I take a closer look?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 500)
    Sleep(400)

    ChrTalk(    #4
        0x9,
        (
            "#1P#178FAs you like.\x01",
            "The queen has given her permission.\x02\x03",

            "Please, if you understand any\x01",
            "of this, share your thoughts.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 500)
    OP_8C(0x8, 45, 500)

    def lambda_48D():
        OP_6D(3630, 0, 4360, 3000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_48D)

    def lambda_4A5():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_4A5)

    def lambda_4BD():
        OP_8E(0x8, 0x9CE, 0x0, 0xC6C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BD)
    OP_8C(0x9, 37, 500)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x8, 339, 1000)
    Sleep(1000)
    OP_8C(0x8, 48, 1000)
    Sleep(1000)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #5
        0x8,
        (
            "#1063F#6PSo this is the 'Ring Guardian'\x01",
            "that was in the report, huh?\x02\x03",

            "It's kinda similar to the robot excavated\x01",
            "in Calvard, but...hmm...\x02\x03",

            "#1067FAhhh, wish I could've seen it moving.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 500)
    Sleep(500)

    ChrTalk(    #6
        0x8,
        "#1063F#4PAnd this...\x02",
    )

    CloseMessageWindow()

    def lambda_5E2():
        OP_8E(0x8, 0xFFFFFD3A, 0x0, 0x1ACC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E2)
    Sleep(1000)
    OP_8C(0x9, 0, 500)

    def lambda_609():
        OP_6D(390, 600, 19290, 6000)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_609)

    def lambda_621():
        OP_67(0, 9500, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_621)

    def lambda_639():
        OP_6B(4200, 6000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_639)
    WaitChrThread(0x101, 0x1)

    def lambda_64E():
        OP_8E(0x8, 0xF0, 0x258, 0x45EC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_64E)
    Sleep(500)

    def lambda_66E():
        OP_8E(0x9, 0xFFFFFDC6, 0x0, 0x2A4E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_66E)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x9, 0x8, 500)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #7
        0x8,
        (
            "#1063FThis thing's an artifact from the last years of the ancient\x01",
            "Zemurian civilization...which makes it at least 1,200 years old.\x02\x03",

            "It's clearly the core of the structure,\x01",
            "but...there's no clear indication as\x01",
            "to what it actually does.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #8
        0x9,
        (
            "#2P#178FAnalysis of artifacts seems to\x01",
            "be impossible with modern tools.\x02\x03",

            "They work on the same principle and energy\x01",
            "as an orbment, but their internal structure is\x01",
            "entirely different from an orbment's...\x02\x03",

            "That's what Professor Russell\x01",
            "told us, at least.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    Sleep(500)

    ChrTalk(    #9
        0x8,
        (
            "#1060F#3PThe church refers to these as 'gifts\x01",
            "from the Goddess, given too early.'\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 225, 500)
    Sleep(500)

    ChrTalk(    #10
        0x8,
        "#1063F#6PAnd over here is...\x02",
    )

    CloseMessageWindow()

    def lambda_927():
        OP_8E(0x8, 0xFFFFE6BA, 0x0, 0x35A2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_927)
    Sleep(1000)

    def lambda_947():
        OP_6D(-6050, 0, 13970, 3000)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_947)

    def lambda_95F():
        OP_67(0, 9500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_95F)
    OP_8C(0x9, 225, 500)
    Sleep(1000)

    def lambda_983():
        OP_8E(0x9, 0xFFFFE8EA, 0x0, 0x285A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_983)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x9, 0x0)
    WaitChrThread(0x9, 0x1)
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #11
        0x8,
        (
            "#5P#1063FSo just after the Black Orbment you\x01",
            "called the 'Gospel' was used...\x02\x03",

            "All the giant pillars that were\x01",
            "in here were set into the floor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x9,
        (
            "#4P#178F#2PYes, all four pillars set into\x01",
            "the floor, like this one.\x02\x03",

            "Even two months later, we're not even\x01",
            "sure what it means...if anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#5P#1065FOkay, so...a seal on the 'Aureole'...\x01",
            "a 'Gospel' was used...\x02\x03",

            "And then the device in here spoke of\x01",
            "'device towers' and a 'second barrier'...\x02\x03",

            "#1067FI think I'm starting to see what kind\x01",
            "of system is at work here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    TurnDirection(0x9, 0x8, 500)

    ChrTalk(    #14
        0x9,
        (
            "#2P#173FErm, 'system'?\x02\x03",

            "What system? There's nothing else here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    Sleep(500)

    ChrTalk(    #15
        0x8,
        (
            "#5P#1060FAh, well, call it gut instinct\x01",
            "at this point. But...\x02\x03",

            "I THINK this was some sort\x01",
            "of 'gate.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x9,
        "#2P#178FGate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#5P#1060FBingo.\x02\x03",

            "#1065FCall it a gate on the trail that leads\x01",
            "to the Goddess' treasure.\x02\x03",

            "And the thing that opens it is a\x01",
            "black key called a 'Gospel.'\x02\x03",

            "#1063FIf you think about it like that, the\x01",
            "Aureole being AWOL makes a lot\x01",
            "more sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        (
            "#2P#178FBut...where's this 'trail' of yours,\x01",
            "then? This is the lowest floor!\x02\x03",

            "According to the professor,\x01",
            "the ruins extend no further!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#5P#1060FAh, think a little less...literally.\x01",
            "It's not a 'trail' you see with your\x01",
            "eyes or normally walk.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Kevin")

    AnonymousTalk(    #20
        (
            "\x07\x00It could be the septium veins that run\x01",
            "through the earth, or maybe it's some\x01",
            "route we can't even imagine...\x02\x03",

            "...but that's where we'll find a clue that\x01",
            "will lead to the Aureole.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_DB()
    Sleep(2000)
    Sleep(1000)
    OP_AD(0x2400A4, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_20(0xBB8)
    OP_AE(0xC8)
    Sleep(2000)
    OP_21()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_DC()
    NewScene("ED6_DT21/T4105   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_124 end

    SaveToFile()

Try(main)
