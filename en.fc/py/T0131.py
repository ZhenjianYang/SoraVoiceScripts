from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0131   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0131.x',
        MapIndex            = 7,
        MapDefaultBGM       = "ed60010",
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
        'Densel',                               # 9
        'Tabitha',                              # 10
        'Elissa',                               # 11
        'Faulkner',                             # 12
        'Trent',                                # 13
        'Mirano',                               # 14
        'Simon',                                # 15
        'Radford',                              # 16
        'Nial',                                 # 17
        'Paddington',                           # 18
        'Ridge',                                # 19
        'Target Camera',                        # 20
    )

    DeclEntryPoint(
        Unknown_00              = 42000,
        Unknown_04              = 0,
        Unknown_08              = 70000,
        Unknown_0C              = 270,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 7,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 40000,
        Unknown_04              = 0,
        Unknown_08              = 64000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 7,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 45000,
        Unknown_04              = 0,
        Unknown_08              = 70000,
        Unknown_0C              = 4,
        Unknown_0E              = 270,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 315,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 7,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT07/CH01280 ._CH',             # 00
        'ED6_DT07/CH01130 ._CH',             # 01
        'ED6_DT07/CH02490 ._CH',             # 02
        'ED6_DT07/CH01270 ._CH',             # 03
        'ED6_DT07/CH01503 ._CH',             # 04
        'ED6_DT07/CH01233 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
        'ED6_DT07/CH01003 ._CH',             # 07
        'ED6_DT07/CH01120 ._CH',             # 08
        'ED6_DT07/CH01250 ._CH',             # 09
        'ED6_DT07/CH01760 ._CH',             # 0A
        'ED6_DT07/CH02060 ._CH',             # 0B
        'ED6_DT06/CH20015 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH01280P._CP',             # 00
        'ED6_DT07/CH01130P._CP',             # 01
        'ED6_DT07/CH02490P._CP',             # 02
        'ED6_DT07/CH01270P._CP',             # 03
        'ED6_DT07/CH01503P._CP',             # 04
        'ED6_DT07/CH01233P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
        'ED6_DT07/CH01003P._CP',             # 07
        'ED6_DT07/CH01120P._CP',             # 08
        'ED6_DT07/CH01250P._CP',             # 09
        'ED6_DT07/CH01760P._CP',             # 0A
        'ED6_DT07/CH02060P._CP',             # 0B
        'ED6_DT06/CH20015P._CP',             # 0C
    )

    DeclNpc(
        X                   = 36450,
        Z                   = 0,
        Y                   = 126300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 4,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 82238,
        Z                   = 0,
        Y                   = 79895,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 40200,
        Z                   = 1500,
        Y                   = 78700,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 34500,
        Z                   = 0,
        Y                   = 75200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 39320,
        Z                   = 220,
        Y                   = 70940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 39570,
        Z                   = 0,
        Y                   = 66410,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 41450,
        Z                   = 0,
        Y                   = 67420,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 39480,
        Z                   = 1650,
        Y                   = 76950,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 36600,
        Z                   = 0,
        Y                   = 75170,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 36500,
        Z                   = 0,
        Y                   = 72960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 36500,
        Z                   = 0,
        Y                   = 72960,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x180,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 35580,
        TriggerZ            = 0,
        TriggerY            = 74990,
        TriggerRange        = 800,
        ActorX              = 34500,
        ActorZ              = 1500,
        ActorY              = 75200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_33E",          # 00, 0
        "Function_1_435",          # 01, 1
        "Function_2_457",          # 02, 2
        "Function_3_46D",          # 03, 3
        "Function_4_61D",          # 04, 4
        "Function_5_718",          # 05, 5
        "Function_6_188D",         # 06, 6
        "Function_7_24BA",         # 07, 7
        "Function_8_2E26",         # 08, 8
        "Function_9_4854",         # 09, 9
        "Function_10_4859",        # 0A, 10
        "Function_11_5A11",        # 0B, 11
        "Function_12_5EF9",        # 0C, 12
        "Function_13_68B6",        # 0D, 13
        "Function_14_6C95",        # 0E, 14
        "Function_15_6F06",        # 0F, 15
        "Function_16_7228",        # 10, 16
    )


    def Function_0_33E(): pass

    label("Function_0_33E")

    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_357")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_36D")

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_361")
    Jump("loc_36D")

    label("loc_361")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_36D")
    ClearChrFlags(0xF, 0x80)

    label("loc_36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_383")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8)

    label("loc_383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AA")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8)
    SetChrPos(0x10, 37320, 0, 75500, 0)

    label("loc_3AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C0")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8)

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_3DB")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8)

    label("loc_3DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_3EF")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8)
    Jump("loc_405")

    label("loc_3EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_405")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x11, 0x8)

    label("loc_405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_41E")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8)
    Jump("loc_434")

    label("loc_41E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_434")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8)

    label("loc_434")

    Return()

    # Function_0_33E end

    def Function_1_435(): pass

    label("Function_1_435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44D")
    OP_B1("t0131_y")
    Jump("loc_456")

    label("loc_44D")

    OP_B1("t0131_n")

    label("loc_456")

    Return()

    # Function_1_435 end

    def Function_2_457(): pass

    label("Function_2_457")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_46C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_457")

    label("loc_46C")

    Return()

    # Function_2_457 end

    def Function_3_46D(): pass

    label("Function_3_46D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_61C")
    Sleep(3000)
    OP_8E(0xFE, 0xA85C, 0x5DC, 0x13434, 0x9C4, 0x0)
    OP_8B(0xFE, 0x186A0, 0x13434, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0xA7B7, 0x5DC, 0x12CC8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA79B, 0x5DC, 0x129A8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA795, 0x0, 0x12296, 0x3E8, 0x0)
    OP_8E(0xFE, 0xA0F0, 0x0, 0x11940, 0x9C4, 0x0)
    OP_8B(0xFE, 0x0, 0x11940, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0xA730, 0x0, 0xFFDC, 0x7D0, 0x0)
    OP_8B(0xFE, 0x186A0, 0xFFDC, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0x8854, 0x0, 0xF974, 0x9C4, 0x0)
    OP_8B(0xFE, 0x0, 0xF938, 0x1F4)
    Sleep(3000)
    OP_8B(0xFE, 0x186A0, 0xF938, 0x1F4)
    OP_8E(0xFE, 0x90EC, 0x0, 0xFBF4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9344, 0x0, 0x10680, 0x9C4, 0x0)
    OP_8B(0xFE, 0x186A0, 0x10680, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0x81B0, 0x0, 0x10D88, 0x7D0, 0x0)
    OP_8E(0xFE, 0x81B0, 0x0, 0x121D8, 0x9C4, 0x0)
    OP_8B(0xFE, 0x0, 0x121D8, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0x8930, 0x0, 0x1320E, 0x7D0, 0x0)
    OP_8E(0xFE, 0x8E30, 0x0, 0x133DA, 0x7D0, 0x0)
    OP_8E(0xFE, 0x9D08, 0x5DC, 0x1336C, 0x9C4, 0x0)
    OP_8B(0xFE, 0x9D08, 0x0, 0x1F4)
    Jump("Function_3_46D")

    label("loc_61C")

    Return()

    # Function_3_46D end

    def Function_4_61D(): pass

    label("Function_4_61D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_717")
    Sleep(3000)
    OP_8E(0xFE, 0x8E62, 0x0, 0x1E26C, 0x7D0, 0x0)
    OP_8B(0xFE, 0x0, 0x1E26C, 0x1F4)
    Sleep(3000)
    OP_8E(0xFE, 0x9308, 0x0, 0x1DA9C, 0x7D0, 0x0)
    OP_8B(0xFE, 0x9308, 0x0, 0x1F4)
    Sleep(3000)
    OP_8B(0xFE, 0x0, 0x1DA9C, 0x1F4)
    OP_8E(0xFE, 0x8F34, 0x0, 0x1E26C, 0x9C4, 0x0)
    OP_8E(0xFE, 0x8F34, 0x0, 0x1ED5C, 0x9C4, 0x0)
    OP_8E(0xFE, 0x9470, 0x0, 0x1F144, 0x9C4, 0x0)
    OP_8E(0xFE, 0x9AB0, 0x0, 0x1F2D4, 0x9C4, 0x0)
    OP_8B(0xFE, 0x9AB0, 0x30D40, 0x1F4)
    Sleep(3000)
    OP_8B(0xFE, 0x0, 0x1F2D4, 0x1F4)
    OP_8E(0xFE, 0x8E62, 0x0, 0x1ED5C, 0x7D0, 0x0)
    OP_8B(0xFE, 0x0, 0x1ED5C, 0x1F4)
    Jump("Function_4_61D")

    label("loc_717")

    Return()

    # Function_4_61D end

    def Function_5_718(): pass

    label("Function_5_718")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 1)), scpexpr(EXPR_END)), "loc_1859")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, 36520, 0, 73960, 0)
    SetChrPos(0x102, 37840, 0, 73590, 315)
    OP_8C(0x10, 180, 0)
    ClearMapFlags(0x1)
    OP_51(0x13, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x10, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x13, 0x3E8)
    OP_A2(0x252)
    OP_28(0x19, 0x1, 0x8)
    OP_28(0x19, 0x1, 0x10)
    OP_28(0x19, 0x1, 0x20)
    OP_28(0x8, 0x4, 0x40)
    OP_28(0xB, 0x4, 0x40)
    OP_4F(0x17, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x10, 0x40)

    NpcTalk(    #0
        0x10,
        "Unshaven Man",
        (
            "#142FHuh? Who are you kids supposed\x01",
            "to be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#000FAre you perhaps...the reporter from\x01",
            "the Liberl News?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #2
        0x10,
        "Unshaven Man",
        (
            "#142FThat's right, but...how do you\x01",
            "know that?\x02\x03",

            "#142FI like getting the scoop on things,\x01",
            "but I hate it when people try and\x01",
            "pry into my life.\x02\x03",

            "#142FWhat business do you have\x01",
            "with me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x102,
        (
            "#010F#4PWe're here representing the Bracer\x01",
            "Guild. We were told that you had\x01",
            "requested an escort.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #4
        0x10,
        "Unshaven Man",
        (
            "#147FOh, so you've finally come, have\x01",
            "you? I've been waiting forever for\x01",
            "you guys to show up.\x02\x03",

            "#141FSo, uh...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10, 45, 400)
    OP_8C(0x10, 180, 400)
    TurnDirection(0x10, 0x101, 400)

    NpcTalk(    #5
        0x10,
        "Unshaven Man",
        "#143FWhere's Cassius Bright?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#007FUm, well the thing is...\x01",
            "He had another job come up.\x02\x03",

            "#007FSo he's not even in Rolent...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #7
        0x10,
        "Unshaven Man",
        (
            "#142FWh-What?!\x02\x03",

            "#142FI came all the way here so I could\x01",
            "get a story on this famous bracer...\x02\x03",

            "#145FCrap...what a waste this trip\x01",
            "turned out to be!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#001FI don't get what you're so disappointed\x01",
            "about, but there's no need to get your\x01",
            "boxers in a bunch.\x02\x03",

            "#001FWe've got you covered! ♪\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #9
        0x10,
        "Unshaven Man",
        (
            "#145FI guess I don't have much of a\x01",
            "choice... You'll have to do...\x02\x03",

            "#145F...\x02\x03",

            "#142FWait. What did you just say...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #10
        0x101,
        "#501F'Don't get your boxers in a bunch'?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #11
        0x10,
        "Unshaven Man",
        (
            "#144FNo, the 'We've got you covered!'\x01",
            "part.\x02\x03",

            "#144FWhat do you mean by that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#000FIt's just like Joshua said, we're\x01",
            "your representative bracers.\x02\x03",

            "#000FOh, and here's our referral.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #13
        "\x07\x00Handed over \x07\x02Guild Referral\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x324, 1)

    NpcTalk(    #14
        0x10,
        "Unshaven Man",
        (
            "#142FHey, this has got to be some\x01",
            "kind of bad joke...\x02\x03",

            "#142FAre you trying to tell me that you\x01",
            "little brats are bracers?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x101,
        (
            "#009FB-Brats?! Is that how you're supposed\x01",
            "to address a lady?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #16
        0x10,
        "Unshaven Man",
        (
            "#141FWhaddya mean, 'lady'?\x01",
            "There's nothing sexy about\x01",
            "you in that outfit!\x02\x03",

            "#141FIf you don't like my assessment, then how\x01",
            "about slipping into a skirt and acting\x01",
            "like all the other girls your age.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#005FThis clothing is specifically designed\x01",
            "for those who wield a staff! And this\x01",
            "looks like a skirt, too! Are you blind?!\x02\x03",

            "#005FYou're such a rude old man...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #18
        0x10,
        "Unshaven Man",
        (
            "#144FWh-Who are you calling an 'old man'?!\x01",
            "I'm still in my 20's, damn it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#017F#4PGetting back to business, sir...\x02\x03",

            "#017FThe fact is that we were dispatched\x01",
            "by the guild.\x02\x03",

            "#010FI'd be more than happy to introduce\x01",
            "you to someone else, but I don't\x01",
            "know when they'll be free.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    NpcTalk(    #20
        0x10,
        "Unshaven Man",
        (
            "#145FArgh...I can't extend the deadline\x01",
            "any longer...\x02\x03",

            "#145FI guess I've got no other alternative.\x02\x03",

            "#141FAll right, rejoice, you kids.\x01",
            "I'm going to leave this up to you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#009FWhat a generous old man\x01",
            "you are...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x102,
        (
            "#010F#4PEasy, Estelle.\x02\x03",

            "#010FI'm Joshua, and this here\x01",
            "is Estelle...\x02\x03",

            "#010FAnd you are...?\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #23
        0x10,
        "Unshaven Man",
        (
            "#141FI'm Nial Burns, ace reporter for\x01",
            "the Liberl News.\x02\x03",

            "#141FThough we won't be working long\x01",
            "together, I hope you'll do a good\x01",
            "job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#009FHmph. I'll be grateful when this\x01",
            "is all over, too.\x02\x03",

            "#007FBy the way...where is it exactly that\x01",
            "you want us to guide you to?\x02\x03",

            "#007FThe way I see it, you need a trusty\x01",
            "guide because you're headed\x01",
            "somewhere dangerous, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#140FRight. My destination is the Esmelas\x01",
            "Tower. I'm sure you've heard of it\x01",
            "before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#006FHa! That's it?\x02\x03",

            "#006FNot only have we heard of it, but we\x01",
            "were there on a job not that long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#141FWell, this may just work out\x01",
            "after all.\x02\x03",

            "#141FSo, what I really want you to do\x01",
            "is guide us to the tower roof.\x02\x03",

            "#141FI want to get a picture for\x01",
            "the magazine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        "#000FWell, aren't you the thrill seeker.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#010F#4PBy 'us' do you mean that someone\x01",
            "else is coming along too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "#140FYeah, I've got my camerawoman\x01",
            "with me.\x02\x03",

            "#140FShe said something about her orbal\x01",
            "camera not working right, so she\x01",
            "took off to the orbal factory...\x02\x03",

            "#142FBut she should have been back\x01",
            "by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#000FIf you're in a hurry, then wouldn't it\x01",
            "be a good idea to head over there now?\x02\x03",

            "#000FNo doubt you're going to take off\x01",
            "to get your story once you meet\x01",
            "up with your partner, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "#140FYeah, that's true...\x02\x03",

            "#140FAll right, then. Let's head straight to\x01",
            "the tower once we pick up my partner\x01",
            "from the orbal factory.\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x10, 0x0, 0x0, 0xBB8, 0x0)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8)
    OP_92(0x1, 0x0, 0x0, 0xBB8, 0x0)
    AddParty(0xE, 0xFF)
    EventEnd(0x0)
    SetMapFlags(0x1)
    Jump("loc_1889")

    label("loc_1859")


    NpcTalk(    #33
        0x10,
        "Unshaven Man",
        "#145FOh, man, I'm starving...\x02",
    )

    CloseMessageWindow()

    label("loc_1889")

    TalkEnd(0x10)
    Return()

    # Function_5_718 end

    def Function_6_188D(): pass

    label("Function_6_188D")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_1A14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1978")
    OP_A2(0x0)

    ChrTalk(    #34
        0xFE,
        (
            "It appears that the new menu\x01",
            "is being well received.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "The menu that Elissa thought up\x01",
            "is especially popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "I might as well hire a new waitress\x01",
            "and get Elissa to help me in the\x01",
            "kitchen full-time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A11")

    label("loc_1978")


    ChrTalk(    #37
        0xFE,
        (
            "The menu that Elissa thought up\x01",
            "is especially popular.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I might as well hire a new waitress\x01",
            "and get Elissa to help me in the\x01",
            "kitchen full-time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A11")

    Jump("loc_24B6")

    label("loc_1A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_1BB3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B41")
    OP_A2(0x0)
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #39
        0xFE,
        (
            "Hey there, Scherazard!\x01",
            "Are you back for another drink?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "I've got some new liquor in that\x01",
            "I think you might like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        "I hope you'll come and have a taste.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x103,
        (
            "#020FWell, I'm really happy to hear that.\x01",
            "I'll have to stop by when I finish up\x01",
            "with some of this work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BB0")

    label("loc_1B41")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #43
        0xFE,
        (
            "I've got some new liquor in that\x01",
            "I think you might like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "I hope you'll come and have a taste.\x02",
    )

    CloseMessageWindow()

    label("loc_1BB0")

    Jump("loc_24B6")

    label("loc_1BB3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_1CDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C86")
    OP_A2(0x0)

    ChrTalk(    #45
        0xFE,
        (
            "It's time I started thinking about\x01",
            "a new menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "I'm going to have all of the staff\x01",
            "here give me their ideas for the\x01",
            "new menu.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "Maybe I should ask Elissa what\x01",
            "she thinks, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CD9")

    label("loc_1C86")


    ChrTalk(    #48
        0xFE,
        (
            "I'm going to have all of the staff\x01",
            "here give me their ideas for the\x01",
            "new menu.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD9")

    Jump("loc_24B6")

    label("loc_1CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_1F6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA7")
    OP_A2(0x0)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #49
        0xFE,
        "Hey, Estelle, do you cook?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#501FAh ha ha, the only meals I cook...\x02\x03",

            "#007F...are the ones I have to make when\x01",
            "it's my turn at home...and well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "It's always best to start with something\x01",
            "simple if you have trouble cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "First, you get your ingredients and\x01",
            "cookware together, and then it's\x01",
            "time to put your all into it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Cooking can be a useful skill\x01",
            "in many ways, and you've got\x01",
            "nothing to lose by trying.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F69")

    label("loc_1EA7")


    ChrTalk(    #54
        0xFE,
        (
            "First you get your ingredients and\x01",
            "cookware together, and then it's\x01",
            "time to put your all into it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Cooking can be a useful skill\x01",
            "in many ways, and you've got\x01",
            "nothing to lose by trying.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F69")

    Jump("loc_24B6")

    label("loc_1F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_20B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2053")
    OP_A2(0x0)

    ChrTalk(    #56
        0xFE,
        (
            "I just got a message from the\x01",
            "Perzel Farm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "They said that the vegetables\x01",
            "should come in any time now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "I'm getting my vegetables from\x01",
            "somewhere else at the moment,\x01",
            "but Perzel Farm's are the best.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20B5")

    label("loc_2053")


    ChrTalk(    #59
        0xFE,
        (
            "I'm getting my vegetables from\x01",
            "somewhere else at the moment,\x01",
            "but Perzel Farm's are the best.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20B5")

    Jump("loc_24B6")

    label("loc_20B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2133")

    ChrTalk(    #60
        0xFE,
        (
            "The vegetables from the Perzel Farm\x01",
            "haven't come in as scheduled.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "I wonder what could have happened...\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B6")

    label("loc_2133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_21D7")

    ChrTalk(    #62
        0x8,
        (
            "Whew, we're busy. This is the time\x01",
            "this place gets the most crowded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x8,
        (
            "After I finish with all these orders,\x01",
            "I'll need to get ready for tomorrow.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24B6")

    label("loc_21D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_234B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D9")
    OP_A2(0x0)

    ChrTalk(    #64
        0x8,
        (
            "In my opinion, there are two kinds\x01",
            "of enjoyment that come from food.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x8,
        (
            "Put bluntly, they are eating and\x01",
            "cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "But I think my passion for cooking\x01",
            "outweighs the other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        (
            "Of course, I enjoy eating delicious\x01",
            "food as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2348")

    label("loc_22D9")


    ChrTalk(    #68
        0x8,
        (
            "The joy of eating, and the joy\x01",
            "of cooking...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        (
            "But I think my passion for cooking\x01",
            "outweighs the other.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2348")

    Jump("loc_24B6")

    label("loc_234B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2470")
    OP_A2(0x2AA)

    ChrTalk(    #70
        0x8,
        (
            "Yo, Estelle and Joshua!\x01",
            "Aren't you a pair of early birds today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        "#000FGood morning.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        "#010FGood morning, Mr. Densel.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "In response to the requests of my\x01",
            "customers, I started offering\x01",
            "breakfast.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        "Today's special is Wholesome Pasta.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        "It's superbly al dente.\x02",
    )

    CloseMessageWindow()
    Jump("loc_24B6")

    label("loc_2470")


    ChrTalk(    #76
        0x8,
        "Today's special is Wholesome Pasta.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        "It's superbly al dente.\x02",
    )

    CloseMessageWindow()

    label("loc_24B6")

    TalkEnd(0x8)
    Return()

    # Function_6_188D end

    def Function_7_24BA(): pass

    label("Function_7_24BA")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_2573")

    ChrTalk(    #78
        0xFE,
        (
            "The new menu is so popular that\x01",
            "we're always running out of\x01",
            "ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        (
            "This is terribly ineffective, so\x01",
            "I think we'll need to reexamine\x01",
            "how we stock our goods.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E22")

    label("loc_2573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_25C4")
    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #80
        0xFE,
        "Well, hi there, Schera.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        "Please make yourself at home.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E22")

    label("loc_25C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_2773")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26C4")
    OP_A2(0x1)

    ChrTalk(    #82
        0xFE,
        (
            "We started this restaurant before\x01",
            "my husband and I were married.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "That's why we have such a\x01",
            "special fondness for the place.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "Somehow I find myself deeply moved\x01",
            "when I see our daughter, Elissa,\x01",
            "helping around here as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2770")

    label("loc_26C4")


    ChrTalk(    #85
        0xFE,
        (
            "We started this restaurant before\x01",
            "my husband and I were married.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Somehow I find myself deeply moved\x01",
            "when I see our daughter, Elissa,\x01",
            "helping around here as well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2770")

    Jump("loc_2E22")

    label("loc_2773")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_289A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2846")
    OP_A2(0x1)

    ChrTalk(    #87
        0xFE,
        (
            "So the bracer combo who's been\x01",
            "having a great showing is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "...the two of you, Joshua and Estelle?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Maybe I should brag that these same\x01",
            "bracers are the friends of my daughter.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2897")

    label("loc_2846")


    ChrTalk(    #90
        0xFE,
        (
            "Maybe I should brag that these same\x01",
            "bracers are the friends of my daughter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2897")

    Jump("loc_2E22")

    label("loc_289A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_293E")

    ChrTalk(    #91
        0xFE,
        (
            "The Perzel Farm looks like they'll\x01",
            "start shipping vegetables again soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "I hear that they had their fields ravaged,\x01",
            "so they hired some bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E22")

    label("loc_293E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_2AB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A46")
    OP_A2(0x1)

    ChrTalk(    #93
        0xFE,
        (
            "We received a message from the\x01",
            "Perzel Farm saying they wouldn't be\x01",
            "able to ship vegetables for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "I wonder what could have\x01",
            "happened up at the farm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "I guess I'll have to make immediate\x01",
            "arrangements with another supplier.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB3")

    label("loc_2A46")


    ChrTalk(    #96
        0xFE,
        (
            "We received a message from the\x01",
            "Perzel Farm saying they wouldn't be\x01",
            "able to ship vegetables for a while.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB3")

    Jump("loc_2E22")

    label("loc_2AB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_2B43")

    ChrTalk(    #97
        0x9,
        (
            "Let's see... That should be about\x01",
            "it with the accounting for today...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x9,
        (
            "I'd better get ready to close up\x01",
            "shop for the day.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E22")

    label("loc_2B43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_2D03")
    TurnDirection(0x9, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C8B")
    OP_A2(0x1)

    ChrTalk(    #99
        0x9,
        (
            "Well, Estelle. I haven't seen you\x01",
            "around here for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x9,
        (
            "It's been some time since you\x01",
            "graduated from Sunday School,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        "Did you say 'hi' to Elissa?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        (
            "She started helping around here\x01",
            "not too long ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x9,
        (
            "Please visit her if you have some\x01",
            "time. She's been wanting to see you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D00")

    label("loc_2C8B")


    ChrTalk(    #104
        0x9,
        (
            "Did you speak with Elissa,\x01",
            "Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x9,
        (
            "I'm sure she's helping around the\x01",
            "place, so why don't you say 'hello'?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D00")

    Jump("loc_2E22")

    label("loc_2D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DB6")
    OP_A2(0x1)

    ChrTalk(    #106
        0x9,
        (
            "Let's see...\x01",
            "Yesterday's sales totaled...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        (
            "Hmm...our breakfast service has\x01",
            "been going really well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x9,
        (
            "Sometimes my husband comes up\x01",
            "with some good ideas.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E22")

    label("loc_2DB6")


    ChrTalk(    #109
        0x9,
        (
            "Let's see...\x01",
            "Yesterday's sales totaled...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x9,
        (
            "Hmm...our breakfast service has\x01",
            "been going really well.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E22")

    TalkEnd(0x9)
    Return()

    # Function_7_24BA end

    def Function_8_2E26(): pass

    label("Function_8_2E26")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_3037")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC1")
    OP_A2(0x3)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #111
        0xFE,
        "If it isn't Estelle and Joshua!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        "What's with all the baggage?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#000FUm, actually...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #114
        "\x07\x05Estelle explained that they were heading to Bose.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #115
        0xFE,
        "Oh, I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "I'd be worried too, if I were in your\x01",
            "shoes. You should probably get\x01",
            "going then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "Waiting around certainly isn't\x01",
            "your style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#001FAh ha ha...you're right.\x01",
            "I'll be going then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3034")

    label("loc_2FC1")


    ChrTalk(    #119
        0xFE,
        (
            "Things have taken a turn for the\x01",
            "worse, haven't they?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #120
        0xFE,
        (
            "Joshua, make sure to support\x01",
            "Estelle, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3034")

    Jump("loc_4850")

    label("loc_3037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_31B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3169")
    OP_A2(0x3)

    ChrTalk(    #121
        0xFE,
        (
            "Ah, Estelle and Joshua.\x01",
            "Welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x103,
        "#020FHi, Elissa.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #123
        0xFE,
        (
            "And, Scherazard, you're here too...\x01",
            "Are you here for a drink today?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Please try not to tease Mr. Faulkner,\x01",
            "okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x103,
        (
            "#021FI wasn't teasing him at all if\x01",
            "that's what he thought.\x02\x03",

            "#027FI was just cuddling him!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31AD")

    label("loc_3169")

    TurnDirection(0xFE, 0x103, 0)

    ChrTalk(    #126
        0xFE,
        (
            "Scherazard, please try not to tease\x01",
            "Mr. Faulkner, okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AD")

    Jump("loc_4850")

    label("loc_31B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_3366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330E")
    OP_A2(0x3)
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #127
        0xFE,
        "Estelle, listen to this!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "The other day Mr. Rinon's mother\x01",
            "dropped by and asked me out of the\x01",
            "blue if I wanted to marry her son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "I haven't felt so surprised since\x01",
            "Scherazard fell off the table when\x01",
            "she was dancing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "But I had to turn her down.\x01",
            "When I'm ready, I want to be\x01",
            "able to choose my own partner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3363")

    label("loc_330E")


    ChrTalk(    #131
        0xFE,
        (
            "Mr. Rinon's getting older. I'm sure\x01",
            "that's why his mother is worried\x01",
            "about him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3363")

    Jump("loc_4850")

    label("loc_3366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_3497")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_341D")
    OP_A2(0x3)

    ChrTalk(    #132
        0xFE,
        (
            "The other day, Scherazard came\x01",
            "for a drink and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "...well...she was just as unbelievable\x01",
            "as you said, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        "I don't even dare say what she did.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3494")

    label("loc_341D")


    ChrTalk(    #135
        0xFE,
        (
            "The other day Scherazard came\x01",
            "for a drink and...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        (
            "...well...she was just unbelievable\x01",
            "like you said, Estelle!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3494")

    Jump("loc_4850")

    label("loc_3497")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_3516")

    ChrTalk(    #137
        0xFE,
        (
            "Estelle, Joshua, how's your own\x01",
            "work coming along?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "Come and take a break here every\x01",
            "once in a while, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4850")

    label("loc_3516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_3717")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36B0")
    OP_A2(0x3)

    ChrTalk(    #139
        0xFE,
        (
            "So you've finally taken your first\x01",
            "step as bracers, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "Your names are already being\x01",
            "mentioned among the customers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x101,
        "#008FR-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xFE,
        (
            "Rolent may be in the country, but\x01",
            "we've got some famous people here\x01",
            "like Cassius and Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "Now, I just wonder how you're going\x01",
            "to break into the big leagues.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        (
            "#007FOh, come on, Elissa. Please don't\x01",
            "put so much pressure on me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3714")

    label("loc_36B0")


    ChrTalk(    #145
        0xFE,
        (
            "So you've finally taken your first\x01",
            "step as bracers, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "Wishing you the best of luck! ★\x02",
    )

    CloseMessageWindow()

    label("loc_3714")

    Jump("loc_4850")

    label("loc_3717")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_3C4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_380B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D4")
    OP_A2(0x3)

    ChrTalk(    #147
        0xA,
        "Welcome, you two. ★\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xA,
        (
            "Stop by and have a bite to eat\x01",
            "every once in a while, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xA,
        (
            "If I ask my mom and dad, I can\x01",
            "probably get you a free meal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3808")

    label("loc_37D4")


    ChrTalk(    #150
        0xA,
        (
            "You can bring your whole family\x01",
            "if you'd like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3808")

    Jump("loc_3C48")

    label("loc_380B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C12")
    OP_A2(0x2A9)

    ChrTalk(    #151
        0xA,
        "Welcome. ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xA,
        "Oh, Estelle and Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x102,
        "#010FIt's been a while, hasn't it, Elissa?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0xA,
        "Is there something going on today?\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #155
        0xA,
        (
            "...Could it be that you're on a date\x01",
            "together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        "#008FAh ha ha...not in a million years.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xA,
        (
            "That reminds me. The both of you\x01",
            "were planning on becoming bracers,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xA,
        "Whatever happened with that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#000FWell...why don't you have a look?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #160
        (
            "\x07\x05Estelle showed the emblem on\x01",
            "her jacket to Elissa.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #161
        0xA,
        (
            "What?! So you passed?!\x01",
            "Congratulations!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xA,
        (
            "You've always wanted to be a\x01",
            "bracer ever since you were a kid,\x01",
            "haven't you, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        "#000FHa ha, I guess I did, didn't I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xA,
        (
            "Oh right, how about we celebrate\x01",
            "before you go?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xA,
        (
            "If I ask my mom and dad, I can\x01",
            "probably get you a free meal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x101,
        "#001FSeriously?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x102,
        (
            "#018FNo can do, Estelle.\x01",
            "Dad's waiting for us at home.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#007FOh, I forgot about that.\x02\x03",

            "#501FI'm really sorry, Elissa...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0xA,
        "Oh, sure. It's no problem.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        (
            "Next time, come in and eat\x01",
            "as a family.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C48")

    label("loc_3C12")


    ChrTalk(    #171
        0xA,
        (
            "Estelle, next time, come in\x01",
            "and eat as a family.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C48")

    Jump("loc_4850")

    label("loc_3C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_446F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_4013")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x55, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F93")
    OP_A2(0x2A8)

    ChrTalk(    #172
        0xA,
        (
            "Really? You're completely finished\x01",
            "with your training?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        (
            "#001FYay! We finally finished, Elissa!\x02\x03",

            "#001FI am OFFICIALLY a real bracer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xA,
        "Well, congratulations, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xA,
        (
            "You've always wanted to be a\x01",
            "bracer ever since you were a kid,\x01",
            "haven't you, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xA,
        (
            "But don't bracers have a lot of\x01",
            "dangerous jobs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        "#501FYeah, something like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        (
            "Joshua, Estelle, don't overdo it,\x01",
            "and watch out for each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0xA,
        (
            "Estelle has this tendency to\x01",
            "get in over her head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x102,
        (
            "#010FThat's a very good observation,\x01",
            "Elissa.\x02\x03",

            "#015FThe only problem is that Estelle\x01",
            "doesn't realize this herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        (
            "#009FHmph.\x01",
            "I'm standing right here, you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0xA,
        (
            "Joshua and I just care about you,\x01",
            "Estelle. That's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0xA,
        (
            "Anyway, don't get too full of yourself\x01",
            "and end up getting hurt, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        "#007FOkay, okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_4010")

    label("loc_3F93")


    ChrTalk(    #185
        0xA,
        (
            "Joshua, Estelle, don't overdo it,\x01",
            "and watch out for each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xA,
        (
            "Estelle has this tendency to\x01",
            "get in over her head.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4010")

    Jump("loc_446C")

    label("loc_4013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43EF")
    OP_A2(0x3)
    OP_A2(0x211)

    ChrTalk(    #187
        0xA,
        "Welcome. ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xA,
        "Oh, Estelle and Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x102,
        (
            "#010FIt's been a while, hasn't it,\x01",
            "Elissa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xA,
        (
            "Is there something going\x01",
            "on today?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #191
        0xA,
        (
            "...Could it be that you're on a date\x01",
            "together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x101,
        (
            "#000FYeah right! But anyway,\x01",
            "check this out!\x02\x03",

            "#001FI am OFFICALLY a real bracer!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0xA,
        "Well, congratulations, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xA,
        (
            "You've always wanted to be a\x01",
            "bracer ever since you were a kid,\x01",
            "haven't you, Estelle?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xA,
        (
            "But don't bracers have a lot of\x01",
            "dangerous jobs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#000FYeah, something like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xA,
        (
            "Joshua, Estelle, don't overdo it,\x01",
            "and watch out for each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xA,
        (
            "Estelle has this tendency to\x01",
            "get in over her head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x102,
        (
            "#010FThat's a very good observation,\x01",
            "Elissa.\x02\x03",

            "#015FThe only problem is that Estelle\x01",
            "doesn't realize this herself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        (
            "#009FHmph.\x01",
            "I'm standing right here, you guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xA,
        (
            "Joshua and I just care about you,\x01",
            "Estelle. That's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xA,
        (
            "Anyway, don't get too full of yourself\x01",
            "and end up getting hurt, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x101,
        "#007FOkay, okay...\x02",
    )

    CloseMessageWindow()
    Jump("loc_446C")

    label("loc_43EF")


    ChrTalk(    #204
        0xA,
        (
            "Joshua, Estelle, don't overdo it,\x01",
            "and watch out for each other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xA,
        (
            "Estelle has this tendency to\x01",
            "get in over her head.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_446C")

    Jump("loc_4850")

    label("loc_446F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x54, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47C1")
    OP_A2(0x2A7)
    OP_A2(0x210)

    ChrTalk(    #206
        0xA,
        "Welcome. ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xA,
        "Oh, Estelle and Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0x102,
        (
            "#010FIt's been a while, hasn't it,\x01",
            "Elissa?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xA,
        (
            "Is there something going\x01",
            "on today?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #210
        0xA,
        (
            "...Could it be that you're on a date\x01",
            "together?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0x101,
        (
            "#000FYeah, right! We're actually on\x01",
            "our way to bracer training now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xA,
        "Oh, is that all?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xA,
        (
            "Everyone from Sunday School seems\x01",
            "to have decided on a career or goal\x01",
            "and is working hard to achieve it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xA,
        (
            "As expected, you're a bit different\x01",
            "than everyone else, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0x101,
        (
            "#006FWhat? Is there something wrong\x01",
            "with that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xA,
        (
            "No, not at all. I just thought it was\x01",
            "very like you to pick the unusual\x01",
            "route, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xA,
        (
            "Oh, that's right. Tio decided that\x01",
            "she was going to help out at her\x01",
            "parents' farm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xA,
        (
            "She even said for us all to go up\x01",
            "and visit her sometime.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x101,
        (
            "#004FSo that's what Tio decided\x01",
            "on, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4850")

    label("loc_47C1")


    ChrTalk(    #220
        0xA,
        (
            "Everyone from Sunday School seems\x01",
            "to have decided on a career or goal\x01",
            "and is working hard to achieve it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #221
        0xA,
        "Anyway, good luck, Estelle.\x02",
    )

    CloseMessageWindow()

    label("loc_4850")

    TalkEnd(0xA)
    Return()

    # Function_8_2E26 end

    def Function_9_4854(): pass

    label("Function_9_4854")

    Call(0, 10)
    Return()

    # Function_9_4854 end

    def Function_10_4859(): pass

    label("Function_10_4859")

    TalkBegin(0xB)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                              # 0
            "Shop\x01",                              # 1
            "[Wholesome Pasta] - 100 mira\x01",      # 2
            "Leave\x01",                             # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48E2")
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_48D7")
    OP_A9(0x75)
    Jump("loc_48D9")

    label("loc_48D7")

    OP_A9(0x5)

    label("loc_48D9")

    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_48E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49F0")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_49B6")
    SubMira(100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #222
        "\x06\x07\x00Ate \x07\x02Wholesome Pasta\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0xB4)
    OP_31(0x1, 0xFD, 0xB4)
    OP_31(0x2, 0xFD, 0xB4)
    OP_31(0x3, 0xFD, 0xB4)
    OP_31(0x4, 0xFD, 0xB4)
    OP_31(0x5, 0xFD, 0xB4)
    OP_31(0x6, 0xFD, 0xB4)
    OP_31(0x7, 0xFD, 0xB4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_49A8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x3)"), scpexpr(EXPR_END)), "loc_4977")
    Jump("loc_49A8")

    label("loc_4977")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #223
        "\x06\x07\x00Learned '\x07\x02Wholesome Pasta\x07\x00' recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_49A8")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_49DE")

    label("loc_49B6")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #224
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_49DE")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xB)
    Return()

    label("loc_49F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A0A")
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_4A0A")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_4B6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ADD")
    OP_A2(0x2)

    ChrTalk(    #225
        0xB,
        (
            "That reminds me, I heard the\x01",
            "mayor's place got robbed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xB,
        (
            "Breaking into the mayor's home of all\x01",
            "places, now that's what I call bold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xB,
        "I'm just glad that nobody was hurt.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B69")

    label("loc_4ADD")


    ChrTalk(    #228
        0xB,
        (
            "That reminds me, I heard the\x01",
            "mayor's place got robbed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xB,
        (
            "Breaking into the mayor's home of all\x01",
            "places, now that's what I call bold.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B69")

    Jump("loc_5A0D")

    label("loc_4B6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_END)), "loc_4DEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DA5")
    OP_A2(0x2)

    ChrTalk(    #230
        0x103,
        "#020FHello, Faulkner!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x103, 400)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #231
        0xB,
        "Aaah! Sch-Sch-Scherazard?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xB,
        "G-Good day to you!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0x103,
        (
            "#027FWhy so tense? You needn't worry,\x01",
            "I'm on duty right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xB,
        (
            "P-Praise the Goddess. Er... I mean...\x01",
            "we appreciate your hard work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0x103,
        (
            "#027FHeehee! When I'm done today,\x01",
            "how about I stop by and we have a\x01",
            "drink together?\x02\x03",

            "#027FI'll be looking forward to seeing\x01",
            "you later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xB,
        "Ha...ha ha... I'll be...here waiting...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0x101,
        (
            "#007F(Nothing inspires fear like Schera's\x01",
            "drunken company.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x102,
        "#017F(Except maybe your cooking...)\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DE7")

    label("loc_4DA5")


    ChrTalk(    #239
        0xB,
        (
            "M-Maybe I should get out of here\x01",
            "sooner rather than later...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DE7")

    Jump("loc_5A0D")

    label("loc_4DEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_5133")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50A7")
    OP_A2(0x2)

    ChrTalk(    #240
        0xB,
        (
            "All the members of the Bracer Guild\x01",
            "can hold their liquor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xB,
        (
            "Scherazard is like a booze-sponge,\x01",
            "but even Cassius can down more\x01",
            "than a few rounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #242
        0xB,
        (
            "But Aina is the most surprising\x01",
            "of them all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x102,
        (
            "#010FI heard the same thing from Schera.\x01",
            "Aina's supposed to be pretty amazing\x01",
            "in the liquor department.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #244
        0xB,
        (
            "That's right. She can drink at\x01",
            "the same pace as Scherazard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xB,
        (
            "On top of that, her face never gets red,\x01",
            "and she acts totally normal!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0x101,
        (
            "#506FHa ha. I think that's much better than\x01",
            "having your ear talked off by Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xB,
        (
            "In any case, the Bracer Guild is\x01",
            "one to be reckoned with at a bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xB,
        (
            "Oh...except for that Ridge fellow.\x01",
            "One drink and he's a goner.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5130")

    label("loc_50A7")


    ChrTalk(    #249
        0xB,
        (
            "I'm just astounded that there's\x01",
            "anyone who can drink at the\x01",
            "same pace as Scherazard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xB,
        (
            "That's what makes Aina\x01",
            "doubly-surprising.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5130")

    Jump("loc_5A0D")

    label("loc_5133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_5391")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5320")
    OP_A2(0x2)

    ChrTalk(    #251
        0xB,
        (
            "Scherazard came here the\x01",
            "other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0xB,
        (
            "And I got stuck drinking with her\x01",
            "even after closing hours...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xB,
        (
            "Even after emptying five bottles\x01",
            "of my strongest stuff she still\x01",
            "didn't act the least bit drunk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0x101,
        (
            "#501FYeah, Schera going from tipsy\x01",
            "to totally wasted is, well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x102,
        (
            "#010FI don't even want to imagine\x01",
            "what would happen...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0xB,
        (
            "Elissa went and hid, and the chef\x01",
            "went home...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xB,
        (
            "I was so dead, I could hardly work\x01",
            "the next day. I still feel pickled...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_538E")

    label("loc_5320")


    ChrTalk(    #258
        0xB,
        (
            "Scherazard came here the\x01",
            "other day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xB,
        (
            "And I got stuck drinking with her\x01",
            "even after closing hours...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_538E")

    Jump("loc_5A0D")

    label("loc_5391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_55E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_553A")
    OP_A2(0x2)

    ChrTalk(    #260
        0xB,
        (
            "You have that foreigner named\x01",
            "Scherazard at the Rolent branch,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xB,
        (
            "Not only is she attractive, but\x01",
            "she's one of my best customers.\x01",
            "Which I'm thankful for, of course...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xB,
        (
            "But when it comes to liquor,\x01",
            "she's unbelievable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xB,
        (
            "And when I say 'unbelievable'\x01",
            "I mean...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0x101,
        "#501FHa ha. Oh, we know.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x102,
        "#015FI can empathize.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0xB,
        (
            "She's normally such a beautiful, friendly\x01",
            "young woman, too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55DE")

    label("loc_553A")


    ChrTalk(    #267
        0xB,
        (
            "When Scherazard comes alone, I'm\x01",
            "afraid, because I'm the one who gets\x01",
            "stuck talking to her all night!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xB,
        (
            "She's normally a beautiful, friendly\x01",
            "young woman...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55DE")

    Jump("loc_5A0D")

    label("loc_55E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_564F")

    ChrTalk(    #269
        0xB,
        (
            "The chef suddenly said something\x01",
            "about changing his supplier...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xB,
        "I wonder what's going on.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5A0D")

    label("loc_564F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_57B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_571C")
    OP_A2(0x2)

    ChrTalk(    #271
        0xB,
        (
            "The chef here makes good use of\x01",
            "his ingredients to really bring out\x01",
            "that hometown flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xB,
        "Rolent has a lot of farms, right?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0xB,
        (
            "Personally, I recommend our\x01",
            "vegetarian menu.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57AD")

    label("loc_571C")


    ChrTalk(    #274
        0xB,
        (
            "The chef here makes good use of\x01",
            "his ingredients to really bring out\x01",
            "that hometown flavor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xB,
        (
            "Personally, I recommend our\x01",
            "vegetarian menu.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57AD")

    Jump("loc_5A0D")

    label("loc_57B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_594F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58C4")
    OP_A2(0x2)

    ChrTalk(    #276
        0xB,
        (
            "It looks like that female merchant\x01",
            "over there came from Bose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xB,
        (
            "Not only does she seem smart,\x01",
            "but she's extremely attractive\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xB,
        (
            "Then again, she'd probably never\x01",
            "give me the time of day...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xB,
        (
            "Her accent is a little different\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_594C")

    label("loc_58C4")


    ChrTalk(    #280
        0xB,
        (
            "That female merchant not only seems\x01",
            "smart, but she's extremely attractive\x01",
            "as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xB,
        (
            "Her accent is a little different\x01",
            "though...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_594C")

    Jump("loc_5A0D")

    label("loc_594F")


    ChrTalk(    #282
        0xB,
        (
            "I started working here because the\x01",
            "owner said he'd let me manage the\x01",
            "bar.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xB,
        (
            "After they started the morning and\x01",
            "lunch service, however, I've been\x01",
            "more of a waiter than anything else.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A0D")

    TalkEnd(0xB)
    Return()

    # Function_10_4859 end

    def Function_11_5A11(): pass

    label("Function_11_5A11")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_5B30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AFB")
    OP_A2(0x4)

    ChrTalk(    #284
        0xFE,
        "*crunch* *smack* *slurp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        "*chew chew chew*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        "*munch munch munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #287
        0xFE,
        "*guuuuuulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "That reminds me.\x01",
            "I saw the boss here in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0xFE,
        (
            "I'd better be careful so he doesn't\x01",
            "catch me ditching work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B2D")

    label("loc_5AFB")


    ChrTalk(    #290
        0xFE,
        "*chomp chomp* *munch munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        "*guuuuuulp*\x02",
    )

    CloseMessageWindow()

    label("loc_5B2D")

    Jump("loc_5EF5")

    label("loc_5B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5C3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C17")
    OP_A2(0x4)

    ChrTalk(    #292
        0xFE,
        "*crunch* *smack* *slurp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0xFE,
        "*chew chew chew*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        "*munch munch munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        "*guuuuuulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0xFE,
        (
            "The whole monster scare has \x01",
            "finally settled down at the mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "Now I can finally eat a relaxing\x01",
            "meal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C38")

    label("loc_5C17")


    ChrTalk(    #298
        0xFE,
        "*chomp chomp* *munch munch*\x02",
    )

    CloseMessageWindow()

    label("loc_5C38")

    Jump("loc_5EF5")

    label("loc_5C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_5D33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CFE")
    OP_A2(0x4)

    ChrTalk(    #299
        0xC,
        "*crunch* *smack* *slurp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0xC,
        "*chew chew chew*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0xC,
        "*munch munch munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xC,
        "*guuuuuulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0xC,
        (
            "I'll get back to work after this\x01",
            "next drink or maybe the drink\x01",
            "after that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D30")

    label("loc_5CFE")


    ChrTalk(    #304
        0xC,
        "*chomp chomp* *munch munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xC,
        "*guuuuuulp*\x02",
    )

    CloseMessageWindow()

    label("loc_5D30")

    Jump("loc_5EF5")

    label("loc_5D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_5E2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DF7")
    OP_A2(0x4)

    ChrTalk(    #306
        0xC,
        "*crunch* *smack* *slurp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #307
        0xC,
        "*chew chew chew*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0xC,
        "*munch munch munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #309
        0xC,
        "*guuuuuulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xC,
        (
            "I'd better get back to the mine\x01",
            "before the boss figures out I\x01",
            "ditched work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E29")

    label("loc_5DF7")


    ChrTalk(    #311
        0xC,
        "*chomp chomp* *munch munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #312
        0xC,
        "*guuuuuulp*\x02",
    )

    CloseMessageWindow()

    label("loc_5E29")

    Jump("loc_5EF5")

    label("loc_5E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EC3")
    OP_A2(0x4)

    ChrTalk(    #313
        0xC,
        "*crunch* *smack* *slurp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0xC,
        "*chew chew chew*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #315
        0xC,
        "*munch munch munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0xC,
        "*guuuuuulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0xC,
        (
            "I get so hungry working in\x01",
            "the mines.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5EF5")

    label("loc_5EC3")


    ChrTalk(    #318
        0xC,
        "*chomp chomp* *munch munch*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #319
        0xC,
        "*guuuuuulp*\x02",
    )

    CloseMessageWindow()

    label("loc_5EF5")

    TalkEnd(0xC)
    Return()

    # Function_11_5A11 end

    def Function_12_5EF9(): pass

    label("Function_12_5EF9")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_6008")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FAC")
    OP_A2(0x5)

    ChrTalk(    #320
        0xFE,
        (
            "Aww...I wanted that esmelas\x01",
            "found in the Malga Mine for\x01",
            "my own private collection.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xFE,
        (
            "I wonder who it was that managed\x01",
            "to purchase it before me...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6005")

    label("loc_5FAC")


    ChrTalk(    #322
        0xFE,
        (
            "Aww... I wanted that esmelas\x01",
            "found in the Malga Mine for\x01",
            "my own private collection.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6005")

    Jump("loc_68B2")

    label("loc_6008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_6246")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6177")
    OP_A2(0x5)

    ChrTalk(    #323
        0xFE,
        (
            "I happened to hear that Rolent\x01",
            "has quite a few skilled bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #324
        0xFE,
        (
            "I've even heard that the newest\x01",
            "two recruits are promising as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #325
        0xFE,
        (
            "Not only does this city have a wealth\x01",
            "of natural resources, but it is also\x01",
            "blessed with human resources.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #326
        0xFE,
        (
            "I wonder if the mayor of Bose would\x01",
            "be happy if I scouted some new\x01",
            "'people' commodities.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6243")

    label("loc_6177")


    ChrTalk(    #327
        0xFE,
        (
            "Not only does this city have a wealth\x01",
            "of natural resources, but it is also\x01",
            "blessed with human resources.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #328
        0xFE,
        (
            "I wonder if the mayor of Bose would\x01",
            "be happy if I scouted some new\x01",
            "'people' commodities.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6243")

    Jump("loc_68B2")

    label("loc_6246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_63C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_635B")
    OP_A2(0x5)

    ChrTalk(    #329
        0xFE,
        "Well! We certainly were lucky this time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #330
        0xFE,
        (
            "Who'd have thought they'd discover\x01",
            "a new lode while we were here\x01",
            "discussing business?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #331
        0xFE,
        (
            "Coming here was much better than\x01",
            "listening to the worthless talk\x01",
            "of merchants from the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xFE,
        "Right, Simon?\x02",
    )

    CloseMessageWindow()
    Jump("loc_63BF")

    label("loc_635B")


    ChrTalk(    #333
        0xFE,
        (
            "Most people think Rolent is nothing\x01",
            "more than country, but it's truly a\x01",
            "treasure of resources.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63BF")

    Jump("loc_68B2")

    label("loc_63C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_6543")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64B9")
    OP_A2(0x5)

    ChrTalk(    #334
        0xD,
        "Ah ha ha ha, Simon!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xD,
        (
            "It was certainly worth coming\x01",
            "here to do business this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0xD,
        (
            "It seems as though I'll be able to\x01",
            "stock up on septium as planned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0xD,
        (
            "It might even be worth staying\x01",
            "in Rolent a little longer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6540")

    label("loc_64B9")


    ChrTalk(    #338
        0xD,
        (
            "It seems as though I'll be able to\x01",
            "stock up on septium as planned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xD,
        (
            "It might even be worth staying\x01",
            "in Rolent a little longer.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6540")

    Jump("loc_68B2")

    label("loc_6543")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_66DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_663C")
    OP_A2(0x5)

    ChrTalk(    #340
        0xD,
        (
            "It seems like somehow I'll be\x01",
            "able to get the lumber I wanted.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0xD,
        (
            "Simon! Our septium purchases are\x01",
            "going to go through fine, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0xD,
        (
            "Since I spared no effort in coming\x01",
            "all the way to Rolent, failure is\x01",
            "not an option.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_66DC")

    label("loc_663C")


    ChrTalk(    #343
        0xD,
        (
            "Simon! Our septium purchases are\x01",
            "going to go through fine, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xD,
        (
            "Since I spared no effort in coming\x01",
            "all the way to Rolent, failure is\x01",
            "not an option.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66DC")

    Jump("loc_68B2")

    label("loc_66DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67AF")
    OP_A2(0x5)

    ChrTalk(    #345
        0xD,
        (
            "Simon! Listen to me and\x01",
            "listen well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0xD,
        (
            "Right now is the time for us to\x01",
            "purchase lumber and septium.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xD,
        (
            "Ignoring the potential risks, I'm\x01",
            "going to buy as much as I can\x01",
            "with the budget.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_68B2")

    label("loc_67AF")


    ChrTalk(    #348
        0xD,
        (
            "My aim is to capitalize on the queen's birthday\x01",
            "celebration. I believe the prices of these goods\x01",
            "will rise before and after the festival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0xD,
        (
            "It would be best to stock up on these\x01",
            "commodities while they're cheap and\x01",
            "then put them onto the market later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68B2")

    TalkEnd(0xD)
    Return()

    # Function_12_5EF9 end

    def Function_13_68B6(): pass

    label("Function_13_68B6")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x49, 7)), scpexpr(EXPR_END)), "loc_6959")

    ChrTalk(    #350
        0xFE,
        (
            "Ms. Mirano, we'd better get back to\x01",
            "Bose or we'll miss our next business\x01",
            "meeting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0xFE,
        (
            "I'm sure the mayor is waiting to\x01",
            "hear our report as well.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C91")

    label("loc_6959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 1)), scpexpr(EXPR_END)), "loc_69C7")

    ChrTalk(    #352
        0xFE,
        "Ms. Mirano...umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0xFE,
        (
            "I-I don't think we have time to be\x01",
            "looking for new 'human' resources.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C91")

    label("loc_69C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_6A72")

    ChrTalk(    #354
        0xFE,
        (
            "Even though she's just being facetious,\x01",
            "she's still completely right about Rolent's\x01",
            "'resources.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0xFE,
        (
            "She has a very good eye for\x01",
            "ALL kinds of commodities.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C91")

    label("loc_6A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_6AF6")

    ChrTalk(    #356
        0xE,
        (
            "That reminds me. I heard a new\x01",
            "lode was discovered in the Malga\x01",
            "Mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0xE,
        (
            "This may be something to look\x01",
            "forward to.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C91")

    label("loc_6AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x40, 5)), scpexpr(EXPR_END)), "loc_6BAF")

    ChrTalk(    #358
        0xE,
        (
            "L-Let's see... I've made contact with some\x01",
            "people at the Malga Mine, and we're working\x01",
            "out a few business details at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #359
        0xE,
        "P-Please wait just a little longer.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6C91")

    label("loc_6BAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C2B")
    OP_A2(0x6)

    ChrTalk(    #360
        0xE,
        (
            "Y-Yes, I've already made arrangements\x01",
            "regarding the lumber.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0xE,
        (
            "I'm looking into the septium\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C91")

    label("loc_6C2B")


    ChrTalk(    #362
        0xE,
        (
            "I've already made arrangements regarding\x01",
            "the lumber, and I'm looking into the septium\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C91")

    TalkEnd(0xE)
    Return()

    # Function_13_68B6 end

    def Function_14_6C95(): pass

    label("Function_14_6C95")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_6DF0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D8F")
    OP_A2(0x7)

    ChrTalk(    #363
        0xFE,
        "I've made up my mind...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0xFE,
        (
            "I'm going to believe in the man\x01",
            "my daughter chose to marry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0xFE,
        (
            "I'm sure he'll work hard to be\x01",
            "independent and make my\x01",
            "daughter happy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0xFE,
        (
            "Maybe I'll just see what I can\x01",
            "do to help him out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DED")

    label("loc_6D8F")


    ChrTalk(    #367
        0xFE,
        "I've made up my mind...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0xFE,
        (
            "I'm going to believe in the man\x01",
            "my daughter chose to marry.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DED")

    Jump("loc_6F02")

    label("loc_6DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EAB")
    OP_A2(0x7)

    ChrTalk(    #369
        0xF,
        "Hic!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0xF,
        (
            "Hmph, my son-in-law is still half a\x01",
            "man when it comes to this business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0xF,
        (
            "This isn't an easy job, and it takes\x01",
            "a good 2-3 years to become a real\x01",
            "woodsman.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6F02")

    label("loc_6EAB")


    ChrTalk(    #372
        0xF,
        "Hic!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #373
        0xF,
        (
            "Hmph, my son-in-law is still half a\x01",
            "man when it comes to this business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F02")

    TalkEnd(0xF)
    Return()

    # Function_14_6C95 end

    def Function_15_6F06(): pass

    label("Function_15_6F06")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D, 0)), scpexpr(EXPR_END)), "loc_7064")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FE0")
    OP_A2(0x8)

    ChrTalk(    #374
        0xFE,
        (
            "Yesterday, I saw something flying\x01",
            "away from the south.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0xFE,
        (
            "It was too big to be a bird, so it\x01",
            "makes me wonder what it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0xFE,
        (
            "These old eyes could have been\x01",
            "playing tricks on me though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7061")

    label("loc_6FE0")


    ChrTalk(    #377
        0xFE,
        (
            "Yesterday, I saw something flying\x01",
            "away from the south.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0xFE,
        (
            "It was too big to be a bird, so it\x01",
            "makes me wonder what it was.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7061")

    Jump("loc_7224")

    label("loc_7064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71A8")
    OP_A2(0x8)

    ChrTalk(    #379
        0xFE,
        (
            "10 years ago, the Imperial Army\x01",
            "broke through the borders and\x01",
            "surrounded Rolent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xFE,
        (
            "And in an effort to convince us\x01",
            "to surrender, they bombarded\x01",
            "the clock tower...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x101,
        "#003F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0xFE,
        (
            "I... I apologize for making you\x01",
            "recall those painful memories...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0x101,
        "#501FNo, it's all right, really...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #384
        0x102,
        "#014F...?\x02",
    )

    CloseMessageWindow()
    Jump("loc_7224")

    label("loc_71A8")


    ChrTalk(    #385
        0xFE,
        (
            "Though the city and clock tower\x01",
            "have been rebuilt...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #386
        0xFE,
        (
            "There are many unseen wounds\x01",
            "that linger in peoples' hearts.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7224")

    TalkEnd(0x11)
    Return()

    # Function_15_6F06 end

    def Function_16_7228(): pass

    label("Function_16_7228")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 1)), scpexpr(EXPR_END)), "loc_73BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7325")
    OP_A2(0x9)

    ChrTalk(    #387
        0x12,
        "Oh, hey there, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x12,
        (
            "I saw some crazy quick monsters on\x01",
            "the Milch Main Road the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x12,
        (
            "Just when I thought they were\x01",
            "charging me, they took off\x01",
            "running.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x12,
        (
            "Seriously, what were those\x01",
            "things...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73B7")

    label("loc_7325")


    ChrTalk(    #391
        0x12,
        (
            "I saw some crazy quick monsters on\x01",
            "the Milch Main Road the other day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x12,
        (
            "Just when I thought they were\x01",
            "charging me, they took off\x01",
            "running.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73B7")

    Jump("loc_74FB")

    label("loc_73BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_74FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_747B")
    OP_A2(0x9)

    ChrTalk(    #393
        0x12,
        "Oh, hey there, Estelle and Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #394
        0x101,
        "#000FRidge...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #395
        0x12,
        (
            "It looks like you had a pretty\x01",
            "rough first day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x12,
        (
            "Was everything all right without\x01",
            "Cassius being around?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_74FB")

    label("loc_747B")


    ChrTalk(    #397
        0x12,
        (
            "It looks like you two had a pretty\x01",
            "rough first day as bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #398
        0x12,
        (
            "Was everything all right without\x01",
            "Cassius being around?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_74FB")

    TalkEnd(0x12)
    Return()

    # Function_16_7228 end

    SaveToFile()

Try(main)
