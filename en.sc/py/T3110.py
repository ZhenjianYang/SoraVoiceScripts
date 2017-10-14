from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3110   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3110.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
        'Louise',                               # 9
        'Yuriel',                               # 10
        'Rutherford',                           # 11
        'Sotiria',                              # 12
        'Stain',                                # 13
        'Elise',                                # 14
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
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH01070 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01030 ._CH',             # 03
        'ED6_DT07/CH01200 ._CH',             # 04
        'ED6_DT07/CH01130 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH01070P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01030P._CP',             # 03
        'ED6_DT07/CH01200P._CP',             # 04
        'ED6_DT07/CH01130P._CP',             # 05
    )

    DeclNpc(
        X                   = -190,
        Z                   = 0,
        Y                   = 23730,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -1840,
        Z                   = 4000,
        Y                   = 23380,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 24940,
        Z                   = 0,
        Y                   = 530,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -4040,
        Z                   = 0,
        Y                   = 3790,
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
        X                   = 48200,
        Z                   = 0,
        Y                   = 23060,
        Direction           = 135,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 27890,
        Z                   = 0,
        Y                   = 22500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_219",          # 01, 1
        "Function_2_21A",          # 02, 2
        "Function_3_397",          # 03, 3
        "Function_4_3BB",          # 04, 4
        "Function_5_3DF",          # 05, 5
        "Function_6_4EA",          # 06, 6
        "Function_7_FDC",          # 07, 7
        "Function_8_1497",         # 08, 8
        "Function_9_1FD3",         # 09, 9
        "Function_10_2645",        # 0A, 10
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1B3")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_218")

    label("loc_1B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1C2")
    SetChrFlags(0xA, 0x80)
    Jump("loc_218")

    label("loc_1C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1DD")
    SetChrPos(0x9, 940, 0, 23830, 319)
    Jump("loc_218")

    label("loc_1DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_1F8")
    SetChrPos(0x9, 940, 0, 23830, 319)
    Jump("loc_218")

    label("loc_1F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_202")
    Jump("loc_218")

    label("loc_202")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_218")
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x10)

    label("loc_218")

    Return()

    # Function_0_19A end

    def Function_1_219(): pass

    label("Function_1_219")

    Return()

    # Function_1_219 end

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

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BA")
    OP_8D(0xFE, 25620, 1830, 23470, -690, 1000)
    Jump("Function_3_397")

    label("loc_3BA")

    Return()

    # Function_3_397 end

    def Function_4_3BB(): pass

    label("Function_4_3BB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DE")
    OP_8D(0xFE, 48200, 23060, 51000, 22330, 1000)
    Jump("Function_4_3BB")

    label("loc_3DE")

    Return()

    # Function_4_3BB end

    def Function_5_3DF(): pass

    label("Function_5_3DF")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_4E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_463")

    ChrTalk(    #0
        0xFE,
        (
            "It was just a small quake, so the\x01",
            "central factory's probably fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Oh, no! I'd better go in for work.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4E6")

    label("loc_463")


    ChrTalk(    #2
        0xFE,
        (
            "Ohhh, it's been a while since an\x01",
            "earthquake hit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "At first I thought maybe Professor\x01",
            "Russell had done something again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4E6")

    TalkEnd(0x8)
    Return()

    # Function_5_3DF end

    def Function_6_4EA(): pass

    label("Function_6_4EA")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_68F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E9")

    ChrTalk(    #4
        0xFE,
        (
            "Everyone's having trouble since the\x01",
            "orbments stopped.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Not me and my sister, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "We don't use orbments all that\x01",
            "much in the kitchen, so we're fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Really, the only person who does \x01",
            "is my sister's boyfriend.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_68C")

    label("loc_5E9")


    ChrTalk(    #8
        0xFE,
        (
            "Ursus should be coming by\x01",
            "pretty soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "He always pops over to deliver\x01",
            "lunch when my sister's busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Sometimes he does the cleaning\x01",
            "while he's at it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68C")

    Jump("loc_FD8")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_ADE")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x417, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_830")
    OP_62(0xFE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #11
        0xFE,
        "Oh, Tita! It's been a while.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "Are you helping out the Professor today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x107,
        (
            "#560FYeah, pretty much.\x02\x03",

            "How about you, Yuriel? Are you\x01",
            "house-sitting again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Yep, that's right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "My sister's working like crazy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Guess she must've been really happy\x01",
            "to get on board the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "She's like a kid in a candy store!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x107,
        "#067FAh...haha...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20BB)
    Jump("loc_8DD")

    label("loc_830")


    ChrTalk(    #19
        0xFE,
        (
            "My sister's really smart, but she still\x01",
            "acts like a kid in a lot of ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        "I mean, her place is always a disaster.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "You're way more grown up than she is,\x01",
            "Tita.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DD")

    Jump("loc_ADB")

    label("loc_8E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A03")

    ChrTalk(    #22
        0xFE,
        (
            "My sister, Louise, has been working\x01",
            "like mad lately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Guess she must've been really happy\x01",
            "to get on board the Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "She left really early this morning,\x01",
            "saying she was gonna study the\x01",
            "abnormality some more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "She's got all the energy of a little kid,\x01",
            "haha.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_ADB")

    label("loc_A03")


    ChrTalk(    #26
        0xFE,
        (
            "My sister is pretty smart, but she still\x01",
            "acts like a kid in a lot of ways.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "Instead of trying to find an answer to the\x01",
            "weirdness going on, I wish she'd just focus\x01",
            "on why our house is always such a disaster!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ADB")

    Jump("loc_FD8")

    label("loc_ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_C57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B67")

    ChrTalk(    #28
        0xFE,
        "Ahh, isn't my sister gonna get married soon?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "I think that's the only way this room\x01",
            "is ever gonna get cleaned.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C54")

    label("loc_B67")


    ChrTalk(    #30
        0xFE,
        (
            "My sister went off to Leiston Fortress\x01",
            "for work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "In other words, this is my chance.\x01",
            "If I clean it now, it might stay clean\x01",
            "for at least a few hours!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Yeah, now I'm motivated. I'm gonna\x01",
            "do my best to clean this place up!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_C54")

    Jump("loc_FD8")

    label("loc_C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_CCC")

    ChrTalk(    #33
        0xFE,
        (
            "My sister went off to Leiston Fortress\x01",
            "for work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "*sigh* I wish she'd cleaned up before she left.\x02",
    )

    CloseMessageWindow()
    Jump("loc_FD8")

    label("loc_CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_E61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 3)), scpexpr(EXPR_END)), "loc_D4C")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #35
        0xFE,
        "Helping the Professor sounds reeeally hard.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I bet my sister could never do it.\x01",
            "I'm 120% sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5E")

    label("loc_D4C")

    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #37
        0xFE,
        "Ah, Tita. Are you helping Russell today?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x107,
        (
            "#060FYeah, pretty much.\x02\x03",

            "I'm setting up some newly developed\x01",
            "measuring equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "I see. Sounds important!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "And you're the only one who\x01",
            "can keep up with the Professor,\x01",
            "so I guess there's no stopping you!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1433)

    label("loc_E5E")

    Jump("loc_FD8")

    label("loc_E61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_EE4")

    ChrTalk(    #41
        0xFE,
        (
            "I think I'll leave the books like\x01",
            "this until Louise comes back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "I'm gonna make her clean it up\x01",
            "no matter what!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD8")

    label("loc_EE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_FD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F52")

    ChrTalk(    #43
        0xFE,
        "Uuugh, my sister is such a slob.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I bet her boyfriend'll give up on her\x01",
            "eventually.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD8")

    label("loc_F52")


    ChrTalk(    #45
        0xFE,
        (
            "Awww, all these books fell\x01",
            "down in that earthquake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "It's all 'cause my sister didn't\x01",
            "put them away like she should've...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_FD8")

    TalkEnd(0x9)
    Return()

    # Function_6_4EA end

    def Function_7_FDC(): pass

    label("Function_7_FDC")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1183")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_10BF")

    ChrTalk(    #47
        0xFE,
        (
            "I've got another business deal to discuss\x01",
            "in the capital with representatives from\x01",
            "the Republic. It's very exciting!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "If exports keep increasing like this,\x01",
            "the airship business has a bright future.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1180")

    label("loc_10BF")


    ChrTalk(    #49
        0xFE,
        (
            "Lately, there've been a lot of\x01",
            "deals involving airships.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "Sales are going great, but the downside\x01",
            "to that is, I'm absurdly busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "I feel like screaming with joy\x01",
            "and exhaustion!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1180")

    Jump("loc_1493")

    label("loc_1183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1334")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_125B")

    ChrTalk(    #52
        0xFE,
        (
            "When I get some time between work, I want\x01",
            "to go and say hello to everyone at the\x01",
            "central factory. Hello and...maybe 'sorry.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "I assume my daughter is causing\x01",
            "everyone all manner of trouble.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1331")

    label("loc_125B")


    ChrTalk(    #54
        0xFE,
        (
            "I didn't think I'd see the day my daughter\x01",
            "would go to work at the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Her motives for joining are suspicious, but\x01",
            "right now, I just want to see her work hard\x01",
            "and make a name for herself.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1331")

    Jump("loc_1493")

    label("loc_1334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_1493")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_13DA")

    ChrTalk(    #56
        0xFE,
        (
            "Oops. Got a bit worked up and let out a\x01",
            "little scream there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "As someone affiliated with the airship\x01",
            "business, that's...a bit embarrassing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1493")

    label("loc_13DA")


    ChrTalk(    #58
        0xFE,
        "Ahh, that was a surprise at the port.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "I got a bit worked up and let out a\x01",
            "little scream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "As someone affiliated with the airship\x01",
            "business, that's...a bit embarrassing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1493")

    TalkEnd(0xA)
    Return()

    # Function_7_FDC end

    def Function_8_1497(): pass

    label("Function_8_1497")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_1680")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A4")

    ChrTalk(    #61
        0xFE,
        (
            "Everyone at the central factory is really\x01",
            "busy preparing to resume their research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "It'll be good practice for my daughter Muriel,\x01",
            "who's an apprentice over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "That girl has a bad habit of underestimating\x01",
            "what it means to work.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_167D")

    label("loc_15A4")


    ChrTalk(    #64
        0xFE,
        (
            "Everyone at the central factory is really\x01",
            "busy preparing to resume their research.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "It'll be good practice for my daughter Muriel.\x01",
            "At the moment, she has a bad habit of\x01",
            "underestimating what it means to work.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_167D")

    Jump("loc_1FCF")

    label("loc_1680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1881")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_178D")

    ChrTalk(    #66
        0xFE,
        (
            "The city was a mess right after\x01",
            "the orbments stopped working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "Everyone pushed into the central factory,\x01",
            "and it was very hard on the Factory Chief.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "The same thing had happened before, so everyone\x01",
            "assumed he was responsible this time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_187E")

    label("loc_178D")


    ChrTalk(    #69
        0xFE,
        (
            "Of course, you know what they say about assuming!\x01",
            "Still, there's a good reason for such assumptions.\x01",
            "Some things, you just don't live down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "Weird things happening in experiments\x01",
            "isn't just a one- or two-time\x01",
            "occurrence, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_187E")

    Jump("loc_1FCF")

    label("loc_1881")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_1A3E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1923")

    ChrTalk(    #71
        0xFE,
        (
            "Hooray! I managed to see my husband\x01",
            "and daughter off to work again without any\x01",
            "problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "Now I can relax until Grandfather comes back.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A3B")

    label("loc_1923")


    ChrTalk(    #73
        0xFE,
        (
            "Hooray! I managed to see my husband\x01",
            "and daughter off to work again without any\x01",
            "problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "Now I can relax until Grandfather comes back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "My grandfather's been at the bar since noon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "He's so strange. The man doesn't even\x01",
            "drink, but he likes to hang out there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1A3B")

    Jump("loc_1FCF")

    label("loc_1A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_1BB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1B0B")

    ChrTalk(    #77
        0xFE,
        (
            "According to my husband, the number of\x01",
            "deals we've been getting from the Empire\x01",
            "has been on the rise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "I wonder if this means we'll be able to\x01",
            "break the ice with the Empire soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB1")

    label("loc_1B0B")


    ChrTalk(    #79
        0xFE,
        (
            "My husband works as an intermediary\x01",
            "in airship sales.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "And lately he's been out a lot.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "He just came back from Bose,\x01",
            "but now he's off to the capital.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1BB1")

    Jump("loc_1FCF")

    label("loc_1BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_1D35")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1C31")

    ChrTalk(    #82
        0xFE,
        (
            "Getting that girl to work hard...\x01",
            "Kind of a shock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Has someone finally lit a fire\x01",
            "under her butt?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D32")

    label("loc_1C31")

    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #84
        0xFE,
        "Oh, Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "How about it? Is my daughter really working?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x107,
        (
            "#560FAh, yeah. It seems like Muriel's working\x01",
            "pretty hard, in fact.\x02\x03",

            "She's always running around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        "Huh, that's a surprise.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "I thought she'd be the laziest worker\x01",
            "there!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1D32")

    Jump("loc_1FCF")

    label("loc_1D35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1EB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1DE8")

    ChrTalk(    #89
        0xFE,
        (
            "Lately, my daughter Muriel's been\x01",
            "helping out at the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "Her questionable motives aside, it's good\x01",
            "that she's interested in work. Finally.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB4")

    label("loc_1DE8")


    ChrTalk(    #91
        0xFE,
        (
            "Lately, my daughter Muriel's been\x01",
            "helping at the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "She wants to be the receptionist.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "It'll be a good chance for her to learn\x01",
            "what the real world is like, if nothing\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1EB4")

    Jump("loc_1FCF")

    label("loc_1EB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_1FCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1F33")

    ChrTalk(    #94
        0xFE,
        "Still, earthquakes...? How peculiar.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "I'd all but forgotten such a thing\x01",
            "existed until a bit ago.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FCF")

    label("loc_1F33")


    ChrTalk(    #96
        0xFE,
        "I hate earthquakes!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "I hate it when the floor under my\x01",
            "feet shakes. It's terrifying!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "Naturally, I don't ride airships for\x01",
            "the same reason.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_1FCF")

    TalkEnd(0xB)
    Return()

    # Function_8_1497 end

    def Function_9_1FD3(): pass

    label("Function_9_1FD3")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2146")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_209A")

    ChrTalk(    #99
        0xFE,
        (
            "Everyone's busy talking about the\x01",
            "earthquakes, but the non-aggression\x01",
            "pact is way more important.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "After all, it's a problem with the\x01",
            "future of the kingdom riding on it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2143")

    label("loc_209A")


    ChrTalk(    #101
        0xFE,
        (
            "Hmm... The signing ceremony for the\x01",
            "non-aggression pact is coming up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        "It's been ten years since that war...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "I hope it's signed without any\x01",
            "resistance.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2143")

    Jump("loc_2641")

    label("loc_2146")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2321")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2220")

    ChrTalk(    #104
        0xFE,
        (
            "The store manager at our place, Jorg,\x01",
            "has been obsessed with this new model\x01",
            "gun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "Looking at its craftsmanship,\x01",
            "I can easily see why.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "It'd be best to get a skilled gunner\x01",
            "to test it out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231E")

    label("loc_2220")


    ChrTalk(    #107
        0xFE,
        (
            "The other day, Karl over at the\x01",
            "central factory showed me the\x01",
            "new model orbal gun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "The detail work is still rough, but\x01",
            "the driver portion's downright\x01",
            "revolutionary.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "If they can get it to the testing phase,\x01",
            "that gun'll probably be huge.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_231E")

    Jump("loc_2641")

    label("loc_2321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_251F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_23F6")

    ChrTalk(    #110
        0xFE,
        (
            "We don't get the latest weapons\x01",
            "at the weapon shop I run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "I've argued a lot over our stock\x01",
            "with the younger staff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "And to their credit, they understand!\x01",
            "They finally agree with me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_251C")

    label("loc_23F6")


    ChrTalk(    #113
        0xFE,
        (
            "We don't get the latest weapons\x01",
            "at the weapon shop I run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "New models, to them, means stuff that hasn't\x01",
            "been vetted as much as older stock. You can't\x01",
            "really trust it to be reliable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "There are all kinds of problems you\x01",
            "only really learn about after using\x01",
            "something extensively.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_251C")

    Jump("loc_2641")

    label("loc_251F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_END)), "loc_2641")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_25AC")

    ChrTalk(    #116
        0xFE,
        "I run a weapon shop in Zeiss.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "It's across the street from the Bracer Guild,\x01",
            "so stop on by if you have the chance.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2641")

    label("loc_25AC")


    ChrTalk(    #118
        0xFE,
        (
            "There don't seem to be any aftershocks,\x01",
            "so my store should be okay...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "Still, earthquakes are rare.\x01",
            "You don't feel those much in Liberl.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2641")

    TalkEnd(0xC)
    Return()

    # Function_9_1FD3 end

    def Function_10_2645(): pass

    label("Function_10_2645")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2788")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2718")

    ChrTalk(    #120
        0xFE,
        (
            "Since we can't use the stove,\x01",
            "I bought some fuel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        "Bell Station really does have everything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "It's reassuring having a store\x01",
            "with a good selection nearby at\x01",
            "times like this.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_2785")

    label("loc_2718")


    ChrTalk(    #123
        0xFE,
        (
            "Since we can't use the stove,\x01",
            "I bought some fuel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "It's not a strong fire,\x01",
            "but at least I can cook.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2785")

    Jump("loc_289B")

    label("loc_2788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_289B")

    ChrTalk(    #125
        0xFE,
        (
            "If you're looking for my husband,\x01",
            "he took Vince and went off to the\x01",
            "central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "They said they were going to have\x01",
            "a look at that mysterious floating\x01",
            "object from the roof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "Don't know why they want a closer look\x01",
            "at something so horrifying, though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_289B")

    TalkEnd(0xFE)
    Return()

    # Function_10_2645 end

    SaveToFile()

Try(main)
