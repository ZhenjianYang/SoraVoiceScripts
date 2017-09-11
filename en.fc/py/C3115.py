from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3115   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3115.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        'Captain Amalthea',                     # 9
        '2nd Lieutenant Lorence',               # 10
        'Colonel Richard',                      # 11
        'Major Cid',                            # 12
        'Professor Russell',                    # 13
        'Black Orbment',                        # 14
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
        'ED6_DT07/CH02450 ._CH',             # 00
        'ED6_DT07/CH02100 ._CH',             # 01
        'ED6_DT07/CH02200 ._CH',             # 02
        'ED6_DT07/CH02030 ._CH',             # 03
        'ED6_DT07/CH02020 ._CH',             # 04
        'ED6_DT06/CH20021 ._CH',             # 05
        'ED6_DT06/CH20141 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT07/CH02450P._CP',             # 00
        'ED6_DT07/CH02100P._CP',             # 01
        'ED6_DT07/CH02200P._CP',             # 02
        'ED6_DT07/CH02030P._CP',             # 03
        'ED6_DT07/CH02020P._CP',             # 04
        'ED6_DT06/CH20021P._CP',             # 05
        'ED6_DT06/CH20141P._CP',             # 06
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
        Direction           = 180,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 917509,
        ChipIndex           = 0x5,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1D0",          # 01, 1
        "Function_2_1E9",          # 02, 2
        "Function_3_13C6",         # 03, 3
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1B0")
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_1B0")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1BC"),
        (SWITCH_DEFAULT, "loc_1CF"),
    )


    label("loc_1BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CC")
    Event(0, 3)

    label("loc_1CC")

    Jump("loc_1CF")

    label("loc_1CF")

    Return()

    # Function_0_1A2 end

    def Function_1_1D0(): pass

    label("Function_1_1D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 3)), scpexpr(EXPR_END)), "loc_1DC")
    OP_22(0xAC, 0x1, 0x46)

    label("loc_1DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 1)), scpexpr(EXPR_END)), "loc_1E8")
    OP_71(0x0, 0x4)

    label("loc_1E8")

    Return()

    # Function_1_1D0 end

    def Function_2_1E9(): pass

    label("Function_2_1E9")

    EventBegin(0x0)
    OP_6D(-6060, 0, 3830, 0)
    OP_67(0, 5730, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrFlags(0x107, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xC, 3670, 0, 4750, 180)
    SetChrPos(0xA, 3550, 0, 2260, 0)
    SetChrPos(0x8, 2710, 0, 1010, 0)
    SetChrPos(0xB, 4000, 0, 770, 0)
    SetChrPos(0xD, 3520, 800, 2960, 0)
    ClearChrFlags(0xD, 0x80)
    OP_6D(4650, 0, 3040, 4000)

    ChrTalk(    #0
        0xA,
        (
            "#111FI really can't thank you\x01",
            "enough, Professor Russell.\x02\x03",

            "Your work on finding a means\x01",
            "of controlling this 'Gospel'\x01",
            "is of great help.\x02\x03",

            "On behalf of the Intelligence\x01",
            "Division, I extend my deepest\x01",
            "gratitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xC,
        (
            "#102FHmph... I should have known that\x01",
            "you were behind all of this.\x02\x03",

            "Colonel Richard...\x01",
            "Chief of Intelligence...\x02\x03",

            "Hard to believe you once\x01",
            "served under Cassius...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xA,
        (
            "#113FAh, yes. You and he were friends,\x01",
            "if my memory serves me correctly.\x02\x03",

            "#110FWe've been looking for him,\x01",
            "actually, although we've yet to\x01",
            "pin down his exact location.\x02\x03",

            "If you have some idea of where\x01",
            "to base a search, we'd be happy\x01",
            "to have that information.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xC,
        (
            "#104FI don't know. Not that I'd\x01",
            "tell you if I did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        (
            "#115FHa ha...\x01",
            "Well, no matter.\x02\x03",

            "If, perchance, the Gospel were to have been\x01",
            "delivered into his hands, then I'm afraid it\x01",
            "would have presented a problem.\x02\x03",

            "However, even if he were to show\x01",
            "his face now, he would have no\x01",
            "means of stopping this current.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xC,
        (
            "#102FThe Black Orbment...or the\x01",
            "'Gospel,' as you call it...\x02\x03",

            "I just want to know what\x01",
            "you plan to do with it.\x02\x03",

            "Scratch that... First and foremost,\x01",
            "I want to know where you even\x01",
            "acquired something that bizarre.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        (
            "#111FI imagine my source would rather their identity\x01",
            "be kept a secret.\x02\x03",

            "Our intentions...well, they will\x01",
            "become evident, very soon.\x02\x03",

            "At that time, Professor, we'll\x01",
            "be happy to release you.\x01",
            "All I ask is that you wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xC,
        (
            "#102FAnd you're going to just let a \x01",
            "witness to your crimes go free...\x02\x03",

            "I assume, then, that you intend to\x01",
            "do something on a grand scale.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xA,
        (
            "#111FHa ha... I'll leave the particulars\x01",
            "up to your fertile imagination.\x02\x03",

            "That said, come the dawn when\x01",
            "everything is realized, you\x01",
            "will assist in our research.\x02\x03",

            "This invention will bring\x01",
            "Liberl riches like none\x01",
            "ever before seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xC,
        "#104FNot interested.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#188F#2PPlease, Professor, allow\x01",
            "him to finish before you\x01",
            "give your answer.\x02\x03",

            "It would truly be a pity if 'she'\x01",
            "were to come into some peril,\x01",
            "and you were unable to help her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xC,
        (
            "#105FY-You... You'd threaten her\x01",
            "to get to me...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(    #12
        0xA,
        (
            "#115FTut-tut, Captain Amalthea.\x02\x03",

            "It looks like your renowned\x01",
            "powers of persuasion are not\x01",
            "as elegant as they once were.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(    #13
        0x8,
        (
            "#182F#2PHa ha ha...\x01",
            "Pardon me, then.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B61():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B61)
    TurnDirection(0xA, 0xC, 400)

    ChrTalk(    #14
        0xA,
        (
            "#110FOne might say that she has\x01",
            "a unique sense of humor.\x02\x03",

            "I don't want any misunderstandings\x01",
            "between us, but you must understand\x01",
            "that we are only soldiers.\x02\x03",

            "You have my word that no civilians\x01",
            "will be involved. Save for you,\x01",
            "of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xC,
        (
            "#102FSo you're doing this out of some\x01",
            "twisted sense of patriotism?\x02\x03",

            "Then, this Black Orbment that\x01",
            "can shut down orbal power...\x02\x03",

            "...I see. So that's your plan,\x01",
            "is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        "#112FHmm...?\x02",
    )

    CloseMessageWindow()
    OP_22(0x6A, 0x0, 0x64)
    Sleep(500)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -850, 0, -4650, 0)

    ChrTalk(    #17
        0x9,
        "#1P...Pardon me.\x02",
    )

    CloseMessageWindow()

    def lambda_D59():

        label("loc_D59")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_D59")

    QueueWorkItem2(0xB, 1, lambda_D59)

    def lambda_D6A():

        label("loc_D6A")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_D6A")

    QueueWorkItem2(0xA, 1, lambda_D6A)

    def lambda_D7B():

        label("loc_D7B")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_D7B")

    QueueWorkItem2(0xC, 1, lambda_D7B)

    def lambda_D8C():

        label("loc_D8C")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_D8C")

    QueueWorkItem2(0x8, 1, lambda_D8C)

    def lambda_D9D():
        OP_6D(3120, 0, 2260, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D9D)
    OP_8E(0x9, 0x4E2, 0x0, 0x636, 0xBB8, 0x0)
    TurnDirection(0x9, 0xA, 400)

    ChrTalk(    #18
        0x8,
        (
            "#180FHello, Lieutenant. The colonel\x01",
            "is presently in a meeting.\x02\x03",

            "He wants no interruptions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        (
            "#110FNo, it's all right.\x02\x03",

            "Give me your report, Lieutenant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "#281FThere's been activity in Grancel.\x02\x03",

            "The white wings were caught in the net,\x01",
            "just as you planned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "#188FMy goodness...\x02",
    )

    CloseMessageWindow()
    OP_44(0xA, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(    #22
        0xA,
        (
            "#115FHa ha...\x01",
            "Check and mate.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F26():
        OP_6D(4650, 0, 3040, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F26)
    TurnDirection(0xA, 0xC, 400)

    def lambda_F45():

        label("loc_F45")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_F45")

    QueueWorkItem2(0xB, 1, lambda_F45)

    def lambda_F56():

        label("loc_F56")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_F56")

    QueueWorkItem2(0xC, 1, lambda_F56)

    def lambda_F67():

        label("loc_F67")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_F67")

    QueueWorkItem2(0x8, 1, lambda_F67)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #23
        0xA,
        (
            "#111FNow, Professor. If you'll please\x01",
            "excuse me.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrFlags(0xD, 0x80)
    OP_0D()
    Sleep(500)
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(    #24
        0xA,
        (
            "#110FMajor Cid, see to the professor\x01",
            "and make sure he's comfortable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xB,
        "#703F...Yes, sir.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    OP_8C(0xA, 225, 400)
    OP_8E(0xA, 0x992, 0x0, 0x776, 0x7D0, 0x0)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)

    def lambda_1069():
        OP_8E(0xFE, 0xFFFFF9D4, 0x0, 0xFFFFE52A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1069)
    Sleep(1000)

    def lambda_1089():
        OP_8E(0xFE, 0xFFFFF9D4, 0x0, 0xFFFFE52A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1089)
    Sleep(500)

    def lambda_10A9():
        OP_8E(0xFE, 0xFFFFF9D4, 0x0, 0xFFFFE52A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10A9)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_22(0xE6, 0x0, 0x64)
    Sleep(500)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    TurnDirection(0xB, 0xC, 400)
    Sleep(500)

    def lambda_10F6():
        OP_6D(4430, 0, 4440, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10F6)
    OP_8E(0xB, 0xDDE, 0x0, 0x8D4, 0x7D0, 0x0)
    TurnDirection(0xB, 0xC, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #26
        0xB,
        (
            "#701FIs there anything you need,\x01",
            "Professor?\x02\x03",

            "I'll get you set up with any\x01",
            "of the standard amenities.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 400)

    ChrTalk(    #27
        0xC,
        (
            "#104F#6PHmph. I'm fine.\x02\x03",

            "#102FI used to believe that you were\x01",
            "different from the others...that\x01",
            "you were a good, upstanding man.\x02\x03",

            "Apparently, I greatly overestimated you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xB,
        (
            "#703F...My apologies.\x02\x03",

            "#700FBut you've been abducted by rebels,\x01",
            "you see. Rebels against the queen.\x01",
            "Nameless, unknown rebels.\x02\x03",

            "Stress that fact, and I might even\x01",
            "let you write a letter to your\x01",
            "granddaughter...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #29
        0xC,
        "#105F#3S#6PGet out of my sight!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        "#703F...As you wish.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 225, 400)
    OP_8E(0xB, 0xFFFFFAF6, 0x0, 0xFFFFEBF6, 0xFA0, 0x0)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(500)
    OP_22(0xE6, 0x0, 0x64)
    Sleep(500)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C3107   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1E9 end

    def Function_3_13C6(): pass

    label("Function_3_13C6")

    AddParty(0xA, 0xFF)
    EventBegin(0x0)
    OP_6D(-250, 0, 1940, 0)
    OP_67(0, 6560, -10000, 0)
    OP_6B(3000, 0)
    SetChrPos(0x10B, -310, 0, 3630, 0)
    SetChrPos(0x101, -1040, 0, -6570, 0)
    SetChrPos(0x106, -1040, 0, -6570, 0)
    SetChrPos(0x102, -1040, 0, -6570, 0)
    SetChrPos(0x107, -1040, 0, -6570, 0)
    FadeToBright(1000, 0)

    def lambda_145A():
        OP_8E(0xFE, 0xFFFFFCFE, 0x0, 0x14, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_145A)
    Sleep(400)

    def lambda_147A():
        OP_8E(0xFE, 0xA0, 0x0, 0xFFFFFE0C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_147A)
    Sleep(400)

    def lambda_149A():
        OP_8E(0xFE, 0xFFFFF6E6, 0x0, 0xFFFFFD30, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_149A)
    Sleep(400)

    def lambda_14BA():
        OP_8E(0xFE, 0xFFFFF97A, 0x0, 0xFFFFFA6A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14BA)

    ChrTalk(    #31
        0x10B,
        "#104FSo you're back...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x107, 400)

    ChrTalk(    #32
        0x10B,
        (
            "#105F#3SEnough! I told you,\x01",
            "I don't want anyth--\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #33
        0x107,
        "#560FGr-grandpa...\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10B, 0xFFFFFEF2, 0x0, 0x8D4, 0x5DC, 0x0)

    ChrTalk(    #34
        0x10B,
        (
            "#103F#3PTita?!\x02\x03",

            "I must be dreaming...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x107,
        "#068FGrandpaaaa!\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    def lambda_15DA():
        OP_6D(-250, 0, 2840, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15DA)
    OP_92(0x107, 0x10B, 0x190, 0x1388, 0x0)

    def lambda_1600():
        OP_8F(0x107, 0xFFFFFF88, 0x0, 0x820, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1600)
    SetChrChipByIndex(0x107, 6)
    SetChrSubChip(0x107, 0)
    SetChrFlags(0x107, 0x20)
    OP_94(0x1, 0x10B, 0xB4, 0x12C, 0x7D0, 0x0)

    ChrTalk(    #36
        0x107,
        (
            "#069F#4PThank goodness you're okay...!\x02\x03",

            "*sniffle*... *sniffle*...\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x107, 0xF, 0x0, 0x12C, 0xFA0)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #37
        0x107,
        "#068F#3S#4PWaaaaaahhhhhh!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #38
        0x10B,
        (
            "#100FThis isn't a dream?\x02\x03",

            "And you lot...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#006FHey, Professor. You don't look\x01",
            "like you're feeling so hot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#010FThe factory chief, Murdock,\x01",
            "asked us to come and get you\x01",
            "out of here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10B,
        (
            "#103FI'm impressed... You actually\x01",
            "sneaked in here?\x02\x03",

            "#101FSo much like your father...\x01",
            "Not a lick of common sense\x01",
            "between the two of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x106,
        (
            "#050FHey, old man.\x02\x03",

            "Sorry to interrupt your little\x01",
            "vacation, but we need you to\x01",
            "get ready for a jailbreak.\x02\x03",

            "We don't have a lot of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10B,
        (
            "#102FWho are you?\x02\x03",

            "You look like you came from the wrong\x01",
            "side of the barn; I can tell that, at least.\x01",
            "You have a head like a chicken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x106,
        "#055FA chi--\x02",
    )

    CloseMessageWindow()
    OP_9E(0x106, 0xF, 0x0, 0x12C, 0xFA0)

    ChrTalk(    #45
        0x106,
        "#054F#3SSay that again, you geezer!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#001FHa ha ha!\x01",
            "Nice one, Professor.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x107, 0x20)
    SetChrChipByIndex(0x107, 65535)
    OP_8F(0x107, 0xFFFFFEDE, 0x0, 0x528, 0x7D0, 0x0)
    TurnDirection(0x107, 0x10B, 0)

    ChrTalk(    #47
        0x107,
        (
            "#562FGr-Grandpa... You shouldn't\x01",
            "say mean things like that.\x02\x03",

            "#560FThis is Agate. He's a senior\x01",
            "bracer over Estelle and Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10B,
        (
            "#103FWell, now...\x01",
            "I had no idea.\x02\x03",

            "#101FCome to think of it, I think\x01",
            "I've heard Cassius mention your\x01",
            "name before.\x02\x03",

            "Something about a bad seed who\x01",
            "was always sulking about one\x01",
            "thing or another, I believe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x106,
        (
            "#057FI'm about this far from wringing\x01",
            "your neck, old man!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x106, 400)

    ChrTalk(    #50
        0x102,
        "#019FNow, now, calm down.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x10B, 400)

    ChrTalk(    #51
        0x102,
        (
            "#010FProfessor, we'll have to save the\x01",
            "explanations for later. For now,\x01",
            "we need to get you out of here.\x02\x03",

            "Is there anything you\x01",
            "want to bring with you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1C4A():

        label("loc_1C4A")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C4A")

    QueueWorkItem2(0x101, 2, lambda_1C4A)

    def lambda_1C5B():

        label("loc_1C5B")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C5B")

    QueueWorkItem2(0x107, 2, lambda_1C5B)

    def lambda_1C6C():

        label("loc_1C6C")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C6C")

    QueueWorkItem2(0x106, 2, lambda_1C6C)

    def lambda_1C7D():

        label("loc_1C7D")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_1C7D")

    QueueWorkItem2(0x10B, 2, lambda_1C7D)

    ChrTalk(    #52
        0x10B,
        (
            "#100FHmmm...\x02\x03",

            "Can we carry the Capel unit?\x02\x03",

            "If we leave it behind, I know\x01",
            "that these fools will just\x01",
            "misuse it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        "#010FUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xFFFFFAB0, 0x0, 0x29E, 0xBB8, 0x0)
    OP_8E(0x102, 0xFFFFFE7A, 0x0, 0x15A4, 0xBB8, 0x0)
    Sleep(500)
    OP_71(0x0, 0x4)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #54
        "\x07\x00Obtained \x07\x02Orbal Calculator\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x364, 1)
    OP_8C(0x102, 180, 400)

    def lambda_1DAF():
        OP_6D(-900, 0, 1970, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DAF)
    OP_8E(0x102, 0xFFFFF8D0, 0x0, 0x7ED, 0xBB8, 0x0)
    TurnDirection(0x102, 0x10B, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x107, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x10B, 0xFF)

    def lambda_1DF6():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1DF6)

    def lambda_1E04():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1E04)

    def lambda_1E12():
        TurnDirection(0xFE, 0x10B, 400)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1E12)

    ChrTalk(    #55
        0x10B,
        (
            "#102FI've been using that in my research\x01",
            "to find a means of controlling the\x01",
            "Black Orbment.\x02\x03",

            "I wasn't able to discern its physical\x01",
            "composition, but I did have some\x01",
            "success with the control method.\x02\x03",

            "Which means that these fools will\x01",
            "be able to cause that phenomenon\x01",
            "to reoccur, whenever they want.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#003FOh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x101, 400)

    ChrTalk(    #57
        0x10B,
        (
            "#104FI'm sorry, Estelle and Joshua.\x02\x03",

            "I hate that it's being so grievously\x01",
            "misused, after you went to all the\x01",
            "trouble of bringing it to me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#013FBelieve me, we understand.\x02\x03",

            "With Tita's safety on the line,\x01",
            "I can't imagine any of us would've\x01",
            "done any differently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        (
            "#007FBesides, it's our fault that\x01",
            "you two got caught up in this\x01",
            "to begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x106,
        (
            "#054FFor the love of AIDIOS! We don't\x01",
            "have time for you to give speeches!\x02\x03",

            "If you're all set, then we\x01",
            "have to GO!\x02\x03",

            "Get your asses in gear! Move as\x01",
            "fast as the old man's slipped\x01",
            "disc will let you!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10B, 0x106, 400)

    ChrTalk(    #61
        0x10B,
        (
            "#102FOh, very clever...\x02\x03",

            "I haven't let any young\x01",
            "man beat me yet, and I'm\x01",
            "not about to start now!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(    #62
        0x107,
        "#067F#6PC-Come on, both of you...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x569)
    OP_28(0x44, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_3_13C6 end

    SaveToFile()

Try(main)
