from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4138   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4138.x',
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
        'Ambassador Crainagh',                  # 9
        'Major Vander',                         # 10
        'Secretary Barkley',                    # 11
        'Jerrold',                              # 12
        'Councilor Alfre',                      # 13
        'Camilla',                              # 14
        'Nathan',                               # 15
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
        'ED6_DT27/CH03713 ._CH',             # 00
        'ED6_DT27/CH03570 ._CH',             # 01
        'ED6_DT07/CH01560 ._CH',             # 02
        'ED6_DT07/CH01570 ._CH',             # 03
        'ED6_DT07/CH01020 ._CH',             # 04
        'ED6_DT07/CH01350 ._CH',             # 05
        'ED6_DT07/CH01570 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT27/CH03713P._CP',             # 00
        'ED6_DT27/CH03570P._CP',             # 01
        'ED6_DT07/CH01560P._CP',             # 02
        'ED6_DT07/CH01570P._CP',             # 03
        'ED6_DT07/CH01020P._CP',             # 04
        'ED6_DT07/CH01350P._CP',             # 05
        'ED6_DT07/CH01570P._CP',             # 06
    )

    DeclNpc(
        X                   = 1190,
        Z                   = 300,
        Y                   = 75010,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x105,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -4180,
        Z                   = 0,
        Y                   = 66110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 55300,
        Z                   = 0,
        Y                   = 59890,
        Direction           = 93,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 53760,
        Z                   = 0,
        Y                   = 65280,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -49800,
        Z                   = 0,
        Y                   = 13300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -48940,
        Z                   = 1000,
        Y                   = 64599,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclActor(
        TriggerX            = 1040,
        TriggerZ            = 4000,
        TriggerY            = 32049,
        TriggerRange        = 800,
        ActorX              = 1040,
        ActorZ              = 4500,
        ActorY              = 32049,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -42830,
        TriggerZ            = 1000,
        TriggerY            = 61060,
        TriggerRange        = 600,
        ActorX              = -42830,
        ActorZ              = 2000,
        ActorY              = 61060,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -42800,
        TriggerZ            = 1000,
        TriggerY            = 59460,
        TriggerRange        = 600,
        ActorX              = -42800,
        ActorZ              = 2000,
        ActorY              = 59460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_22E",          # 00, 0
        "Function_1_2CE",          # 01, 1
        "Function_2_315",          # 02, 2
        "Function_3_492",          # 03, 3
        "Function_4_1174",         # 04, 4
        "Function_5_11B2",         # 05, 5
        "Function_6_149B",         # 06, 6
        "Function_7_1ACD",         # 07, 7
        "Function_8_210E",         # 08, 8
        "Function_9_2655",         # 09, 9
        "Function_10_2D5F",        # 0A, 10
        "Function_11_3AB2",        # 0B, 11
        "Function_12_5458",        # 0C, 12
        "Function_13_54A0",        # 0D, 13
        "Function_14_54E8",        # 0E, 14
        "Function_15_5530",        # 0F, 15
        "Function_16_5578",        # 10, 16
        "Function_17_5600",        # 11, 17
        "Function_18_5625",        # 12, 18
        "Function_19_565E",        # 13, 19
        "Function_20_56A4",        # 14, 20
        "Function_21_580C",        # 15, 21
    )


    def Function_0_22E(): pass

    label("Function_0_22E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_255")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_252")
    SetChrPos(0xA, 5740, 0, 75240, 87)

    label("loc_252")

    Jump("loc_2AD")

    label("loc_255")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_27C")
    SetChrPos(0xA, 2430, 0, 76110, 180)
    Jump("loc_2AD")

    label("loc_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 2)), scpexpr(EXPR_END)), "loc_29C")
    SetChrPos(0x9, 54220, 0, 7400, 90)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_2AD")

    label("loc_29C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_2A6")
    Jump("loc_2AD")

    label("loc_2A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2AD")

    label("loc_2AD")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2B9"),
        (SWITCH_DEFAULT, "loc_2CD"),
    )


    label("loc_2B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_2CA")

    Jump("loc_2CD")

    label("loc_2CD")

    Return()

    # Function_0_22E end

    def Function_1_2CE(): pass

    label("Function_1_2CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EE")
    OP_B1("t4138_y")
    Jump("loc_2F7")

    label("loc_2EE")

    OP_B1("t4138_n")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30F")
    OP_64(0x0, 0x1)
    OP_71(0x2, 0x10)
    Jump("loc_314")

    label("loc_30F")

    OP_72(0x2, 0x10)

    label("loc_314")

    Return()

    # Function_1_2CE end

    def Function_2_315(): pass

    label("Function_2_315")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_47C")

    label("loc_33A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_353")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_47C")

    label("loc_353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_47C")

    label("loc_36C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_47C")

    label("loc_385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_47C")

    label("loc_39E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B7")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_47C")

    label("loc_3B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D0")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_47C")

    label("loc_3D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E9")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_47C")

    label("loc_3E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_402")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_47C")

    label("loc_402")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41B")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_47C")

    label("loc_41B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_434")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_47C")

    label("loc_434")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44D")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_47C")

    label("loc_44D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_466")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_47C")

    label("loc_466")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47C")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_47C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_491")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_47C")

    label("loc_491")

    Return()

    # Function_2_315 end

    def Function_3_492(): pass

    label("Function_3_492")

    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x2, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4B7")
    SetChrSubChip(0x8, 1)
    Jump("loc_4BC")

    label("loc_4B7")

    SetChrSubChip(0x8, 2)

    label("loc_4BC")

    OP_8C(0x8, 180, 0)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_9AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 6)), scpexpr(EXPR_END)), "loc_527")

    ChrTalk(    #0
        0x8,
        (
            "#1100FI-I wish communications could be\x01",
            "restored, at least...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AC")

    label("loc_527")


    ChrTalk(    #1
        0x8,
        (
            "#1102FHmm...\x02\x03",

            "What on earth could it mean...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1000FHello, Ambassador Crainagh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        (
            "#1101F...Oh, you lot. Good timing.\x02\x03",

            "#1100FWhat do you know about the\x01",
            "current situation?\x02\x03",

            "Any details you could provide\x01",
            "would be of great assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x101,
        "#1011FWell, this is certainly out of the blue.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#1101FFar from it. Orbments malfunctioning on\x01",
            "such a mass scale is utterly unheard of.\x02\x03",

            "#1100FI won't be able to keep regular contact\x01",
            "with Erebonia at this rate. I can't even\x01",
            "get any work done! It's unacceptable!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#1015FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#1042FPardon me, sir.\x02\x03",

            "Have you inquired with Grancel Castle\x01",
            "yet?\x02\x03",

            "#1040FIt's possible that Queen Alicia might be\x01",
            "able to help you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#1101FOf course! I did that some time ago.\x02\x03",

            "#1100FSeveral times, in fact. I've yet to\x01",
            "receive a response of any kind\x01",
            "from Her Majesty.\x02\x03",

            "I think it's safe to assume that\x01",
            "the palace is in just an unfortunate\x01",
            "state, given the circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1004FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#1100FIf I could just restore communications,\x01",
            "I could handle the rest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#1011F(We can't give him a ZFG, right?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#1042F(Of course not.)\x02\x03",

            "(We barely have enough as it is.\x01",
            "He just has to deal with it for now.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20DE)

    label("loc_9AC")

    Jump("loc_116B")

    label("loc_9AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_116B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_EAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 3)), scpexpr(EXPR_END)), "loc_AC9")

    ChrTalk(    #13
        0x8,
        (
            "#1100FAllow me express my earnest gratitude\x01",
            "for your efforts.\x02\x03",

            "Thanks to your efforts, a false suspicion\x01",
            "hanging upon my fatherland has been\x01",
            "cleared.\x02\x03",

            "Miniscule as it was, even a single\x01",
            "blight upon the Empire's dignity brings\x01",
            "me great displeasure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAB")

    label("loc_AC9")


    ChrTalk(    #14
        0x8,
        (
            "#1100FHmm... Good day, Olivier.\x02\x03",

            "And to you as well, bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x104,
        "#031FGood day, ambassador.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#1100FHarumph! Bumming around as\x01",
            "usual, I see.\x02\x03",

            "I should hope you're not using\x01",
            "Mueller's absence as an excuse\x01",
            "to run wild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x104,
        (
            "#030FTut tut! And you're far too serious,\x01",
            "as usual.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "#1100F...What do you need today?\x02\x03",

            "I've already received a report about\x01",
            "the letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        "#1011FOh, really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        (
            "#1102FYes. I was told it was written by those\x01",
            "Special Ops criminals.\x02\x03",

            "#1100FAll completely unrelated to the Empire,\x01",
            "as I'd insisted before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1015F(Weeell, I wouldn't say 'completely'...)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D6B")

    ChrTalk(    #22
        0x106,
        (
            "#053F(Eh, tellin' him the truth would only\x01",
            "make him more nervous.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DAB")

    label("loc_D6B")


    ChrTalk(    #23
        0x103,
        (
            "#020F(Telling him the truth would only\x01",
            "complicate things.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAB")


    ChrTalk(    #24
        0x8,
        (
            "#1100FAllow me express my earnest gratitude\x01",
            "for your efforts.\x02\x03",

            "Thanks to your efforts, a false suspicion\x01",
            "hanging upon my fatherland has been\x01",
            "cleared.\x02\x03",

            "Miniscule as it was, even a single\x01",
            "blight upon the Empire's dignity brings\x01",
            "me great displeasure.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x165B)

    label("loc_EAB")

    Jump("loc_116B")

    label("loc_EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_116B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FD6")

    ChrTalk(    #25
        0x8,
        (
            "#1100FI've received reports that numerous\x01",
            "branches inside the Empire have been\x01",
            "attacked one after the other.\x02\x03",

            "Given that you're bracers yourselves,\x01",
            "I fear that you may be an easy target for\x01",
            "whoever is responsible.\x02\x03",

            "I wish you and your fellow bracers well.\x01",
            "Do not lose hope.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116B")

    label("loc_FD6")


    ChrTalk(    #26
        0x8,
        (
            "#1100FThe path of the bracer continues to prove\x01",
            "itself a harsh one, indeed.\x02\x03",

            "Several months ago, I'd received reports\x01",
            "concerning the Bracer Guild.\x02\x03",

            "Various branches have been attacked in\x01",
            "my country, one after the other.\x02\x03",

            "#1102FGiven that you're bracers yourselves,\x01",
            "I fear that you may be an easy target for\x01",
            "whoever is responsible.\x02\x03",

            "#1100FI wish you and your fellow bracers well.\x01",
            "Do not lose hope.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_116B")

    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_3_492 end

    def Function_4_1174(): pass

    label("Function_4_1174")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 2)), scpexpr(EXPR_END)), "loc_11AE")

    ChrTalk(    #27
        0x9,
        "#270FWhat is it? Did you forget something?\x02",
    )

    CloseMessageWindow()

    label("loc_11AE")

    TalkEnd(0x9)
    Return()

    # Function_4_1174 end

    def Function_5_11B2(): pass

    label("Function_5_11B2")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_128E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_128B")

    ChrTalk(    #28
        0xFE,
        (
            "There was a strange order from\x01",
            "Erebonia before the orbal shutdown\x01",
            "occurred, from what I've been told.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Just as the ambassador tried to\x01",
            "inquire about it, communications\x01",
            "suddenly dropped.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_128B")

    Jump("loc_1497")

    label("loc_128E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1497")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_12F8")

    ChrTalk(    #30
        0xFE,
        "How odd...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "We haven't received our routine\x01",
            "report from Mueller in Bose...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1497")

    label("loc_12F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_1497")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1397")

    ChrTalk(    #32
        0xFE,
        (
            "I imagine you must be having a\x01",
            "difficult time trying to find the culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Never hesitate to let us know if we\x01",
            "can be of assistance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1497")

    label("loc_1397")


    ChrTalk(    #34
        0xFE,
        (
            "I imagine you must be having a\x01",
            "difficult time trying to find the culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Though I suppose if there some\x01",
            "clue--any clue at all--we wouldn't\x01",
            "be in the position we're in now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Still, don't hesitate to let us know if\x01",
            "we can be of assistance.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1497")

    TalkEnd(0xA)
    Return()

    # Function_5_11B2 end

    def Function_6_149B(): pass

    label("Function_6_149B")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1534")

    ChrTalk(    #37
        0xFE,
        (
            "I wonder what that last communique\x01",
            "from the Empire meant\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "He was yelling something like,\x01",
            "'What do you MEAN, don't move?!'\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1534")

    Jump("loc_1AC9")

    label("loc_1537")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_17A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_15E6")

    ChrTalk(    #39
        0xFE,
        (
            "When we annexed the independent state,\x01",
            "the chancellor's command was incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "No, no, really, this is what the\x01",
            "orbal railroad is for.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179D")

    label("loc_15E6")


    ChrTalk(    #41
        0xFE,
        (
            "During our conflicts with the independent state,\x01",
            "the chancellor's command was incredible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "To assemble a military force spread across such\x01",
            "an enormous space temporarily at the borders with\x01",
            "the orbal railroad...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Claim victory with a shock attack, then return\x01",
            "the forces as quickly as possible to their\x01",
            "defensive positions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "This is what the orbal railroad is for, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "Ha ha, our fatherland has no weaknesses now.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_179D")

    Jump("loc_1AC9")

    label("loc_17A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_1875")

    ChrTalk(    #46
        0xFE,
        (
            "Chancellor Osborne is former man\x01",
            "of the military turned politician.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I believe he reached his position,\x01",
            "oh...ten years ago?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "I remember he elevated through\x01",
            "the political world very quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC9")

    label("loc_1875")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1AC9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1947")

    ChrTalk(    #49
        0xFE,
        (
            "The closest Imperial city to Liberl\x01",
            "borders is a place called Parm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "I'm actually from there, by the way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "It's close to Bose, which makes it\x01",
            "convenient to return home for visits.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AC9")

    label("loc_1947")


    ChrTalk(    #52
        0xFE,
        (
            "The closest Imperial city to Liberl\x01",
            "borders is a place called Parm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "I'm actually from there, by the way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "It's close to Bose, which makes it\x01",
            "convenient to return home for visits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Of course, it's not so convenient to\x01",
            "visit the Imperial capital from there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "There aren't any public scheduled\x01",
            "liners in Erebonia, so I have to switch\x01",
            "over to the railway system.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1AC9")

    TalkEnd(0xB)
    Return()

    # Function_6_149B end

    def Function_7_1ACD(): pass

    label("Function_7_1ACD")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1BA9")

    ChrTalk(    #57
        0xFE,
        (
            "I wonder what that object floating\x01",
            "above the lake is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "Is this phenomenon occurring in\x01",
            "the Empire as well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "It'd be nice to know SOMETHING.\x01",
            "Knowing nothing at all is so nerve-\x01",
            "racking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA9")

    Jump("loc_210A")

    label("loc_1BAC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_210A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1E3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1CA4")

    ChrTalk(    #60
        0xFE,
        (
            "Had the criminal turned out to be a\x01",
            "Republican citizen, I highly doubt the\x01",
            "Empire would have stayed quiet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "And the opposite is surely true as\x01",
            "well. It would have put a great strain\x01",
            "on the non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3A")

    label("loc_1CA4")


    ChrTalk(    #62
        0xFE,
        (
            "Queen Alicia's most likely more relieved\x01",
            "than anyone that the criminal turned out\x01",
            "to be a former member of the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I realize that might be callous, but think\x01",
            "about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Had the criminal turned out to be a\x01",
            "Republican citizen, do you think the\x01",
            "Empire would have stayed quiet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "And the opposite is surely true as\x01",
            "well. It would have put a great strain\x01",
            "on the non-aggression pact.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1E3A")

    Jump("loc_210A")

    label("loc_1E3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_205D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1EC9")

    ChrTalk(    #66
        0xFE,
        (
            "Queen Alicia's diplomatic efforts using\x01",
            "her orbal technology are masterful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "If anything should happen to her... \x02",
    )

    CloseMessageWindow()
    Jump("loc_205A")

    label("loc_1EC9")


    ChrTalk(    #68
        0xFE,
        (
            "The Liberl Kingdom is what we would\x01",
            "call a 'buffer state.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Buffer states are what we call countries\x01",
            "sandwiched between larger nations,\x01",
            "forming a barrier that prevents conflict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "It's imperative that said buffer ensures\x01",
            "a balance of power between those nations.\x01",
            "If it wants to stay independent, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Perhaps this non-aggression pact also\x01",
            "exists to uphold the balance of power.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_205A")

    Jump("loc_210A")

    label("loc_205D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_210A")

    ChrTalk(    #72
        0xFE,
        "Hey, Olivier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I heard you went to the hot springs.\x01",
            "I'm so envious!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "I've been working until I'm dead on\x01",
            "my feet getting ready for the signing\x01",
            "ceremony.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_210A")

    TalkEnd(0xC)
    Return()

    # Function_7_1ACD end

    def Function_8_210E(): pass

    label("Function_8_210E")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2211")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_220E")

    ChrTalk(    #75
        0xFE,
        (
            "I wonder if my father and mother in\x01",
            "the Empire are safe...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "Olivier left the other day. I wonder if\x01",
            "he's all right.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Not being able to communicate with\x01",
            "your own country in a situation like this\x01",
            "is terrifying, I'll admit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_220E")

    Jump("loc_2651")

    label("loc_2211")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2651")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_22B9")

    ChrTalk(    #78
        0xFE,
        (
            "Now, now, Olivier! Don't get in the way\x01",
            "of work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "As you have no doubt noticed,\x01",
            "the ambassador insists we keep\x01",
            "this place neat and tidy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2651")

    label("loc_22B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_2367")

    ChrTalk(    #80
        0xFE,
        (
            "...Olivier, please don't tease the\x01",
            "ambassador too much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "The chancellor's been giving him\x01",
            "enough stress. The poor man's hair\x01",
            "has grown thinner as of late.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2651")

    label("loc_2367")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2651")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 4)), scpexpr(EXPR_END)), "loc_2441")

    ChrTalk(    #82
        0xFE,
        (
            "I wonder who Olivier's REALLY\x01",
            "targeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "What do you think? Is Mueller still\x01",
            "his one an only, or has he moved\x01",
            "on to greener pastures?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x104,
        "#030FWhy, you need only ask!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        "#1019FNO. THANKS.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2651")

    label("loc_2441")

    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x104, 400)
    Sleep(600)

    ChrTalk(    #86
        0xFE,
        "Oh, hey! It's been a while, Olivier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "Are these your guests?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x104,
        (
            "#035FIndeed, one could call them guests,\x01",
            "but I'm more inclined to think of them\x01",
            "as my soul mates.\x02\x03",

            "#030FOur days spent together have been so\x01",
            "tender, so sweet, I feel to merely call this\x01",
            "force 'love' does a disservice to our bond.\x02\x03",

            "#037FIs that not so, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "My...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Wait, does that mean you've\x01",
            "dumped Mueller?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#1019FMy... My head hurts...\x02\x03",

            "I think I'm starting to understand\x01",
            "Mueller's suffering...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x165C)

    label("loc_2651")

    TalkEnd(0xD)
    Return()

    # Function_8_210E end

    def Function_9_2655(): pass

    label("Function_9_2655")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2716")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2713")

    ChrTalk(    #92
        0xFE,
        "You know that golden, floating object?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "I've never seen or heard of anything\x01",
            "like that before in my entire life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "It's damn creepy, that much is for sure.\x02",
    )

    CloseMessageWindow()

    label("loc_2713")

    Jump("loc_2D5B")

    label("loc_2716")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_29FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2873")

    ChrTalk(    #95
        0xFE,
        (
            "Restrictions are fairly stringent in the\x01",
            "Erebonian Empire. Published materials\x01",
            "are especially scrutinized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "My job involves making sure it's all\x01",
            "appropriate for public consumption.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "I've got to check whether published works\x01",
            "are suitable for our nation as whole, if they\x01",
            "breaks any laws, and all that stuff.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F9")

    label("loc_2873")


    ChrTalk(    #98
        0xFE,
        (
            "Liberlians are given the right to freedom\x01",
            "of speech, unlike the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "Restrictions are fairly stringent in\x01",
            "the Empire. Published materials are\x01",
            "especially scrutinized.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "My job involves making sure it's all\x01",
            "appropriate for public consumption.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "I've got to check whether published works\x01",
            "are suitable for our nation as whole, if they\x01",
            "breaks any laws, and all that stuff.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_29F9")

    Jump("loc_2D5B")

    label("loc_29FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_END)), "loc_2C7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 0)), scpexpr(EXPR_END)), "loc_2B32")

    ChrTalk(    #102
        0xFE,
        (
            "If you haven't read it yet, I'd highly\x01",
            "recommend this amazing book called\x01",
            "'Carnelia.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "I don't know who the author is, but I'd\x01",
            "guess they're probably from the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "They describe the capital in such vivid\x01",
            "detail! There's no way they couldn't have\x01",
            "done so without living there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C78")

    label("loc_2B32")


    ChrTalk(    #105
        0xFE,
        "How could this...BE?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "This book is banned in Erebonia!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "Who p-put this on the shelf...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2F)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BB6")

    ChrTalk(    #108
        0x130,
        "#274F(...)\x02",
    )

    CloseMessageWindow()

    label("loc_2BB6")


    ChrTalk(    #109
        0xFE,
        (
            "Crap, crap, craaaap. If Ambassador\x01",
            "Crainagh knew, I'd get an earful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "Ah! I know! You there. Take this book!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #111
        "\x07\x00Received #573i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x23D, 1)
    OP_A2(0x10B8)

    label("loc_2C78")

    Jump("loc_2D5B")

    label("loc_2C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2D5B")

    ChrTalk(    #112
        0xFE,
        (
            "All the books in this room were\x01",
            "published in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "To learn about someone's nation,\x01",
            "start with their culture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "You're free to read them, but please\x01",
            "put them back where you found them\x01",
            "once you're done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5B")

    TalkEnd(0xE)
    Return()

    # Function_9_2655 end

    def Function_10_2D5F(): pass

    label("Function_10_2D5F")

    EventBegin(0x0)
    OP_6D(910, 4000, 27010, 0)
    OP_67(0, 10110, -10000, 0)
    OP_6B(2140, 0)
    OP_6C(45000, 0)
    OP_6E(453, 0)
    SetChrPos(0x104, 1590, 0, 4140, 0)
    SetChrPos(0x101, 430, 0, 4150, 0)
    SetChrPos(0x105, 210, 0, 2710, 0)
    SetChrPos(0x108, 1520, 0, 2840, 0)

    def lambda_2DE8():
        OP_6D(970, 0, 5940, 7000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2DE8)

    def lambda_2E00():
        OP_67(0, 10110, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E00)
    OP_C8(0x200, 0x46, "C_PLAC12._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(1490, 0, 4150, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #115
        0x108,
        "#073FThis is...quite the building!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#1011F#6PWhoa...\x02\x03",

            "This place definitely matches the Calvardian\x01",
            "embassy in terms of fanciness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x105,
        (
            "#047FGrandiose, and yet powerful\x01",
            "at the same time.\x02\x03",

            "#048FIt's very Imperial, if nothing else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x104,
        (
            "#030FHm. It is a stage upon which the\x01",
            "Empire can parade its influence\x01",
            "and power.\x02\x03",

            "#035FAlas that the actors are unequal\x01",
            "to the set dressing...\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_72(0x3, 0x10)
    OP_6F(0x3, 60)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 12690, 0, 5860, 270)
    OP_4A(0x9, 255)

    NpcTalk(    #119
        0x9,
        "Man's Voice",
        (
            "#3PYou realize Lord Crainagh would\x01",
            "hit the roof if he heard you say that.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_30F2():

        label("loc_30F2")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_30F2")

    QueueWorkItem2(0x104, 2, lambda_30F2)

    def lambda_3103():

        label("loc_3103")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3103")

    QueueWorkItem2(0x101, 2, lambda_3103)
    Sleep(200)

    def lambda_3119():

        label("loc_3119")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3119")

    QueueWorkItem2(0x108, 2, lambda_3119)

    def lambda_312A():

        label("loc_312A")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_312A")

    QueueWorkItem2(0x105, 2, lambda_312A)
    OP_6D(10750, 0, 5950, 2000)

    def lambda_314C():
        OP_8E(0xFE, 0x35C, 0x0, 0x1568, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_314C)

    def lambda_3167():
        OP_6D(990, 0, 4480, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3167)
    OP_72(0x3, 0x800)
    OP_71(0x3, 0x10)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x9, 0x0)
    OP_8C(0x9, 180, 400)
    OP_71(0x3, 0x800)
    OP_44(0x104, 0x2)
    OP_44(0x101, 0x2)
    OP_44(0x108, 0x2)
    OP_44(0x105, 0x2)
    OP_8C(0x104, 0, 0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #120
        0x104,
        (
            "#031F#7PAh! My most bosom companion!\x02\x03",

            "It has been an age!\x01",
            "Are you well, dear Mueller?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x9,
        (
            "#274F#6PI would be better if I could cut you\x01",
            "in half and be done with it.\x02\x03",

            "I told you, again and again, to ensure\x01",
            "we're constantly aware of your location,\x01",
            "and you--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x104,
        (
            "#037F#7PAh, but 'tis a tactic in the war of\x01",
            "love.\x02\x03",

            "Did you know? Absence makes the\x01",
            "heart grow fonder.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x9,
        (
            "#276F#6P...Estelle Bright, you have my\x01",
            "thanks.\x02\x03",

            "I can only imagine the trouble this\x01",
            "idiot's been causing you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#1016F#7PHaha... Actually, he hasn't been\x01",
            "TOO bad, I guess.\x02\x03",

            "#1006FHe's been really well-mannered.\x01",
            "Comparatively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        (
            "#272F#6PWell, ignoring the lunatic...\x02\x03",

            "#277FI presume you have business here\x01",
            "at the embassy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x101,
        (
            "#1002F#7PYes, sir.\x02\x03",

            "We would like to speak to the\x01",
            "ambassador.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #127
        (
            "\x07\x05Estelle explained her desire to meet with the\x01",
            "ambassador concerning the letter.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #128
        0x9,
        (
            "#273F#6PThat letter, right...\x02\x03",

            "#270FI'd been somewhat concerned myself,\x01",
            "but I'm surprised the guild is acting.\x02\x03",

            "This is a request from Brigadier General Bright and\x01",
            "the Royal Army, I take it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x101,
        (
            "#1006F#7PTechnically, yes, but...\x02\x03",

            "We're trying to investigate it as neutrally\x01",
            "as we can, y'know? Nobody's guilty till\x01",
            "proven, that kind of thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x9,
        (
            "#277F#6PHm. A commendable mindset.\x01",
            "No doubt why he chose you.\x02\x03",

            "Very well. I shall introduce you to Lord\x01",
            "Ambassador Crainagh.\x02\x03",

            "I suspect you'll find it easier to gain\x01",
            "his trust if I do the introductions as\x01",
            "opposed to a certain someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x101,
        "#1004F#7PReally? Thanks, Mueller!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x108,
        "#071FYeah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x105,
        "#041F#2PThank you, sir.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x104, 225, 400)

    ChrTalk(    #134
        0x104,
        (
            "#036F#6PUm, wait... You really have so\x01",
            "little faith in me...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #135
        0x101,
        (
            "#1004F#6PYou, uh, thought we had faith\x01",
            "in you for this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x108,
        (
            "#070FIf you introduced us, he'd probably\x01",
            "want to have us kicked out.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 45, 400)

    ChrTalk(    #137
        0x105,
        "#045F#5PUm... Sorry, Olivier.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x104,
        "#034F#6PAh! The sting of being forsaken!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        "#272F#6PThe sting of the truth, maybe.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x105, 0, 400)
    OP_8C(0x104, 0, 400)

    ChrTalk(    #140
        0x9,
        (
            "#277F#6PLord Crainagh is in his office on the\x01",
            "second floor.\x02\x03",

            "I shall go announce your arrival.\x01",
            "Give me a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        "#1006F#7PWe'll wait, then.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)

    def lambda_39FF():
        OP_6D(6830, 0, 8520, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_39FF)

    def lambda_3A17():

        label("loc_3A17")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3A17")

    QueueWorkItem2(0x104, 2, lambda_3A17)

    def lambda_3A28():

        label("loc_3A28")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3A28")

    QueueWorkItem2(0x101, 2, lambda_3A28)

    def lambda_3A39():

        label("loc_3A39")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3A39")

    QueueWorkItem2(0x108, 2, lambda_3A39)

    def lambda_3A4A():

        label("loc_3A4A")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_3A4A")

    QueueWorkItem2(0x105, 2, lambda_3A4A)
    OP_8E(0x9, 0x2242, 0x0, 0x1EE6, 0xBB8, 0x0)
    OP_8E(0x9, 0x2454, 0x7D0, 0x3AF2, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    OP_6D(1020, 0, 3870, 2000)
    OP_44(0x104, 0x2)
    OP_44(0x101, 0x2)
    OP_44(0x108, 0x2)
    OP_44(0x105, 0x2)
    OP_72(0x2, 0x10)
    OP_65(0x0, 0x1)
    OP_A2(0x1620)
    EventEnd(0x0)
    Return()

    # Function_10_2D5F end

    def Function_11_3AB2(): pass

    label("Function_11_3AB2")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x104, 1500, 4000, 29410, 0)
    SetChrPos(0x101, 320, 4000, 29600, 0)
    SetChrPos(0x108, 1380, 4000, 28080, 0)
    SetChrPos(0x105, -110, 4000, 28000, 0)
    OP_6D(920, 4000, 30680, 0)
    OP_67(0, 7300, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_4A(0x9, 255)
    OP_0D()

    ChrTalk(    #142
        0x101,
        "#1015F#6PSo this is the office? Wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x104,
        (
            "#031F#7PHeh, indeed.\x02\x03",

            "Shall we make our grand entrance and\x01",
            "shock the ambassador into silence?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #144
        0x101,
        (
            "#1019F#6PMueller CAN totally cut you\x01",
            "in half, you know.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    OP_72(0x2, 0x10)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    Sleep(1000)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 1020, 4000, 32900, 180)
    ClearChrFlags(0x9, 0x80)
    OP_8C(0x101, 0, 400)

    def lambda_3C62():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xC8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3C62)
    OP_8E(0x9, 0x384, 0xFA0, 0x79EA, 0x7D0, 0x0)

    ChrTalk(    #145
        0x9,
        (
            "#277F#6PI apologize for the wait.\x01",
            "Lord Crainagh will see you now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        "#1006F#7PLet's go, then.\x02",
    )

    CloseMessageWindow()

    def lambda_3CED():
        OP_8E(0xFE, 0x96A, 0xFA0, 0x7A08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3CED)
    WaitChrThread(0x9, 0x0)
    OP_8C(0x9, 270, 400)
    OP_43(0x101, 0x0, 0x0, 0x11)
    Sleep(500)
    OP_43(0x104, 0x0, 0x0, 0x11)
    Sleep(300)
    OP_43(0x105, 0x0, 0x0, 0x11)
    Sleep(600)
    OP_43(0x108, 0x0, 0x0, 0x11)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0x2F, 0xFF, 0xFF)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x130, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6D(450, 0, 67280, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(2000, 0)

    def lambda_3DB7():
        OP_6D(1760, 0, 73830, 6000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3DB7)
    OP_43(0x101, 0x1, 0x0, 0xC)
    Sleep(600)
    OP_43(0x104, 0x1, 0x0, 0xD)
    Sleep(600)
    OP_43(0x105, 0x1, 0x0, 0xE)
    Sleep(600)
    OP_43(0x108, 0x1, 0x0, 0xF)
    Sleep(600)
    OP_43(0x130, 0x1, 0x0, 0x10)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x2)
    OP_0D()

    ChrTalk(    #147
        0x8,
        (
            "#1100F#6PWelcome to the Erebonian embassy,\x01",
            "guests.\x02\x03",

            "I am Lord Davil Crainagh, the duly\x01",
            "appointed ambassador and voice of\x01",
            "the Empire in this land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        "#1011F#2PUm, I'm Estelle Bright of the Bracer Guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x108,
        "#070F#2PZin Vathek, also of the guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x105,
        (
            "#040FI'm Kloe Rinz, second-year student at the\x01",
            "Jenis Royal Academy and assistant to\x01",
            "the bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x104,
        (
            "#031FAnd I...am the servant of love and peace,\x01",
            "Olivier Lenheim!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x8,
        (
            "#1102F#6PErgh... You.\x02\x03",

            "#1100FI'd heard you'd gone missing in\x01",
            "Elmo Village.\x02\x03",

            "Try not to worry Mueller further...\x01",
            "Olivier.\x02\x03",

            "Or me, for that matter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x104,
        (
            "#035FSuch a strict dressing down.\x01",
            "Much more and I'll have to lose my jacket.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x8,
        (
            "#1100F#6PMmmmmph. Setting that aside...\x02\x03",

            "You are here to inquire about the\x01",
            "threatening letter, yes?\x02\x03",

            "What do you want to know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x101,
        (
            "#1002F#2POkay, I'll be direct, sir.\x02\x03",

            "Do you have any idea who might be\x01",
            "behind the letter?\x02\x03",

            "Is there anyone in the Empire who\x01",
            "might oppose the signing of the pact?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "#1102F#6PMy! You ARE direct, young bracer.\x01",
            "I appreciate that.\x02\x03",

            "#1100FI can tell you truthfully, however,\x01",
            "that I can think of no such person.\x02\x03",

            "His Majesty is very happy with\x01",
            "the pact as it stands, in fact.\x02\x03",

            "And no one within the Empire would be\x01",
            "foolish enough to gainsay his leadership\x01",
            "on such a matter, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x101,
        (
            "#1007F#2PU-Uh... Yeah, I...bet...\x02\x03",

            "#1015FSo you think it's the work of someone\x01",
            "outside the Empire, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x8,
        (
            "#1100F#6PWhat other answer could there be?\x02\x03",

            "If you want my opinion, it's the 'opposition\x01",
            "party' in Calvard behind all this. Some silly\x01",
            "ploy to make the 'president' look bad, no doubt.\x02\x03",

            "Opposition! Doing whatever it pleases!\x01",
            "This is a perfect example of the fallacies\x01",
            "of mob rule.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x108,
        (
            "#073F#2PHuh. I have to question that, ah, your\x01",
            "lordship.\x02\x03",

            "#070FDon't get me wrong, our major political\x01",
            "parties basically beat each other over\x01",
            "the head any time they can. But...\x02\x03",

            "Even if the pact fell apart due to this,\x01",
            "I don't think anyone could blame it on\x01",
            "President Rocksmith.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "#1102F#6PDetails! You think the mob thinks like that?\x01",
            "Pah.\x02\x03",

            "#1100FAll I can say for certain is that the\x01",
            "person issuing these threats cannot\x01",
            "be from our Empire.\x02\x03",

            "That should be more than enough\x01",
            "assurance for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1015F#2PW-Well... Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x105,
        (
            "#047F#2PExcuse me, Lord Crainagh?\x02\x03",

            "#042FMay I ask what Chancellor Osborne's\x01",
            "opinion of the non-aggression pact is?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #163
        0x8,
        "#1101F#6PWhat?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x130, 225, 400)
    Sleep(200)

    ChrTalk(    #164
        0x130,
        "#273F#6PHmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x104,
        "#035FHeh. Flawless riposte, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        "#1016F#2PUm... Who?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x104,
        (
            "#030FThe highest appointed official of our most\x01",
            "glorious and august Imperial government--\x01",
            "the Blood and Iron Chancellor, Giliath Osborne.\x02\x03",

            "His nickname comes from his personal motto:\x01",
            "'Our nation's peace must be built on a foundation\x01",
            "of blood and iron.' He has overseen the...\x02\x03",

            "#035Fexpansion of the rail system...as well as the\x01",
            "annexation of several smaller states on our\x01",
            "borders through...less than diplomatic means.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #168
        0x101,
        "#1004F#2PAnnex...? W-Wait, you mean he--\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    ChrTalk(    #169
        0x8,
        (
            "#1103F#6POL-OLIVIER!\x02\x03",

            "How can you criticize your empire's\x01",
            "chancellor?!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #170
        0x104,
        (
            "#035FOh, but, Davil, how was I criticizing?\x01",
            "I simply stated the facts.\x02\x03",

            "#030FBut come now, it wouldn't hurt to be a bit\x01",
            "more cooperative, no?\x02\x03",

            "We've already spoken with the lovely\x01",
            "Ambassador Cochrane over at the Calvardian\x01",
            "embassy.\x02\x03",

            "She was quite helpful, you see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        "#1101F#6PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x104,
        (
            "#034FWhy, if we don't help these people now,\x01",
            "it will give them cause to doubt the\x01",
            "character of Erebonia!\x02\x03",

            "That would be a tragedy, wouldn't you\x01",
            "agree?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        "#1101F#6PGrrrrrrgh...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x130, 270, 400)

    ChrTalk(    #174
        0x130,
        (
            "#276F#4PMy Lord Crainagh.\x02\x03",

            "There's no need to keep information\x01",
            "related to this hidden.\x02\x03",

            "May I humbly suggest that being open\x01",
            "in this case will not present a problem?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        (
            "#1102F#6PMmm. You have a point, Mueller.\x01",
            "Very well.\x02\x03",

            "#1100FTo answer your question, miss,\x01",
            "Chancellor Osborne, like His Majesty,\x01",
            "is most receptive to this pact.\x02\x03",

            "In fact, I hear he is actually the one who\x01",
            "suggested His Majesty should sign it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x105,
        "#044F#2PReally...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x104,
        "#030FHmm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1015F#2PThat's because he's looking forward to\x01",
            "getting the engine, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x8,
        (
            "#1102F#6PNo. Apparently, he recommended it to\x01",
            "His Majesty before any mention of the engine.\x02\x03",

            "#1100FIf anything, I'm glad there is harmony at\x01",
            "home over this pact. There's been no pressure\x01",
            "for us to negotiate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x108,
        (
            "#074F#2PHmmm...\x02\x03",

            "#070FHate to say it, Estelle, but it's looking\x01",
            "like there really isn't any chance it's\x01",
            "someone from the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#1007F#2PYeah, looks that way.\x02\x03",

            "#1006FAmbassador, thanks a lot for answering\x01",
            "our questions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x8,
        (
            "#1101F#6PHmph! See? It is as I said.\x02\x03",

            "If you're looking for the guilty party,\x01",
            "you should look elsewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#1004F#2POh, but, uh, one sec!\x02\x03",

            "#1015FIf you don't mind, we have one\x01",
            "more question...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #184
        "\x07\x05Estelle asked Lord Crainagh about Renne's parents.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #185
        0x8,
        (
            "#1102F#6PYes... A most pitiable situation,\x01",
            "the separation of a child from her\x01",
            "parents.\x02\x03",

            "#1100FImperial traders do visit the embassy at\x01",
            "times, but...\x02\x03",

            "A merchant from Crossbell?\x01",
            "I do not recall such a man, no.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 1)
    Sleep(300)

    ChrTalk(    #186
        0x8,
        (
            "#1100F#6PAre you familiar with this Hayworth,\x01",
            "Mueller?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x130,
        "#272F#4PNo... I've never heard of the man, either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        (
            "#1015F#2PReally? Awww...\x02\x03",

            "#1007FThis is starting to look kinda grim.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    Sleep(300)

    ChrTalk(    #189
        0x8,
        (
            "#1100F#6PTo search at once for both a blackmailer\x01",
            "and a lost child's parents sounds most\x01",
            "trying.\x02\x03",

            "It may seem trite, but I do wish you luck,\x01",
            "young lady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        "#1006F#2PUh... Thanks, Miste- er, Lord Crainagh!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x130, 225, 400)
    Sleep(400)

    ChrTalk(    #191
        0x130,
        "#277F#6PAllow me to show you to the gate, then.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(700, 0, 70010, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 700, 0, 70010, 180)
    SetChrPos(0x1, 700, 0, 70010, 180)
    SetChrPos(0x2, 700, 0, 70010, 180)
    SetChrPos(0x3, 700, 0, 70010, 180)
    SetChrPos(0x130, 700, 0, 70010, 180)
    OP_71(0x2, 0x10)
    OP_64(0x0, 0x1)
    OP_A2(0x1621)
    OP_28(0x8B, 0x2, 0x20)
    OP_28(0x8B, 0x1, 0x40)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_11_3AB2 end

    def Function_12_5458(): pass

    label("Function_12_5458")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -220, 0, 63670, 0)

    def lambda_547F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_547F)
    OP_8E(0xFE, 0x406, 0x0, 0x11990, 0x7D0, 0x0)
    Return()

    # Function_12_5458 end

    def Function_13_54A0(): pass

    label("Function_13_54A0")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -220, 0, 63670, 0)

    def lambda_54C7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_54C7)
    OP_8E(0xFE, 0xFFFFFF2E, 0x0, 0x11756, 0x7D0, 0x0)
    Return()

    # Function_13_54A0 end

    def Function_14_54E8(): pass

    label("Function_14_54E8")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -220, 0, 63670, 0)

    def lambda_550F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_550F)
    OP_8E(0xFE, 0x73A, 0x0, 0x116B6, 0x7D0, 0x0)
    Return()

    # Function_14_54E8 end

    def Function_15_5530(): pass

    label("Function_15_5530")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -220, 0, 63670, 0)

    def lambda_5557():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5557)
    OP_8E(0xFE, 0x24E, 0x0, 0x11472, 0x7D0, 0x0)
    Return()

    # Function_15_5530 end

    def Function_16_5578(): pass

    label("Function_16_5578")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, -220, 0, 63670, 0)

    def lambda_559F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_559F)
    OP_8E(0xFE, 0xFFFFFFBA, 0x0, 0xFF45, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    OP_22(0x7, 0x0, 0x64)
    Sleep(500)
    OP_8E(0xFE, 0xCB2, 0x0, 0x10F90, 0x9C4, 0x0)
    OP_8E(0xFE, 0xCB2, 0x0, 0x11EFE, 0x9C4, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_16_5578 end

    def Function_17_5600(): pass

    label("Function_17_5600")

    OP_8E(0xFE, 0x3CA, 0xFA0, 0x82D2, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_5600 end

    def Function_18_5625(): pass

    label("Function_18_5625")

    OP_8E(0xFE, 0x302, 0xFA0, 0x7A58, 0xBB8, 0x0)
    OP_8E(0xFE, 0x3CA, 0xFA0, 0x82D2, 0xBB8, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_5625 end

    def Function_19_565E(): pass

    label("Function_19_565E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #192
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_19_565E end

    def Function_20_56A4(): pass

    label("Function_20_56A4")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #193
        "\x07\x05This shelf holds the [Carnelia] series.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Read Chapter 1]\x01",      # 0
            "[Read Chapter 2]\x01",      # 1
            "[Read Chapter 3]\x01",      # 2
            "[Read Chapter 4]\x01",      # 3
            "[Read Chapter 5]\x01",      # 4
            "[Read Chapter 6]\x01",      # 5
            "[Stop]\x01",                # 6
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57AE")
    OP_B8(0x212, 0x0)

    label("loc_57AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57C0")
    OP_B8(0x213, 0x0)

    label("loc_57C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57D2")
    OP_B8(0x214, 0x0)

    label("loc_57D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57E4")
    OP_B8(0x215, 0x0)

    label("loc_57E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57F6")
    OP_B8(0x216, 0x0)

    label("loc_57F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5808")
    OP_B8(0x217, 0x0)

    label("loc_5808")

    TalkEnd(0xFF)
    Return()

    # Function_20_56A4 end

    def Function_21_580C(): pass

    label("Function_21_580C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #194
        "\x07\x05This shelf holds the [Carnelia] series.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "[Read Chapter 7]\x01",       # 0
            "[Read Chapter 8]\x01",       # 1
            "[Read Chapter 9]\x01",       # 2
            "[Read Chapter 10]\x01",      # 3
            "[Read Finale]\x01",          # 4
            "[Stop]\x01",                 # 5
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5903")
    OP_B8(0x218, 0x0)

    label("loc_5903")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5915")
    OP_B8(0x219, 0x0)

    label("loc_5915")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5927")
    OP_B8(0x21A, 0x0)

    label("loc_5927")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5939")
    OP_B8(0x21B, 0x0)

    label("loc_5939")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_594B")
    OP_B8(0x21C, 0x0)

    label("loc_594B")

    TalkEnd(0xFF)
    Return()

    # Function_21_580C end

    SaveToFile()

Try(main)
