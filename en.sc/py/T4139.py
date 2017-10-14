from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4139   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4139.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4139_1 ._SN',
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
        'Ambassador Cochrane',                  # 9
        'Residing Officer Yakumo',              # 10
        'Farrah',                               # 11
        'Councilor Benicio',                    # 12
        'Sandy',                                # 13
        'Ricarda',                              # 14
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
        'ED6_DT27/CH03723 ._CH',             # 00
        'ED6_DT07/CH01490 ._CH',             # 01
        'ED6_DT07/CH01180 ._CH',             # 02
        'ED6_DT07/CH01680 ._CH',             # 03
        'ED6_DT07/CH02540 ._CH',             # 04
        'ED6_DT07/CH01230 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT27/CH03723P._CP',             # 00
        'ED6_DT07/CH01490P._CP',             # 01
        'ED6_DT07/CH01180P._CP',             # 02
        'ED6_DT07/CH01680P._CP',             # 03
        'ED6_DT07/CH02540P._CP',             # 04
        'ED6_DT07/CH01230P._CP',             # 05
    )

    DeclNpc(
        X                   = 55000,
        Z                   = 200,
        Y                   = 65540,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x105,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -54910,
        Z                   = 0,
        Y                   = 61420,
        Direction           = 101,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -51570,
        Z                   = 0,
        Y                   = -44740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 55260,
        Z                   = 0,
        Y                   = 10640,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -6760,
        Z                   = 0,
        Y                   = 7960,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -52030,
        Z                   = 0,
        Y                   = 58230,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclActor(
        TriggerX            = 1030,
        TriggerZ            = 6000,
        TriggerY            = 33170,
        TriggerRange        = 800,
        ActorX              = 1030,
        ActorZ              = 6500,
        ActorY              = 33170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1030,
        TriggerZ            = 6000,
        TriggerY            = 33170,
        TriggerRange        = 800,
        ActorX              = 1030,
        ActorZ              = 6500,
        ActorY              = 33170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -60560,
        TriggerZ            = 0,
        TriggerY            = -46570,
        TriggerRange        = 600,
        ActorX              = -60560,
        ActorZ              = 1000,
        ActorY              = -46470,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -60560,
        TriggerZ            = 0,
        TriggerY            = -44950,
        TriggerRange        = 600,
        ActorX              = -60560,
        ActorZ              = 1000,
        ActorY              = -44700,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -60560,
        TriggerZ            = 0,
        TriggerY            = -43230,
        TriggerRange        = 600,
        ActorX              = -60560,
        ActorZ              = 1000,
        ActorY              = -42960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_24E",          # 00, 0
        "Function_1_2C5",          # 01, 1
        "Function_2_33B",          # 02, 2
        "Function_3_4B8",          # 03, 3
        "Function_4_4DC",          # 04, 4
        "Function_5_113F",         # 05, 5
        "Function_6_1822",         # 06, 6
        "Function_7_1F43",         # 07, 7
        "Function_8_288F",         # 08, 8
        "Function_9_2E2C",         # 09, 9
        "Function_10_2FF8",        # 0A, 10
        "Function_11_32DB",        # 0B, 11
        "Function_12_3474",        # 0C, 12
        "Function_13_4E20",        # 0D, 13
        "Function_14_4E5E",        # 0E, 14
        "Function_15_4E9C",        # 0F, 15
        "Function_16_4EDA",        # 10, 16
        "Function_17_4F18",        # 11, 17
        "Function_18_4F55",        # 12, 18
        "Function_19_5106",        # 13, 19
        "Function_20_52E3",        # 14, 20
    )


    def Function_0_24E(): pass

    label("Function_0_24E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_269")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_266")
    ClearChrFlags(0xD, 0x80)

    label("loc_266")

    Jump("loc_2A4")

    label("loc_269")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_289")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jump("loc_2A4")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_293")
    Jump("loc_2A4")

    label("loc_293")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_29D")
    Jump("loc_2A4")

    label("loc_29D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2A4")

    label("loc_2A4")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_2B0"),
        (SWITCH_DEFAULT, "loc_2C4"),
    )


    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C1")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_2C1")

    Jump("loc_2C4")

    label("loc_2C4")

    Return()

    # Function_0_24E end

    def Function_1_2C5(): pass

    label("Function_1_2C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2E1")
    OP_B1("t4139_y")
    Jump("loc_2EA")

    label("loc_2E1")

    OP_B1("t4139_n")

    label("loc_2EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_309")
    OP_64(0x0, 0x1)
    OP_72(0x2, 0x10)
    Jump("loc_32A")

    label("loc_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31D")
    OP_64(0x1, 0x1)
    OP_72(0x2, 0x10)
    Jump("loc_32A")

    label("loc_31D")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_71(0x2, 0x10)

    label("loc_32A")

    Jump("loc_33A")

    label("loc_32D")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_71(0x2, 0x10)

    label("loc_33A")

    Return()

    # Function_1_2C5 end

    def Function_2_33B(): pass

    label("Function_2_33B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_360")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4A2")

    label("loc_360")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_379")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4A2")

    label("loc_379")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4A2")

    label("loc_392")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4A2")

    label("loc_3AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C4")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4A2")

    label("loc_3C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4A2")

    label("loc_3DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F6")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4A2")

    label("loc_3F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4A2")

    label("loc_40F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_428")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4A2")

    label("loc_428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_441")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4A2")

    label("loc_441")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4A2")

    label("loc_45A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_473")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4A2")

    label("loc_473")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4A2")

    label("loc_48C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A2")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4A2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4A2")

    label("loc_4B7")

    Return()

    # Function_2_33B end

    def Function_3_4B8(): pass

    label("Function_3_4B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4DB")
    OP_8D(0xFE, -59290, 60000, -52170, 63360, 2000)
    Jump("Function_3_4B8")

    label("loc_4DB")

    Return()

    # Function_3_4B8 end

    def Function_4_4DC(): pass

    label("Function_4_4DC")

    TalkBegin(0x8)
    ClearChrFlags(0x8, 0x10)
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_501")
    SetChrSubChip(0x8, 1)
    Jump("loc_506")

    label("loc_501")

    SetChrSubChip(0x8, 2)

    label("loc_506")

    OP_8C(0x8, 180, 0)
    SetChrFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_A3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41B, 5)), scpexpr(EXPR_END)), "loc_5D8")

    ChrTalk(    #0
        0x8,
        (
            "#1113FIf it's come to this, then us acting\x01",
            "carelessly isn't a good idea.\x02\x03",

            "#1110FWhile this is disconcerting, we'll just stand\x01",
            "strong and wait for things to settle.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3C")

    label("loc_5D8")


    ChrTalk(    #1
        0x101,
        "#1000FHello, Ambassador Cochrane.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#1110FEstelle... Good timing.\x02\x03",

            "#1112FI will put this to you directly: do you have\x01",
            "any information about the situation?\x02\x03",

            "Given that the Royal Army seems to be acting\x01",
            "quite calmly and confidently, I assume this\x01",
            "situation was predicted?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1013F(Ugh, she's sharp...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#1113F...\x02\x03",

            "*sigh* It seems I've let myself get a bit\x01",
            "flustered by it all.\x02\x03",

            "#1110FI can guess Liberl has its own circumstances.\x02\x03",

            "Even if you knew anything, you probably\x01",
            "couldn't tell me everything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1016FEr... I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#1111FDon't worry about it.\x02\x03",

            "#1110FThinking about if our positions were reversed,\x01",
            "I really can't complain.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1000FAmbassador Cochrane...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "#1112FLet me just ask one thing, then.\x02\x03",

            "Are we okay to just wait like this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1011FWh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#1040F(She's asking if she can leave the\x01",
            "situation to the Bracer Guild... To us,\x01",
            "in other words. I think.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1006FY-Yes, of course!\x02\x03",

            "Right now the Bracer Guild and the\x01",
            "Royal Army are putting their full force\x01",
            "into investigating this.\x02\x03",

            "I'm sure we'll resolve this phenomenon\x01",
            "and get things back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "#1111FPlease do.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20DD)

    label("loc_A3C")

    Jump("loc_1136")

    label("loc_A3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1136")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_A55")
    Jump("loc_1136")

    label("loc_A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_FA4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 6)), scpexpr(EXPR_END)), "loc_AE2")

    ChrTalk(    #13
        0x8,
        (
            "#1110FThe ties that bind people sometimes\x01",
            "grant great power once bound.\x02\x03",

            "Since we've met, I'd like to value this bond.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FA1")

    label("loc_AE2")


    ChrTalk(    #14
        0x8,
        (
            "#1110FBracers... Hmm?\x02\x03",

            "#1111FYou have quite the adorable young lady\x01",
            "with you today.\x02\x03",

            "Are you the young lady from Crossbell we\x01",
            "were talking about yesterday?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1011FAh, no... This is someone else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x107,
        (
            "#064FUm, um...\x02\x03",

            "#060FNice to meet you. I'm Tita Russell.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#1112F...Russell?\x02\x03",

            "Are you perhaps related to the famous\x01",
            "Professor Russell?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        "#067FY-Yes, Professor Russell's my grandfather.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "#1113FI heard he had a daughter and a son in law,\x01",
            "but a granddaughter...\x02\x03",

            "#1111FBetween you and Estelle, I'm happy\x01",
            "to be so blessed with acquaintances.\x02\x03",

            "In Calvard, they say that 'Chance\x01",
            "meetings are no such thing.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x108,
        (
            "#070F'The reason your sleeves touch those of an unknown\x01",
            "person is because something connects you' is\x01",
            "another such saying in the Republic.\x02\x03",

            "Certainly, it's a widely shared sentiment\x01",
            "in the East.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#1110FYes, indeed. And perhaps meeting\x01",
            "Tita, too, is some kind of destiny.\x02\x03",

            "Not just that...\x02\x03",

            "Perhaps there is some great\x01",
            "meaning to all of you here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1018FHuh, it's kind of a nice thought.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "#1113FThe ties that bind people sometimes\x01",
            "grant great power once bound.\x02\x03",

            "#1111FOf course, that does not apply\x01",
            "to every such binding, but...\x02\x03",

            "Since we've met, I'd like to value this bond.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1656)

    label("loc_FA1")

    Jump("loc_1136")

    label("loc_FA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_1136")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107E")

    ChrTalk(    #24
        0x8,
        (
            "#1110FI wonder when Zin intends to\x01",
            "move up to being S-rank?\x02\x03",

            "Bracer experts, of which there\x01",
            "are only four on the continent...\x02\x03",

            "I'd love for the fifth S-rank bracer to come\x01",
            "from the Republic.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1136")

    label("loc_107E")


    ChrTalk(    #25
        0x8,
        (
            "#1110FEstelle Bright...\x02\x03",

            "Our embassy owes the guild greatly\x01",
            "for your constant support.\x02\x03",

            "Should we have any jobs come up, I would be\x01",
            "happy if you would be the one to take them on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1136")

    SetChrSubChip(0x8, 0)
    TalkEnd(0x8)
    Return()

    # Function_4_4DC end

    def Function_5_113F(): pass

    label("Function_5_113F")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_12F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_11F7")

    ChrTalk(    #26
        0xFE,
        (
            "Eventually, there should be an investigation\x01",
            "team sent from the Republic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "We need to gather as much information\x01",
            "as we can before then, but...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12F8")

    label("loc_11F7")


    ChrTalk(    #28
        0xFE,
        (
            "Given that all communication from Liberl has cut\x01",
            "off, I imagine the Republic is in quite a tizzy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Eventually, someone will send an investigation\x01",
            "team to represent them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "We need to gather as much information\x01",
            "as we can before then, but...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_12F8")

    Jump("loc_181E")

    label("loc_12FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_181E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1311")
    Jump("loc_181E")

    label("loc_1311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1513")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_13DF")

    ChrTalk(    #31
        0xFE,
        (
            "This time we'll be simply exchanging documents,\x01",
            "so it's not technically a 'signing.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Well, it's easier for the populace to visualize\x01",
            "a 'signed' accord, so it's being called that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1510")

    label("loc_13DF")


    ChrTalk(    #33
        0xFE,
        (
            "The process of the non-aggression pact\x01",
            "is twofold: signing and ratification.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Representatives confirm and accept the contents of\x01",
            "the pact, then as proof, sign their names to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Then the nation checks the content of the pact\x01",
            "one last time, and exchanges them with other\x01",
            "agreeing parties.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1510")

    Jump("loc_181E")

    label("loc_1513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_1640")

    ChrTalk(    #36
        0xFE,
        (
            "Ambassador Cochrane can at times come\x01",
            "across a bit too abrasive, and I need to step in\x01",
            "to smooth things over after she causes offense.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "She genuinely does care about her\x01",
            "country, though. That much I know\x01",
            "for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "As such, I'm more than happy to do\x01",
            "anything I can to help her.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181E")

    label("loc_1640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CA, 7)), scpexpr(EXPR_END)), "loc_1706")

    ChrTalk(    #39
        0xFE,
        (
            "The prepping for the signing ceremony has got\x01",
            "me so busy that I'd accept a cat's help if it\x01",
            "offered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Well, knowing that it's all for the sake of my\x01",
            "homeland, I'm happy to do it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181E")

    label("loc_1706")


    ChrTalk(    #41
        0xFE,
        "Oh, Zin. Come to Liberl again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x108,
        (
            "#070FHey, Yakumo. It seems I'll be here\x01",
            "for a while again.\x02\x03",

            "You seem pretty busy yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "Of course we are. After all, we've\x01",
            "got a pact signing approaching.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Ha ha, sorry, but I won't have time\x01",
            "to bother with you for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1657)

    label("loc_181E")

    TalkEnd(0x9)
    Return()

    # Function_5_113F end

    def Function_6_1822(): pass

    label("Function_6_1822")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_19DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_18E4")

    ChrTalk(    #45
        0xFE,
        (
            "We didn't have orbments when I was young,\x01",
            "so I'm not really fussed that they're out now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Perhaps now is exactly when I can\x01",
            "be of aid to the ambassador.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19DE")

    label("loc_18E4")


    ChrTalk(    #47
        0xFE,
        (
            "We didn't have orbments when I was young,\x01",
            "so I'm not really fussed that they're out now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "I understand why one would worry, since\x01",
            "orbments are so common nowadays, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Perhaps now is exactly when I can\x01",
            "be of aid to the ambassador.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_19DE")

    Jump("loc_1F3F")

    label("loc_19E1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1B16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A7B")

    ChrTalk(    #50
        0xFE,
        (
            "The ambassador does not hesitate to voice\x01",
            "her dislike of Erebonia, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "Those feelings come from somewhere else.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B13")

    label("loc_1A7B")


    ChrTalk(    #52
        0xFE,
        (
            "The ambassador does not hesitate to voice\x01",
            "her dislike of Erebonia, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "Those feelings come from somewhere else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "I know quite well.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1B13")

    Jump("loc_1F3F")

    label("loc_1B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1BE6")

    ChrTalk(    #55
        0xFE,
        (
            "Why, I wonder, would someone resort to\x01",
            "something so despicable as sending a\x01",
            "threat letter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        "For our countries to take hands as friends...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "Who could possibly stand to suffer from this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F3F")

    label("loc_1BE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1F3F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 0)), scpexpr(EXPR_END)), "loc_1E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_1D79")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1C72")

    ChrTalk(    #58
        0xFE,
        (
            "My recommendation, ah... yes, it\x01",
            "would have to be the Doll Knight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        "It's a very heartwarming story.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D76")

    label("loc_1C72")


    ChrTalk(    #60
        0xFE,
        (
            "If you have the time, why not read a\x01",
            "book here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "They say that books are nourishment for the\x01",
            "heart, so make sure you find time to read.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "My recommendation is... Ah, yes!\x01",
            "It would have to be the Doll Knight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "It's a very heartwarming story.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1D76")

    Jump("loc_1E20")

    label("loc_1D79")


    ChrTalk(    #64
        0xFE,
        (
            "Zin is always going back and forth\x01",
            "between Liberl and the Republic. It must\x01",
            "be hard on him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "Do take care not to push yourself\x01",
            "too hard and lose your health.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E20")

    Jump("loc_1F3F")

    label("loc_1E23")

    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #66
        0xFE,
        (
            "My, my, my! Is that hulk of a\x01",
            "man over there Zin?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I don't even need to see your\x01",
            "face to know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x108,
        (
            "#073FHey, hey! Are you seriously going\x01",
            "to judge based on my body size?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1001F...I thought you were a bear when\x01",
            "we first met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x105,
        "#044FMy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x108,
        "#070F...Geez.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1658)

    label("loc_1F3F")

    TalkEnd(0xA)
    Return()

    # Function_6_1822 end

    def Function_7_1F43(): pass

    label("Function_7_1F43")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1FE5")

    ChrTalk(    #72
        0xFE,
        "Even Ambassador Cochrane seems quite tired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Her efforts to gather information have taken\x01",
            "quite the toll on her sleep, apparently.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FE5")

    Jump("loc_288B")

    label("loc_1FE8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_288B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_20CD")

    ChrTalk(    #74
        0xFE,
        (
            "Seems like these Intelligence Division folk\x01",
            "were behind one of the recent incidents.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "Well, I doubt it will affect the signing ceremony.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "I can appreciate Queen Alicia's feelings\x01",
            "on the matter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_288B")

    label("loc_20CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2173")

    ChrTalk(    #77
        0xFE,
        (
            "The Crossbell Problem has been a\x01",
            "headache for Calvard as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "What kind of effect will this non-aggression\x01",
            "pact meeting have, I wonder...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2315")

    label("loc_2173")


    ChrTalk(    #79
        0xFE,
        (
            "The Crossbell Problem has been a\x01",
            "headache for Calvard as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "For now, the president is managing to\x01",
            "stave off the declarations of the opposition\x01",
            "party, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "There are no few that insist upon a\x01",
            "military annexation of the territory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "Every time this issue is brought up it causes\x01",
            "chaos in the Republican sessions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "What kind of effect will this non-aggression\x01",
            "pact meeting have, I wonder...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2315")

    Jump("loc_288B")

    label("loc_2318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_288B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 1)), scpexpr(EXPR_END)), "loc_255C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_24D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_23C9")

    ChrTalk(    #84
        0xFE,
        (
            "Ruan is a cornerstone of sea traffic, and\x01",
            "many Republican ships put to port there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "I need to check the results of the\x01",
            "mayoral election.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24D2")

    label("loc_23C9")


    ChrTalk(    #86
        0xFE,
        (
            "The Ruan mayoral election was today,\x01",
            "wasn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "The first commoner mayor of Ruan,\x01",
            "due to the dismantling of the Dalmore family,\x01",
            "huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "Ruan is a cornerstone of sea traffic, and\x01",
            "many Republican ships put to port there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "I need to check up on it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_24D2")

    Jump("loc_2559")

    label("loc_24D5")


    ChrTalk(    #90
        0xFE,
        (
            "There's also the possibility the\x01",
            "threat letter was just a prank.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "Why don't you see what Ambassador Cochrane\x01",
            "thinks first?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2559")

    Jump("loc_288B")

    label("loc_255C")


    ChrTalk(    #92
        0xFE,
        "Oh, you all are...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x108, 400)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #93
        0xFE,
        "Why, if it isn't Zin.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x108,
        "#070FCouncilor, a pleasure.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "All together here...\x01",
            "Are they your guests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x108,
        "#070FYes, they're co-workers with the guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "Are you here about the threat letter?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x108,
        (
            "#070FIt's as you guessed. It's a request\x01",
            "from the Royal Army.\x02\x03",

            "#072FDo you have any ideas?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "Threat letters like that aren't\x01",
            "exactly rare in the Republic...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "To be honest, I barely paid it any heed\x01",
            "at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x108,
        (
            "#572F...True, there are a lot of radical\x01",
            "groups in the country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "Yes, they always cause trouble when\x01",
            "the issue of immigration comes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "Well, this time at least I can't say anything.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2888")

    ChrTalk(    #104
        0xFE,
        (
            "Why don't you see what Ambassador Cochrane\x01",
            "thinks first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x108,
        (
            "#070FYes, we'll go do that right now.\x02\x03",

            "If you'll pardon us...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2888")

    OP_A2(0x1659)

    label("loc_288B")

    TalkEnd(0xB)
    Return()

    # Function_7_1F43 end

    def Function_8_288F(): pass

    label("Function_8_288F")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2A72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2969")

    ChrTalk(    #106
        0xFE,
        (
            "Lamps are inconvenient and need care when\x01",
            "handing, but there's something really\x01",
            "heartwarming about them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "It may be a bit inappropriate to be\x01",
            "thinking that right now, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A72")

    label("loc_2969")


    ChrTalk(    #108
        0xFE,
        (
            "Since orbal lighting doesn't work,\x01",
            "we're getting our light with lamps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "Lamps are inconvenient and need care when\x01",
            "handing, but there's something really\x01",
            "heartwarming about them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "It may be a bit inappropriate to be\x01",
            "thinking that right now, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2A72")

    Jump("loc_2E28")

    label("loc_2A75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2B19")

    ChrTalk(    #111
        0xFE,
        (
            "If you're looking for Ambassador Cochrane,\x01",
            "she's out inspecting the royal villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "After all, it is the site of the signing ceremony.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E28")

    label("loc_2B19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2C9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2BAB")

    ChrTalk(    #113
        0xFE,
        (
            "Imperial maids are very precise and seem\x01",
            "incredibly strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "I tried imitating them but I got exhausted in\x01",
            "ten minutes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C99")

    label("loc_2BAB")


    ChrTalk(    #115
        0xFE,
        (
            "Sometimes when I go out to the department\x01",
            "store for shopping I run into the Erebonian\x01",
            "embassy maids.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Imperial maids are very precise and seem\x01",
            "incredibly strict.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "I tried imitating them but I got exhausted in\x01",
            "ten minutes.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2C99")

    Jump("loc_2E28")

    label("loc_2C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2E28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CB, 2)), scpexpr(EXPR_END)), "loc_2D5B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_END)), "loc_2D02")

    ChrTalk(    #118
        0xFE,
        "La la la... ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "Maybe I'll go out shopping today.\x01",
            "It's been a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D58")

    label("loc_2D02")


    ChrTalk(    #120
        0xFE,
        "Zin, come by and stay any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "I'll have everything squeaky clean for you.\x02",
    )

    CloseMessageWindow()

    label("loc_2D58")

    Jump("loc_2E28")

    label("loc_2D5B")

    TurnDirection(0xFE, 0x108, 400)

    ChrTalk(    #122
        0xFE,
        "...Ah, Zin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x108,
        (
            "#071FHey, I'm back.\x02\x03",

            "#070FI might end up borrowing a room,\x01",
            "so I'll be in your care if that happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "Heehee, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "I'll have everything squeaky clean for you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x165A)

    label("loc_2E28")

    TalkEnd(0xC)
    Return()

    # Function_8_288F end

    def Function_9_2E2C(): pass

    label("Function_9_2E2C")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2FF4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2EE2")

    ChrTalk(    #126
        0xFE,
        (
            "My husband is off to Grancel Castle\x01",
            "to meet with the queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "I think he'll just end up waiting pointlessly\x01",
            "without an appointment, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF4")

    label("loc_2EE2")


    ChrTalk(    #128
        0xFE,
        "My husband is currently off at Grancel Castle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "He apparently wants to inquire directly\x01",
            "if there's any way to contact our home\x01",
            "country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "I think he'll just end up waiting pointlessly\x01",
            "without an appointment, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "As always, he is missing the point.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2FF4")

    TalkEnd(0xD)
    Return()

    # Function_9_2E2C end

    def Function_10_2FF8(): pass

    label("Function_10_2FF8")

    EventBegin(0x0)
    OP_6D(-2640, 6000, 31460, 0)
    OP_67(0, 10000, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(315000, 0)
    OP_6E(467, 0)
    SetChrPos(0x101, 1740, 0, 4440, 0)
    SetChrPos(0x108, 470, 0, 4430, 0)
    SetChrPos(0x104, 660, 0, 2980, 0)
    SetChrPos(0x105, 2100, 0, 3060, 0)

    def lambda_3081():
        OP_6D(1080, 0, 6030, 8000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_3081)

    def lambda_3099():
        OP_67(0, 9000, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_3099)
    OP_C8(0x200, 0x46, "C_PLAC12._CH", 0x1, 0x7D0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Fade(1000)
    OP_6D(1080, 0, 6030, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #132
        0x104,
        "#033FOoh. Magnificent!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1011F#5PWow, this is the Calvardian embassy?\x02\x03",

            "I didn't expect it to be quite so fancy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x105,
        (
            "#048FAnd yet it's a bit exotic, as well.\x01",
            "I really like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x108,
        (
            "#070F#6PWell, quite a few people from even farther\x01",
            "east have settled in Calvard, you know.\x01",
            "They've had an impact on our culture, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x108, 90, 400)

    ChrTalk(    #136
        0x108,
        (
            "#070F#6PAnyway, Elsa's office is the furthest room\x01",
            "on the second floor.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)

    ChrTalk(    #137
        0x101,
        "#1006F#2PAll-righty!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x161C)
    EventEnd(0x0)
    Return()

    # Function_10_2FF8 end

    def Function_11_32DB(): pass

    label("Function_11_32DB")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 1240, 6000, 30810, 0)
    SetChrPos(0x105, 1990, 6000, 29630, 0)
    SetChrPos(0x104, 890, 6000, 29500, 0)
    SetChrPos(0x108, 990, 6000, 32270, 180)
    OP_6D(880, 6000, 31940, 0)
    OP_67(0, 9360, -10000, 0)
    OP_6B(2360, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #138
        0x108,
        (
            "#070F#7PThis should be the ambassador's office.\x01",
            "Shall we say hello to Elsa?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Talk to Her\x01",          # 0
            "Come Back Later\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3418"),
        (1, "loc_346E"),
        (SWITCH_DEFAULT, "loc_3471"),
    )


    label("loc_3418")


    ChrTalk(    #139
        0x108,
        "#070F#7PAll right! Let me introduce you.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x108, 0, 400)
    Sleep(500)
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)
    FadeToDark(500, 0, -1)
    OP_0D()
    Call(0, 12)
    Jump("loc_3471")

    label("loc_346E")

    Jump("loc_3471")

    label("loc_3471")

    EventEnd(0x0)
    Return()

    # Function_11_32DB end

    def Function_12_3474(): pass

    label("Function_12_3474")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x108, 0x80)
    SetChrPos(0x101, 55250, 0, 53510, 0)
    SetChrPos(0x105, 55250, 0, 53510, 0)
    SetChrPos(0x104, 55250, 0, 53510, 0)
    SetChrPos(0x108, 53600, 0, 57290, 0)
    OP_6D(54510, 0, 65790, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(500, 0)
    OP_0D()
    OP_62(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #140
        0x8,
        (
            "#1112F#7PHm...?\x02\x03",

            "Yes, come in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x108,
        "#2PPardon us, Elsa.\x02",
    )

    CloseMessageWindow()
    OP_6D(54860, 0, 59130, 1500)
    SetChrPos(0x108, 55250, 0, 53510, 0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    def lambda_359B():
        OP_6D(54870, 0, 64209, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_359B)
    OP_43(0x108, 0x1, 0x0, 0xD)
    Sleep(700)
    OP_43(0x101, 0x1, 0x0, 0xE)
    Sleep(500)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_43(0x105, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0x104, 0x1, 0x0, 0x10)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #142
        0x8,
        (
            "#1111FWhy, Zin! Zin Vathek!\x01",
            "Hello, hello! Come in!\x02\x03",

            "Last I heard, you'd returned to Calvard.\x01",
            "What's an old dog like you doing back\x01",
            "here in Grancel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x108,
        (
            "#070F#5PHah, well! Let's just say this old dog\x01",
            "had a trick or two more to show off.\x02\x03",

            "I'll likely be here in Liberl for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x8,
        (
            "#1113FAs to be expected of an A-rank bracer,\x01",
            "I suppose. You never let up, do you?\x02\x03",

            "#1110FSo, who's this with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#1011F#5PUm, a pleasure to meet you, ma'am.\x02\x03",

            "I'm Estelle Bright, of the Bracer Guild.\x02\x03",

            "These are our, um, assistants--\x01",
            "Olivier Lenheim and Kloe Rinz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x104,
        "#035FA pleasure, Ambassador.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x105,
        "#048FIt's a pleasure to meet you, Ambassador.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "#1111FThe pleasure is mine.\x01",
            "I'm Elsa Cochrane, Calvard's ambassador\x01",
            "to Liberl.\x02\x03",

            "#1110FI...get the feeling this is a bit more\x01",
            "than a social call, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x108,
        "#074F#5PI'm afraid so...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #150
        (
            "\x07\x05Estelle and her party asked about the threatening\x01",
            "letter the embassy received.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #151
        0x8,
        (
            "#1113FAh, that letter, yes.\x02\x03",

            "#1112FYou're helping the Royal Army\x01",
            "investigate the matter, then?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#1002F#5PTechnically, yes.\x02\x03",

            "Threats of terrorism aren't exactly something\x01",
            "the guild can ignore either, though.\x02\x03",

            "Would you mind helping us out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x8,
        (
            "#1113FWell...I suppose. We're well stuck into\x01",
            "the situation, after all.\x02\x03",

            "#1110FWhat would you like to know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        (
            "#1015F#5PWell, uh. To start with, do you have any\x01",
            "idea who would've sent that letter?\x02\x03",

            "Like, does anyone in the Republic oppose\x01",
            "the signing of the pact, or...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x8,
        (
            "#1111FWell, of course.\x02\x03",

            "You're looking at one, after all.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #156
        0x101,
        "#1020F#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x108,
        (
            "#075F#5PElsa, please.\x02\x03",

            "Try not to tease the kids too much, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x8,
        (
            "#1110FWell, the truth's the truth, Zin.\x02\x03",

            "I'm pretty sure I've chewed your ear off\x01",
            "about Erebonia enough for you to know\x01",
            "what I think, hmm?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x108,
        "#073F#5PWell...yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x8,
        (
            "#1111FHaha. Still, Ms. Bright, don't\x01",
            "misunderstand me.\x02\x03",

            "President Rocksmith and Parliament have\x01",
            "already approved the pact.\x02\x03",

            "My personal feelings won't get in the\x01",
            "way of my job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#1007F#5PEr, right...\x02\x03",

            "#1015FIs there anyone else from Calvard\x01",
            "who might oppose the pact?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x8,
        (
            "#1113FOh, certainly. They're all tiny groups, though.\x02\x03",

            "And to be honest, there's no real reason\x01",
            "to oppose it, anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        "#1004F#5PNo...reason? I don't quite follow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x8,
        (
            "#1110FIt's not worth bothering!\x01",
            "The pact doesn't have any practical effect.\x02\x03",

            "It's simply agreeing to the statement 'We shall\x01",
            "not rely on violence to solve international\x01",
            "problems and negotiate instead.'\x02\x03",

            "It's more of a declaration than anything else.\x01",
            "But...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x104,
        (
            "#030FIt is little more than a promise which can\x01",
            "be broken without consequence, save a\x01",
            "loss of face, no?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        (
            "#1111FPrecisely. The worst it could do would be to\x01",
            "rally other countries against the aggressor.\x02\x03",

            "#1110FNow, it's true that relations between Erebonia\x01",
            "and Calvard have gotten even WORSE than\x01",
            "usual over the past decade...\x02\x03",

            "So there is some value in establishing Liberl\x01",
            "as a place where we can negotiate.\x01",
            "But again, who'd bother opposing that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#1015F#5PYeah...\x02\x03",

            "It doesn't really seem like the thing you'd\x01",
            "send a bunch of threatening letters about.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x105,
        (
            "#047FWell, Ambassador Cochrane.\x02\x03",

            "#042FIf you don't believe someone from Calvard\x01",
            "is the perpetrator, then whom do you suspect?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x8,
        (
            "#1110FHeh... Well.\x02\x03",

            "My gut, of course, tells me to blame it all on\x01",
            "the Erebonians. Their militaristic 'hawk'\x01",
            "faction, specifically.\x02\x03",

            "#1113FBut frankly...even they have that new engine on\x01",
            "the line. They aren't so stupid as to cut off\x01",
            "their noses to spite their faces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#1004F#5PThe new engine? Wait, you mean the one\x01",
            "from the Arseille?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        (
            "#1111FYes. An engineering sample will be provided\x01",
            "to both Calvard and Erebonia.\x02\x03",

            "It'll happen right after the signing, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        "#1004F#5PWhoa!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x104,
        (
            "#031FAh, as to be expected of Queen Alicia.\x02\x03",

            "She holds both Empire and Republic in\x01",
            "the palm of her hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x8,
        (
            "#1113FYes. I have to admit, she's handled this\x01",
            "masterfully.\x02\x03",

            "#1112FThat cutting-edge engine is going to birth a\x01",
            "whole new generation of airship designs.\x02\x03",

            "And Alicia is practically handing it out, so long\x01",
            "as you sign this agreement...and play nice with\x01",
            "it and each other, at least for a while.\x02\x03",

            "Even the most testosterone-poisoned ninnies\x01",
            "among the Erebonian hawks wouldn't want to\x01",
            "miss this chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#1016F#5PYeah, I guess so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x108,
        (
            "#070F#5PWhich means, of course...\x02\x03",

            "...that the possibility that either the Republic\x01",
            "OR the Empire interfering directly is pretty\x01",
            "low.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        (
            "#1110FIndeed.\x02\x03",

            "I'm sorry I can't be of more help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x101,
        (
            "#1006F#5PNo, you were a big help!\x02\x03",

            "Just being able to cross suspects\x01",
            "off the list helps a lot!\x02\x03",

            "#1004FOh, speaking of which, though,\x01",
            "we'd like to ask you about\x01",
            "something else...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #179
        "\x07\x05Estelle asked Ambassador Cochrane about Renne's parents.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #180
        0x8,
        (
            "#1112FHarold Hayworth, a merchant from\x01",
            "Crossbell... Hmm...\x02\x03",

            "#1113FI can't say it rings any bells, I'm sorry.\x02\x03",

            "He's never visited the embassy, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        "#1007F#5PDarn... Well, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x8,
        (
            "#1110FDo remember that Crossbell sits directly\x01",
            "between Erebonia and Calvard, however.\x02\x03",

            "You may want to inquire at the Erebonian\x01",
            "embassy, as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x101,
        (
            "#1006F#5POkay, thanks, Ambassador.\x02\x03",

            "And thanks for being so open with us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x8,
        (
            "#1110FYou're quite welcome.\x01",
            "I'm glad I could help.\x02\x03",

            "By the way...you said your name\x01",
            "was Estelle Bright.\x02\x03",

            "You wouldn't happen to be Brigadier General Bright's\x01",
            "daughter?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x101,
        "#1004F#5POh! You know Dad?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x8,
        (
            "#1111FHaha! Of course.\x02\x03",

            "The heroic vanquisher of the Imperial Army,\x01",
            "and now the head of Liberl's Royal Army...\x02\x03",

            "I'd heard he had a daughter, but I didn't\x01",
            "expect to meet you like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        (
            "#1015F#5PEr, um, well, I'm just kind of an inexperienced\x01",
            "newbie myself, still...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x8,
        (
            "#1110FYou're off to a good start, then, I think.\x02\x03",

            "We at the embassy have relied on the\x01",
            "guild a number of times in the past.\x02\x03",

            "Should the time come again, I hope you'll\x01",
            "aid us, Ms. Bright.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        (
            "#1016F#5PAhaha... Well, if the chance comes up, sure!\x02\x03",

            "#1006FWell, we'll see you around!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 55140, 0, 59720, 180)
    SetChrPos(0x1, 55140, 0, 59720, 180)
    SetChrPos(0x2, 55140, 0, 59720, 180)
    SetChrPos(0x3, 55140, 0, 59720, 180)
    OP_6D(55140, 0, 59720, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_71(0x2, 0x10)
    OP_64(0x0, 0x1)
    OP_A2(0x161D)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_28(0x8B, 0x2, 0x8)
    OP_28(0x8B, 0x1, 0x10)
    EventEnd(0x0)
    Return()

    # Function_12_3474 end

    def Function_13_4E20(): pass

    label("Function_13_4E20")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4E36():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4E36)
    OP_8E(0xFE, 0xDA7A, 0x0, 0xF528, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_4E20 end

    def Function_14_4E5E(): pass

    label("Function_14_4E5E")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4E74():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4E74)
    OP_8E(0xFE, 0xD6EC, 0x0, 0xF2EE, 0x9C4, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_14_4E5E end

    def Function_15_4E9C(): pass

    label("Function_15_4E9C")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4EB2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4EB2)
    OP_8E(0xFE, 0xDA52, 0x0, 0xEDEE, 0x9C4, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_15_4E9C end

    def Function_16_4EDA(): pass

    label("Function_16_4EDA")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)

    def lambda_4EF0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4EF0)
    OP_8E(0xFE, 0xD566, 0x0, 0xEDA8, 0x9C4, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_16_4EDA end

    def Function_17_4F18(): pass

    label("Function_17_4F18")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #190
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_17_4F18 end

    def Function_18_4F55(): pass

    label("Function_18_4F55")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #191
        "\x07\x05This shelf holds [The Doll Knight] series.\x02",
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
            "[Read Chapter 7]\x01",      # 6
            "[Read Chapter 8]\x01",      # 7
            "[Stop]\x01",                # 8
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5084")
    OP_B8(0x2EE, 0x0)

    label("loc_5084")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5096")
    OP_B8(0x2EF, 0x0)

    label("loc_5096")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50A8")
    OP_B8(0x2F0, 0x0)

    label("loc_50A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50BA")
    OP_B8(0x2F1, 0x0)

    label("loc_50BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50CC")
    OP_B8(0x2F2, 0x0)

    label("loc_50CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50DE")
    OP_B8(0x2F3, 0x0)

    label("loc_50DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50F0")
    OP_B8(0x2F4, 0x0)

    label("loc_50F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5102")
    OP_B8(0x2F5, 0x0)

    label("loc_5102")

    TalkEnd(0xFF)
    Return()

    # Function_18_4F55 end

    def Function_19_5106(): pass

    label("Function_19_5106")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #192
        "\x07\x05This shelf holds [The Doll Knight] series.\x02",
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
            "[Read Chapter 9]\x01",       # 0
            "[Read Chapter 10]\x01",      # 1
            "[Read Chapter 11]\x01",      # 2
            "[Read Chapter 12]\x01",      # 3
            "[Read Chapter 13]\x01",      # 4
            "[Read Chapter 14]\x01",      # 5
            "[Read Chapter 15]\x01",      # 6
            "[Read Chapter 16]\x01",      # 7
            "[Stop]\x01",                 # 8
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_523C")
    OP_B8(0x2F6, 0x0)

    label("loc_523C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_524E")
    OP_B8(0x2F7, 0x0)

    label("loc_524E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5260")
    OP_B8(0x2F8, 0x0)

    label("loc_5260")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5272")
    OP_B8(0x2F9, 0x0)

    label("loc_5272")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5284")
    OP_B8(0x2FA, 0x0)

    label("loc_5284")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5296")
    OP_B8(0x2FB, 0x0)

    label("loc_5296")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52CD")
    OP_B8(0x2FC, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52CD")
    Sleep(500)
    Call(1, 0)

    label("loc_52CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52DF")
    OP_B8(0x2FD, 0x0)

    label("loc_52DF")

    TalkEnd(0xFF)
    Return()

    # Function_19_5106 end

    def Function_20_52E3(): pass

    label("Function_20_52E3")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #193
        "\x07\x05This shelf holds [The Doll Knight] series.\x02",
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
            "[Read Chapter 17]\x01",      # 0
            "[Read Chapter 18]\x01",      # 1
            "[Read Chapter 19]\x01",      # 2
            "[Read Chapter 20]\x01",      # 3
            "[Read Chapter 21]\x01",      # 4
            "[Read Finale]\x01",          # 5
            "[Stop]\x01",                 # 6
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53F2")
    OP_B8(0x2FE, 0x0)

    label("loc_53F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5404")
    OP_B8(0x2FF, 0x0)

    label("loc_5404")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5416")
    OP_B8(0x300, 0x0)

    label("loc_5416")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5428")
    OP_B8(0x301, 0x0)

    label("loc_5428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_543A")
    OP_B8(0x302, 0x0)

    label("loc_543A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_544C")
    OP_B8(0x303, 0x0)

    label("loc_544C")

    TalkEnd(0xFF)
    Return()

    # Function_20_52E3 end

    SaveToFile()

Try(main)
