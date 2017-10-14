from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1300   ._SN',
        MapName             = 'Bose',
        Location            = 'T1300.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        'Private Cutinger',                     # 9
        'Private Usher',                        # 10
        'Manoria Coast',                        # 11
        'West Bose Highway',                    # 12
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
        'ED6_DT07/CH01640 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01640P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
    )

    DeclNpc(
        X                   = -47800,
        Z                   = -50,
        Y                   = 11380,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -47800,
        Z                   = -50,
        Y                   = -8500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -50220,
        Z                   = -500,
        Y                   = -35780,
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

    DeclNpc(
        X                   = -40370,
        Z                   = -500,
        Y                   = 36990,
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


    DeclActor(
        TriggerX            = -51690,
        TriggerZ            = -470,
        TriggerY            = 23510,
        TriggerRange        = 1500,
        ActorX              = -51690,
        ActorZ              = 1800,
        ActorY              = 23510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -53780,
        TriggerZ            = -510,
        TriggerY            = -19530,
        TriggerRange        = 1500,
        ActorX              = -53780,
        ActorZ              = 1900,
        ActorY              = -19530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -42460,
        TriggerZ            = -50,
        TriggerY            = -11830,
        TriggerRange        = 1700,
        ActorX              = -42460,
        ActorZ              = 1200,
        ActorY              = -11830,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A6",          # 00, 0
        "Function_1_1BF",          # 01, 1
        "Function_2_21A",          # 02, 2
        "Function_3_397",          # 03, 3
        "Function_4_A4D",          # 04, 4
        "Function_5_1029",         # 05, 5
        "Function_6_1057",         # 06, 6
        "Function_7_10E3",         # 07, 7
        "Function_8_1174",         # 08, 8
    )


    def Function_0_1A6(): pass

    label("Function_0_1A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1BE")
    SetChrPos(0x9, -45660, -50, -12110, 90)

    label("loc_1BE")

    Return()

    # Function_0_1A6 end

    def Function_1_1BF(): pass

    label("Function_1_1BF")

    OP_16(0x2, 0xFA0, 0xFFFD48B0, 0xFFFE17B8, 0x230044)
    OP_B1("T1300_n")
    OP_71(0x0, 0x10)
    OP_1C(0x0, 0x0, 0x8)
    OP_1C(0x1, 0x0, 0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D")
    OP_72(0x0, 0x10)
    OP_6F(0x0, 99)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 99)

    label("loc_20D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219")
    OP_64(0x2, 0x1)

    label("loc_219")

    Return()

    # Function_1_1BF end

    def Function_2_21A(): pass

    label("Function_2_21A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_381")

    label("loc_23F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_258")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_381")

    label("loc_258")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_271")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_381")

    label("loc_271")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_381")

    label("loc_28A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A3")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_381")

    label("loc_2A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BC")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_381")

    label("loc_2BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_381")

    label("loc_2D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_381")

    label("loc_2EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_307")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_381")

    label("loc_307")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_320")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_381")

    label("loc_320")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_339")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_381")

    label("loc_339")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_352")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_381")

    label("loc_352")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_381")

    label("loc_36B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_381")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_381")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_396")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_381")

    label("loc_396")

    Return()

    # Function_2_21A end

    def Function_3_397(): pass

    label("Function_3_397")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_564")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A4")

    ChrTalk(    #0
        0xFE,
        (
            "The Orbal Shutdown Phenomenon\x01",
            "occurred immediately after that floating\x01",
            "object appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Just as I thought the lights had gone out\x01",
            "here, a flash ran across the sky above\x01",
            "the lake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "It was bright, almost like the dawning\x01",
            "of the sun.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_561")

    label("loc_4A4")


    ChrTalk(    #3
        0xFE,
        (
            "The Orbal Shutdown Phenomenon\x01",
            "occurred immediately after that floating\x01",
            "object appeared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "Just as I thought the lights had gone out\x01",
            "here, a flash ran across the sky above\x01",
            "the lake.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_561")

    Jump("loc_A49")

    label("loc_564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_78F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EA")

    ChrTalk(    #5
        0xFE,
        (
            "You can see the floating object very clearly\x01",
            "from the Ruan side of the checkpoint.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Usher's even abandoned his post to\x01",
            "look at the damn thing. Hmph!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "...Though I'd be lying if I said I wasn't\x01",
            "curious about it myself...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "If only Colonel Richard and the Intelligence\x01",
            "Division were still in service!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "I'm sure he'd have answers for all\x01",
            "our questions.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_78C")

    label("loc_6EA")


    ChrTalk(    #10
        0xFE,
        (
            "We still don't have an official answer\x01",
            "for what that object in the sky is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "If only Colonel Richard and the Intelligence\x01",
            "Division were still in service!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_78C")

    Jump("loc_A49")

    label("loc_78F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_822")

    ChrTalk(    #12
        0xFE,
        (
            "Along with all scheduled flights resuming,\x01",
            "the market has reopened for business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "Feels like everything's finally settled down.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A49")

    label("loc_822")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_8C8")

    ChrTalk(    #14
        0xFE,
        (
            "Thanks to this dragon business,\x01",
            "the entire post is on high alert.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "I kind of doubt a dragon would bother\x01",
            "with us, but nothing beats being careful.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A49")

    label("loc_8C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_974")

    ChrTalk(    #16
        0xFE,
        (
            "Lately there have been a number of\x01",
            "powerful monsters on the roads,\x01",
            "making them dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Feel free to use the post facilities to\x01",
            "get some rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A49")

    label("loc_974")


    ChrTalk(    #18
        0xFE,
        (
            "Hello! Good work making it all the\x01",
            "way out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "Lately, there have been a number\x01",
            "of powerful monsters on the roads,\x01",
            "making them dangerous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Feel free to use the post facilities\x01",
            "to get some rest.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A49")

    TalkEnd(0x8)
    Return()

    # Function_3_397 end

    def Function_4_A4D(): pass

    label("Function_4_A4D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_BE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2F")

    ChrTalk(    #21
        0xFE,
        (
            "What's going on now HAS to be related\x01",
            "to that floating thing, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "We really should just shoot it down\x01",
            "already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Ah, but I know it's not that easy.\x01",
            "Our cannons don't work, for starters.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_BDE")

    label("loc_B2F")


    ChrTalk(    #24
        0xFE,
        (
            "And we don't have any gunpowder\x01",
            "cannons that can reach that far, and\x01",
            "obviously airships are right out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "In short, shooting it down is just this\x01",
            "side of impossible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BDE")

    Jump("loc_1025")

    label("loc_BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C81")

    ChrTalk(    #26
        0xFE,
        "You can see the floating object from here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "No matter how I look at it,\x01",
            "it has to be man-made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        "Can we really just ignore it?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_CDC")

    label("loc_C81")


    ChrTalk(    #29
        0xFE,
        (
            "No matter how I look at it,\x01",
            "it has to be man-made.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "Can we really just ignore it?\x02",
    )

    CloseMessageWindow()

    label("loc_CDC")

    Jump("loc_1025")

    label("loc_CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_D38")

    ChrTalk(    #31
        0xFE,
        "Hello there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "It must've been quite the trip to\x01",
            "make it out this far.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1025")

    label("loc_D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_F18")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DEF")

    ChrTalk(    #33
        0xFE,
        (
            "If we could just catch those bandits or\x01",
            "the traitors, we'd have an even easier\x01",
            "time of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Doesn't look like we'll be letting our\x01",
            "guard down any time soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F15")

    label("loc_DEF")

    OP_A2(0x1)

    ChrTalk(    #35
        0xFE,
        (
            "With modern airship travel being what\x01",
            "it is, we don't see a lot of traffic through\x01",
            "here anymore.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "In a way, though, that just makes\x01",
            "it harder to find the sky bandits or the\x01",
            "remnants of the Intelligence Division.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Doesn't look like we'll be letting our\x01",
            "guard down any time soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F15")

    Jump("loc_1025")

    label("loc_F18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1025")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F8B")

    ChrTalk(    #38
        0xFE,
        (
            "There are a lot of strong monsters on the\x01",
            "roads these days. Feel free to get some\x01",
            "rest here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1025")

    label("loc_F8B")

    OP_A2(0x1)

    ChrTalk(    #39
        0xFE,
        (
            "Oh, travelers! Your sort is kind of rare\x01",
            "these days, what with all the monsters\x01",
            "on the roads.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "Go ahead and get some rest.\x01",
            "I bet you need it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1025")

    TalkEnd(0xFE)
    Return()

    # Function_4_A4D end

    def Function_5_1029(): pass

    label("Function_5_1029")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x2400CF, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    Sleep(500)
    OP_A2(0x20EA)
    TalkEnd(0xFF)
    Return()

    # Function_5_1029 end

    def Function_6_1057(): pass

    label("Function_6_1057")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #41
        (
            "\x07\x05East: City of Bose - 441 selge\x01",
            "SW: City of Ruan - 669 selge   Manoria Village - 357 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_6_1057 end

    def Function_7_10E3(): pass

    label("Function_7_10E3")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #42
        (
            "\x07\x05South: City of Ruan - 669 selge   Manoria Village - 357 selge\x01",
            "NE: City of Bose - 441 selge    \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_10E3 end

    def Function_8_1174(): pass

    label("Function_8_1174")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_8_1174 end

    SaveToFile()

Try(main)
