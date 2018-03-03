from ED63RDScenarioHelper import *

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
        X                   = 60,
        Z                   = 0,
        Y                   = 26440,
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
        X                   = -1760,
        Z                   = 4000,
        Y                   = 23400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 24940,
        Z                   = 0,
        Y                   = 520,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
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
        NpcIndex            = 0x181,
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    ScpFunction(
        "Function_0_17A",          # 00, 0
        "Function_1_1A0",          # 01, 1
        "Function_2_1A1",          # 02, 2
        "Function_3_31E",          # 03, 3
        "Function_4_342",          # 04, 4
        "Function_5_366",          # 05, 5
        "Function_6_426",          # 06, 6
        "Function_7_5C0",          # 07, 7
        "Function_8_7F0",          # 08, 8
        "Function_9_990",          # 09, 9
    )


    def Function_0_17A(): pass

    label("Function_0_17A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19F")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)

    label("loc_19F")

    Return()

    # Function_0_17A end

    def Function_1_1A0(): pass

    label("Function_1_1A0")

    Return()

    # Function_1_1A0 end

    def Function_2_1A1(): pass

    label("Function_2_1A1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C6")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_308")

    label("loc_1C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DF")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_308")

    label("loc_1DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F8")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_308")

    label("loc_1F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_211")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_308")

    label("loc_211")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22A")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_308")

    label("loc_22A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_243")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_308")

    label("loc_243")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25C")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_308")

    label("loc_25C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_275")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_308")

    label("loc_275")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_308")

    label("loc_28E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A7")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_308")

    label("loc_2A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C0")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_308")

    label("loc_2C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D9")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_308")

    label("loc_2D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F2")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_308")

    label("loc_2F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_308")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_308")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31D")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_308")

    label("loc_31D")

    Return()

    # Function_2_1A1 end

    def Function_3_31E(): pass

    label("Function_3_31E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_341")
    OP_8D(0xFE, 25620, 1830, 23470, -690, 1000)
    Jump("Function_3_31E")

    label("loc_341")

    Return()

    # Function_3_31E end

    def Function_4_342(): pass

    label("Function_4_342")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_365")
    OP_8D(0xFE, 48200, 23060, 51000, 22330, 1000)
    Jump("Function_4_342")

    label("loc_365")

    Return()

    # Function_4_342 end

    def Function_5_366(): pass

    label("Function_5_366")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_422")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3DE")

    ChrTalk(    #0
        0xFE,
        "Why did no one wake me up?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Crap... I'm in real trouble now... I need a new\x01",
            "excuse, fast!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_422")

    label("loc_3DE")


    ChrTalk(    #2
        0xFE,
        "What?! Why is it afternoon already?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "I slept in AGAIN!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_422")

    TalkEnd(0xFE)
    Return()

    # Function_5_366 end

    def Function_6_426(): pass

    label("Function_6_426")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_5BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_537")

    ChrTalk(    #4
        0xFE,
        (
            "She's only NOT been late two days this week,\x01",
            "and they were both the days Ursus came to\x01",
            "wake her up. That barely even counts!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I wish she could be more conscious of how \x01",
            "much of a slob she is and not expect others\x01",
            "to cover for her all the time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BC")

    label("loc_537")


    ChrTalk(    #6
        0xFE,
        (
            "*sigh* I should've known my sister wouldn't be \x01",
            "able to get herself up in time on her own...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "She's completely hopeless.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_5BC")

    TalkEnd(0xFE)
    Return()

    # Function_6_426 end

    def Function_7_5C0(): pass

    label("Function_7_5C0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_7EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_706")

    ChrTalk(    #8
        0xFE,
        (
            "I might sell airships, but I'll be honest:\x01",
            "I can't pretend to be an expert on exactly\x01",
            "how they work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "But I can't exactly let that show to my clients,\x01",
            "or they're obviously not going to trust me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Maybe it's time I started crackin' open a few\x01",
            "books and researching the product I'm selling...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EC")

    label("loc_706")


    ChrTalk(    #11
        0xFE,
        (
            "Part of my work involves selling airships to\x01",
            "clients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "But I've been getting asked a lot lately whether\x01",
            "they just fall out of the sky if the flow of orbal\x01",
            "power stops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "I...think they do? At least not immediately.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_7EC")

    TalkEnd(0xFE)
    Return()

    # Function_7_5C0 end

    def Function_8_7F0(): pass

    label("Function_8_7F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_98C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_88C")

    ChrTalk(    #14
        0xFE,
        "My husband's been home quite a lot lately.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Heehee. Actually having someone to cook\x01",
            "for makes it feel so much more worthwhile!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_98C")

    label("loc_88C")


    ChrTalk(    #16
        0xFE,
        (
            "At one point, my husband was always out\x01",
            "of the house for one business discussion\x01",
            "or another...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "...but lately, he's been coming back home\x01",
            "a lot more often.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "Heehee. Actually having someone to cook\x01",
            "for makes it feel so much more worthwhile!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_98C")

    TalkEnd(0xFE)
    Return()

    # Function_8_7F0 end

    def Function_9_990(): pass

    label("Function_9_990")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_B1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_A41")

    ChrTalk(    #19
        0xFE,
        (
            "The final adjustments are probably the hardest \x01",
            "part of things like that, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I was once an engineer myself, so I know that\x01",
            "as well as anyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1F")

    label("loc_A41")


    ChrTalk(    #21
        0xFE,
        (
            "Karl's new model of orbal gun's finally going to\x01",
            "be sold on the mass market, by the sounds of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "He said he was in the middle of making the final\x01",
            "adjustments to it so that can happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "I can hardly wait!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_B1F")

    TalkEnd(0xFE)
    Return()

    # Function_9_990 end

    SaveToFile()

Try(main)
