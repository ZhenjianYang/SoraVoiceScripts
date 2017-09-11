from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0012   ._SN',
        MapName             = 'event',
        Location            = 'E0012.x',
        MapIndex            = 232,
        MapDefaultBGM       = "ed60001",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT01/E0012   ._SN',
            'ED6_DT01/E0012_1 ._SN',
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
        'Maintenance Chief Gustav',             # 9
        'Rehmann',                              # 10
        'Faye',                                 # 11
        'Igor',                                 # 12
        'Antoine',                              # 13
        'Wilmont',                              # 14
        'Agate',                                # 15
        'Tita',                                 # 16
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
        Unknown_3A              = 232,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH02440 ._CH',             # 00
        'ED6_DT06/CH20078 ._CH',             # 01
        'ED6_DT07/CH01550 ._CH',             # 02
        'ED6_DT07/CH01250 ._CH',             # 03
        'ED6_DT07/CH01700 ._CH',             # 04
        'ED6_DT07/CH01450 ._CH',             # 05
        'ED6_DT07/CH00050 ._CH',             # 06
        'ED6_DT07/CH00060 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02440P._CP',             # 00
        'ED6_DT06/CH20078P._CP',             # 01
        'ED6_DT07/CH01550P._CP',             # 02
        'ED6_DT07/CH01250P._CP',             # 03
        'ED6_DT07/CH01700P._CP',             # 04
        'ED6_DT07/CH01450P._CP',             # 05
        'ED6_DT07/CH00050P._CP',             # 06
        'ED6_DT07/CH00060P._CP',             # 07
    )

    DeclNpc(
        X                   = -37000,
        Z                   = -3800,
        Y                   = 145500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1D5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 115320,
        Z                   = 0,
        Y                   = 100,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 117500,
        Z                   = 0,
        Y                   = 100,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_1EA",          # 00, 0
        "Function_1_2CA",          # 01, 1
        "Function_2_2E3",          # 02, 2
        "Function_3_460",          # 03, 3
        "Function_4_537",          # 04, 4
        "Function_5_60E",          # 05, 5
        "Function_6_761",          # 06, 6
        "Function_7_8DD",          # 07, 7
        "Function_8_8F4",          # 08, 8
        "Function_9_B3F",          # 09, 9
        "Function_10_E23",         # 0A, 10
        "Function_11_106A",        # 0B, 11
        "Function_12_16B1",        # 0C, 12
        "Function_13_246C",        # 0D, 13
    )


    def Function_0_1EA(): pass

    label("Function_0_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1F8")
    OP_A3(0x3FA)
    Event(0, 11)

    label("loc_1F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_206")
    OP_A3(0x3FB)
    Event(0, 12)

    label("loc_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_218")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)

    label("loc_218")

    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 58980, -2000, 54010, 5)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 28040, 0, -7450, 270)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x0, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_271")
    SetChrPos(0x8, 29550, 0, 8860, 90)
    Jump("loc_282")

    label("loc_271")

    SetChrPos(0x8, 32860, 0, 7250, 180)

    label("loc_282")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 60760, -2000, 53780, 45)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 60590, 0, 3070, 265)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 88670, 0, -280, 81)
    Return()

    # Function_0_1EA end

    def Function_1_2CA(): pass

    label("Function_1_2CA")

    OP_10(0x0, 0x0)
    OP_22(0x7A, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_END)), "loc_2E2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E2")

    Return()

    # Function_1_2CA end

    def Function_2_2E3(): pass

    label("Function_2_2E3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_308")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_44A")

    label("loc_308")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_321")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_44A")

    label("loc_321")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_44A")

    label("loc_33A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_353")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_44A")

    label("loc_353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_44A")

    label("loc_36C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_44A")

    label("loc_385")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_44A")

    label("loc_39E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B7")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_44A")

    label("loc_3B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_44A")

    label("loc_3D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E9")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_44A")

    label("loc_3E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_402")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_44A")

    label("loc_402")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41B")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_44A")

    label("loc_41B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_434")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_44A")

    label("loc_434")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_44A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_44A")

    label("loc_45F")

    Return()

    # Function_2_2E3 end

    def Function_3_460(): pass

    label("Function_3_460")

    OP_A2(0x5CC)
    TalkBegin(0xFE)
    OP_4A(0xF, 255)

    ChrTalk(    #0
        0xF,
        (
            "#061F#4PVery well then, let's see your\x01",
            "combat orbment.\x02\x03",

            "I'll just run a quick diagnostic\x01",
            "on it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xE,
        (
            "#052F#6PUm, this isn't...\x02\x03",

            "#051FBut wow, you just light all up \x01",
            "around some new gadget. \x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xF, 255)
    TalkEnd(0xFE)
    Return()

    # Function_3_460 end

    def Function_4_537(): pass

    label("Function_4_537")

    OP_A2(0x5CC)
    TalkBegin(0xFE)
    OP_4A(0xE, 255)

    ChrTalk(    #2
        0xF,
        (
            "#061F#4PVery well then, let's see your\x01",
            "combat orbment.\x02\x03",

            "I'll just run a quick diagnostic\x01",
            "on it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xE,
        (
            "#052F#6PUm, this isn't...\x02\x03",

            "#051FBut wow, you just light all up \x01",
            "around some new gadget. \x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xE, 255)
    TalkEnd(0xFE)
    Return()

    # Function_4_537 end

    def Function_5_60E(): pass

    label("Function_5_60E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_759")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6A0")

    ChrTalk(    #4
        0xFE,
        (
            "#690FWhat? Are you that worried about\x01",
            "the container?\x02\x03",

            "#691FIt's a perfect replica, so just relax\x01",
            "and get some shut-eye.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_756")

    label("loc_6A0")

    OP_A2(0x0)

    ChrTalk(    #5
        0xFE,
        (
            "#691FSomething wrong?\x02\x03",

            "The flight to Leiston Fortress\x01",
            "should take about 30 minutes.\x02\x03",

            "Gotta get the container ready\x01",
            "for you guys, so you'd best go\x01",
            "enjoy moving while you can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_756")

    Jump("loc_75D")

    label("loc_759")

    Call(0, 13)

    label("loc_75D")

    TalkEnd(0xFE)
    Return()

    # Function_5_60E end

    def Function_6_761(): pass

    label("Function_6_761")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_END)), "loc_7A1")

    ChrTalk(    #6
        0xFE,
        "Time's finally come...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "Man, I'm nervous.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8D9")

    label("loc_7A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_861")

    ChrTalk(    #8
        0xFE,
        (
            "But if anyone else knew that the\x01",
            "professor had been captured...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "Heck, it's freaking ME out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I mean, we don't even know what\x01",
            "to do with that 'Capel' thing\x01",
            "without him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D9")

    label("loc_861")

    OP_A2(0x4)

    ChrTalk(    #11
        0xFE,
        "And now he's gone...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "The factory chief not telling us\x01",
            "sooner didn't help either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "Show a little trust!\x02",
    )

    CloseMessageWindow()

    label("loc_8D9")

    TalkEnd(0xFE)
    Return()

    # Function_6_761 end

    def Function_7_8DD(): pass

    label("Function_7_8DD")

    TalkBegin(0xFE)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #14
        0xFE,
        "Nyaa!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_8DD end

    def Function_8_8F4(): pass

    label("Function_8_8F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_END)), "loc_962")

    ChrTalk(    #15
        0xFE,
        (
            "We should be coming into visual\x01",
            "range of Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "Prepare yourselves, people.\x02",
    )

    CloseMessageWindow()
    Jump("loc_B34")

    label("loc_962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_9DC")
    TurnDirection(0xFE, 0x9, 400)

    ChrTalk(    #17
        0xFE,
        (
            "Hey, Rehmann, do something\x01",
            "about our heading!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "The wind from Lake Valleria's\x01",
            "pushing the stern.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B34")

    label("loc_9DC")

    OP_A2(0x3)
    OP_A2(0x1)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x9, 400)

    ChrTalk(    #19
        0xFE,
        (
            "Rehmann, we're being swept\x01",
            "north-northeast!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "You son of a...hurry up and get\x01",
            "us back on-course!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Every minute you play around\x01",
            "is putting Professor Russell in\x01",
            "greater danger.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #22
        0x9,
        "Just shut it, old-timer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "I can't concentrate with you\x01",
            "barking in my ear like that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B34")

    OP_8C(0xFE, 45, 400)
    TalkEnd(0xFE)
    Return()

    # Function_8_8F4 end

    def Function_9_B3F(): pass

    label("Function_9_B3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_BA5")
    TalkBegin(0xFE)

    ChrTalk(    #24
        0xFE,
        (
            "Thank you for delivering the\x01",
            "container so quickly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "O-Okay, let's get to work!\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_BA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BCF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x35E)"), scpexpr(EXPR_END)), "loc_BCF")
    Call(1, 2)
    TalkEnd(0xFE)
    Return()

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_CFE")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_END)), "loc_C20")

    ChrTalk(    #26
        0xFE,
        "There. Our decoy is in place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "Let's hope it works.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CFB")

    label("loc_C20")

    SetChrFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x31, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_C98")

    ChrTalk(    #28
        0xFE,
        "Okay, Faye, keep it here and now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Don't worry about Rudi and Brahm,\x01",
            "and just focus on work!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CF6")

    label("loc_C98")


    ChrTalk(    #30
        0xFE,
        "Okay, Faye, keep it here and now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "Put the private thoughts aside\x01",
            "and focus on work!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF6")

    ClearChrFlags(0xA, 0x10)

    label("loc_CFB")

    Jump("loc_E1F")

    label("loc_CFE")

    TalkBegin(0xFE)
    OP_A2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_END)), "loc_D51")

    ChrTalk(    #32
        0xFE,
        "There. Our decoy is in place.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "Let's hope our plan works.\x02",
    )

    CloseMessageWindow()
    Jump("loc_E1F")

    label("loc_D51")


    ChrTalk(    #34
        0xFE,
        (
            "Professor Russell abducted by\x01",
            "the Royal Army...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "This changes so many things.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "If they notice the container's fake,\x01",
            "it'll ruin the rescue and expose\x01",
            "our troops.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "I have GOT to concentrate.\x02",
    )

    CloseMessageWindow()

    label("loc_E1F")

    TalkEnd(0xFE)
    Return()

    # Function_9_B3F end

    def Function_10_E23(): pass

    label("Function_10_E23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAC, 2)), scpexpr(EXPR_END)), "loc_E82")

    ChrTalk(    #38
        0xFE,
        (
            "Man, I'm so nervous I can\x01",
            "barely fly straight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "Can't make any mistakes.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1066")

    label("loc_E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EFF")

    ChrTalk(    #40
        0xFE,
        (
            "Like I couldn't tell we were\x01",
            "caught in the wind...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "It's you that's causing me to\x01",
            "lose my focus, old man!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1066")

    label("loc_EFF")

    OP_A2(0x1)
    OP_A2(0x3)
    OP_4A(0xB, 255)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x9, 400)

    ChrTalk(    #42
        0xB,
        (
            "Rehmann, we're being swept\x01",
            "north-northeast!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xB,
        (
            "You son of a...hurry up and get\x01",
            "us back on-course!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xB,
        (
            "Every minute you play around\x01",
            "is putting Professor Russell in\x01",
            "greater danger.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0xFE,
        "Just shut it, old-timer!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I can't concentrate with you\x01",
            "barking in my ear like that.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 45, 400)
    OP_4B(0xB, 255)

    label("loc_1066")

    TalkEnd(0xFE)
    Return()

    # Function_10_E23 end

    def Function_11_106A(): pass

    label("Function_11_106A")

    ClearMapFlags(0x2000000)
    EventBegin(0x0)
    OP_6D(29240, 0, 7250, 0)
    OP_67(0, 10730, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 28810, 0, 8640, 90)
    SetChrPos(0x101, 29240, 0, 7250, 90)
    SetChrPos(0x102, 28260, 0, 6830, 90)
    SetChrPos(0x106, 29420, 0, 6290, 45)
    SetChrPos(0x107, 28480, 0, 6070, 45)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #47
        0x8,
        (
            "#691FThis is the container where\x01",
            "you'll all be hiding.\x02\x03",

            "I hope all of you are REAL close\x01",
            "friends. It's going to be a tight\x01",
            "squeeze for four people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#501F#6PReally? It looks big enough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        (
            "#693FIt's only half as big inside as\x01",
            "it looks. Gotta have cargo in\x01",
            "there for camouflage's sake.\x02\x03",

            "Ha ha ha... Think of yourselves\x01",
            "like the filling for a doughnut.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#007F#6PThat's...not encouraging.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#010FWe'll be fine. It's all a matter of\x01",
            "how you approach the situation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x106,
        (
            "#053FIt'll get the job done, but\x01",
            "I wouldn't want to take a\x01",
            "vacation in there.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #53
        0x106,
        (
            "#050FOh, right. Say, man...you got\x01",
            "any orbment facilities here\x01",
            "or anything?\x02\x03",

            "I'm a little off-kilter, so\x01",
            "I want to change things up.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13DF():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13DF)

    def lambda_13ED():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_13ED)

    def lambda_13FB():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_13FB)
    TurnDirection(0x8, 0x106, 400)

    ChrTalk(    #54
        0x8,
        (
            "#691FWe have an on-board factory,\x01",
            "of sorts. You're welcome to\x01",
            "make use of it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(    #55
        0x107,
        (
            "#560FI'll go, too. My orbment could\x01",
            "use a little tune-up after all\x01",
            "it's been through!\x02\x03",

            "This way, Agate.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x107, 400)

    def lambda_14DE():

        label("loc_14DE")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_14DE")

    QueueWorkItem2(0x106, 1, lambda_14DE)

    ChrTalk(    #56
        0x106,
        "#052FUh, all right.\x02",
    )

    CloseMessageWindow()

    def lambda_1508():

        label("loc_1508")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_1508")

    QueueWorkItem2(0x101, 1, lambda_1508)

    def lambda_1519():

        label("loc_1519")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_1519")

    QueueWorkItem2(0x102, 1, lambda_1519)
    OP_8E(0x107, 0x7580, 0x0, 0xEB0, 0xBB8, 0x0)

    def lambda_153E():
        OP_8E(0xFE, 0x751C, 0x0, 0xFFFFE912, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_153E)
    OP_8E(0x106, 0x751C, 0x0, 0xD98, 0xBB8, 0x0)

    def lambda_156D():
        OP_8E(0xFE, 0x751C, 0x0, 0xFFFFE912, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_156D)
    Sleep(1000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_1595():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1595)

    def lambda_15A3():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15A3)

    ChrTalk(    #57
        0x8,
        (
            "#691FLeiston Fortress is a thirty-\x01",
            "minute flight from here.\x02\x03",

            "It won't be too comfortable in\x01",
            "that container, so you oughta\x01",
            "get some rest while you can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#006F#6PSure thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        "#010FThank you.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x106, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrPos(0x106, 29240, 0, 7250, 0)
    SetChrPos(0x107, 29240, 0, 7250, 0)
    OP_4B(0x8, 255)
    OP_A2(0x561)
    EventEnd(0x0)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x6, 0xFF)
    Return()

    # Function_11_106A end

    def Function_12_16B1(): pass

    label("Function_12_16B1")

    EventBegin(0x0)
    AddParty(0x5, 0xFF)
    AddParty(0x6, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    OP_6D(116590, 0, 5710, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrPos(0x106, 115790, 0, 4200, 0)
    SetChrPos(0x107, 115590, 0, 5610, 90)
    OP_89(0x101, 113320, -2000, 7580, 0)
    OP_89(0x102, 113320, -2000, 7580, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #60
        0x107,
        (
            "#061F#5POof. Okay, this ought to do it.\x02\x03",

            "The metal part of the slot\x01",
            "connectors got loose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x106,
        (
            "#053FAnyone ever tell you\x01",
            "you're a busybody?\x02\x03",

            "If I wanted mods that simple,\x01",
            "I could do them myself.\x02\x03",

            "#051FBut, hey...thanks.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x106, 400)

    ChrTalk(    #62
        0x107,
        (
            "#061F#5PHa ha... You're welcome.\x02\x03",

            "#063FOh... By the way, how\x01",
            "are you feeling?\x02\x03",

            "I hope you don't feel all yucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x106,
        (
            "#053FYeah, I'm fine. You really\x01",
            "don't have to worry.\x02\x03",

            "#050FIf you really want to worry about\x01",
            "someone, worry about yourself.\x02\x03",

            "Now's the time to back out,\x01",
            "if you still want to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x107,
        "#065F#5PI...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x106,
        (
            "#552FDon't get me wrong. I ain't\x01",
            "telling you not to come.\x02\x03",

            "It's just...aren't you scared?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x107,
        "#064F#5PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x106,
        (
            "#050FEven though we're doing this\x01",
            "for the old man, we're still\x01",
            "breaking into a military base.\x02\x03",

            "Most kids would piss themselves\x01",
            "at the idea of doing something\x01",
            "this major.\x02\x03",

            "So, how come you're all\x01",
            "carefree about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x107,
        (
            "#562F#5PUm...\x02\x03",

            "Well, I'm really scared\x01",
            "out of my mind...\x02\x03",

            "#560F...but I have Joshua \x01",
            "and Estelle with me.\x02\x03",

            "And you're here, too...\x02\x03",

            "Not being alone makes it easier,\x01",
            "so I don't have to think about\x01",
            "how scared I am.\x02\x03",

            "#067FHee hee...\x01",
            "Maybe that's a little stupid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x106,
        (
            "#052F...\x02\x03",

            "#051FHa ha.\x01",
            "A 'little'? Try 'incredibly.'\x02\x03",

            "Anyway, worrying is just\x01",
            "a waste of time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x107,
        (
            "#067F#5PHee hee... Sorry.\x02\x03",

            "#060F...\x02\x03",

            "#560FUmm...\x01",
            "Can I ask you something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x106,
        "#052FWhere'd this come from?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x107,
        (
            "#060F#5PI, um...\x01",
            "I was just wondering...\x02\x03",

            "Who's Mischa?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #73
        0x106,
        "#057F...How do you know that name?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x107,
        (
            "#065F#5PUh, I, um...\x02\x03",

            "You called me that when\x01",
            "you were poisoned...\x02\x03",

            "#063F...I'm sorry. I shouldn't\x01",
            "have said anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x106,
        (
            "#053FNah...\x01",
            "It's nothing I'm ashamed of.\x02\x03",

            "#050FMischa's my kid sister.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x107,
        (
            "#064F#5POh, wow.\x01",
            "You're a big brother?\x02\x03",

            "#061FHow old is she?\x02\x03",

            "Older than me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x106,
        (
            "#552FWell...sort of.\x02\x03",

            "#051FI guess she'd be around your age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x107,
        (
            "#064F#5P...?\x02\x03",

            "I guess you haven't seen\x01",
            "her in a long time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x106,
        (
            "#051F...Work keeps me busy.\x02\x03",

            "I only go home about once a year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x107,
        (
            "#063F#5POh...\x02\x03",

            "Poor Mischa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x106,
        "#055FWhat's that supposed to mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x107,
        (
            "#067F#5PI just think that if I had a\x01",
            "big brother, I'd want to be\x01",
            "with him all the time.\x02\x03",

            "#062FI bet she feels the same way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x106,
        (
            "#055F...R-Really?\x02\x03",

            "#552FWell, you might be right.\x02\x03",

            "If I was more reliable,\x01",
            "maybe I'd be with her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x107,
        "#064F#5PHuh...?\x02",
    )

    CloseMessageWindow()
    OP_22(0xA6, 0x0, 0x64)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Crew Member's Voice")

    AnonymousTalk(    #85
        (
            "\x07\x05We'll be landing at Leiston\x01",
            "Fortress soon.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #86
        "\x07\x05All bracers to the cargo hold.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(    #87
        0x106,
        "#052FLooks like it's time.\x02",
    )

    CloseMessageWindow()
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)

    def lambda_211F():

        label("loc_211F")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_211F")

    QueueWorkItem2(0x101, 1, lambda_211F)

    def lambda_2130():

        label("loc_2130")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_2130")

    QueueWorkItem2(0x102, 1, lambda_2130)

    def lambda_2141():
        OP_6D(114220, 0, 4820, 1500)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_2141)

    def lambda_2159():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2159)

    def lambda_216B():
        OP_8E(0xFE, 0x1BB48, 0x0, 0xD8E, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_216B)

    def lambda_2186():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2186)
    OP_8E(0x102, 0x1B832, 0x0, 0x10A4, 0x7D0, 0x0)

    def lambda_21AC():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_21AC)
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #88
        0x101,
        "#501FOh, here you are.\x02",
    )

    CloseMessageWindow()

    def lambda_21DD():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_21DD)

    def lambda_21EB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_21EB)

    def lambda_21F9():
        OP_8E(0xFE, 0x1BFEE, 0x0, 0xD2A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_21F9)

    def lambda_2214():
        OP_8E(0xFE, 0x1BD00, 0x0, 0xF3C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_2214)

    def lambda_222F():

        label("loc_222F")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_222F")

    QueueWorkItem2(0x102, 1, lambda_222F)
    OP_6D(116590, 0, 5710, 1500)

    ChrTalk(    #89
        0x107,
        "#560F#5PHi, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#006F#2PDidn't you hear the announcement?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        "#010FWe'll be arriving soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x106,
        "#053F#2PYeah, I'm all done getting ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#000F#2PDid you get everything\x01",
            "you need, sweetie?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x107,
        (
            "#060F#5PYup! You bet'cha. I even\x01",
            "tested the timing.\x02\x03",

            "I think I should be able to\x01",
            "handle the bio-sensor, so\x01",
            "leave that to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#006F#2PWell, now.\x01",
            "That's encouraging.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        "#010FWe're counting on you, Tita.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x107,
        "#061F#5PRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x106,
        (
            "#051F#2PWhy don't we head down\x01",
            "to the cargo hold?\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    OP_21()
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1E()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_A2(0x562)
    OP_28(0x44, 0x1, 0x1)
    SetMapFlags(0x2000000)
    SetMapFlags(0x800)
    EventEnd(0x0)
    Return()

    # Function_12_16B1 end

    def Function_13_246C(): pass

    label("Function_13_246C")

    EventBegin(0x0)
    ClearMapFlags(0x800)
    Fade(1000)
    OP_6D(33030, 0, 6430, 0)
    OP_67(0, 9490, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 32860, 0, 7250, 180)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x106, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrPos(0x102, 32450, 0, 5900, 0)
    SetChrPos(0x101, 33410, 0, 5850, 0)
    SetChrPos(0x106, 32200, 0, 4810, 0)
    SetChrPos(0x107, 33070, 0, 4590, 0)

    def lambda_252E():

        label("loc_252E")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_252E")

    QueueWorkItem2(0x102, 2, lambda_252E)

    def lambda_253F():

        label("loc_253F")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_253F")

    QueueWorkItem2(0x101, 2, lambda_253F)

    def lambda_2550():

        label("loc_2550")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2550")

    QueueWorkItem2(0x107, 2, lambda_2550)

    def lambda_2561():

        label("loc_2561")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2561")

    QueueWorkItem2(0x106, 2, lambda_2561)
    OP_4A(0x8, 255)
    OP_0D()

    ChrTalk(    #99
        0x8,
        "#691FGood. You're here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#006FLooks like you've got\x01",
            "everything set up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x8,
        (
            "#691FI'm all done with disguising\x01",
            "the container.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_25FD():
        OP_6D(31660, 0, 8900, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_25FD)
    OP_8E(0x8, 0x7F25, 0x0, 0x1B9E, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(500)
    OP_22(0xA8, 0x0, 0x64)
    OP_70(0x3, 0xB4)
    OP_73(0x3)

    ChrTalk(    #102
        0x8,
        (
            "#691FIf you just open it up, all you'll \x01",
            "see are these plates that are\x01",
            "used for fixing ship hulls.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x7F3A, 0x0, 0x22F6, 0x7D0, 0x0)
    OP_22(0xA9, 0x0, 0x64)
    OP_70(0x4, 0xB4)
    OP_73(0x4)

    ChrTalk(    #103
        0x8,
        (
            "#693FBut there's another door on \x01",
            "this side, and you can't tell\x01",
            "it's there when it's closed.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2731():
        OP_6D(33030, 0, 6430, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2731)
    OP_8E(0x8, 0x82BE, 0x0, 0x1BF8, 0x7D0, 0x0)
    TurnDirection(0x8, 0x101, 400)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #104
        0x101,
        "#004FHeeeey, that's pretty cool.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#010FThis ought to fool the\x01",
            "bio-sensor and allow us\x01",
            "to sneak in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "#690FSo, all that's left is\x01",
            "for you to pile in.\x02\x03",

            "Are you folks ready for this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#006FOf course we are!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x106,
        "#051FI was born ready.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x8,
        (
            "#691FOkay, then you'll need\x01",
            "to get in one at a time.\x02\x03",

            "Once you're all inside, I'll\x01",
            "close the hidden door.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x102,
        "#010FUnderstood. I'll go first.\x02",
    )

    CloseMessageWindow()

    def lambda_28F5():
        OP_6D(31660, 0, 8900, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_28F5)

    def lambda_290D():

        label("loc_290D")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_290D")

    QueueWorkItem2(0x101, 2, lambda_290D)

    def lambda_291E():

        label("loc_291E")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_291E")

    QueueWorkItem2(0x107, 2, lambda_291E)

    def lambda_292F():

        label("loc_292F")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_292F")

    QueueWorkItem2(0x106, 2, lambda_292F)

    def lambda_2940():

        label("loc_2940")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_2940")

    QueueWorkItem2(0x8, 2, lambda_2940)
    OP_8E(0x102, 0x7FB1, 0x0, 0x1C0C, 0x7D0, 0x0)
    OP_8E(0x102, 0x7F25, 0x0, 0x23BE, 0x7D0, 0x0)
    OP_8E(0x102, 0x7986, 0x0, 0x23BE, 0x3E8, 0x0)
    OP_8E(0x101, 0x7FB1, 0x0, 0x1C0C, 0x7D0, 0x0)

    ChrTalk(    #111
        0x101,
        (
            "#007FMan, this is cramped. If you\x01",
            "don't get in exactly right...\x02\x03",

            "#503F...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29F0():

        label("loc_29F0")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_29F0")

    QueueWorkItem2(0x107, 2, lambda_29F0)

    def lambda_2A01():

        label("loc_2A01")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2A01")

    QueueWorkItem2(0x106, 2, lambda_2A01)

    def lambda_2A12():

        label("loc_2A12")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2A12")

    QueueWorkItem2(0x8, 2, lambda_2A12)

    ChrTalk(    #112
        0x102,
        (
            "#014F...?\x02\x03",

            "Estelle? Are you okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#504FI-I'm fine!\x02",
    )

    CloseMessageWindow()

    def lambda_2A60():
        OP_6B(2300, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A60)

    def lambda_2A70():
        OP_6D(31110, 0, 9150, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2A70)
    OP_8E(0x101, 0x7F25, 0x0, 0x23BE, 0x7D0, 0x0)
    OP_8E(0x101, 0x7986, 0x0, 0x23BE, 0x3E8, 0x0)

    ChrTalk(    #114
        0x101,
        "#505F#2PThere we go...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        "#015F#1PTurn your head this way.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#006F#2POkay...\x02\x03",

            "#004F...Oh.\x02\x03",

            "#503FU-Umm, Joshua...\x02\x03",

            "I don't know about\x01",
            "holding this pose...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        (
            "#018F#1PW-We've just got to deal\x01",
            "with it.\x02\x03",

            "Otherwise, we'll never get\x01",
            "all four of us in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#503F#2PR-Right...\x02\x03",

            "Yeah, we have to do this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        (
            "#015F#1PAhem!\x02\x03",

            "#010FNext up is Tita.\x01",
            "Agate, you're in the back.\x02\x03",

            "We should all fit if we\x01",
            "do it that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x107,
        (
            "#061F#1POkay.\x01",
            "In I go!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2C74():

        label("loc_2C74")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_2C74")

    QueueWorkItem2(0x106, 2, lambda_2C74)

    def lambda_2C85():

        label("loc_2C85")

        TurnDirection(0xFE, 0x107, 0)
        OP_48()
        Jump("loc_2C85")

    QueueWorkItem2(0x8, 2, lambda_2C85)
    OP_8E(0x107, 0x7FB1, 0x0, 0x1C0C, 0x7D0, 0x0)
    OP_8E(0x107, 0x7F25, 0x0, 0x23BE, 0x7D0, 0x0)
    OP_8E(0x107, 0x7986, 0x0, 0x23BE, 0x3E8, 0x0)

    ChrTalk(    #121
        0x107,
        (
            "#062F#2POof...\x01",
            "Sorry, Estelle...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#001F#1PAww... Tita, you're all\x01",
            "warm and snuggly.\x02\x03",

            "Mmmm, and you even smell kinda\x01",
            "sweet, like fresh milk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x107,
        (
            "#065F#2PH-Hey...\x01",
            "Don't hug so tight...\x02\x03",

            "I kinda can't breathe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#507F#1PHeh heh heh...\x01",
            "It's not that bad, is it?\x02\x03",

            "#502FHmmmm... My, what squishable\x01",
            "cheeks you have!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x107,
        "#067F#2PEeep!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x102,
        (
            "#018F#3PEstelle...\x01",
            "Quit playing around.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x106, 0x7FB1, 0x0, 0x1C0C, 0x7D0, 0x0)

    ChrTalk(    #127
        0x106,
        (
            "#551FOkay, now I'm getting nervous.\x02\x03",

            "#054FHey, kids. Make a little room.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2EB7():

        label("loc_2EB7")

        TurnDirection(0xFE, 0x106, 0)
        OP_48()
        Jump("loc_2EB7")

    QueueWorkItem2(0x8, 2, lambda_2EB7)
    OP_8E(0x106, 0x7F25, 0x0, 0x23BE, 0x7D0, 0x0)
    OP_8E(0x106, 0x7986, 0x0, 0x23BE, 0x3E8, 0x0)

    ChrTalk(    #128
        0x107,
        "#065F#1POof...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x106,
        (
            "#052F#2PThere...\x01",
            "Is it too cramped?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x107,
        (
            "#560F#1PN-No... I'm okay.\x02\x03",

            "I can hold out...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x106,
        (
            "#050F#2PDon't be stubborn. If it's too\x01",
            "uncomfortable, just say so.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x107,
        "#067F#1PO-Okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x106,
        (
            "#051F#2POkay, man.\x01",
            "I think we're set.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        "#691FGot'cha. I'll close the door.\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_8E(0x8, 0x7F3A, 0x0, 0x22F6, 0x7D0, 0x0)
    Sleep(500)

    def lambda_302C():
        OP_6B(2600, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_302C)
    OP_22(0xA9, 0x0, 0x64)
    OP_6F(0x4, 180)
    OP_70(0x4, 0x0)
    OP_73(0x4)

    ChrTalk(    #135
        0x8,
        (
            "#691FI'll make sure we unload this\x01",
            "container ASAP after we land.\x01",
            "And from there...it's all on you.\x02\x03",

            "Just be patient and stay calm.\x01",
            "Good luck, kids.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x7F25, 0x0, 0x1B9E, 0x7D0, 0x0)
    OP_8C(0x8, 270, 400)
    Sleep(500)
    OP_6F(0x3, 180)
    OP_70(0x3, 0x0)
    Sleep(600)
    OP_22(0xA8, 0x0, 0x64)
    OP_73(0x3)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_20(0x5DC)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    ClearMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C3102   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_246C end

    SaveToFile()

Try(main)
