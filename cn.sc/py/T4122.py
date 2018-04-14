from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4122   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4122.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
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
        '菲尔妲',                               # 9
        '莎夏',                                 # 10
        '哈尔德',                               # 11
        '乘客',                                 # 12
        '乘客',                                 # 13
        '乘客',                                 # 14
        '布露姆老奶奶',                         # 15
        '莉莉',                                 # 16
        '丹顿',                                 # 17
        '蜜蒂',                                 # 18
        '艾德尔店长',                           # 19
        '基蒂',                                 # 20
        '希娜',                                 # 21
        '特雷诺',                               # 22
        '布露姆老奶奶',                         # 23
        '阿加特',                               # 24
        '雪拉扎德',                             # 25
        '提妲',                                 # 26
        '穆拉',                                 # 27
        '中年男子',                             # 28
        '戴眼镜的女性',                         # 29
        '玲',                                   # 30
        '目标用照相机',                         # 31
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
        'ED6_DT07/CH01290 ._CH',             # 00
        'ED6_DT07/CH01540 ._CH',             # 01
        'ED6_DT27/CH03570 ._CH',             # 02
        'ED6_DT27/CH03710 ._CH',             # 03
        'ED6_DT27/CH03720 ._CH',             # 04
        'ED6_DT27/CH03510 ._CH',             # 05
        'ED6_DT07/CH01150 ._CH',             # 06
        'ED6_DT07/CH01020 ._CH',             # 07
        'ED6_DT07/CH01770 ._CH',             # 08
        'ED6_DT07/CH01210 ._CH',             # 09
        'ED6_DT07/CH01120 ._CH',             # 0A
        'ED6_DT07/CH01130 ._CH',             # 0B
        'ED6_DT07/CH01010 ._CH',             # 0C
        'ED6_DT07/CH01013 ._CH',             # 0D
        'ED6_DT07/CH00050 ._CH',             # 0E
        'ED6_DT07/CH00020 ._CH',             # 0F
        'ED6_DT27/CH03060 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH01290P._CP',             # 00
        'ED6_DT07/CH01540P._CP',             # 01
        'ED6_DT27/CH03570P._CP',             # 02
        'ED6_DT27/CH03710P._CP',             # 03
        'ED6_DT27/CH03720P._CP',             # 04
        'ED6_DT27/CH03510P._CP',             # 05
        'ED6_DT07/CH01150P._CP',             # 06
        'ED6_DT07/CH01020P._CP',             # 07
        'ED6_DT07/CH01770P._CP',             # 08
        'ED6_DT07/CH01210P._CP',             # 09
        'ED6_DT07/CH01120P._CP',             # 0A
        'ED6_DT07/CH01130P._CP',             # 0B
        'ED6_DT07/CH01010P._CP',             # 0C
        'ED6_DT07/CH01013P._CP',             # 0D
        'ED6_DT07/CH00050P._CP',             # 0E
        'ED6_DT07/CH00020P._CP',             # 0F
        'ED6_DT27/CH03060P._CP',             # 10
    )

    DeclNpc(
        X                   = -1440,
        Z                   = 0,
        Y                   = 65550,
        Direction           = 179,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
    )

    DeclNpc(
        X                   = 1970,
        Z                   = 0,
        Y                   = 65550,
        Direction           = 175,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 18,
    )

    DeclNpc(
        X                   = -3140,
        Z                   = 0,
        Y                   = 63640,
        Direction           = 6,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 19,
    )

    DeclNpc(
        X                   = -4370,
        Z                   = 0,
        Y                   = 62760,
        Direction           = 92,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 20,
    )

    DeclNpc(
        X                   = 4950,
        Z                   = 0,
        Y                   = 60820,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
    )

    DeclNpc(
        X                   = -3020,
        Z                   = 0,
        Y                   = 57190,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )

    DeclNpc(
        X                   = 3110,
        Z                   = 250,
        Y                   = 60150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 8790,
        Z                   = 0,
        Y                   = 10500,
        Direction           = 196,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 12170,
        Z                   = 0,
        Y                   = -4050,
        Direction           = 163,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = 9850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -50,
        Z                   = 0,
        Y                   = 10,
        Direction           = 204,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -13690,
        Z                   = 250,
        Y                   = 11270,
        Direction           = 191,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -13060,
        Z                   = 0,
        Y                   = 6390,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 13590,
        Z                   = 0,
        Y                   = -8540,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = -10100,
        Z                   = 0,
        Y                   = -7930,
        Direction           = 200,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 90,
        Z                   = 0,
        Y                   = 63630,
        Direction           = 343,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 24,
    )

    DeclNpc(
        X                   = 90,
        Z                   = 0,
        Y                   = 63630,
        Direction           = 343,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 25,
    )

    DeclNpc(
        X                   = 2900,
        Z                   = 0,
        Y                   = 3330,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 26,
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
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 27,
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


    DeclActor(
        TriggerX            = 8450,
        TriggerZ            = 0,
        TriggerY            = 8650,
        TriggerRange        = 800,
        ActorX              = 8790,
        ActorZ              = 1500,
        ActorY              = 10500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 11970,
        TriggerZ            = 0,
        TriggerY            = -5950,
        TriggerRange        = 800,
        ActorX              = 12170,
        ActorZ              = 1500,
        ActorY              = -4050,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6400,
        TriggerZ            = 0,
        TriggerY            = 9620,
        TriggerRange        = 800,
        ActorX              = -4540,
        ActorZ              = 1500,
        ActorY              = 9850,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1370,
        TriggerZ            = 0,
        TriggerY            = 63610,
        TriggerRange        = 800,
        ActorX              = -1440,
        ActorZ              = 1500,
        ActorY              = 65550,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1850,
        TriggerZ            = 0,
        TriggerY            = 63640,
        TriggerRange        = 800,
        ActorX              = 1970,
        ActorZ              = 1500,
        ActorY              = 65550,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4C6",          # 00, 0
        "Function_1_5D8",          # 01, 1
        "Function_2_669",          # 02, 2
        "Function_3_7E6",          # 03, 3
        "Function_4_80A",          # 04, 4
        "Function_5_80F",          # 05, 5
        "Function_6_BF0",          # 06, 6
        "Function_7_BF5",          # 07, 7
        "Function_8_EBA",          # 08, 8
        "Function_9_EBF",          # 09, 9
        "Function_10_13BC",        # 0A, 10
        "Function_11_16BA",        # 0B, 11
        "Function_12_188C",        # 0C, 12
        "Function_13_1A88",        # 0D, 13
        "Function_14_1D24",        # 0E, 14
        "Function_15_1F9E",        # 0F, 15
        "Function_16_1FA3",        # 10, 16
        "Function_17_252D",        # 11, 17
        "Function_18_2532",        # 12, 18
        "Function_19_2BAA",        # 13, 19
        "Function_20_2E9D",        # 14, 20
        "Function_21_2EFA",        # 15, 21
        "Function_22_2F2E",        # 16, 22
        "Function_23_2F83",        # 17, 23
        "Function_24_2F99",        # 18, 24
        "Function_25_3079",        # 19, 25
        "Function_26_3141",        # 1A, 26
        "Function_27_323A",        # 1B, 27
        "Function_28_34C7",        # 1C, 28
        "Function_29_4E94",        # 1D, 29
        "Function_30_4EEA",        # 1E, 30
        "Function_31_4EFF",        # 1F, 31
        "Function_32_4F14",        # 20, 32
        "Function_33_570A",        # 21, 33
        "Function_34_57A6",        # 22, 34
    )


    def Function_0_4C6(): pass

    label("Function_0_4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4EF")
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x11, -13690, 250, 11270, 191)
    OP_64(0x2, 0x1)
    SetChrFlags(0x16, 0x80)
    Jump("loc_586")

    label("loc_4EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_51D")
    SetChrFlags(0x13, 0x80)
    SetChrPos(0x11, -13690, 250, 11270, 191)
    OP_64(0x2, 0x1)
    SetChrFlags(0x16, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_586")

    label("loc_51D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_56A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_567")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_540")
    ClearChrFlags(0x17, 0x80)
    Jump("loc_545")

    label("loc_540")

    ClearChrFlags(0x18, 0x80)

    label("loc_545")

    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 5430, 0, 1900, 0)
    OP_43(0x1D, 0x0, 0x0, 0x2)

    label("loc_567")

    Jump("loc_586")

    label("loc_56A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_586")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_586")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5A2"),
        (101, "loc_5A2"),
        (102, "loc_5A2"),
        (103, "loc_5A2"),
        (104, "loc_5BA"),
        (SWITCH_DEFAULT, "loc_5D7"),
    )


    label("loc_5A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5B7")
    SetMapFlags(0x10000000)
    Event(0, 32)

    label("loc_5B7")

    Jump("loc_5D7")

    label("loc_5BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D4")
    ClearMapFlags(0x10)
    SetMapFlags(0x10000000)
    Event(0, 28)

    label("loc_5D4")

    Jump("loc_5D7")

    label("loc_5D7")

    Return()

    # Function_0_4C6 end

    def Function_1_5D8(): pass

    label("Function_1_5D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F4")
    OP_B1("t4122_y")
    Jump("loc_5FD")

    label("loc_5F4")

    OP_B1("t4122_n")

    label("loc_5FD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_615")
    OP_10(0x6, 0x0)
    OP_10(0x5, 0x1)
    OP_10(0x4, 0x0)
    Jump("loc_644")

    label("loc_615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_628")
    OP_10(0x6, 0x0)
    OP_10(0x5, 0x0)
    OP_10(0x4, 0x1)
    Jump("loc_644")

    label("loc_628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_63B")
    OP_10(0x6, 0x0)
    OP_10(0x4, 0x0)
    OP_10(0x5, 0x1)
    Jump("loc_644")

    label("loc_63B")

    OP_10(0x6, 0x0)
    OP_10(0x5, 0x0)
    OP_10(0x4, 0x1)

    label("loc_644")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_668")
    OP_72(0x0, 0x10)
    OP_6F(0x0, 59)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 59)

    label("loc_668")

    Return()

    # Function_1_5D8 end

    def Function_2_669(): pass

    label("Function_2_669")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_68E")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_7D0")

    label("loc_68E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A7")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_7D0")

    label("loc_6A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C0")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_7D0")

    label("loc_6C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D9")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_7D0")

    label("loc_6D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F2")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_7D0")

    label("loc_6F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70B")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_7D0")

    label("loc_70B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_724")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_7D0")

    label("loc_724")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73D")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_7D0")

    label("loc_73D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_756")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_7D0")

    label("loc_756")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76F")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_7D0")

    label("loc_76F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_788")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_7D0")

    label("loc_788")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A1")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_7D0")

    label("loc_7A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7BA")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_7D0")

    label("loc_7BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7D0")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_7D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E5")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_7D0")

    label("loc_7E5")

    Return()

    # Function_2_669 end

    def Function_3_7E6(): pass

    label("Function_3_7E6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_809")
    OP_8D(0xFE, -11560, -6690, -7260, -10580, 1000)
    Jump("Function_3_7E6")

    label("loc_809")

    Return()

    # Function_3_7E6 end

    def Function_4_80A(): pass

    label("Function_4_80A")

    Call(0, 5)
    Return()

    # Function_4_80A end

    def Function_5_80F(): pass

    label("Function_5_80F")

    TalkBegin(0xF)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_849")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_834")
    OP_A9(0xD8)
    Jump("loc_842")

    label("loc_834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_840")
    OP_A9(0xD7)
    Jump("loc_842")

    label("loc_840")

    OP_A9(0xD2)

    label("loc_842")

    TalkEnd(0xF)
    Return()

    label("loc_849")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85A")
    TalkEnd(0xF)
    Return()

    label("loc_85A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_903")

    ChrTalk(    #0
        0xF,
        "欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xF,
        (
            "因为导力的停止，\x01",
            "利贝尔通讯的最新一期\x01",
            "只在王都发售哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xF,
        (
            "即便如此，我还是很佩服能按时\x01",
            "制作出杂志的编辑和记者。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xF,
        "我也得努力贩卖啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BEC")

    label("loc_903")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_969")

    ChrTalk(    #4
        0xF,
        (
            "今天从早上起大家就\x01",
            "都在议论那起事件。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xF,
        (
            "能在签字仪式前抓获\x01",
            "情报部的余党真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEC")

    label("loc_969")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_A17")

    ChrTalk(    #6
        0xF,
        (
            "尊敬的顾客，利贝尔通讯的\x01",
            "最新一期已经到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xF,
        (
            "特辑可是卢安市长的\x01",
            "选举结果哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xF,
        (
            "我虽然不能在工作时间阅读，\x01",
            "不过封面还是能看清的，\x01",
            "真是令人牵肠挂肚啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BEC")

    label("loc_A17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8C")

    ChrTalk(    #9
        0xF,
        (
            "对柏斯超市的考察\x01",
            "似乎深深刺激了\x01",
            "基蒂小姐呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xF,
        (
            "她说下次休假\x01",
            "还要去柏斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xF,
        "难道基蒂小姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BEC")

    label("loc_A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_BAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5B")

    ChrTalk(    #12
        0xF,
        (
            "前几天我们在店长的\x01",
            "计划下去考察了柏斯超市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xF,
        (
            "我还真担心对方\x01",
            "会认出我是同行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xF,
        (
            "店长还向店员堂而皇之地\x01",
            "咨询了进货的价格呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xF,
        (
            "那份爽快的气质似乎还\x01",
            "很受柏斯市长的赏识……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_BA7")

    label("loc_B5B")


    ChrTalk(    #16
        0xF,
        (
            "店长和柏斯市长还挺\x01",
            "惺惺相惜的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xF,
        (
            "今后还会通过交换信息\x01",
            "来相互合作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA7")

    Jump("loc_BEC")

    label("loc_BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_BEC")

    ChrTalk(    #18
        0xF,
        "欢迎～！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xF,
        (
            "艾德尔百货店从礼品\x01",
            "到日用品应有尽有哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEC")

    TalkEnd(0xF)
    Return()

    # Function_5_80F end

    def Function_6_BF0(): pass

    label("Function_6_BF0")

    Call(0, 7)
    Return()

    # Function_6_BF0 end

    def Function_7_BF5(): pass

    label("Function_7_BF5")

    TalkBegin(0x10)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C12")
    OP_A9(0xD3)
    TalkEnd(0x10)
    Return()

    label("loc_C12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C23")
    TalkEnd(0x10)
    Return()

    label("loc_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_C78")

    ChrTalk(    #20
        0x10,
        "我们店长很可靠吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "平日里那句『我在雪山上\x01",
            "也要卖冰』可不是盖的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB6")

    label("loc_C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_D00")

    ChrTalk(    #22
        0x10,
        (
            "理查德上校在市民中\x01",
            "很有人气。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "我也能理解作为他直属部下的\x01",
            "情报部的那群人的心情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        "不过也不用出动坦克吧……坦克！\x02",
    )

    CloseMessageWindow()
    Jump("loc_EB6")

    label("loc_D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_D75")

    ChrTalk(    #25
        0x10,
        (
            "卢安市长已经\x01",
            "决定了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "希望这样一来各种\x01",
            "交易都能顺利进行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "一定要请这位新\x01",
            "市长多多努力了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB6")

    label("loc_D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DDD")

    ChrTalk(    #28
        0x10,
        (
            "不过我从顾客那里听到\x01",
            "一个传言，不知是真是假。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "好像说卢安的各地\x01",
            "都出现了幽灵……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB6")

    label("loc_DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_E78")

    ChrTalk(    #30
        0x10,
        (
            "真希望卢安的新市长\x01",
            "能够快点选出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "自从戴尔蒙市长事件以来，\x01",
            "卢安方向的物流就很混乱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10,
        (
            "也难怪，因为有很多手续\x01",
            "必须有市长的许可。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EB6")

    label("loc_E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_EB6")

    ChrTalk(    #33
        0x10,
        "欢迎光临，你们是观光吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x10,
        (
            "这里有各式\x01",
            "礼品哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EB6")

    TalkEnd(0x10)
    Return()

    # Function_7_BF5 end

    def Function_8_EBA(): pass

    label("Function_8_EBA")

    Call(0, 9)
    Return()

    # Function_8_EBA end

    def Function_9_EBF(): pass

    label("Function_9_EBF")

    TalkBegin(0x11)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDC")
    OP_A9(0xD4)
    TalkEnd(0x11)
    Return()

    label("loc_EDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EED")
    TalkEnd(0x11)
    Return()

    label("loc_EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_F91")

    ChrTalk(    #35
        0x11,
        (
            "本是去柏斯的\x01",
            "姐姐现在好像在洛连特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x11,
        "呼，太好了……她没事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x11,
        "我、我可没在担心她。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        (
            "都是因为我要和她堂堂正正\x01",
            "地较量，夺取红茶销售员职务。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B8")

    label("loc_F91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1094")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1041")

    ChrTalk(    #39
        0x11,
        (
            "姐姐为了开一间自己的店，\x01",
            "好像要去柏斯学习。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x11,
        (
            "有可能就会辞去\x01",
            "百货商店的工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x11,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x11,
        (
            "姐姐，别丢下我，\x01",
            "我会寂寞的……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1091")

    label("loc_1041")


    ChrTalk(    #43
        0x11,
        (
            "姐姐有可能就要辞去\x01",
            "百货商店的工作……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x11,
        (
            "姐姐，别丢下我，\x01",
            "我会寂寞的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1091")

    Jump("loc_13B8")

    label("loc_1094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1119")

    ChrTalk(    #45
        0x11,
        (
            "呼呼呼……\x01",
            "来了……终于来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x11,
        (
            "在姐姐不在期间，\x01",
            "由我负责红茶销售。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x11,
        (
            "看着吧，我要从姐姐那里\x01",
            "抢走销售员的位子！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B8")

    label("loc_1119")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_118F")

    ChrTalk(    #48
        0x11,
        (
            "最近姐姐好像\x01",
            "一直在想心事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        "看着吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x11,
        (
            "我要在她还在发呆的时候\x01",
            "让她失去红茶销售员的职位。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B8")

    label("loc_118F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_12C2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1278")

    ChrTalk(    #51
        0x11,
        (
            "现在想想，姐姐从小到大\x01",
            "都是一个人占便宜！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x11,
        (
            "因为她低血压，每天早上\x01",
            "总是我去拿报纸！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x11,
        (
            "因为她害怕蟑螂，\x01",
            "每次都是我负责消灭！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x11,
        (
            "明明是双胞胎，为什么\x01",
            "只有我吃了甜的会发胖！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x11,
        "每一条都令人无法原谅！\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_12BF")

    label("loc_1278")


    ChrTalk(    #56
        0x11,
        "看着吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x11,
        (
            "至少要让她把从我这里夺走的\x01",
            "红茶销售员位子抢回来！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BF")

    Jump("loc_13B8")

    label("loc_12C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_13B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1375")

    ChrTalk(    #58
        0x11,
        (
            "嗯～泡出美味红茶的\x01",
            "黄金秘诀……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x11,
        (
            "……我这个人，\x01",
            "一听到『学习』这两个字\x01",
            "就犯困……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x11,
        "啊，不可以不可以。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x11,
        (
            "一切都为了夺回姐姐的\x01",
            "红茶销售员位子！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_13B8")

    label("loc_1375")


    ChrTalk(    #62
        0x11,
        "可恶！绝不能睡着！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x11,
        (
            "一切都为了夺回姐姐的\x01",
            "红茶销售员位子！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B8")

    TalkEnd(0x11)
    Return()

    # Function_9_EBF end

    def Function_10_13BC(): pass

    label("Function_10_13BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_146E")

    ChrTalk(    #64
        0xFE,
        (
            "没有货进来的话，\x01",
            "只能我们自己去进货来卖了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "能卖的都要卖得一干二净！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "因为顾客需要\x01",
            "我们的商品。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "就算有些事我们没办法，\x01",
            "可是还有一大堆可以做的事！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B6")

    label("loc_146E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_14FB")

    ChrTalk(    #68
        0xFE,
        (
            "我家在西街区，\x01",
            "能听到港口传来很响的声音。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "想不到竟是情报部的坦克，\x01",
            "连我也吓了一跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "还好房子没被那玩意儿\x01",
            "给毁了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B6")

    label("loc_14FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1586")

    ChrTalk(    #71
        0xFE,
        (
            "刚才出去的那女孩子，\x01",
            "最近好像常见到……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "好像是个游客，\x01",
            "可她父母呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "有很多小孩子在这家店\x01",
            "迷路，真有点担心她呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B6")

    label("loc_1586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15D4")

    ChrTalk(    #74
        0xFE,
        (
            "实在抱歉，\x01",
            "本店很快就要打烊了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        (
            "欢迎您的\x01",
            "再度光临～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B6")

    label("loc_15D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1651")

    ChrTalk(    #76
        0xFE,
        (
            "这种时节销售额\x01",
            "很容易下滑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "所以更要利用签字仪式\x01",
            "这一大事件了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "好，我们要大搞条约\x01",
            "缔结纪念的促销！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B6")

    label("loc_1651")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_16B6")

    ChrTalk(    #79
        0xFE,
        (
            "欢迎光临，\x01",
            "欢迎光临艾德尔百货店。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "我们正在为了打倒柏斯超市\x01",
            "这一目标而不懈地努力～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B6")

    TalkEnd(0xFE)
    Return()

    # Function_10_13BC end

    def Function_11_16BA(): pass

    label("Function_11_16BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1705")

    ChrTalk(    #81
        0xFE,
        (
            "我从明天起要\x01",
            "休假一阵子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "红茶角就交给\x01",
            "妹妹蜜蒂了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1888")

    label("loc_1705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1793")

    ChrTalk(    #83
        0xFE,
        (
            "能被带去参观\x01",
            "柏斯超市真让我\x01",
            "受益匪浅。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "不仅如此，我还……\x01",
            "找到了自己前进的方向。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0xFE,
        (
            "虽然现在还不能告诉\x01",
            "妹妹蜜蒂……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1888")

    label("loc_1793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1819")

    ChrTalk(    #86
        0xFE,
        "欢迎光临！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xFE,
        (
            "尊敬的客人，要不要\x01",
            "来一杯美味的红茶？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "如果您想知道怎样\x01",
            "泡出美味的红茶\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        "就问我吧，请不要客气。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1888")

    label("loc_1819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1888")

    ChrTalk(    #90
        0xFE,
        (
            "前几天我和店里的同事们\x01",
            "去参观了柏斯的市场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        (
            "超市里面的每个人\x01",
            "都很努力……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "这令我很感动。\x02",
    )

    CloseMessageWindow()

    label("loc_1888")

    TalkEnd(0xFE)
    Return()

    # Function_11_16BA end

    def Function_12_188C(): pass

    label("Function_12_188C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1911")

    ChrTalk(    #93
        0xFE,
        (
            "最近，鱼都从钓公师团买，\x01",
            "而不是从卢安了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "本以为他们只是普通的兴趣团体，\x01",
            "不过在导力停止后他们真是活跃啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A84")

    label("loc_1911")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_196B")

    ChrTalk(    #95
        0xFE,
        (
            "城里很吵啊，\x01",
            "是不是出了什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "最近我忙于家务，\x01",
            "都有点不问世事了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A84")

    label("loc_196B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_19B3")

    ChrTalk(    #97
        0xFE,
        (
            "好想吃久违的\x01",
            "卢安海鲜啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "最近在这儿都\x01",
            "很难买到了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A84")

    label("loc_19B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19F2")

    ChrTalk(    #99
        0xFE,
        (
            "唔～今天来得太晚，\x01",
            "都没什么好东西留下了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A84")

    label("loc_19F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1A23")

    ChrTalk(    #100
        0xFE,
        (
            "为了健康也得\x01",
            "让我家那口子吃蔬菜。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A84")

    label("loc_1A23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1A84")

    ChrTalk(    #101
        0xFE,
        (
            "最近在蔡斯似乎\x01",
            "频繁发生着地震呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xFE,
        (
            "近来我都没去了，\x01",
            "也不知道亚尔摩温泉怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A84")

    TalkEnd(0xFE)
    Return()

    # Function_12_188C end

    def Function_13_1A88(): pass

    label("Function_13_1A88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1ADC")

    ChrTalk(    #103
        0xFE,
        (
            "现在比起那些瓶瓶罐罐的，\x01",
            "还是得先保存食品……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        "真是不得了了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D20")

    label("loc_1ADC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1B69")

    ChrTalk(    #105
        0xFE,
        (
            "昨晚我看见亲卫队的队员\x01",
            "跑去西街区哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "一架像大炮一样的东西\x01",
            "从飞船坪移动过来了，\x01",
            "那是什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        "这、这还闹得真不小……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D20")

    label("loc_1B69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1BD6")

    ChrTalk(    #108
        0xFE,
        "嗯？你们好像在赶时间？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "由我这个顾客来说可能不太合适，\x01",
            "不过你们可别碰翻这些瓶瓶罐罐的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D20")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C1F")

    ChrTalk(    #110
        0xFE,
        "已经傍晚了啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "得赶紧回去了，\x01",
            "不然老婆要唠叨。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D20")

    label("loc_1C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1C69")

    ChrTalk(    #112
        0xFE,
        "哟，这壶是中世纪帝国的东西啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "……真是个不错的壶。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D20")

    label("loc_1C69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1D20")

    ChrTalk(    #114
        0xFE,
        (
            "做为政变的主犯之一……\x01",
            "杜南公爵好像受到了女王\x01",
            "陛下要求他谨慎而居的处分呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "自称是公爵管家的人\x01",
            "时常来这家店买东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "可不知为什么，\x01",
            "每次来买的都是炸面圈和连环画。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D20")

    TalkEnd(0xFE)
    Return()

    # Function_13_1A88 end

    def Function_14_1D24(): pass

    label("Function_14_1D24")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1D7C")

    ChrTalk(    #117
        0xFE,
        "嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "我还是没能为儿子\x01",
            "找到结婚对象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        "真是羞愧又不甘心……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F9A")

    label("loc_1D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1E1D")

    ChrTalk(    #120
        0xFE,
        (
            "我为儿子找结婚对象很久了，\x01",
            "不过仍然没有合适的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "王都的人是多，\x01",
            "不过都是些吊儿郎当的孩子，\x01",
            "怎么也看不上眼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "真是的，看来得换个街区了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F9A")

    label("loc_1E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ED9")
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #123
        0xFE,
        "……我好像在哪儿见过你。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        (
            "（嗯……好像\x01",
            "#1015F　是在哪儿见过。）\x02\x03",

            "（……她是谁？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "我这几个月看过\x01",
            "不少女孩子，\x01",
            "不可能一个个都记住。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "我可没有在发呆！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F9A")

    label("loc_1ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1F64")

    ChrTalk(    #127
        0xFE,
        (
            "我是为了给儿子找结婚对象\x01",
            "才来的王都。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "如果你们认识好的女孩子\x01",
            "一定要介绍给我哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "怎么也找不到让我\x01",
            "满意的女孩子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F9A")

    label("loc_1F64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1F9A")

    ChrTalk(    #130
        0xFE,
        "嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "走得太累了，\x01",
            "在这里休息一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F9A")

    TalkEnd(0xFE)
    Return()

    # Function_14_1D24 end

    def Function_15_1F9E(): pass

    label("Function_15_1F9E")

    Call(0, 16)
    Return()

    # Function_15_1F9E end

    def Function_16_1FA3(): pass

    label("Function_16_1FA3")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1FFE"),
        (1, "loc_24F1"),
        (SWITCH_DEFAULT, "loc_2526"),
    )


    label("loc_1FFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_20AD")

    ChrTalk(    #132
        0x8,
        (
            "一时间这里也聚集了不少人，\x01",
            "不过在女王陛下的帮助下\x01",
            "总算恢复了平静。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x8,
        (
            "听说不久前在蔡斯\x01",
            "似乎也发生了\x01",
            "相似的事件……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x8,
        (
            "想不到导力器不能用\x01",
            "会令人如此不安……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24EE")

    label("loc_20AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_210E")

    ChrTalk(    #135
        0x8,
        "听见情报部三个字我就火大。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x8,
        (
            "在他们的『帮助』下，\x01",
            "我和公司都蒙受了巨大的损失。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24EE")

    label("loc_210E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_217C")

    ChrTalk(    #137
        0x8,
        (
            "哟，工程船和林德号\x01",
            "按计划进港了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x8,
        (
            "啊～能按计划开始\x01",
            "工作真是太好了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x8,
        "本来就应该是这样\x02",
    )

    CloseMessageWindow()
    Jump("loc_24EE")

    label("loc_217C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_21E2")

    ChrTalk(    #140
        0x8,
        (
            "我们接到了要求紧急准备\x01",
            "『埃尔赛尤』用的跑道的通知！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x8,
        (
            "得赶紧通知工作人员\x01",
            "检查跑道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24EE")

    label("loc_21E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_228E")

    ChrTalk(    #142
        0x8,
        "1、2、3……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x8,
        (
            "嗯～这样一来指定的\x01",
            "那段时间的名单就全了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x8,
        (
            "游击士协会让我们\x01",
            "提供一份乘客名单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x8,
        (
            "平时总受他们照顾，\x01",
            "这点协助调查是理所应当的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24EE")

    label("loc_228E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2315")

    ChrTalk(    #146
        0x8,
        "政变后真不得了了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x8,
        (
            "又要善后，还要兼顾\x01",
            "定期船的正常\x01",
            "运行……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x8,
        (
            "现在回忆起那时每天加班的情景\x01",
            "还是会让人掉眼泪啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24EE")

    label("loc_2315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_23A9")

    ChrTalk(    #149
        0x8,
        (
            "最近的飞船都按\x01",
            "计划在运行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x8,
        (
            "政变时因为\x01",
            "军用船的出入和情报部的\x01",
            "封锁而变得一团糟。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x8,
        (
            "我也『可喜可贺』地被\x01",
            "克雷马负责人解职了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24EE")

    label("loc_23A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_244F")

    ChrTalk(    #152
        0x8,
        (
            "说起来关于新型引擎的\x01",
            "内容应该询问作为开发方的\x01",
            "中央工房，而非飞船公社啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x8,
        (
            "说到底，我们只负责维修\x01",
            "兼临时保管。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x8,
        (
            "外国人大概是不太\x01",
            "明白这一点的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24EE")

    label("loc_244F")

    OP_A2(0x0)

    ChrTalk(    #155
        0x8,
        (
            "呼，现在的人\x01",
            "脾气都这么大啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x8,
        (
            "也难怪，因为那是\x01",
            "高速巡洋舰『埃尔赛尤』搭载的\x01",
            "新型引擎样本啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x8,
        (
            "我理解他们那股子拼命劲儿，\x01",
            "但毕竟是还没完成啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24EE")

    Jump("loc_2529")

    label("loc_24F1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2502")
    OP_A9(0xD9)
    Jump("loc_2521")

    label("loc_2502")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_250E")
    OP_A9(0xD1)
    Jump("loc_2521")

    label("loc_250E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_251F")
    OP_A9(0xD0)
    Jump("loc_2521")

    label("loc_251F")

    OP_A9(0xCF)

    label("loc_2521")

    OP_56(0x0)
    Jump("loc_2529")

    label("loc_2526")

    Jump("loc_2529")

    label("loc_2529")

    TalkEnd(0x8)
    Return()

    # Function_16_1FA3 end

    def Function_17_252D(): pass

    label("Function_17_252D")

    Call(0, 18)
    Return()

    # Function_17_252D end

    def Function_18_2532(): pass

    label("Function_18_2532")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2576")

    ChrTalk(    #158
        0x9,
        (
            "现在所有的飞船都\x01",
            "暂停飞行了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x9,
        "敬请大家谅解。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BA6")

    label("loc_2576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_25BE")

    ChrTalk(    #160
        0x9,
        "刚才林德号起飞了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x9,
        "接下来向西的赛希莉亚号要进港了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BA6")

    label("loc_25BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C6, 5)), scpexpr(EXPR_END)), "loc_2608")

    ChrTalk(    #162
        0x9,
        (
            "现在第２跑道停着\x01",
            "中央工房的船。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x9,
        (
            "请注意不要\x01",
            "搞错跑道。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA6")

    label("loc_2608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2664")

    ChrTalk(    #164
        0x9,
        "林德号即将到达。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x9,
        (
            "要搭乘的顾客，\x01",
            "在买好票之后\x01",
            "请到外面的接待处办理手续。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA6")

    label("loc_2664")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_271E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_26CB")

    ChrTalk(    #166
        0x9,
        (
            "刚才来了一个\x01",
            "银发的女游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x9,
        (
            "她询问了我们关于\x01",
            "公司收到的恐吓信的事情。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_271B")

    label("loc_26CB")


    ChrTalk(    #168
        0x9,
        (
            "刚才来了一个\x01",
            "红发的游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x9,
        (
            "他询问了我们关于\x01",
            "公司收到的恐吓信的事情。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_271B")

    Jump("loc_2BA6")

    label("loc_271E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2780")

    ChrTalk(    #170
        0x9,
        (
            "因为恐吓信的缘故，\x01",
            "公司内部确实产生了动摇。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x9,
        (
            "希望别引发造成顾客\x01",
            "困扰的事件……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA6")

    label("loc_2780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_27A9")

    ChrTalk(    #172
        0x9,
        (
            "欢迎！\x01",
            "欢迎光临飞船公社。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA6")

    label("loc_27A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 4)), scpexpr(EXPR_END)), "loc_27F9")

    ChrTalk(    #173
        0x9,
        (
            "#5P请把您的票\x01",
            "交到外面的\x01",
            "接待处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x9,
        "#5P请在那里办理登船手续。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BA6")

    label("loc_27F9")

    EventBegin(0x0)
    Fade(1000)
    OP_4A(0x9, 255)
    OP_8C(0x9, 180, 0)
    OP_6D(1800, 0, 64920, 0)
    SetChrPos(0xF7, 2190, 0, 63630, 0)
    SetChrPos(0x101, 1250, 0, 63630, 0)
    OP_0D()

    ChrTalk(    #175
        0x9,
        "#5P欢迎光临。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x9,
        (
            "#5P请问是要搭乘国内航班，\x01",
            "还是要搭乘国际航班呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#6P#1006F嗯～我们需要2张\x01",
            "前往卢安的船票。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x9,
        "#5P请稍等……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x9,
        (
            "#5P啊，小姐，\x01",
            "你们是游击士协会的人吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2A23")

    ChrTalk(    #180
        0x9,
        (
            "#5P请问是艾丝蒂尔小姐和阿加特先生\x01",
            "吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        "#6P#1004F嗯、嗯，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x9,
        (
            "#5P王都支部的艾南先生\x01",
            "已经替你们付了船票费用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x9,
        "#5P请拿好。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #184
        "\x07\x00得到了２张\x1F\xF2\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F2, 2)

    ChrTalk(    #185
        0x101,
        "#6P#1011F哦，是艾南先生啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x106,
        (
            "#051F不愧是艾南。\x01",
            "做事真是周到。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B54")

    label("loc_2A23")


    ChrTalk(    #187
        0x9,
        (
            "#5P请问是艾丝蒂尔小姐和雪拉扎德小姐\x01",
            "吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        "#6P#1004F嗯、嗯，怎么了？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x9,
        (
            "#5P王都支部的艾南先生\x01",
            "已经替你们付了船票费用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x9,
        "#5P请拿好。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #191
        "\x07\x00得到了２张\x1F\xF2\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F2, 2)

    ChrTalk(    #192
        0x101,
        "#6P#1011F嘿嘿，是艾南先生啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x103,
        (
            "#021F不愧是艾南先生。\x01",
            "真是一如既往地细心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B54")


    ChrTalk(    #194
        0x9,
        (
            "#5P那么，请把票\x01",
            "交到外面的\x01",
            "接待处。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0x9,
        "#5P请在那里办理登船手续。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1204)
    OP_4B(0x9, 255)
    EventEnd(0x0)
    Return()

    label("loc_2BA6")

    TalkEnd(0x9)
    Return()

    # Function_18_2532 end

    def Function_19_2BAA(): pass

    label("Function_19_2BAA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2C24")

    ChrTalk(    #196
        0xA,
        "啊，这下玩儿完了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xA,
        (
            "我努力促成的\x01",
            "旅游路线这样一来\x01",
            "也就泡汤了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0xA,
        (
            "现在大家哪儿还\x01",
            "顾得上旅游啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E99")

    label("loc_2C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2CAC")

    ChrTalk(    #199
        0xA,
        (
            "情报部的余党之前\x01",
            "出现了，吓了我一跳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xA,
        (
            "治安一旦混乱，旅游的营业额\x01",
            "就会一下子跌入谷底。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xA,
        "他们都被逮捕真是太好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E99")

    label("loc_2CAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_2D1D")

    ChrTalk(    #202
        0xA,
        "唔，应该怎么办呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0xA,
        (
            "安特洛丝餐厅的老板\x01",
            "是个很\x01",
            "固执的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0xA,
        (
            "应该不可能给旅游\x01",
            "路线打折……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E99")

    label("loc_2D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D9D")

    ChrTalk(    #205
        0xA,
        "唔，真难办。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0xA,
        (
            "我考虑了一下柏斯\x01",
            "旅游路线的具体内容……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xA,
        (
            "如果在其中加上安特洛丝\x01",
            "餐厅的话价格就会上升。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E99")

    label("loc_2D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_2E34")

    ChrTalk(    #208
        0xA,
        (
            "我准备和飞船公社\x01",
            "合作筹划旅游路线。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xA,
        (
            "我提议把前几天去考察的柏斯\x01",
            "作为第一条路线，公司也表示赞同。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xA,
        (
            "接下来要确定\x01",
            "路线的具体内容。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E99")

    label("loc_2E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_2E99")

    ChrTalk(    #211
        0xA,
        (
            "互不侵犯条约对旅游业应该是\x01",
            "相当相当有利的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #212
        0xA,
        (
            "真想以该条约为契机，\x01",
            "多招揽些游客来啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E99")

    TalkEnd(0xFE)
    Return()

    # Function_19_2BAA end

    def Function_20_2E9D(): pass

    label("Function_20_2E9D")

    TalkBegin(0xFE)

    ChrTalk(    #213
        0xFE,
        (
            "刚才那两个人\x01",
            "不知为什么气势汹汹的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xFE,
        (
            "看上去确实像有点\x01",
            "来头的人，到底是谁呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2E9D end

    def Function_21_2EFA(): pass

    label("Function_21_2EFA")

    TalkBegin(0xFE)

    ChrTalk(    #215
        0xFE,
        (
            "好、好可怕……\x01",
            "这样一来终于可以买票了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2EFA end

    def Function_22_2F2E(): pass

    label("Function_22_2F2E")

    TalkBegin(0xFE)

    ChrTalk(    #216
        0xFE,
        (
            "真是的，在这种场合\x01",
            "发火就不嫌丢人吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "真希望都能学学\x01",
            "什么叫礼貌。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2F2E end

    def Function_23_2F83(): pass

    label("Function_23_2F83")

    TalkBegin(0xFE)

    ChrTalk(    #218
        0xFE,
        (
            "假定\x01",
            "假定\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_2F83 end

    def Function_24_2F99(): pass

    label("Function_24_2F99")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2FF1")

    ChrTalk(    #219
        0xFE,
        (
            "#050F你们在这里就表示说\x01",
            "要从大使馆开始调查？\x02\x03",

            "#051F总之就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3075")

    label("loc_2FF1")


    ChrTalk(    #220
        0xFE,
        (
            "#052F艾丝蒂尔，怎么了？\x02\x03",

            "#050F我现在正要去\x01",
            "公社询问情况。\x02\x03",

            "你们在这里就表示说\x01",
            "要从大使馆开始调查？\x02\x03",

            "#051F总之就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_3075")

    TalkEnd(0xFE)
    Return()

    # Function_24_2F99 end

    def Function_25_3079(): pass

    label("Function_25_3079")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_30C8")

    ChrTalk(    #221
        0xFE,
        (
            "#020F你们在这里就表示说\x01",
            "要从大使馆开始调查？\x02\x03",

            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_313D")

    label("loc_30C8")


    ChrTalk(    #222
        0xFE,
        (
            "#023F咦，怎么了？\x02\x03",

            "#020F我现在正要去\x01",
            "公社询问情况。\x02\x03",

            "你们在这里就表示说\x01",
            "要从大使馆开始调查？\x02\x03",

            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_313D")

    TalkEnd(0xFE)
    Return()

    # Function_25_3079 end

    def Function_26_3141(): pass

    label("Function_26_3141")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D1, 0)), scpexpr(EXPR_END)), "loc_3174")

    ChrTalk(    #223
        0xFE,
        (
            "#560F我们还要在这里\x01",
            "买点东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3236")

    label("loc_3174")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #224
        0xFE,
        "#560F啊，姐姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0x101,
        (
            "#1000F提妲，小玲就\x01",
            "交给你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0xFE,
        (
            "#061F嗯，交给我吧。\x02\x03",

            "#560F我有很多地方\x01",
            "想和小玲一起去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0x101,
        (
            "#1000F这样啊。\x01",
            "可别迷路。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0xFE,
        (
            "#061F嗯～\x01",
            "姐姐也要努力工作哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1688)

    label("loc_3236")

    TalkEnd(0xFE)
    Return()

    # Function_26_3141 end

    def Function_27_323A(): pass

    label("Function_27_323A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D0, 7)), scpexpr(EXPR_END)), "loc_3289")

    ChrTalk(    #229
        0xFE,
        (
            "#260F买好东西以后\x01",
            "还想去些别的地方。\x02\x03",

            "我要让提妲带我到处走。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34C3")

    label("loc_3289")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #230
        0x101,
        "#1001F小玲，你在这里吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "#264F啊，姐姐……\x02\x03",

            "#265F我说，姐姐你\x01",
            "喜欢哪个布偶？。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0x101,
        (
            "#1011F让我想想，那边的兔子\x01",
            "挺可爱的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #233
        0xFE,
        (
            "#260F真的？\x02\x03",

            "#261F真巧，玲也最喜欢\x01",
            "那只兔子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0x101,
        (
            "#1015F……看到布偶就让人\x01",
            "想起亚妮拉丝。\x02\x03",

            "不知道她现在怎么样了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #235
        0xFE,
        "#264F亚妮……拉丝？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0x101,
        (
            "#1000F她和我同为游击士，\x01",
            "是个很喜欢布偶的大姐姐。\x02\x03",

            "#1001F一定会和小玲\x01",
            "很合得来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "#264F哦……\x01",
            "玲能见到那位姐姐吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0x101,
        (
            "#1000F她现在不在王都，\x01",
            "不过不久后应该能见到。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "#265F不久是多久？\x01",
            "明天？　还是后天？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x101,
        (
            "#1013F这个嘛……\x01",
            "我就不知道了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        "#267F啊？真没劲……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1687)

    label("loc_34C3")

    TalkEnd(0xFE)
    Return()

    # Function_27_323A end

    def Function_28_34C7(): pass

    label("Function_28_34C7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34DA")
    Call(0, 33)

    label("loc_34DA")

    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1A, 1210, 0, 62900, 266)
    SetChrPos(0x1B, 800, 0, 62000, 270)
    SetChrPos(0x1C, -1180, 0, 62510, 90)
    SetChrPos(0x101, 200, 0, 54480, 0)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-90, -20, 56890, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_359B")
    SetChrPos(0x106, 1160, 0, 54550, 0)
    Jump("loc_35AC")

    label("loc_359B")

    SetChrPos(0x103, 1160, 0, 54550, 0)

    label("loc_35AC")

    FadeToBright(1000, 0)

    def lambda_35BB():
        OP_8E(0x101, 0x1C2, 0x0, 0xDCB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_35BB)

    def lambda_35D6():
        OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35D6)
    Sleep(300)

    def lambda_35ED():
        OP_8E(0xF7, 0x578, 0x0, 0xDBEC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 0, lambda_35ED)

    def lambda_3608():
        OP_9F(0xF7, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_3608)
    WaitChrThread(0xF7, 0x0)
    WaitChrThread(0xF7, 0x1)
    OP_0D()

    ChrTalk(    #242
        0x101,
        "#5P#1004F咦……？\x02",
    )

    CloseMessageWindow()

    def lambda_363C():
        OP_6D(1040, 0, 63300, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_363C)

    def lambda_3654():
        OP_67(0, 6990, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3654)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)

    NpcTalk(    #243
        0x1C,
        "戴眼镜的女性",
        (
            "#6P#1112F这就叫自高自大的\x01",
            "帝国贵族……\x02\x03",

            "臭不可闻也得\x01",
            "有个度吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #244
        0x1B,
        "中年男子",
        (
            "#2P#1101F哼，臭不可闻的\x01",
            "是你才对吧。\x02\x03",

            "首先，关于提供引擎的问题，\x01",
            "共和国凭什么指手画脚的？\x02\x03",

            "这才是干涉内政吧。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #245
        0x1C,
        "戴眼镜的女性",
        (
            "#6P#1111F这关乎国家安全。\x02\x03",

            "贵国侵略利贝尔到现在\x01",
            "还不满１０年吧。\x02\x03",

            "#1113F让这种侵略性的国家得到\x01",
            "最新技术实在是太不像话了。\x02\x03",

            "即便以利贝尔友邦的立场\x01",
            "来看也不能不加以提醒。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #246
        0x1B,
        "中年男子",
        (
            "#2P#1103F什、什么友邦啊！\x02\x03",

            "10年前也没有\x01",
            "派兵援助他们！\x02\x03",

            "一区区旁观者，\x01",
            "少在旁边摆架子！\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #247
        0x1C,
        "戴眼镜的女性",
        "#6P#1114F你、你说什么……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x1B, 400)

    ChrTalk(    #248
        0x1A,
        (
            "#272F#5P达维尔大使……\x01",
            "就到此为止吧。\x02\x03",

            "会给其他旅客添麻烦的。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1B, 0, 400)

    ChrTalk(    #249
        0x1B,
        "#1101F可、可是穆拉……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1A, 266, 400)

    ChrTalk(    #250
        0x1A,
        (
            "#270F#5P爱尔莎大使也请\x01",
            "适当控制下自己的情绪吧。\x02\x03",

            "关于刚才的问题，我们另找\x01",
            "机会在双方的大使馆讨论吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0x1C,
        (
            "#6P#1113F……也对。\x02\x03",

            "虽然接受帝国军人的\x01",
            "意见并不令人愉快。\x02\x03",

            "#1111F不过比自大蛮横、根子腐败不堪的\x01",
            "帝国贵族可要好多了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x1C, 500)

    ChrTalk(    #252
        0x1B,
        "#1103F#2P你、你说什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x1C,
        (
            "#6P#1113F那么祝你们愉快。\x01",
            "各位，我先告辞了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x1C, 180, 400)

    def lambda_3A49():
        OP_8E(0x1C, 0xFFFFFCE0, 0x0, 0xD5A2, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 0, lambda_3A49)

    def lambda_3A64():
        OP_6D(670, 0, 59460, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_3A64)

    def lambda_3A7C():
        OP_67(0, 6990, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_3A7C)

    def lambda_3A94():

        label("loc_3A94")

        TurnDirection(0x1B, 0x1C, 0)
        OP_48()
        Jump("loc_3A94")

    QueueWorkItem2(0x1B, 1, lambda_3A94)

    def lambda_3AA5():

        label("loc_3AA5")

        TurnDirection(0x1A, 0x1C, 0)
        OP_48()
        Jump("loc_3AA5")

    QueueWorkItem2(0x1A, 1, lambda_3AA5)

    def lambda_3AB6():

        label("loc_3AB6")

        TurnDirection(0x101, 0x1C, 0)
        OP_48()
        Jump("loc_3AB6")

    QueueWorkItem2(0x101, 2, lambda_3AB6)

    def lambda_3AC7():

        label("loc_3AC7")

        TurnDirection(0xF7, 0x1C, 0)
        OP_48()
        Jump("loc_3AC7")

    QueueWorkItem2(0xF7, 2, lambda_3AC7)
    Sleep(3500)

    def lambda_3ADD():
        OP_9F(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3ADD)
    WaitChrThread(0x1C, 0x0)
    WaitChrThread(0x1C, 0x1)
    SetChrFlags(0x1C, 0x80)
    OP_44(0x1A, 0x1)
    OP_44(0x1B, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0xF7, 0x2)
    WaitChrThread(0x1A, 0x2)
    WaitChrThread(0x1A, 0x3)
    Sleep(1000)

    ChrTalk(    #254
        0x1B,
        (
            "#1101F#6P怎、怎么有这么没礼貌的女人！\x02\x03",

            "这就叫毫无历史和传统的\x01",
            "平民暴发户……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x1B, 400)

    ChrTalk(    #255
        0x1A,
        "#272F#6P大使……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x1B, 270, 400)
    OP_8C(0x1B, 0, 400)

    ChrTalk(    #256
        0x1B,
        (
            "#1102F#6P……哼，我明白。\x02\x03",

            "#1100F我先回大使馆了。\x01",
            "关于那件事就交给你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0x1A,
        "#270F#6P明白了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1B, 400)
    TurnDirection(0xF7, 0x1B, 400)

    def lambda_3C0C():

        label("loc_3C0C")

        TurnDirection(0x1A, 0x1B, 0)
        OP_48()
        Jump("loc_3C0C")

    QueueWorkItem2(0x1A, 1, lambda_3C0C)
    OP_43(0x1B, 0x1, 0x0, 0x1D)
    Sleep(1000)

    def lambda_3C29():
        OP_6D(1830, 0, 62950, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_3C29)

    def lambda_3C41():
        OP_67(0, 6150, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_3C41)
    OP_43(0x101, 0x1, 0x0, 0x1E)
    Sleep(500)
    OP_43(0xF7, 0x1, 0x0, 0x1F)
    WaitChrThread(0xF7, 0x1)
    OP_44(0x1A, 0x1)

    def lambda_3C75():
        TurnDirection(0x101, 0x1A, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3C75)

    def lambda_3C83():
        TurnDirection(0xF7, 0x1A, 1000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C83)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x1A, 0x2)
    WaitChrThread(0x1A, 0x3)

    ChrTalk(    #258
        0x101,
        "#1011F#6P你好。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D48")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇奥利维尔捕获事件未完成】\x01",      # 0
            "【◇奥利维尔捕获事件已完成】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D2F"),
        (1, "loc_3D37"),
        (SWITCH_DEFAULT, "loc_3D3F"),
    )


    label("loc_3D2F")

    OP_28(0x55, 0x3, 0x10)
    Jump("loc_3D3F")

    label("loc_3D37")

    OP_28(0x55, 0x4, 0x10)
    Jump("loc_3D3F")

    label("loc_3D3F")

    FadeToBright(300, 0)

    label("loc_3D48")

    OP_62(0x1A, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x55, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DC3")

    ChrTalk(    #259
        0x1A,
        (
            "#273F#5P你是……\x01",
            "我记得你叫艾丝蒂尔吧。\x02\x03",

            "#277F好久不见。\x01",
            "自从武术大会之后。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E2A")

    label("loc_3DC3")


    ChrTalk(    #260
        0x1A,
        (
            "#273F#5P你是……\x01",
            "我记得你叫艾丝蒂尔吧。\x02\x03",

            "#277F好久不见。\x01",
            "自从诞辰庆典麻烦你帮忙之后就一直没见过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E2A")


    ChrTalk(    #261
        0x101,
        (
            "#1016F#6P太好了。\x01",
            "你还记得我。\x02\x03",

            "#1011F不过话说回来……\x01",
            "刚才的争论真激烈。\x02\x03",

            "他们是什么人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0x1A,
        (
            "#277F#5P那位男子是\x01",
            "埃雷波尼亚帝国的达维尔大使。\x02\x03",

            "那位女性是\x01",
            "卡尔瓦德共和国的爱尔莎大使。\x02\x03",

            "双方都是各自国家在王都\x01",
            "大使馆的负责人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0x101,
        "#1004F#6P这、这样啊。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3FA9")

    ChrTalk(    #264
        0x106,
        (
            "#551F#4P不过两位大使级人物的\x01",
            "争论倒像是小孩子在吵架。\x02\x03",

            "这就是大使的工作作风？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0x101,
        "#1019F#6P等、等等，阿加特。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4005")

    label("loc_3FA9")


    ChrTalk(    #266
        0x103,
        (
            "#027F#4P哼，那就是大使啊。\x02\x03",

            "都用那种粗野的方式\x01",
            "来进行外交？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0x101,
        "#1019F#6P雪、雪拉姐。\x02",
    )

    CloseMessageWindow()

    label("loc_4005")


    ChrTalk(    #268
        0x1A,
        (
            "#276F#5P唉，真不好意思。\x02\x03",

            "#272F本来帝国和共和国\x01",
            "的关系就不甚友好。\x02\x03",

            "而且那两个人在性格上\x01",
            "也完全合不上拍。\x02\x03",

            "#277F不过每次见面\x01",
            "都要吵架，说不定也反证了\x01",
            "他们其实很合得来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x101,
        (
            "#1016F#6P哈哈，可能也有点道理。\x02\x03",

            "#1015F不过……\x01",
            "他们说的话挺令人在意的。\x02\x03",

            "提供引擎和内政干涉什么的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x1A,
        "#270F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        "#1025F#6P啊，我是不是不该问的？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0x1A,
        (
            "#272F#5P……不，没关系。\x02\x03",

            "#277F引擎指的是中央工房现在\x01",
            "正在开发的最新型号。\x02\x03",

            "利贝尔有意在完成后\x01",
            "将样品提供给\x01",
            "帝国和共和国双方……\x02\x03",

            "我们来协商这件事，\x01",
            "就正好巧遇爱尔莎大使。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #273
        0x101,
        (
            "#1000F#6P哦，原来如此。\x02\x03",

            "#1015F不过为了一个新型引擎\x01",
            "有什么好吵的？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_42D3")

    ChrTalk(    #274
        0x106,
        (
            "#555F#4P那可是左右飞船性能的\x01",
            "最重要的零件。\x02\x03",

            "想想军舰搭载它之后会变得怎样，\x01",
            "就知道这不是什么小事啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_434A")

    label("loc_42D3")


    ChrTalk(    #275
        0x103,
        (
            "#026F#4P导力引擎的性能\x01",
            "可以直接左右飞船的性能。\x02\x03",

            "#020F想想军舰搭载它之后会变得怎样，\x01",
            "就知道这里面牵扯得有多深了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_434A")


    ChrTalk(    #276
        0x101,
        (
            "#1002F#6P原来如此……\x02\x03",

            "#1007F确实，如果帝国军因此\x01",
            "提升了战力，\x01",
            "可就不好办了。\x02\x03",

            "#1008F……啊，不好意思。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0x1A,
        (
            "#272F#5P不，你说得没错。\x02\x03",

            "#277F通常来说，向别国提供最新技术\x01",
            "是无法想象的，\x01",
            "不过这也是女王陛下的想法。\x02\x03",

            "并不独占技术的高峰，\x01",
            "而是通过向各国提供技术\x01",
            "来确保各国间的和平……\x02\x03",

            "这是她老人家的想法。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0x101,
        (
            "#1011F#6P原来如此……\x01",
            "这听起来确实像是陛下说的话。\x02\x03",

            "#1001F唔～从这一点上来看\x01",
            "女王陛下果然了不起。\x02\x03",

            "感觉这已经不是一种单纯的理想，\x01",
            "而是有深谋远虑的\x01",
            "外交政策了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0x1A,
        (
            "#272F#5P嗯，利贝尔的国民应该\x01",
            "好好地以陛下为荣。\x02\x03",

            "#277F……抱歉。\x01",
            "有点谈得忘乎所以了。\x02\x03",

            "你们要买票吧？\x01",
            "我就先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #280
        0x101,
        (
            "#1004F#6P啊，嗯。\x02\x03",

            "#1015F对了，穆拉先生，\x01",
            "奥利维尔……\x02\x03",

            "他已经回\x01",
            "埃雷波尼亚了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0x1A,
        "#273F#5P怎么？你不知道？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0x101,
        (
            "#1007F#6P自从诞辰庆典之后\x01",
            "一直没机会跟他打招呼。\x02\x03",

            "让我觉得有点抱歉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0x1A,
        (
            "#277F#5P不用担心，\x01",
            "那个轻佻的大赖皮蛋还留在利贝尔的境内。\x02\x03",

            "说什么要『优雅地\x01",
            "逗留在亚尔摩温泉』。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_470E")

    ChrTalk(    #284
        0x101,
        (
            "#1008F#6P噢，是这样啊。\x02\x03",

            "#1012F呵呵……\x01",
            "真像是奥利维尔的风格。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4756")

    label("loc_470E")


    ChrTalk(    #285
        0x101,
        "#1008F#6P哦，是这样啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0x103,
        (
            "#027F#4P呵呵……\x01",
            "像是奥利维尔的风格。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4756")


    ChrTalk(    #287
        0x1A,
        (
            "#277F#5P等那家伙回了大使馆，\x01",
            "我就把你们的事告诉他。\x02\x03",

            "至少让他在回国前\x01",
            "联络一下协会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x101,
        "#1017F#6P谢谢你，穆拉先生。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_47F1")

    ChrTalk(    #289
        0x103,
        "#021F#4P拜托了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_47F1")

    label("loc_47F1")


    ChrTalk(    #290
        0x1A,
        (
            "#277F#5P我才要谢谢你们愿意\x01",
            "陪着那个怪人呢。\x02\x03",

            "那么就此别过。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4838():
        OP_6D(670, 0, 59460, 2500)
        ExitThread()

    QueueWorkItem(0xF7, 2, lambda_4838)

    def lambda_4850():
        OP_67(0, 6990, -10000, 2500)
        ExitThread()

    QueueWorkItem(0xF7, 3, lambda_4850)

    def lambda_4868():
        OP_8E(0x1A, 0xFFFFFC54, 0x0, 0xEF74, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_4868)

    def lambda_4883():

        label("loc_4883")

        TurnDirection(0x101, 0x1A, 0)
        OP_48()
        Jump("loc_4883")

    QueueWorkItem2(0x101, 1, lambda_4883)

    def lambda_4894():

        label("loc_4894")

        TurnDirection(0xF7, 0x1A, 0)
        OP_48()
        Jump("loc_4894")

    QueueWorkItem2(0xF7, 1, lambda_4894)
    WaitChrThread(0x1A, 0x1)

    def lambda_48AA():
        OP_8E(0x1A, 0xFFFFFCB8, 0x0, 0xD4E4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_48AA)
    Sleep(1900)

    def lambda_48CA():
        OP_9F(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_48CA)
    Sleep(400)
    WaitChrThread(0x1A, 0x1)
    SetChrFlags(0x1A, 0x80)
    OP_44(0x101, 0x1)
    OP_44(0xF7, 0x1)
    WaitChrThread(0xF7, 0x2)
    WaitChrThread(0xF7, 0x3)

    def lambda_48FD():
        OP_6D(1360, 0, 61620, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_48FD)

    def lambda_4915():
        OP_67(0, 6990, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4915)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4BA6")
    OP_8C(0x106, 280, 500)

    ChrTalk(    #291
        0x106,
        (
            "#555F#2P想不到这么一个严肃的军人\x01",
            "会是那个金发男人的朋友。\x02\x03",

            "他是什么角色？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x101,
        (
            "#1006F#5P他是穆拉先生，\x01",
            "帝国大使馆的常驻士官。\x02\x03",

            "不过我们也\x01",
            "只见过一两次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x106,
        (
            "#552F#2P哦……\x01",
            "言行得体又无懈可击。\x02\x03",

            "可以说是头藏起了\x01",
            "獠牙的军用犬。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0x101,
        (
            "#1007F#5P真是的，你真没礼貌。\x02\x03",

            "#1015F不过确实……\x01",
            "给人的感觉是他很强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0x106,
        (
            "#057F#2P哼，帝国的人都不可信赖，\x01",
            "那个金发男人也一样。\x02\x03",

            "好像和卡西乌斯大叔\x01",
            "私下说过什么话……\x02\x03",

            "也不知道他长居此地\x01",
            "有什么目的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x101,
        (
            "#1015F#5P嗯～好像也有点道理。\x02\x03",

            "#1011F奥利维尔虽然有点怪，\x01",
            "但不是个坏人……\x02\x03",

            "穆拉先生看上去也\x01",
            "不像是坏人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0x106,
        (
            "#053F#2P哼，天知道。\x02\x03",

            "#050F算了，我们赶紧去\x01",
            "柜台买票吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E8E")

    label("loc_4BA6")

    OP_8C(0x103, 280, 500)

    ChrTalk(    #298
        0x103,
        (
            "#021F#2P呵呵，想不到这么一个严肃的军人\x01",
            "会是那个奥利维尔的朋友。\x02\x03",

            "#020F看上去是个帝国军人，\x01",
            "他是什么角色？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0x101,
        (
            "#1006F#5P他是穆拉先生，\x01",
            "帝国大使馆的常驻士官。\x02\x03",

            "不过我们也\x01",
            "只见过一两次。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x103,
        (
            "#027F#2P哦～这么年轻就\x01",
            "一脸沧桑了。\x02\x03",

            "#021F真想有机会和他喝一杯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x101,
        (
            "#1007F#5P真是的，你那副表情好像\x01",
            "在说我会丢利贝尔的脸一样。\x02\x03",

            "#1011F对了，雪拉姐\x01",
            "后来有没有见过奥利维尔？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0x103,
        (
            "#020F#2P嗯，在王都见了几次。\x02\x03",

            "其实他还约我去温泉呢，\x01",
            "被我严肃地拒绝了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #303
        0x101,
        (
            "#1004F#5P哎哎！？\x02\x03",

            "#1013F就是说……\x01",
            "是……是那种意思？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0x103,
        (
            "#027F#2P呵呵，天知道。\x02\x03",

            "#021F不过我最近一个月也很忙，\x01",
            "根本没那个空闲。\x02\x03",

            "要在平时的话，我就会让他负责\x01",
            "全部住宿费然后拉他陪我喝酒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0x101,
        (
            "#1016F#5P哈…哈…\x01",
            "从某种意义上说，奥利维尔也真不幸。\x02\x03",

            "#1006F不说这些了。\x01",
            "我们先去\x01",
            "买票吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E8E")

    OP_A2(0x1203)
    EventEnd(0x0)
    Return()

    # Function_28_34C7 end

    def Function_29_4E94(): pass

    label("Function_29_4E94")

    OP_8E(0xFE, 0xFFFFFD12, 0x0, 0xEB3C, 0x7D0, 0x0)

    def lambda_4EAE():
        OP_8E(0xFE, 0xFFFFFD62, 0x0, 0xD57A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 3, lambda_4EAE)
    Sleep(2500)

    def lambda_4ECE():
        OP_9F(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_4ECE)
    Sleep(400)
    WaitChrThread(0x1B, 0x3)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_29_4E94 end

    def Function_30_4EEA(): pass

    label("Function_30_4EEA")

    OP_8E(0x101, 0x23A, 0x0, 0xEF06, 0x7D0, 0x0)
    Return()

    # Function_30_4EEA end

    def Function_31_4EFF(): pass

    label("Function_31_4EFF")

    OP_8E(0xF7, 0x5DC, 0x0, 0xED30, 0x7D0, 0x0)
    Return()

    # Function_31_4EFF end

    def Function_32_4F14(): pass

    label("Function_32_4F14")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F2B")
    Call(0, 33)
    Call(0, 34)

    label("loc_4F2B")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_4F43"),
        (101, "loc_4FC7"),
        (102, "loc_504B"),
        (103, "loc_50CF"),
        (SWITCH_DEFAULT, "loc_5153"),
    )


    label("loc_4F43")

    SetChrPos(0x101, -9240, 0, 440, 90)
    SetChrPos(0x107, -9330, 0, -480, 90)
    SetChrPos(0xF7, -10150, 0, -550, 90)
    SetChrPos(0xF9, -10150, 0, 520, 90)
    OP_6D(-9640, 0, 0, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_5153")

    label("loc_4FC7")

    SetChrPos(0x101, 440, 0, 6410, 180)
    SetChrPos(0x107, -480, 0, 6500, 180)
    SetChrPos(0xF7, 550, 0, 7320, 180)
    SetChrPos(0xF9, -520, 0, 7320, 180)
    OP_6D(0, 0, 6810, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_5153")

    label("loc_504B")

    SetChrPos(0x101, 8570, 0, -480, 270)
    SetChrPos(0x107, 8660, 0, 440, 270)
    SetChrPos(0xF7, 9480, 0, 550, 270)
    SetChrPos(0xF9, 9480, 0, -520, 270)
    OP_6D(8970, 0, 0, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_5153")

    label("loc_50CF")

    SetChrPos(0x101, -480, 0, -7240, 0)
    SetChrPos(0x107, 440, 0, -7330, 0)
    SetChrPos(0xF7, -520, 0, -8150, 0)
    SetChrPos(0xF9, 550, 0, -8150, 0)
    OP_6D(0, 0, -7640, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Jump("loc_5153")

    label("loc_5153")

    SetChrFlags(0x12, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #306
        0x101,
        "#1004F啊……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1D, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_51AD"),
        (101, "loc_523A"),
        (102, "loc_52BC"),
        (103, "loc_536A"),
        (SWITCH_DEFAULT, "loc_53F7"),
    )


    label("loc_51AD")

    SetChrPos(0x1D, 4530, 0, -10, 90)

    def lambda_51C4():
        OP_6D(9530, 0, 0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51C4)
    OP_8E(0x1D, 0x253A, 0x0, 0xFFFFFFF6, 0x7D0, 0x0)
    OP_72(0x1, 0x10)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    Sleep(1000)
    OP_8E(0x1D, 0x30CA, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(500)
    SetChrFlags(0x1D, 0x80)
    Fade(500)
    OP_6D(-9640, 0, 0, 0)
    OP_0D()
    Jump("loc_53F7")

    label("loc_523A")

    SetChrPos(0x1D, 0, 0, -3700, 180)

    def lambda_5251():
        OP_6D(0, 0, -8200, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5251)
    OP_8E(0x1D, 0x0, 0x0, 0xFFFFDAE4, 0x7D0, 0x0)

    def lambda_527D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_527D)
    OP_8E(0x1D, 0x0, 0x0, 0xFFFFD6FC, 0x7D0, 0x0)
    SetChrFlags(0x1D, 0x80)
    Fade(1000)
    OP_6D(0, 0, 6810, 0)
    OP_0D()
    Jump("loc_53F7")

    label("loc_52BC")

    SetChrPos(0x1D, -5200, 0, 0, 90)

    def lambda_52D3():
        OP_6D(-10200, 0, 0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_52D3)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_8E(0x1D, 0xFFFFD31E, 0x0, 0x0, 0x7D0, 0x0)

    def lambda_532B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_532B)
    OP_8E(0x1D, 0xFFFFCF36, 0x0, 0x0, 0x7D0, 0x0)
    SetChrFlags(0x1D, 0x80)
    Fade(1000)
    OP_6D(8970, 0, 0, 0)
    OP_0D()
    Jump("loc_53F7")

    label("loc_536A")

    SetChrPos(0x1D, 0, 0, 2870, 0)

    def lambda_5381():
        OP_6D(0, 0, 7370, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5381)
    OP_8E(0x1D, 0x0, 0x0, 0x1CCA, 0x7D0, 0x0)
    Sleep(500)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    Sleep(1000)
    OP_8E(0x1D, 0x0, 0x0, 0x28FA, 0x7D0, 0x0)
    SetChrFlags(0x1D, 0x80)
    Fade(1000)
    OP_6D(0, 0, -7640, 0)
    OP_0D()
    Jump("loc_53F7")

    label("loc_53F7")

    Sleep(200)

    ChrTalk(    #307
        0x101,
        "#1006F哟，在那儿！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #308
        0x107,
        "#065F得、得赶紧追。\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5445"),
        (101, "loc_54F6"),
        (102, "loc_55A7"),
        (103, "loc_5658"),
        (SWITCH_DEFAULT, "loc_5709"),
    )


    label("loc_5445")


    def lambda_544B():
        OP_6D(-150, 0, -180, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_544B)

    def lambda_5463():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5463)

    def lambda_547E():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_547E)
    Sleep(100)

    def lambda_549E():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_549E)

    def lambda_54B9():
        OP_90(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_54B9)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_44(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4101   ._SN", 106, 0, 0)
    IdleLoop()
    Jump("loc_5709")

    label("loc_54F6")


    def lambda_54FC():
        OP_6D(-150, 0, -180, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_54FC)

    def lambda_5514():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5514)

    def lambda_552F():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_552F)
    Sleep(100)

    def lambda_554F():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_554F)

    def lambda_556A():
        OP_90(0xFE, 0x0, 0x0, 0xFFFFD8F0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_556A)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_44(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4101   ._SN", 107, 0, 0)
    IdleLoop()
    Jump("loc_5709")

    label("loc_55A7")


    def lambda_55AD():
        OP_6D(-150, 0, -180, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_55AD)

    def lambda_55C5():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55C5)

    def lambda_55E0():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_55E0)
    Sleep(100)

    def lambda_5600():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_5600)

    def lambda_561B():
        OP_90(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_561B)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_44(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4101   ._SN", 108, 0, 0)
    IdleLoop()
    Jump("loc_5709")

    label("loc_5658")


    def lambda_565E():
        OP_6D(-150, 0, -180, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_565E)

    def lambda_5676():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5676)

    def lambda_5691():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5691)
    Sleep(100)

    def lambda_56B1():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_56B1)

    def lambda_56CC():
        OP_90(0xFE, 0x0, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_56CC)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_44(0x101, 0x0)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T4101   ._SN", 105, 0, 0)
    IdleLoop()
    Jump("loc_5709")

    label("loc_5709")

    Return()

    # Function_32_4F14 end

    def Function_33_570A(): pass

    label("Function_33_570A")

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
        (0, "loc_5787"),
        (1, "loc_578D"),
        (SWITCH_DEFAULT, "loc_5793"),
    )


    label("loc_5787")

    OP_A2(0x1200)
    Jump("loc_5793")

    label("loc_578D")

    OP_A2(0x1201)
    Jump("loc_5793")

    label("loc_5793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_57A1")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_57A5")

    label("loc_57A1")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_57A5")

    Return()

    # Function_33_570A end

    def Function_34_57A6(): pass

    label("Function_34_57A6")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_57E5")
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)
    Jump("loc_57FF")

    label("loc_57E5")

    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x5, 0x6, 0xFF, 0x4, 0x7, 0xFFFF)

    label("loc_57FF")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_34_57A6 end

    SaveToFile()

Try(main)
