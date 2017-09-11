from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C2210   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2210.x',
        MapIndex            = 84,
        MapDefaultBGM       = "ed60031",
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
        'Deen',                                 # 9
        'Rais',                                 # 10
        'Rocco',                                # 11
        'Young Man',                            # 12
        'Young Man',                            # 13
        'Young Man',                            # 14
        'Young Man',                            # 15
        'Young Man',                            # 16
        'Young Man',                            # 17
        'Black-Clad Man',                       # 18
        'Black-Clad Man',                       # 19
        'Steward Gilbert',                      # 20
        'Vogt',                                 # 21
        'Camera',                               # 22
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
        Unknown_3A              = 84,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01390 ._CH',             # 00
        'ED6_DT07/CH00370 ._CH',             # 01
        'ED6_DT07/CH00371 ._CH',             # 02
        'ED6_DT07/CH00374 ._CH',             # 03
        'ED6_DT07/CH00372 ._CH',             # 04
        'ED6_DT07/CH00100 ._CH',             # 05
        'ED6_DT07/CH00110 ._CH',             # 06
        'ED6_DT07/CH00140 ._CH',             # 07
        'ED6_DT07/CH00101 ._CH',             # 08
        'ED6_DT07/CH00111 ._CH',             # 09
        'ED6_DT07/CH02420 ._CH',             # 0A
        'ED6_DT07/CH00150 ._CH',             # 0B
        'ED6_DT07/CH00151 ._CH',             # 0C
        'ED6_DT07/CH00152 ._CH',             # 0D
        'ED6_DT06/CH20102 ._CH',             # 0E
        'ED6_DT09/CH10020 ._CH',             # 0F
        'ED6_DT09/CH10021 ._CH',             # 10
        'ED6_DT07/CH01330 ._CH',             # 11
        'ED6_DT07/CH02510 ._CH',             # 12
        'ED6_DT07/CH02520 ._CH',             # 13
        'ED6_DT07/CH02530 ._CH',             # 14
        'ED6_DT07/CH00450 ._CH',             # 15
        'ED6_DT07/CH00451 ._CH',             # 16
        'ED6_DT07/CH00454 ._CH',             # 17
        'ED6_DT07/CH00452 ._CH',             # 18
        'ED6_DT07/CH00460 ._CH',             # 19
        'ED6_DT07/CH00461 ._CH',             # 1A
        'ED6_DT07/CH00464 ._CH',             # 1B
        'ED6_DT07/CH00462 ._CH',             # 1C
        'ED6_DT07/CH00470 ._CH',             # 1D
        'ED6_DT07/CH00471 ._CH',             # 1E
        'ED6_DT07/CH00474 ._CH',             # 1F
        'ED6_DT07/CH00472 ._CH',             # 20
        'ED6_DT06/CH20053 ._CH',             # 21
        'ED6_DT06/CH20085 ._CH',             # 22
        'ED6_DT07/CH00015 ._CH',             # 23
        'ED6_DT06/CH20079 ._CH',             # 24
        'ED6_DT07/CH00141 ._CH',             # 25
        'ED6_DT07/CH00340 ._CH',             # 26
        'ED6_DT07/CH00341 ._CH',             # 27
        'ED6_DT07/CH00342 ._CH',             # 28
        'ED6_DT07/CH00440 ._CH',             # 29
        'ED6_DT07/CH00441 ._CH',             # 2A
        'ED6_DT07/CH00442 ._CH',             # 2B
        'ED6_DT06/CH20080 ._CH',             # 2C
    )

    AddCharChipPat(
        'ED6_DT07/CH01390P._CP',             # 00
        'ED6_DT07/CH00370P._CP',             # 01
        'ED6_DT07/CH00371P._CP',             # 02
        'ED6_DT07/CH00374P._CP',             # 03
        'ED6_DT07/CH00372P._CP',             # 04
        'ED6_DT07/CH00100P._CP',             # 05
        'ED6_DT07/CH00110P._CP',             # 06
        'ED6_DT07/CH00140P._CP',             # 07
        'ED6_DT07/CH00101P._CP',             # 08
        'ED6_DT07/CH00111P._CP',             # 09
        'ED6_DT07/CH02420P._CP',             # 0A
        'ED6_DT07/CH00150P._CP',             # 0B
        'ED6_DT07/CH00151P._CP',             # 0C
        'ED6_DT07/CH00152P._CP',             # 0D
        'ED6_DT06/CH20102P._CP',             # 0E
        'ED6_DT09/CH10020P._CP',             # 0F
        'ED6_DT09/CH10021P._CP',             # 10
        'ED6_DT07/CH01330P._CP',             # 11
        'ED6_DT07/CH02510P._CP',             # 12
        'ED6_DT07/CH02520P._CP',             # 13
        'ED6_DT07/CH02530P._CP',             # 14
        'ED6_DT07/CH00450P._CP',             # 15
        'ED6_DT07/CH00451P._CP',             # 16
        'ED6_DT07/CH00454P._CP',             # 17
        'ED6_DT07/CH00452P._CP',             # 18
        'ED6_DT07/CH00460P._CP',             # 19
        'ED6_DT07/CH00461P._CP',             # 1A
        'ED6_DT07/CH00464P._CP',             # 1B
        'ED6_DT07/CH00462P._CP',             # 1C
        'ED6_DT07/CH00470P._CP',             # 1D
        'ED6_DT07/CH00471P._CP',             # 1E
        'ED6_DT07/CH00474P._CP',             # 1F
        'ED6_DT07/CH00472P._CP',             # 20
        'ED6_DT06/CH20053P._CP',             # 21
        'ED6_DT06/CH20085P._CP',             # 22
        'ED6_DT07/CH00015P._CP',             # 23
        'ED6_DT06/CH20079P._CP',             # 24
        'ED6_DT07/CH00141P._CP',             # 25
        'ED6_DT07/CH00340P._CP',             # 26
        'ED6_DT07/CH00341P._CP',             # 27
        'ED6_DT07/CH00342P._CP',             # 28
        'ED6_DT07/CH00440P._CP',             # 29
        'ED6_DT07/CH00441P._CP',             # 2A
        'ED6_DT07/CH00442P._CP',             # 2B
        'ED6_DT06/CH20080P._CP',             # 2C
    )

    DeclNpc(
        X                   = -11200,
        Z                   = 0,
        Y                   = 7490,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -9460,
        Z                   = 0,
        Y                   = 7150,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -10770,
        Z                   = 0,
        Y                   = 5350,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -11930,
        Z                   = 0,
        Y                   = 4280,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -11460,
        Z                   = 0,
        Y                   = 1930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -10100,
        Z                   = 0,
        Y                   = 2930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -11930,
        Z                   = 0,
        Y                   = 4280,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -11460,
        Z                   = 0,
        Y                   = 1930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -10100,
        Z                   = 0,
        Y                   = 2930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -11460,
        Z                   = 0,
        Y                   = 1930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -10100,
        Z                   = 0,
        Y                   = 2930,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3670,
        Z                   = 90,
        Y                   = 200850,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x104,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -3810,
        Y                   = 2250,
        Z                   = 106920,
        Range               = 2000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 6,
    )


    ScpFunction(
        "Function_0_3F2",          # 00, 0
        "Function_1_5EF",          # 01, 1
        "Function_2_614",          # 02, 2
        "Function_3_62A",          # 03, 3
        "Function_4_11FA",         # 04, 4
        "Function_5_15C0",         # 05, 5
        "Function_6_19B6",         # 06, 6
        "Function_7_3B41",         # 07, 7
        "Function_8_3B95",         # 08, 8
        "Function_9_3C0C",         # 09, 9
        "Function_10_3C72",        # 0A, 10
        "Function_11_3CFD",        # 0B, 11
    )


    def Function_0_3F2(): pass

    label("Function_0_3F2")

    SetMapFlags(0x40000000)
    AddParty(0xFF, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_40E"),
        (102, "loc_421"),
        (104, "loc_434"),
        (SWITCH_DEFAULT, "loc_447"),
    )


    label("loc_40E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41E")
    Event(0, 3)

    label("loc_41E")

    Jump("loc_447")

    label("loc_421")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_431")
    Event(0, 4)

    label("loc_431")

    Jump("loc_447")

    label("loc_434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_444")
    Event(0, 5)

    label("loc_444")

    Jump("loc_447")

    label("loc_447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 3)), scpexpr(EXPR_END)), "loc_4D4")
    SetChrFlags(0xF, 0x800)
    SetChrFlags(0x10, 0x800)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x10, 0x1)
    SetChrChipByIndex(0xA, 31)
    SetChrChipByIndex(0xF, 36)
    SetChrChipByIndex(0x10, 36)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, 102990, 0, 98020, 270)
    SetChrPos(0xF, 104030, 0, 99080, 0)
    SetChrPos(0x10, 102870, 0, 100160, 135)

    label("loc_4D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 2)), scpexpr(EXPR_END)), "loc_561")
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xE, 0x800)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    SetChrChipByIndex(0x9, 27)
    SetChrChipByIndex(0xD, 36)
    SetChrChipByIndex(0xE, 36)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 102640, 0, 1840, 270)
    SetChrPos(0xD, 101950, 0, 3240, 0)
    SetChrPos(0xE, 101850, 0, 770, 135)

    label("loc_561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 1)), scpexpr(EXPR_END)), "loc_5EE")
    SetChrFlags(0xB, 0x800)
    SetChrFlags(0xC, 0x800)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0x8, -240, 0, 6100, 225)
    SetChrPos(0xB, 1680, 0, 4920, 180)
    SetChrPos(0xC, -1990, 0, 5180, 315)
    SetChrChipByIndex(0x8, 23)
    SetChrChipByIndex(0xB, 36)
    SetChrChipByIndex(0xC, 36)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5EE")

    Return()

    # Function_0_3F2 end

    def Function_1_5EF(): pass

    label("Function_1_5EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FE")
    Jump("loc_5FE")

    label("loc_5FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x392), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_613")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_613")

    Return()

    # Function_1_5EF end

    def Function_2_614(): pass

    label("Function_2_614")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_629")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_614")

    label("loc_629")

    Return()

    # Function_2_614 end

    def Function_3_62A(): pass

    label("Function_3_62A")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(400, 0, -2430, 0)
    SetChrPos(0x101, 1330, 0, -5430, 0)
    SetChrPos(0x102, -680, 0, -5890, 0)
    SetChrPos(0x106, 380, 0, -4780, 0)
    SetChrPos(0x105, 190, 0, -6650, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, 0, 0, 0, 0)
    SetChrPos(0xB, 500, 0, 2140, 225)
    SetChrPos(0xC, -1740, 0, 1110, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        "#005FThese guys again?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x105,
        "#043FAren't they the ones from before...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x106,
        (
            "#057FI swear, if I wasn't looking at\x01",
            "them with my own eyes right now,\x01",
            "I'd never believe it...\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x106, 0x78, 0x0, 0xFFFFF448, 0x7D0, 0x0)
    TurnDirection(0x106, 0x8, 400)

    ChrTalk(    #3
        0x106,
        (
            "#054FHey, what the hell are you all\x01",
            "doing here?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7D8():
        TurnDirection(0xFE, 0x101, 230)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7D8)

    def lambda_7E6():
        TurnDirection(0xFE, 0x101, 230)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7E6)

    def lambda_7F4():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_7F4)
    Sleep(400)
    OP_62(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05The Raven Gang members' eyes are blank and emotionless.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #5
        0x106,
        "#055FH-Hey...\x02",
    )

    CloseMessageWindow()

    def lambda_8B2():
        OP_8E(0xFE, 0xFFFFFF56, 0x0, 0xFFFFFA38, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_8B2)
    Sleep(300)
    OP_63(0x8)
    OP_63(0xB)
    OP_63(0xC)
    SetChrChipByIndex(0x8, 24)
    OP_51(0x0, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0x1FC, 0x0, 0x64)

    def lambda_8F0():
        OP_99(0xFE, 0x0, 0x2, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8F0)

    def lambda_900():
        OP_6D(-170, 0, -1480, 700)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_900)

    ChrTalk(    #6
        0x102,
        "#016FAgate, look out!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x20)

    def lambda_93D():
        OP_93(0xFE, 0x106, 0x384, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_93D)
    OP_51(0x0, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_99(0x8, 0x2, 0x4, 0xFA0)
    OP_22(0xD6, 0x0, 0x64)
    OP_44(0x106, 0xFF)
    SetChrChipByIndex(0x106, 12)
    OP_94(0x1, 0x106, 0xB4, 0x64, 0x1388, 0x0)

    def lambda_983():
        OP_9E(0xFE, 0x14, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_983)

    def lambda_99D():
        OP_9E(0xFE, 0x14, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_99D)
    OP_6B(2800, 700)
    Sleep(500)

    ChrTalk(    #7
        0x106,
        (
            "#052F#4PWhere are they getting this\x01",
            "strength from...?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_A06():
        OP_6B(3000, 150)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_A06)

    def lambda_A16():
        OP_99(0x8, 0x4, 0x7, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A16)
    SetChrFlags(0x8, 0x20)
    OP_95(0x106, 0x0, 0x0, 0xFFFFFA24, 0x12C, 0x1388)
    OP_95(0x106, 0x0, 0x0, 0xFFFFFE0C, 0x64, 0x1388)
    SetChrChipByIndex(0x106, 11)
    ClearChrFlags(0x8, 0x20)
    Sleep(100)
    SetChrChipByIndex(0x8, 21)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x105, 7)
    Sleep(500)

    ChrTalk(    #8
        0x106,
        "#057FDeen, you son of a...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        "...\x02",
    )

    CloseMessageWindow()

    def lambda_AAA():
        OP_8E(0xFE, 0x4B0, 0x0, 0xB0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AAA)

    def lambda_AC5():
        OP_8E(0xFE, 0xFFFFFC18, 0x0, 0x100, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_AC5)
    WaitChrThread(0xC, 0x1)
    SetChrChipByIndex(0xC, 1)
    OP_22(0x1FC, 0x0, 0x64)
    OP_8C(0xC, 180, 0)
    WaitChrThread(0xB, 0x1)
    SetChrChipByIndex(0xB, 1)
    OP_22(0x1FC, 0x0, 0x64)
    OP_8C(0xB, 180, 0)

    ChrTalk(    #10
        0x106,
        (
            "#057FThis is just perfect...\x02\x03",

            "Now I don't know what kind\x01",
            "of drugs you're smoking...\x02\x03",

            "#054FBut if I have to beat some sense\x01",
            "back into you I will!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x105, 0x1000)
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x101, 8)

    def lambda_BBB():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BBB)
    Sleep(50)
    SetChrChipByIndex(0x102, 9)

    def lambda_BE0():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BE0)
    SetChrChipByIndex(0x105, 37)

    def lambda_C00():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C00)
    SetChrChipByIndex(0xB, 2)

    def lambda_C20():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C20)
    Sleep(100)
    SetChrChipByIndex(0xC, 2)

    def lambda_C45():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C45)
    Sleep(50)
    SetChrChipByIndex(0x8, 22)

    def lambda_C6A():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C6A)
    OP_44(0x106, 0xFF)
    SetChrChipByIndex(0x106, 13)

    def lambda_C8E():
        OP_99(0x106, 0x0, 0x5, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_C8E)

    def lambda_C9E():
        OP_95(0x106, 0x0, 0x0, 0x5DC, 0x5DC, 0x1B58)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_C9E)
    Sleep(300)
    Battle(0x38F, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_CD4"),
        (SWITCH_DEFAULT, "loc_CD7"),
    )


    label("loc_CD4")

    OP_B4(0x0)
    Return()

    label("loc_CD7")

    EventBegin(0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x105, 0xFF)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    ClearChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrChipByIndex(0x105, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrChipByIndex(0x102, 35)
    OP_6D(340, 0, 4960, 0)
    OP_44(0x8, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    SetChrPos(0x102, 860, 0, 4710, 90)
    SetChrPos(0x106, -830, 0, 4400, 0)
    SetChrPos(0x101, 420, 0, 3000, 0)
    SetChrPos(0x105, -880, 0, 2850, 0)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xC, 0x1)
    SetChrPos(0x8, -240, 0, 6100, 225)
    SetChrPos(0xB, 1680, 0, 4920, 180)
    SetChrPos(0xC, -1990, 0, 5180, 315)
    SetChrChipByIndex(0x8, 23)
    SetChrChipByIndex(0xB, 36)
    SetChrChipByIndex(0xC, 36)
    OP_51(0x8, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #11
        0x101,
        (
            "#009FI-I can't believe it...\x02\x03",

            "These guys are a hundred times stronger\x01",
            "than when we dealt with them at\x01",
            "the warehouse!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x105,
        (
            "#043FThey appear to be acting rather\x01",
            "strange... I wonder what's going\x01",
            "on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x106,
        (
            "#057FHmm...\x02\x03",

            "It looks like they're being controlled\x01",
            "by someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#004FC-Controlled...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x102)

    ChrTalk(    #15
        0x102,
        "#015FYeah, I agree.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x102, 400)
    TurnDirection(0x105, 0x102, 400)
    Fade(250)
    SetChrChipByIndex(0x102, 65535)
    OP_0D()
    Sleep(500)
    OP_8C(0x102, 225, 400)

    ChrTalk(    #16
        0x102,
        (
            "#012FI'd say it's some sort of special hypnotic\x01",
            "induction using a combination of drugs\x01",
            "and suggestion.\x02\x03",

            "This allows the person controlling\x01",
            "them to draw out their maximum\x01",
            "physical potential.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        "#004FC-Can someone really do that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x106,
        (
            "#057FOf course, but they'd need to be\x01",
            "pretty skilled to even attempt\x01",
            "such a thing.\x02\x03",

            "And I can only think of one group\x01",
            "that could pull off something like\x01",
            "this...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x106, 400)

    ChrTalk(    #19
        0x105,
        (
            "#044FYou have an idea who might\x01",
            "be responsible?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x105, 400)

    ChrTalk(    #20
        0x106,
        (
            "#053FYeah...possibly.\x02\x03",

            "#050FBut there's no time to talk about\x01",
            "it now. Let's head upstairs.\x02\x03",

            "The real perpetrators should be\x01",
            "up there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#006FAll right, let's go!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x439)
    OP_28(0x3E, 0x1, 0x40)
    EventEnd(0x0)
    Return()

    # Function_3_62A end

    def Function_4_11FA(): pass

    label("Function_4_11FA")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(96710, 0, 2960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x105, 7)
    SetChrChipByIndex(0x106, 11)
    SetChrPos(0x101, 96610, 0, 4430, 180)
    SetChrPos(0x102, 95640, 0, 5100, 180)
    SetChrPos(0x106, 97840, 0, 5070, 180)
    SetChrPos(0x105, 96810, 0, 5780, 180)
    SetChrChipByIndex(0x9, 25)
    SetChrChipByIndex(0xD, 1)
    SetChrChipByIndex(0xE, 1)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x9, 96530, 0, -1510, 0)
    SetChrPos(0xD, 94530, 0, -1770, 0)
    SetChrPos(0xE, 98360, 0, -790, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #22
        0x9,
        "#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#005FHere they come again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        (
            "#012FIt looks like we don't have any\x01",
            "choice but to put them down the\x01",
            "hard way...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 26)

    def lambda_137E():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_137E)
    Sleep(50)
    SetChrChipByIndex(0xD, 2)

    def lambda_13A3():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_13A3)
    Sleep(50)
    SetChrChipByIndex(0xE, 2)

    def lambda_13C8():
        OP_90(0xFE, 0x0, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_13C8)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x105, 0x1000)
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x101, 8)

    def lambda_13FC():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13FC)
    Sleep(50)
    SetChrChipByIndex(0x102, 9)

    def lambda_1421():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1421)
    Sleep(50)
    SetChrChipByIndex(0x106, 12)

    def lambda_1446():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1446)
    Sleep(50)
    SetChrChipByIndex(0x105, 37)

    def lambda_146B():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_146B)
    Sleep(200)
    Battle(0x390, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_149E"),
        (SWITCH_DEFAULT, "loc_14A1"),
    )


    label("loc_149E")

    OP_B4(0x0)
    Return()

    label("loc_14A1")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x105, 0xFF)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    ClearChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrChipByIndex(0x105, 65535)
    OP_44(0x9, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    SetChrFlags(0xD, 0x800)
    SetChrFlags(0xE, 0x800)
    ClearChrFlags(0xD, 0x1)
    ClearChrFlags(0xE, 0x1)
    SetChrChipByIndex(0x9, 27)
    SetChrChipByIndex(0xD, 36)
    SetChrChipByIndex(0xE, 36)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 102640, 0, 1840, 270)
    SetChrPos(0xD, 101950, 0, 3240, 0)
    SetChrPos(0xE, 101850, 0, 770, 135)
    OP_6D(100640, 0, 1850, 0)
    SetChrPos(0x101, 100640, 0, 1850, 95)
    SetChrPos(0x102, 100640, 0, 1850, 95)
    SetChrPos(0x106, 100640, 0, 1850, 95)
    SetChrPos(0x105, 100640, 0, 1850, 95)
    FadeToBright(1000, 0)
    OP_A2(0x43A)
    EventEnd(0x0)
    Return()

    # Function_4_11FA end

    def Function_5_15C0(): pass

    label("Function_5_15C0")

    ClearMapFlags(0x1)
    EventBegin(0x0)
    OP_6D(102090, 0, 102370, 0)
    SetChrChipByIndex(0xA, 29)
    SetChrChipByIndex(0xF, 1)
    SetChrChipByIndex(0x10, 1)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x105, 7)
    SetChrChipByIndex(0x106, 11)
    SetChrPos(0x101, 104660, 0, 103320, 225)
    SetChrPos(0x102, 104440, 0, 104470, 225)
    SetChrPos(0x106, 103330, 0, 103120, 225)
    SetChrPos(0x105, 103150, 0, 104290, 225)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, 98520, 0, 98750, 45)
    SetChrPos(0xF, 97520, 0, 99170, 45)
    SetChrPos(0x10, 99010, 0, 97700, 45)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #25
        0xA,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x105,
        (
            "#043FI'm really sorry about this...\x02\x03",

            "I really don't want to fight with\x01",
            "anyone being controlled, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x106,
        (
            "#053FThis isn't the time to be\x01",
            "holding back.\x02\x03",

            "#054FWe don't need to kill them,\x01",
            "just knock them out!\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x105, 0x1000)
    SetChrFlags(0x106, 0x1000)
    SetChrChipByIndex(0xA, 30)

    def lambda_1788():
        OP_90(0xFE, 0xBB8, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1788)
    Sleep(50)
    SetChrChipByIndex(0xF, 2)

    def lambda_17AD():
        OP_90(0xFE, 0xBB8, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_17AD)
    Sleep(50)
    SetChrChipByIndex(0x10, 2)

    def lambda_17D2():
        OP_90(0xFE, 0xBB8, 0x0, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_17D2)
    SetChrChipByIndex(0x106, 12)

    def lambda_17F2():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_17F2)
    Sleep(50)
    SetChrChipByIndex(0x105, 37)

    def lambda_1817():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1817)
    Sleep(50)
    SetChrChipByIndex(0x101, 8)

    def lambda_183C():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_183C)
    Sleep(50)
    SetChrChipByIndex(0x102, 9)

    def lambda_1861():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1861)
    Sleep(300)
    Battle(0x391, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1894"),
        (SWITCH_DEFAULT, "loc_1897"),
    )


    label("loc_1894")

    OP_B4(0x0)
    Return()

    label("loc_1897")

    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    ClearChrFlags(0x106, 0x1000)
    OP_6D(100440, 0, 98970, 0)
    SetChrPos(0x101, 100440, 0, 98970, 90)
    SetChrPos(0x102, 100440, 0, 98970, 90)
    SetChrPos(0x106, 100440, 0, 98970, 90)
    SetChrPos(0x105, 100440, 0, 98970, 90)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x105, 0xFF)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x106, 65535)
    SetChrChipByIndex(0x105, 65535)
    OP_44(0xA, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    SetChrFlags(0xF, 0x800)
    SetChrFlags(0x10, 0x800)
    ClearChrFlags(0xF, 0x1)
    ClearChrFlags(0x10, 0x1)
    SetChrChipByIndex(0xA, 31)
    SetChrChipByIndex(0xF, 36)
    SetChrChipByIndex(0x10, 36)
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, 102990, 0, 98020, 270)
    SetChrPos(0xF, 104030, 0, 99080, 0)
    SetChrPos(0x10, 102870, 0, 100160, 135)
    FadeToBright(1000, 0)
    OP_A2(0x43B)
    EventEnd(0x0)
    Return()

    # Function_5_15C0 end

    def Function_6_19B6(): pass

    label("Function_6_19B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19C3")
    Return()

    label("loc_19C3")

    OP_A2(0x43C)
    ClearMapFlags(0x1)
    EventBegin(0x0)

    def lambda_19D3():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_19D3)

    def lambda_19E1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_19E1)

    def lambda_19EF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_19EF)

    def lambda_19FD():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_19FD)
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x1, 0x1)
    WaitChrThread(0x2, 0x1)
    WaitChrThread(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A64")

    ChrTalk(    #28
        0x101,
        "#004FHey... You hear that?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B62")

    label("loc_1A64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB7")

    ChrTalk(    #29
        0x102,
        (
            "#012FHold on a minute. There's more\x01",
            "than one person talking...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B62")

    label("loc_1AB7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B17")

    ChrTalk(    #30
        0x105,
        (
            "#044FHuh...? I know I've heard one of those\x01",
            "voices from somewhere before...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B62")

    label("loc_1B17")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B62")

    ChrTalk(    #31
        0x106,
        (
            "#057FQuiet. I think I can make out\x01",
            "what they're saying...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B62")

    OP_20(0x5DC)
    Sleep(100)
    Fade(1000)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x13, -1490, 0, 198560, 270)
    SetChrPos(0x11, -2330, 0, 199540, 180)
    SetChrPos(0x12, -2780, 0, 198270, 90)
    OP_6D(-2200, 0, 198720, 0)
    OP_67(0, 7710, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_21()
    OP_1D(0x51)
    OP_0D()
    Sleep(500)

    ChrTalk(    #32
        0x13,
        (
            "#675FHeh heh heh...\x01",
            "A job well done.\x02\x03",

            "Now we'll be able to blame this mess\x01",
            "on those punks and everything will\x01",
            "work out perfectly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x11,
        (
            "So, I take it that you're satisfied\x01",
            "with our work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x13,
        (
            "#675FYes. You've handled things nicely.\x02\x03",

            "But just to make sure...\x01",
            "You haven't left any incriminating\x01",
            "evidence, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x12,
        (
            "Ha ha. You've got nothing to worry\x01",
            "about there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x12,
        (
            "And even when those fools regain\x01",
            "their senses, they won't remember\x01",
            "a thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        (
            "The lighthouse keeper shouldn't\x01",
            "wake up until morning either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x13,
        (
            "#675FI'm relieved to hear that.\x02\x03",

            "With this, the matron of that\x01",
            "orphanage should give up on\x01",
            "her dreams of rebuilding it...\x02\x03",

            "And the series of incidents along\x01",
            "with this arson will end up looking\x01",
            "like the work of those lowlifes.\x02\x03",

            "We can get two birds with one\x01",
            "stone. It's perfect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x12,
        (
            "We are glad to see that our clients\x01",
            "are happy with our work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        (
            "However, if you don't mind me asking,\x01",
            "what's the benefit in destroying that\x01",
            "orphanage...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x11,
        (
            "That's the one thing I've been having\x01",
            "a hard time understanding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x13,
        (
            "#675FHeh! Puh-lease. If you really want\x01",
            "to know so bad, I'll let you in\x01",
            "on the secret.\x02\x03",

            "The mayor intends to transform that\x01",
            "entire area into a series of very,\x01",
            "VERY upscale vacation homes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x11,
        "Interesting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x13,
        (
            "#675FA scenic seaside area not far\x01",
            "from Ruan City...\x02\x03",

            "What more favorable geographic\x01",
            "conditions could there be than\x01",
            "that for a vacation home?\x02\x03",

            "We'll build lavish estates there\x01",
            "and then sell them off to the\x01",
            "highest bidders.\x02\x03",

            "That's been the mayor's plan\x01",
            "all along.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x12,
        (
            "Now, that's a ritzy plan if ever\x01",
            "I've heard one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x12,
        (
            "But, I still don't get why it was\x01",
            "necessary to burn the orphanage\x01",
            "to the ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x13,
        (
            "#675FHa ha, think about it.\x02\x03",

            "Imagine trying to sell a luxury estate\x01",
            "to someone with a ramshackle place\x01",
            "like that marring the view.\x02\x03",

            "Not to mention all the little brats\x01",
            "running around close by and making\x01",
            "a ruckus.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x11,
        (
            "I see... Something like that would\x01",
            "definitely cut their value in half.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        (
            "But instead of going to an extreme\x01",
            "like that, why not just buy up the\x01",
            "place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x13,
        (
            "#675FHa! You didn't really think that stubborn\x01",
            "woman would sell off the land left to her\x01",
            "by her late husband, did you?\x02\x03",

            "And if we were to haul away the burned out remains\x01",
            "while they were away and built something in its\x01",
            "place, there's not much they could do, could they?\x02\x03",

            "Heh heh heh... And since they have no money\x01",
            "to rebuild the place, they'll have no choice\x01",
            "but to accept their fate.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)
    SetChrFlags(0x105, 0x1000)
    SetChrFlags(0x106, 0x1000)
    SetChrPos(0x101, 3950, 0, 204590, 225)
    SetChrPos(0x102, 3860, 0, 205710, 225)
    SetChrPos(0x106, 2790, 0, 204560, 225)
    SetChrPos(0x105, 2640, 0, 205560, 225)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x105, 7)
    SetChrChipByIndex(0x106, 11)

    ChrTalk(    #51
        0x105,
        "#6PThat was your reasoning...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1200)

    def lambda_264B():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_264B)

    def lambda_2659():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2659)

    def lambda_2667():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2667)

    def lambda_2675():
        OP_6D(1330, 0, 201850, 2000)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2675)

    def lambda_268D():
        OP_67(0, 6000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_268D)

    def lambda_26A5():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_26A5)
    WaitChrThread(0x14, 0x1)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x13, 0xFFFFF952, 0x0, 0x304F8, 0x1388, 0x0)

    ChrTalk(    #52
        0x13,
        (
            "#676FH-How long have you been\x01",
            "standing there...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x105,
        (
            "#049FFor something like that...?\x02\x03",

            "You hurt Matron Theresa and the children and\x01",
            "burned their memories to ashes...\x02\x03",

            "You deprived those children\x01",
            "of their smiles...for that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x13,
        (
            "#674FH-How did you know we\x01",
            "were here?!\x02\x03",

            "But before that...what are those\x01",
            "lowlifes doing downstairs?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#006F#4PToo bad for you. They're taking\x01",
            "a loooong nap.\x02\x03",

            "Tsk. And to think that the mayor\x01",
            "was behind it all.\x02\x03",

            "Plus some faces we've seen before\x01",
            "seem to be involved, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x11,
        (
            "So...you know who we are,\x01",
            "do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x12,
        (
            "We have been...briefly acquainted\x01",
            "with that redheaded bracer before...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x106,
        (
            "#057FHa!\x02\x03",

            "So running off like dogs with your tails\x01",
            "between your legs and siccing some monsters\x01",
            "on me means we're acquainted, huh?\x02\x03",

            "But now I've finally got you where\x01",
            "I want you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x13,
        (
            "#674FK-Kill them! Kill them all!\x02\x03",

            "Now that they've seen my face, I\x01",
            "can't let them walk out of here\x01",
            "alive!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x105,
        (
            "#042FIt's unfortunate that you've\x01",
            "fallen this far, Gilbert...\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x12, 0xFFFFFA06, 0x0, 0x3099E, 0xBB8, 0x0)
    TurnDirection(0x12, 0x106, 0)
    SetChrChipByIndex(0x12, 38)

    ChrTalk(    #61
        0x11,
        (
            "Well, since this is a request from\x01",
            "our client, I guess we'll just have\x01",
            "to comply.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 41)

    ChrTalk(    #62
        0x12,
        "Let's see what you've got, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x101,
        "#006F#4PThat's exactly what I was thinking!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x105,
        (
            "#042FJust because you're 'hired help',\x01",
            "don't think that you're any less\x01",
            "responsible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x106,
        (
            "#054FI think it's time to make you taste\x01",
            "the power of the Heavy Blade!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 39)

    def lambda_2C3F():
        OP_91(0xFE, 0xBB8, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2C3F)
    Sleep(100)
    SetChrChipByIndex(0x12, 42)

    def lambda_2C64():
        OP_91(0xFE, 0xBB8, 0x0, 0xBB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2C64)
    SetChrChipByIndex(0x106, 12)

    def lambda_2C84():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2C84)
    Sleep(50)
    SetChrChipByIndex(0x105, 37)

    def lambda_2CA9():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2CA9)
    Sleep(50)
    SetChrChipByIndex(0x101, 8)

    def lambda_2CCE():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CCE)
    Sleep(50)
    SetChrChipByIndex(0x102, 9)

    def lambda_2CF3():
        OP_90(0xFE, 0xFFFFF448, 0x0, 0xFFFFF448, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2CF3)
    Sleep(300)
    Battle(0x392, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_2D26"),
        (SWITCH_DEFAULT, "loc_2D29"),
    )


    label("loc_2D26")

    OP_B4(0x0)
    Return()

    label("loc_2D29")

    EventBegin(0x0)
    OP_6D(-390, 0, 200780, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x106, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x105, 7)
    SetChrChipByIndex(0x106, 11)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x106, 0)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x11, 38)
    SetChrChipByIndex(0x12, 41)
    OP_51(0x11, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x13, -600, 0, 197930, 0)
    SetChrPos(0x11, -2220, 0, 197930, 45)
    SetChrPos(0x12, -3180, 0, 199000, 45)
    SetChrPos(0x101, 1470, 0, 201530, 225)
    SetChrPos(0x106, 400, 0, 201760, 225)
    SetChrPos(0x102, 120, 0, 202880, 225)
    SetChrPos(0x105, 1590, 0, 202760, 225)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #66
        0x13,
        "#676FTh-This can't be...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x106,
        (
            "#057F#6PGilbert, steward of the mayor,\x01",
            "and you boys in black.\x02\x03",

            "In accordance with the laws of the\x01",
            "Bracer Guild, you are hereby placed\x01",
            "under arrest.\x02\x03",

            "Give it up and surrender.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x13,
        "#676FUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        (
            "#2PYou're pretty tough,\x01",
            "I'll give you that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x11,
        (
            "#2PGoing toe-to-toe with you hasn't\x01",
            "disappointed me at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x12,
        (
            "Ah, the lieutenant's going to be mad.\x01",
            "He warned us about this. We shouldn't\x01",
            "have been as careless as we were.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        (
            "#012FThe lieutenant...?\x02\x03",

            "Do you mean that guy wearing the\x01",
            "red mask who was negotiating with\x01",
            "the sky bandits?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x11,
        (
            "#2PI'm surprised you know\x01",
            "about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x12,
        (
            "It looks like you dogs from the guild\x01",
            "are better at sniffing things out than\x01",
            "we thought...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        (
            "#005FYour insults are pretty funny\x01",
            "considering we just gave you\x01",
            "a serious beat-down.\x02\x03",

            "Now hurry up and throw down\x01",
            "your weapons and surrender!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x11,
        "#2PSorry, but we can't do that.\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x11, 17)
    OP_8E(0x11, 0xFFFFF970, 0x0, 0x30494, 0x5DC, 0x0)
    TurnDirection(0x11, 0x13, 400)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x11, 43)
    OP_22(0xD8, 0x0, 0x64)
    Sleep(500)
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x13, 0x11, 400)

    ChrTalk(    #77
        0x13,
        "#676F#2PWha--?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#005FWh-What do you think\x01",
            "you're doing?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x11,
        "#1PDon't move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x11,
        (
            "#1PCome any closer and this guy's\x01",
            "brains are going to be splattered\x01",
            "all over this place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x13,
        (
            "#674F#2PWh-What is the meaning\x01",
            "of this?!\x02\x03",

            "What do you intend to do by\x01",
            "threatening your employer?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x11,
        "#1PYou're wrong about that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x11,
        (
            "#1PYou are not our employer,\x01",
            "the mayor is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x12,
        (
            "#1PBut whether it was you or the\x01",
            "mayor here, the outcome would've\x01",
            "been the same.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x12,
        (
            "#1PWe only cooperated with you\x01",
            "because we shared a mutual\x01",
            "interest...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x11,
        (
            "#1PAnd we couldn't care less whether\x01",
            "you live or die.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_9E(0x13, 0x32, 0x0, 0x258, 0x1770)

    ChrTalk(    #87
        0x13,
        (
            "#676F#2PP-Please...\x02\x03",

            "Don't shoot! Don't shoot me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x106,
        (
            "#057F#6PCut the tears and the crap.\x02\x03",

            "Don't think you can get away by\x01",
            "trying to fool us with a show\x01",
            "like that...\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x11, 0x0, 0x2, 0x7D0)
    OP_22(0x1F7, 0x0, 0x64)

    def lambda_3517():
        OP_99(0xFE, 0x3, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3517)

    def lambda_3527():
        OP_6D(1400, 0, 201500, 1000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3527)
    OP_96(0x13, 0x2EE, 0x0, 0x30782, 0x64, 0x1388)
    SetChrChipByIndex(0x13, 44)
    LoadEffect(0x0, "map\\\\mp020_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 700, 0, 198510, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    OP_9E(0x13, 0x32, 0x0, 0x258, 0x1770)

    ChrTalk(    #89
        0x13,
        (
            "#677F#2PGyaaah...\x02\x03",

            "#677FMy leg! Aaaaah, my leg!!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x105,
        "#046FG-Gilbert?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x106,
        "#057F#3PTch...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x102,
        (
            "#012FLooks like they were serious\x01",
            "about what they said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x12,
        (
            "If this isn't enough of a show\x01",
            "for you...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x14, 400)
    SetChrFlags(0x12, 0x20)
    SetChrSubChip(0x12, 0)
    SetChrChipByIndex(0x12, 43)
    ClearChrFlags(0x12, 0x20)

    ChrTalk(    #94
        0x12,
        (
            "...then how about we blow the brains\x01",
            "out of the lighthouse keeper?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        "#005F#4PH-He has nothing to do with this!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x106, 400)

    ChrTalk(    #96
        0x11,
        (
            "If his life means anything to you,\x01",
            "then I suggest you back up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x11,
        (
            "Let's see...\x01",
            "Like over by the stairs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x106,
        (
            "#050F#3PSeems we don't have much\x01",
            "of a choice...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_37C2():
        OP_6D(530, 0, 202030, 2000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_37C2)
    SetChrChipByIndex(0x105, 65535)

    def lambda_37DF():
        OP_8F(0xFE, 0xE06, 0x0, 0x321D6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_37DF)
    Sleep(100)
    SetChrChipByIndex(0x102, 65535)

    def lambda_3804():
        OP_8F(0xFE, 0x9EC, 0x0, 0x32208, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3804)
    Sleep(100)
    SetChrChipByIndex(0x101, 65535)

    def lambda_3829():
        OP_8F(0xFE, 0xE9C, 0x0, 0x31D4E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3829)
    Sleep(100)
    SetChrChipByIndex(0x106, 33)

    def lambda_384E():
        OP_8F(0xFE, 0xA0A, 0x0, 0x31CE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_384E)
    Sleep(200)
    WaitChrThread(0x106, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x105, 0x1)

    ChrTalk(    #99
        0x12,
        (
            "Hahaha...\x01",
            "That's right, do what you're told\x01",
            "like the dogs you are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x11,
        (
            "And it looks like this is where\x01",
            "we bid you farewell.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3904():

        label("loc_3904")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_3904")

    QueueWorkItem2(0x101, 2, lambda_3904)

    def lambda_3915():

        label("loc_3915")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_3915")

    QueueWorkItem2(0x102, 2, lambda_3915)

    def lambda_3926():

        label("loc_3926")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_3926")

    QueueWorkItem2(0x105, 2, lambda_3926)

    def lambda_3937():

        label("loc_3937")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_3937")

    QueueWorkItem2(0x106, 2, lambda_3937)
    SetChrChipByIndex(0x11, 42)

    def lambda_394D():
        OP_6D(3130, 0, 201480, 2000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_394D)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x11, 0x4)
    OP_8E(0x11, 0xFFFFF02E, 0x0, 0x2FAA8, 0x1770, 0x0)
    ClearChrFlags(0x11, 0x4)
    OP_8E(0x11, 0xFFFFF592, 0x0, 0x2FB5C, 0x1770, 0x0)

    def lambda_399C():

        label("loc_399C")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_399C")

    QueueWorkItem2(0x106, 2, lambda_399C)
    OP_8E(0x11, 0x7D9, 0x3E8, 0x2FA80, 0x1770, 0x0)

    def lambda_39C1():
        OP_8E(0x11, 0x1DEC, 0x3E8, 0x31100, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_39C1)
    Sleep(100)
    SetChrChipByIndex(0x12, 42)
    OP_8F(0x12, 0x3DE, 0x0, 0x30B88, 0xFA0, 0x0)
    OP_8F(0x12, 0xDFC, 0x0, 0x30778, 0xFA0, 0x0)
    OP_22(0xA3, 0x0, 0x64)
    OP_96(0x12, 0x12C0, 0x3E8, 0x3055C, 0x7D0, 0x1770)

    def lambda_3A2A():
        OP_8E(0x12, 0x1DEC, 0x3E8, 0x31100, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_3A2A)
    WaitChrThread(0x11, 0x1)
    OP_4A(0x11, 1)
    OP_4A(0x12, 1)
    OP_6F(0x0, 20)
    OP_48()
    OP_6F(0x0, 40)
    OP_48()
    OP_70(0x0, 0x50)
    OP_4B(0x11, 1)
    OP_4B(0x12, 1)

    def lambda_3A71():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_3A71)

    def lambda_3A83():
        OP_8E(0xFE, 0x22F6, 0x3E8, 0x3124A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_3A83)
    WaitChrThread(0x12, 0x1)

    def lambda_3AA3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_3AA3)

    def lambda_3AB5():
        OP_8E(0xFE, 0x22F6, 0x3E8, 0x3124A, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_3AB5)

    ChrTalk(    #101
        0x101,
        "#005FWait!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x106,
        (
            "#054FDon't think you're getting away\x01",
            "this time!\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    ClearChrFlags(0x105, 0x1000)
    ClearChrFlags(0x106, 0x1000)
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C2200   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_6_19B6 end

    def Function_7_3B41(): pass

    label("Function_7_3B41")

    OP_93(0x13, 0x106, 0x258, 0x2EE0, 0x0)

    ChrTalk(    #103 op#5
        0x13,
        "#670FArgh...\x05\x02",
    )

    TurnDirection(0x106, 0x13, 0)
    TurnDirection(0x13, 0x106, 0)

    def lambda_3B75():
        OP_94(0x1, 0x13, 0x0, 0x258, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3B75)
    OP_94(0x1, 0x106, 0xB4, 0x258, 0x1770, 0x0)
    Return()

    # Function_7_3B41 end

    def Function_8_3B95(): pass

    label("Function_8_3B95")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3BAB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3BAB)
    SetChrChipByIndex(0x101, 8)
    OP_8E(0xFE, 0xB5E, 0x0, 0x327DA, 0x1388, 0x0)
    OP_8E(0xFE, 0xC6C, 0x0, 0x32546, 0x1388, 0x0)
    OP_8E(0x101, 0x6D6, 0x0, 0x31A10, 0x1388, 0x0)
    OP_8C(0xFE, 225, 0)
    SetChrChipByIndex(0x101, 5)
    OP_43(0x101, 0x2, 0x0, 0x2)
    Return()

    # Function_8_3B95 end

    def Function_9_3C0C(): pass

    label("Function_9_3C0C")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3C22():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C22)
    OP_8E(0xFE, 0xB5E, 0x0, 0x327DA, 0x1388, 0x0)
    OP_8E(0xFE, 0xC6C, 0x0, 0x32546, 0x1388, 0x0)
    OP_8E(0x105, 0x456, 0x0, 0x31CB8, 0x1388, 0x0)
    OP_8C(0xFE, 225, 0)
    Return()

    # Function_9_3C0C end

    def Function_10_3C72(): pass

    label("Function_10_3C72")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3C88():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3C88)
    SetChrChipByIndex(0x102, 9)
    OP_8E(0xFE, 0xB5E, 0x0, 0x327DA, 0x1388, 0x0)
    OP_8E(0xFE, 0xC6C, 0x0, 0x32546, 0x1388, 0x0)
    OP_8E(0x102, 0x852, 0x0, 0x32096, 0x1388, 0x0)
    OP_8E(0x102, 0x30C, 0x0, 0x320DC, 0x1388, 0x0)
    OP_8C(0xFE, 225, 0)
    SetChrChipByIndex(0x102, 6)
    OP_43(0x102, 0x2, 0x0, 0x2)
    Return()

    # Function_10_3C72 end

    def Function_11_3CFD(): pass

    label("Function_11_3CFD")

    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_3D13():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3D13)
    SetChrChipByIndex(0x106, 12)
    OP_8E(0xFE, 0xB5E, 0x0, 0x327DA, 0x1388, 0x0)
    OP_8E(0xFE, 0xC6C, 0x0, 0x32546, 0x1388, 0x0)
    OP_8E(0x106, 0xD2A, 0x0, 0x31AF6, 0x1388, 0x0)
    OP_8C(0xFE, 225, 0)
    SetChrChipByIndex(0x106, 11)
    OP_43(0x106, 0x2, 0x0, 0x2)
    Return()

    # Function_11_3CFD end

    SaveToFile()

Try(main)
