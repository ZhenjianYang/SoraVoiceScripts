from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4210   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4210.x',
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
        'ED6_DT07/CH01330 ._CH',             # 06
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
        'ED6_DT07/CH01330P._CP',             # 06
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
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
        TalkScenaIndex      = 12,
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
        TalkScenaIndex      = 13,
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


    ScpFunction(
        "Function_0_292",          # 00, 0
        "Function_1_31D",          # 01, 1
        "Function_2_32C",          # 02, 2
        "Function_3_3FA",          # 03, 3
        "Function_4_1753",         # 04, 4
        "Function_5_18D0",         # 05, 5
        "Function_6_1938",         # 06, 6
        "Function_7_228A",         # 07, 7
        "Function_8_22B3",         # 08, 8
        "Function_9_33F0",         # 09, 9
        "Function_10_3469",        # 0A, 10
        "Function_11_35FB",        # 0B, 11
        "Function_12_38C0",        # 0C, 12
        "Function_13_392E",        # 0D, 13
    )


    def Function_0_292(): pass

    label("Function_0_292")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2A2"),
        (108, "loc_2B8"),
        (SWITCH_DEFAULT, "loc_2CE"),
    )


    label("loc_2A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B5")
    OP_A2(0x639)
    Event(0, 3)

    label("loc_2B5")

    Jump("loc_2CE")

    label("loc_2B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2CB")
    OP_A2(0x641)
    Event(0, 6)

    label("loc_2CB")

    Jump("loc_2CE")

    label("loc_2CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F8")
    SetChrChipByIndex(0x0, 3)
    SetChrChipByIndex(0x1, 4)
    SetChrChipByIndex(0x138, 5)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_31C")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x10, 0x80)

    label("loc_31C")

    Return()

    # Function_0_292 end

    def Function_1_31D(): pass

    label("Function_1_31D")

    OP_71(0x0, 0x2)
    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_31D end

    def Function_2_32C(): pass

    label("Function_2_32C")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_351")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3E4")

    label("loc_351")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36A")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3E4")

    label("loc_36A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_383")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3E4")

    label("loc_383")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39C")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3E4")

    label("loc_39C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B5")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3E4")

    label("loc_3B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CE")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3E4")

    label("loc_3CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E4")
    OP_99(0xFE, 0x6, 0x7, 0x546)

    label("loc_3E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F9")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3E4")

    label("loc_3F9")

    Return()

    # Function_2_32C end

    def Function_3_3FA(): pass

    label("Function_3_3FA")

    EventBegin(0x0)
    SetChrPos(0x101, 520, 0, -22530, 0)
    SetChrPos(0x102, -1610, 0, -22470, 0)
    SetChrPos(0x108, -290, 0, -21870, 0)
    OP_6D(-210, 0, -19730, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(10000, 0)
    OP_6E(280, 0)

    def lambda_472():
        OP_6D(180, 9000, 14710, 10000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_472)

    def lambda_48A():
        OP_67(0, 4950, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48A)

    def lambda_4A2():
        OP_6B(2190, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4A2)

    def lambda_4B2():
        OP_6C(45000, 12000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4B2)

    def lambda_4C2():
        OP_6E(899, 10000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4C2)
    FadeToBright(2000, 0)
    Sleep(12000)
    Fade(1000)
    OP_6D(30, 0, -22200, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        "#000FWhoaaa...\x02",
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
            "#070FIt's not just pretty...\x01",
            "It's got history.\x02\x03",

            "I can really feel the traditions\x01",
            "and rules of the old kingdom here.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 770, 0, -9870, 180)
    SetChrPos(0x9, -280, 0, -9260, 180)

    ChrTalk(    #3
        0x8,
        "Welcome to Grancel Castle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "You are Zin and his team,\x01",
            "correct?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_67F():
        OP_8E(0xFE, 0xFFFFFFB0, 0x0, 0xFFFFB41A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_67F)

    def lambda_69A():
        OP_8E(0xFE, 0xFFFFFCAE, 0x0, 0xFFFFB758, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_69A)
    OP_6D(130, 0, -20310, 3000)

    ChrTalk(    #5
        0x101,
        "#000F(Erk... Captain Amalthea...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#010F(This isn't really unexpected,\x01",
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
            "#180FHa ha... Pardon me.\x02\x03",

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
            "#070FYou're too kind, really.\x02\x03",

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
            "#180FMy, but you are the flatterer.\x02\x03",

            "But I'm not so young as\x01",
            "your bracer friends.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#000F...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#010F...\x02",
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
        "#000F...Yeah, I guess it has.\x02",
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
            "#180FUnfortunately, the matter concerning\x01",
            "Professor Russell is yet to be resolved.\x02\x03",

            "It appears that he and his grand-\x01",
            "daughter were abducted by a group\x01",
            "of nefarious individuals.\x02\x03",

            "You wouldn't happen to know\x01",
            "anything about that, would you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#000FI-I'm afraid not...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#010FWe left that case up to the\x01",
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
            "#180FI see... Ha ha...\x01",
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
        "#000F(Wh-What the hell's with her...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#010FUnderstood.\x02\x03",

            "We trust you to take care\x01",
            "of the professor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "#180FOh, absolutely...\x02\x03",

            "Now, we must show you to\x01",
            "your rooms.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #23
        0x8,
        (
            "#180FShea, if you would please\x01",
            "do the honors?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #24
        0x9,
        "Yes, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#180FSee to their needs...\x02\x03",

            "...but do not bore them with\x01",
            "any idle chatter.\x02\x03",

            "Do I make myself clear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x9,
        "Y-Yes, ma'am... I understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        "#180FHa ha... Very good.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x102, 400)
    TurnDirection(0x8, 0x108, 400)

    ChrTalk(    #28
        0x8,
        (
            "#180FNow, everyone...\x01",
            "I hope you enjoy your evening.\x02\x03",

            "For my part, I must bid you farewell.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EA5():

        label("loc_EA5")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EA5")

    QueueWorkItem2(0x108, 1, lambda_EA5)

    def lambda_EB6():

        label("loc_EB6")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EB6")

    QueueWorkItem2(0x101, 1, lambda_EB6)

    def lambda_EC7():

        label("loc_EC7")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_EC7")

    QueueWorkItem2(0x102, 1, lambda_EC7)
    OP_8E(0x8, 0x730, 0x0, 0xFFFFC2F2, 0x7D0, 0x0)

    def lambda_EEC():
        OP_8E(0xFE, 0x1CC0, 0x0, 0xFFFFD88C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EEC)
    Sleep(1500)

    ChrTalk(    #29
        0x108,
        (
            "#070FMmm-mm-mmm.\x01",
            "Now that is one fine woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#000FI hate to say this, Zin, but\x01",
            "your taste in women is crap.\x02\x03",

            "There's nothing 'fine' about\x01",
            "that fox-faced harpy.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    TurnDirection(0x102, 0x108, 400)

    ChrTalk(    #31
        0x102,
        (
            "#010FI think that might just be his\x01",
            "favorite type of woman.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x108,
        (
            "#070FHa ha... I just tend to find that women\x01",
            "like that turn out be pretty good people,\x01",
            "once you peel back a few layers.\x02\x03",

            "So to speak...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #33
        0x101,
        (
            "#000FYou're hopeless.\x02\x03",

            "Not that it matters, but you \x01",
            "really do sound like a dirty\x01",
            "old man sometimes.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1108():
        TurnDirection(0xFE, 0x101, 800)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1108)

    ChrTalk(    #34
        0x108,
        "#070FOh, my honor!\x02",
    )

    CloseMessageWindow()

    def lambda_112E():
        OP_6D(-240, 0, -20830, 1000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_112E)
    OP_8E(0x9, 0xFFFFFEFC, 0x0, 0xFFFFB186, 0x5DC, 0x0)
    TurnDirection(0x9, 0x108, 400)

    ChrTalk(    #35
        0x9,
        "U-Umm...\x02",
    )

    CloseMessageWindow()

    def lambda_116F():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_116F)

    def lambda_117D():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_117D)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #36
        0x101,
        (
            "#000FOh, sorry about that.\x02\x03",

            "You were supposed to show\x01",
            "us to our room, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        "Yes, please allow me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        (
            "Pardon my not saying before,\x01",
            "but I am Shea, a maid here at\x01",
            "the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "I will be at your service this\x01",
            "evening, from the dinner party\x01",
            "until the morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "If anything is not to your\x01",
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
            "Certainly.\x01",
            "It's on the second floor.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x9, 0x1, 0x0, 0x4)
    Sleep(50)
    OP_8E(0x108, 0xFFFFFF10, 0x0, 0xFFFFAEA2, 0xBB8, 0x0)
    OP_6A(0x108)
    OP_43(0x108, 0x1, 0x0, 0x4)
    Sleep(150)
    OP_43(0x102, 0x1, 0x0, 0x4)
    Sleep(400)
    OP_43(0x101, 0x1, 0x0, 0x4)
    Sleep(12000)
    OP_66(0x0)
    WaitChrThread(0x9, 0x1)

    def lambda_13BE():
        OP_6E(196, 3000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_13BE)

    def lambda_13CE():
        OP_8E(0xFE, 0x32, 0x2328, 0x5A6E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_13CE)
    WaitChrThread(0x108, 0x1)

    def lambda_13EE():
        OP_8E(0xFE, 0x410, 0x2328, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_13EE)
    WaitChrThread(0x102, 0x1)

    def lambda_140E():
        OP_8E(0xFE, 0xFFFFFB96, 0x2328, 0x524E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_140E)
    WaitChrThread(0x101, 0x1)

    def lambda_142E():
        OP_8E(0xFE, 0xFFFFFF92, 0x2328, 0x4FBA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_142E)

    ChrTalk(    #44
        0x101,
        (
            "#000FOh, WOW...\x02\x03",

            "Get a load of that chandelier!\x01",
            "Talk about classy...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1493():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1493)

    ChrTalk(    #45
        0x102,
        (
            "#010FHush, Estelle.\x02\x03",

            "What's that way...?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_14CF():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14CF)

    def lambda_14DD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_14DD)

    def lambda_14EB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_14EB)
    OP_8C(0x9, 0, 400)

    ChrTalk(    #46
        0x9,
        "That's the Throne Room.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "Queen Alicia uses it to receive\x01",
            "personal guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "It hasn't seen much use in\x01",
            "recent days, though...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_158A():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_158A)

    def lambda_1598():
        TurnDirection(0xFE, 0x9, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1598)
    TurnDirection(0x102, 0x9, 400)

    ChrTalk(    #49
        0x102,
        "#010F...I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x108,
        (
            "#070FBut is the queen's condition\x01",
            "really that bad?\x02\x03",

            "Isn't the Birthday Celebration\x01",
            "coming up soon?\x02",
        )
    )

    CloseMessageWindow()
    ClearMapFlags(0x1)
    OP_69(0x102, 0x3E8)
    OP_6A(0x102)
    TurnDirection(0x9, 0x108, 400)

    ChrTalk(    #51
        0x9,
        "O-Oh, no...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "It's just that it's the head\x01",
            "maid who tends to her in the\x01",
            "Royal Keep of late.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "I shouldn't speak on subjects\x01",
            "about which I'm unfamiliar...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 0)

    ChrTalk(    #54
        0x9,
        "C-Come then, shall we?\x02",
    )

    CloseMessageWindow()
    OP_66(0x1)
    OP_43(0x9, 0x1, 0x0, 0x5)
    Sleep(420)
    OP_43(0x102, 0x1, 0x0, 0x5)
    Sleep(150)
    OP_43(0x101, 0x1, 0x0, 0x5)
    Sleep(400)
    OP_43(0x108, 0x1, 0x0, 0x5)
    Sleep(3000)
    OP_28(0x49, 0x1, 0x80)
    OP_28(0x49, 0x1, 0x100)
    OP_28(0x49, 0x1, 0x200)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4222   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3FA end

    def Function_4_1753(): pass

    label("Function_4_1753")

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

    # Function_4_1753 end

    def Function_5_18D0(): pass

    label("Function_5_18D0")

    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFFF1E6, 0x2328, 0x5DD4, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFE0E8, 0x2328, 0x6504, 0xBB8, 0x1)
    OP_8E(0xFE, 0xFFFFDA9E, 0x2328, 0x65C2, 0xBB8, 0x1)

    def lambda_1917():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1917)
    OP_8E(0xFE, 0xFFFFCD9C, 0x2328, 0x65C2, 0xBB8, 0x1)
    Return()

    # Function_5_18D0 end

    def Function_6_1938(): pass

    label("Function_6_1938")

    EventBegin(0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xA, -6640, 8000, 13770, 80)
    SetChrPos(0x8, -7900, 7500, 13100, 62)
    SetChrPos(0x101, -7920, 9000, 24630, 118)
    SetChrPos(0x102, -7520, 9000, 25920, 118)

    ChrTalk(    #55
        0xA,
        "#110FOh, it's you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#000FWha...!\x02",
    )

    CloseMessageWindow()

    def lambda_19BA():
        OP_6D(-3860, 9000, 20630, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_19BA)
    Sleep(1000)

    def lambda_19D7():
        OP_8E(0xFE, 0xFFFFF813, 0x2328, 0x3A20, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_19D7)

    def lambda_19F2():
        OP_8E(0xFE, 0xFFFFF72C, 0x2328, 0x35CA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_19F2)
    WaitChrThread(0xA, 0x1)

    def lambda_1A12():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1A12)
    WaitChrThread(0x8, 0x1)

    def lambda_1A25():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A25)

    def lambda_1A33():

        label("loc_1A33")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1A33")

    QueueWorkItem2(0x101, 1, lambda_1A33)

    def lambda_1A44():

        label("loc_1A44")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1A44")

    QueueWorkItem2(0x102, 1, lambda_1A44)

    ChrTalk(    #57
        0x102,
        "#010FColonel Richard...\x02",
    )

    CloseMessageWindow()

    def lambda_1A72():
        OP_6D(-7040, 9000, 25530, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1A72)
    OP_43(0xA, 0x1, 0x0, 0x7)
    Sleep(300)
    OP_43(0x8, 0x1, 0x0, 0x7)
    WaitChrThread(0xA, 0x1)

    def lambda_1AA2():

        label("loc_1AA2")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_1AA2")

    QueueWorkItem2(0xA, 1, lambda_1AA2)

    def lambda_1AB3():
        OP_8E(0xFE, 0xFFFFE778, 0x2328, 0x6324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1AB3)
    WaitChrThread(0x8, 0x1)

    def lambda_1AD3():

        label("loc_1AD3")

        OP_8C(0xFE, 270, 0)
        OP_48()
        Jump("loc_1AD3")

    QueueWorkItem2(0x8, 1, lambda_1AD3)
    WaitChrThread(0xA, 0x2)

    ChrTalk(    #58
        0xA,
        (
            "#110FHa ha...\x01",
            "Estelle and Joshua.\x02\x03",

            "I can scarcely recall the last\x01",
            "time we spoke in person.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x101,
        "#000F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
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

    ChrTalk(    #61
        0xA,
        (
            "#110FI realize that we exchanged few\x01",
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

    ChrTalk(    #62
        0x101,
        "#000FH-How'd you find THAT out?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        (
            "#110FHa ha. Please understand, I'm not\x01",
            "trying to show off the Intelligence\x01",
            "Division's capabilities.\x02\x03",

            "I'm greatly indebted to him from\x01",
            "our time together in the army.\x02\x03",

            "Indeed...more than words\x01",
            "can properly express.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#000F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xA,
        (
            "#110FMight I persuade you to stay\x01",
            "a while and talk?\x02\x03",

            "I've been hoping to speak with\x01",
            "you two for quite some time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#000FHuh?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x102,
        "#010F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 400)

    ChrTalk(    #68
        0x8,
        (
            "#180FP-Pardon me, Colonel...\x02\x03",

            "...but don't you have a meeting\x01",
            "with His Grace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xA,
        (
            "#110FI don't mind being a bit late.\x02\x03",

            "Ahh, yes. If we're going to\x01",
            "talk, why don't we use the\x01",
            "lounge inside?\x02\x03",

            "I'll mix you up a couple\x01",
            "of virgin cocktails.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x8,
        "#180FI-I'll prepare them, sir!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x8, 400)

    ChrTalk(    #71
        0xA,
        (
            "#110FNo, that won't be necessary.\x02\x03",

            "I want you to go to His Excellency\x01",
            "and inform him that I'll be delayed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        "#180FY-Yes, sir...\x02",
    )

    CloseMessageWindow()

    def lambda_204D():

        label("loc_204D")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_204D")

    QueueWorkItem2(0xA, 1, lambda_204D)

    def lambda_205E():

        label("loc_205E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_205E")

    QueueWorkItem2(0x101, 1, lambda_205E)

    def lambda_206F():

        label("loc_206F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_206F")

    QueueWorkItem2(0x102, 1, lambda_206F)
    OP_62(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x8, 0x101, 800)

    ChrTalk(    #73
        0x8,
        "#180F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        "#000F(*gulp*)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        "#180FPardon me, then.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xFFFFFF6A, 0x2328, 0x6EC8, 0xBB8, 0x0)

    def lambda_20EE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_20EE)
    OP_8E(0x8, 0xFFFFFFBA, 0x2328, 0x8200, 0xBB8, 0x0)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_8C(0xA, 270, 400)

    def lambda_2127():

        label("loc_2127")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_2127")

    QueueWorkItem2(0x101, 1, lambda_2127)

    def lambda_2138():

        label("loc_2138")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_2138")

    QueueWorkItem2(0x102, 1, lambda_2138)

    ChrTalk(    #76
        0xA,
        (
            "#110FNow, then... Shall we retire\x01",
            "to the lounge?\x02\x03",

            "Please, follow me.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2193():
        OP_8E(0xFE, 0x23AA, 0x2328, 0x64B4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2193)
    Sleep(300)
    OP_6D(-5680, 9000, 25260, 2000)

    ChrTalk(    #77
        0x101,
        (
            "#000FUh...\x02\x03",

            "Joshua...? What should we do?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        (
            "#010FI don't see where we have much\x01",
            "choice but to follow him.\x02\x03",

            "We'll be a little late, but we\x01",
            "can talk to the head maid later.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x4A, 0x1, 0x8)
    OP_28(0x4A, 0x1, 0x10)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4221   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1938 end

    def Function_7_228A(): pass

    label("Function_7_228A")

    OP_8E(0xFE, 0xFFFFF8F8, 0x2328, 0x5168, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFED7C, 0x2328, 0x5CE4, 0xBB8, 0x0)
    Return()

    # Function_7_228A end

    def Function_8_22B3(): pass

    label("Function_8_22B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22C0")
    Return()

    label("loc_22C0")

    EventBegin(0x0)
    OP_A2(0x647)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, -70, 9000, 27870, 180)
    SetChrPos(0xB, -800, 9000, 28970, 180)
    SetChrPos(0xC, 530, 9000, 28970, 180)

    ChrTalk(    #79
        0x8,
        (
            "...What, might I inquire, are\x01",
            "you doing at this late hour?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_237B():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_237B)

    def lambda_2389():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2389)
    OP_6D(10, 9000, 27580, 3000)
    AddParty(0x7, 0xFF)
    SetChrPos(0x101, -550, 9000, 16309, 0)
    SetChrPos(0x102, 670, 9000, 16190, 0)
    SetChrPos(0x108, 6350, 9000, 24020, 225)
    SetChrFlags(0x108, 0x80)

    def lambda_23E3():
        OP_8E(0xFE, 0x8C, 0x2328, 0x4DE4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_23E3)

    def lambda_23FE():
        OP_8E(0xFE, 0xFFFFFDBC, 0x2328, 0x5294, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_23FE)

    def lambda_2419():
        OP_8E(0xFE, 0x33E, 0x2328, 0x529E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2419)
    OP_6D(100, 9000, 18910, 3000)

    ChrTalk(    #80
        0x101,
        "#000FAh...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        "#010FCaptain Amalthea...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #82
        0x8,
        (
            "#180FHeehee...\x01",
            "Good evening.\x02\x03",

            "I realize that you've been invited here...\x02\x03",

            "But don't you think it a bit\x01",
            "late for you kids to be out\x01",
            "walking around?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x102,
        (
            "#010FPlease, pardon us.\x02\x03",

            "We've simply never been in a castle\x01",
            "like this, and we couldn't resist\x01",
            "the urge to take a look around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "#180FOh, that's certainly understandable.\x02\x03",

            "So, where were you,\x01",
            "half an hour ago?\x02\x03",

            "Please enlighten me, if only\x01",
            "for my own edification.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#000FUhh...\x02",
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
        (0, "loc_26D5"),
        (1, "loc_2746"),
        (2, "loc_2773"),
        (3, "loc_2825"),
        (4, "loc_28E3"),
        (SWITCH_DEFAULT, "loc_2970"),
    )


    label("loc_26D5")


    ChrTalk(    #86
        0x8,
        (
            "#180FOh, that's strange.\x02\x03",

            "I was making my rounds through\x01",
            "there, and I never saw you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        "#000FW-Well...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2970")

    label("loc_2746")


    ChrTalk(    #88
        0x8,
        "#180FHa ha... I admire your honesty.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2970")

    label("loc_2773")


    ChrTalk(    #89
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

    ChrTalk(    #90
        0x101,
        "#000FW-Well...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2970")

    label("loc_2825")


    ChrTalk(    #91
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

    ChrTalk(    #92
        0x101,
        "#000FW-Well...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2970")

    label("loc_28E3")


    ChrTalk(    #93
        0x8,
        (
            "#180FWhat was that...?\x02\x03",

            "And just what do you think you\x01",
            "were doing down there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        (
            "#000FW-We weren't doing anything\x01",
            "in particular...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2970")

    label("loc_2970")


    ChrTalk(    #95
        0x8,
        (
            "#180FCome, let's not waste time on games.\x02\x03",

            "I've received numerous reports \x01",
            "of you going in and out of the\x01",
            "maid quarters several times.\x02\x03",

            "Do you not think it a bit odd\x01",
            "to be 'looking around' in that\x01",
            "particular place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#000FWha...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        (
            "#010FYou don't think that questioning\x01",
            "someone like that, when you already\x01",
            "have the facts, is a little cruel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x8,
        (
            "#180FHa ha ha...\x01",
            "I'll take that as a compliment.\x02\x03",

            "So, what business have you\x01",
            "in the maid quarters?\x02\x03",

            "I suggest you answer honestly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x102,
        "#010FWell, we...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x108,
        "Oh! Estelle! Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x108,
        "You been here the whole time?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x108, 0x80)

    def lambda_2BB6():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2BB6)

    def lambda_2BC4():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BC4)

    def lambda_2BD2():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2BD2)

    def lambda_2BE0():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2BE0)

    def lambda_2BEE():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2BEE)
    OP_6D(3230, 9000, 20920, 2000)

    def lambda_2C0D():

        label("loc_2C0D")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2C0D")

    QueueWorkItem2(0x101, 1, lambda_2C0D)

    def lambda_2C1E():

        label("loc_2C1E")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2C1E")

    QueueWorkItem2(0x102, 1, lambda_2C1E)

    def lambda_2C2F():

        label("loc_2C2F")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2C2F")

    QueueWorkItem2(0x8, 1, lambda_2C2F)

    def lambda_2C40():

        label("loc_2C40")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2C40")

    QueueWorkItem2(0xB, 1, lambda_2C40)

    def lambda_2C51():

        label("loc_2C51")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_2C51")

    QueueWorkItem2(0xC, 1, lambda_2C51)

    ChrTalk(    #102
        0x102,
        "#010FZin...\x02",
    )

    CloseMessageWindow()

    def lambda_2C73():
        OP_6D(900, 9000, 19490, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C73)

    def lambda_2C8B():
        OP_6E(256, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2C8B)

    def lambda_2C9B():
        OP_9E(0xFE, 0x3C, 0x0, 0x1388, 0x2BC)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2C9B)
    OP_8E(0x108, 0x758, 0x2328, 0x4B32, 0x7D0, 0x0)
    SetChrChipByIndex(0x108, 7)
    OP_99(0x108, 0x0, 0x7, 0x7D0)

    ChrTalk(    #103
        0x101,
        "#000FYou're drunk...\x02",
    )

    CloseMessageWindow()
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x108, 65535)
    TurnDirection(0x108, 0x8, 400)

    ChrTalk(    #104
        0x108,
        (
            "#070FOops...heh, sorry...\x02\x03",

            "An' heeeeyyy... If it ain't my\x01",
            "favorite gorgeous officer lady...\x02\x03",

            "Nice... Some luck that we\x01",
            "met up again, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x8,
        "#180FI-I suppose...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x108,
        (
            "#070FSo, what's goin' on...?\x02\x03",

            "Are my students here causin'\x01",
            "any trouble?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#000FSt-students...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x8,
        (
            "#180FNo, it's just that they were in\x01",
            "the maid quarters for a while...\x02\x03",

            "I merely wanted to know their business,\x01",
            "simply as a security precaution.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x102, 400)

    ChrTalk(    #109
        0x108,
        (
            "#070FHmmm, yeah, I totally get'cha.\x02\x03",

            "I just sent 'em off to find some\x01",
            "munchies to go with my booze.\x02\x03",

            "Hey, Joshua.\x01",
            "You kids find anythin' to eat?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
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

    ChrTalk(    #111
        0x108,
        (
            "#070F*sigh* Oh, well. I'll have\x01",
            "to do without, I guess.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x108, 0x8, 400)
    Sleep(1000)

    ChrTalk(    #112
        0x108,
        (
            "#070FHey...\x01",
            "I just had a great idea!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3065():
        OP_9E(0xFE, 0x64, 0x0, 0xBB8, 0x12C)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_3065)
    OP_92(0x108, 0x8, 0x258, 0x3E8, 0x0)

    ChrTalk(    #113
        0x108,
        (
            "#070FYou wanna come an' join\x01",
            "me for a drink?\x02\x03",

            "I mean, hey...nothing goes with\x01",
            "drinks like a beautiful lady.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_94(0x1, 0x8, 0xB4, 0x258, 0xBB8, 0x0)
    Sleep(1000)

    ChrTalk(    #114
        0x8,
        (
            "#180FI-I'm afraid I'm busy, so I'll have\x01",
            "to decline your generous offer.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #115
        0x8,
        (
            "#180FMy apologies for the misunderstanding...\x02\x03",

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

    def lambda_3262():

        label("loc_3262")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3262")

    QueueWorkItem2(0x101, 1, lambda_3262)

    def lambda_3273():

        label("loc_3273")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3273")

    QueueWorkItem2(0x102, 1, lambda_3273)

    def lambda_3284():

        label("loc_3284")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_3284")

    QueueWorkItem2(0x108, 1, lambda_3284)

    ChrTalk(    #116
        0x101,
        "#000FO-Of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        (
            "#010FIt IS late... We should probably\x01",
            "just get to bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x8,
        (
            "#180FHa ha... Very good, then.\x02\x03",

            "Now, if you'll excuse us...\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x8, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0xB, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0xC, 0x1, 0x0, 0x9)
    OP_6D(710, 9000, 17230, 3000)
    Sleep(500)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)

    ChrTalk(    #119
        0x108,
        (
            "#070FAww...denied.\x02\x03",

            "Oh, well... Might as well just\x01",
            "go back to the room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#000FR-Right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        "#010FWe'll go with you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4222   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_22B3 end

    def Function_9_33F0(): pass

    label("Function_9_33F0")

    OP_8E(0xFE, 0xFFFFF9C0, 0x2328, 0x4A38, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFFF9C0, 0x2328, 0x3C6E, 0xBB8, 0x0)
    OP_8E(0xFE, 0x64, 0x2328, 0x375A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x10E0, 0x2328, 0x375A, 0xBB8, 0x0)
    OP_8E(0xFE, 0x2058, 0x1C52, 0x34A8, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3552, 0x1194, 0x25E4, 0xBB8, 0x0)
    Return()

    # Function_9_33F0 end

    def Function_10_3469(): pass

    label("Function_10_3469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35FA")
    EventBegin(0x1)
    OP_4A(0xD, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3540")
    TurnDirection(0xD, 0x0, 400)

    ChrTalk(    #122
        0xD,
        (
            "Well, if it isn't Hilda.\x01",
            "What do you need from us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
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
    Jump("loc_35EF")

    label("loc_3540")

    TurnDirection(0xD, 0x0, 400)

    ChrTalk(    #124
        0xD,
        (
            "This is the Intelligence Division's\x01",
            "office. Authorized personnel only.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xD,
        (
            "Keep your distance, unless you're\x01",
            "keen on getting arrested.\x02",
        )
    )

    CloseMessageWindow()
    OP_90(0x0, 0xFFFFFA24, 0x0, 0x0, 0xBB8, 0x0)
    OP_8C(0xD, 270, 0)

    label("loc_35EF")

    OP_4B(0xD, 255)
    Sleep(50)
    EventEnd(0x4)

    label("loc_35FA")

    Return()

    # Function_10_3469 end

    def Function_11_35FB(): pass

    label("Function_11_35FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3608")
    Return()

    label("loc_3608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_36C8")
    EventBegin(0x1)
    OP_4A(0x10, 255)
    OP_4A(0x11, 255)

    ChrTalk(    #126
        0x11,
        (
            "Hey, what are you doing?\x01",
            "The castle gate's sealed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
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
    Jump("loc_38B8")

    label("loc_36C8")

    EventBegin(0x1)
    OP_4A(0xE, 255)
    OP_4A(0xF, 255)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x37)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37B9")
    TurnDirection(0xE, 0x0, 400)
    TurnDirection(0xF, 0x0, 400)

    ChrTalk(    #128
        0xE,
        (
            "Oh, hello, Hilda. What brings\x01",
            "you out at this hour?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xF,
        (
            "As instructed, the castle gate\x01",
            "is currently sealed, to help\x01",
            "ensure security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xF,
        (
            "No one is allowed in or out\x01",
            "without special permission.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_388E")

    label("loc_37B9")

    TurnDirection(0xE, 0x0, 400)
    TurnDirection(0xF, 0x0, 400)

    ChrTalk(    #131
        0xF,
        (
            "The castle gate is currently sealed,\x01",
            "to help ensure security.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xE,
        (
            "Please, feel free to walk around\x01",
            "the castle for the time being.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xE,
        (
            "I'm sorry for any inconvenience,\x01",
            "but nothing can be done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_388E")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    OP_8C(0xE, 0, 0)
    OP_8C(0xF, 0, 0)
    OP_4B(0xE, 255)
    OP_4B(0xF, 255)

    label("loc_38B8")

    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_11_35FB end

    def Function_12_38C0(): pass

    label("Function_12_38C0")

    TalkBegin(0xFE)

    ChrTalk(    #134
        0x10,
        "I feel almost like I've come home.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x10,
        (
            "As the Royal Army, it's our duty\x01",
            "to safeguard the castle.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_38C0 end

    def Function_13_392E(): pass

    label("Function_13_392E")

    TalkBegin(0xFE)

    ChrTalk(    #136
        0x11,
        (
            "I can't believe that Colonel Richard\x01",
            "was the man behind the coup...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x11,
        (
            "As a fellow soldier, I really\x01",
            "just don't know what to say.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_392E end

    SaveToFile()

Try(main)
