from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2200   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        'Gartner',                              # 9
        'Provost Guardsman',                    # 10
        'Ruan - South Block',                   # 11
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
        'ED6_DT07/CH01460 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01460P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
    )

    DeclNpc(
        X                   = 98500,
        Z                   = 0,
        Y                   = 17600,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 110290,
        Z                   = 1990,
        Y                   = 24010,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 68010,
        Z                   = 0,
        Y                   = 21970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_127",          # 01, 1
        "Function_2_13F",          # 02, 2
        "Function_3_1E1",          # 03, 3
        "Function_4_35E",          # 04, 4
        "Function_5_8A1",          # 05, 5
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_126")
    SetChrFlags(0x9, 0x80)

    label("loc_126")

    Return()

    # Function_0_11A end

    def Function_1_127(): pass

    label("Function_1_127")

    OP_16(0x2, 0xFA0, 0xFFFFC180, 0xFFFE5A20, 0x23004A)
    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_127 end

    def Function_2_13F(): pass

    label("Function_2_13F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1E0")
    OP_8E(0xFE, 0x181E6, 0x0, 0x4A60, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x180C4, 0x0, 0x44C0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x17B10, 0x0, 0x42CC, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x17A98, 0x0, 0x48C6, 0xBB8, 0x0)
    OP_8C(0xFE, 120, 400)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0xFE)
    Jump("Function_2_13F")

    label("loc_1E0")

    Return()

    # Function_2_13F end

    def Function_3_1E1(): pass

    label("Function_3_1E1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_206")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_348")

    label("loc_206")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_348")

    label("loc_21F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_348")

    label("loc_238")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_251")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_348")

    label("loc_251")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_348")

    label("loc_26A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_348")

    label("loc_283")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29C")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_348")

    label("loc_29C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_348")

    label("loc_2B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CE")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_348")

    label("loc_2CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_348")

    label("loc_2E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_348")

    label("loc_300")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_319")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_348")

    label("loc_319")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_348")

    label("loc_332")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_348")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_348")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_35D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_348")

    label("loc_35D")

    Return()

    # Function_3_1E1 end

    def Function_4_35E(): pass

    label("Function_4_35E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_525")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_409")

    ChrTalk(    #0
        0xFE,
        (
            "Once the next mayor is decided, the\x01",
            "mansion will once again belong to the\x01",
            "citizens of Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "We also desire that a worthy person\x01",
            "reside here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_522")

    label("loc_409")

    OP_A2(0x1)

    ChrTalk(    #2
        0xFE,
        (
            "Once the next mayor is decided, the\x01",
            "mansion will once again belong to the\x01",
            "citizens of Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Doesn't matter which candidate wins.\x01",
            "He'll be the first commoner to become\x01",
            "mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I wonder if the remnants of the old\x01",
            "noble rule will continue to be wiped\x01",
            "away like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_522")

    Jump("loc_89D")

    label("loc_525")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_677")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5C8")

    ChrTalk(    #5
        0xFE,
        (
            "Improving our cooperation with the\x01",
            "guild is a target objective for the entire\x01",
            "army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "The brass has been pushing for it a lot\x01",
            "these days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_674")

    label("loc_5C8")

    OP_A2(0x1)

    ChrTalk(    #7
        0xFE,
        (
            "I was told there was some kind of\x01",
            "disturbance, but there's nothing out\x01",
            "of the ordinary here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "If anything comes up, we'll contact\x01",
            "the Bracer Guild immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_674")

    Jump("loc_89D")

    label("loc_677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_806")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_72D")

    ChrTalk(    #9
        0xFE,
        (
            "The maids here are really kind.\x01",
            "They even serve us tea!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "The food they serve is also pretty\x01",
            "amazing, so I really don't want to go\x01",
            "back to the fortress.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_803")

    label("loc_72D")

    OP_A2(0x1)

    ChrTalk(    #11
        0xFE,
        (
            "This manor is currently under the\x01",
            "purview of the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "You're welcome to enter as you wish,\x01",
            "but there are valuable items inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "We ask that you take care inside\x01",
            "so that nothing is damaged.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_803")

    Jump("loc_89D")

    label("loc_806")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_89D")

    ChrTalk(    #14
        0xFE,
        (
            "This manor is currently under the\x01",
            "purview of the Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "It's scheduled to be used as a city\x01",
            "hall once the next mayor is elected.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89D")

    TalkEnd(0xFE)
    Return()

    # Function_4_35E end

    def Function_5_8A1(): pass

    label("Function_5_8A1")

    TalkBegin(0xFE)
    OP_63(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_908")

    ChrTalk(    #16
        0xFE,
        (
            "A bracer ran by just a moment ago\x01",
            "in a real hurry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "I wonder what's goin' on.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CB9")

    label("loc_908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_9B2")

    ChrTalk(    #18
        0xFE,
        (
            "Our new mayor's been elected, and I'm\x01",
            "feeling more motivated than ever before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Thankfully, taking care of the shrubs\x01",
            "has nothin' to do with orbments.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB9")

    label("loc_9B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_A26")

    ChrTalk(    #20
        0xFE,
        (
            "Phew! My stomach's tellin' me it's\x01",
            "about time for food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "Guess I'll peek into the kitchen later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CB9")

    label("loc_A26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_AB2")

    ChrTalk(    #22
        0xFE,
        "Y'know, since the soldiers are here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Might be fun to shape one of the\x01",
            "shrubs or hedges into a guardsman\x01",
            "or somethin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB9")

    label("loc_AB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B24")

    ChrTalk(    #24
        0xFE,
        (
            "Knowin' this is the garden of the\x01",
            "queen herself, well, it makes ya\x01",
            "wanna do a good job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD6")

    label("loc_B24")

    OP_A2(0x0)

    ChrTalk(    #25
        0xFE,
        (
            "This mansion belongs to the\x01",
            "Royal Army now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "So, that makes our new employer\x01",
            "Queen Alicia!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Heh, nothin' more a craftsman could\x01",
            "ask for than to work for a queen.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BD6")

    Jump("loc_CB9")

    label("loc_BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_CB9")

    ChrTalk(    #28
        0xFE,
        (
            "It's been a while since the last mayor\x01",
            "was arrested.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "But I like this job a lot. I wouldn't mind\x01",
            "workin' here forever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I ain't been told nothin' different since\x01",
            "the arrest, so I've just kept on working.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CB9")

    TalkEnd(0xFE)
    Return()

    # Function_5_8A1 end

    SaveToFile()

Try(main)
