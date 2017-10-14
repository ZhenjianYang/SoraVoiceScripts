from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0101   ._SN',
        MapName             = 'Rolent',
        Location            = 'C0101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60030",
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
        'Miner Landan',                         # 9
        'Miner Trent',                          # 10
        'Miner Pierre',                         # 11
        'Miner Heinrich',                       # 12
        'Miner Bones',                          # 13
        'Mine Chief Gaton',                     # 14
        'Ridge',                                # 15
        'Crab Boss',                            # 16
        'Crab',                                 # 17
        'Crab',                                 # 18
        'Crab',                                 # 19
        'Crab',                                 # 20
        'Crab',                                 # 21
        'Crab',                                 # 22
        'Crab',                                 # 23
        'Crab',                                 # 24
        'Crab',                                 # 25
        'Crab',                                 # 26
        'Crab',                                 # 27
        'Crab',                                 # 28
        'Targeting Camera',                     # 29
        '',                                     # 30
        '',                                     # 31
        '',                                     # 32
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
        'ED6_DT29/CH12920 ._CH',             # 00
        'ED6_DT29/CH12921 ._CH',             # 01
        'ED6_DT09/CH10000 ._CH',             # 02
        'ED6_DT09/CH10001 ._CH',             # 03
        'ED6_DT07/CH01500 ._CH',             # 04
        'ED6_DT07/CH01530 ._CH',             # 05
        'ED6_DT07/CH00490 ._CH',             # 06
    )

    AddCharChipPat(
        'ED6_DT29/CH12920P._CP',             # 00
        'ED6_DT29/CH12921P._CP',             # 01
        'ED6_DT09/CH10000P._CP',             # 02
        'ED6_DT09/CH10001P._CP',             # 03
        'ED6_DT07/CH01500P._CP',             # 04
        'ED6_DT07/CH01530P._CP',             # 05
        'ED6_DT07/CH00490P._CP',             # 06
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x101,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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


    DeclMonster(
        X                   = 125180,
        Z                   = 0,
        Y                   = 20140,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 112970,
        Z                   = -210,
        Y                   = 81150,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 104360,
        Z                   = 0,
        Y                   = 53370,
        Unknown_0C          = 0,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x56,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 90600,
        Y                   = -1000,
        Z                   = 68100,
        Range               = 97100,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x10EB4,
        Unknown_18          = 0x0,
        Unknown_1C          = 34,
    )

    DeclEvent(
        X                   = 125000,
        Y                   = -1000,
        Z                   = 24700,
        Range               = 134000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x65F4,
        Unknown_18          = 0x0,
        Unknown_1C          = 17,
    )

    DeclEvent(
        X                   = 106480,
        Y                   = -1000,
        Z                   = 31780,
        Range               = 104940,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x5E60,
        Unknown_18          = 0x0,
        Unknown_1C          = 24,
    )

    DeclEvent(
        X                   = 98500,
        Y                   = -1000,
        Z                   = 3100,
        Range               = 99500,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x3BC4,
        Unknown_18          = 0x0,
        Unknown_1C          = 32,
    )


    DeclActor(
        TriggerX            = 54000,
        TriggerZ            = 500,
        TriggerY            = 58200,
        TriggerRange        = 600,
        ActorX              = 54000,
        ActorZ              = 500,
        ActorY              = 58200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 14000,
        TriggerZ            = 1000,
        TriggerY            = 31800,
        TriggerRange        = 1000,
        ActorX              = 14000,
        ActorZ              = 1000,
        ActorY              = 31800,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 45,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_49E",          # 00, 0
        "Function_1_653",          # 01, 1
        "Function_2_9CE",          # 02, 2
        "Function_3_B4B",          # 03, 3
        "Function_4_D48",          # 04, 4
        "Function_5_E9A",          # 05, 5
        "Function_6_10B7",         # 06, 6
        "Function_7_1376",         # 07, 7
        "Function_8_156D",         # 08, 8
        "Function_9_17D6",         # 09, 9
        "Function_10_24E6",        # 0A, 10
        "Function_11_4C4F",        # 0B, 11
        "Function_12_5D3F",        # 0C, 12
        "Function_13_5D53",        # 0D, 13
        "Function_14_5D80",        # 0E, 14
        "Function_15_5DAD",        # 0F, 15
        "Function_16_5DDA",        # 10, 16
        "Function_17_6B34",        # 11, 17
        "Function_18_6D0E",        # 12, 18
        "Function_19_7706",        # 13, 19
        "Function_20_7771",        # 14, 20
        "Function_21_77DC",        # 15, 21
        "Function_22_7847",        # 16, 22
        "Function_23_78C9",        # 17, 23
        "Function_24_795F",        # 18, 24
        "Function_25_8601",        # 19, 25
        "Function_26_862E",        # 1A, 26
        "Function_27_865B",        # 1B, 27
        "Function_28_8688",        # 1C, 28
        "Function_29_86B5",        # 1D, 29
        "Function_30_86D1",        # 1E, 30
        "Function_31_86ED",        # 1F, 31
        "Function_32_8709",        # 20, 32
        "Function_33_990B",        # 21, 33
        "Function_34_9E1E",        # 22, 34
        "Function_35_A3A2",        # 23, 35
        "Function_36_C1B1",        # 24, 36
        "Function_37_C237",        # 25, 37
        "Function_38_C2C4",        # 26, 38
        "Function_39_C315",        # 27, 39
        "Function_40_C34A",        # 28, 40
        "Function_41_C37F",        # 29, 41
        "Function_42_C3B4",        # 2A, 42
        "Function_43_C3E9",        # 2B, 43
        "Function_44_C40C",        # 2C, 44
        "Function_45_C484",        # 2D, 45
    )


    def Function_0_49E(): pass

    label("Function_0_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_507")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrPos(0xD, 24270, -200, 15450, 315)
    SetChrPos(0x9, 12850, 0, 12900, 140)
    SetChrPos(0xC, 10170, 0, 29510, 315)
    SetChrPos(0xA, 36510, 0, 25540, 270)
    SetChrPos(0xB, 36500, -130, 23470, 270)
    Jump("loc_652")

    label("loc_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_END)), "loc_652")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 0)), scpexpr(EXPR_END)), "loc_617")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 132100, 0, 74120, 225)
    SetChrPos(0x9, 132170, 0, 72480, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_END)), "loc_57C")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, 131940, 0, 69900, 315)
    SetChrPos(0xB, 130930, 0, 68610, 45)
    SetChrFlags(0x1D, 0x80)
    Jump("loc_5A8")

    label("loc_57C")

    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, 130610, 1000, 14190, 180)
    SetChrPos(0xB, 130610, 1000, 12770, 0)

    label("loc_5A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_END)), "loc_5C8")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 124780, 0, 74190, 180)
    Jump("loc_5DE")

    label("loc_5C8")

    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 96530, -70, 29250, 0)

    label("loc_5DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_END)), "loc_5FE")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 126540, 0, 75140, 180)
    Jump("loc_614")

    label("loc_5FE")

    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 86190, -500, 13450, 0)

    label("loc_614")

    Jump("loc_652")

    label("loc_617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 7)), scpexpr(EXPR_END)), "loc_637")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 51720, 0, 55230, 180)
    Jump("loc_652")

    label("loc_637")

    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 53910, 0, 53890, 0)

    label("loc_652")

    Return()

    # Function_0_49E end

    def Function_1_653(): pass

    label("Function_1_653")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_END)), "loc_675")
    OP_6F(0x0, 75)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_675")
    OP_65(0x0, 0x1)

    label("loc_675")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_814")
    OP_D2(0x26006E, 0x260073, 0x7)
    OP_D2(0x26006E, 0x260073, 0x8)
    OP_D2(0x26006E, 0x260073, 0x9)
    OP_D2(0x270110, 0x270120, 0xA)
    OP_D2(0x270111, 0x270121, 0xB)
    OP_D2(0x270130, 0x270140, 0xC)
    OP_D2(0x270131, 0x270141, 0xD)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_6DC"),
        (5, "loc_6F3"),
        (6, "loc_70A"),
        (7, "loc_721"),
        (SWITCH_DEFAULT, "loc_738"),
    )


    label("loc_6DC")

    OP_D2(0x701D0, 0x701DC, 0xE)
    OP_D2(0x701D1, 0x701DD, 0xF)
    Jump("loc_738")

    label("loc_6F3")

    OP_D2(0x70218, 0x70224, 0xE)
    OP_D2(0x70219, 0x70225, 0xF)
    Jump("loc_738")

    label("loc_70A")

    OP_D2(0x70230, 0x7023C, 0xE)
    OP_D2(0x70231, 0x7023D, 0xF)
    Jump("loc_738")

    label("loc_721")

    OP_D2(0x70248, 0x70254, 0xE)
    OP_D2(0x70249, 0x70255, 0xF)
    Jump("loc_738")

    label("loc_738")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_751"),
        (5, "loc_768"),
        (6, "loc_77F"),
        (7, "loc_796"),
        (SWITCH_DEFAULT, "loc_7AD"),
    )


    label("loc_751")

    OP_D2(0x701D0, 0x701DC, 0x10)
    OP_D2(0x701D1, 0x701DD, 0x11)
    Jump("loc_7AD")

    label("loc_768")

    OP_D2(0x70218, 0x70224, 0x10)
    OP_D2(0x70219, 0x70225, 0x11)
    Jump("loc_7AD")

    label("loc_77F")

    OP_D2(0x70230, 0x7023C, 0x10)
    OP_D2(0x70231, 0x7023D, 0x11)
    Jump("loc_7AD")

    label("loc_796")

    OP_D2(0x70248, 0x70254, 0x10)
    OP_D2(0x70249, 0x70255, 0x11)
    Jump("loc_7AD")

    label("loc_7AD")

    LoadEffect(0x0, "map\\\\mp002_00.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 95730, 0, 78730, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 1000)
    OP_D2(0x29039C, 0x2903A0, 0x12)
    OP_D2(0x29039D, 0x2903A1, 0x13)
    OP_D2(0x2903A2, 0x2903A3, 0x14)

    label("loc_814")

    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_71(0xF, 0x4)
    OP_71(0x10, 0x4)
    OP_71(0x11, 0x4)
    OP_71(0x12, 0x4)
    OP_71(0x13, 0x4)
    OP_71(0x14, 0x4)
    OP_71(0x15, 0x4)
    OP_71(0x16, 0x4)
    OP_71(0x17, 0x4)
    OP_71(0x18, 0x4)
    OP_71(0x19, 0x4)
    OP_71(0x1A, 0x4)
    OP_71(0x1B, 0x4)
    OP_71(0x1C, 0x4)
    OP_71(0x1D, 0x4)
    OP_71(0x1E, 0x4)
    OP_71(0x1F, 0x4)
    OP_71(0x20, 0x4)
    OP_71(0x21, 0x4)
    OP_71(0x22, 0x4)
    OP_71(0x23, 0x4)
    OP_71(0x24, 0x4)
    OP_71(0x25, 0x4)
    OP_71(0x26, 0x4)
    OP_71(0x27, 0x4)
    OP_71(0x28, 0x4)
    OP_71(0x29, 0x4)
    OP_71(0x2A, 0x4)
    OP_71(0x2B, 0x4)
    OP_71(0x2C, 0x4)
    OP_71(0x2D, 0x4)
    OP_71(0x2E, 0x4)
    OP_71(0x2F, 0x4)
    OP_71(0x30, 0x4)
    OP_71(0x31, 0x4)
    OP_71(0x32, 0x4)
    OP_79(0x4, 0x2)
    OP_79(0x5, 0x2)
    OP_79(0x6, 0x2)
    OP_79(0x7, 0x2)
    OP_79(0x8, 0x2)
    OP_79(0x9, 0x2)
    OP_79(0xA, 0x2)
    OP_79(0xB, 0x2)
    OP_79(0xC, 0x2)
    OP_79(0xD, 0x2)
    OP_79(0xE, 0x2)
    OP_79(0xF, 0x2)
    OP_79(0x10, 0x2)
    OP_79(0x11, 0x2)
    OP_79(0x12, 0x2)
    OP_79(0x13, 0x2)
    OP_79(0x14, 0x2)
    OP_79(0x15, 0x2)
    OP_79(0x16, 0x2)
    OP_79(0x17, 0x2)
    OP_79(0x18, 0x2)
    OP_79(0x19, 0x2)
    OP_79(0x1A, 0x2)
    OP_79(0x1B, 0x2)
    OP_79(0x1C, 0x2)
    OP_79(0x1D, 0x2)
    OP_79(0x1E, 0x2)
    OP_79(0x1F, 0x2)
    OP_79(0x20, 0x2)
    OP_79(0x21, 0x2)
    OP_79(0x22, 0x2)
    OP_79(0x23, 0x2)
    OP_79(0x24, 0x2)
    OP_79(0x25, 0x2)
    OP_79(0x26, 0x2)
    OP_79(0x27, 0x2)
    OP_79(0x28, 0x2)
    OP_79(0x29, 0x2)
    OP_79(0x2A, 0x2)
    OP_79(0x2B, 0x2)
    OP_79(0x2C, 0x2)
    OP_79(0x2D, 0x2)
    OP_79(0x2E, 0x2)
    OP_79(0x2F, 0x2)
    OP_79(0x30, 0x2)
    OP_79(0x31, 0x2)
    OP_79(0x32, 0x2)
    OP_7B()
    OP_77(0x96, 0x96, 0x96, 0x0, 0x0)
    OP_D7(0x1, 20000, 0)
    Return()

    # Function_1_653 end

    def Function_2_9CE(): pass

    label("Function_2_9CE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F3")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_B35")

    label("loc_9F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0C")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_B35")

    label("loc_A0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A25")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_B35")

    label("loc_A25")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A3E")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_B35")

    label("loc_A3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A57")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_B35")

    label("loc_A57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A70")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_B35")

    label("loc_A70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A89")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_B35")

    label("loc_A89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA2")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_B35")

    label("loc_AA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ABB")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_B35")

    label("loc_ABB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD4")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_B35")

    label("loc_AD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AED")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_B35")

    label("loc_AED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B06")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_B35")

    label("loc_B06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B1F")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_B35")

    label("loc_B1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B35")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_B35")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B4A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_B35")

    label("loc_B4A")

    Return()

    # Function_2_9CE end

    def Function_3_B4B(): pass

    label("Function_3_B4B")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 0)), scpexpr(EXPR_END)), "loc_CA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB8")

    ChrTalk(    #0
        0xFE,
        "I'm glad everyone's safe!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I hope you find that other\x01",
            "bracer soon, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C9D")

    label("loc_BB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C30")

    ChrTalk(    #2
        0xFE,
        (
            "I'm sure more of my miner\x01",
            "buddies are hiding up in the\x01",
            "tunnel somewhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Please, find them!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C9D")

    label("loc_C30")


    ChrTalk(    #4
        0xFE,
        (
            "Till then, I'm gonna stay\x01",
            "back here with Trent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "So, you know, good luck\x01",
            "finding the chief and all!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9D")

    Jump("loc_D44")

    label("loc_CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 7)), scpexpr(EXPR_END)), "loc_D3F")

    ChrTalk(    #6
        0xFE,
        (
            "Sorry, but could you check\x01",
            "and see what's going on inside\x01",
            "the tunnel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "The boss is somewhere in there,\x01",
            "waiting to be saved. I just know it!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D44")

    label("loc_D3F")

    Call(0, 9)
    Return()

    label("loc_D44")

    TalkEnd(0x8)
    Return()

    # Function_3_B4B end

    def Function_4_D48(): pass

    label("Function_4_D48")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_E50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DE0")

    ChrTalk(    #8
        0xFE,
        "Hey, bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Work started just as I was\x01",
            "finally about to go back and\x01",
            "eat my lunch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "So hungry... Can't...move...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_E4D")

    label("loc_DE0")


    ChrTalk(    #11
        0xFE,
        (
            "Work started just as I was\x01",
            "finally about to go back and\x01",
            "eat my lunch!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "So hungry... Can't...move...\x02",
    )

    CloseMessageWindow()

    label("loc_E4D")

    Jump("loc_E96")

    label("loc_E50")


    ChrTalk(    #13
        0xFE,
        (
            "H-Hurry up and find everyone!\x01",
            "I want out of here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "*shudder*\x02",
    )

    CloseMessageWindow()

    label("loc_E96")

    TalkEnd(0x9)
    Return()

    # Function_4_D48 end

    def Function_5_E9A(): pass

    label("Function_5_E9A")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_105F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA3")

    ChrTalk(    #15
        0xFE,
        (
            "Hey there, bracers! Thanks for\x01",
            "helping us out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "I get the feeling this whole thing\x01",
            "was some kind of Divine Providence\x01",
            "from Aidios Herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I mean, this accident was\x01",
            "something else. What do you\x01",
            "think She was trying to tell us? \x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_105C")

    label("loc_FA3")


    ChrTalk(    #18
        0xFE,
        (
            "I'm sure this whole mess was some\x01",
            "kind of message from the Goddess!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "I'm going to comb through the Testaments\x01",
            "again and see if I can figure out exactly what\x01",
            "She's telling us. \x02",
        )
    )

    CloseMessageWindow()

    label("loc_105C")

    Jump("loc_10B3")

    label("loc_105F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_END)), "loc_10AE")

    ChrTalk(    #20
        0xFE,
        "Sweet Aidios, please save Your children!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "*mutter* *mumble*\x02",
    )

    CloseMessageWindow()
    Jump("loc_10B3")

    label("loc_10AE")

    Call(0, 18)
    Return()

    label("loc_10B3")

    TalkEnd(0xA)
    Return()

    # Function_5_E9A end

    def Function_6_10B7(): pass

    label("Function_6_10B7")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_12EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1231")

    ChrTalk(    #22
        0xFE,
        (
            "Pierre's going on and on about the\x01",
            "Goddess being responsible for all this,\x01",
            "as usual. Can't say I'm surprised, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "...makes you wonder if he knows who\x01",
            "really saved us. Hmph!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "If something like this happens again,\x01",
            "can you do me a favor and NOT save\x01",
            "him?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "That nitwit won't ever figure out a damn\x01",
            "thing unless we shake him up a little!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_12EB")

    label("loc_1231")


    ChrTalk(    #26
        0xFE,
        (
            "Pierre's going on and on about the\x01",
            "Goddess being responsible for all this,\x01",
            "as usual. Can't say I'm surprised, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "...makes you wonder if he knows who\x01",
            "really saved us. Hmph!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EB")

    Jump("loc_1372")

    label("loc_12EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_END)), "loc_136D")

    ChrTalk(    #28
        0xFE,
        (
            "Pierre's praying again,\x01",
            "I see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "*sigh* I'm so sick of it that\x01",
            "I can't even be bothered to\x01",
            "complain anymore!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1372")

    label("loc_136D")

    Call(0, 18)
    Return()

    label("loc_1372")

    TalkEnd(0xB)
    Return()

    # Function_6_10B7 end

    def Function_7_1376(): pass

    label("Function_7_1376")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_153C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14BC")

    ChrTalk(    #30
        0xFE,
        (
            "Trent was trying to skip\x01",
            "work again, so the boss is\x01",
            "real ticked off at him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "That's what he gets for only\x01",
            "trying to save his own ass\x01",
            "during the accident!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "Man, though... Don't think\x01",
            "I've ever seen someone run\x01",
            "that fast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "Maybe he could try moving\x01",
            "like that when he's working\x01",
            "for once.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1539")

    label("loc_14BC")


    ChrTalk(    #34
        0xFE,
        (
            "Man, Trent really booked it\x01",
            "during the accident...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Maybe he could try moving\x01",
            "like that when he's working\x01",
            "for once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1539")

    Jump("loc_1569")

    label("loc_153C")


    ChrTalk(    #36
        0xFE,
        (
            "*pant* *pant*\x01",
            "Th-That sure was scary...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1569")

    TalkEnd(0xC)
    Return()

    # Function_7_1376 end

    def Function_8_156D(): pass

    label("Function_8_156D")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1702")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1673")

    ChrTalk(    #37
        0xD,
        "Well, if it isn't the bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xD,
        (
            "Thanks to you kids, we're\x01",
            "already hard at work again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xD,
        (
            "The elevator's still a busted\x01",
            "piece of junk, but there's no\x01",
            "use whining about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xD,
        (
            "We're just trying to mine\x01",
            "wherever we can for now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_16FF")

    label("loc_1673")


    ChrTalk(    #41
        0xD,
        (
            "The elevator's still a busted\x01",
            "piece of junk, but there's no\x01",
            "use whining about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xD,
        (
            "Wish we had something like\x01",
            "that thing you used.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16FF")

    Jump("loc_17D2")

    label("loc_1702")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1789")

    ChrTalk(    #43
        0xD,
        (
            "That bracer might still be\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xD,
        (
            "He was doing just about all\x01",
            "he could to give us enough\x01",
            "time to escape.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_17D2")

    label("loc_1789")


    ChrTalk(    #45
        0xD,
        (
            "That bracer might still be\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xD,
        "Sure hope he's safe...\x02",
    )

    CloseMessageWindow()

    label("loc_17D2")

    TalkEnd(0xD)
    Return()

    # Function_8_156D end

    def Function_9_17D6(): pass

    label("Function_9_17D6")

    EventBegin(0x0)
    Fade(500)
    OP_6D(54410, 60, 52800, 0)
    OP_67(0, 7910, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 54510, 150, 52380, 0)
    SetChrPos(0x102, 53460, 160, 52670, 0)
    SetChrPos(0xF8, 54510, 150, 51180, 0)
    SetChrPos(0xF9, 53460, 160, 51470, 0)
    OP_4A(0x8, 255)
    OP_0D()

    ChrTalk(    #47
        0x8,
        "Oh, bloody hell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "Gehenna just...swallow me right now.\x01",
            "It'll be quicker.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#1015F#4PMr. Landan? What's wrong?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #50
        0x8,
        (
            "Oh! Estelle!\x01",
            "I was wondering if you'd come by.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        "I think we still owe you from way back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#1016F#4PHahaha! Man, memories...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        (
            "#1040F#3PThat's right, one of our first real bracer\x01",
            "missions was carrying the septium crystal\x01",
            "away after that cave-in.\x02\x03",

            "#1035FIt is a nice memory, but we don't\x01",
            "really have time to talk about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1004F#4PAh, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x8,
        (
            "Yeah, we have a problem.\x01",
            "The elevator isn't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x8,
        (
            "The boss 'n everyone are stuck\x01",
            "down there in the mines.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B30")

    ChrTalk(    #57
        0x103,
        (
            "#022FThey were doing some work\x01",
            "in the tunnels, correct?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC4")

    label("loc_1B30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B7E")

    ChrTalk(    #58
        0x108,
        (
            "#072FWe heard they were doing\x01",
            "some work in the tunnels.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BC4")

    label("loc_1B7E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BC4")

    ChrTalk(    #59
        0x106,
        (
            "#050FRight, we heard they were\x01",
            "doin' some digging.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC4")


    ChrTalk(    #60
        0x8,
        (
            "That's right. We're all working on shoring\x01",
            "the tunnels up after the cave-in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x8,
        (
            "We got the framework back up, but we still\x01",
            "need to take care of our 'rat problem.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1002F#4PYou mean the holes that opened\x01",
            "up in the cave-in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#1042F#3PYes, the ones that opened up into monster\x01",
            "nests when we were here last.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        "Exactly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "The boss dynamited them after you\x01",
            "left to fill 'em in quick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "Problem is, they're still dangerous if\x01",
            "they lead to monster nests, especially\x01",
            "digging ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "We talked it over and decided we\x01",
            "needed to seal them up proper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#1042F#3PNow I understand.\x02\x03",

            "That's why Ridge was asked to guard you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x101,
        (
            "#1015F#4PAnd then, right in the middle of all that...\x01",
            "kaboom, all your orbal gear stopped working.\x02\x03",

            "#1003FI hope everyone's okay down there.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F64")

    ChrTalk(    #70
        0x106,
        (
            "#057FEven if they are now, they won't\x01",
            "be for long. This is bad.\x02\x03",

            "We need to get down there somehow\x01",
            "and help them out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_206E")

    label("loc_1F64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FE1")

    ChrTalk(    #71
        0x108,
        (
            "#072FIf they are trapped down there,\x01",
            "they are in danger.\x02\x03",

            "We should find a way down\x01",
            "as soon as we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_206E")

    label("loc_1FE1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_206E")

    ChrTalk(    #72
        0x103,
        (
            "#022FIf they've no way out of the mine...\x01",
            "they may not be for long.\x02\x03",

            "We desperately need to get\x01",
            "down there and help them!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206E")


    ChrTalk(    #73
        0x8,
        (
            "Well, don't get me wrong, I'd love for you\x01",
            "to do that, but we got one little problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "There's no way to actually\x01",
            "get down there!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "This elevator shaft is the only way down\x01",
            "and that elevator ain't going anywhere.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0x101,
        (
            "#1019F#4POh. Right. Little problem. Gehenna\x01",
            "does sound nice right about now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        (
            "#1043F#3POf course.\x01",
            "It IS driven by orbments.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_222F")

    ChrTalk(    #78
        0x107,
        "#064FU-Umm... There's no other way down?\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A4")

    label("loc_222F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2270")

    ChrTalk(    #79
        0x103,
        "#023FIs there literally no other way down?\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A4")

    label("loc_2270")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22A4")

    ChrTalk(    #80
        0x108,
        "#072FThere is no other way down?\x02",
    )

    CloseMessageWindow()

    label("loc_22A4")


    ChrTalk(    #81
        0x8,
        (
            "Of course not!\x01",
            "We'd have used it to get the boss and\x01",
            "everyone out by now otherwise.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2329")

    ChrTalk(    #82
        0x107,
        "#562FOh, um, right...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2376")

    label("loc_2329")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2353")

    ChrTalk(    #83
        0x103,
        "#025FAh, of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2376")

    label("loc_2353")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2376")

    ChrTalk(    #84
        0x108,
        "#073FAh, right.\x02",
    )

    CloseMessageWindow()

    label("loc_2376")


    ChrTalk(    #85
        0x101,
        (
            "#1002F#4PBut, seriously, we can't just give\x01",
            "up on them!\x02\x03",

            "Everyone's waiting!\x01",
            "We have to do something for them!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x102,
        "#1043F#3PYes, but the question is, what?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x8,
        (
            "I know we don't have much to go\x01",
            "on, but if you have any ideas,\x01",
            "could you give them a shot?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        (
            "I'm sure everyone's waiting\x01",
            "to be rescued.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0xCCCE, 0x0, 0xD7D2, 0x7D0, 0x0)
    OP_8C(0x8, 180, 400)
    OP_4B(0x8, 255)
    OP_65(0x0, 0x1)
    ClearChrFlags(0x8, 0x10)
    OP_A2(0x2087)
    OP_28(0xBF, 0x4, 0x2)
    OP_28(0xBF, 0x4, 0x8)
    OP_28(0xBF, 0x1, 0x1)
    EventEnd(0x0)
    Return()

    # Function_9_17D6 end

    def Function_10_24E6(): pass

    label("Function_10_24E6")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #89
        "\x07\x05There is no response to the button being pressed.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(500)
    OP_6D(54080, 0, 55500, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2601")
    OP_D2(0x70065, 0x7006D, 0x7)
    SetChrPos(0x101, 54510, 0, 54700, 0)
    SetChrPos(0x107, 53490, 0, 54670, 0)
    SetChrPos(0x102, 54620, 0, 53520, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25ED")
    SetChrPos(0xF9, 53390, 0, 53520, 0)
    Jump("loc_25FE")

    label("loc_25ED")

    SetChrPos(0xF8, 53390, 0, 53520, 0)

    label("loc_25FE")

    Jump("loc_2645")

    label("loc_2601")

    SetChrPos(0x101, 54510, 0, 54700, 0)
    SetChrPos(0x102, 53490, 0, 54670, 0)
    SetChrPos(0xF8, 54620, 0, 53520, 0)
    SetChrPos(0xF9, 53390, 0, 53520, 0)

    label("loc_2645")

    OP_0D()

    ChrTalk(    #90
        0x101,
        "#1026F#4PReally not working... Darn it!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26E4")

    ChrTalk(    #91
        0x103,
        (
            "#022FThe control key has been inserted, too.\x02\x03",

            "It's purely down to the shutdown\x01",
            "phenomenon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27EE")

    label("loc_26E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2750")

    ChrTalk(    #92
        0x106,
        (
            "#050FLooks like the control key's in, too.\x02\x03",

            "Gotta be due to the orbments not working.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27EE")

    label("loc_2750")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27EE")

    ChrTalk(    #93
        0x108,
        (
            "#072FIt appears the control key for\x01",
            "the lift has been inserted.\x02\x03",

            "The only reason it wouldn't function is\x01",
            "due to the shutdown phenomenon...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3D93")

    ChrTalk(    #94
        0x107,
        "#062F#6PHmm...\x02",
    )

    CloseMessageWindow()

    def lambda_2816():

        label("loc_2816")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_2816")

    QueueWorkItem2(0x101, 1, lambda_2816)
    Sleep(500)

    ChrTalk(    #95
        0x101,
        (
            "#1002F#4PTita? Please tell me you've had\x01",
            "a brainwave or something.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #96
        0x107,
        (
            "#060F#6POh, um...maybe.\x01",
            "I was just thinking.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x8, 400)

    ChrTalk(    #97
        0x107,
        (
            "#060F#2PExcuse me!\x01",
            "Is this elevator an internal drive model?\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)

    def lambda_28FA():

        label("loc_28FA")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_28FA")

    QueueWorkItem2(0x8, 1, lambda_28FA)
    Sleep(400)

    ChrTalk(    #98
        0x8,
        "Er...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        "Uh, yeah, it should be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x107,
        "#064F#2PThought so!\x02",
    )

    CloseMessageWindow()

    def lambda_2951():
        OP_6D(54090, 50, 56090, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2951)

    def lambda_2969():
        OP_6C(31000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2969)
    OP_8E(0x107, 0xD23C, 0x32, 0xE150, 0x7D0, 0x0)
    OP_8C(0x107, 0, 400)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #101
        0x107,
        (
            "#062F#6POkay, then.\x01",
            "If the control key's put in here...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x107, 7)
    OP_0D()

    ChrTalk(    #102
        0x107,
        (
            "#062F#6PThen the drive orbment must\x01",
            "be around...here?\x02\x03",

            "It should be if it's been built\x01",
            "according to standard plan.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AFB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ABA")
    OP_62(0xF9, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2AF8")

    label("loc_2ABA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE1")
    OP_62(0xF9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2AF8")

    label("loc_2AE1")

    OP_62(0xF9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2AF8")

    Jump("loc_2B60")

    label("loc_2AFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B22")
    OP_62(0xF8, 0x0, 2300, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2B60")

    label("loc_2B22")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B49")
    OP_62(0xF8, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Jump("loc_2B60")

    label("loc_2B49")

    OP_62(0xF8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)

    label("loc_2B60")

    Sleep(1000)

    ChrTalk(    #103
        0x101,
        "#1016F#4PUh, Tita.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2BAD")

    ChrTalk(    #104
        0x106,
        "#551FAnd off she goes again.\x02",
    )

    CloseMessageWindow()

    label("loc_2BAD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C17")

    ChrTalk(    #105
        0x108,
        (
            "#071FHaha! She certainly is the professor's\x01",
            "granddaughter, the way she loves machines.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C17")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C5E")

    ChrTalk(    #106
        0x103,
        (
            "#021FWell, well! She's so dedicated.\x01",
            "It's adorable.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C5E")


    ChrTalk(    #107
        0x8,
        (
            "#6PThis girl is, uh, better with machines\x01",
            "than I would've guessed...\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()
    OP_8C(0x107, 180, 400)

    ChrTalk(    #108
        0x107,
        (
            "#060F#6PYeah... Okay, I think I can do\x01",
            "something with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1011F#4PDo something? You mean...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D5F")

    ChrTalk(    #110
        0x103,
        "#023FYou can get the elevator moving?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DDA")

    label("loc_2D5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D9A")

    ChrTalk(    #111
        0x106,
        "#052FYou can move this hunk of junk?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DDA")

    label("loc_2D9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DDA")

    ChrTalk(    #112
        0x108,
        (
            "#073FYou can get the elevator\x01",
            "working, Tita?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DDA")


    ChrTalk(    #113
        0x107,
        (
            "#060F#6PI think so, yeah.\x02\x03",

            "If we use a Zero Field Generator,\x01",
            "it SHOULD work. I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#1004F#4POur zero thingies will work here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x107,
        (
            "#560F#6PThey should, since the drive mechanism\x01",
            "is right here on the elevator. We just need\x01",
            "to get a field generator really close to it.\x02\x03",

            "If it reaches, I think we can get the elevator\x01",
            "working, even if nothing else does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x102,
        (
            "#1044FI see. It sounds like the\x01",
            "best plan we have.\x02\x03",

            "#1040FGive it a shot, Tita.\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_40(0x151, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FBD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2FBD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FD5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2FD5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FED")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_2FED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3005")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_3005")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_301D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_301D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3035")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_3035")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3073")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_305B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_305B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3073")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_3073")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30B1")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3099")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_3099")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30B1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_30B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30EF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30D7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_30D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30EF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_30EF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_312D")

    ChrTalk(    #117
        0x107,
        "#560F#6POkay! Give me a sec.\x02",
    )

    CloseMessageWindow()
    Jump("loc_36A9")

    label("loc_312D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3229")

    ChrTalk(    #118
        0x101,
        (
            "#1006F#4PFirst off, you'll need a\x01",
            "generator thingy.\x02\x03",

            "Here, you can use mine.\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #119
        "\x07\x00Estelle handed Tita her #337i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #120
        0x107,
        (
            "#560F#6PThanks, Estelle!\x02\x03",

            "Okay! Here we go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A9")

    label("loc_3229")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3346")

    ChrTalk(    #121
        0x107,
        "#560F#6POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x101,
        (
            "#1015F#4PWait, first off, you'll need\x01",
            "a generator thingy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x102,
        "#1040FHere, Tita. You can use mine.\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #124
        "\x07\x00Joshua handed over his #337i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #125
        0x107,
        (
            "#560F#6POh, thanks, Joshua!\x02\x03",

            "Okay! Here we go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A9")

    label("loc_3346")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_346C")

    ChrTalk(    #126
        0x107,
        "#560F#6POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        (
            "#1015F#4PWait, first off, you'll need\x01",
            "a generator thingy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x103,
        "#020FYou can use mine, honey.\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #129
        "\x07\x00Scherazard handed over her #337i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #130
        0x107,
        (
            "#560F#6POh, thanks, Schera.\x02\x03",

            "Okay! Here we go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A9")

    label("loc_346C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3591")

    ChrTalk(    #131
        0x107,
        "#560F#6POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1015F#4PWait, first off, you'll need\x01",
            "a generator thingy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x106,
        "#051FYou can use mine, shortstuff.\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #134
        "\x07\x00Agate handed over his #337i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #135
        0x107,
        (
            "#560F#6PUm, thanks, Agate!\x02\x03",

            "Okay! Here we go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36A9")

    label("loc_3591")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36A9")

    ChrTalk(    #136
        0x107,
        "#560F#6POkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x101,
        (
            "#1015F#4PWait, first off, you'll need\x01",
            "a generator thingy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x108,
        "#070FYou may use mine, Tita.\x02",
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #139
        "\x07\x00Zin handed over his #337i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #140
        0x107,
        (
            "#560F#6POh, thanks, Zin.\x02\x03",

            "Okay! Here we go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36A9")

    WaitChrThread(0x101, 0x2)
    OP_8C(0x107, 0, 400)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #141
        (
            "\x07\x05Tita attached the Zero Field Generator to the\x01",
            "elevator control stand.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(400)
    LoadEffect(0x1, "map\\\\mp007_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 54000, 800, 58200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x90, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #142
        0x8,
        "WHAT in tarnation!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1020F#4PWhoa...\x02\x03",

            "This light...!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3811")

    ChrTalk(    #144
        0x103,
        "#023FJust like what a Gospel emits!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3889")

    label("loc_3811")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3853")

    ChrTalk(    #145
        0x106,
        "#052FIt's just like the friggin' Gospels...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3889")

    label("loc_3853")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3889")

    ChrTalk(    #146
        0x108,
        "#072FJust the same as the Gospels.\x02",
    )

    CloseMessageWindow()

    label("loc_3889")


    ChrTalk(    #147
        0x102,
        (
            "#1042FThe generator is trying to negate\x01",
            "the orbal suppression effect.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x107,
        "#062F#6PCome on...\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x2)
    OP_23(0x90)
    Sleep(500)

    ChrTalk(    #149
        0x8,
        "It stopped...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x107,
        (
            "#561F#6PPhew!\x02\x03",

            "Okay, I think it worked.\x01",
            "We just need to see...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x5)
    OP_73(0x1)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39BD")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_39FB")

    label("loc_39BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39E4")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_39FB")

    label("loc_39E4")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_39FB")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A27")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3A65")

    label("loc_3A27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A4E")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3A65")

    label("loc_3A4E")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3A65")

    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #151
        0x107,
        "#065F#6PWaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        "#1004F#4PIt's moving!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x102,
        (
            "#1042FLooks like the elevator has power again.\x02\x03",

            "Let's get on.\x01",
            "If we're going, this is our chance.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B42")

    ChrTalk(    #154
        0x103,
        "#525FNicely done, Tita. ㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BAB")

    label("loc_3B42")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3B8C")

    ChrTalk(    #155
        0x106,
        "#051FHeh. You've saved our bacon again, shortstuff.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BAB")

    label("loc_3B8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BAB")

    ChrTalk(    #156
        0x108,
        "#072FRight!\x02",
    )

    CloseMessageWindow()

    label("loc_3BAB")


    def lambda_3BB1():
        OP_6D(54080, 50, 56970, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BB1)

    def lambda_3BC9():
        OP_8E(0xFE, 0xD4EE, 0x0, 0xE164, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3BC9)
    Sleep(100)

    def lambda_3BE9():
        OP_8E(0xFE, 0xD55C, 0x0, 0xDCC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3BE9)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C27")
    OP_8E(0xF9, 0xD08E, 0x0, 0xDCC8, 0x1388, 0x0)
    Jump("loc_3C3B")

    label("loc_3C27")

    OP_8E(0xF8, 0xD08E, 0x0, 0xDCC8, 0x1388, 0x0)

    label("loc_3C3B")


    ChrTalk(    #157 op#A
        0x8,
        "#2AI'll come too!\x02",
    )

    CloseMessageWindow()

    def lambda_3C58():

        label("loc_3C58")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3C58")

    QueueWorkItem2(0x102, 1, lambda_3C58)
    Sleep(100)

    def lambda_3C6E():

        label("loc_3C6E")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3C6E")

    QueueWorkItem2(0x101, 1, lambda_3C6E)
    Sleep(100)

    def lambda_3C84():

        label("loc_3C84")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3C84")

    QueueWorkItem2(0xF8, 1, lambda_3C84)

    def lambda_3C95():

        label("loc_3C95")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_3C95")

    QueueWorkItem2(0xF9, 1, lambda_3C95)

    ChrTalk(    #158 op#A
        0x102,
        "#1046F#2AHurry, then!\x02",
    )

    CloseMessageWindow()
    SetChrBattleFlags(0x8, 0x20)

    def lambda_3CC6():
        OP_8E(0xFE, 0xD25A, 0x32, 0xD840, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3CC6)

    def lambda_3CE1():
        OP_8F(0xFE, 0xD55C, 0x0, 0xDDF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3CE1)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D26")

    def lambda_3D0E():
        OP_8F(0xFE, 0xD08E, 0x0, 0xDDF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_3D0E)
    Jump("loc_3D41")

    label("loc_3D26")


    def lambda_3D2C():
        OP_8F(0xFE, 0xD08E, 0x0, 0xDDF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_3D2C)

    label("loc_3D41")

    WaitChrThread(0x8, 0x1)
    OP_8E(0x8, 0xD25A, 0x0, 0xDC28, 0x1388, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_8C(0x107, 0, 800)

    ChrTalk(    #159
        0x107,
        "#062F#6POkay, here we go!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C4A")

    label("loc_3D93")


    ChrTalk(    #160
        0x102,
        "#1043F#3PHmm...\x02",
    )

    CloseMessageWindow()

    def lambda_3DAE():

        label("loc_3DAE")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_3DAE")

    QueueWorkItem2(0x101, 1, lambda_3DAE)
    Sleep(500)

    ChrTalk(    #161
        0x101,
        "#1002F#4PJoshua? What is it?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #162
        0x102,
        (
            "#1040F#3PJust a sec...\x02\x03",

            "I think I have an idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        "#1011F#4PAn idea? About the elevator?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)

    ChrTalk(    #164
        0x102,
        (
            "#1040F#4PMr. Landan, is this elevator\x01",
            "internally driven?\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0x8, 255)

    def lambda_3E96():

        label("loc_3E96")

        TurnDirection(0xFE, 0x102, 400)
        OP_48()
        Jump("loc_3E96")

    QueueWorkItem2(0x8, 1, lambda_3E96)
    Sleep(400)

    ChrTalk(    #165
        0x8,
        "#1PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x8,
        "#1PUh, yeah, it should be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x102,
        "#1035F#4PAll right, good.\x02",
    )

    CloseMessageWindow()

    def lambda_3EF8():
        OP_6D(54090, 50, 56090, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3EF8)

    def lambda_3F10():
        OP_6C(31000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3F10)
    OP_8E(0x102, 0xD23C, 0x32, 0xE150, 0x7D0, 0x0)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #168
        0x102,
        (
            "#1043F#6PThe control key's been inserted here...\x02\x03",

            "So...the drive orbment should be\x01",
            "almost directly below it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3FDB")

    ChrTalk(    #169
        0x106,
        "#052FYou got something in mind?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4048")

    label("loc_3FDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_401E")

    ChrTalk(    #170
        0x103,
        (
            "#027FOh? Hatching a plot,\x01",
            "my former student?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4048")

    label("loc_401E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4048")

    ChrTalk(    #171
        0x108,
        "#073FYou have an idea?\x02",
    )

    CloseMessageWindow()

    label("loc_4048")

    OP_8C(0x102, 180, 400)
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "OP_40(0x151, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4071")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_4071")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4089")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_4089")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40A1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_40A1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40B9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_40B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40F7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40DF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_40DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_40F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4135")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_411D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_411D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4135")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_4135")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4173")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_415B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_415B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4173")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_4173")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x1, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4226")

    ChrTalk(    #172
        0x102,
        (
            "#1043F#6PI'm not sure it will work,\x01",
            "but it's worth trying.\x02\x03",

            "I think if we use a Zero Field Generator\x01",
            "right here, we can get the elevator working.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_456E")

    label("loc_4226")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_D5(0x0, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4356")

    ChrTalk(    #173
        0x102,
        (
            "#1043F#6PI'm not sure it will work,\x01",
            "but it's worth trying.\x02\x03",

            "#1040FEstelle. Can you lend me your\x01",
            "Zero Field Generator?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1011F#4PMy generator?\x02\x03",

            "#1015FUh, okay, but what...?\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #175
        "\x07\x00Estelle handed Joshua her #337i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_456E")

    label("loc_4356")


    ChrTalk(    #176
        0x102,
        (
            "#1040F#6PI'm not sure it will work,\x01",
            "but it's worth trying.\x02\x03",

            "#1040FCould I borrow someone's Zero Field Generator?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4424")

    ChrTalk(    #177
        0x103,
        (
            "#020FAhhhh, I see.\x01",
            "Here, Joshua, take mine.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44F0")

    label("loc_4424")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4493")

    ChrTalk(    #178
        0x106,
        (
            "#051FSure, take mine.\x02\x03",

            "Think I see where you're\x01",
            "goin' with this...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44F0")

    label("loc_4493")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44F0")

    ChrTalk(    #179
        0x108,
        (
            "#070FAhh, of course. A good idea.\x02\x03",

            "Here, take mine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44F0")

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #180
        "\x07\x00Joshua took the #337i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #181
        0x102,
        "#1040F#6PI'll be borrowing this for a minute.\x02",
    )

    CloseMessageWindow()

    label("loc_456E")


    ChrTalk(    #182
        0x101,
        (
            "#1002F#4PWhat are you planning on\x01",
            "doing with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x102,
        (
            "#1040F#6PGive me just a second\x01",
            "and you'll see.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #184
        (
            "\x07\x05Joshua placed the Zero Field Generator onto the\x01",
            "control stand.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(400)
    LoadEffect(0x1, "map\\\\mp007_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 54000, 800, 58200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x90, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #185
        0x8,
        "WHAT in tarnation!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#1020F#4PWhoa...\x02\x03",

            "This light...!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4736")

    ChrTalk(    #187
        0x103,
        "#023FJust like what a Gospel emits!\x02",
    )

    CloseMessageWindow()
    Jump("loc_47AE")

    label("loc_4736")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4778")

    ChrTalk(    #188
        0x106,
        "#052FIt's just like the friggin' Gospels...\x02",
    )

    CloseMessageWindow()
    Jump("loc_47AE")

    label("loc_4778")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_47AE")

    ChrTalk(    #189
        0x108,
        "#072FJust the same as the Gospels.\x02",
    )

    CloseMessageWindow()

    label("loc_47AE")


    ChrTalk(    #190
        0x102,
        (
            "#1042F#6PDon't worry... I think this is the result of the\x01",
            "orbal fields interfering with one another.\x02\x03",

            "If I understand everything right,\x01",
            "the orbment should be getting\x01",
            "power again right...about...\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x2)
    OP_23(0x90)
    Sleep(500)

    ChrTalk(    #191
        0x8,
        "It stopped...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x102,
        "#1042F#6P...\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x5)
    OP_73(0x1)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4915")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4953")

    label("loc_4915")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_493C")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4953")

    label("loc_493C")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4953")

    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_497F")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_49BD")

    label("loc_497F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49A6")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_49BD")

    label("loc_49A6")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_49BD")

    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    ChrTalk(    #193
        0x101,
        "#1004F#4PIt's moving!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0x102,
        "#1042F#6PThere we are! It's back online.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 180, 800)

    ChrTalk(    #195
        0x102,
        "#1046F#6PGet on! This is our chance!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A76")

    ChrTalk(    #196
        0x103,
        "#525FNicely done!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4ABA")

    label("loc_4A76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A9B")

    ChrTalk(    #197
        0x106,
        "#051FRight on!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4ABA")

    label("loc_4A9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4ABA")

    ChrTalk(    #198
        0x108,
        "#072FRight!\x02",
    )

    CloseMessageWindow()

    label("loc_4ABA")


    def lambda_4AC0():
        OP_6D(54080, 50, 56970, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4AC0)

    def lambda_4AD8():
        OP_8E(0xFE, 0xD4EE, 0x0, 0xE164, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4AD8)
    Sleep(100)

    def lambda_4AF8():
        OP_8E(0xFE, 0xD55C, 0x0, 0xDCC8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4AF8)
    Sleep(100)
    OP_8E(0xF9, 0xD08E, 0x0, 0xDCC8, 0x1388, 0x0)

    ChrTalk(    #199 op#A
        0x8,
        "#2AI'll come too!\x02",
    )

    CloseMessageWindow()

    def lambda_4B43():

        label("loc_4B43")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4B43")

    QueueWorkItem2(0x101, 1, lambda_4B43)
    Sleep(100)

    def lambda_4B59():

        label("loc_4B59")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4B59")

    QueueWorkItem2(0xF8, 1, lambda_4B59)

    def lambda_4B6A():

        label("loc_4B6A")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_4B6A")

    QueueWorkItem2(0xF9, 1, lambda_4B6A)

    ChrTalk(    #200 op#A
        0x101,
        "#1005F#2AHurry up then, Mr. Landan!\x02",
    )

    CloseMessageWindow()
    SetChrBattleFlags(0x8, 0x20)

    def lambda_4BA9():
        OP_8E(0xFE, 0xD25A, 0x32, 0xD840, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4BA9)

    def lambda_4BC4():
        OP_8F(0xFE, 0xD55C, 0x0, 0xDDF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_4BC4)
    Sleep(200)

    def lambda_4BE4():
        OP_8F(0xFE, 0xD08E, 0x0, 0xDDF4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 2, lambda_4BE4)
    WaitChrThread(0x8, 0x1)
    OP_8E(0x8, 0xD25A, 0x0, 0xDC28, 0x1388, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_8C(0x102, 0, 800)

    ChrTalk(    #201
        0x102,
        "#1046F#6PBeginning our descent!\x02",
    )

    CloseMessageWindow()

    label("loc_4C4A")

    Call(0, 11)
    Return()

    # Function_10_24E6 end

    def Function_11_4C4F(): pass

    label("Function_11_4C4F")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 5)
    OP_70(0x1, 0xF)
    OP_73(0x1)

    ChrTalk(    #202 op#A op#5
        0x101,
        "#1004F#2A#5PWaah-aaah-aaah!\x05\x02",
    )

    CloseMessageWindow()
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 15)
    OP_70(0x1, 0x19)
    OP_73(0x1)

    ChrTalk(    #203 op#A op#5
        0x101,
        "#1004F#2A#5PWah-wah-wah-wah-wah...\x05\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 25)
    OP_70(0x1, 0x23)
    OP_73(0x1)
    Sleep(200)
    OP_0D()
    OP_6D(129000, 0, 76700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6F(0x2, 360)
    OP_6F(0x2, 280)
    OP_48()
    SetChrBattleFlags(0x8, 0x20)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4DF0")
    OP_89(0x101, 129600, 15000, 77700, 180)
    OP_89(0x107, 128919, 15000, 77680, 0)
    OP_89(0x102, 129720, 15000, 76820, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DDC")
    OP_89(0xF9, 128320, 15000, 76820, 180)
    Jump("loc_4DED")

    label("loc_4DDC")

    OP_89(0xF8, 128320, 15000, 76820, 180)

    label("loc_4DED")

    Jump("loc_4E34")

    label("loc_4DF0")

    OP_89(0x101, 129600, 15000, 77700, 180)
    OP_89(0x102, 128919, 15000, 77680, 0)
    OP_89(0xF8, 129720, 15000, 76820, 180)
    OP_89(0xF9, 128320, 15000, 76820, 180)

    label("loc_4E34")

    OP_89(0x8, 128949, 15000, 76360, 180)
    LoadEffect(0x1, "Craft\\\\cr162_02.eff")
    LoadEffect(0x2, "Craft\\\\cr162_00.eff")
    LoadEffect(0x3, "Craft\\\\cr161_00.eff")
    LoadEffect(0x4, "scraft\\\\sc000_11.eff")
    OP_D2(0x90003, 0x90007, 0x7)
    OP_D2(0x270130, 0x270140, 0x8)
    OP_D2(0x270139, 0x270149, 0x9)
    FadeToBright(1000, 0)
    Sleep(400)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x2, 280)
    OP_70(0x2, 0x10E)
    OP_73(0x2)
    Sleep(400)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x2, 270)
    OP_70(0x2, 0x104)
    OP_73(0x2)
    Sleep(400)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x2, 260)
    OP_70(0x2, 0xFA)
    OP_73(0x2)
    Sleep(400)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x2, 250)
    OP_70(0x2, 0xF0)
    OP_73(0x2)
    OP_23(0x68)
    Sleep(1000)

    ChrTalk(    #204
        0x102,
        "#1035FPhew!...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5005")

    ChrTalk(    #205
        0x103,
        (
            "#025FWell, I can't speak for everyone,\x01",
            "but I certainly came close to biting\x01",
            "off my tongue there.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5005")


    ChrTalk(    #206
        0x101,
        (
            "#1019FYou know, I think it might've been more\x01",
            "pleasant to just throw ourselves against\x01",
            "the elevator. Repeatedly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_50DF")

    ChrTalk(    #207
        0x107,
        (
            "#067FEhehehehe... The, um, the drive orbment's\x01",
            "not quite at full power, so...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51FA")

    label("loc_50DF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_516C")

    ChrTalk(    #208
        0x108,
        (
            "#070FThe drive orbment probably isn't\x01",
            "quite at full output.\x02\x03",

            "Anyway, we did manage to make\x01",
            "it down. Let's investigate.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51FA")

    label("loc_516C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51FA")

    ChrTalk(    #209
        0x106,
        (
            "#552FThe orbment probably ain't puttin'\x01",
            "out enough power.\x02\x03",

            "#053FEh, given the situation, we can't\x01",
            "complain about the ride.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51FA")


    def lambda_5200():
        OP_6D(129479, 150, 73430, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5200)

    def lambda_5218():
        OP_8E(0xFE, 0x1F7E8, 0x3C, 0x119B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5218)
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52E2")

    def lambda_5246():
        OP_8E(0xFE, 0x1FA0E, 0x0, 0x12304, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5246)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_528B")

    def lambda_5273():
        OP_8E(0xFE, 0x1F612, 0x0, 0x12304, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5273)
    Jump("loc_52A6")

    label("loc_528B")


    def lambda_5291():
        OP_8E(0xFE, 0x1F612, 0x0, 0x12304, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5291)

    label("loc_52A6")

    Sleep(100)

    def lambda_52B1():
        OP_8E(0xFE, 0x1FA0E, 0x0, 0x126EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52B1)
    Sleep(50)
    OP_8E(0x107, 0x1F612, 0x0, 0x126EC, 0x7D0, 0x0)
    Jump("loc_5356")

    label("loc_52E2")


    def lambda_52E8():
        OP_8E(0xFE, 0x1FA0E, 0x0, 0x12304, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_52E8)
    Sleep(100)

    def lambda_5308():
        OP_8E(0xFE, 0x1F612, 0x0, 0x12304, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5308)
    Sleep(100)

    def lambda_5328():
        OP_8E(0xFE, 0x1FA0E, 0x0, 0x126EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5328)
    Sleep(50)
    OP_8E(0x102, 0x1F612, 0x0, 0x126EC, 0x7D0, 0x0)

    label("loc_5356")

    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x8, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_8C(0x8, 45, 400)
    Sleep(500)

    ChrTalk(    #210
        0x8,
        (
            "Ah, right. Luckily, I've got a \x01",
            "non-orbal light set up here...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 270, 400)

    def lambda_53D9():

        label("loc_53D9")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_53D9")

    QueueWorkItem2(0x101, 1, lambda_53D9)

    def lambda_53EA():

        label("loc_53EA")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_53EA")

    QueueWorkItem2(0x102, 1, lambda_53EA)

    def lambda_53FB():

        label("loc_53FB")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_53FB")

    QueueWorkItem2(0xF8, 1, lambda_53FB)

    def lambda_540C():

        label("loc_540C")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_540C")

    QueueWorkItem2(0xF9, 1, lambda_540C)

    def lambda_541D():
        OP_6D(127060, 0, 73010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_541D)
    OP_8E(0x8, 0x1E938, 0x0, 0x11940, 0x7D0, 0x0)
    OP_8C(0x8, 225, 400)
    Sleep(500)

    ChrTalk(    #211
        0x8,
        "#1P...Tunnels sure are quiet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0x8,
        (
            "#1PWhere are the guys?\x01",
            "You think we might be overreacti--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #213
        0x8,
        "#1PHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0x102,
        "#1044FDid you hear something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x8,
        "#1PYeah, someone's coming!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x8,
        (
            "#1PHeeey, I recognize him!\x01",
            "That's Trent!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x8,
        (
            "#1PYo, Trent! What're you doin'\x01",
            "over there, you lazy...\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, 120370, 0, 67550, 90)

    def lambda_55A9():

        label("loc_55A9")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_55A9")

    QueueWorkItem2(0x8, 1, lambda_55A9)

    def lambda_55BA():

        label("loc_55BA")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_55BA")

    QueueWorkItem2(0x101, 1, lambda_55BA)

    def lambda_55CB():

        label("loc_55CB")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_55CB")

    QueueWorkItem2(0x102, 1, lambda_55CB)

    def lambda_55DC():

        label("loc_55DC")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_55DC")

    QueueWorkItem2(0xF8, 1, lambda_55DC)

    def lambda_55ED():

        label("loc_55ED")

        TurnDirection(0xFE, 0x9, 400)
        OP_48()
        Jump("loc_55ED")

    QueueWorkItem2(0xF9, 1, lambda_55ED)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x9, 0x1EB54, 0x0, 0x11602, 0x1770, 0x0)

    def lambda_5624():
        OP_6D(129380, 60, 72150, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5624)
    OP_8E(0x9, 0x203AA, 0x0, 0x11698, 0x1770, 0x0)
    OP_8C(0x9, 270, 400)
    WaitChrThread(0x101, 0x2)
    OP_62(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    TurnDirection(0x8, 0x9, 400)
    Sleep(500)

    ChrTalk(    #218
        0x8,
        "Hey...what's with that face?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x9,
        "B-Behind...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0x8,
        "Eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0x9,
        "THEY'RE COMING FROM BEHIND!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x10, 121610, 0, 69620, 45)
    SetChrPos(0x11, 118640, 0, 68820, 45)
    SetChrPos(0x12, 118570, 0, 67630, 45)
    SetChrPos(0x13, 119440, 0, 66840, 45)
    SetChrPos(0x14, 120720, 0, 67050, 45)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_59()
    Fade(1000)
    OP_6D(121150, 0, 69600, 0)
    OP_6C(270000, 0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0x8, 0x1)
    SetChrPos(0x8, 123930, 0, 71340, 0)
    TurnDirection(0x8, 0x9, 0)
    OP_0D()

    def lambda_57BA():
        OP_94(0x1, 0xFE, 0xA, 0x47E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_57BA)
    Sleep(100)

    def lambda_57D5():
        OP_94(0x1, 0xFE, 0xA, 0x47E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_57D5)

    def lambda_57EB():
        OP_94(0x1, 0xFE, 0xA, 0x47E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_57EB)
    Sleep(100)

    def lambda_5806():
        OP_94(0x1, 0xFE, 0xA, 0x47E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5806)

    def lambda_581C():
        OP_94(0x1, 0xFE, 0xA, 0x47E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_581C)

    def lambda_5832():
        OP_94(0x1, 0xFE, 0xA, 0x47E, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5832)
    OP_8C(0x8, 235, 400)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0x8, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    Sleep(400)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_5894():
        OP_94(0x1, 0x8, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5894)

    ChrTalk(    #222
        0x8,
        "WAAAAAAAAH!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrChipByIndex(0x102, 9)
    SetChrSubChip(0x102, 3)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0x102, 123030, 3000, 70820, 235)
    PlayEffect(0x1, 0x0, 0x102, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    OP_83(0x0, 0x2)
    OP_43(0x102, 0x1, 0x0, 0xC)
    Sleep(300)
    PlayEffect(0x3, 0xFF, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x4, 0xFF, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4A(0x10, 0)
    SetChrChipByIndex(0x10, 7)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x10, 0x40)

    def lambda_59BB():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_59BB)
    OP_8F(0x10, 0x1D9AC, 0x0, 0x10E46, 0x1B58, 0x0)
    SetChrChipByIndex(0x10, 2)
    ClearChrFlags(0x10, 0x20)
    OP_4B(0x10, 0)
    OP_96(0x102, 0x1E168, 0x0, 0x1149A, 0x1F4, 0x1388)
    SetChrFlags(0x8, 0x40)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8E(0x8, 0x1F25C, 0x0, 0x125D4, 0xFA0, 0x0)

    def lambda_5A39():
        OP_8E(0xFE, 0x1FAFD, 0x0, 0x125C0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5A39)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)

    def lambda_5A63():
        OP_6D(122730, 0, 70630, 2000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5A63)
    OP_43(0x101, 0x1, 0x0, 0xD)
    Sleep(100)
    OP_43(0xF8, 0x1, 0x0, 0xE)
    Sleep(100)
    OP_43(0xF9, 0x1, 0x0, 0xF)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x40)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AD7")

    ChrTalk(    #223
        0x106,
        "#057FTch. Monsters already?\x02",
    )

    CloseMessageWindow()

    label("loc_5AD7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B0C")

    ChrTalk(    #224
        0x107,
        "#065FAaaaaaaaah! There's so many!\x02",
    )

    CloseMessageWindow()

    label("loc_5B0C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B4F")

    ChrTalk(    #225
        0x108,
        (
            "#070FHaha, looks like we get a\x01",
            "welcoming party.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B4F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BB7")

    ChrTalk(    #226
        0x103,
        (
            "#025F*sigh* Shelled monsters. I hate these\x01",
            "things. They're so hard to whip properly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5BB7")


    ChrTalk(    #227
        0x101,
        (
            "#1002F#4POh, heck.\x01",
            "More monsters from that nest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x102,
        (
            "#1042F#7PMost likely.\x02\x03",

            "We don't really have time to think\x01",
            "about it! Defend yourselves!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10, 3)

    def lambda_5C54():
        OP_94(0x1, 0xFE, 0x0, 0x6A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_5C54)
    Sleep(30)
    SetChrChipByIndex(0x11, 3)
    SetChrChipByIndex(0x14, 3)

    def lambda_5C79():
        OP_94(0x1, 0xFE, 0x0, 0x6A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_5C79)

    def lambda_5C8F():
        OP_94(0x1, 0xFE, 0x0, 0x6A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_5C8F)
    Sleep(30)
    SetChrChipByIndex(0x12, 3)
    SetChrChipByIndex(0x13, 3)

    def lambda_5CB4():
        OP_94(0x1, 0xFE, 0x0, 0x6A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_5CB4)

    def lambda_5CCA():
        OP_94(0x1, 0xFE, 0x0, 0x6A4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5CCA)
    WaitChrThread(0x10, 0x1)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    Battle(0x57, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_5D1C"),
        (SWITCH_DEFAULT, "loc_5D21"),
    )


    label("loc_5D1C")

    OP_B4(0x0)
    Jump("loc_5D21")

    label("loc_5D21")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    Call(0, 16)
    Return()

    # Function_11_4C4F end

    def Function_12_5D3F(): pass

    label("Function_12_5D3F")

    OP_99(0xFE, 0x3, 0xB, 0x7D0)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_12_5D3F end

    def Function_13_5D53(): pass

    label("Function_13_5D53")

    SetChrPos(0xFE, 126140, 0, 74760, 225)
    OP_8E(0xFE, 0x1E0E6, 0x0, 0x11936, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_13_5D53 end

    def Function_14_5D80(): pass

    label("Function_14_5D80")

    SetChrPos(0xFE, 128370, 0, 74230, 225)
    OP_8E(0xFE, 0x1E672, 0x0, 0x112EC, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_14_5D80 end

    def Function_15_5DAD(): pass

    label("Function_15_5DAD")

    SetChrPos(0xFE, 128690, 0, 75630, 225)
    OP_8E(0xFE, 0x1E708, 0x0, 0x117BA, 0x1388, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_15_5DAD end

    def Function_16_5DDA(): pass

    label("Function_16_5DDA")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_6D(123290, 0, 71580, 0)
    OP_67(0, 7880, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 123110, 0, 71990, 225)
    SetChrPos(0x102, 123240, 0, 70810, 225)
    SetChrPos(0xF8, 124530, 0, 70380, 225)
    SetChrPos(0xF9, 124680, 0, 71610, 225)
    OP_4A(0x8, 255)
    OP_4A(0x9, 255)
    SetChrPos(0x8, 132100, 0, 74120, 225)
    SetChrPos(0x9, 132170, 0, 72480, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #229
        0x101,
        "#1002FThat should be all of them.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F48")

    ChrTalk(    #230
        0x103,
        (
            "#025FThat's more work than I needed\x01",
            "after an elevator ride like that...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5FDA")

    label("loc_5F48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5F84")

    ChrTalk(    #231
        0x106,
        "#050FKinda tough for Rolent critters.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5FDA")

    label("loc_5F84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5FDA")

    ChrTalk(    #232
        0x108,
        (
            "#075FHm. Not the kind of monster we\x01",
            "can let our guard down around.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FDA")


    ChrTalk(    #233
        0x102,
        "#1035FYes, we'll need to be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x8,
        "#5PH-Hey, bracers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x9,
        (
            "#5PIs it okay to come out?\x01",
            "Please?\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    OP_22(0xD5, 0x0, 0x64)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #236
        0x101,
        "#1011FOh, yeah! It's clear now.\x02",
    )

    CloseMessageWindow()
    OP_59()
    SetChrPos(0x9, 131020, 0, 71030, 270)
    SetChrPos(0x8, 130449, 220, 72720, 270)

    def lambda_60A5():
        OP_6D(124320, 0, 71010, 1500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_60A5)

    def lambda_60BD():
        OP_6C(315000, 1500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_60BD)

    def lambda_60CD():
        OP_8E(0xFE, 0x1EC8A, 0x0, 0x115B2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_60CD)

    def lambda_60E8():
        OP_8E(0xFE, 0x1ECB2, 0x0, 0x11A08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_60E8)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)

    def lambda_610D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_610D)

    def lambda_611B():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_611B)
    Sleep(100)
    SetChrChipByIndex(0x102, 65535)

    def lambda_6133():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6133)
    WaitChrThread(0x9, 0x1)

    ChrTalk(    #237
        0x9,
        "Ohhhh, thank you so much!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x9,
        (
            "Thanks to you guys, I get to\x01",
            "live to enjoy another meal!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #239
        0x8,
        (
            "#2PYou idiot!\x01",
            "This isn't the time for that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x8,
        (
            "#2PFirst things first. Where's the boss\x01",
            "and the rest of the boys?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0x101,
        (
            "#1002FYeah, can you tell us what's\x01",
            "going on down here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0x102,
        "#1042F#3PWas there an accident or something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x9,
        "Uh... Yeah, kinda.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0x9,
        (
            "So we were working when suddenly the lights\x01",
            "we use to chase away the monsters cut out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0x9,
        (
            "Wasn't much we could do, so we put\x01",
            "the job aside and came here to wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x9,
        (
            "And then this morning, a huge swarm of\x01",
            "monsters flooded out of the dig site!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0x9,
        (
            "Gaa-aaah... I thought we were\x01",
            "monster food for sure!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0x101,
        (
            "#1002FHold on a sec.\x02\x03",

            "Wasn't there a bracer with you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x9,
        "Y-Yeah, there was...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0x9,
        (
            "He bought some time\x01",
            "for us to get away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x9,
        (
            "But... But the last we saw of him,\x01",
            "he was being swallowed up by\x01",
            "the horde of monsters...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6511")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_654F")

    label("loc_6511")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6538")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_654F")

    label("loc_6538")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_654F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6576")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_65B4")

    label("loc_6576")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_659D")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_65B4")

    label("loc_659D")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_65B4")

    Sleep(800)

    ChrTalk(    #252
        0x101,
        "#1020FNO!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_65EB")

    ChrTalk(    #253
        0x107,
        "#065F#6POh, no!\x02",
    )

    CloseMessageWindow()

    label("loc_65EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_661D")

    ChrTalk(    #254
        0x103,
        "#023F#6PYou mean Ridge is...?!\x02",
    )

    CloseMessageWindow()

    label("loc_661D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_663C")

    ChrTalk(    #255
        0x108,
        "#072F#6P...\x02",
    )

    CloseMessageWindow()

    label("loc_663C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_665F")

    ChrTalk(    #256
        0x106,
        "#057F#6PDamn...\x02",
    )

    CloseMessageWindow()

    label("loc_665F")


    ChrTalk(    #257
        0x102,
        (
            "#1042F...We need to get moving.\x01",
            "Right now.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_670F")

    ChrTalk(    #258
        0x103,
        (
            "#022F#6PYes, we need to rescue those miners first.\x02\x03",

            "We can go save Ridge afterward.\x01",
            "And we WILL save him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6833")

    label("loc_670F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6796")

    ChrTalk(    #259
        0x108,
        (
            "#072F#6PFirst we must hurry and\x01",
            "save the miners.\x02\x03",

            "We can talk about...recovering our\x01",
            "brother-in-arms after that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6833")

    label("loc_6796")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6833")

    ChrTalk(    #260
        0x106,
        (
            "#057F#6PYeah. Saving the miners has\x01",
            "got to be our first priority.\x02\x03",

            "After that we can think about gettin'\x01",
            "Ridge back...one way or another.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6833")


    ChrTalk(    #261
        0x101,
        (
            "#1003F...Yeah, you're right.\x02\x03",

            "I'm worried about Ridge,\x01",
            "but we have our mission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x9,
        (
            "I... I got so hungry I made a\x01",
            "break for it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x9,
        (
            "I think the boss and everyone else\x01",
            "are still hiding somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6945")

    ChrTalk(    #264
        0x108,
        "#072F#6PHow many miners are here in total?\x02",
    )

    CloseMessageWindow()
    Jump("loc_69CB")

    label("loc_6945")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_698A")

    ChrTalk(    #265
        0x106,
        "#052F#6PHow many of you are down here, anyway?\x02",
    )

    CloseMessageWindow()
    Jump("loc_69CB")

    label("loc_698A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69CB")

    ChrTalk(    #266
        0x103,
        "#022F#6PHow many of the miners were on shift?\x02",
    )

    CloseMessageWindow()

    label("loc_69CB")

    OP_8C(0x8, 270, 400)

    ChrTalk(    #267
        0x8,
        "#2PThere should be four others.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x8,
        "#2PFive if you count the bracer guy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        (
            "#1002FOkay. Five people.\x02\x03",

            "Let's get looking, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x102,
        "#1042FLet's hurry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x9,
        "G-Good luck!\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 255)
    OP_4B(0x9, 255)
    SetChrPos(0x8, 132100, 0, 74120, 225)
    SetChrPos(0x9, 132170, 0, 72480, 270)
    OP_6D(123230, 0, 71000, 0)
    SetChrPos(0x0, 123230, 0, 71000, 270)
    SetChrPos(0x1, 123230, 0, 71000, 270)
    SetChrPos(0x2, 123230, 0, 71000, 270)
    SetChrPos(0x3, 123230, 0, 71000, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x2088)
    OP_28(0xBF, 0x1, 0x2)
    OP_28(0xBF, 0x1, 0x4)
    OP_28(0xBF, 0x1, 0x8)
    EventEnd(0x0)
    Return()

    # Function_16_5DDA end

    def Function_17_6B34(): pass

    label("Function_17_6B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6B41")
    Return()

    label("loc_6B41")

    EventBegin(0x0)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    SetChrPos(0xA, 130610, 1000, 14190, 180)
    SetChrPos(0xB, 130610, 1000, 12770, 0)

    def lambda_6B73():
        OP_6D(130580, 1000, 13440, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B73)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #272
        0xA,
        (
            "#1SOh, Aidios, who dwells above...please reach\x01",
            "out your hand to us, your unworthy children...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xB,
        "#1S(SHH! Keep quiet!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xB,
        (
            "#1S(Quit muttering like that.\x01",
            "The monsters will hear you!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xA,
        (
            "#1SHmph! In the last cave-in it was surely\x01",
            "the grace of the Goddess which saved us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xA,
        (
            "#1SA little faith wouldn't hurt you\x01",
            "in a situation like this, Heinrich.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)
    OP_4B(0xA, 255)
    OP_4B(0xB, 255)
    OP_69(0x0, 0x0)
    OP_0D()
    OP_A2(0x2089)
    EventEnd(0x1)
    Return()

    # Function_17_6B34 end

    def Function_18_6D0E(): pass

    label("Function_18_6D0E")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(130139, 1000, 12840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    SetChrFlags(0x1E, 0x80)
    AddParty(0x48, 0xFF, 0xFF)
    AddParty(0x49, 0xFF, 0xFF)
    SetChrFlags(0x149, 0x80)
    SetChrFlags(0x14A, 0x80)
    SetChrPos(0x101, 129190, 1000, 12210, 90)
    SetChrPos(0x102, 128000, 1000, 11480, 90)
    SetChrPos(0xF8, 129220, 1000, 13440, 90)
    SetChrPos(0xF9, 127720, 1000, 13010, 90)
    OP_4A(0xA, 255)
    OP_4A(0xB, 255)
    OP_8C(0xA, 270, 0)
    OP_8C(0xB, 270, 0)
    OP_0D()

    ChrTalk(    #277
        0xB,
        "#6PWho the?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x102,
        "#1042F#4PWe're from the Bracer Guild.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x101,
        "#1002FAre you two hurt at all?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0xB,
        "#6PNo, we're fine, somehow.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xA,
        "#3POh, Aidios, thank you for this salvation...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F0D")

    ChrTalk(    #282
        0x108,
        (
            "#072FYou're welcome to be as faithful as you\x01",
            "wish, but thanks are a bit premature.\x02\x03",

            "We need to get you out of\x01",
            "here as soon as we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FFE")

    label("loc_6F0D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F92")

    ChrTalk(    #283
        0x106,
        (
            "#050FHey, hey. It's a little early to be\x01",
            "thankin' the Goddess just yet.\x02\x03",

            "We need to get you out of here first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6FFE")

    label("loc_6F92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6FFE")

    ChrTalk(    #284
        0x103,
        (
            "#022FIt's a little early yet for prayers, Pierre.\x02\x03",

            "We need to get you out of here first.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FFE")

    OP_59()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x102, 315, 400)
    SetChrChipByIndex(0x102, 12)
    SetChrSubChip(0x102, 0)
    OP_22(0xD5, 0x0, 0x64)

    ChrTalk(    #285
        0x102,
        "#1042F#6PYes. First, we--\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)

    def lambda_7060():
        OP_6D(127130, 1000, 12140, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_7060)
    OP_43(0x10, 0x1, 0x0, 0x13)
    Sleep(200)

    def lambda_7084():

        label("loc_7084")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_7084")

    QueueWorkItem2(0x101, 1, lambda_7084)

    def lambda_7095():

        label("loc_7095")

        TurnDirection(0xFE, 0x10, 400)
        OP_48()
        Jump("loc_7095")

    QueueWorkItem2(0x102, 1, lambda_7095)

    def lambda_70A6():

        label("loc_70A6")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_70A6")

    QueueWorkItem2(0xF8, 1, lambda_70A6)

    def lambda_70B7():

        label("loc_70B7")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_70B7")

    QueueWorkItem2(0xF9, 1, lambda_70B7)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    Sleep(200)
    OP_43(0x11, 0x1, 0x0, 0x14)
    Sleep(400)
    OP_43(0x12, 0x1, 0x0, 0x15)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_712E():
        OP_94(0x1, 0xFE, 0xBE, 0xC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_712E)
    Sleep(100)
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_715B():
        OP_94(0x1, 0xFE, 0xAA, 0xC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_715B)

    ChrTalk(    #286
        0xB,
        "#6POh, crap!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xA,
        "#3PGoddess' mercy!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71CB")

    ChrTalk(    #288
        0x103,
        "#024FThey're coming! Watch out!\x02",
    )

    CloseMessageWindow()
    Jump("loc_723C")

    label("loc_71CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7201")

    ChrTalk(    #289
        0x106,
        "#054FHere they come! BREAK 'EM!\x02",
    )

    CloseMessageWindow()
    Jump("loc_723C")

    label("loc_7201")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_723C")

    ChrTalk(    #290
        0x108,
        "#076FHere they come! Defend yourselves!\x02",
    )

    CloseMessageWindow()

    label("loc_723C")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    SetChrChipByIndex(0x10, 3)

    def lambda_7257():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7257)
    Sleep(30)
    SetChrChipByIndex(0x11, 3)

    def lambda_7277():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7277)
    Sleep(30)
    SetChrChipByIndex(0x12, 3)

    def lambda_7297():
        OP_94(0x1, 0xFE, 0x0, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7297)
    WaitChrThread(0x10, 0x1)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    Battle(0xED8, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_72D1"),
        (SWITCH_DEFAULT, "loc_72D6"),
    )


    label("loc_72D1")

    OP_B4(0x0)
    Jump("loc_72D6")

    label("loc_72D6")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    RemoveParty(0x48, 0xFF)
    RemoveParty(0x49, 0xFF)
    EventBegin(0x0)
    OP_6D(128650, 1000, 12260, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, 130610, 1000, 12770, 270)
    SetChrPos(0xA, 130610, 1000, 14190, 270)
    SetChrPos(0x101, 129190, 1000, 12210, 270)
    SetChrPos(0x102, 128000, 1000, 11480, 270)
    SetChrPos(0xF8, 129220, 1000, 13440, 270)
    SetChrPos(0xF9, 127720, 1000, 13010, 270)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #291
        0x101,
        (
            "#1006FAllllll right!\x01",
            "Nothing beats us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0xB,
        "#6PGwaaaaaaah... Ohh, sweet Aidios!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xA,
        "#3PI was sweating bullets there...\x02",
    )

    CloseMessageWindow()

    def lambda_7422():
        OP_8C(0x102, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7422)

    def lambda_7430():
        OP_8C(0xF8, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_7430)
    Sleep(200)

    def lambda_7443():
        OP_8C(0x101, 90, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7443)

    def lambda_7451():
        OP_8C(0xF9, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_7451)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #294
        0x102,
        (
            "#1042FRun for the elevator immediately.\x02\x03",

            "The way should still be clear,\x01",
            "but you need to go right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xB,
        "#6PR-Right! Thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xA,
        "#6PAidios' grace be with you, heroes!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1D, 0x80)

    def lambda_7518():

        label("loc_7518")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_7518")

    QueueWorkItem2(0x102, 1, lambda_7518)

    def lambda_7529():

        label("loc_7529")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_7529")

    QueueWorkItem2(0x101, 1, lambda_7529)

    def lambda_753A():

        label("loc_753A")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_753A")

    QueueWorkItem2(0xF8, 1, lambda_753A)

    def lambda_754B():

        label("loc_754B")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_754B")

    QueueWorkItem2(0xF9, 1, lambda_754B)

    def lambda_755C():
        OP_6D(126940, 1000, 12790, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_755C)
    OP_43(0xB, 0x1, 0x0, 0x16)
    Sleep(200)
    OP_43(0xA, 0x1, 0x0, 0x17)
    WaitChrThread(0xA, 0x1)
    OP_44(0x102, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    OP_A2(0x208A)
    OP_28(0xBF, 0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7665")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as saved all three groups\x01",      # 0
            "No change\x01",                          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7612"),
        (SWITCH_DEFAULT, "loc_7665"),
    )


    label("loc_7612")

    OP_A2(0x2089)
    OP_A2(0x208A)
    OP_A2(0x208B)
    OP_A2(0x208C)
    SetChrPos(0xA, 131940, 0, 69900, 315)
    SetChrPos(0xB, 130930, 0, 68610, 45)
    SetChrPos(0xC, 124780, 0, 74190, 180)
    SetChrPos(0xD, 126540, 0, 75140, 180)
    Jump("loc_7665")

    label("loc_7665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7703")
    OP_A2(0x0)
    OP_51(0x1C, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)

    def lambda_76C1():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_76C1)

    def lambda_76CF():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_76CF)
    Sleep(150)

    def lambda_76E2():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_76E2)

    def lambda_76F0():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_76F0)
    OP_69(0x1C, 0x7D0)
    Call(0, 33)

    label("loc_7703")

    EventEnd(0x0)
    Return()

    # Function_18_6D0E end

    def Function_19_7706(): pass

    label("Function_19_7706")

    SetChrPos(0xFE, 124640, 0, 21610, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x1E064, 0x0, 0x4E16, 0x1388, 0x0)
    OP_8E(0xFE, 0x1E064, 0x1F4, 0x3B42, 0x1388, 0x0)
    OP_8E(0xFE, 0x1EAC8, 0x1F4, 0x2A62, 0x1388, 0x0)
    OP_8C(0x10, 90, 400)
    SetChrChipByIndex(0x10, 2)
    OP_43(0xFE, 0x0, 0x0, 0x2)
    Return()

    # Function_19_7706 end

    def Function_20_7771(): pass

    label("Function_20_7771")

    SetChrPos(0xFE, 124640, 0, 21610, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x1E064, 0x0, 0x4E16, 0x1388, 0x0)
    OP_8E(0xFE, 0x1E064, 0x1F4, 0x3B42, 0x1388, 0x0)
    OP_8E(0xFE, 0x1E71C, 0x1F4, 0x2ECC, 0x1388, 0x0)
    OP_8C(0x11, 90, 400)
    SetChrChipByIndex(0x11, 2)
    OP_43(0xFE, 0x0, 0x0, 0x2)
    Return()

    # Function_20_7771 end

    def Function_21_77DC(): pass

    label("Function_21_77DC")

    SetChrPos(0xFE, 124640, 0, 21610, 90)
    SetChrChipByIndex(0xFE, 3)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x1E064, 0x0, 0x4E16, 0x1388, 0x0)
    OP_8E(0xFE, 0x1E064, 0x1F4, 0x3B42, 0x1388, 0x0)
    OP_8E(0xFE, 0x1E460, 0x1F4, 0x32F0, 0x1388, 0x0)
    OP_8C(0x12, 90, 400)
    SetChrChipByIndex(0xFE, 2)
    OP_43(0xFE, 0x0, 0x0, 0x2)
    Return()

    # Function_21_77DC end

    def Function_22_7847(): pass

    label("Function_22_7847")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x1F7D3, 0x3E8, 0x2A94, 0x1388, 0x0)
    OP_8E(0xFE, 0x1ED02, 0x1F4, 0x2A94, 0x1388, 0x0)
    OP_8E(0xFE, 0x1DF60, 0x1F4, 0x3836, 0x1388, 0x0)
    OP_8E(0xFE, 0x1DF06, 0xFFFFFE98, 0x4704, 0x1388, 0x0)
    ClearChrFlags(0xFE, 0x40)
    SetChrPos(0xB, 130930, 0, 68610, 45)
    OP_4B(0xB, 255)
    Return()

    # Function_22_7847 end

    def Function_23_78C9(): pass

    label("Function_23_78C9")

    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0x1FE32, 0x3E8, 0x31E2, 0x1388, 0x0)
    OP_8E(0xFE, 0x1F7D3, 0x3E8, 0x2A94, 0x1388, 0x0)
    OP_8E(0xFE, 0x1ED02, 0x1F4, 0x2A94, 0x1388, 0x0)
    OP_8E(0xFE, 0x1DF60, 0x1F4, 0x3836, 0x1388, 0x0)
    OP_8E(0xFE, 0x1DF06, 0xFFFFFE98, 0x4704, 0x1388, 0x0)
    ClearChrFlags(0xFE, 0x40)
    SetChrPos(0xA, 131940, 0, 69900, 315)
    OP_4B(0xA, 255)
    Return()

    # Function_23_78C9 end

    def Function_24_795F(): pass

    label("Function_24_795F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_796C")
    Return()

    label("loc_796C")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0xC, 255)
    SetChrPos(0xC, 91290, 0, 30810, 129)
    SetChrFlags(0xC, 0x40)
    OP_6C(0, 0)
    TurnDirection(0x0, 0xC, 0)
    TurnDirection(0x1, 0xC, 0)
    TurnDirection(0x2, 0xC, 0)
    TurnDirection(0x3, 0xC, 0)
    OP_0D()

    def lambda_79B9():
        OP_6D(94990, -500, 28960, 2500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_79B9)
    OP_8E(0xC, 0x16C56, 0xFFFFFF10, 0x727E, 0x3E8, 0x0)
    OP_62(0xC, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)
    AddParty(0x4A, 0xFF, 0xFF)

    ChrTalk(    #297
        0xC,
        (
            "#6PD-Darn you, Trent, running\x01",
            "off on your own...!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xC,
        (
            "#6PWhat am I supposed to do\x01",
            "all alone like this?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0xC, 270, 400)
    SetChrChipByIndex(0x10, 3)
    SetChrChipByIndex(0x12, 3)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 87360, -450, 30190, 181)
    SetChrPos(0x12, 86520, -380, 28480, 180)
    SetChrPos(0x11, 99570, 0, 24640, 315)
    SetChrPos(0x13, 100440, 0, 25840, 315)

    def lambda_7AE8():
        OP_6D(93440, -330, 29110, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7AE8)

    def lambda_7B00():
        OP_92(0x10, 0xC, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7B00)

    def lambda_7B15():
        OP_92(0x12, 0xC, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_7B15)
    WaitChrThread(0x10, 0x1)
    SetChrChipByIndex(0x10, 2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    WaitChrThread(0x12, 0x1)
    SetChrChipByIndex(0x12, 2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #299
        0xC,
        "#6PWhat DO I do? This is bad...\x02",
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xC, 90, 400)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x11, 3)
    SetChrChipByIndex(0x13, 3)

    def lambda_7BA3():
        OP_8E(0xFE, 0x17B06, 0x0, 0x6F90, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_7BA3)

    def lambda_7BBE():
        OP_8E(0xFE, 0x17584, 0xFFFFFEB6, 0x6F0E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7BBE)
    OP_94(0x1, 0xC, 0x0, 0x1F4, 0x7D0, 0x0)
    TurnDirection(0xC, 0x11, 0)
    OP_62(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_95(0xC, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_94(0x1, 0xC, 0xB4, 0x1F4, 0x1388, 0x0)
    WaitChrThread(0x11, 0x1)
    SetChrChipByIndex(0x11, 2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    WaitChrThread(0x13, 0x1)
    SetChrChipByIndex(0x13, 2)
    OP_43(0x13, 0x0, 0x0, 0x2)

    ChrTalk(    #300
        0xC,
        "Gyah!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 90, 0)
    OP_8C(0x12, 90, 0)
    OP_44(0x10, 0x1)
    OP_44(0x11, 0x1)
    OP_44(0x12, 0x1)
    OP_44(0x13, 0x1)
    SetChrChipByIndex(0x10, 3)
    SetChrChipByIndex(0x11, 3)
    SetChrChipByIndex(0x12, 3)
    SetChrChipByIndex(0x13, 3)

    def lambda_7C8B():

        label("loc_7C8B")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_7C8B")

    QueueWorkItem2(0x10, 2, lambda_7C8B)

    def lambda_7C9C():

        label("loc_7C9C")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_7C9C")

    QueueWorkItem2(0x11, 2, lambda_7C9C)

    def lambda_7CAD():

        label("loc_7CAD")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_7CAD")

    QueueWorkItem2(0x13, 2, lambda_7CAD)

    def lambda_7CBE():
        OP_6D(93850, -230, 29940, 1500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7CBE)

    def lambda_7CD6():
        OP_94(0x1, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_7CD6)

    def lambda_7CEC():
        OP_92(0xFE, 0xC, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7CEC)
    Sleep(120)
    OP_43(0x12, 0x1, 0x0, 0x1D)
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0xC, 0x16DA0, 0xFFFFFF2E, 0x7454, 0x3E8, 0x0)
    OP_8C(0xC, 225, 400)
    OP_8F(0xC, 0x172E6, 0xFFFFFF10, 0x779C, 0x3E8, 0x0)

    ChrTalk(    #301
        0xC,
        (
            "Oh, hell! No, not yet!\x01",
            "NOT YET!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xC,
        "SOMEONE! HEEEEEELP!\x02",
    )

    CloseMessageWindow()

    def lambda_7D8C():
        OP_6D(96410, -130, 28390, 2000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_7D8C)

    def lambda_7DA4():
        OP_6C(315000, 2000)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_7DA4)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_43(0x102, 0x1, 0x0, 0x1A)
    Sleep(200)
    OP_43(0x101, 0x1, 0x0, 0x19)
    Sleep(200)
    OP_43(0xF9, 0x1, 0x0, 0x1C)
    Sleep(200)
    OP_43(0xF8, 0x1, 0x0, 0x1B)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0xC, 0x1)
    TurnDirection(0xC, 0x101, 800)

    ChrTalk(    #303
        0xC,
        "#6PWha...? Estelle Bright?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x101,
        "#1006F#2PQuestions later!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x102,
        "#1042F#1PWe'll save you!\x02",
    )

    CloseMessageWindow()
    Battle(0xED9, 0x300018, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_7E89"),
        (SWITCH_DEFAULT, "loc_7E8E"),
    )


    label("loc_7E89")

    OP_B4(0x0)
    Jump("loc_7E8E")

    label("loc_7E8E")

    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    EventBegin(0x0)
    RemoveParty(0x4A, 0xFF)
    OP_6D(95530, -350, 29670, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 95990, -230, 28580, 180)
    SetChrPos(0x102, 94980, -500, 28580, 180)
    SetChrPos(0xF8, 96920, 0, 28930, 90)
    SetChrPos(0xF9, 93800, -470, 28930, 225)
    OP_8C(0xC, 180, 0)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0xC, 95240, -270, 30370, 180)
    ClearChrFlags(0xC, 0x40)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #306
        0xC,
        "#3PHaah, hooh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xC,
        (
            "#3PMan, oh, man...\x01",
            "I thought I was dead for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x101,
        (
            "#1007FIs it me or does this get\x01",
            "harder every time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0x102,
        "#1043FIt was a close one, that's for sure.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8069")

    ChrTalk(    #310
        0x107,
        "#561FI'm so glad we made it!\x02",
    )

    CloseMessageWindow()
    Jump("loc_80F9")

    label("loc_8069")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80B4")

    ChrTalk(    #311
        0x108,
        (
            "#073FNo kidding... We were\x01",
            "just in the nick of time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_80F9")

    label("loc_80B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80F9")

    ChrTalk(    #312
        0x103,
        (
            "#027FReally... Good job giving us\x01",
            "a scare, Bones.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80F9")


    ChrTalk(    #313
        0xC,
        "#3PI knew it, it's you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xC,
        (
            "#3PYou guys saved us from\x01",
            "that cave-in!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)

    def lambda_8162():

        label("loc_8162")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_8162")

    QueueWorkItem2(0x101, 1, lambda_8162)

    def lambda_8173():

        label("loc_8173")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_8173")

    QueueWorkItem2(0x102, 1, lambda_8173)
    Sleep(200)
    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)

    def lambda_819D():

        label("loc_819D")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_819D")

    QueueWorkItem2(0xF8, 1, lambda_819D)

    def lambda_81AE():

        label("loc_81AE")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_81AE")

    QueueWorkItem2(0xF9, 1, lambda_81AE)

    ChrTalk(    #315
        0x101,
        "#1006FThat's us!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x102,
        (
            "#1040F#2PWe were only junior bracers\x01",
            "back then, mind.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xC,
        "So you guys are senior bracers now, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #318
        0xC,
        (
            "Lookin' at you now, yeah, you've got that\x01",
            "same kinda posture that Scherazard has.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0x101,
        (
            "#1008FAhaha, thanks.\x02\x03",

            "#1007FThough...this isn't really the time\x01",
            "to be swapping compliments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xC,
        "Yeah, good point.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xC,
        (
            "I'm guessing you guys\x01",
            "found a way down here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #322
        0x102,
        (
            "#1042F#2PWe did. Get back to the elevator shaft.\x02\x03",

            "If you go now, you SHOULD be\x01",
            "able to avoid any monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0xC,
        "#3PRight, got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xC,
        (
            "You guys be careful down here, too.\x01",
            "This place is crawling!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8407():
        OP_6D(97510, 0, 28150, 2000)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8407)

    def lambda_841F():
        OP_8F(0xFE, 0x17A3E, 0xFFFFFFF6, 0x6CF2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_841F)

    def lambda_843A():

        label("loc_843A")

        TurnDirection(0xFE, 0xC, 400)
        OP_48()
        Jump("loc_843A")

    QueueWorkItem2(0x101, 1, lambda_843A)
    OP_8E(0xC, 0x1845C, 0x0, 0x696E, 0xFA0, 0x0)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_8E(0xC, 0x1A838, 0x0, 0x6AF4, 0xFA0, 0x0)
    OP_44(0x101, 0x1)
    SetChrPos(0xC, 124780, 0, 74190, 180)
    OP_4B(0xC, 255)
    OP_A2(0x208B)
    OP_28(0xBF, 0x1, 0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8561")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as saved all three groups\x01",      # 0
            "No change\x01",                          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_850E"),
        (SWITCH_DEFAULT, "loc_8561"),
    )


    label("loc_850E")

    OP_A2(0x2089)
    OP_A2(0x208A)
    OP_A2(0x208B)
    OP_A2(0x208C)
    SetChrPos(0xA, 131940, 0, 69900, 315)
    SetChrPos(0xB, 130930, 0, 68610, 45)
    SetChrPos(0xC, 124780, 0, 74190, 180)
    SetChrPos(0xD, 126540, 0, 75140, 180)
    Jump("loc_8561")

    label("loc_8561")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_85FE")
    OP_A2(0x1)
    Fade(500)
    OP_6D(95210, -440, 28870, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(22000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 95750, -310, 28080, 315)
    SetChrPos(0x102, 94440, -500, 28540, 45)
    SetChrPos(0xF8, 96210, -160, 29110, 225)
    SetChrPos(0xF9, 94950, -500, 29820, 135)
    OP_0D()
    Call(0, 33)

    label("loc_85FE")

    EventEnd(0x0)
    Return()

    # Function_24_795F end

    def Function_25_8601(): pass

    label("Function_25_8601")

    SetChrPos(0xFE, 106130, 0, 27510, 45)
    OP_8E(0xFE, 0x184F2, 0x0, 0x69A0, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_25_8601 end

    def Function_26_862E(): pass

    label("Function_26_862E")

    SetChrPos(0xFE, 106130, 0, 27510, 45)
    OP_8E(0xFE, 0x181B4, 0x0, 0x66D0, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_26_862E end

    def Function_27_865B(): pass

    label("Function_27_865B")

    SetChrPos(0xFE, 106130, 0, 27510, 45)
    OP_8E(0xFE, 0x189A2, 0x0, 0x67A2, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_27_865B end

    def Function_28_8688(): pass

    label("Function_28_8688")

    SetChrPos(0xFE, 106130, 0, 27510, 45)
    OP_8E(0xFE, 0x184C0, 0x0, 0x62C0, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_28_8688 end

    def Function_29_86B5(): pass

    label("Function_29_86B5")

    OP_8E(0xFE, 0x16C1A, 0xFFFFFEB6, 0x70DA, 0x7D0, 0x0)
    TurnDirection(0x12, 0xC, 400)
    Return()

    # Function_29_86B5 end

    def Function_30_86D1(): pass

    label("Function_30_86D1")

    OP_8E(0xF8, 0x1766A, 0xFFFFFEFC, 0x7422, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_30_86D1 end

    def Function_31_86ED(): pass

    label("Function_31_86ED")

    OP_8E(0xF9, 0x170C0, 0xFFFFFEC0, 0x7580, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_31_86ED end

    def Function_32_8709(): pass

    label("Function_32_8709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8716")
    Return()

    label("loc_8716")

    EventBegin(0x0)
    Fade(500)
    OP_4A(0xD, 255)
    SetChrPos(0xD, 83170, -500, 10620, 90)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x10, 86220, -500, 12400, 270)
    SetChrPos(0x11, 87000, -500, 11330, 270)
    SetChrPos(0x12, 86950, -500, 9870, 270)
    SetChrPos(0x13, 86220, -500, 8710, 270)
    SetChrChipByIndex(0x10, 2)
    SetChrChipByIndex(0x11, 2)
    SetChrChipByIndex(0x12, 2)
    SetChrChipByIndex(0x13, 2)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8804")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8842")

    label("loc_8804")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_882B")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8842")

    label("loc_882B")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8842")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8869")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_88A7")

    label("loc_8869")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8890")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_88A7")

    label("loc_8890")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_88A7")

    TurnDirection(0x0, 0xD, 0)
    TurnDirection(0x1, 0xD, 0)
    TurnDirection(0x2, 0xD, 0)
    TurnDirection(0x3, 0xD, 0)
    Sleep(1000)

    ChrTalk(    #325
        0x101,
        "#1020FOh, no!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0x102,
        "#1044FThat's...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)

    def lambda_88FC():
        OP_6D(83130, -340, 10670, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_88FC)
    OP_6C(315000, 0)
    OP_0D()
    OP_43(0xD, 0x0, 0x0, 0x2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)

    def lambda_8941():
        OP_94(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8941)
    Sleep(120)

    def lambda_895C():
        OP_94(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_895C)
    Sleep(100)

    def lambda_8977():
        OP_94(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8977)
    Sleep(150)
    OP_94(0x0, 0x13, 0x0, 0x2BC, 0x3E8, 0x0)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_89B3():
        OP_91(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_89B3)
    Sleep(150)
    Sleep(50)

    def lambda_89D8():
        OP_94(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_89D8)
    Sleep(100)

    def lambda_89F3():
        OP_94(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_89F3)
    Sleep(100)

    def lambda_8A0E():
        OP_94(0x0, 0xFE, 0x0, 0x2BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8A0E)
    Sleep(120)
    OP_94(0x0, 0x13, 0x0, 0x2BC, 0x3E8, 0x0)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_8A4A():
        OP_91(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8A4A)
    Sleep(200)

    def lambda_8A6A():
        OP_94(0x0, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_8A6A)
    Sleep(100)

    def lambda_8A85():
        OP_94(0x0, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8A85)
    Sleep(120)

    def lambda_8AA0():
        OP_94(0x0, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_8AA0)
    Sleep(100)

    def lambda_8ABB():
        OP_94(0x0, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_8ABB)
    Sleep(200)

    def lambda_8AD6():
        OP_91(0xFE, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8AD6)
    WaitChrThread(0xD, 0x1)
    OP_4A(0xD, 255)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)
    WaitChrThread(0x12, 0x1)
    WaitChrThread(0x13, 0x1)
    Sleep(400)

    ChrTalk(    #327
        0xD,
        "Son of a...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xD,
        (
            "Well, it was a good plan, up to 'get\x01",
            "all the monsters to chase me here'...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 45, 400)
    Sleep(400)
    OP_8C(0xD, 135, 400)
    Sleep(400)
    OP_8C(0xD, 90, 400)
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #329
        0xD,
        "Aw, hell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xD,
        (
            "Looks like I might've\x01",
            "overdone it again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xD,
        "Anya, Frissa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xD,
        (
            "I'm sorry... I guess I won't\x01",
            "be coming home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #333
        0x101,
        "Gaton!\x02",
    )

    CloseMessageWindow()
    Sleep(400)
    AddParty(0x32, 0xFF, 0xFF)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrPos(0x101, 94580, -350, 10790, 5000)
    SetChrPos(0x102, 94510, -390, 9750, 5000)
    SetChrPos(0xF8, 95840, -240, 10950, 5000)
    SetChrPos(0xF9, 95640, -410, 9340, 5000)

    def lambda_8CB7():
        OP_6D(84450, -500, 10830, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8CB7)

    def lambda_8CCF():
        OP_8E(0xFE, 0x1561C, 0xFFFFFEA2, 0x2A26, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8CCF)
    Sleep(300)

    def lambda_8CEF():
        OP_8E(0xFE, 0x155D6, 0xFFFFFE7A, 0x2616, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8CEF)
    Sleep(200)

    def lambda_8D0F():
        OP_8E(0xFE, 0x15CFC, 0xFFFFFF10, 0x2AC6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_8D0F)
    Sleep(40)
    OP_8E(0xF9, 0x15C34, 0xFFFFFE66, 0x247C, 0x1388, 0x0)
    Sleep(1000)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #334
        0xD,
        "Estelle Bright?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x101,
        (
            "#1005F#2PDon't worry!\x01",
            "We'll save you!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DFB")

    ChrTalk(    #336
        0x108,
        (
            "#076FWe won't make it fighting normally.\x02\x03",

            "We must carve a path straight\x01",
            "through their ranks!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EC7")

    label("loc_8DFB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8E64")

    ChrTalk(    #337
        0x106,
        (
            "#054FWe won't save him fightin' normally.\x02\x03",

            "C'mon! We'll slice a path right to him!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8EC7")

    label("loc_8E64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8EC7")

    ChrTalk(    #338
        0x103,
        (
            "#024FWe can't just fight them off normally.\x02\x03",

            "We'll break through them!\x01",
            "Come on!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8EC7")


    ChrTalk(    #339
        0x102,
        "#1046F#2PForward!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F02")

    ChrTalk(    #340
        0x107,
        "#062FHere we go!\x02",
    )

    CloseMessageWindow()

    label("loc_8F02")


    def lambda_8F08():
        OP_90(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F08)

    def lambda_8F23():
        OP_90(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8F23)

    def lambda_8F3E():
        OP_90(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_8F3E)

    def lambda_8F59():
        OP_90(0xFE, 0xFFFFFA88, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_8F59)
    Sleep(200)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF9, 0xFF)
    Battle(0xEDA, 0x300018, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    EventBegin(0x0)
    RemoveParty(0x32, 0xFF)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    OP_6D(82190, -500, 10990, 0)
    OP_67(0, 8109, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 84100, -500, 10790, 90)
    SetChrPos(0x102, 84110, -410, 9850, 90)
    SetChrPos(0xF8, 83380, -470, 11670, 90)
    SetChrPos(0xF9, 83620, -180, 8820, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #341
        0x101,
        (
            "#1007F#5POkay...\x01",
            "We...somehow...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x102,
        "#1043F#5P...We managed to win, it seems.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_90F5")

    ChrTalk(    #343
        0x107,
        "#561FHaah, haah... My heart's racing...\x02",
    )

    CloseMessageWindow()

    label("loc_90F5")

    SetChrChipByIndex(0xF8, 65535)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)

    def lambda_910F():

        label("loc_910F")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_910F")

    QueueWorkItem2(0xF8, 1, lambda_910F)

    def lambda_9120():

        label("loc_9120")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_9120")

    QueueWorkItem2(0xF9, 1, lambda_9120)
    Sleep(200)
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)

    def lambda_914A():

        label("loc_914A")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_914A")

    QueueWorkItem2(0x101, 1, lambda_914A)

    def lambda_915B():

        label("loc_915B")

        TurnDirection(0xFE, 0xD, 400)
        OP_48()
        Jump("loc_915B")

    QueueWorkItem2(0x102, 1, lambda_915B)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91A0")

    ChrTalk(    #344
        0x103,
        "#020FGaton, are you all right?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9201")

    label("loc_91A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_91D1")

    ChrTalk(    #345
        0x106,
        "#051FYou all right, chief?\x02",
    )

    CloseMessageWindow()
    Jump("loc_9201")

    label("loc_91D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9201")

    ChrTalk(    #346
        0x108,
        "#070FAre you all right, sir?\x02",
    )

    CloseMessageWindow()

    label("loc_9201")


    ChrTalk(    #347
        0xD,
        "Yeah... Just scratches, is all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xD,
        (
            "Man, they really must teach you guys\x01",
            "to have perfect timing at Bracer School\x01",
            "or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xD,
        (
            "Wish you could stop by when we're\x01",
            "not in the middle of a damned crisis!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x101,
        (
            "#1016FHaha! Yeah, really.\x02\x03",

            "Seems like the only time we ever come by\x01",
            "the mines is when there's an emergency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x102,
        (
            "#1048FIt would be nice to visit once\x01",
            "without being in mortal danger.\x02\x03",

            "#1035FStill, there will be time for\x01",
            "joking later.\x02\x03",

            "We need you to get to safety\x01",
            "first, Mr. Gaton.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0xD,
        "Ah, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x101,
        (
            "#1002FWe're getting everyone to go meet\x01",
            "Trent and Landan over by the elevator.\x02\x03",

            "Head over there for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0xD,
        "Right, I'll do that.\x02",
    )

    CloseMessageWindow()

    def lambda_948F():
        OP_6D(84620, -500, 10450, 1500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_948F)
    OP_8E(0xD, 0x1417C, 0xFFFFFEF2, 0x2EC2, 0xBB8, 0x0)
    OP_8E(0xD, 0x144EC, 0xFFFFFE48, 0x316A, 0xBB8, 0x0)
    OP_8E(0xD, 0x15158, 0xFFFFFE0C, 0x3070, 0xBB8, 0x0)
    OP_8E(0xD, 0x15842, 0xFFFFFE0C, 0x2742, 0xBB8, 0x0)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xD, 0x101, 400)
    Sleep(500)

    ChrTalk(    #355
        0xD,
        "Oh... One other thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0xD,
        (
            "That other bracer who came\x01",
            "to run guard duty for us...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xD,
        "Have you found him already?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x101,
        "#1026F#3PRidge? Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0x102,
        (
            "#1043F#3PNo, unfortunately.\x02\x03",

            "We haven't come across him yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0xD,
        (
            "I was afraid of that.\x02\x03",

            "If you haven't seen him, head\x01",
            "to the construction site.\x02\x03",

            "We last saw Ridge trying to\x01",
            "buy us some time there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        "#1002F#3P...Okay. Thanks.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_96CE")

    ChrTalk(    #362
        0x108,
        "#072FMmm... We'll keep that in mind.\x02",
    )

    CloseMessageWindow()
    Jump("loc_974B")

    label("loc_96CE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9708")

    ChrTalk(    #363
        0x106,
        "#050FYeah, we'll keep that in mind.\x02",
    )

    CloseMessageWindow()
    Jump("loc_974B")

    label("loc_9708")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_974B")

    ChrTalk(    #364
        0x103,
        (
            "#022FWe'll keep that in mind, Gaton.\x01",
            "Thank you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_974B")


    def lambda_9751():
        OP_6D(90550, -420, 10520, 1500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_9751)
    OP_8E(0xD, 0x18E16, 0x0, 0x2BCA, 0xBB8, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    SetChrPos(0xD, 126540, 0, 75140, 180)
    OP_4B(0xD, 255)
    OP_A2(0x208C)
    OP_28(0xBF, 0x1, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_986B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as saved all three groups\x01",      # 0
            "No change\x01",                          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9818"),
        (SWITCH_DEFAULT, "loc_986B"),
    )


    label("loc_9818")

    OP_A2(0x2089)
    OP_A2(0x208A)
    OP_A2(0x208B)
    OP_A2(0x208C)
    SetChrPos(0xA, 131940, 0, 69900, 315)
    SetChrPos(0xB, 130930, 0, 68610, 45)
    SetChrPos(0xC, 124780, 0, 74190, 180)
    SetChrPos(0xD, 126540, 0, 75140, 180)
    Jump("loc_986B")

    label("loc_986B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9908")
    OP_A2(0x2)
    Fade(500)
    OP_6D(82850, -460, 10740, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 83690, -500, 10780, 270)
    SetChrPos(0x102, 82740, -440, 11720, 180)
    SetChrPos(0xF8, 82930, -430, 9940, 0)
    SetChrPos(0xF9, 82130, -280, 10740, 90)
    OP_0D()
    Call(0, 33)

    label("loc_9908")

    EventEnd(0x0)
    Return()

    # Function_32_8709 end

    def Function_33_990B(): pass

    label("Function_33_990B")

    EventBegin(0x0)

    ChrTalk(    #365
        0x101,
        "#1002FOkay...that should be everyone, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x102,
        (
            "#1040FYes, we've saved all of\x01",
            "the miners, I believe.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_99EA")

    ChrTalk(    #367
        0x103,
        (
            "#026FIn that case, all that's left is Ridge.\x02\x03",

            "#522FWe haven't...seen any trace of him yet.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE0")

    label("loc_99EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9A4E")

    ChrTalk(    #368
        0x106,
        (
            "#552FThat leaves just Ridge, then.\x02\x03",

            "Didn't notice any...trace of him earlier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AE0")

    label("loc_9A4E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9AE0")

    ChrTalk(    #369
        0x108,
        (
            "#072FThe only one remaining is\x01",
            "our brother bracer, Ridge.\x02\x03",

            "I did not see any trace of him while\x01",
            "we were rescuing the others...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AE0")


    ChrTalk(    #370
        0x101,
        (
            "#1002FGaton said he last saw Ridge\x01",
            "by the construction site.\x02\x03",

            "He said Ridge was covering their\x01",
            "escape...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9BB3")

    ChrTalk(    #371
        0x106,
        (
            "#050FWe got no time to be talkin'.\x02\x03",

            "Let's get over there before it's too late.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C43")

    label("loc_9BB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9BF8")

    ChrTalk(    #372
        0x108,
        (
            "#072FLet's hurry.\x02\x03",

            "We may already be too late.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C43")

    label("loc_9BF8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9C43")

    ChrTalk(    #373
        0x103,
        (
            "#022FLet's hurry, then.\x02\x03",

            "Oh, Aidios, let us be in time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D1D")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as rescued Pierre, Heinrich last\x01",      # 0
            "Set as rescued Bones last\x01",                 # 1
            "Set as rescued Gaton last\x01",                 # 2
            "No change\x01",                                 # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9CF9"),
        (1, "loc_9D05"),
        (2, "loc_9D11"),
        (SWITCH_DEFAULT, "loc_9D1D"),
    )


    label("loc_9CF9")

    OP_A2(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    Jump("loc_9D1D")

    label("loc_9D05")

    OP_A3(0x0)
    OP_A2(0x1)
    OP_A3(0x2)
    Jump("loc_9D1D")

    label("loc_9D11")

    OP_A3(0x0)
    OP_A3(0x1)
    OP_A2(0x2)
    Jump("loc_9D1D")

    label("loc_9D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9D68")
    OP_A3(0x0)

    ChrTalk(    #374
        0x102,
        (
            "#1042FThe construction site should\x01",
            "be northwest of here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DF3")

    label("loc_9D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9DAF")
    OP_A3(0x2)

    ChrTalk(    #375
        0x102,
        (
            "#1042FThe construction site should\x01",
            "be north of here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9DF3")

    label("loc_9DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_9DF3")
    OP_A3(0x1)

    ChrTalk(    #376
        0x102,
        (
            "#1042FThe construction site should\x01",
            "be north of here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9DF3")


    ChrTalk(    #377
        0x101,
        "#1002FLet's go, then!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x208D)
    OP_28(0xBF, 0x1, 0x80)
    OP_28(0xBF, 0x1, 0x100)
    Return()

    # Function_33_990B end

    def Function_34_9E1E(): pass

    label("Function_34_9E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 5)), scpexpr(EXPR_END)), "loc_A24C")
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A047")
    Fade(500)
    OP_6D(93490, -500, 66260, 0)
    SetChrPos(0x101, 93950, -260, 66700, 0)
    SetChrPos(0x102, 93090, -480, 66700, 0)
    SetChrPos(0xF8, 94220, -230, 65500, 0)
    SetChrPos(0xF9, 92880, -350, 65500, 0)
    OP_0D()

    ChrTalk(    #378
        0x101,
        "#1002FSo past here is the monster nest...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F03")

    ChrTalk(    #379
        0x106,
        (
            "#057FHells...\x02\x03",

            "You smell that?\x01",
            "Nothin' but monster.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FC6")

    label("loc_9F03")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9F4B")

    ChrTalk(    #380
        0x103,
        (
            "#523FUgh, this is hideous.\x02\x03",

            "It REEKS of monsters.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FC6")

    label("loc_9F4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9FC6")

    ChrTalk(    #381
        0x108,
        (
            "#072FMmmmm... This almost feels like a grave.\x02\x03",

            "The stench of monster is omnipresent\x01",
            "just standing here.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FC6")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #382
        0x102,
        (
            "#1042FWe won't be able to turn\x01",
            "back once we go in...\x02\x03",

            "Estelle. Are you sure our equipment\x01",
            "and everything is okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A120")

    label("loc_A047")

    Fade(500)
    OP_6D(93490, -500, 66260, 0)
    SetChrPos(0x101, 93950, -260, 66700, 0)
    SetChrPos(0x102, 93090, -480, 66700, 0)
    SetChrPos(0xF8, 94220, -230, 65500, 0)
    SetChrPos(0xF9, 92880, -350, 65500, 0)
    OP_0D()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #383
        0x102,
        (
            "#1042FEstelle. Are you sure we're properly\x01",
            "equipped and everything?\x02\x03",

            "We won't be able to turn\x01",
            "back once we go in.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A120")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Let's go!\x01",      # 0
            "Wait\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A176"),
        (1, "loc_A17D"),
        (SWITCH_DEFAULT, "loc_A249"),
    )


    label("loc_A176")

    Call(0, 35)
    Jump("loc_A249")

    label("loc_A17D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x411, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A217")
    OP_A2(0x208E)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #384
        0x101,
        (
            "#1015FWe should be okay, but...\x02\x03",

            "Might be a good idea to go\x01",
            "over everything one last time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #385
        0x102,
        "#1040FGood idea. Let's do that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A244")

    label("loc_A217")


    ChrTalk(    #386
        0x102,
        "#1040FYes, let's make sure we're ready.\x02",
    )

    CloseMessageWindow()

    label("loc_A244")

    EventEnd(0x0)
    Jump("loc_A249")

    label("loc_A249")

    Jump("loc_A3A1")

    label("loc_A24C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A31A")

    ChrTalk(    #387
        0x101,
        "#1025FThis is the monster nest, isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x102,
        (
            "#1042FWe should make sure we've rescued\x01",
            "all the miners before charging in there.\x02\x03",

            "There are still some unaccounted for.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x101,
        "#1002FRight.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x8)
    Jump("loc_A386")

    label("loc_A31A")


    ChrTalk(    #390
        0x101,
        (
            "#1002FSo this is the monster nest...\x02\x03",

            "We need to make sure the miners\x01",
            "are safe before we take this on.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A386")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_A3A1")

    Return()

    # Function_34_9E1E end

    def Function_35_A3A2(): pass

    label("Function_35_A3A2")

    TurnDirection(0x101, 0x102, 400)
    Sleep(500)

    ChrTalk(    #391
        0x101,
        (
            "#1006FOkay... We're as ready as\x01",
            "we'll ever be, I think.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x102,
        "#1042FLet's go, then!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)

    def lambda_A41A():
        OP_6D(95620, 0, 73830, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A41A)

    def lambda_A432():
        OP_8E(0xFE, 0x176CE, 0xFFFFFEA2, 0x1269C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A432)
    Sleep(200)

    def lambda_A452():
        OP_8E(0xFE, 0x176CE, 0xFFFFFEA2, 0x1269C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A452)
    Sleep(200)

    def lambda_A472():
        OP_8E(0xFE, 0x176CE, 0xFFFFFEA2, 0x1269C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_A472)
    Sleep(200)

    def lambda_A492():
        OP_8E(0xFE, 0x176CE, 0xFFFFFEA2, 0x1269C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_A492)
    Sleep(400)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0xF8, 0x1)
    OP_44(0xF9, 0x1)
    OP_44(0x101, 0x2)
    SetChrPos(0x101, 185820, -450, 52650, 0)
    SetChrPos(0x102, 185820, -450, 52650, 0)
    SetChrPos(0xF8, 185820, -450, 52650, 0)
    SetChrPos(0xF9, 185820, -450, 52650, 0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x10, 189500, -250, 70370, 180)
    SetChrPos(0x11, 190500, -250, 69540, 225)
    SetChrPos(0x12, 190400, -130, 68040, 315)
    SetChrPos(0x13, 188000, -250, 70370, 180)
    SetChrPos(0x14, 187000, -250, 69540, 135)
    SetChrPos(0x15, 186900, -130, 68040, 45)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x16, 188680, 0, 73010, 202)
    SetChrPos(0x17, 185450, 0, 71540, 139)
    SetChrPos(0x19, 191630, 0, 71750, 239)
    SetChrPos(0x1A, 193000, -130, 68420, 270)
    SetChrPos(0x1B, 184070, 0, 68530, 103)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_D2(0x90002, 0x90006, 0x7)
    OP_D2(0x7051D, 0x70524, 0x4)
    OP_D2(0x7051E, 0x70525, 0x5)
    SetChrChipByIndex(0xE, 5)
    SetChrSubChip(0xE, 3)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 188800, -250, 68950, 0)
    LoadEffect(0x1, "scraft\\\\sc000_11.eff")
    LoadEffect(0x2, "map\\\\mp023_00.eff")
    LoadEffect(0x3, "monster\\\\msc0550.eff")
    SoundLoad(287)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 12)
    SetChrChipByIndex(0xF8, 14)
    SetChrChipByIndex(0xF9, 16)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x102, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x10, 2)
    SetChrChipByIndex(0x11, 2)
    SetChrChipByIndex(0x12, 2)
    SetChrChipByIndex(0x13, 2)
    SetChrChipByIndex(0x14, 2)
    SetChrChipByIndex(0x15, 2)
    OP_43(0x10, 0x0, 0x0, 0x2)
    OP_43(0x11, 0x0, 0x0, 0x2)
    OP_43(0x12, 0x0, 0x0, 0x2)
    OP_43(0x13, 0x0, 0x0, 0x2)
    OP_43(0x14, 0x0, 0x0, 0x2)
    OP_43(0x15, 0x0, 0x0, 0x2)
    SetChrChipByIndex(0x16, 2)
    SetChrChipByIndex(0x17, 2)
    SetChrChipByIndex(0x18, 2)
    SetChrChipByIndex(0x19, 2)
    SetChrChipByIndex(0x1A, 2)
    SetChrChipByIndex(0x1B, 2)
    OP_43(0x16, 0x0, 0x0, 0x2)
    OP_43(0x17, 0x0, 0x0, 0x2)
    OP_43(0x18, 0x0, 0x0, 0x2)
    OP_43(0x19, 0x0, 0x0, 0x2)
    OP_43(0x1A, 0x0, 0x0, 0x2)
    OP_43(0x1B, 0x0, 0x0, 0x2)
    OP_20(0x3E8)
    Sleep(1000)
    OP_21()
    OP_1D(0x56)
    Sleep(1000)
    OP_6D(199700, 110, 73850, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(107000, 0)
    OP_6E(262, 0)

    def lambda_A7C1():
        OP_6D(188900, -250, 69050, 5000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A7C1)

    def lambda_A7D9():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_A7D9)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0xD, 0x1)

    ChrTalk(    #393
        0xE,
        "#4PUg-uggghh...\x02",
    )

    CloseMessageWindow()

    def lambda_A80D():

        label("loc_A80D")

        OP_9E(0xFE, 0x32, 0x0, 0x3E8, 0x7D0)
        OP_48()
        Jump("loc_A80D")

    QueueWorkItem2(0xE, 1, lambda_A80D)
    OP_99(0xE, 0x3, 0x0, 0x258)
    OP_44(0xE, 0x1)
    SetChrChipByIndex(0xE, 6)
    OP_43(0x13, 0x1, 0x0, 0x24)
    Sleep(200)
    OP_43(0x10, 0x1, 0x0, 0x25)
    Sleep(500)

    def lambda_A854():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A854)

    def lambda_A862():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_A862)

    def lambda_A870():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_A870)

    def lambda_A87E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_A87E)
    Sleep(200)

    def lambda_A891():

        label("loc_A891")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_A891")

    QueueWorkItem2(0x16, 1, lambda_A891)

    def lambda_A8A2():

        label("loc_A8A2")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_A8A2")

    QueueWorkItem2(0x17, 1, lambda_A8A2)

    def lambda_A8B3():

        label("loc_A8B3")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_A8B3")

    QueueWorkItem2(0x18, 1, lambda_A8B3)

    def lambda_A8C4():

        label("loc_A8C4")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_A8C4")

    QueueWorkItem2(0x19, 1, lambda_A8C4)

    def lambda_A8D5():

        label("loc_A8D5")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_A8D5")

    QueueWorkItem2(0x1A, 1, lambda_A8D5)

    def lambda_A8E6():

        label("loc_A8E6")

        TurnDirection(0xFE, 0xE, 400)
        OP_48()
        Jump("loc_A8E6")

    QueueWorkItem2(0x1B, 1, lambda_A8E6)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0xE, 0x1)
    OP_44(0x16, 0x1)
    OP_44(0x17, 0x1)
    OP_44(0x18, 0x1)
    OP_44(0x19, 0x1)
    OP_44(0x1A, 0x1)
    OP_44(0x1B, 0x1)

    ChrTalk(    #394
        0xE,
        "Agh!\x02",
    )

    CloseMessageWindow()

    def lambda_A923():

        label("loc_A923")

        OP_9E(0xFE, 0x32, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_A923")

    QueueWorkItem2(0xE, 1, lambda_A923)
    Sleep(200)
    OP_99(0xE, 0x3, 0x0, 0x12C)
    Sleep(200)
    OP_44(0xE, 0x1)
    SetChrChipByIndex(0xE, 6)

    ChrTalk(    #395
        0xE,
        "Uuuuuhhh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x101,
        "#5PRidge!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A996")

    ChrTalk(    #397
        0x103,
        "#1PRIDGE!\x02",
    )

    CloseMessageWindow()
    Jump("loc_A9B2")

    label("loc_A996")


    ChrTalk(    #398
        0x102,
        "#1PAre you all right?!\x02",
    )

    CloseMessageWindow()

    label("loc_A9B2")

    OP_44(0xE, 0x3)
    OP_43(0x101, 0x1, 0x0, 0x27)
    OP_43(0x101, 0x2, 0x0, 0x2B)
    Sleep(500)
    OP_43(0x102, 0x1, 0x0, 0x28)
    Sleep(500)
    OP_43(0xF8, 0x1, 0x0, 0x29)
    Sleep(500)
    OP_43(0xF9, 0x1, 0x0, 0x2A)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AAB3")

    ChrTalk(    #399
        0xE,
        "Who... Estelle? Schera?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xE,
        "What're you...doin' here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x103,
        (
            "#524FRidge, don't worry, you fought well.\x02\x03",

            "You've done enough. Just relax.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x102,
        "#1042FLeave the rest to us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AB50")

    label("loc_AAB3")


    ChrTalk(    #403
        0xE,
        "Who... Estelle? And...izzat Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0xE,
        "What're you...doin' here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #405
        0x101,
        "#1006FWe're here to help you out, of course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #406
        0x102,
        "#1042FLeave the rest to us.\x02",
    )

    CloseMessageWindow()

    label("loc_AB50")


    ChrTalk(    #407
        0xE,
        "#2PI get it... Cool...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0xE,
        (
            "B-But...be careful...\x01",
            "They don't just...\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 5)
    OP_22(0x20C, 0x0, 0x64)
    OP_99(0xE, 0x0, 0x3, 0x3E8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC00")
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #409
        0x108,
        (
            "#072FMmm...?\x02\x03",

            "#076FGh! Get back!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACA2")

    label("loc_AC00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AC54")
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #410
        0x106,
        (
            "#052FMm?\x02\x03",

            "#054FDAMN IT! Get back!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACA2")

    label("loc_AC54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ACA2")
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #411
        0x103,
        (
            "#022FTsk!\x02\x03",

            "Everyone! Get back!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ACA2")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_ACB1():
        OP_6D(188840, 720, 70020, 2000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_ACB1)

    def lambda_ACC9():
        OP_67(0, 3720, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_ACC9)

    def lambda_ACE1():
        OP_6B(2780, 2000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_ACE1)

    def lambda_ACF1():
        OP_6C(5000, 2000)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_ACF1)

    def lambda_AD01():
        OP_96(0xFE, 0x2E568, 0x0, 0xF15E, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_AD01)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(10)

    def lambda_AD29():
        OP_96(0xFE, 0x2D9A6, 0xFFFFFF7E, 0xF262, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_AD29)
    Sleep(100)

    def lambda_AD4C():
        OP_96(0xFE, 0x2E22A, 0xFFFFFF88, 0xF636, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AD4C)
    OP_22(0xA3, 0x0, 0x64)
    Sleep(10)

    def lambda_AD74():
        OP_96(0xFE, 0x2DDC0, 0xFFFFFF06, 0xF690, 0x1F4, 0x1B58)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AD74)
    WaitChrThread(0x102, 0x1)
    SetChrPos(0x1C, 188800, -250, 68950, 0)

    def lambda_ADA8():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_ADA8)

    def lambda_ADB6():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_ADB6)

    def lambda_ADC4():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_ADC4)

    def lambda_ADD2():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_ADD2)

    def lambda_ADE0():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_ADE0)

    def lambda_ADEE():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_ADEE)

    def lambda_ADFC():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_ADFC)

    def lambda_AE0A():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_AE0A)

    def lambda_AE18():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_AE18)

    def lambda_AE26():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_AE26)

    def lambda_AE34():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_AE34)

    def lambda_AE42():
        TurnDirection(0xFE, 0x1C, 400)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_AE42)
    Sleep(600)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x12, 0x10)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x15, 0x10)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0x13, 0x40)
    SetChrFlags(0x14, 0x40)
    SetChrFlags(0x15, 0x40)

    def lambda_AE91():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_AE91)

    def lambda_AEA7():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_AEA7)

    def lambda_AEBD():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_AEBD)

    def lambda_AED3():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_AED3)

    def lambda_AEE9():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_AEE9)

    def lambda_AEFF():
        OP_94(0x1, 0xFE, 0xB4, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_AEFF)

    def lambda_AF15():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_AF15)

    def lambda_AF2B():
        OP_8F(0xFE, 0x2D4F6, 0x0, 0x119FE, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_AF2B)

    def lambda_AF46():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_AF46)

    def lambda_AF5C():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_AF5C)

    def lambda_AF72():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_AF72)

    def lambda_AF88():
        OP_8F(0xFE, 0x2CF24, 0x0, 0x10C66, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_AF88)
    Sleep(100)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x4)
    SetChrFlags(0xF, 0x20)
    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 20)
    SetChrSubChip(0xF, 0)
    SetChrPos(0xF, 188800, 10000, 68950, 185)
    OP_8F(0xF, 0x2E180, 0xFFFFFEA2, 0x10D56, 0x4E20, 0x0)

    def lambda_AFFC():
        OP_9E(0xFE, 0x28, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_AFFC)
    OP_22(0x88, 0x0, 0x64)
    OP_7C(0x0, 0x7D0, 0x2710, 0x64)

    def lambda_B02C():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_B02C)

    def lambda_B04A():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_B04A)

    def lambda_B068():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_B068)

    def lambda_B086():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_B086)

    def lambda_B0A4():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_B0A4)

    def lambda_B0C2():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xFA0)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_B0C2)

    def lambda_B0E0():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_B0E0)

    def lambda_B0FE():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_B0FE)

    def lambda_B11C():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_B11C)

    def lambda_B13A():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_B13A)

    def lambda_B158():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0x12C, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_B158)

    def lambda_B176():
        OP_95(0xFE, 0x0, 0x0, 0x0, 0xC8, 0xFA0)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_B176)
    Sleep(100)
    PlayEffect(0x2, 0x0, 0xFF, 187810, -250, 68250, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    OP_82(0x0, 0x2)

    def lambda_B1D6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_B1D6)

    def lambda_B1E4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_B1E4)

    def lambda_B1F2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_B1F2)

    def lambda_B200():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x13, 3, lambda_B200)

    def lambda_B20E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_B20E)

    def lambda_B21C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_B21C)

    def lambda_B22A():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_B22A)

    def lambda_B238():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_B238)

    def lambda_B246():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_B246)

    def lambda_B254():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_B254)

    def lambda_B262():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_B262)

    def lambda_B270():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_B270)
    Sleep(1400)
    Fade(100)
    SetChrChipByIndex(0xF, 18)
    SetChrSubChip(0xF, 5)
    OP_99(0xF, 0x5, 0x1, 0x5DC)
    OP_22(0x11F, 0x0, 0x64)

    def lambda_B2A0():
        OP_6D(188840, -250, 68280, 3000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B2A0)

    def lambda_B2B8():
        OP_6B(3180, 3000)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_B2B8)

    def lambda_B2C8():
        OP_67(0, 4100, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_B2C8)
    OP_7C(0x12C, 0x0, 0x1770, 0x3E8)
    Sleep(1000)
    OP_7C(0xC8, 0x0, 0x1194, 0x3E8)
    Sleep(1000)
    OP_7C(0x64, 0x0, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xF, 18)
    SetChrSubChip(0xF, 0)
    Sleep(50)
    SetChrChipByIndex(0xF, 0)
    SetChrSubChip(0xF, 0)

    def lambda_B344():

        label("loc_B344")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B344")

    QueueWorkItem2(0xF, 0, lambda_B344)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B378")

    ChrTalk(    #412
        0x107,
        "#065F#5PWaaaaaaaah!\x02",
    )

    CloseMessageWindow()

    label("loc_B378")


    ChrTalk(    #413
        0x101,
        "#1005F#5PWhat in the hell?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B3C7")

    ChrTalk(    #414
        0x106,
        "#550F#5POh, like I'd know!\x02",
    )

    CloseMessageWindow()

    label("loc_B3C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B409")

    ChrTalk(    #415
        0x103,
        (
            "#023F#5PThe pack leader of the\x01",
            "nest, possibly.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B409")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B44D")

    ChrTalk(    #416
        0x108,
        (
            "#070F#5PHaha! It's a strong foe,\x01",
            "whatever it is!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B44D")


    ChrTalk(    #417
        0x102,
        (
            "#1043F#5PRegardless of WHAT it is...\x02\x03",

            "It clearly doesn't like us\x01",
            "being here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x101,
        "#1020F#5PUh oh...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B4E6")

    ChrTalk(    #419
        0x103,
        "#024F#5PEstelle! Come on!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B552")

    label("loc_B4E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B519")

    ChrTalk(    #420
        0x108,
        "#076F#5PEveryone, to battle!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B552")

    label("loc_B519")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B552")

    ChrTalk(    #421
        0x106,
        "#054F#5PAll right, let's carve it up!\x02",
    )

    CloseMessageWindow()

    label("loc_B552")

    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_44(0xF, 0x0)
    SetChrChipByIndex(0xF, 0)
    SetChrSubChip(0xF, 1)
    OP_22(0x23B, 0x0, 0x64)

    def lambda_B574():
        OP_96(0xF, 0x2DFC8, 0xFFFFFF06, 0xFC80, 0x5DC, 0x1B58)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_B574)

    def lambda_B592():
        OP_99(0xFE, 0x1, 0x3, 0x5DC)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_B592)

    def lambda_B5A2():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_B5A2)

    def lambda_B5B7():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_B5B7)

    def lambda_B5CC():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B5CC)

    def lambda_B5E1():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_B5E1)

    def lambda_B5F6():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_B5F6)

    def lambda_B60B():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B60B)

    def lambda_B620():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_B620)

    def lambda_B635():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_B635)

    def lambda_B64A():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B64A)

    def lambda_B65F():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_B65F)

    def lambda_B674():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_B674)

    def lambda_B689():
        OP_92(0xFE, 0xE, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_B689)
    Sleep(300)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xF8, 0xFF)
    OP_44(0xE, 0xFF)
    Battle(0xEDB, 0x0, 0x0, 0x0, 0xFF)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_B707"),
        (SWITCH_DEFAULT, "loc_B70C"),
    )


    label("loc_B707")

    OP_B4(0x0)
    Jump("loc_B70C")

    label("loc_B70C")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_6D(189040, -250, 72180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_D2(0x7051E, 0x70525, 0x5)
    SetChrPos(0x101, 188750, -150, 63910, 0)
    SetChrPos(0x102, 187450, -250, 64030, 0)
    SetChrPos(0xF8, 189850, 0, 63000, 0)
    SetChrPos(0xF9, 186360, -140, 63140, 0)
    SetChrChipByIndex(0xE, 5)
    SetChrSubChip(0xE, 3)
    SetChrPos(0xE, 187650, 0, 60830, 0)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x14, 0xFF)
    OP_44(0x15, 0xFF)
    OP_44(0x16, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1A, 0xFF)
    OP_44(0x1B, 0xFF)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)

    def lambda_B839():
        OP_6D(189040, -250, 65180, 4000)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B839)
    FadeToBright(1000, 0)
    WaitChrThread(0xE, 0x1)

    ChrTalk(    #422
        0x101,
        "#1021F#6PO-Okay... It's dead...right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x102,
        "#1042F#6PI'm...pretty sure it is, yeah.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B8E2")

    ChrTalk(    #424
        0x107,
        "#561FThat was so scaaaaary...\x02",
    )

    CloseMessageWindow()

    label("loc_B8E2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B944")

    ChrTalk(    #425
        0x103,
        (
            "#026FEverything else has gone quiet...\x02\x03",

            "Looks like that takes care of that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA12")

    label("loc_B944")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B9A9")

    ChrTalk(    #426
        0x108,
        (
            "#070FI don't sense any other monsters\x01",
            "nearby.\x02\x03",

            "We've driven them off, I think!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BA12")

    label("loc_B9A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BA12")

    ChrTalk(    #427
        0x106,
        (
            "#050FDon't hear any other monsters\x01",
            "scurryin' around...\x02\x03",

            "Think that drove 'em all off.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA12")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_22(0xD5, 0x0, 0x64)
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #428
        0x101,
        "#1004F#6POh, crap! How's Ridge?!\x02",
    )

    CloseMessageWindow()

    def lambda_BA70():
        OP_6D(188340, 0, 61600, 1500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_BA70)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF8, 0)

    def lambda_BA92():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_BA92)
    Sleep(50)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)

    def lambda_BAAF():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BAAF)
    Sleep(50)
    SetChrChipByIndex(0xF9, 65535)
    SetChrSubChip(0xF9, 0)

    def lambda_BACC():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_BACC)
    Sleep(700)
    WaitChrThread(0xE, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB22")

    ChrTalk(    #429
        0x103,
        (
            "#027FHe's all right...\x01",
            "He's just unconscious.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB5F")

    label("loc_BB22")


    ChrTalk(    #430
        0x102,
        (
            "#1040FI think he's just so tired he\x01",
            "lost consciousness.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBB4")

    ChrTalk(    #431
        0x107,
        (
            "#065FWe really need to get him back\x01",
            "to town, though! Or, or...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC83")

    label("loc_BBB4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC20")

    ChrTalk(    #432
        0x108,
        (
            "#070FWe should carry him back\x01",
            "to Rolent.\x02\x03",

            "He'll still need some rest,\x01",
            "after all this.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC83")

    label("loc_BC20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC83")

    ChrTalk(    #433
        0x106,
        (
            "#552FWe should get him back to town.\x02\x03",

            "After somethin' like this, he needs rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC83")


    ChrTalk(    #434
        0x101,
        "#1000FYeah, absolutely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0x102,
        (
            "#1040FLet's get back to the elevator and\x01",
            "get everyone to the surface, then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD1B")

    ChrTalk(    #436
        0x103,
        "#020FYes, let's go.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD70")

    label("loc_BD1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD45")

    ChrTalk(    #437
        0x106,
        "#051FLet's move it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD70")

    label("loc_BD45")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BD70")

    ChrTalk(    #438
        0x108,
        "#070FCome on! Let's go.\x02",
    )

    CloseMessageWindow()

    label("loc_BD70")

    FadeToDark(2000, 0, -1)
    OP_0D()
    EventBegin(0x0)

    AnonymousTalk(    #439
        (
            "\x07\x05And so the crisis in the Malga Mine stemming\x01",
            "from the orbal shutdown phenomenon ended safely.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_6D(53610, 0, 51680, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_D2(0x7051E, 0x70525, 0x7)
    OP_D2(0x70109, 0x7010D, 0x8)
    SetChrChipByIndex(0xD, 8)
    SetChrPos(0xA, 53220, 0, 52940, 0)
    SetChrPos(0xB, 51880, 0, 53800, 0)
    SetChrPos(0x8, 53210, 0, 54100, 90)
    SetChrPos(0xD, 55190, 0, 54000, 180)
    SetChrPos(0xC, 55250, 0, 51960, 0)
    SetChrPos(0x9, 56100, 0, 52360, 0)
    TurnDirection(0xC, 0x9, 0)
    TurnDirection(0x9, 0xC, 0)
    TurnDirection(0xB, 0xA, 0)
    TurnDirection(0xA, 0xB, 0)
    SetChrChipByIndex(0xE, 7)
    SetChrSubChip(0xE, 3)
    ClearChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x20)
    OP_6F(0x1, 55)
    OP_48()
    OP_89(0x101, 54600, -4530, 57510, 180)
    OP_89(0x102, 53690, -4530, 57700, 0)
    OP_89(0xF8, 54620, -4530, 56530, 180)
    OP_89(0xF9, 53370, -4530, 57200, 180)
    OP_89(0xE, 53400, -4530, 56550, 180)
    FadeToBright(2000, 0)
    Sleep(2000)
    OP_43(0xD, 0x1, 0x0, 0x2C)
    OP_6D(54140, 0, 54820, 2000)
    Sleep(200)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 65)
    OP_70(0x1, 0x37)
    OP_73(0x1)
    Sleep(500)
    Sleep(200)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 55)
    OP_70(0x1, 0x2D)
    OP_73(0x1)
    Sleep(500)
    Sleep(200)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 45)
    OP_70(0x1, 0x23)
    OP_73(0x1)
    Sleep(500)
    Sleep(200)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 25)
    OP_70(0x1, 0xF)
    OP_73(0x1)
    Sleep(500)
    Sleep(200)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0xC8, 0xBB8, 0x12C)
    OP_6F(0x1, 15)
    OP_70(0x1, 0x0)
    OP_73(0x1)
    OP_62(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(120)
    OP_62(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_63(0xA)
    OP_63(0xB)
    OP_63(0x8)
    OP_63(0xD)
    OP_63(0xC)
    OP_63(0x9)

    AnonymousTalk(    #440
        (
            "\x07\x05After returning to the surface and celebrating\x01",
            "their escape with the miners...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #441
        (
            "\x07\x05Estelle's group carried on to town with Gaton to\x01",
            "bring Ridge home and report their success.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T0121   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_35_A3A2 end

    def Function_36_C1B1(): pass

    label("Function_36_C1B1")

    SetChrChipByIndex(0xFE, 7)

    def lambda_C1BC():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C1BC)

    def lambda_C1CC():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_C1CC)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xE, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 0x2)

    def lambda_C221():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_C221)
    SetChrChipByIndex(0xFE, 2)
    Return()

    # Function_36_C1B1 end

    def Function_37_C237(): pass

    label("Function_37_C237")

    SetChrChipByIndex(0xFE, 7)

    def lambda_C242():
        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C242)

    def lambda_C252():
        OP_94(0x1, 0xFE, 0x0, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_C252)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xE, 0, 500, 300, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0xE, 0x1, 0x0, 0x26)
    WaitChrThread(0xFE, 0x2)

    def lambda_C2AE():
        OP_94(0x1, 0xFE, 0xB4, 0x1F4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_C2AE)
    SetChrChipByIndex(0xFE, 2)
    Return()

    # Function_37_C237 end

    def Function_38_C2C4(): pass

    label("Function_38_C2C4")

    OP_6A(0xE)
    SetChrChipByIndex(0xE, 4)
    SetChrPos(0x1C, 188900, -250, 69050, 0)
    OP_96(0xFE, 0x2DD02, 0x0, 0xED9E, 0x1F4, 0x1388)
    OP_9E(0xFE, 0x96, 0x0, 0x190, 0xFA0)
    SetChrChipByIndex(0xE, 5)
    SetChrSubChip(0xFE, 3)
    OP_6A(0xFF)
    Return()

    # Function_38_C2C4 end

    def Function_39_C315(): pass

    label("Function_39_C315")

    OP_8E(0xFE, 0x2D492, 0x3C, 0xEBC8, 0x1388, 0x0)
    OP_8E(0xFE, 0x2E22A, 0xFFFFFF88, 0xFA1E, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_39_C315 end

    def Function_40_C34A(): pass

    label("Function_40_C34A")

    OP_8E(0xFE, 0x2D492, 0x3C, 0xEBC8, 0x1388, 0x0)
    OP_8E(0xFE, 0x2DDC0, 0xFFFFFF06, 0xFA78, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_40_C34A end

    def Function_41_C37F(): pass

    label("Function_41_C37F")

    OP_8E(0xFE, 0x2D492, 0x3C, 0xEBC8, 0x1388, 0x0)
    OP_8E(0xFE, 0x2E43C, 0x0, 0xF546, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_41_C37F end

    def Function_42_C3B4(): pass

    label("Function_42_C3B4")

    OP_8E(0xFE, 0x2D492, 0x3C, 0xEBC8, 0x1388, 0x0)
    OP_8E(0xFE, 0x2D9A6, 0xFFFFFF7E, 0xF64A, 0x1388, 0x0)
    OP_22(0xD5, 0x0, 0x64)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_42_C3B4 end

    def Function_43_C3E9(): pass

    label("Function_43_C3E9")

    OP_6D(187810, -40, 61790, 1500)
    OP_6D(188510, -100, 63310, 2000)
    Return()

    # Function_43_C3E9 end

    def Function_44_C40C(): pass

    label("Function_44_C40C")

    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_4A(0xD, 0)
    OP_8C(0xD, 0, 400)
    Sleep(400)

    def lambda_C439():
        OP_8C(0xA, 0, 400)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_C439)

    def lambda_C447():
        OP_8C(0xB, 0, 400)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_C447)
    Sleep(400)

    def lambda_C45A():
        OP_8C(0x8, 0, 400)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_C45A)

    def lambda_C468():
        OP_8C(0xC, 0, 400)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_C468)
    Sleep(400)

    def lambda_C47B():
        OP_8C(0x9, 0, 400)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_C47B)
    Return()

    # Function_44_C40C end

    def Function_45_C484(): pass

    label("Function_45_C484")

    SetMapFlags(0x80)
    Sleep(30)
    OP_22(0x64, 0x0, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4B2")
    OP_70(0x3, 0x19)
    OP_73(0x3)
    OP_6F(0x3, 25)
    OP_A2(0x9)
    Jump("loc_C4C6")

    label("loc_C4B2")

    OP_70(0x3, 0x0)
    OP_73(0x3)
    OP_6F(0x3, 0)
    OP_A3(0x9)

    label("loc_C4C6")

    OP_73(0x3)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #442
        (
            "\x07\x05Flipped the lever, but nothing happened.\x01",
            "It seems the orbal energy is cut off.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    ClearMapFlags(0x80)
    TalkEnd(0xFF)
    Return()

    # Function_45_C484 end

    SaveToFile()

Try(main)
