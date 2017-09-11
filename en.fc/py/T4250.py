from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4250   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4250.x',
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
        'Captain Amalthea',                     # 9
        'Shea',                                 # 10
        'Colonel Richard',                      # 11
        'Special Ops Soldier',                  # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Special Ops Soldier',                  # 15
        'Special Ops Soldier',                  # 16
        'Royal Guardsman',                      # 17
        'Royal Guardsman',                      # 18
        'Special Ops Soldier',                  # 19
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
        'ED6_DT07/CH02100 ._CH',             # 00
        'ED6_DT07/CH02540 ._CH',             # 01
        'ED6_DT07/CH02030 ._CH',             # 02
        'ED6_DT07/CH02460 ._CH',             # 03
        'ED6_DT07/CH02230 ._CH',             # 04
        'ED6_DT07/CH02240 ._CH',             # 05
        'ED6_DT07/CH01610 ._CH',             # 06
        'ED6_DT07/CH00177 ._CH',             # 07
        'ED6_DT07/CH01640 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02100P._CP',             # 00
        'ED6_DT07/CH02540P._CP',             # 01
        'ED6_DT07/CH02030P._CP',             # 02
        'ED6_DT07/CH02460P._CP',             # 03
        'ED6_DT07/CH02230P._CP',             # 04
        'ED6_DT07/CH02240P._CP',             # 05
        'ED6_DT07/CH01610P._CP',             # 06
        'ED6_DT07/CH00177P._CP',             # 07
        'ED6_DT07/CH01640P._CP',             # 08
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
        X                   = 21430,
        Z                   = 750,
        Y                   = -3970,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2750,
        Z                   = 0,
        Y                   = -26300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2980,
        Z                   = 0,
        Y                   = -26300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 2750,
        Z                   = 0,
        Y                   = -26300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -2980,
        Z                   = 0,
        Y                   = -26300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 9000,
        Y                   = 29350,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )


    DeclEvent(
        X                   = 4010,
        Y                   = 10000,
        Z                   = 16219,
        Range               = -4330,
        Unknown_10          = 0x1F40,
        Unknown_14          = 0x2D78,
        Unknown_18          = 0x0,
        Unknown_1C          = 8,
    )

    DeclEvent(
        X                   = 21060,
        Y                   = -1000,
        Z                   = -1860,
        Range               = 19780,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE854,
        Unknown_18          = 0x0,
        Unknown_1C          = 10,
    )

    DeclEvent(
        X                   = 4290,
        Y                   = -1000,
        Z                   = -25590,
        Range               = -4690,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFA33A,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 0,
        Y                   = 8000,
        Z                   = 30350,
        Range               = 3000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 12,
    )


    ScpFunction(
        "Function_0_2D2",          # 00, 0
        "Function_1_36B",          # 01, 1
        "Function_2_38A",          # 02, 2
        "Function_3_458",          # 03, 3
        "Function_4_18D2",         # 04, 4
        "Function_5_1A4F",         # 05, 5
        "Function_6_1AB7",         # 06, 6
        "Function_7_250F",         # 07, 7
        "Function_8_2538",         # 08, 8
        "Function_9_3BE8",         # 09, 9
        "Function_10_3C61",        # 0A, 10
        "Function_11_3DF3",        # 0B, 11
        "Function_12_40B8",        # 0C, 12
        "Function_13_4238",        # 0D, 13
        "Function_14_42A6",        # 0E, 14
        "Function_15_4336",        # 0F, 15
    )


    def Function_0_2D2(): pass

    label("Function_0_2D2")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2E2"),
        (108, "loc_2F8"),
        (SWITCH_DEFAULT, "loc_30B"),
    )


    label("loc_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F5")
    OP_A2(0x639)
    Event(0, 3)

    label("loc_2F5")

    Jump("loc_30B")

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_308")
    Event(0, 6)

    label("loc_308")

    Jump("loc_30B")

    label("loc_30B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_335")
    SetChrChipByIndex(0x0, 3)
    SetChrChipByIndex(0x1, 4)
    SetChrChipByIndex(0x138, 5)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_359")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_359")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36A")
    ClearChrFlags(0x12, 0x80)

    label("loc_36A")

    Return()

    # Function_0_2D2 end

    def Function_1_36B(): pass

    label("Function_1_36B")

    OP_71(0xC, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_END)), "loc_380")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_380")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_36B end

    def Function_2_38A(): pass

    label("Function_2_38A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_442")

    label("loc_3AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C8")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_442")

    label("loc_3C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E1")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_442")

    label("loc_3E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FA")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_442")

    label("loc_3FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_413")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_442")

    label("loc_413")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_442")

    label("loc_42C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_442")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_442")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_457")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_442")

    label("loc_457")

    Return()

    # Function_2_38A end

    def Function_3_458(): pass

    label("Function_3_458")

    EventBegin(0x0)
    SetChrPos(0x102, 520, 0, -22530, 0)
    SetChrPos(0x101, -1610, 0, -22470, 0)
    SetChrPos(0x108, -290, 0, -21870, 0)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_6D(-70, 14350, 22560, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(12000, 0)
    OP_6E(280, 0)

    def lambda_4DA():
        OP_6D(-8920, 10250, -21440, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DA)

    def lambda_4F2():
        OP_67(0, 8000, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F2)

    def lambda_50A():
        OP_6B(3920, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_50A)

    def lambda_51A():
        OP_6C(44000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51A)

    def lambda_52A():
        OP_6E(280, 10000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_52A)
    FadeToBright(2000, 0)
    Sleep(10000)
    Fade(1000)
    OP_6D(30, 0, -22200, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        "#6P#004FWhoaaa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x102,
        (
            "#010FYou can say that again...\x02\x03",

            "I've never seen anything that\x01",
            "compares to this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x108,
        (
            "#074FIt's not just pretty...\x01",
            "It's got history.\x02\x03",

            "#070FI can really feel the traditions\x01",
            "and rules of the old kingdom here.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 770, 0, -9870, 180)
    SetChrPos(0x9, -280, 0, -9260, 180)

    NpcTalk(    #3
        0x8,
        "Woman's Voice",
        "#4PWelcome to Grancel Castle.\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x8,
        "Woman's Voice",
        (
            "#4PYou are Zin and his team,\x01",
            "correct?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_744():
        OP_8E(0xFE, 0xFFFFFFB0, 0x0, 0xFFFFB41A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_744)

    def lambda_75F():
        OP_8E(0xFE, 0xFFFFFCAE, 0x0, 0xFFFFB758, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_75F)
    OP_6D(130, 0, -20310, 3000)

    ChrTalk(    #5
        0x101,
        "#2P#509F(Erk... Captain Amalthea...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#012F(This isn't really unexpected,\x01",
            "but even so...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x108,
        (
            "#070FThat's right. We come at the\x01",
            "invitation of the good duke.\x02\x03",

            "And, uh...you are?\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #8
        0x8,
        (
            "#182FHa ha... Pardon me.\x02\x03",

            "I am Captain Kanone Amalthea of\x01",
            "the Intelligence Division, head\x01",
            "of Grancel Castle's defense.\x02\x03",

            "I would like to extend my\x01",
            "heartfelt congratulations for\x01",
            "your championship victory.\x02\x03",

            "Watching the match was truly\x01",
            "a spectacular experience.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x108,
        (
            "#071FYou're too kind, really.\x02\x03",

            "And may I say, I didn't know\x01",
            "they made women as young and\x01",
            "pretty as you into captains.\x02\x03",

            "You must do fine work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#184FMy, but you are the flatterer.\x02\x03",

            "#180FBut I'm not so young as\x01",
            "your bracer friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#2P#002F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#012F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "#180FEstelle and Joshua Bright.\x02\x03",

            "It's been some time since the\x01",
            "incident in Zeiss, hasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#2P#006F...Yeah, I guess it has.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        "#010FQuite some time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#181FUnfortunately, the matter concerning\x01",
            "Professor Russell is yet to be resolved.\x02\x03",

            "It appears that he and his grand-\x01",
            "daughter were abducted by a group\x01",
            "of nefarious individuals.\x02\x03",

            "#188FYou wouldn't happen to know\x01",
            "anything about that, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#2P#505FI-I'm afraid not...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#015FWe left that case up to the\x01",
            "full-fledged bracers and came\x01",
            "to Grancel.\x02\x03",

            "We never even heard the\x01",
            "follow-up report on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#188FI see... Ha ha...\x01",
            "That's truly a shame.\x02\x03",

            "Well, with the resources of the Intelligence\x01",
            "Division, it's only a matter of time before\x01",
            "the culprits are arrested.\x02\x03",

            "Have no fear on that score.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#2P#009F(Wh-What the hell's with her...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#019FUnderstood.\x02\x03",

            "We trust you to take care\x01",
            "of the professor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#181FOh, absolutely...\x02\x03",

            "#182FNow, we must show you to\x01",
            "your rooms.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #23
        0x8,
        (
            "#182F#4PShea, if you would please\x01",
            "do the honors?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #24
        0x9,
        "#3PYes, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#180F#4PSee to their needs...\x02\x03",

            "...but do not bore them with\x01",
            "any idle chatter.\x02\x03",

            "Do I make myself clear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        "#3PY-Yes, ma'am... I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        "#188F#4PHa ha... Very good.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)
    TurnDirection(0x8, 0x108, 400)

    ChrTalk(    #28
        0x8,
        (
            "#182FNow, everyone...\x01",
            "I hope you enjoy your evening.\x02\x03",

            "For my part, I must bid you farewell.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F97():

        label("loc_F97")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_F97")

    QueueWorkItem2(0x108, 1, lambda_F97)

    def lambda_FA8():

        label("loc_FA8")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_FA8")

    QueueWorkItem2(0x101, 1, lambda_FA8)

    def lambda_FB9():

        label("loc_FB9")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_FB9")

    QueueWorkItem2(0x102, 1, lambda_FB9)
    OP_8C(0x8, 45, 400)
    OP_8E(0x8, 0x730, 0x0, 0xFFFFC2F2, 0x7D0, 0x0)

    def lambda_FE5():
        OP_8E(0xFE, 0x1CC0, 0x0, 0xFFFFD88C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FE5)
    Sleep(1500)

    ChrTalk(    #29
        0x108,
        (
            "#6P#070FMmm-mm-mmm.\x01",
            "Now that is one fine woman.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #30
        0x101,
        (
            "#509FI hate to say this, Zin, but\x01",
            "your taste in women is crap.\x02\x03",

            "There's nothing 'fine' about\x01",
            "that fox-faced harpy.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x108, 400)

    ChrTalk(    #31
        0x102,
        (
            "#014FI think that might just be his\x01",
            "favorite type of woman.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #32
        0x108,
        (
            "#071F#6PHa ha... I just tend to find that women\x01",
            "like that turn out be pretty good people,\x01",
            "once you peel back a few layers.\x02\x03",

            "So to speak...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#007FYou're hopeless.\x02\x03",

            "#006FNot that it matters, but you \x01",
            "really do sound like a dirty\x01",
            "old man sometimes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x108,
        "#072F#6P#5SOh, my honor!\x02",
    )

    CloseMessageWindow()

    def lambda_124D():
        OP_6D(-240, 0, -20830, 1000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_124D)
    OP_8E(0x9, 0xFFFFFEFC, 0x0, 0xFFFFB186, 0x5DC, 0x0)
    TurnDirection(0x9, 0x108, 400)

    ChrTalk(    #35
        0x9,
        "#3PU-Umm...\x02",
    )

    CloseMessageWindow()

    def lambda_1291():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1291)

    def lambda_129F():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_129F)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #36
        0x101,
        (
            "#2P#506FOh, sorry about that.\x02\x03",

            "You were supposed to show\x01",
            "us to our room, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        "#3PYes, please allow me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "#3PPardon my not saying before,\x01",
            "but I am Shea, a maid here at\x01",
            "the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "#3PI will be at your service this\x01",
            "evening, from the dinner party\x01",
            "until the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "#3PIf anything is not to your\x01",
            "satisfaction, please don't\x01",
            "hesitate to let me know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x108,
        "#070FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#010FWill you please show us\x01",
            "the room then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "#3PCertainly.\x01",
            "It's on the second floor.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 315, 400)
    OP_43(0x9, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_8E(0x108, 0xFFFFFF10, 0x0, 0xFFFFAEA2, 0xBB8, 0x0)
    OP_6A(0x108)
    OP_43(0x108, 0x1, 0x0, 0x4)
    Sleep(150)
    OP_43(0x101, 0x1, 0x0, 0x4)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(12000)
    OP_66(0x0)
    WaitChrThread(0x9, 0x1)

    def lambda_14F9():
        OP_6E(196, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_14F9)

    def lambda_1509():
        OP_8E(0xFE, 0x32, 0x2328, 0x5A6E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1509)
    WaitChrThread(0x108, 0x1)

    def lambda_1529():
        OP_8E(0xFE, 0x410, 0x2328, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1529)
    WaitChrThread(0x101, 0x1)

    def lambda_1549():
        OP_8E(0xFE, 0xFFFFFB96, 0x2328, 0x524E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1549)
    WaitChrThread(0x102, 0x1)

    def lambda_1569():
        OP_8E(0xFE, 0xFFFFFF92, 0x2328, 0x4FBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1569)
    ClearMapFlags(0x1)
    OP_6D(4840, 9000, 32350, 3000)

    ChrTalk(    #44
        0x101,
        "#004F#5SOh, WOW...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#001FGet a load of that chandelier!\x01",
            "Talk about classy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        (
            "#017FHush, Estelle.\x02\x03",

            "#010FWhat's that way...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1623():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1623)

    def lambda_1631():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1631)

    def lambda_163F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_163F)
    OP_8C(0x9, 180, 400)

    ChrTalk(    #47
        0x9,
        "#1PThat's the Throne Room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "#1PHer Majesty uses it to receive\x01",
            "personal guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x9,
        (
            "#1PIt hasn't seen much use in\x01",
            "recent days, though...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16E6():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16E6)

    def lambda_16F4():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_16F4)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(    #50
        0x102,
        "#012F...I see.\x02",
    )

    CloseMessageWindow()
    OP_69(0x9, 0x5DC)
    OP_6A(0x9)

    ChrTalk(    #51
        0x108,
        (
            "#073F#4PBut is the queen's condition\x01",
            "really that bad?\x02\x03",

            "Isn't the Birthday Celebration\x01",
            "coming up soon?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x9, 0x108, 400)

    ChrTalk(    #52
        0x9,
        "#3PO-Oh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "#3PIt's just that it's the head\x01",
            "maid who tends to her in the\x01",
            "Royal Keep of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "#3PI shouldn't speak on subjects\x01",
            "about which I'm unfamiliar...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 0)

    ChrTalk(    #55
        0x9,
        "#3PC-Come then, shall we?\x02",
    )

    CloseMessageWindow()
    OP_66(0x1)
    OP_8C(0x9, 270, 400)
    OP_43(0x9, 0x1, 0x0, 0x5)
    Sleep(420)
    OP_43(0x101, 0x1, 0x0, 0x5)
    Sleep(150)
    OP_43(0x102, 0x1, 0x0, 0x5)
    Sleep(400)
    OP_43(0x108, 0x1, 0x0, 0x5)
    Sleep(3000)
    OP_28(0x49, 0x1, 0x80)
    OP_28(0x49, 0x1, 0x100)
    OP_28(0x49, 0x1, 0x200)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4262   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_458 end

    def Function_4_18D2(): pass

    label("Function_4_18D2")

    OP_8E(0xFE, 0xFFFFFB46, 0x0, 0xFFFFC338, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFF8BC, 0x0, 0xFFFFC694, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFF114, 0x0, 0xFFFFCF18, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFE070, 0x0, 0xFFFFD7C4, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFE070, 0x0, 0xFFFFD7C4, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFCD60, 0x0, 0xFFFFDC1A, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFC3C4, 0x0, 0xFFFFE43A, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFBBB8, 0x0, 0xFFFFFDF8, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFBCDA, 0x4E2, 0xC4E, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFC0A5, 0x9C4, 0x1662, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFC50E, 0xDAC, 0x1F18, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFCD24, 0x1388, 0x2990, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFD742, 0x186A, 0x3070, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFE00C, 0x1C52, 0x3426, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFE96C, 0x203A, 0x367E, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFF75E, 0x2328, 0x3868, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFFB78, 0x2328, 0x3A20, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFFE52, 0x2328, 0x3DC2, 0xBB8, 0x1)
    OP_8E(0xFE, 0x14, 0x2328, 0x44B6, 0xBB8, 0x1)
    Return()

    # Function_4_18D2 end

    def Function_5_1A4F(): pass

    label("Function_5_1A4F")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFF1E6, 0x2328, 0x5DD4, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFE0E8, 0x2328, 0x6504, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFDA9E, 0x2328, 0x65C2, 0xBB8, 0x1)

    def lambda_1A96():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1A96)
    OP_8E(0xFE, 0xFFFFCD9C, 0x2328, 0x65C2, 0xBB8, 0x1)
    Return()

    # Function_5_1A4F end

    def Function_6_1AB7(): pass

    label("Function_6_1AB7")

    EventBegin(0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xA, -6640, 8000, 13770, 80)
    SetChrPos(0x8, -7900, 7500, 13100, 62)
    SetChrPos(0x101, -7920, 9000, 24630, 90)
    SetChrPos(0x102, -7520, 9000, 25920, 90)
    OP_6D(-7580, 9000, 25280, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Sleep(1000)

    NpcTalk(    #56
        0xA,
        "Man's Voice",
        "#1POh, it's you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#580FWha...!\x02",
    )

    CloseMessageWindow()

    def lambda_1B85():
        OP_6D(-3860, 9000, 20630, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1B85)

    def lambda_1B9D():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B9D)

    def lambda_1BAB():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BAB)
    Sleep(1000)

    def lambda_1BBE():
        OP_8E(0xFE, 0xFFFFF813, 0x2328, 0x3A20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BBE)

    def lambda_1BD9():
        OP_8E(0xFE, 0xFFFFF72C, 0x2328, 0x35CA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1BD9)
    WaitChrThread(0xA, 0x1)

    def lambda_1BF9():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1BF9)
    WaitChrThread(0x8, 0x1)

    def lambda_1C0C():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1C0C)

    def lambda_1C1A():

        label("loc_1C1A")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1C1A")

    QueueWorkItem2(0x101, 1, lambda_1C1A)

    def lambda_1C2B():

        label("loc_1C2B")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1C2B")

    QueueWorkItem2(0x102, 1, lambda_1C2B)

    ChrTalk(    #58
        0x102,
        "#012FColonel Richard...\x02",
    )

    CloseMessageWindow()

    def lambda_1C59():
        OP_6D(-4040, 9000, 25340, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1C59)
    OP_43(0xA, 0x1, 0x0, 0x7)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x7)
    Sleep(2000)

    def lambda_1C89():
        OP_8E(0xFE, 0xFFFFEB4C, 0x2328, 0x6022, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C89)
    Sleep(300)

    def lambda_1CA9():
        OP_8E(0xFE, 0xFFFFEAFC, 0x2328, 0x646E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CA9)
    WaitChrThread(0xA, 0x1)

    def lambda_1CC9():

        label("loc_1CC9")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_1CC9")

    QueueWorkItem2(0xA, 1, lambda_1CC9)

    def lambda_1CDA():
        OP_8E(0xFE, 0xFFFFF196, 0x2328, 0x62F2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1CDA)
    WaitChrThread(0x8, 0x1)

    def lambda_1CFA():

        label("loc_1CFA")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_1CFA")

    QueueWorkItem2(0x8, 1, lambda_1CFA)
    WaitChrThread(0xA, 0x2)

    ChrTalk(    #59
        0xA,
        (
            "#111F#4PHa ha...\x01",
            "Estelle and Joshua.\x02\x03",

            "This is our first opportunity\x01",
            "to truly speak face-to-face,\x01",
            "I believe...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#004F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        (
            "#010FThe last time we saw one another\x01",
            "was right after Mayor Dalmore was\x01",
            "arrested, wasn't it?\x02\x03",

            "I'm honestly surprised that\x01",
            "you remember us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xA,
        (
            "#110F#4PI realize that we exchanged few\x01",
            "words, but you made quite an\x01",
            "impression on me.\x02\x03",

            "My curiosity was piqued, so I\x01",
            "did a bit of checking up on you.\x02\x03",

            "I was quite surprised to learn\x01",
            "that you were the children of\x01",
            "Colonel Cassius.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #63
        0x101,
        "#580FH-How'd you find THAT out?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xA,
        (
            "#111F#4PHa ha. Please understand, I'm not\x01",
            "trying to show off the Intelligence\x01",
            "Division's capabilities.\x02\x03",

            "#115FI'm greatly indebted to him from\x01",
            "our time together in the army.\x02\x03",

            "Indeed...more than words\x01",
            "can properly express.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#002F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#110F#4PMight I persuade you to stay\x01",
            "a while and talk?\x02\x03",

            "I've been hoping to speak with\x01",
            "you two for quite some time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#580FHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        "#012F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(    #69
        0x8,
        (
            "#184FP-Pardon me, Colonel...\x02\x03",

            "...but don't you have a meeting\x01",
            "with His Grace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xA,
        (
            "#115F#4PI don't mind being a bit late.\x02\x03",

            "#110FAhh, yes. If we're going to\x01",
            "talk, why don't we use the\x01",
            "lounge inside?\x02\x03",

            "I'll mix you up a couple\x01",
            "of virgin cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        "#187FI-I'll prepare them, sir!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(    #72
        0xA,
        (
            "#112FNo, that won't be necessary.\x02\x03",

            "I want you to go to His Grace and\x01",
            "inform him that I'll be delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        "#183FY-Yes, sir...\x02",
    )

    CloseMessageWindow()

    def lambda_2299():

        label("loc_2299")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2299")

    QueueWorkItem2(0xA, 1, lambda_2299)

    def lambda_22AA():

        label("loc_22AA")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_22AA")

    QueueWorkItem2(0x101, 1, lambda_22AA)

    def lambda_22BB():

        label("loc_22BB")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_22BB")

    QueueWorkItem2(0x102, 1, lambda_22BB)
    TurnDirection(0x8, 0x101, 400)
    OP_62(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #74
        0x8,
        "#186F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#509F(*gulp*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        "#181FPardon me, then.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 45, 400)
    OP_8E(0x8, 0xFFFFFF6A, 0x2328, 0x6EC8, 0xBB8, 0x0)

    def lambda_2346():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2346)
    OP_8E(0x8, 0xFFFFFFBA, 0x2328, 0x8200, 0xBB8, 0x0)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_8C(0xA, 270, 400)

    def lambda_237F():

        label("loc_237F")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_237F")

    QueueWorkItem2(0x101, 1, lambda_237F)

    def lambda_2390():

        label("loc_2390")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_2390")

    QueueWorkItem2(0x102, 1, lambda_2390)

    ChrTalk(    #77
        0xA,
        (
            "#110F#4PNow, then... Shall we retire\x01",
            "to the lounge?\x02\x03",

            "Please, follow me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)

    def lambda_23F5():
        OP_8E(0xFE, 0x23AA, 0x2328, 0x64B4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_23F5)

    def lambda_2410():
        OP_6D(-3040, 9000, 25340, 1500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2410)
    Sleep(500)

    ChrTalk(    #78
        0x101,
        (
            "#580FUh...\x02\x03",

            "#003F(Joshua...? What should we do?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        (
            "#012F(I don't see where we have much\x01",
            "choice but to follow him.)\x02\x03",

            "(We'll be a little late, but we\x01",
            "can talk to the head maid later.)\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4A, 0x1, 0x8)
    OP_28(0x4A, 0x1, 0x10)
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4261   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1AB7 end

    def Function_7_250F(): pass

    label("Function_7_250F")

    OP_8E(0xFE, 0xFFFFF8F8, 0x2328, 0x5168, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF56A, 0x2328, 0x5F6E, 0xBB8, 0x0)
    Return()

    # Function_7_250F end

    def Function_8_2538(): pass

    label("Function_8_2538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2545")
    Return()

    label("loc_2545")

    EventBegin(0x0)
    OP_A2(0x647)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, -70, 9000, 27870, 180)
    SetChrPos(0xB, -800, 9000, 28970, 180)
    SetChrPos(0xC, 530, 9000, 28970, 180)

    NpcTalk(    #80
        0x8,
        "Woman's Voice",
        (
            "#4P...What, might I inquire, are\x01",
            "you doing at this late hour?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)

    def lambda_2616():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2616)

    def lambda_2624():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2624)
    OP_6D(10, 9000, 27580, 2000)

    ChrTalk(    #81
        0x101,
        "#580F#1PAh...!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    AddParty(0x7, 0xFF)
    SetChrPos(0x101, -550, 9000, 16309, 0)
    SetChrPos(0x102, 670, 9000, 16190, 0)
    SetChrFlags(0x108, 0x80)

    def lambda_2686():
        OP_8E(0xFE, 0x8C, 0x2328, 0x4DE4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2686)
    Sleep(200)

    def lambda_26A6():
        OP_8E(0xFE, 0xFFFFFDBC, 0x2328, 0x5294, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_26A6)
    Sleep(100)

    def lambda_26C6():
        OP_8E(0xFE, 0x33E, 0x2328, 0x529E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_26C6)
    OP_6D(100, 9000, 18910, 3000)

    ChrTalk(    #82
        0x102,
        "#012FCaptain Amalthea...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #83
        0x8,
        (
            "#182FHeehee...\x01",
            "Good evening.\x02\x03",

            "I realize that you've been invited here...\x02\x03",

            "But don't you think it a bit\x01",
            "late for you kids to be out\x01",
            "walking around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x102,
        (
            "#015FPlease, pardon us.\x02\x03",

            "We've simply never been in a castle\x01",
            "like this, and we couldn't resist\x01",
            "the urge to take a look around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "#182FOh, that's certainly understandable.\x02\x03",

            "So, where were you,\x01",
            "half an hour ago?\x02\x03",

            "Please enlighten me, if only\x01",
            "for my own edification.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        "#505FUhh...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Kitchen]\x01",                  # 0
            "[Maid Quarters]\x01",            # 1
            "[Administrative Room]\x01",      # 2
            "[Royal Guard Room]\x01",         # 3
            "[Cellar]\x01",                   # 4
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2971"),
        (1, "loc_2AC4"),
        (2, "loc_2BC5"),
        (3, "loc_2D59"),
        (4, "loc_2EF9"),
        (SWITCH_DEFAULT, "loc_3067"),
    )


    label("loc_2971")


    ChrTalk(    #87
        0x8,
        (
            "#180FOh, that's strange.\x02\x03",

            "I was making my rounds through\x01",
            "there, and I never saw you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#009FW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        (
            "#181FCome, let's not waste time on games.\x02\x03",

            "#188FActually, I've received reports \x01",
            "of you going in and out of the\x01",
            "maid quarters several times.\x02\x03",

            "Do you not think it a bit odd\x01",
            "to be 'looking around' in that\x01",
            "particular place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3067")

    label("loc_2AC4")


    ChrTalk(    #90
        0x8,
        (
            "#180FHa ha... I admire your honesty.\x02\x03",

            "#181FSo let's not waste time on games.\x02\x03",

            "#188FI did, in fact, receive several\x01",
            "reports of you going in and out\x01",
            "of the maid quarters.\x02\x03",

            "Do you not think it a bit odd\x01",
            "to be 'looking around' in that\x01",
            "particular place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3067")

    label("loc_2BC5")


    ChrTalk(    #91
        0x8,
        (
            "#180FAll of the government officials\x01",
            "in the administrative areas went\x01",
            "home quite some time ago.\x02\x03",

            "Might I inquire what, exactly,\x01",
            "you were doing there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#009FW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "#181FCome, let's not waste time on games.\x02\x03",

            "#188FActually, I've received reports \x01",
            "of you going in and out of the\x01",
            "maid quarters several times.\x02\x03",

            "Do you not think it a bit odd\x01",
            "to be 'looking around' in that\x01",
            "particular place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3067")

    label("loc_2D59")


    ChrTalk(    #94
        0x8,
        (
            "#180FMy, that's certainly strange.\x02\x03",

            "The Intelligence Division has\x01",
            "been using that area for some\x01",
            "time now...\x02\x03",

            "I'm fairly certain that you\x01",
            "would have been noticed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#009FW-Well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "#181FCome, let's not waste time on games.\x02\x03",

            "#188FActually, I've received reports \x01",
            "of you going in and out of the\x01",
            "maid quarters several times.\x02\x03",

            "Do you not think it a bit odd\x01",
            "to be 'looking around' in that\x01",
            "particular place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3067")

    label("loc_2EF9")


    ChrTalk(    #97
        0x8,
        (
            "#183FWhat was that...?\x02\x03",

            "And just what do you think you\x01",
            "were doing down there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#009FW-We weren't doing anything\x01",
            "in particular...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "#181FCome, let's not waste time on games.\x02\x03",

            "#188FI've received numerous reports \x01",
            "of you going in and out of the\x01",
            "maid quarters several times.\x02\x03",

            "Do you not think it a bit odd\x01",
            "to be 'looking around' in that\x01",
            "particular place?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3067")

    label("loc_3067")


    ChrTalk(    #100
        0x101,
        "#005FWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        (
            "#012FYou don't think that questioning\x01",
            "someone like that, when you already\x01",
            "have the facts, is a little cruel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "#188FHa ha ha...\x01",
            "I'll take that as a compliment.\x02\x03",

            "So, what business have you\x01",
            "in the maid quarters?\x02\x03",

            "I suggest you answer honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x102,
        "#013FWell, we...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x108, 7350, 9000, 25020, 225)

    NpcTalk(    #104
        0x108,
        "Man's Voice",
        "#3POh! Estelle! Joshua!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #105
        0x108,
        "Man's Voice",
        "#3PYou been here the whole time?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x108, 0x80)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3282():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3282)

    def lambda_3290():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3290)

    def lambda_329E():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_329E)

    def lambda_32AC():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_32AC)

    def lambda_32BA():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_32BA)
    OP_6D(3730, 9000, 21420, 2000)

    def lambda_32D9():

        label("loc_32D9")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_32D9")

    QueueWorkItem2(0x101, 1, lambda_32D9)

    def lambda_32EA():

        label("loc_32EA")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_32EA")

    QueueWorkItem2(0x102, 1, lambda_32EA)

    def lambda_32FB():

        label("loc_32FB")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_32FB")

    QueueWorkItem2(0x8, 1, lambda_32FB)

    def lambda_330C():

        label("loc_330C")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_330C")

    QueueWorkItem2(0xB, 1, lambda_330C)

    def lambda_331D():

        label("loc_331D")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_331D")

    QueueWorkItem2(0xC, 1, lambda_331D)

    ChrTalk(    #106
        0x102,
        "#014FZin...\x02",
    )

    CloseMessageWindow()

    def lambda_333F():
        OP_6D(900, 9000, 19490, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_333F)

    def lambda_3357():
        OP_6E(256, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3357)

    def lambda_3367():
        OP_9E(0xFE, 0x3C, 0x0, 0xBB8, 0x2BC)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3367)
    OP_8E(0x108, 0x758, 0x2328, 0x4B32, 0x7D0, 0x0)
    Sleep(400)
    SetChrChipByIndex(0x108, 7)
    OP_22(0xB2, 0x0, 0x64)
    SetChrSubChip(0x108, 0)
    Sleep(150)
    SetChrSubChip(0x108, 1)
    Sleep(150)
    SetChrSubChip(0x108, 2)
    Sleep(150)
    SetChrSubChip(0x108, 0)
    Sleep(150)
    SetChrSubChip(0x108, 1)
    Sleep(150)
    SetChrSubChip(0x108, 2)
    Sleep(150)
    SetChrSubChip(0x108, 0)
    Sleep(180)
    SetChrSubChip(0x108, 1)
    Sleep(180)
    SetChrSubChip(0x108, 2)
    Sleep(200)
    SetChrSubChip(0x108, 3)
    Sleep(100)
    SetChrSubChip(0x108, 4)
    Sleep(170)

    ChrTalk(    #107
        0x108,
        "#079FWhoa...! Now THAT'S the stuff!\x02",
    )

    SetChrSubChip(0x108, 5)
    Sleep(70)
    SetChrSubChip(0x108, 6)
    Sleep(70)
    SetChrSubChip(0x108, 7)
    Sleep(350)
    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#509FYou're drunk...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x108, 65535)
    OP_0D()
    TurnDirection(0x108, 0x8, 0)
    Sleep(400)

    ChrTalk(    #109
        0x108,
        (
            "#570FOops...heh, sorry...\x02\x03",

            "An' heeeeyyy... If it ain't my\x01",
            "favorite gorgeous officer lady...\x02\x03",

            "#079FNice... Some luck that we\x01",
            "met up again, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x8,
        "#184FI-I suppose...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x108,
        (
            "#078FSo, what's goin' on...?\x02\x03",

            "Are my students here causin'\x01",
            "any trouble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        "#004FSt-students...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x8,
        (
            "#183FNo, it's just that they were in\x01",
            "the maid quarters for a while...\x02\x03",

            "I merely wanted to know their business,\x01",
            "simply as a security precaution.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x108,
        (
            "#079FHmmm, yeah, I totally get'cha.\x02\x03",

            "I just sent 'em off to find some\x01",
            "munchies to go with my booze.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x108, 225, 0)
    Sleep(400)

    ChrTalk(    #115
        0x108,
        (
            "#078FHey, Joshua.\x01",
            "You kids find anythin' to eat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        (
            "#010FNo... The cooks aren't back yet,\x01",
            "I guess.\x02\x03",

            "We went to ask the maid if there\x01",
            "was any way we could get our\x01",
            "hands on something, but no luck.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x108,
        (
            "#571F*sigh* Oh, well. I'll have\x01",
            "to do without, I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #118
        0x108,
        (
            "#570FHey...\x01",
            "I just had a great idea!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x8, 0)
    Sleep(400)

    def lambda_3805():
        OP_9E(0xFE, 0x64, 0x0, 0x3E8, 0x12C)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3805)
    OP_92(0x108, 0x8, 0x320, 0x3E8, 0x0)

    ChrTalk(    #119
        0x108,
        (
            "#079F#4PYou wanna come an' join\x01",
            "me for a drink?\x02\x03",

            "I mean, hey...nothing goes with\x01",
            "drinks like a beautiful lady.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0xB4, 0x1F4, 0xBB8, 0x0)

    ChrTalk(    #120
        0x8,
        (
            "#187FI-I'm afraid I'm busy, so I'll have\x01",
            "to decline your generous offer.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #121
        0x8,
        (
            "#183F#3PMy apologies for the misunderstanding...\x02\x03",

            "...but I would advise you to\x01",
            "return to your room and remain\x01",
            "there for the rest of the night.\x02\x03",

            "I have to investigate any suspicious\x01",
            "activity, you understand.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)

    def lambda_3A03():

        label("loc_3A03")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3A03")

    QueueWorkItem2(0x101, 1, lambda_3A03)

    def lambda_3A14():

        label("loc_3A14")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3A14")

    QueueWorkItem2(0x102, 1, lambda_3A14)

    def lambda_3A25():

        label("loc_3A25")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3A25")

    QueueWorkItem2(0x108, 1, lambda_3A25)

    ChrTalk(    #122
        0x101,
        "#009FO-Of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        (
            "#015FIt IS late... We should probably\x01",
            "just get to bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x8,
        (
            "#180F#3PHa ha... Very good, then.\x02\x03",

            "#181FNow, if you'll excuse us...\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x8, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0xB, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0x9)

    def lambda_3AF1():
        OP_6D(710, 9000, 17230, 3000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_3AF1)
    Sleep(1500)
    OP_44(0x108, 0xFF)
    OP_8C(0x108, 180, 0)
    WaitChrThread(0x8, 0x2)
    Sleep(2000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_6D(710, 9000, 18930, 1000)
    Sleep(400)

    ChrTalk(    #125
        0x108,
        (
            "#570FAww...denied.\x02\x03",

            "#571FOh, well... Might as well just\x01",
            "go back to the room.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x108, 400)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #126
        0x101,
        "#506FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x102,
        "#010FWe'll go with you.\x02",
    )

    CloseMessageWindow()
    FadeToBright(1500, 0)
    OP_0D()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4262   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_2538 end

    def Function_9_3BE8(): pass

    label("Function_9_3BE8")

    OP_8E(0xFE, 0xFFFFF9C0, 0x2328, 0x4A38, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF9C0, 0x2328, 0x3C6E, 0xBB8, 0x0)
    OP_8E(0xFE, 0x64, 0x2328, 0x375A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x10E0, 0x2328, 0x375A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x2058, 0x1C52, 0x34A8, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3552, 0x1194, 0x25E4, 0xBB8, 0x0)
    Return()

    # Function_9_3BE8 end

    def Function_10_3C61(): pass

    label("Function_10_3C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DF2")
    EventBegin(0x1)
    OP_4A(0xD, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D38")
    TurnDirection(0xD, 0x0, 400)

    ChrTalk(    #128
        0xD,
        (
            "Well, if it isn't Hilda.\x01",
            "What do you need from us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xD,
        (
            "This is the Intelligence Division's\x01",
            "office. Please, it's best if you\x01",
            "keep your distance.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    OP_8C(0xD, 270, 0)
    Jump("loc_3DE7")

    label("loc_3D38")

    TurnDirection(0xD, 0x0, 400)

    ChrTalk(    #130
        0xD,
        (
            "This is the Intelligence Division's\x01",
            "office. Authorized personnel only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xD,
        (
            "Keep your distance, unless you're\x01",
            "keen on getting arrested.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    OP_8C(0xD, 270, 0)

    label("loc_3DE7")

    OP_4B(0xD, 255)
    Sleep(50)
    EventEnd(0x4)

    label("loc_3DF2")

    Return()

    # Function_10_3C61 end

    def Function_11_3DF3(): pass

    label("Function_11_3DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E00")
    Return()

    label("loc_3E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_3EC0")
    EventBegin(0x1)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)

    ChrTalk(    #132
        0x11,
        (
            "Hey, what are you doing?\x01",
            "The castle gate's sealed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x10,
        (
            "I'm sorry, but you'll have to\x01",
            "stay in the castle for the\x01",
            "time being.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    OP_8C(0x10, 0, 0)
    OP_8C(0x11, 0, 0)
    OP_4B(0x10, 255)
    OP_4B(0x11, 255)
    Jump("loc_40B0")

    label("loc_3EC0")

    EventBegin(0x1)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FB1")
    TurnDirection(0xE, 0x0, 400)
    TurnDirection(0xF, 0x0, 400)

    ChrTalk(    #134
        0xE,
        (
            "Oh, hello, Hilda. What brings\x01",
            "you out at this hour?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xF,
        (
            "As instructed, the castle gate\x01",
            "is currently sealed, to help\x01",
            "ensure security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xF,
        (
            "No one is allowed in or out\x01",
            "without special permission.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4086")

    label("loc_3FB1")

    TurnDirection(0xE, 0x0, 400)
    TurnDirection(0xF, 0x0, 400)

    ChrTalk(    #137
        0xF,
        (
            "The castle gate is currently sealed,\x01",
            "to help ensure security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xE,
        (
            "Please, feel free to walk around\x01",
            "the castle for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xE,
        (
            "I'm sorry for any inconvenience,\x01",
            "but nothing can be done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4086")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    OP_8C(0xE, 0, 0)
    OP_8C(0xF, 0, 0)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)

    label("loc_40B0")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_11_3DF3 end

    def Function_12_40B8(): pass

    label("Function_12_40B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_40C5")
    Return()

    label("loc_40C5")

    EventBegin(0x1)
    OP_4A(0x12, 255)
    TurnDirection(0x12, 0x0, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4173")

    ChrTalk(    #140
        0x12,
        (
            "There's currently an important meeting\x01",
            "being held in the audience chamber.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x12,
        (
            "I apologize, but you'll have to\x01",
            "wait before you can enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4211")

    label("loc_4173")


    ChrTalk(    #142
        0x12,
        (
            "There's currently an important meeting\x01",
            "being held in the Throne Room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x12,
        (
            "If you were hoping to look\x01",
            "around, I'm afraid you'll\x01",
            "have to try again later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4211")

    OP_8C(0x12, 180, 0)
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    OP_4B(0x12, 255)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_12_40B8 end

    def Function_13_4238(): pass

    label("Function_13_4238")

    TalkBegin(0xFE)

    ChrTalk(    #144
        0x10,
        "I feel almost like I've come home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x10,
        (
            "As the Royal Army, it's our duty\x01",
            "to safeguard the castle.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_4238 end

    def Function_14_42A6(): pass

    label("Function_14_42A6")

    TalkBegin(0xFE)

    ChrTalk(    #146
        0x11,
        (
            "I can't believe that Colonel Richard\x01",
            "was the man behind the coup...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x11,
        (
            "As a fellow soldier, I really\x01",
            "just don't know what to say.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_42A6 end

    def Function_15_4336(): pass

    label("Function_15_4336")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43D5")

    ChrTalk(    #148
        0x12,
        (
            "There's currently an important meeting\x01",
            "being held in the Throne Room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x12,
        (
            "I apologize, but you'll have to\x01",
            "wait before you can enter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4473")

    label("loc_43D5")


    ChrTalk(    #150
        0x12,
        (
            "There's currently an important meeting\x01",
            "being held in the Throne Room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x12,
        (
            "If you were hoping to look\x01",
            "around, I'm afraid you'll\x01",
            "have to try again later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4473")

    TalkEnd(0xFE)
    Return()

    # Function_15_4336 end

    SaveToFile()

Try(main)
