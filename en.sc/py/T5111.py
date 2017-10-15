from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T5111   ._SN',
        MapName             = 'Other',
        Location            = 'T5111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60084",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Anelace',                              # 9
        'Kurt',                                 # 10
        'Robert',                               # 11
        'Phyllis',                              # 12
        'Jaeger',                               # 13
        'Jaeger Woman',                         # 14
        'Targeted Smoke Bomb',                  # 15
        'Targeting Camera',                     # 16
        'Dish',                                 # 17
        'Dish',                                 # 18
        'Dish',                                 # 19
        'Coffee',                               # 20
        'Coffee',                               # 21
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
        'ED6_DT27/CH03090 ._CH',             # 00
        'ED6_DT27/CH03003 ._CH',             # 01
        'ED6_DT27/CH03093 ._CH',             # 02
        'ED6_DT07/CH00411 ._CH',             # 03
        'ED6_DT07/CH01450 ._CH',             # 04
        'ED6_DT27/CH03900 ._CH',             # 05
        'ED6_DT07/CH00341 ._CH',             # 06
        'ED6_DT07/CH00261 ._CH',             # 07
        'ED6_DT06/CH20008 ._CH',             # 08
        'ED6_DT06/CH20020 ._CH',             # 09
        'ED6_DT07/CH00414 ._CH',             # 0A
        'ED6_DT06/CH20020 ._CH',             # 0B
        'ED6_DT06/CH20021 ._CH',             # 0C
        'ED6_DT07/CH01620 ._CH',             # 0D
        'ED6_DT27/CH04000 ._CH',             # 0E
        'ED6_DT07/CH00420 ._CH',             # 0F
        'ED6_DT27/CH04820 ._CH',             # 10
        'ED6_DT27/CH04821 ._CH',             # 11
        'ED6_DT27/CH04640 ._CH',             # 12
        'ED6_DT27/CH04641 ._CH',             # 13
        'ED6_DT06/CH20067 ._CH',             # 14
        'ED6_DT27/CH04001 ._CH',             # 15
        'ED6_DT07/CH00421 ._CH',             # 16
        'ED6_DT27/CH03005 ._CH',             # 17
        'ED6_DT27/CH03093 ._CH',             # 18
        'ED6_DT27/CH03133 ._CH',             # 19
        'ED6_DT27/CH03091 ._CH',             # 1A
        'ED6_DT27/CH04824 ._CH',             # 1B
        'ED6_DT26/CH20265 ._CH',             # 1C
        'ED6_DT26/CH20267 ._CH',             # 1D
    )

    AddCharChipPat(
        'ED6_DT27/CH03090P._CP',             # 00
        'ED6_DT27/CH03003P._CP',             # 01
        'ED6_DT27/CH03093P._CP',             # 02
        'ED6_DT07/CH00411P._CP',             # 03
        'ED6_DT07/CH01450P._CP',             # 04
        'ED6_DT27/CH03900P._CP',             # 05
        'ED6_DT07/CH00341P._CP',             # 06
        'ED6_DT07/CH00261P._CP',             # 07
        'ED6_DT06/CH20008P._CP',             # 08
        'ED6_DT06/CH20000P._CP',             # 09
        'ED6_DT07/CH00414P._CP',             # 0A
        'ED6_DT06/CH20020P._CP',             # 0B
        'ED6_DT06/CH20021P._CP',             # 0C
        'ED6_DT07/CH01620P._CP',             # 0D
        'ED6_DT27/CH04000P._CP',             # 0E
        'ED6_DT07/CH00420P._CP',             # 0F
        'ED6_DT27/CH04820P._CP',             # 10
        'ED6_DT27/CH04821P._CP',             # 11
        'ED6_DT27/CH04640P._CP',             # 12
        'ED6_DT27/CH04641P._CP',             # 13
        'ED6_DT06/CH20067P._CP',             # 14
        'ED6_DT27/CH04001P._CP',             # 15
        'ED6_DT07/CH00421P._CP',             # 16
        'ED6_DT27/CH03005P._CP',             # 17
        'ED6_DT27/CH03093P._CP',             # 18
        'ED6_DT27/CH03133P._CP',             # 19
        'ED6_DT27/CH03091P._CP',             # 1A
        'ED6_DT27/CH04824P._CP',             # 1B
        'ED6_DT26/CH20265P._CP',             # 1C
        'ED6_DT26/CH20267P._CP',             # 1D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 26690,
        Z                   = 0,
        Y                   = 5140,
        Direction           = 270,
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
        X                   = 24500,
        Z                   = 0,
        Y                   = 12470,
        Direction           = 270,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Direction           = 180,
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
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1900553,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1E6,
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
        NpcIndex            = 0x80,
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
        Unknown3            = 65547,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65547,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 65547,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1572875,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
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
        Unknown3            = 1638411,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 120250,
        Y                   = 0,
        Z                   = 1000,
        Range               = 123170,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7D0,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )


    DeclActor(
        TriggerX            = 25470,
        TriggerZ            = -300,
        TriggerY            = 4940,
        TriggerRange        = 800,
        ActorX              = 26690,
        ActorZ              = 1500,
        ActorY              = 5140,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 22500,
        TriggerZ            = 0,
        TriggerY            = 12360,
        TriggerRange        = 800,
        ActorX              = 24500,
        ActorZ              = 1500,
        ActorY              = 12470,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 85780,
        TriggerZ            = 0,
        TriggerY            = 41480,
        TriggerRange        = 800,
        ActorX              = 85180,
        ActorZ              = 500,
        ActorY              = 41480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_3C6",          # 00, 0
        "Function_1_4B1",          # 01, 1
        "Function_2_522",          # 02, 2
        "Function_3_5C9",          # 03, 3
        "Function_4_D0B",          # 04, 4
        "Function_5_F7D",          # 05, 5
        "Function_6_F82",          # 06, 6
        "Function_7_11F9",         # 07, 7
        "Function_8_11FE",         # 08, 8
        "Function_9_16DF",         # 09, 9
        "Function_10_26B0",        # 0A, 10
        "Function_11_2F23",        # 0B, 11
        "Function_12_3D49",        # 0C, 12
    )


    def Function_0_3C6(): pass

    label("Function_0_3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48D")
    SetChrPos(0x10, 18160, 800, 11990, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x13, 17670, 800, 12040, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, 17600, 800, 11180, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x14, 18270, 750, 10980, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x12, 18190, 750, 11550, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x8, 115820, 0, 39550, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 88540, 200, -30700, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 25)
    SetChrSubChip(0x9, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x8, 0)
    OP_43(0x8, 0x0, 0x0, 0x2)

    label("loc_48D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_499")
    Event(0, 9)

    label("loc_499")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 4)), scpexpr(EXPR_END)), "loc_4B0")
    Event(0, 11)

    label("loc_4B0")

    Return()

    # Function_0_3C6 end

    def Function_1_4B1(): pass

    label("Function_1_4B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C4")
    OP_64(0x2, 0x1)
    Jump("loc_4C8")

    label("loc_4C4")

    OP_65(0x2, 0x1)

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DF")
    OP_72(0x0, 0x20)
    OP_70(0x19, 0x0)
    Jump("loc_4EB")

    label("loc_4DF")

    OP_72(0x0, 0x20)
    OP_6F(0x19, 60)

    label("loc_4EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x397), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_521")

    label("loc_50C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_521")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_521")

    Return()

    # Function_1_4B1 end

    def Function_2_522(): pass

    label("Function_2_522")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_END)),
        (0, "loc_553"),
        (1, "loc_55F"),
        (2, "loc_56B"),
        (3, "loc_577"),
        (4, "loc_583"),
        (5, "loc_58F"),
        (6, "loc_59B"),
        (SWITCH_DEFAULT, "loc_5A7"),
    )


    label("loc_553")

    OP_99(0xFE, 0x0, 0x7, 0x5AA)
    Jump("loc_5B3")

    label("loc_55F")

    OP_99(0xFE, 0x0, 0x7, 0x60E)
    Jump("loc_5B3")

    label("loc_56B")

    OP_99(0xFE, 0x0, 0x7, 0x640)
    Jump("loc_5B3")

    label("loc_577")

    OP_99(0xFE, 0x0, 0x7, 0x578)
    Jump("loc_5B3")

    label("loc_583")

    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_5B3")

    label("loc_58F")

    OP_99(0xFE, 0x0, 0x7, 0x546)
    Jump("loc_5B3")

    label("loc_59B")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B3")

    label("loc_5A7")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B3")

    label("loc_5B3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5C8")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_5B3")

    label("loc_5C8")

    Return()

    # Function_2_522 end

    def Function_3_5C9(): pass

    label("Function_3_5C9")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_659")
    Jump("loc_69B")

    label("loc_659")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_675")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_69B")

    label("loc_675")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_691")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_69B")

    label("loc_691")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_69B")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x207, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFB")
    OP_A2(0x1039)

    ChrTalk(    #0
        0x9,
        "#840FEstelle, good evening.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1000FHi, Kurt.\x02\x03",

            "Are you reading something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "#840FYes, I'm looking over some military\x01",
            "treatises from the Far East.\x02\x03",

            "The subject is ancient warfare, but you\x01",
            "would be surprised how much of it applies\x01",
            "to conflict of any era.\x02\x03",

            "You should give them a read yourself.\x01",
            "You may find them enlightening.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1016FUhhh, I think I'll pass. I kinda\x01",
            "suspect they'd go over my head.\x02\x03",

            "#1015FFar East military books, though...\x02\x03",

            "Kurt, I've been sort of curious--\x01",
            "are you from the East yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x9,
        (
            "#843FIn a sense, I suppose. I was born\x01",
            "in Liberl, but my family does indeed\x01",
            "hail from the lands beyond Calvard.\x02\x03",

            "We emigrated during the time of my\x01",
            "grandfather, from what I understand.\x02\x03",

            "#840FThe special arts I use are something\x01",
            "that my grandfather passed down to\x01",
            "me, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1011FOh, I see!\x02\x03",

            "I've always thought what you do is pretty\x01",
            "incredible and handy, but I've never seen\x01",
            "anyone else do stuff like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x9,
        (
            "#844FA fair observation. I know of\x01",
            "no other practitioners of the\x01",
            "art aside from myself...\x02\x03",

            "#840FIf you're that interested,\x01",
            "however, I would be honored\x01",
            "to teach it to you, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1004FWhoa, really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        (
            "#840FHaha, really. It would be my pleasure.\x02\x03",

            "However, you would need to study a\x01",
            "number of military treatises first...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#1007FErk...\x02\x03",

            "I think I'm gonna have to pass...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D02")

    label("loc_BFB")


    ChrTalk(    #10
        0x9,
        (
            "#840FWe can learn much from the\x01",
            "writings of past ages.\x02\x03",

            "I do think you should try reading\x01",
            "them at some point, rather than\x01",
            "avoiding them so.\x02\x03",

            "Being a bracer is more than just having\x01",
            "combat skills--they must strive to train\x01",
            "their minds as well. Remember that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D02")

    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Return()

    # Function_3_5C9 end

    def Function_4_D0B(): pass

    label("Function_4_D0B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x207, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECD")
    OP_A2(0x1038)

    ChrTalk(    #11
        0x8,
        (
            "#814FOh, Estelle! Not in bed yet, huh?\x02\x03",

            "Still getting ready for tomorrow?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1011FWell, yeah, that too, but...\x02\x03",

            "What are YOU up to, Anelace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        "#810FI was just talking with Mr. Bear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1004FMr...Bear?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "#1310FIsn't he cuuuute?\x02\x03",

            "#1311FThat soft, plushy fur...\x02\x03",

            "Oooh, just touching it makes me tingly!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#1016FAh...hahaha...\x02\x03",

            "Sooooo this is where you\x01",
            "get your energy from, huh,\x01",
            "Anelace?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        "#816FHeck yeah, it is!\x02",
    )

    CloseMessageWindow()
    Jump("loc_F79")

    label("loc_ECD")


    ChrTalk(    #18
        0x8,
        (
            "#1311FMmmmm... Just touching stuffed animals\x01",
            "makes me feel like a million mira.\x02\x03",

            "#811FYeah! Like I said! Cuteness is justice!\x01",
            "And justice is poweeer! ...Or something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F79")

    TalkEnd(0x8)
    Return()

    # Function_4_D0B end

    def Function_5_F7D(): pass

    label("Function_5_F7D")

    Call(0, 6)
    Return()

    # Function_5_F7D end

    def Function_6_F82(): pass

    label("Function_6_F82")

    TalkBegin(0xB)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 1)), scpexpr(EXPR_END)), "loc_FA2")
    OP_A9(0xFC)
    Jump("loc_FA4")

    label("loc_FA2")

    OP_A9(0xFF)

    label("loc_FA4")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_FAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FBE")
    TalkEnd(0xB)
    Return()

    label("loc_FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x206, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1188")
    OP_A2(0x1036)

    ChrTalk(    #19
        0xB,
        "Estelle! Good job with your training.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        (
            "From the look on your face, Kurt worked\x01",
            "you raw, didn't he?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1007FYeah, I'm exhausted.\x02\x03",

            "#1006FBut, hey, it's part of our training,\x01",
            "so I just gotta buckle down and do it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        "That's the spirit! ㈱\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xB,
        (
            "Well, then, you'd best get supplies\x01",
            "ready for tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xB,
        (
            "Who knows what else Kurt has planned?\x01",
            "Better get ready now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1011FYeah, good idea.\x02\x03",

            "I'll be back to look over stuff, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11F5")

    label("loc_1188")


    ChrTalk(    #26
        0xB,
        (
            "You should get everything you\x01",
            "need ready now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "You're probably going to be very\x01",
            "busy come tomorrow!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11F5")

    TalkEnd(0xB)
    Return()

    # Function_6_F82 end

    def Function_7_11F9(): pass

    label("Function_7_11F9")

    Call(0, 8)
    Return()

    # Function_7_11F9 end

    def Function_8_11FE(): pass

    label("Function_8_11FE")

    TalkBegin(0xA)
    OP_A2(0x1007)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x2D6, 0x0)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BA")

    ChrTalk(    #28
        0xA,
        (
            "Hey, Estelle...is that a 'Heaven's Eye'\x01",
            "quartz you have there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xA,
        (
            "Well, I'll be damned. That's some pretty\x01",
            "high-grade quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xA,
        (
            "You'll need to upgrade an orbment slot\x01",
            "in order to set one of those.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xA,
        (
            "It requires a fair bit of sepith, but it'll also\x01",
            "increase your orbment's EP charge capacity,\x01",
            "so you should give it a try.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        (
            "If you select 'Slots' from 'Upgrade/Exchange,'\x01",
            "you can upgrade your slots.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    OP_A2(0x1041)
    TalkEnd(0xA)
    Return()

    label("loc_13BA")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                  # 0
            "Upgrade/Exchange\x01",      # 1
            "Shop\x01",                  # 2
            "Leave\x01",                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1428")
    OP_0D()
    OP_A9(0xFA)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_1428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1441")
    OP_0D()
    OP_A9(0xFB)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_1441")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1452")
    TalkEnd(0xA)
    Return()

    label("loc_1452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_153D")

    ChrTalk(    #33
        0xA,
        (
            "You can't set a high-grade quartz without\x01",
            "an upgraded slot. You'd damage the\x01",
            "orbment if you tried!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xA,
        (
            "You'll need sepith to upgrade your slots,\x01",
            "but a nice bonus is that the upgrade\x01",
            "increases your max EP capacity, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DB")

    label("loc_153D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1646")
    OP_A2(0x1)

    ChrTalk(    #35
        0xA,
        "Hey, well done today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xA,
        (
            "You got some sepith in today's training,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xA,
        "If you want, try making some new quartz.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xA,
        (
            "It's important to experiment with new things\x01",
            "quartz-wise, if only because you still\x01",
            "need to get used to the new models.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DB")

    label("loc_1646")


    ChrTalk(    #39
        0xA,
        (
            "If you want, try making some more\x01",
            "quartz.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        (
            "What's that saying again? Oh, right!\x01",
            "'Don't think, feel!' Just experiment and\x01",
            "get a feel for it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16DB")

    TalkEnd(0xA)
    Return()

    # Function_8_11FE end

    def Function_9_16DF(): pass

    label("Function_9_16DF")

    EventBegin(0x0)
    OP_70(0x19, 0x0)
    OP_6D(27560, 0, 11600, 0)
    OP_67(0, 5860, -10000, 0)
    OP_6B(3190, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x10A, 0x4)
    SetChrPos(0x10A, 18080, 200, 12890, 180)
    SetChrPos(0x101, 18120, 200, 10470, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x101, 1)
    SetChrChipByIndex(0x10A, 2)
    SetChrPos(0x10, 18160, 800, 11990, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x13, 17670, 800, 12040, 0)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x11, 17600, 800, 11180, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x14, 18270, 800, 10980, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x12, 18190, 800, 11550, 0)
    ClearChrFlags(0x12, 0x80)
    FadeToBright(1000, 0)

    def lambda_17E2():
        OP_6D(18250, 200, 11830, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17E2)

    def lambda_17FA():
        OP_67(0, 7000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_17FA)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #41
        0x10A,
        (
            "#819F#6PPhew! Today was like hardball\x01",
            "played with boulders!\x02\x03",

            "#810FIt sounds like that's almost it for our\x01",
            "training here at Le Locle, though.\x01",
            "Sure feels like it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1015FYeah. I mean, I'm happy to be almost\x01",
            "done, but...it makes me feel a little sad\x01",
            "at the same time, you know?\x02\x03",

            "#1011FEarlier was amazing, too.\x01",
            "Kurt really is strong, isn't he?\x02\x03",

            "He took us both on at once, and I got\x01",
            "the feeling he could've kept going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10A,
        (
            "#811F#6PWell, yeah! He could probably\x01",
            "throw us around like spears!\x02\x03",

            "#816FI mean, he got that 'Artful Tactician'\x01",
            "title because he's the second-best\x01",
            "bracer in all Liberl, y'know!\x02\x03",

            "The very best is your dad, of course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1025FOh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10A,
        (
            "#810F#6POh, yeah, speaking of. I think Schera\x01",
            "mentioned this to you once, but there's\x01",
            "seven ranks for senior bracers--G to A.\x02\x03",

            "I'm ranked F currently since I've\x01",
            "only been senior for half a year...\x02\x03",

            "But Kurt's a B. Pretty much an A, even!\x01",
            "He's getting promoted real soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1011FWow, rank A? That'd put him\x01",
            "on the same level as Zin!\x02\x03",

            "#1003F(Although...there's a certain someone \x01",
            "out there who can not only take down \x01",
            "Kurt, but steal his memory...)\x02\x03",

            "(Do I really have a chance\x01",
            "against someone like that?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10A,
        (
            "#814F#6PUh... Estelle?\x02\x03",

            "What's wrong? You look so...\x01",
            "serious, all of a sudden.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1004FOh!\x02\x03",

            "#1013FS-Sorry, I was just spacing\x01",
            "out for a second, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x10A,
        (
            "#812F#6PSpacing out, huh?\x02\x03",

            "Spacing out about Joshua, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1013FW-Well...\x02\x03",

            "#1025FYou could say that, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10A,
        (
            "#1314F#6PI kinda figured as much...\x02\x03",

            "I, uh...haven't wanted to pry or anything,\x01",
            "but Schera did tell me a little bit about\x01",
            "what happened.\x02\x03",

            "You must be worried sick.\x01",
            "I really do hope he's okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1003FYeah...\x02\x03",

            "#1006FBut, hey! I'm not too worried.\x02\x03",

            "Joshua's just a lost boy who ran away\x01",
            "from home because of a misunderstanding.\x02\x03",

            "#1005FI'll bring him back even if I have to tie a\x01",
            "leash to his neck and walk him home!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10A,
        (
            "#811F#6PTHAT'S the spirit!\x01",
            "(I'd pay good mira to see that, too...)\x02\x03",

            "#816FEstelle, keep that up and you\x01",
            "WILL find Joshua!\x02\x03",

            "I give it my super-shiny senior\x01",
            "bracer guarantee!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1016FHaha! Thanks, Anelace.\x02\x03",

            "#1015FBut, ah...didn't we just finish talking\x01",
            "about how you aren't really that old\x01",
            "or senior yet?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10A,
        (
            "#812F#6PWhaaat? Estelle, you meanieface!\x02\x03",

            "You're saying I'm like a kid,\x01",
            "aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1008F(Urk!) Er, no, nooooo!\x01",
            "That's not what I meant at all!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10A,
        (
            "#1316F#6PMaaaan, and I'm like two years\x01",
            "older than you, too...\x02\x03",

            "#810FWell, to be honest, I'd much rather be\x01",
            "your friend than be your superior.\x02\x03",

            "#811FSo we're friends forever,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#1008FAh...yeah. You bet!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 0)
    ClearChrFlags(0x10A, 0x4)
    SetChrPos(0x10A, 19230, 0, 12970, 98)
    OP_0D()
    SetChrSubChip(0x101, 2)
    TurnDirection(0x10A, 0x101, 400)
    Sleep(500)

    ChrTalk(    #59
        0x10A,
        (
            "#810F#6POoooookay, then! Time to scoot off\x01",
            "to bed and rest for tomorrow!\x02\x03",

            "You seem kinda bushed, Estelle.\x01",
            "You want to skip tomorrow's morning practice?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        (
            "#1006FNo, that's okay.\x02\x03",

            "No matter how tired I get, a good\x01",
            "night's sleep here always seems\x01",
            "to charge me right back up.\x02\x03",

            "As long as you're up for it,\x01",
            "I'm good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10A,
        (
            "#811F#6PSweet! We'll do some more stuffing-beating\x01",
            "tomorrow morning then, 'kay?\x02\x03",

            "#1310FFor now, though, good night!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1011FGood night, Anelace!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x10A, 0x5154, 0x0, 0x2472, 0xBB8, 0x0)

    def lambda_244E():
        OP_8E(0x10A, 0x6CAC, 0x7D0, 0x2346, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_244E)

    def lambda_2469():
        OP_6D(20870, 200, 10700, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2469)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x10A, 0x1)

    def lambda_248B():
        OP_8E(0x10A, 0x6C84, 0x7D0, 0x2ABC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_248B)
    WaitChrThread(0x10A, 0x1)

    def lambda_24AB():
        OP_8E(0x10A, 0x63D8, 0xDAC, 0x2C1A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_24AB)

    def lambda_24C6():
        OP_9F(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_24C6)
    WaitChrThread(0x10A, 0x1)

    def lambda_24DD():
        OP_69(0x101, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24DD)
    WaitChrThread(0x101, 0x1)
    SetChrFlags(0x10A, 0x80)
    SetChrSubChip(0x101, 0)
    Sleep(500)

    ChrTalk(    #63
        0x101,
        (
            "#1012F#6PI AM kind of beat...\x01",
            "Time to go crash into a nice, warm bed.\x02\x03",

            "#1015FThough, hang on, we DID get a lot of sepith\x01",
            "during the training mission today.\x02\x03",

            "#1006FBuilding a new set of quartz sounds like\x01",
            "a good idea right about now. Maybe I\x01",
            "should go bug Robert before going to bed.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(19120, 0, 10210, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    ClearChrFlags(0x101, 0x4)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 19120, 0, 10210, 103)
    RemoveParty(0x9, 0xFF)
    OP_A2(0x100B)
    OP_28(0x7E, 0x1, 0x100)
    OP_28(0x7E, 0x1, 0x200)
    OP_28(0x7E, 0x1, 0x400)
    OP_28(0x7E, 0x1, 0x800)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_9_16DF end

    def Function_10_26B0(): pass

    label("Function_10_26B0")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Stay Up\x01",       # 0
            "Slumber!\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_270B")
    TalkEnd(0xFF)
    Return()

    label("loc_270B")

    EventBegin(0x0)

    ChrTalk(    #64
        0x101,
        (
            "#1007FMrrrr...so tired...\x02\x03",

            "#1000FTime to hit the hay and\x01",
            "get ready for tomorrow...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_20(0x3E8)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x9, 0xFE, 0x0)
    OP_0D()
    Sleep(5000)
    SetChrFlags(0x8, 0x80)
    OP_22(0x1F7, 0x0, 0x1E)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x28)
    Sleep(150)
    OP_22(0x1F7, 0x0, 0x23)
    Sleep(500)
    OP_22(0x1F7, 0x0, 0x28)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x32)
    Sleep(150)
    OP_22(0x1F7, 0x0, 0x2D)
    Sleep(400)
    OP_22(0x1F7, 0x0, 0x32)
    Sleep(100)
    OP_22(0x1F7, 0x0, 0x3C)
    Sleep(150)
    OP_22(0x1F7, 0x0, 0x37)
    Sleep(300)
    OP_22(0x20F, 0x0, 0x4B)
    Sleep(800)
    OP_22(0x1F7, 0x0, 0x4B)
    Sleep(300)
    OP_22(0x246, 0x0, 0x5A)
    Sleep(800)
    OP_22(0x1F7, 0x0, 0x5A)
    Sleep(400)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrPos(0x101, 85170, 300, 42180, 180)
    SetChrChipByIndex(0x101, 8)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #65
        0x101,
        (
            "#1P#455F(Mm...?)\x02\x03",

            "#452F(Did I...hear something?)\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Wake Up\x01",                   # 0
            "Don't Care. SLUMBER!\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C26")

    ChrTalk(    #66
        0x101,
        (
            "#1P#459F(Nngh...so sleepy...)\x02\x03",

            "#455F(Screw it... Deal w'it...n th' mornin'...)\x02\x03",

            "(...Mmmrrrrrr...)\x02\x03",

            "#456F*snore*\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x72, 0x0, 0x64)
    Sleep(300)
    Sleep(1000)
    SetChrPos(0x8, 86790, 0, 33860, 0)

    NpcTalk(    #67
        0x8,
        "Girl's Voice",
        "#40W#5P...telle...\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    NpcTalk(    #68
        0x8,
        "Girl's Voice",
        "#40W#5PEstelle...you awake...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        "#459F#1P...Mrr?\x02",
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    OP_22(0x1B, 0x0, 0x3C)
    Sleep(300)
    OP_22(0x1C, 0x0, 0x3C)
    Sleep(300)
    OP_22(0x1B, 0x0, 0x46)
    Sleep(300)
    OP_22(0x1C, 0x0, 0x46)
    Sleep(300)
    OP_22(0x1B, 0x0, 0x50)
    Sleep(300)
    OP_22(0x1C, 0x0, 0x50)
    Sleep(300)
    OP_22(0x1B, 0x0, 0x5A)
    Sleep(300)
    OP_22(0x1C, 0x0, 0x5A)
    Sleep(300)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1C, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1B, 0x0, 0x64)
    Sleep(300)
    OP_22(0x1C, 0x0, 0x64)
    Sleep(300)
    SetChrPos(0x8, 86100, 0, 41700, 270)
    OP_44(0x8, 0x0)
    Sleep(500)

    ChrTalk(    #70
        0x8,
        "#2P#3SEstelle! Wake up!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#1P#453FAaah!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x8, 86510, 0, 40980, 259)
    SetChrSubChip(0x8, 0)
    ClearChrFlags(0x8, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x0, 60)
    OP_70(0x0, 0x14)
    OP_99(0x101, 0x0, 0x8, 0x4B0)
    OP_99(0x101, 0x11, 0x12, 0x4B0)
    SetChrSubChip(0x101, 23)

    ChrTalk(    #72
        0x101,
        "#453FA-Anelace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#4P#812FEstelle, you're awake! Thank Aidios...\x02\x03",

            "C'mon, grab your gear!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#451FWh-What's wrong?\x01",
            "You look so pale...\x02\x03",

            "And those sounds... W-Wait!\x01",
            "Is that GUNFIRE?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "#4P#815FYeah! We're under attack by...\x01",
            "somebody! I dunno who!\x02\x03",

            "Kurt's trying to fight them off,\x01",
            "but we need to go help him!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E83")

    label("loc_2C26")

    OP_2B(0x7E, 0x3)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x0, 60)
    OP_70(0x0, 0x14)
    OP_99(0x101, 0x0, 0x8, 0x3E8)
    OP_99(0x101, 0x11, 0x12, 0x3E8)

    ChrTalk(    #76
        0x101,
        (
            "#451FMmph. What IS that sound...\x02\x03",

            "#453FW-Wait a minute! Is that GUNFIRE?!\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x72, 0x0, 0x64)
    Sleep(300)
    SetChrPos(0x8, 86790, 0, 33860, 0)

    ChrTalk(    #77
        0x8,
        (
            "#1PEstelle!\x02\x03",

            "Estelle, are you awake?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)
    Sleep(200)
    SetChrPos(0x8, 86530, 0, 35990, 0)
    OP_9F(0x8, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 26)

    def lambda_2D40():
        OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2D40)
    OP_8E(0x8, 0x15202, 0x0, 0x9B64, 0xFA0, 0x0)
    SetChrChipByIndex(0x8, 0)
    SetChrSubChip(0x101, 23)

    ChrTalk(    #78
        0x101,
        "#451FAnelace?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        (
            "#4P#812FEstelle, you're awake! Thank Aidios...\x02\x03",

            "C'mon, grab your gear!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#451FR-Right!\x02\x03",

            "Hey, is that really gunfire, or...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "#4P#815FYeah! We're under attack by...\x01",
            "somebody! I dunno who!\x02\x03",

            "Kurt's trying to fight them off,\x01",
            "but we need to go help him!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E83")

    OP_1D(0x29)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(86600, 0, 40930, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrPos(0x101, 86600, 0, 40930, 180)
    SetChrFlags(0x8, 0x80)
    AddParty(0x9, 0xF7, 0xFF)
    Sleep(500)
    OP_A2(0x100C)
    OP_28(0x7F, 0x4, 0x2)
    OP_28(0x7F, 0x4, 0x8)
    OP_28(0x7F, 0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x9, 0xFE, 0x0)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_26B0 end

    def Function_11_2F23(): pass

    label("Function_11_2F23")

    EventBegin(0x0)
    OP_4A(0xA, 255)
    OP_44(0x9, 0x0)
    OP_44(0x8, 0x0)
    OP_44(0xB, 0x0)
    SetChrPos(0x101, 27210, 2000, 9020, 253)
    SetChrPos(0x10A, 28160, 2000, 8910, 262)
    SetChrPos(0xA, 18980, -300, 5950, 166)
    SetChrPos(0xB, 17150, -300, 5260, 170)
    SetChrPos(0x9, 19400, -550, 370, 0)
    SetChrPos(0xC, 20970, 0, 18840, 176)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x10A, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    TurnDirection(0xA, 0x9, 1000)
    TurnDirection(0xB, 0x9, 1000)

    def lambda_2FC8():

        label("loc_2FC8")

        TurnDirection(0xA, 0x9, 0)
        OP_48()
        Jump("loc_2FC8")

    QueueWorkItem2(0xA, 1, lambda_2FC8)

    def lambda_2FD9():

        label("loc_2FD9")

        TurnDirection(0xB, 0x9, 0)
        OP_48()
        Jump("loc_2FD9")

    QueueWorkItem2(0xB, 1, lambda_2FD9)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_9F(0x9, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)

    def lambda_3038():
        OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3038)
    OP_8E(0x9, 0x4BC8, 0xFFFFFDDA, 0x73A, 0x3E8, 0x0)
    Sleep(500)
    OP_8C(0x9, 180, 2000)
    Sleep(500)
    WaitChrThread(0x9, 0x1)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #82
        0x9,
        (
            "#6P#847FNngh... That should hold them off...\x01",
            "for a moment...\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0)
    SetChrChipByIndex(0x9, 10)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0x9, 0x0, 0x3, 0x4B0)

    ChrTalk(    #83
        0xA,
        "#6PAre you all right?!\x02",
    )

    CloseMessageWindow()

    def lambda_30F4():
        OP_8E(0xB, 0x4934, 0xFFFFFDDA, 0x898, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_30F4)
    Sleep(500)

    def lambda_3114():
        OP_8E(0xA, 0x4A06, 0xFFFFFED4, 0xEE2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3114)
    WaitChrThread(0xB, 0x1)
    OP_8C(0xB, 125, 500)

    ChrTalk(    #84
        0xB,
        "#5PH-He's not! Kurt, your arm...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x9,
        (
            "#2P#844FIt's...nothing. Just a scratch.\x02\x03",

            "It's far more important that we\x01",
            "put an end to this...intrusion.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_31D0():
        OP_6D(21710, 0, 8600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_31D0)

    def lambda_31E8():
        OP_67(0, 8000, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_31E8)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x10A, 0x80)

    def lambda_320A():
        OP_8E(0x101, 0x54CE, 0x0, 0x2198, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_320A)
    Sleep(200)

    def lambda_322A():
        OP_8E(0x10A, 0x5A8C, 0x0, 0x229C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_322A)
    WaitChrThread(0x101, 0x1)
    TurnDirection(0x101, 0x9, 1000)
    TurnDirection(0x10A, 0x9, 1000)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(200)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #86
        0x101,
        "#1020F#6PKurt?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10A,
        "#815F#6PKURT! Are you okay?! You're injured!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 1000)
    TurnDirection(0xA, 0x101, 1000)

    ChrTalk(    #88
        0xB,
        "#1PEstelle! Anelace!\x02",
    )

    CloseMessageWindow()

    def lambda_32FF():
        OP_6D(19720, -300, 3340, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_32FF)

    def lambda_3317():
        OP_8E(0x101, 0x4D08, 0xFFFFFED4, 0xD0C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3317)
    Sleep(200)

    def lambda_3337():
        OP_8E(0x10A, 0x51D6, 0xFFFFFED4, 0xC3A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_3337)
    TurnDirection(0xA, 0x9, 500)
    TurnDirection(0xB, 0x9, 500)
    WaitChrThread(0x10A, 0x1)
    WaitChrThread(0x10A, 0x2)
    TurnDirection(0x101, 0x9, 1000)
    TurnDirection(0x10A, 0x9, 1000)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 29)
    SetChrSubChip(0x9, 1)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #89
        0x9,
        (
            "#844FForgive me. I let my guard down...\x02\x03",

            "As you can see, the lodge is under\x01",
            "attack by a group of armed men.\x02\x03",

            "I need your help in driving them away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1005FR-Roger!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10A,
        (
            "#813F#6PBut, but...they...HURT you, Kurt...\x02\x03",

            "#815FWho the heck ARE these guys?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x9,
        (
            "#844FI'm not yet entirely certain, but I got\x01",
            "a fairly good look at their gear when\x01",
            "fighting a moment ago.\x02\x03",

            "Judging from its design, I would\x01",
            "guess they're jaegers.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #93
        0x101,
        (
            "#1004FJaegers... Hang on, you mean those\x01",
            "elite, crazy mercenaries I heard about\x01",
            "in Grancel?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x10A,
        "#1317F#6PB-B-But...why would they be HERE?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x9,
        (
            "#844FOutside of Liberl, the guild and\x01",
            "the jaegers are dire enemies.\x02\x03",

            "It is not out of the question that they\x01",
            "would dare to attack us here. Though it\x01",
            "would be oddly brazen, even for them.\x02\x03",

            "#843FGiven that, though. This could very well\x01",
            "be at the behest of the 'society.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1020FWHAT?! You me--\x02",
    )

    CloseMessageWindow()
    OP_22(0x134, 0x0, 0x64)
    OP_72(0x19, 0x20)
    OP_6F(0x19, 0)
    OP_70(0x19, 0x3C)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(40)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(40)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(40)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_37BB():
        OP_6D(21830, 0, 13880, 1200)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_37BB)

    def lambda_37D3():
        TurnDirection(0x101, 0xC, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37D3)

    def lambda_37E1():
        TurnDirection(0x10A, 0xC, 600)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_37E1)

    def lambda_37EF():
        TurnDirection(0xA, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_37EF)

    def lambda_37FD():
        TurnDirection(0xB, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_37FD)
    Sleep(800)
    SetChrChipByIndex(0xC, 17)
    OP_9F(0xC, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x80)

    def lambda_382A():
        OP_9F(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_382A)
    OP_96(0xC, 0x52D0, 0x0, 0x3A7A, 0x7D0, 0x1B58)
    OP_22(0xA4, 0x0, 0x64)
    SetChrChipByIndex(0xC, 16)
    Sleep(500)

    ChrTalk(    #97
        0x10A,
        "#1P#1317FGyah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1P#1005FSon of a...!\x02",
    )

    CloseMessageWindow()

    def lambda_3891():
        OP_6D(21130, 0, 9590, 800)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_3891)
    SetChrChipByIndex(0xC, 17)

    def lambda_38AE():
        OP_8E(0xC, 0x51B8, 0x0, 0x2774, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_38AE)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x10A, 0x1000)
    SetChrChipByIndex(0x101, 21)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x10A, 22)
    SetChrSubChip(0x10A, 0)

    def lambda_38E7():
        OP_8E(0x101, 0x512C, 0xFFFFFED4, 0x1D2E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38E7)
    Sleep(100)

    def lambda_3907():
        OP_8E(0x10A, 0x55DC, 0xFFFFFED4, 0x1D6A, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3907)
    Sleep(500)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    Battle(0x397, 0x0, 0x0, 0x0, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_3970"),
        (0, "loc_397D"),
        (SWITCH_DEFAULT, "loc_398A"),
    )


    label("loc_3970")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_398A")

    label("loc_397D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_398A")

    label("loc_398A")

    EventBegin(0x0)
    OP_72(0x19, 0x20)
    OP_72(0x19, 0x8)
    OP_6F(0x19, 60)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39B3")
    OP_28(0x7F, 0x1, 0x40)
    Jump("loc_3D3F")

    label("loc_39B3")

    OP_2B(0x7E, 0x3)
    OP_6D(21510, 0, 12500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_44(0x9, 0x0)
    OP_44(0x8, 0x0)
    OP_44(0xB, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrPos(0x101, 20540, 0, 9660, 0)
    SetChrChipByIndex(0x101, 14)
    SetChrPos(0x10A, 21750, 0, 9710, 0)
    SetChrChipByIndex(0x10A, 15)
    SetChrPos(0xC, 21300, 0, 14260, 170)
    SetChrPos(0xD, 21060, 0, 18750, 182)
    SetChrChipByIndex(0xC, 27)
    SetChrSubChip(0xC, 3)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #99
        0x101,
        (
            "#2P#1002F*pant*... *pant*...\x01",
            "We managed to win...somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10A,
        (
            "#815F#2PO-Okay, whoever you are!\x01",
            "DROP the weapon and surrender!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xC,
        (
            "#6PHeh heh...\x01",
            "You brats are better than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xC,
        "#6PStill not good enough, though.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x10A,
        "#814F#2PWha...?\x02",
    )

    CloseMessageWindow()

    def lambda_3B72():
        OP_6D(21490, 0, 14710, 1200)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_3B72)

    def lambda_3B8A():
        OP_67(0, 8000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3B8A)
    SetChrChipByIndex(0xD, 19)
    SetChrSubChip(0xD, 2)
    SetChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x80)
    OP_96(0xD, 0x4F1A, 0x0, 0x3B4C, 0x7D0, 0x1B58)
    SetChrChipByIndex(0xD, 18)
    SetChrSubChip(0xD, 0)
    OP_22(0xA4, 0x0, 0x64)
    OP_99(0xC, 0x3, 0x0, 0x708)
    SetChrChipByIndex(0xC, 16)
    SetChrChipByIndex(0xD, 28)
    SetChrFlags(0xD, 0x2)
    LoadEffect(0x0, "map\\\\mp004_00.eff")
    SetChrPos(0xE, 21290, 0, 11110, 13)

    def lambda_3C19():
        OP_99(0xFE, 0x0, 0x9, 0x5DC)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3C19)
    Sleep(800)
    PlayEffect(0x0, 0xFF, 0xD, 250, 900, -500, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    Sleep(300)

    def lambda_3C68():
        OP_6D(21360, 0, 11490, 1000)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_3C68)
    Sleep(1000)
    OP_22(0x7F, 0x0, 0x64)
    Sleep(500)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    OP_71(0xD, 0x4)
    Sleep(2000)

    ChrTalk(    #104
        0x10A,
        "#1317FGnaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#6P#1020FA smoke bomb?! *cough*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xD,
        "#5PTeehee...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xD,
        "#5PNighty night, little kittens.\x02",
    )

    CloseMessageWindow()
    OP_C4(0x0, 0x10)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    Sleep(1000)
    FadeToBright(0, 16777215)
    OP_0D()
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_28(0x7F, 0x1, 0x10)

    label("loc_3D3F")

    NewScene("ED6_DT21/C5504   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2F23 end

    def Function_12_3D49(): pass

    label("Function_12_3D49")

    EventBegin(0x1)
    OP_8C(0x0, 174, 500)
    OP_22(0x71, 0x0, 0x64)
    Sleep(1000)

    AnonymousTalk(    #108
        "\x07\x05The door is locked tight.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_90(0x0, 0x0, 0x0, 0x3E8, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_12_3D49 end

    SaveToFile()

Try(main)
