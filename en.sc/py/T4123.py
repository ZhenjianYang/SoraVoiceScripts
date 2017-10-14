from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4123   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4123.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        'Elnan',                                # 9
        'Butler Phillip',                       # 10
        'Scherazard',                           # 11
        'Agate',                                # 12
        'Olivier',                              # 13
        'Kloe',                                 # 14
        'Tita',                                 # 15
        'Zin',                                  # 16
        'Anelace',                              # 17
        'Letter',                               # 18
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
        'ED6_DT07/CH02580 ._CH',             # 00
        'ED6_DT07/CH02470 ._CH',             # 01
        'ED6_DT07/CH00020 ._CH',             # 02
        'ED6_DT06/CH20053 ._CH',             # 03
        'ED6_DT07/CH00030 ._CH',             # 04
        'ED6_DT07/CH00040 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT07/CH00070 ._CH',             # 07
        'ED6_DT07/CH01630 ._CH',             # 08
        'ED6_DT26/CH20301 ._CH',             # 09
        'ED6_DT07/CH00024 ._CH',             # 0A
        'ED6_DT07/CH00054 ._CH',             # 0B
        'ED6_DT07/CH00034 ._CH',             # 0C
        'ED6_DT07/CH00044 ._CH',             # 0D
        'ED6_DT07/CH00064 ._CH',             # 0E
        'ED6_DT07/CH00074 ._CH',             # 0F
        'ED6_DT07/CH00033 ._CH',             # 10
        'ED6_DT07/CH00073 ._CH',             # 11
        'ED6_DT06/CH20021 ._CH',             # 12
        'ED6_DT27/CH03085 ._CH',             # 13
        'ED6_DT27/CH03091 ._CH',             # 14
        'ED6_DT26/CH20415 ._CH',             # 15
    )

    AddCharChipPat(
        'ED6_DT07/CH02580P._CP',             # 00
        'ED6_DT07/CH02470P._CP',             # 01
        'ED6_DT07/CH00020P._CP',             # 02
        'ED6_DT06/CH20053P._CP',             # 03
        'ED6_DT07/CH00030P._CP',             # 04
        'ED6_DT07/CH00040P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT07/CH00070P._CP',             # 07
        'ED6_DT07/CH01630P._CP',             # 08
        'ED6_DT26/CH20301P._CP',             # 09
        'ED6_DT07/CH00024P._CP',             # 0A
        'ED6_DT07/CH00054P._CP',             # 0B
        'ED6_DT07/CH00034P._CP',             # 0C
        'ED6_DT07/CH00044P._CP',             # 0D
        'ED6_DT07/CH00064P._CP',             # 0E
        'ED6_DT07/CH00074P._CP',             # 0F
        'ED6_DT07/CH00033P._CP',             # 10
        'ED6_DT07/CH00073P._CP',             # 11
        'ED6_DT06/CH20021P._CP',             # 12
        'ED6_DT27/CH03085P._CP',             # 13
        'ED6_DT27/CH03091P._CP',             # 14
        'ED6_DT26/CH20415P._CP',             # 15
    )

    DeclNpc(
        X                   = -4460,
        Z                   = 0,
        Y                   = 960,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x111,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x191,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x191,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x191,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 1966096,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 4970,
        TriggerZ            = 0,
        TriggerY            = -1040,
        TriggerRange        = 1400,
        ActorX              = 4970,
        ActorZ              = 2000,
        ActorY              = -1040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2BE",          # 00, 0
        "Function_1_3F8",          # 01, 1
        "Function_2_405",          # 02, 2
        "Function_3_582",          # 03, 3
        "Function_4_622",          # 04, 4
        "Function_5_6B5",          # 05, 5
        "Function_6_70D",          # 06, 6
        "Function_7_760",          # 07, 7
        "Function_8_7B5",          # 08, 8
        "Function_9_80E",          # 09, 9
        "Function_10_866",         # 0A, 10
        "Function_11_8B7",         # 0B, 11
        "Function_12_3529",        # 0C, 12
        "Function_13_3578",        # 0D, 13
        "Function_14_35C7",        # 0E, 14
        "Function_15_3616",        # 0F, 15
        "Function_16_3646",        # 10, 16
        "Function_17_3683",        # 11, 17
        "Function_18_36C0",        # 12, 18
        "Function_19_3712",        # 13, 19
        "Function_20_374B",        # 14, 20
        "Function_21_3780",        # 15, 21
        "Function_22_37C1",        # 16, 22
        "Function_23_3802",        # 17, 23
        "Function_24_383C",        # 18, 24
        "Function_25_386C",        # 19, 25
        "Function_26_3892",        # 1A, 26
        "Function_27_3918",        # 1B, 27
    )


    def Function_0_2BE(): pass

    label("Function_0_2BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_3C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_2E2")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -5450, 0, 310, 0)

    label("loc_2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_310")
    OP_4A(0xB, 255)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 54780, 200, -3510, 90)
    SetChrChipByIndex(0xB, 11)
    Jump("loc_334")

    label("loc_310")

    OP_4A(0xA, 255)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 54780, 200, -3510, 90)
    SetChrChipByIndex(0xA, 10)

    label("loc_334")

    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xF, 0x4)
    SetChrPos(0xC, 57160, 200, -5120, 270)
    SetChrPos(0xD, 60800, 0, 2300, 0)
    SetChrPos(0xE, 58950, 0, 2510, 180)
    SetChrPos(0xF, 54780, 200, -5080, 90)
    SetChrChipByIndex(0xC, 12)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 14)
    SetChrChipByIndex(0xF, 15)
    OP_4A(0x8, 255)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 0)

    label("loc_3C5")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3D1"),
        (SWITCH_DEFAULT, "loc_3F7"),
    )


    label("loc_3D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x2000000)
    SetMapFlags(0x10000000)
    Event(0, 11)

    label("loc_3F4")

    Jump("loc_3F7")

    label("loc_3F7")

    Return()

    # Function_0_2BE end

    def Function_1_3F8(): pass

    label("Function_1_3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_404")
    OP_72(0x5, 0x4)

    label("loc_404")

    Return()

    # Function_1_3F8 end

    def Function_2_405(): pass

    label("Function_2_405")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42A")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_56C")

    label("loc_42A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_443")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_56C")

    label("loc_443")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_56C")

    label("loc_45C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_475")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_56C")

    label("loc_475")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_56C")

    label("loc_48E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A7")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_56C")

    label("loc_4A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C0")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_56C")

    label("loc_4C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D9")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_56C")

    label("loc_4D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F2")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_56C")

    label("loc_4F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50B")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_56C")

    label("loc_50B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_524")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_56C")

    label("loc_524")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53D")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_56C")

    label("loc_53D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_556")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_56C")

    label("loc_556")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56C")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_56C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_581")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_56C")

    label("loc_581")

    Return()

    # Function_2_405 end

    def Function_3_582(): pass

    label("Function_3_582")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 2)), scpexpr(EXPR_END)), "loc_5D3")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #0
        "\x07\x05Elnan is collapsed here, asleep.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_61E")

    label("loc_5D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 1)), scpexpr(EXPR_END)), "loc_61E")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #1
        "\x07\x05Elnan is collapsed here, asleep.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_61E")

    TalkEnd(0x8)
    Return()

    # Function_3_582 end

    def Function_4_622(): pass

    label("Function_4_622")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        (
            "#720FMiss Estelle, please leave\x01",
            "it to me to look after everyone\x01",
            "here.\x02\x03",

            "In turn, I would ask you to take\x01",
            "care of His Highness the Duke.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_4_622 end

    def Function_5_6B5(): pass

    label("Function_5_6B5")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        "\x07\x05Scherazard is slumped over the table, asleep.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFE)
    Return()

    # Function_5_6B5 end

    def Function_6_70D(): pass

    label("Function_6_70D")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #4
        "\x07\x05Agate is slumped over the table, asleep.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFE)
    Return()

    # Function_6_70D end

    def Function_7_760(): pass

    label("Function_7_760")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #5
        "\x07\x05Olivier is slumped over the table, asleep.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFE)
    Return()

    # Function_7_760 end

    def Function_8_7B5(): pass

    label("Function_8_7B5")

    TalkBegin(0xD)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #6
        "\x07\x05Kloe is leaning against the bookshelf, asleep.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xD)
    Return()

    # Function_8_7B5 end

    def Function_9_80E(): pass

    label("Function_9_80E")

    TalkBegin(0xE)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #7
        "\x07\x05Tita is leaning up against the board, asleep.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xE)
    Return()

    # Function_9_80E end

    def Function_10_866(): pass

    label("Function_10_866")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #8
        "\x07\x05Zin is slumped over the table, asleep.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFE)
    Return()

    # Function_10_866 end

    def Function_11_8B7(): pass

    label("Function_11_8B7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CA")
    Call(0, 26)

    label("loc_8CA")

    OP_4A(0x8, 255)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x143, 0x80)
    SetChrFlags(0xF7, 0x80)
    OP_6D(30, -250, -5270, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x5, 0x4)
    FadeToBright(1500, 0)
    Sleep(500)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0xC)
    Sleep(800)
    OP_43(0x109, 0x1, 0x0, 0xD)
    Sleep(800)
    OP_43(0x143, 0x1, 0x0, 0xE)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #9
        0x101,
        "#1011F#6PElnan, I'm b--\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x7D0)
    OP_6D(-4460, 0, 960, 2000)
    Sleep(1000)
    Fade(1000)
    OP_6D(-2420, 0, -1880, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(277, 0)
    OP_0D()
    OP_1D(0x51)

    ChrTalk(    #10
        0x101,
        "#1020F#5PE-ELNAN!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x143,
        "#721FWhat...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        "#1069FDamn it! This must've been their next move!\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0xF)
    Sleep(500)
    OP_43(0x143, 0x1, 0x0, 0x11)
    Sleep(200)
    OP_43(0x109, 0x1, 0x0, 0x10)

    def lambda_A8F():
        OP_6D(-5430, 0, 690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A8F)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #13
        0x101,
        "#1020F#6PElnan?! ELNAN, SAY SOMETHING!\x02",
    )

    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x101, 0x2)
    Fade(250)
    SetChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 19)
    SetChrSubChip(0x109, 3)
    OP_0D()
    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #14
        0x109,
        (
            "#1067FCalm down, Estelle. He's breathing normally...\x01",
            "and peacefully. Looks like he's in a deep sleep.\x02\x03",

            "#1063FI take it this is the Grancel guild receptionist?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        "#1026FY-Yeah...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x101, 135, 400)

    ChrTalk(    #16
        0x101,
        "#1020F...Oh, oh, NO! EVERYONE!\x02",
    )

    CloseMessageWindow()

    def lambda_C01():

        label("loc_C01")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_C01")

    QueueWorkItem2(0x143, 2, lambda_C01)
    OP_8E(0x101, 0xFFFFEF7A, 0x0, 0xFFFFF4FC, 0x1770, 0x0)

    def lambda_C26():
        OP_6D(-1050, 0, 3360, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C26)
    OP_8E(0x101, 0xFFFFFC18, 0x0, 0xFFFFF4B6, 0x1770, 0x0)
    OP_8E(0x101, 0x10AE, 0x0, 0x1202, 0x1770, 0x0)
    OP_8E(0x101, 0xFFFFF2A4, 0xDAC, 0x1388, 0x1770, 0x0)
    Fade(1000)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 56220, 600, -3080, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CBD")
    OP_4A(0xB, 255)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrPos(0xB, 54780, 200, -3510, 90)
    SetChrChipByIndex(0xB, 11)
    Jump("loc_CE1")

    label("loc_CBD")

    OP_4A(0xA, 255)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0xA, 54780, 200, -3510, 90)
    SetChrChipByIndex(0xA, 10)

    label("loc_CE1")

    ClearChrFlags(0x109, 0x2)
    SetChrChipByIndex(0x109, 65535)
    OP_44(0x143, 0x2)
    OP_4A(0xD, 255)
    OP_4A(0xE, 255)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xF, 0x4)
    SetChrPos(0xC, 57160, 200, -5120, 270)
    SetChrPos(0xD, 60800, 0, 2300, 0)
    SetChrPos(0xE, 58950, 0, 2510, 180)
    SetChrPos(0xF, 54780, 200, -5080, 90)
    SetChrChipByIndex(0xC, 12)
    SetChrChipByIndex(0xD, 13)
    SetChrChipByIndex(0xE, 14)
    SetChrChipByIndex(0xF, 15)
    OP_6D(56580, 0, -270, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_43(0x101, 0x1, 0x0, 0x17)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #17
        0x101,
        "#1020F#6PNO!\x02",
    )

    CloseMessageWindow()

    def lambda_DD4():
        OP_6D(54530, 0, -560, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DD4)
    OP_8E(0x101, 0xD624, 0x0, 0xFFFFFAEC, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E2C")

    ChrTalk(    #18
        0x101,
        "#1020F#4PAgate! Olivier! Zin!\x02",
    )

    CloseMessageWindow()
    Jump("loc_E50")

    label("loc_E2C")


    ChrTalk(    #19
        0x101,
        "#1020F#4PSchera! Olivier! Zin!\x02",
    )

    CloseMessageWindow()

    label("loc_E50")

    OP_8C(0x101, 45, 600)
    Sleep(500)

    def lambda_E62():
        OP_6D(57790, 0, 1880, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E62)
    OP_8E(0x101, 0xE8E4, 0x0, 0x38E, 0xFA0, 0x0)
    TurnDirection(0x101, 0xE, 400)
    Sleep(500)
    TurnDirection(0x101, 0xD, 400)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #20
        0x101,
        "#1020F#5PTITA! KLOE!\x02",
    )

    CloseMessageWindow()
    OP_43(0x109, 0x1, 0x0, 0x12)
    Sleep(800)
    OP_43(0x143, 0x1, 0x0, 0x13)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #21
        0x109,
        "#1068F#6PDamn. They got everyone...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 90, 400)
    WaitChrThread(0x143, 0x1)
    OP_43(0x143, 0x1, 0x0, 0x14)
    Sleep(400)
    OP_8E(0x109, 0xE47A, 0x0, 0x348, 0xBB8, 0x0)
    TurnDirection(0x109, 0x101, 400)

    ChrTalk(    #22
        0x109,
        "#1063F#6PAre they all okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        (
            "#1026F#5PLooks like it... They're all just asleep.\x02\x03",

            "#1007FWhat the hell happened?!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x143, 0x1)

    def lambda_FC4():

        label("loc_FC4")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_FC4")

    QueueWorkItem2(0x143, 1, lambda_FC4)
    Sleep(500)

    ChrTalk(    #24
        0x143,
        (
            "#720F#6PIf I must hazard a guess, Miss Estelle,\x01",
            "they were put to sleep with drugs.\x02\x03",

            "They all look as though sleep took them\x01",
            "very suddenly.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 315, 400)

    ChrTalk(    #25
        0x101,
        "#1015F#5PY-Yeah, good point.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)

    ChrTalk(    #26
        0x109,
        "#1064F#6PHey, good catch.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x11, 400)
    Sleep(1000)

    def lambda_10E1():

        label("loc_10E1")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_10E1")

    QueueWorkItem2(0x109, 1, lambda_10E1)

    def lambda_10F2():
        OP_6D(56030, 0, 20, 1500)
        ExitThread()

    QueueWorkItem(0x143, 2, lambda_10F2)
    OP_8E(0x101, 0xDBE2, 0x0, 0xFFFFF70E, 0xBB8, 0x0)
    TurnDirection(0x101, 0x11, 400)
    WaitChrThread(0x143, 0x2)
    WaitChrThread(0x143, 0x3)

    ChrTalk(    #27
        0x101,
        "#1004F#5PWait, what's this? A letter?\x02",
    )

    CloseMessageWindow()
    OP_44(0x109, 0x1)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_117A():
        OP_8E(0xFE, 0xDDCC, 0x0, 0xFFFFFC86, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_117A)
    WaitChrThread(0x109, 0x0)
    TurnDirection(0x109, 0x11, 400)

    ChrTalk(    #28
        0x109,
        (
            "#1064F#4PHold on a second...\x02\x03",

            "That's the same kind of envelope we got!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x101,
        "#1020F#5PIt is!\x02",
    )

    CloseMessageWindow()
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0x11, 0x80)
    Sleep(500)
    TurnDirection(0x101, 0x109, 400)
    Sleep(500)
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(200)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #30
        "\x07\x05Estelle ripped open the envelope and read the letter.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AD(0x240097, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #31
        (
            "\x07\x05I've taken the duke and the girl.\x02\x03",

            "If you want them back, come attend our little tea party.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1500)

    ChrTalk(    #32
        0x101,
        "#1005F#5PWHAAAAAAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x143,
        "#721F#4PHis Highness...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        (
            "#1065F#4PSo the 'tea party' is in the capital after all...\x01",
            "Thought so.\x02\x03",

            "#1063FWho's this girl they're talking about,\x01",
            "Estelle?\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #35
        0x101,
        "#1004F#5PGirl? No...!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 270, 600)
    Sleep(500)
    OP_8C(0x101, 90, 600)
    Sleep(500)

    ChrTalk(    #36
        0x101,
        (
            "#1020F#5PRenne?!\x02\x03",

            "Renne, where are you?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1451():

        label("loc_1451")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_1451")

    QueueWorkItem2(0x109, 1, lambda_1451)

    def lambda_1462():
        OP_6D(63130, 0, 4190, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1462)
    OP_8E(0x101, 0xFB22, 0x0, 0x140, 0x1770, 0x0)
    OP_8E(0x101, 0xFC4E, 0x7D0, 0x1284, 0x1770, 0x0)
    OP_8E(0x101, 0xF0D2, 0xF0A, 0x1284, 0x1770, 0x0)
    OP_44(0x109, 0x1)
    OP_44(0x143, 0x1)
    Fade(1000)
    OP_6D(119700, 0, 4700, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 125400, -2000, 4700, 270)
    OP_8E(0x101, 0x1D394, 0x0, 0x125C, 0x1388, 0x0)
    OP_69(0x101, 0x0)

    def lambda_152C():

        label("loc_152C")

        OP_69(0x101, 0x0)
        OP_48()
        Jump("loc_152C")

    QueueWorkItem2(0x101, 1, lambda_152C)
    OP_8E(0x101, 0x1D394, 0x0, 0xFFFFFA92, 0x1388, 0x0)
    OP_8C(0x101, 270, 600)
    Sleep(500)
    OP_8C(0x101, 90, 600)
    Sleep(500)
    OP_43(0x109, 0x1, 0x0, 0x15)
    OP_8C(0x101, 180, 600)
    Sleep(500)
    OP_44(0x101, 0x1)
    Sleep(300)
    OP_43(0x143, 0x1, 0x0, 0x16)

    def lambda_158C():
        OP_6D(119410, 0, -320, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_158C)
    WaitChrThread(0x109, 0x1)

    ChrTalk(    #37
        0x109,
        (
            "#1063F#4PKidnapped, I'm guessing...\x02\x03",

            "Another member of your team?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #38
        0x101,
        (
            "#1026F#6PNo, she's just a kid we were taking care of!\x02\x03",

            "#1027FI can't believe we got her involved in this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x109,
        "#1067F#4PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x143,
        "#722FMiss Estelle...\x02",
    )

    CloseMessageWindow()
    OP_61(0x101)

    ChrTalk(    #41
        0x101,
        (
            "#1003F#6PPhillip, I'm sorry.\x02\x03",

            "I'm pretty sure Dunan's been taken as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x143,
        (
            "#720FYou need not apologize.\x02\x03",

            "If it's true, it is his responsibility for\x01",
            "going off to...play about on his own.\x02\x03",

            "Do not blame yourself for his failings,\x01",
            "Miss Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x109,
        (
            "#1063F#4PHe's right, Estelle.\x02\x03",

            "First we need to figure out what the\x01",
            "tea party in the letter is!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1002F#6PR-Right...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(200)
    Sleep(200)
    FadeToDark(300, 0, 100)
    OP_AD(0x240097, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetChrName("")
    SetMessageWindowPos(-1, 300, -1, 3)

    AnonymousTalk(    #45
        (
            "\x07\x05I've taken the duke and the girl.\x02\x03",

            "If you want them back, come attend our little tea party.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1500)
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #46
        0x101,
        (
            "#1015F#6PI kinda remember Elnan saying something\x01",
            "about a 'tea party' in relation to the\x01",
            "Intelligence guys...\x02\x03",

            "#1004F...Wait, Kevin.\x02\x03",

            "When I read the letter you said\x01",
            "it's, 'in the capital after all.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        (
            "#1064F#4POh, er. You heard that didja?\x02\x03",

            "#1066FYeeeeah, 'bout that...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2788")
    SetChrPos(0xA, 125400, 0, 4700, 270)

    NpcTalk(    #48
        0xA,
        "Woman's Voice",
        "#5PI believe I can explain, Father.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_4A(0xA, 255)
    SetChrChipByIndex(0xA, 2)
    SetChrPos(0xA, 125400, -2000, 4700, 270)
    ClearChrFlags(0xA, 0x80)

    def lambda_1A90():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A90)

    def lambda_1A9E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x143, 1, lambda_1A9E)

    def lambda_1AAC():
        OP_6D(118950, 0, 1040, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AAC)
    OP_8E(0xA, 0x1D394, 0x0, 0x125C, 0xBB8, 0x0)
    OP_8E(0xA, 0x1D394, 0x0, 0x6EA, 0xBB8, 0x0)

    ChrTalk(    #49
        0x109,
        "#1062F#5PHeeey, nice timing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1004F#5PHuh?\x02\x03",

            "Sch-SCHERA?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "#027FHello, Estelle.\x02\x03",

            "Things have gotten a little serious,\x01",
            "haven't they?\x02\x03",

            "#025FAnd...Father, it looks like neither\x01",
            "of us made it in time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x109,
        (
            "#1068F#5PYeah. Nobody's hurt, thank Aidios,\x01",
            "but I got no excuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1020F#5PSchera, why are you here...\x02\x03",

            "And what are you talking about?\x01",
            "How do you two know each other?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xA,
        (
            "#020FI imagine you heard that Anelace and I found\x01",
            "the Intelligence Division base?\x02\x03",

            "We met Father Kevin there.\x02\x03",

            "He helped us investigate where the Intelligence\x01",
            "special forces had run off to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1025F#5POh, I see...\x01",
            "That's why he's so up to speed, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x109,
        "#1060F#5PHaha, bingo!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x10, 125400, 0, 4700, 270)

    NpcTalk(    #57
        0x10,
        "Girl's Voice",
        "#5PScheraaaa!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x10, 400)

    def lambda_1DC7():

        label("loc_1DC7")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_1DC7")

    QueueWorkItem2(0xA, 1, lambda_1DC7)
    SetChrPos(0x10, 125400, -2000, 4700, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 20)
    OP_8E(0x10, 0x1D394, 0x0, 0x125C, 0x1388, 0x0)
    OP_8E(0x10, 0x1D77C, 0x0, 0x672, 0x1388, 0x0)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 0)
    OP_44(0xA, 0x1)

    ChrTalk(    #58
        0x101,
        "#1004F#5PAnelace!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "#811F#4PEstelle! Yay, you're safe!\x02\x03",

            "#1310FAnd hey, Kevin's here too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x109,
        "#1060F#5PYeah. Afraid I didn't make it in time, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xA,
        "#020F#6PHow's the phone downstairs?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xA, 400)

    ChrTalk(    #62
        0x10,
        (
            "#1316F#4PNo good. Someone removed some crucial bits,\x01",
            "so it's totally useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xA,
        "#026F#6PI wonder...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 225, 500)

    def lambda_1F6A():

        label("loc_1F6A")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1F6A")

    QueueWorkItem2(0x101, 1, lambda_1F6A)

    def lambda_1F7B():

        label("loc_1F7B")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1F7B")

    QueueWorkItem2(0x109, 1, lambda_1F7B)

    def lambda_1F8C():

        label("loc_1F8C")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1F8C")

    QueueWorkItem2(0x143, 1, lambda_1F8C)

    def lambda_1F9D():

        label("loc_1F9D")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_1F9D")

    QueueWorkItem2(0x10, 1, lambda_1F9D)
    OP_8E(0xA, 0x1CB6A, 0x0, 0x19A, 0xBB8, 0x0)

    def lambda_1FC2():
        OP_6D(116400, 0, 3390, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1FC2)

    def lambda_1FDA():
        OP_67(0, 3500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1FDA)

    def lambda_1FF2():
        OP_6B(3140, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1FF2)

    def lambda_2002():
        OP_6E(306, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2002)
    OP_8E(0xA, 0x1BFDA, 0xFA, 0x230, 0xBB8, 0x0)
    OP_8E(0xA, 0x1C14C, 0xFA, 0x12F2, 0xBB8, 0x0)
    Sleep(1000)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0x143, 0x1)
    OP_44(0x10, 0x1)

    ChrTalk(    #64
        0xA,
        "#522F#6PSame with this one. Damn!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(118020, 0, 400, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(315000, 0)
    OP_6E(306, 0)
    OP_8C(0xA, 180, 400)
    OP_43(0xA, 0x0, 0x0, 0x18)
    Sleep(500)
    OP_43(0x10, 0x0, 0x0, 0x19)

    def lambda_20D7():

        label("loc_20D7")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_20D7")

    QueueWorkItem2(0x101, 1, lambda_20D7)

    def lambda_20E8():

        label("loc_20E8")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_20E8")

    QueueWorkItem2(0x109, 1, lambda_20E8)

    def lambda_20F9():

        label("loc_20F9")

        TurnDirection(0xFE, 0xA, 0)
        OP_48()
        Jump("loc_20F9")

    QueueWorkItem2(0x143, 1, lambda_20F9)
    WaitChrThread(0xA, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0x143, 0x1)
    OP_44(0x10, 0x1)

    ChrTalk(    #65
        0x101,
        "#1002F#2PSo...the 'enemy' broke them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xA,
        (
            "#022F#6PI'm sure of it.\x02\x03",

            "I still can't fathom their goals, though...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x101,
        "#1004F#2POh, Schera! They left this letter...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #68
        "\x07\x05Estelle showed Schera the letter and explained the situation.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #69
        0xA,
        (
            "#026F#6PA 'tea party'... Now it's all making sense.\x02\x03",

            "#022FIt must be the Intelligence Division men\x01",
            "who kidnapped the duke and the girl.\x01",
            "I'm sure of it.\x02\x03",

            "And Ouroboros is pulling their strings.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1026F#2PYeah, we got attacked by some weird\x01",
            "machines...\x02\x03",

            "But what does 'attend our tea party' mean?\x01",
            "Where are we even supposed to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xA,
        (
            "#026F#6PWe'll simply have to search anywhere\x01",
            "that seems likely.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 45, 400)
    Sleep(400)

    ChrTalk(    #72
        0xA,
        "#020F#6PAnelace. Can I ask you a favor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        "#814FSure, what's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xA,
        (
            "#022F#6PI need you to run to the Erbe Royal Villa and\x01",
            "get in touch with the patrol HQ there.\x02\x03",

            "The men on the roads are a diversion;\x01",
            "the real fight is going to be in Grancel\x01",
            "tonight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1002F#2POh, yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x109,
        (
            "#1063F#2PTheir goal is nothing less than dominance\x01",
            "of the capital, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10,
        (
            "#816FU-Understood!\x02\x03",

            "I'll run until my legs fall off!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #78
        0x101,
        "#1002FAnelace! Be careful, okay?\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #79
        0x10,
        "#811FI will! You too, Estelle!\x02",
    )

    CloseMessageWindow()

    def lambda_25F3():

        label("loc_25F3")

        TurnDirection(0x109, 0x10, 400)
        OP_48()
        Jump("loc_25F3")

    QueueWorkItem2(0x109, 0, lambda_25F3)

    def lambda_2604():

        label("loc_2604")

        TurnDirection(0x143, 0x10, 400)
        OP_48()
        Jump("loc_2604")

    QueueWorkItem2(0x143, 0, lambda_2604)
    OP_8C(0x10, 0, 400)

    def lambda_261C():
        OP_6D(119000, 0, 1990, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_261C)
    SetChrChipByIndex(0x10, 20)
    OP_8E(0x10, 0x1D394, 0x0, 0x125C, 0x1388, 0x0)
    OP_8E(0x10, 0x1E9D8, 0xFFFFF830, 0x125C, 0x1388, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    def lambda_266B():
        OP_6D(118020, 0, 400, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_266B)
    OP_8C(0xA, 90, 400)

    def lambda_268A():
        OP_8C(0x101, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_268A)
    Sleep(50)

    def lambda_269D():
        OP_8C(0x109, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_269D)
    Sleep(50)

    def lambda_26B0():
        OP_8C(0x143, 270, 400)
        ExitThread()

    QueueWorkItem(0x143, 0, lambda_26B0)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #80
        0xA,
        (
            "#020F#6PSir, I'm sorry, but can you wait here?\x02\x03",

            "We'll bring the duke back.\x01",
            "You have my word.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x143,
        (
            "#720F#2PVery well.\x02\x03",

            "I will tend to your friends while I am here.\x02\x03",

            "Please...recover His Highness.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3511")

    label("loc_2788")

    SetChrPos(0xB, 125400, 0, 4700, 270)

    NpcTalk(    #82
        0xB,
        "Man's Voice",
        "#5PThink I can help you out there, Kevin.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_4A(0xB, 255)
    SetChrChipByIndex(0xB, 3)
    SetChrPos(0xB, 125400, -2000, 4700, 270)
    ClearChrFlags(0xB, 0x80)

    def lambda_2815():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2815)

    def lambda_2823():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x143, 1, lambda_2823)

    def lambda_2831():
        OP_6D(118950, 0, 1040, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2831)
    OP_8E(0xB, 0x1D394, 0x0, 0x125C, 0xBB8, 0x0)
    OP_8E(0xB, 0x1D394, 0x0, 0x6EA, 0xBB8, 0x0)

    ChrTalk(    #83
        0x109,
        "#1062F#5PHeeey, nice timing!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1004F#5PHuh?\x02\x03",

            "A-AGATE?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xB,
        (
            "#051FHey, Estelle.\x02\x03",

            "Looks like things got kinda crazy\x01",
            "around here.\x02\x03",

            "#053FGuess neither of us got here in time, Kevin.\x01",
            "Damn it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x109,
        (
            "#1068F#5PYeah. Nobody's hurt, thank Aidios,\x01",
            "but I got no excuse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1020F#5PAgate, why are you here...\x02\x03",

            "And what are you talking about?\x01",
            "How do you two know each other?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xB,
        (
            "#051FThink Elnan mighta filled you in on what we\x01",
            "found in Bose. The Intelligence goons' base?\x02\x03",

            "We met this guy there.\x02\x03",

            "He helped us track down where those thugs'd\x01",
            "run off to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#1025F#5POh, I see...\x01",
            "That's why he's so up to speed, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x109,
        "#1060F#5PHaha, bingo!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x10, 125400, 0, 4700, 270)

    NpcTalk(    #91
        0x10,
        "Girl's Voice",
        "#5PAgaaaaate!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x10, 400)

    def lambda_2B30():

        label("loc_2B30")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_2B30")

    QueueWorkItem2(0xB, 1, lambda_2B30)
    SetChrPos(0x10, 125400, -2000, 4700, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 20)
    OP_8E(0x10, 0x1D394, 0x0, 0x125C, 0x1388, 0x0)
    OP_8E(0x10, 0x1D77C, 0x0, 0x672, 0x1388, 0x0)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 0)
    OP_44(0xB, 0x1)

    ChrTalk(    #92
        0x101,
        "#1004F#5PAnelace!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10,
        (
            "#811F#4PEstelle! Yay, you're safe!\x02\x03",

            "#1310FAnd hey, Kevin's here too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x109,
        (
            "#1060F#5PYeah. Afraid I didn't make it\x01",
            "in time, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xB,
        "#050F#6PHow's the phone downstairs?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xB, 400)

    ChrTalk(    #96
        0x10,
        (
            "#1316F#4PNo good. Someone removed some crucial bits,\x01",
            "so it's totally useless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xB,
        "#552F#6PDamn. Wonder if they...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 225, 500)

    def lambda_2CDF():

        label("loc_2CDF")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2CDF")

    QueueWorkItem2(0x101, 1, lambda_2CDF)

    def lambda_2CF0():

        label("loc_2CF0")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2CF0")

    QueueWorkItem2(0x109, 1, lambda_2CF0)

    def lambda_2D01():

        label("loc_2D01")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2D01")

    QueueWorkItem2(0x143, 1, lambda_2D01)

    def lambda_2D12():

        label("loc_2D12")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2D12")

    QueueWorkItem2(0x10, 1, lambda_2D12)
    OP_8E(0xB, 0x1CB6A, 0x0, 0x19A, 0xBB8, 0x0)

    def lambda_2D37():
        OP_6D(116400, 0, 3390, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D37)

    def lambda_2D4F():
        OP_67(0, 3500, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2D4F)

    def lambda_2D67():
        OP_6B(3140, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2D67)

    def lambda_2D77():
        OP_6E(306, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2D77)
    OP_8E(0xB, 0x1BFDA, 0xFA, 0x230, 0xBB8, 0x0)
    OP_8E(0xB, 0x1C14C, 0xFA, 0x12F2, 0xBB8, 0x0)
    Sleep(1000)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0x143, 0x1)
    OP_44(0x10, 0x1)

    ChrTalk(    #98
        0xB,
        "#555F#6PAh, same with this one.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(118020, 0, 400, 0)
    OP_67(0, 5230, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(315000, 0)
    OP_6E(306, 0)
    OP_8C(0xB, 180, 400)
    OP_43(0xB, 0x0, 0x0, 0x18)
    Sleep(500)
    OP_43(0x10, 0x0, 0x0, 0x19)

    def lambda_2E4A():

        label("loc_2E4A")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2E4A")

    QueueWorkItem2(0x101, 1, lambda_2E4A)

    def lambda_2E5B():

        label("loc_2E5B")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2E5B")

    QueueWorkItem2(0x109, 1, lambda_2E5B)

    def lambda_2E6C():

        label("loc_2E6C")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_2E6C")

    QueueWorkItem2(0x143, 1, lambda_2E6C)
    WaitChrThread(0xB, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x109, 0x1)
    OP_44(0x143, 0x1)
    OP_44(0x10, 0x1)

    ChrTalk(    #99
        0x101,
        "#1002F#2PSo...the 'enemy' broke them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xB,
        (
            "#050F#6PYeah, no question.\x02\x03",

            "Just wish I understood what the hell\x01",
            "it is they're trying to do.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #101
        0x101,
        "#1004F#2POh, Agate! They left this letter...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #102
        "\x07\x05Estelle showed Agate the letter and explained the situation.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #103
        0xB,
        (
            "#053F#6PA 'tea party,' huh...\x01",
            "Now I'm starting to get it.\x02\x03",

            "#057FIt's those Intelligence bastards who\x01",
            "kidnapped the duke and that girl.\x02\x03",

            "And it's goddamn Ouroboros behind it all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#1026F#2PYeah, we got attacked by some weird\x01",
            "machines...\x02\x03",

            "But what does 'attend our tea party' mean?\x01",
            "Where are we even supposed to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xB,
        (
            "#053F#6PCould be anywhere.\x01",
            "We'll have to search the whole city.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 45, 400)
    Sleep(400)

    ChrTalk(    #106
        0xB,
        "#050F#6PAnelace. Got a favor to ask you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        "#814FSure, what's up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xB,
        (
            "#050F#6PNeed you to get over to the Erbe Royal Villa,\x01",
            "and get in touch with the patrol HQ there.\x02\x03",

            "The guys on the roads are just a distraction.\x01",
            "The city's where things're gonna go down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1002F#2POh, yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x109,
        (
            "#1063F#2PTheir goal is nothing less than dominance\x01",
            "of the capital, I bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x10,
        (
            "#816FU-Understood!\x02\x03",

            "I'll run until my legs fall off!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)
    Sleep(400)

    ChrTalk(    #112
        0x101,
        "#1002FAnelace! Be careful, okay?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)

    ChrTalk(    #113
        0x10,
        "#811FI will! You too, Estelle!\x02",
    )

    CloseMessageWindow()

    def lambda_3372():

        label("loc_3372")

        TurnDirection(0x109, 0x10, 400)
        OP_48()
        Jump("loc_3372")

    QueueWorkItem2(0x109, 0, lambda_3372)

    def lambda_3383():

        label("loc_3383")

        TurnDirection(0x143, 0x10, 400)
        OP_48()
        Jump("loc_3383")

    QueueWorkItem2(0x143, 0, lambda_3383)
    OP_8C(0x10, 0, 400)

    def lambda_339B():
        OP_6D(119000, 0, 1990, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_339B)
    SetChrChipByIndex(0x10, 20)
    OP_8E(0x10, 0x1D394, 0x0, 0x125C, 0x1388, 0x0)
    OP_8E(0x10, 0x1E9D8, 0xFFFFF830, 0x125C, 0x1388, 0x0)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    def lambda_33EA():
        OP_6D(118020, 0, 400, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_33EA)
    OP_8C(0xB, 90, 400)

    def lambda_3409():
        OP_8C(0x101, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3409)
    Sleep(50)

    def lambda_341C():
        OP_8C(0x109, 270, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_341C)
    Sleep(50)

    def lambda_342F():
        OP_8C(0x143, 270, 400)
        ExitThread()

    QueueWorkItem(0x143, 0, lambda_342F)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #114
        0xB,
        (
            "#050F#6PPhillip, right?\x02\x03",

            "You mind stayin' here at the guildhouse?\x02\x03",

            "Don't worry, we'll get your duke back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x143,
        (
            "#720F#2PVery well.\x02\x03",

            "I will tend to your friends while I am here.\x02\x03",

            "Please...recover His Highness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3511")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4310   ._SN", 105, 0, 0)
    IdleLoop()
    Return()

    # Function_11_8B7 end

    def Function_12_3529(): pass

    label("Function_12_3529")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 90, -500, -7250, 0)

    def lambda_3550():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3550)
    OP_8E(0xFE, 0xFFFFFFEC, 0xFFFFFF7E, 0xFFFFEEA8, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_12_3529 end

    def Function_13_3578(): pass

    label("Function_13_3578")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 90, -500, -7250, 0)

    def lambda_359F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_359F)
    OP_8E(0xFE, 0x442, 0xFFFFFF7E, 0xFFFFEE94, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_13_3578 end

    def Function_14_35C7(): pass

    label("Function_14_35C7")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 90, -500, -7250, 0)

    def lambda_35EE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_35EE)
    OP_8E(0xFE, 0xFFFFFFD8, 0xFFFFFF06, 0xFFFFEA5C, 0x7D0, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_14_35C7 end

    def Function_15_3616(): pass

    label("Function_15_3616")

    OP_8E(0xFE, 0xFFFFEE80, 0x0, 0xFFFFF47A, 0x1388, 0x0)
    OP_8E(0xFE, 0xFFFFE9BC, 0x0, 0x26C, 0x1388, 0x0)
    TurnDirection(0xFE, 0x8, 400)
    Return()

    # Function_15_3616 end

    def Function_16_3646(): pass

    label("Function_16_3646")

    OP_8E(0xFE, 0xFFFFF5CE, 0x0, 0xFFFFF2F4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFECC8, 0x0, 0xFFFFF36C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFED86, 0x0, 0x0, 0xFA0, 0x0)
    Return()

    # Function_16_3646 end

    def Function_17_3683(): pass

    label("Function_17_3683")

    OP_8E(0xFE, 0xFFFFF5CE, 0x0, 0xFFFFF2F4, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFECC8, 0x0, 0xFFFFF36C, 0xFA0, 0x0)
    OP_8E(0xFE, 0xFFFFE99E, 0x0, 0xFFFFFC0E, 0xFA0, 0x0)
    Return()

    # Function_17_3683 end

    def Function_18_36C0(): pass

    label("Function_18_36C0")

    SetChrPos(0xFE, 60250, -2000, 4530, 270)
    OP_8E(0xFE, 0xD746, 0x0, 0x128E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xD764, 0x0, 0x744, 0xBB8, 0x0)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_18_36C0 end

    def Function_19_3712(): pass

    label("Function_19_3712")

    SetChrPos(0xFE, 60250, -2000, 4530, 270)
    OP_8E(0xFE, 0xD746, 0x0, 0x128E, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    TurnDirection(0xFE, 0xE, 400)
    Return()

    # Function_19_3712 end

    def Function_20_374B(): pass

    label("Function_20_374B")

    Sleep(1000)
    OP_8E(0xFE, 0xD764, 0x0, 0xA3C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xE15A, 0x0, 0xA3C, 0xBB8, 0x0)
    TurnDirection(0xFE, 0xE, 400)
    Return()

    # Function_20_374B end

    def Function_21_3780(): pass

    label("Function_21_3780")

    SetChrPos(0xFE, 125400, -2000, 4700, 270)
    OP_8E(0xFE, 0x1D394, 0x0, 0x125C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1D61E, 0x0, 0xFFFFFF6A, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_21_3780 end

    def Function_22_37C1(): pass

    label("Function_22_37C1")

    SetChrPos(0xFE, 125400, -2000, 4700, 270)
    OP_8E(0xFE, 0x1D394, 0x0, 0x125C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1D1C8, 0x0, 0xFFFFFF4C, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_22_37C1 end

    def Function_23_3802(): pass

    label("Function_23_3802")

    SetChrPos(0xFE, 58740, -2000, 4560, 270)
    OP_8E(0xFE, 0xD6B0, 0x0, 0x1310, 0x1388, 0x0)
    OP_8E(0xFE, 0xD5C0, 0x0, 0xE42, 0x1388, 0x0)
    Return()

    # Function_23_3802 end

    def Function_24_383C(): pass

    label("Function_24_383C")

    OP_8E(0xFE, 0x1BFDA, 0xFA, 0x230, 0xBB8, 0x0)
    OP_8E(0xFE, 0x1C9BC, 0x0, 0xFFFFFE0C, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 500)
    Return()

    # Function_24_383C end

    def Function_25_386C(): pass

    label("Function_25_386C")

    OP_8E(0xFE, 0x1D1B4, 0x0, 0x5DC, 0x7D0, 0x0)

    def lambda_3886():

        label("loc_3886")

        OP_8C(0xFE, 225, 400)
        OP_48()
        Jump("loc_3886")

    QueueWorkItem2(0xFE, 1, lambda_3886)
    Return()

    # Function_25_386C end

    def Function_26_3892(): pass

    label("Function_26_3892")

    FadeToDark(0, 0, -1)
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
        (0, "loc_390B"),
        (1, "loc_3911"),
        (SWITCH_DEFAULT, "loc_3917"),
    )


    label("loc_390B")

    OP_A2(0x1200)
    Jump("loc_3917")

    label("loc_3911")

    OP_A2(0x1201)
    Jump("loc_3917")

    label("loc_3917")

    Return()

    # Function_26_3892 end

    def Function_27_3918(): pass

    label("Function_27_3918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3929")
    OP_2A(0xBD, 0xBE, 0xFFFF)
    Jump("loc_3976")

    label("loc_3929")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_3940")
    OP_2A(0xAA, 0xAC, 0xC4, 0xAB, 0xA9, 0xFFFF)
    Jump("loc_3976")

    label("loc_3940")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_END)), "loc_3955")
    OP_2A(0xAA, 0xAC, 0xC4, 0xAB, 0xFFFF)
    Jump("loc_3976")

    label("loc_3955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_3968")
    OP_2A(0xAA, 0xAC, 0xC4, 0xFFFF)
    Jump("loc_3976")

    label("loc_3968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_3976")
    OP_2A(0xAA, 0xAC, 0xFFFF)

    label("loc_3976")

    TalkEnd(0xFF)
    Return()

    # Function_27_3918 end

    SaveToFile()

Try(main)
