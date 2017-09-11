from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R1403   ._SN',
        MapName             = 'Bose',
        Location            = 'R1403.x',
        MapIndex            = 58,
        MapDefaultBGM       = "ed60086",
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
        'Kyle',                                 # 9
        'Josette',                              # 10
        'Sky Bandit Aaron',                     # 11
        'Sky Bandit Lonnie',                    # 12
        'Sky Bandit Dino',                      # 13
        'Sky Bandit Lyall',                     # 14
        'Sky Bandit Rosco',                     # 15
        'Sky Bandit Ryan',                      # 16
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
        Unknown_3A              = 58,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02120 ._CH',             # 00
        'ED6_DT07/CH02130 ._CH',             # 01
        'ED6_DT07/CH01380 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02120P._CP',             # 00
        'ED6_DT07/CH02130P._CP',             # 01
        'ED6_DT07/CH01380P._CP',             # 02
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x141,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 26500,
        Z                   = 0,
        Y                   = 12600,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x141,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 800,
        Z                   = 500,
        Y                   = 500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -500,
        Z                   = 500,
        Y                   = 900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3200,
        Z                   = 500,
        Y                   = -700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2300,
        Z                   = 500,
        Y                   = -2700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1000,
        Z                   = 500,
        Y                   = -2800,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1000,
        Z                   = 500,
        Y                   = -1900,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1C2",          # 00, 0
        "Function_1_1ED",          # 01, 1
        "Function_2_200",          # 02, 2
        "Function_3_216",          # 03, 3
        "Function_4_1441",         # 04, 4
    )


    def Function_0_1C2(): pass

    label("Function_0_1C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_1DE")
    OP_A3(0x3FB)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)

    label("loc_1DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1EC")
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_1EC")

    Return()

    # Function_0_1C2 end

    def Function_1_1ED(): pass

    label("Function_1_1ED")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x3001E)
    Return()

    # Function_1_1ED end

    def Function_2_200(): pass

    label("Function_2_200")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_215")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_200")

    label("loc_215")

    Return()

    # Function_2_200 end

    def Function_3_216(): pass

    label("Function_3_216")

    AddParty(0x3, 0xFF)
    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(12760, -10, 9570, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(4600, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x64)
    SetChrPos(0x101, 6340, -210, -12440, 315)
    SetChrPos(0x102, 7380, -380, -12200, 315)
    SetChrPos(0x103, 5970, -290, -13400, 315)
    SetChrPos(0x104, 12230, 1020, -21130, 319)
    OP_8B(0xA, 0xFFFFFBB4, 0xFFFFFD30, 0x0)
    OP_8B(0xB, 0xFFFFFBB4, 0xFFFFFD30, 0x0)
    OP_8B(0xC, 0xFFFFFBB4, 0xFFFFFD30, 0x0)
    OP_8B(0xD, 0xFFFFFBB4, 0xFFFFFD30, 0x0)
    OP_8B(0xE, 0xFFFFFBB4, 0xFFFFFD30, 0x0)
    OP_8B(0xF, 0xFFFFFBB4, 0xFFFFFD30, 0x0)
    FadeToBright(2000, 0)
    OP_6D(1960, -10, 2560, 5000)
    Fade(1000)
    OP_6D(3800, 120, -9560, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #0
        0x103,
        (
            "#020F#5PSo they're parked in front of the\x01",
            "Amberl Tower, huh?\x02\x03",

            "This is definitely the perfect place to\x01",
            "land since it's off the main road.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xF, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D6")

    ChrTalk(    #1
        0x101,
        (
            "#002F#5PIsn't the Amberl Tower supposed to\x01",
            "be just like the Esmelas Tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#012F#2PYes. It's one of the ancient ruins\x01",
            "referred to as a tetracyclic tower.\x02\x03",

            "So what do you want to do, Schera?\x01",
            "Should we subdue them?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51D")

    label("loc_4D6")


    ChrTalk(    #3
        0x102,
        (
            "#012F#2PSo what do you want to do, Schera?\x01",
            "Should we subdue them?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51D")


    ChrTalk(    #4
        0x103,
        (
            "#522F#5PHmm...that's one way to go about\x01",
            "things...\x02\x03",

            "But there's more than double their\x01",
            "number since the last time we\x01",
            "encountered them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#006F#5PDon't worry. Even with twice as many\x01",
            "guys they're no match for us.\x02\x03",

            "So how about we take them all\x01",
            "on at once...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #6
        0x104,
        "Man's Voice",
        (
            "#1PHmm...I don't know if that's the best\x01",
            "way to go about things.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_67E():
        OP_6D(6810, -410, -12820, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_67E)

    def lambda_696():

        label("loc_696")

        TurnDirection(0xFE, 0x104, 400)
        OP_48()
        Jump("loc_696")

    QueueWorkItem2(0x101, 1, lambda_696)

    def lambda_6A7():

        label("loc_6A7")

        TurnDirection(0xFE, 0x104, 400)
        OP_48()
        Jump("loc_6A7")

    QueueWorkItem2(0x102, 1, lambda_6A7)

    def lambda_6B8():

        label("loc_6B8")

        TurnDirection(0xFE, 0x104, 400)
        OP_48()
        Jump("loc_6B8")

    QueueWorkItem2(0x103, 1, lambda_6B8)
    SetChrFlags(0x104, 0x4)
    OP_8E(0x104, 0x2850, 0x398, 0xFFFFB5F0, 0x1388, 0x0)
    OP_96(0x104, 0x23E6, 0xFFFFFF92, 0xFFFFC068, 0x3E8, 0x1388)
    ClearChrFlags(0x104, 0x4)
    OP_8E(0x104, 0x1D24, 0xFFFFFE0C, 0xFFFFC8CE, 0x1388, 0x0)
    OP_8C(0x104, 315, 400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #7
        0x104,
        "#031FSorry to keep you all waiting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#004F#3S#6PO-Oli...!\x02",
    )

    CloseMessageWindow()
    OP_44(0x102, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)

    ChrTalk(    #9
        0x102,
        (
            "#012FKeep it down...or they're going\x01",
            "to hear you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#002F#6P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    TurnDirection(0x102, 0x104, 0)

    ChrTalk(    #11
        0x103,
        (
            "#023FWell, isn't this a surprise...\x02\x03",

            "I can't believe you're standing here\x01",
            "after the state you were in before.\x01",
            "Your tolerance is...impressive.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(    #12
        0x104,
        (
            "#035FHeh. Who do you think you're talking to?\x02\x03",

            "Rather than miss a minute of your fair company,\x01",
            "I dutifully puked my guts up and dumped a bucket of\x01",
            "cold water over my head. Voila, I was good to go.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #13
        0x101,
        (
            "#007F#6PI dunno about that... I think I hear your\x01",
            "liver screaming somewhere in there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x102,
        "#018FThat's some serious tenacity...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x104,
        (
            "#031FCome on, I couldn't let you enjoy all\x01",
            "the fun yourselves, right?\x02\x03",

            "I had just come out of the inn when I saw\x01",
            "you guys hit the road, so I came running\x01",
            "from behind to catch up with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x103,
        (
            "#025FI guess I went a little too easy\x01",
            "on you...\x02\x03",

            "Maybe I should have had you down\x01",
            "all that brandy at once.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #17
        0x104,
        (
            "#034FYou'd have put me to sleep for good\x01",
            "if you'd done that, Schera...\x02\x03",

            "#030FBut anyway...\x02\x03",

            "Fighting the sky bandits here would\x01",
            "lack finesse, don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        "#009F#6PI don't think that's the issue here!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x104,
        (
            "#032FNo, I'm serious.\x02\x03",

            "Even if you subdued them all and managed\x01",
            "to arrest the two siblings...\x02\x03",

            "There's still a chance they won't\x01",
            "tell you where their hideout is.\x02\x03",

            "And they might even use the hostages\x01",
            "as leverage to demand their release.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x103,
        (
            "#022FWell, there's a risk involved with\x01",
            "whatever course of action we\x01",
            "take...\x02\x03",

            "...or do you have a good plan on how\x01",
            "we can avoid taking such a risk?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x104,
        (
            "#031FHa! Boy, do I ever.\x01",
            "Listen up, everyone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#509F#6POkay...\x02\x03",

            "But if you blow in my ear, I'm\x01",
            "seriously going to punch your\x01",
            "lights out.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrPos(0x8, -340, -40, -16430, 0)
    SetChrPos(0x9, 700, -10, -16580, 0)
    OP_6D(-1120, 520, -1770, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3730, 0)
    OP_6C(224000, 0)
    OP_6E(261, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_F84():
        OP_8E(0xFE, 0xFFFFFAA6, 0x10E, 0xFFFFEC32, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_F84)

    def lambda_F9F():

        label("loc_F9F")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_F9F")

    QueueWorkItem2(0xA, 1, lambda_F9F)

    def lambda_FB0():

        label("loc_FB0")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FB0")

    QueueWorkItem2(0xB, 1, lambda_FB0)

    def lambda_FC1():

        label("loc_FC1")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FC1")

    QueueWorkItem2(0xC, 1, lambda_FC1)

    def lambda_FD2():

        label("loc_FD2")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FD2")

    QueueWorkItem2(0xD, 1, lambda_FD2)

    def lambda_FE3():

        label("loc_FE3")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FE3")

    QueueWorkItem2(0xE, 1, lambda_FE3)

    def lambda_FF4():

        label("loc_FF4")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FF4")

    QueueWorkItem2(0xF, 1, lambda_FF4)
    Sleep(800)

    def lambda_100A():
        OP_8E(0xFE, 0xFFFFFE0C, 0x96, 0xFFFFE976, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_100A)
    OP_6D(-1870, 520, -4370, 3000)

    ChrTalk(    #23
        0xA,
        "Kyle, Josette!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xB,
        (
            "It's good to see you made it back!\x01",
            "I didn't think you'd be gone so long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xC,
        (
            "#2PSo talks took longer than expected,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "#200F#3PYeah...but we're nearing an end\x01",
            "with our negotiations.\x02\x03",

            "We also managed to get a great\x01",
            "deal of information about what's\x01",
            "going on with the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xD,
        "#2PSo what you're saying is...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x9,
        (
            "#210F#3PYep, we'll be getting the ransom\x01",
            "money within a few days.\x02\x03",

            "We'll finally be one step closer to\x01",
            "making our dream a reality.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(    #29
        0xE,
        "#2PWe did it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xF,
        "#2PSweet!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#200F#3PCool it down, guys. It's a little too\x01",
            "early to be getting excited yet.\x02\x03",

            "For the moment, we need to get back\x01",
            "to the hideout and report to Don.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x9,
        (
            "#211F#3PAll right, everyone! Pack up and\x01",
            "let's get out of here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33 op#A
        0xA,
        "#5A#3P#1KRoger that!\x02",
    )


    ChrTalk(    #34 op#A
        0xB,
        "#5A#4P#1KRoger that!\x02",
    )


    ChrTalk(    #35 op#A
        0xC,
        "#5A#2P#1KRoger that!\x02",
    )


    ChrTalk(    #36 op#A
        0xD,
        "#5A#2P#1KRoger that!\x02",
    )


    ChrTalk(    #37 op#A
        0xE,
        "#5A#1P#1KRoger that!\x02",
    )


    ChrTalk(    #38 op#A
        0xF,
        "#5A#3P#1KRoger that!\x02",
    )

    OP_56(0x1)
    OP_59()
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    Sleep(1000)
    NewScene("ED6_DT01/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_216 end

    def Function_4_1441(): pass

    label("Function_4_1441")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6D(16867, 6300, -3100, 0)
    OP_6B(4400, 0)
    OP_67(0, 2500, -10000, 0)
    OP_6C(324000, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x2710)

    def lambda_14B8():
        OP_6D(14820, 6300, -3700, 15000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14B8)

    def lambda_14D0():
        OP_6B(5500, 15000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14D0)

    def lambda_14E0():
        OP_6C(135000, 15000)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_14E0)

    def lambda_14F0():
        OP_67(0, 10600, -10000, 15000)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_14F0)
    OP_22(0x79, 0x0, 0x64)
    Sleep(6500)
    OP_22(0xCD, 0x0, 0x64)
    Sleep(8500)
    OP_A2(0x3FB)
    SetMapFlags(0x2000000)
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT01/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_1441 end

    SaveToFile()

Try(main)
