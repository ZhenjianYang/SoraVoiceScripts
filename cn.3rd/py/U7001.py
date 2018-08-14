from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'U7001   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U7001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60210",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            'ED6_DT21/U7001_5 ._SN',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '约修亚',                               # 9
        '凯文',                                 # 10
        '莉丝',                                 # 11
        '提妲',                                 # 12
        '尤莉亚\u3000\u3000\u3000\u3000\u3000\u3000\u3000',# 13
        '穆拉',                                 # 14
        '乔丝特',                               # 15
        '科洛丝',                               # 16
        '基库',                                 # 17
        '奥利维尔',                             # 18
        '金',                                   # 19
        '亚妮拉丝',                             # 20
        '雪拉扎德',                             # 21
        '阿加特',                               # 22
        '艾丝蒂尔',                             # 23
        '理查德',                               # 24
        '玲',                                   # 25
        '基尔巴特',                             # 26
        '假设镜头',                             # 27
        ' ',                                    # 28
        ' ',                                    # 29
        ' ',                                    # 30
        ' ',                                    # 31
        '',                                     # 32
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT26/CH20622 ._CH',             # 00
        'ED6_DT27/CH03250 ._CH',             # 01
        'ED6_DT26/CH20660 ._CH',             # 02
        'ED6_DT26/CH20650 ._CH',             # 03
        'ED6_DT27/CH03150 ._CH',             # 04
        'ED6_DT27/CH03080 ._CH',             # 05
        'ED6_DT07/CH00060 ._CH',             # 06
        'ED6_DT27/CH03580 ._CH',             # 07
        'ED6_DT27/CH03570 ._CH',             # 08
        'ED6_DT27/CH03100 ._CH',             # 09
        'ED6_DT27/CH03210 ._CH',             # 0A
        'ED6_DT07/CH02323 ._CH',             # 0B
        'ED6_DT27/CH03260 ._CH',             # 0C
        'ED6_DT07/CH00070 ._CH',             # 0D
        'ED6_DT07/CH01630 ._CH',             # 0E
        'ED6_DT27/CH03240 ._CH',             # 0F
        'ED6_DT06/CH20053 ._CH',             # 10
        'ED6_DT27/CH03000 ._CH',             # 11
        'ED6_DT07/CH02030 ._CH',             # 12
        'ED6_DT27/CH03510 ._CH',             # 13
        'ED6_DT26/CH20655 ._CH',             # 14
        'ED6_DT27/CH03153 ._CH',             # 15
        'ED6_DT27/CH03103 ._CH',             # 16
        'ED6_DT27/CH03093 ._CH',             # 17
        'ED6_DT27/CH03243 ._CH',             # 18
        'ED6_DT06/CH20020 ._CH',             # 19
        'ED6_DT06/CH20021 ._CH',             # 1A
        'ED6_DT07/CH00312 ._CH',             # 1B
        'ED6_DT26/CH20501 ._CH',             # 1C
    )

    AddCharChipPat(
        'ED6_DT26/CH20622P._CP',             # 00
        'ED6_DT27/CH03250P._CP',             # 01
        'ED6_DT26/CH20660P._CP',             # 02
        'ED6_DT26/CH20650P._CP',             # 03
        'ED6_DT27/CH03150P._CP',             # 04
        'ED6_DT27/CH03080P._CP',             # 05
        'ED6_DT07/CH00060P._CP',             # 06
        'ED6_DT27/CH03580P._CP',             # 07
        'ED6_DT27/CH03570P._CP',             # 08
        'ED6_DT27/CH03100P._CP',             # 09
        'ED6_DT27/CH03210P._CP',             # 0A
        'ED6_DT07/CH02323P._CP',             # 0B
        'ED6_DT27/CH03260P._CP',             # 0C
        'ED6_DT07/CH00070P._CP',             # 0D
        'ED6_DT07/CH01630P._CP',             # 0E
        'ED6_DT27/CH03240P._CP',             # 0F
        'ED6_DT06/CH20053P._CP',             # 10
        'ED6_DT27/CH03000P._CP',             # 11
        'ED6_DT07/CH02030P._CP',             # 12
        'ED6_DT27/CH03510P._CP',             # 13
        'ED6_DT26/CH20655P._CP',             # 14
        'ED6_DT27/CH03153P._CP',             # 15
        'ED6_DT27/CH03103P._CP',             # 16
        'ED6_DT27/CH03093P._CP',             # 17
        'ED6_DT27/CH03243P._CP',             # 18
        'ED6_DT06/CH20020P._CP',             # 19
        'ED6_DT06/CH20021P._CP',             # 1A
        'ED6_DT07/CH00312P._CP',             # 1B
        'ED6_DT26/CH20501P._CP',             # 1C
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 14,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 13,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
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
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 5,
        TalkScenaIndex      = 15,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C0,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 26,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 262170,
        ChipIndex           = 0x1A,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1966105,
        ChipIndex           = 0x19,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 9000000,
        Z                   = 9000000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1835033,
        ChipIndex           = 0x19,
        NpcIndex            = 0x116,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -3000,
        Y                   = -1000,
        Z                   = -21000,
        Range               = 2610,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFFBFF0,
        Unknown_18          = 0x0,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 0,
        Y                   = 0,
        Z                   = 0,
        Range               = 0,
        Unknown_10          = 0x0,
        Unknown_14          = 0x0,
        Unknown_18          = 0x2,
        Unknown_1C          = 9,
    )


    DeclActor(
        TriggerX            = 10,
        TriggerZ            = -10000,
        TriggerY            = -93360,
        TriggerRange        = 1800,
        ActorX              = 10,
        ActorZ              = -9500,
        ActorY              = -93360,
        Flags               = 0x7C,
        TalkScenaIndex      = 5,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 6580,
        TriggerZ            = -11000,
        TriggerY            = -91000,
        TriggerRange        = 1800,
        ActorX              = 6580,
        ActorZ              = -10000,
        ActorY              = -91000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -10060,
        TriggerZ            = -11000,
        TriggerY            = -97280,
        TriggerRange        = 1800,
        ActorX              = -10060,
        ActorZ              = -10000,
        ActorY              = -97280,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6410,
        TriggerZ            = -11000,
        TriggerY            = -91400,
        TriggerRange        = 1800,
        ActorX              = -6410,
        ActorZ              = -10000,
        ActorY              = -91400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 40,
        TriggerZ            = -11000,
        TriggerY            = -88660,
        TriggerRange        = 1800,
        ActorX              = 40,
        ActorZ              = -10000,
        ActorY              = -88660,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6410,
        TriggerZ            = -11000,
        TriggerY            = -91400,
        TriggerRange        = 1800,
        ActorX              = -6410,
        ActorZ              = -10000,
        ActorY              = -91400,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_58A",          # 00, 0
        "Function_1_674",          # 01, 1
        "Function_2_8D0",          # 02, 2
        "Function_3_16AD",         # 03, 3
        "Function_4_16DA",         # 04, 4
        "Function_5_1744",         # 05, 5
        "Function_6_317B",         # 06, 6
        "Function_7_31D3",         # 07, 7
        "Function_8_4534",         # 08, 8
        "Function_9_466E",         # 09, 9
        "Function_10_4789",        # 0A, 10
        "Function_11_4DD7",        # 0B, 11
        "Function_12_52EB",        # 0C, 12
        "Function_13_5319",        # 0D, 13
        "Function_14_534C",        # 0E, 14
        "Function_15_546C",        # 0F, 15
        "Function_16_5811",        # 10, 16
        "Function_17_5D8F",        # 11, 17
        "Function_18_5FDA",        # 12, 18
        "Function_19_6290",        # 13, 19
        "Function_20_670E",        # 14, 20
        "Function_21_67B8",        # 15, 21
    )


    def Function_0_58A(): pass

    label("Function_0_58A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F2")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_5A2"),
        (SWITCH_DEFAULT, "loc_5F2"),
    )


    label("loc_5A2")

    SetChrPos(0x0, -20, 1000, -21810, 180)
    SetChrPos(0x1, -20, 1000, -21810, 180)
    SetChrPos(0x2, -20, 1000, -21810, 180)
    SetChrPos(0x3, -20, 1000, -21810, 180)
    OP_30(0x1)
    OP_69(0x0, 0x0)
    Jump("loc_5F2")

    label("loc_5F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_611")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 8)
    Jump("loc_66B")

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_630")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 7)
    Jump("loc_66B")

    label("loc_630")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_64F")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 5)
    Jump("loc_66B")

    label("loc_64F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_66B")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_66B")

    Call(0, 11)
    Call(0, 10)
    Return()

    # Function_0_58A end

    def Function_1_674(): pass

    label("Function_1_674")

    OP_16(0x2, 0xFA0, 0xFFFE2082, 0xFFFD8D0C, 0x23007B)
    OP_10(0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_6A1")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)
    Jump("loc_6C4")

    label("loc_6A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E1, 0)), scpexpr(EXPR_END)), "loc_6D1")
    OP_C4(0x0, 0x200)

    label("loc_6D1")

    LoadEffect(0x0, "map\\mp089_00.eff")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F7")
    OP_65(0x0, 0x1)
    Jump("loc_6FB")

    label("loc_6F7")

    OP_64(0x0, 0x1)

    label("loc_6FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 0)), scpexpr(EXPR_END)), "loc_706")
    OP_64(0x5, 0x1)

    label("loc_706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_765")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_762")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -10060, -10000, -97280, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_762")

    Jump("loc_771")

    label("loc_765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_771")
    OP_64(0x2, 0x1)

    label("loc_771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x522, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CD")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 6920, -10000, -91400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_7CD")

    Jump("loc_7E1")

    label("loc_7D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E1")
    OP_64(0x1, 0x1)

    label("loc_7E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x541, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_840")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83D")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -6410, -10000, -91400, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_83D")

    Jump("loc_84C")

    label("loc_840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84C")
    OP_64(0x3, 0x1)

    label("loc_84C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A8")
    LoadEffect(0x1, "map\\mp257_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 40, -10000, -88660, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)

    label("loc_8A8")

    Jump("loc_8B7")

    label("loc_8AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B7")
    OP_64(0x4, 0x1)

    label("loc_8B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8CF")
    OP_E5(0x1, 0xFF, 0x11, 262144)
    OP_E5(0x1, 0xFF, 0x13, 262144)

    label("loc_8CF")

    Return()

    # Function_1_674 end

    def Function_2_8D0(): pass

    label("Function_2_8D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_AD(0x2400E3, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    Sleep(2000)
    SetChrPos(0x109, -1370, -11000, -90020, 0)
    SetChrPos(0x10F, -6970, -11000, -92640, 270)
    OP_6D(-2750, -7150, -71840, 0)
    OP_67(0, 8400, -10000, 0)
    OP_6B(3980, 0)
    OP_6C(313000, 0)
    OP_6E(529, 0)
    Sleep(1000)
    OP_43(0x109, 0x0, 0x0, 0x3)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    OP_1D(0xD2)

    def lambda_9A0():
        OP_6D(-2750, -7150, -94090, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9A0)

    def lambda_9B8():
        OP_67(0, 6910, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9B8)

    def lambda_9D0():
        OP_6B(4170, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_9D0)

    def lambda_9E0():
        OP_6C(313000, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_9E0)

    def lambda_9F0():
        OP_6E(529, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_9F0)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_6D(-6020, -11000, -90210, 0)
    OP_67(0, 5770, -10000, 0)
    OP_6B(1950, 0)
    OP_6C(351000, 0)
    OP_6E(482, 0)
    OP_0D()
    Sleep(1000)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #0
        0x109,
        (
            "#1063F#6P《无明祭祀书》……\x02\x03",

            "《威加那的眷属》……\x02\x03",

            "《宇宙图鉴》……\x01",
            "这边还有《苍之断章》吗……\x02\x03",

            "#1065F──历代各地的\x01",
            "贵重书籍在这里\x01",
            "竟然都有收藏。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 0, 400)
    Sleep(500)

    ChrTalk(    #1
        0x109,
        (
            "#1064F#6P哦哦！？\x01",
            "这本是《伊斯特米亚异闻》！\x01",
            "这可是禁书呀！\x02\x03",

            "#1068F要是让封圣省的家伙看到\x01",
            "肯定连眼睛的颜色都变了吧！？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10F, 0x0)

    ChrTalk(    #2
        0x10F,
        (
            "#1446F#6P不止珍稀的书籍……\x01",
            "连今年刚出的书也有。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 225, 400)

    ChrTalk(    #3
        0x109,
        (
            "#1079F#2P什么……！？\x02\x03",

            "#1069F是什么标题？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 45, 400)
    Sleep(300)

    ChrTalk(    #4
        0x10F,
        (
            "#1440F#6P《边走边吃王国纪行》\x01",
            "───利贝尔通讯社出版。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x109,
        (
            "#1068F#2P呼……！\x02\x03",

            "#1069F为什么这样的东西\x01",
            "会和禁书放在一起呀！\x02\x03",

            "怎么想都太奇怪了吧！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        (
            "#1802F#6P就算你对我这么说……\x02\x03",

            "#1447F料理的照片\x01",
            "看起来很美味哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x109,
        (
            "#1078F#2P啊，这个应该是\x01",
            "朵洛希拍的照片吧。\x02\x03",

            "#1079F对了，说起来的话，\x01",
            "你的肚子不是饿了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10F,
        (
            "#1447F#6P凯文在看书的时候，\x01",
            "我已经把肚子填饱了……\x02\x03",

            "#1448F剩下的就给你吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E2C():
        OP_6D(-5610, -11000, -89970, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E2C)
    OP_8F(0x10F, 0xFFFFEAA2, 0xFFFFD508, 0xFFFE9904, 0x7D0, 0x0)
    WaitChrThread(0x109, 0x0)
    OP_3E(0x193, 1)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x93\x01\x07\x00。\x02",
    )

    Jump("loc_E83")

    label("loc_E83")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_8F(0x10F, 0xFFFFE958, 0xFFFFD508, 0xFFFE97A6, 0x3E8, 0x0)

    ChrTalk(    #10
        0x109,
        (
            "#1064F#2P什、什么时候就……\x02\x03",

            "#1068F话说回来，\x01",
            "明明买了那么多，\x01",
            "怎么只剩下这么点……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x10F,
        (
            "#1442F#6P无论哪个面包都很美味。\x02\x03",

            "虽然面粉也很重要，\x01",
            "但用的水不好的话，\x01",
            "是做不出这么美味的面包的。\x02\x03",

            "#1447F……利贝尔也许是个不错的国家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x109,
        (
            "#1840F#2P的确，我承认\x01",
            "这个国家的饭菜是很不错的……\x02\x03",

            "#1068F好了，适可而止，\x01",
            "别再说吃饭的话题了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10F,
        (
            "#1446F#6P……明白了。\x02\x03",

            "#1443F无论怎么想\x01",
            "这个地方也太奇怪了。\x02\x03",

            "总之我想应该先\x01",
            "到处调查一番看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        (
            "#1065F#2P是呀……\x02\x03",

            "#1079F对了，说起来。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x10F,
        (
            "#1802F#6P……………………………\x02\x03",

            "已经……没有光了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x109,
        (
            "#1067F#2P是呀，完全没有反应了。\x02\x03",

            "#1063F虽说如此，\x01",
            "我们的确是在这东西发光后\x01",
            "才被送到这个场所的……\x02\x03",

            "看来我们陷入了\x01",
            "超乎想象的麻烦当中呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10F,
        (
            "#1443F#6P…………………………………\x02\x03",

            "#1446F凯文，那个借我。\x02\x03",

            "放在我这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #18
        0x109,
        (
            "#1064F#2P哎……\x01",
            "怎么，这可是很危险的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10F,
        (
            "#1443F#6P保护你是\x01",
            "作为随从骑士的我的使命。\x02\x03",

            "这么危险的东西\x01",
            "是不能让你拿着的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x109,
        "#1840F#2P莉丝……我说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10F,
        "#1443F#6P请交给我。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x109,
        (
            "#1065F#2P呼……\x01",
            "好了，放轻松点吧。\x02\x03",

            "#1063F我们会来到这个地方\x01",
            "还不能肯定就是\x01",
            "这个『方石』的原因。\x02\x03",

            "而且，之前明明是我拿着，\x01",
            "你不是也被一起卷进来了吗。\x02\x03",

            "那么就算是你拿着\x01",
            "危险也是不会改变的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10F,
        "#1441F#6P可是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1060F#2P对不起，这是上司的决定。\x02\x03",

            "随从骑士要听从\x01",
            "守护骑士的话吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10F,
        (
            "#1445F#6P………………………………\x02\x03",

            "#1446F………知道了。\x02\x03",

            "#1443F但是，如果真的发生危险\x01",
            "就马上扔掉。\x02\x03",

            "这个我是不会让步的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        "#1840F#2P知道了，我答应你。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #27
        0x109,
        (
            "#1060F#2P……那么\x01",
            "我们这就开始搜索吧。\x02\x03",

            "赶紧查出这个\x01",
            "古怪的地方是哪里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10F,
        "#1440F#6P………明白。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1615():
        OP_6B(2800, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1615)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2600)
    OP_6D(-4560, -11000, -93520, 0)
    OP_67(0, 7900, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(450, 0)
    SetChrPos(0x109, -4560, -11000, -93520, 135)
    SetChrPos(0x10F, -4560, -11000, -93520, 135)
    OP_69(0x0, 0x0)
    Sleep(1000)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_2_8D0 end

    def Function_3_16AD(): pass

    label("Function_3_16AD")

    Sleep(2000)
    OP_8C(0x109, 270, 400)
    Sleep(300)
    OP_8E(0xFE, 0xFFFFED72, 0xFFFFD508, 0xFFFE9C74, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_3_16AD end

    def Function_4_16DA(): pass

    label("Function_4_16DA")

    Sleep(1000)
    OP_8F(0xFE, 0xFFFFE372, 0xFFFFD508, 0xFFFE92E2, 0x1F4, 0x0)
    Sleep(300)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(3000)
    OP_8C(0xFE, 315, 400)
    OP_8F(0xFE, 0xFFFFE4C6, 0xFFFFD508, 0xFFFE9620, 0x1F4, 0x0)
    Sleep(300)
    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_4_16DA end

    def Function_5_1744(): pass

    label("Function_5_1744")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x1)
    SetChrPos(0x109, 350, 1000, -20010, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10F, 200, 1000, -33740, 180)
    SetChrPos(0x22, 200, 1000, -33740, 180)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    OP_6D(200, 1000, -33740, 0)
    OP_67(0, 7210, -10000, 0)
    OP_6B(2480, 0)
    OP_6C(315000, 0)
    OP_6E(315, 0)
    OP_6A(0x22)
    Sleep(500)

    def lambda_17E8():
        OP_8E(0xFE, 0xF0, 0x3E8, 0xFFFEAC82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_17E8)

    def lambda_1803():
        OP_8E(0xFE, 0xF0, 0x3E8, 0xFFFEAC82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_1803)
    FadeToBright(2000, 0)
    OP_0D()
    OP_43(0x109, 0x0, 0x0, 0x6)

    ChrTalk(    #29 op#A op#5
        0x109,
        (
            "#3P#9A……莉丝……！\x02\x03",

            "#17A喂，我说莉丝！\x05\x02",
        )
    )

    CloseMessageWindow()

    def lambda_186C():
        OP_8E(0xFE, 0xF0, 0x3E8, 0xFFFEAC82, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_186C)
    Sleep(500)

    def lambda_188C():
        OP_8E(0xFE, 0xF0, 0x3E8, 0xFFFEAC82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_188C)

    ChrTalk(    #30 op#A op#5
        0x10F,
        "#1445F#6P#7A…………………………………\x05\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31 op#A op#5
        0x109,
        (
            "#1063F#27A#11P怎么……\x01",
            "在生什么气？\x02\x03",

            "#1079F#42A啊，对了……\x01",
            "这里到处都是\x01",
            "你不认识的同伴。\x02\x03",

            "#1068F#45A我光顾着自己热闹……\x01",
            "却没顾及你的感受，真是迟钝呀。\x02\x03",

            "#1840F#19A对不起，我道歉。\x05\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32 op#A op#5
        0x10F,
        "#1446F#6A#6P…………………………………\x05\x02",
    )

    CloseMessageWindow()
    OP_44(0x10F, 0x0)
    SetChrSubChip(0x10F, 0)
    OP_44(0x22, 0x0)
    OP_6A(0xFF)
    Sleep(500)
    OP_44(0x109, 0x0)
    OP_44(0x109, 0x1)
    SetChrSubChip(0x109, 0)
    Sleep(300)
    Fade(500)
    SetChrPos(0x109, 250, 1000, -72880, 180)
    SetChrPos(0x10F, 310, 1000, -75240, 180)
    OP_6D(-520, 1000, -74810, 0)
    OP_67(0, 6130, -10000, 0)
    OP_6B(2500, 0)
    OP_6C(219000, 0)
    OP_6E(315, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #33
        0x10F,
        "#1445F#5P……还想蒙混下去吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        "#1064F#12P哎……\x02",
    )

    CloseMessageWindow()
    OP_1D(0xAD)
    Sleep(500)

    ChrTalk(    #35
        0x10F,
        (
            "#1446F#5P的确……\x01",
            "我觉得有些被冷落是事实。\x02\x03",

            "我感到，\x01",
            "他们不愧是你在那次事件里\x01",
            "一起度过危机的同伴。\x02",
        )
    )

    Jump("loc_1B40")

    label("loc_1B40")

    CloseMessageWindow()

    ChrTalk(    #36
        0x109,
        (
            "#1840F#12P哈哈……\x01",
            "嗯，发生了很多事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10F,
        (
            "#1806F#5P说实话……\x01",
            "我既觉得寂寞，又有些羡慕。\x02\x03",

            "这五年里，\x01",
            "凯文一直在躲避我……\x02\x03",

            "#1445F看到凯文在我不知情的时候\x01",
            "结交了那么多朋友，\x01",
            "真的有些……悲哀。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x109,
        "#1067F#12P莉丝……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10F,
        (
            "#1447F#5P不过……\x01",
            "我觉得这也不错。\x02\x03",

            "#1445F那天，姐姐发生了那样的事，\x01",
            "凯文也因此受到打击……\x02\x03",

            "还自责到逼着自己\x01",
            "不断接受肮脏的工作……\x02\x03",

            "我只是听到传闻，\x01",
            "就明白你受得伤有多大……\x02\x03",

            "#1806F因此……\x01",
            "看到你交到合意的朋友，\x01",
            "我虽然寂寞，但也很高兴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x109,
        "#1841F#12P莉丝，那个……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10F,
        "#1446F#5P──但是，并不是这样的。\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10F, 0, 400)
    Sleep(300)

    ChrTalk(    #42
        0x10F,
        (
            "#1443F#5P凯文你……\x01",
            "对那里的任何人\x01",
            "都没有敞开心扉。\x02\x03",

            "心里明明冷冰冰的，\x01",
            "却在表面做样子配合。\x02\x03",

            "完美地控制着感情，\x01",
            "装出一副开朗的样子。\x02\x03",

            "在我观察了一段时间后，终于明白了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x109,
        (
            "#1079F#12P…………………………………\x02\x03",

            "#1840F哈哈，\x01",
            "你又在莫名其妙地担心了。\x02\x03",

            "#1071F不好意思，\x01",
            "我可没有那么精明。\x02\x03",

            "开心的时候开心，\x01",
            "生气的时候也抑制不住自己。\x02\x03",

            "#1066F你从前也知道，\x01",
            "我是个很容易被看透的男人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x10F,
        (
            "#1447F#5P确实……\x02\x03",

            "#1806F『影之王』说的话\x01",
            "看来真的让你动摇了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #45
        0x109,
        "#1076F#12P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10F,
        (
            "#1443F#5P凯文你注意到了……\x01",
            "那些家伙到底在说什么。\x02\x03",

            "但却继续在其他人面前\x01",
            "假装不知道。\x02\x03",

            "#1445F不……\x01",
            "说不定对你自己也是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        "#1066F#12P哈哈……你说什么呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10F,
        (
            "#1446F#5P『领受新供品，\x01",
            "  即让汝等发现印记。』\x02\x03",

            "#1805F……这是什么意思？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x109,
        (
            "#1067F#12P…………………………………\x02\x03",

            "#1841F……我说，莉丝。\x01",
            "你有些累了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x10F,
        "#1444F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x109,
        (
            "#1840F#12P对我的愤怒和不满……\x01",
            "这些感情胡乱交织在一起，\x01",
            "让你乱了方寸吧。\x02\x03",

            "你是因为疲劳\x01",
            "才会这样胡思乱想的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x10F,
        "#1802F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x109,
        (
            "#1065F#12P……说实话，我觉得\x01",
            "这对你来说是件坏事。\x02\x03",

            "我之前确实很忙……\x01",
            "也没有找机会\x01",
            "好好地交流过。\x02\x03",

            "#1078F不过，\x01",
            "往后还要一起工作──\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x10F,
        "#1445F#5P……够了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x109,
        "#1064F#12P哎……\x02",
    )

    CloseMessageWindow()

    def lambda_235C():
        OP_6D(-520, 1000, -74160, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_235C)

    def lambda_2374():
        OP_8E(0xFE, 0x140, 0x3E8, 0xFFFEE094, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2374)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x109, 0x0)
    Fade(1000)

    def lambda_239E():
        OP_6B(2400, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_239E)
    SetChrChipByIndex(0x10F, 3)
    SetChrSubChip(0x10F, 0)
    SetChrFlags(0x10F, 0x2)
    OP_99(0x10F, 0x0, 0x2, 0x5DC)
    OP_22(0xA5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 3)
    SetChrSubChip(0x109, 19)
    SetChrFlags(0x109, 0x2)

    def lambda_23DA():
        OP_99(0xFE, 0x3, 0x8, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_23DA)

    def lambda_23EA():
        OP_99(0xFE, 0x13, 0x1A, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_23EA)
    WaitChrThread(0x10F, 0x0)
    Fade(250)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    ClearChrFlags(0x10F, 0x2)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #56
        0x109,
        "#1079F#12P啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x10F,
        (
            "#1441F#5P……适可而止吧。\x02\x03",

            "这样的废话……\x01",
            "你以为会对我有用吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_248E():
        OP_99(0xFE, 0x1A, 0x1C, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_248E)
    WaitChrThread(0x109, 0x0)
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    ClearChrFlags(0x109, 0x2)
    OP_0D()
    Sleep(300)

    ChrTalk(    #58
        0x109,
        "#1067F#12P…………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_24EE():
        OP_6D(-520, 1000, -74560, 1200)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_24EE)

    def lambda_2506():
        OP_6B(2500, 1200)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2506)

    def lambda_2516():
        OP_8F(0xFE, 0x14A, 0x3E8, 0xFFFEDE32, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2516)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x10F, 0x0)
    Sleep(300)

    ChrTalk(    #59
        0x10F,
        (
            "#1806F#5P就算我随从骑士失职……\x01",
            "我也不愿和你继续在一起了。\x02\x03",

            "我不希望再看到\x01",
            "……如同空壳一般的凯文……\x02\x03",

            "#1445F……所以……\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10F, 180, 400)
    WaitChrThread(0x10F, 0x0)
    SetChrFlags(0x10F, 0x4)

    def lambda_260A():
        OP_6D(-520, 1000, -76500, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_260A)

    def lambda_2622():
        OP_8E(0xFE, 0xFFFFFF7E, 0x3E8, 0xFFFEA070, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2622)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #60
        0x109,
        (
            "#1079F#12P啊……\x02\x03",

            "#1067F………………………………\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x10F, 0x1)
    SetChrFlags(0x10F, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 350, 1000, -63600, 180)
    Sleep(500)

    ChrTalk(    #61
        0x10,
        "#1P……凯文？\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Fade(500)
    OP_6D(-600, 1000, -68450, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(2610, 0)
    OP_6C(315000, 0)
    OP_6E(313, 0)

    def lambda_2728():
        OP_6D(-640, 1000, -70550, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2728)

    def lambda_2740():
        OP_8E(0xFE, 0xD2, 0x3E8, 0xFFFEED78, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_2740)
    Sleep(1000)
    OP_8C(0x109, 0, 400)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(300)

    ChrTalk(    #62
        0x109,
        (
            "#1067F#6P约修亚吗……\x02\x03",

            "#1840F哈哈……好像让你看到\x01",
            "我丢脸的样子了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "#1500F#11P不……\x02\x03",

            "#1503F………………………………\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x109,
        (
            "#1075F#6P……喂，约修亚。\x02\x03",

            "#1060F你对我的事\x01",
            "做过某种程度的调查吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        (
            "#1505F#11P……是的。\x02\x03",

            "#1502F『异端制裁者』凯文·格拉汉姆。\x02\x03",

            "统帅星杯骑士团的\x01",
            "十二名『守护骑士』中的一个。\x02\x03",

            "并且是一手揽下对\x01",
            "万恶不赦的大罪人处刑之任的执行人。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x109,
        (
            "#1066F#6P哈哈，真厉害。\x02\x03",

            "只要是接近艾丝蒂尔的男人，\x01",
            "其经历都被彻底地调查了吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10,
        (
            "#1503F#11P嗯……\x02\x03",

            "#1505F不过你除了罪人以外\x01",
            "绝不会随意伤人。\x02\x03",

            "#1500F从这点上\x01",
            "我判断你没有危险。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x109,
        "#1840F#6P呵呵……原来如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10,
        (
            "#1502F#11P那么……\x01",
            "怀斯曼果然是被你干掉的？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x109,
        (
            "#1075F#6P是呀……是我干掉的。\x02\x03",

            "#1063F原本我的任务\x01",
            "就只是消灭他罢了。\x02\x03",

            "除此以外的事都\x01",
            "不过是刻意安排的烟雾弹。\x02\x03",

            "#1065F和你们的合作关系也是如此。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10,
        (
            "#1505F#11P……我明白了。\x02\x03",

            "#1503F艾丝蒂尔被带到\x01",
            "『古罗力亚斯』那次……\x02\x03",

            "#1502F你也应该\x01",
            "一开始就预料到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x109,
        (
            "#1075F#6P呵呵……这都被你看穿了。\x02\x03",

            "#1073F对，我注意到了\x01",
            "艾丝蒂尔被带走的可能性，\x01",
            "但并没有做出任何应对。\x02\x03",

            "让她作为诱饵，\x01",
            "我才能掌握怀斯曼，\x01",
            "还有行踪不定的你的动向。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x10,
        (
            "#1503F#11P……是这样啊。\x02\x03",

            "#1505F但我还是……\x01",
            "想要感谢你。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x109,
        "#1074F#6P哎……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10,
        (
            "#1503F#11P没有你的帮助，\x01",
            "我就会成为教授操纵的人偶。\x02\x03",

            "会将无比重要的东西……\x01",
            "亲手毁坏。\x02\x03",

            "#1500F这笔人情，\x01",
            "我想我这一生都无法偿还。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x109,
        (
            "#1073F#6P哈哈，太夸张了。\x02\x03",

            "#1075F我先声明，\x01",
            "那可不是为了你才这么做的。\x02\x03",

            "只不过想借解除你的咒缚让他动摇，\x01",
            "从而制造出机会……\x02\x03",

            "#1072F只是为了这个才帮你的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10,
        (
            "#1513F#11P但是我……\x01",
            "还是不得不感谢你。\x02\x03",

            "#1501F就算知道真相，\x01",
            "我对你还是抱有好感。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x109,
        (
            "#1071F#6P哈哈……\x02\x03",

            "#1840F……你从『结社』逃脱出来，\x01",
            "也许是正确的呢。\x02\x03",

            "不管怎么想你都不适合那里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x10,
        (
            "#1513F#11P呵呵……虽然事已至此，\x01",
            "不过我也是这么想的。\x02\x03",

            "#1500F──暂时就由我来\x01",
            "代替莉丝小姐的工作吧。\x02\x03",

            "虽然可能没她做的那么好，\x01",
            "但我想我可以\x01",
            "尽力支援凯文先生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x109,
        (
            "#1841F#6P我都说了，\x01",
            "你不用把那当人情来还的……\x02\x03",

            "#1840F……唉，算了吧。\x01",
            "你还担心着艾丝蒂尔，\x01",
            "这也是没有办法的事。\x02\x03",

            "那就感谢你的帮助了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10,
        "#1513F#11P嗯，就这么办吧。\x02",
    )

    CloseMessageWindow()

    def lambda_3077():
        OP_6B(3000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3077)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2900)
    OP_28(0x2F, 0x4, 0x10)
    OP_28(0x2F, 0x4, 0x20)
    OP_28(0x30, 0x4, 0x10)
    OP_28(0x30, 0x4, 0x20)
    OP_28(0x31, 0x4, 0x10)
    OP_28(0x31, 0x4, 0x20)
    OP_28(0x32, 0x4, 0x4)
    OP_28(0x32, 0x4, 0x8)
    OP_28(0x32, 0x1, 0x1)
    OP_28(0x32, 0x1, 0x2)
    OP_28(0x32, 0x1, 0x4)
    OP_3F(0x358, 1)
    OP_3F(0x359, 1)
    OP_DB(0x0, 0x3)
    OP_A2(0x25C9)
    Call(6, 13)
    OP_DB(0x0, 0x7)
    OP_A2(0x25CD)
    Call(6, 17)
    SetChrFlags(0x10, 0x80)
    OP_DB(0x1, 0xE)
    ClearParty()
    AddParty(0x8, 0xEE, 0xFF)
    AddParty(0x1, 0xEF, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    OP_DD(0x1, 0x0, 0x0, 258, 0, 0, 0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C0(0x20, 0x1, 0x102, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_A2(0x2504)
    OP_A2(0x2508)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_5_1744 end

    def Function_6_317B(): pass

    label("Function_6_317B")

    SetChrPos(0x109, 200, 1000, -22740, 180)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_319D():
        OP_8E(0xFE, 0xF0, 0x3E8, 0xFFFEAC82, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_319D)
    Sleep(4000)

    def lambda_31BD():
        OP_8E(0xFE, 0xF0, 0x3E8, 0xFFFEAC82, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_31BD)
    Return()

    # Function_6_317B end

    def Function_7_31D3(): pass

    label("Function_7_31D3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS440._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS441._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS442._CH")
    OP_C5(0x3, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS443._CH")
    Sleep(1000)
    OP_22(0x73, 0x0, 0x64)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(1500)
    SetMessageWindowPos(120, 150, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #82
        (
            "\x07\x0C#40W抬起头来──\x01",
            "凯文·格拉汉姆。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 280, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #83
        (
            "\x07\x0C#60W…………………………………\x02\x03",

            "……瑟尔纳特……教官……？\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_1D(0xAF)
    Sleep(300)
    OP_C6(0x0, 0x3, -1, 2000, 0)
    Sleep(3000)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #84
        (
            "\x07\x0C#30W你瘦了……\x02\x03",

            "别说吃饭了，\x01",
            "竟然连水也一点没喝。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #85
        "\x07\x0C#60W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #86
        (
            "\x07\x0C#30W我听过报告了。\x01",
            "露菲娜的事我也很遗憾。\x02\x03",

            "不过，不幸的意外\x01",
            "是经常发生的。\x02\x03",

            "特别是像我们这样的人。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #87
        (
            "\x07\x0C#60W…………………………………\x02\x03",

            "……请……杀了我吧………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #88
        "\x07\x0C#30W……什么………………\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #89
        (
            "\x07\x0C#60W我……已经没有……\x01",
            "……再做骑士的意义了……\x02\x03",

            "不仅如此………\x01",
            "……我的……生存意义也………\x02\x03",

            "由教官来的话………\x01",
            "………我毫无怨言…………\x02\x03",

            "别让我感觉到痛苦………\x01",
            "请你……给我个痛快吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #90
        (
            "\x07\x0C#30W我明白了，好吧──#3500W \x01",
            "#20W你以为我会这么说吗？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #91
        "\x07\x0C#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #92
        (
            "\x07\x0C#30W不想感到痛苦而期望\x01",
            "我能痛痛快快的杀掉你吗？\x02\x03",

            "别开玩笑了。\x01",
            "你以为我还对你\x01",
            "有那种权利吗？\x02\x03",

            "对这个血肉归于七耀之理，\x01",
            "灵魂献于女神的你？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #93
        "\x07\x0C#40W…………哎……………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #94
        (
            "\x07\x0C#30W呵呵……\x01",
            "既然你向我如此诉苦，\x01",
            "那我就不再有所顾忌，直接告诉你吧。\x02\x03",

            "就算是我，\x01",
            "这次也稍稍迟疑了一下。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #95
        "\x07\x0C#40W……………？………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #96
        (
            "\x07\x0C#30W──随从骑士凯文·格拉汉姆。\x02\x03",

            "从今日起你将成为\x01",
            "『守护骑士』第五位。\x02\x03",

            "这是由封圣省决定的，\x01",
            "法王阁下也已经认可了。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #97
        "\x07\x0C#60W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x1, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #98
        "\x07\x0C#40W………哎………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #99
        (
            "\x07\x0C#30W你也至少应该听说过，\x01",
            "最近数十年\x01",
            "『第五位』一直空缺。\x02\x03",

            "恭喜你──\x01",
            "你现在就是那个『第五位』了。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #100
        "\x07\x0C#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #101
        (
            "\x07\x0C#30W哼，这下你和我就是同僚了……\x02\x03",

            "长久无主的伍号机也\x01",
            "总算可以重见天日了。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #102
        "\x07\x0C#60W……什么……这……………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #103
        (
            "\x07\x0C#30W还有，守护骑士\x01",
            "都有各自的称号。\x02\x03",

            "你也可以趁现在\x01",
            "适当地考虑一下。\x02\x03",

            "顺带一提，我的称号就是\x01",
            "众所周知的『红耀石』──\x01",
            "又无趣又冷淡的名字。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #104
        (
            "\x07\x0C#40W这种事……\x01",
            "……从没听说过……\x02\x03",

            "为什么是我……怎么会……\x02\x03",

            "姐姐……露菲娜姐姐被……\x01",
            "………没有保护住她的我………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #105
        (
            "\x07\x0C#30W『──那没有什么问题。』\x02\x03",

            "『问题是露菲娜·亚尔珍特\x01",
            "  是个极其优秀的骑士。』\x02\x03",

            "『虽然没有显现圣痕，\x01",
            "  但她解决问题的能力\x01",
            "  也经常凌驾于守护骑士之上。』\x02\x03",

            "『我就期待这个第五位的努力工作\x01",
            "  来弥补这『损失』吧──』\x02\x03",

            "──这是红衣主教大人的话。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -1, 0, 0)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #106
        (
            "\x07\x0C#40W……………………………………\x02\x03",

            "……呵呵………哈哈哈………\x02\x03",

            "这算什么………\x02\x03",

            "……这到底算什么啊………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #107
        "\x07\x0C#30W#4S哇哈哈哈哈哈！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #108
        "\x07\x0C#30W…………………………………\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #109
        (
            "\x07\x0C#30W哈哈……我！？\x02\x03",

            "本想保护露菲娜姐姐\x01",
            "而成为骑士的我！？\x02\x03",

            "可却因为牺牲了姐姐\x01",
            "而被选为守护骑士……！？\x02\x03",

            "啊哈哈，杰作呀！\x01",
            "真是杰作，我简直要笑死了！\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #110
        "\x07\x0C#30W#4S哇──哈哈哈哈哈！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #111
        "\x07\x0C#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, -1, 0, 0)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #112
        (
            "\x07\x0C#30W……呵呵……哈哈哈………\x02\x03",

            "………哼哼……哈哈…………\x02\x03",

            "……………………………………\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #113
        (
            "\x07\x0C#30W──好了。\x01",
            "你想怎么办，凯文·格拉汉姆。\x02\x03",

            "我提醒你，\x01",
            "你有权申请辞退这个委任。\x02\x03",

            "不过在骑士团千年的历史中，\x01",
            "被选为守护骑士还要辞退的人，\x01",
            "可是连一个都没有哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #114
        "\x07\x0C#30W呵呵……是这样吗。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, -1, 500, 0)
    Sleep(1000)
    OP_C6(0x0, 0x3, 16777215, 0, 0)
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("随从骑士凯文")

    AnonymousTalk(    #115
        (
            "\x07\x0C#30W──『守护骑士』第五位，\x01",
            "我就恭敬地接受下来了。\x02\x03",

            "现在就可以\x01",
            "分配任务给我。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 250, -1, -1)
    SetChrName("守护骑士瑟尔纳特")

    AnonymousTalk(    #116
        (
            "\x07\x0C#30W……是吗…………\x02\x03",

            "明白了，就这么办吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(350, 350, -1, -1)
    SetChrName("守护骑士凯文")

    AnonymousTalk(    #117
        (
            "\x07\x0C#30W嗯，既然要做的话就请\x01",
            "尽可能分配些困难的工作。\x02\x03",

            "对了……\x01",
            "接下来还有称号对吧？\x02\x03",

            "嗯，这样吧……\x02",
        )
    )

    Jump("loc_449B")

    label("loc_449B")

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x3, 0x3, 16777215, 1500, 0)
    Sleep(2500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("守护骑士凯文")

    AnonymousTalk(    #118
        (
            "\x07\x0C#40W『异端制裁者』──\x01",
            "就这么定下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_20(0x1388)
    OP_21()
    Sleep(1000)
    OP_C7(0x1, 0xFF, 0x0)
    OP_AD(0x2400E7, 0x0, 0x0, 0x64)
    Sleep(4000)
    OP_56(0x2)
    OP_AE(0xC8)
    OP_20(0x7D0)
    Sleep(2000)
    Call(0, 8)
    Return()

    # Function_7_31D3 end

    def Function_8_4534(): pass

    label("Function_8_4534")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 200, -10500, -93300, 270)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    SetChrFlags(0x11, 0x800)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 0, -11000, -94710, 0)
    SetChrChipByIndex(0x12, 4)
    SetChrSubChip(0x12, 0)
    SetChrFlags(0xEE, 0x80)
    SetChrFlags(0xEF, 0x80)
    SetChrFlags(0xF0, 0x80)
    SetChrFlags(0xF1, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    OP_6D(-410, -11000, -92950, 0)
    OP_67(0, 7320, -10000, 0)
    OP_6B(2100, 0)
    OP_6C(323000, 0)
    OP_6E(421, 0)

    def lambda_4631():
        OP_6B(1700, 6000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4631)
    OP_1D(0xAD)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    OP_A2(0x250B)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_8_4534 end

    def Function_9_466E(): pass

    label("Function_9_466E")

    Call(0, 11)
    Call(0, 10)
    Call(0, 12)
    OP_C0(0x27, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46F8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46DB")
    ClearMapFlags(0x2000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46D8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x49), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x1F4)
    OP_21()
    OP_1D(0x49)

    label("loc_46D8")

    Jump("loc_46F8")

    label("loc_46DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46F8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_20(0x1F4)
    OP_21()
    OP_1D(0xD2)

    label("loc_46F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4788")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4725")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_4725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4746")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_4746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4767")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_4767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4788")
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    label("loc_4788")

    Return()

    # Function_9_466E end

    def Function_10_4789(): pass

    label("Function_10_4789")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_47E3")
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x800)
    SetChrChipByIndex(0x21, 28)
    SetChrSubChip(0x21, 0)
    OP_44(0x21, 0x0)
    SetChrFlags(0x21, 0x4)
    SetChrPos(0x21, 5160, -11000, -95940, 315)
    SetChrPos(0x16, 4050, -11000, -96420, 61)
    SetChrPos(0x1F, -8800, -11000, -95510, 291)
    Jump("loc_4DD6")

    label("loc_47E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_47ED")
    Jump("loc_4DD6")

    label("loc_47ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_486B")
    SetChrPos(0x16, -10900, 1000, -91030, 325)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_END)), "loc_483F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4824")
    OP_43(0x16, 0x0, 0x0, 0xE)
    Jump("loc_483C")

    label("loc_4824")

    SetChrPos(0x16, 9000000, 9000000, 0, 180)
    OP_44(0x16, 0xFF)
    OP_82(0x7, 0x0)

    label("loc_483C")

    Jump("loc_4846")

    label("loc_483F")

    OP_43(0x16, 0x0, 0x0, 0xE)

    label("loc_4846")

    SetChrPos(0x14, -6820, -11000, -92640, 309)
    SetChrPos(0x17, -5020, -11000, -91640, 325)
    Jump("loc_4DD6")

    label("loc_486B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 5)), scpexpr(EXPR_END)), "loc_48A8")
    SetChrPos(0x10, -6010, -11000, -92450, 316)
    SetChrPos(0x17, -5150, -11000, -91780, 325)
    SetChrPos(0x16, -10900, 1000, -91030, 325)
    Jump("loc_4DD6")

    label("loc_48A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 0)), scpexpr(EXPR_END)), "loc_4909")
    SetChrPos(0x17, -5150, -11000, -91780, 328)
    SetChrChipByIndex(0x1C, 24)
    SetChrSubChip(0x1C, 0)
    OP_44(0x1C, 0x0)
    SetChrFlags(0x1C, 0x4)
    SetChrPos(0x1C, -4580, -10700, -96300, 118)
    SetChrPos(0x23, -4930, -10700, -96560, 348)
    SetChrPos(0x25, -5200, -10500, -96570, 246)
    Jump("loc_4DD6")

    label("loc_4909")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x560, 0)), scpexpr(EXPR_END)), "loc_4946")
    SetChrPos(0x1C, 5830, -11000, -91440, 47)
    SetChrPos(0x17, -6010, -11000, -92450, 316)
    SetChrPos(0x16, -5150, -11000, -91780, 325)
    Jump("loc_4DD6")

    label("loc_4946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 7)), scpexpr(EXPR_END)), "loc_4985")
    SetChrPos(0x16, -480, -11000, -91850, 179)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 50, -10450, -93300, 270)
    Jump("loc_4DD6")

    label("loc_4985")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 4)), scpexpr(EXPR_END)), "loc_49E6")
    SetChrPos(0x1C, 440, -11000, -94210, 319)
    SetChrPos(0x10, 1260, -11000, -89620, 15)
    SetChrPos(0x16, -480, -11000, -91850, 179)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 50, -10450, -93300, 270)
    Jump("loc_4DD6")

    label("loc_49E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_4A58")
    SetChrPos(0x11, 50, -10450, -93300, 270)
    SetChrChipByIndex(0x11, 2)
    SetChrSubChip(0x11, 0)
    OP_44(0x11, 0x0)
    SetChrFlags(0x11, 0x4)
    SetChrPos(0x11, 50, -10450, -93300, 270)
    SetChrPos(0x10, 440, -11000, -94210, 319)
    SetChrPos(0x16, -480, -11000, -91850, 179)
    SetChrPos(0x17, -910, -11000, -94440, 31)
    Jump("loc_4DD6")

    label("loc_4A58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_4B34")
    SetChrPos(0x19, -3450, -11000, -95110, 120)
    SetChrChipByIndex(0x12, 21)
    SetChrSubChip(0x12, 0)
    OP_44(0x12, 0x0)
    SetChrFlags(0x12, 0x4)
    SetChrPos(0x12, -4470, -10700, -95930, 120)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AEB")
    SetChrPos(0x1C, -4920, -11000, -92550, 147)
    SetChrPos(0x16, -3550, -11000, -99540, 0)
    SetChrChipByIndex(0x1B, 23)
    SetChrSubChip(0x1B, 0)
    OP_44(0x1B, 0x0)
    SetChrFlags(0x1B, 0x4)
    SetChrPos(0x1B, -4950, -10700, -96800, 120)
    Jump("loc_4B31")

    label("loc_4AEB")

    SetChrPos(0x1C, -2300, -11000, -96280, 272)
    SetChrPos(0x16, -4070, -11000, -98430, 344)
    SetChrChipByIndex(0x1B, 23)
    SetChrSubChip(0x1B, 1)
    OP_44(0x1B, 0x0)
    SetChrFlags(0x1B, 0x4)
    SetChrPos(0x1B, -4950, -10700, -96800, 120)

    label("loc_4B31")

    Jump("loc_4DD6")

    label("loc_4B34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 2)), scpexpr(EXPR_END)), "loc_4D18")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B95")
    SetChrPos(0x12, 4050, -11000, -99830, 66)
    SetChrPos(0x13, 4960, -11000, -98150, 182)
    SetChrPos(0x16, 6270, -11000, -99980, 274)
    Jump("loc_4D15")

    label("loc_4B95")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BDE")
    SetChrPos(0x13, 4150, -11000, -99850, 93)
    SetChrPos(0x16, 6270, -11000, -99980, 274)
    Jump("loc_4D15")

    label("loc_4BDE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C27")
    SetChrPos(0x12, 4150, -11000, -99850, 93)
    SetChrPos(0x16, 6270, -11000, -99980, 274)
    Jump("loc_4D15")

    label("loc_4C27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4C70")
    SetChrPos(0x12, 4150, -11000, -99850, 93)
    SetChrPos(0x13, 6270, -11000, -99980, 274)
    Jump("loc_4D15")

    label("loc_4C70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CA8")
    SetChrPos(0x16, 5760, -11000, -99090, 255)
    Jump("loc_4D15")

    label("loc_4CA8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CE0")
    SetChrPos(0x13, 5760, -11000, -99090, 255)
    Jump("loc_4D15")

    label("loc_4CE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D15")
    SetChrPos(0x12, 5760, -11000, -99090, 255)

    label("loc_4D15")

    Jump("loc_4DD6")

    label("loc_4D18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 5)), scpexpr(EXPR_END)), "loc_4D66")
    SetChrPos(0x12, 13380, -11000, -95790, 71)
    SetChrPos(0x13, 12910, -11000, -96630, 25)
    SetChrPos(0x16, 11430, -11000, -96590, 73)
    SetChrPos(0x1B, 12030, -11000, -95090, 90)
    Jump("loc_4DD6")

    label("loc_4D66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x520, 0)), scpexpr(EXPR_END)), "loc_4DA3")
    SetChrPos(0x12, 13380, -11000, -95790, 71)
    SetChrPos(0x13, 12050, -11000, -97160, 45)
    SetChrPos(0x16, 10710, -11000, -97080, 62)
    Jump("loc_4DD6")

    label("loc_4DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x500, 0)), scpexpr(EXPR_END)), "loc_4DAD")
    Jump("loc_4DD6")

    label("loc_4DAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E2, 4)), scpexpr(EXPR_END)), "loc_4DD6")
    SetChrPos(0x14, 1050, -11000, -89570, 20)
    SetChrPos(0x15, -700, -11000, -89530, 0)

    label("loc_4DD6")

    Return()

    # Function_10_4789 end

    def Function_11_4DD7(): pass

    label("Function_11_4DD7")

    OP_C0(0x23, 0x11, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x12, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x13, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x14, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x15, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x16, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x10, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x17, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x18, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x19, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1A, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1B, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1C, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1D, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1E, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x1F, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C0(0x23, 0x20, 0x181, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x11, 9000000, 9000000, 0, 0)
    SetChrPos(0x12, 9000000, 9000000, 0, 0)
    SetChrPos(0x13, 9000000, 9000000, 0, 0)
    SetChrPos(0x14, 9000000, 9000000, 0, 0)
    SetChrPos(0x15, 9000000, 9000000, 0, 0)
    SetChrPos(0x16, 9000000, 9000000, 0, 0)
    SetChrPos(0x10, 9000000, 9000000, 0, 0)
    SetChrPos(0x17, 9000000, 9000000, 0, 0)
    SetChrPos(0x18, 9000000, 9000000, 0, 0)
    SetChrPos(0x19, 9000000, 9000000, 0, 0)
    SetChrPos(0x1A, 9000000, 9000000, 0, 0)
    SetChrPos(0x1B, 9000000, 9000000, 0, 0)
    SetChrPos(0x1C, 9000000, 9000000, 0, 0)
    SetChrPos(0x1D, 9000000, 9000000, 0, 0)
    SetChrPos(0x1E, 9000000, 9000000, 0, 0)
    SetChrPos(0x1F, 9000000, 9000000, 0, 0)
    SetChrPos(0x20, 9000000, 9000000, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5150")
    SetChrFlags(0x13, 0x80)
    Jump("loc_5155")

    label("loc_5150")

    ClearChrFlags(0x13, 0x80)

    label("loc_5155")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_516B")
    SetChrFlags(0x14, 0x80)
    Jump("loc_5170")

    label("loc_516B")

    ClearChrFlags(0x14, 0x80)

    label("loc_5170")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5186")
    SetChrFlags(0x15, 0x80)
    Jump("loc_518B")

    label("loc_5186")

    ClearChrFlags(0x15, 0x80)

    label("loc_518B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51A1")
    SetChrFlags(0x16, 0x80)
    Jump("loc_51A6")

    label("loc_51A1")

    ClearChrFlags(0x16, 0x80)

    label("loc_51A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51BC")
    SetChrFlags(0x10, 0x80)
    Jump("loc_51C1")

    label("loc_51BC")

    ClearChrFlags(0x10, 0x80)

    label("loc_51C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51D7")
    SetChrFlags(0x17, 0x80)
    Jump("loc_51DC")

    label("loc_51D7")

    ClearChrFlags(0x17, 0x80)

    label("loc_51DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_51F2")
    SetChrFlags(0x19, 0x80)
    Jump("loc_51F7")

    label("loc_51F2")

    ClearChrFlags(0x19, 0x80)

    label("loc_51F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_520D")
    SetChrFlags(0x1A, 0x80)
    Jump("loc_5212")

    label("loc_520D")

    ClearChrFlags(0x1A, 0x80)

    label("loc_5212")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5228")
    SetChrFlags(0x1B, 0x80)
    Jump("loc_522D")

    label("loc_5228")

    ClearChrFlags(0x1B, 0x80)

    label("loc_522D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5243")
    SetChrFlags(0x1C, 0x80)
    Jump("loc_5248")

    label("loc_5243")

    ClearChrFlags(0x1C, 0x80)

    label("loc_5248")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_525E")
    SetChrFlags(0x1D, 0x80)
    Jump("loc_5263")

    label("loc_525E")

    ClearChrFlags(0x1D, 0x80)

    label("loc_5263")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5279")
    SetChrFlags(0x1E, 0x80)
    Jump("loc_527E")

    label("loc_5279")

    ClearChrFlags(0x1E, 0x80)

    label("loc_527E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5294")
    SetChrFlags(0x1F, 0x80)
    Jump("loc_5299")

    label("loc_5294")

    ClearChrFlags(0x1F, 0x80)

    label("loc_5299")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52AF")
    SetChrFlags(0x20, 0x80)
    Jump("loc_52B4")

    label("loc_52AF")

    ClearChrFlags(0x20, 0x80)

    label("loc_52B4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52CA")
    SetChrFlags(0x12, 0x80)
    Jump("loc_52CF")

    label("loc_52CA")

    ClearChrFlags(0x12, 0x80)

    label("loc_52CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_52E5")
    SetChrFlags(0x11, 0x80)
    Jump("loc_52EA")

    label("loc_52E5")

    ClearChrFlags(0x11, 0x80)

    label("loc_52EA")

    Return()

    # Function_11_4DD7 end

    def Function_12_52EB(): pass

    label("Function_12_52EB")

    OP_A3(0x1)
    OP_A3(0x2)
    OP_A3(0x3)
    OP_A3(0x4)
    OP_A3(0x5)
    OP_A3(0x6)
    OP_A3(0x7)
    OP_A3(0x8)
    OP_A3(0x9)
    OP_A3(0xA)
    OP_A3(0xB)
    OP_A3(0xC)
    OP_A3(0xD)
    OP_A3(0xE)
    OP_A3(0xF)
    Return()

    # Function_12_52EB end

    def Function_13_5319(): pass

    label("Function_13_5319")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x540, 0)), scpexpr(EXPR_END)), "loc_5323")
    Jump("loc_534B")

    label("loc_5323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x521, 6)), scpexpr(EXPR_END)), "loc_5347")
    SetChrChipByIndex(0xFE, 20)

    label("loc_532F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5344")
    OP_99(0xFE, 0x0, 0x1, 0x1F4)
    Jump("loc_532F")

    label("loc_5344")

    Jump("loc_534B")

    label("loc_5347")

    Call(6, 2)

    label("loc_534B")

    Return()

    # Function_13_5319 end

    def Function_14_534C(): pass

    label("Function_14_534C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x565, 3)), scpexpr(EXPR_END)), "loc_535A")
    Call(6, 2)
    Jump("loc_546B")

    label("loc_535A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 0)), scpexpr(EXPR_END)), "loc_5467")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_END)), "loc_541D")

    label("loc_5368")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_541A")
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
    OP_99(0xFE, 0x0, 0x2, 0x7D0)
    Sleep(1000)
    PlayEffect(0x0, 0x7, 0xFE, 200, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_C0(0x24, 0x0, 0xFE, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2710), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_53F0")
    OP_22(0x1F7, 0x0, 0x32)

    label("loc_53F0")

    OP_99(0xFE, 0x3, 0x7, 0x7D0)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5412")
    Sleep(2000)
    Jump("loc_5417")

    label("loc_5412")

    Sleep(4000)

    label("loc_5417")

    Jump("loc_5368")

    label("loc_541A")

    Jump("loc_5464")

    label("loc_541D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5464")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5446")
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)

    label("loc_5446")

    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_541D")

    label("loc_5464")

    Jump("loc_546B")

    label("loc_5467")

    Call(6, 2)

    label("loc_546B")

    Return()

    # Function_14_534C end

    def Function_15_546C(): pass

    label("Function_15_546C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x522, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54C0")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #119
        "\x07\x05在书架上发现有趣的书。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2672)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_580D")

    label("loc_54C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5672")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #120
        "\x07\x05书架上摆放着有趣的书。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读《猫语日常会话入门》】\x01",        # 0
            "【阅读《艾尔贝啄木鸟的生态》】\x01",      # 1
            "【阅读《哈茨少年冒险记·上》】\x01",      # 2
            "【阅读《哈茨少年冒险记·下》】\x01",      # 3
            "【阅读《31棵丝柏树》】\x01",              # 4
            "【阅读《肉体改造论》】\x01",              # 5
            "【放弃】\x01",                            # 6
        )
    )

    Jump("loc_55E1")

    label("loc_55E1")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5616")
    OP_B8(0xE1, 0x0)

    label("loc_5616")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5628")
    OP_B8(0xE2, 0x0)

    label("loc_5628")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_563A")
    OP_B8(0xE3, 0x0)

    label("loc_563A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_564C")
    OP_B8(0xE4, 0x0)

    label("loc_564C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_565E")
    OP_B8(0xE5, 0x0)

    label("loc_565E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_566F")
    Call(0, 16)

    label("loc_566F")

    Jump("loc_580D")

    label("loc_5672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57FD")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #121
        "\x07\x05书架上摆放着有趣的书。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读《猫语日常会话入门》】\x01",        # 0
            "【阅读《艾尔贝啄木鸟的生态》】\x01",      # 1
            "【阅读《哈茨少年冒险记·上》】\x01",      # 2
            "【阅读《哈茨少年冒险记·下》】\x01",      # 3
            "【阅读《31棵丝柏树》】\x01",              # 4
            "【放弃】\x01",                            # 5
        )
    )

    Jump("loc_577D")

    label("loc_577D")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57B2")
    OP_B8(0xE1, 0x0)

    label("loc_57B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57C4")
    OP_B8(0xE2, 0x0)

    label("loc_57C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57D6")
    OP_B8(0xE3, 0x0)

    label("loc_57D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57E8")
    OP_B8(0xE4, 0x0)

    label("loc_57E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57FA")
    OP_B8(0xE5, 0x0)

    label("loc_57FA")

    Jump("loc_580D")

    label("loc_57FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CB, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_580D")
    Call(0, 16)

    label("loc_580D")

    TalkEnd(0xFF)
    Return()

    # Function_15_546C end

    def Function_16_5811(): pass

    label("Function_16_5811")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #122
        (
            "\x07\x05基尔巴特·斯坦因著……\x01",
            "《肉体改造论》。\x02",
        )
    )

    CloseMessageWindow()
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "读读看\x01",      # 0
            "算了\x01",        # 1
        )
    )

    Jump("loc_5882")

    label("loc_5882")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D8E")
    OP_62(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_63(0x0)
    Sleep(800)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (8, "loc_5911"),
        (14, "loc_595C"),
        (0, "loc_59C1"),
        (1, "loc_59FF"),
        (4, "loc_5A75"),
        (6, "loc_5AAD"),
        (5, "loc_5ACF"),
        (2, "loc_5B1A"),
        (3, "loc_5B45"),
        (10, "loc_5BA9"),
        (9, "loc_5C15"),
        (7, "loc_5C5E"),
        (13, "loc_5CA8"),
        (12, "loc_5CEA"),
        (11, "loc_5D18"),
        (15, "loc_5D40"),
        (SWITCH_DEFAULT, "loc_5D8D"),
    )


    label("loc_5911")


    ChrTalk(    #123
        0x109,
        (
            "#1064F哇…………\x02\x03",

            "#1068F那位小哥\x01",
            "真的经历过很多事……\x02",
        )
    )

    Jump("loc_5D8D")

    label("loc_595C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x584, 0)), scpexpr(EXPR_END)), "loc_5992")

    ChrTalk(    #124
        0x10F,
        "#1936F…………………………无语。\x02",
    )

    Jump("loc_59BE")

    label("loc_5992")


    ChrTalk(    #125
        0x10F,
        "#1446F…………………………无语。\x02",
    )


    label("loc_59BE")

    Jump("loc_5D8D")

    label("loc_59C1")


    ChrTalk(    #126
        0x101,
        (
            "#1019F哇，这是什么……\x02\x03",

            "好像很难启齿……\x02",
        )
    )

    Jump("loc_5D8D")

    label("loc_59FF")


    ChrTalk(    #127
        0x102,
        (
            "#1502F……这、这是………………\x02\x03",

            "#1508F（看来这是基于\x01",
            "  『结社』的猎兵强化训练\x01",
            "  而写出来的……）\x02",
        )
    )

    Jump("loc_5D8D")

    label("loc_5A75")


    ChrTalk(    #128
        0x105,
        (
            "#1165F啊哈哈……\x01",
            "（看来吃了不少苦呀……）\x02",
        )
    )

    Jump("loc_5D8D")

    label("loc_5AAD")


    ChrTalk(    #129
        0x107,
        "#065F真可怜…………\x02",
    )

    Jump("loc_5D8D")

    label("loc_5ACF")


    ChrTalk(    #130
        0x106,
        (
            "#055F呜………………\x02\x03",

            "#551F他做了不少\x01",
            "艰苦的修行呢……\x02",
        )
    )

    Jump("loc_5D8D")

    label("loc_5B1A")


    ChrTalk(    #131
        0x103,
        "#1527F哦，还有这样的事啊……\x02",
    )

    Jump("loc_5D8D")

    label("loc_5B45")


    ChrTalk(    #132
        0x104,
        "#1542F……唔唔唔………………\x02",
    )

    CloseMessageWindow()
    OP_62(0x0, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #133
        0x104,
        "#1547F……哦哦！\x02",
    )

    Jump("loc_5D8D")

    label("loc_5BA9")


    ChrTalk(    #134
        0x10B,
        (
            "#216F哇哇…………！？\x02\x03",

            "#215F……………………………………\x02\x03",

            "#413F感觉好像很糟……\x02",
        )
    )

    Jump("loc_5D8D")

    label("loc_5C15")


    ChrTalk(    #135
        0x10A,
        (
            "#1317F唔………………！\x02\x03",

            "#817F尽是些没见过的事……  \x02",
        )
    )

    Jump("loc_5D8D")

    label("loc_5C5E")


    ChrTalk(    #136
        0x108,
        (
            "#074F………呼………………\x02\x03",

            "#075F这种书卖不出去吧……\x02",
        )
    )

    Jump("loc_5D8D")

    label("loc_5CA8")

    OP_62(0x0, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #137
        0x10E,
        "#176F（放回里面吧……）\x02",
    )

    Jump("loc_5D8D")

    label("loc_5CEA")


    ChrTalk(    #138
        0x10D,
        "#272F……无可救药的男人…………\x02",
    )

    Jump("loc_5D8D")

    label("loc_5D18")


    ChrTalk(    #139
        0x10C,
        "#115F………………是吗……\x02",
    )

    Jump("loc_5D8D")

    label("loc_5D40")


    ChrTalk(    #140
        0x110,
        (
            "#264F呼……………………\x02\x03",

            "#261F嘻嘻，\x01",
            "看来他也很努力呢。\x02",
        )
    )

    Jump("loc_5D8D")

    label("loc_5D8D")

    CloseMessageWindow()

    label("loc_5D8E")

    Return()

    # Function_16_5811 end

    def Function_17_5D8F(): pass

    label("Function_17_5D8F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DE0")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #141
        "\x07\x05在书架上发现《红耀石》。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2670)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_5FD9")

    label("loc_5DE0")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #142
        "\x07\x05书架上有《红耀石》。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读第１卷】\x01",      # 0
            "【阅读第２卷】\x01",      # 1
            "【阅读第３卷】\x01",      # 2
            "【阅读第４卷】\x01",      # 3
            "【阅读第５卷】\x01",      # 4
            "【阅读第６卷】\x01",      # 5
            "【阅读第７卷】\x01",      # 6
            "【阅读第８卷】\x01",      # 7
            "【阅读第９卷】\x01",      # 8
            "【阅读第10卷】\x01",      # 9
            "【阅读最终卷】\x01",      # 10
            "【放弃】\x01",            # 11
        )
    )

    Jump("loc_5EDE")

    label("loc_5EDE")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F16")
    OP_B8(0xE6, 0x0)

    label("loc_5F16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F28")
    OP_B8(0xE7, 0x0)

    label("loc_5F28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F3A")
    OP_B8(0xE8, 0x0)

    label("loc_5F3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F4C")
    OP_B8(0xE9, 0x0)

    label("loc_5F4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F5E")
    OP_B8(0xEA, 0x0)

    label("loc_5F5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F70")
    OP_B8(0xEB, 0x0)

    label("loc_5F70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F82")
    OP_B8(0xEC, 0x0)

    label("loc_5F82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F94")
    OP_B8(0xED, 0x0)

    label("loc_5F94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FA6")
    OP_B8(0xEE, 0x0)

    label("loc_5FA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FB8")
    OP_B8(0xEF, 0x0)

    label("loc_5FB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FCA")
    OP_B8(0xF0, 0x0)

    label("loc_5FCA")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)

    label("loc_5FD9")

    Return()

    # Function_17_5D8F end

    def Function_18_5FDA(): pass

    label("Function_18_5FDA")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_602F")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #143
        "\x07\x05在书架上发现《赌博师杰克》。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2673)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_628F")

    label("loc_602F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #144
        "\x07\x05书架上有《赌博师杰克》。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读第１卷】\x01",      # 0
            "【阅读第２卷】\x01",      # 1
            "【阅读第３卷】\x01",      # 2
            "【阅读第４卷】\x01",      # 3
            "【阅读第５卷】\x01",      # 4
            "【阅读第６卷】\x01",      # 5
            "【阅读第７卷】\x01",      # 6
            "【阅读第８卷】\x01",      # 7
            "【阅读第９卷】\x01",      # 8
            "【阅读第10卷】\x01",      # 9
            "【阅读第11卷】\x01",      # 10
            "【阅读第12卷】\x01",      # 11
            "【阅读第13卷】\x01",      # 12
            "【阅读最终卷】\x01",      # 13
            "【放弃】\x01",            # 14
        )
    )

    Jump("loc_615E")

    label("loc_615E")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6196")
    OP_B8(0xFD, 0x0)

    label("loc_6196")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61A8")
    OP_B8(0xFE, 0x0)

    label("loc_61A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61BA")
    OP_B8(0xFF, 0x0)

    label("loc_61BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61CC")
    OP_B8(0x100, 0x0)

    label("loc_61CC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61DE")
    OP_B8(0x101, 0x0)

    label("loc_61DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_61F0")
    OP_B8(0x102, 0x0)

    label("loc_61F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6202")
    OP_B8(0x103, 0x0)

    label("loc_6202")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6214")
    OP_B8(0x104, 0x0)

    label("loc_6214")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6226")
    OP_B8(0x105, 0x0)

    label("loc_6226")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6238")
    OP_B8(0x106, 0x0)

    label("loc_6238")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_624A")
    OP_B8(0x107, 0x0)

    label("loc_624A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_625C")
    OP_B8(0x108, 0x0)

    label("loc_625C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_626E")
    OP_B8(0x109, 0x0)

    label("loc_626E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6280")
    OP_B8(0x10A, 0x0)

    label("loc_6280")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)

    label("loc_628F")

    Return()

    # Function_18_5FDA end

    def Function_19_6290(): pass

    label("Function_19_6290")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4CE, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62E3")
    OP_22(0x17, 0x0, 0x64)
    OP_82(0x0, 0x2)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #145
        "\x07\x05在书架上发现《人偶骑士》。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x2674)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_670D")

    label("loc_62E3")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #146
        "\x07\x05书架上有《人偶骑士》。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【１～１１卷】\x01",        # 0
            "【１２～最终卷】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6360"),
        (1, "loc_652F"),
        (SWITCH_DEFAULT, "loc_66FE"),
    )


    label("loc_6360")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        1,
        (
            "【阅读第１卷】\x01",      # 0
            "【阅读第２卷】\x01",      # 1
            "【阅读第３卷】\x01",      # 2
            "【阅读第４卷】\x01",      # 3
            "【阅读第５卷】\x01",      # 4
            "【阅读第６卷】\x01",      # 5
            "【阅读第７卷】\x01",      # 6
            "【阅读第８卷】\x01",      # 7
            "【阅读第９卷】\x01",      # 8
            "【阅读第10卷】\x01",      # 9
            "【阅读第11卷】\x01",      # 10
            "【放弃】\x01",            # 11
        )
    )

    Jump("loc_6440")

    label("loc_6440")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6478")
    OP_B8(0x10B, 0x0)

    label("loc_6478")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_648A")
    OP_B8(0x10C, 0x0)

    label("loc_648A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_649C")
    OP_B8(0x10D, 0x0)

    label("loc_649C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64AE")
    OP_B8(0x10E, 0x0)

    label("loc_64AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64C0")
    OP_B8(0x10F, 0x0)

    label("loc_64C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64D2")
    OP_B8(0x110, 0x0)

    label("loc_64D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64E4")
    OP_B8(0x111, 0x0)

    label("loc_64E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64F6")
    OP_B8(0x112, 0x0)

    label("loc_64F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6508")
    OP_B8(0x113, 0x0)

    label("loc_6508")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_651A")
    OP_B8(0x114, 0x0)

    label("loc_651A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_652C")
    OP_B8(0x115, 0x0)

    label("loc_652C")

    Jump("loc_66FE")

    label("loc_652F")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        10,
        10,
        1,
        (
            "【阅读第12卷】\x01",      # 0
            "【阅读第13卷】\x01",      # 1
            "【阅读第14卷】\x01",      # 2
            "【阅读第15卷】\x01",      # 3
            "【阅读第16卷】\x01",      # 4
            "【阅读第17卷】\x01",      # 5
            "【阅读第18卷】\x01",      # 6
            "【阅读第19卷】\x01",      # 7
            "【阅读第20卷】\x01",      # 8
            "【阅读第21卷】\x01",      # 9
            "【阅读最终卷】\x01",      # 10
            "【放弃】\x01",            # 11
        )
    )

    Jump("loc_660F")

    label("loc_660F")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6647")
    OP_B8(0x116, 0x0)

    label("loc_6647")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6659")
    OP_B8(0x117, 0x0)

    label("loc_6659")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_666B")
    OP_B8(0x118, 0x0)

    label("loc_666B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_667D")
    OP_B8(0x119, 0x0)

    label("loc_667D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_668F")
    OP_B8(0x11A, 0x0)

    label("loc_668F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66A1")
    OP_B8(0x11B, 0x0)

    label("loc_66A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66B3")
    OP_B8(0x11C, 0x0)

    label("loc_66B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66C5")
    OP_B8(0x11D, 0x0)

    label("loc_66C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66D7")
    OP_B8(0x11E, 0x0)

    label("loc_66D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66E9")
    OP_B8(0x11F, 0x0)

    label("loc_66E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66FB")
    OP_B8(0x120, 0x0)

    label("loc_66FB")

    Jump("loc_66FE")

    label("loc_66FE")

    FadeToBright(300, 0)
    OP_5F(0x0)
    TalkEnd(0xFF)

    label("loc_670D")

    Return()

    # Function_19_6290 end

    def Function_20_670E(): pass

    label("Function_20_670E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #147
        (
            "\x07\x05《无明祭祀书》、《威加那的眷属》、\x01",
            "《宇宙图鉴》、《苍之断章》、\x01",
            "《边走边吃王国纪行》…………\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #148
        "\x07\x05珍贵的书籍当中混杂着最近出版的书。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_20_670E end

    def Function_21_67B8(): pass

    label("Function_21_67B8")

    SetMapFlags(0x80)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(500, 0, -1)

    def lambda_67D6():
        OP_90(0x0, 0x0, 0x0, 0x3E8, 0x514, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_67D6)
    OP_0D()
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_21_67B8 end

    SaveToFile()

Try(main)
