from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2132   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2132.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2132   ._SN',
            'ED6_DT21/T2132_1 ._SN',
            'ED6_DT21/T2132_2 ._SN',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Nial',                                 # 9
        'Dorothy',                              # 10
        'Ernest',                               # 11
        'Norman',                               # 12
        'Dels',                                 # 13
        'Nial',                                 # 14
        'Herio',                                # 15
        'Belden',                               # 16
        'Santos',                               # 17
        'Herio',                                # 18
        'Bargo',                                # 19
        'Berna',                                # 20
        'Kuper',                                # 21
        'Agate',                                # 22
        'Scherazard',                           # 23
        'Olivier',                              # 24
        'Targeting Camera',                     # 25
        'Targeting Camera2',                    # 26
        'Dels',                                 # 27
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
        Unknown_28              = 2600,
        Unknown_2C              = 262,
        Unknown_30              = 35,
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
        'ED6_DT07/CH02063 ._CH',             # 00
        'ED6_DT26/CH20285 ._CH',             # 01
        'ED6_DT07/CH01570 ._CH',             # 02
        'ED6_DT07/CH01200 ._CH',             # 03
        'ED6_DT07/CH01040 ._CH',             # 04
        'ED6_DT07/CH02060 ._CH',             # 05
        'ED6_DT07/CH01220 ._CH',             # 06
        'ED6_DT07/CH01140 ._CH',             # 07
        'ED6_DT07/CH01660 ._CH',             # 08
        'ED6_DT07/CH01460 ._CH',             # 09
        'ED6_DT06/CH20039 ._CH',             # 0A
        'ED6_DT07/CH00050 ._CH',             # 0B
        'ED6_DT07/CH00020 ._CH',             # 0C
        'ED6_DT07/CH00030 ._CH',             # 0D
        'ED6_DT07/CH01043 ._CH',             # 0E
        'ED6_DT07/CH01390 ._CH',             # 0F
        'ED6_DT07/CH01210 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH02063P._CP',             # 00
        'ED6_DT26/CH20285P._CP',             # 01
        'ED6_DT07/CH01570P._CP',             # 02
        'ED6_DT07/CH01200P._CP',             # 03
        'ED6_DT07/CH01040P._CP',             # 04
        'ED6_DT07/CH02060P._CP',             # 05
        'ED6_DT07/CH01220P._CP',             # 06
        'ED6_DT07/CH01140P._CP',             # 07
        'ED6_DT07/CH01660P._CP',             # 08
        'ED6_DT07/CH01460P._CP',             # 09
        'ED6_DT06/CH20039P._CP',             # 0A
        'ED6_DT07/CH00050P._CP',             # 0B
        'ED6_DT07/CH00020P._CP',             # 0C
        'ED6_DT07/CH00030P._CP',             # 0D
        'ED6_DT07/CH01043P._CP',             # 0E
        'ED6_DT07/CH01390P._CP',             # 0F
        'ED6_DT07/CH01210P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x195,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -1900,
        Z                   = 0,
        Y                   = 11500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = -2660,
        Z                   = 0,
        Y                   = 80950,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -2570,
        Z                   = 0,
        Y                   = 79390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -2570,
        Z                   = 0,
        Y                   = 79390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 1,
    )

    DeclNpc(
        X                   = 650,
        Z                   = 0,
        Y                   = 43430,
        Direction           = 95,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -46277,
        Z                   = 0,
        Y                   = 4360,
        Direction           = 346,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 2,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 28130,
        Z                   = 0,
        Y                   = 49490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 1760,
        Z                   = 0,
        Y                   = 3430,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 5100,
        Z                   = 0,
        Y                   = 8920,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 16,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 16,
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
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 11,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -4500,
        Z                   = 250,
        Y                   = 80360,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )


    DeclEvent(
        X                   = 22000,
        Y                   = -100,
        Z                   = 78170,
        Range               = 22800,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x12818,
        Unknown_18          = 0x10000,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = 5280,
        Y                   = 1900,
        Z                   = 41390,
        Range               = 7180,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x9C18,
        Unknown_18          = 0x10000,
        Unknown_1C          = 3,
    )

    DeclEvent(
        X                   = -1290,
        Y                   = -100,
        Z                   = 4070,
        Range               = 2510,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFFC4A,
        Unknown_18          = 0x10000,
        Unknown_1C          = 14,
    )

    DeclEvent(
        X                   = -5120,
        Y                   = -100,
        Z                   = -900,
        Range               = -1040,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFFFF9C,
        Unknown_18          = 0x10000,
        Unknown_1C          = 15,
    )


    DeclActor(
        TriggerX            = -2020,
        TriggerZ            = 0,
        TriggerY            = 10280,
        TriggerRange        = 400,
        ActorX              = -1900,
        ActorZ              = 1500,
        ActorY              = 11500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 29950,
        TriggerZ            = -200,
        TriggerY            = 49030,
        TriggerRange        = 500,
        ActorX              = 29950,
        ActorZ              = 1700,
        ActorY              = 49030,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_45A",          # 00, 0
        "Function_1_704",          # 01, 1
        "Function_2_7A2",          # 02, 2
        "Function_3_B36",          # 03, 3
        "Function_4_BD4",          # 04, 4
        "Function_5_14A1",         # 05, 5
        "Function_6_15EC",         # 06, 6
        "Function_7_182A",         # 07, 7
        "Function_8_18F2",         # 08, 8
        "Function_9_1F42",         # 09, 9
        "Function_10_1F67",        # 0A, 10
        "Function_11_2205",        # 0B, 11
        "Function_12_220A",        # 0C, 12
        "Function_13_2C82",        # 0D, 13
        "Function_14_2F0C",        # 0E, 14
        "Function_15_326A",        # 0F, 15
        "Function_16_3512",        # 10, 16
        "Function_17_42B7",        # 11, 17
        "Function_18_4306",        # 12, 18
        "Function_19_4355",        # 13, 19
        "Function_20_43A4",        # 14, 20
        "Function_21_43F3",        # 15, 21
    )


    def Function_0_45A(): pass

    label("Function_0_45A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_482")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_696")

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_634")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4BD")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -7590, 0, 82320, 188)
    Jump("loc_631")

    label("loc_4BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5FC")
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xE, -3880, 0, 83810, 180)
    SetChrPos(0xB, -430, 0, 80990, 225)
    SetChrPos(0x14, -2450, 0, 80960, 180)
    SetChrFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_5A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_54E")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -3320, 0, 9510, 45)
    Jump("loc_56B")

    label("loc_54E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_56B")
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -3320, 0, 9510, 45)

    label("loc_56B")

    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -2620, 0, 8220, 0)
    SetChrPos(0x14, -7880, 0, 83450, 0)
    SetChrPos(0xE, -3740, 0, 78670, 0)
    Jump("loc_5F9")

    label("loc_5A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_5C6")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -2430, 0, 79710, 0)
    Jump("loc_5E3")

    label("loc_5C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5E3")
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -2430, 0, 79710, 0)

    label("loc_5E3")

    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -1300, 0, 78180, 0)

    label("loc_5F9")

    Jump("loc_631")

    label("loc_5FC")

    ClearChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_620")
    SetChrPos(0xE, 22470, 0, 76980, 90)
    Jump("loc_631")

    label("loc_620")

    SetChrPos(0xE, 22470, 0, 76980, 90)

    label("loc_631")

    Jump("loc_696")

    label("loc_634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_65E")
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrPos(0xC, -7340, 0, 81680, 142)
    Jump("loc_696")

    label("loc_65E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_672")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_696")

    label("loc_672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_685")
    SetChrFlags(0xC, 0x80)
    Jump("loc_696")

    label("loc_685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_696")
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_696")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x66, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_6A5")
    SetChrFlags(0x10, 0x80)

    label("loc_6A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6E2")
    SetChrFlags(0x9, 0x4)
    SetChrPos(0x8, 26640, 200, 48910, 270)
    SetChrPos(0x9, 29690, 300, 48620, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_6E2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_703")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_703")
    Event(0, 16)

    label("loc_703")

    Return()

    # Function_0_45A end

    def Function_1_704(): pass

    label("Function_1_704")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_713")
    Jump("loc_717")

    label("loc_713")

    OP_64(0x1, 0x1)

    label("loc_717")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_755")
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_72(0x2, 0x20)
    OP_72(0x2, 0x8)
    OP_72(0x3, 0x20)
    OP_72(0x3, 0x8)
    OP_72(0x4, 0x20)
    OP_72(0x4, 0x8)

    label("loc_755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_766")
    OP_72(0xC, 0x4)

    label("loc_766")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A1")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (115, "loc_794"),
        (116, "loc_794"),
        (117, "loc_794"),
        (SWITCH_DEFAULT, "loc_7A1"),
    )


    label("loc_794")

    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x1A, 0x80)
    Jump("loc_7A1")

    label("loc_7A1")

    Return()

    # Function_1_704 end

    def Function_2_7A2(): pass

    label("Function_2_7A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C6")
    Call(1, 6)
    Jump("loc_B32")

    label("loc_7C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_8EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_837")

    ChrTalk(    #0
        0xFE,
        "Anyway, I'm gonna be helpin' with the election.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "I'll start there to change myself.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E8")

    label("loc_837")

    OP_A2(0x6)

    ChrTalk(    #2
        0xFE,
        (
            "I was tryin' to look for the right\x01",
            "timin' to talk about it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Things got kinda out of hand,\x01",
            "and I got more and more scared.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "...Even I know it's pathetic.\x02",
    )

    CloseMessageWindow()

    label("loc_8E8")

    Jump("loc_B32")

    label("loc_8EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_9CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_95C")

    ChrTalk(    #5
        0xFE,
        "Anyway, I'm gonna be helpin' with the election.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "I'll start there to change myself.\x02",
    )

    CloseMessageWindow()
    Jump("loc_9CA")

    label("loc_95C")

    OP_A2(0x6)

    ChrTalk(    #7
        0xFE,
        "It was pretty rough back there, huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Honestly, I was really on edge\x01",
            "wonderin' how it'd turn out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9CA")

    Jump("loc_B32")

    label("loc_9CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_A58")

    ChrTalk(    #9
        0xFE,
        (
            "For now I've taken on a part-time\x01",
            "job to help with the election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "I've just started, but I guess\x01",
            "things are goin' okay.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B32")

    label("loc_A58")

    OP_A2(0x6)

    ChrTalk(    #11
        0xFE,
        (
            "For now I've taken on a part-time\x01",
            "job to help with the election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "I've just started, but I guess\x01",
            "things are goin' okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Thankfully my dad's too busy to have much\x01",
            "time to worry about me, it seems like.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B32")

    TalkEnd(0xFE)
    Return()

    # Function_2_7A2 end

    def Function_3_B36(): pass

    label("Function_3_B36")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_B7B")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #14
        0x9,
        "#157F...Hnnn... Zzzzz...\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_BD0")

    label("loc_B7B")

    OP_A2(0x5)
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #15
        0x9,
        (
            "#157F...Hnn...\x02\x03",

            "So...cuu...te...\x02\x03",

            "... *sNOOOOOORE*\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE)

    label("loc_BD0")

    TalkEnd(0xFE)
    Return()

    # Function_3_B36 end

    def Function_4_BD4(): pass

    label("Function_4_BD4")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BF9")
    SetChrSubChip(0xFE, 2)
    Jump("loc_BFE")

    label("loc_BF9")

    SetChrSubChip(0xFE, 1)

    label("loc_BFE")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24C, 1)), scpexpr(EXPR_END)), "loc_C86")

    ChrTalk(    #16
        0x8,
        (
            "#141FWell, I hope you don't take it hard, and\x01",
            "if anything else comes, up contact me.\x02\x03",

            "Well, then, take care.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1498")

    label("loc_C86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_120D")
    OP_A2(0x1261)

    ChrTalk(    #17
        0x8,
        (
            "#143FHm...? What is it?\x02\x03",

            "Did you find the criminal?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_F7D")

    ChrTalk(    #18
        0x101,
        (
            "#1015FWell, we uncovered the truth, but...\x02\x03",

            "The truth is there was no criminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "#142FWhaddaya mean?\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #20
        (
            "\x07\x05Estelle explained that the 'crime' was actually just an\x01",
            "unfortunate accident.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #21
        0x8,
        (
            "#140F...Huh, I see.\x02\x03",

            "Well, that sure would make for no criminal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1000FThink you can make an article?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "#145FNah, probably not.\x02\x03",

            "There's no real case here, so there's\x01",
            "no point in puttin' it in the paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1007FAww, bummer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#141FWell, I hope you don't take it hard, and\x01",
            "if anything else comes, up contact me.\x02\x03",

            "Well, then, I got a draft I need to work on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1011FAh, got'cha...\x01",
            "Well, see you again sometime.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120A")

    label("loc_F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_FDC")

    ChrTalk(    #27
        0x106,
        (
            "#050FYeah, we found the truth.\x02\x03",

            "Don't think it's what you're expectin', though.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1040")

    label("loc_FDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1040")

    ChrTalk(    #28
        0x103,
        (
            "#020FWell, we did get to the bottom of things.\x02\x03",

            "It's not what you're expecting, though.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1040")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05Estelle explained the overview of the case.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #30
        0x8,
        "#140F...Huh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1000FThink you can make an article?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#145FNah, probably not.\x02\x03",

            "There's no real case here, so there's\x01",
            "no point in puttin' it in the paper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1007FAww, bummer.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#141FWell, I hope you don't take it hard, and\x01",
            "if anything else comes, up contact me.\x02\x03",

            "Well, then, I got a draft I need to work on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1006FOkay. Catch you later.\x02",
    )

    CloseMessageWindow()

    label("loc_120A")

    Jump("loc_1498")

    label("loc_120D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_145E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24C, 0)), scpexpr(EXPR_END)), "loc_1292")

    ChrTalk(    #36
        0x8,
        (
            "#140FHm...? What is it?\x02\x03",

            "#145FSorry, but I need to focus on the draft\x01",
            "for my article. Deadline's coming up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_145B")

    label("loc_1292")

    OP_A2(0x1260)

    ChrTalk(    #37
        0x8,
        "#140FHm...? Haven't you left yet?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#1015FYeah, actually a case suddenly popped up.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#142FMm?\x02\x03",

            "Whaddaya mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1000FWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x05Estelle explained the assault case to Nial.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #42
        0x8,
        "#140FAh, I see.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1011FHuh? You don't seem too interested.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#140FYeah, I doubt it's big enough\x01",
            "to make an article out of.\x02\x03",

            "Well, just in case, once you solve\x01",
            "it tell me what ya got.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#1006FYeah, will do.\x02",
    )

    CloseMessageWindow()

    label("loc_145B")

    Jump("loc_1498")

    label("loc_145E")


    ChrTalk(    #46
        0x8,
        (
            "#141FIf anything else crops up, let me know.\x02\x03",

            "Later.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1498")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_4_BD4 end

    def Function_5_14A1(): pass

    label("Function_5_14A1")

    OP_4A(0xB, 255)
    OP_4A(0xD, 255)

    ChrTalk(    #47
        0xD,
        (
            "#140FWell, then, for my next question...\x02\x03",

            "Candidate, you are part of the tourism\x01",
            "promotion faction, correct?\x02\x03",

            "What kind of plans do you have to\x01",
            "invigorate the tourism industry?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xB,
        (
            "I wish you wouldn't say 'tourism\x01",
            "promotion faction' like that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xB,
        (
            "It sounds like I have nothing else\x01",
            "on my mind but tourism.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xB, 255)
    OP_4B(0xD, 255)
    Return()

    # Function_5_14A1 end

    def Function_6_15EC(): pass

    label("Function_6_15EC")

    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16DE")

    ChrTalk(    #50
        0xB,
        (
            "Incidentally, have we decided on\x01",
            "a site for the speech?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xC,
        (
            "Yes, we're thinking of the Langland\x01",
            "Bridge as our first candidate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xC,
        (
            "It's a heavily trafficked location, so I'm\x01",
            "sure we'll get a fair number of listeners.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1821")

    label("loc_16DE")

    OP_A2(0x1)

    ChrTalk(    #53
        0xC,
        "So, how's your son?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        "Same as always...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xB,
        (
            "I don't know what he's so afraid of,\x01",
            "but he's locked himself in his room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xC,
        "I see... I'm sorry to hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xB,
        "Me complaining won't change anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xB,
        "Ultimately, it's my son's problem to deal with.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xB,
        "...Let us return to talking about work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xC,
        "Ah, yes.\x02",
    )

    CloseMessageWindow()

    label("loc_1821")

    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    Return()

    # Function_6_15EC end

    def Function_7_182A(): pass

    label("Function_7_182A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_18E4")
    OP_4A(0xB, 255)

    ChrTalk(    #61
        0xD,
        (
            "#140FHowever, candidate Norman, your campaign\x01",
            "promises are those of invigorating tourism.\x02\x03",

            "Don't you think it's only natural that\x01",
            "you're being labeled as such?\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xB, 255)
    Jump("loc_18EE")

    label("loc_18E4")

    OP_A2(0x1)
    OP_A2(0x4)
    Call(0, 5)

    label("loc_18EE")

    TalkEnd(0xFE)
    Return()

    # Function_7_182A end

    def Function_8_18F2(): pass

    label("Function_8_18F2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1916")
    Call(1, 12)
    Jump("loc_1F3E")

    label("loc_1916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A15")

    ChrTalk(    #62
        0xFE,
        (
            "Personally, I think not enough consideration\x01",
            "has been given to the people who have\x01",
            "contributed to the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "To ensure no further misunderstandings happen,\x01",
            "I intend to keep an open line of communication\x01",
            "with them at all times.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD6")

    label("loc_1A15")

    OP_A2(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1AF8")

    ChrTalk(    #64
        0xFE,
        "Ohh, bracers. Wonderful work today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "If you hadn't resolved things, opposition\x01",
            "would have only grown deeper.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "Well, then, I hope you will strive ever harder\x01",
            "in your work for the sake of the people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BD6")

    label("loc_1AF8")


    ChrTalk(    #67
        0xFE,
        "Oh, bracers. Good work before.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "I appreciate you sorting things out before.\x01",
            "I wasn't sure how it was going to turn out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "Well, then, I hope you will strive ever harder\x01",
            "in your work for the sake of the people.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BD6")

    Jump("loc_1F3E")

    label("loc_1BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1CFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1CF2")
    OP_4A(0xD, 255)

    ChrTalk(    #70
        0xFE,
        (
            "The tourism and shipping industries\x01",
            "are both integral to one another.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "However, from a long-term perspective,\x01",
            "the most effective way to grow is\x01",
            "through the tourism industry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "Which is why I promote developing\x01",
            "that sector more for our futures.\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xD, 255)
    Jump("loc_1CF9")

    label("loc_1CF2")

    OP_A2(0x1)
    Call(0, 5)

    label("loc_1CF9")

    Jump("loc_1F3E")

    label("loc_1CFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F33")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E14")

    ChrTalk(    #73
        0xFE,
        (
            "I am not unappreciative of the feelings\x01",
            "of those in the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "Under the governance of the last mayor, the\x01",
            "funds for the harbor facilities were slashed\x01",
            "and the equipment has aged poorly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "The people of the harbor fear\x01",
            "seeing that happen again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F30")

    label("loc_1E14")

    OP_A2(0x1)

    ChrTalk(    #76
        0xFE,
        (
            "The future of the City of Ruan depends on\x01",
            "the expansion of the tourism industry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "More tourists will enrich the city as a whole,\x01",
            "and naturally result in the shipping industry\x01",
            "also flourishing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "Which is what I need the people of\x01",
            "the city to understand more broadly...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F30")

    Jump("loc_1F3E")

    label("loc_1F33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1F3E")
    Call(0, 6)

    label("loc_1F3E")

    TalkEnd(0xFE)
    Return()

    # Function_8_18F2 end

    def Function_9_1F42(): pass

    label("Function_9_1F42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F63")
    Call(1, 13)

    label("loc_1F63")

    TalkEnd(0xFE)
    Return()

    # Function_9_1F42 end

    def Function_10_1F67(): pass

    label("Function_10_1F67")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2037")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1FE3")

    ChrTalk(    #79
        0xFE,
        "Ah, bracers. Good work back there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "Honestly, I was relieved to hear\x01",
            "there was no criminal.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2034")

    label("loc_1FE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_2034")

    ChrTalk(    #81
        0xFE,
        "Ah, bracers. Good work back there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "Ugh, my head still aches.\x02",
    )

    CloseMessageWindow()

    label("loc_2034")

    Jump("loc_2201")

    label("loc_2037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_21F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_20C9")

    ChrTalk(    #83
        0xFE,
        (
            "The start of the riot was really\x01",
            "just a little argument.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "For something so trivial to grow\x01",
            "into a big mess like that...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21F3")

    label("loc_20C9")

    OP_A2(0x2)

    ChrTalk(    #85
        0xFE,
        (
            "The start of the riot was really\x01",
            "just a little argument.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "It was just a little disagreement with some\x01",
            "of Portos' camp about the site of a speech.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "We were just quarreling a bit, and\x01",
            "then suddenly it turned into that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "*sigh* I feel bad, like I rubbed\x01",
            "dirt into Norman's face.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21F3")

    Jump("loc_2201")

    label("loc_21F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2201")
    Call(0, 6)

    label("loc_2201")

    TalkEnd(0xFE)
    Return()

    # Function_10_1F67 end

    def Function_11_2205(): pass

    label("Function_11_2205")

    Call(0, 12)
    Return()

    # Function_11_2205 end

    def Function_12_220A(): pass

    label("Function_12_220A")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_222A")
    Jump("loc_2258")

    label("loc_222A")

    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2247")
    OP_0D()
    OP_A9(0x6B)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_2247")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2258")
    TalkEnd(0xA)
    Return()

    label("loc_2258")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2279")
    Call(1, 9)
    Jump("loc_2C7E")

    label("loc_2279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2472")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C2")

    ChrTalk(    #89
        0xA,
        (
            "The owner of this hotel is the new mayor,\x01",
            "Mr. Norman, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        (
            "When I saw him the other day\x01",
            "he looked terribly tired.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "I have heard he has been staying at\x01",
            "the mayoral manor over the last\x01",
            "few days tending to his duties.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        (
            "He has just started as mayor.\x01",
            "I hope he does not push himself\x01",
            "too hard.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_246F")

    label("loc_23C2")


    ChrTalk(    #93
        0xA,
        (
            "Mr. Norman seems troubled about\x01",
            "how to respond as the mayor...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "I have heard he has been staying at\x01",
            "the mayoral manor over the last few\x01",
            "days tending to his duties.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_246F")

    Jump("loc_2C7E")

    label("loc_2472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2606")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2557")

    ChrTalk(    #95
        0xA,
        (
            "I have found replacement options\x01",
            "for lighting and hot water, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        (
            "In this situation it is terribly difficult\x01",
            "to maintain our normal services.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        "I wonder how long this situation will persist...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_2603")

    label("loc_2557")


    ChrTalk(    #98
        0xA,
        (
            "In this situation it is terribly difficult\x01",
            "to maintain our normal services.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        (
            "I hope, on my stubbornness as a service\x01",
            "professional, to maintain a certain standard.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2603")

    Jump("loc_2C7E")

    label("loc_2606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_299D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_27C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_26A7")

    ChrTalk(    #100
        0xA,
        (
            "I hope you will stay at our\x01",
            "hotel on any visits to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xA,
        (
            "Our owner and employees all sincerely\x01",
            "await your patronage.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27C2")

    label("loc_26A7")

    OP_A2(0x0)

    ChrTalk(    #102
        0xA,
        (
            "Bracers, thank you very much\x01",
            "for your efforts today.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xA,
        (
            "As a representative of our hotel,\x01",
            "allow me to offer our gratitude\x01",
            "for resolving the case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "I hope you will stay at our hotel\x01",
            "on any visits to Ruan.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xA,
        (
            "Our owner and employees all sincerely\x01",
            "await your patronage.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27C2")

    Jump("loc_299A")

    label("loc_27C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_2836")

    ChrTalk(    #106
        0xA,
        "It seems something troubling has occurred.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        "I hope you'll be willing to lend us your aid.\x02",
    )

    CloseMessageWindow()
    Jump("loc_299A")

    label("loc_2836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_28C8")

    ChrTalk(    #108
        0xA,
        (
            "Just a bit ago, we received an order\x01",
            "from Mr. Norman for the Lavantar, in fact.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        "It seems it was lunch for the campaign staff.\x02",
    )

    CloseMessageWindow()
    Jump("loc_299A")

    label("loc_28C8")

    OP_A2(0x0)

    ChrTalk(    #110
        0xA,
        (
            "Our hotel's room service extends to taking\x01",
            "orders from local dining establishments.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xA,
        (
            "One of our proud services is to allow you\x01",
            "to enjoy the offerings from local eateries\x01",
            "leisurely in your own room.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_299A")

    Jump("loc_2C7E")

    label("loc_299D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2A33")

    ChrTalk(    #112
        0xA,
        (
            "It seems there was a misunderstanding\x01",
            "between both camps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xA,
        (
            "I hope both choose to fight with their campaigns,\x01",
            "not with their fists.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7E")

    label("loc_2A33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_2A8E")

    ChrTalk(    #114
        0xA,
        "Ah, guests. May I help you with something?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xA,
        "You seem quite worked up...\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C7E")

    label("loc_2A8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B50")

    ChrTalk(    #116
        0xA,
        (
            "We have few tourist guests currently as\x01",
            "we are in the middle of an election.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xA,
        (
            "As such, we have many open rooms,\x01",
            "so we will be glad to show you to any\x01",
            "room you would like.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C7E")

    label("loc_2B50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2C7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2BF9")

    ChrTalk(    #118
        0xA,
        (
            "Currently the suite room is being used as\x01",
            "election headquarters for Mr. Norman,\x01",
            "the mayoral candidate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xA,
        "Mr. Norman is the owner of this hotel.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C7E")

    label("loc_2BF9")

    OP_A2(0x0)

    ChrTalk(    #120
        0xA,
        "Welcome. Welcome to Hotel Blanche.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xA,
        (
            "We hope you will enjoy the services of our\x01",
            "hotel. All our rooms offer an ocean view.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C7E")

    TalkEnd(0xA)
    Return()

    # Function_12_220A end

    def Function_13_2C82(): pass

    label("Function_13_2C82")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2DAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D35")

    ChrTalk(    #122
        0xFE,
        "Those people with the bandanas...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "I see them all over the town.\x01",
            "Are they a youth group?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "Haha, they're so energetic.\x01",
            "It's rather refreshing.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_2DA7")

    label("loc_2D35")


    ChrTalk(    #125
        0xFE,
        (
            "Are those people with the bandanas a\x01",
            "youth group, I wonder?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "They're so energetic. It's very refreshing.\x02",
    )

    CloseMessageWindow()

    label("loc_2DA7")

    Jump("loc_2F08")

    label("loc_2DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2F08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E9C")

    ChrTalk(    #127
        0xFE,
        "I came here from Bose, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "Of all things to happen, it seems the\x01",
            "liners have stopped running again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "I was slowed down quite a bit on\x01",
            "my way here, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        "*sigh* It seems liners and I get along poorly.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_2F08")

    label("loc_2E9C")


    ChrTalk(    #131
        0xFE,
        "Apparently the liners have stopped again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "Now, what to do... I wonder if\x01",
            "I should extend my stay.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F08")

    TalkEnd(0x13)
    Return()

    # Function_13_2C82 end

    def Function_14_2F0C(): pass

    label("Function_14_2F0C")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_3077")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF8")

    ChrTalk(    #133
        0xFE,
        (
            "My co-worker Dels is staying behind beside\x01",
            "the mayor as a secretary, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "From what I heard from the front,\x01",
            "they're really busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "Well, no airships are coming, so\x01",
            "maybe I should go back and help.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_3074")

    label("loc_2FF8")


    ChrTalk(    #136
        0xFE,
        (
            "I'd planned on leaving supporting\x01",
            "Mayor Norman to Dels, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "No airships are coming, so\x01",
            "maybe I should go help.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3074")

    Jump("loc_3266")

    label("loc_3077")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3266")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31E2")

    ChrTalk(    #138
        0xFE,
        (
            "Just as things were settled with the election\x01",
            "and I'm on my way back to the capital...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "That island-like thing appeared in the\x01",
            "sky and now orbments won't work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "*sigh* I really don't feel like walking\x01",
            "all the way back to the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "Passing through the Kaldia Tunnel without the\x01",
            "orbal lights is something I could never do.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_3266")

    label("loc_31E2")


    ChrTalk(    #142
        0xFE,
        (
            "I wonder when the airships are gonna\x01",
            "resume service.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "If it's going to drag on, maybe I should\x01",
            "go back and help the mayor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3266")

    TalkEnd(0x11)
    Return()

    # Function_14_2F0C end

    def Function_15_326A(): pass

    label("Function_15_326A")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_33DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3306")

    ChrTalk(    #144
        0xFE,
        (
            "The crossing to the south\x01",
            "block is underground here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "Should you wish to use it, please go\x01",
            "to the first floor underground.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_33DA")

    label("loc_3306")


    ChrTalk(    #146
        0xFE,
        (
            "Heh heh. I'm gettin' used to this\x01",
            "talkin' polite thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "I hated it at first, but now it's kinda\x01",
            "fulfillin', ya know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "Helpin' out, bein' useful to someone...\x01",
            "It's weird, but it feels kinda nice.\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x13)

    label("loc_33DA")

    Jump("loc_350E")

    label("loc_33DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_350E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3472")

    ChrTalk(    #149
        0xFE,
        (
            "Ahh, the crossing to the south\x01",
            "block is underground here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "Per, peher... Pherthons wishing to croth,\x01",
            "please head down.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_350E")

    label("loc_3472")


    ChrTalk(    #151
        0xFE,
        "D-Damn it. I bit my tongue again...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "PER-SON-S wishing to cross...\x01",
            "There. Phew!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "All right, got it perfect. Not\x01",
            "gonna bite my tongue again!\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x13)

    label("loc_350E")

    TalkEnd(0x12)
    Return()

    # Function_15_326A end

    def Function_16_3512(): pass

    label("Function_16_3512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3523")
    Call(0, 21)

    label("loc_3523")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0xF7, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x104, 0x80)
    OP_6D(25960, 0, 47550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2440, 0)
    OP_6C(35000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6, 0x0, 0x64)
    Sleep(1000)

    def lambda_3590():
        OP_6D(27120, 0, 48140, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3590)
    OP_43(0x101, 0x1, 0x0, 0x11)
    Sleep(500)
    OP_43(0x104, 0x1, 0x0, 0x14)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x12)
    Sleep(500)
    OP_43(0x105, 0x1, 0x0, 0x13)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #154
        0x101,
        (
            "#1001F#6PHello! \x02",

            "#1004FEr...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 1)

    ChrTalk(    #155
        0x8,
        (
            "#143F#6PAh, you guys.\x02\x03",

            "#141FI heard from Dorothy that you guys\x01",
            "solved our little ghost problem.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_367B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_367B)
    Sleep(50)

    def lambda_368E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_368E)
    Sleep(50)

    def lambda_36A1():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_36A1)
    Sleep(50)

    def lambda_36B4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_36B4)
    WaitChrThread(0x104, 0x1)
    Sleep(300)

    ChrTalk(    #156
        0x101,
        (
            "#1015FYeah, we did, but...\x02\x03",

            "Is...Dorothy okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x8,
        (
            "#142F#6PShe was yammerin' on drowsily\x01",
            "about what happened...\x02\x03",

            "Once she was finished, she conked\x01",
            "right out, so I had to put her to bed.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3824")

    ChrTalk(    #158
        0x106,
        (
            "#051F#6PHeh, well. A hell of a lot happened\x01",
            "last night, and she saved our skins.\x02\x03",

            "I can't blame her for being kinda\x01",
            "tired. Let her rest, okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38BD")

    label("loc_3824")


    ChrTalk(    #159
        0x103,
        (
            "#027F#6PHmm... I'm afraid we did drag her\x01",
            "along with us in the dead of night.\x02\x03",

            "Not only that, but we owe her our\x01",
            "lives. She's earned a bit of rest.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38BD")


    ChrTalk(    #160
        0x8,
        (
            "#145F#6PHmph. A real reporter can go a good week\x01",
            "without sleep when he's got a scoop.\x02\x03",

            "#141FOh, yeah, some of the stuff she was\x01",
            "talking about sounded wild, but she\x01",
            "didn't really explain it all...\x02\x03",

            "Mind if I ask you guys a few questions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1006FSure, go ahead.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #162
        (
            "\x07\x05Estelle gave Nial an outline of their encounter\x01",
            "with Bleublanc and answered his questions.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #163
        0x8,
        (
            "#145F#6PAll right, I think I get it now.\x02\x03",

            "#142FSon of a... Phantom Thief B himself is in Liberl\x01",
            "AND he's one of those 'Ouroboros' people?\x01",
            "Kinda wish I HADN'T heard that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        (
            "#1004FWhat?!\x02\x03",

            "#1005FNial, you know about that masked weirdo?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x8,
        (
            "#142F#6POh, yeah. He's a famous thief who's caused\x01",
            "a stir in every major city on the continent.\x02\x03",

            "If he wants something, he'll get it.\x01",
            "And he always steals things with\x01",
            "a big ol' show...\x02\x03",

            "For a 'phantom,' he's got a love\x01",
            "of drama, that's for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3C90")

    ChrTalk(    #166
        0x106,
        (
            "#555F#6PMmph... Yeah, that sounds like\x01",
            "our weirdo, all right.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3CE3")

    label("loc_3C90")


    ChrTalk(    #167
        0x103,
        (
            "#022F#6PThat certainly matches the man we\x01",
            "met beneath the schoolhouse, yes...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D92")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Candelabrum Theft Event to Uncleared\x01",      # 0
            "Set Candelabrum Theft Event to Cleared\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D79"),
        (1, "loc_3D81"),
        (SWITCH_DEFAULT, "loc_3D89"),
    )


    label("loc_3D79")

    OP_28(0x20, 0x3, 0x10)
    Jump("loc_3D89")

    label("loc_3D81")

    OP_28(0x20, 0x4, 0x10)
    Jump("loc_3D89")

    label("loc_3D89")

    FadeToBright(300, 0)

    label("loc_3D92")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3DE7")

    ChrTalk(    #168
        0x101,
        (
            "#1007FHe even admitted he's 'Phantom Thief B'\x01",
            "from those cards, so...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DE7")


    ChrTalk(    #169
        0x8,
        (
            "#145F#6PLike I said, though. Thievery is one\x01",
            "thing, but he's also a lackey of the\x01",
            "society?\x02\x03",

            "Wouldn't think Ouroboros would have\x01",
            "use for someone like him, but at the\x01",
            "same time, if they DO, it's...terrifying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x105,
        (
            "#043F#2PNial, I'm curious.\x02\x03",

            "Do you intend to write an article\x01",
            "about what happened?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        (
            "#140F#6PNah, the guild and the Royal Army asked\x01",
            "me not to report on anything to do with the\x01",
            "society.\x02\x03",

            "I'll probably end up writing about someone's\x01",
            "'ill-intended crime of pleasure'...or something.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x104,
        (
            "#4P#035FWith the coup d'etat foiled, the\x01",
            "kingdom is beginning to settle.\x02\x03",

            "#030FI do see the wisdom in this. There is little\x01",
            "sense in terrifying the populace with news\x01",
            "of a dangerous secret society just yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "#145F#6PYeah, I ain't happy about it as a\x01",
            "reporter, but I guess I see where\x01",
            "the government is comin' from.\x02\x03",

            "#141FStill, if anything else happens,\x01",
            "tell me about it, yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1006FOf course!\x02\x03",

            "Anyway, we're off for Zeiss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        (
            "#143F#6PAh, right.\x02\x03",

            "I've got a draft I need to write\x01",
            "up, so I can't see you off, but...\x02\x03",

            "Want me to wake Dorothy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        (
            "#1016FNo, it's okay. She's fast asleep\x01",
            "and I'd hate to disturb her.\x02\x03",

            "#1011FGive her our best when she gets up, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        "#141F#6PWill do. Be careful, guys.\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    OP_A2(0x1401)
    EventEnd(0x0)
    Return()

    # Function_16_3512 end

    def Function_17_42B7(): pass

    label("Function_17_42B7")

    SetChrPos(0xFE, 23940, 0, 47510, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_42DE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_42DE)
    OP_8E(0xFE, 0x69F0, 0x0, 0xB928, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_17_42B7 end

    def Function_18_4306(): pass

    label("Function_18_4306")

    SetChrPos(0xFE, 23940, 0, 47510, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_432D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_432D)
    OP_8E(0xFE, 0x65FE, 0x0, 0xB8EC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_18_4306 end

    def Function_19_4355(): pass

    label("Function_19_4355")

    SetChrPos(0xFE, 23860, 0, 46420, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_437C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_437C)
    OP_8E(0xFE, 0x6586, 0x0, 0xB4E6, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_19_4355 end

    def Function_20_43A4(): pass

    label("Function_20_43A4")

    SetChrPos(0xFE, 23860, 0, 46420, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_43CB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_43CB)
    OP_8E(0xFE, 0x6978, 0x0, 0xB4DC, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_20_43A4 end

    def Function_21_43F3(): pass

    label("Function_21_43F3")

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
        (0, "loc_446C"),
        (1, "loc_4472"),
        (SWITCH_DEFAULT, "loc_4478"),
    )


    label("loc_446C")

    OP_A2(0x1200)
    Jump("loc_4478")

    label("loc_4472")

    OP_A2(0x1201)
    Jump("loc_4478")

    label("loc_4478")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_4486")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_448A")

    label("loc_4486")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_448A")

    Return()

    # Function_21_43F3 end

    SaveToFile()

Try(main)
