from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4400   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        'Larry',                                # 9
        'Tourist',                              # 10
        'Tourist',                              # 11
        'Tourist',                              # 12
        'Dockworker',                           # 13
        'Dockworker',                           # 14
        'Dockworker',                           # 15
        'Worker',                               # 16
        'Worker',                               # 17
        'Dockworker',                           # 18
        'Grancel - West Block',                 # 19
        'Grancel - N Warehouse District',       # 20
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
        'ED6_DT07/CH01500 ._CH',             # 00
        'ED6_DT07/CH01050 ._CH',             # 01
        'ED6_DT07/CH01070 ._CH',             # 02
        'ED6_DT07/CH01060 ._CH',             # 03
        'ED6_DT07/CH01530 ._CH',             # 04
        'ED6_DT07/CH01460 ._CH',             # 05
        'ED6_DT06/CH20159 ._CH',             # 06
        'ED6_DT07/CH01450 ._CH',             # 07
        'ED6_DT07/CH01550 ._CH',             # 08
        'ED6_DT07/CH01500 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH01500P._CP',             # 00
        'ED6_DT07/CH01050P._CP',             # 01
        'ED6_DT07/CH01070P._CP',             # 02
        'ED6_DT07/CH01060P._CP',             # 03
        'ED6_DT07/CH01530P._CP',             # 04
        'ED6_DT07/CH01460P._CP',             # 05
        'ED6_DT06/CH20159P._CP',             # 06
        'ED6_DT07/CH01450P._CP',             # 07
        'ED6_DT07/CH01550P._CP',             # 08
        'ED6_DT07/CH01500P._CP',             # 09
    )

    DeclNpc(
        X                   = -8750,
        Z                   = 0,
        Y                   = -3530,
        Direction           = 268,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 22130,
        Z                   = 0,
        Y                   = -5230,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 24260,
        Z                   = 0,
        Y                   = -5500,
        Direction           = 180,
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
        X                   = 23230,
        Z                   = 0,
        Y                   = -5500,
        Direction           = 180,
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
        X                   = 13390,
        Z                   = 0,
        Y                   = 2850,
        Direction           = 90,
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
        X                   = 14890,
        Z                   = 0,
        Y                   = 2850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -22680,
        Z                   = 0,
        Y                   = -15490,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -18690,
        Z                   = 0,
        Y                   = 6110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -17670,
        Z                   = 0,
        Y                   = 7510,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -15960,
        Z                   = 0,
        Y                   = 25420,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 60310,
        Z                   = 0,
        Y                   = -1230,
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
        X                   = -9950,
        Z                   = 0,
        Y                   = 71270,
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
        "Function_0_27A",          # 00, 0
        "Function_1_2BD",          # 01, 1
        "Function_2_322",          # 02, 2
        "Function_3_49F",          # 03, 3
        "Function_4_4C8",          # 04, 4
        "Function_5_E95",          # 05, 5
        "Function_6_102E",         # 06, 6
        "Function_7_1151",         # 07, 7
        "Function_8_1272",         # 08, 8
        "Function_9_1469",         # 09, 9
        "Function_10_15F5",        # 0A, 10
        "Function_11_18E8",        # 0B, 11
        "Function_12_1B46",        # 0C, 12
        "Function_13_1C93",        # 0D, 13
        "Function_14_1EDB",        # 0E, 14
    )


    def Function_0_27A(): pass

    label("Function_0_27A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2AD")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x10, -14520, 0, -5650, 262)

    label("loc_2AD")

    Jump("loc_2BC")

    label("loc_2B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2BC")
    SetChrFlags(0x10, 0x10)

    label("loc_2BC")

    Return()

    # Function_0_27A end

    def Function_1_2BD(): pass

    label("Function_1_2BD")

    OP_16(0x2, 0xFA0, 0xFFFE3AE0, 0xFFFE69C0, 0x23006D)
    OP_22(0x1C5, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F4")
    OP_B1("t4400_y")
    Jump("loc_2FD")

    label("loc_2F4")

    OP_B1("t4400_n")

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_317")
    OP_72(0xC, 0x4)

    label("loc_317")

    OP_71(0xB, 0x4)
    OP_1C(0x3, 0x0, 0xE)
    Return()

    # Function_1_2BD end

    def Function_2_322(): pass

    label("Function_2_322")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_347")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_489")

    label("loc_347")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_360")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_489")

    label("loc_360")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_379")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_489")

    label("loc_379")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_392")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_489")

    label("loc_392")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_489")

    label("loc_3AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C4")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_489")

    label("loc_3C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DD")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_489")

    label("loc_3DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F6")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_489")

    label("loc_3F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_489")

    label("loc_40F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_428")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_489")

    label("loc_428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_441")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_489")

    label("loc_441")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_489")

    label("loc_45A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_473")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_489")

    label("loc_473")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_489")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_489")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49E")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_489")

    label("loc_49E")

    Return()

    # Function_2_322 end

    def Function_3_49F(): pass

    label("Function_3_49F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4C7")
    OP_8D(0xFE, -8750, -2900, -6330, -5850, 1500)
    Sleep(2000)
    Jump("Function_3_49F")

    label("loc_4C7")

    Return()

    # Function_3_49F end

    def Function_4_4C8(): pass

    label("Function_4_4C8")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_614")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_611")

    ChrTalk(    #0
        0xFE,
        (
            "If the haulage vehicles aren't\x01",
            "gonna work, then freight transport's\x01",
            "gonna have to be done by hand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "B-But there's no freight to carry\x01",
            "coming in anymore...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Guess this isn't the time to\x01",
            "be saying I'm lucky that I get\x01",
            "to slack off on the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Wh-What's gonna happen to\x01",
            "my paycheck? My FOOD?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_611")

    Jump("loc_E91")

    label("loc_614")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_7EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_670")

    ChrTalk(    #4
        0xFE,
        (
            "*pheeew* Boy, am I glad I\x01",
            "wasn't on night shift that day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7EC")

    label("loc_670")


    ChrTalk(    #5
        0xFE,
        (
            "The office was attacked, and both\x01",
            "Phelio and Duncan got mixed up\x01",
            "in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "What'd they ever do to deserve\x01",
            "getting mixed up in a mess like\x01",
            "that? Isn't it just terrible?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "I-I'm glad I wasn't there in the\x01",
            "office that day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "D-Doesn't stop the situation from\x01",
            "being any less terrible, of course!\x01",
            "But I am grateful for that. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Y-You, uh, know what I mean,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_7EC")

    Jump("loc_E91")

    label("loc_7EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_9CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_877")

    ChrTalk(    #10
        0xFE,
        (
            "I-I'm just a powerless worker\x01",
            "who does his job and eats his\x01",
            "food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "But, I still live pretty happily,\x01",
            "I'd say.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9CB")

    label("loc_877")


    ChrTalk(    #12
        0xFE,
        (
            "You're looking for a girl\x01",
            "in a white dress...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "I-I'm just a helpless guy who\x01",
            "does his job and eats his food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "But, I still live pretty happily,\x01",
            "I'd say.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "Well, I mean, occasionally\x01",
            "I think about how nice it'd be\x01",
            "to go on a date with a girl...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Ah, that's probably not\x01",
            "something I should say\x01",
            "out loud. Like, at all.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9CB")

    Jump("loc_E91")

    label("loc_9CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A8E")

    ChrTalk(    #17
        0xFE,
        (
            "You ever just picture having\x01",
            "yourself a drink on the way\x01",
            "home from a long day of work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I always liked the idea of it.\x01",
            "It seems like such a grown\x01",
            "up thing to do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B8A")

    label("loc_A8E")


    ChrTalk(    #19
        0xFE,
        (
            "I've... I've been workin' real\x01",
            "hard today, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "All right! This is it! This is gonna\x01",
            "be the day I have me an ice-cold\x01",
            "beer on my way home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "...Yeah, right. I can barely\x01",
            "handle alcohol.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I-I'm sorry...\x01",
            "I just wanted to say it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B8A")

    Jump("loc_E91")

    label("loc_B8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_C52")

    ChrTalk(    #23
        0xFE,
        (
            "J-Just between you and me,\x01",
            "I wanted to work at the airship\x01",
            "company.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "But it's impossible!\x01",
            "It's really competitive over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I never stood a chance.\x01",
            "I don't have the guts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E91")

    label("loc_C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_E91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CFD")

    ChrTalk(    #26
        0xFE,
        (
            "I-I thought maybe I'd try to act like\x01",
            "I had tons of experience, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "I couldn't act like that to someone\x01",
            "who's much more experienced in life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E91")

    label("loc_CFD")


    ChrTalk(    #28
        0xFE,
        (
            "I-I've been working here\x01",
            "for two years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "And recently, they assigned me\x01",
            "to oversee a new guy. I've been\x01",
            "all jittery ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "See, this new guy? He's older than\x01",
            "me! And on top of that, he married!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "I-I thought maybe I'd try to act like\x01",
            "I had tons of experience, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "What a joke. As if I could act like\x01",
            "that in front of a guy who's obviously\x01",
            "way more experienced than I am.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_E91")

    TalkEnd(0x8)
    Return()

    # Function_4_4C8 end

    def Function_5_E95(): pass

    label("Function_5_E95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA7")
    Jump("loc_102A")

    label("loc_EA7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_EBD")
    Jump("loc_102A")

    label("loc_EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_EFC")

    ChrTalk(    #33
        0xFE,
        (
            "Ahaha... It's hard to be\x01",
            "bored with these kids.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102A")

    label("loc_EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F47")

    ChrTalk(    #34
        0xFE,
        (
            "Okay, I think we'd better be\x01",
            "getting back to the lodge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102A")

    label("loc_F47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1003")

    ChrTalk(    #35
        0xFE,
        (
            "Watching their faces light up from\x01",
            "something as simple as bringing them\x01",
            "to the harbor is somethin' else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Doesn't hurt that it's so cheap, too!\x01",
            "Did I luck out, or what?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_102A")

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_102A")

    ChrTalk(    #37
        0xFE,
        "Ahhhh, what a lovely lake.\x02",
    )

    CloseMessageWindow()

    label("loc_102A")

    TalkEnd(0xFE)
    Return()

    # Function_5_E95 end

    def Function_6_102E(): pass

    label("Function_6_102E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1040")
    Jump("loc_114D")

    label("loc_1040")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_114D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1056")
    Jump("loc_114D")

    label("loc_1056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1091")

    ChrTalk(    #38
        0xFE,
        (
            "Liiiiiisten!\x01",
            "This isn't a sea, it's a lake!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_114D")

    label("loc_1091")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10BF")

    ChrTalk(    #39
        0xFE,
        "Aww, I'd rather have meat.\x02",
    )

    CloseMessageWindow()
    Jump("loc_114D")

    label("loc_10BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_112E")

    ChrTalk(    #40
        0xFE,
        (
            "I wanna see the gulls more\x01",
            "than the fish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "But I guess gulls don't swing\x01",
            "by lakes, do they?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_114D")

    label("loc_112E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_114D")

    ChrTalk(    #42
        0xFE,
        "I like this place.\x02",
    )

    CloseMessageWindow()

    label("loc_114D")

    TalkEnd(0xFE)
    Return()

    # Function_6_102E end

    def Function_7_1151(): pass

    label("Function_7_1151")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1163")
    Jump("loc_126E")

    label("loc_1163")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1179")
    Jump("loc_126E")

    label("loc_1179")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_11B2")

    ChrTalk(    #43
        0xFE,
        (
            "The～sea～is biiiiiig,\x01",
            "it's hu～uge... ♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126E")

    label("loc_11B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1204")

    ChrTalk(    #44
        0xFE,
        (
            "I wonder what we'll have for\x01",
            "dinner tonight. I want some fish.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_126E")

    label("loc_1204")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1234")

    ChrTalk(    #45
        0xFE,
        "Hey, hey, are there any fishies?\x02",
    )

    CloseMessageWindow()
    Jump("loc_126E")

    label("loc_1234")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_126E")

    ChrTalk(    #46
        0xFE,
        (
            "This is my first time at a port.\x01",
            "I'm excited!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126E")

    TalkEnd(0xFE)
    Return()

    # Function_7_1151 end

    def Function_8_1272(): pass

    label("Function_8_1272")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12BD")

    ChrTalk(    #47
        0xFE,
        (
            "When the heck are the ships\x01",
            "gonna get movin' again?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1465")

    label("loc_12BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1465")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_12D3")
    Jump("loc_1465")

    label("loc_12D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1352")

    ChrTalk(    #48
        0xFE,
        (
            "Sounds like Ruan's finally got\x01",
            "itself a new mayor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "That should get things movin'\x01",
            "again here at the harbor.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1465")

    label("loc_1352")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A6")

    ChrTalk(    #50
        0xFE,
        (
            "Now, work's over. Maybe I'll invite\x01",
            "everyone to go out drinkin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1465")

    label("loc_13A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_13EB")

    ChrTalk(    #51
        0xFE,
        (
            "Well, all I can do is keep my\x01",
            "cool and do what I can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1465")

    label("loc_13EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1465")

    ChrTalk(    #52
        0xFE,
        (
            "It's about time to clean up and\x01",
            "organize the warehouses.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "It's gonna start gettin' real busy\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1465")

    TalkEnd(0xFE)
    Return()

    # Function_8_1272 end

    def Function_9_1469(): pass

    label("Function_9_1469")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_149A")

    ChrTalk(    #54
        0xFE,
        "Man, I am out of shape...\x02",
    )

    CloseMessageWindow()
    Jump("loc_15F1")

    label("loc_149A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_14B0")
    Jump("loc_15F1")

    label("loc_14B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_14F4")

    ChrTalk(    #55
        0xFE,
        (
            "Darn it. I was hopin' Portos\x01",
            "would win the election.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F1")

    label("loc_14F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_155D")

    ChrTalk(    #56
        0xFE,
        (
            "Maybe it's because I've been\x01",
            "so busy lately, but time just feels\x01",
            "like it flies on by.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F1")

    label("loc_155D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_159E")

    ChrTalk(    #57
        0xFE,
        (
            "Which warehouse should\x01",
            "we start with, I wonder...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15F1")

    label("loc_159E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_15F1")

    ChrTalk(    #58
        0xFE,
        (
            "I hate having lots of\x01",
            "free time, but bein' too\x01",
            "busy's no good, either.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15F1")

    TalkEnd(0xFE)
    Return()

    # Function_9_1469 end

    def Function_10_15F5(): pass

    label("Function_10_15F5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A0")

    ChrTalk(    #59
        0xFE,
        (
            "Work sure as hell ain't\x01",
            "happenin'. All I can do\x01",
            "is wait and do some fishin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "How about you? You should wet\x01",
            "your line, too. It'll calm ya down.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E4")

    label("loc_16A0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_16B6")
    Jump("loc_18E4")

    label("loc_16B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1769")

    ChrTalk(    #61
        0xFE,
        (
            "The guy who gave me that rod\x01",
            "came by here a while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "Oddball he may be, but I learned that\x01",
            "he's part of the Fisherman's Guild, so\x01",
            "that's one mystery solved.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E4")

    label("loc_1769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17C2")

    ChrTalk(    #63
        0xFE,
        (
            "This hour of the day is just perfect!\x01",
            "It's the best time for fishin'!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E4")

    label("loc_17C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_180E")

    ChrTalk(    #64
        0xFE,
        (
            "It's pretty nice to be able to do\x01",
            "some fishin' between jobs.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18E4")

    label("loc_180E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_18E4")

    ChrTalk(    #65
        0xFE,
        (
            "So this guy came up to me a bit ago and BAM,\x01",
            "I got a fishin' rod. Dunno why, but if someone wants\x01",
            "to give me free stuff, I ain't sayin' no.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Figured I might as well try fishin'\x01",
            "if I've got it, too.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E4")

    TalkEnd(0xFE)
    Return()

    # Function_10_15F5 end

    def Function_11_18E8(): pass

    label("Function_11_18E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1953")

    ChrTalk(    #67
        0xFE,
        (
            "Geez, with orbments not\x01",
            "working, there's not much of\x01",
            "a job for technicians like us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B42")

    label("loc_1953")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1969")
    Jump("loc_1B42")

    label("loc_1969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1A0C")

    ChrTalk(    #68
        0xFE,
        (
            "Most skills are easy enough\x01",
            "to pick up just by watching,\x01",
            "if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Girls, though? Hah! Haven't\x01",
            "been able to pick them up to\x01",
            "save my life.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B42")

    label("loc_1A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A60")

    ChrTalk(    #70
        0xFE,
        "Ahaha, r-really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "Ah, no, no, gotta be stricter\x01",
            "than that...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B42")

    label("loc_1A60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1AE8")

    ChrTalk(    #72
        0xFE,
        (
            "Heh, you know, it feels nice\x01",
            "getting complimented like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Still, gotta be strict when showing\x01",
            "newbies the ropes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B42")

    label("loc_1AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1B42")

    ChrTalk(    #74
        0xFE,
        (
            "Technology's one of those\x01",
            "things you sorta get better\x01",
            "working with over time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B42")

    TalkEnd(0xFE)
    Return()

    # Function_11_18E8 end

    def Function_12_1B46(): pass

    label("Function_12_1B46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B9E")

    ChrTalk(    #75
        0xFE,
        "Aww, why isn't it working?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "C'mon, be a good boy\x01",
            "and wooork.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8F")

    label("loc_1B9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C8F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1BB4")
    Jump("loc_1C8F")

    label("loc_1BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1BE7")

    ChrTalk(    #77
        0xFE,
        (
            "Oh, sir, what does this\x01",
            "circuit do?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8F")

    label("loc_1BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C29")

    ChrTalk(    #78
        0xFE,
        (
            "Holy crap, that's incredible!\x01",
            "You're so smart!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8F")

    label("loc_1C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1C58")

    ChrTalk(    #79
        0xFE,
        "Your work is just so inspiring!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C8F")

    label("loc_1C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1C8F")

    ChrTalk(    #80
        0xFE,
        (
            "I could never hope to compare\x01",
            "to you, sir!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8F")

    TalkEnd(0xFE)
    Return()

    # Function_12_1B46 end

    def Function_13_1C93(): pass

    label("Function_13_1C93")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D3B")

    ChrTalk(    #81
        0xFE,
        (
            "I come to my job every day,\x01",
            "but with the way things are,\x01",
            "ain't no way work's gettin' done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "I wonder how things are\x01",
            "gonna turn out for us...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED7")

    label("loc_1D3B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1D51")
    Jump("loc_1ED7")

    label("loc_1D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1DB6")

    ChrTalk(    #83
        0xFE,
        "*yaaaawn*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "Damn, that was close!\x01",
            "Can't afford to get injured\x01",
            "at a time like this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED7")

    label("loc_1DB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DFB")

    ChrTalk(    #85
        0xFE,
        (
            "I'm gettin' real hungry.\x01",
            "What should I eat today?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED7")

    label("loc_1DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1E91")

    ChrTalk(    #86
        0xFE,
        (
            "All right, once I'm done with\x01",
            "this, I think I'll take a break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "Our body's our capital, so resting's\x01",
            "an important part of the job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ED7")

    label("loc_1E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1ED7")

    ChrTalk(    #88
        0xFE,
        (
            "This is the management office\x01",
            "for the warehouse district.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ED7")

    TalkEnd(0xFE)
    Return()

    # Function_13_1C93 end

    def Function_14_1EDB(): pass

    label("Function_14_1EDB")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_14_1EDB end

    SaveToFile()

Try(main)
