from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1230   ._SN',
        MapName             = 'Bose',
        Location            = 'T1230.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Apple',                                # 9
        'Limon',                                # 10
        'Lewey',                                # 11
        'Fran',                                 # 12
        'Pesca',                                # 13
        'Figaro',                               # 14
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
        'ED6_DT07/CH01050 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01470 ._CH',             # 02
        'ED6_DT07/CH01070 ._CH',             # 03
        'ED6_DT07/CH01143 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01050P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01470P._CP',             # 02
        'ED6_DT07/CH01070P._CP',             # 03
        'ED6_DT07/CH01143P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
    )

    DeclNpc(
        X                   = -730,
        Z                   = 0,
        Y                   = 5300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 440,
        Z                   = 0,
        Y                   = 32439,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -3550,
        Z                   = 0,
        Y                   = 32400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -3550,
        Z                   = 0,
        Y                   = 31160,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -940,
        Z                   = 300,
        Y                   = 34630,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1D4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -750,
        Z                   = 0,
        Y                   = 35490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    DeclActor(
        TriggerX            = -780,
        TriggerZ            = 0,
        TriggerY            = 4190,
        TriggerRange        = 400,
        ActorX              = -700,
        ActorZ              = 1500,
        ActorY              = 5300,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1500,
        TriggerZ            = 0,
        TriggerY            = 31600,
        TriggerRange        = 400,
        ActorX              = 440,
        ActorZ              = 1500,
        ActorY              = 32439,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1E2",          # 00, 0
        "Function_1_20D",          # 01, 1
        "Function_2_277",          # 02, 2
        "Function_3_3F4",          # 03, 3
        "Function_4_3F9",          # 04, 4
        "Function_5_C25",          # 05, 5
        "Function_6_C2A",          # 06, 6
        "Function_7_1802",         # 07, 7
        "Function_8_1DFA",         # 08, 8
        "Function_9_20B0",         # 09, 9
        "Function_10_23E0",        # 0A, 10
    )


    def Function_0_1E2(): pass

    label("Function_0_1E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1FB")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_20C")

    label("loc_1FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_20C")
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    label("loc_20C")

    Return()

    # Function_0_1E2 end

    def Function_1_20D(): pass

    label("Function_1_20D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_220")
    OP_B1("T1230_n")
    Jump("loc_23C")

    label("loc_220")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_233")
    OP_B1("T1230_y")
    Jump("loc_23C")

    label("loc_233")

    OP_B1("T1230_n")

    label("loc_23C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24D")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_263")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x0)
    OP_10(0x8, 0x1)
    OP_10(0x9, 0x1)
    Jump("loc_276")

    label("loc_263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_276")
    OP_10(0x0, 0x0)
    OP_10(0x5, 0x0)
    OP_10(0x6, 0x1)
    OP_10(0x7, 0x1)

    label("loc_276")

    Return()

    # Function_1_20D end

    def Function_2_277(): pass

    label("Function_2_277")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29C")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_3DE")

    label("loc_29C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_3DE")

    label("loc_2B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CE")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_3DE")

    label("loc_2CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_3DE")

    label("loc_2E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_3DE")

    label("loc_300")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_319")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_3DE")

    label("loc_319")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_3DE")

    label("loc_332")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_3DE")

    label("loc_34B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_364")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_3DE")

    label("loc_364")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37D")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_3DE")

    label("loc_37D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_396")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_3DE")

    label("loc_396")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_3DE")

    label("loc_3AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C8")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_3DE")

    label("loc_3C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DE")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_3DE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F3")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_3DE")

    label("loc_3F3")

    Return()

    # Function_2_277 end

    def Function_3_3F4(): pass

    label("Function_3_3F4")

    Call(0, 4)
    Return()

    # Function_3_3F4 end

    def Function_4_3F9(): pass

    label("Function_4_3F9")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_459")
    OP_0D()
    OP_A9(0x47)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_459")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46A")
    TalkEnd(0x8)
    Return()

    label("loc_46A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_566")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_514")

    ChrTalk(    #0
        0x8,
        "Things certainly have been crazy lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "Dragons burning villages, islands\x01",
            "floating in the sky...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "I really hope nothing ELSE happens.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_563")

    label("loc_514")


    ChrTalk(    #3
        0x8,
        "We just want to live peacefully!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        "I really hope nothing ELSE happens.\x02",
    )

    CloseMessageWindow()

    label("loc_563")

    Jump("loc_C21")

    label("loc_566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_711")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_670")

    ChrTalk(    #5
        0x8,
        "Welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "So...I guess the orbments have stopped\x01",
            "even in Ravennue, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "I, um, didn't notice, since I don't\x01",
            "leave the shop much...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "...Limon wouldn't let me hear the end\x01",
            "of my 'obliviousness' when she came in\x01",
            "earlier. Mrrrr...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_70E")

    label("loc_670")


    ChrTalk(    #9
        0x8,
        "We've always used oil lamps in this store!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "And the clock over there is real,\x01",
            "pre-orbal clockwork!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "I mean, really, how was I supposed to\x01",
            "know?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70E")

    Jump("loc_C21")

    label("loc_711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_88A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7BA")

    ChrTalk(    #12
        0x8,
        (
            "The orchard's been cleaned up, and life\x01",
            "is getting a little back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "We'll keep at it, working toward the\x01",
            "day our saplings bear fruit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_887")

    label("loc_7BA")


    ChrTalk(    #14
        0x8,
        "Ah, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "The orchard's been cleaned up, and life\x01",
            "is getting a little back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "The day will come when those new saplings\x01",
            "bear fruit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "And until then, we'll just keep at it!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_887")

    Jump("loc_C21")

    label("loc_88A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_9C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_900")

    ChrTalk(    #18
        0x8,
        "The orchard folks were up late talking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "I'm sure it's hard, but I hope they do\x01",
            "their best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BD")

    label("loc_900")


    ChrTalk(    #20
        0x8,
        "The orchard folks were up late talking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "It has to be rough for them, but I'm\x01",
            "sure they'll pull through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "Our stores, our VILLAGE, exist because\x01",
            "of the orchards, after all!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9BD")

    Jump("loc_C21")

    label("loc_9C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_ADF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A40")

    ChrTalk(    #23
        0x8,
        "*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        (
            "Limon came over to tell me to cheer up,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        "I can't. I just can't! I feel how I feel.\x02",
    )

    CloseMessageWindow()
    Jump("loc_ADC")

    label("loc_A40")


    ChrTalk(    #26
        0x8,
        "Ah, welcome...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "Limon came over to tell me to cheer up,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        "I can't. I just can't! I feel how I feel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x8,
        "*sigh* What a day it's been.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_ADC")

    Jump("loc_C21")

    label("loc_ADF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_C21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B7C")

    ChrTalk(    #30
        0x8,
        (
            "Our fruit that had finally come to,\x01",
            "well, fruition is all gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "I can't even find anything encouraging\x01",
            "to say to everyone else...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C21")

    label("loc_B7C")


    ChrTalk(    #32
        0x8,
        "It looks like the fire's out...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        (
            "But all the fruit that had finally\x01",
            "come to, well, fruition is gone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "What can I even say to the orchard\x01",
            "tenders...?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_C21")

    TalkEnd(0x8)
    Return()

    # Function_4_3F9 end

    def Function_5_C25(): pass

    label("Function_5_C25")

    Call(0, 6)
    Return()

    # Function_5_C25 end

    def Function_6_C2A(): pass

    label("Function_6_C2A")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",       # 0
            "Shop\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8A")
    OP_0D()
    OP_A9(0x48)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_C8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9B")
    TalkEnd(0x9)
    Return()

    label("loc_C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_11EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E90")
    TurnDirection(0x9, 0x106, 0)

    ChrTalk(    #35
        0x9,
        "Oh, my, hello, Agate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        "Here on work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x106,
        (
            "#050FNah, not work, exactly.\x02\x03",

            "Just came by to see how everyone's doin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x9,
        "Ah, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x9,
        (
            "Well, with the orbments stopped, everyone's\x01",
            "in a bit of a rough spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "It would make us all breathe easier if\x01",
            "you bracers came to check in on us every\x01",
            "now and then!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "I know you're busy, but do drop by\x01",
            "every now and again, won't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x106,
        (
            "#051FYeah, don't worry.\x02\x03",

            "If we're ever in the area,\x01",
            "we'll stop in.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2092)
    OP_A2(0x2)
    Jump("loc_11EB")

    label("loc_E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F47")

    ChrTalk(    #43
        0x9,
        (
            "It would make everyone breathe easier if\x01",
            "you bracers came to check in on us every\x01",
            "now and then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x9,
        (
            "I know you're busy, but do drop by\x01",
            "every now and again, won't you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11EB")

    label("loc_F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1103")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1079")

    ChrTalk(    #45
        0x9,
        (
            "The children are helping, so we're\x01",
            "managing to keep things going, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "We still don't know what caused the\x01",
            "orbments to stop at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x9,
        (
            "It'd be nice if the Royal Army could\x01",
            "make some kind of announcement...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "With us being so near Erebonia,\x01",
            "it's really got me worried.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1100")

    label("loc_1079")


    ChrTalk(    #49
        0x9,
        (
            "We still don't know what caused the\x01",
            "orbments to stop at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "And with us being so near Erebonia,\x01",
            "it's really got me worried.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1100")

    Jump("loc_11EB")

    label("loc_1103")


    ChrTalk(    #51
        0x9,
        "Oh, hello, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "Did you come by to keep an eye\x01",
            "on things here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "The village is quiet for now, but who knows\x01",
            "what might happen?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "I know you're busy, but do stop by to check\x01",
            "on us every now and again, all right?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11EB")

    Jump("loc_17FE")

    label("loc_11EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_131E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1261")

    ChrTalk(    #55
        0x9,
        (
            "I hear Elder Reisen took donations\x01",
            "of some kind for the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        "Encouraging, isn't it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_131B")

    label("loc_1261")


    ChrTalk(    #57
        0x9,
        "Welcooooome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x9,
        (
            "I hear Elder Reisen took donations\x01",
            "of some kind for the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "Maybe we really will be able to restore\x01",
            "the orchards now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        "Yeah, we're gonna be okay!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_131B")

    Jump("loc_17FE")

    label("loc_131E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1530")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 1)), scpexpr(EXPR_END)), "loc_13AC")

    ChrTalk(    #61
        0x9,
        (
            "You were out cold until just a bit ago,\x01",
            "and now you're already back at work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        "Being a bracer seems like tough work!\x02",
    )

    CloseMessageWindow()
    Jump("loc_152D")

    label("loc_13AC")

    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x9, 0x106, 0)
    Sleep(400)

    ChrTalk(    #63
        0x9,
        "Hello, Agate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x9,
        "Already back at work?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x106,
        "#050FYeah, things are kinda busy right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "Being a bracer really is a full-time job,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        (
            "Well, once you're done for the day,\x01",
            "come over and have a drink.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        "I'll treat you to one of our best ciders.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x106,
        (
            "#053FOh, yeah?\x02\x03",

            "#051FI'll hold you to that, Limon.\x01",
            "Lookin' forward to it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A49)

    label("loc_152D")

    Jump("loc_17FE")

    label("loc_1530")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_166B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_15A9")

    ChrTalk(    #70
        0x9,
        (
            "I heard Agate was injured and had to\x01",
            "be carried back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        "I should go check in on him later.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1668")

    label("loc_15A9")


    ChrTalk(    #72
        0x9,
        (
            "I heard Agate was injured and had to\x01",
            "be carried back home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "And I thought I saw a little girl coming\x01",
            "out of his house a bit ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        (
            "Who...is that?\x01",
            "She almost reminds me of...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1668")

    Jump("loc_17FE")

    label("loc_166B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_17FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16FB")

    ChrTalk(    #75
        0x9,
        (
            "The symbol of the village, and everyone's\x01",
            "pride, ruined in an instant.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "I'm so frustrated and angry I can't\x01",
            "even cry!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FE")

    label("loc_16FB")


    ChrTalk(    #77
        0x9,
        (
            "Everyone in the village put something\x01",
            "of themselves into that orchard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        (
            "We took care of it through the rain,\x01",
            "the wind, and yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "It was all torn down and burned to ashes\x01",
            "in a single moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        (
            "I'm so frustrated and angry I can't\x01",
            "even cry!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_17FE")

    TalkEnd(0x9)
    Return()

    # Function_6_C2A end

    def Function_7_1802(): pass

    label("Function_7_1802")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 0)), scpexpr(EXPR_END)), "loc_1AAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1930")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_187C")

    ChrTalk(    #81
        0xFE,
        "Everybody was up late talking.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "I guess they're really busy with the\x01",
            "orchard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_192D")

    label("loc_187C")


    ChrTalk(    #83
        0xFE,
        "Agate, Miss Bracer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "Did you catch the dragon yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x106,
        "#050FNo, we're gonna go deal with it now.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #86
        0xFE,
        "Oh, o-okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "Good luck! I'll be rooting for you!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_192D")

    Jump("loc_1A60")

    label("loc_1930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_1A11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_199C")

    ChrTalk(    #88
        0xFE,
        "I'm being good, just like Dad asked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "They're all still cleaning\x01",
            "up the orchards.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0E")

    label("loc_199C")


    ChrTalk(    #90
        0xFE,
        "Miss Bracer...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "I'm being good, just like Dad asked.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "They're all still cleaning\x01",
            "up the orchards.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1A0E")

    Jump("loc_1A60")

    label("loc_1A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1A60")

    ChrTalk(    #93
        0xFE,
        "You be careful too, miss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "The dragon's really big, after all.\x02",
    )

    CloseMessageWindow()

    label("loc_1A60")

    Jump("loc_1AAB")

    label("loc_1A63")


    ChrTalk(    #95
        0xFE,
        "You be careful too, miss!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        "The dragon's really big, after all.\x02",
    )

    CloseMessageWindow()

    label("loc_1AAB")

    Jump("loc_1DF6")

    label("loc_1AAE")

    OP_62(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)

    ChrTalk(    #97
        0xFE,
        "Oh, Miss Bracer...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1B51")
    TurnDirection(0xFE, 0x106, 400)
    Sleep(400)

    ChrTalk(    #98
        0xFE,
        "And Agate?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x101,
        "#1000FHeeey, Lewey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x106,
        (
            "#051F'Sup, squirt?\x01",
            "You doin' all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B97")

    label("loc_1B51")


    ChrTalk(    #101
        0x101,
        (
            "#1000FHeeey, Lewey.\x02\x03",

            "#1007FThank Aidios... I'm glad you're safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B97")


    ChrTalk(    #102
        0xFE,
        "Y-Yeah, I'm fine.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        "But, but...the orchards...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1016FAww, you tear up so easily...\x02\x03",

            "#1006FDon't worry, it's okay!\x02\x03",

            "We're all together, and we won't let\x01",
            "the dragon do anything else bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        "R-Really...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1D01")

    ChrTalk(    #106
        0x101,
        "#1006FReally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x106,
        "#051FYeah, we promise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        (
            "#1000FSo just listen to your dad and be\x01",
            "a good boy, okay? Just for a little\x01",
            "longer!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDB")

    label("loc_1D01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_1D73")

    ChrTalk(    #109
        0x101,
        (
            "#1012FReally.\x02\x03",

            "#1000FSo just listen to your dad and be\x01",
            "a good boy, okay? Just for a little\x01",
            "longer!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DDB")

    label("loc_1D73")


    ChrTalk(    #110
        0x101,
        (
            "#1012FReally.\x02\x03",

            "#1000FSo just listen to your dad and be\x01",
            "a good boy, okay? Just for a little\x01",
            "longer!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDB")


    ChrTalk(    #111
        0xFE,
        "Okay... I will!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A48)
    OP_A2(0x3)

    label("loc_1DF6")

    TalkEnd(0xA)
    Return()

    # Function_7_1802 end

    def Function_8_1DFA(): pass

    label("Function_8_1DFA")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1E72")

    ChrTalk(    #112
        0xFE,
        "I wonder if Pesca and Gray made up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "They're grown-ups, so they oughtta be\x01",
            "able to work together!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20AC")

    label("loc_1E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_1F25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1EB8")

    ChrTalk(    #114
        0xFE,
        "I still can't go outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        "I'm booooored...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F22")

    label("loc_1EB8")


    ChrTalk(    #116
        0xFE,
        "I still can't go outside.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        "I'm booooored...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Maybe Miss Limon will make a dessert\x01",
            "for me!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1F22")

    Jump("loc_20AC")

    label("loc_1F25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_20AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1FA1")

    ChrTalk(    #119
        0xFE,
        "Are dragons really that scary?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "In the stories, they're all nice and good\x01",
            "and help the Goddess...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20AC")

    label("loc_1FA1")


    ChrTalk(    #121
        0xFE,
        (
            "But everyone's saying I can't go outside\x01",
            "because of the mean dragon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "Are dragons really that scary?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "In the stories, they're all nice and good\x01",
            "and help the Goddess...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "I guess dragons have different\x01",
            "personalities, just like Lewey\x01",
            "and Vince, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_20AC")

    TalkEnd(0xB)
    Return()

    # Function_8_1DFA end

    def Function_9_20B0(): pass

    label("Function_9_20B0")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2263")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D0")

    ChrTalk(    #125
        0xFE,
        (
            "I heard Emile complaining.\x01",
            "Apparently this orbment thing has shut\x01",
            "down all distribution too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "Without any way to ship, we can't even\x01",
            "export what fruit we have, and we'll run\x01",
            "out of everyday stuff real quick out here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "This, uh, might be pretty bad...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_2260")

    label("loc_21D0")


    ChrTalk(    #128
        0xFE,
        (
            "Having the ENTIRE national distribution\x01",
            "network shut down is a pretty big\x01",
            "problem!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "This might not be the time to sit here\x01",
            "drinking...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2260")

    Jump("loc_23DC")

    label("loc_2263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_23DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2351")

    ChrTalk(    #130
        0xFE,
        (
            "With the saplings planted, we can finally\x01",
            "take a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "Even if orbments have stopped working,\x01",
            "life here won't be all that hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "We can cook with old-style ovens,\x01",
            "and we've got lamps aplenty for light.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_23DC")

    label("loc_2351")


    ChrTalk(    #133
        0xFE,
        (
            "Even if orbments have stopped working,\x01",
            "life here won't be all that hard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "One of the upshots of being part of\x01",
            "a village, I guess!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23DC")

    TalkEnd(0xC)
    Return()

    # Function_9_20B0 end

    def Function_10_23E0(): pass

    label("Function_10_23E0")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_2636")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257A")

    ChrTalk(    #135
        0xFE,
        (
            "The cargo flights have stopped, huh?\x01",
            "Sounds like things are a mess in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "But if airships aren't working, that\x01",
            "means the Air Force ain't patrolling,\x01",
            "either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "Ain't too comforting for those of us\x01",
            "who live on the border with the blood-\x01",
            "thirsty, conquest-happy Empire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "I don't want to be too loud about it,\x01",
            "but I'm really worried about what\x01",
            "the Erebonians might do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_2633")

    label("loc_257A")


    ChrTalk(    #139
        0xFE,
        (
            "To those of us on the Imperial border,\x01",
            "losing the Air Force is a huge blow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "I don't want to be too loud about it,\x01",
            "but I'm really worried about what\x01",
            "the Erebonians might do.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2633")

    Jump("loc_28A8")

    label("loc_2636")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_28A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2830")

    ChrTalk(    #141
        0xFE,
        (
            "The saplings are planted, and we can\x01",
            "finally, finally rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "I thought we could rest...but then\x01",
            "the latest craziness happened!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "I wonder how Lore's family is doing.\x01",
            "They run a store in the Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "If I recall rightly, it's a hardware\x01",
            "store he runs with his wife.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "With the orbments out, the Air Force,\x01",
            "the pride of the Liberlian army, is now\x01",
            "one big joke.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "I don't want to be too loud about it,\x01",
            "but I'm really worried about what\x01",
            "the Erebonians might do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_28A8")

    label("loc_2830")


    ChrTalk(    #147
        0xFE,
        "I bet things are hard in Bose, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "I wonder how Lore's family is doing.\x01",
            "They run a store in the Bose Market.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A8")

    TalkEnd(0xD)
    Return()

    # Function_10_23E0 end

    SaveToFile()

Try(main)
