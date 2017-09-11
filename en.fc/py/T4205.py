from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4205   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4205.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Queen Alicia',                         # 9
        '1st Lieutenant Schwarz',               # 10
        'Joshua',                               # 11
        'Olivier',                              # 12
        'Zin',                                  # 13
        '2nd Lieutenant Lorence',               # 14
        'Vision of Lorence',                    # 15
        'Vision of Lorence',                    # 16
        'Vision of Lorence',                    # 17
        'Vision of Lorence',                    # 18
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
        'ED6_DT07/CH02010 ._CH',             # 00
        'ED6_DT07/CH02090 ._CH',             # 01
        'ED6_DT07/CH00010 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00070 ._CH',             # 04
        'ED6_DT07/CH00260 ._CH',             # 05
        'ED6_DT07/CH00262 ._CH',             # 06
        'ED6_DT07/CH00100 ._CH',             # 07
        'ED6_DT07/CH00101 ._CH',             # 08
        'ED6_DT07/CH00120 ._CH',             # 09
        'ED6_DT07/CH00121 ._CH',             # 0A
        'ED6_DT07/CH00140 ._CH',             # 0B
        'ED6_DT07/CH00141 ._CH',             # 0C
        'ED6_DT07/CH02200 ._CH',             # 0D
        'ED6_DT07/CH00264 ._CH',             # 0E
        'ED6_DT07/CH00104 ._CH',             # 0F
        'ED6_DT07/CH00124 ._CH',             # 10
        'ED6_DT07/CH00144 ._CH',             # 11
        'ED6_DT07/CH02460 ._CH',             # 12
        'ED6_DT07/CH02230 ._CH',             # 13
        'ED6_DT07/CH02240 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH02010P._CP',             # 00
        'ED6_DT07/CH02090P._CP',             # 01
        'ED6_DT07/CH00010P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00070P._CP',             # 04
        'ED6_DT07/CH00260P._CP',             # 05
        'ED6_DT07/CH00262P._CP',             # 06
        'ED6_DT07/CH00100P._CP',             # 07
        'ED6_DT07/CH00101P._CP',             # 08
        'ED6_DT07/CH00120P._CP',             # 09
        'ED6_DT07/CH00121P._CP',             # 0A
        'ED6_DT07/CH00140P._CP',             # 0B
        'ED6_DT07/CH00141P._CP',             # 0C
        'ED6_DT07/CH02200P._CP',             # 0D
        'ED6_DT07/CH00264P._CP',             # 0E
        'ED6_DT07/CH00104P._CP',             # 0F
        'ED6_DT07/CH00124P._CP',             # 10
        'ED6_DT07/CH00144P._CP',             # 11
        'ED6_DT07/CH02460P._CP',             # 12
        'ED6_DT07/CH02230P._CP',             # 13
        'ED6_DT07/CH02240P._CP',             # 14
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_301",          # 01, 1
        "Function_2_32E",          # 02, 2
        "Function_3_344",          # 03, 3
        "Function_4_576",          # 04, 4
        "Function_5_3151",         # 05, 5
        "Function_6_31F3",         # 06, 6
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_29E"),
        (SWITCH_DEFAULT, "loc_2B4"),
    )


    label("loc_29E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B1")
    OP_A2(0x666)
    Event(0, 4)

    label("loc_2B1")

    Jump("loc_2B4")

    label("loc_2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DE")
    SetChrChipByIndex(0x0, 18)
    SetChrChipByIndex(0x1, 19)
    SetChrChipByIndex(0x138, 20)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_300")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 2170, 12000, 62700, 0)

    label("loc_300")

    Return()

    # Function_0_292 end

    def Function_1_301(): pass

    label("Function_1_301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 0)), scpexpr(EXPR_END)), "loc_31D")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x4A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 6)
    Jump("loc_32D")

    label("loc_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_32D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_32D")

    Return()

    # Function_1_301 end

    def Function_2_32E(): pass

    label("Function_2_32E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_343")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_32E")

    label("loc_343")

    Return()

    # Function_2_32E end

    def Function_3_344(): pass

    label("Function_3_344")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xDF, 0)), scpexpr(EXPR_END)), "loc_3CC")
    TurnDirection(0x8, 0x102, 0)

    ChrTalk(    #0
        0x8,
        (
            "#090FEstelle...Joshua... I haven't\x01",
            "had such a wonderful day in a\x01",
            "very long time.\x02\x03",

            "You must come again for tea.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_572")

    label("loc_3CC")

    OP_A2(0x6F8)
    TurnDirection(0x8, 0x138, 0)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #1
        0x8,
        (
            "#097FWell, now...\x02\x03",

            "#090FI was wondering how Hilda managed\x01",
            "to get you two in here.\x02\x03",

            "Now I see!\x02\x03",

            "#091FThose outfits were a marvelous\x01",
            "idea. You both look quite\x01",
            "convincing.\x02\x03",

            "#090FEstelle...Joshua... I haven't\x01",
            "had such a wonderful day in a\x01",
            "very long time.\x02\x03",

            "You must come again for tea.\x02\x03",

            "I'd like it if Klaudia and Cassius\x01",
            "could join us next time. We could\x01",
            "all have a nice chat together...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_572")

    TalkEnd(0xFE)
    Return()

    # Function_3_344 end

    def Function_4_576(): pass

    label("Function_4_576")

    EventBegin(0x0)
    OP_28(0x4E, 0x1, 0x8)
    OP_6D(2240, 12000, 50930, 0)
    OP_67(0, 11000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(135000, 0)
    OP_6E(255, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x8, 2170, 12000, 62700, 0)
    SetChrPos(0xD, 4080, 12000, 64099, 180)
    SetChrPos(0x101, 1870, 12000, 45230, 0)
    SetChrPos(0x105, 1870, 12000, 45230, 0)
    SetChrPos(0x103, 1870, 12000, 45230, 0)
    SetChrChipByIndex(0x101, 7)
    SetChrChipByIndex(0x103, 9)
    SetChrChipByIndex(0x105, 11)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_650():
        OP_6D(1570, 12000, 55660, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_650)

    def lambda_668():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_668)

    def lambda_67A():
        OP_8E(0xFE, 0x730, 0x2EE0, 0xD566, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_67A)
    Sleep(500)

    def lambda_69A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_69A)

    def lambda_6AC():
        OP_8E(0xFE, 0xBCC, 0x2EE0, 0xD0AC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AC)
    Sleep(500)

    def lambda_6CC():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6CC)

    def lambda_6DE():
        OP_8E(0xFE, 0x26C, 0x2EE0, 0xD19C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6DE)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #2
        0x105,
        "#040FAre you all right, Grandmother?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#000FWe're here to rescue you,\x01",
            "Your Majesty!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x105, 400)

    ChrTalk(    #4
        0x8,
        "#090FKlaudia...and Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xD,
        (
            "So, you're finally here... I was\x01",
            "getting quite bored with waiting.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7CC():
        OP_8E(0xD, 0xAD2, 0x2EE0, 0xF3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_7CC)

    def lambda_7E7():

        label("loc_7E7")

        TurnDirection(0xD, 0x105, 0)
        OP_48()
        Jump("loc_7E7")

    QueueWorkItem2(0xD, 1, lambda_7E7)

    def lambda_7F8():
        OP_6D(2180, 13000, 59350, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7F8)

    def lambda_810():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_810)

    def lambda_820():
        OP_6E(321, 3000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_820)

    def lambda_830():
        OP_67(0, 6360, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_830)
    Sleep(800)

    def lambda_84D():
        OP_8F(0xFE, 0x88E, 0x2EE0, 0xF744, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_84D)
    Sleep(200)

    def lambda_86D():
        OP_8E(0xFE, 0x83E, 0x2EE0, 0xDDC2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_86D)
    Sleep(110)

    def lambda_88D():
        OP_8E(0xFE, 0xD20, 0x2EE0, 0xDFB6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_88D)
    Sleep(100)

    def lambda_8AD():
        OP_8E(0xFE, 0x280, 0x2EE0, 0xE074, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8AD)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #6
        0x101,
        (
            "#000FLieutenant Lorence!\x01",
            "What are you doing here...?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xD, 0xFF)

    ChrTalk(    #7
        0xD,
        (
            "#280FHa ha... My duty is to guard\x01",
            "Her Majesty.\x02\x03",

            "Is it truly any wonder that\x01",
            "I'm here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#000FEnough of your crap!\x02\x03",

            "No matter how strong you are,\x01",
            "we've still got three-to-one\x01",
            "odds on you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x103,
        (
            "#020FThis one certainly seems skilled.\x02\x03",

            "Just who is he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#000FCommander of the Intelligence\x01",
            "Division's Special Ops...\x01",
            "2nd Lieutenant Lorence Belgar!\x02\x03",

            "Former jaeger, and scout\x01",
            "for the colonel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xD,
        (
            "#280FSo you've done your research,\x01",
            "I see. Most impressive.\x02\x03",

            "But what else would one expect of the\x01",
            "daughter of an S-ranked bracer...one\x01",
            "Cassius Bright, I believe...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#000F!!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x103,
        (
            "#020FMy master's rank has never been\x01",
            "public knowledge, and yet...\x02\x03",

            "You are not one to be\x01",
            "trifled with, I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xD,
        (
            "#280FHa ha...\x01",
            "I know you, as well.\x02\x03",

            "Scherazard Harvey, also known as\x01",
            "the 'Silver Streak'. C-ranked.\x02\x03",

            "And very close to ascending\x01",
            "to B rank, it seems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x103,
        "#020F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x105,
        (
            "#040FP-Please...release my grandmother.\x02\x03",

            "If you were just fighting in the\x01",
            "employ of the colonel, there is\x01",
            "no further call to do this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xD,
        (
            "#280FThere are more things in heaven\x01",
            "and earth than are dreamt of in\x01",
            "your philosophy...\x02\x03",

            "You see only the surface, like that\x01",
            "of a quartz grid...with no concept\x01",
            "of the forces at work within.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x105,
        "#040FWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xD,
        (
            "#280FTake heed, Princess Klaudia.\x02\x03",

            "The nation is like an enormously\x01",
            "complex orbment.\x02\x03",

            "The people are like the units\x01",
            "of quartz that provide the power\x01",
            "and organize the system...\x02\x03",

            "And the territory which houses\x01",
            "them is the frame...\x02\x03",

            "If you lack the means to under-\x01",
            "stand how it works, then you are\x01",
            "unfit to be its queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x105,
        "#040F?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#090FAn interesting metaphor...\x02\x03",

            "You may even be right.\x02\x03",

            "I certainly never expected to\x01",
            "hear a theory on the nature of\x01",
            "politics at a time like this...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(    #22
        0xD,
        (
            "#280FHeh... Pardon my rudeness. You've no\x01",
            "need to hear my useless sermonizing,\x01",
            "Your Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#000FI...don't really understand\x01",
            "this all that well...\x02\x03",

            "...but the general gist is\x01",
            "that you don't plan to let\x01",
            "the queen go, do you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #24
        0xD,
        "#280FAnd if I do not...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#000FObviously we'd take her back\x01",
            "by force!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x103,
        (
            "#020FIndeed... After we've come this far,\x01",
            "we certainly can't go back now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x105,
        (
            "#040FYou don't give me the impression\x01",
            "that you bear us any ill will...\x02\x03",

            "...but I WILL bring my blade to\x01",
            "bear on you, if it will get my\x01",
            "grandmother back!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xD,
        "#280FHa ha... Good.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x8, 400)
    OP_8E(0xD, 0x9E2, 0x2EE0, 0xF4E2, 0x7D0, 0x0)

    def lambda_121E():
        OP_90(0xFE, 0x0, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_121E)

    def lambda_1239():
        OP_91(0xFE, 0x0, 0x0, 0x7D0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1239)

    def lambda_1254():
        OP_67(0, 5500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1254)

    def lambda_126C():
        OP_6E(295, 3000)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_126C)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0xD, 0x20)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 6)
    TurnDirection(0xD, 0x105, 400)

    def lambda_129D():
        OP_99(0xFE, 0x0, 0xB, 0xBB8)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_129D)
    OP_96(0xD, 0x8AC, 0x2EE0, 0xEEFC, 0x190, 0x1B58)
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #29
        0xD,
        (
            "#280FCome, then...\x01",
            "Do what you can.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    Battle(0x39A, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x0)
    SetChrPos(0x101, 3360, 12000, 57270, 0)
    SetChrPos(0x105, 2110, 12000, 56770, 0)
    SetChrPos(0x103, 640, 12000, 57460, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1348"),
        (1, "loc_1785"),
        (SWITCH_DEFAULT, "loc_18D2"),
    )


    label("loc_1348")

    OP_28(0x4E, 0x1, 0x10)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 14)
    SetChrPos(0xD, 2220, 12000, 61180, 180)
    OP_2B(0x4D, 0x3)

    ChrTalk(    #30
        0xD,
        (
            "#280FAmazing... I hadn't realized\x01",
            "that you were this strong.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#000F*huff* *huff*\x02\x03",

            "You were holding back in the\x01",
            "finals, weren't you?!\x02\x03",

            "We should never have even\x01",
            "stood a chance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x103,
        (
            "#020FI-I'm impressed we beat\x01",
            "this monster...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x105,
        "#040FI... I can't believe it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xD,
        (
            "#280FEstelle Bright... I apologize for\x01",
            "treating you as an unworthy opponent.\x02\x03",

            "Perhaps one day you may\x01",
            "reach your father's level...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#000FWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xD,
        "#280FHowever...that day has yet to arrive.\x02",
    )

    CloseMessageWindow()

    def lambda_1554():
        OP_6D(2400, 12000, 57540, 2000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1554)
    OP_99(0xD, 0x3, 0x0, 0x7D0)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 6)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0xC8, 0x0)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x64, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x32, 0x0)
    SetChrPos(0xE, 2220, 12000, 61180, 180)
    SetChrPos(0xF, 2220, 12000, 61180, 180)
    SetChrPos(0x10, 2220, 12000, 61180, 180)
    SetChrPos(0x11, 2220, 12000, 61180, 180)
    OP_43(0xD, 0x1, 0x0, 0x5)
    Sleep(70)
    OP_43(0xE, 0x1, 0x0, 0x5)
    Sleep(70)
    OP_43(0xF, 0x1, 0x0, 0x5)
    Sleep(70)
    OP_43(0x10, 0x1, 0x0, 0x5)
    Sleep(70)
    OP_43(0x11, 0x1, 0x0, 0x5)
    OP_A6(0x0)

    def lambda_162F():
        OP_6C(24000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_162F)
    OP_A6(0x0)

    def lambda_1642():
        OP_67(0, 6730, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1642)
    OP_A6(0x2)
    PlayEffect(0x8, 0xFF, 0xFF, 2360, 14000, 57260, 0, 0, 0, 2400, 2400, 2400, 0xFF, 0, 0, 0, 0)
    OP_51(0x105, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 17)
    TurnDirection(0x105, 0xD, 0)

    def lambda_16A9():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_16A9)

    def lambda_16BF():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16BF)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 16)
    TurnDirection(0x103, 0xD, 0)

    def lambda_16E6():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_16E6)

    def lambda_16FC():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_16FC)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 15)
    TurnDirection(0x101, 0xD, 0)

    def lambda_1723():
        OP_94(0x1, 0xFE, 0xB4, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1723)

    def lambda_1739():
        OP_99(0xFE, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1739)
    Sleep(500)

    ChrTalk(    #37
        0x101,
        "#000FAaaaahhh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x103,
        "#020FAck...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x105,
        "#040FAgh...!!\x02",
    )

    CloseMessageWindow()
    Jump("loc_18D2")

    label("loc_1785")

    OP_28(0x4E, 0x1, 0x20)
    SetChrChipByIndex(0x105, 17)
    SetChrChipByIndex(0x103, 16)
    SetChrChipByIndex(0x101, 15)

    ChrTalk(    #40
        0xD,
        (
            "#280F...How disappointing.\x02\x03",

            "I had thought you would prove\x01",
            "more of a challenge...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#000FH-How...\x02\x03",

            "How can he be so much stronger\x01",
            "than during the tournament...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x103,
        (
            "#020FHe was probably holding\x01",
            "back deliberately...\x02\x03",

            "He might be as strong as\x01",
            "Master Cassius...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x105,
        (
            "#040FGrandmother...\x01",
            "I...I'm sorry...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D2")

    label("loc_18D2")


    ChrTalk(    #44
        0x8,
        "#090FKlaudia! Estelle!\x02",
    )

    CloseMessageWindow()

    def lambda_18F4():
        OP_8E(0xFE, 0x6F4, 0x2EE0, 0xF1EA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_18F4)
    Sleep(200)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    TurnDirection(0xD, 0x8, 400)

    def lambda_192F():
        OP_6D(2260, 12000, 60490, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_192F)

    def lambda_1947():

        label("loc_1947")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_1947")

    QueueWorkItem2(0xD, 1, lambda_1947)
    OP_96(0xD, 0xB0E, 0x2EE0, 0xF1FE, 0x3E8, 0xFA0)
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(    #45
        0xD,
        (
            "#280FThat will be far enough, Your\x01",
            "Majesty, if you please.\x02\x03",

            "They are not mortally wounded,\x01",
            "I assure you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        "#090F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xD,
        "#280FHa ha... That's fine.\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xD, 0x20)
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xD, 13)
    OP_44(0xD, 0xFF)
    TurnDirection(0xD, 0x105, 400)

    ChrTalk(    #48
        0xD,
        (
            "#280FNow, then...\x01",
            "That was a fine warm-up.\x02\x03",

            "My apologies.\x01",
            "Allow me to remove this...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xD, 400)
    TurnDirection(0x105, 0xD, 0)
    OP_99(0x105, 0x3, 0x0, 0x3E8)
    SetChrChipByIndex(0x105, 11)
    TurnDirection(0x101, 0xD, 0)
    OP_99(0x101, 0x3, 0x0, 0x3E8)
    SetChrChipByIndex(0x101, 7)
    TurnDirection(0x103, 0xD, 0)
    OP_99(0x103, 0x3, 0x0, 0x3E8)
    SetChrChipByIndex(0x103, 9)

    ChrTalk(    #49
        0x101,
        "#000FS-Silver hair...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#020FNo... \x01",
            "It's ash blond...\x02\x03",

            "I'd guess that you were born\x01",
            "somewhere up north.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xD,
        (
            "#280FHa ha...\x01",
            "Indeed, you are correct.\x02\x03",

            "Though it's closer than\x01",
            "you might think...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x105,
        "#040FWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "#090FYour eyes betray much...\x02\x03",

            "You are so young...yet you have\x01",
            "endured such hardships already...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(    #54
        0xD,
        (
            "#280F...\x02\x03",

            "Your Majesty, you are hardly\x01",
            "qualified to feel pity for me.\x02\x03",

            "You, who know the name of 'Hamel'...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #55
        0x8,
        "#090FWhat...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x105, 400)

    ChrTalk(    #56
        0xD,
        (
            "#280FIt's almost time.\x02\x03",

            "I will return Her Majesty to\x01",
            "you, just as you wished.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#000FHuh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xD,
        (
            "#280FIf you wish to stop the colonel,\x01",
            "you had best hurry below.\x02\x03",

            "You may well already be too late...\x02\x03",

            "But you may be able to prevent any further\x01",
            "needless damage from occurring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x8,
        (
            "#090FBelow...?\x02\x03",

            "You cannot mean beneath there...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x8, 400)

    ChrTalk(    #60
        0xD,
        (
            "#280FHeh... However unpleasant you may\x01",
            "find it, I was certain that you would \x01",
            "understand the significance.\x02\x03",

            "You can show them the way.\x02\x03",

            "And now, I bid you adieu.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1EC1():

        label("loc_1EC1")

        TurnDirection(0xFE, 0xD, 0)
        OP_48()
        Jump("loc_1EC1")

    QueueWorkItem2(0x8, 1, lambda_1EC1)

    def lambda_1ED2():
        OP_6D(1670, 12000, 63950, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1ED2)

    def lambda_1EEA():
        OP_6E(347, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1EEA)

    def lambda_1EFA():
        OP_67(0, 6160, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_1EFA)
    OP_8E(0xD, 0xBFE, 0x2EE0, 0xFC26, 0x1B58, 0x0)
    OP_8E(0xD, 0x906, 0x2EE0, 0x1054A, 0x1B58, 0x0)
    OP_96(0xD, 0x5E6, 0x3138, 0x108C4, 0x320, 0x1B58)
    OP_96(0xD, 0x51E, 0xFFFFD120, 0x12066, 0x3E8, 0x1B58)
    WaitChrThread(0xD, 0x2)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)

    ChrTalk(    #61
        0x101,
        "#000FHey!!\x02",
    )

    CloseMessageWindow()
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)

    def lambda_1FFD():
        OP_8E(0xFE, 0xEEC, 0x2EE0, 0x1064E, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FFD)

    ChrTalk(    #62
        0x103,
        "#020FIs he insane?!\x02",
    )

    CloseMessageWindow()

    def lambda_2031():
        OP_6D(2270, 12000, 66180, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2031)

    def lambda_2049():
        OP_6C(129000, 2000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2049)
    Sleep(200)
    OP_51(0x103, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x103, 65535)

    def lambda_206E():
        OP_8E(0xFE, 0x2EE, 0x2EE0, 0x106DA, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_206E)
    Sleep(500)
    OP_51(0x105, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x105, 65535)

    def lambda_209E():
        OP_8E(0xFE, 0x6EA, 0x2EE0, 0xED4E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_209E)
    WaitChrThread(0x105, 0x1)

    def lambda_20BE():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_20BE)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #63
        0x101,
        (
            "#000FH-He's gone...\x02\x03",

            "Did he drop into the lake?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 0x1)

    ChrTalk(    #64
        0x103,
        (
            "#020FBut the water's undisturbed...\x02\x03",

            "Just who is this guy...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x105,
        "#040FGrandmother! Are you hurt?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#090FI am unharmed, Klaudia.\x01",
            "He never laid a hand on me.\x02\x03",

            "But more importantly...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0xB, 1870, 12000, 45230, 0)
    SetChrPos(0xA, 1870, 12000, 45230, 0)
    SetChrPos(0xC, 1870, 12000, 45230, 0)
    SetChrPos(0x9, 1870, 12000, 45230, 0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    ChrTalk(    #67
        0xA,
        "Estelle!\x02",
    )

    CloseMessageWindow()

    def lambda_2271():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2271)

    def lambda_227F():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_227F)

    def lambda_228D():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_228D)

    def lambda_229B():
        OP_6D(2540, 12000, 61390, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_229B)

    def lambda_22B3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_22B3)

    def lambda_22C5():
        OP_8E(0xFE, 0xD2A, 0x2EE0, 0xE394, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_22C5)
    Sleep(500)

    def lambda_22E5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_22E5)

    def lambda_22F7():
        OP_8E(0xFE, 0x7D0, 0x2EE0, 0xE876, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_22F7)
    Sleep(500)

    def lambda_2317():

        label("loc_2317")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2317")

    QueueWorkItem2(0xB, 1, lambda_2317)

    def lambda_2328():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2328)

    def lambda_233A():
        OP_8E(0xFE, 0x816, 0x2EE0, 0xE204, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_233A)
    Sleep(500)

    def lambda_235A():

        label("loc_235A")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_235A")

    QueueWorkItem2(0xC, 1, lambda_235A)

    def lambda_236B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_236B)

    def lambda_237D():
        OP_8E(0xFE, 0x2C6, 0x2EE0, 0xE448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_237D)

    def lambda_2398():
        OP_8E(0xFE, 0xDF2, 0x2EE0, 0xE826, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2398)
    Sleep(500)

    def lambda_23B8():
        OP_8E(0xFE, 0x96, 0x2EE0, 0xEBB4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_23B8)

    def lambda_23D3():
        OP_6D(2140, 12000, 59300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_23D3)

    def lambda_23EB():
        OP_6E(307, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_23EB)
    SetChrFlags(0x105, 0x40)
    OP_8E(0x105, 0xB22, 0x2EE0, 0xF000, 0x7D0, 0x0)
    TurnDirection(0x105, 0x9, 400)
    WaitChrThread(0x103, 0x1)

    def lambda_2420():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2420)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #68
        0x101,
        (
            "#000FJoshua?!\x02\x03",

            "Thank Aidios you're all right!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        (
            "#010FYou, too...\x02\x03",

            "Since Colonel Richard and Lieu-\x01",
            "tenant Lorence weren't in the\x01",
            "castle, I started to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#000FThe red helmet guy was here\x01",
            "just a minute ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        "#010FWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x103,
        (
            "#020FHe jumped out that window\x01",
            "and escaped.\x02\x03",

            "He's some kind of monster,\x01",
            "all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xA,
        (
            "#010FI... I see...\x02\x03",

            "Praise Aidios for keeping you safe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#000FJoshua...\x02",
    )

    CloseMessageWindow()
    OP_8E(0x9, 0x730, 0x2EE0, 0xEBD2, 0x7D0, 0x0)

    ChrTalk(    #75
        0x9,
        (
            "#170FYour Majesty... It's good to\x01",
            "see you unharmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#090FWell met, Lieutenant Schwarz.\x02\x03",

            "Indeed, I owe all of you a\x01",
            "debt of gratitude.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2672():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2672)

    def lambda_2680():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2680)

    def lambda_268E():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_268E)

    def lambda_269C():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_269C)

    def lambda_26AA():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_26AA)

    def lambda_26B8():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_26B8)

    ChrTalk(    #77
        0xB,
        "#030FYou are far too kind, Your Majesty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xC,
        (
            "#070FWe're just glad to be of help.\x02\x03",

            "I don't think this is over\x01",
            "yet, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "#170FWe've dealt with the Special Ops\x01",
            "inside the castle, but I'm afraid\x01",
            "there are bad tidings...\x02\x03",

            "Army reinforcements from every\x01",
            "province are on their way to\x01",
            "Grancel.\x02\x03",

            "From the sounds of it, the\x01",
            "Intelligence Division is\x01",
            "somehow maintaining control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        "#090FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        (
            "#170FTime is short, my Liege.\x02\x03",

            "I must ask that you board the\x01",
            "I.D. ship and escape at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "#090FNo... That I cannot do.\x02\x03",

            "The situation has grown more dire.\x02\x03",

            "Colonel Richard must be stopped,\x01",
            "whatever the cost.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        (
            "#170FWh-What do you mean,\x01",
            "Your Majesty?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "#090FLast night, I finally understood\x01",
            "the true intentions of which the\x01",
            "colonel spoke.\x02\x03",

            "He wants the Shining Ring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#000FShining Ring...\x02\x03",

            "Why does that sound so familiar...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xA,
        (
            "#010FIt's one of the Sept-Terrions that\x01",
            "the Goddess gave the ancients...\x02\x03",

            "The legend says that it has the\x01",
            "power to control nature itself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#000FOh, yeah.\x01",
            "Professor Alba told us about it.\x02\x03",

            "But I thought that was just some\x01",
            "silly story that was passed down\x01",
            "through the church...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        "#090F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#000FHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xB,
        (
            "#030FHrm...\x01",
            "So it does exist?\x02\x03",

            "And it lies somewhere within Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x8,
        (
            "#090FAccording to an old legend\x01",
            "of the royal family...\x02\x03",

            "'The Shining Ring shall bring catastrophe,\x01",
            "condemning the souls of men to eternal\x01",
            "purgatory.'\x02\x03",

            "'It has been sealed within the interval of the\x01",
            "blackest dark, that we might retain our\x01",
            "humanity.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xC,
        (
            "#070F'Condemning the souls of men to\x01",
            "eternal purgatory'...?\x02\x03",

            "Well, that's not a little ominous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "#090FThese words have been passed down\x01",
            "in the royal family as a warning.\x02\x03",

            "Perhaps this 'Shining Ring' truly\x01",
            "was so dangerous that the royal\x01",
            "family's ancestors sealed it away.\x02\x03",

            "Also, there was that massive\x01",
            "orbal reaction that was detected\x01",
            "beneath the city...\x02\x03",

            "If one takes both of these\x01",
            "into account...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "#010FThis Shining Ring must be sealed\x01",
            "away underneath Grancel.\x02\x03",

            "It makes sense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        (
            "#090FYes...and I believe that the colonel\x01",
            "has reached the same conclusion.\x02\x03",

            "There remain no details of what,\x01",
            "exactly, the Shining Ring is...\x02\x03",

            "...but I believe there will be\x01",
            "grave danger for all, should it\x01",
            "be restored.\x02\x03",

            "It could be a disaster on par with\x01",
            "the Great Collapse of legend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x105,
        "#040FN-No...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x103,
        "#020FIncredible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#000FE-Excuse me, Your Majesty!\x02\x03",

            "Lieutenant Lorence told us\x01",
            "to go underground...\x02\x03",

            "...but what did that really mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "#090FThere is a mysterious room\x01",
            "within Grancel Castle...\x02\x03",

            "...where nothing, not even a grain of\x01",
            "rice, has been kept in generations. \x01",
            "Forbidden since long ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x105,
        "#040FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        "#170FYou mean the Treasury?!\x02",
    )

    CloseMessageWindow()
    OP_28(0x4E, 0x1, 0x40)
    OP_28(0x4E, 0x1, 0x80)
    OP_28(0x4E, 0x1, 0x100)
    OP_28(0x4E, 0x1, 0x200)
    OP_28(0x4E, 0x1, 0x400)
    OP_28(0x4F, 0x4, 0x2)
    OP_28(0x4F, 0x4, 0x4)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4240   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_576 end

    def Function_5_3151(): pass

    label("Function_5_3151")

    SetChrFlags(0xFE, 0x40)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0xFE, 0x80)
    OP_96(0xFE, 0x83E, 0x2EE0, 0xEB28, 0x190, 0x1770)
    SetChrChipByIndex(0xFE, 6)

    def lambda_3187():
        OP_99(0xFE, 0x0, 0x1, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3187)
    OP_96(0xFE, 0x79E, 0x3A98, 0xE6AA, 0xBB8, 0x1F40)
    OP_A2(0x0)
    Sleep(300)
    OP_A2(0x1)

    def lambda_31B9():
        OP_99(0xFE, 0x2, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_31B9)
    OP_96(0xFE, 0x744, 0x2EE0, 0xE204, 0x0, 0x3A98)
    OP_A2(0x2)
    Sleep(1000)

    def lambda_31E8():
        OP_99(0xFE, 0x3, 0xB, 0xFA0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_31E8)
    Return()

    # Function_5_3151 end

    def Function_6_31F3(): pass

    label("Function_6_31F3")

    OP_1F(0x50, 0xC8)
    Return()

    # Function_6_31F3 end

    SaveToFile()

Try(main)
