from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0123   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0123.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0123   ._SN',
            'ED6_DT21/T0123_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Aina',                                 # 9
        'Scherazard',                           # 10
        'Agate',                                # 11
        'Olivier',                              # 12
        'Kloe',                                 # 13
        'Tita',                                 # 14
        'Zin',                                  # 15
        'Mayor Klaus',                          # 16
        'Rinon',                                # 17
        'Bloom',                                # 18
        'Kitty',                                # 19
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
        'ED6_DT07/CH02560 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH00050 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00060 ._CH',             # 05
        'ED6_DT07/CH00070 ._CH',             # 06
        'ED6_DT07/CH00023 ._CH',             # 07
        'ED6_DT07/CH00053 ._CH',             # 08
        'ED6_DT07/CH00033 ._CH',             # 09
        'ED6_DT07/CH00073 ._CH',             # 0A
        'ED6_DT07/CH02350 ._CH',             # 0B
        'ED6_DT07/CH01040 ._CH',             # 0C
        'ED6_DT07/CH01010 ._CH',             # 0D
        'ED6_DT07/CH01770 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH02560P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH00050P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00060P._CP',             # 05
        'ED6_DT07/CH00070P._CP',             # 06
        'ED6_DT07/CH00023P._CP',             # 07
        'ED6_DT07/CH00053P._CP',             # 08
        'ED6_DT07/CH00033P._CP',             # 09
        'ED6_DT07/CH00073P._CP',             # 0A
        'ED6_DT07/CH02350P._CP',             # 0B
        'ED6_DT07/CH01040P._CP',             # 0C
        'ED6_DT07/CH01010P._CP',             # 0D
        'ED6_DT07/CH01770P._CP',             # 0E
    )

    DeclNpc(
        X                   = 750,
        Z                   = 0,
        Y                   = 118600,
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3800,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 47500,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 46300,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )


    DeclActor(
        TriggerX            = 1271,
        TriggerZ            = 0,
        TriggerY            = 116402,
        TriggerRange        = 800,
        ActorX              = 750,
        ActorZ              = 1500,
        ActorY              = 118600,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3810,
        TriggerZ            = 0,
        TriggerY            = 1080,
        TriggerRange        = 800,
        ActorX              = 3800,
        ActorZ              = 1500,
        ActorY              = 2000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4900,
        TriggerZ            = 0,
        TriggerY            = 112600,
        TriggerRange        = 1400,
        ActorX              = 4900,
        ActorZ              = 2000,
        ActorY              = 112600,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2EE",          # 00, 0
        "Function_1_2EF",          # 01, 1
        "Function_2_3D6",          # 02, 2
        "Function_3_553",          # 03, 3
        "Function_4_69F",          # 04, 4
        "Function_5_6A4",          # 05, 5
        "Function_6_A44",          # 06, 6
        "Function_7_10EC",         # 07, 7
        "Function_8_12AB",         # 08, 8
        "Function_9_14E6",         # 09, 9
        "Function_10_1706",        # 0A, 10
        "Function_11_19A4",        # 0B, 11
        "Function_12_1ACF",        # 0C, 12
        "Function_13_1D02",        # 0D, 13
        "Function_14_1ED6",        # 0E, 14
        "Function_15_1FE3",        # 0F, 15
        "Function_16_39D2",        # 10, 16
        "Function_17_3B04",        # 11, 17
        "Function_18_3B55",        # 12, 18
        "Function_19_3BDE",        # 13, 19
    )


    def Function_0_2EE(): pass

    label("Function_0_2EE")

    Return()

    # Function_0_2EE end

    def Function_1_2EF(): pass

    label("Function_1_2EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_335")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)

    label("loc_335")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_362")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 9)
    SetChrPos(0xB, 1060, 200, 69820, 360)

    label("loc_362")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_385")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1940, 0, 74490, 360)

    label("loc_385")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A8")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)

    label("loc_3A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D5")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)

    label("loc_3D5")

    Return()

    # Function_1_2EF end

    def Function_2_3D6(): pass

    label("Function_2_3D6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FB")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_53D")

    label("loc_3FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_414")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_53D")

    label("loc_414")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42D")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_53D")

    label("loc_42D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_446")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_53D")

    label("loc_446")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45F")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_53D")

    label("loc_45F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_478")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_53D")

    label("loc_478")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_491")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_53D")

    label("loc_491")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AA")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_53D")

    label("loc_4AA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C3")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_53D")

    label("loc_4C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DC")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_53D")

    label("loc_4DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F5")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_53D")

    label("loc_4F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50E")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_53D")

    label("loc_50E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_527")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_53D")

    label("loc_527")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53D")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_53D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_552")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_53D")

    label("loc_552")

    Return()

    # Function_2_3D6 end

    def Function_3_553(): pass

    label("Function_3_553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_572")
    Call(0, 15)
    Jump("loc_69E")

    label("loc_572")

    TalkBegin(0x8)
    Call(6, 5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_689")
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x3)"), scpexpr(EXPR_END)), "loc_5FB")

    ChrTalk(    #0
        0x8,
        (
            "#740FGood work out there, everyone.\x02\x03",

            "If you complete any other jobs,\x01",
            "make sure to report to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_680")

    label("loc_5FB")


    ChrTalk(    #1
        0x8,
        (
            "#740FLooks like you don't have any\x01",
            "work to report on at the moment.\x02\x03",

            "If you complete any other jobs,\x01",
            "make sure to report to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_680")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_689")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69A")
    TalkEnd(0x8)
    Return()

    label("loc_69A")

    Call(0, 5)

    label("loc_69E")

    Return()

    # Function_3_553 end

    def Function_4_69F(): pass

    label("Function_4_69F")

    Call(0, 6)
    Return()

    # Function_4_69F end

    def Function_5_6A4(): pass

    label("Function_5_6A4")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_71B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",             # 0
            "Report\x01",           # 1
            "Call Allies\x01",      # 2
            "End\x01",              # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jump("loc_71F")

    label("loc_71B")

    Call(6, 5)

    label("loc_71F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B0")
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B3")
    OP_28(0xC3, 0x4, 0x20)
    OP_A9(0x3)

    ChrTalk(    #2
        0x8,
        (
            "#740FGood work out there, everyone.\x02\x03",

            "If you complete any other jobs,\x01",
            "make sure to report to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A7")

    label("loc_7B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x3)"), scpexpr(EXPR_END)), "loc_822")

    ChrTalk(    #3
        0x8,
        (
            "#740FGood work out there, everyone.\x02\x03",

            "If you complete any other jobs,\x01",
            "make sure to report to me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A7")

    label("loc_822")


    ChrTalk(    #4
        0x8,
        (
            "#740FLooks like you don't have any\x01",
            "work to report on at the moment.\x02\x03",

            "If you complete any other jobs,\x01",
            "make sure to report to me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A7")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_8B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8C1")
    TalkEnd(0x8)
    Return()

    label("loc_8C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8E0")
    Call(0, 15)
    Jump("loc_A43")

    label("loc_8E0")

    OP_A2(0x1884)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_979")

    ChrTalk(    #5
        0x8,
        (
            "#740FBest of luck on the coma investigation.\x02\x03",

            "We can't say for sure what's going on,\x01",
            "so be sure to proceed very carefully on\x01",
            "this one.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A40")

    label("loc_979")


    ChrTalk(    #6
        0x8,
        (
            "#740FMayor Klaus has asked you all to\x01",
            "start investigating the coma incidents.\x02\x03",

            "The paperwork's just been processed,\x01",
            "so you guys have officially been put on\x01",
            "the case.\x02\x03",

            "Best of luck out there.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A40")

    TalkEnd(0x8)

    label("loc_A43")

    Return()

    # Function_5_6A4 end

    def Function_6_A44(): pass

    label("Function_6_A44")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 5)), scpexpr(EXPR_END)), "loc_A79")
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A68")
    OP_A9(0x2)
    TalkEnd(0x10)
    Return()

    label("loc_A68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A79")
    TalkEnd(0x10)
    Return()

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_10E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 5)), scpexpr(EXPR_END)), "loc_E14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B72")

    ChrTalk(    #7
        0x10,
        (
            "The girl my mother brought over\x01",
            "said she'll help out around the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "No doubt it's another one of her \x01",
            "schemes to find me a wife!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "*siiigh* I can't take all this pressure...\x01",
            "How do I turn her down...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D5B")

    label("loc_B72")


    ChrTalk(    #10
        0x10,
        (
            "You guys look like you're working\x01",
            "hard as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10,
        (
            "I know it's tough being a bracer,\x01",
            "but right now I'd pick being a bracer\x01",
            "over everything I've been dealing with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "See, this girl my mother brought over\x01",
            "said she'll help out around the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "I'd normally be happy for the extra hand,\x01",
            "but you know how my mother is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "No doubt that this is another one of her \x01",
            "schemes to find me a wife!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "*siiigh* I can't take all this pressure...\x01",
            "I'm not ready to get married yet!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_D5B")

    Jump("loc_E11")

    label("loc_D5E")


    ChrTalk(    #16
        0x10,
        (
            "if you're ever short on equipment\x01",
            "or anything, feel free to drop by the\x01",
            "store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        "We're gonna be open pretty late tonight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "All right, keep up the good work,\x01",
            "you guys.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E11")

    Jump("loc_10E8")

    label("loc_E14")

    OP_62(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x10, 0x101, 0)
    Sleep(400)

    ChrTalk(    #19
        0x10,
        "Whoa, Estelle! About time!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        (
            "#1008FHaha, it's been a while, Rinon.\x02\x03",

            "Sorry for not stopping by sooner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        "No, no, not at all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "You sure picked a bad time to come\x01",
            "back, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        "Are you out on patrol?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1015FPretty much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x103,
        (
            "#020FThe guild is stepping up its presence\x01",
            "so we can be ready for anything.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x103, 400)

    ChrTalk(    #26
        0x10,
        "Man, sounds rough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "Makes it easier for the rest of us\x01",
            "to sleep at night, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10,
        (
            "By the way, if you're ever short on\x01",
            "equipment or anything, feel free to\x01",
            "drop by the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "We're gonna be open pretty late tonight.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x103,
        "#525FYou never know! Thanks, Rinon. ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1006FYeah, thanks. Catch you later.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #32
        0x10,
        "Good luck with the patrols!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1885)
    OP_A2(0x2)

    label("loc_10E8")

    TalkEnd(0x10)
    Return()

    # Function_6_A44 end

    def Function_7_10EC(): pass

    label("Function_7_10EC")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_12A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_118E")

    ChrTalk(    #33
        0xFE,
        (
            "Kitty's helping around the store\x01",
            "starting tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Rinon's been fidgety ever since,\x01",
            "but I swear, I had nary a thing\x01",
            "to do with it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A7")

    label("loc_118E")


    ChrTalk(    #35
        0xFE,
        "Kitty was the one who insisted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "Kitty's helping around the store\x01",
            "starting tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Rinon's been so fidgety ever since\x01",
            "I told him about her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "He probably thinks I put her up to it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Try to arrange one or two marriages\x01",
            "and no one trusts you anymore. Hmph!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_12A7")

    TalkEnd(0x11)
    Return()

    # Function_7_10EC end

    def Function_8_12AB(): pass

    label("Function_8_12AB")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_14E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1375")

    ChrTalk(    #40
        0xFE,
        (
            "I kept asking and asking until they finally\x01",
            "said I could work in the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "They're taking care of me, so it's only\x01",
            "right that I do whatever I can to help them\x01",
            "out, right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E2")

    label("loc_1375")


    ChrTalk(    #42
        0xFE,
        (
            "I kept asking and asking until they finally\x01",
            "said I could work in the store.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "They're taking care of me, so it's only\x01",
            "right that I do whatever I can to help them\x01",
            "out, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Ms. Bloom's son doesn't seem all that\x01",
            "jazzed to have me around, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Maybe he's really uncomfortable having\x01",
            "some stranger suddenly coming in to work\x01",
            "out of nowhere...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_14E2")

    TalkEnd(0x12)
    Return()

    # Function_8_12AB end

    def Function_9_14E6(): pass

    label("Function_9_14E6")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1576")
    Jump("loc_15B8")

    label("loc_1576")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1592")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15B8")

    label("loc_1592")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15AE")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15B8")

    label("loc_15AE")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15B8")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    ChrTalk(    #46
        0xA,
        "#050FHey, how's the investigation goin'?\x02",
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
            "Change Party\x01",      # 0
            "End\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1663"),
        (1, "loc_168A"),
        (SWITCH_DEFAULT, "loc_16FD"),
    )


    label("loc_1663")


    ChrTalk(    #47
        0xA,
        "#051FYeah, yeah, I got it.\x02",
    )

    CloseMessageWindow()
    Call(0, 14)
    Jump("loc_16FD")

    label("loc_168A")


    ChrTalk(    #48
        0xA,
        (
            "#052FWhat, changed your mind?\x02\x03",

            "#050FWell, if you ever need somebody to\x01",
            "swing a sword around, gimme a call.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16FD")

    label("loc_16FD")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    # Function_9_14E6 end

    def Function_10_1706(): pass

    label("Function_10_1706")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1796")
    Jump("loc_17D8")

    label("loc_1796")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_17B2")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17D8")

    label("loc_17B2")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17CE")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_17D8")

    label("loc_17CE")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17D8")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    ChrTalk(    #49
        0xB,
        (
            "#034FMy, oh, my... What a terrible night.\x02\x03",

            "#030FIf you wish, perhaps I should play\x01",
            "a song to lighten the mood?\x02",
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
            "Change Party\x01",      # 0
            "End\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_18C9"),
        (1, "loc_1930"),
        (SWITCH_DEFAULT, "loc_199B"),
    )


    label("loc_18C9")


    ChrTalk(    #50
        0xB,
        (
            "#030FAh, of course!\x02\x03",

            "You need the power of my genius.\x01",
            "Not to worry; I understand entirely.\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 14)
    Jump("loc_199B")

    label("loc_1930")


    ChrTalk(    #51
        0xB,
        (
            "#030FOh? Changed your mind?\x02\x03",

            "Well, should you ever long for my\x01",
            "dulcet tones, simply give the word.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_199B")

    label("loc_199B")

    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    # Function_10_1706 end

    def Function_11_19A4(): pass

    label("Function_11_19A4")

    TalkBegin(0xC)

    ChrTalk(    #52
        0xC,
        (
            "#043FOh, hey, guys.\x02\x03",

            "Anything I can help with?\x02",
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
            "Change Party\x01",      # 0
            "End\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A33"),
        (1, "loc_1A64"),
        (SWITCH_DEFAULT, "loc_1ACB"),
    )


    label("loc_1A33")


    ChrTalk(    #53
        0xC,
        "#042FI'd be more than happy to help.\x02",
    )

    CloseMessageWindow()
    Call(0, 14)
    Jump("loc_1ACB")

    label("loc_1A64")


    ChrTalk(    #54
        0xC,
        (
            "#049FThe fog outside is terrible...\x02\x03",

            "I hope it doesn't spread any further\x01",
            "than it already has.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ACB")

    label("loc_1ACB")

    TalkEnd(0xC)
    Return()

    # Function_11_19A4 end

    def Function_12_1ACF(): pass

    label("Function_12_1ACF")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0F")

    ChrTalk(    #55
        0xD,
        (
            "#560FOh, hi, Agate!\x02\x03",

            "Is everything okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B72")

    label("loc_1B0F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B49")

    ChrTalk(    #56
        0x107,
        "#060FHi, Estelle! What's up?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B72")

    label("loc_1B49")


    ChrTalk(    #57
        0x107,
        (
            "#060FHi, guys!\x02\x03",

            "Is everything okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B72")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Change Party\x01",      # 0
            "End\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BCA"),
        (1, "loc_1C33"),
        (SWITCH_DEFAULT, "loc_1CFE"),
    )


    label("loc_1BCA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C07")

    ChrTalk(    #58
        0x107,
        "#060FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C2C")

    label("loc_1C07")


    ChrTalk(    #59
        0x107,
        "#560FYeah, I can come with you.\x02",
    )

    CloseMessageWindow()

    label("loc_1C2C")

    Call(0, 14)
    Jump("loc_1CFE")

    label("loc_1C33")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1CA3")

    ChrTalk(    #60
        0x107,
        (
            "#064FHuh? Are you sure?\x02\x03",

            "#060FWell, I'll be here. Just call for\x01",
            "me if you need me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CFB")

    label("loc_1CA3")


    ChrTalk(    #61
        0x107,
        (
            "#064FHuh? Are you sure?\x02\x03",

            "#060FWell, I'll be here. Just call for\x01",
            "me if you need me!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CFB")

    Jump("loc_1CFE")

    label("loc_1CFE")

    TalkEnd(0xD)
    Return()

    # Function_12_1ACF end

    def Function_13_1D02(): pass

    label("Function_13_1D02")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D92")
    Jump("loc_1DD4")

    label("loc_1D92")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1DAE")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DD4")

    label("loc_1DAE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1DCA")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DD4")

    label("loc_1DCA")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DD4")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #62
        0xE,
        "#072FHey, how's it going?\x02",
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
            "Change Party\x01",      # 0
            "End\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E70"),
        (1, "loc_1EA3"),
        (SWITCH_DEFAULT, "loc_1ECD"),
    )


    label("loc_1E70")


    ChrTalk(    #63
        0xE,
        "#072FNeed me to sub in, huh? I'm game!\x02",
    )

    CloseMessageWindow()
    Call(0, 14)
    Jump("loc_1ECD")

    label("loc_1EA3")


    ChrTalk(    #64
        0xE,
        "#072FI'll be here if you need me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1ECD")

    label("loc_1ECD")

    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Return()

    # Function_13_1D02 end

    def Function_14_1ED6(): pass

    label("Function_14_1ED6")

    OP_C9(0x1, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F41")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)

    label("loc_1F41")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F6E")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrChipByIndex(0xB, 9)
    SetChrPos(0xB, 1060, 200, 69820, 360)

    label("loc_1F6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F91")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1940, 0, 74490, 360)

    label("loc_1F91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FB4")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)

    label("loc_1FB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FE1")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)

    label("loc_1FE1")

    OP_0D()
    Return()

    # Function_14_1ED6 end

    def Function_15_1FE3(): pass

    label("Function_15_1FE3")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2007")
    Call(0, 18)
    FadeToBright(0, 0)
    Call(0, 19)

    label("loc_2007")

    Fade(1000)
    OP_6D(370, 0, 117930, 0)
    OP_67(0, 6810, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 640, 0, 116600, 0)
    SetChrPos(0x103, 1600, 0, 116600, 0)
    SetChrPos(0xF8, 1800, 0, 115320, 0)
    SetChrPos(0xF9, 840, 0, 115320, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_215A")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as haven't talked to Aina since left the church\x01",      # 0
            "Set as talked to Aina since left the church\x01",              # 1
            "No change\x01",                                                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_214E"),
        (1, "loc_2154"),
        (SWITCH_DEFAULT, "loc_215A"),
    )


    label("loc_214E")

    OP_A3(0x1884)
    Jump("loc_215A")

    label("loc_2154")

    OP_A2(0x1884)
    Jump("loc_215A")

    label("loc_215A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21DF")

    ChrTalk(    #65
        0x8,
        (
            "#742FSo you're investigating the coma cases\x01",
            "officially on behalf of Mayor Klaus? Good.\x02\x03",

            "How's the questioning going?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2229")

    label("loc_21DF")


    ChrTalk(    #66
        0x8,
        (
            "#742FGood work with the investigation.\x02\x03",

            "How's the questioning going?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2229")


    ChrTalk(    #67
        0x101,
        (
            "#1025F#6PPretty well, I think.\x02\x03",

            "We've heard from the families of\x01",
            "everyone who's been affected, but...\x02",
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
            "I wanna poke around some more.\x01",      # 0
            "I think we're ready!\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2365")

    ChrTalk(    #68
        0x8,
        (
            "#742FAll right.\x02\x03",

            "Return to the guildhouse when you\x01",
            "feel ready to report.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1884)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Jump("loc_39D1")

    label("loc_2365")


    ChrTalk(    #69
        0x8,
        (
            "#742FAll right.\x02\x03",

            "Let's call everyone together and compare\x01",
            "notes on what we've discovered.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    Call(0, 16)
    OP_4A(0x8, 255)
    OP_6D(140, 0, 117080, 0)
    OP_67(0, 6760, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 510, 0, 116600, 0)
    SetChrPos(0x103, 1570, 0, 116600, 0)
    SetChrPos(0x105, -230, 0, 115790, 0)
    SetChrPos(0x104, 2320, 0, 115270, 0)
    SetChrPos(0x107, 1070, 0, 115580, 0)
    SetChrPos(0x108, 250, 0, 114280, 0)
    SetChrPos(0x106, 1500, 0, 114310, 0)
    OP_8C(0x8, 180, 0)
    OP_1D(0x73)
    Sleep(500)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #70
        0x8,
        (
            "#744FI see. It sounds like your investigation\x01",
            "went well.\x02\x03",

            "#742FThe testimonies of those close to the\x01",
            "affected is particularly interesting.\x02\x03",

            "There seems to be at least one common\x01",
            "thread among all of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1004F#6PYeah, that's--\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #72
        (
            "\x18\x07\x05What was the common feature across all four\x01",
            "testimonies?\x02",
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "Time It Happened\x01",          # 0
            "No Witnesses\x01",              # 1
            "The sound they heard\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_267A"),
        (1, "loc_284A"),
        (2, "loc_28F7"),
        (SWITCH_DEFAULT, "loc_2A37"),
    )


    label("loc_267A")

    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #73
        0x103,
        (
            "#524F#4PNot quite... There's a bit of a discrepancy\x01",
            "between all of them.\x02\x03",

            "Lita was found by the Mrs. Mylene before 5,\x01",
            "so she likely collapsed around 4:30.\x02\x03",

            "On the other hand, Radford fell asleep at 5:30.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #74
        0x101,
        (
            "#1015F#6PThat's true... So it's more like it happened\x01",
            "over the space of an hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x103,
        (
            "#026F#4PThere is one commonality between all\x01",
            "the testimonies...\x02\x03",

            "#022FThere were NO witnesses to anyone collapsing.\x01",
            "At all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#1004F#6PAh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A37")

    label("loc_284A")

    OP_2B(0x90, 0x3)
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #77
        0x103,
        (
            "#026F#4PYes. Exactly.\x02\x03",

            "#022FThe one commonality between all four\x01",
            "testimonies...is that there were NO witnesses\x01",
            "to anyone collapsing. At all.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_2A37")

    label("loc_28F7")

    OP_2B(0x90, 0x1)
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #78
        0x103,
        (
            "#524F#4PThat...bell sound, yes.\x02\x03",

            "While I'm curious about that too, it wasn't\x01",
            "heard in the cases of Tabitha or Luke.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #79
        0x101,
        "#1015F#6POh, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x103,
        (
            "#026F#4PThere is one commonality between all the\x01",
            "testimonies...\x02\x03",

            "#022FThere were NO witnesses to anyone collapsing.\x01",
            "At all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        "#1004F#6PAh!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A37")

    label("loc_2A37")


    ChrTalk(    #82
        0x106,
        (
            "#051F#5PI get it.\x02\x03",

            "They were put to sleep when they were\x01",
            "alone, is what you're sayin'.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x105, 90, 400)
    Sleep(500)

    ChrTalk(    #83
        0x105,
        (
            "#043F#6PIn that sense, the fog begins to make sense.\x02\x03",

            "It's hard to see anything when vision is\x01",
            "this poor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x104,
        (
            "#035F#5PA demon that devours the souls of its\x01",
            "victims, unseen by others, shrouded in\x01",
            "fog...\x02\x03",

            "#030FA horrific image, to be sure, but one\x01",
            "which fits our antagonists perfectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x107,
        "#065F#5PWaaah, that's scary!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1007F#6PThanks for the nightmare fuel,\x01",
            "Olivier.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "#744FIn that case...\x02\x03",

            "#740FWe do have some useful testimony on\x01",
            "the identity of our 'demon.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x103,
        (
            "#026F#4PYes. The sound of a bell and a woman\x01",
            "robed in black.\x02\x03",

            "#022FI'd say it's safe to say both of them are\x01",
            "related to our slumbering citizens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1015F#6PThe problem is, though, Elissa is the\x01",
            "only one who saw a woman in black.\x02\x03",

            "Maybe it's just a coincidence?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x103,
        (
            "#027F#4PI very much doubt that.\x02\x03",

            "You have to remember what happened\x01",
            "at the place the woman was seen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        "#1004F#6POh!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #92
        (
            "\x18\x07\x05What happened at the place the\x01",
            "woman appeared?\x02",
        )
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "Tabitha Collapsed\x01",      # 0
            "Radford Collapsed\x01",      # 1
            "Luke Collapsed\x01",         # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2ED3"),
        (1, "loc_2F7F"),
        (2, "loc_301C"),
        (SWITCH_DEFAULT, "loc_30A0"),
    )


    label("loc_2ED3")


    ChrTalk(    #93
        0x103,
        (
            "#026F#4PMm, no. Tabitha collapsed on the terrace\x01",
            "outside the bar.\x02\x03",

            "The black-robed woman was leaving the\x01",
            "clock tower.\x02\x03",

            "#022FAnd that would be where Pat found Luke.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A0")

    label("loc_2F7F")


    ChrTalk(    #94
        0x103,
        (
            "#026F#4PMm, no. Radford collapsed at his own home.\x02\x03",

            "The black-robed woman was leaving the\x01",
            "clock tower.\x02\x03",

            "#022FAnd that would be where Pat found Luke.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A0")

    label("loc_301C")

    OP_2B(0x90, 0x3)

    ChrTalk(    #95
        0x103,
        (
            "#026F#4PYes, exactly. The black-robed woman was\x01",
            "leaving the clock tower.\x02\x03",

            "#022FAnd that would be where Pat found Luke.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A0")

    label("loc_30A0")


    ChrTalk(    #96
        0x101,
        (
            "#1020F#6PYeah, there's no way that's a coincidence.\x02\x03",

            "So that woman in black is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x108,
        (
            "#1P#074F#3PThere's no question, now.\x02\x03",

            "#072FThere's an Enforcer skulking around in\x01",
            "the mist here in Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x106,
        "#057F#5PSon of a...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x105,
        (
            "#047F#6PFog from an unknown source and people\x01",
            "collapsing into comas would be our\x01",
            "'phenomena' then.\x02\x03",

            "#042FAnd the sound of that bell is the\x01",
            "message.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "#744FAt least we know the nature of our foe\x01",
            "now.\x02\x03",

            "#742FI'm going to contact the other guild branches,\x01",
            "especially Elnan, and let them know our\x01",
            "situation.\x02\x03",

            "What do you plan to do?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 0, 400)

    def lambda_32DD():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_32DD)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #101
        0x103,
        (
            "#522F#6PHmmm.\x02\x03",

            "It's almost certain that there will be\x01",
            "more attacks on the citizenry.\x02\x03",

            "#022FWe need to spend the night patrolling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#1006F#6PYeah, I'm up for that.\x02\x03",

            "If we do it in shifts, we should be able\x01",
            "to rest a little, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x106)
    Sleep(50)
    OP_63(0x108)

    ChrTalk(    #103
        0x108,
        "#3P#070FYou shouldn't worry about that.\x02",
    )

    CloseMessageWindow()

    def lambda_3445():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3445)
    Sleep(50)

    def lambda_3458():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3458)
    Sleep(50)

    def lambda_346B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_346B)
    Sleep(50)

    def lambda_347E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_347E)
    Sleep(400)

    ChrTalk(    #104
        0x101,
        "#1004F#4PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x106,
        (
            "#051F#5PLeave the night patrol to us guys.\x02\x03",

            "You all go home and get some rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1026F#4PBut, wait--\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #107
        0x103,
        (
            "#524F#4PIt's a good idea, Estelle.\x01",
            "You look dead on your feet,\x01",
            "and I know this has been draining for you.\x02\x03",

            "Take Kloe and Tita home with you,\x01",
            "and you three get some rest.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #108
        0x101,
        (
            "#1026F#6PBut...\x02\x03",

            "#1007F...Okay, I will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x106,
        (
            "#555F#5PUh, Scherazard. Why're you acting like we're\x01",
            "talkin' about someone else?\x02\x03",

            "Like I said, leave the patrol to us guys.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x103, 180, 400)

    def lambda_36A0():
        OP_8C(0x101, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36A0)

    ChrTalk(    #110
        0x103,
        "#023F#4P...What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x108,
        (
            "#3P#070FIt's not really about gender, mind. You've\x01",
            "been working yourself as raw as Estelle\x01",
            "on this case all day.\x02\x03",

            "Let us handle things for tonight.\x01",
            "You go rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x103,
        (
            "#024F#4PNow just a MINUTE!\x02\x03",

            "I'm a B-rank bracer!\x01",
            "I don't need my hand held like some--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x104,
        (
            "#030F#5PSchera, do not look a gift horse in the\x01",
            "mouth, hmm?\x02\x03",

            "Your words protest your lack of weariness,\x01",
            "but your body language states otherwise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x103,
        "#522F#4PTsk.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x104,
        (
            "#031F#5PIs it not also the responsibility of a\x01",
            "bracer to stay rested and ready to act?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x103,
        (
            "#522F#4P...\x02\x03",

            "#025FVery well.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #117
        0x101,
        "#1026F#6PSchera...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x103,
        (
            "#524F#4PAgate, Zin.\x02\x03",

            "Be careful out there, all right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x108,
        "#3P#071FLeave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x106,
        (
            "#051F#5PWell, remember, you guys better be ready\x01",
            "for action tomorrow morning.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearParty()
    AddParty(0x0, 0xF6, 0xFF)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T0101   ._SN", 110, 0, 0)
    IdleLoop()

    label("loc_39D1")

    Return()

    # Function_15_1FE3 end

    def Function_16_39D2(): pass

    label("Function_16_39D2")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A0B")
    AddParty(0x3, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3A0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A44")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A2C")
    AddParty(0x4, 0xFA, 0xFF)
    Jump("loc_3A30")

    label("loc_3A2C")

    AddParty(0x4, 0xFB, 0xFF)

    label("loc_3A30")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3A44")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3A91")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A65")
    AddParty(0x7, 0xFA, 0xFF)
    Jump("loc_3A7D")

    label("loc_3A65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A79")
    AddParty(0x7, 0xFB, 0xFF)
    Jump("loc_3A7D")

    label("loc_3A79")

    AddParty(0x7, 0xFC, 0xFF)

    label("loc_3A7D")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3A91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3ADE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB2")
    AddParty(0x5, 0xFA, 0xFF)
    Jump("loc_3ACA")

    label("loc_3AB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AC6")
    AddParty(0x5, 0xFB, 0xFF)
    Jump("loc_3ACA")

    label("loc_3AC6")

    AddParty(0x5, 0xFC, 0xFF)

    label("loc_3ACA")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3ADE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B03")
    AddParty(0x6, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3B03")

    Return()

    # Function_16_39D2 end

    def Function_17_3B04(): pass

    label("Function_17_3B04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3B14")
    RemoveParty(0x3, 0xFF)

    label("loc_3B14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3B24")
    RemoveParty(0x4, 0xFF)

    label("loc_3B24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3B34")
    RemoveParty(0x6, 0xFF)

    label("loc_3B34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3B44")
    RemoveParty(0x7, 0xFF)

    label("loc_3B44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3B54")
    RemoveParty(0x5, 0xFF)

    label("loc_3B54")

    Return()

    # Function_17_3B04 end

    def Function_18_3B55(): pass

    label("Function_18_3B55")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
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
        (0, "loc_3BD1"),
        (1, "loc_3BD7"),
        (SWITCH_DEFAULT, "loc_3BDD"),
    )


    label("loc_3BD1")

    OP_A2(0x1200)
    Jump("loc_3BDD")

    label("loc_3BD7")

    OP_A2(0x1201)
    Jump("loc_3BDD")

    label("loc_3BDD")

    Return()

    # Function_18_3B55 end

    def Function_19_3BDE(): pass

    label("Function_19_3BDE")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_19_3BDE end

    SaveToFile()

Try(main)
