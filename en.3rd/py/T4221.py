from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4221   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4221.x',
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
        'Prince Olivert',                       # 9
        'Major Vander',                         # 10
        'Chancellor Osborne',                   # 11
        'Pot',                                  # 12
        'Tea',                                  # 13
        'Tea',                                  # 14
        'Target Camera',                        # 15
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
        'ED6_DT27/CH03260 ._CH',             # 00
        'ED6_DT27/CH03570 ._CH',             # 01
        'ED6_DT27/CH03950 ._CH',             # 02
        'ED6_DT27/CH03263 ._CH',             # 03
        'ED6_DT26/CH20804 ._CH',             # 04
        'ED6_DT06/CH20020 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT27/CH03260P._CP',             # 00
        'ED6_DT27/CH03570P._CP',             # 01
        'ED6_DT27/CH03950P._CP',             # 02
        'ED6_DT27/CH03263P._CP',             # 03
        'ED6_DT26/CH20804P._CP',             # 04
        'ED6_DT06/CH20020P._CP',             # 05
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
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
        Unknown3            = 1703941,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638405,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
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
        "Function_0_1BA",          # 00, 0
        "Function_1_202",          # 01, 1
        "Function_2_20C",          # 02, 2
        "Function_3_1B1B",         # 03, 3
        "Function_4_3106",         # 04, 4
    )


    def Function_0_1BA(): pass

    label("Function_0_1BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_201")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_1E5")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_201")

    label("loc_1E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_201")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_201")

    Return()

    # Function_0_1BA end

    def Function_1_202(): pass

    label("Function_1_202")

    OP_B1("t4221_n")
    Return()

    # Function_1_202 end

    def Function_2_20C(): pass

    label("Function_2_20C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 67000, 0, 7200, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, 28000, 250, 53040, 90)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 30820, 300, 52900, 270)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x13, 29500, 300, 52600, 0)
    SetChrPos(0x14, 29900, 300, 53140, 0)
    SetChrPos(0x15, 28900, 300, 53140, 0)
    OP_6D(84260, 0, 8440, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(280, 0)

    def lambda_311():
        OP_6D(68220, 0, 8440, 8000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_311)

    def lambda_329():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_329)

    def lambda_339():
        OP_6B(2800, 8000)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_339)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x16, 0x0)
    Sleep(500)

    def lambda_35D():
        OP_6D(67820, 0, 18440, 6000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_35D)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0x16, 0xFF)
    OP_6D(37490, 0, 59950, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_3C1():
        OP_6D(31190, 0, 54740, 5000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_3C1)

    def lambda_3D9():
        OP_67(0, 5160, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3D9)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x16, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x12,
        (
            "#1485F#11PAhh...\x02\x03",

            "It's obvious that Her Majesty is quite the tea \x01",
            "fancier, if this blend is anything to go by.\x02\x03",

            "The fragrance, the temperature, the taste...\x01",
            "I'd be hard-pressed to find fault with any of it.\x02\x03",

            "#1480FI've always been more of a coffee man myself,\x01",
            "but I have no doubt that I'd be content with a\x01",
            "cup of this at my desk each morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "#1551F#6P...As much as I agree with you, I don't believe\x01",
            "we're here to talk about beverages.\x02\x03",

            "#1542FSo, shall we get right to the point? What did you\x01",
            "want to discuss with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x12,
        (
            "#1485F#11PHaha...\x02\x03",

            "#1481FI see your sojourn in Liberl has proven most\x01",
            "fruitful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        "#1543F#6P...Pardon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x12,
        (
            "#1480F#11PWhen we last spoke, you struck me as a bright,\x01",
            "flexible young man...\x02\x03",

            "...and no doubt, you still are. But now, I see\x01",
            "in you a resilient inner strength girding those\x01",
            "aspects.\x02\x03",

            "#1485FI'm sure His Majesty will be most delighted with\x01",
            "your personal development.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        (
            "#1545F#6PHeh. Meanwhile, I see you're the same fearless\x01",
            "man I've always known you to be.\x02\x03",

            "#1540FMore so, even. That crushing aura about you\x01",
            "seems to have only grown with time.\x02\x03",

            "#1541FIt's as if you feed on the resentment of those\x01",
            "who live in the territories you annex.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x12,
        (
            "#1481F#11PHaha. Such harsh words, Your Highness.\x02\x03",

            "#1485FPersonally, I prefer the term 'political unification.' \x01",
            "'Annex' can carry such...negative connotations,\x01",
            "you know.\x02\x03",

            "Since the end of the Hundred Days War, our army\x01",
            "hasn't committed a single act of aggression.\x01",
            "All our unifications have been entirely peaceful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10,
        (
            "#1545F#6POh, you're quite right about that.\x02\x03",

            "#1540F...On the surface.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x12,
        "#1483F#11POh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#1544F#6PIt's amazing how similar the annexation process\x01",
            "is every single time it happens.\x02\x03",

            "#1542FIt starts with a small nation or independent state\x01",
            "with an array of problems beyond repair.\x02\x03",

            "Those problems start to worsen, after which\x01",
            "jaegers and other dangerous elements enter,\x01",
            "plunging public order to an all-time low...\x02\x03",

            "#1551FDesperate for a solution, the local government\x01",
            "requests the help of the Imperial Army.\x01",
            "Before they know it, they're part of the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x12,
        (
            "#1480F#11PWell, it's not as though I can deny what you're\x01",
            "saying. Each instance does share certain\x01",
            "commonalities.\x02\x03",

            "#1485FStill, it's to be expected--an inevitable\x01",
            "consequence of the age of unchecked growth\x01",
            "and progress in which we live.\x02\x03",

            "The Imperial Army is simply acting in the Empire's\x01",
            "best interests, helping to stabilize our neighbors\x01",
            "for the good of the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "#1540F#6PAnd it's understandable that they would.\x02\x03",

            "#1541FI do find myself rather curious why Intelligence\x01",
            "Division members are going to such nations with\x01",
            "such peculiar frequency...\x02\x03",

            "Well before the problems I described worsen, \x01",
            "no less.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x12,
        (
            "#1485F#11PHaha. I won't press as to where you came by\x01",
            "such information, as curious as I am...\x02\x03",

            "#1481F...but I will say this: at its most basic level,\x01",
            "these actions are about risk management.\x02\x03",

            "It's because we've been acting to minimize such\x01",
            "risks beforehand that the army has been able to\x01",
            "successfully quell each problem in turn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#1544F#6PWith the small price of earning the disdain of \x01",
            "the people in those nations and an increased\x01",
            "risk of terrorism in exchange.\x02\x03",

            "#1542FTo tell you the truth, I'm rather astounded that\x01",
            "you had the courage to come here to Liberl all\x01",
            "on your own to begin with.\x02\x03",

            "After all, you've earned yourself the biggest\x01",
            "target for terrorists in all of Erebonia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x12,
        (
            "#1485F#11PHaha. Your concern is touching, Your Highness.\x02\x03",

            "#1480FI would ask that you not trouble yourself with\x01",
            "my safety.\x02\x03",

            "I employ some very skilled subordinates tasked\x01",
            "primarily with eliminating the risk of terrorist\x01",
            "attacks against me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#1543F#6PReally, now?\x02\x01",

            "#1542FThat Lechter is one of those, I assume?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x12,
        (
            "#1485F#11PHaha. A rather peculiar fellow, isn't he? But\x01",
            "a very useful one all the same.\x02\x03",

            "Working out the scheduling for this trip and\x01",
            "taking all the necessary precautions to ward\x01",
            "off terrorist threats were both his doing.\x02\x03",

            "#1480FAnd thanks to his commendable efforts, I can\x01",
            "depart for Crossbell free from worries as soon\x01",
            "as I've finished my business here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #17
        0x10,
        "#1543F#6P#3SCrossbell?!\x02",
    )

    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #18
        0x12,
        (
            "#1480F#11PAre you surprised? I'll be participating in a top-\x01",
            "secret discussion with a representative of the\x01",
            "Crossbell government.\x02\x03",

            "Recently, a large amount of funding has been\x01",
            "flowing into the country through Republican\x01",
            "channels, putting our allies on the defensive.\x02\x03",

            "#1485FI'd always meant to visit at some point, and this\x01",
            "seemed the perfect opportunity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#1550F#6PA-Are you out of your mind?!\x02\x03",

            "#1544FCrossbell is full of enemies and different factions\x01",
            "at each other's throats!\x02\x03",

            "I hear it's now even a hotbed for terrorists and\x01",
            "criminal organizations because of its position as\x01",
            "a buffer state...\x02\x03",

            "#1542FDoes that really sound like a place the Erebonian\x01",
            "chancellor should be going even on an unofficial\x01",
            "visit?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x12,
        (
            "#1481F#11PI'm surprised to hear you advocating caution in\x01",
            "the face of potential danger, Your Highness.\x02\x03",

            "After all, it was you who flew onto an ancient city--\x01",
            "at great risk to your own safety--and returned\x01",
            "unharmed after surveying it.\x02\x03",

            "#1485FCompared to such rousing risk-taking, my visit to\x01",
            "Crossbell will be child's play. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "#1542F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x12,
        (
            "#1480F#11PAs I'm sure you're aware, you're regarded as\x01",
            "something of a hero back in Erebonia now.\x02\x03",

            "Ah, to see a hero make a grand return befitting\x01",
            "his newly-minted legend...and aboard the famous\x01",
            "Arseille, no less.\x02\x03",

            "Naturally, our hero has also taken the time to\x01",
            "ensure that every well-known newspaper and\x01",
            "magazine are aware of his homecoming, too...\x02\x03",

            "#1485FOh, I have no doubts that your triumphant arrival\x01",
            "will be every bit as glorious as it has played out\x01",
            "in your imaginings, Your Highness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        "#1549F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x12,
        (
            "#1485F#11PHaha. Do be sure to capitalize on this chance as\x01",
            "best you can to build yourself a firm foothold.\x02\x03",

            "#1481FI expect great things from you, after all.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1AF4():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1AF4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_20C end

    def Function_3_1B1B(): pass

    label("Function_3_1B1B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 67000, 0, 7200, 180)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x4)
    SetChrPos(0x10, 28000, 250, 53040, 90)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, 30820, 300, 52900, 270)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x13, 29500, 300, 52600, 0)
    SetChrPos(0x14, 29900, 300, 53140, 0)
    SetChrPos(0x15, 28900, 300, 53140, 0)
    OP_6D(31190, 0, 54740, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_1C20():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1C20)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x16, 0x0)
    Sleep(500)

    ChrTalk(    #25
        0x10,
        (
            "#1542F#6PDo you, now?\x02\x03",

            "#1545FHaha. I have to admit, I never imagined that\x01",
            "would be the case.\x02\x03",

            "#1540FOn the contrary, I was expecting you to tell\x01",
            "me to back off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x12,
        (
            "#1483F#11POh, Aidios forbid. What reason would I have to\x01",
            "suggest such a thing?\x02\x03",

            "#1481FAfter all, at the end of the day, our positions are\x01",
            "functionally the same.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x10,
        "#1543F#6PI'm not sure I understand.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetChrPos(0x12, 30820, 300, 53040, 270)
    OP_6D(37270, 0, 54090, 0)
    OP_67(0, 5370, -26010, 0)
    OP_6B(1800, 0)
    OP_6C(82000, 0)
    OP_6E(190, 0)

    def lambda_1E2D():
        OP_6B(1600, 36000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1E2D)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #28
        0x12,
        (
            "#1484F#5PDo you not think so? Personally, I find it\x01",
            "difficult to believe that you would not harbor\x01",
            "some hatred toward Erebonia as it is today.\x02\x03",

            "A grand empire clinging to the glories of a\x01",
            "bygone era--ruled by the nobility and shackled\x01",
            "by meaningless conventions.\x02\x03",

            "#1481FAm I wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "#1542F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x12,
        (
            "#1480F#5PPeople call me the Blood and Iron Chancellor\x01",
            "as though I hold the whole of Erebonia in the\x01",
            "palm of my hand...\x02\x03",

            "...but in reality, my position is far more tenuous.\x02\x03",

            "#1485FI have supporters and allies in the capital,\x01",
            "certainly, but outside its walls, the nobility holds\x01",
            "far more sway than any of them.\x02\x03",

            "And while it IS true I hold a great amount of\x01",
            "power in the form of the Imperial Army, even\x01",
            "then, I only truly command around 70% of it.\x02\x03",

            "The remainder is loyal to the nobility, who also\x01",
            "maintain their own private armies. With those\x01",
            "factored in, my 'advantage' shrinks substantially.\x02\x03",

            "#1481FSo you see, I'm still very much in the midst of\x01",
            "a battle to truly exert control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#1551F#6PWhich is why you're building railways all over the\x01",
            "country to expand your area of influence...\x02\x03",

            "...and you've been annexing new territory to that\x01",
            "same end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x12,
        (
            "#1485F#5PAs I've long thought, you clearly understand me\x01",
            "better than anyone else.\x02\x03",

            "#1482FThat is why I'll say this once again: work with me,\x01",
            "Your Highness.\x02\x03",

            "With your support, our nation will be able to bring\x01",
            "about real reform faster than ever.\x02\x03",

            "The Noble Faction, bloated with its centuries of\x01",
            "decadence, can be stopped before they even have\x01",
            "the chance to unify against us.\x02\x03",

            "#1485FSurely that's what you desire more than anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x10,
        (
            "#1551F#6P...\x02\x03",

            "#1542FLet me just ask a simple question, Chancellor.\x02\x03",

            "What connection do you have with Ouroboros?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x12,
        (
            "#1485F#5PHmm... I'm afraid I'm not quite sure what you're\x01",
            "asking.\x02\x03",

            "#1481FI WILL say this, however: I'm a firm believer in\x01",
            "using every resource at my disposal in the name\x01",
            "of achieving reform.\x02\x03",

            "That's the way I believe in handling politics.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10,
        (
            "#1541F#6PI see... Well, it certainly does seem as though\x01",
            "we would see eye to eye in many ways.\x02\x03",

            "#1540FAnd that's all the more reason why I am afraid\x01",
            "I must refuse your offer.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #36
        0x12,
        "#1483F#5PIs that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "#1551F#6PYes, I find it difficult to like the rotten Noble\x01",
            "Faction that exists in the Empire...\x02\x03",

            "Or...perhaps you're right that 'hate' is the more\x01",
            "appropriate word.\x02\x03",

            "#1542FBut my feelings of fear towards your methods are\x01",
            "far greater than my feelings of hatred towards\x01",
            "the nobles.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x12,
        "#1480F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#1540F#6PWhat you seem to be doing is trying to compel\x01",
            "Erebonians with a delusive utopia--to whip them\x01",
            "into an enthusiastic frenzy.\x02\x03",

            "No doubt by successfully convincing the people,\x01",
            "the old guard will fall into the metaphorical\x01",
            "firestorm created...\x02\x03",

            "#1551F...and yet by then, the gears will have already\x01",
            "begun turning; there will be no satisfying a roused\x01",
            "populace with a thirst for revolution.\x02\x03",

            "The storm will just keep growing larger and more\x01",
            "ravenous, engulfing anything and everything in its\x01",
            "wake...\x02\x03",

            "#1542FYou know this, don't you, Chancellor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x12,
        (
            "#1486F#5PBut of course!\x02\x03",

            "#1481FAfter all, that's what I intend to happen.\x01",
            "It's the first stage of my reforms.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #41
        0x10,
        "#1549F#6P...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_44(0x16, 0xFF)
    OP_6D(31190, 0, 54740, 0)
    OP_67(0, 5160, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x12, 30820, 300, 52900, 270)
    OP_0D()
    Sleep(500)

    ChrTalk(    #42
        0x12,
        (
            "#1485F#11PI'd be more than happy to share further details\x01",
            "with you if you were to decide to work with me, \x01",
            "Your Highness.\x02\x03",

            "#1480FIn the meantime, I wish you well in strengthening\x01",
            "your foothold back in the Empire.\x02\x03",

            "Of course, if that's your intention, you'll find\x01",
            "it a necessity to work with those nobles you so\x01",
            "despise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#1545F#6PHeh. You truly do see through everything,\x01",
            "don't you?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_43(0x10, 0x3, 0x0, 0x4)
    Sleep(1200)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x12, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x12,
        (
            "#1485F#11PWell, that sounds like the noon bell. The airship\x01",
            "should be arriving shortly.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    SetChrPos(0x12, 30540, 0, 52900, 270)
    SetChrChipByIndex(0x12, 2)
    SetChrSubChip(0x12, 0)
    OP_0D()
    Sleep(500)

    def lambda_2D80():
        OP_6D(31500, 0, 54300, 1500)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2D80)

    def lambda_2D98():
        OP_8E(0xFE, 0x774C, 0x0, 0xC8C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2D98)
    SetChrSubChip(0x10, 2)
    WaitChrThread(0x12, 0x1)
    OP_8C(0x12, 270, 400)
    Sleep(500)

    ChrTalk(    #45
        0x12,
        (
            "#1480F#11PWhich means it's time for me to take my leave,\x01",
            "I'm afraid.\x02\x03",

            "#1485FI look forward to seeing you again in the capital\x01",
            "in two weeks' time.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_8C(0x12, 90, 400)

    def lambda_2E6C():
        OP_6D(34750, 0, 54160, 3000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2E6C)

    def lambda_2E84():
        OP_6B(3200, 3000)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2E84)

    def lambda_2E94():
        OP_8E(0xFE, 0x8818, 0x0, 0xC800, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2E94)
    Sleep(800)
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x12, 0x1)

    def lambda_2ECB():
        OP_8E(0xFE, 0x87F0, 0x0, 0xC418, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2ECB)
    WaitChrThread(0x12, 0x1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_2EF5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2EF5)

    def lambda_2F07():
        OP_8E(0xFE, 0x87F0, 0x0, 0xBD74, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2F07)
    WaitChrThread(0x12, 0x1)
    SetChrFlags(0x12, 0x80)
    OP_22(0x7, 0x0, 0x64)
    Sleep(2000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, 34800, 0, 48500, 0)

    def lambda_2F5C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2F5C)

    def lambda_2F6E():
        OP_8E(0xFE, 0x8746, 0x0, 0xC62A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2F6E)
    WaitChrThread(0x11, 0x1)

    def lambda_2F8E():
        OP_6D(30890, 0, 55120, 4000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_2F8E)

    def lambda_2FA6():
        OP_8E(0xFE, 0x7CE2, 0x0, 0xD41C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2FA6)
    WaitChrThread(0x11, 0x1)

    def lambda_2FC6():
        OP_8E(0xFE, 0x774C, 0x0, 0xD41C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2FC6)
    WaitChrThread(0x11, 0x1)
    TurnDirection(0x11, 0x10, 400)
    OP_63(0x10)
    Sleep(500)
    WaitChrThread(0x16, 0x0)

    ChrTalk(    #46
        0x11,
        (
            "#276F#5PI take it the discussion is over, then?\x02\x03",

            "#270FWhat's wrong? You look awfully tired...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10,
        "#1544F#6POh, nothing...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x10, 0)
    Sleep(500)

    ChrTalk(    #48
        0x10,
        (
            "#1540F#6PI'm just feeling awed anew at what a monster\x01",
            "I decided to pick a fight with.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30E4():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_30E4)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/T4201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_1B1B end

    def Function_4_3106(): pass

    label("Function_4_3106")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_311C")
    OP_22(0xB5, 0x0, 0x5A)
    Sleep(2500)
    Jump("Function_4_3106")

    label("loc_311C")

    Return()

    # Function_4_3106 end

    SaveToFile()

Try(main)
