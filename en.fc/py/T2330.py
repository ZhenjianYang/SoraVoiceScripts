from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2330   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2330.x',
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
        'Rex',                                  # 9
        'Carla',                                # 10
        'Matron Theresa',                       # 11
        'Daniel',                               # 12
        'Mary',                                 # 13
        'Polly',                                # 14
        'Clem',                                 # 15
        'Mayor Dalmore',                        # 16
        'Steward Gilbert',                      # 17
        'Carna',                                # 18
        'Alvin',                                # 19
        'Shelby',                               # 20
        'Lucia',                                # 21
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
        'ED6_DT07/CH01270 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
        'ED6_DT07/CH02640 ._CH',             # 02
        'ED6_DT07/CH02630 ._CH',             # 03
        'ED6_DT07/CH02570 ._CH',             # 04
        'ED6_DT07/CH02410 ._CH',             # 05
        'ED6_DT07/CH02420 ._CH',             # 06
        'ED6_DT07/CH01030 ._CH',             # 07
        'ED6_DT07/CH01240 ._CH',             # 08
        'ED6_DT07/CH02500 ._CH',             # 09
        'ED6_DT07/CH01020 ._CH',             # 0A
        'ED6_DT07/CH01140 ._CH',             # 0B
        'ED6_DT07/CH01070 ._CH',             # 0C
        'ED6_DT06/CH20093 ._CH',             # 0D
        'ED6_DT06/CH20101 ._CH',             # 0E
        'ED6_DT06/CH20053 ._CH',             # 0F
        'ED6_DT07/CH01023 ._CH',             # 10
        'ED6_DT07/CH01143 ._CH',             # 11
    )

    AddCharChipPat(
        'ED6_DT07/CH01270P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
        'ED6_DT07/CH02640P._CP',             # 02
        'ED6_DT07/CH02630P._CP',             # 03
        'ED6_DT07/CH02570P._CP',             # 04
        'ED6_DT07/CH02410P._CP',             # 05
        'ED6_DT07/CH02420P._CP',             # 06
        'ED6_DT07/CH01030P._CP',             # 07
        'ED6_DT07/CH01240P._CP',             # 08
        'ED6_DT07/CH02500P._CP',             # 09
        'ED6_DT07/CH01020P._CP',             # 0A
        'ED6_DT07/CH01140P._CP',             # 0B
        'ED6_DT07/CH01070P._CP',             # 0C
        'ED6_DT06/CH20093P._CP',             # 0D
        'ED6_DT06/CH20101P._CP',             # 0E
        'ED6_DT06/CH20053P._CP',             # 0F
        'ED6_DT07/CH01023P._CP',             # 10
        'ED6_DT07/CH01143P._CP',             # 11
    )

    DeclNpc(
        X                   = -25500,
        Z                   = 0,
        Y                   = 43210,
        Direction           = 270,
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
        X                   = -37500,
        Z                   = 0,
        Y                   = 44500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -50190,
        Z                   = 0,
        Y                   = -1000,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -50850,
        Z                   = 0,
        Y                   = 180,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -50850,
        Z                   = 0,
        Y                   = 1400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -50570,
        Z                   = 0,
        Y                   = -2840,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -49420,
        Z                   = 0,
        Y                   = -2280,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1200,
        Z                   = 4000,
        Y                   = 16700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -400,
        Z                   = 0,
        Y                   = 45400,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = -33200,
        Z                   = 150,
        Y                   = 41740,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -32060,
        Z                   = 150,
        Y                   = 42960,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -23900,
        Z                   = 0,
        Y                   = -1170,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )


    DeclActor(
        TriggerX            = -37020,
        TriggerZ            = 0,
        TriggerY            = 42970,
        TriggerRange        = 400,
        ActorX              = -37500,
        ActorZ              = 1500,
        ActorY              = 44500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26870,
        TriggerZ            = 0,
        TriggerY            = 42820,
        TriggerRange        = 400,
        ActorX              = -25500,
        ActorZ              = 1500,
        ActorY              = 43210,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_322",          # 00, 0
        "Function_1_5C7",          # 01, 1
        "Function_2_611",          # 02, 2
        "Function_3_627",          # 03, 3
        "Function_4_62C",          # 04, 4
        "Function_5_1964",         # 05, 5
        "Function_6_1969",         # 06, 6
        "Function_7_21B7",         # 07, 7
        "Function_8_2951",         # 08, 8
        "Function_9_31C7",         # 09, 9
        "Function_10_372B",        # 0A, 10
        "Function_11_37FA",        # 0B, 11
        "Function_12_38F4",        # 0C, 12
        "Function_13_398B",        # 0D, 13
        "Function_14_3A3A",        # 0E, 14
        "Function_15_3AE4",        # 0F, 15
        "Function_16_3BA5",        # 10, 16
        "Function_17_68EC",        # 11, 17
        "Function_18_6907",        # 12, 18
        "Function_19_6918",        # 13, 19
        "Function_20_6929",        # 14, 20
        "Function_21_693A",        # 15, 21
        "Function_22_6950",        # 16, 22
        "Function_23_7F9D",        # 17, 23
        "Function_24_7FBE",        # 18, 24
        "Function_25_7FDF",        # 19, 25
        "Function_26_8000",        # 1A, 26
        "Function_27_802E",        # 1B, 27
        "Function_28_8061",        # 1C, 28
        "Function_29_8094",        # 1D, 29
        "Function_30_80C7",        # 1E, 30
    )


    def Function_0_322(): pass

    label("Function_0_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_32C")
    Jump("loc_591")

    label("loc_32C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_393")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -48350, 0, 150, 215)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -50850, 0, 180, 135)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -50570, 0, -2840, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -49420, 0, -2280, 315)
    Jump("loc_591")

    label("loc_393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_42B")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, -53290, 0, 2040, 180)
    SetChrPos(0xA, -53080, 0, -870, 180)
    SetChrPos(0xB, -50850, 0, -230, 270)
    SetChrPos(0xD, -50850, 0, -1430, 270)
    SetChrPos(0xC, -52530, 0, -2420, 0)
    SetChrPos(0xE, -50800, 0, 1470, 270)
    Jump("loc_591")

    label("loc_42B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_502")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x10)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x11, -53000, 0, 2040, 90)
    SetChrPos(0xA, -53000, 0, -870, 90)
    SetChrChipByIndex(0xA, 13)
    SetChrChipByIndex(0x11, 14)
    OP_44(0x11, 0xFF)
    OP_44(0xA, 0xFF)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrPos(0xB, -50850, 0, -230, 270)
    SetChrPos(0xD, -50850, 0, -1430, 270)
    SetChrPos(0xC, -52530, 0, -2420, 0)
    SetChrPos(0xE, -50800, 0, 1470, 270)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_591")

    label("loc_502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_511")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_591")

    label("loc_511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_562")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -48450, 0, -990, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -49210, 0, -2360, 315)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -47720, 0, 2100, 0)
    Jump("loc_591")

    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_56C")
    Jump("loc_591")

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_576")
    Jump("loc_591")

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_580")
    Jump("loc_591")

    label("loc_580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_58A")
    Jump("loc_591")

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_591")

    label("loc_591")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (107, "loc_59D"),
        (SWITCH_DEFAULT, "loc_5C6"),
    )


    label("loc_59D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B0")
    OP_A2(0x428)
    Event(0, 16)

    label("loc_5B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C3")
    OP_A2(0x436)
    Event(0, 22)

    label("loc_5C3")

    Jump("loc_5C6")

    label("loc_5C6")

    Return()

    # Function_0_322 end

    def Function_1_5C7(): pass

    label("Function_1_5C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F7")
    OP_B1("t2330_y")
    OP_72(0x2, 0x20)
    OP_6F(0x2, 15)
    OP_72(0x4, 0x20)
    OP_6F(0x4, 15)
    Jump("loc_600")

    label("loc_5F7")

    OP_B1("t2330_n")

    label("loc_600")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_610")
    OP_64(0x0, 0x1)

    label("loc_610")

    Return()

    # Function_1_5C7 end

    def Function_2_611(): pass

    label("Function_2_611")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_626")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_611")

    label("loc_626")

    Return()

    # Function_2_611 end

    def Function_3_627(): pass

    label("Function_3_627")

    Call(0, 4)
    Return()

    # Function_3_627 end

    def Function_4_62C(): pass

    label("Function_4_62C")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                             # 0
            "Shop\x01",                             # 1
            "[Diehard Paella] - 500 mira\x01",      # 2
            "Leave\x01",                            # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A8")
    OP_0D()
    OP_A9(0x2A)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_6A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_77A")
    SubMira(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06\x07\x00Ate \x07\x02Diehard Paella\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x1C2)
    OP_31(0x1, 0xFD, 0x1C2)
    OP_31(0x2, 0xFD, 0x1C2)
    OP_31(0x3, 0xFD, 0x1C2)
    OP_31(0x4, 0xFD, 0x1C2)
    OP_31(0x5, 0xFD, 0x1C2)
    OP_31(0x6, 0xFD, 0x1C2)
    OP_31(0x7, 0xFD, 0x1C2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x1)"), scpexpr(EXPR_END)), "loc_73C")
    Jump("loc_76C")

    label("loc_73C")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06\x07\x00Learned '\x07\x02Diehard Paella\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_76C")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_7A2")

    label("loc_77A")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_7A2")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x8)
    Return()

    label("loc_7B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C5")
    TalkEnd(0x8)
    Return()

    label("loc_7C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F8F")
    EventBegin(0x0)
    OP_69(0x8, 0x320)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5E")

    ChrTalk(    #3
        0x8,
        "Welcome to the White Magnolia.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "I don't recall seeing you before.\x01",
            "Are you here on vacation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#006FNo, we're just passing through\x01",
            "on our way to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        (
            "#010FWe came from Bose, by way\x01",
            "of the Krone Pass.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        "You're joking!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        (
            "Wow...I never thought I'd meet another\x01",
            "person brave enough to handle that\x01",
            "place, in this day and age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "You're into hiking, I assume?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#501FNo, not especially.\x02\x03",

            "#501FIt sure works up an appetite,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        (
            "#010FIs there anything you'd\x01",
            "particularly recommend?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "Oh, yes...I'd suggest trying\x01",
            "the box lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#004FWhat's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "That windmill at the edge of town\x01",
            "has a platform with a great view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "Every day at lunch, lots of\x01",
            "people buy them and take them\x01",
            "there to eat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#001FOh, that might be nice.♪\x02\x03",

            "From what you're saying,\x01",
            "it sounds like something\x01",
            "I'd like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        (
            "#019FWell, why don't we try it?\x02\x03",

            "#010FWhat kind of box lunches\x01",
            "are there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "Well, there's the smoked ham\x01",
            "sandwich and the seafood paella...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        (
            "Either would be good,\x01",
            "in my opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#501FHmm...I think I'll try the sandwich.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        "#010FThen I'll have the seafood paella.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "Thank you. That'll be 120 mira.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CCD")

    label("loc_C5E")


    ChrTalk(    #23
        0x8,
        (
            "My two favorite box lunches are\x01",
            "the smoked ham sandwich and\x01",
            "the seafood paella.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x8,
        "That'll be 120 mira.\x02",
    )

    CloseMessageWindow()

    label("loc_CCD")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Buy]\x01",             # 0
            "[Never mind]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D31"),
        (1, "loc_EBF"),
        (SWITCH_DEFAULT, "loc_F8A"),
    )


    label("loc_D31")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E62")
    OP_4F(0x12, (scpexpr(EXPR_PUSH_LONG, 0x78), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    OP_22(0x14, 0x0, 0x64)
    Sleep(1000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #25
        "\x07\x00Received '\x07\x02Special Boxed Lunch\x07\x00'.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x33C, 1)

    ChrTalk(    #26
        0x8,
        (
            "And I'll toss in some herb tea\x01",
            "at no charge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        "It's my specialty.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        "#001FThanks! ㈱\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #29
        0x102,
        (
            "#010FWant to go over to the\x01",
            "viewing platform?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #30
        0x101,
        "#006FSure!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x413)
    Jump("loc_EBC")

    label("loc_E62")


    ChrTalk(    #31
        0x8,
        (
            "Oh...it looks like you don't\x01",
            "have enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "Perhaps you could come\x01",
            "back later?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x401)

    label("loc_EBC")

    Jump("loc_F8A")

    label("loc_EBF")


    ChrTalk(    #33
        0x8,
        "Would you prefer to eat here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "We do have several other items\x01",
            "on the menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#007FAww, I kinda had my heart\x01",
            "set on eating outside.\x02\x03",

            "#008FI'm sorry. Let me think on\x01",
            "it for a little bit.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x401)
    Jump("loc_F8A")

    label("loc_F8A")

    EventEnd(0x1)
    Jump("loc_1960")

    label("loc_F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_113C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_108D")
    OP_A2(0x0)

    ChrTalk(    #36
        0x8,
        (
            "I'm not surprised that Steward\x01",
            "Gilbert is a criminal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x8,
        (
            "But even so, it's hard to believe\x01",
            "that the mayor would be involved\x01",
            "in something that terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "I guess he'll have the rest of his\x01",
            "life to pay for what he's done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1139")

    label("loc_108D")


    ChrTalk(    #39
        0x8,
        (
            "But even so, it's hard to believe\x01",
            "that the mayor would be involved\x01",
            "in something that terrible.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "I guess he'll have the rest of his\x01",
            "life to pay for what he's done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1139")

    Jump("loc_1960")

    label("loc_113C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_12A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120B")
    OP_A2(0x0)

    ChrTalk(    #41
        0x8,
        (
            "I think I've seen the person who\x01",
            "did this before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        (
            "I have to wonder if it was the\x01",
            "mayor's personal steward...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x8,
        (
            "I must be mistaken though...\x01",
            "It's too crazy to be possible.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12A2")

    label("loc_120B")


    ChrTalk(    #44
        0x8,
        (
            "I can't help thinking that the\x01",
            "criminal looked kind of like\x01",
            "the mayor's steward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        (
            "I must be mistaken though...\x01",
            "It's too crazy to be possible.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A2")

    Jump("loc_1960")

    label("loc_12A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_136A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1330")
    OP_A2(0x0)

    ChrTalk(    #46
        0x8,
        (
            "If you're looking for the matron,\x01",
            "she's upstairs resting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x8,
        (
            "First the arson, and now this...\x01",
            "those poor kids.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1367")

    label("loc_1330")


    ChrTalk(    #48
        0x8,
        (
            "First the arson, and now this...\x01",
            "those poor kids.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1367")

    Jump("loc_1960")

    label("loc_136A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_14C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_143A")
    OP_A2(0x0)

    ChrTalk(    #49
        0x8,
        (
            "It's almost time for the\x01",
            "campus festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "I think the kids from the\x01",
            "orphanage are going, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        (
            "I just hope they can forget about\x01",
            "all this mess, at least for a\x01",
            "little while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C6")

    label("loc_143A")


    ChrTalk(    #52
        0x8,
        (
            "I think the kids from the\x01",
            "orphanage are going, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x8,
        (
            "I just hope they can forget about\x01",
            "all this mess, at least for a\x01",
            "little while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C6")

    Jump("loc_1960")

    label("loc_14C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1539")

    ChrTalk(    #54
        0x8,
        (
            "I saw a boy from the orphanage go\x01",
            "running by, a little while ago...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        "I wonder what happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1960")

    label("loc_1539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_1653")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1605")
    OP_A2(0x0)

    ChrTalk(    #56
        0x8,
        (
            "Was everything destroyed in\x01",
            "the fire at the orphanage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x8,
        (
            "I went ahead and let the kids\x01",
            "use my room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "If you wouldn't mind, could you go\x01",
            "and try to cheer them up a little?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1650")

    label("loc_1605")


    ChrTalk(    #59
        0x8,
        (
            "If you wouldn't mind, could you go\x01",
            "and try to cheer them up a little?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1650")

    Jump("loc_1960")

    label("loc_1653")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_16A3")

    ChrTalk(    #60
        0x8,
        "Not much wind today...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "It'd be nice to walk on\x01",
            "the beach...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1960")

    label("loc_16A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_181C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179F")
    OP_A2(0x0)

    ChrTalk(    #62
        0x8,
        (
            "We get lots of people here who\x01",
            "come to check out the scenery.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "The others are mountain climbers,\x01",
            "like those two, over there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        (
            "Used to be, we got all our\x01",
            "business from people going back\x01",
            "and forth between Ruan and Bose.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1819")

    label("loc_179F")


    ChrTalk(    #65
        0x8,
        (
            "How was the view from\x01",
            "the windmill?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "I never get tired of the sight\x01",
            "of the windmill and the blue\x01",
            "ocean together.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1819")

    Jump("loc_1960")

    label("loc_181C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_18BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1895")
    OP_A2(0x0)

    ChrTalk(    #67
        0x8,
        "Hey, weren't you here earlier?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x8,
        "Is everything okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "A little boy?\x01",
            "Haven't seen him...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18BC")

    label("loc_1895")


    ChrTalk(    #70
        0x8,
        (
            "A little boy?\x01",
            "Haven't seen him...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18BC")

    Jump("loc_1960")

    label("loc_18BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_1960")

    ChrTalk(    #71
        0x8,
        (
            "That windmill at the edge of\x01",
            "town has a platform with a\x01",
            "fantastic view.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        (
            "Every day at lunch, lots of\x01",
            "people buy them and take\x01",
            "them there to eat.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1960")

    TalkEnd(0x8)
    Return()

    # Function_4_62C end

    def Function_5_1964(): pass

    label("Function_5_1964")

    Call(0, 6)
    Return()

    # Function_5_1964 end

    def Function_6_1969(): pass

    label("Function_6_1969")

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
            "Rest\x01",       # 1
            "Leave\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C9")
    OP_0D()
    OP_A9(0x29)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_19C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19DA")
    TalkEnd(0x9)
    Return()

    label("loc_19DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A56")

    ChrTalk(    #73
        0x9,
        (
            "I asked everyone from the \x01",
            "orphanage to stay here,\x01",
            "until they can rebuild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x9,
        "We've had a good bit of fun.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21B3")

    label("loc_1A56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_1B0C")

    ChrTalk(    #75
        0x9,
        (
            "I heard that the arsonist\x01",
            "was caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x9,
        (
            "I think he should experience some\x01",
            "street justice before he's turned\x01",
            "over to the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        "Maybe a good stoning...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_21B3")

    label("loc_1B0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_1B56")

    ChrTalk(    #78
        0x9,
        "How could this have happened?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        "I won't stand for this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_21B3")

    label("loc_1B56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_1C4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF9")
    OP_A2(0x1)

    ChrTalk(    #80
        0x9,
        (
            "The orphans and Matron Theresa\x01",
            "are being well looked after,\x01",
            "never you fear.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        (
            "We have to come together in\x01",
            "times of trouble, you know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C4A")

    label("loc_1BF9")


    ChrTalk(    #82
        0x9,
        (
            "The orphans and Matron Theresa\x01",
            "are being well looked after,\x01",
            "never you fear.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4A")

    Jump("loc_21B3")

    label("loc_1C4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_1CA9")

    ChrTalk(    #83
        0x9,
        "I think Clem just ran out of here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x9,
        (
            "I wonder what could be\x01",
            "the matter?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21B3")

    label("loc_1CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_1E94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E04")
    OP_A2(0x1)
    TurnDirection(0x9, 0x136, 0)

    ChrTalk(    #85
        0x9,
        (
            "Oh, that's a royal academy\x01",
            "uniform...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x9,
        (
            "Is your name Kloe,\x01",
            "by any chance?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x136,
        "#044FYes...why do you ask?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x9,
        (
            "The children from the orphanage\x01",
            "talk about you a great deal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "They're all upstairs in the\x01",
            "big room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "You should go and see them,\x01",
            "whenever you get the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x136,
        "#043FOh...I will. Pardon me.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E91")

    label("loc_1E04")

    TurnDirection(0x9, 0x136, 0)

    ChrTalk(    #92
        0x9,
        (
            "The children from the orphanage\x01",
            "talk about you a great deal, Kloe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        (
            "You should go and see them,\x01",
            "whenever you get the chance.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E91")

    Jump("loc_21B3")

    label("loc_1E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_1F87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F2F")
    OP_A2(0x1)

    ChrTalk(    #94
        0x9,
        (
            "Okay...next up is getting the\x01",
            "laundry done.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        (
            "Today's supposed to be sunny,\x01",
            "so I'll have no better chance\x01",
            "to dry the clothes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F84")

    label("loc_1F2F")


    ChrTalk(    #96
        0x9,
        (
            "Today's supposed to be sunny,\x01",
            "so I'll have no better chance\x01",
            "to dry the clothes.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F84")

    Jump("loc_21B3")

    label("loc_1F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2048")

    ChrTalk(    #97
        0x9,
        (
            "The magnolias are blooming\x01",
            "in twos and threes again,\x01",
            "this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "This village has no particular specialties,\x01",
            "but we sometimes have some people who come\x01",
            "to see those flowers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21B3")

    label("loc_2048")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_20B7")

    ChrTalk(    #99
        0x9,
        (
            "A little boy?\x01",
            "Nope, I haven't seen him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x9,
        (
            "I did see a girl from the royal\x01",
            "academy, though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21B3")

    label("loc_20B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_21B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_217F")
    OP_A2(0x1)

    ChrTalk(    #101
        0x9,
        "Welcome, welcome!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "Care for some food? We'd be happy\x01",
            "to have you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        (
            "I make it all myself, with the\x01",
            "help of my husband, and I'm quite\x01",
            "confident you'll love every bite!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21B3")

    label("loc_217F")


    ChrTalk(    #104
        0x9,
        (
            "Care for some food? We'd be happy\x01",
            "to have you!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21B3")

    TalkEnd(0x9)
    Return()

    # Function_6_1969 end

    def Function_7_21B7(): pass

    label("Function_7_21B7")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_221D")

    ChrTalk(    #105
        0xFE,
        (
            "All right, time to get back\x01",
            "to climbing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "The peaks of Krone are calling\x01",
            "to me!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_294D")

    label("loc_221D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_22B0")

    ChrTalk(    #107
        0xFE,
        "Hah...the arsonist was caught.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "I'd like to take the bastard up\x01",
            "into the mountains to teach him\x01",
            "a lesson or two about survival.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_294D")

    label("loc_22B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_236C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2325")
    OP_A2(0x2)

    ChrTalk(    #109
        0xFE,
        "The kids were mugged?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x12, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #110
        0xFE,
        (
            "What the hell?\x01",
            "When does it stop?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2369")

    label("loc_2325")


    ChrTalk(    #111
        0xFE,
        "The kids were mugged?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "What the hell?\x01",
            "When does it stop?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2369")

    Jump("loc_294D")

    label("loc_236C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2545")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24AE")
    OP_A2(0x2)

    ChrTalk(    #113
        0xFE,
        (
            "The weather's perfect for scaling\x01",
            "that mountain I've had my sights\x01",
            "set on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "But I can't stop worrying about\x01",
            "the kids from the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "I still want to watch out for them,\x01",
            "at least for a little while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "I know I'm not the most\x01",
            "dependable person around,\x01",
            "but I have to do something.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2542")

    label("loc_24AE")


    ChrTalk(    #117
        0xFE,
        (
            "The weather's perfect for scaling\x01",
            "that mountain I've had my sights\x01",
            "set on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "But I can't stop worrying about\x01",
            "the kids from the orphanage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2542")

    Jump("loc_294D")

    label("loc_2545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_25BA")

    ChrTalk(    #119
        0xFE,
        (
            "Is it true that someone set\x01",
            "fire to the orphanage?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "There are some real lowlifes\x01",
            "in this world...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_294D")

    label("loc_25BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_260E")

    ChrTalk(    #121
        0xFE,
        "I heard the kids crying upstairs...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "What in the world happened?\x02",
    )

    CloseMessageWindow()
    Jump("loc_294D")

    label("loc_260E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_276C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E4")
    OP_A2(0x2)

    ChrTalk(    #123
        0xFE,
        "I love the mountains!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "There's nothing as refreshing as\x01",
            "waking up early and smelling\x01",
            "that mountain air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "Plus there's the feel of it on\x01",
            "your skin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "Man, I want to go climbing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2769")

    label("loc_26E4")


    ChrTalk(    #127
        0xFE,
        (
            "There's nothing as refreshing as\x01",
            "waking up early and smelling\x01",
            "that mountain air.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Plus there's the feel of it on\x01",
            "your skin.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2769")

    Jump("loc_294D")

    label("loc_276C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2870")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2837")
    OP_A2(0x2)

    ChrTalk(    #129
        0xFE,
        "Man, I want to go mountain climbing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "You want to know why I\x01",
            "climb mountains?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "That's a silly question.\x01",
            "Because they're there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#506FUmmm...I didn't actually ask...\x02",
    )

    CloseMessageWindow()
    Jump("loc_286D")

    label("loc_2837")


    ChrTalk(    #133
        0xFE,
        (
            "Why do I climb mountains?\x01",
            "Because they're there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_286D")

    Jump("loc_294D")

    label("loc_2870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_28BB")

    ChrTalk(    #134
        0xFE,
        "Hmm...a boy in a cap, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "I don't think I've seen him.\x02",
    )

    CloseMessageWindow()
    Jump("loc_294D")

    label("loc_28BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_294D")

    ChrTalk(    #136
        0xFE,
        (
            "We're all woodsmen, hikers,\x01",
            "and mountain nuts here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "We came to Manoria so that we\x01",
            "could do some climbing in the\x01",
            "Krone mountains.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_294D")

    TalkEnd(0x12)
    Return()

    # Function_7_21B7 end

    def Function_8_2951(): pass

    label("Function_8_2951")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_29C9")

    ChrTalk(    #138
        0xFE,
        (
            "Hmm...too much snow on the\x01",
            "south face for it to be safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "I guess we'll have to plan\x01",
            "a new route.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C3")

    label("loc_29C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_2A73")

    ChrTalk(    #140
        0xFE,
        (
            "Hmph...so the criminals have finally\x01",
            "been caught.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "That should help put my friend's\x01",
            "mind a little more at ease.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        "I feel pretty good about it, too.\x02",
    )

    CloseMessageWindow()
    Jump("loc_31C3")

    label("loc_2A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_2B17")

    ChrTalk(    #143
        0xFE,
        (
            "I wonder if the muggers and the\x01",
            "arsonists are the same people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "There are some things that no sane\x01",
            "person could ever do. It makes me\x01",
            "so angry...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C3")

    label("loc_2B17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_2B9D")

    ChrTalk(    #145
        0xFE,
        (
            "Hmm...I guess we can go climbing\x01",
            "as much as we want, now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "I can't say that either of us\x01",
            "sees that as a bad thing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C3")

    label("loc_2B9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_2C1E")

    ChrTalk(    #147
        0xFE,
        (
            "By the looks of the weather,\x01",
            "we should be able to take on\x01",
            "the Krone mountains soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        "Our wait has paid off...\x02",
    )

    CloseMessageWindow()
    Jump("loc_31C3")

    label("loc_2C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 4)), scpexpr(EXPR_END)), "loc_2C54")

    ChrTalk(    #149
        0xFE,
        (
            "Hmm...something unusual is\x01",
            "going on...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C3")

    label("loc_2C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 1)), scpexpr(EXPR_END)), "loc_2EA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DEE")
    OP_A2(0x3)

    ChrTalk(    #150
        0xFE,
        (
            "The Krone mountains push out into\x01",
            "Valleria Lake like a small peninsula.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "You've got to have climbing gear,\x01",
            "because of the sheer elevation\x01",
            "involved.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "The season and weather are important,\x01",
            "but you've also got to plan out the right\x01",
            "route.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "Right now, we're just waiting for\x01",
            "the weather to settle down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xFE,
        (
            "It's fine here, but it's still pretty\x01",
            "nasty up in the mountaintops.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E9D")

    label("loc_2DEE")


    ChrTalk(    #155
        0xFE,
        (
            "To climb the Krone mountains,\x01",
            "you need a level head, as well\x01",
            "as the right equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "Right now, we're just waiting\x01",
            "here for the weather to settle\x01",
            "down a little bit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E9D")

    Jump("loc_31C3")

    label("loc_2EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_2FFB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F72")
    OP_A2(0x3)

    ChrTalk(    #157
        0xFE,
        (
            "We've got all the provisions\x01",
            "we need, so now we're getting\x01",
            "the equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xFE,
        (
            "Last time we were here, the weather\x01",
            "stayed too nasty for us to climb,\x01",
            "but it's looking better this time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FF8")

    label("loc_2F72")


    ChrTalk(    #159
        0xFE,
        (
            "It goes without saying that mountains\x01",
            "are very dangerous places.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xFE,
        (
            "My friend, Alvin, wants to take\x01",
            "every possible precaution.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FF8")

    Jump("loc_31C3")

    label("loc_2FFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_30F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30BE")
    OP_A2(0x3)

    ChrTalk(    #161
        0xFE,
        (
            "A little boy...? Anything special\x01",
            "about him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x101,
        (
            "#505FHmm...well, he was wearing a\x01",
            "cap, and he's kind of a brat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "Sorry...I haven't seen him.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        "#501FOh, well...\x02",
    )

    CloseMessageWindow()
    Jump("loc_30EF")

    label("loc_30BE")


    ChrTalk(    #165
        0xFE,
        (
            "A little boy...? Sorry, I haven't\x01",
            "seen him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30EF")

    Jump("loc_31C3")

    label("loc_30F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 6)), scpexpr(EXPR_END)), "loc_31C3")

    ChrTalk(    #166
        0xFE,
        "We're self-proclaimed mountaineers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0xFE,
        (
            "I know Manoria is the best place to set\x01",
            "off for a trek up the Krone mountains...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "We're just trying to get everything\x01",
            "we need to make the climb safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31C3")

    TalkEnd(0x13)
    Return()

    # Function_8_2951 end

    def Function_9_31C7(): pass

    label("Function_9_31C7")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_31D4")
    Jump("loc_3727")

    label("loc_31D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_3448")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F8")
    OP_A2(0x4)

    ChrTalk(    #169
        0xFE,
        (
            "#750FOh, my...hello again.\x02\x03",

            "I heard from the innkeeper that\x01",
            "the criminals have been arrested.\x02\x03",

            "You keep helping us so much and\x01",
            "I've no way to properly repay you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#008FYou really don't need to worry...\x01",
            "It's nothing to be embarrassed\x01",
            "over.\x02\x03",

            "#008FReally...\x02\x03",

            "#503F(Hmm...it's probably better not\x01",
            "to tell her everything, just yet.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x102,
        (
            "#010FWe're going back to Ruan for a little\x01",
            "bit, so we can deliver our report.\x02\x03",

            "Carna's keeping an eye on the\x01",
            "prisoners, so you can relax on\x01",
            "that score.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        "#750FThank you so much...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3445")

    label("loc_33F8")


    ChrTalk(    #173
        0xFE,
        (
            "#750FYou keep helping us so much and\x01",
            "I've no way to properly repay you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3445")

    Jump("loc_3727")

    label("loc_3448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_3480")

    AnonymousTalk(    #174
        "\x07\x05Matron Theresa is sleeping peacefully.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_3727")

    label("loc_3480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 5)), scpexpr(EXPR_END)), "loc_35DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_355B")
    OP_A2(0x4)

    ChrTalk(    #175
        0xFE,
        (
            "#750FOh, hello...\x02\x03",

            "I'm truly indebted to you, for a\x01",
            "multitude of reasons...\x02\x03",

            "The Manorians greatly appreciate \x01",
            "all that you've done.\x02\x03",

            "#751FI'm really grateful to everyone\x01",
            "for all they've done.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35DA")

    label("loc_355B")


    ChrTalk(    #176
        0xFE,
        (
            "#750FI'm truly indebted to you, for a\x01",
            "multitude of reasons...\x02\x03",

            "#751FI'm really grateful to everyone\x01",
            "for all they've done.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35DA")

    Jump("loc_3727")

    label("loc_35DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3727")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_369C")
    OP_A2(0x4)

    ChrTalk(    #177
        0xFE,
        (
            "#756FMary told me what happened...\x02\x03",

            "This is terrible... What an awful\x01",
            "thing for him to overhear...\x02\x03",

            "#752FI beg of you...please, find Clem\x01",
            "and bring him back safely.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3727")

    label("loc_369C")


    ChrTalk(    #178
        0xFE,
        (
            "#756FThis is terrible... What an awful\x01",
            "thing for him to overhear...\x02\x03",

            "#752FI beg of you...please, find Clem\x01",
            "and bring him back safely.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3727")

    TalkEnd(0xFE)
    Return()

    # Function_9_31C7 end

    def Function_10_372B(): pass

    label("Function_10_372B")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3738")
    Jump("loc_37F6")

    label("loc_3738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_379F")

    ChrTalk(    #179
        0xFE,
        (
            "#770FOh...hi, Miss Estelle!\x02\x03",

            "Did you really find those guys\x01",
            "and beat them up?\x02\x03",

            "Awesome!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37F6")

    label("loc_379F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_37F6")

    ChrTalk(    #180
        0xFE,
        (
            "#770FMister Joshua...\x02\x03",

            "I hope I grow up to be as strong\x01",
            "as you, someday...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37F6")

    TalkEnd(0xE)
    Return()

    # Function_10_372B end

    def Function_11_37FA(): pass

    label("Function_11_37FA")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3807")
    Jump("loc_38F0")

    label("loc_3807")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_3865")

    ChrTalk(    #181
        0xFE,
        (
            "The matron finally woke up,\x01",
            "earlier this morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xFE,
        "Hee hee...thank Aidios.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38F0")

    label("loc_3865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_38D1")

    ChrTalk(    #183
        0xFE,
        (
            "Everyone's finally calmed down\x01",
            "a little bit...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0xFE,
        (
            "Now, if the matron would\x01",
            "just wake up...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38F0")

    label("loc_38D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_38F0")

    ChrTalk(    #185
        0xFE,
        "Please, find Clem!\x02",
    )

    CloseMessageWindow()

    label("loc_38F0")

    TalkEnd(0xC)
    Return()

    # Function_11_37FA end

    def Function_12_38F4(): pass

    label("Function_12_38F4")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3901")
    Jump("loc_3987")

    label("loc_3901")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_393F")

    ChrTalk(    #186
        0xFE,
        (
            "Man...I'm so relieved.\x01",
            "Now I'm staaaaarving...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3987")

    label("loc_393F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_395E")

    ChrTalk(    #187
        0xFE,
        "*hic* *sniffle*\x02",
    )

    CloseMessageWindow()
    Jump("loc_3987")

    label("loc_395E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3987")

    ChrTalk(    #188
        0xFE,
        "What got Clem all worked up?\x02",
    )

    CloseMessageWindow()

    label("loc_3987")

    TalkEnd(0xB)
    Return()

    # Function_12_38F4 end

    def Function_13_398B(): pass

    label("Function_13_398B")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3998")
    Jump("loc_3A36")

    label("loc_3998")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_END)), "loc_39C4")

    ChrTalk(    #189
        0xFE,
        "Yaaaay! Matron's uppy again!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A36")

    label("loc_39C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_39F0")

    ChrTalk(    #190
        0xFE,
        "Matron's gon'be okay, right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A36")

    label("loc_39F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x85, 0)), scpexpr(EXPR_END)), "loc_3A36")

    ChrTalk(    #191
        0xFE,
        (
            "Clem din't say anyfing since\x01",
            "when we were eatin' puddin'.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A36")

    TalkEnd(0xD)
    Return()

    # Function_13_398B end

    def Function_14_3A3A(): pass

    label("Function_14_3A3A")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 5)), scpexpr(EXPR_END)), "loc_3AB4")

    ChrTalk(    #192
        0xFE,
        (
            "I'm guarding the donations until\x01",
            "the matron wakes up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xFE,
        (
            "I won't fail this time.\x01",
            "You can count on me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AE0")

    label("loc_3AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_3AE0")

    AnonymousTalk(    #194
        "\x07\x05Carna is sleeping peacefully.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_3AE0")

    TalkEnd(0x11)
    Return()

    # Function_14_3A3A end

    def Function_15_3AE4(): pass

    label("Function_15_3AE4")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 5)), scpexpr(EXPR_END)), "loc_3BA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B71")
    OP_A2(0x9)

    ChrTalk(    #195
        0xFE,
        (
            "All the orphans have been crying\x01",
            "ever since they got back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "Why? Why would anybody pick\x01",
            "on them like that?!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BA1")

    label("loc_3B71")


    ChrTalk(    #197
        0xFE,
        (
            "Why would anybody pick\x01",
            "on them like that?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BA1")

    TalkEnd(0x14)
    Return()

    # Function_15_3AE4 end

    def Function_16_3BA5(): pass

    label("Function_16_3BA5")

    EventBegin(0x0)
    OP_6D(-50180, 0, -790, 0)
    OP_6B(2800, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xA, -52390, 0, 510, 90)
    SetChrPos(0xB, -50850, 0, 180, 315)
    SetChrPos(0xD, -50850, 0, 1400, 225)
    SetChrPos(0xC, -50570, 0, -2840, 45)
    SetChrPos(0xE, -49420, 0, -2280, 225)
    SetChrPos(0x101, -46270, 0, -1540, 270)
    SetChrPos(0x102, -46100, 0, -760, 270)
    SetChrPos(0x136, -47050, 0, -1030, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #198
        0x136,
        "#043FMatron! Everyone...!\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_4A(0xD, 255)
    OP_4A(0xC, 255)
    OP_4A(0xE, 255)

    def lambda_3D31():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3D31)

    def lambda_3D3F():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3D3F)

    def lambda_3D4D():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3D4D)

    def lambda_3D5B():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3D5B)

    def lambda_3D69():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3D69)
    Sleep(400)

    ChrTalk(    #199
        0xE,
        "#774FMiss Kloe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xC,
        "You came!\x02",
    )

    CloseMessageWindow()

    def lambda_3DA0():
        OP_6D(-50670, 0, -380, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3DA0)

    def lambda_3DB8():
        OP_8F(0xFE, 0xFFFF41A6, 0x0, 0xFFFFFE8E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_3DB8)
    Sleep(100)

    def lambda_3DD8():
        OP_8E(0xFE, 0xFFFF3DD2, 0x0, 0x21C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3DD8)
    Sleep(100)

    def lambda_3DF8():
        OP_8E(0xFE, 0xFFFF3D5A, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_3DF8)

    def lambda_3E13():
        OP_8E(0xFE, 0xFFFF3FD0, 0x0, 0xFFFFFB50, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_3E13)
    Sleep(100)

    def lambda_3E33():
        OP_8E(0xFE, 0xFFFF4322, 0x0, 0xFFFFFBD2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_3E33)
    WaitChrThread(0xE, 0x2)
    TurnDirection(0xE, 0x136, 400)

    ChrTalk(    #201
        0x136,
        "#042F#2PIs anyone hurt?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xB,
        "#1PWe're okay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xD,
        "#2PHee hee... I is okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x136,
        "#048F#2PThank goodness...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xA, 0x4)
    OP_8E(0xA, 0xFFFF394A, 0x0, 0xB4, 0x7D0, 0x0)

    ChrTalk(    #205
        0xA,
        (
            "#750FHa ha... I'm glad you're here.\x02\x03",

            "#751FIs that Estelle and Joshua I see\x01",
            "with you?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F3D():

        label("loc_3F3D")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_3F3D")

    QueueWorkItem2(0xA, 1, lambda_3F3D)

    def lambda_3F4E():

        label("loc_3F4E")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_3F4E")

    QueueWorkItem2(0xB, 1, lambda_3F4E)

    def lambda_3F5F():

        label("loc_3F5F")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_3F5F")

    QueueWorkItem2(0xD, 1, lambda_3F5F)

    def lambda_3F70():

        label("loc_3F70")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_3F70")

    QueueWorkItem2(0xC, 1, lambda_3F70)

    def lambda_3F81():

        label("loc_3F81")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_3F81")

    QueueWorkItem2(0xE, 1, lambda_3F81)

    def lambda_3F92():

        label("loc_3F92")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_3F92")

    QueueWorkItem2(0x136, 1, lambda_3F92)

    def lambda_3FA3():
        OP_8E(0xFE, 0xFFFF4124, 0x0, 0xFFFFF498, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3FA3)
    Sleep(500)

    def lambda_3FC3():
        OP_8E(0xFE, 0xFFFF441C, 0x0, 0xFFFFF5F6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3FC3)
    WaitChrThread(0x101, 0x2)

    def lambda_3FE3():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FE3)
    WaitChrThread(0x102, 0x2)

    def lambda_3FF6():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FF6)
    Sleep(500)
    OP_44(0xA, 0xFF)

    ChrTalk(    #206
        0x101,
        (
            "#000FYes, since someone contacted\x01",
            "the guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x102,
        (
            "#010FWe're investigating the incident\x01",
            "and thought we'd stop by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xA,
        (
            "#750FI see... Thank you for taking\x01",
            "the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xE,
        (
            "#772F#2PInvestigating... You mean about\x01",
            "the fire, right?\x02\x03",

            "Do you know who did it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        "#003FUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x102,
        "#013FWell, how to put it...?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #212
        "\x07\x05Estelle and Joshua exchanged awkward glances.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TurnDirection(0x136, 0x101, 400)
    OP_62(0x136, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x136)
    OP_44(0x136, 0xFF)
    TurnDirection(0x136, 0xB, 400)
    Sleep(200)
    TurnDirection(0x136, 0x102, 400)

    ChrTalk(    #213
        0x136,
        (
            "#040FSo, um, who's hungry?\x02\x03",

            "I missed breakfast, so I was\x01",
            "thinking about getting some\x01",
            "food.\x02\x03",

            "#041FGood boys and girls who join\x01",
            "me will get some sweet treats!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_426D():

        label("loc_426D")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_426D")

    QueueWorkItem2(0x101, 1, lambda_426D)

    def lambda_427E():

        label("loc_427E")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_427E")

    QueueWorkItem2(0x102, 1, lambda_427E)
    Sleep(50)

    def lambda_4294():

        label("loc_4294")

        TurnDirection(0xFE, 0x136, 400)
        OP_48()
        Jump("loc_4294")

    QueueWorkItem2(0xA, 1, lambda_4294)
    OP_44(0xB, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xE, 0xFF)
    Sleep(50)

    def lambda_42BA():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_42BA)

    def lambda_42C8():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_42C8)
    Sleep(50)

    def lambda_42DB():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_42DB)

    def lambda_42E9():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_42E9)

    ChrTalk(    #214
        0xB,
        "#1PReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xD,
        "#2PI's wants some puddin'!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xE,
        "#773F#1PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xC,
        "#1P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xE, 400)

    ChrTalk(    #218
        0xC,
        "#1PC'mon, Clem!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xC, 400)

    ChrTalk(    #219
        0xE,
        "#774F#2PHuh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xC,
        "#1PQuit griping and come on!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xC,
        "#1PLet's go downstairs, Miss Kloe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0x136,
        "#048FHa ha, okay.\x02",
    )

    CloseMessageWindow()
    OP_43(0x136, 0x2, 0x0, 0x11)
    OP_43(0xE, 0x2, 0x0, 0x12)
    OP_43(0xC, 0x2, 0x0, 0x13)
    OP_43(0xB, 0x2, 0x0, 0x14)
    OP_43(0xD, 0x2, 0x0, 0x15)

    def lambda_4406():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_4406)
    Sleep(600)

    def lambda_4426():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4426)
    Sleep(50)

    def lambda_4446():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4446)
    Sleep(200)

    def lambda_4466():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4466)
    Sleep(300)

    def lambda_4486():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4486)
    WaitChrThread(0x136, 0x1)
    SetChrFlags(0x136, 0x80)
    WaitChrThread(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    WaitChrThread(0xC, 0x1)
    SetChrFlags(0xC, 0x80)
    WaitChrThread(0xB, 0x1)
    SetChrFlags(0xB, 0x80)
    WaitChrThread(0xD, 0x1)
    SetChrFlags(0xD, 0x80)
    Sleep(500)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xA, 0xFF)

    ChrTalk(    #223
        0x101,
        (
            "#007FPhew... That was close.\x02\x03",

            "I really wouldn't want the\x01",
            "little kids to hear about\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0x102,
        (
            "#015F#5PIndeed.\x02\x03",

            "#010FAlthough I get the feeling\x01",
            "that Mary understands at least\x01",
            "some of what's happening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xA,
        (
            "#751FHa ha... Yes, isn't she great?\x01",
            "I'm happy to have her around.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 0)
    Sleep(300)

    ChrTalk(    #226
        0xA,
        (
            "#750FNow, you were saying...?\x02\x03",

            "Please, tell me what you can.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 0)
    Sleep(100)
    TurnDirection(0x102, 0xA, 0)

    ChrTalk(    #227
        0x102,
        "#012F#5PThanks for your understanding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x101,
        "#002FOkay, then...\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x101, -49200, 0, -1200, 0)
    SetChrPos(0x102, -50100, 0, -990, 45)
    SetChrPos(0xA, -49670, 0, 200, 180)
    OP_6D(-50810, 0, 340, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #229
        0x102,
        (
            "#012FFirst, we checked out where\x01",
            "the fire started...\x02\x03",

            "...and it does appear that it\x01",
            "was set deliberately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xA,
        (
            "#754F#2PMy suspicions were correct, then.\x02\x03",

            "I've always been very careful\x01",
            "about fire, so I suspected it\x01",
            "might be something like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x102,
        (
            "#012FDo you have any idea who could\x01",
            "have done this?\x02\x03",

            "Whoever was responsible must have\x01",
            "had some kind of motivation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xA,
        (
            "#757F#2PI have no idea...\x02\x03",

            "We have no real money to speak\x01",
            "of, nor has anyone ever borne\x01",
            "a grudge against us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x101,
        (
            "#002FSo, it wasn't a robbery,\x01",
            "and it wasn't for revenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x102,
        (
            "#012FWe have to acknowledge the\x01",
            "possibility that someone did \x01",
            "it just for fun...\x02\x03",

            "Did you happen to notice anything\x01",
            "unusual leading up to or during\x01",
            "the incident?\x02\x03",

            "Any strange people hanging\x01",
            "around the orphanage, for\x01",
            "instance...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xA,
        (
            "#756F#2PYes, actually...\x02\x03",

            "Not during the daytime when you\x01",
            "were there, but afterward...\x02\x03",

            "#757F...Though I can't imagine HE would\x01",
            "do something like this...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x101,
        "#002FWho's 'he'?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xA,
        (
            "#754F#2PWhile we were trying to escape\x01",
            "from the burning building...\x02\x03",

            "...the beams fell in and blocked\x01",
            "our way through the entry hall.\x02\x03",

            "#750FBut then he showed up and\x01",
            "helped us all get free...\x02\x03",

            "We owe him our lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        (
            "#004FR-Really...\x02\x03",

            "Was he Manorian?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xA,
        (
            "#756F#2PRight after he helped us, he\x01",
            "called the villagers over and\x01",
            "left in the confusion.\x02\x03",

            "I asked the other villagers\x01",
            "about him, but no one seemed\x01",
            "to know anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x102,
        (
            "#012F...Sounds suspicious.\x02\x03",

            "What business would anyone\x01",
            "have around the orphanage at\x01",
            "such a late hour?\x02\x03",

            "Did you notice anything in\x01",
            "particular about him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xA,
        (
            "#750F#2PHe was a man, maybe in his\x01",
            "late twenties.\x02\x03",

            "He also had brilliant silver hair.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x102,
        "#014FSilver hair...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xA,
        (
            "#750F#2PHe had a troubled look about him,\x01",
            "though...that made him seem far\x01",
            "older than he looked.\x02\x03",

            "But he didn't strike me as\x01",
            "a bad man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x101,
        (
            "#000FHe sounds suspicious,\x01",
            "but he did help you out.\x02\x03",

            "Doesn't sound like our guy\x01",
            "to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x102,
        "#014F...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x102, 300)

    ChrTalk(    #246
        0x101,
        (
            "#002F#2PJoshua?\x02\x03",

            "What's with the goofy stare?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 200)

    ChrTalk(    #247
        0x102,
        (
            "#013F#1POh, it's nothing...\x02\x03",

            "Perhaps he was just a bracer\x01",
            "who happened to pass by.\x02\x03",

            "#015FI think that we should\x01",
            "disregard him as a suspect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        "#002F#2PUm, okay...\x02",
    )

    CloseMessageWindow()
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #249
        0x136,
        "#1PPardon me...\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    TurnDirection(0x136, 0xA, 0)
    ClearChrFlags(0x136, 0x80)

    def lambda_4FB2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4FB2)

    def lambda_4FC0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4FC0)

    def lambda_4FCE():
        OP_6D(-49000, 0, -520, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4FCE)

    def lambda_4FE6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x136, 3, lambda_4FE6)
    OP_8E(0x136, 0xFFFF4818, 0x0, 0xFFFFFCAE, 0x7D0, 0x0)
    Sleep(300)

    ChrTalk(    #250
        0x101,
        "#000FOh, hi, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x102,
        "#010FWhere are the children?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x136,
        (
            "#041FHa ha... They're downstairs,\x01",
            "having some dessert.\x02\x03",

            "#040FMatron Theresa...you have a guest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xA,
        "#753FHmm?\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xF, -44560, 0, -1000, 0)
    SetChrPos(0x10, -44420, 0, -1440, 0)
    OP_9F(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xF, 0xA, 0)

    NpcTalk(    #254
        0xF,
        "Man's Voice",
        "#1PPardon my intrusion.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x136, 0xFFFF44B2, 0x0, 0xFFFFF8D0, 0x7D0, 0x0)

    def lambda_513B():

        label("loc_513B")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_513B")

    QueueWorkItem2(0x136, 1, lambda_513B)

    def lambda_514C():

        label("loc_514C")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_514C")

    QueueWorkItem2(0x101, 1, lambda_514C)

    def lambda_515D():

        label("loc_515D")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_515D")

    QueueWorkItem2(0x102, 1, lambda_515D)

    def lambda_516E():

        label("loc_516E")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_516E")

    QueueWorkItem2(0xA, 1, lambda_516E)
    ClearChrFlags(0xF, 0x80)

    def lambda_5184():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_5184)

    def lambda_5196():
        OP_8E(0xFE, 0xFFFF4926, 0x0, 0xFFFFFD76, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_5196)
    Sleep(500)
    ClearChrFlags(0x10, 0x80)

    def lambda_51BB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_51BB)

    def lambda_51CD():
        OP_8E(0xFE, 0xFFFF4DD6, 0x0, 0xFFFFFA60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_51CD)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #255
        0x101,
        "#004FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x102,
        "#014FMayor Dalmore...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xF,
        (
            "#660F#2POh, so the bracers I met\x01",
            "yesterday are here as well.\x02\x03",

            "Jean's reputation for responding\x01",
            "quickly is well-earned.\x02\x03",

            "#664FNow, then...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_52A7():
        OP_8E(0xFE, 0xFFFF443A, 0x0, 0xFA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_52A7)
    Sleep(500)

    def lambda_52C7():
        OP_8E(0xFE, 0xFFFF4796, 0x0, 0xFFFFFC68, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_52C7)
    WaitChrThread(0xF, 0x1)
    TurnDirection(0xF, 0xA, 400)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #258
        0xF,
        (
            "#660F#4PIt's good to see you again,\x01",
            "Matron Theresa.\x02\x03",

            "After I heard what happened,\x01",
            "I came over as quickly as I could. \x02\x03",

            "I'm glad that you're safe.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xA,
        (
            "#750FThank you, Mayor.\x02\x03",

            "It's very kind of you to come\x01",
            "by. I know you're a very busy\x01",
            "man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xF,
        (
            "#660F#4PNonsense... It is my responsibility\x01",
            "to look after all areas of the\x01",
            "region.\x02\x03",

            "#664FMore to the point, those who\x01",
            "did this must not be allowed\x01",
            "to get away with it.\x02\x03",

            "Joseph always loved that place...\x01",
            "Such an atrocity...\x02\x03",

            "#662FAllow me to express my most heartfelt\x01",
            "condolences.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xA,
        (
            "#754FThank you...\x02\x03",

            "But I am sure that he would just be\x01",
            "relieved that the children are alive and well.\x02\x03",

            "#757FMy sole regret is that all my\x01",
            "mementos of him were lost to\x01",
            "the fire...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x136,
        "#043FMatron Theresa...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xF, 225, 300)

    ChrTalk(    #263
        0xF,
        (
            "#662FTell me, bracers. Have you any\x01",
            "thoughts on who might have\x01",
            "done this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x102,
        (
            "#012FWe've only just begun our\x01",
            "investigation, so it's too\x01",
            "early to say, sir.\x02\x03",

            "It does look like it might have\x01",
            "been done simply out of malice,\x01",
            "however.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xF,
        (
            "#664FI see...\x01",
            "What a terrible thought.\x02\x03",

            "For something so heinous to happen\x01",
            "in such a peaceful place...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 315, 400)

    ChrTalk(    #266
        0x10,
        "#673FPardon me, Mayor...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(    #267
        0xF,
        "#660FHmm? What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x10,
        (
            "#671FDo you think that those people\x01",
            "might have a hand in this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0xF,
        "#662F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x101,
        (
            "#004FWhoa, hold up! Who do you\x01",
            "mean by 'those people'?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 300)

    ChrTalk(    #271
        0x10,
        (
            "#671FYou encountered them yesterday.\x02\x03",

            "The ruffians down in the\x01",
            "warehouse district of Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x101,
        "#002FOh, them...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x136,
        "#043F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0x102,
        (
            "#012FPardon my bluntness...but what\x01",
            "makes you suspect them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0x10,
        (
            "#671FThey've been openly defying the mayor for\x01",
            "quite some time now.\x02\x03",

            "They certainly seem to get their kicks out\x01",
            "of causing trouble for him.\x02\x03",

            "#673FAnd since he and Matron Theresa\x01",
            "are friends, it--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xF,
        "#665FGilbert!\x02",
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x10, 315, 400)

    ChrTalk(    #277
        0x10,
        "#676FS-Sir!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xF,
        (
            "#663FWild speculation does no\x01",
            "one any good.\x02\x03",

            "This is a dire offense. We must\x01",
            "have no false accusations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x10,
        (
            "#676FM-My apologies, sir.\x01",
            "That was foolish of me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xF,
        (
            "#664FI think it would be best to\x01",
            "let the bracers identify and\x01",
            "locate the ones responsible.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF, 225, 400)

    ChrTalk(    #281
        0xF,
        "#660FCan I count on your help?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x101,
        "#006FSure! Leave it to us.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x102,
        (
            "#010FWe will devote our full\x01",
            "attention to it, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xF,
        (
            "#661FGood, good.\x01",
            "I'm glad to hear it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0xA, 400)
    Sleep(500)
    OP_8C(0x10, 270, 0)

    ChrTalk(    #285
        0xF,
        (
            "#660F#4PBy the way, Matron Theresa...\x01",
            "I do have one question to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xA,
        "#753FWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xF,
        (
            "#660F#4PWhat do you plan to do with\x01",
            "the orphanage now?\x02\x03",

            "Rebuilding will take time and\x01",
            "a not inconsiderable amount of\x01",
            "mira to complete.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xA,
        (
            "#757F...\x02\x03",

            "Honestly, I'm at a loss.\x02\x03",

            "We have a modest reserve of mira,\x01",
            "but the cost will be phenomenal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        "#003FMatron...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x136,
        "#043F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xF,
        (
            "#664F#4PI was afraid of that.\x02\x03",

            "#660FWell, I have a proposal of\x01",
            "sorts for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xA,
        "#750F...What might that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xF,
        (
            "#660F#4PAt the Dalmore estate in\x01",
            "Grancel, I have a villa.\x02\x03",

            "It's only used for special\x01",
            "occasions, so...\x02\x03",

            "What say you to having the\x01",
            "children stay there for a\x01",
            "little while?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xA,
        "#753FOh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xF,
        (
            "#660F#4PAnd of course, charging rent\x01",
            "would be particularly boorish\x01",
            "of me.\x02\x03",

            "You'd be welcome to stay there\x01",
            "for as long as the rebuilding\x01",
            "process takes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xA,
        (
            "#757FB-But there's no need for\x01",
            "you to shoulder the burden\x01",
            "of our troubles...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xF,
        (
            "#661F#4PBut the villa sits unused.\x02\x03",

            "If you have misgivings, then I\x01",
            "will grant you control of the\x01",
            "grounds.\x02\x03",

            "Think of it as a well-deserved\x01",
            "reward, if you will.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xA,
        (
            "#756FMayor...\x02\x03",

            "...\x02\x03",

            "#757FMay I have some time to think\x01",
            "it over?\x02\x03",

            "Your offer is most generous,\x01",
            "but I can barely process it\x01",
            "with everything going on...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xF,
        (
            "#664F#4PPerfectly understandable.\x01",
            "You should get some rest.\x02\x03",

            "#660FI must be off as well.\x02\x03",

            "If you decide to accept,\x01",
            "please feel free to contact\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xA,
        "#750FI will... Thank you so very much.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF, 0x10, 400)

    ChrTalk(    #301
        0xF,
        "#660FLet us go, Gilbert.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0xF, 400)

    ChrTalk(    #302
        0x10,
        "#670FYes, sir!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10, 0xFFFF4818, 0x0, 0xFFFFF9B6, 0x7D0, 0x0)
    OP_8C(0x10, 0, 400)

    def lambda_619F():
        OP_8E(0xFE, 0xFFFF4F20, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_619F)
    WaitChrThread(0xF, 0x1)

    def lambda_61BF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_61BF)

    def lambda_61D1():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_61D1)
    Sleep(300)

    def lambda_61F1():
        OP_8E(0xFE, 0xFFFF4F20, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_61F1)
    WaitChrThread(0x10, 0x1)

    def lambda_6211():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_6211)

    def lambda_6223():
        OP_8E(0xFE, 0xFFFF51F0, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_6223)
    WaitChrThread(0xF, 0x1)
    SetChrFlags(0xF, 0x80)
    WaitChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)

    def lambda_625C():
        OP_6D(-49600, 0, -480, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_625C)
    Sleep(1000)

    ChrTalk(    #303
        0x101,
        (
            "#008FWow... That was a shock.\x02\x03",

            "He's certainly the generous type.\x01",
            "On par with Mayor Maybelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x102,
        (
            "#010FIndeed. Particularly in light\x01",
            "of his being a former noble.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x136, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x136)

    def lambda_633A():
        OP_6D(-49200, 0, 70, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_633A)
    OP_44(0x136, 0xFF)
    OP_8E(0x136, 0xFFFF4354, 0x0, 0xFFFFFF9C, 0x7D0, 0x0)
    TurnDirection(0x136, 0xA, 400)
    OP_44(0xA, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)

    def lambda_637D():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_637D)

    def lambda_638B():
        TurnDirection(0xFE, 0x136, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_638B)
    TurnDirection(0xA, 0x136, 400)

    ChrTalk(    #305
        0x136,
        (
            "#049FWhat do you intend to do in\x01",
            "regards to the mayor's offer,\x01",
            "Matron?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xA,
        (
            "#754FWell, what do you think of\x01",
            "the situation?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0x136,
        (
            "#049F...\x02\x03",

            "#049FConventional wisdom dictates\x01",
            "that you should accept it.\x02\x03",

            "However, once you've gone to\x01",
            "Grancel...\x02\x03",

            "#043FOh... Never mind me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xA,
        (
            "#750FHa ha... You always were such\x01",
            "a thoughtful child.\x02\x03",

            "It's all right. I want you to\x01",
            "give me your honest opinion.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x136,
        (
            "#043F...\x02\x03",

            "#049FThe herb garden and the people\x01",
            "I care about would be gone...\x02\x03",

            "So... And...\x02\x03",

            "#047FWith you and Joseph gone,\x01",
            "I feel like all of my good\x01",
            "memories will fade away...\x02\x03",

            "I'm sorry... I'm just being\x01",
            "stupid and selfish.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xA,
        (
            "#750FHa ha... I share your feelings.\x02\x03",

            "The orphanage is home to my\x01",
            "memories of him, as well as\x01",
            "the children's memories.\x02\x03",

            "But...though memories are precious,\x01",
            "having a place to live is of the\x01",
            "utmost importance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #311
        0x136,
        "#049FYes, ma'am...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xA,
        (
            "#750FI believe this will all be\x01",
            "settled soon.\x02\x03",

            "Please, try to focus on tending\x01",
            "to the campus festival, for now.\x02\x03",

            "The children are really\x01",
            "looking forward to it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x136,
        "#048F...Yes, ma'am.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 300)

    ChrTalk(    #314
        0xA,
        (
            "#750F#4PEstelle and Joshua...\x02\x03",

            "I wish I could be of more\x01",
            "help, but I must leave the\x01",
            "investigation in your hands.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 0)
    Sleep(100)
    TurnDirection(0x102, 0xA, 0)

    ChrTalk(    #315
        0x102,
        "#010FWe will handle it, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x101,
        (
            "#006FWe're going to take the culprit\x01",
            "down! You can count on it!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_28(0x3B, 0x1, 0x80)
    OP_28(0x3B, 0x1, 0x100)
    OP_28(0x3B, 0x1, 0x200)
    OP_28(0x3B, 0x1, 0x400)
    OP_28(0x3C, 0x4, 0x2)
    OP_28(0x3C, 0x4, 0x4)
    OP_28(0x3C, 0x1, 0x1)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T2300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3BA5 end

    def Function_17_68EC(): pass

    label("Function_17_68EC")

    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_9F(0x136, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_17_68EC end

    def Function_18_6907(): pass

    label("Function_18_6907")

    Sleep(2000)
    OP_9F(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_18_6907 end

    def Function_19_6918(): pass

    label("Function_19_6918")

    Sleep(2500)
    OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_19_6918 end

    def Function_20_6929(): pass

    label("Function_20_6929")

    Sleep(3000)
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_20_6929 end

    def Function_21_693A(): pass

    label("Function_21_693A")

    Sleep(3500)
    OP_9F(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    OP_22(0x7, 0x0, 0x64)
    Return()

    # Function_21_693A end

    def Function_22_6950(): pass

    label("Function_22_6950")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(-50180, 0, -790, 0)
    AddParty(0x5, 0xFF)
    SetChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x4)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8)
    SetChrPos(0x9, -52430, 0, 480, 0)
    SetChrPos(0xB, -50850, 0, -1230, 270)
    SetChrPos(0xD, -51540, 0, -2430, 0)
    SetChrPos(0xC, -52530, 0, -2420, 0)
    SetChrPos(0xE, -50800, 0, 1470, 270)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x106, 0x80)
    SetChrPos(0x101, -44330, 0, -1080, 270)
    SetChrPos(0x102, -44330, 0, -1080, 270)
    SetChrPos(0x105, -44330, 0, -1080, 270)
    SetChrPos(0x106, -44330, 0, -1080, 270)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4A(0x9, 255)
    OP_4A(0xB, 255)
    OP_4A(0xD, 255)
    OP_4A(0xC, 255)
    OP_4A(0xE, 255)
    SetChrFlags(0x106, 0x80)
    FadeToBright(1000, 0)
    OP_43(0x105, 0x1, 0x0, 0x19)
    OP_9F(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_43(0x101, 0x1, 0x0, 0x17)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_43(0x102, 0x1, 0x0, 0x18)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x11, 0x1)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_6B49():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6B49)

    def lambda_6B57():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6B57)

    def lambda_6B65():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6B65)

    def lambda_6B73():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_6B73)

    def lambda_6B81():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6B81)

    ChrTalk(    #317
        0xE,
        "#775F#3POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xC,
        "#3PMiss Kloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x105,
        "#043FEveryone...\x02",
    )

    CloseMessageWindow()
    OP_43(0xB, 0x1, 0x0, 0x1A)
    OP_43(0xC, 0x1, 0x0, 0x1B)
    OP_43(0xE, 0x1, 0x0, 0x1C)
    OP_43(0xD, 0x1, 0x0, 0x1D)
    WaitChrThread(0xB, 0x1)
    OP_43(0x9, 0x1, 0x0, 0x1E)

    ChrTalk(    #320
        0xB,
        "#3PWaaaahhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xD,
        "#5PIt was so scary!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x101,
        (
            "#008F#2PThank goodness you're\x01",
            "all safe...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x1)

    def lambda_6C56():

        label("loc_6C56")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_6C56")

    QueueWorkItem2(0x102, 1, lambda_6C56)

    ChrTalk(    #323
        0x102,
        (
            "#012F#1PPardon me, but what about the\x01",
            "others? How is Matron Theresa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0x9,
        "Don't worry. They're not hurt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0x9,
        (
            "They haven't woken up, though,\x01",
            "which has me a little worried.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x102,
        (
            "#015F#1PIf I may, then, I'd like\x01",
            "to see them.\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x102, 0x4)

    def lambda_6D59():

        label("loc_6D59")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_6D59")

    QueueWorkItem2(0x101, 1, lambda_6D59)

    def lambda_6D6A():

        label("loc_6D6A")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_6D6A")

    QueueWorkItem2(0x105, 1, lambda_6D6A)

    def lambda_6D7B():

        label("loc_6D7B")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_6D7B")

    QueueWorkItem2(0xE, 1, lambda_6D7B)

    def lambda_6D8C():

        label("loc_6D8C")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_6D8C")

    QueueWorkItem2(0xC, 1, lambda_6D8C)

    def lambda_6D9D():

        label("loc_6D9D")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_6D9D")

    QueueWorkItem2(0x9, 1, lambda_6D9D)
    OP_8E(0x102, 0xFFFF42DC, 0x0, 0x5A, 0x7D0, 0x0)
    OP_8E(0x102, 0xFFFF3F6C, 0x0, 0x3CA, 0x7D0, 0x0)

    def lambda_6DD6():
        OP_6D(-52260, 0, -520, 2000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6DD6)
    OP_8E(0x102, 0xFFFF3896, 0x0, 0x226, 0x7D0, 0x0)
    OP_8E(0x102, 0xFFFF30EE, 0x0, 0x1F4, 0x7D0, 0x0)
    OP_8C(0x102, 0, 400)
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_8C(0x102, 180, 400)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #327
        0x102,
        (
            "#013FNo doubt about it...\x01",
            "Someone used sleeping powder.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #328
        0x101,
        "#580FS-Sleeping powder?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #329
        0x102,
        (
            "#012FYes. There's still a faint\x01",
            "hint of it in the air.\x02\x03",

            "It's probably the kind without\x01",
            "side effects, so there's no real\x01",
            "need for concern...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xC, 0xFF)

    ChrTalk(    #330
        0x101,
        "#505FHmm...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 90, 400)

    def lambda_6F7E():
        OP_6D(-50370, 0, -640, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_6F7E)
    OP_8E(0x102, 0xFFFF3A80, 0x0, 0xF0, 0x7D0, 0x0)
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #331
        0x101,
        (
            "#002F#1PHey, Clem. Can you tell us\x01",
            "what happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xE,
        "#773F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 400)

    ChrTalk(    #333
        0xC,
        "#1PI'll tell you...\x02",
    )

    CloseMessageWindow()
    OP_44(0x9, 0xFF)

    def lambda_701A():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_701A)

    def lambda_7028():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7028)
    Sleep(50)

    def lambda_703B():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_703B)

    def lambda_7049():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_7049)
    Sleep(50)

    def lambda_705C():
        TurnDirection(0xFE, 0xC, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_705C)

    def lambda_706A():
        TurnDirection(0xFE, 0xC, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_706A)
    Sleep(50)
    OP_44(0xE, 0xFF)
    TurnDirection(0xE, 0x101, 400)
    Sleep(500)

    ChrTalk(    #334
        0xC,
        (
            "#1PWe were walking along the coast\x01",
            "road with the bracer lady...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xC,
        (
            "#1P...and these strange guys in\x01",
            "masks showed up outta nowhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xC,
        (
            "#1PThe bracer lady fought them\x01",
            "for a while...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xC,
        "#1P...but they surrounded her.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0xC,
        (
            "#1PShe fought 'em to save us and\x01",
            "Matron Theresa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xC,
        "#1PThat's why...*sniffle*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x101,
        (
            "#003FThere, there... It must have\x01",
            "been so scary...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xE,
        (
            "#773FThey... They took an envelope\x01",
            "from the matron...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7237():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7237)
    Sleep(50)

    def lambda_724A():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_724A)
    Sleep(50)

    def lambda_725D():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_725D)
    Sleep(50)

    def lambda_7270():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_7270)
    Sleep(50)
    TurnDirection(0x102, 0xE, 400)
    Sleep(500)

    ChrTalk(    #342
        0xE,
        (
            "#775FI wanted really bad to get\x01",
            "it back...\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0xE, 0xFF)
    TurnDirection(0xE, 0x102, 300)

    ChrTalk(    #343
        0xE,
        (
            "#777FMr. Joshua...\x01",
            "I couldn't help her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0x102,
        (
            "#015F#3PDon't think that way, Clem.\x02\x03",

            "I know that Matron Theresa would\x01",
            "just be happy that all of you\x01",
            "are safe.\x02\x03",

            "#012FThat's why you mustn't blame\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0xE,
        "#777FBut I... I...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xC,
        "#3P*sob*...*sniffle*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0x101,
        (
            "#005F#1PI don't believe this! Who\x01",
            "would do such a thing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x105,
        "#047F#6P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #349
        0x105,
        (
            "#042F#6PWhoever it is...must certainly\x01",
            "be skilled at hiding his or her\x01",
            "presence.\x02\x03",

            "After all, the bracer wasn't\x01",
            "alerted, and Matron Theresa\x01",
            "is unconscious...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_74C7():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_74C7)

    def lambda_74D5():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_74D5)

    def lambda_74E3():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_74E3)
    TurnDirection(0xE, 0x105, 400)

    ChrTalk(    #350
        0x101,
        "#004F#1PKloe...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x105,
        (
            "#042F#6PI get the feeling that this\x01",
            "was very deliberate.\x02\x03",

            "I'd say that the criminals were\x01",
            "probably targeting the donations\x01",
            "Matron Theresa had on her.\x02\x03",

            "If we find the money,\x01",
            "we'll find the culprit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x102,
        "#012F#3PYes, you're probably right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x101,
        (
            "#006F#1PYou seem a little calmer\x01",
            "than earlier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x105,
        (
            "#043F#6PYes... In order to help the\x01",
            "matron and the kids, I must\x01",
            "compose myself.\x02\x03",

            "Regardless, we must find who\x01",
            "did this as soon as possible.\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x106, -44560, 0, -1160, 0)
    TurnDirection(0x106, 0x105, 0)
    ClearChrFlags(0x106, 0x80)

    NpcTalk(    #355
        0x106,
        "Man's Voice",
        "#1PShe's right, you know.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    SetChrChipByIndex(0x106, 15)

    def lambda_7763():
        OP_6D(-49600, 0, -620, 1500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7763)
    ClearChrFlags(0x106, 0x80)

    def lambda_7780():
        OP_8E(0xFE, 0xFFFF4598, 0x0, 0xFFFFFD08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_7780)

    def lambda_779B():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_779B)

    def lambda_77A9():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_77A9)

    def lambda_77B7():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_77B7)

    def lambda_77C5():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_77C5)

    def lambda_77D3():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_77D3)

    def lambda_77E1():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_77E1)

    def lambda_77EF():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_77EF)

    def lambda_77FD():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_77FD)
    OP_9F(0x106, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0x106, 0x1)

    ChrTalk(    #356
        0x101,
        "#004F#3PAaahh!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x102,
        "#014F#3PAgate...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x106,
        (
            "#051FI heard what was going on\x01",
            "at the guild.\x02\x03",

            "Looks like you've gotten wrapped\x01",
            "up in one hell of a mess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x101,
        (
            "#005F#3PHey! Don't make light of\x01",
            "the situation!\x02\x03",

            "Carna got hurt, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x106,
        (
            "#053FI know that...so quit your\x01",
            "yapping.\x02\x03",

            "#050FCarna's no amateur, either.\x01",
            "It'd take someone pretty\x01",
            "skilled to beat her.\x02\x03",

            "How about you give me a quick\x01",
            "rundown of what's been going\x01",
            "on here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x102,
        "#012F#3POkay...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #362
        (
            "\x07\x05Joshua and Estelle told Agate the whole story about the donations for the\x01",
            "orphanage.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #363
        0x106,
        (
            "#552FHuh... All right, then.\x01",
            "There's definitely something\x01",
            "weird going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x101,
        "#505F#3PWeird how?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x106,
        (
            "#050FWell, here's the thing...\x02\x03",

            "You know that Raven gang that was\x01",
            "hanging out at the warehouse? They're\x01",
            "all gone now. Warehouse is empty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x101,
        (
            "#580F#3PThen...\x02\x03",

            "#005FThey must be the ones who\x01",
            "assaulted Matron Theresa!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x102,
        (
            "#012F#3PI'm not so sure about that.\x02\x03",

            "I really doubt they'd have what\x01",
            "it takes to get the upper hand\x01",
            "on Carna.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x101,
        (
            "#007F#3PYeah, that's true...\x02\x03",

            "They talk a big game, but I\x01",
            "don't think they could back\x01",
            "it up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x106,
        (
            "#057FYeah, give 'em a single hard\x01",
            "look and they shut right up. \x02\x03",

            "However, today they're suddenly\x01",
            "nowhere to be found.\x02\x03",

            "Couple that with today's little incident,\x01",
            "and what do you get? Like I said, something\x01",
            "weird is going on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x102,
        (
            "#012F#3PEven if they're not directly responsible\x01",
            "for the fire, I do feel like they're\x01",
            "involved, somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x106,
        (
            "#050FYeah, but this ain't the time\x01",
            "to go checking that out.\x02\x03",

            "Come on, greenhorns.\x01",
            "Let's go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #372
        0x101,
        (
            "#004F#3PWhat are you talking about?\x02\x03",

            "#002FWhere are we going?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0x106,
        (
            "#551FYou slow in the head or something? \x01",
            "Obviously, we're going to the seaside\x01",
            "path where the crime happened.\x02\x03",

            "How those idiots did it\x01",
            "doesn't matter right now...\x02\x03",

            "#054FWe've gotta focus on finding some\x01",
            "clues as to where they are!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x101,
        "#004F#3PAh... True.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x102,
        "#012F#3PUnderstood. We'll help.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T2301   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_6950 end

    def Function_23_7F9D(): pass

    label("Function_23_7F9D")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF4070, 0x0, 0xFFFFFA6A, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_23_7F9D end

    def Function_24_7FBE(): pass

    label("Function_24_7FBE")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF430E, 0x0, 0xFFFFFD44, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_24_7FBE end

    def Function_25_7FDF(): pass

    label("Function_25_7FDF")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFF3EA4, 0x0, 0xFFFFFE52, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_25_7FDF end

    def Function_26_8000(): pass

    label("Function_26_8000")

    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3C42, 0x0, 0xFFFFFD12, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_26_8000 end

    def Function_27_802E(): pass

    label("Function_27_802E")

    Sleep(150)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3F8A, 0x0, 0xFFFFF7B8, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_27_802E end

    def Function_28_8061(): pass

    label("Function_28_8061")

    Sleep(100)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3F12, 0x0, 0x10E, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_28_8061 end

    def Function_29_8094(): pass

    label("Function_29_8094")

    Sleep(50)
    OP_62(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0xFE, 0xFFFF3D28, 0x0, 0xFFFFFAB0, 0xBB8, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_29_8094 end

    def Function_30_80C7(): pass

    label("Function_30_80C7")

    SetChrFlags(0x9, 0x40)
    SetChrFlags(0x9, 0x4)
    OP_8E(0x9, 0xFFFF3922, 0x0, 0x15E, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF3E4A, 0x0, 0x3F2, 0x7D0, 0x0)
    OP_8E(0x9, 0xFFFF4336, 0x0, 0x35C, 0x7D0, 0x0)
    TurnDirection(0x9, 0x102, 400)
    Return()

    # Function_30_80C7 end

    SaveToFile()

Try(main)
