from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1111   ._SN',
        MapName             = 'Bose',
        Location            = 'T1111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
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
        'Mayor Maybelle',                       # 9
        'Lila',                                 # 10
        'Sarah',                                # 11
        'Butler Mayner',                        # 12
        'Anelace',                              # 13
        'Target Camera',                        # 14
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
        'ED6_DT07/CH02360 ._CH',             # 00
        'ED6_DT07/CH02370 ._CH',             # 01
        'ED6_DT07/CH01350 ._CH',             # 02
        'ED6_DT07/CH02363 ._CH',             # 03
        'ED6_DT07/CH01560 ._CH',             # 04
        'ED6_DT27/CH03090 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH02360P._CP',             # 00
        'ED6_DT07/CH02370P._CP',             # 01
        'ED6_DT07/CH01350P._CP',             # 02
        'ED6_DT07/CH02363P._CP',             # 03
        'ED6_DT07/CH01560P._CP',             # 04
        'ED6_DT27/CH03090P._CP',             # 05
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
        Direction           = 0,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        "Function_0_19A",          # 00, 0
        "Function_1_1BA",          # 01, 1
        "Function_2_1BB",          # 02, 2
        "Function_3_765",          # 03, 3
        "Function_4_7C0",          # 04, 4
        "Function_5_833",          # 05, 5
        "Function_6_8A1",          # 06, 6
        "Function_7_917",          # 07, 7
        "Function_8_99C",          # 08, 8
        "Function_9_324A",         # 09, 9
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_1B9")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_1B9")

    Return()

    # Function_0_19A end

    def Function_1_1BA(): pass

    label("Function_1_1BA")

    Return()

    # Function_1_1BA end

    def Function_2_1BB(): pass

    label("Function_2_1BB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, -120710, 200, 68600, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, -120260, 0, 65470, 0)
    OP_6D(-121830, 0, 68600, 0)
    OP_67(0, 4550, -10000, 0)
    OP_6B(2550, 0)
    OP_6C(315000, 0)
    OP_6E(322, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #0
        0x13,
        (
            "#6PHmm...\x02\x03",

            "Have I noticed anything strange in Lila's\x01",
            "behavior lately, you say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "#610F#2PWell, have you?\x02\x03",

            "For example, have you seen her with anyone you\x01",
            "don't recognize?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x13,
        (
            "#6PHmm... Actually, now that you mention it, I have\x01",
            "on one occasion.\x02\x03",

            "It was when I went to visit Trino at his home the\x01",
            "other day.\x02\x03",

            "I saw her walking side-by-side with a young man\x01",
            "I'd never seen before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        "#610F#2PWhat kind of person was he?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x13,
        (
            "#6PHe looked like a bar waiter, or like a man of \x01",
            "some other similar profession.\x02\x03",

            "He was a well-kept, pleasant-looking young man.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 0)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, -62700, -3000, 65960, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -64050, -3000, 65990, 90)
    SetChrFlags(0x13, 0x80)
    OP_6D(-64500, -3000, 66970, 0)
    OP_67(0, 5580, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(275, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #5
        0x12,
        (
            "#5POh, come to think of it...\x02\x03",

            "I think I've seen the man we're talking about\x01",
            "escorting Lila back home once before, too.\x02\x03",

            "As well as shopping together one time, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#610FI see...\x02\x03",

            "It sounds like there's no mistaking it, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x12,
        (
            "#5PWait... Is this what I think it is?\x02\x03",

            "A-Are you suggesting he's her...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#610FPlease just watch over her for now, Sarah.\x02\x03",

            "That's what I intend to do, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x12,
        (
            "#5PO-Of course... All right, then.\x02\x03",

            "Still, the day's finally come, huh? Oh my...\x02\x03",

            "This world is just full of surprises...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/T1101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1BB end

    def Function_3_765(): pass

    label("Function_3_765")

    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_775():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_775)

    def lambda_787():
        OP_8E(0xFE, 0xFFFE32E8, 0x0, 0xFB0D, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_787)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFE2BEA, 0x0, 0x1007C, 0x5DC, 0x0)
    Return()

    # Function_3_765 end

    def Function_4_7C0(): pass

    label("Function_4_7C0")


    def lambda_7C6():
        OP_8E(0xFE, 0xFFFE32E8, 0x0, 0xFB0D, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7C6)
    WaitChrThread(0xFE, 0x2)
    OP_8C(0xFE, 180, 400)
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)

    def lambda_7F7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7F7)

    def lambda_809():
        OP_8E(0xFE, 0xFFFE33EC, 0x0, 0xF424, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_809)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_4_7C0 end

    def Function_5_833(): pass

    label("Function_5_833")

    OP_8C(0xFE, 90, 400)
    OP_8F(0xFE, 0xFFFE33B0, 0x0, 0xFBB8, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)

    def lambda_865():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_865)

    def lambda_877():
        OP_8E(0xFE, 0xFFFE336A, 0x0, 0xF42E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_877)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    SetChrFlags(0xFE, 0x80)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_5_833 end

    def Function_6_8A1(): pass

    label("Function_6_8A1")

    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_8B1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8B1)

    def lambda_8C3():
        OP_8E(0xFE, 0xFFFE33EC, 0x0, 0xFC07, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8C3)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFE2E24, 0x0, 0xFC07, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE2A3C, 0x0, 0xFFEF, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_6_8A1 end

    def Function_7_917(): pass

    label("Function_7_917")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_92F():
        OP_8E(0xFE, 0xFFFE32E8, 0x0, 0xFB0D, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_92F)
    WaitChrThread(0xFE, 0x2)
    OP_8C(0xFE, 180, 500)
    Sleep(200)
    OP_22(0x6, 0x0, 0x64)

    def lambda_960():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_960)

    def lambda_972():
        OP_8E(0xFE, 0xFFFE33EC, 0x0, 0xF424, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_972)
    WaitChrThread(0xFE, 0x1)
    WaitChrThread(0xFE, 0x2)
    OP_22(0x7, 0x0, 0x64)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_7_917 end

    def Function_8_99C(): pass

    label("Function_8_99C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x0, -120000, 0, 65800, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x10, -120710, 200, 68600, 180)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x40)
    SetChrPos(0x13, -115800, 0, 60820, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -120510, 0, 66280, 0)
    OP_6D(-122340, 0, 69030, 0)
    OP_67(0, 4550, -10000, 0)
    OP_6B(2850, 0)
    OP_6C(315000, 0)
    OP_6E(322, 0)
    FadeToBright(2000, 0)
    OP_6B(2550, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(    #10
        0x10,
        (
            "#615F#11PI see... So the man in question is Lenard\x01",
            "from the Kingfisher Inn?\x02\x03",

            "#610FI wonder how those two came to know\x01",
            "each other...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x14,
        "#814F#6POh, you know Lenard already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#610F#11POnly by name. I can't say I've ever spoken\x01",
            "to him in person as such.\x02\x03",

            "The Kingfisher Inn has really made a name\x01",
            "for itself in recent years.\x02\x03",

            "#615FIt's been doing quite well financially, too.\x01",
            "As things stand, it's a good target for\x01",
            "investment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x14,
        (
            "#816F#6PTrino said that, too. I'm no expert on that\x01",
            "kind of stuff, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#615F#11PStill, from what I can gather based on your\x01",
            "report, their relationship is a healthy one.\x02\x03",

            "#611FAnd you seem to think very highly of Lenard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14,
        (
            "#819F#6POh, absolutely.\x02\x03",

            "#1310FEven his little sister, Sophina, is super sweet.\x02\x03",

            "#811FI'd say you don't have anything to worry about\x01",
            "with them. From what I've gathered, they'd make\x01",
            "for a picture-perfect married couple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#611F#11PI-I'd like to believe that's still a while off...\x02\x03",

            "#618FThen again, if they really are dating, it's a reality\x01",
            "I'll have to come to terms with sooner or later.\x02\x03",

            "#617FHeehee... I'm happy for her, but at the same time,\x01",
            "I'm a little sad, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x14,
        "#1314F#6PI get what you mean...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "#615F#11PThank you very much for your report, Anelace.\x02\x03",

            "#611FIt sounds like she's made a fine choice.\x02\x03",

            "So I suppose all I can do now is wait for her to\x01",
            "share the truth with me herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x14,
        "#819F#6PThat sounds like a good plan.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_22(0x71, 0x0, 0x64)
    Sleep(800)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1057():
        OP_6D(-121020, 0, 68070, 1200)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1057)

    def lambda_106F():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_106F)
    Sleep(200)
    SetChrSubChip(0x10, 1)
    WaitChrThread(0x10, 0x1)
    Sleep(300)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -115800, 0, 60820, 0)

    NpcTalk(    #20
        0x11,
        "Lila's Voice",
        (
            "#2P...Miss Maybelle? It's me, Lila.\x02\x03",

            "Could I have a little of your time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x14,
        "#814F#5POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#617F#5PHeehee. Speak of the devil.\x02\x03",

            "#611FI wonder if the time has finally come?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x10, 500)
    Sleep(300)

    ChrTalk(    #23
        0x14,
        (
            "#819F#6PThat'd be one funny coincidence, but maybe\x01",
            "it has!\x02\x03",

            "#1310FAnd if it has, then it's just about time I made\x01",
            "my exit. I wouldn't want to get in the way.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x10, 0)
    Sleep(200)

    ChrTalk(    #24
        0x10,
        (
            "#615F#11PNonsense. I'd actually prefer if you stayed.\x02\x03",

            "#610FIf she does tell us what I expect her to, I don't\x01",
            "intend to hide the truth of what I asked you to\x01",
            "do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x14,
        (
            "#814F#6POh, I see...\x02\x03",

            "#816FWell, okay, then!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #26
        0x11,
        "Lila's Voice",
        "#2P...Miss Maybelle?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x10, 1)
    Sleep(200)

    ChrTalk(    #27
        0x10,
        (
            "#610F#5POh! Sorry, Lila.\x02\x03",

            "Come on in.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #28
        0x11,
        "Lila's Voice",
        "#2PAs you wish.\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_1391():
        OP_6D(-121830, 0, 68600, 3000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1391)
    SetChrPos(0x11, -117780, 0, 62500, 0)
    OP_43(0x11, 0x0, 0x0, 0x3)
    Sleep(200)

    def lambda_13C6():

        label("loc_13C6")

        TurnDirection(0xFE, 0x11, 500)
        OP_48()
        Jump("loc_13C6")

    QueueWorkItem2(0x14, 2, lambda_13C6)
    Sleep(300)

    def lambda_13DC():
        OP_8F(0xFE, 0xFFFE2370, 0x0, 0x101E4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_13DC)
    Sleep(1500)
    SetChrSubChip(0x10, 0)
    WaitChrThread(0x11, 0x0)
    OP_62(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x11, 0x14, 400)
    Sleep(300)

    ChrTalk(    #29
        0x11,
        (
            "#622F#12POh... Miss Anelace?\x02\x03",

            "#623FPlease do accept my apologies. I didn't realize\x01",
            "I was intruding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x14,
        (
            "#819F#5PYou're not, you're not! Don't mind me.\x02\x03",

            "#816FI was just here to give my report on an\x01",
            "investigation on behalf of the mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        "#622F#12PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "#615F#11PSo, what brings you here, Lila?\x02\x03",

            "#610FDo you have something you want to talk\x01",
            "to me about?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x11, 0, 400)
    Sleep(300)

    ChrTalk(    #33
        0x11,
        (
            "#620F#6PYou could say that, yes.\x02\x03",

            "I have an important request I wish you\x01",
            "make of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        "#617F#11PR-Really, now? What would it happen to be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x11,
        (
            "#621F#6PWell, it concerns the Kingfisher Inn near\x01",
            "Valleria Lake...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0x10,
        "#610F#11PMy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x14,
        "#816F#5PWe were right!\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #38
        0x11,
        "#622F#6P...Excuse me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#617F#11PHeehee...\x02\x03",

            "#611FDid you think I had no idea what was happening?\x02\x03",

            "I already know everything there is to know.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #40
        0x11,
        "#625F#6PHow could you possibly...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "#615F#11PI'm sorry. I actually had Anelace here look into\x01",
            "it for me.\x02\x03",

            "I was worried about you, you see... You'd been \x01",
            "behaving so strangely lately.\x02\x03",

            "#618FI'm sorry that I did it, but I just couldn't help\x01",
            "myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        (
            "#621F#6PI see...\x02\x03",

            "#620FThere's no need for you to apologize, however.\x01",
            "I didn't mean to worry you... Perhaps I should \x01",
            "have been more open from the start.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#613F#11PS-So...umm...\x02\x03",

            "#617F...is Lenard being good to you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x14,
        (
            "#1317F#5P(D-Damn...)\x02\x03",

            "#819F(Cut right to the chase, why don'cha?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x11,
        "#622F#6PHe's a very kind man, yes. Why do you ask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        (
            "#618F#11PTh-That wasn't what I was asking... Oooh!\x01",
            "You know what I mean, Lila.\x02\x03",

            "#612FSo...is there anything else you want to say\x01",
            "on the matter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "#623F#6PWell, yes...\x02\x03",

            "#621FIf it's all right with you, I'd like to get right\x01",
            "to discussing the date for the big day.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(300)

    ChrTalk(    #48
        0x14,
        "#1317F#5P#4SAlready?!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #49
        0x10,
        (
            "#613F#11PTH-THE big day?!\x02\x03",

            "#614F#3SYou've already started mapping it out?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x11,
        (
            "#620F#6PWe have. We were hoping to keep it a\x01",
            "secret for as long as possible in order to\x01",
            "surprise you.\x02\x03",

            "Naturally, I've made sure everything fits\x01",
            "into your schedule.\x02\x03",

            "#621FDo I have your okay to begin making the\x01",
            "necessary arrangements?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        "#618F#11P#40W...\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_44(0x14, 0xFF)
    OP_62(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x14, 0x10, 500)
    Sleep(400)
    TurnDirection(0x14, 0x11, 500)
    Sleep(200)

    ChrTalk(    #52
        0x14,
        "#819F#5PUmm... Wooowie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x11,
        "#622F#6PIs something wrong?\x02",
    )

    CloseMessageWindow()
    OP_63(0x10)
    Sleep(300)

    ChrTalk(    #54
        0x10,
        "#618F#11P#60W#1S...Yo.. ..mmy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x11,
        "#625F#6PWhat was that?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #56
        0x10,
        "#616F#11P#5SYou dummy!\x02",
    )

    OP_7C(0x0, 0x1F4, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #57
        0x11,
        "#628F#6P#3S...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10,
        (
            "#618F#11PI-I can see why you might've wanted to\x01",
            "surprise me. I can!\x02\x03",

            "#619FBut did you really have to keep this from\x01",
            "me until THIS late in the process?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x11,
        "#625F#6PUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x10,
        (
            "#616F#11PI mean, you've got a right to your own private\x01",
            "life, and you don't have to share everything in\x01",
            "that with me. I'm not saying you have to.\x02\x03",

            "But I can't believe you would decide something\x01",
            "so important without consulting me even once!\x02\x03",

            "#619FDo I mean THAT little to you?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x11,
        "#622F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        (
            "#618F#11PB-Besides, you've only been going out for\x01",
            "about a month!\x02\x03",

            "Aren't wedding bells at this stage a LITTLE\x01",
            "premature?!\x02\x03",

            "#619FThis decision is going to impact you for the\x01",
            "rest of your life, Lila!\x02\x03",

            "You understand that, right?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x14,
        (
            "#1317F#5PI-I think you should calm down and listen to\x01",
            "what she has to say, Mayor Maybelle...\x02\x03",

            "I'm sure she does understand, and has her\x01",
            "own reasons for decidi--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x11,
        (
            "#627F#6PUmm...\x02\x03",

            "#625FI have a horrible feeling that there is a very\x01",
            "grave misunderstanding taking place here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x14,
        "#814F#5P...? You serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x10,
        "#618F#11P#40WJust what are we misunderstanding?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x11,
        (
            "#621F#6PThe arrangements I have been making are for\x01",
            "your next vacation.\x02\x03",

            "You've been so busy lately that I thought you\x01",
            "really ought to have one, so I've been making\x01",
            "the necessary arrangements in secret.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x14)
    OP_63(0x10)
    Sleep(300)

    ChrTalk(    #68
        0x14,
        "#1317F#1P#3SWhat?!\x02",
    )


    ChrTalk(    #69
        0x10,
        "#613F#2P#3SWhat?!\x02",
    )

    OP_56(0x1)
    OP_59()
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #70
        0x11,
        (
            "#627F#6PYou mentioned before that you would like to\x01",
            "visit the famous Kingfisher Inn once, you see...\x02\x03",

            "So when Lenard needed to come to Bose Market\x01",
            "to do some shopping, we decided to use the\x01",
            "chance to meet and discuss how to go about this.\x02\x03",

            "#623FI hadn't realized my actions were causing so many\x01",
            "problems for you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10,
        "#613F#11P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x14,
        "#819F#5P...Whoopsie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x11,
        (
            "#625F#6P*sigh* I worry about you sometimes...\x02\x03",

            "#624FBesides, I have no intention of getting married\x01",
            "before a certain mistress of mine.\x02\x03",

            "Which doesn't seem to be any time soon since she\x01",
            "makes a hobby of turning down countless marriage\x01",
            "proposals in favor of devoting herself to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10,
        (
            "#618F#11PI-It's not a hobby! It's because I have so much\x01",
            "work on my plate that I don't have time for\x01",
            "marriage to be on the brain!\x02\x03",

            "#617F...So there's nothing between you and Lenard?\x01",
            "Nothing at all?\x02\x03",

            "Everyone says you two have been getting along\x01",
            "so well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x11,
        (
            "#623F#6PI'll admit that he's a lovely man, and one I have a\x01",
            "very positive impression of...\x02\x03",

            "...but I've never considered him a potential partner.\x01",
            "Not once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x10,
        (
            "#612F#11PWh-Why?\x02\x03",

            "All girls your age experience romance at least\x01",
            "once. It wouldn't be right for you not to do the\x01",
            "same...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x11,
        (
            "#621F#6PThis isn't something I intended to come out and\x01",
            "say, but it seems you leave me with no choice.\x02\x03",

            "Right now, the most important thing in my life is\x01",
            "your happiness; I will put that over anything and\x01",
            "everything else.\x02\x03",

            "Ensuring it is my greatest joy. My very reason for\x01",
            "being.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #78
        0x10,
        "#613F#11P...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x11,
        (
            "#621F#6PUntil you've decided upon a partner to supplement\x01",
            "that happiness, I have absolutely no intention of\x01",
            "looking at anyone but you.\x02\x03",

            "#623FI do appreciate you worrying about me...\x02\x03",

            "If it's my happiness you want, I ask that you focus\x01",
            "on your own happiness first and foremost.\x02\x03",

            "#627FAnd yet like clockwork, I see you disregarding your\x01",
            "well-being and taking on far more work than is\x01",
            "humanly possib--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        (
            "#616F#11PFine! Fine! I get it, I get it!\x02\x03",

            "Now that we can put the whole marriage\x01",
            "thing behind us, I will accept your offer of\x01",
            "a vacation!\x02\x03",

            "So feel free to proceed with your plan--\x01",
            "I leave arranging the schedule to you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x11,
        (
            "#621F#6PHeehee. As you wish...\x02\x03",

            "#620FThen if you will permit me to excuse myself,\x01",
            "I shall.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x14, 400)
    Sleep(300)

    ChrTalk(    #82
        0x11,
        "#621F#12PGood day to you, too, Miss Anelace.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x14,
        "#814F#5POh...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 135, 400)

    def lambda_2CB2():

        label("loc_2CB2")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_2CB2")

    QueueWorkItem2(0x14, 2, lambda_2CB2)

    def lambda_2CC3():
        OP_6D(-121430, 0, 68300, 2000)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2CC3)
    OP_43(0x11, 0x0, 0x0, 0x4)
    Sleep(1500)
    SetChrSubChip(0x10, 1)
    WaitChrThread(0x11, 0x0)
    OP_44(0x14, 0x2)
    Sleep(1000)

    def lambda_2CFA():
        OP_6D(-122340, 0, 69030, 1200)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2CFA)
    OP_44(0x14, 0xFF)
    TurnDirection(0x14, 0x10, 400)
    WaitChrThread(0x10, 0x1)
    Sleep(300)

    ChrTalk(    #84
        0x14,
        (
            "#1317F#5PU-Umm...\x02\x03",

            "#1316FI'm reeeally sorry... It looks like my research\x01",
            "may have been a tad incomplete.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x10, 0)
    Sleep(300)

    ChrTalk(    #85
        0x10,
        (
            "#617F#11PDon't worry about it. I don't think anything\x01",
            "was wrong with your report.\x02\x03",

            "#618FAll of this was due to me foolishly jumping to\x01",
            "conclusions.\x02\x03",

            "*sigh* I can't believe I ended up giving her yet\x01",
            "another excuse to lecture me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x14,
        (
            "#819F#5PAww! It's no big deal.\x02\x03",

            "#1314FI gotta admit, though. I am jealous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10,
        "#613F#11P...Jealous?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x14,
        (
            "#1310F#5PHa! You never heard that. Anyway, I'm sure I'll\x01",
            "see you around!\x02\x03",

            "#819FUmm... You two look great together!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x14, 135, 500)

    def lambda_2F78():
        OP_6D(-121430, 0, 68300, 1200)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2F78)
    OP_43(0x14, 0x0, 0x0, 0x7)
    Sleep(500)
    OP_43(0x10, 0x0, 0x0, 0x9)

    ChrTalk(    #89 op#A
        0x10,
        "#613F#5P#25AOh...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x14, 0x0)
    Sleep(300)

    def lambda_2FC4():
        OP_6D(-122700, 0, 70040, 1500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2FC4)
    WaitChrThread(0x10, 0x0)
    Sleep(500)

    ChrTalk(    #90
        0x10,
        (
            "#618F#5P*sigh* Oh, Anelace...\x02\x03",

            "#615F...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(300)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #91
        0x10,
        (
            "#617F#11PHeehee... What a day.\x02\x03",

            "I feel almost ashamed to be this relieved\x01",
            "over all of this...\x02\x03",

            "#618F*sigh* I don't know if I'll ever be able to\x01",
            "manage without her at my side...\x02",
        )
    )

    CloseMessageWindow()
    OP_C4(0x1, 0x20000000)

    def lambda_30F8():
        OP_6B(2350, 3000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_30F8)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_F7(0x9, 0x9, 0x0)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(350, 400, -1, -1)
    SetChrName("")

    AnonymousTalk(    #92
        "\x07\x00Side Story [Like a Mother] finished!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    OP_D6(0x1)
    OP_E3(0x1, 0x0)
    OP_C2(0x1, 0x0)
    Call(6, 25)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xB, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_323D")
    Sleep(1000)
    OP_28(0xB, 0x4, 0x10)
    OP_28(0xB, 0x4, 0x20)
    OP_3E(0x1EF, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #93
        "\x07\x05Received \x1F\xEF\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31FC")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x44)"), scpexpr(EXPR_END)), "loc_31D4")
    Jump("loc_31FC")

    label("loc_31D4")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #94
        "\x07\x05Learned the recipe for \x1F\xEF\x01\x07\x05.\x02",
    )

    CloseMessageWindow()

    label("loc_31FC")

    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(50000)
    AddMira(50000)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #95
        "\x07\x05Received \x07\x02100,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_323D")

    OP_A2(0x2506)
    NewScene("ED6_DT21/U2512   ._SN", 109, 0, 0)
    IdleLoop()
    Return()

    # Function_8_99C end

    def Function_9_324A(): pass

    label("Function_9_324A")

    SetChrSubChip(0x10, 0)
    Sleep(1000)
    SetChrSubChip(0x10, 1)
    Return()

    # Function_9_324A end

    SaveToFile()

Try(main)
