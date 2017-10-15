from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1210   ._SN',
        MapName             = 'Bose',
        Location            = 'T1210.x',
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
        'Agate',                                # 9
        'Tita',                                 # 10
        'Elder Reisen',                         # 11
        'General Morgan',                       # 12
        'Royal Army Officer',                   # 13
        'Orange',                               # 14
        'Melony',                               # 15
        'Birnette',                             # 16
        'Vince',                                # 17
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
        'ED6_DT26/CH20365 ._CH',             # 00
        'ED6_DT07/CH00060 ._CH',             # 01
        'ED6_DT07/CH01490 ._CH',             # 02
        'ED6_DT07/CH02080 ._CH',             # 03
        'ED6_DT07/CH01600 ._CH',             # 04
        'ED6_DT27/CH03003 ._CH',             # 05
        'ED6_DT07/CH00023 ._CH',             # 06
        'ED6_DT07/CH00033 ._CH',             # 07
        'ED6_DT07/CH00043 ._CH',             # 08
        'ED6_DT07/CH00073 ._CH',             # 09
        'ED6_DT07/CH01493 ._CH',             # 0A
        'ED6_DT07/CH02083 ._CH',             # 0B
        'ED6_DT07/CH01010 ._CH',             # 0C
        'ED6_DT07/CH01030 ._CH',             # 0D
        'ED6_DT07/CH01180 ._CH',             # 0E
        'ED6_DT26/CH20365 ._CH',             # 0F
        'ED6_DT07/CH01060 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT26/CH20365P._CP',             # 00
        'ED6_DT07/CH00060P._CP',             # 01
        'ED6_DT07/CH01490P._CP',             # 02
        'ED6_DT07/CH02080P._CP',             # 03
        'ED6_DT07/CH01600P._CP',             # 04
        'ED6_DT27/CH03003P._CP',             # 05
        'ED6_DT07/CH00023P._CP',             # 06
        'ED6_DT07/CH00033P._CP',             # 07
        'ED6_DT07/CH00043P._CP',             # 08
        'ED6_DT07/CH00073P._CP',             # 09
        'ED6_DT07/CH01493P._CP',             # 0A
        'ED6_DT07/CH02083P._CP',             # 0B
        'ED6_DT07/CH01010P._CP',             # 0C
        'ED6_DT07/CH01030P._CP',             # 0D
        'ED6_DT07/CH01180P._CP',             # 0E
        'ED6_DT26/CH20365P._CP',             # 0F
        'ED6_DT07/CH01060P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -25500,
        Z                   = 0,
        Y                   = 5060,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -3080,
        Z                   = 0,
        Y                   = 3140,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 5920,
        Z                   = 0,
        Y                   = 49500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -25900,
        Z                   = 0,
        Y                   = 8660,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = -26120,
        TriggerZ            = 0,
        TriggerY            = 47750,
        TriggerRange        = 1000,
        ActorX              = -26120,
        ActorZ              = 1000,
        ActorY              = 47750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_276",          # 00, 0
        "Function_1_3A6",          # 01, 1
        "Function_2_440",          # 02, 2
        "Function_3_5BD",          # 03, 3
        "Function_4_72D",          # 04, 4
        "Function_5_1099",         # 05, 5
        "Function_6_18AC",         # 06, 6
        "Function_7_20FF",         # 07, 7
        "Function_8_2C68",         # 08, 8
        "Function_9_2CB8",         # 09, 9
        "Function_10_4CD9",        # 0A, 10
        "Function_11_4D49",        # 0B, 11
        "Function_12_4DA7",        # 0C, 12
        "Function_13_6166",        # 0D, 13
        "Function_14_6182",        # 0E, 14
        "Function_15_61B2",        # 0F, 15
        "Function_16_61CE",        # 10, 16
        "Function_17_61EA",        # 11, 17
        "Function_18_6206",        # 12, 18
        "Function_19_6300",        # 13, 19
    )


    def Function_0_276(): pass

    label("Function_0_276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2A3")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2100, 0, 48460, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A0")
    SetChrFlags(0xF, 0x80)

    label("loc_2A0")

    Jump("loc_36B")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2F1")
    SetChrPos(0xF, 7570, 0, 46210, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2100, 0, 48460, 0)
    SetChrPos(0xD, -31510, 0, 2960, 197)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2EE")
    SetChrFlags(0xA, 0x80)

    label("loc_2EE")

    Jump("loc_36B")

    label("loc_2F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_36B")
    SetChrPos(0x8, -24200, 400, 47000, 0)
    SetChrPos(0x9, -25480, 0, 46660, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    SetChrPos(0xF, 7570, 0, 46210, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2100, 0, 48460, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xD, -31510, 0, 2960, 197)

    label("loc_36B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_381")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 9)
    Jump("loc_3A5")

    label("loc_381")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_38D"),
        (SWITCH_DEFAULT, "loc_3A5"),
    )


    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A2")
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_3A2")

    Jump("loc_3A5")

    label("loc_3A5")

    Return()

    # Function_0_276 end

    def Function_1_3A6(): pass

    label("Function_1_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3B9")
    OP_B1("T1210_n")
    Jump("loc_3D5")

    label("loc_3B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x350, 3)), scpexpr(EXPR_END)), "loc_3CC")
    OP_B1("T1210_y")
    Jump("loc_3D5")

    label("loc_3CC")

    OP_B1("T1210_n")

    label("loc_3D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3F0")
    Jump("loc_3FE")

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_3FE")
    OP_6F(0x1, 10)

    label("loc_3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_420")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x0)
    OP_10(0x8, 0x1)
    OP_10(0x9, 0x1)
    OP_10(0xA, 0x1)
    OP_10(0xB, 0x1)
    Jump("loc_43F")

    label("loc_420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_43F")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    OP_10(0x3, 0x0)
    OP_10(0x4, 0x1)
    OP_10(0x5, 0x1)
    OP_10(0x6, 0x1)
    OP_10(0x7, 0x1)

    label("loc_43F")

    Return()

    # Function_1_3A6 end

    def Function_2_440(): pass

    label("Function_2_440")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_465")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5A7")

    label("loc_465")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47E")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_5A7")

    label("loc_47E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_497")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_5A7")

    label("loc_497")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B0")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_5A7")

    label("loc_4B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C9")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_5A7")

    label("loc_4C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E2")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_5A7")

    label("loc_4E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FB")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_5A7")

    label("loc_4FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_514")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_5A7")

    label("loc_514")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_5A7")

    label("loc_52D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_546")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_5A7")

    label("loc_546")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_5A7")

    label("loc_55F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_578")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_5A7")

    label("loc_578")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_591")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_5A7")

    label("loc_591")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_5A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5BC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5A7")

    label("loc_5BC")

    Return()

    # Function_2_440 end

    def Function_3_5BD(): pass

    label("Function_3_5BD")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_654")

    ChrTalk(    #0
        0xFE,
        (
            "The dragons that come up in stories\x01",
            "are almost always good guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I've never imagined they'd be nearly\x01",
            "as violent as that one...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_729")

    label("loc_654")


    ChrTalk(    #2
        0xFE,
        (
            "So dragons really exist. I thought\x01",
            "they were just fairy tales!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "But the dragons that come up in\x01",
            "stories are almost always good guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I've never imagined they'd be nearly\x01",
            "as violent as that one...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_729")

    TalkEnd(0x10)
    Return()

    # Function_3_5BD end

    def Function_4_72D(): pass

    label("Function_4_72D")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_854")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E3")

    ChrTalk(    #5
        0xFE,
        (
            "Why'd orbments stop working all\x01",
            "at once, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Maybe it has something to do with\x01",
            "that weird island above the lake the\x01",
            "kids are always looking at.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_851")

    label("loc_7E3")


    ChrTalk(    #7
        0xFE,
        (
            "It never occurred to me that\x01",
            "orbments could just...STOP\x01",
            "like this before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        "What could be causing it?\x02",
    )

    CloseMessageWindow()

    label("loc_851")

    Jump("loc_1095")

    label("loc_854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_9AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_912")

    ChrTalk(    #9
        0xFE,
        (
            "If you're looking for Gray, he's off\x01",
            "checking his trees again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "That old fuddy-duddy probably hasn't\x01",
            "even noticed that the orbments have\x01",
            "stopped working. Hmph!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_9A8")

    label("loc_912")


    ChrTalk(    #11
        0xFE,
        (
            "If you're looking for Gray, he's off\x01",
            "checking his trees again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I wish he would at least offer to help\x01",
            "around the house at a time like this!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A8")

    Jump("loc_1095")

    label("loc_9AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_ACD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A3A")

    ChrTalk(    #13
        0xFE,
        (
            "Gray's out working together with\x01",
            "the youngsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "Always brings a smile to my face\x01",
            "to see everyone banding together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACA")

    label("loc_A3A")


    ChrTalk(    #15
        0xFE,
        (
            "Gray's out working together with\x01",
            "the youngsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "I guess even a hardheaded guy like\x01",
            "him can set aside his pride now and\x01",
            "then, hmm?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_ACA")

    Jump("loc_1095")

    label("loc_ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_D13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 2)), scpexpr(EXPR_END)), "loc_B29")

    ChrTalk(    #17
        0xFE,
        "May the Goddess guide your steps.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "I'll be here, praying for you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D10")

    label("loc_B29")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x106, 0)
    Sleep(400)

    ChrTalk(    #19
        0xFE,
        "Oh, my! It's you, Agate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I thought your injuries were keeping\x01",
            "you in bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x106,
        (
            "#053FThey did, but I'm better now.\x02\x03",

            "#050FMa'am, did the dragon damage\x01",
            "your place at all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "Thankfully not.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "The Goddess was watching out for us,\x01",
            "I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x106,
        (
            "#552FThe Goddess, huh...?\x02\x03",

            "Yeah. Maybe she was. I'd like to\x01",
            "think so, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "Goodness! That's positively devout,\x01",
            "coming from you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "I'll pray for Her blessings to reach\x01",
            "you on your way, then.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A4A)

    label("loc_D10")

    Jump("loc_1095")

    label("loc_D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_F19")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E43")

    ChrTalk(    #27
        0xFE,
        (
            "Most of the homes here were hit by\x01",
            "incendiary shells during the war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "The Erebonians were supposedly aiming\x01",
            "at the Royal Army men who were camping\x01",
            "in the woods.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Why resort to such horrifying weapons?\x01",
            "What could be important enough to justify\x01",
            "doing that to your fellow man?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F16")

    label("loc_E43")


    ChrTalk(    #30
        0xFE,
        (
            "Most of the homes here were hit by\x01",
            "incendiary shells during the war.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Agate's home took the very worst\x01",
            "of it all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "It was such a cruel thing to do.\x01",
            "Everyone came together to rebuild\x01",
            "his house.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_F16")

    Jump("loc_1095")

    label("loc_F19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_1095")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FA4")

    ChrTalk(    #33
        0xFE,
        (
            "Oh, where on this earth did Vince\x01",
            "run off to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "And after I told him not to go out\x01",
            "because it was dangerous, too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1095")

    label("loc_FA4")


    ChrTalk(    #35
        0xFE,
        (
            "Oh, where on this earth did Vince\x01",
            "run off to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "And after I told him not to go out\x01",
            "because it was dangerous, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "*sigh* He really does take after his\x01",
            "grandfather. Everything's in one ear\x01",
            "and out the other with both of them!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1095")

    TalkEnd(0xD)
    Return()

    # Function_4_72D end

    def Function_5_1099(): pass

    label("Function_5_1099")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_121B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1174")

    ChrTalk(    #38
        0xFE,
        (
            "They say that even the airships and\x01",
            "haulage vehicles have stopped working\x01",
            "over in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "It hasn't affected us too badly yet, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "If this keeps up, how will we get what\x01",
            "we need?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1218")

    label("loc_1174")


    ChrTalk(    #41
        0xFE,
        (
            "They say that even the airships and\x01",
            "haulage vehicles have stopped working\x01",
            "over in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "I get anxious just thinking about what\x01",
            "could be if this keeps up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1218")

    Jump("loc_18A8")

    label("loc_121B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1378")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E8")

    ChrTalk(    #43
        0xFE,
        (
            "Just as I thought the problem with the\x01",
            "orchard was settled, now our orbments\x01",
            "have stopped working!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "The bad times just won't end...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "*sigh* Will we ever know peace again?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_1375")

    label("loc_12E8")


    ChrTalk(    #46
        0xFE,
        (
            "Just as I thought the problem with the\x01",
            "orchard was settled, now our orbments\x01",
            "have stopped working!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "The bad times just won't end...\x02",
    )

    CloseMessageWindow()

    label("loc_1375")

    Jump("loc_18A8")

    label("loc_1378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_154A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_141A")

    ChrTalk(    #48
        0xFE,
        (
            "Everyone's going all out with\x01",
            "planting the new saplings, my\x01",
            "husband included.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "It feels like a new beginning for\x01",
            "Pesca and myself, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1547")

    label("loc_141A")


    ChrTalk(    #50
        0xFE,
        (
            "Everyone's going all out with\x01",
            "planting the new saplings, my\x01",
            "husband included.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "I've been feeling so uneasy for the\x01",
            "last week or so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Everyone's been working so hard,\x01",
            "though. I'm actually starting to think\x01",
            "we can make it through it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "It finally feels like I can let\x01",
            "my hair down!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1547")

    Jump("loc_18A8")

    label("loc_154A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1657")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_15C5")

    ChrTalk(    #54
        0xFE,
        (
            "I saw everyone talking about what\x01",
            "to do with the orchards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "Pesca was all smiles afterward, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1654")

    label("loc_15C5")


    ChrTalk(    #56
        0xFE,
        (
            "I saw everyone talking about what\x01",
            "to do with the orchards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "Pesca was all smiles afterward, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        "Maybe things are looking up.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1654")

    Jump("loc_18A8")

    label("loc_1657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_16EB")

    ChrTalk(    #59
        0xFE,
        (
            "My husband still hasn't come back\x01",
            "from the orchards...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "I hope he isn't worrying over things\x01",
            "too much. He's always so serious...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A8")

    label("loc_16EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_18A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_175F")

    ChrTalk(    #61
        0xFE,
        (
            "My husband poured his heart into\x01",
            "researching fruit trees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "And now...now it's all gone...\x02",
    )

    CloseMessageWindow()
    Jump("loc_18A8")

    label("loc_175F")


    ChrTalk(    #63
        0xFE,
        (
            "My husband poured his heart into\x01",
            "researching fruit trees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "He introduced more efficient machines,\x01",
            "carefully crossbred trees to be shorter\x01",
            "so that harvesting would be easier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "He's done so much for the orchards.\x01",
            "They're his passion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "But now...now...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "What can I possibly even say to make\x01",
            "things better?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_18A8")

    TalkEnd(0xE)
    Return()

    # Function_5_1099 end

    def Function_6_18AC(): pass

    label("Function_6_18AC")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_199B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1945")

    ChrTalk(    #68
        0xFE,
        (
            "Every time something like this\x01",
            "happens, I can't help but think\x01",
            "of the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        "Ten years later, it still haunts us all.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1998")

    label("loc_1945")


    ChrTalk(    #70
        0xFE,
        (
            "Every time something like this\x01",
            "happens, I can't help but think\x01",
            "of the Empire.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1998")

    Jump("loc_20FB")

    label("loc_199B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1B4F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1A5D")

    ChrTalk(    #71
        0xFE,
        (
            "Things are starting to go back\x01",
            "to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "My husband's gone to visit the\x01",
            "memorial for the first time in a\x01",
            "while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "I'm sure he has plenty to say\x01",
            "to everyone there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B4C")

    label("loc_1A5D")


    ChrTalk(    #74
        0xFE,
        (
            "Things are starting to go back\x01",
            "to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "I know it will take some time\x01",
            "to rebuild the orchards...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        (
            "But if we all come together as\x01",
            "a village, we can overcome this.\x01",
            "I know it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Just as we overcame the scars\x01",
            "of the war.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1B4C")

    Jump("loc_20FB")

    label("loc_1B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1D59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 4)), scpexpr(EXPR_END)), "loc_1BB4")

    ChrTalk(    #78
        0xFE,
        (
            "It sounds like you have a lot\x01",
            "of work ahead of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "Take care, all right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D56")

    label("loc_1BB4")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x106, 0)
    Sleep(400)

    ChrTalk(    #80
        0xFE,
        "Agate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Thank Aidios! I'm glad to see you\x01",
            "on your feet again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x106,
        (
            "#053FYeah, I'm sorry. Guess I made you\x01",
            "worry, huh?\x02\x03",

            "#051FI'm fine now, though.\x02\x03",

            "#051FWell, I ain't exactly top shape yet,\x01",
            "but not like gonna keel over from\x01",
            "a little walkin' around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        "I'm glad to hear that, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "It sounds like you have a lot\x01",
            "of work ahead of you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        "Please, take care of yourself.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A4C)

    label("loc_1D56")

    Jump("loc_20FB")

    label("loc_1D59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_1F97")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1DEA")

    ChrTalk(    #86
        0xFE,
        (
            "Mischa had the loveliest smile,\x01",
            "and she dearly loved Agate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "It's been ten years since then...\x01",
            "Time passes so quickly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F94")

    label("loc_1DEA")


    ChrTalk(    #88
        0xFE,
        (
            "Mischa had the loveliest smile,\x01",
            "and she dearly loved Agate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Ah, but she was just as strong-\x01",
            "willed and stubborn as her brother.\x01",
            "Perhaps even more so!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "When she set her mind on something,\x01",
            "she was the type who never let it go\x01",
            "until she damn well made it happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "I sometimes can't help but wonder\x01",
            "what the future would've held for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "I think she would've been head\x01",
            "of the orchards by now! If only...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1F94")

    Jump("loc_20FB")

    label("loc_1F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_END)), "loc_20FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2032")

    ChrTalk(    #93
        0xFE,
        (
            "The... The screams of the children,\x01",
            "the smoke of burning trees...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Oh, mercy, everything from ten years\x01",
            "ago's come rushing back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20FB")

    label("loc_2032")


    ChrTalk(    #95
        0xFE,
        (
            "The... The screams of the children,\x01",
            "the smoke of burning trees...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Oh, mercy, everything from ten years\x01",
            "ago's come rushing back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "It took but a single moment to lose\x01",
            "everything we had.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_20FB")

    TalkEnd(0xF)
    Return()

    # Function_6_18AC end

    def Function_7_20FF(): pass

    label("Function_7_20FF")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2857")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2589")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21EE")

    ChrTalk(    #98
        0xFE,
        "Hello there, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "Did you come by to check on us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x106,
        (
            "#051FYeah, wanted to make sure you\x01",
            "guys were all right in this mess.\x02\x03",

            "Sorta figured we wouldn't have\x01",
            "as big a problem, though.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)
    Jump("loc_2271")

    label("loc_21EE")


    ChrTalk(    #101
        0xFE,
        "Hello there, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1000FHi, Elder Reisen!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x102,
        (
            "#1041FIt's good to see you well, sir.\x02\x03",

            "How is Ravennue doing?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    label("loc_2271")


    ChrTalk(    #104
        0xFE,
        "Hmm.. Well, we're fine, for the moment.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "We weren't very orbal-dependant in the\x01",
            "first place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "For once, that seems to have been to\x01",
            "our benefit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#1011FI'll say!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2380")

    ChrTalk(    #108
        0x108,
        (
            "#070FYeah, the cities are in rougher\x01",
            "shape than here, that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243A")

    label("loc_2380")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23D4")

    ChrTalk(    #109
        0x103,
        (
            "#020FYes, the cities are in far worse\x01",
            "shape than Ravennue is.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243A")

    label("loc_23D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_243A")

    ChrTalk(    #110
        0x106,
        (
            "#050FYeah, the cities are a damned\x01",
            "mess right now. This is paradise\x01",
            "in comparison.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243A")


    ChrTalk(    #111
        0x102,
        (
            "#1043FAs much as they make life more\x01",
            "convenient, they also create more\x01",
            "points of failure...\x02\x03",

            "Orbments can't be the solution to\x01",
            "everything.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #112
        0xFE,
        (
            "Even a lit fireplace can burn\x01",
            "a house down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        (
            "Any technology can have dangers\x01",
            "you never realized when it was first\x01",
            "conceived.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "We'll be just fine. Don't you fret.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x2093)
    Jump("loc_2854")

    label("loc_2589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_27E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_260D")

    ChrTalk(    #115
        0xFE,
        "Ravennue is at peace for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "We've been spared, ironically, by our\x01",
            "underdeveloped orbal infrastructure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27DE")

    label("loc_260D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_272F")

    ChrTalk(    #117
        0xFE,
        (
            "The situation with the orbments is a\x01",
            "critical issue for the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "Even with the non-aggression pact in\x01",
            "place, we must watch the movements\x01",
            "of the Erebonians closely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "One might think me a little paranoid,\x01",
            "but personally, I feel that one can never\x01",
            "be too careful.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_27DE")

    label("loc_272F")


    ChrTalk(    #120
        0xFE,
        (
            "The situation with the orbments is a\x01",
            "critical issue for the army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "Even with the non-aggression pact in\x01",
            "place, we must watch the movements\x01",
            "of the Erebonians closely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27DE")

    Jump("loc_2854")

    label("loc_27E1")


    ChrTalk(    #122
        0xFE,
        "Ravennue is at peace for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "We've been spared, ironically, by our\x01",
            "underdeveloped orbal infrastructure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2854")

    Jump("loc_2C64")

    label("loc_2857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2C0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x349, 3)), scpexpr(EXPR_END)), "loc_28CE")

    ChrTalk(    #124
        0xFE,
        (
            "We all wish you the best of luck in\x01",
            "your efforts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "But please, don't push yourself too hard.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C0A")

    label("loc_28CE")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #126
        0xFE,
        "Hello there!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        "How goes your capture plan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x101,
        (
            "#1015FWell, we know what's causing the\x01",
            "dragon to go crazy now.\x02\x03",

            "#1006FIf our next plan goes okay, we should\x01",
            "have this whole mess sorted out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #129
        0xFE,
        "Haha! That's wonderful news!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "But I must implore you: be careful.\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #131
        0xFE,
        "Especially you, Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Your sister would haunt me for\x01",
            "eternity if something happened\x01",
            "to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x106,
        (
            "#552FEh, you don't need to worry.\x02\x03",

            "I've got a little watcher keeping an\x01",
            "eye on me all the time as it stands.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #134
        0x107,
        "#067FAha...haha...ha.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Hmm. That's good enough for\x01",
            "me, I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "Be careful, all of you. And good luck.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "Dragons are creatures beyond mortal\x01",
            "understanding. Who knows what could\x01",
            "happen if you challenge one?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x106,
        "#053FI'm keepin' that in mind, trust me.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A4B)

    label("loc_2C0A")

    Jump("loc_2C64")

    label("loc_2C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 2)), scpexpr(EXPR_END)), "loc_2C64")

    ChrTalk(    #139
        0xFE,
        "Leave Agate's care to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "Fair roads to you on your way\x01",
            "back to Bose.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C64")

    TalkEnd(0xA)
    Return()

    # Function_7_20FF end

    def Function_8_2C68(): pass

    label("Function_8_2C68")

    TalkBegin(0x9)

    ChrTalk(    #141
        0x9,
        (
            "#060FI'll keep a close eye on Agate.\x02\x03",

            "You guys be careful, promise?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_8_2C68 end

    def Function_9_2CB8(): pass

    label("Function_9_2CB8")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrPos(0x0, -27360, 0, 44980, 305)
    OP_6D(-27230, 0, 39560, 0)
    OP_67(0, 7150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x8, -24200, 400, 47000, 0)
    SetChrPos(0x9, -25480, 0, 46660, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0)
    OP_6F(0x1, 10)
    OP_4A(0x9, 255)

    def lambda_2D5F():
        OP_6D(-24990, 0, 47100, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D5F)

    def lambda_2D77():
        OP_67(0, 6150, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D77)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    Fade(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DB2")
    Call(0, 18)

    label("loc_2DB2")

    OP_6D(4120, 200, 47460, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(33000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 3250, 200, 45650, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E32")
    SetChrPos(0xF7, 4580, 200, 45570, 0)
    SetChrPos(0xF8, 2310, 200, 46950, 90)
    Jump("loc_2E54")

    label("loc_2E32")

    SetChrPos(0xF8, 4580, 200, 45570, 0)
    SetChrPos(0xF7, 2310, 200, 46950, 90)

    label("loc_2E54")

    SetChrPos(0xB, 3300, 250, 48050, 180)
    SetChrPos(0xA, 4600, 200, 48050, 180)
    SetChrPos(0xC, 2350, 0, 48960, 180)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0xF7, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0xF7, 0x40)
    SetChrFlags(0xF8, 0x40)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0xF7, 0x80)
    ClearChrFlags(0xF8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0xF7, 0x1)
    ClearChrFlags(0xF8, 0x1)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xA, 0x1)
    SetChrFlags(0xF, 0x80)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0xA, 10)
    SetChrSubChip(0xA, 7)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 11)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F21")
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 6)

    label("loc_2F21")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F39")
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x104, 7)

    label("loc_2F39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F51")
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 8)

    label("loc_2F51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F69")
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 9)

    label("loc_2F69")

    OP_4A(0xA, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_DC()

    ChrTalk(    #142
        0xA,
        "I see... What a mess.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xA,
        (
            "Miss Bright, General, sir.\x01",
            "I'm sorry to have caused you so much trouble.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#1003F#2PNo...\x02\x03",

            "In the end, we couldn't stop the dragon's\x01",
            "rampage.\x02\x03",

            "#1007FI'm sorry we weren't of much help, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xB,
        (
            "#163F#6PYou've no reason to disparage yourself,\x01",
            "Miss Bright.\x02\x03",

            "#160FEven with the dragon still on the loose,\x01",
            "you have proven indispensable in the\x01",
            "aid you have given others.\x02\x03",

            "You successfully evacuated the market, and\x01",
            "Mr. Crosner's firefighting efforts were marvelous.\x01",
            "Only you bracers could have responded so quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x101,
        (
            "#1016F#2PAh-hahaha... I have to admit, General,\x01",
            "it feels a little...strange...to hear you\x01",
            "say that.\x02\x03",

            "#1026FBut, um...about Agate.\x02\x03",

            "Is it true that, during the war, his little\x01",
            "sister was...um...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xA,
        "It...is, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xA,
        (
            "Liberl's forces and the Imperial Army were\x01",
            "fighting on the village's outskirts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xA,
        (
            "During the battle, some Erebonian incendiary\x01",
            "rounds hit the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xA,
        (
            "Ultimately, some of the homes were burnt\x01",
            "and some of our villagers lost their lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xA,
        "One of them...was Mischa Crosner.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#1003F#2P...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34C0")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33D6")
    SetChrSubChip(0xF7, 2)
    Sleep(300)
    Jump("loc_33FB")

    label("loc_33D6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33F1")
    SetChrSubChip(0xF8, 2)
    Sleep(300)
    Jump("loc_33FB")

    label("loc_33F1")

    SetChrSubChip(0xF8, 1)
    Sleep(300)

    label("loc_33FB")


    ChrTalk(    #153
        0x103,
        (
            "#524FTo be honest...\x01",
            "I'd heard a little bit about this.\x02\x03",

            "Agate never seemed remotely interested in\x01",
            "talking about it, though, so I never brought\x01",
            "it up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x101,
        "#1026F#2PNow I understand...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0)

    label("loc_34C0")


    ChrTalk(    #155
        0xB,
        (
            "#163F#6P...In a way, the Royal Army is culpable\x01",
            "for that entire incident.\x02\x03",

            "#160FThe defensive line we established to protect\x01",
            "the village ended up doing little more than\x01",
            "drawing the fighting into it.\x02\x03",

            "The end result was large portions of the\x01",
            "village being laid waste.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        "#1026F#2POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xB,
        (
            "#163F#6PAnd the order to establish the defensive\x01",
            "line came from my desk.\x02\x03",

            "You can very easily say that the blood\x01",
            "of those people is on my hands.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(    #158
        0xA,
        (
            "#4PGeneral, sir. Please, you don't need\x01",
            "to blame yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xA,
        (
            "#4PThe Royal Army was doing their duty,\x01",
            "that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xA,
        (
            "#4PThe whole thing was just a tragedy built\x01",
            "on several coincidences colliding.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 1)
    Sleep(300)

    ChrTalk(    #161
        0xB,
        (
            "#160F#6PNo, Reisen. You needn't make excuses\x01",
            "for me.\x02\x03",

            "Those sort of justifications hold no\x01",
            "meaning for those who lost family.\x02\x03",

            "Those like that red-haired young man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xA,
        "#4PWell...\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(300)

    ChrTalk(    #163
        0xB,
        (
            "#163F#6PAfter the battle, I attended the funeral\x01",
            "for the village's dead as a representative\x01",
            "of the army.\x02\x03",

            "I still clearly remember the eyes of one\x01",
            "particular red-haired young man in\x01",
            "attendance.\x02\x03",

            "Bottomless sadness, twisted by rage...\x01",
            "Eyes such as I have never seen before\x01",
            "or since.\x02\x03",

            "#160FAnd I was the one responsible for giving\x01",
            "him such eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xA,
        "#4P...No. That isn't true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xA,
        (
            "#4PAgate never blamed the Erebonians,\x01",
            "or the Royal Army, or even you, General.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xA,
        "#4PThe person he blamed was himself.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 1)
    Sleep(300)

    ChrTalk(    #167
        0xB,
        "#161F#6PHm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        "#1015F#2PWhat do you mean?\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0)
    Sleep(50)

    ChrTalk(    #169
        0xA,
        "All I know is what I observed, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        (
            "Agate always seemed to blame himself,\x01",
            "in some way, for Mischa's death.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0xA,
        (
            "Wasn't even remotely true, of course.\x01",
            "But he convinced himself it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xA,
        (
            "And then, after practically torturing himself\x01",
            "over what happened, he left the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xA,
        (
            "He wanted to search for an answer--\x01",
            "to find a way to make it up to Mischa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xA,
        (
            "I always thought his time as a street thug\x01",
            "in Ruan was because of that...\x01",
            "Because he never found his answer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        "#1003F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xA,
        (
            "He did eventually get his head screwed back\x01",
            "on and began walking the path of a bracer,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xA,
        (
            "I don't think he ever truly found\x01",
            "the answer he sought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        (
            "He's still trapped by that same sadness...\x01",
            "that same anger at himself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xB,
        "#163F#6PHow terrible...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x101,
        (
            "#1002F#2PHey...General.\x02\x03",

            "Are you sure you won't let us bracers\x01",
            "help against the dragon?\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0)
    Sleep(50)

    ChrTalk(    #181
        0xB,
        "#161F#6PWhat...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#1000F#2PWe definitely have some strong points\x01",
            "the army doesn't.\x02\x03",

            "We're smaller so we can respond faster,\x01",
            "we're closer to the civilian population...\x02\x03",

            "It's a bit easier for us to get to places\x01",
            "where the army has trouble getting to,\x01",
            "too.\x02\x03",

            "I know we could help if you'd let us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xB,
        "#163F#6PBut--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        (
            "#1010F#2PNow that I've heard all this, I think Agate became\x01",
            "a bracer because he thought there was potential\x01",
            "in those abilities.\x02\x03",

            "The potential to find a way to make peace\x01",
            "with his sister...\x02\x03",

            "#1003FYeah... I think I can understand, now, why Agate\x01",
            "became a bracer when Dad invited him.\x02\x03",

            "Dad became a bracer when he...\x01",
            "lost Mom, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0xB,
        "#160F#6P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1002F#2PSo to prove the potential of bracers...\x02\x03",

            "And, more than anything, to help the\x01",
            "people in need around me...\x02\x03",

            "I want to do everything I possibly can.\x02\x03",

            "So...please! Let us help you!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4172")

    ChrTalk(    #187
        0x105,
        "#542FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x103,
        "#027FNicely said.\x02",
    )

    CloseMessageWindow()
    Jump("loc_432A")

    label("loc_4172")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41D3")

    ChrTalk(    #189
        0x104,
        "#035FAh! Beautifully said, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x103,
        "#027FYes, nicely said.\x02",
    )

    CloseMessageWindow()
    Jump("loc_432A")

    label("loc_41D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4229")

    ChrTalk(    #191
        0x103,
        "#524FEstelle... Oh, honey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x108,
        "#070FHeh, well said!\x02",
    )

    CloseMessageWindow()
    Jump("loc_432A")

    label("loc_4229")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4283")

    ChrTalk(    #193
        0x105,
        "#542FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x104,
        "#035FAh! Beautifully said, Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_432A")

    label("loc_4283")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42CE")

    ChrTalk(    #195
        0x105,
        "#542FEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x108,
        "#070FHeh, well said!\x02",
    )

    CloseMessageWindow()
    Jump("loc_432A")

    label("loc_42CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_432A")

    ChrTalk(    #197
        0x104,
        "#035FAh! Beautifully said, Estelle.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x108,
        "#070FYes, well said!\x02",
    )

    CloseMessageWindow()

    label("loc_432A")


    ChrTalk(    #199
        0xB,
        (
            "#160F#6P...\x02\x03",

            "#163FI wonder. Had bracers been in Bose\x01",
            "ten years ago, could it all have been...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        "#1015F#2PHm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xB,
        (
            "#163F#6PIt's nothing.\x02\x03",

            "#160FCassius is swamped with other duties,\x01",
            "so I will be taking command of army\x01",
            "operations against the dragon.\x02\x03",

            "I need to head back to the Haken Gate and\x01",
            "hold council over our next moves.\x02\x03",

            "I will take your suggestion under advisement.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0x101,
        "#1018F#2PSo, then...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xB,
        (
            "#163F#6PDo not be hasty.\x01",
            "I merely said I would take it under advisement.\x02\x03",

            "#160FI will contact your guildhouse tonight\x01",
            "with the results of our deliberations.\x02\x03",

            "That is all I can promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        "#1006F#2P...Right. We understand.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45F8")

    ChrTalk(    #205
        0x103,
        (
            "#027FWe'll be on pins and needles for\x01",
            "the response, General.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4690")

    label("loc_45F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_463B")

    ChrTalk(    #206
        0x108,
        "#071FWe'll be waiting to hear from you, sir.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4690")

    label("loc_463B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4690")

    ChrTalk(    #207
        0x104,
        (
            "#031FThe orchestra tenses, awaiting a single word!\x01",
            "I cannot wait.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4690")


    ChrTalk(    #208
        0xB,
        "#160F#6PI must pardon myself here, then.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 1)
    Sleep(300)

    ChrTalk(    #209
        0xB,
        "#160F#6PReisen, my thanks for your hospitality.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 1)
    Sleep(300)

    ChrTalk(    #210
        0xA,
        "#4PNo, no. Please, come by any time.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    SetChrFlags(0xB, 0x1)
    SetChrPos(0xB, 2480, 0, 48000, 270)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 3)
    OP_0D()

    def lambda_4762():
        OP_6D(1500, 0, 44410, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4762)
    OP_43(0xB, 0x1, 0x0, 0xA)
    Sleep(800)
    OP_43(0xC, 0x1, 0x0, 0xB)
    SetChrSubChip(0x101, 1)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF7)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47B5")
    SetChrSubChip(0xF7, 1)
    Sleep(50)
    SetChrSubChip(0xF8, 2)
    Sleep(300)
    Jump("loc_47C9")

    label("loc_47B5")

    SetChrSubChip(0xF7, 2)
    Sleep(50)
    SetChrSubChip(0xF8, 1)
    Sleep(300)

    label("loc_47C9")

    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_6D(4370, 0, 47120, 3000)
    WaitChrThread(0xC, 0x1)
    SetChrSubChip(0x101, 0)
    Sleep(300)

    ChrTalk(    #211
        0x101,
        (
            "#1006F#2POkay, we'd better get back to Bose.\x02\x03",

            "#1015FAgate...should probably stay here, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_48D9")

    ChrTalk(    #212
        0x105,
        (
            "#047FHe's going to need at least a few days\x01",
            "to recover from his wounds.\x02\x03",

            "#542FWe should let him sleep for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49E9")

    label("loc_48D9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4951")

    ChrTalk(    #213
        0x108,
        (
            "#074FInjuries like his will take at least\x01",
            "a few days to heal.\x02\x03",

            "#070FLet us let him sleep for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49E9")

    label("loc_4951")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49E9")

    ChrTalk(    #214
        0x104,
        (
            "#035FThe slings and arrows our Raven-knight\x01",
            "has endured shall keep him abed for\x01",
            "several days.\x02\x03",

            "#030FWe should leave him to his rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49E9")


    ChrTalk(    #215
        0x101,
        (
            "#1006F#2PYeah, good idea.\x02\x03",

            "Let's check in on him before we go and\x01",
            "fill in Tita with what's going on.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF8, 0)
    Sleep(50)
    SetChrSubChip(0xF7, 0)
    Sleep(300)

    ChrTalk(    #216
        0x101,
        (
            "#1015F#2POh, um, Elder Reisen?\x02\x03",

            "I know now's not the best time to ask,\x01",
            "but please take care of Agate for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xA,
        (
            "#6PHaha, you don't need to worry.\x01",
            "He's part of our family here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xA,
        (
            "#6PBesides, compared to ten years ago?\x01",
            "A dragon is nothing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xA,
        (
            "#6PWe should be thanking the Goddess\x01",
            "no one's died yet.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(1820, 0, 44890, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1820, 0, 44890, 225)
    SetChrPos(0x1, 1820, 0, 44890, 225)
    SetChrPos(0x2, 1820, 0, 44890, 225)
    OP_69(0x0, 0x0)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0xF7, 65535)
    SetChrChipByIndex(0xF8, 65535)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0xF7, 0x4)
    ClearChrFlags(0xF8, 0x4)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0xF7, 0x40)
    ClearChrFlags(0xF8, 0x40)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0xF7, 0x1)
    SetChrFlags(0xF8, 0x1)
    SetChrFlags(0xB, 0x1)
    SetChrFlags(0xA, 0x1)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 7570, 0, 46210, 90)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 2)
    SetChrPos(0xA, -2100, 0, 48460, 0)
    OP_43(0xA, 0x0, 0x0, 0x2)
    OP_43(0xF, 0x0, 0x0, 0x2)
    OP_A2(0x1A1A)
    OP_28(0x94, 0x1, 0x80)
    OP_28(0x94, 0x1, 0x100)
    OP_28(0x94, 0x1, 0x200)
    OP_28(0x94, 0x1, 0x400)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_9_2CB8 end

    def Function_10_4CD9(): pass

    label("Function_10_4CD9")

    OP_8E(0xFE, 0x35C, 0x0, 0xBA9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF74, 0x0, 0x9E3E, 0x7D0, 0x0)
    OP_4A(0xC, 255)
    SetChrSubChip(0xC, 0)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_4B(0xC, 255)

    def lambda_4D1E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D1E)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFF74, 0x0, 0x9542, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_10_4CD9 end

    def Function_11_4D49(): pass

    label("Function_11_4D49")

    OP_8E(0xFE, 0x35C, 0x0, 0xBA9A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF74, 0x0, 0x9E3E, 0x7D0, 0x0)

    def lambda_4D77():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4D77)
    SetChrFlags(0xFE, 0x4)
    OP_8E(0xFE, 0xFFFFFF74, 0x0, 0x9542, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_11_4D49 end

    def Function_12_4DA7(): pass

    label("Function_12_4DA7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4DBA")
    Call(0, 18)

    label("loc_4DBA")

    OP_6D(-24530, 0, 47200, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -25870, -500, 37510, 0)
    SetChrPos(0xF7, -25870, -500, 37510, 0)
    SetChrPos(0xF8, -25870, -500, 37510, 0)
    OP_4A(0x9, 255)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x71, 0x0, 0x64)
    Sleep(500)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4E64():

        label("loc_4E64")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_4E64")

    QueueWorkItem2(0x9, 1, lambda_4E64)
    OP_22(0x6, 0x0, 0x64)

    def lambda_4E7A():
        OP_6D(-25990, 0, 46100, 3500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E7A)

    def lambda_4E92():

        label("loc_4E92")

        TurnDirection(0x9, 0x101, 400)
        OP_48()
        Jump("loc_4E92")

    QueueWorkItem2(0x9, 1, lambda_4E92)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(800)
    OP_43(0xF7, 0x1, 0x0, 0xE)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0xF)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #220
        0x9,
        "#560FEstelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x101,
        (
            "#1006F#6PHi, Tita.\x02\x03",

            "How's Agate doing?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x9,
        (
            "#561FHe's still asleep.\x02\x03",

            "#066FBut, um, his face looks a lot better,\x01",
            "so I think he'll be okay so long as he\x01",
            "gets a lot of rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #223
        0x101,
        (
            "#1025F#6PI see.\x02\x03",

            "#1006FSo...this is Agate's house, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    OP_8C(0x101, 90, 400)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_502E")

    ChrTalk(    #224
        0x104,
        (
            "#031FHm. It is small...\x01",
            "but it is warm and comfortable.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_50D5")

    label("loc_502E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5070")

    ChrTalk(    #225
        0x105,
        "#048FIt's small, but it feels so...so warm.\x02",
    )

    CloseMessageWindow()
    Jump("loc_50D5")

    label("loc_5070")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50D5")

    ChrTalk(    #226
        0x103,
        (
            "#021FHmmmmm. A bit on the small side...\x01",
            "but every rege exudes warmth and comfort.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50D5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_511E")

    ChrTalk(    #227
        0x108,
        "#070FThis is where he lived with his sister, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_51DF")

    label("loc_511E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5188")

    ChrTalk(    #228
        0x103,
        (
            "#027FYes, every rege exudes warmth.\x01",
            "This is where he lived with his sister, then...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51DF")

    label("loc_5188")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51DF")

    ChrTalk(    #229
        0x105,
        (
            "#048FIt's so...loving.\x01",
            "This must be where he lived with his sister.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51DF")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #230
        0x101,
        "#1004F#6PHey!\x02",
    )

    CloseMessageWindow()

    def lambda_521B():
        OP_6D(-26280, 0, 46950, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_521B)

    def lambda_5233():
        OP_8E(0xFE, 0xFFFF98AE, 0x0, 0xB6EE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5233)
    WaitChrThread(0x101, 0x2)
    OP_44(0x9, 0x1)

    ChrTalk(    #231
        0x101,
        "#1011F#6PThis photograph...\x02",
    )

    CloseMessageWindow()
    OP_43(0xF7, 0x1, 0x0, 0x10)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x11)
    Sleep(500)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_AD(0x240082, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #232
        (
            "\x07\x00#1006FThis looks like a picture of when Agate\x01",
            "was a kid.\x02\x03",

            "That means this girl must be...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(300, 310, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #233
        "\x07\x00#066FYes... I think it's Mischa.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5402")
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #234
        (
            "\x07\x00#021FOh, my goodness. She might just be the\x01",
            "most adorable girl to have ever lived!\x02\x03",

            "It looks like she and Agate were very close.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Jump("loc_5507")

    label("loc_5402")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5489")
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #235
        (
            "\x07\x00#031FHmmmm... What a sweet little child.\x02\x03",

            "#030FShe and Agate seem to have been quite close.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Jump("loc_5507")

    label("loc_5489")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5507")
    SetMessageWindowPos(200, 320, -1, -1)
    SetChrName("Kloe")

    AnonymousTalk(    #236
        (
            "\x07\x00#048FShe's such an adorable little girl...\x02\x03",

            "It looks like she and Agate were very close.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()

    label("loc_5507")

    SetMessageWindowPos(300, 310, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #237
        (
            "\x07\x00#067FHeehee! I think so, too.\x02\x03",

            "Agate and Mischa look really happy,\x01",
            "after all...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #238
        (
            "\x07\x00#1006FYeah...they really do.\x02\x03",

            "Agate looks about fourteen in this,\x01",
            "so Mischa would be...what, twelve?\x02\x03",

            "Agate's got the sort of face that just\x01",
            "screams 'I'm the world's biggest prankster!'\x02\x03",

            "#1001FHeehee... I bet he was an interesting kid.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5727")
    SetMessageWindowPos(150, 320, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #239
        (
            "\x07\x00#070FHey, now, don't read too much into a\x01",
            "man's old photographs.\x02\x03",

            "It's a little embarrassing.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #240
        "\x07\x00#1016FAhaha... Really?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()

    label("loc_5727")

    SetMessageWindowPos(72, 320, 56, 3)
    OP_8C(0x101, 180, 0)
    OP_AE(0x1F4)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #241
        0x101,
        (
            "#1015F#6PStill, though...\x02\x03",

            "Why did Agate keep quiet about his sister?\x02\x03",

            "He kept talking about her as if\x01",
            "she was alive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x9,
        (
            "#063F#4PYeah...but, um.\x02\x03",

            "#561FIf you think about it, Agate never said\x01",
            "Mischa was alive.\x02\x03",

            "He said he 'comes back to visit,' and I bet\x01",
            "he meant he visits her grave...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    Sleep(300)

    ChrTalk(    #243
        0x101,
        (
            "#1026FNow that you mention it, yeah.\x02\x03",

            "#1015FHe still should've known we had the wrong\x01",
            "idea about it, though.\x02\x03",

            "Why wouldn't he correct us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x9,
        (
            "#063F#4PI don't know, but...\x02\x03",

            "#067FAgate said once work calmed down a bit\x01",
            "he'd introduce us all.\x02\x03",

            "I think he was going to tell us then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x101,
        (
            "#1006FThat's right. I bet that's it.\x02\x03",

            "#1007FWell, we can ask him later what he\x01",
            "intended, but...\x02\x03",

            "#1015FUm...Tita.\x02\x03",

            "We need to head back to the Bose\x01",
            "guildhouse soon. But, uh...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x9,
        "#064F#4PWhat is it?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #247
        (
            "\x07\x05Estelle explained that the army would be\x01",
            "contacting the guild that evening.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #248
        0x9,
        (
            "#063F#4POh, I see.\x02\x03",

            "...\x02\x03",

            "#561FU-Umm, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x101,
        (
            "#1006FYou don't need to say anything, Tita.\x02\x03",

            "You're gonna say you want to stay behind\x01",
            "to take care of Agate, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #250
        0x9,
        "#065F#4PEr! Umm!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x101,
        (
            "#1028FMuahaha. Underestimate me at\x01",
            "your own peril, my little Tita.\x02\x03",

            "I can read the inside of your mind like a\x01",
            "picture book. It's a 'big sister' thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x9,
        "#562F#4PAwwww...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CA4")

    ChrTalk(    #253
        0x103,
        "#021FWe've got the rest handled, Tita.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D2A")

    label("loc_5CA4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CE0")

    ChrTalk(    #254
        0x104,
        "#031FHeh. Leave the rest to us, Tita.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5D2A")

    label("loc_5CE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D2A")

    ChrTalk(    #255
        0x105,
        (
            "#041FHaha, Tita, don't worry.\x01",
            "We will handle the rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DA0")

    ChrTalk(    #256
        0x108,
        (
            "#070FYou just put your efforts into nursing Agate\x01",
            "back to health so he can be back on his\x01",
            "feet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E70")

    label("loc_5DA0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E00")

    ChrTalk(    #257
        0x105,
        (
            "#048FTita, you can focus on helping Agate heal,\x01",
            "all right? We understand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E70")

    label("loc_5E00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E70")

    ChrTalk(    #258
        0x104,
        (
            "#035FHeh, my little Tita. All you need do now is focus\x01",
            "on mending your Raven's broken wings.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E70")

    OP_44(0x9, 0x1)
    OP_8C(0x9, 180, 400)
    Sleep(300)

    ChrTalk(    #259
        0x9,
        (
            "#560F#4PEstelle, everyone...\x02\x03",

            "#067FThank you so much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0x101,
        (
            "#1016FD'aww. You don't need to thank us.\x02\x03",

            "#1006FThere's only one thing I'll ask you to do.\x01",
            "When Agate wakes up, tell him what we\x01",
            "just told you, okay?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 270, 400)

    ChrTalk(    #261
        0x9,
        (
            "#064F#4PAh, you mean the stuff about the bracers\x01",
            "and army working together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x101,
        (
            "#1006FYeah. Also, I want you to stop Agate from\x01",
            "trying anything reckless--physically,\x01",
            "if necessary.\x02\x03",

            "You're not to let him out of this bed\x01",
            "until he's fully healed, got it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x9,
        (
            "#067F#4PYeah... I'll do my best!\x02\x03",

            "#560FEstelle, everyone, be careful, okay?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-25860, 0, 43830, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, -25790, 0, 43940, 180)
    SetChrPos(0x1, -25790, 0, 43940, 180)
    SetChrPos(0x2, -25790, 0, 43940, 180)
    ClearChrFlags(0xF7, 0x4)
    ClearChrFlags(0xF8, 0x4)
    OP_69(0x0, 0x0)
    OP_8C(0x9, 90, 0)
    OP_4B(0x9, 255)
    OP_A2(0x1A1B)
    OP_28(0x94, 0x1, 0x800)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_12_4DA7 end

    def Function_13_6166(): pass

    label("Function_13_6166")

    OP_8E(0xFE, 0xFFFF9B10, 0x0, 0xAFBE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_6166 end

    def Function_14_6182(): pass

    label("Function_14_6182")

    OP_8E(0xFE, 0xFFFF98F4, 0x0, 0xA726, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF9DFE, 0x0, 0xA9E2, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_6182 end

    def Function_15_61B2(): pass

    label("Function_15_61B2")

    OP_8E(0xFE, 0xFFFF98CC, 0x0, 0xAAC8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_61B2 end

    def Function_16_61CE(): pass

    label("Function_16_61CE")

    OP_8E(0xFE, 0xFFFF9CDC, 0x0, 0xB108, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_16_61CE end

    def Function_17_61EA(): pass

    label("Function_17_61EA")

    OP_8E(0xFE, 0xFFFF9A5C, 0x0, 0xAFB4, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_17_61EA end

    def Function_18_6206(): pass

    label("Function_18_6206")

    FadeToDark(0, 0, -1)
    OP_6D(-15500, 30, 64410, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_62BC"),
        (1, "loc_62C2"),
        (SWITCH_DEFAULT, "loc_62C8"),
    )


    label("loc_62BC")

    OP_A2(0x1200)
    Jump("loc_62C8")

    label("loc_62C2")

    OP_A2(0x1201)
    Jump("loc_62C8")

    label("loc_62C8")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x3, 0x0, 0xFF, 0xFF, 0x2, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_18_6206 end

    def Function_19_6300(): pass

    label("Function_19_6300")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x240082, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_19_6300 end

    SaveToFile()

Try(main)
