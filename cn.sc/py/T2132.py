from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '奈尔',                                 # 9
        '朵洛希',                               # 10
        '亚内斯特',                             # 11
        '诺曼',                                 # 12
        '德尔斯',                               # 13
        '奈尔',                                 # 14
        '海利欧',                               # 15
        '贝尔夫',                               # 16
        '森特',                                 # 17
        '海利欧',                               # 18
        '巴克',                                 # 19
        '贝尔娜',                               # 20
        '昆茨',                                 # 21
        '阿加特',                               # 22
        '雪拉扎德',                             # 23
        '奥利维尔',                             # 24
        '目标用照相机',                         # 25
        '目标用照相机2',                        # 26
        '德尔斯',                               # 27
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
        "Function_2_767",          # 02, 2
        "Function_3_9B0",          # 03, 3
        "Function_4_AA2",          # 04, 4
        "Function_5_1121",         # 05, 5
        "Function_6_11E1",         # 06, 6
        "Function_7_1365",         # 07, 7
        "Function_8_13EF",         # 08, 8
        "Function_9_1799",         # 09, 9
        "Function_10_17BE",        # 0A, 10
        "Function_11_1981",        # 0B, 11
        "Function_12_1986",        # 0C, 12
        "Function_13_2038",        # 0D, 13
        "Function_14_21E7",        # 0E, 14
        "Function_15_2419",        # 0F, 15
        "Function_16_25C9",        # 10, 16
        "Function_17_2E92",        # 11, 17
        "Function_18_2EE1",        # 12, 18
        "Function_19_2F30",        # 13, 19
        "Function_20_2F7F",        # 14, 20
        "Function_21_2FCE",        # 15, 21
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

    Return()

    # Function_1_704 end

    def Function_2_767(): pass

    label("Function_2_767")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_78B")
    Call(1, 6)
    Jump("loc_9AC")

    label("loc_78B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_841")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_7DD")

    ChrTalk(    #0
        0xFE,
        (
            "总之我会\x01",
            "努力帮忙选举的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "首先从这里开始\x01",
            "改变自己。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_83E")

    label("loc_7DD")

    OP_A2(0x6)

    ChrTalk(    #2
        0xFE,
        (
            "本来是想找个机会\x01",
            "谈谈的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "总觉得话太沉重\x01",
            "越来越害怕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "……自己也觉得丢脸啊。\x02",
    )

    CloseMessageWindow()

    label("loc_83E")

    Jump("loc_9AC")

    label("loc_841")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_8E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_893")

    ChrTalk(    #5
        0xFE,
        (
            "总之我会\x01",
            "努力帮忙选举的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "首先从这里开始\x01",
            "改变自己。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8DD")

    label("loc_893")

    OP_A2(0x6)

    ChrTalk(    #7
        0xFE,
        "刚才真是不得了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "不知到底会变成怎样，\x01",
            "说实话真捏了一把汗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8DD")

    Jump("loc_9AC")

    label("loc_8E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_934")

    ChrTalk(    #9
        0xFE,
        (
            "总之先打工吧，\x01",
            "从帮忙选举开始。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "虽然才刚刚开始，\x01",
            "工作还算顺利。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AC")

    label("loc_934")

    OP_A2(0x6)

    ChrTalk(    #11
        0xFE,
        (
            "总之先打工吧，\x01",
            "从帮忙选举开始。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "虽然才刚刚开始，\x01",
            "工作也还算是顺利吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "幸运的是父亲也很忙，\x01",
            "没空管我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AC")

    TalkEnd(0xFE)
    Return()

    # Function_2_767 end

    def Function_3_9B0(): pass

    label("Function_3_9B0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_A05")
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #14
        0x9,
        (
            "#157F……嗯～……………\x01",
            "………呜喵呜喵。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE)
    Jump("loc_A9E")

    label("loc_A05")

    OP_A2(0x5)
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #15
        0x9,
        (
            "#157F……嗯～……………\x01",
            "…………………………\x02\x03",

            "抱……住…………\x01",
            "是啊………………\x02\x03",

            "…………………………\x01",
            "………呜喵呜喵。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE)

    label("loc_A9E")

    TalkEnd(0xFE)
    Return()

    # Function_3_9B0 end

    def Function_4_AA2(): pass

    label("Function_4_AA2")

    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AC7")
    SetChrSubChip(0xFE, 2)
    Jump("loc_ACC")

    label("loc_AC7")

    SetChrSubChip(0xFE, 1)

    label("loc_ACC")

    OP_8C(0xFE, 270, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24C, 1)), scpexpr(EXPR_END)), "loc_B24")

    ChrTalk(    #16
        0x8,
        (
            "#141F嗯，那就先这样，\x01",
            "有什么事再请多关照了。\x02\x03",

            "那么，保重啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1118")

    label("loc_B24")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_F0B")
    OP_A2(0x1261)

    ChrTalk(    #17
        0x8,
        (
            "#143F嗯……？　怎么了？\x02\x03",

            "难道\x01",
            "找到犯人了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_D3C")

    ChrTalk(    #18
        0x101,
        (
            "#1015F嗯，说找到\x01",
            "也算是找到了……\x02\x03",

            "就结局来说，\x01",
            "其实是没有犯人的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "#142F怎么回事？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #20
        "\x07\x05说明了事件是意外的事故。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #21
        0x8,
        (
            "#140F……哦～原来如此啊。\x02\x03",

            "那确实是没有犯人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        "#1000F能写成报导吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "#145F不，没可能吧。\x02\x03",

            "没有事件性，\x01",
            "就没有在杂志上刊登的意义了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1007F呜～这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "#141F嗯，那就先这样，\x01",
            "有什么事再请多关照了。\x02\x03",

            "那么，我还得\x01",
            "回去写稿子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1011F啊，嗯……\x01",
            "那么，回头见。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F08")

    label("loc_D3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_D81")

    ChrTalk(    #27
        0x106,
        (
            "#050F啊啊，说找到也算找到了。\x02\x03",

            "但不是你期待的那样哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DC3")

    label("loc_D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_DC3")

    ChrTalk(    #28
        0x103,
        (
            "#020F嗯嗯，说找到也算找到了。\x02\x03",

            "但不是你期待的那样哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05说明了事件的梗概。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #30
        0x8,
        "#140F……哦～原来如此啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1000F能写成报导吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        (
            "#145F不，不太可能吧。\x02\x03",

            "这个程度的话，\x01",
            "就没有在杂志上刊登的意义了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        "#1007F呜～这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#141F嗯，那就先这样，\x01",
            "有什么事再请多关照了。\x02\x03",

            "那么，我还得\x01",
            "回去写稿子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#1006F嗯，那回头见。\x02",
    )

    CloseMessageWindow()

    label("loc_F08")

    Jump("loc_1118")

    label("loc_F0B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_10DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24C, 0)), scpexpr(EXPR_END)), "loc_F6B")

    ChrTalk(    #36
        0x8,
        (
            "#140F嗯……？\x01",
            "怎么了？\x02\x03",

            "#145F不好意思，让我专心写稿子吧。\x01",
            "就快截稿了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10D7")

    label("loc_F6B")

    OP_A2(0x1260)

    ChrTalk(    #37
        0x8,
        (
            "#140F嗯……？\x01",
            "还没走吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1015F嗯，其实\x01",
            "又发生了事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x8,
        (
            "#142F？？？\x02\x03",

            "怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1000F简而言之……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #41
        "\x07\x05向奈尔说明了伤害事件的事。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #42
        0x8,
        "#140F嗯～原来如此啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1011F咦？你好像没什么兴趣啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#140F啊啊，我觉得还\x01",
            "不足以写成报导啊。\x02\x03",

            "不过，以防万一\x01",
            "解决之后还是告诉我吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#1006F嗯，好吧。\x02",
    )

    CloseMessageWindow()

    label("loc_10D7")

    Jump("loc_1118")

    label("loc_10DA")


    ChrTalk(    #46
        0x8,
        (
            "#141F要是发生什么事件\x01",
            "一定要告诉我哦。\x02\x03",

            "那么，小心点啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1118")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xFE)
    Return()

    # Function_4_AA2 end

    def Function_5_1121(): pass

    label("Function_5_1121")

    OP_4A(0xB, 255)
    OP_4A(0xD, 255)

    ChrTalk(    #47
        0xD,
        (
            "#140F那么，下一个问题……\x02\x03",

            "候选人里有\x01",
            "旅游推进派对吧？\x02\x03",

            "对于旅游业的活性化\x01",
            "有怎样的对策？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xB,
        (
            "『旅游推进派』\x01",
            "这个说法就免了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xB,
        (
            "说得好像我只会考虑\x01",
            "旅游的事情似的。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xB, 255)
    OP_4B(0xD, 255)
    Return()

    # Function_5_1121 end

    def Function_6_11E1(): pass

    label("Function_6_11E1")

    OP_4A(0xB, 255)
    OP_4A(0xC, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1274")

    ChrTalk(    #50
        0xB,
        (
            "对了，演讲会的地方\x01",
            "已经决定了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xC,
        (
            "嗯嗯，预定在\x01",
            "伦格兰德大桥附近。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xC,
        (
            "因为都是人来人往的地方嘛。\x01",
            "一定能聚集很多听众。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_135C")

    label("loc_1274")

    OP_A2(0x1)

    ChrTalk(    #53
        0xC,
        "对了，令郎的情况怎样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xB,
        "呼，还是老样子……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xB,
        (
            "不知道在怕什么，\x01",
            "一直把自己关在房间里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xC,
        "是吗……真可怜。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xB,
        (
            "这个事\x01",
            "我再怎么叹气也没办法啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xB,
        (
            "说到底\x01",
            "还是儿子本人的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xB,
        "……还是谈谈工作吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xC,
        "啊，是。\x02",
    )

    CloseMessageWindow()

    label("loc_135C")

    OP_4B(0xB, 255)
    OP_4B(0xC, 255)
    Return()

    # Function_6_11E1 end

    def Function_7_1365(): pass

    label("Function_7_1365")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_13E1")
    OP_4A(0xB, 255)

    ChrTalk(    #61
        0xD,
        (
            "#140F不过，诺曼候选人好像\x01",
            "把旅游的活性化作为了承诺吧。\x02\x03",

            "从市民的眼光来看，\x01",
            "这样说也是可以理解的。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xB, 255)
    Jump("loc_13EB")

    label("loc_13E1")

    OP_A2(0x1)
    OP_A2(0x4)
    Call(0, 5)

    label("loc_13EB")

    TalkEnd(0xFE)
    Return()

    # Function_7_1365 end

    def Function_8_13EF(): pass

    label("Function_8_13EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1413")
    Call(1, 12)
    Jump("loc_1795")

    label("loc_1413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_15AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_147C")

    ChrTalk(    #62
        0xFE,
        (
            "我个人也觉得\x01",
            "对港湾劳动者考虑不够。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "以后为了不产生误解，\x01",
            "打算积极与他们对话。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AA")

    label("loc_147C")

    OP_A2(0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1519")

    ChrTalk(    #64
        0xFE,
        (
            "哦哦，诸位游击士啊。\x01",
            "今天真是表现精彩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "如果不是诸位解决了问题，\x01",
            "对立可会更加深化了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "那么，以后也要为市民\x01",
            "更加努力工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15AA")

    label("loc_1519")


    ChrTalk(    #67
        0xFE,
        (
            "哎呀，诸位游击士啊。\x01",
            "之前真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "总算解决了问题，真是帮大忙了。\x01",
            "一时还在担心会怎样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "那么，以后也要为市民\x01",
            "更加努力工作啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15AA")

    Jump("loc_1795")

    label("loc_15AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_164B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1641")
    OP_4A(0xD, 255)

    ChrTalk(    #70
        0xFE,
        (
            "旅游业和海运业\x01",
            "原本是一体的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "但是，考虑到将来\x01",
            "旅游业的发展是第一大事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "也就是说我主张\x01",
            "把这个作为支柱产业。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0xD, 255)
    Jump("loc_1648")

    label("loc_1641")

    OP_A2(0x1)
    Call(0, 5)

    label("loc_1648")

    Jump("loc_1795")

    label("loc_164B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_178A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_16E6")

    ChrTalk(    #73
        0xFE,
        (
            "在港口工作的人的心情\x01",
            "并不是不能理解。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        (
            "前市长时代\x01",
            "削减了港湾设施的预算，\x01",
            "设备开始老朽化了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "港口的诸位害怕\x01",
            "重蹈覆辙啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1787")

    label("loc_16E6")

    OP_A2(0x1)

    ChrTalk(    #76
        0xFE,
        (
            "卢安市的未来\x01",
            "和旅游业的发展密切相关。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "如果游客增加了，\x01",
            "城市全体的景气就会变好，\x01",
            "最后海运业也会繁盛起来的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "如果市民们能更深刻地\x01",
            "理解这件事……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1787")

    Jump("loc_1795")

    label("loc_178A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1795")
    Call(0, 6)

    label("loc_1795")

    TalkEnd(0xFE)
    Return()

    # Function_8_13EF end

    def Function_9_1799(): pass

    label("Function_9_1799")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17BA")
    Call(1, 13)

    label("loc_17BA")

    TalkEnd(0xFE)
    Return()

    # Function_9_1799 end

    def Function_10_17BE(): pass

    label("Function_10_17BE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1863")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_181B")

    ChrTalk(    #79
        0xFE,
        (
            "啊，游击士。\x01",
            "刚才真精彩啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "没有犯人，\x01",
            "说实话真松了一口气。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1860")

    label("loc_181B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_1860")

    ChrTalk(    #81
        0xFE,
        (
            "啊，游击士。\x01",
            "刚才辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "呜呜，头还阵阵地疼呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1860")

    Jump("loc_197D")

    label("loc_1863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1972")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_18BA")

    ChrTalk(    #83
        0xFE,
        (
            "骚动的契机\x01",
            "只是一点口角而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "而转瞬间\x01",
            "却引起那样的骚动……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_196F")

    label("loc_18BA")

    OP_A2(0x2)

    ChrTalk(    #85
        0xFE,
        (
            "刚才骚动的契机\x01",
            "只是一点口角而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "因为演讲会的场所问题\x01",
            "和波尔多斯阵营发生了点争执。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "相互争执着\x01",
            "不知不觉就变成那样了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "唉，真是给诺曼先生丢脸，\x01",
            "太对不起他了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196F")

    Jump("loc_197D")

    label("loc_1972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_197D")
    Call(0, 6)

    label("loc_197D")

    TalkEnd(0xFE)
    Return()

    # Function_10_17BE end

    def Function_11_1981(): pass

    label("Function_11_1981")

    Call(0, 12)
    Return()

    # Function_11_1981 end

    def Function_12_1986(): pass

    label("Function_12_1986")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19A6")
    Jump("loc_19D4")

    label("loc_19A6")

    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C3")
    OP_0D()
    OP_A9(0x6B)
    OP_56(0x0)
    TalkEnd(0xA)
    Return()

    label("loc_19C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19D4")
    TalkEnd(0xA)
    Return()

    label("loc_19D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19F5")
    Call(1, 9)
    Jump("loc_2034")

    label("loc_19F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1B13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABA")

    ChrTalk(    #89
        0xA,
        (
            "这家酒店的所有者\x01",
            "是新市长诺曼……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xA,
        (
            "前几天碰到他的时候\x01",
            "看起来好像相当疲劳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "听说这几天都\x01",
            "住在市长官邸里办公呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xA,
        (
            "市长的工作才刚刚开始。\x01",
            "希望他不要勉强就好……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1B10")

    label("loc_1ABA")


    ChrTalk(    #93
        0xA,
        (
            "诺曼大人作为市长\x01",
            "也在苦思对策的样子……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        (
            "听说这几天都\x01",
            "住在市长官邸里办公呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B10")

    Jump("loc_2034")

    label("loc_1B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB5")

    ChrTalk(    #95
        0xA,
        (
            "虽然照明和热水什么的\x01",
            "都准备了代替的手段……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xA,
        (
            "要维持平常的服务质量，\x01",
            "说实话目前相当困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xA,
        (
            "这样的状态\x01",
            "到底要持续到什么时候呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_1C27")

    label("loc_1BB5")


    ChrTalk(    #98
        0xA,
        (
            "要维持平常的服务质量，\x01",
            "说实话目前相当困难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xA,
        (
            "我身为这家酒店的代理管理者，\x01",
            "无论如何也要想办法保持水准啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C27")

    Jump("loc_2034")

    label("loc_1C2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1E68")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1D3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C9E")

    ChrTalk(    #100
        0xA,
        (
            "光临卢安的时候\x01",
            "请务必光临本酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xA,
        (
            "老板和工作人员\x01",
            "都会衷心等候您的到来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D3A")

    label("loc_1C9E")

    OP_A2(0x0)

    ChrTalk(    #102
        0xA,
        (
            "各位游击士，\x01",
            "今天真是多谢了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xA,
        (
            "我代表本酒店\x01",
            "感谢你们\x01",
            "解决了事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xA,
        (
            "再光临卢安的时候\x01",
            "请务必光临本酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xA,
        (
            "老板和工作人员\x01",
            "都会衷心等候的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D3A")

    Jump("loc_1E65")

    label("loc_1D3D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_1D87")

    ChrTalk(    #106
        0xA,
        (
            "似乎发生了\x01",
            "很严重的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xA,
        (
            "还请各位……\x01",
            "助一臂之力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E65")

    label("loc_1D87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DDA")

    ChrTalk(    #108
        0xA,
        (
            "刚才诺曼大人\x01",
            "向拉旺塔尔\x01",
            "下了订单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xA,
        (
            "好像是各位\x01",
            "活动人员的午饭。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E65")

    label("loc_1DDA")

    OP_A2(0x0)

    ChrTalk(    #110
        0xA,
        (
            "本酒店的客房服务\x01",
            "还包括向卢安市内\x01",
            "各饮食店下订单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xA,
        (
            "可以在房间一边休息并\x01",
            "一边享受各处的名产料理，\x01",
            "这是我们引以为傲的客户服务。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E65")

    Jump("loc_2034")

    label("loc_1E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1EBD")

    ChrTalk(    #112
        0xA,
        (
            "在两阵营之间\x01",
            "似乎有纠纷呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xA,
        (
            "真不希望用暴力,\x01",
            "而是用政策来战斗啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2034")

    label("loc_1EBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_1EFF")

    ChrTalk(    #114
        0xA,
        (
            "哎呀，客人。\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xA,
        (
            "好像相当\x01",
            "慌张的样子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2034")

    label("loc_1EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F73")

    ChrTalk(    #116
        0xA,
        (
            "现在因为在选举期间，\x01",
            "所以旅游的客人很少。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xA,
        (
            "客房也有些空下来，\x01",
            "可以为各位准备很不错的房间喔。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2034")

    label("loc_1F73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2034")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1FD9")

    ChrTalk(    #118
        0xA,
        (
            "现在总统套房\x01",
            "是市长候选人诺曼大人\x01",
            "的选举事务所。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xA,
        (
            "诺曼大人是本酒店\x01",
            "的老板。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2034")

    label("loc_1FD9")

    OP_A2(0x0)

    ChrTalk(    #120
        0xA,
        (
            "欢迎光临。\x01",
            "欢迎来到布朗西酒店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xA,
        (
            "本酒店全部房间都能观赏海洋景观，\x01",
            "请务必光临。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2034")

    TalkEnd(0xA)
    Return()

    # Function_12_1986 end

    def Function_13_2038(): pass

    label("Function_13_2038")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_20FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20BA")

    ChrTalk(    #122
        0xFE,
        "那些卷着印花头巾的人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "看起来像是城里人，\x01",
            "会不会是青年团？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "呵呵，精神十足\x01",
            "又清爽的感觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_20FB")

    label("loc_20BA")


    ChrTalk(    #125
        0xFE,
        (
            "那些卷着印花头巾的人\x01",
            "会不会是青年团？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "感觉精神又清爽。\x02",
    )

    CloseMessageWindow()

    label("loc_20FB")

    Jump("loc_21E3")

    label("loc_20FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_21E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21A1")

    ChrTalk(    #127
        0xFE,
        (
            "我是从柏斯\x01",
            "过来旅行的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "但是好像定期船\x01",
            "又停运了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "上次来这里的时候，\x01",
            "也是哪都不能去啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "唉，我和定期船\x01",
            "好像性格不合啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x11)
    Jump("loc_21E3")

    label("loc_21A1")


    ChrTalk(    #131
        0xFE,
        (
            "定期船\x01",
            "又停运了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "好了，怎么办呢……\x01",
            "要延长逗留时间吗。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E3")

    TalkEnd(0x13)
    Return()

    # Function_13_2038 end

    def Function_14_21E7(): pass

    label("Function_14_21E7")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_22CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2282")

    ChrTalk(    #133
        0xFE,
        (
            "市长身边有同辈的德尔斯\x01",
            "留下当秘书……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0xFE,
        (
            "听服务台的人说，\x01",
            "好像相当忙碌的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "唔，定期船也不会来，\x01",
            "可能该回去帮忙吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_22CC")

    label("loc_2282")


    ChrTalk(    #136
        0xFE,
        (
            "诺曼市长的助理\x01",
            "是德尔斯……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "反正定期船也不会来\x01",
            "要不要去帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22CC")

    Jump("loc_2415")

    label("loc_22CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2415")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B0")

    ChrTalk(    #138
        0xFE,
        (
            "选举后的杂务也总算结束了，\x01",
            "正想返回王都……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "结果那个贝壳一样的物体出现在天空，\x01",
            "把导力器都停住了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "呼，但是回王都\x01",
            "到底是不能靠步行啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "要通过漆黑的卡鲁迪亚隧道\x01",
            "对我来说是绝对不可能的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x12)
    Jump("loc_2415")

    label("loc_23B0")


    ChrTalk(    #142
        0xFE,
        (
            "可是，到底什么时候\x01",
            "定期船才会恢复原状呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "要是会继续延期，\x01",
            "回去帮市长的忙\x01",
            "可能会比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2415")

    TalkEnd(0x11)
    Return()

    # Function_14_21E7 end

    def Function_15_2419(): pass

    label("Function_15_2419")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_24EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2473")

    ChrTalk(    #144
        0xFE,
        (
            "南区的渡口\x01",
            "在这边地下。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0xFE,
        (
            "要使用的人\x01",
            "请从台阶到地下１层。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_24E7")

    label("loc_2473")


    ChrTalk(    #146
        0xFE,
        (
            "嘿嘿，差不多\x01",
            "也习惯礼貌说话了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "开始觉得挺烦的，\x01",
            "但现在却觉得很充实。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "能帮别人的忙，\x01",
            "心情真是好。\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x13)

    label("loc_24E7")

    Jump("loc_25C5")

    label("loc_24EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_25C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_254F")

    ChrTalk(    #149
        0xFE,
        (
            "嗯～南区的渡口\x01",
            "可以从地下１层前往。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0xFE,
        (
            "要使用的人请、请……\x01",
            "请往下边走。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x13)
    Jump("loc_25C5")

    label("loc_254F")


    ChrTalk(    #151
        0xFE,
        (
            "可、可恶。\x01",
            "字到嘴边说不出来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xFE,
        (
            "要使用的人\x01",
            "请．这．边．走……吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "好，这样就顺畅了。\x01",
            "不会再说错了！\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x13)

    label("loc_25C5")

    TalkEnd(0x12)
    Return()

    # Function_15_2419 end

    def Function_16_25C9(): pass

    label("Function_16_25C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25DA")
    Call(0, 21)

    label("loc_25DA")

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

    def lambda_2647():
        OP_6D(27120, 0, 48140, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2647)
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
            "#1001F#6P你们好～#1425W #20W \x01",
            "#1004F唔……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 1)

    ChrTalk(    #155
        0x8,
        (
            "#143F#5P是、是你们啊。\x02\x03",

            "#141F我听朵洛希说了。\x01",
            "幽灵骚动好像解决了啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2719():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2719)
    Sleep(50)

    def lambda_272C():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_272C)
    Sleep(50)

    def lambda_273F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_273F)
    Sleep(50)

    def lambda_2752():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2752)
    WaitChrThread(0x104, 0x1)
    Sleep(300)

    ChrTalk(    #156
        0x101,
        (
            "#1015F嗯，算是吧……\x02\x03",

            "朵洛希怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x8,
        (
            "#142F#5P报告事件的时候\x01",
            "她就一直很困的样子……\x02\x03",

            "刚一结束就大睡起来，\x01",
            "没办法只好抬到床上去了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2841")

    ChrTalk(    #158
        0x106,
        (
            "#051F#6P不过昨天一直忙到半夜，\x01",
            "发生了很多事嘛。\x02\x03",

            "可能是太累了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2888")

    label("loc_2841")


    ChrTalk(    #159
        0x103,
        (
            "#027F#6P不过昨天一直忙到半夜，\x01",
            "她都陪着我们。\x02\x03",

            "会犯困也没办法吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2888")


    ChrTalk(    #160
        0x8,
        (
            "#145F#5P哼，能够持续熬夜\x01",
            "才是够格的记者啦。\x02\x03",

            "#141F对了，光听这家伙的说明\x01",
            "还是有点不是很明白……\x02\x03",

            "关于此次的事件\x01",
            "可以问几个问题吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        "#1006F嗯，好啊。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #162
        (
            "\x07\x05艾丝蒂尔等人一边回答奈尔的问题\x01",
            "一边说明了事件的来龙去脉。\x02",
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
            "#145F#5P原来如此，大致明白了。\x02\x03",

            "#142F话说回来『怪盗Ｂ』\x01",
            "竟然来了利贝尔……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        (
            "#1004F咦……！\x02\x03",

            "#1005F奈尔竟然\x01",
            "知道怪盗男！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x8,
        (
            "#142F#5P好像是在大陆各地大都市\x01",
            "引起骚乱的有名盗贼哦。\x02\x03",

            "瞄准了的猎物绝对不会放跑。\x01",
            "华丽地偷盗然后离开……\x02\x03",

            "好像就是个这么做作的盗贼。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2AC7")

    ChrTalk(    #166
        0x106,
        (
            "#555F#6P哼……\x01",
            "同一个人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AF2")

    label("loc_2AC7")


    ChrTalk(    #167
        0x103,
        (
            "#022F#6P原来如此……\x01",
            "像是同一个人呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B8B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇完成了烛台失窃事件任务】\x01",      # 0
            "【◇未完成烛台失窃事件任务】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2B72"),
        (1, "loc_2B7A"),
        (SWITCH_DEFAULT, "loc_2B82"),
    )


    label("loc_2B72")

    OP_28(0x20, 0x3, 0x10)
    Jump("loc_2B82")

    label("loc_2B7A")

    OP_28(0x20, 0x4, 0x10)
    Jump("loc_2B82")

    label("loc_2B82")

    FadeToBright(300, 0)

    label("loc_2B8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2BBC")

    ChrTalk(    #168
        0x101,
        (
            "#1007F本人也这么说了，\x01",
            "应该没错。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BBC")


    ChrTalk(    #169
        0x8,
        (
            "#145F#5P不过，那个『怪盗Ｂ』\x01",
            "竟然是结社的爪牙。\x02\x03",

            "『噬身之蛇』……\x01",
            "真是群来路不明的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x105,
        (
            "#043F#6P那个，奈尔。\x02\x03",

            "关于此次的事件\x01",
            "打算报导多少呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x8,
        (
            "#140F#5P啊，其实协会和王国军\x01",
            "拜托我控制\x01",
            "关于结社的报导。\x02\x03",

            "我想应该会写成\x01",
            "『恶性愉快犯』所为吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x104,
        (
            "#035F不过，政变也终结了，\x01",
            "国内总算安定了。\x02\x03",

            "#030F考虑到市民的不安，\x01",
            "这可说是妥当的判断吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x8,
        (
            "#145F#5P作为记者很不甘心，\x01",
            "不过这个我也理解。\x02\x03",

            "#141F不过作为补偿，如果再发生什么事\x01",
            "也一定要告诉我们哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x101,
        (
            "#1006F嗯，明白了。\x02\x03",

            "那么，我们\x01",
            "就出发去蔡斯了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x8,
        (
            "#143F#5P哦哦，是吗。\x02\x03",

            "我还要写稿子\x01",
            "没法去送行……\x02\x03",

            "不过我去把朵洛希那家伙弄醒吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        (
            "#1016F啊，不用了不用了。\x01",
            "难得睡得那么香嘛。\x02\x03",

            "#1011F奈尔帮忙打个招呼吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x8,
        (
            "#141F#5P明白了。\x01",
            "多加小心哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0)
    OP_A2(0x1401)
    EventEnd(0x0)
    Return()

    # Function_16_25C9 end

    def Function_17_2E92(): pass

    label("Function_17_2E92")

    SetChrPos(0xFE, 23940, 0, 47510, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2EB9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EB9)
    OP_8E(0xFE, 0x69F0, 0x0, 0xB928, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_17_2E92 end

    def Function_18_2EE1(): pass

    label("Function_18_2EE1")

    SetChrPos(0xFE, 23940, 0, 47510, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2F08():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F08)
    OP_8E(0xFE, 0x65FE, 0x0, 0xB8EC, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_18_2EE1 end

    def Function_19_2F30(): pass

    label("Function_19_2F30")

    SetChrPos(0xFE, 23860, 0, 46420, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2F57():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F57)
    OP_8E(0xFE, 0x6586, 0x0, 0xB4E6, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_19_2F30 end

    def Function_20_2F7F(): pass

    label("Function_20_2F7F")

    SetChrPos(0xFE, 23860, 0, 46420, 90)
    ClearChrFlags(0xFE, 0x80)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2FA6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FA6)
    OP_8E(0xFE, 0x6978, 0x0, 0xB4DC, 0x7D0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_20_2F7F end

    def Function_21_2FCE(): pass

    label("Function_21_2FCE")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3048"),
        (1, "loc_304E"),
        (SWITCH_DEFAULT, "loc_3054"),
    )


    label("loc_3048")

    OP_A2(0x1200)
    Jump("loc_3054")

    label("loc_304E")

    OP_A2(0x1201)
    Jump("loc_3054")

    label("loc_3054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3062")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_3066")

    label("loc_3062")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_3066")

    Return()

    # Function_21_2FCE end

    SaveToFile()

Try(main)
