from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0121   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0121.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T0121   ._SN',
            'ED6_DT21/T0121_1 ._SN',
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
        '爱娜',                                 # 9
        '雪拉扎德',                             # 10
        '阿加特',                               # 11
        '奥利维尔',                             # 12
        '科洛丝',                               # 13
        '提妲',                                 # 14
        '金',                                   # 15
        '克劳斯市长',                           # 16
        '里农',                                 # 17
        '利吉',                                 # 18
        '布露姆老奶奶',                         # 19
        '基蒂',                                 # 20
        '菲特 ',                                # 21
        '加通老大',                             # 22
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
        'ED6_DT07/CH02560 ._CH',             # 00
        'ED6_DT07/CH00020 ._CH',             # 01
        'ED6_DT07/CH00050 ._CH',             # 02
        'ED6_DT07/CH00030 ._CH',             # 03
        'ED6_DT07/CH00040 ._CH',             # 04
        'ED6_DT07/CH00060 ._CH',             # 05
        'ED6_DT07/CH00070 ._CH',             # 06
        'ED6_DT07/CH00023 ._CH',             # 07
        'ED6_DT07/CH00053 ._CH',             # 08
        'ED6_DT07/CH00033 ._CH',             # 09
        'ED6_DT07/CH00073 ._CH',             # 0A
        'ED6_DT07/CH02350 ._CH',             # 0B
        'ED6_DT07/CH01040 ._CH',             # 0C
        'ED6_DT07/CH01760 ._CH',             # 0D
        'ED6_DT07/CH01010 ._CH',             # 0E
        'ED6_DT26/CH20241 ._CH',             # 0F
        'ED6_DT07/CH01770 ._CH',             # 10
        'ED6_DT26/CH20311 ._CH',             # 11
        'ED6_DT06/CH20049 ._CH',             # 12
        'ED6_DT07/CH01020 ._CH',             # 13
        'ED6_DT07/CH01530 ._CH',             # 14
    )

    AddCharChipPat(
        'ED6_DT07/CH02560P._CP',             # 00
        'ED6_DT07/CH00020P._CP',             # 01
        'ED6_DT07/CH00050P._CP',             # 02
        'ED6_DT07/CH00030P._CP',             # 03
        'ED6_DT07/CH00040P._CP',             # 04
        'ED6_DT07/CH00060P._CP',             # 05
        'ED6_DT07/CH00070P._CP',             # 06
        'ED6_DT07/CH00023P._CP',             # 07
        'ED6_DT07/CH00053P._CP',             # 08
        'ED6_DT07/CH00033P._CP',             # 09
        'ED6_DT07/CH00073P._CP',             # 0A
        'ED6_DT07/CH02350P._CP',             # 0B
        'ED6_DT07/CH01040P._CP',             # 0C
        'ED6_DT07/CH01760P._CP',             # 0D
        'ED6_DT07/CH01010P._CP',             # 0E
        'ED6_DT26/CH20241P._CP',             # 0F
        'ED6_DT07/CH01770P._CP',             # 10
        'ED6_DT26/CH20311P._CP',             # 11
        'ED6_DT06/CH20049P._CP',             # 12
        'ED6_DT07/CH01020P._CP',             # 13
        'ED6_DT07/CH01530P._CP',             # 14
    )

    DeclNpc(
        X                   = 750,
        Z                   = 0,
        Y                   = 118600,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 17,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 16,
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
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3800,
        Z                   = 0,
        Y                   = 2000,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -355,
        Z                   = 0,
        Y                   = 71450,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 47500,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 46300,
        Z                   = 0,
        Y                   = -1110,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 2110,
        Z                   = 0,
        Y                   = -1700,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 2380,
        Y                   = 0,
        Z                   = 109620,
        Range               = 5580,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x1B0E4,
        Unknown_18          = 0x10000,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = 1271,
        TriggerZ            = 0,
        TriggerY            = 116402,
        TriggerRange        = 800,
        ActorX              = 750,
        ActorZ              = 1500,
        ActorY              = 118600,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3810,
        TriggerZ            = 0,
        TriggerY            = 1080,
        TriggerRange        = 800,
        ActorX              = 3800,
        ActorZ              = 1500,
        ActorY              = 2000,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4900,
        TriggerZ            = 0,
        TriggerY            = 112600,
        TriggerRange        = 1400,
        ActorX              = 4900,
        ActorZ              = 2000,
        ActorY              = 112600,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_39E",          # 00, 0
        "Function_1_77C",          # 01, 1
        "Function_2_7C3",          # 02, 2
        "Function_3_940",          # 03, 3
        "Function_4_9C1",          # 04, 4
        "Function_5_9C6",          # 05, 5
        "Function_6_9CB",          # 06, 6
        "Function_7_1AE1",         # 07, 7
        "Function_8_34E1",         # 08, 8
        "Function_9_39C4",         # 09, 9
        "Function_10_40A7",        # 0A, 10
        "Function_11_455E",        # 0B, 11
        "Function_12_47E5",        # 0C, 12
        "Function_13_49D7",        # 0D, 13
        "Function_14_4D00",        # 0E, 14
        "Function_15_4DE5",        # 0F, 15
        "Function_16_5025",        # 10, 16
        "Function_17_51FB",        # 11, 17
        "Function_18_53CE",        # 12, 18
        "Function_19_54F7",        # 13, 19
        "Function_20_5731",        # 14, 20
        "Function_21_6AA1",        # 15, 21
        "Function_22_79CB",        # 16, 22
        "Function_23_7A36",        # 17, 23
        "Function_24_823A",        # 18, 24
        "Function_25_9DBC",        # 19, 25
        "Function_26_9DD8",        # 1A, 26
        "Function_27_9E08",        # 1B, 27
        "Function_28_9E24",        # 1C, 28
        "Function_29_9E59",        # 1D, 29
        "Function_30_9EA0",        # 1E, 30
        "Function_31_9F08",        # 1F, 31
        "Function_32_9F70",        # 20, 32
        "Function_33_9FD8",        # 21, 33
        "Function_34_B1A2",        # 22, 34
        "Function_35_B1BE",        # 23, 35
        "Function_36_B1F3",        # 24, 36
        "Function_37_B219",        # 25, 37
        "Function_38_B26E",        # 26, 38
        "Function_39_B2B0",        # 27, 39
        "Function_40_C72C",        # 28, 40
        "Function_41_C85E",        # 29, 41
        "Function_42_C8AF",        # 2A, 42
        "Function_43_C939",        # 2B, 43
    )


    def Function_0_39E(): pass

    label("Function_0_39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3F6")
    SetChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CD")
    SetChrPos(0x13, 6360, 0, -930, 90)
    OP_43(0x13, 0x0, 0x0, 0x3)
    Jump("loc_3F3")

    label("loc_3CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E2")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_3F3")

    label("loc_3E2")

    SetChrPos(0x13, 44360, 0, -2420, 270)

    label("loc_3F3")

    Jump("loc_4D4")

    label("loc_3F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_441")
    SetChrPos(0x11, 4300, 0, 114900, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_426")
    SetChrPos(0x12, 44800, 0, 2410, 180)

    label("loc_426")

    SetChrPos(0x13, 6360, 0, -930, 90)
    OP_43(0x13, 0x0, 0x0, 0x3)
    Jump("loc_4D4")

    label("loc_441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_474")
    SetChrPos(0x11, -1050, 0, 67400, 180)
    SetChrPos(0x13, 6360, 0, -930, 90)
    OP_43(0x13, 0x0, 0x0, 0x3)
    Jump("loc_4D4")

    label("loc_474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_49B")
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x13, 6360, 0, -930, 90)
    OP_43(0x13, 0x0, 0x0, 0x3)
    Jump("loc_4D4")

    label("loc_49B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_4AF")
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_4D4")

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_4CF")
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x12, 47500, 0, -1110, 270)
    Jump("loc_4D4")

    label("loc_4CF")

    SetChrFlags(0x13, 0x80)

    label("loc_4D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5E8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52C")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)

    label("loc_52C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_575")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_55F")
    SetChrFlags(0xB, 0x2)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 18)
    Jump("loc_564")

    label("loc_55F")

    SetChrChipByIndex(0xB, 9)

    label("loc_564")

    SetChrPos(0xB, 1060, 200, 69820, 360)

    label("loc_575")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_598")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1940, 0, 74490, 360)

    label("loc_598")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5BB")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)

    label("loc_5BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E8")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)

    label("loc_5E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_62A")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 7)
    SetChrPos(0x9, 1060, 200, 69820, 360)

    label("loc_62A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_657")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)

    label("loc_657")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_67A")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)

    label("loc_67A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6A7")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)

    label("loc_6A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_6C6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_A3(0x10F0)
    Event(0, 20)
    Jump("loc_77B")

    label("loc_6C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_6DC")
    SetMapFlags(0x10000000)
    OP_A3(0x10F1)
    Event(0, 21)
    Jump("loc_77B")

    label("loc_6DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_6F2")
    SetMapFlags(0x10000000)
    OP_A3(0x10F2)
    Event(0, 39)
    Jump("loc_77B")

    label("loc_6F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_708")
    SetMapFlags(0x10000000)
    OP_A3(0x10F3)
    Event(1, 3)
    Jump("loc_77B")

    label("loc_708")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_71E")
    SetMapFlags(0x10000000)
    OP_A3(0x10F4)
    Event(1, 15)
    Jump("loc_77B")

    label("loc_71E")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (103, "loc_72A"),
        (SWITCH_DEFAULT, "loc_77B"),
    )


    label("loc_72A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_742")
    SetMapFlags(0x10000000)
    Event(1, 4)
    Jump("loc_778")

    label("loc_742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_75A")
    SetMapFlags(0x10000000)
    Event(0, 24)
    Jump("loc_778")

    label("loc_75A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_778")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_778")

    Jump("loc_77B")

    label("loc_77B")

    Return()

    # Function_0_39E end

    def Function_1_77C(): pass

    label("Function_1_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A0")
    OP_B1("t0121_y")
    Jump("loc_7A9")

    label("loc_7A0")

    OP_B1("t0121_n")

    label("loc_7A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x308, 3)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7C2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7C2")

    Return()

    # Function_1_77C end

    def Function_2_7C3(): pass

    label("Function_2_7C3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7E8")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_92A")

    label("loc_7E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_801")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_92A")

    label("loc_801")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81A")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_92A")

    label("loc_81A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_833")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_92A")

    label("loc_833")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84C")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_92A")

    label("loc_84C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_865")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_92A")

    label("loc_865")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87E")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_92A")

    label("loc_87E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_897")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_92A")

    label("loc_897")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B0")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_92A")

    label("loc_8B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8C9")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_92A")

    label("loc_8C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E2")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_92A")

    label("loc_8E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8FB")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_92A")

    label("loc_8FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_914")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_92A")

    label("loc_914")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92A")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_92A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_93F")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_92A")

    label("loc_93F")

    Return()

    # Function_2_7C3 end

    def Function_3_940(): pass

    label("Function_3_940")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C0")
    OP_8E(0xFE, 0x18D8, 0x0, 0xFFFFFC5E, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x18D8, 0x0, 0xFFFFF6A0, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(3000)
    OP_8E(0xFE, 0x1630, 0x0, 0xFFFFF178, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1716, 0x0, 0xFFFFED54, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Sleep(3000)
    Jump("Function_3_940")

    label("loc_9C0")

    Return()

    # Function_3_940 end

    def Function_4_9C1(): pass

    label("Function_4_9C1")

    Call(0, 6)
    Return()

    # Function_4_9C1 end

    def Function_5_9C6(): pass

    label("Function_5_9C6")

    Call(0, 7)
    Return()

    # Function_5_9C6 end

    def Function_6_9CB(): pass

    label("Function_6_9CB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A3E")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",          # 0
            "报告\x01",          # 1
            "呼叫同伴\x01",      # 2
            "离开\x01",          # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jump("loc_A42")

    label("loc_A3E")

    Call(6, 5)

    label("loc_A42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6B")
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC0, 0x0, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ABC")
    OP_28(0xC3, 0x4, 0x20)
    OP_A9(0x3)

    ChrTalk(    #0
        0x8,
        (
            "#740F辛苦了。\x01",
            "看来顺利达成目的了呢。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B62")

    label("loc_ABC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_A9(0x3)"), scpexpr(EXPR_END)), "loc_B11")

    ChrTalk(    #1
        0x8,
        (
            "#740F辛苦了。\x01",
            "看来顺利达成目的了呢。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B62")

    label("loc_B11")


    ChrTalk(    #2
        0x8,
        (
            "#740F哎呀，现在\x01",
            "好像没有可以报告的工作吧。\x02\x03",

            "完成了什么任务的话\x01",
            "再来报告吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B62")

    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_B6B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C16")

    ChrTalk(    #3
        0x8,
        (
            "#740F要叫同伴来吗？\x02\x03",

            "明白了。\x01",
            "我马上去联络。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05联络各支部，\x01",
            "集合了待命人员。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_CE(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_C16")

    TalkEnd(0x8)
    Return()

    label("loc_C1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C2E")
    TalkEnd(0x8)
    Return()

    label("loc_C2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_D1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_C88")

    ChrTalk(    #5
        0x8,
        (
            "#740F利吉和你们，\x01",
            "今天都辛苦了。\x02\x03",

            "以后也请保持这个状态，\x01",
            "继续努力。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D17")

    label("loc_C88")


    ChrTalk(    #6
        0x8,
        (
            "#740F导力停止现象\x01",
            "似乎影响到了\x01",
            "意想不到的地方。\x02\x03",

            "玛鲁加矿山的事件就是一个例子，\x01",
            "今后也必须多加注意。\x02\x03",

            "你们也不要疏忽大意\x01",
            "继续保持警戒哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D17")

    Jump("loc_1ADD")

    label("loc_D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_EAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 4)), scpexpr(EXPR_END)), "loc_D82")

    ChrTalk(    #7
        0x8,
        (
            "#740F刚刚才联络，\x01",
            "哪能马上好呢。\x02\x03",

            "如果要去王都，\x01",
            "那时也顺便去一下支部吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E37")

    label("loc_D82")


    ChrTalk(    #8
        0x8,
        (
            "#740F总之公告板的工作\x01",
            "和附近的巡视就拜托了。\x02\x03",

            "其中玛鲁加矿山尤其令人在意。\x01",
            "正好工程也预定开始了，\x01",
            "利吉已经去警备了。\x02\x03",

            "考虑到可能发生万不得已的事态，\x01",
            "你们能去看看情况就更好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E37")

    OP_A2(0x1)
    Jump("loc_EAA")

    label("loc_E3D")


    ChrTalk(    #9
        0x8,
        (
            "#740F总之公告板的工作\x01",
            "和附近的巡视就拜托了。\x02\x03",

            "特别是工程预定开始的矿山，\x01",
            "就是希望去看看情况的地方之一。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EAA")

    Jump("loc_1ADD")

    label("loc_EAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_120F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_10AD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1032")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE0")
    TurnDirection(0x8, 0x104, 0)

    ChrTalk(    #10
        0x8,
        (
            "#740F哎呀，是奥利维尔啊。\x01",
            "已经好了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x104,
        (
            "#035F呼，当然。\x02\x03",

            "这种程度的酒\x01",
            "可醉不倒我哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#740F是吗，那就放心了。\x02\x03",

            "#741F那么，下次再邀请我哦。\x01",
            "到时候可要大灌你一场。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x104,
        (
            "#037F哈，哈哈……\x01",
            "我期待着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1016F（唔，嗯……\x01",
            "　皮笑肉不笑啊。)\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x76, 0x1, 0x400)
    Jump("loc_102F")

    label("loc_FE0")


    ChrTalk(    #15
        0x8,
        (
            "#740F不管怎样，\x01",
            "好久没喝得像今天这么痛快了。\x02\x03",

            "那么，\x01",
            "以后也要多加注意哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_102F")

    Jump("loc_10AA")

    label("loc_1032")


    ChrTalk(    #16
        0x8,
        (
            "#740F奥利维尔的话\x01",
            "已经在２楼待命了。\x02\x03",

            "看起来稍微有点累，\x01",
            "不过身体似乎没有大碍，\x01",
            "就带他去吧。\x02\x03",

            "那么，今后也请当心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10AA")

    Jump("loc_120C")

    label("loc_10AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_111E")

    ChrTalk(    #17
        0x8,
        (
            "#740F去柏斯的票\x01",
            "已经安排好了。\x02\x03",

            "和飞船坪的阿兰说一下\x01",
            "就可以马上办理手续了。\x02\x03",

            "那么，今后也请当心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_120C")

    label("loc_111E")


    ChrTalk(    #18
        0x8,
        (
            "#740F关于定期船的票\x01",
            "已经安排好了。\x02\x03",

            "和飞船坪的阿兰说一下\x01",
            "应该马上就可以办手续了。\x02\x03",

            "#744F这下没有被实验的地区\x01",
            "就只剩下柏斯了。\x02\x03",

            "说不定会成为\x01",
            "前所未有的严峻旅途……\x02\x03",

            "#740F不过是你们的话，\x01",
            "一定能渡过难关的。\x02\x03",

            "请加油吧。\x01",
            "祝你们好运。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_120C")

    Jump("loc_1ADD")

    label("loc_120F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_1371")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1285")

    ChrTalk(    #19
        0x8,
        (
            "#740F既然是自投罗网，\x01",
            "我就不说什么要当心之类的俗套话了。\x02\x03",

            "请尽量发挥游击士的实力，\x01",
            "惩治犯人吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_136E")

    label("loc_1285")


    ChrTalk(    #20
        0x8,
        (
            "#740F我作为协会的接待员\x01",
            "也支持你们的决定。\x02\x03",

            "虽说去神秘森林\x01",
            "等于就是往陷阱里跳，\x01",
            "但现在的形势下也没有别的办法了。\x02\x03",

            "既然是自投罗网，\x01",
            "我就不说什么要当心之类的俗套话了。\x02\x03",

            "请尽量发挥游击士的实力，\x01",
            "惩治犯人吧。\x02\x03",

            "……我就说这些了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_136E")

    Jump("loc_1ADD")

    label("loc_1371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_14C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_13F9")

    ChrTalk(    #21
        0x8,
        (
            "#740F去农场要从米尔西街道出去，\x01",
            "然后向西，途中再向南拐弯就到了。\x02\x03",

            "虽然是你们很熟悉的道路，\x01",
            "但行动也不可疏忽大意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C4")

    label("loc_13F9")


    ChrTalk(    #22
        0x8,
        (
            "#740F就麻烦你们\x01",
            "帮助帕赛尔农场\x01",
            "的人们避难吧。\x02\x03",

            "去农场要从米尔西街道出去，\x01",
            "然后向西，途中再向南拐弯就到了。\x02\x03",

            "雾比昨天更加浓，\x01",
            "几乎看不清前方的路。\x02\x03",

            "虽然是你们很熟悉的道路，\x01",
            "但行动也不可疏忽大意。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_14C4")

    Jump("loc_1ADD")

    label("loc_14C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_18AB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 6)), scpexpr(EXPR_END)), "loc_14E9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 7)), scpexpr(EXPR_END)), "loc_14FA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_14FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 0)), scpexpr(EXPR_END)), "loc_150B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_150B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1534"),
        (1, "loc_1600"),
        (2, "loc_1675"),
        (4, "loc_16E8"),
        (3, "loc_175B"),
        (5, "loc_17AD"),
        (6, "loc_1801"),
        (7, "loc_1855"),
        (SWITCH_DEFAULT, "loc_18A5"),
    )


    label("loc_1534")


    ChrTalk(    #23
        0x8,
        (
            "#740F总之就是想拜托你们\x01",
            "确认一下雾扩张的范围。\x02\x03",

            "南边的艾利兹街道，\x01",
            "西边的米尔西街道，北边的玛鲁加山道。\x02\x03",

            "希望你们去这三条道路确认\x01",
            "雾到底蔓延到哪里了。\x02\x03",

            "现在到处视野都很差，\x01",
            "无论如何调查都要慎重。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A8")

    label("loc_1600")


    ChrTalk(    #24
        0x8,
        (
            "#740F辛苦了……\x01",
            "调查似乎很顺利。\x02\x03",

            "剩下西边的米尔西街道\x01",
            "和北边的玛鲁加山道两处了。\x02\x03",

            "那么，请你们\x01",
            "继续调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A8")

    label("loc_1675")


    ChrTalk(    #25
        0x8,
        (
            "#740F辛苦了……\x01",
            "调查似乎很顺利。\x02\x03",

            "剩下南边的艾利兹街道\x01",
            "和北边的玛鲁加山道两处了。\x02\x03",

            "那么，就请\x01",
            "继续调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A8")

    label("loc_16E8")


    ChrTalk(    #26
        0x8,
        (
            "#740F辛苦了……\x01",
            "调查似乎很顺利。\x02\x03",

            "剩下南边的艾利兹街道\x01",
            "西边的米尔西街道两处了。\x02\x03",

            "那么，请你们\x01",
            "继续调查吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A8")

    label("loc_175B")


    ChrTalk(    #27
        0x8,
        (
            "#740F调查方面也只剩下\x01",
            "北边的玛鲁加山道。\x02\x03",

            "那么，就拜托你们\x01",
            "完成这任务了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A8")

    label("loc_17AD")


    ChrTalk(    #28
        0x8,
        (
            "#740F调查方面也只剩下\x01",
            "西边的米尔西街道了。\x02\x03",

            "那么，就拜托你们\x01",
            "完成这任务了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A8")

    label("loc_1801")


    ChrTalk(    #29
        0x8,
        (
            "#740F调查方面也只剩下\x01",
            "南边的艾利兹街道了。\x02\x03",

            "那么，就拜托你们\x01",
            "完成这任务了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A8")

    label("loc_1855")


    ChrTalk(    #30
        0x8,
        (
            "#743F对了，你不先回家\x01",
            "看看家里的状况吗？\x02\x03",

            "#740F雾的调查报告\x01",
            "可以先等一等。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18A5")

    Jump("loc_18A8")

    label("loc_18A8")

    Jump("loc_1ADD")

    label("loc_18AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_1ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 5)), scpexpr(EXPR_END)), "loc_1A10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_18EF")

    ChrTalk(    #31
        0x8,
        (
            "#740F艾丝蒂尔……今天\x01",
            "就请回家休息吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A0D")

    label("loc_18EF")

    TurnDirection(0x8, 0x142, 0)

    ChrTalk(    #32
        0x8,
        "#740F……你是七耀教会的人吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x142,
        (
            "#1060F嗯，是的。\x01",
            "我叫凯文·格拉汉姆。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "#742F（虽然不知道发生了什么事，\x01",
            "　但这样的艾丝蒂尔还是第一次看到……）\x02\x03",

            "#740F（麻烦你暂时\x01",
            "陪伴她一下吧。）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x142,
        "#1060F（我原本就是这样打算的。）\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x8,
        "#740F拜托了，凯文先生……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#505F？？？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_1A0D")

    Jump("loc_1ADD")

    label("loc_1A10")

    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x8, 0x101, 400)
    Sleep(600)
    OP_63(0x8)

    ChrTalk(    #38
        0x8,
        (
            "#743F…………艾丝蒂尔！？\x02\x03",

            "怎么了？\x01",
            "不是应该还在王都吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#000F嗯，因为约修亚\x01",
            "应该在家，我来接他的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x8,
        (
            "#743F……接约修亚？\x02\x03",

            "#742F…………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x102D)

    label("loc_1ADD")

    TalkEnd(0x8)
    Return()

    # Function_6_9CB end

    def Function_7_1AE1(): pass

    label("Function_7_1AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AF9")
    Call(0, 23)
    Jump("loc_34E0")

    label("loc_1AF9")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B55")
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B44")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B3B")
    OP_A9(0x6)
    Jump("loc_1B3D")

    label("loc_1B3B")

    OP_A9(0x2)

    label("loc_1B3D")

    TalkEnd(0x10)
    Return()

    label("loc_1B44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B55")
    TalkEnd(0x10)
    Return()

    label("loc_1B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_217D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5E")
    TurnDirection(0x10, 0x101, 0)

    ChrTalk(    #41
        0x10,
        (
            "哦哦……\x01",
            "这不是艾丝蒂尔和约修亚吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x10,
        (
            "呀～终于\x01",
            "两人一起出现了呢！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1008F出、出现……\x01",
            "我们又不是魔兽和幽灵来着。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#1040F里农先生也\x01",
            "和平时一样，真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(    #45
        0x10,
        (
            "啊啊，托你的福呢。\x01",
            "生意也不错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        (
            "不，不过，倒是人生\x01",
            "稍微有点危险……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        "#1044F？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        "#1011F咦……发生什么事了？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x101, 400)
    OP_62(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)

    ChrTalk(    #49
        0x10,
        (
            "不，没事……\x01",
            "当我没说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10,
        (
            "哎，别说我了，\x01",
            "约修亚可是好久没回故乡了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10,
        (
            "虽说这时期非常忙碌，\x01",
            "不过还是慢慢逛逛再走吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        "#1048F哦、哦……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x2098)
    Jump("loc_217A")

    label("loc_1D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_1E08")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DC2")

    ChrTalk(    #53
        0x10,
        (
            "刚才基蒂\x01",
            "送货回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10,
        "好像一直笑眯眯的呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        "发生什么好事了吗？\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1E05")

    label("loc_1DC2")


    ChrTalk(    #56
        0x10,
        (
            "送货回来以后基蒂\x01",
            "好像一直笑眯眯的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10,
        "发生什么好事了吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1E05")

    Jump("loc_217A")

    label("loc_1E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 5)), scpexpr(EXPR_END)), "loc_1F38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1E75")

    ChrTalk(    #58
        0x10,
        (
            "虽说现在应该非常忙碌，\x01",
            "还是慢慢逛逛再走吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10,
        (
            "特别约修亚隔了好久\x01",
            "才回到洛连特的嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F35")

    label("loc_1E75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EEA")

    ChrTalk(    #60
        0x10,
        "呀，艾丝蒂尔和约修亚。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x10,
        (
            "似乎矿山\x01",
            "有什么麻烦的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x10,
        (
            "哎，导力器\x01",
            "突然停了嘛。\x01",
            "也难怪啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1F35")

    label("loc_1EEA")


    ChrTalk(    #63
        0x10,
        (
            "似乎矿山\x01",
            "有什么麻烦的样子呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x10,
        (
            "哎，导力器\x01",
            "突然停了嘛。\x01",
            "也难怪啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F35")

    Jump("loc_217A")

    label("loc_1F38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2038")

    ChrTalk(    #65
        0x102,
        "#1044F……对了，里农先生。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x102, 400)

    ChrTalk(    #66
        0x10,
        "嗯？什么？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x13, 400)

    ChrTalk(    #67
        0x102,
        (
            "#1040F嗯，那位\x01",
            "是新的店员吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x10,
        "嗯、嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        (
            "说，说是打工呢～\x01",
            "又好像客人一样……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10,
        (
            "是老妈带来\x01",
            "帮店里忙的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x102,
        (
            "#1035F原、原来如此……\x01",
            "（里农先生看来也挺辛苦的……）\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20D6)
    Jump("loc_217A")

    label("loc_2038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20F0")

    ChrTalk(    #72
        0x10,
        (
            "多亏基蒂，\x01",
            "店里生意不错哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        (
            "和她相处也很融洽，\x01",
            "现在就和家人一样的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10,
        (
            "嗯，虽然说\x01",
            "这是件好事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10,
        (
            "不、不过我作为男人的一面\x01",
            "却有一种被逼到死角的感觉。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_217A")

    label("loc_20F0")


    ChrTalk(    #76
        0x10,
        (
            "和基蒂相处也很融洽，\x01",
            "现在就和家人一样的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10,
        (
            "嗯，虽然说\x01",
            "这是件好事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10,
        (
            "呼，呼……\x01",
            "总觉得事情好像\x01",
            "都在老妈的算计之中一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_217A")

    Jump("loc_34DD")

    label("loc_217D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_2460")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 6)), scpexpr(EXPR_END)), "loc_22A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_220C")

    ChrTalk(    #79
        0x10,
        (
            "基蒂暂时\x01",
            "留在这里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x10,
        (
            "哎，有她在\x01",
            "倒是帮了店里的大忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10,
        (
            "总觉得有点害怕，事情好像\x01",
            "都在老妈的算计里一样……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A3")

    label("loc_220C")


    ChrTalk(    #82
        0x10,
        (
            "基蒂暂时\x01",
            "留在这里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10,
        (
            "说是为了以后自己\x01",
            "开店来学习……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10,
        (
            "感、感觉又高兴又害怕……\x01",
            "真是复杂的心情。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x10,
        (
            "哎，有她在\x01",
            "倒是帮了店里的大忙。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_22A3")

    Jump("loc_245D")

    label("loc_22A6")

    TurnDirection(0x10, 0x101, 0)
    Sleep(400)

    ChrTalk(    #86
        0x10,
        (
            "呀，艾丝蒂尔和\x01",
            "雪拉扎德。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x10,
        (
            "我听说了哦，你们似乎\x01",
            "又要马上出发了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1016F就、就传开了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x103,
        "#020F呵呵，消息真灵。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10,
        (
            "托你们的福，商品也\x01",
            "顺利地重新开始进货了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10,
        (
            "有什么必要的东西\x01",
            "就在出发前买好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        (
            "#1000F嗯，谢谢里农先生。\x02\x03",

            "要是进了斯托雷加的新鞋子\x01",
            "记得帮我留着啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x10,
        "哈哈，明白啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x10,
        (
            "那么，你们俩\x01",
            "今后也要多努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x103,
        (
            "#027F嗯嗯，以后有机会\x01",
            "再来慢慢挑东西。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1001F那么再见，里农先生。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1885)
    OP_A2(0x1A56)

    label("loc_245D")

    Jump("loc_34DD")

    label("loc_2460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_2954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_253D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_24B6")

    ChrTalk(    #97
        0x10,
        (
            "真不愧是在王都的\x01",
            "百货店工作过的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x10,
        (
            "基蒂\x01",
            "相当能干。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_253A")

    label("loc_24B6")


    ChrTalk(    #99
        0x10,
        (
            "是啊是啊，关于那边\x01",
            "的女人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x10,
        (
            "是王都来的，叫基蒂。\x01",
            "现在在店里帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x10,
        (
            "感觉是打算在定期船开动之前\x01",
            "进行短期的打工吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_253A")

    Jump("loc_2951")

    label("loc_253D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 5)), scpexpr(EXPR_END)), "loc_26B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2594")

    ChrTalk(    #102
        0x10,
        (
            "基蒂……\x01",
            "非常努力哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x10,
        (
            "要选择人生的搭档，\x01",
            "就该选这样的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B1")

    label("loc_2594")


    ChrTalk(    #104
        0x10,
        (
            "基蒂……\x01",
            "非常努力哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10,
        (
            "说是来帮忙店里，一开始\x01",
            "还以为是老妈暗地里安排的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x10,
        (
            "但看了基蒂的样子，\x01",
            "感觉是真的喜欢工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10,
        (
            "虽、虽然我不大喜欢\x01",
            "老妈帮我安排相亲……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10,
        (
            "不过要选择人生的搭档，\x01",
            "我还真想选这样的人啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x10,
        (
            "不过既然是喜欢店里工作的人，\x01",
            "感觉应该能发展顺利吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_26B1")

    Jump("loc_2951")

    label("loc_26B4")

    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x10, 0x101, 0)
    Sleep(400)

    ChrTalk(    #110
        0x10,
        (
            "哦！\x01",
            "艾丝蒂尔，终于来了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#1017F里农先生……\x01",
            "嘿嘿，好久不见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x10,
        (
            "呀～我就听客人\x01",
            "说你回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x10,
        (
            "不知道几时会来，\x01",
            "一直等着你呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        (
            "#1025F这样啊。\x01",
            "抱歉这么晚才来打招呼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x10,
        "哪里哪里，没关系啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x10,
        (
            "不过你回来的\x01",
            "可真不是时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x10,
        "今天雾还是这么大啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1007F嗯，真的是……\x02\x03",

            "#1015F话说回来……\x01",
            "昨天夜里不要紧吗？\x02\x03",

            "没发生什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x10,
        "？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x10,
        (
            "呀，倒是\x01",
            "没什么特别的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x10,
        (
            "啊啊，对了，睡觉之前\x01",
            "有个红头发的游击士来过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x10,
        (
            "说是在巡逻中，\x01",
            "是你们的伙伴吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x101,
        (
            "#1006F啊，嗯。\x01",
            "他叫阿加特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x103,
        (
            "#027F呵呵，看来\x01",
            "很认真的在巡逻呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x10,
        "这种时候，就拜托你们了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x10,
        (
            "有什么需要的东西，\x01",
            "随时都可以来。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    OP_A2(0x1885)

    label("loc_2951")

    Jump("loc_34DD")

    label("loc_2954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2BA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_29C1")

    ChrTalk(    #127
        0x10,
        (
            "真不愧是在王都的\x01",
            "百货店工作过的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x10,
        (
            "那个明亮的笑容\x01",
            "真令人禁不住着迷啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B47")

    label("loc_29C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2A88")

    ChrTalk(    #129
        0x10,
        (
            "基蒂好像在王都的百货店\x01",
            "卖红茶来着……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x10,
        (
            "所以她对茶和点心的事\x01",
            "特别的清楚哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x10,
        (
            "商品的展示啊，\x01",
            "小东西的选择都很有品味……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x10,
        (
            "更出色的是，那明亮的笑容\x01",
            "和灵活的应对真是太棒了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_2B47")

    label("loc_2A88")


    ChrTalk(    #133
        0x10,
        (
            "咦，艾丝蒂尔。\x01",
            "还有什么要买吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x10,
        "对了对了，我想你应该见过了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x10,
        "外面有个女人在工作吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x10,
        (
            "她叫基蒂，\x01",
            "现在在店里帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0x10,
        (
            "感觉是打算在定期船开动之前\x01",
            "进行短期的打工吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    OP_A2(0x1885)

    label("loc_2B47")

    Jump("loc_2BA2")

    label("loc_2B4A")


    ChrTalk(    #138
        0x10,
        (
            "有什么其他需要\x01",
            "就不用客气尽管对她说吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x10,
        (
            "从点心到杂志，\x01",
            "她什么都会给你找到的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA2")

    Jump("loc_34DD")

    label("loc_2BA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_312A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 5)), scpexpr(EXPR_END)), "loc_2D41")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2C40")

    ChrTalk(    #140
        0x10,
        (
            "老妈从王都回来的时候，\x01",
            "带来一个没见过的小姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x10,
        (
            "说、说不定真的\x01",
            "是给我找来的媳妇人选。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x10,
        (
            "唉唉，真不该\x01",
            "让她去什么王都……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D3E")

    label("loc_2C40")


    ChrTalk(    #143
        0x10,
        (
            "我老妈也是搭刚才的定期船\x01",
            "从王都回来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x10,
        (
            "让人伤脑筋的是，\x01",
            "她居然带来个不认识的小姐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x10,
        (
            "说是在定期船上认识的，\x01",
            "不知道到底真的假的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x10,
        (
            "说、说不定真的\x01",
            "是给我找来的媳妇人选。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0x10,
        (
            "虽然觉得应该不可能……\x01",
            "……但是老妈可是什么都做得出来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2D3E")

    Jump("loc_3127")

    label("loc_2D41")

    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x10, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 4)), scpexpr(EXPR_END)), "loc_2DB5")

    ChrTalk(    #148
        0x10,
        (
            "哦，艾丝蒂尔。\x01",
            "终于回来了吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x101,
        "#1000F嗯，里农先生好久不见。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E48")

    label("loc_2DB5")


    ChrTalk(    #150
        0x10,
        "哦哦……这不是艾丝蒂尔吗！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x10,
        (
            "好久不见呢。\x01",
            "几时回来的呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x101,
        (
            "#1000F嗯，就刚才呢。\x02\x03",

            "里农先生看起来也很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x10,
        "那可不，生龙活虎的啦。\x02",
    )

    CloseMessageWindow()

    label("loc_2E48")


    ChrTalk(    #154
        0x10,
        (
            "对了，听说\x01",
            "你上哪里训练去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x10,
        "那，成果怎样？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x101,
        (
            "#1001F嘿嘿，当然是ＯＫ啰……\x02\x03",

            "#1015F……咦，里农先生\x01",
            "是从哪儿知道训练的事的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0x10,
        (
            "哈哈，可别小瞧\x01",
            "街坊邻里的消息网哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0x10,
        (
            "你去训练这点事，\x01",
            "大家应该都知道吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        (
            "#1016F啊、啊哈哈……\x01",
            "说来也是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x103,
        (
            "#020F呵呵，这里\x01",
            "看来一点也没变呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x10,
        "对了对了，话说回来……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x10,
        (
            "关于今天这雾，\x01",
            "真的是有点诡异呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x10,
        (
            "前往柏斯的定期船\x01",
            "好像也停了，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        (
            "#1007F嗯，其实我们也是\x01",
            "因此才没法继续走的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x103,
        (
            "#027F不过，打算停留期间\x01",
            "也顺便调查一下这雾。\x02\x03",

            "协会也希望\x01",
            "尽快搞清楚状况。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x103, 400)

    ChrTalk(    #166
        0x10,
        (
            "是吗……\x01",
            "那样可真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x10,
        (
            "但是，雪拉扎德你们\x01",
            "也要多加注意。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x10,
        (
            "这个雾实在奇怪。\x01",
            "感觉没那么简单。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #169
        0x103,
        "#020F是啊……我们会小心的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        (
            "#1002F嗯……\x02\x03",

            "#1000F那再见了，里农先生。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1885)

    label("loc_3127")

    Jump("loc_34DD")

    label("loc_312A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_34DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 4)), scpexpr(EXPR_END)), "loc_318B")

    ChrTalk(    #171
        0x10,
        (
            "话说回来，我老妈\x01",
            "还在给我找新娘候选人呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x10,
        (
            "唉哟……\x01",
            "真希望她赶快死心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34DD")

    label("loc_318B")


    ChrTalk(    #173
        0x10,
        "哟…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x10,
        "这不是艾丝蒂尔吗！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x10,
        (
            "好久不见了呢，\x01",
            "何时回来的呀？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x101,
        "#001F里农先生，气色不错嘛。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x10,
        "那可不，生龙活虎的啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0x10,
        (
            "对了对了，很快会有\x01",
            "斯托雷加的新作运动鞋到货哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #179
        0x101,
        "#501F咦～真的吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x142,
        (
            "#1060F记得是斯托雷加社创立５０周年的\x01",
            "Anniversary限定款式吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x10,
        "喔，小哥，你真了解。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x142,
        (
            "#1061F因为，我可是\x01",
            "斯托雷加的超级爱好者啊。\x02\x03",

            "#1062F看，现在穿的也是……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x10, 0x142, 200)
    TurnDirection(0x101, 0x142, 300)
    Sleep(500)

    ChrTalk(    #183
        0x10,
        "喔喔!这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #184
        0x101,
        (
            "#004F我在杂志上看到过。\x02\x03",

            "记得是利贝尔买不到的\x01",
            "外国限定款式啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #185
        0x142,
        "#1061F非常正确！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0x101,
        (
            "#007F虽然很想要，\x01",
            "但是没办法买到呀～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x142,
        (
            "#1064F……咦，艾丝蒂尔\x01",
            "莫非也是运动鞋迷？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0x101,
        "#506F算，算是吧……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #189
        0x142,
        (
            "#1061F呀～没想到\x01",
            "有共同语言，太高兴了。\x02\x03",

            "#1062F嗯嗯，这也\x01",
            "一定是女神的指引呀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0x101,
        (
            "#509F不过，七耀教会的\x01",
            "神父穿运动鞋的吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0x10,
        "咦，这个人，是神父？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0x142,
        (
            "#1061F啊哈哈，别说\x01",
            "这种死板的话嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x102C)

    label("loc_34DD")

    TalkEnd(0x10)

    label("loc_34E0")

    Return()

    # Function_7_1AE1 end

    def Function_8_34E1(): pass

    label("Function_8_34E1")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_34EE")
    Jump("loc_39C0")

    label("loc_34EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_3763")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34A, 7)), scpexpr(EXPR_END)), "loc_3596")

    ChrTalk(    #193
        0xFE,
        (
            "我也知道艾丝蒂尔你们的\x01",
            "任务是非常辛苦的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        (
            "所以，支部的事情就交给我，\x01",
            "你们集中于自己的工作就好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #195
        0xFE,
        (
            "交给支部的事，\x01",
            "我一个人会想办法应付的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3760")

    label("loc_3596")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x103, 0)
    Sleep(400)

    ChrTalk(    #196
        0xFE,
        (
            "啊，雪拉前辈。\x01",
            "我听爱娜小姐说了哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "好像马上又要\x01",
            "出发去柏斯了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x103,
        "#020F嗯嗯，是这么打算的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x101,
        (
            "#1007F抱歉哦，利吉先生。\x02\x03",

            "感觉总是\x01",
            "麻烦你看家似的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #200
        0xFE,
        "哪里，别介意。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "以前一直受卡西乌斯先生和\x01",
            "雪拉前辈照顾的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #202
        0xFE,
        (
            "为了能独当一面，\x01",
            "这点事当然要能胜任啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x103,
        (
            "#526F呵呵，就是这股劲儿。\x02\x03",

            "还要再离开一段时间，\x01",
            "洛连特的事就麻烦你了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #204
        0xFE,
        "嗯嗯，交给我吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "那么，祝前辈们\x01",
            "去柏斯旅途顺风。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A57)

    label("loc_3760")

    Jump("loc_39C0")

    label("loc_3763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 3)), scpexpr(EXPR_END)), "loc_3871")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_37C4")

    ChrTalk(    #206
        0xFE,
        (
            "听到铃声的方向……\x01",
            "是神秘森林没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0xFE,
        (
            "虽然很微弱，\x01",
            "却是非常悦耳的音色。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_386E")

    label("loc_37C4")


    ChrTalk(    #208
        0xFE,
        (
            "听到那个铃声的方向……\x01",
            "是神秘森林那边吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "虽然很微弱，\x01",
            "但是非常悦耳的音色没错。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0xFE,
        (
            "话说回来，没想到\x01",
            "出门期间竟然发生这样的事件……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #211
        0xFE,
        "我也是时运不济啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_386E")

    Jump("loc_39C0")

    label("loc_3871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_39C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_38BD")

    ChrTalk(    #212
        0xFE,
        "恭喜晋升正游击士。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #213
        0xFE,
        (
            "期待再和你们\x01",
            "一起在这里工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C0")

    label("loc_38BD")


    ChrTalk(    #214
        0xFE,
        "哎呀，这不是艾丝蒂尔吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #215
        0xFE,
        (
            "我听爱娜小姐说了哦。\x01",
            "恭喜晋升正游击士。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        "#006F嘿嘿，谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0xFE,
        (
            "说起来雪拉前辈和\x01",
            "约修亚怎样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xFE,
        "好像没看到人啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0x101,
        (
            "#000F雪拉姐还在王都呢。\x02\x03",

            "约修亚应该先\x01",
            "回家了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #220
        0xFE,
        (
            "是吗，期待能再\x01",
            "和你们一起在这里工作。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_39C0")

    TalkEnd(0x11)
    Return()

    # Function_8_34E1 end

    def Function_9_39C4(): pass

    label("Function_9_39C4")

    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_3A29")

    ChrTalk(    #221
        0xFE,
        (
            "今天的婚礼很不错呢。\x01",
            "忍不住感动起来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #222
        0xFE,
        (
            "里农要是也能举行\x01",
            "那么棒的婚礼就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4095")

    label("loc_3A29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3ADA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A9B")

    ChrTalk(    #223
        0xFE,
        (
            "店里好像\x01",
            "一大早就很忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        (
            "大家都来\x01",
            "买蜡烛和油灯了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #225
        0xFE,
        (
            "今天还有婚礼呢，\x01",
            "真伤脑筋。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)
    Jump("loc_3AD7")

    label("loc_3A9B")


    ChrTalk(    #226
        0xFE,
        (
            "店里好像\x01",
            "一大早就很忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #227
        0xFE,
        (
            "大家都来\x01",
            "买蜡烛和油灯了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD7")

    Jump("loc_4095")

    label("loc_3ADA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_3D5B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3BC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3B23")

    ChrTalk(    #228
        0xFE,
        (
            "不过，也因此\x01",
            "让我想起了\x01",
            "那个久违的料理。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BBF")

    label("loc_3B23")


    ChrTalk(    #229
        0xFE,
        "哎呀，是艾丝蒂尔啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0xFE,
        (
            "你们也够辛苦呢。\x01",
            "还得应付\x01",
            "老爷爷耍性子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0xFE,
        (
            "不过，也因此\x01",
            "让我想起了\x01",
            "那个久违的料理。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #232
        0xFE,
        (
            "这件事倒是得感谢\x01",
            "拉欧爷爷啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3BBF")

    Jump("loc_3D58")

    label("loc_3BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_3C20")

    ChrTalk(    #233
        0xFE,
        (
            "真是抱歉呢。\x01",
            "似乎让你们有了过多的期待。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #234
        0xFE,
        (
            "真是的，人生在世\x01",
            "可不能太慷慨呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D58")

    label("loc_3C20")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x1, 0x200)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x75, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C4B")
    Call(1, 1)
    Jump("loc_3D58")

    label("loc_3C4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3CA7")

    ChrTalk(    #235
        0xFE,
        (
            "里农似乎对基蒂\x01",
            "也挺中意的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "接下来可不能鲁莽行事，\x01",
            "要仔细观察情况。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D58")

    label("loc_3CA7")


    ChrTalk(    #237
        0xFE,
        (
            "基蒂暂时\x01",
            "会待在我们家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #238
        0xFE,
        "我当然再高兴不过了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0xFE,
        (
            "里农似乎对基蒂\x01",
            "也挺中意的样子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "接下来可不能鲁莽行事，\x01",
            "要仔细观察情况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #241
        0xFE,
        (
            "顺其自然、水到渠成\x01",
            "才是最好的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3D58")

    Jump("loc_4095")

    label("loc_3D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_3E0F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3DAC")

    ChrTalk(    #242
        0xFE,
        (
            "里农对基蒂\x01",
            "也是很钦佩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0xFE,
        (
            "唔……\x01",
            "好像有不错的预感哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E0C")

    label("loc_3DAC")


    ChrTalk(    #244
        0xFE,
        (
            "基蒂似乎\x01",
            "工作很努力。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        (
            "里农对那女孩\x01",
            "也是很钦佩呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #246
        0xFE,
        (
            "唔……\x01",
            "好像有不错的预感哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3E0C")

    Jump("loc_4095")

    label("loc_3E0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_3E73")

    ChrTalk(    #247
        0xFE,
        (
            "今天早上开始基蒂\x01",
            "就在下面工作了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "精神十足的声音这里\x01",
            "都听得到，真令人心情愉快。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4095")

    label("loc_3E73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_3F96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3EED")

    ChrTalk(    #249
        0xFE,
        (
            "这位小姐\x01",
            "似乎预定去柏斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xFE,
        (
            "定期船停航了，\x01",
            "真是运气不好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #251
        0xFE,
        (
            "不过，暂时就\x01",
            "让她待在我们家了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F93")

    label("loc_3EED")


    ChrTalk(    #252
        0xFE,
        (
            "这位小姐是\x01",
            "定期船上认识的人……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0xFE,
        (
            "不凑巧由于这雾\x01",
            "没法到达目的地了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #254
        0xFE,
        (
            "看她一个人挺可怜的，就让她\x01",
            "在船开动之前住在我家了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0xFE,
        "困难的时候要互相帮助嘛。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3F93")

    Jump("loc_4095")

    label("loc_3F96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_END)), "loc_4095")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3FF7")

    ChrTalk(    #256
        0xFE,
        (
            "我这么努力地帮儿子找媳妇， \x01",
            "他却好像没什么兴趣。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #257
        0xFE,
        "真是的，这个不孝子。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4095")

    label("loc_3FF7")


    ChrTalk(    #258
        0xFE,
        "呼…………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0xFE,
        (
            "能嫁给里农的女孩\x01",
            "可真难找呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #260
        0xFE,
        (
            "……既然如此，\x01",
            "只好出去旅行找儿媳妇了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #261
        0xFE,
        "人多的地方……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xFE,
        (
            "对了，难得的机会\x01",
            "就去王都看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_4095")

    TalkEnd(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_40A6")
    OP_8C(0x12, 180, 0)

    label("loc_40A6")

    Return()

    # Function_9_39C4 end

    def Function_10_40A7(): pass

    label("Function_10_40A7")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 6)), scpexpr(EXPR_END)), "loc_4117")

    ChrTalk(    #263
        0xFE,
        (
            "哈，刚才\x01",
            "真吓了一跳……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xFE,
        (
            "居然接到了\x01",
            "新娘捧花……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #265
        0xFE,
        (
            "哈哈哈，或许可以\x01",
            "稍微期待一小下哟？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_455A")

    label("loc_4117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_41F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4197")

    ChrTalk(    #266
        0xFE,
        (
            "欢迎！\x01",
            "欢迎光临里农杂货铺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #267
        0xFE,
        (
            "应该是因为导力器停了，\x01",
            "今天客人可真多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0xFE,
        (
            "大家都来找\x01",
            "应急用品了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)
    Jump("loc_41F1")

    label("loc_4197")


    ChrTalk(    #269
        0xFE,
        (
            "应该是因为导力器停了，\x01",
            "今天客人可真多。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0xFE,
        (
            "要找什么东西的话，\x01",
            "就不要客气尽管说吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41F1")

    Jump("loc_455A")

    label("loc_41F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_END)), "loc_4316")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4259")

    ChrTalk(    #271
        0xFE,
        (
            "去不成柏斯，\x01",
            "那休假中就待在这里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #272
        0xFE,
        (
            "为了学习自己开店的经验，\x01",
            "打算努力呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4313")

    label("loc_4259")


    ChrTalk(    #273
        0xFE,
        (
            "欢迎！\x01",
            "欢迎光临里农杂货铺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #274
        0xFE,
        (
            "我会暂时\x01",
            "在这里学习的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #275
        0xFE,
        (
            "为了学习自己开店的经验，\x01",
            "打算努力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #276
        0xFE,
        (
            "而且，店主里农先生\x01",
            "也对我很好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #277
        0xFE,
        (
            "感觉像在自己家一样，\x01",
            "真的很安心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_4313")

    Jump("loc_455A")

    label("loc_4316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x304, 2)), scpexpr(EXPR_END)), "loc_43D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4373")

    ChrTalk(    #278
        0xFE,
        (
            "向各位游击士们\x01",
            "推荐的是这些方便的药哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #279
        0xFE,
        (
            "出门的时候\x01",
            "请一定要购买！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_43D3")

    label("loc_4373")


    ChrTalk(    #280
        0xFE,
        (
            "欢迎！\x01",
            "客人们是游击士吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #281
        0xFE,
        (
            "那样的话，\x01",
            "有方便的药哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xFE,
        (
            "出门的时候\x01",
            "请一定要购买！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_43D3")

    Jump("loc_455A")

    label("loc_43D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_4460")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_4406")

    ChrTalk(    #283
        0xFE,
        (
            "欢迎！\x01",
            "请轻松愉快地观看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_445D")

    label("loc_4406")


    ChrTalk(    #284
        0xFE,
        (
            "欢迎！\x01",
            "欢迎光临里农杂货铺。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xFE,
        (
            "从食品到杂货，\x01",
            "应有尽有哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #286
        0xFE,
        "请随便看看。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_445D")

    Jump("loc_455A")

    label("loc_4460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 4)), scpexpr(EXPR_END)), "loc_455A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_44CD")

    ChrTalk(    #287
        0xFE,
        (
            "到定期船重新开始航行之前，\x01",
            "决定承蒙关照了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0xFE,
        (
            "既然添了麻烦，\x01",
            "就打算在店里多帮点忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_455A")

    label("loc_44CD")


    ChrTalk(    #289
        0xFE,
        (
            "承蒙布露姆老奶奶的关照，\x01",
            "决定留在这里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0xFE,
        (
            "可以的话，打算\x01",
            "在店里帮点忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0xFE,
        (
            "我平时也在王都的\x01",
            "百货店工作的。\x01",
            "待客还算有点自信。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_455A")

    TalkEnd(0x13)
    Return()

    # Function_10_40A7 end

    def Function_11_455E(): pass

    label("Function_11_455E")

    TalkBegin(0x14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_47E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x413, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_474A")

    ChrTalk(    #292
        0xFE,
        (
            "哦，艾丝蒂尔啊……\x01",
            "这，这不是约修亚吗！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x102,
        "#1030F好久不见了，菲特先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #294
        0xFE,
        (
            "哟，才多久没见啊，\x01",
            "就完全长成个男子汉了嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #295
        0xFE,
        (
            "呀，这我就放心了。\x01",
            "和艾丝蒂尔在游击士的道路上都\x01",
            "做得很漂亮嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #296
        0x102,
        "#1030F是啊，拖您的福。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #297
        0xFE,
        (
            "看来王国中\x01",
            "好像发生了严重的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #298
        0xFE,
        (
            "回归军队的卡西乌斯\x01",
            "也忙得不可开交吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xFE,
        (
            "作为游击士的你们两个\x01",
            "可要努力，不能输给他哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #300
        0x101,
        "#1000F嗯嗯，在很努力工作呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #301
        0x102,
        (
            "#1030F如果有什么困难\x01",
            "就联系协会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #302
        0xFE,
        (
            "我会的。\x01",
            "那么，两人都要小心。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)
    OP_A2(0x209B)
    Jump("loc_47E1")

    label("loc_474A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_478D")

    ChrTalk(    #303
        0xFE,
        (
            "有什么事我\x01",
            "会联络协会的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xFE,
        "那么，两人都要小心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_47E1")

    label("loc_478D")


    ChrTalk(    #305
        0xFE,
        (
            "今天早上起床的时候\x01",
            "发现导力灯打不开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xFE,
        (
            "总之先想办法\x01",
            "把照明问题解决了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_47E1")

    TalkEnd(0x14)
    Return()

    # Function_11_455E end

    def Function_12_47E5(): pass

    label("Function_12_47E5")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xA)
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x0, 0)
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4875")
    Jump("loc_48B7")

    label("loc_4875")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4891")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48B7")

    label("loc_4891")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48AD")
    OP_51(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_48B7")

    label("loc_48AD")

    OP_51(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_48B7")

    OP_51(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    ChrTalk(    #307
        0xA,
        "#051F哟，怎么了？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_494C"),
        (SWITCH_DEFAULT, "loc_498C"),
    )


    label("loc_494C")


    ChrTalk(    #308
        0xA,
        (
            "#051F哦，知道了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4985")
    Call(0, 19)
    Jump("loc_4989")

    label("loc_4985")

    Call(0, 18)

    label("loc_4989")

    Jump("loc_49CE")

    label("loc_498C")


    ChrTalk(    #309
        0xA,
        (
            "#052F怎么，不调整了吗？\x02\x03",

            "#050F需要我的重剑时\x01",
            "尽管开口吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49CE")

    label("loc_49CE")

    SetChrSubChip(0xA, 0)
    TalkEnd(0xA)
    Return()

    # Function_12_47E5 end

    def Function_13_49D7(): pass

    label("Function_13_49D7")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xB)
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x0, 0)
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4A67")
    Jump("loc_4AA9")

    label("loc_4A67")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4A83")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AA9")

    label("loc_4A83")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A9F")
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AA9")

    label("loc_4A9F")

    OP_51(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4AA9")

    OP_51(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AF3")

    ChrTalk(    #310
        0xB,
        "◆没有台词。\x02",
    )

    CloseMessageWindow()
    Call(0, 19)
    Jump("loc_4CF7")

    label("loc_4AF3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4B2D")

    ChrTalk(    #311
        0xB,
        (
            "#038F唔唔……诸位。\x02\x03",

            "有、有什么事……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B6E")

    label("loc_4B2D")


    ChrTalk(    #312
        0xB,
        (
            "#030F呀，诸位。\x01",
            "贵安。\x02\x03",

            "看来好像有事……\x01",
            "不过先来一曲怎样？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B6E")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4C60")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4BD1"),
        (SWITCH_DEFAULT, "loc_4C14"),
    )


    label("loc_4BD1")


    ChrTalk(    #313
        0xB,
        (
            "#037F呵，原来如此……\x02\x03",

            "看来是需要\x01",
            "我这个天才的力量啊。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_4C5D")

    label("loc_4C14")


    ChrTalk(    #314
        0xB,
        (
            "#037F哎呀，不要我了吗？\x02\x03",

            "呼，思恋我美妙的琴声时，\x01",
            "尽管来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C5D")

    label("loc_4C5D")

    Jump("loc_4CF7")

    label("loc_4C60")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4C6D"),
        (SWITCH_DEFAULT, "loc_4CAE"),
    )


    label("loc_4C6D")


    ChrTalk(    #315
        0xB,
        (
            "#030F呵，原来如此。\x02\x03",

            "看来是需要\x01",
            "我这个天才的力量啊。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_4CF7")

    label("loc_4CAE")


    ChrTalk(    #316
        0xB,
        (
            "#030F哎呀，不要我了吗？\x02\x03",

            "呼，思恋我美妙的琴声时，\x01",
            "尽管来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CF7")

    label("loc_4CF7")

    SetChrSubChip(0xB, 0)
    TalkEnd(0xB)
    Return()

    # Function_13_49D7 end

    def Function_14_4D00(): pass

    label("Function_14_4D00")

    TalkBegin(0xC)

    ChrTalk(    #317
        0xC,
        (
            "#040F各位，辛苦了。\x02\x03",

            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4D83"),
        (SWITCH_DEFAULT, "loc_4DAC"),
    )


    label("loc_4D83")


    ChrTalk(    #318
        0xC,
        (
            "#040F明白了。\x01",
            "要调整队伍吧？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 18)
    Jump("loc_4DE1")

    label("loc_4DAC")


    ChrTalk(    #319
        0xC,
        (
            "#040F我在这里待命。\x02\x03",

            "如果有事，\x01",
            "请尽管开口。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DE1")

    label("loc_4DE1")

    TalkEnd(0xC)
    Return()

    # Function_14_4D00 end

    def Function_15_4DE5(): pass

    label("Function_15_4DE5")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E26")

    ChrTalk(    #320
        0xD,
        (
            "#560F啊，阿加特哥哥。\x02\x03",

            "那个，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E99")

    label("loc_4E26")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4E66")

    ChrTalk(    #321
        0xD,
        (
            "#060F啊，姐姐，是你们啊。\x01",
            "怎么了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E99")

    label("loc_4E66")


    ChrTalk(    #322
        0xD,
        (
            "#060F啊，姐姐，是你们啊。\x02\x03",

            "那个，有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E99")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4EF2"),
        (SWITCH_DEFAULT, "loc_4F74"),
    )


    label("loc_4EF2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F34")

    ChrTalk(    #323
        0xD,
        (
            "#060F啊，嗯，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F5A")

    label("loc_4F34")


    ChrTalk(    #324
        0xD,
        (
            "#560F啊，明白了。\x01",
            "要调整队伍吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F5A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F6D")
    Call(0, 19)
    Jump("loc_4F71")

    label("loc_4F6D")

    Call(0, 18)

    label("loc_4F71")

    Jump("loc_5021")

    label("loc_4F74")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4FD5")

    ChrTalk(    #325
        0xD,
        (
            "#064F咦，又不要了吗……？\x02\x03",

            "#060F我就在这里等，\x01",
            "有什么事就来找我吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_501E")

    label("loc_4FD5")


    ChrTalk(    #326
        0xD,
        (
            "#064F咦，又不要了吗……？\x02\x03",

            "#060F我会在这里等的，\x01",
            "随时都可以来找我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_501E")

    Jump("loc_5021")

    label("loc_5021")

    TalkEnd(0xD)
    Return()

    # Function_15_4DE5 end

    def Function_16_5025(): pass

    label("Function_16_5025")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_50B5")
    Jump("loc_50F7")

    label("loc_50B5")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_50D1")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50F7")

    label("loc_50D1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50ED")
    OP_51(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_50F7")

    label("loc_50ED")

    OP_51(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50F7")

    OP_51(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)

    ChrTalk(    #327
        0xE,
        "#070F哦，情况怎么样？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5190"),
        (SWITCH_DEFAULT, "loc_51C3"),
    )


    label("loc_5190")


    ChrTalk(    #328
        0xE,
        "#070F要调整队伍吧？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_51BC")
    Call(0, 19)
    Jump("loc_51C0")

    label("loc_51BC")

    Call(0, 18)

    label("loc_51C0")

    Jump("loc_51F2")

    label("loc_51C3")


    ChrTalk(    #329
        0xE,
        (
            "#070F我在这里等。\x01",
            "需要的时候就说一声。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51F2")

    label("loc_51F2")

    SetChrSubChip(0xE, 0)
    TalkEnd(0xE)
    Return()

    # Function_16_5025 end

    def Function_17_51FB(): pass

    label("Function_17_51FB")

    OP_51(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_528B")
    Jump("loc_52CD")

    label("loc_528B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_52A7")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52CD")

    label("loc_52A7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52C3")
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_52CD")

    label("loc_52C3")

    OP_51(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52CD")

    OP_51(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    ChrTalk(    #330
        0x9,
        "#020F嗯，怎么了？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "【队伍组成】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5362"),
        (SWITCH_DEFAULT, "loc_5388"),
    )


    label("loc_5362")


    ChrTalk(    #331
        0x9,
        "#020F哎呀，要调整队伍吗？\x02",
    )

    CloseMessageWindow()
    Call(0, 19)
    Jump("loc_53C5")

    label("loc_5388")


    ChrTalk(    #332
        0x9,
        (
            "#020F呵呵，我就在这儿\x01",
            "休息吧。\x02\x03",

            "那么，之后就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53C5")

    label("loc_53C5")

    SetChrSubChip(0x9, 0)
    TalkEnd(0x9)
    Return()

    # Function_17_51FB end

    def Function_18_53CE(): pass

    label("Function_18_53CE")

    OP_C9(0x1, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5439")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)

    label("loc_5439")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5482")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x76, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_546C")
    SetChrFlags(0xB, 0x2)
    SetChrSubChip(0xB, 0)
    SetChrChipByIndex(0xB, 18)
    Jump("loc_5471")

    label("loc_546C")

    SetChrChipByIndex(0xB, 9)

    label("loc_5471")

    SetChrPos(0xB, 1060, 200, 69820, 360)

    label("loc_5482")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_54A5")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -1940, 0, 74490, 360)

    label("loc_54A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_54C8")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)

    label("loc_54C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_54F5")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)

    label("loc_54F5")

    OP_0D()
    Return()

    # Function_18_53CE end

    def Function_19_54F7(): pass

    label("Function_19_54F7")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    OP_A3(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5594")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 7)
    SetChrPos(0x9, 1060, 200, 69820, 360)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5579")
    OP_41(0x2, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_5579")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5594")
    OP_41(0x2, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_5594")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_55F7")
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x4)
    SetChrChipByIndex(0xA, 8)
    SetChrPos(0xA, -790, 200, 69820, 360)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55DC")
    OP_41(0x5, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_55DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55F7")
    OP_41(0x5, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_55F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5650")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -4290, 0, 73800, 360)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5635")
    OP_41(0x6, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_5635")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5650")
    OP_41(0x6, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_5650")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56B3")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 10)
    SetChrPos(0xE, 140, 200, 71510, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5698")
    OP_41(0x7, 0x0, 0x3)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_5698")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_D5(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x151), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56B3")
    OP_41(0x7, 0x0, 0x4)
    OP_3E(0x151, 1)
    OP_A2(0x0)

    label("loc_56B3")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5730")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #333
        (
            "\x07\x05※要待命的成员\x01",
            "　装备着『零力场发生器』。\x01",
            "　将其回收加入队伍的携带品。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_5730")

    Return()

    # Function_19_54F7 end

    def Function_20_5731(): pass

    label("Function_20_5731")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5744")
    Call(0, 42)

    label("loc_5744")

    OP_4A(0x8, 255)
    OP_6D(1310, 0, 112280, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(2730, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    AddParty(0x2, 0xF7, 0xFF)
    AddParty(0x5, 0xF8, 0xFF)
    AddParty(0x6, 0xF9, 0xFF)
    AddParty(0x3, 0xFA, 0xFF)
    AddParty(0x4, 0xFB, 0xFF)
    AddParty(0x7, 0xFC, 0xFF)
    SetChrPos(0x101, 540, 0, 116590, 0)
    SetChrPos(0x103, 1740, 0, 116600, 0)
    SetChrPos(0x108, -60, 0, 114490, 0)
    SetChrPos(0x104, 3390, 0, 114890, 0)
    SetChrPos(0x106, 2040, 0, 115240, 0)
    SetChrPos(0x107, 1100, 0, 115100, 0)
    SetChrPos(0x105, 110, 0, 115560, 0)

    def lambda_581A():
        OP_6D(80, 0, 117460, 2500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_581A)

    def lambda_5832():
        OP_67(0, 6590, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5832)
    FadeToBright(1500, 0)
    OP_0D()
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #334
        0x8,
        (
            "#741F呵呵，没想到这个时候\x01",
            "你们会来。\x02\x03",

            "#740F记得\x01",
            "本来是要去柏斯支部的吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0x103,
        (
            "#025F#6P嗯嗯，没错。\x02\x03",

            "#524F不失时机地\x01",
            "被这事情耽搁了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #336
        0x8,
        (
            "#741F不过因此\x01",
            "倒是帮了我们大忙。\x02\x03",

            "#740F话说回来……\x01",
            "艾丝蒂尔去了训练场以后\x01",
            "就没再见过了吧？\x02\x03",

            "工作用的新衣服\x01",
            "也很合身嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x101,
        "#1025F#6P是、是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #338
        0x8,
        (
            "#740F和金先生、科洛蒂娅殿下、\x01",
            "还有小提妲初次见面吧？\x02\x03",

            "我是负责洛连特支部\x01",
            "接待的爱娜。\x02\x03",

            "请多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0x105,
        "#048F#6P是，请多关照。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #340
        0x107,
        (
            "#560F#6P那个那个……\x01",
            "请多关照。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #341
        0x108,
        (
            "#071F哈哈，你的事迹\x01",
            "听过不少哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #342
        0x8,
        "#743F哎呀……是这样吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)
    Sleep(500)

    ChrTalk(    #343
        0x8,
        (
            "#740F对了奥利维尔先生。\x01",
            "你在那儿干什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_91(0x104, 0xFFFFFED4, 0x0, 0x0, 0x3E8, 0x0)

    ChrTalk(    #344
        0x104,
        (
            "#031F#6P哈哈哈……\x01",
            "别，别介意。\x02\x03",

            "一定是回想\x01",
            "起了那晚的事了。\x01",
            "是这样没错吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #345
        0x8,
        "#743F？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #346
        0x103,
        (
            "#021F#6P呵呵……\x01",
            "别提了吧。\x02\x03",

            "#020F说起来阿加特\x01",
            "认识爱娜的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)

    ChrTalk(    #347
        0x106,
        (
            "#051F算是吧。\x02\x03",

            "只不过很少来洛连特，\x01",
            "才见过几面而已。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0x8,
        (
            "#741F呵呵，这次就麻烦你了。\x02\x03",

            "#742F寒暄就到此为止。\x01",
            "赶快听我说明状况吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #349
        0x103,
        "#022F#6P嗯嗯，拜托了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #350
        0x8,
        (
            "#742F……起雾是在\x01",
            "今天清晨左右。\x02\x03",

            "一开始只是\x01",
            "薄薄的雾霭……\x02\x03",

            "但是慢慢就浓了起来，\x01",
            "开始遮挡住视线。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #351
        0x105,
        (
            "#043F#6P起雾的原因\x01",
            "现在还不清楚吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #352
        0x8,
        (
            "#742F嗯嗯，现在是的。\x02\x03",

            "可以确定已经覆盖了\x01",
            "洛连特市内整片区域……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x108,
        (
            "#074F雾也分很多种类的。\x02\x03",

            "有的在海上产生，\x01",
            "并慢慢飘到岸上，\x01",
            "也有在盆地直接产生的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x104,
        (
            "#030F#6P唔……从王国地图上看，\x01",
            "洛连特好像在盆地里吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x8,
        (
            "#740F嗯嗯，算是的。\x02\x03",

            "所以也很有可能\x01",
            "只是单纯的自然现象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x103,
        (
            "#026F#6P无论如何……\x01",
            "最好还是警戒一下吧。\x02\x03",

            "#020F柏斯行中断，\x01",
            "暂时留在在洛连特地区\x01",
            "看看情况比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #357
        0x106,
        (
            "#051F看来是这样比较好。\x02\x03",

            "况且在雾散之前，\x01",
            "定期船也无法启动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x101,
        "#1003F#6P啊……那个……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #359
        0x106,
        "#052F什么，艾丝蒂尔？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #360
        0x101,
        (
            "#1025F#5P嗯，想问问\x01",
            "那个空贼事件怎样了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x106,
        (
            "#050F那个事件\x01",
            "是因为暂时没有别的事情\x01",
            "才打算调查看看的吧？\x02\x03",

            "但调查现在也由王国军在做了，\x01",
            "所以我们也没必要勉强帮忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x101,
        "#1026F#5P但，但是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x106,
        (
            "#555F怎么……\x01",
            "什么地方值得注意吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x101,
        (
            "#1003F#5P啊，不是……\x01",
            "倒不是这个意思。\x02\x03",

            "但是……我……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(50)
    TurnDirection(0x105, 0x101, 400)
    Sleep(50)
    TurnDirection(0x104, 0x101, 400)
    Sleep(500)

    ChrTalk(    #365
        0x103,
        (
            "#026F……艾丝蒂尔。\x02\x03",

            "#020F虽然不知道\x01",
            "你在想什么……\x02\x03",

            "但稍微冷静点吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #366
        0x101,
        "#1004F#5P咦……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #367
        0x103,
        (
            "#020F空贼艇抢夺事件，\x01",
            "在某种程度上是已经结束了的事件哦。\x02\x03",

            "若是有人质被抓走也就罢了，\x01",
            "但还没有到需要协会出动那地步。\x02\x03",

            "再说空贼在柏斯周边地区\x01",
            "停留的可能性也很小了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x101,
        "#1026F#5P这、这……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x103,
        (
            "#026F另一方面这边的异常现象\x01",
            "引起的事件现在还层出不穷。\x02\x03",

            "而且很可能会是\x01",
            "『结社』干的好事。\x02\x03",

            "#022F那么……\x01",
            "如何取舍才是对的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x101,
        (
            "#1003F#5P………………………………\x01",
            "………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #371
        0x105,
        "#043F#6P……艾丝蒂尔。\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #372
        0x107,
        (
            "#065F#6P那、那个，雪拉姐！\x02\x03",

            "我想姐姐大概\x01",
            "也有自己的原因！\x02\x03",

            "所以，那个……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Sleep(500)

    ChrTalk(    #373
        0x101,
        (
            "#1003F#5P……不，提妲。\x02\x03",

            "#1007F雪拉姐说得对。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #374
        0x107,
        "#063F#6P姐姐……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #375
        0x101,
        (
            "#1025F#5P对不起，雪拉姐……\x02\x03",

            "看来我还\x01",
            "没搞清楚状况。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #376
        0x103,
        (
            "#524F不用道歉。\x02\x03",

            "搞不清楚状况\x01",
            "的时候谁都会有。\x02\x03",

            "#021F连我也会这样的，\x01",
            "特别是那边的阿加特。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x103, 400)

    ChrTalk(    #377
        0x106,
        "#055F你说啥？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #378
        0x103,
        (
            "#026F但是，不迷失自我、\x01",
            "不断摸索最好的道路，\x01",
            "对游击士来说也是必要的思想准备哦。\x02\x03",

            "#525F说起来容易，\x01",
            "做起来难倒是真的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #379
        0x108,
        (
            "#070F关于这方面，\x01",
            "我也还在学着呢。\x02\x03",

            "比起大人我们还差得远呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #380
        0x101,
        "#1004F#2P是，是吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #381
        0x108,
        (
            "#074F在任何逆境中都不会迷失自我……\x01",
            "那诙谐幽默而坚强的心灵……\x02\x03",

            "#070F以前，大人来卡尔瓦德时，\x01",
            "好几次把我从危机中救出来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #382
        0x101,
        "#1025F#2P是这样啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #383
        0x106,
        (
            "#051F不过，那大叔的境界\x01",
            "可没那么简单就能达到。\x02\x03",

            "我们就以自己的步调\x01",
            "一步步前进吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)

    ChrTalk(    #384
        0x101,
        "#1006F#5P嗯……是啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)
    Sleep(500)

    ChrTalk(    #385
        0x101,
        (
            "#1007F#6P爱娜姐，对不起。\x01",
            "跑题了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_65B0():
        OP_8C(0x103, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_65B0)
    Sleep(50)

    def lambda_65C3():
        OP_8C(0x108, 0, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_65C3)
    Sleep(50)

    def lambda_65D6():
        OP_8C(0x104, 0, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_65D6)
    Sleep(50)

    def lambda_65E9():
        OP_8C(0x106, 0, 400)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_65E9)
    Sleep(50)

    def lambda_65FC():
        OP_8C(0x107, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_65FC)
    Sleep(50)

    def lambda_660F():
        OP_8C(0x105, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_660F)
    Sleep(500)

    ChrTalk(    #386
        0x8,
        (
            "#741F呵呵，没关系的。\x02\x03",

            "#740F那么我就\x01",
            "继续往下说了……\x02\x03",

            "此时此刻没有什么\x01",
            "特别的工作要委托你们。\x02\x03",

            "只是以防万一，\x01",
            "在这里待命就可以了。\x02\x03",

            "回家里等也可以哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #387
        0x101,
        (
            "#1011F#6P啊，嗯。\x01",
            "我是打算回家一趟……\x02\x03",

            "除此以外，\x01",
            "还有没有需要注意的事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #388
        0x8,
        (
            "#744F嗯……是。\x02\x03",

            "#742F一定要说的话，就希望你们\x01",
            "调查一下各街道的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x101,
        "#1004F#6P调查街道的情况？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #390
        0x8,
        (
            "#742F刚才也说过了，\x01",
            "雾覆盖了\x01",
            "洛连特市整个地区……\x02\x03",

            "而且似乎在城外\x01",
            "也扩展得相当快。\x02\x03",

            "考虑到今后的事，\x01",
            "还是视察清楚\x01",
            "具体起雾的范围比较好。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #391
        0x104,
        (
            "#030F#6P嗯，像这样\x01",
            "定期船持续无法启动的话，\x01",
            "就需要确保陆路的安全了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #392
        0x8,
        (
            "#740F嗯嗯，正是如此。\x02\x03",

            "南边的艾利兹街道，\x01",
            "西边的米尔西街道，北边的玛鲁加山道。\x02\x03",

            "希望你们去确认这三条街道的状态，\x01",
            "看看雾到底蔓延到哪里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x101,
        (
            "#1006F#6P明白。\x01",
            "这点工作小事一桩啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #394
        0x103,
        (
            "#027F那么，既然如此……\x02\x03",

            "这次我和艾丝蒂尔\x01",
            "来当向导比较好呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #395
        0x101,
        (
            "#1006F#5P嗯，是啊。\x01",
            "洛连特地区大致上我们都很熟悉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #396
        0x106,
        (
            "#051F没办法了……\x01",
            "赶快选择同行者吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    SetChrName("")

    AnonymousTalk(    #397
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_6D(16980, 0, 120650, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(300, 0)
    OP_0D()
    OP_A2(0x180C)
    OP_A2(0x10F0)
    ClearMapFlags(0x2000000)
    NewScene("ED6_DT21/T0100   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_20_5731 end

    def Function_21_6AA1(): pass

    label("Function_21_6AA1")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AC1")
    Call(0, 42)
    FadeToBright(0, 0)
    Call(0, 43)

    label("loc_6AC1")

    Call(0, 40)
    OP_4A(0x8, 255)
    OP_6D(210, 0, 117420, 0)
    OP_67(0, 6120, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(279, 0)
    SetChrPos(0x101, 510, 0, 116600, 0)
    SetChrPos(0x103, 1570, 0, 116600, 0)
    SetChrPos(0x105, -230, 0, 115790, 0)
    SetChrPos(0x106, 2320, 0, 115270, 0)
    SetChrPos(0x108, 250, 0, 114280, 0)
    SetChrPos(0x104, 1850, 0, 114310, 0)
    SetChrPos(0x107, 1070, 0, 115580, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #398
        0x8,
        (
            "#740F大家都辛苦了。\x02\x03",

            "首先请让我\x01",
            "支付报酬吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x8F, 0x4, 0x10)
    OP_AF(0x3, 0x8F)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #399
        0x8,
        (
            "#744F不过，本以为\x01",
            "报告不会太清晰……\x02\x03",

            "没想到雾扩散的界线，\x01",
            "调查的这么清楚。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0x103,
        (
            "#022F#6P嗯嗯……\x01",
            "说起来是有点不自然。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #401
        0x101,
        (
            "#1015F#6P实际在地图上\x01",
            "雾是怎样蔓延的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #402
        0x8,
        "#742F……稍等一下。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS135._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS220._CH")
    OP_C6(0x0, 0x4, 0, 0, 0)
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(1500)
    SetChrName("爱娜")
    SetMessageWindowPos(250, 50, -1, -1)

    AnonymousTalk(    #403
        (
            "\x07\x00#744F艾利兹街道方向是６０塞尔矩，\x01",
            "米尔西街道方向８０塞尔矩，\x01",
            "玛鲁加山道方向１４０塞尔矩……\x02\x03",

            "#740F……这样可以了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x4, 0, 0, 0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_61(0x101)
    SetMessageWindowPos(150, 50, -1, -1)

    AnonymousTalk(    #404
        (
            "#1007F嗯，只是这样的话\x01",
            "还是很不清楚啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_61(0x105)
    SetMessageWindowPos(100, 80, -1, -1)

    AnonymousTalk(    #405
        (
            "#043F嗯……\x02\x03",

            "雾的蔓延形式，似乎根据\x01",
            "产生原因和风向流动而变化。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 1000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #406
        0x106,
        (
            "#555F说回来，这情况\x01",
            "还真是不清不楚啊。\x02\x03",

            "还是只能在这里待命\x01",
            "以备不时之需吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #407
        0x8,
        (
            "#745F嗯～只能这样吧。\x02\x03",

            "单凭现状，王国军\x01",
            "好像也难以决定是否出动。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #408
        0x101,
        "#1004F#6P啊，这么说来……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)
    Sleep(500)

    ChrTalk(    #409
        0x101,
        (
            "#1018F#5P对了，提妲！\x02\x03",

            "『除雾装置』之类的新发明，\x01",
            "博士不是做出来了吗！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6F9F():

        label("loc_6F9F")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_6F9F")

    QueueWorkItem2(0x107, 3, lambda_6F9F)

    def lambda_6FB0():

        label("loc_6FB0")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_6FB0")

    QueueWorkItem2(0x103, 3, lambda_6FB0)

    def lambda_6FC1():

        label("loc_6FC1")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_6FC1")

    QueueWorkItem2(0x106, 3, lambda_6FC1)

    def lambda_6FD2():

        label("loc_6FD2")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_6FD2")

    QueueWorkItem2(0x104, 3, lambda_6FD2)

    def lambda_6FE3():

        label("loc_6FE3")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_6FE3")

    QueueWorkItem2(0x105, 3, lambda_6FE3)

    def lambda_6FF4():

        label("loc_6FF4")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_6FF4")

    QueueWorkItem2(0x108, 3, lambda_6FF4)
    Sleep(500)

    ChrTalk(    #410
        0x107,
        (
            "#064F#6P啊啊……！？\x02\x03",

            "#063F嗯～唔……\x02\x03",

            "之前爷爷是\x01",
            "发明过『除湿机』\x01",
            "之类的东西……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0x101,
        (
            "#1006F#5P『除湿器』──从名称来看，\x01",
            "就是除去湿气的装置吧。\x02\x03",

            "那个能用吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #412
        0x107,
        (
            "#561F#6P嗯～应该不行哦。\x02\x03",

            "#063F要处理室外的空气\x01",
            "会需要几百台才行……\x02\x03",

            "就算准备除湿机，\x01",
            "也只能暂时起些作用。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x101,
        (
            "#1007F#5P唉……\x01",
            "没那么简单啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x108,
        (
            "#074F要是有和『结社』\x01",
            "扯上关系的证据就好了。\x02\x03",

            "但现在要硬说是他们干的\x01",
            "又看起来不大像。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #415
        0x101,
        "#1004F#5P这话怎么说？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #416
        0x108,
        (
            "#072F像之前的事件，\x01",
            "他们使用『福音』后\x01",
            "就发生了『不可能的现象』。\x02\x03",

            "但是，这次的雾\x01",
            "看起来并没有那么夸张啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x101,
        "#1002F#5P这倒是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x104,
        (
            "#035F#6P呼，还有一点。\x02\x03",

            "#030F他们每次都会以\x01",
            "某种形式发送『暗示』。\x02\x03",

            "可是，这次看来还\x01",
            "没收到类似的东西。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #419
        0x101,
        "#1004F#5P暗示？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0x104,
        (
            "#035F#6P亡灵骚乱、戴墨镜的男子、\x01",
            "还有送到各处的恐吓信……\x02\x03",

            "#030F就是说让我们感到\x01",
            "『可疑』的挑衅性标志。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #421
        0x101,
        "#1015F#5P原，原来如此……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #422
        0x8,
        (
            "#742F唔……\x01",
            "确实给人一种疑惑的感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #423
        0x103,
        "#522F#6P………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0x8,
        (
            "#743F？？？\x02\x03",

            "怎么了，雪拉扎德？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0x103,
        (
            "#026F#6P……刚刚说的暗示。\x02\x03",

            "#022F搞不好已经\x01",
            "收到了也说不定。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #426
        0x8,
        "#742F喔……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #427
        0x101,
        "#1020F#5P怎、怎么说？\x02",
    )

    CloseMessageWindow()
    OP_20(0xBB8)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    SetChrPos(0xF, 4170, 0, 108710, 0)

    NpcTalk(    #428
        0xF,
        "老人的声音",
        "#2P#3S不、不好啦～！\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_7545():

        label("loc_7545")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_7545")

    QueueWorkItem2(0x101, 3, lambda_7545)

    def lambda_7556():

        label("loc_7556")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_7556")

    QueueWorkItem2(0x103, 3, lambda_7556)

    def lambda_7567():

        label("loc_7567")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_7567")

    QueueWorkItem2(0x106, 3, lambda_7567)

    def lambda_7578():

        label("loc_7578")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_7578")

    QueueWorkItem2(0x104, 3, lambda_7578)

    def lambda_7589():

        label("loc_7589")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_7589")

    QueueWorkItem2(0x105, 3, lambda_7589)

    def lambda_759A():

        label("loc_759A")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_759A")

    QueueWorkItem2(0x107, 3, lambda_759A)

    def lambda_75AB():

        label("loc_75AB")

        TurnDirection(0xFE, 0xF, 400)
        OP_48()
        Jump("loc_75AB")

    QueueWorkItem2(0x108, 3, lambda_75AB)

    def lambda_75BC():
        OP_6D(2380, 0, 113020, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75BC)
    Sleep(1000)
    OP_43(0xF, 0x0, 0x0, 0x16)
    WaitChrThread(0x101, 0x1)

    def lambda_75E5():
        OP_6D(-420, 0, 116820, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_75E5)

    def lambda_75FD():
        OP_6B(2670, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_75FD)

    def lambda_760D():
        OP_8F(0xFE, 0xFFFFFC40, 0x0, 0x1C174, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_760D)
    Sleep(100)

    def lambda_762D():
        OP_8F(0xFE, 0x80C, 0x0, 0x1BE86, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_762D)
    WaitChrThread(0xF, 0x0)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x3)
    OP_44(0x103, 0x3)
    OP_44(0x106, 0x3)
    OP_44(0x104, 0x3)
    OP_44(0x105, 0x3)
    OP_44(0x107, 0x3)
    OP_44(0x108, 0x3)

    ChrTalk(    #429
        0x101,
        "#1026F#2P市、市长爷爷！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7724")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇不与克劳斯市长重逢】\x01",      # 0
            "【◇与克劳斯市长重逢】\x01",        # 1
            "【◇不变更】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7718"),
        (1, "loc_771E"),
        (SWITCH_DEFAULT, "loc_7724"),
    )


    label("loc_7718")

    OP_A3(0x1881)
    Jump("loc_7724")

    label("loc_771E")

    OP_A2(0x1881)
    Jump("loc_7724")

    label("loc_7724")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77EC")

    ChrTalk(    #430
        0xF,
        (
            "#603F呼呼……啊啊……\x02\x03",

            "#604F哦、哦哦……艾丝蒂尔……\x01",
            "真是好久不见了啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x101,
        (
            "#1025F#2P啊……嗯。\x01",
            "好久不见了。\x02\x03",

            "不过，您怎么了？\x01",
            "这么惊慌……\x02\x03",

            "#1015F……唔，好像和上次\x01",
            "事件时候一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7880")

    label("loc_77EC")


    ChrTalk(    #432
        0xF,
        (
            "#603F呼呼……啊啊……\x02\x03",

            "#604F太、太好了……\x01",
            "正好大家都在……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #433
        0x101,
        (
            "#1025F#2P您怎、怎么了？\x01",
            "这么惊慌……\x02\x03",

            "#1015F……唔，好像和上次\x01",
            "事件时候一样。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7880")


    ChrTalk(    #434
        0x103,
        (
            "#022F#2P市长先生。\x01",
            "请先冷静下来。\x02\x03",

            "发生了什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #435
        0xF,
        (
            "#604F发、发生什么……\x02\x03",

            "#602F唔，你们都\x01",
            "没事吧～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x103,
        "#023F#2P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #437
        0x8,
        "#743F请问，是怎么回事？\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x51)
    Sleep(300)

    ChrTalk(    #438
        0xF,
        (
            "#602F……刚才，我家的玲达\x01",
            "突然昏倒了。\x02\x03",

            "而且，好像还有其它市民\x01",
            "也和她一样昏倒了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #439
        0x101,
        "#1020F#2P！！！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x8,
        "#742F什么！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 41)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0101   ._SN", 110, 0, 0)
    IdleLoop()
    Return()

    # Function_21_6AA1 end

    def Function_22_79CB(): pass

    label("Function_22_79CB")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x4)

    def lambda_79E6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_79E6)
    OP_8E(0xFE, 0xF64, 0x0, 0x1B01C, 0xBB8, 0x0)
    OP_8E(0xFE, 0x352, 0x0, 0x1B9E0, 0xBB8, 0x0)
    OP_8E(0xFE, 0x29E, 0x0, 0x1BD78, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_22_79CB end

    def Function_23_7A36(): pass

    label("Function_23_7A36")

    EventBegin(0x0)
    OP_4A(0x10, 255)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7ACE")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇和里农第一次重逢】\x01",      # 0
            "【◇已经见过里农】\x01",          # 1
            "【◇不变更】\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7AC2"),
        (1, "loc_7AC8"),
        (SWITCH_DEFAULT, "loc_7ACE"),
    )


    label("loc_7AC2")

    OP_A3(0x1885)
    Jump("loc_7ACE")

    label("loc_7AC8")

    OP_A2(0x1885)
    Jump("loc_7ACE")

    label("loc_7ACE")

    Fade(1000)
    OP_6D(4490, 0, 1340, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 3390, 0, 50, 0)
    SetChrPos(0x103, 4490, 0, 50, 0)
    SetChrPos(0x107, 3240, 0, -1100, 0)
    SetChrPos(0x105, 4350, 0, -1100, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C8E")

    ChrTalk(    #441
        0x10,
        (
            "#5P哦！\x01",
            "艾丝蒂尔，终于来了啊！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #442
        0x101,
        (
            "#1017F里农先生……\x01",
            "嘿嘿，好久不见。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #443
        0x10,
        (
            "#5P呀～从客人那里\x01",
            "说你回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #444
        0x10,
        (
            "#5P我一直期待\x01",
            "你什么时候过来呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x101,
        (
            "#1025F这样啊。\x01",
            "抱歉这么晚才来打招呼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #446
        0x10,
        "#5P哪里哪里，没关系啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0x10,
        (
            "#5P不过时机真是不好，\x01",
            "回来的可真不是时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0x10,
        "#5P今天雾还是这么大啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7CCF")

    label("loc_7C8E")


    ChrTalk(    #449
        0x10,
        "#5P早啊，艾丝蒂尔。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #450
        0x10,
        (
            "#5P呀～\x01",
            "今天一大早雾还是这么大啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7CCF")


    ChrTalk(    #451
        0x101,
        (
            "#1007F是啊，没错。\x02\x03",

            "#1015F话说回来……\x01",
            "昨天晚上没什么事吗？\x02\x03",

            "没发生什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #452
        0x10,
        "#5P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #453
        0x10,
        (
            "#5P不，起床后没发现\x01",
            "有什么特别的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #454
        0x10,
        (
            "#5P啊啊，睡觉前\x01",
            "有个红头发的游击士来过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #455
        0x10,
        (
            "#5P说是在巡逻，\x01",
            "是你们的伙伴吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #456
        0x101,
        (
            "#1006F啊，嗯。\x01",
            "他叫阿加特。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #457
        0x103,
        (
            "#027F呵呵，看来\x01",
            "很认真的在巡逻呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x107,
        (
            "#064F#6P对了……\x02\x03",

            "#560F对了，姐姐。\x02\x03",

            "要不要给阿加特哥哥他们\x01",
            "买些吃的？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_7E64():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E64)
    Sleep(100)

    def lambda_7E77():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7E77)
    Sleep(100)

    def lambda_7E8A():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7E8A)
    Sleep(200)

    ChrTalk(    #459
        0x101,
        (
            "#1018F#5P啊……\x01",
            "提妲，Nice idea！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x105,
        (
            "#048F#2P呵呵，这样的话……\x01",
            "好像甜食比较好。\x02\x03",

            "累的时候\x01",
            "男人也会喜欢甜食的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #461
        0x10,
        (
            "#5P那就推荐\x01",
            "刚刚到货的巧克力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0x10,
        "#5P微苦的味道也很适合男性。\x02",
    )

    CloseMessageWindow()

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #463
        "#6P#15W\x07\x05巧克力的价格是每个200米拉。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    CloseMessageWindow()

    def lambda_7F7A():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7F7A)
    Sleep(100)

    def lambda_7F8D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7F8D)
    Sleep(100)

    def lambda_7FA0():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7FA0)
    Sleep(200)

    ChrTalk(    #464
        0x101,
        (
            "#1006F这么说，\x01",
            "３个就是６００米拉吧。\x02\x03",

            "话说奥利维尔\x01",
            "有没有乖乖巡逻…\x01",
            "真令人怀疑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0x105,
        (
            "#045F好啦好啦。\x02\x03",

            "#542F那么就怀着感谢的心情\x01",
            "大家一起付钱吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0x107,
        "#061F#6P好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #467
        0x103,
        (
            "#021F呵呵，偶尔\x01",
            "这样也不错。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【出１５０米拉】\x01",      # 0
            "【不出】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8151")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_80EF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8151")

    label("loc_80EF")


    ChrTalk(    #468
        0x10,
        "#5P给，谢谢惠顾！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #469
        "\x07\x00得到３个\x1F\xF7\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F7, 3)
    SubMira(150)

    label("loc_8151")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_822A")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #470
        0x103,
        (
            "#023F#2P哎呀……\x01",
            "钱不够吗？\x02\x03",

            "#025F没办法了。\x01",
            "我先垫着吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #471
        0x10,
        "#5P给，谢谢惠顾！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #472
        "\x07\x00得到３个\x1F\xF7\x03\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x3F7, 3)

    ChrTalk(    #473
        0x101,
        (
            "#1019F（呜……\x01",
            "总觉得挺内疚的。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_822A")

    OP_A2(0xA)
    OP_A2(0x181D)
    OP_A2(0x1885)
    OP_4B(0x10, 255)
    EventEnd(0x0)
    Return()

    # Function_23_7A36 end

    def Function_24_823A(): pass

    label("Function_24_823A")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_6D(160, 0, 117520, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 4410, 0, 109480, 0)
    SetChrPos(0x107, 4410, 0, 109480, 0)
    SetChrPos(0x103, 4410, 0, 109480, 0)
    SetChrPos(0x105, 4410, 0, 109480, 0)
    SetChrPos(0xA, 300, 0, 116600, 0)
    SetChrPos(0xE, 1600, 0, 116590, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xE, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)

    ChrTalk(    #474
        0x101,
        "#2P早～！\x02",
    )

    CloseMessageWindow()

    def lambda_832F():

        label("loc_832F")

        TurnDirection(0xA, 0x101, 400)
        OP_48()
        Jump("loc_832F")

    QueueWorkItem2(0xA, 1, lambda_832F)

    def lambda_8340():

        label("loc_8340")

        TurnDirection(0xE, 0x103, 400)
        OP_48()
        Jump("loc_8340")

    QueueWorkItem2(0xE, 1, lambda_8340)

    ChrTalk(    #475
        0x107,
        "#5P早安。\x02",
    )

    CloseMessageWindow()

    def lambda_8360():
        OP_6D(-150, 0, 116560, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8360)
    OP_43(0x101, 0x1, 0x0, 0x19)
    Sleep(700)
    OP_43(0x103, 0x1, 0x0, 0x1A)
    Sleep(700)
    OP_43(0x107, 0x1, 0x0, 0x1B)
    Sleep(700)
    OP_43(0x105, 0x1, 0x0, 0x1C)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x101, 0x2)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x107, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_44(0xA, 0x1)
    OP_44(0xE, 0x1)

    ChrTalk(    #476
        0x8,
        "#740F呀，早。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0xA,
        "#051F#5P哦，来了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #478
        0xE,
        "#070F#2P昨晚睡得好吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0x101,
        (
            "#1006F#6P啊，嗯。\x01",
            "完全消除疲劳了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0x103,
        (
            "#524F#6P谢谢你们俩了。\x02\x03",

            "夜晚的巡逻，\x01",
            "很辛苦吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #481
        0x107,
        (
            "#560F#6P那个那个。\x01",
            "你们…辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #482
        0xE,
        (
            "#071F#2P哪里，我们交班的时候\x01",
            "都稍微睡了一下，不要紧的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #483
        0xA,
        (
            "#051F#5P虽说有个家伙\x01",
            "现在还在旅馆呼呼大睡。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_859C")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇在旅店没看到奥利维尔】\x01",      # 0
            "【◇在旅店看到了奥利维尔】\x01",      # 1
            "【◇不变更】\x01",                    # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8590"),
        (1, "loc_8596"),
        (SWITCH_DEFAULT, "loc_859C"),
    )


    label("loc_8590")

    OP_A3(0x1886)
    Jump("loc_859C")

    label("loc_8596")

    OP_A2(0x1886)
    Jump("loc_859C")

    label("loc_859C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 6)), scpexpr(EXPR_END)), "loc_8611")

    ChrTalk(    #484
        0x105,
        "#542F#6P啊，是奥利维尔啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #485
        0x101,
        (
            "#1006F#6P刚才看到他\x01",
            "在旅馆里呼呼大睡呢。\x02\x03",

            "奥利维尔他\x01",
            "也参加了巡逻吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8662")

    label("loc_8611")


    ChrTalk(    #486
        0x105,
        (
            "#542F#6P啊……\x01",
            "是奥利维尔吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #487
        0x101,
        (
            "#1004F#6P咦，奥利维尔他也\x01",
            "参加了巡逻吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8662")


    ChrTalk(    #488
        0xE,
        (
            "#070F#2P哈哈，算是吧。\x02\x03",

            "虽说牢骚满腹，\x01",
            "该做的事还是做得好好的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #489
        0x103,
        (
            "#021F#6P呵呵，待会儿\x01",
            "得向他道谢才行。\x02\x03",

            "#022F说回来……\x01",
            "情况怎样了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0x8,
        (
            "#744F多亏进行巡逻了，\x01",
            "再没有昏睡的人出现。\x02\x03",

            "#742F只是，昨天昏睡的人\x01",
            "今天早上也没清醒。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0x101,
        "#1007F#6P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #492
        0x107,
        "#063F#6P真担心啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #493
        0x103,
        (
            "#022F#6P雾的情况怎样了？\x02\x03",

            "和昨天比…\x01",
            "感觉好像更浓了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #494
        0x8,
        (
            "#742F嗯嗯……\x01",
            "浓度好像上升了。\x02\x03",

            "与之相应\x01",
            "产生范围好像也扩大了。\x02\x03",

            "#744F直至玛鲁加山道尽头，\x01",
            "几乎整个地区都被笼罩在雾里了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #495
        0x101,
        "#1002F#6P这、这样啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #496
        0x105,
        (
            "#043F#6P看来情况\x01",
            "越来越严重了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #497
        0x8,
        (
            "#740F也不光是坏消息。\x02\x03",

            "接到我们的报告，\x01",
            "军队决定派遣部队了。\x02\x03",

            "为了警备洛连特市。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0x101,
        "#1018F#6P真的！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #499
        0x8,
        (
            "#741F嗯嗯，威尔特桥方面已经\x01",
            "派了两个小队来这边了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #500
        0x103,
        (
            "#021F#6P这真令人振奋。\x02\x03",

            "城市交给军队的话，\x01",
            "我们也能自由行动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #501
        0xA,
        (
            "#051F#5P啊啊，没错。\x02\x03",

            "必须赶快找到『结社』的\x01",
            "那些家伙并制服他们。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0xE,
        (
            "#074F#2P嗯，应该潜伏在\x01",
            "洛连特近郊吧……\x02\x03",

            "#072F不过现在还没有线索。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #503
        0x101,
        (
            "#1007F#6P洛连特地方虽小，\x01",
            "但也不可能调查到每一个角落……\x02\x03",

            "#1015F嗯……没什么\x01",
            "具体能做的事吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0x8,
        (
            "#740F话虽如此……\x02\x03",

            "首先协助\x01",
            "民众避难如何。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #505
        0x101,
        "#1004F#6P民众避难？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #506
        0x8,
        (
            "#744F昏睡事件在雾的产生范围内\x01",
            "再发生的可能性很高。\x02\x03",

            "#742F而今天早上，\x01",
            "这发生范围还更广了……\x02\x03",

            "连帕赛尔农场和玛鲁加矿山\x01",
            "都覆盖到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #507
        0x101,
        "#1020F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0x103,
        (
            "#026F#6P原来如此……\x02\x03",

            "#020F要保证农场一家\x01",
            "和矿工的安全吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0x8,
        (
            "#740F嗯嗯，这也是协会\x01",
            "肩负的义务啊。\x02\x03",

            "寻找敌人的所在处之前，\x01",
            "能先处理这件工作吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #510
        0xA,
        (
            "#053F#5P没办法……\x01",
            "看来这边优先啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0xE,
        (
            "#070F#2P矿山和农场\x01",
            "相隔好像比较远啊。\x02\x03",

            "既然如此，就这样\x01",
            "兵分两路比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #512
        0x103,
        "#027F#6P嗯嗯，这样比较有效率。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0x101,
        (
            "#1015F#6P那，那样的话…\x01",
            "我们去农场行不行？\x02\x03",

            "那是我朋友的家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #514
        0xE,
        (
            "#073F#2P哦，这样啊。\x02\x03",

            "#070F那么我们\x01",
            "去矿山吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #515
        0xA,
        (
            "#051F#5P啊啊，就这么定了。\x02\x03",

            "把奥利维尔那家伙叫起来，\x01",
            "赶快出发吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_22(0xBE, 0x0, 0x64)
    Sleep(2000)
    SetChrPos(0xB, 4250, 0, 108920, 0)

    NpcTalk(    #516
        0xB,
        "青年的声音",
        "#2P呵呵，叫我？\x02",
    )

    CloseMessageWindow()
    OP_9F(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 15)
    SetChrSubChip(0xB, 0)
    ClearChrFlags(0xB, 0x80)

    def lambda_8D96():
        OP_6D(2550, 0, 112570, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8D96)

    def lambda_8DAE():

        label("loc_8DAE")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_8DAE")

    QueueWorkItem2(0x101, 1, lambda_8DAE)
    Sleep(50)

    def lambda_8DC4():

        label("loc_8DC4")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_8DC4")

    QueueWorkItem2(0xA, 1, lambda_8DC4)
    Sleep(50)

    def lambda_8DDA():

        label("loc_8DDA")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_8DDA")

    QueueWorkItem2(0x103, 1, lambda_8DDA)
    Sleep(50)

    def lambda_8DF0():

        label("loc_8DF0")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_8DF0")

    QueueWorkItem2(0xE, 1, lambda_8DF0)
    Sleep(50)

    def lambda_8E06():

        label("loc_8E06")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_8E06")

    QueueWorkItem2(0x107, 1, lambda_8E06)
    Sleep(50)

    def lambda_8E1C():

        label("loc_8E1C")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_8E1C")

    QueueWorkItem2(0x105, 1, lambda_8E1C)
    Sleep(100)
    WaitChrThread(0x101, 0x0)
    OP_43(0xB, 0x1, 0x0, 0x1D)
    Sleep(500)

    def lambda_8E43():
        OP_6D(650, 0, 116600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8E43)
    WaitChrThread(0xB, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0x105, 0x1)
    OP_8C(0x103, 180, 0)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #517
        0xE,
        "#071F#2P哦哦，起来啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #518
        0x101,
        (
            "#1007F#5P干嘛还特地\x01",
            "弹琴……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #519
        0xB,
        (
            "#031F哈哈哈。\x01",
            "因为今早天气也很不好嘛。\x02\x03",

            "至少希望用我华丽的演奏\x01",
            "让气氛明快一点……\x02\x03",

            "就当是我这名音乐家\x01",
            "独特而美丽的演出吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #520
        0xA,
        (
            "#551F#5P真是的，一大早\x01",
            "情绪就这么高涨。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #521
        0x101,
        (
            "#1006F#5P不过，奥利维尔\x01",
            "似乎也认真巡逻了呢。\x02\x03",

            "对你有点改观了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0x103,
        (
            "#021F#2P呵呵，是啊。\x01",
            "辛苦你了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #523
        0xB,
        (
            "#031F哈哈哈。\x01",
            "作为绅士这是当然的义务啦。\x02\x03",

            "#030F原本打算在\x01",
            "巡逻的时候\x01",
            "去艾丝蒂尔家打扰的。\x02\x03",

            "#034F但是视线比想象中更差，\x01",
            "只好忍痛放弃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #524
        0x101,
        (
            "#1019F#5P真是的……\x01",
            "刚想改观就这样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #525
        0x8,
        (
            "#740F那么，向奥利维尔\x01",
            "简单说明情况吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(10, 0, 116530, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, -890, 0, 116590, 135)
    OP_8C(0x101, 0, 0)
    OP_8C(0x103, 0, 0)
    OP_8C(0x107, 0, 0)
    OP_8C(0x105, 0, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #526
        0xB,
        (
            "#033F#5P嗯，怎么说\x01",
            "这都是游击士协会的工作呢。\x02\x03",

            "#030F好吧。\x01",
            "我也来帮忙吧。\x02\x03",

            "#031F那么你们\x01",
            "带我去农场吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 400)

    ChrTalk(    #527
        0xA,
        (
            "#555F#6P都～说你是\x01",
            "和我们一起的～～\x02\x03",

            "你就是来故意捣乱的吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 400)

    ChrTalk(    #528
        0xB,
        (
            "#031F#5P讨厌啦，那么\x01",
            "想和我在一起啊。\x02\x03",

            "#037F阿加特兄真可爱㈱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #529
        0xA,
        "#055F#6P少恶心了！\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #530
        0x107,
        (
            "#065F#6P啊哇哇……\x01",
            "真是、是这样吗～！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x107, 400)

    ChrTalk(    #531
        0xA,
        (
            "#055F#5P啊～！\x01",
            "这你都相信啊～！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #532
        0x101,
        "#1007F#6P啊哈哈，感觉轻松了很多呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #533
        0x103,
        (
            "#021F#6P呵呵……\x01",
            "总比越来越沉重要好吧。\x02\x03",

            "#027F不过我们都还是\x01",
            "赶快完成工作比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #534
        0xA,
        "#551F#5P啊啊，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #535
        0xE,
        (
            "#070F#2P那么我们\x01",
            "就去矿山啦。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9411")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇没买巧克力】\x01",      # 0
            "【◇买了巧克力】\x01",      # 1
            "【◇不变更】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9405"),
        (1, "loc_940B"),
        (SWITCH_DEFAULT, "loc_9411"),
    )


    label("loc_9405")

    OP_A3(0x181D)
    Jump("loc_9411")

    label("loc_940B")

    OP_A2(0x181D)
    Jump("loc_9411")

    label("loc_9411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_949F")
    TurnDirection(0xB, 0x101, 400)
    Sleep(500)

    ChrTalk(    #536
        0xB,
        (
            "#031F#5P呼，暂时要分别了。\x01",
            "我可爱的小猫咪们。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_945E():

        label("loc_945E")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_945E")

    QueueWorkItem2(0x101, 1, lambda_945E)

    def lambda_946F():

        label("loc_946F")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_946F")

    QueueWorkItem2(0x103, 1, lambda_946F)

    def lambda_9480():

        label("loc_9480")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_9480")

    QueueWorkItem2(0x105, 1, lambda_9480)

    def lambda_9491():

        label("loc_9491")

        TurnDirection(0xFE, 0xB, 400)
        OP_48()
        Jump("loc_9491")

    QueueWorkItem2(0x107, 1, lambda_9491)
    Jump("loc_9A0C")

    label("loc_949F")


    ChrTalk(    #537
        0x107,
        (
            "#064F#6P啊……\x01",
            "姐姐，那些吃的啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(800)
    TurnDirection(0x101, 0x107, 400)

    def lambda_94EA():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_94EA)

    def lambda_94F8():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_94F8)

    def lambda_9506():
        TurnDirection(0xFE, 0x107, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_9506)

    ChrTalk(    #538
        0x101,
        "#1006F#5P啊，是哦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #539
        0xA,
        "#052F#5P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #540
        0xE,
        "#073F#2P怎么了？\x02",
    )

    CloseMessageWindow()
    OP_8F(0x101, 0x2C6, 0x0, 0x1BF44, 0x5DC, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #541
        "\x07\x05艾丝蒂尔把巧克力的包包递给提妲。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x3F7, 3)

    ChrTalk(    #542
        0x101,
        (
            "#1001F#5P快快。\x01",
            "发起人来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #543
        0x107,
        "#560F#6P嗯、嗯。\x02",
    )

    CloseMessageWindow()

    def lambda_95FC():
        OP_8F(0xFE, 0xFFFFFEAC, 0x0, 0x1C05C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_95FC)

    def lambda_9617():
        OP_8C(0xFE, 90, 200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9617)
    Sleep(500)

    def lambda_962A():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_962A)

    def lambda_9638():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9638)

    def lambda_9646():
        OP_8F(0xFE, 0x1D6, 0x0, 0x1C1C4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9646)
    WaitChrThread(0x101, 0x1)

    def lambda_9666():
        OP_8C(0xFE, 0, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9666)
    WaitChrThread(0x107, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x105, 0x1)
    Sleep(500)

    ChrTalk(    #544
        0x107,
        (
            "#560F#6P阿加特哥哥、\x01",
            "金先生、奥利维尔先生。\x02\x03",

            "昨天真是\x01",
            "辛苦你们了。\x02\x03",

            "#061F那个那个……\x01",
            "这个，是慰劳品。\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x107, 0x1D6, 0x0, 0x1C43A, 0x5DC, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #545
        "\x07\x05提妲把黑巧克力交给了阿加特等人。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    def lambda_975E():
        OP_8F(0xFE, 0x1D6, 0x0, 0x1C2C8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_975E)
    Sleep(500)

    ChrTalk(    #546
        0xA,
        "#055F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #547
        0xB,
        "#033F#5P哦哦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #548
        0xE,
        "#073F#2P呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #549
        0x103,
        "#021F#6P呵呵，一点小意思。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #550
        0x105,
        (
            "#048F#6P钱也是大家\x01",
            "一起出的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #551
        0x101,
        (
            "#1006F#6P嗯，你们可要\x01",
            "好好品尝哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #552
        0xE,
        (
            "#071F#2P呀，疲劳的时候\x01",
            "收到甜食做慰劳真令人高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #553
        0xB,
        (
            "#031F#5P呵，你们甜美的爱，\x01",
            "我就收下了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #554
        0xA,
        "#555F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #555
        0x107,
        "#065F#6P啊，阿加特哥哥……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #556
        0x105,
        (
            "#043F#6P难不成\x01",
            "你不喜欢吃甜食？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #557
        0xA,
        (
            "#552F#5P不……\x01",
            "不至于不喜欢。\x02\x03",

            "#551F倒是你们……\x01",
            "还做这么让人难为情的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #558
        0x101,
        "#1001F#6P啊哈哈，害羞啦。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #559
        0x103,
        "#027F#6P修行还不够呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #560
        0xA,
        (
            "#055F#5P啰嗦。\x02\x03",

            "#051F算了，肚子饿了\x01",
            "我就随便吃吃了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #561
        0x107,
        "#067F#6P好。\x02",
    )

    CloseMessageWindow()

    def lambda_99CE():

        label("loc_99CE")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_99CE")

    QueueWorkItem2(0x101, 1, lambda_99CE)

    def lambda_99DF():

        label("loc_99DF")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_99DF")

    QueueWorkItem2(0x103, 1, lambda_99DF)

    def lambda_99F0():

        label("loc_99F0")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_99F0")

    QueueWorkItem2(0x105, 1, lambda_99F0)

    def lambda_9A01():

        label("loc_9A01")

        TurnDirection(0xFE, 0xA, 400)
        OP_48()
        Jump("loc_9A01")

    QueueWorkItem2(0x107, 1, lambda_9A01)

    label("loc_9A0C")


    def lambda_9A12():
        OP_6D(2550, 0, 112570, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9A12)
    OP_43(0xE, 0x1, 0x0, 0x1E)
    Sleep(100)
    OP_43(0xA, 0x1, 0x0, 0x1F)
    Sleep(700)
    OP_43(0xB, 0x1, 0x0, 0x20)
    WaitChrThread(0xB, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x107, 0x1)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 5)), scpexpr(EXPR_END)), "loc_9BCE")

    def lambda_9A6F():
        OP_6D(-530, 0, 115950, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9A6F)
    Sleep(500)
    TurnDirection(0x101, 0x103, 400)

    def lambda_9A93():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9A93)
    Sleep(50)

    def lambda_9AA6():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9AA6)
    Sleep(50)

    def lambda_9AB9():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9AB9)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #562
        0x101,
        (
            "#1006F#5P好了，我们\x01",
            "也向帕赛尔农场出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #563
        0x105,
        "#041F嗯嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #564
        0x107,
        (
            "#560F#2P嗯，是姐姐的\x01",
            "朋友家对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #565
        0x101,
        (
            "#1011F#5P嗯，叫缇欧～\x01",
            "是主日学校时代的好友。\x02\x03",

            "还有叔叔、阿姨、\x01",
            "双胞胎姐弟总共５人的家族吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #566
        0x103,
        (
            "#026F护卫对象中还有小孩，\x01",
            "看来这工作不可大意了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D30")

    label("loc_9BCE")


    def lambda_9BD4():
        OP_6D(-530, 0, 115950, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9BD4)
    Sleep(500)
    TurnDirection(0x101, 0x105, 400)

    def lambda_9BF8():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9BF8)
    Sleep(50)

    def lambda_9C0B():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9C0B)
    Sleep(50)

    def lambda_9C1E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9C1E)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #567
        0x101,
        (
            "#1006F#5P好了，我们\x01",
            "也向帕赛尔农场出发吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #568
        0x105,
        "#041F嗯嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #569
        0x107,
        (
            "#560F#6P嗯，是姐姐的\x01",
            "朋友家对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #570
        0x101,
        (
            "#1011F#5P嗯，叫缇欧～\x01",
            "是主日学校时代的好友。\x02\x03",

            "还有叔叔、阿姨、\x01",
            "双胞胎姐弟总共５人的家族吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #571
        0x103,
        (
            "#026F护卫对象中还有小孩，\x01",
            "看来这工作不可大意了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D30")

    TurnDirection(0x103, 0x8, 400)

    def lambda_9D3D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9D3D)

    def lambda_9D4B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9D4B)

    def lambda_9D59():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9D59)

    ChrTalk(    #572
        0x103,
        (
            "#020F#6P那么爱娜。\x01",
            "我们也走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #573
        0x8,
        "#741F#2P嗯嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x181E)
    OP_28(0x91, 0x4, 0x2)
    OP_28(0x91, 0x4, 0x8)
    OP_28(0x91, 0x1, 0x1)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_24_823A end

    def Function_25_9DBC(): pass

    label("Function_25_9DBC")

    OP_8E(0xFE, 0x2C6, 0x0, 0x1C138, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_25_9DBC end

    def Function_26_9DD8(): pass

    label("Function_26_9DD8")

    OP_8E(0xFE, 0x9EC, 0x0, 0x1B7A6, 0x9C4, 0x0)
    OP_8E(0xFE, 0x730, 0x0, 0x1C138, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_26_9DD8 end

    def Function_27_9E08(): pass

    label("Function_27_9E08")

    OP_8E(0xFE, 0x2E4, 0x0, 0x1BC88, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_27_9E08 end

    def Function_28_9E24(): pass

    label("Function_28_9E24")

    OP_22(0x7, 0x0, 0x64)
    OP_8E(0xFE, 0x9EC, 0x0, 0x1B7A6, 0x9C4, 0x0)
    OP_8E(0xFE, 0x730, 0x0, 0x1BC88, 0x9C4, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_28_9E24 end

    def Function_29_9E59(): pass

    label("Function_29_9E59")


    def lambda_9E5F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9E5F)
    OP_8E(0xFE, 0xF50, 0x0, 0x1AFD6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x636, 0x0, 0x1B738, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    SetChrSubChip(0x101, 0)
    Return()

    # Function_29_9E59 end

    def Function_30_9EA0(): pass

    label("Function_30_9EA0")

    OP_8E(0xFE, 0xA8C, 0x0, 0x1C6E2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA3C, 0x0, 0x1B45E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF78, 0x0, 0x1AD1A, 0x7D0, 0x0)

    def lambda_9EE2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9EE2)
    OP_8E(0xFE, 0x104A, 0x0, 0x1A7DE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_30_9EA0 end

    def Function_31_9F08(): pass

    label("Function_31_9F08")

    OP_8E(0xFE, 0xA8C, 0x0, 0x1C6E2, 0x7D0, 0x0)
    OP_8E(0xFE, 0xA3C, 0x0, 0x1B45E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF78, 0x0, 0x1AD1A, 0x7D0, 0x0)

    def lambda_9F4A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9F4A)
    OP_8E(0xFE, 0x104A, 0x0, 0x1A7DE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_31_9F08 end

    def Function_32_9F70(): pass

    label("Function_32_9F70")

    OP_8E(0xFE, 0xFFFFFC36, 0x0, 0x1BE0E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF50, 0x0, 0x1AFD6, 0x7D0, 0x0)
    OP_8E(0xFE, 0xF78, 0x0, 0x1AD1A, 0x7D0, 0x0)

    def lambda_9FB2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9FB2)
    OP_8E(0xFE, 0x104A, 0x0, 0x1A7DE, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_32_9F70 end

    def Function_33_9FD8(): pass

    label("Function_33_9FD8")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    OP_20(0x1F4)
    OP_6D(160, 0, 117520, 0)
    OP_67(0, 6400, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, 4410, 0, 109480, 0)
    SetChrPos(0x107, 4410, 0, 109480, 0)
    SetChrPos(0x103, 4410, 0, 109480, 0)
    SetChrPos(0x105, 4410, 0, 109480, 0)
    SetChrPos(0xB, -700, 0, 116590, 45)
    SetChrPos(0xA, 500, 0, 116600, 0)
    SetChrPos(0xE, 1800, 0, 116590, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)
    Sleep(500)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xE, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A114():

        label("loc_A114")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_A114")

    QueueWorkItem2(0xA, 1, lambda_A114)

    def lambda_A125():

        label("loc_A125")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_A125")

    QueueWorkItem2(0xE, 1, lambda_A125)

    def lambda_A136():

        label("loc_A136")

        TurnDirection(0xFE, 0x103, 400)
        OP_48()
        Jump("loc_A136")

    QueueWorkItem2(0xB, 1, lambda_A136)

    def lambda_A147():
        OP_6D(-150, 0, 116560, 2500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A147)
    OP_43(0x101, 0x1, 0x0, 0x22)
    OP_43(0x103, 0x1, 0x0, 0x23)
    OP_43(0x107, 0x1, 0x0, 0x24)
    OP_43(0x105, 0x1, 0x0, 0x25)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x101, 0x2)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x107, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_44(0xA, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0xB, 0x1)

    ChrTalk(    #574
        0xA,
        "#051F#5P哦，终于回来了吗。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #575
        0xE,
        (
            "#073F#2P怎样？\x01",
            "怎么这么晚啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #576
        0x103,
        "#025F#6P嗯嗯，发生了不少事。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #577
        0x101,
        (
            "#1015F#6P阿加特你们\x01",
            "已经去过矿山了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #578
        0xA,
        (
            "#051F#5P啊啊，早就\x01",
            "回来了。\x02\x03",

            "出发得快，\x01",
            "所以意外地回来得早。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #579
        0xE,
        (
            "#074F#2P不过，回来途中\x01",
            "出现了奇怪的魔兽。\x02\x03",

            "现在就正在说这事呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #580
        0x101,
        "#1004F#6P奇怪的魔兽？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x21)
    Sleep(400)

    ChrTalk(    #581
        0xB,
        (
            "#032F#5P出现在雾中\x01",
            "被打倒后就会消失的魔兽啊。\x02\x03",

            "该称为『雾魔』吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #582
        0x101,
        "#1020F#6P那、那是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #583
        0x105,
        "#042F#6P和那个魔兽一样呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #584
        0xA,
        (
            "#052F#5P怎么，你们那儿\x01",
            "也出现了吗……\x02\x03",

            "没受伤吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #585
        0x107,
        (
            "#063F#6P嗯，我们\x01",
            "倒是不要紧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #586
        0x101,
        "#1003F#6P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #587
        0xA,
        "#555F#5P？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #588
        0x8,
        (
            "#742F好像发生了什么事呢。\x02\x03",

            "能报告一下吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #589
        0x103,
        "#022F#6P嗯嗯，其实……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #590
        "\x07\x05把在农场发生的事情报告了一遍。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #591
        0x8,
        (
            "#745F是吗……\x01",
            "看来晚了一步呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #592
        0x103,
        (
            "#522F#6P……是我的失误。\x02\x03",

            "要是做得再好些，\x01",
            "就能捉住犯人了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #593
        0x101,
        (
            "#1003F#6P不……\x01",
            "完全不是雪拉姐的错。\x02\x03",

            "错的是关键时刻\x01",
            "却动弹不得的我。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #594
        0x8,
        (
            "#742F别介意。\x02\x03",

            "看来你们\x01",
            "是被人设了陷阱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #595
        0x101,
        "#1004F#6P陷、陷阱！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #596
        0xE,
        (
            "#074F#2P进入农场同时\x01",
            "听到的铃声……\x02\x03",

            "埋伏的雾之魔兽，\x01",
            "还有上锁的正门……\x02\x03",

            "#072F差之毫厘的时机\x01",
            "让你们没赶上，\x01",
            "感觉就像被算计了一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #597
        0x101,
        "#1020F#6P不，不只是偶然吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #598
        0xB,
        (
            "#032F#5P不，经过对昏睡事件的思考，\x01",
            "『黑衣女人』行事相当的巧妙。\x02\x03",

            "特地抢先让\x01",
            "你们保护的人睡着……\x02\x03",

            "#035F呵呵，说不定\x01",
            "这是她对你们的挑衅呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #599
        0x101,
        (
            "#1015F#6P嗯、嗯……\x02\x03",

            "只知道是『黑衣女人』，\x01",
            "其实也完全没有线索……\x02\x03",

            "也没有实际被挑衅的印象。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #600
        0x103,
        "#522F#6P……………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)
    Sleep(1000)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, 4250, 0, 108920, 0)
    ClearChrFlags(0x11, 0x80)
    OP_4A(0x11, 255)

    NpcTalk(    #601
        0x11,
        "青年的声音",
        "#2P呼，我回来了。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_62(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_62(0x107, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_62(0xE, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(10)
    OP_62(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A846():
        OP_6D(2550, 0, 112570, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A846)
    Sleep(50)

    def lambda_A863():

        label("loc_A863")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_A863")

    QueueWorkItem2(0x101, 1, lambda_A863)
    Sleep(50)

    def lambda_A879():

        label("loc_A879")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_A879")

    QueueWorkItem2(0x103, 1, lambda_A879)
    Sleep(50)

    def lambda_A88F():

        label("loc_A88F")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_A88F")

    QueueWorkItem2(0x105, 1, lambda_A88F)
    Sleep(50)

    def lambda_A8A5():

        label("loc_A8A5")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_A8A5")

    QueueWorkItem2(0x107, 1, lambda_A8A5)
    Sleep(50)

    def lambda_A8BB():

        label("loc_A8BB")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_A8BB")

    QueueWorkItem2(0xA, 1, lambda_A8BB)
    Sleep(50)

    def lambda_A8D1():

        label("loc_A8D1")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_A8D1")

    QueueWorkItem2(0xB, 1, lambda_A8D1)
    Sleep(50)

    def lambda_A8E7():

        label("loc_A8E7")

        TurnDirection(0xFE, 0x11, 400)
        OP_48()
        Jump("loc_A8E7")

    QueueWorkItem2(0xE, 1, lambda_A8E7)
    WaitChrThread(0x101, 0x0)
    OP_43(0x11, 0x1, 0x0, 0x26)
    Sleep(500)

    def lambda_A909():
        OP_6D(650, 0, 116600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A909)
    WaitChrThread(0x11, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x103, 0x1)
    OP_44(0x105, 0x1)
    OP_44(0x107, 0x1)
    OP_44(0xA, 0x1)
    OP_44(0xB, 0x1)
    OP_44(0xE, 0x1)
    OP_44(0x8, 0x1)
    WaitChrThread(0x101, 0x0)

    ChrTalk(    #602
        0x101,
        "#1004F#5P咦，利吉先生？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #603
        0x103,
        (
            "#020F#2P说起来你是为了护卫工作\x01",
            "去了王都吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #604
        0x11,
        (
            "#6P嗯嗯，一早去了那边\x01",
            "终于回来了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #605
        0x11,
        (
            "#6P话说回来……\x01",
            "到底发生了什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #606
        0x11,
        (
            "#6P雾蔓延的范围也扩大了…\x01",
            "士兵在城里巡逻的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #607
        0x8,
        (
            "#742F其实昨天傍晚时分\x01",
            "发生了很多严重的事情。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #608
        (
            "\x07\x05把昨天到今天的事情\x01",
            "概括地向利吉说明了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #609
        0x11,
        (
            "#6P哇……\x01",
            "竟然有这种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #610
        0x11,
        "#6P我出去的真不是时候。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #611
        0x101,
        (
            "#1006F#5P哪里，别在意。\x02\x03",

            "既然定期船停了，\x01",
            "护卫也是十分重要的工作。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #612
        0x103,
        (
            "#027F#2P因为我们都没有\x01",
            "余力来承担这些工作。\x02\x03",

            "有你帮忙真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #613
        0x11,
        "#6P非，非常荣幸。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #614
        0x11,
        (
            "#6P这么说来……\x01",
            "关于那个『铃声』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #615
        0x11,
        (
            "#6P那是从雾的某处\x01",
            "传来的对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #616
        0x103,
        "#025F#2P嗯嗯，是啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #617
        0x101,
        (
            "#1007F#5P虽然还不清楚\x01",
            "为什么会出现铃声。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #618
        0x11,
        "#6P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #619
        0x103,
        "#023F#2P有什么线索吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #620
        0x11,
        (
            "#6P刚才通过\x01",
            "艾利兹街道的时候……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #621
        0x11,
        "#6P好像听到了微弱的铃声。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(10)
    OP_62(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #622
        0x101,
        "#1005F#5P你、你说什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #623
        0x103,
        (
            "#024F#2P大概在\x01",
            "艾利兹街道哪里听到的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #624
        0x11,
        "#6P唔，嗯……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #625
        0x11,
        (
            "#6P从格鲁纳门刚出来\x01",
            "就听到了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #626
        0x11,
        "#6P应该是从神秘森林那边传来的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #627
        0x103,
        "#022F#2P神秘森林……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #628
        0xE,
        (
            "#072F#2P记得是洛连特地区\x01",
            "东南方的森林吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #629
        0x11,
        (
            "#6P一开始还以为有人在，\x01",
            "就向发出声音的方向\x01",
            "大声喊了一下看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #630
        0x11,
        (
            "#6P但是没有任何回声，\x01",
            "想来是我的错觉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #631
        0xB,
        (
            "#032F#5P唔……\x02\x03",

            "很可能就是希望引起我们注意，\x01",
            "而特地鸣响的呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #632
        0x105,
        "#042F#5P这算是……挑衅吗～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #633
        0xA,
        "#057F#5P哼，真是看不起人……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #634
        0x101,
        "#1002F#5P……………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #635
        0x101,
        "#1002F#5P雪拉姐……怎么办～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #636
        0x103,
        "#026F#2P是啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    Sleep(500)

    ChrTalk(    #637
        0x103,
        (
            "#022F#4P虽然很可能是圈套，\x01",
            "但也只能往里跳了。\x02\x03",

            "就应邀拜访吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x11, 0x80)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #638
        (
            "\x07\x05※进行队伍的重新编组。\x01",
            "　请选择２名固定成员以外的同行者。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(100)
    OP_6D(17370, 0, 123310, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 255)
    OP_A2(0x1823)
    OP_28(0x92, 0x4, 0x2)
    OP_28(0x92, 0x4, 0x8)
    OP_28(0x92, 0x1, 0x1)
    OP_20(0x7D0)
    OP_21()
    Sleep(500)
    OP_6D(1370, 0, 113410, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 1370, 0, 113410, 180)
    SetChrPos(0x1, 1370, 0, 113410, 180)
    SetChrPos(0x2, 1370, 0, 113410, 180)
    SetChrPos(0x3, 1370, 0, 113410, 180)
    OP_69(0x0, 0x0)
    OP_1D(0xA)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_33_9FD8 end

    def Function_34_B1A2(): pass

    label("Function_34_B1A2")

    OP_8E(0xFE, 0x2C6, 0x0, 0x1C138, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_34_B1A2 end

    def Function_35_B1BE(): pass

    label("Function_35_B1BE")

    Sleep(500)
    OP_8E(0xFE, 0x9EC, 0x0, 0x1B7A6, 0xBB8, 0x0)
    OP_8E(0xFE, 0x730, 0x0, 0x1C138, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_35_B1BE end

    def Function_36_B1F3(): pass

    label("Function_36_B1F3")

    Sleep(500)
    Sleep(500)
    OP_8E(0xFE, 0x2E4, 0x0, 0x1BC88, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_36_B1F3 end

    def Function_37_B219(): pass

    label("Function_37_B219")

    Sleep(500)
    Sleep(500)
    Sleep(500)

    def lambda_B22E():
        OP_8E(0xFE, 0x9EC, 0x0, 0x1B7A6, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_B22E)
    Sleep(300)
    OP_22(0x7, 0x0, 0x64)
    WaitChrThread(0x105, 0x3)
    OP_8E(0xFE, 0x730, 0x0, 0x1BC88, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_37_B219 end

    def Function_38_B26E(): pass

    label("Function_38_B26E")


    def lambda_B274():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B274)
    OP_8E(0xFE, 0xF50, 0x0, 0x1AFD6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x636, 0x0, 0x1B738, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_38_B26E end

    def Function_39_B2B0(): pass

    label("Function_39_B2B0")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2D0")
    Call(0, 42)
    FadeToBright(0, 0)
    Call(0, 43)

    label("loc_B2D0")

    Call(0, 40)
    OP_4A(0x8, 255)
    OP_6D(400, 0, 117350, 0)
    OP_67(0, 6220, -10000, 0)
    OP_6B(2820, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 610, 0, 116590, 0)
    SetChrPos(0x103, 1630, 0, 116600, 0)
    SetChrPos(0x107, 1490, 0, 115380, 0)
    SetChrPos(0x105, -10, 0, 115840, 0)
    SetChrPos(0x108, 980, 0, 114460, 0)
    SetChrPos(0x104, 2630, 0, 114990, 0)
    SetChrPos(0x106, -240, 0, 114330, 0)
    ClearMapFlags(0x2000000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #639
        0x8,
        (
            "#744F是吗……\x01",
            "竟然有这种事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #640
        0x103,
        (
            "#522F#6P对不起，爱娜。\x02\x03",

            "如果我早点将心里的想法\x01",
            "告诉你就好了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #641
        0x8,
        (
            "#740F呵呵，不用在意的。\x02\x03",

            "就算当时知道了她是你的旧识，\x01",
            "也一样做不了什么啊。\x02\x03",

            "#741F想道歉的话，下次请我喝酒就可以了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #642
        0x103,
        "#021F#6P哈哈～那是小事一桩。\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #643
        0x101,
        (
            "#1016F#6P厄…这两个人一起喝酒的话……\x01",
            "怎么想也不可能是『小事』啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_9E(0x104, 0xF, 0x0, 0x12C, 0xFA0)
    Sleep(500)

    ChrTalk(    #644
        0x104,
        "#034F呜啊啊啊（发抖）……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #645
        0x8,
        (
            "#740F雾散天晴，\x01",
            "昏睡的人们也从梦中醒了过来。\x02\x03",

            "#741F大家辛苦了。\x02\x03",

            "这次的任务一共有好几个，\x01",
            "报酬合在一起支付给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x90, 0x4, 0x10)
    OP_AF(0x3, 0x90)
    Sleep(100)
    OP_28(0x91, 0x4, 0x10)
    OP_AF(0x3, 0x91)
    Sleep(100)
    OP_28(0x92, 0x4, 0x10)
    OP_AF(0x3, 0x92)
    Sleep(100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)

    ChrTalk(    #646
        0x101,
        (
            "#1007F#6P不过，这次的问题\x01",
            "也没有得到根本的解决。\x02\x03",

            "『福音』已经\x01",
            "影响到了人的精神。\x02\x03",

            "#1015F看来凭现今的技术力\x01",
            "还无法解释这个现象啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #647
        0x107,
        (
            "#063F#6P嗯，是的……\x01",
            "这是目前为止最难以解释的事件。\x02\x03",

            "等等要把报告书\x01",
            "给爷爷传过去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #648
        0x106,
        (
            "#053F看来『福音』的秘密\x01",
            "只能等老爷子来分析了。\x02\x03",

            "#050F更重要的是，总算能看清了一些\x01",
            "『结社』的势力结构。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #649
        0x108,
        (
            "#074F嗯，结合这次的事件……\x02\x03",

            "#072F一共已经有５名『执行者』\x01",
            "的身份可以确定了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #650
        0x8,
        "#744F是啊……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x6E)
    Sleep(500)
    OP_AD(0x240089, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("爱娜")

    AnonymousTalk(    #651
        (
            "\x07\x00#742FＮＯ．Ⅹ。\x01",
            "『怪盗绅士』布卢布兰。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24008A, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("爱娜")

    AnonymousTalk(    #652
        (
            "#742FＮＯ．Ⅷ。\x01",
            "『瘦狼』瓦鲁特。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x2400D5, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("爱娜")

    AnonymousTalk(    #653
        (
            "#742FＮＯ．ⅩⅤ。\x01",
            "『歼灭天使』玲。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24008C, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("爱娜")

    AnonymousTalk(    #654
        (
            "#742FＮＯ．Ⅵ。\x01",
            "『幻惑之铃』露茜奥拉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24008D, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("爱娜")

    AnonymousTalk(    #655
        (
            "#742FＮＯ．０。\x01",
            "『小丑』肯帕雷拉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    OP_AD(0x24008E, 0x0, 0x0, 0x1F4)
    Sleep(1000)
    SetChrName("爱娜")

    AnonymousTalk(    #656
        (
            "#744F然后，除了这５个人之外，\x01",
            "另外还有『教授』和『莱维』\x01",
            "这两个尚未确认的人物。\x02\x03",

            "#742F或许其中的某一个\x01",
            "就是洛伦斯少尉。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 280, -1, -1)
    OP_61(0x101)

    AnonymousTalk(    #657
        (
            "#1003F嗯……\x01",
            "这个可能性应该不低。\x02\x03",

            "两个人可能都是\x01",
            "我认识的人……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 320, -1, -1)
    OP_61(0x105)

    AnonymousTalk(    #658
        (
            "#043F确实，洛伦斯那个名字\x01",
            "也有可能是假的名字。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(1000, 0)
    OP_AE(0x1F4)
    Sleep(1500)
    OP_0D()

    ChrTalk(    #659
        0x106,
        (
            "#555F但是，仅仅只有７个人\x01",
            "就干出了这番事情。\x02\x03",

            "真是一帮令人头痛的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #660
        0x103,
        (
            "#026F#6P是啊……\x02\x03",

            "#022F看来，我们也应该\x01",
            "更小心行事了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #661
        0x101,
        "#1026F#5P雪拉姐……这样行吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #662
        0x103,
        (
            "#524F#4P呵呵，我不是已经说过了吗？\x01",
            "利贝尔就是我新的故乡。\x02\x03",

            "保护自己的故乡难道还需要任何理由吗？\x02\x03",

            "就算是和曾经的回忆产生冲突，\x01",
            "我也绝对不会……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #663
        0x101,
        "#1026F#5P雪拉姐……\x02",
    )

    CloseMessageWindow()
    OP_62(0x108, 0x0, 2300, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x108)
    Sleep(500)

    ChrTalk(    #664
        0x108,
        (
            "#070F我说，雪拉扎德。\x02\x03",

            "我认为你并没有必要这么早\x01",
            "就下定这种决心。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x103, 0x108, 400)

    ChrTalk(    #665
        0x103,
        "#023F#2P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #666
        0x108,
        (
            "#074F我和瓦鲁特之间的战斗\x01",
            "早已经是注定无可避免的了。\x02\x03",

            "因为我和他之间除了拳头之外，\x01",
            "再没有更好的交流方式。\x02\x03",

            "#070F但你们之间的关系\x01",
            "却未必到了这种程度吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #667
        0x103,
        "#522F#2P这个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #668
        0x101,
        (
            "#1006F#5P我认为金先生说的没错。\x02\x03",

            "雪拉姐不必太早下定论，今后该怎么做，\x01",
            "从现在开始慢慢考虑就可以了。\x02\x03",

            "我也是……\x01",
            "好不容易才想通的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #669
        0x103,
        "#023F啊#4P……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)
    Sleep(500)

    ChrTalk(    #670
        0x101,
        (
            "#1011F#2P对了，各位。\x02\x03",

            "虽然现在状况不大好……不过\x01",
            "还是有样东西希望大家看看。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BE37():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_BE37)
    Sleep(100)
    TurnDirection(0xF9, 0x101, 400)

    ChrTalk(    #671
        0x106,
        "#052F啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #672
        0x105,
        "#044F#6P艾丝蒂尔……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #673
        0x103,
        "#023F#4P艾丝蒂尔，难道你……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #674
        0x101,
        (
            "#1012F#2P嗯……\x02\x03",

            "#1025F这是从杂志社那里\x01",
            "拿到的照片……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x5DC)
    Fade(250)
    SetChrChipByIndex(0x101, 17)
    SetChrSubChip(0x101, 0)
    OP_0D()
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #675
        "\x07\x05给大家看朵洛希拍摄的照片。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AD(0x240091, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(100, 280, -1, -1)
    OP_61(0x106)

    AnonymousTalk(    #676
        (
            "\x07\x00#555F这不是……\x01",
            "抢夺空贼艇事件的照片吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 320, -1, -1)
    OP_61(0x104)

    AnonymousTalk(    #677
        (
            "#033F原来如此……\x01",
            "还真是有这样的东西啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(300, 280, -1, -1)
    OP_61(0x108)

    AnonymousTalk(    #678
        (
            "#073F嗯，在左边的\x01",
            "是出席了武术大会\x01",
            "空贼团的女孩。\x02\x03",

            "……右面的那个……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 280, -1, -1)
    OP_61(0x105)

    AnonymousTalk(    #679
        "#043F#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 320, -1, -1)
    OP_61(0x107)

    AnonymousTalk(    #680
        "#065F#6P约、约修亚哥哥！？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x3E8)
    OP_21()
    OP_AE(0xC8)
    Sleep(1500)
    Fade(250)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_1D(0x1)
    Sleep(500)

    ChrTalk(    #681
        0x101,
        (
            "#1007F#2P嗯……\x01",
            "对不起，一直没有和大家说起。\x02\x03",

            "#1003F那时候很迷惑，\x01",
            "不知道怎么说出来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #682
        0x107,
        "#063F#6P姐姐……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #683
        0x105,
        "#043F#6P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #684
        0x101,
        (
            "#1002F#2P约修亚想做什么\x01",
            "我不是很清楚……不过\x02\x03",

            "我猜，约修亚一定是想用自己的方法\x01",
            "来接近『结社』。\x02\x03",

            "就算和空贼们在一起\x01",
            "并不意味肯定做了什么坏事……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #685
        0x8,
        (
            "#744F是啊，我们都明白的。\x02\x03",

            "#740F照片也只照下了一半的脸，\x01",
            "还不能成为决定性的证据。\x02\x03",

            "这个情报就在协会内部\x01",
            "留存就好，不要再传播了。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #686
        0x101,
        "#1017F#6P谢谢，爱娜姐。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #687
        0x105,
        (
            "#043F#6P但，但是……\x01",
            "艾丝蒂尔，难道就如此罢休了吗？\x02\x03",

            "好不容易找到了约修亚的\x01",
            "一点点线索……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #688
        0x101,
        (
            "#1012F#2P嗯……\x02\x03",

            "#1006F只要我还是我，\x01",
            "和约修亚之间的缘分便不会就此断掉的。\x02\x03",

            "只要这么一想的话，\x01",
            "就不会太过焦急了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #689
        0x105,
        "#044F#6P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #690
        0x101,
        (
            "#1006F#2P虽然行走的道路不同，\x01",
            "肯定最终的目标是相同的。\x02\x03",

            "#1012F所以现在……\x01",
            "我想走我自己的路。\x02\x03",

            "不这样的话，\x01",
            "我就不能变坚强。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #691
        0x105,
        "#542F#6P艾丝蒂尔……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #692
        0x101,
        (
            "#1008F#2P哈哈……\x01",
            "多少还是有点好面子，所以……\x02\x03",

            "约修亚和那个男人婆之间的关系，\x01",
            "我还是十分在意哟。\x02\x03",

            "#1007F这就是修行还远远不足的证据。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #693
        0x105,
        (
            "#045F#6P呵呵……\x01",
            "艾丝蒂尔。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #694
        0x103,
        (
            "#021F#4P呵呵，不是已经找到了\x01",
            "想要的答案了吗？\x02\x03",

            "#027F看来，在森林中看到的梦…\x01",
            "好像正朝好的方向发展了嘛？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Sleep(500)

    ChrTalk(    #695
        0x101,
        (
            "#1017F#5P嗯……\x02\x03",

            "我再次深深的感觉到\x01",
            "与约修亚之间的羁绊。\x02\x03",

            "也能够感觉到\x01",
            "妈妈的那种温馨。\x02\x03",

            "#1001F别的不说，单是这次的事件\x01",
            "就应该感谢『福音』。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #696
        0x107,
        "#061F#6P呵呵，姐姐真是的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #697
        0x106,
        (
            "#051F真是的……\x01",
            "你还真是想得开。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #698
        0x104,
        (
            "#031F呵，在艾丝蒂尔面前\x01",
            "『福音』也变得一点不可怕了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Call(0, 41)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C636")
    OP_A2(0x183C)

    label("loc_C636")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C647")
    OP_A2(0x183D)

    label("loc_C647")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C658")
    OP_A2(0x183E)

    label("loc_C658")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C669")
    OP_A2(0x183F)

    label("loc_C669")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C67A")
    OP_A2(0x1840)

    label("loc_C67A")

    OP_AD(0x2400B1, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_A2(0x1843)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x126), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6D(100000, -100000, 100000, 0)
    FadeToBright(0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        240,
        180,
        0,
        (
            "【保存进度】\x01",        # 0
            "【进入下一章】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6F6")
    ShowSaveMenu()

    label("loc_C6F6")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_AE(0xC8)
    Sleep(2000)
    OP_A3(0x1843)
    OP_4F(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C0705   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_39_B2B0 end

    def Function_40_C72C(): pass

    label("Function_40_C72C")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C765")
    AddParty(0x7, 0xFA, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C765")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C79E")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C786")
    AddParty(0x4, 0xFA, 0xFF)
    Jump("loc_C78A")

    label("loc_C786")

    AddParty(0x4, 0xFB, 0xFF)

    label("loc_C78A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C79E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C7EB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7BF")
    AddParty(0x3, 0xFA, 0xFF)
    Jump("loc_C7D7")

    label("loc_C7BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C7D3")
    AddParty(0x3, 0xFB, 0xFF)
    Jump("loc_C7D7")

    label("loc_C7D3")

    AddParty(0x3, 0xFC, 0xFF)

    label("loc_C7D7")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C7EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C838")
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C80C")
    AddParty(0x5, 0xFA, 0xFF)
    Jump("loc_C824")

    label("loc_C80C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C820")
    AddParty(0x5, 0xFB, 0xFF)
    Jump("loc_C824")

    label("loc_C820")

    AddParty(0x5, 0xFC, 0xFF)

    label("loc_C824")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C838")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C85D")
    AddParty(0x6, 0xFC, 0xFF)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C85D")

    Return()

    # Function_40_C72C end

    def Function_41_C85E(): pass

    label("Function_41_C85E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_C86E")
    RemoveParty(0x7, 0xFF)

    label("loc_C86E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_C87E")
    RemoveParty(0x4, 0xFF)

    label("loc_C87E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_C88E")
    RemoveParty(0x6, 0xFF)

    label("loc_C88E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_C89E")
    RemoveParty(0x3, 0xFF)

    label("loc_C89E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_C8AE")
    RemoveParty(0x5, 0xFF)

    label("loc_C8AE")

    Return()

    # Function_41_C85E end

    def Function_42_C8AF(): pass

    label("Function_42_C8AF")

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
        (0, "loc_C92C"),
        (1, "loc_C932"),
        (SWITCH_DEFAULT, "loc_C938"),
    )


    label("loc_C92C")

    OP_A2(0x1200)
    Jump("loc_C938")

    label("loc_C932")

    OP_A2(0x1201)
    Jump("loc_C938")

    label("loc_C938")

    Return()

    # Function_42_C8AF end

    def Function_43_C939(): pass

    label("Function_43_C939")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_43_C939 end

    SaveToFile()

Try(main)
