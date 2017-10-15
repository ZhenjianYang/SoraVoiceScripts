from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1101   ._SN',
        MapName             = 'Bose',
        Location            = 'T1101.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60011",
        Flags               = 1,
        EntryFunctionIndex  = 0,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T1101   ._SN',
            'ED6_DT21/T1101_1 ._SN',
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
        'Mayor Maybelle',                       # 9
        'Lila',                                 # 10
        'Jacob',                                # 11
        'Harry',                                # 12
        'Mina',                                 # 13
        'Orvid',                                # 14
        'Elegia',                               # 15
        'Letta',                                # 16
        'Fannie',                               # 17
        'Sting',                                # 18
        'Mirano',                               # 19
        'West Bose Highway',                    # 20
        'East Bose Highway',                    # 21
        'Bose - South Block',                   # 22
        'Bose International Port',              # 23
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
        'ED6_DT07/CH02360 ._CH',             # 00
        'ED6_DT07/CH02370 ._CH',             # 01
        'ED6_DT07/CH01000 ._CH',             # 02
        'ED6_DT07/CH01160 ._CH',             # 03
        'ED6_DT07/CH01170 ._CH',             # 04
        'ED6_DT07/CH01120 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01040 ._CH',             # 07
        'ED6_DT07/CH01050 ._CH',             # 08
        'ED6_DT27/CH03790 ._CH',             # 09
        'ED6_DT07/CH01230 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT07/CH02360P._CP',             # 00
        'ED6_DT07/CH02370P._CP',             # 01
        'ED6_DT07/CH01000P._CP',             # 02
        'ED6_DT07/CH01160P._CP',             # 03
        'ED6_DT07/CH01170P._CP',             # 04
        'ED6_DT07/CH01120P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01040P._CP',             # 07
        'ED6_DT07/CH01050P._CP',             # 08
        'ED6_DT27/CH03790P._CP',             # 09
        'ED6_DT07/CH01230P._CP',             # 0A
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 48310,
        Z                   = 0,
        Y                   = 46460,
        Direction           = 262,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 35880,
        Z                   = 0,
        Y                   = 53880,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 35880,
        Z                   = 0,
        Y                   = 52760,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 49430,
        Z                   = 0,
        Y                   = 47820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 63060,
        Z                   = 0,
        Y                   = 49000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 68240,
        Z                   = 0,
        Y                   = 53360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 68240,
        Z                   = 0,
        Y                   = 51940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 65250,
        Z                   = 0,
        Y                   = 61510,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 19300,
        Z                   = 0,
        Y                   = 48720,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 4530,
        Z                   = 0,
        Y                   = 45190,
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
        X                   = 87650,
        Z                   = 0,
        Y                   = 60410,
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
        X                   = 47990,
        Z                   = -3000,
        Y                   = 29310,
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
        X                   = 47940,
        Z                   = 0,
        Y                   = 93220,
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


    DeclEvent(
        X                   = 25200,
        Y                   = 0,
        Z                   = 57940,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 39,
    )

    DeclEvent(
        X                   = 18880,
        Y                   = 0,
        Z                   = 76030,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 40,
    )

    DeclEvent(
        X                   = 36200,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 41,
    )

    DeclEvent(
        X                   = 59000,
        Y                   = 0,
        Z                   = 79200,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 42,
    )

    DeclEvent(
        X                   = 38540,
        Y                   = 0,
        Z                   = 59990,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = 48040,
        Y                   = 100,
        Z                   = 69500,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = 57480,
        Y                   = 0,
        Z                   = 60010,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = 48010,
        Y                   = 0,
        Z                   = 50550,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 43,
    )

    DeclEvent(
        X                   = 67340,
        Y                   = -500,
        Z                   = 73070,
        Range               = 1500,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 44,
    )

    DeclEvent(
        X                   = 72240,
        Y                   = 0,
        Z                   = 44910,
        Range               = 1000,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 45,
    )

    DeclEvent(
        X                   = 47960,
        Y                   = 0,
        Z                   = 85570,
        Range               = 1000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x41,
        Unknown_1C          = 46,
    )

    DeclEvent(
        X                   = 43880,
        Y                   = 0,
        Z                   = 39840,
        Range               = 45290,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xC4F4,
        Unknown_18          = 0x0,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 56070,
        Y                   = 0,
        Z                   = 39690,
        Range               = 52630,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xC36E,
        Unknown_18          = 0x0,
        Unknown_1C          = 31,
    )


    DeclActor(
        TriggerX            = 53860,
        TriggerZ            = 0,
        TriggerY            = 40250,
        TriggerRange        = 1700,
        ActorX              = 53860,
        ActorZ              = 1000,
        ActorY              = 40250,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 29,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4A6",          # 00, 0
        "Function_1_682",          # 01, 1
        "Function_2_6D8",          # 02, 2
        "Function_3_7D5",          # 03, 3
        "Function_4_8D2",          # 04, 4
        "Function_5_A2D",          # 05, 5
        "Function_6_CE4",          # 06, 6
        "Function_7_1079",         # 07, 7
        "Function_8_1655",         # 08, 8
        "Function_9_18B0",         # 09, 9
        "Function_10_1A87",        # 0A, 10
        "Function_11_1DD1",        # 0B, 11
        "Function_12_2107",        # 0C, 12
        "Function_13_2A7E",        # 0D, 13
        "Function_14_3105",        # 0E, 14
        "Function_15_314B",        # 0F, 15
        "Function_16_3191",        # 10, 16
        "Function_17_31D7",        # 11, 17
        "Function_18_324C",        # 12, 18
        "Function_19_3D8C",        # 13, 19
        "Function_20_3F0B",        # 14, 20
        "Function_21_3F6C",        # 15, 21
        "Function_22_46D3",        # 16, 22
        "Function_23_46EF",        # 17, 23
        "Function_24_471F",        # 18, 24
        "Function_25_474F",        # 19, 25
        "Function_26_47AE",        # 1A, 26
        "Function_27_4FDA",        # 1B, 27
        "Function_28_4FFD",        # 1C, 28
        "Function_29_5020",        # 1D, 29
        "Function_30_504E",        # 1E, 30
        "Function_31_5067",        # 1F, 31
        "Function_32_507D",        # 20, 32
        "Function_33_5783",        # 21, 33
        "Function_34_5DAB",        # 22, 34
        "Function_35_6425",        # 23, 35
        "Function_36_6523",        # 24, 36
        "Function_37_65AC",        # 25, 37
        "Function_38_6609",        # 26, 38
        "Function_39_6662",        # 27, 39
        "Function_40_6666",        # 28, 40
        "Function_41_666A",        # 29, 41
        "Function_42_666E",        # 2A, 42
        "Function_43_6672",        # 2B, 43
        "Function_44_6676",        # 2C, 44
        "Function_45_667A",        # 2D, 45
        "Function_46_667E",        # 2E, 46
    )


    def Function_0_4A6(): pass

    label("Function_0_4A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_527")
    SetChrFlags(0xD, 0x80)
    SetChrPos(0xA, 52840, 0, 42530, 180)
    OP_43(0xA, 0x0, 0x6, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_4EA")
    SetChrFlags(0x10, 0x80)
    SetChrPos(0xF, 67450, 0, 52800, 260)
    Jump("loc_524")

    label("loc_4EA")

    SetChrPos(0xE, 49520, 0, 44390, 180)
    OP_43(0xE, 0x0, 0x6, 0x2)
    SetChrPos(0xB, 50500, 0, 46500, 180)
    SetChrPos(0xC, 51550, 0, 46750, 180)

    label("loc_524")

    Jump("loc_57A")

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_57A")
    SetChrPos(0xA, 46680, 0, 77450, 180)
    OP_43(0xA, 0x0, 0x6, 0x2)
    SetChrPos(0xE, 66340, 0, 51290, 315)
    OP_43(0xE, 0x0, 0x6, 0x2)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_57A")
    SetChrFlags(0x11, 0x10)

    label("loc_57A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_58A")
    SetChrFlags(0xD, 0x80)

    label("loc_58A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AA")
    ClearChrFlags(0x12, 0x80)

    label("loc_5AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_5C9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_681")

    label("loc_5C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_5DA")
    OP_A3(0x10F3)
    Event(0, 18)
    Jump("loc_681")

    label("loc_5DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_5F0")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 21)
    Jump("loc_681")

    label("loc_5F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_606")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 26)
    Jump("loc_681")

    label("loc_606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_61C")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(1, 3)
    Jump("loc_681")

    label("loc_61C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7C, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_642")
    SetMapFlags(0x10000000)
    Event(1, 6)
    Jump("loc_681")

    label("loc_642")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_663")
    Event(0, 33)
    Jump("loc_681")

    label("loc_663")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_681")
    Event(0, 34)

    label("loc_681")

    Return()

    # Function_0_4A6 end

    def Function_1_682(): pass

    label("Function_1_682")

    OP_16(0x2, 0xFA0, 0xFFFEC780, 0xFFFEF660, 0x230041)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_6CB")
    OP_72(0xA, 0x10)
    OP_6F(0xA, 59)
    OP_72(0xB, 0x10)
    OP_6F(0xB, 59)
    OP_72(0xC, 0x10)
    OP_6F(0xC, 59)
    OP_72(0xD, 0x10)
    OP_6F(0xD, 59)

    label("loc_6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D7")
    OP_64(0x0, 0x1)

    label("loc_6D7")

    Return()

    # Function_1_682 end

    def Function_2_6D8(): pass

    label("Function_2_6D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D4")
    OP_8E(0xFE, 0xF654, 0x0, 0x119F4, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF2A8, 0x0, 0x12214, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEF74, 0x0, 0x12426, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8A16, 0x0, 0x12426, 0x9C4, 0x0)
    OP_8E(0xFE, 0x839A, 0x0, 0x120A2, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0x11E36, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8048, 0x0, 0xBC66, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8264, 0x0, 0xB414, 0x9C4, 0x0)
    OP_8E(0xFE, 0x85E8, 0x0, 0xAFE6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xEB96, 0x0, 0xAFE6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF122, 0x0, 0xB1C6, 0x9C4, 0x0)
    OP_8E(0xFE, 0xF654, 0x0, 0xB874, 0x9C4, 0x0)
    Jump("Function_2_6D8")

    label("loc_7D4")

    Return()

    # Function_2_6D8 end

    def Function_3_7D5(): pass

    label("Function_3_7D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8D1")
    OP_8E(0xFE, 0x8E44, 0x0, 0xB57C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88F4, 0x0, 0xB770, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8750, 0x0, 0xB9DC, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8750, 0x0, 0x118D2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x88C2, 0x0, 0x11D00, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8B1A, 0x0, 0x11E4A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEA06, 0x0, 0x11E4A, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEE34, 0x0, 0x11CBA, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF046, 0x0, 0x11A62, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF046, 0x0, 0xBB44, 0x7D0, 0x0)
    OP_8E(0xFE, 0xED62, 0x0, 0xB6EE, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEB82, 0x0, 0xB57C, 0x7D0, 0x0)
    Jump("Function_3_7D5")

    label("loc_8D1")

    Return()

    # Function_3_7D5 end

    def Function_4_8D2(): pass

    label("Function_4_8D2")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_93D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F5")
    Call(0, 6)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_93A")

    label("loc_8F5")


    ChrTalk(    #0
        0xFE,
        (
            "I, uh, guess this is what being\x01",
            "lost for words feels like, huh?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93A")

    Jump("loc_A29")

    label("loc_93D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_988")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_985")

    ChrTalk(    #1
        0xFE,
        "This is kinda crazy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        "Wh-What should I do...?\x02",
    )

    CloseMessageWindow()

    label("loc_985")

    Jump("loc_A29")

    label("loc_988")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_A06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_9F5")

    ChrTalk(    #3
        0xFE,
        "If Mina says it, it's gotta be true!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "All right! I'm gonna do my best\x01",
            "and succeed!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A03")

    label("loc_9F5")

    Call(0, 6)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_A03")

    Jump("loc_A29")

    label("loc_A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_A29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_A20")

    ChrTalk(    #5
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_A29")

    label("loc_A20")

    Call(0, 6)
    ClearChrFlags(0xC, 0x10)

    label("loc_A29")

    TalkEnd(0xB)
    Return()

    # Function_4_8D2 end

    def Function_5_A2D(): pass

    label("Function_5_A2D")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_AD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A46")
    Call(0, 6)
    Jump("loc_AD0")

    label("loc_A46")


    ChrTalk(    #6
        0xFE,
        (
            "You need to quit WETTING THE BED\x01",
            "before talking about 'economics,' Harry!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "It's gonna be hard to be cool if you\x01",
            "keep doing that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD0")

    Jump("loc_CE0")

    label("loc_AD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_B42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3F")

    ChrTalk(    #8
        0xFE,
        "That huge thing in the sky is so scary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "Was the dragon just the start of things?\x02",
    )

    CloseMessageWindow()

    label("loc_B3F")

    Jump("loc_CE0")

    label("loc_B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_BDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_BCE")

    ChrTalk(    #10
        0xFE,
        (
            "Sometimes, to make people do stuff,\x01",
            "you have to tell a little lie.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Harry really drives me up the wall\x01",
            "sometimes.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BDC")

    label("loc_BCE")

    Call(0, 6)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0xC, 0x10)

    label("loc_BDC")

    Jump("loc_CE0")

    label("loc_BDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_CD7")

    ChrTalk(    #12
        0xFE,
        (
            "He talks big when it comes to his dreams,\x01",
            "but does he ever think about what it takes\x01",
            "to actually ACHIEVE them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Just once, I wish he'd come up with a\x01",
            "plan first before diving right into yet\x01",
            "another one of his crazy ideas.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE0")

    label("loc_CD7")

    Call(0, 6)
    ClearChrFlags(0xC, 0x10)

    label("loc_CE0")

    TalkEnd(0xC)
    Return()

    # Function_5_A2D end

    def Function_6_CE4(): pass

    label("Function_6_CE4")

    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_E4E")

    ChrTalk(    #14
        0xB,
        (
            "Since the orbments aren't working,\x01",
            "all the ships have stopped, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xB,
        (
            "The market's gonna run out of goods\x01",
            "at this rate!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xC,
        (
            "Yeah, it's kinda bad for the, um,\x01",
            "economy and stuff, I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xC,
        (
            "Shouldn't we worry about the lights\x01",
            "first, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xC,
        (
            "If you can't go to the potty at night,\x01",
            "YOU'RE gonna be in real trouble, Harry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xB,
        "...\x02",
    )

    CloseMessageWindow()
    Jump("loc_106A")

    label("loc_E4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E58")
    Jump("loc_106A")

    label("loc_E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_FD8")

    ChrTalk(    #20
        0xB,
        "Hey, Mina.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xC,
        "What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xB,
        (
            "Do you think I have what it takes to be\x01",
            "a merchant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        "Yeah, I think so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xB,
        "...R-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xC,
        (
            "Yeah. You really like it, and you\x01",
            "really want to do it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xC,
        (
            "I kind of think you're too honest sometimes,\x01",
            "but that also makes you really easy to\x01",
            "trust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xC,
        "So... Umm. I think you'll succeed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xB,
        "O-Oh. Umm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        "Ooookay! I'm gonna do my best!\x02",
    )

    CloseMessageWindow()
    Jump("loc_106A")

    label("loc_FD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_106A")

    ChrTalk(    #30
        0xB,
        (
            "Hmm. I wonder how you succeed\x01",
            "at being a merchant...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xC,
        "I dunno.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xC,
        (
            "Why not worry about that once\x01",
            "you become a merchant?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xB,
        "...\x02",
    )

    CloseMessageWindow()

    label("loc_106A")

    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    OP_A2(0x2)
    OP_A2(0x3)
    Return()

    # Function_6_CE4 end

    def Function_7_1079(): pass

    label("Function_7_1079")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1085")
    Call(1, 1)
    Return()

    label("loc_1085")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_11C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_114D")

    ChrTalk(    #34
        0xFE,
        (
            "The town's calmed down a bit\x01",
            "But it feels...false.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "Has everyone truly forgotten the doom\x01",
            "that seems to hover overhead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        "It's amazing what people can get used to.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_11C5")

    label("loc_114D")


    ChrTalk(    #37
        0xFE,
        (
            "Has everyone truly forgotten the doom\x01",
            "that seems to hover overhead?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        "It's amazing what people can get used to.\x02",
    )

    CloseMessageWindow()

    label("loc_11C5")

    Jump("loc_1651")

    label("loc_11C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_139B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D7")

    ChrTalk(    #39
        0xFE,
        (
            "From here you can clearly see that\x01",
            "island, floating in the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "The moment it appeared, the lights\x01",
            "all across the city went out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Just as we were recovering from the\x01",
            "dragon's assault, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "What will happen to our Bose, I wonder?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1398")

    label("loc_12D7")


    ChrTalk(    #43
        0xFE,
        (
            "From here you can clearly see that\x01",
            "island, floating in the sky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "I never would have guessed we would\x01",
            "be threatened by something like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        "What will happen to our Bose, I wonder?\x02",
    )

    CloseMessageWindow()

    label("loc_1398")

    Jump("loc_1651")

    label("loc_139B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_14CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1411")

    ChrTalk(    #46
        0xFE,
        (
            "The market's reopened for business with\x01",
            "no delay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "Hoho! Ah, what a tough old town Bose is.\x02",
    )

    CloseMessageWindow()
    Jump("loc_14CA")

    label("loc_1411")


    ChrTalk(    #48
        0xFE,
        (
            "The market's reopened for business with\x01",
            "no delay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "The flights and shipping's resumed,\x01",
            "so everything is as it should be again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "Hoho! Ah, what a tough old town Bose is.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_14CA")

    Jump("loc_1651")

    label("loc_14CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1651")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_152C")

    ChrTalk(    #51
        0xFE,
        (
            "Bose's future looks as bright as the\x01",
            "sun does this morning!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "Hohoho!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1651")

    label("loc_152C")


    ChrTalk(    #53
        0xFE,
        (
            "The Bose Market is one of the centers\x01",
            "of Liberl's economy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "After all, the market's merchants even\x01",
            "sell goods to the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "With the non-aggression pact signed,\x01",
            "cross-border trade must be booming.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Bose's future looks as bright as the\x01",
            "sun does this morning!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "Hohoho!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1651")

    TalkEnd(0xA)
    Return()

    # Function_7_1079 end

    def Function_8_1655(): pass

    label("Function_8_1655")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_16E5")

    ChrTalk(    #58
        0xFE,
        (
            "The market's started a big bargain sale,\x01",
            "apparently.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Doing it at a time like this?\x01",
            "They sure think of some crazy things!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18AC")

    label("loc_16E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_17A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1769")

    ChrTalk(    #60
        0xFE,
        (
            "I'm looking for a good part-time position,\x01",
            "but... Ugh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "Seems like this REALLY isn't the time\x01",
            "for it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_179F")

    label("loc_1769")


    ChrTalk(    #62
        0xFE,
        (
            "No one's hiring part-timers at a time\x01",
            "like this!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179F")

    Jump("loc_18AC")

    label("loc_17A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_18AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1817")

    ChrTalk(    #63
        0xFE,
        "I'm looking for a new side-job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "The market's probably the best option\x01",
            "for that right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18AC")

    label("loc_1817")


    ChrTalk(    #65
        0xFE,
        "I'm looking for a new side-job.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Ideally I'd like to get as good a wage\x01",
            "as I can.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "That means the market's probably the\x01",
            "best option!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_18AC")

    TalkEnd(0xF)
    Return()

    # Function_8_1655 end

    def Function_9_18B0(): pass

    label("Function_9_18B0")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1947")

    ChrTalk(    #68
        0xFE,
        "Last night was scary...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "People were yelling at each other late\x01",
            "into the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "This is when we need to come together,\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A83")

    label("loc_1947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1A83")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_19DB")

    ChrTalk(    #71
        0xFE,
        (
            "Wow, the food at the Anterose lives up\x01",
            "to its reputation!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Just the idea of tasting it again gets\x01",
            "me through the workday!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A83")

    label("loc_19DB")


    ChrTalk(    #73
        0xFE,
        (
            "I actually went to the Anterose a little\x01",
            "while ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "And everything was SOOO delicious.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "Just the idea of tasting it again gets\x01",
            "me through the workday!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1A83")

    TalkEnd(0x10)
    Return()

    # Function_9_18B0 end

    def Function_10_1A87(): pass

    label("Function_10_1A87")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_END)), "loc_1B9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B32")

    ChrTalk(    #76
        0xFE,
        (
            "I can hear a lot of excited voices\x01",
            "coming from the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "I wonder if there's a sale or something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "I'll have to take a look later!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1B97")

    label("loc_1B32")


    ChrTalk(    #79
        0xFE,
        (
            "I can hear voices echoing from inside\x01",
            "the market.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "I wonder if there's a sale or something.\x02",
    )

    CloseMessageWindow()

    label("loc_1B97")

    Jump("loc_1DCD")

    label("loc_1B9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C32")

    ChrTalk(    #81
        0xFE,
        "I mean, what IS that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "And why have all the orbments stopped\x01",
            "working?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Oooooh, what's going on?!\x01",
            "I don't understand!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_1C82")

    label("loc_1C32")


    ChrTalk(    #84
        0xFE,
        "I mean, what IS that?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "And why have all the orbments stopped\x01",
            "working?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C82")

    Jump("loc_1DCD")

    label("loc_1C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1D54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1CF0")

    ChrTalk(    #86
        0xFE,
        "I'm so happy! The market's reopened.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "This is a great day!\x01",
            "I should go shopping.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D51")

    label("loc_1CF0")


    ChrTalk(    #88
        0xFE,
        (
            "Yes! I'm so glad!\x01",
            "The market's reopened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "This is a great day!\x01",
            "I should go shopping.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_1D51")

    Jump("loc_1DCD")

    label("loc_1D54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1DCD")

    ChrTalk(    #90
        0xFE,
        "Hmm... What to buy today...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "Sometimes it feels like the world's so\x01",
            "dull. Shopping is my only pleasure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DCD")

    TalkEnd(0xE)
    Return()

    # Function_10_1A87 end

    def Function_11_1DD1(): pass

    label("Function_11_1DD1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED0")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Cleared 'Come, Ingredient Hunters' in ch. 1 of SC\x01",      # 0
            "Cleared 'Mushroom Hunting,' 'Escort Job' in FC\x01",         # 1
            "Did not clear\x01",                                          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1E9A"),
        (1, "loc_1EAC"),
        (2, "loc_1EBE"),
        (SWITCH_DEFAULT, "loc_1ED0"),
    )


    label("loc_1E9A")

    OP_28(0x65, 0x4, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_1ED0")

    label("loc_1EAC")

    OP_28(0x65, 0x3, 0x10)
    OP_28(0x5, 0x4, 0x10)
    OP_28(0x1F, 0x4, 0x10)
    Jump("loc_1ED0")

    label("loc_1EBE")

    OP_28(0x65, 0x3, 0x10)
    OP_28(0x5, 0x3, 0x10)
    OP_28(0x1F, 0x3, 0x10)
    Jump("loc_1ED0")

    label("loc_1ED0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x5, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x1F, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1EED")
    Call(1, 4)
    Return()

    label("loc_1EED")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1FB2")

    ChrTalk(    #92
        0xD,
        "The market has finally been reopened!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xD,
        (
            "I must continue to get close to the local\x01",
            "merchants, then, so I can make the deal\x01",
            "with the Anterose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xD,
        "Time to get down to business!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2103")

    label("loc_1FB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2103")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_204F")

    ChrTalk(    #95
        0xD,
        (
            "Well, then!\x01",
            "Let's just dive right into business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xD,
        (
            "If I'm going to get a deal with the Anterose,\x01",
            "I'll need support from the locals.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2103")

    label("loc_204F")


    ChrTalk(    #97
        0xD,
        "So this is the Bose Market, eh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xD,
        (
            "Well, then!\x01",
            "Let's just dive right into business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xD,
        (
            "If I'm going to get a deal with the Anterose,\x01",
            "I'll need support from the locals.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2103")

    TalkEnd(0xD)
    Return()

    # Function_11_1DD1 end

    def Function_12_2107(): pass

    label("Function_12_2107")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_2114")
    OP_A2(0x8)

    label("loc_2114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2185")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Met Sting in FC\x01",               # 0
            "Did not meet Sting in FC\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2179"),
        (1, "loc_217F"),
        (SWITCH_DEFAULT, "loc_2185"),
    )


    label("loc_2179")

    OP_A2(0x8)
    Jump("loc_2185")

    label("loc_217F")

    OP_A3(0x8)
    Jump("loc_2185")

    label("loc_2185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2A7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 3)), scpexpr(EXPR_END)), "loc_22D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2279")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_2202")

    ChrTalk(    #100
        0x11,
        "I should be able to cover Bose now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x11,
        (
            "Sorry you had to spend time filling in\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2276")

    label("loc_2202")


    ChrTalk(    #102
        0x11,
        "Hey, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x11,
        "I should be able to cover Bose now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x11,
        (
            "Sorry you had to spend time filling in\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_2276")

    Jump("loc_22D4")

    label("loc_2279")


    ChrTalk(    #105
        0x11,
        "I should be able to cover Bose now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x11,
        (
            "Sorry you had to spend time covering\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22D4")

    Jump("loc_2A7A")

    label("loc_22D7")


    ChrTalk(    #107
        0x11,
        "...\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2613")

    ChrTalk(    #108
        0x101,
        (
            "#1011FOh, hey.\x02\x03",

            "You're Sting, right? With the Bose branch?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #109
        0x11,
        "You're that junior bracer from before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x11,
        "Wait, no, you've been promoted.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        "#1016FYeah, I somehow made it through alive!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B9")

    ChrTalk(    #112
        0x103,
        "#027FHello, Sting. It's been quite a while.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x11)
    TurnDirection(0x11, 0x103, 400)

    ChrTalk(    #113
        0x11,
        "Scherazard, hey.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x11,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x11,
        "Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x103,
        (
            "#026FYou don't need to. It was the only\x01",
            "right thing to do, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2610")

    label("loc_24B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2595")

    ChrTalk(    #117
        0x106,
        "#051FSup, Sting? Been a while.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x11)
    TurnDirection(0x11, 0x106, 400)

    ChrTalk(    #118
        0x11,
        "Same to you, Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x11,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x11,
        "Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x106,
        (
            "#051FNah, no need.\x01",
            "Just part of the job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2610")

    label("loc_2595")


    ChrTalk(    #122
        0x11,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x11,
        "Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "#1002FNah, I was just doing what any bracer\x01",
            "should, really.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2610")

    Jump("loc_29F1")

    label("loc_2613")


    ChrTalk(    #125
        0x101,
        (
            "#1015F(Huh? Hey, this guy...)\x02\x03",

            "(Now that I look, he's got a guild emblem on!)\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2753")

    ChrTalk(    #126
        0x103,
        "#027FHello, Sting. It's been quite a while.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x11)
    TurnDirection(0x11, 0x103, 400)

    ChrTalk(    #127
        0x11,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x11,
        "Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x103,
        (
            "#026FYou don't need to. It was the only\x01",
            "right thing to do, after all.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F1")

    label("loc_2753")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_282F")

    ChrTalk(    #130
        0x106,
        "#051FSup, Sting? Been a while.\x02",
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x11)
    TurnDirection(0x11, 0x106, 400)

    ChrTalk(    #131
        0x11,
        "Same to you, Agate.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x11,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x11,
        "Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x106,
        (
            "#051FNah. No need.\x01",
            "Just part of the job.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29F1")

    label("loc_282F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2869")

    ChrTalk(    #135
        0x108,
        "#070F(Seems to be a fellow bracer.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_28A2")

    label("loc_2869")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28A2")

    ChrTalk(    #136
        0x104,
        "#030F(I would assume he is a bracer.)\x02",
    )

    CloseMessageWindow()

    label("loc_28A2")

    TurnDirection(0x11, 0x101, 400)

    ChrTalk(    #137
        0x11,
        "You.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x11,
        "You're the new senior bracer Lugran mentioned.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1011FOh, Lugran's probably been bragging, yeah.\x02\x03",

            "#1015FYeah, he was probably talking about me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x11,
        "I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x11,
        "Heard you handled that dragon incident.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x11,
        "Thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        (
            "#1002FNah, I was just doing what any bracer\x01",
            "should, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x11,
        "Hmm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x11,
        "A good answer.\x02",
    )

    CloseMessageWindow()

    label("loc_29F1")


    ChrTalk(    #146
        0x11,
        "I should be able to cover Bose now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x11,
        "You should return to your mission.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x11,
        (
            "Sorry you had to spend time covering\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A53)
    OP_A2(0x9)

    label("loc_2A7A")

    TalkEnd(0x11)
    Return()

    # Function_12_2107 end

    def Function_13_2A7E(): pass

    label("Function_13_2A7E")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A95")
    Call(0, 36)
    Call(0, 38)

    label("loc_2A95")

    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_4A(0xE, 255)
    OP_4A(0xA, 255)
    OP_6D(59660, 480, 80570, 0)
    OP_67(0, 9550, -10000, 0)
    OP_6B(2540, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3B)
    OP_73(0x3)
    Sleep(500)

    def lambda_2B14():
        OP_6D(59380, 0, 76340, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B14)
    OP_43(0x101, 0x1, 0x0, 0xE)
    Sleep(800)
    OP_43(0x102, 0x1, 0x0, 0xF)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x10)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x11)
    WaitChrThread(0xF9, 0x1)
    Sleep(300)

    ChrTalk(    #149
        0x101,
        (
            "#1015FOookay... Obviously, airship travel is\x01",
            "right out for this, so we'll be walking.\x02\x03",

            "Where should we go first? Rolent or Ruan?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x102,
        (
            "#1035F#5PHmm... Neither choice is better\x01",
            "than the other, really.\x02\x03",

            "#1043FAll of the guildhouses need working phones,\x01",
            "so all we can do is pick a direction and go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x101,
        "#1007FGood point...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D26")

    ChrTalk(    #152
        0x106,
        (
            "#053FJoshua's got it, I think.\x02\x03",

            "#050FNo matter which way we go,\x01",
            "I'm bettin' we'll have our work\x01",
            "cut out for us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E51")

    label("loc_2D26")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DC8")

    ChrTalk(    #153
        0x103,
        (
            "#026FI think Joshua has a point...\x02\x03",

            "#524FI suspect there'll be people who\x01",
            "need our help no matter where we\x01",
            "go, so we should just get to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E51")

    label("loc_2DC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E51")

    ChrTalk(    #154
        0x108,
        (
            "#074FJoshua has the right of it, I think.\x02\x03",

            "#070FNo matter where we go, people are\x01",
            "likely to need our help regardless.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E51")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E9A")

    ChrTalk(    #155
        0x107,
        "#560FI hope we can help all the people in trouble!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F24")

    label("loc_2E9A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EDC")

    ChrTalk(    #156
        0x108,
        "#070FWe must help those in need, after all.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F24")

    label("loc_2EDC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F24")

    ChrTalk(    #157
        0x103,
        (
            "#524FWe have sworn to help\x01",
            "those in need, after all.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F24")


    ChrTalk(    #158
        0x101,
        "#1006FYeah... Okay then!\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #159
        (
            "\x07\x05During the Shutdown Phenomenon, only characters\x01",
            "equipped with a Zero Field Generator can use\x01",
            "Orbal Arts. Equip a generator in the Accessory\x01",
            "slot to use it.\x02\x03",

            "Furthermore, as Tita uses an orbal cannon,\x01",
            "she cannot act in any way other than movement\x01",
            "or her gunpowder-powered Cannon Impulse\x01",
            "S-Craft without a generator.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_C4(0x0, 0x8)
    OP_28(0x9A, 0x1, 0x1000)
    OP_28(0x9A, 0x1, 0x2000)
    OP_28(0x9B, 0x4, 0x2)
    OP_28(0x9B, 0x4, 0x8)
    OP_28(0x9B, 0x1, 0x1)
    OP_28(0x9B, 0x1, 0x2)
    OP_28(0x9B, 0x1, 0x4)
    OP_28(0x9B, 0x1, 0x10)
    OP_28(0x9B, 0x1, 0x40)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_3E(0x151, 4)
    OP_4B(0xE, 255)
    OP_4B(0xA, 255)
    OP_20(0x3E8)
    OP_21()
    EventEnd(0x0)
    OP_1D(0x1A)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_2A7E end

    def Function_14_3105(): pass

    label("Function_14_3105")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6C8, 0x0, 0x13272, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE65A, 0x0, 0x124F8, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_3105 end

    def Function_15_314B(): pass

    label("Function_15_314B")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6C8, 0x0, 0x13272, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE290, 0x0, 0x128E0, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_15_314B end

    def Function_16_3191(): pass

    label("Function_16_3191")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE6C8, 0x0, 0x13272, 0x7D0, 0x0)
    OP_8E(0xFE, 0xEAC4, 0x0, 0x128E0, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_16_3191 end

    def Function_17_31D7(): pass

    label("Function_17_31D7")

    SetChrPos(0xFE, 59000, 500, 81490, 180)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xE696, 0x1E0, 0x136DC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(200)
    OP_72(0x3, 0x800)
    OP_6F(0x3, 59)
    OP_70(0x3, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x3)
    OP_71(0x3, 0x800)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xE6A0, 0x0, 0x12BEC, 0x7D0, 0x0)
    Return()

    # Function_17_31D7 end

    def Function_18_324C(): pass

    label("Function_18_324C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3263")
    Call(0, 36)
    Call(0, 37)

    label("loc_3263")

    Call(0, 19)
    SetChrPos(0xF8, 60660, 0, 76570, 135)
    SetChrPos(0x101, 61720, 0, 76670, 135)
    SetChrPos(0xF7, 61830, 0, 77710, 135)
    SetChrPos(0xF9, 60400, 0, 77960, 135)
    SetChrPos(0xFA, 62880, 0, 75050, 315)
    SetChrPos(0xFB, 63770, 0, 75420, 315)
    SetChrPos(0xFC, 62310, 0, 74280, 315)
    OP_6D(61500, 0, 77120, 0)
    OP_67(0, 8670, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(324000, 0)
    OP_6E(262, 0)
    OP_4A(0xE, 255)
    OP_4A(0xA, 255)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_337E")

    ChrTalk(    #160
        0x106,
        (
            "#051F#5PAll right, we'll head for the\x01",
            "Kingfisher Inn first.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_349B")

    label("loc_337E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_33D7")

    ChrTalk(    #161
        0x103,
        (
            "#021F#5PWell, then! We'll head for the\x01",
            "Kingfisher Inn ahead of you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_349B")

    label("loc_33D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3428")

    ChrTalk(    #162
        0x108,
        (
            "#071F#5PRight, then! We'll head on to\x01",
            "the inn ahead of you!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_349B")

    label("loc_3428")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_349B")

    ChrTalk(    #163
        0x104,
        (
            "#031F#5PNever fear, my bosom companions!\x01",
            "We shall make for the glorious Kingfisher\x01",
            "ahead of you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_349B")


    ChrTalk(    #164
        0x101,
        (
            "#1006F#6PThanks for doing this, guys.\x02\x03",

            "Make sure we all get checked in!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3564")

    ChrTalk(    #165
        0x103,
        (
            "#027F#6PLugran called ahead of us, so I doubt\x01",
            "we'll have TOO much trouble getting\x01",
            "rooms for everyone.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C3")

    label("loc_3564")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D0")

    ChrTalk(    #166
        0x106,
        (
            "#051F#6PEh, Lugran called ahead, so gettin' rooms\x01",
            "for everyone shouldn't be too hard.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C3")

    label("loc_35D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3646")

    ChrTalk(    #167
        0x108,
        (
            "#070F#6PMr. Lugran already contacted the inn.\x01",
            "I doubt we'll have difficulty securing our rooms.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36C3")

    label("loc_3646")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36C3")

    ChrTalk(    #168
        0x104,
        (
            "#030F#6PLugran, generous soul that he is,\x01",
            "has already contacted the inn.\x01",
            "I doubt we'll have any problems.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_36F9")

    ChrTalk(    #169
        0x107,
        "#061F#5PLeave it to us, Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3793")

    label("loc_36F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_372B")

    ChrTalk(    #170
        0x105,
        "#048F#5PYes, leave it to us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3793")

    label("loc_372B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3764")

    ChrTalk(    #171
        0x104,
        "#031F#5PNever fear! Leave it to us.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3793")

    label("loc_3764")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3793")

    ChrTalk(    #172
        0x108,
        "#071F#5PYes, leave it to us.\x02",
    )

    CloseMessageWindow()

    label("loc_3793")

    OP_8C(0xFA, 180, 400)

    def lambda_37A0():
        OP_8E(0xFE, 0xF8D4, 0x0, 0xF618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFA, 1, lambda_37A0)
    Sleep(500)
    OP_8C(0xFB, 180, 400)

    def lambda_37C7():
        OP_8E(0xFE, 0xFCEE, 0x0, 0xF618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFB, 1, lambda_37C7)
    Sleep(500)
    OP_8C(0xFC, 180, 400)

    def lambda_37EE():
        OP_8E(0xFE, 0xF46A, 0x0, 0xF618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFC, 1, lambda_37EE)

    def lambda_3809():
        OP_6D(62540, 0, 74000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3809)

    def lambda_3821():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_3821)
    Sleep(100)

    def lambda_3834():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3834)
    Sleep(100)

    def lambda_3847():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3847)
    Sleep(100)

    def lambda_385A():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_385A)
    WaitChrThread(0xFC, 0x1)
    SetChrFlags(0xFA, 0x80)
    SetChrFlags(0xFB, 0x80)
    SetChrFlags(0xFC, 0x80)
    WaitChrThread(0x101, 0x0)

    def lambda_3881():
        OP_6D(60780, 0, 77800, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3881)
    WaitChrThread(0x101, 0x0)

    def lambda_389E():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_389E)
    Sleep(50)

    def lambda_38B1():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_38B1)
    Sleep(50)

    def lambda_38C4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_38C4)
    Sleep(50)

    def lambda_38D7():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_38D7)
    Sleep(400)

    ChrTalk(    #173
        0x101,
        (
            "#1006F#5POkay, so we should probably check the\x01",
            "guild board just in case, don't you think?\x02\x03",

            "I mean, the whole dragon mess has died down,\x01",
            "but it might've kicked up some other issues,\x01",
            "and I'm still kinda worried...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A53")

    ChrTalk(    #174
        0x106,
        (
            "#051FLugran did have kind of a point, remember.\x02\x03",

            "Let's NOT kill ourselves on work for once\x01",
            "and actually go enjoy a bit of rest.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C3E")

    label("loc_3A53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AF2")

    ChrTalk(    #175
        0x103,
        (
            "#020FWell, Lugran did have a point earlier, remember.\x02\x03",

            "There IS some wisdom in not overdoing it\x01",
            "and simply going to enjoy the lakefront.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C3E")

    label("loc_3AF2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B90")

    ChrTalk(    #176
        0x108,
        (
            "#070FThe elder did speak wisdom to us, I think.\x02\x03",

            "We should not kill ourselves on work.\x01",
            "We should enjoy the chance to rest while we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C3E")

    label("loc_3B90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C3E")

    ChrTalk(    #177
        0x104,
        (
            "#035FAh, but do not forget Lugran's\x01",
            "words of wisdom to us.\x02\x03",

            "#030FIt would be wise for us to go and actually\x01",
            "enjoy the pleasures of the lakefront and rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C3E")


    ChrTalk(    #178
        0x101,
        (
            "#1015F#5PYou have a point...\x02\x03",

            "#1001FAll right, let's just tie up the loose ends\x01",
            "and head to Valleria Lake!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD2")

    ChrTalk(    #179
        0x107,
        "#061F#6PYeah!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D4C")

    label("loc_3CD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CF7")

    ChrTalk(    #180
        0x105,
        "#041F#6PLet's.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D4C")

    label("loc_3CF7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D26")

    ChrTalk(    #181
        0x104,
        "#031F#6PHeh, as you say.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D4C")

    label("loc_3D26")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D4C")

    ChrTalk(    #182
        0x108,
        "#071F#6PAfter you.\x02",
    )

    CloseMessageWindow()

    label("loc_3D4C")

    Sleep(100)
    Call(0, 20)
    Sleep(100)
    OP_4B(0xA, 255)
    OP_4B(0xE, 255)
    OP_28(0x78, 0x4, 0x40)
    OP_28(0x96, 0x1, 0x800)
    OP_28(0x96, 0x1, 0x1000)
    OP_28(0x97, 0x4, 0x2)
    OP_28(0x97, 0x4, 0x8)
    OP_28(0x97, 0x1, 0x1)
    OP_28(0x97, 0x1, 0x2)
    EventEnd(0x0)
    Return()

    # Function_18_324C end

    def Function_19_3D8C(): pass

    label("Function_19_3D8C")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3DC5")
    AddParty(0x7, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3DC5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3DFE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DE6")
    AddParty(0x4, 0xFA, 0xFF)
    Jump("loc_3DEA")

    label("loc_3DE6")

    AddParty(0x4, 0xFB, 0xFF)

    label("loc_3DEA")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3DFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3E4B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E1F")
    AddParty(0x3, 0xFA, 0xFF)
    Jump("loc_3E37")

    label("loc_3E1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E33")
    AddParty(0x3, 0xFB, 0xFF)
    Jump("loc_3E37")

    label("loc_3E33")

    AddParty(0x3, 0xFC, 0xFF)

    label("loc_3E37")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3E98")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6C")
    AddParty(0x5, 0xFA, 0xFF)
    Jump("loc_3E84")

    label("loc_3E6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E80")
    AddParty(0x5, 0xFB, 0xFF)
    Jump("loc_3E84")

    label("loc_3E80")

    AddParty(0x5, 0xFC, 0xFF)

    label("loc_3E84")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3E98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3EE5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EB9")
    AddParty(0x2, 0xFA, 0xFF)
    Jump("loc_3ED1")

    label("loc_3EB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ECD")
    AddParty(0x2, 0xFB, 0xFF)
    Jump("loc_3ED1")

    label("loc_3ECD")

    AddParty(0x2, 0xFC, 0xFF)

    label("loc_3ED1")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3EE5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F0A")
    AddParty(0x6, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3F0A")

    Return()

    # Function_19_3D8C end

    def Function_20_3F0B(): pass

    label("Function_20_3F0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3F1B")
    RemoveParty(0x7, 0xFF)

    label("loc_3F1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3F2B")
    RemoveParty(0x4, 0xFF)

    label("loc_3F2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3F3B")
    RemoveParty(0x6, 0xFF)

    label("loc_3F3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3F4B")
    RemoveParty(0x3, 0xFF)

    label("loc_3F4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3F5B")
    RemoveParty(0x5, 0xFF)

    label("loc_3F5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_3F6B")
    RemoveParty(0x2, 0xFF)

    label("loc_3F6B")

    Return()

    # Function_20_3F0B end

    def Function_21_3F6C(): pass

    label("Function_21_3F6C")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F7F")
    Call(0, 35)

    label("loc_3F7F")

    OP_4A(0xE, 255)
    OP_4A(0xA, 255)
    OP_6D(59000, 400, 79200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 59000, 500, 81490, 180)
    SetChrPos(0x106, 59000, 500, 81490, 180)
    SetChrPos(0xF8, 59000, 500, 81490, 180)
    SetChrPos(0xF9, 59000, 500, 81490, 180)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3B)
    OP_73(0x1)
    Sleep(500)
    OP_43(0x101, 0x1, 0x0, 0x16)
    Sleep(800)
    OP_43(0x106, 0x1, 0x0, 0x17)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x18)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x19)
    Sleep(1000)

    def lambda_405E():
        OP_6D(59010, 0, 74980, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_405E)

    def lambda_4076():
        OP_6C(65000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4076)
    WaitChrThread(0xF9, 0x1)
    Sleep(500)

    ChrTalk(    #183
        0x101,
        (
            "#1006FOkay, so! If we're going all over the region\x01",
            "to find these wanted monsters...\x02\x03",

            "Since we're out, why don't we stop at\x01",
            "Ravennue Village?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4422")

    ChrTalk(    #184
        0x107,
        "#560FYeah! ♪\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x106,
        (
            "#555FUh. Why are you looking at me like you're\x01",
            "expecting something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x107,
        (
            "#067FHeehee...\x02\x03",

            "I do want to go see your\x01",
            "hometown, Agate.\x02\x03",

            "#063FD-Do you not want to?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x106,
        (
            "#053F...Not right now, no.\x02\x03",

            "#050FWe need to settle our current jobs first,\x01",
            "including hunting these monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x107,
        "#561FAwww...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x101,
        (
            "#1019FYou unfeeling clod.\x02\x03",

            "Come on, Tita's here. Would it literally\x01",
            "make your head catch fire to be nice\x01",
            "for once?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x106,
        "#551FThe hell do you even...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x107,
        (
            "#065FEstelle, it's okay, really!\x02\x03",

            "It's only normal that we should\x01",
            "put work first...\x02\x03",

            "#562FAgate, I'm sorry for prodding you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x106,
        (
            "#552F...Nah.\x02\x03",

            "#556FAnd...y'know.\x01",
            "I'll definitely take you once things have\x01",
            "settled down a bit.\x02\x03",

            "Just be a good girl for now, shortstuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x107,
        "#061FOkay!\x02",
    )

    CloseMessageWindow()
    Jump("loc_46A3")

    label("loc_4422")


    ChrTalk(    #194
        0x106,
        (
            "#555FUh. Pretty sure I made this clear on the\x01",
            "flight over.\x02\x03",

            "We'll visit Ravennue AFTER we're done\x01",
            "with work here in Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x101,
        "#1019FYou unfeeling clod.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_453D")

    ChrTalk(    #196
        0x104,
        (
            "#035FHeh. Agate has the right of it, I think.\x02\x03",

            "#037FOr would you want to go and leave our\x01",
            "Tita behind?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_463F")

    label("loc_453D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_45AC")

    ChrTalk(    #197
        0x105,
        (
            "#045FHaha... I think Agate has a point.\x02\x03",

            "#542FWe can hardly go to Ravennue without\x01",
            "Tita.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_463F")

    label("loc_45AC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_463F")

    ChrTalk(    #198
        0x103,
        (
            "#021FWell, I think Agate has a point,\x01",
            "here.\x02\x03",

            "#027FOr would you rather we leave poor\x01",
            "Tita behind and enjoy Ravennue\x01",
            "without her?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_463F")


    ChrTalk(    #199
        0x101,
        "#1001FOooooh, right! ♪ Gotta bring Tita!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x106,
        (
            "#055FD'you have to agree just because\x01",
            "of THAT?!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46A3")

    OP_A2(0x1A0D)
    OP_28(0x93, 0x4, 0x2)
    OP_28(0x93, 0x4, 0x8)
    OP_28(0x93, 0x1, 0x1)
    OP_28(0x93, 0x1, 0x2)
    OP_28(0x93, 0x1, 0x10)
    OP_28(0x93, 0x1, 0x80)
    OP_4B(0xE, 255)
    OP_4B(0xA, 255)
    EventEnd(0x0)
    Return()

    # Function_21_3F6C end

    def Function_22_46D3(): pass

    label("Function_22_46D3")

    OP_8E(0xFE, 0xE678, 0x0, 0x121CE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_22_46D3 end

    def Function_23_46EF(): pass

    label("Function_23_46EF")

    OP_8E(0xFE, 0xE678, 0x0, 0x13042, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE966, 0x0, 0x12426, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_23_46EF end

    def Function_24_471F(): pass

    label("Function_24_471F")

    OP_8E(0xFE, 0xE678, 0x0, 0x13042, 0x7D0, 0x0)
    OP_8E(0xFE, 0xE330, 0x0, 0x12548, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_24_471F end

    def Function_25_474F(): pass

    label("Function_25_474F")

    OP_8E(0xFE, 0xE678, 0x190, 0x13560, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_72(0x3, 0x800)
    OP_6F(0x3, 59)
    OP_70(0x3, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x1)
    OP_71(0x3, 0x800)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xE678, 0x0, 0x12872, 0x7D0, 0x0)
    Return()

    # Function_25_474F end

    def Function_26_47AE(): pass

    label("Function_26_47AE")

    EventBegin(0x0)
    OP_6D(63080, 0, 53130, 0)
    OP_67(0, 9460, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(265, 0)
    SetChrPos(0xA, 62320, 0, 51020, 360)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x6, 0x2)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)

    def lambda_482E():
        OP_6D(62390, 0, 58620, 3500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_482E)
    FadeToBright(2000, 0)
    OP_8E(0xA, 0xF370, 0x0, 0xE704, 0x7D0, 0x0)
    OP_4A(0xA, 255)
    SetChrPos(0x8, 61930, 0, 68420, 180)
    SetChrPos(0x9, 62610, 0, 68980, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #201
        0x8,
        "Woman's Voice",
        "#6PGood day, Mr. Jacob.\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_48DA():
        OP_6D(62420, 0, 60760, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_48DA)

    def lambda_48F2():
        OP_67(0, 9360, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_48F2)

    def lambda_490A():
        OP_6E(272, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_490A)

    def lambda_491A():
        OP_8E(0xFE, 0xF1EA, 0x0, 0xEF7E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_491A)
    Sleep(100)

    def lambda_493A():
        OP_8E(0xFE, 0xF492, 0x0, 0xF104, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_493A)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #202
        0xA,
        "Ahhh, if it isn't young Maybelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xA,
        (
            "Are you on your way to services at\x01",
            "the church?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x8,
        (
            "#611F#6PI'm afraid not. I've got to check in at\x01",
            "the market first.\x02\x03",

            "I'll be sure to give Aidios Her full due\x01",
            "afterwards, though!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 225, 400)

    ChrTalk(    #205
        0x9,
        (
            "#623F#4PMilady...\x02\x03",

            "You claimed the exact same thing the\x01",
            "other day but ultimately did not attend.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #206
        0x8,
        (
            "#615F#6PLila... How DO you remember such\x01",
            "trivial things?\x02\x03",

            "#612FI absolutely will visit today. I promise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xA,
        (
            "Ho ho! Well, remember, child, hard work is\x01",
            "good for the soul, but so is finding time\x01",
            "for yourself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xA,
        (
            "And that goes double for people in positions\x01",
            "of responsibility, like yourself!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BDD():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4BDD)
    Sleep(150)
    OP_8C(0x9, 180, 400)

    ChrTalk(    #209
        0x8,
        (
            "#617F#6PI know, I know... I'll find some time to\x01",
            "go today. I promise, really.\x02\x03",

            "#611FBut for now, I must ask for your pardon.\x01",
            "Have a good day, Mr. Jacob.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x9,
        "#621F#4PPardon us.\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_4CB2():

        label("loc_4CB2")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_4CB2")

    QueueWorkItem2(0xA, 1, lambda_4CB2)
    OP_43(0x8, 0x1, 0x0, 0x1B)
    Fade(1000)
    OP_6D(59360, 0, 60210, 0)
    OP_67(0, 10720, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(270000, 0)
    OP_6E(262, 0)
    Sleep(800)
    OP_43(0x9, 0x1, 0x0, 0x1C)
    WaitChrThread(0x8, 0x1)
    Sleep(300)
    OP_72(0xB, 0x10)
    OP_6F(0xB, 0)
    OP_70(0xB, 0x3B)
    OP_73(0xB)

    def lambda_4D38():
        OP_8E(0xFE, 0xD516, 0x1F4, 0xEA6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4D38)
    Sleep(500)

    def lambda_4D58():
        OP_8E(0xFE, 0xD516, 0x1F4, 0xEA6A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4D58)

    def lambda_4D73():
        OP_6D(62320, 0, 59140, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D73)

    def lambda_4D8B():
        OP_67(0, 9500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D8B)

    def lambda_4DA3():
        OP_6C(242000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4DA3)

    def lambda_4DB3():
        OP_6E(262, 4000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4DB3)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    OP_6F(0xB, 59)
    OP_70(0xB, 0x0)
    OP_71(0xB, 0x10)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    OP_44(0xA, 0x1)
    WaitChrThread(0xA, 0x2)

    ChrTalk(    #211
        0xA,
        (
            "#6PI wasn't sure about her when she\x01",
            "nominated herself for the mayoralty\x01",
            "right after her poor father passed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xA,
        (
            "#6PBut now...look at her. The real face of\x01",
            "a mayor. He'd sure be proud.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xA,
        (
            "#6PShe could serve to learn to relax a little,\x01",
            "but--\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 400)
    OP_8E(0xA, 0xF370, 0x0, 0xE8F8, 0x7D0, 0x1)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0xA, 90, 400)
    OP_62(0xA, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0xA)

    ChrTalk(    #214
        0xA,
        "#5PWhat in Aidios' name?\x02",
    )

    CloseMessageWindow()

    def lambda_4F63():
        OP_6D(64379, 0, 59730, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F63)

    def lambda_4F7B():
        OP_67(0, 7140, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4F7B)

    def lambda_4F93():
        OP_6B(3110, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4F93)

    def lambda_4FA3():
        OP_6C(270000, 7000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4FA3)

    def lambda_4FB3():
        OP_6E(632, 7000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_4FB3)
    Sleep(4000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_26_47AE end

    def Function_27_4FDA(): pass

    label("Function_27_4FDA")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xE088, 0x19A, 0xEA6A, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_27_4FDA end

    def Function_28_4FFD(): pass

    label("Function_28_4FFD")

    OP_8C(0xFE, 270, 400)
    OP_8E(0xFE, 0xE470, 0x0, 0xEA6A, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_28_4FFD end

    def Function_29_5020(): pass

    label("Function_29_5020")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x2400CD, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    Sleep(500)
    OP_A2(0x20EA)
    TalkEnd(0xFF)
    Return()

    # Function_29_5020 end

    def Function_30_504E(): pass

    label("Function_30_504E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5066")
    OP_A2(0xC)
    Call(0, 32)

    label("loc_5066")

    Return()

    # Function_30_504E end

    def Function_31_5067(): pass

    label("Function_31_5067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x412, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_507C")
    Call(0, 32)

    label("loc_507C")

    Return()

    # Function_31_5067 end

    def Function_32_507D(): pass

    label("Function_32_507D")

    EventBegin(0x0)
    Fade(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_50D2")
    SetChrPos(0x101, 46000, 0, 45140, 90)
    SetChrPos(0x102, 45600, 0, 44220, 90)
    SetChrPos(0xF8, 44800, 0, 45140, 90)
    SetChrPos(0xF9, 44400, 0, 44220, 90)
    Jump("loc_5116")

    label("loc_50D2")

    SetChrPos(0x101, 55500, 0, 45140, 270)
    SetChrPos(0x102, 55900, 0, 44220, 270)
    SetChrPos(0xF8, 56700, 0, 45140, 270)
    SetChrPos(0xF9, 57100, 0, 44220, 270)

    label("loc_5116")

    OP_69(0x101, 0x0)

    def lambda_5123():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5123)
    Sleep(30)

    def lambda_513E():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_513E)
    Sleep(30)

    def lambda_5159():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5159)
    Sleep(30)

    def lambda_5174():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5174)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_51D2")

    def lambda_5191():
        OP_6D(47500, 0, 44800, 2000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5191)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Jump("loc_5216")

    label("loc_51D2")


    def lambda_51D8():
        OP_6D(52500, 0, 44800, 2000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_51D8)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    label("loc_5216")

    OP_0D()
    WaitChrThread(0xD, 0x1)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #215
        0x101,
        (
            "#1015FHuh?\x02\x03",

            "What's going on?\x01",
            "Why are all these people looking up at--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0x102, 180, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_52D9")

    ChrTalk(    #216
        0x102,
        (
            "#1043FI see...\x02\x03",

            "#1035FSo that's it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5305")

    label("loc_52D9")


    ChrTalk(    #217
        0x102,
        (
            "#1043F#6PI see...\x02\x03",

            "#1035FSo that's it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5305")

    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x101, 180, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_5355")

    ChrTalk(    #218
        0x101,
        "#1020FAh!\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_5340():
        OP_6D(47500, 8000, 35000, 5500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5340)
    Jump("loc_5380")

    label("loc_5355")


    ChrTalk(    #219
        0x101,
        "#1020F#3PAh!\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_536E():
        OP_6D(52500, 8000, 35500, 5500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_536E)

    label("loc_5380")


    def lambda_5386():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5386)
    Sleep(100)

    def lambda_5399():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5399)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x1)
    Sleep(1400)
    OP_AD(0x2400CD, 0x0, 0x0, 0xC8)
    Sleep(2500)
    FadeToBright(0, 0)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x0)
    OP_8C(0xF8, 180, 0)
    OP_8C(0xF9, 180, 0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #220
        (
            "#1020FThe floating city?!\x02\x03",

            "It's so huge!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5498")
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #221
        "#065FWaaaah!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5498")

    SetMessageWindowPos(400, 340, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #222
        "#1042FIt's overwhelming, seeing it from down here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_55F3")

    ChrTalk(    #223
        0x106,
        (
            "#053FWell, I can understand why the civvies\x01",
            "are freaking out.\x02\x03",

            "#050FWe might not be able to do a hell of a\x01",
            "lot, but times like this are when bracers\x01",
            "have to step up.\x02\x03",

            "We gotta do our best to make this better\x01",
            "and give the citizens some peace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_574D")

    label("loc_55F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56D2")

    ChrTalk(    #224
        0x103,
        (
            "#022FI can rather empathize with the panic\x01",
            "of the citizens.\x02\x03",

            "Our abilities as bracers are about to be\x01",
            "tested as never before.\x02\x03",

            "What we can actually DO might be limited,\x01",
            "but let's do everything we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_574D")

    label("loc_56D2")


    ChrTalk(    #225
        0x108,
        (
            "#072FIt is easy to see why the citizenry is\x01",
            "so terrified.\x02\x03",

            "It falls to us to do what we can to\x01",
            "alleviate their fears.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_574D")


    ChrTalk(    #226
        0x101,
        "#1002FY-Yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x102,
        "#1042FYes. Let's hurry.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20EA)
    EventEnd(0x0)
    Return()

    # Function_32_507D end

    def Function_33_5783(): pass

    label("Function_33_5783")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrPos(0x101, 48500, 0, 49500, 180)
    SetChrPos(0x102, 47600, 250, 49900, 180)
    SetChrPos(0xF8, 48500, 250, 50700, 180)
    SetChrPos(0xF9, 47600, 250, 51100, 180)
    OP_69(0x101, 0x0)

    def lambda_57E0():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57E0)
    Sleep(30)

    def lambda_57FB():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57FB)
    Sleep(30)

    def lambda_5816():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5816)
    Sleep(30)

    def lambda_5831():
        OP_94(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5831)

    def lambda_5847():
        OP_6D(48220, 0, 47000, 2000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5847)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xD, 0x1)
    OP_8C(0x101, 135, 400)

    def lambda_5875():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_5875)
    Sleep(120)

    def lambda_5888():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5888)
    Sleep(60)

    def lambda_589B():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_589B)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #228
        0x101,
        (
            "#1015F#6PHuh?\x02\x03",

            "What's going on?\x01",
            "Why are all these people looking up at--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0x102, 180, 400)

    ChrTalk(    #229
        0x102,
        (
            "#1043F#3PI see...\x02\x03",

            "#1035FSo that's it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #230
        0x101,
        "#1020F#6PAh!\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_5993():
        OP_6D(48220, 8000, 35000, 5500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5993)

    def lambda_59AB():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_59AB)
    Sleep(100)

    def lambda_59BE():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_59BE)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x1)
    Sleep(1400)
    OP_AD(0x2400CD, 0x0, 0x0, 0xC8)
    Sleep(2500)
    FadeToBright(0, 0)
    OP_51(0xD, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0xF9, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0xD, 0x0)
    OP_8C(0xF8, 180, 0)
    OP_8C(0xF9, 180, 0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #231
        (
            "#1020FThe floating city?!\x02\x03",

            "It's so huge!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5ABD")
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #232
        "#065FWaaaah!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5ABD")

    SetMessageWindowPos(400, 340, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #233
        "#1042FIt's overwhelming, seeing it from down here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C18")

    ChrTalk(    #234
        0x106,
        (
            "#053FWell, I can understand why the civvies\x01",
            "are freaking out.\x02\x03",

            "#050FWe might not be able to do a hell of a\x01",
            "lot, but times like this are when bracers\x01",
            "have to step up.\x02\x03",

            "We gotta do our best to make this better\x01",
            "and give the citizens some peace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D72")

    label("loc_5C18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5CF7")

    ChrTalk(    #235
        0x103,
        (
            "#022FI can rather empathize with the panic\x01",
            "of the citizens.\x02\x03",

            "Our abilities as bracers are about to be\x01",
            "tested as never before.\x02\x03",

            "What we can actually DO might be limited,\x01",
            "but let's do everything we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D72")

    label("loc_5CF7")


    ChrTalk(    #236
        0x108,
        (
            "#072FIt is easy to see why the citizenry is\x01",
            "so terrified.\x02\x03",

            "It falls to us to do what we can to\x01",
            "alleviate their fears.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D72")


    ChrTalk(    #237
        0x101,
        "#1002F#6PY-Yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x102,
        "#1042FYes. Let's hurry.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20EA)
    EventEnd(0x0)
    Return()

    # Function_33_5783 end

    def Function_34_5DAB(): pass

    label("Function_34_5DAB")

    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    SetChrPos(0x101, 49070, -750, 38730, 0)
    SetChrPos(0x102, 47920, -1000, 38550, 0)
    SetChrPos(0xF8, 49350, -1500, 37760, 0)
    SetChrPos(0xF9, 48170, -1750, 37520, 0)
    OP_6D(49500, -250, 39450, 0)
    OP_67(0, 9090, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_5E3E():
        OP_8E(0xFE, 0xBEC8, 0x0, 0xA578, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5E3E)
    Sleep(30)

    def lambda_5E5E():
        OP_8E(0xFE, 0xB950, 0x0, 0xA550, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5E5E)
    Sleep(30)

    def lambda_5E7E():
        OP_8E(0xFE, 0xBE50, 0x0, 0xA050, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5E7E)
    Sleep(30)

    def lambda_5E9E():
        OP_8E(0xFE, 0xB87E, 0x0, 0xA03C, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5E9E)

    def lambda_5EB9():
        OP_6D(50030, 0, 43350, 3000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_5EB9)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xD, 0x1)
    WaitChrThread(0x101, 0x1)
    OP_8C(0x101, 45, 400)
    WaitChrThread(0xF7, 0x1)

    def lambda_5EF1():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_5EF1)
    Sleep(60)
    WaitChrThread(0xF8, 0x1)

    def lambda_5F09():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_5F09)
    Sleep(60)
    WaitChrThread(0xF9, 0x1)

    def lambda_5F21():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_5F21)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #239
        0x101,
        (
            "#1015F#5PHuh?\x02\x03",

            "What's going on?\x01",
            "Why are all these people looking up at--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0x102, 180, 400)

    ChrTalk(    #240
        0x102,
        (
            "#1043F#5PI see...\x02\x03",

            "#1035FSo that's it.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_8C(0x101, 180, 400)

    ChrTalk(    #241
        0x101,
        "#1020F#5PAh!\x02",
    )

    CloseMessageWindow()
    OP_59()

    def lambda_6019():
        OP_6D(48220, 8000, 35000, 5500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_6019)

    def lambda_6031():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_6031)
    Sleep(100)

    def lambda_6044():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_6044)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x1)
    Sleep(1400)
    OP_AD(0x2400CD, 0x0, 0x0, 0xC8)
    Sleep(2500)
    FadeToBright(0, 0)
    OP_6D(48890, 0, 42880, 0)
    OP_67(0, 9090, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_8C(0xF8, 180, 0)
    OP_8C(0xF9, 180, 0)
    SetMessageWindowPos(100, 300, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #242
        (
            "#1020FThe floating city?!\x02\x03",

            "It's so huge!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_613A")
    SetMessageWindowPos(250, 320, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #243
        "#065FWaaaah!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_613A")

    SetMessageWindowPos(400, 340, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #244
        "#1042FIt's overwhelming, seeing it from down here.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6295")

    ChrTalk(    #245
        0x106,
        (
            "#053FWell, I can understand why the civvies\x01",
            "are freaking out.\x02\x03",

            "#050FWe might not be able to do a hell of a\x01",
            "lot, but times like this are when bracers\x01",
            "have to step up.\x02\x03",

            "We gotta do our best to make this better\x01",
            "and give the citizens some peace.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63EF")

    label("loc_6295")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6374")

    ChrTalk(    #246
        0x103,
        (
            "#022FI can rather empathize with the panic\x01",
            "of the citizens.\x02\x03",

            "Our abilities as bracers are about to be\x01",
            "tested as never before.\x02\x03",

            "What we can actually DO might be limited,\x01",
            "but let's do everything we can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63EF")

    label("loc_6374")


    ChrTalk(    #247
        0x108,
        (
            "#072FIt is easy to see why the citizenry is\x01",
            "so terrified.\x02\x03",

            "It falls to us to do what we can to\x01",
            "alleviate their fears.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63EF")


    ChrTalk(    #248
        0x101,
        "#1002FY-Yeah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0x102,
        "#1042FYes. Let's hurry.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x20EA)
    EventEnd(0x0)
    Return()

    # Function_34_5DAB end

    def Function_35_6425(): pass

    label("Function_35_6425")

    FadeToDark(0, 0, -1)
    OP_6D(97010, 0, 95840, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
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
        (0, "loc_64DB"),
        (1, "loc_64E1"),
        (SWITCH_DEFAULT, "loc_64E7"),
    )


    label("loc_64DB")

    OP_A2(0x1200)
    Jump("loc_64E7")

    label("loc_64E1")

    OP_A2(0x1201)
    Jump("loc_64E7")

    label("loc_64E7")

    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x5, 0xFF, 0xFF, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_35_6425 end

    def Function_36_6523(): pass

    label("Function_36_6523")

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
        (0, "loc_659F"),
        (1, "loc_65A5"),
        (SWITCH_DEFAULT, "loc_65AB"),
    )


    label("loc_659F")

    OP_A2(0x1200)
    Jump("loc_65AB")

    label("loc_65A5")

    OP_A2(0x1201)
    Jump("loc_65AB")

    label("loc_65AB")

    Return()

    # Function_36_6523 end

    def Function_37_65AC(): pass

    label("Function_37_65AC")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 92)
    FadeToBright(0, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0xFF, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_37_65AC end

    def Function_38_6609(): pass

    label("Function_38_6609")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_38_6609 end

    def Function_39_6662(): pass

    label("Function_39_6662")

    SetPlaceName(0x2A)
    Return()

    # Function_39_6662 end

    def Function_40_6666(): pass

    label("Function_40_6666")

    SetPlaceName(0x26)
    Return()

    # Function_40_6666 end

    def Function_41_666A(): pass

    label("Function_41_666A")

    SetPlaceName(0x25)
    Return()

    # Function_41_666A end

    def Function_42_666E(): pass

    label("Function_42_666E")

    SetPlaceName(0x20)
    Return()

    # Function_42_666E end

    def Function_43_6672(): pass

    label("Function_43_6672")

    SetPlaceName(0x28)
    Return()

    # Function_43_6672 end

    def Function_44_6676(): pass

    label("Function_44_6676")

    SetPlaceName(0x2B)
    Return()

    # Function_44_6676 end

    def Function_45_667A(): pass

    label("Function_45_667A")

    SetPlaceName(0x21)
    Return()

    # Function_45_667A end

    def Function_46_667E(): pass

    label("Function_46_667E")

    SetPlaceName(0x27)
    Return()

    # Function_46_667E end

    SaveToFile()

Try(main)
