from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3400   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3400.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        'Gundolf',                              # 9
        'Private Jules',                        # 10
        'Private Hector',                       # 11
        'Private Chesley',                      # 12
        'Armand',                               # 13
        'Ellie',                                # 14
        'Private Wayne',                        # 15
        'Warrant Officer Talbot',               # 16
        'Sanders',                              # 17
        'Tammy',                                # 18
        'Marian',                               # 19
        'Norche',                               # 20
        'Talia',                                # 21
        'CWO Dale',                             # 22
        'Private Wolpe',                        # 23
        'Private Olnis',                        # 24
        'Ritter Roadway',                       # 25
        'Royal Avenue',                         # 26
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
        'ED6_DT07/CH01750 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT07/CH01640 ._CH',             # 02
        'ED6_DT07/CH01300 ._CH',             # 03
        'ED6_DT07/CH01140 ._CH',             # 04
        'ED6_DT07/CH01150 ._CH',             # 05
        'ED6_DT07/CH01300 ._CH',             # 06
        'ED6_DT07/CH01300 ._CH',             # 07
        'ED6_DT07/CH01520 ._CH',             # 08
        'ED6_DT07/CH01350 ._CH',             # 09
        'ED6_DT07/CH01210 ._CH',             # 0A
        'ED6_DT07/CH01230 ._CH',             # 0B
        'ED6_DT07/CH01180 ._CH',             # 0C
        'ED6_DT07/CH01310 ._CH',             # 0D
        'ED6_DT07/CH01640 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT07/CH01750P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT07/CH01640P._CP',             # 02
        'ED6_DT07/CH01300P._CP',             # 03
        'ED6_DT07/CH01140P._CP',             # 04
        'ED6_DT07/CH01150P._CP',             # 05
        'ED6_DT07/CH01300P._CP',             # 06
        'ED6_DT07/CH01300P._CP',             # 07
        'ED6_DT07/CH01520P._CP',             # 08
        'ED6_DT07/CH01350P._CP',             # 09
        'ED6_DT07/CH01210P._CP',             # 0A
        'ED6_DT07/CH01230P._CP',             # 0B
        'ED6_DT07/CH01180P._CP',             # 0C
        'ED6_DT07/CH01310P._CP',             # 0D
        'ED6_DT07/CH01640P._CP',             # 0E
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
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
        TalkScenaIndex      = 16,
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
        TalkScenaIndex      = 17,
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
        TalkScenaIndex      = 18,
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
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 35300,
        Z                   = 0,
        Y                   = -3600,
        Direction           = 92,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 35310,
        Z                   = 0,
        Y                   = 3610,
        Direction           = 92,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -37360,
        Z                   = 0,
        Y                   = 960,
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
        X                   = 83520,
        Z                   = 0,
        Y                   = 630,
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
        "Function_0_362",          # 00, 0
        "Function_1_6E8",          # 01, 1
        "Function_2_736",          # 02, 2
        "Function_3_74C",          # 03, 3
        "Function_4_770",          # 04, 4
        "Function_5_C22",          # 05, 5
        "Function_6_138B",         # 06, 6
        "Function_7_138C",         # 07, 7
        "Function_8_138D",         # 08, 8
        "Function_9_138E",         # 09, 9
        "Function_10_138F",        # 0A, 10
        "Function_11_1390",        # 0B, 11
        "Function_12_1391",        # 0C, 12
        "Function_13_1392",        # 0D, 13
        "Function_14_1393",        # 0E, 14
        "Function_15_18A1",        # 0F, 15
        "Function_16_1C49",        # 10, 16
        "Function_17_20D0",        # 11, 17
        "Function_18_2BE0",        # 12, 18
        "Function_19_2E14",        # 13, 19
        "Function_20_30B0",        # 14, 20
        "Function_21_36C9",        # 15, 21
    )


    def Function_0_362(): pass

    label("Function_0_362")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (106, "loc_36E"),
        (SWITCH_DEFAULT, "loc_384"),
    )


    label("loc_36E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_381")
    OP_A2(0x605)
    Event(0, 20)

    label("loc_381")

    Jump("loc_384")

    label("loc_384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_38E")
    Jump("loc_436")

    label("loc_38E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_3AE")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 9970, 0, 6140, 257)
    Jump("loc_436")

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_3B8")
    Jump("loc_436")

    label("loc_3B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_3C2")
    Jump("loc_436")

    label("loc_3C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_3CC")
    Jump("loc_436")

    label("loc_3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_3D6")
    Jump("loc_436")

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_3E0")
    Jump("loc_436")

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_END)), "loc_3EA")
    Jump("loc_436")

    label("loc_3EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 1)), scpexpr(EXPR_END)), "loc_3F4")
    Jump("loc_436")

    label("loc_3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_419")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 9970, 0, 6140, 257)
    SetChrFlags(0x8, 0x10)
    Jump("loc_436")

    label("loc_419")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_436")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 3560, 0, -430, 90)

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_456")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_476")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_496")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_4B6")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_4D6")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_4D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_4F6")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_516")
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_562")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10640, 0, -3930, 285)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 10660, 0, 3380, 263)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_562")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_5AE")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10640, 0, -3930, 285)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 10660, 0, 3380, 263)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_5FA")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10640, 0, -3930, 285)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 10660, 0, 3380, 263)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    Jump("loc_6E7")

    label("loc_5FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_672")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10640, 0, -3930, 285)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 10660, 0, 3380, 263)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 26240, 7250, -33770, 101)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 26260, 7250, -34450, 85)
    Jump("loc_6E7")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_6E7")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10640, 0, -3930, 285)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 10660, 0, 3380, 263)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15080, 11750, -60, 276)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 26240, 7250, -33770, 101)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 26260, 7250, -34450, 85)

    label("loc_6E7")

    Return()

    # Function_0_362 end

    def Function_1_6E8(): pass

    label("Function_1_6E8")

    OP_16(0x2, 0xFA0, 0xFFFE65D8, 0xFFFE0C00, 0x30056)
    OP_6F(0x0, 160)
    OP_6F(0x1, 160)
    OP_72(0x0, 0x10)
    OP_72(0x1, 0x10)
    OP_1C(0x2, 0x0, 0x15)
    OP_1C(0x3, 0x0, 0x15)
    OP_1C(0x4, 0x0, 0x15)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_735")
    OP_28(0x2A, 0x1, 0x8000)

    label("loc_735")

    Return()

    # Function_1_6E8 end

    def Function_2_736(): pass

    label("Function_2_736")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_736")

    label("loc_74B")

    Return()

    # Function_2_736 end

    def Function_3_74C(): pass

    label("Function_3_74C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_76F")
    OP_8D(0xFE, 7090, 6400, -600, -6500, 1500)
    Jump("Function_3_74C")

    label("loc_76F")

    Return()

    # Function_3_74C end

    def Function_4_770(): pass

    label("Function_4_770")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_81E")

    ChrTalk(    #0
        0xFE,
        (
            "You know, I heard that General\x01",
            "Morgan of the Royal Border\x01",
            "Patrol is really intimidating.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "But he's in schoolbooks, too,\x01",
            "so he's definitely a great man.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_81E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_8B2")

    ChrTalk(    #2
        0xFE,
        (
            "The Royal Guard and the Special\x01",
            "Ops Unit are supposed to be\x01",
            "equally tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I'd hate to be under attack from\x01",
            "either one of them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_8B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_94F")

    ChrTalk(    #4
        0xFE,
        (
            "The level of policing that the\x01",
            "Royal Army's responsible for\x01",
            "has been raised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "The chief said we have a\x01",
            "higher risk of attack here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A19")

    label("loc_94F")

    OP_A2(0xE)

    ChrTalk(    #6
        0xFE,
        (
            "The level of policing that the\x01",
            "Royal Army's responsible for\x01",
            "has been raised.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "The chief said we have a\x01",
            "higher risk of attack here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "That makes guard duty a heck\x01",
            "of a lot more stressful.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A19")

    Jump("loc_C1E")

    label("loc_A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_A95")

    ChrTalk(    #9
        0xFE,
        (
            "Today's the start of the Martial\x01",
            "Arts Competition.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I used to go with my mom and\x01",
            "watch it every year.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_A95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_B21")

    ChrTalk(    #11
        0xFE,
        (
            "Man, I'm still tired from all those\x01",
            "anti-terrorist drills we did before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "But times are tough. I gotta pull\x01",
            "it together.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_END)), "loc_B7D")

    ChrTalk(    #13
        0xFE,
        (
            "I hope we can catch those\x01",
            "terrorists before the birthday\x01",
            "celebration starts.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_C17")

    ChrTalk(    #14
        0xFE,
        (
            "I just got transferred to this\x01",
            "garrison recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "I'm surrounded by all these\x01",
            "hardcore soldiers. I feel pretty\x01",
            "overwhelmed sometimes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C1E")

    label("loc_C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_C1E")

    label("loc_C1E")

    TalkEnd(0xFE)
    Return()

    # Function_4_770 end

    def Function_5_C22(): pass

    label("Function_5_C22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_D94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_CD6")

    ChrTalk(    #16
        0xFE,
        (
            "The Martial Arts Competition's\x01",
            "done, but the birthday celebration's\x01",
            "up next. Gotta stay frosty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "We don't know when those\x01",
            "terrorists are going to hit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D91")

    label("loc_CD6")

    OP_A2(0xF)

    ChrTalk(    #18
        0xFE,
        "Nothing to report!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "The Martial Arts Competition's\x01",
            "done, but the birthday celebration's\x01",
            "up next. Gotta stay frosty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "We don't know when those\x01",
            "terrorists are going to hit.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D91")

    Jump("loc_1387")

    label("loc_D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_E2D")

    ChrTalk(    #21
        0xFE,
        (
            "Lately it seems like the chief's\x01",
            "been worrying about something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "I guess there's plenty to worry\x01",
            "about when you're in the Royal\x01",
            "Army.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1387")

    label("loc_E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_F3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_EAD")

    ChrTalk(    #23
        0xFE,
        (
            "Until just a little while ago I'd\x01",
            "always dreamed of becoming\x01",
            "a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "It came down to that or this.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F3A")

    label("loc_EAD")

    OP_A2(0xF)

    ChrTalk(    #25
        0xFE,
        "Are you guys bracers?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Until just a little while ago I'd\x01",
            "always dreamed of becoming\x01",
            "a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "It came down to that or this.\x02",
    )

    CloseMessageWindow()

    label("loc_F3A")

    Jump("loc_1387")

    label("loc_F3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_1004")

    ChrTalk(    #28
        0xFE,
        (
            "A little earlier, I saw this glowing\x01",
            "monster on the road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "He flashed once and then\x01",
            "vanished with this smug look.\x01",
            "He was a cheeky little thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        "It was kind of...cute, really.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1387")

    label("loc_1004")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1196")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_10AC")

    ChrTalk(    #31
        0xFE,
        (
            "I heard the terrorists were dressed\x01",
            "as Royal Guardsmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "But what if they really WERE\x01",
            "Royal Guardsmen who vanished\x01",
            "into the castle somewhere?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1193")

    label("loc_10AC")

    OP_A2(0xF)

    ChrTalk(    #33
        0xFE,
        (
            "I'd heard the terrorists were dressed\x01",
            "as Royal Guardsmen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "But what if they really WERE\x01",
            "Royal Guardsmen who vanished\x01",
            "into the castle somewhere?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "If we have to take on the Royal\x01",
            "Guard, it will not end pretty for\x01",
            "us.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1193")

    Jump("loc_1387")

    label("loc_1196")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 7)), scpexpr(EXPR_END)), "loc_122E")

    ChrTalk(    #36
        0xFE,
        (
            "Those guys that just went through?\x01",
            "I heard they were hired to hunt\x01",
            "the terrorists.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "I got a bad feeling about that,\x01",
            "let me tell you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1387")

    label("loc_122E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_1380")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_END)), "loc_12C8")

    ChrTalk(    #38
        0xFE,
        (
            "Those terrorists could be hiding\x01",
            "anywhere. Be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Well, around here there should\x01",
            "just be soldiers, so you should\x01",
            "be safe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137D")

    label("loc_12C8")

    OP_A2(0xF)

    ChrTalk(    #40
        0xFE,
        (
            "Are you on your way to\x01",
            "the capital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Those terrorists could be hiding\x01",
            "anywhere. Be careful.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Well, around here there should\x01",
            "just be soldiers, so you should\x01",
            "be safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137D")

    Jump("loc_1387")

    label("loc_1380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_1387")

    label("loc_1387")

    TalkEnd(0xFE)
    Return()

    # Function_5_C22 end

    def Function_6_138B(): pass

    label("Function_6_138B")

    Return()

    # Function_6_138B end

    def Function_7_138C(): pass

    label("Function_7_138C")

    Return()

    # Function_7_138C end

    def Function_8_138D(): pass

    label("Function_8_138D")

    Return()

    # Function_8_138D end

    def Function_9_138E(): pass

    label("Function_9_138E")

    Return()

    # Function_9_138E end

    def Function_10_138F(): pass

    label("Function_10_138F")

    Return()

    # Function_10_138F end

    def Function_11_1390(): pass

    label("Function_11_1390")

    Return()

    # Function_11_1390 end

    def Function_12_1391(): pass

    label("Function_12_1391")

    Return()

    # Function_12_1391 end

    def Function_13_1392(): pass

    label("Function_13_1392")

    Return()

    # Function_13_1392 end

    def Function_14_1393(): pass

    label("Function_14_1393")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_END)), "loc_178C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 7)), scpexpr(EXPR_END)), "loc_140E")
    TalkBegin(0xFE)

    ChrTalk(    #43
        0xFE,
        "Whew...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "Those monsters coming at\x01",
            "you in swarms is something\x01",
            "else, eh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "Wears a body out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1789")

    label("loc_140E")

    OP_A2(0x57F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1477")
    TalkBegin(0xFE)

    ChrTalk(    #46
        0xFE,
        "Hey, guys.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #47
        0xFE,
        (
            "Agate! You look pretty good,\x01",
            "for a guy on his death bed.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14E2")

    label("loc_1477")

    SetChrFlags(0xFE, 0x10)
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #48
        0xFE,
        "Well, if it isn't Agate!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        "Lookin' good for a dead man!\x02",
    )

    CloseMessageWindow()

    label("loc_14E2")


    ChrTalk(    #50
        0x106,
        (
            "#051FYeah, like a little thing like THAT'D\x01",
            "slow me down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Heh heh heh, yeah,\x01",
            "I'd guess not.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "Gotta keep it up, though...otherwise\x01",
            "ol' 'Heavy Blade' here'll get angry.\x01",
            "Can't have that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x106,
        (
            "#050FGundolf, can this wait?\x02\x03",

            "We've got places to go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "Right, right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "I leave the professor to you guys.\x01",
            "Don't screw it up now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x106,
        "#051FThanks, DAD.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAF, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1683")
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #57
        0xFE,
        "Good luck with those juniors.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1707")

    label("loc_1683")

    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #58
        0xFE,
        (
            "So, you're the infamous 'Junior\x01",
            "Bracer Duo,' are you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "I heard about you from Kilika.\x01",
            "Help Agate pull through this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1707")


    ChrTalk(    #60
        0x102,
        "#012FWe'll do the best we can.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        "#002F110%. I promise.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(    #62
        0xFE,
        "Okay. I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "Aidios watch over you.\x02",
    )

    CloseMessageWindow()

    label("loc_1789")

    Jump("loc_189D")

    label("loc_178C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_189D")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_17F9")

    ChrTalk(    #64
        0xFE,
        "Damn that Wong.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "I was hoping he'd be around\x01",
            "and make things easier for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189D")

    label("loc_17F9")

    OP_A2(0x0)

    ChrTalk(    #66
        0xFE,
        "Oh well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "There's been a lot of monster killing\x01",
            "requests coming in for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "And lots of monsters I've never\x01",
            "seen before. That can't be a\x01",
            "good sign.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189D")

    TalkEnd(0xFE)
    Return()

    # Function_14_1393 end

    def Function_15_18A1(): pass

    label("Function_15_18A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_191A")

    ChrTalk(    #69
        0xFE,
        "Welcome to the Sanktheim Gate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "Travelers' paperwork can be submitted\x01",
            "for approval at the counter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C45")

    label("loc_191A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1A85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_19A3")

    ChrTalk(    #71
        0xFE,
        (
            "The chief was just as\x01",
            "surprised as us when we were\x01",
            "ordered to cancel inspections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "I thought it was a mistake.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A82")

    label("loc_19A3")

    OP_A2(0x1)

    ChrTalk(    #73
        0xFE,
        (
            "I mean, we still haven't caught\x01",
            "the terrorists yet and we\x01",
            "cancel inspections?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "I don't get it, but soldiers don't\x01",
            "need to understand their orders,\x01",
            "only carry them out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "It's all for the good of the kingdom.\x02",
    )

    CloseMessageWindow()

    label("loc_1A82")

    Jump("loc_1C45")

    label("loc_1A85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1B14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A9F")

    ChrTalk(    #76
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B11")

    label("loc_1A9F")

    OP_A2(0x1)

    ChrTalk(    #77
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "I'm on guard duty.\x01",
            "No fraternization.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "If you want to go sightseeing\x01",
            "you'd better do it now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B11")

    Jump("loc_1C45")

    label("loc_1B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_1BAA")

    ChrTalk(    #80
        0xFE,
        (
            "You can climb up here from the\x01",
            "Sanktheim gate all the way to\x01",
            "the Ahnenburg Wall.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "It's worth taking the time to\x01",
            "see at least once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C45")

    label("loc_1BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C45")

    ChrTalk(    #82
        0xFE,
        (
            "Welcome to the Sanktheim Gate.\x01",
            "Please proceed inside.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "This gate is part of the ruins of\x01",
            "old Ahnenburg Castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "We welcome sightseers!\x02",
    )

    CloseMessageWindow()

    label("loc_1C45")

    TalkEnd(0xFE)
    Return()

    # Function_15_18A1 end

    def Function_16_1C49(): pass

    label("Function_16_1C49")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_1CC2")

    ChrTalk(    #85
        0xFE,
        (
            "Are you going to join in on\x01",
            "the birthday festivities?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "The other sightseers have all\x01",
            "already left.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20CC")

    label("loc_1CC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_1E07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1D4D")

    ChrTalk(    #87
        0xFE,
        (
            "I wonder if they've caught those\x01",
            "terrorists yet...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "I imagine they'd announce it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "No use worrying about it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E04")

    label("loc_1D4D")

    OP_A2(0x2)

    ChrTalk(    #90
        0xFE,
        (
            "Yeah, inspections are over.\x01",
            "I wonder what happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "Oh well, it's not like they need\x01",
            "to give us a reason.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "I'm just glad we don't have to\x01",
            "do it anymore. It was dull.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E04")

    Jump("loc_20CC")

    label("loc_1E07")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_1EBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1E4D")

    ChrTalk(    #93
        0xFE,
        (
            "All it was doing was making\x01",
            "us stiff and tired.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EB7")

    label("loc_1E4D")

    OP_A2(0x2)

    ChrTalk(    #94
        0xFE,
        "Hey, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Because of that incident at\x01",
            "the central factory, we're\x01",
            "holding gate inspections.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB7")

    Jump("loc_20CC")

    label("loc_1EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1F37")

    ChrTalk(    #96
        0xFE,
        (
            "Pretty impressive that people\x01",
            "managed to build this gigantic\x01",
            "wall without any orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        "Isn't it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2074")

    label("loc_1F37")

    OP_A2(0x2)

    ChrTalk(    #98
        0xFE,
        (
            "These are all historical ruins.\x01",
            "It's a pretty famous tourist spot.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        (
            "We're all kind of used to seeing\x01",
            "it every day ourselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "But I'm impressed that people\x01",
            "built all of this without any help\x01",
            "from orbments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #102
        0xFE,
        (
            "What?! I was just soaking in\x01",
            "all of these buildings!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2074")

    Jump("loc_20CC")

    label("loc_2077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_20CC")

    ChrTalk(    #103
        0xFE,
        "Something up?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "The chief's inside. You can\x01",
            "take any problems to him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20CC")

    TalkEnd(0xFE)
    Return()

    # Function_16_1C49 end

    def Function_17_20D0(): pass

    label("Function_17_20D0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC9, 1)), scpexpr(EXPR_END)), "loc_214C")

    ChrTalk(    #105
        0xFE,
        (
            "There doesn't seem to have been\x01",
            "any other terrorist activity in\x01",
            "Zeiss recently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        "Maybe they got away.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_214C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 7)), scpexpr(EXPR_END)), "loc_21CD")

    ChrTalk(    #107
        0xFE,
        "The finals should be starting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "Since I'm military, I'm kind of\x01",
            "cheering for the Special \x01",
            "Ops team to win it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_21CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_2247")

    ChrTalk(    #109
        0xFE,
        (
            "I bet the streets are just wild\x01",
            "in Grancel right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        (
            "I hope someone catches those\x01",
            "terrorists soon...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_2247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 1)), scpexpr(EXPR_END)), "loc_22FD")

    ChrTalk(    #111
        0xFE,
        (
            "I'd like to be in the Martial\x01",
            "Arts Competition just once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "But we have our own internal preliminaries\x01",
            "to choose who gets to represent each branch\x01",
            "of the military.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_22FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_235E")

    ChrTalk(    #113
        0xFE,
        (
            "Being on guard duty all the time\x01",
            "wears you out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        "My shoulders are so stiff...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_235E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_23CC")

    ChrTalk(    #115
        0xFE,
        "Are you all students?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "We have people come from time\x01",
            "to time to study the Ahnenburg\x01",
            "ruins.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_23CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 5)), scpexpr(EXPR_END)), "loc_2531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_247F")

    ChrTalk(    #117
        0xFE,
        (
            "I reported that strange airship\x01",
            "to the chief...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "But the upper deck didn't report\x01",
            "any unusual noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "I bet it was some kind of\x01",
            "experimental vessel.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_252E")

    label("loc_247F")

    OP_A2(0x3)

    ChrTalk(    #120
        0xFE,
        (
            "I reported seeing a strange\x01",
            "airship to the chief...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "But the upper deck didn't report\x01",
            "any unusual noise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "I thought I'd finally done something\x01",
            "notable. Wrong.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_252E")

    Jump("loc_2BDC")

    label("loc_2531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2701")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_25F5")

    ChrTalk(    #123
        0xFE,
        (
            "There was this airship I've never\x01",
            "seen before flying out to the west.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "Leiston Fortress is to the west...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "Do you think they're testing some\x01",
            "new model airship there?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26FE")

    label("loc_25F5")

    OP_A2(0x3)

    ChrTalk(    #126
        0xFE,
        (
            "Last night I saw an airship I've\x01",
            "never seen before flying in the\x01",
            "western sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "I thought it might have had\x01",
            "something to do with the \x01",
            "incident, so I reported it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Inspections are over, so we\x01",
            "probably won't be doing any\x01",
            "more terrorist investigations.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26FE")

    Jump("loc_2BDC")

    label("loc_2701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2882")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_27A1")

    ChrTalk(    #129
        0xFE,
        (
            "If they do get away though,\x01",
            "it's going to look really\x01",
            "embarrassing for all of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "Looks like we're going to be\x01",
            "on alert for a while.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_287F")

    label("loc_27A1")

    OP_A2(0x3)

    ChrTalk(    #131
        0xFE,
        (
            "I keep getting the feeling\x01",
            "somebody's going to jump\x01",
            "out of the bushes at me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "If the terrorists do get away,\x01",
            "it's going to be embarrassing\x01",
            "for all of us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "Looks like we're going to be\x01",
            "on alert for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_287F")

    Jump("loc_2BDC")

    label("loc_2882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2A49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2944")

    ChrTalk(    #134
        0xFE,
        (
            "Staring out at the horizon day in\x01",
            "and day out has really heightened\x01",
            "my visual perspicuity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "My friends at home don't like\x01",
            "it. They say it's a sign that\x01",
            "I'm overworked.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A46")

    label("loc_2944")

    OP_A2(0x3)

    ChrTalk(    #136
        0xFE,
        (
            "We're always staring off at\x01",
            "the horizon, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "My eyes have gotten really sharp as a\x01",
            "result. All my friends at home think there's\x01",
            "something wrong with me, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "But it's just a side-effect of the job.\x01",
            "It's not like I'm sick or anything!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A46")

    Jump("loc_2BDC")

    label("loc_2A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2BDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2AC8")

    ChrTalk(    #139
        0xFE,
        "Ah, the wind feels nice!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "On good days like today you can see\x01",
            "all the way to the Kaldian foothills. \x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BDC")

    label("loc_2AC8")

    OP_A2(0x3)

    ChrTalk(    #141
        0xFE,
        "Liberl's peaceful again today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "If there's one problem, it's that\x01",
            "it's too peaceful, and we all keep\x01",
            "falling asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        "*yawn*\x02",
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0xB)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #144
        0xFE,
        (
            "Uh-oh. I've got to hold out until\x01",
            "my replacement arrives.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BDC")

    TalkEnd(0xFE)
    Return()

    # Function_17_20D0 end

    def Function_18_2BE0(): pass

    label("Function_18_2BE0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2BED")
    Jump("loc_2E10")

    label("loc_2BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2BF7")
    Jump("loc_2E10")

    label("loc_2BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2C01")
    Jump("loc_2E10")

    label("loc_2C01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2C82")

    ChrTalk(    #145
        0xFE,
        "Ah, I'm so happy!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        (
            "I'm in this beautiful place,\x01",
            "with the woman I love...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        "The world is a wonderful place.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E10")

    label("loc_2C82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2D0E")

    ChrTalk(    #148
        0xFE,
        (
            "To be honest, I don't remember\x01",
            "the scenic route very well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        (
            "I couldn't take my eyes off of\x01",
            "my darling, you see...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E10")

    label("loc_2D0E")

    OP_A2(0x4)

    ChrTalk(    #150
        0xFE,
        (
            "I was on my way to Grancel for\x01",
            "the birthday celebrations...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "...and then I decided to invite my\x01",
            "girlfriend and take the Erbe Scenic\x01",
            "Route here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "Walking through the trees,\x01",
            "hand-in-hand...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #153
        0xFE,
        "It was like a dream!\x02",
    )

    CloseMessageWindow()

    label("loc_2E10")

    TalkEnd(0xFE)
    Return()

    # Function_18_2BE0 end

    def Function_19_2E14(): pass

    label("Function_19_2E14")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_END)), "loc_2E21")
    Jump("loc_30AC")

    label("loc_2E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 1)), scpexpr(EXPR_END)), "loc_2E2B")
    Jump("loc_30AC")

    label("loc_2E2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_2E35")
    Jump("loc_30AC")

    label("loc_2E35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_2F0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2EA6")

    ChrTalk(    #154
        0xFE,
        "This wall is enormous!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "It's nothing like the garrison at\x01",
            "the Verte Bridge Checkpoint.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F09")

    label("loc_2EA6")

    OP_A2(0x5)

    ChrTalk(    #156
        0xFE,
        (
            "We just started dating and this\x01",
            "is our first trip...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        "...but he's been such a sweetie!\x02",
    )

    CloseMessageWindow()

    label("loc_2F09")

    Jump("loc_30AC")

    label("loc_2F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_30AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2F9F")

    ChrTalk(    #158
        0xFE,
        (
            "We took the gorgeous scenic route\x01",
            "here. The trees were so beautiful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xFE,
        (
            "It was like we were in our own\x01",
            "personal storybook!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30AC")

    label("loc_2F9F")

    OP_A2(0x5)

    ChrTalk(    #160
        0xFE,
        (
            "We took the gorgeous scenic route\x01",
            "here. The trees were so beautiful!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xFE,
        (
            "The colors of these old stones\x01",
            "are so romantic.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xFE,
        (
            "It was like we were in our own\x01",
            "personal storybook!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #163
        0xFE,
        (
            "It was like we were Oscar and\x01",
            "Princess Cecilia...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30AC")

    TalkEnd(0xFE)
    Return()

    # Function_19_2E14 end

    def Function_20_30B0(): pass

    label("Function_20_30B0")

    EventBegin(0x0)
    OP_6D(29440, 0, 4420, 0)
    OP_67(0, 9960, -10000, 0)
    OP_6B(10000, 0)
    OP_6C(62000, 0)
    OP_6E(262, 0)
    StopSound(0x88B8, 0x61A80, 0x0)
    SetChrPos(0x101, -11860, 0, 1880, 0)
    SetChrPos(0x102, -11610, 0, 330, 0)
    FadeToBright(2000, 0)

    def lambda_312D():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_312D)
    Sleep(1000)

    def lambda_3142():
        OP_6D(7000, 0, 4630, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3142)
    Sleep(2000)

    def lambda_315F():
        OP_8E(0xFE, 0x67C, 0x0, 0x5E6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_315F)
    Sleep(600)

    def lambda_317F():
        OP_8E(0xFE, 0x67C, 0x0, 0xFFFFFF38, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_317F)
    WaitChrThread(0x101, 0x2)
    Fade(500)
    OP_6D(4040, 0, -300, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    StopSound(0x88B8, 0x249F0, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #164
        0x101,
        (
            "#006F#3PSo, this is the Sanktheim Gate...\x02\x03",

            "It looks a lot like the Gurune\x01",
            "Gate, back in Rolent.\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #165
        0x102,
        (
            "#010F#5PWell, both gates cut through the\x01",
            "same wall. Ahnenburg Wall completely\x01",
            "surrounds the Grancel region.\x02\x03",

            "It was built almost a thousand years\x01",
            "ago, but it's solid enough that it\x01",
            "held off the Imperial forces.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        (
            "#001F#3PIt sure looks like it'd take\x01",
            "more than a few guns to knock\x01",
            "it down.\x02\x03",

            "#501FStill, it looks like a tourist attraction.\x01",
            "One where you could climb up to the top\x01",
            "and check out the view...\x02\x03",

            "#503F...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #167
        0x102,
        (
            "#019F#2PHa ha... So you're planning to\x01",
            "get up there and sprint all\x01",
            "along the walls, are you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x102, 600)

    ChrTalk(    #168
        0x101,
        (
            "#005F#3PI-I didn't say that!\x02\x03",

            "#503FI was just thinking that...it'd be nice for\x01",
            "us to have a nice, quiet lunch together.\x01",
            "Just the, um...two of us...\x02\x03",

            "And just...uh, talk about whatever...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x102,
        (
            "#010F#2P???\x02\x03",

            "Isn't that what we always do,\x01",
            "anyway?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1200)

    ChrTalk(    #170
        0x101,
        (
            "#007F#3P*sigh*... Never mind.\x02\x03",

            "Let's just get the paperwork\x01",
            "done and move on to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x102,
        (
            "#014F#2PUhh...\x01",
            "Okay, maybe it's just me...\x02\x03",

            "But are you mad about something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x101,
        (
            "#509F#3PIt's just you.\x02\x03",

            "Let's just go in and forget\x01",
            "this whole conversation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x102,
        "#017F#2P(Girls can be so difficult...)\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_20_30B0 end

    def Function_21_36C9(): pass

    label("Function_21_36C9")

    TalkBegin(0xFF)
    Sleep(400)
    TalkEnd(0xFF)
    Return()

    # Function_21_36C9 end

    SaveToFile()

Try(main)
